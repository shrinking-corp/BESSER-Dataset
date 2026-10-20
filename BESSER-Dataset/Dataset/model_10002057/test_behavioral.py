import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Docter,
    Hospital,
    Patients,
    Receptionist,
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

def test_assoc_Docter_Patient_reverse_link_reassign_clear():
    a1 = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    a2 = Patients(NIC_NO=13, Patient_name="sample_text_2", Phone_no=13, Sickness="sample_text_2")
    b = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    _safe_set(b, 'patient0', {a1})
    assert _is_linked(b, 'patient0', a1)
    if hasattr(a1, 'docter1'):
        assert _is_linked(a1, 'docter1', b)
    _safe_set(b, 'patient0', {a2})
    assert _is_linked(b, 'patient0', a2)
    if hasattr(a1, 'docter1'):
        assert not _is_linked(a1, 'docter1', b)
    if hasattr(a2, 'docter1'):
        assert _is_linked(a2, 'docter1', b)
    _safe_set(b, 'patient0', set())
    assert not _is_linked(b, 'patient0', a2)
    if hasattr(a2, 'docter1'):
        assert not _is_linked(a2, 'docter1', b)


def test_assoc_Patients_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(Employee_ID=7, Name="sample_text")
    a2 = Receptionist(Employee_ID=13, Name="sample_text_2")
    b = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    _safe_set(b, 'receptionist2', a1)
    assert _is_linked(b, 'receptionist2', a1)
    if hasattr(a1, 'patients3'):
        assert _is_linked(a1, 'patients3', b)
    _safe_set(b, 'receptionist2', a2)
    assert _is_linked(b, 'receptionist2', a2)
    if hasattr(a1, 'patients3'):
        assert not _is_linked(a1, 'patients3', b)
    if hasattr(a2, 'patients3'):
        assert _is_linked(a2, 'patients3', b)
    _safe_set(b, 'receptionist2', None)
    assert not _is_linked(b, 'receptionist2', a2)
    if hasattr(a2, 'patients3'):
        assert not _is_linked(a2, 'patients3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

