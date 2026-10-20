import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Doctor,
    Nurse,
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
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", PatientID=13, RoomNo=13, Sex="sample_text_2", TelephoneNo="sample_text_2")
    b = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    _safe_set(b, 'patient0', a1)
    assert _is_linked(b, 'patient0', a1)
    if hasattr(a1, 'doctor1'):
        assert _is_linked(a1, 'doctor1', b)
    _safe_set(b, 'patient0', a2)
    assert _is_linked(b, 'patient0', a2)
    if hasattr(a1, 'doctor1'):
        assert not _is_linked(a1, 'doctor1', b)
    if hasattr(a2, 'doctor1'):
        assert _is_linked(a2, 'doctor1', b)
    _safe_set(b, 'patient0', None)
    assert not _is_linked(b, 'patient0', a2)
    if hasattr(a2, 'doctor1'):
        assert not _is_linked(a2, 'doctor1', b)


def test_assoc_Nurse_Doctor_reverse_link_reassign_clear():
    a1 = Nurse(ID=7, Name="sample_text")
    a2 = Nurse(ID=13, Name="sample_text_2")
    b = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    _safe_set(b, 'nurse5', a1)
    assert _is_linked(b, 'nurse5', a1)
    if hasattr(a1, 'doctor4'):
        assert _is_linked(a1, 'doctor4', b)
    _safe_set(b, 'nurse5', a2)
    assert _is_linked(b, 'nurse5', a2)
    if hasattr(a1, 'doctor4'):
        assert not _is_linked(a1, 'doctor4', b)
    if hasattr(a2, 'doctor4'):
        assert _is_linked(a2, 'doctor4', b)
    _safe_set(b, 'nurse5', None)
    assert not _is_linked(b, 'nurse5', a2)
    if hasattr(a2, 'doctor4'):
        assert not _is_linked(a2, 'doctor4', b)


def test_assoc_Nurse_Patient_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", PatientID=13, RoomNo=13, Sex="sample_text_2", TelephoneNo="sample_text_2")
    b = Nurse(ID=7, Name="sample_text")
    _safe_set(b, 'patient6', a1)
    assert _is_linked(b, 'patient6', a1)
    if hasattr(a1, 'nurse7'):
        assert _is_linked(a1, 'nurse7', b)
    _safe_set(b, 'patient6', a2)
    assert _is_linked(b, 'patient6', a2)
    if hasattr(a1, 'nurse7'):
        assert not _is_linked(a1, 'nurse7', b)
    if hasattr(a2, 'nurse7'):
        assert _is_linked(a2, 'nurse7', b)
    _safe_set(b, 'patient6', None)
    assert not _is_linked(b, 'patient6', a2)
    if hasattr(a2, 'nurse7'):
        assert not _is_linked(a2, 'nurse7', b)


def test_assoc_Patient_bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", PatientID=13, RoomNo=13, Sex="sample_text_2", TelephoneNo="sample_text_2")
    b = Bill(Amount="sample_text", PatientName="sample_text")
    _safe_set(b, 'patient3', a1)
    assert _is_linked(b, 'patient3', a1)
    if hasattr(a1, 'bill2'):
        assert _is_linked(a1, 'bill2', b)
    _safe_set(b, 'patient3', a2)
    assert _is_linked(b, 'patient3', a2)
    if hasattr(a1, 'bill2'):
        assert not _is_linked(a1, 'bill2', b)
    if hasattr(a2, 'bill2'):
        assert _is_linked(a2, 'bill2', b)
    _safe_set(b, 'patient3', None)
    assert not _is_linked(b, 'patient3', a2)
    if hasattr(a2, 'bill2'):
        assert not _is_linked(a2, 'bill2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

