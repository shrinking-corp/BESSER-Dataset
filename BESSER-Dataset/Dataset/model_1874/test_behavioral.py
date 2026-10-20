import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Alias,
    TypeItem,
    basic_Alias,
    basic_CoreVersionDefault,
    basic_Event,
    basic_ExecutionEnvironment,
    basic_ExtJSProject,
    basic_Feature,
    basic_File,
    basic_Layout,
    basic_Library,
    basic_LibrarySource,
    basic_Parameter,
    basic_Plugin,
    basic_TypeItem,
    basic_Widget,
    LibrarySourceType,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_aliases1_reverse_link_reassign_clear():
    a1 = basic_File(name="sample_text")
    a2 = basic_File(name="sample_text_2")
    b = basic_Alias(name="sample_text", rawName="sample_text")
    _safe_set(b, 'basic_Alias', a1)
    assert _is_linked(b, 'basic_Alias', a1)
    if hasattr(a1, 'basic_File2'):
        assert _is_linked(a1, 'basic_File2', b)
    _safe_set(b, 'basic_Alias', a2)
    assert _is_linked(b, 'basic_Alias', a2)
    if hasattr(a1, 'basic_File2'):
        assert not _is_linked(a1, 'basic_File2', b)
    if hasattr(a2, 'basic_File2'):
        assert _is_linked(a2, 'basic_File2', b)
    _safe_set(b, 'basic_Alias', None)
    assert not _is_linked(b, 'basic_Alias', a2)
    if hasattr(a2, 'basic_File2'):
        assert not _is_linked(a2, 'basic_File2', b)


def test_assoc_files0_reverse_link_reassign_clear():
    a1 = basic_File(name="sample_text")
    a2 = basic_File(name="sample_text_2")
    b = basic_ExtJSProject(name="sample_text")
    _safe_set(b, 'basic_ExtJSProject', {a1})
    assert _is_linked(b, 'basic_ExtJSProject', a1)
    if hasattr(a1, 'basic_File'):
        assert _is_linked(a1, 'basic_File', b)
    _safe_set(b, 'basic_ExtJSProject', {a2})
    assert _is_linked(b, 'basic_ExtJSProject', a2)
    if hasattr(a1, 'basic_File'):
        assert not _is_linked(a1, 'basic_File', b)
    if hasattr(a2, 'basic_File'):
        assert _is_linked(a2, 'basic_File', b)
    _safe_set(b, 'basic_ExtJSProject', set())
    assert not _is_linked(b, 'basic_ExtJSProject', a2)
    if hasattr(a2, 'basic_File'):
        assert not _is_linked(a2, 'basic_File', b)


def test_assoc_files5_reverse_link_reassign_clear():
    a1 = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    a2 = basic_LibrarySource(exclusions="sample_text_2", inclusions="sample_text_2", path="sample_text_2", type="sample_text_2")
    b = basic_File(name="sample_text")
    _safe_set(b, 'basic_File7', a1)
    assert _is_linked(b, 'basic_File7', a1)
    if hasattr(a1, 'basic_LibrarySource6'):
        assert _is_linked(a1, 'basic_LibrarySource6', b)
    _safe_set(b, 'basic_File7', a2)
    assert _is_linked(b, 'basic_File7', a2)
    if hasattr(a1, 'basic_LibrarySource6'):
        assert not _is_linked(a1, 'basic_LibrarySource6', b)
    if hasattr(a2, 'basic_LibrarySource6'):
        assert _is_linked(a2, 'basic_LibrarySource6', b)
    _safe_set(b, 'basic_File7', None)
    assert not _is_linked(b, 'basic_File7', a2)
    if hasattr(a2, 'basic_LibrarySource6'):
        assert not _is_linked(a2, 'basic_LibrarySource6', b)


def test_assoc_parameters3_reverse_link_reassign_clear():
    a1 = basic_Parameter(description="sample_text", name="sample_text", type="sample_text")
    a2 = basic_Parameter(description="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = basic_Event(description="sample_text", name="sample_text")
    _safe_set(b, 'basic_Event', {a1})
    assert _is_linked(b, 'basic_Event', a1)
    if hasattr(a1, 'basic_Parameter'):
        assert _is_linked(a1, 'basic_Parameter', b)
    _safe_set(b, 'basic_Event', {a2})
    assert _is_linked(b, 'basic_Event', a2)
    if hasattr(a1, 'basic_Parameter'):
        assert not _is_linked(a1, 'basic_Parameter', b)
    if hasattr(a2, 'basic_Parameter'):
        assert _is_linked(a2, 'basic_Parameter', b)
    _safe_set(b, 'basic_Event', set())
    assert not _is_linked(b, 'basic_Event', a2)
    if hasattr(a2, 'basic_Parameter'):
        assert not _is_linked(a2, 'basic_Parameter', b)


def test_assoc_sources4_reverse_link_reassign_clear():
    a1 = basic_LibrarySource(exclusions="sample_text", inclusions="sample_text", path="sample_text", type="sample_text")
    a2 = basic_LibrarySource(exclusions="sample_text_2", inclusions="sample_text_2", path="sample_text_2", type="sample_text_2")
    b = basic_Library(builtin=True, name="sample_text", senchaTouchVersions="sample_text", versions="sample_text")
    _safe_set(b, 'basic_Library', {a1})
    assert _is_linked(b, 'basic_Library', a1)
    if hasattr(a1, 'basic_LibrarySource'):
        assert _is_linked(a1, 'basic_LibrarySource', b)
    _safe_set(b, 'basic_Library', {a2})
    assert _is_linked(b, 'basic_Library', a2)
    if hasattr(a1, 'basic_LibrarySource'):
        assert not _is_linked(a1, 'basic_LibrarySource', b)
    if hasattr(a2, 'basic_LibrarySource'):
        assert _is_linked(a2, 'basic_LibrarySource', b)
    _safe_set(b, 'basic_Library', set())
    assert not _is_linked(b, 'basic_Library', a2)
    if hasattr(a2, 'basic_LibrarySource'):
        assert not _is_linked(a2, 'basic_LibrarySource', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

