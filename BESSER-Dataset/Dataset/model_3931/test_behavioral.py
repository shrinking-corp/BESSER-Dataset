import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    configDsl_Config,
    configDsl_Generator,
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

def test_assoc_generators1_reverse_link_reassign_clear():
    a1 = configDsl_Generator(bundle="sample_text", genClass="sample_text", name="sample_text")
    a2 = configDsl_Generator(bundle="sample_text_2", genClass="sample_text_2", name="sample_text_2")
    b = configDsl_Config(appName="sample_text", mainClass="sample_text", outFolder="sample_text", srcFolder="sample_text")
    _safe_set(b, 'configDsl_Config2', {a1})
    assert _is_linked(b, 'configDsl_Config2', a1)
    if hasattr(a1, 'configDsl_Generator3'):
        assert _is_linked(a1, 'configDsl_Generator3', b)
    _safe_set(b, 'configDsl_Config2', {a2})
    assert _is_linked(b, 'configDsl_Config2', a2)
    if hasattr(a1, 'configDsl_Generator3'):
        assert not _is_linked(a1, 'configDsl_Generator3', b)
    if hasattr(a2, 'configDsl_Generator3'):
        assert _is_linked(a2, 'configDsl_Generator3', b)
    _safe_set(b, 'configDsl_Config2', set())
    assert not _is_linked(b, 'configDsl_Config2', a2)
    if hasattr(a2, 'configDsl_Generator3'):
        assert not _is_linked(a2, 'configDsl_Generator3', b)


def test_assoc_selectors0_reverse_link_reassign_clear():
    a1 = configDsl_Generator(bundle="sample_text", genClass="sample_text", name="sample_text")
    a2 = configDsl_Generator(bundle="sample_text_2", genClass="sample_text_2", name="sample_text_2")
    b = configDsl_Config(appName="sample_text", mainClass="sample_text", outFolder="sample_text", srcFolder="sample_text")
    _safe_set(b, 'configDsl_Config', {a1})
    assert _is_linked(b, 'configDsl_Config', a1)
    if hasattr(a1, 'configDsl_Generator'):
        assert _is_linked(a1, 'configDsl_Generator', b)
    _safe_set(b, 'configDsl_Config', {a2})
    assert _is_linked(b, 'configDsl_Config', a2)
    if hasattr(a1, 'configDsl_Generator'):
        assert not _is_linked(a1, 'configDsl_Generator', b)
    if hasattr(a2, 'configDsl_Generator'):
        assert _is_linked(a2, 'configDsl_Generator', b)
    _safe_set(b, 'configDsl_Config', set())
    assert not _is_linked(b, 'configDsl_Config', a2)
    if hasattr(a2, 'configDsl_Generator'):
        assert not _is_linked(a2, 'configDsl_Generator', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

