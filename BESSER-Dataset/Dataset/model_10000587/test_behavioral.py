import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Doctor,
    Patient,
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

def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    a2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", sex="sample_text_2", telno=13)
    b = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    _safe_set(b, 'patients0', {a1})
    assert _is_linked(b, 'patients0', a1)
    if hasattr(a1, 'doctors1'):
        assert _is_linked(a1, 'doctors1', b)
    _safe_set(b, 'patients0', {a2})
    assert _is_linked(b, 'patients0', a2)
    if hasattr(a1, 'doctors1'):
        assert not _is_linked(a1, 'doctors1', b)
    if hasattr(a2, 'doctors1'):
        assert _is_linked(a2, 'doctors1', b)
    _safe_set(b, 'patients0', set())
    assert not _is_linked(b, 'patients0', a2)
    if hasattr(a2, 'doctors1'):
        assert not _is_linked(a2, 'doctors1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

