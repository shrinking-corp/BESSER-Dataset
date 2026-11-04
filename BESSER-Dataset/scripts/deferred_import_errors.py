"""pytest plugin: a name python_code lacks fails only the tests that use it.

Load it with: python -m pytest test_super_suite.py -p deferred_import_errors
(with this file's folder on PYTHONPATH).

Without it, `from python_code import A, B` at the top of a suite fails while
pytest collects the file, so one missing class means no test runs. With it,
the import succeeds, A or B may be a placeholder, and:
- a test whose body names a missing element fails before it starts;
- a test reaching one through a strategy fails when the strategy touches it.

When python_code provides every name, nothing changes. Code that doesn't
import at all is left alone and still fails collection. One pytest process
per model, as python_code is cached in sys.modules.

Why: docs/2026-10-28-hypothesis-seed-and-comparable-test-runs.md, section 5.
"""
import dis
import importlib
import sys
import types

import pytest

_tests_running = False
_missing_names = set()


class MissingElement(Exception):
    pass


class _Missing:
    def __init__(self, name):
        object.__setattr__(self, "_name", name)

    def _fail(self):
        name = object.__getattribute__(self, "_name")
        raise MissingElement(f"python_code does not provide {name}")

    def __getattribute__(self, attr):
        # While the file is collected, things inspect the placeholder:
        # st.builds(...) runs isinstance() on it for a cache key, and other
        # installed pytest plugins look at every name in the module. So stay
        # harmless until tests run. After that nothing is answered, or
        # inspect.isabstract() would pass on it.
        if not _tests_running:
            if attr == "__class__":
                return _Missing
            raise AttributeError(attr)
        object.__getattribute__(self, "_fail")()

    def __call__(self, *args, **kwargs):
        object.__getattribute__(self, "_fail")()

    def __repr__(self):
        return f"<missing {object.__getattribute__(self, '_name')}>"


def _placeholder_for(name):
    if name.startswith("__"):
        raise AttributeError(name)
    _missing_names.add(name)
    return _Missing(name)


def _globals_read(code):
    """Global names a test's code reads, including nested lambdas etc."""
    names = {i.argval for i in dis.get_instructions(code)
             if i.opname in ("LOAD_GLOBAL", "LOAD_NAME")}
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            names |= _globals_read(const)
    return names


def pytest_collectstart(collector):
    # Runs just before pytest imports the test file.
    if not isinstance(collector, pytest.Module):
        return
    folder = str(collector.path.parent)
    if folder not in sys.path:
        sys.path.insert(0, folder)
    try:
        module = importlib.import_module("python_code")
    except (Exception, SystemExit):
        return  # the suite's own import reports this as a collection error
    module.__getattr__ = _placeholder_for


@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    # pytest would inspect an imported `test...` name as a test function.
    if type(obj) is _Missing:
        return []
    return None


def pytest_collection_finish(session):
    global _tests_running
    _tests_running = True


@pytest.hookimpl(tryfirst=True)
def pytest_pyfunc_call(pyfuncitem):
    # `assert X is not None` runs no code on the placeholder, so it can't raise
    # by itself. Fail any test whose body names a missing element.
    if not _missing_names:
        return None
    func = pyfuncitem.obj
    func = getattr(getattr(func, "hypothesis", None), "inner_test", func)
    code = getattr(func, "__code__", None)
    used = sorted(_globals_read(code) & _missing_names) if code else []
    if used:
        raise MissingElement(f"python_code does not provide {', '.join(used)}")
    return None
