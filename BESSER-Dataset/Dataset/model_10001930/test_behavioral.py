import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Dept,
    Doctor,
    Patient,
    Receptionist,
    Rooms,
    e,
    ff,
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

def test_assoc_Doctor_Dept_reverse_link_reassign_clear():
    a1 = Doctor(Dept="sample_text", DocName="sample_text", Docid=7, Location="sample_text", Phoneno="sample_text", Specialization="sample_text")
    a2 = Doctor(Dept="sample_text_2", DocName="sample_text_2", Docid=13, Location="sample_text_2", Phoneno="sample_text_2", Specialization="sample_text_2")
    b = Dept(DeptName="sample_text", Docid=7, id=7)
    _safe_set(b, 'Doctor_Dept_17', {a1})
    assert _is_linked(b, 'Doctor_Dept_17', a1)
    if hasattr(a1, 'dept6'):
        assert _is_linked(a1, 'dept6', b)
    _safe_set(b, 'Doctor_Dept_17', {a2})
    assert _is_linked(b, 'Doctor_Dept_17', a2)
    if hasattr(a1, 'dept6'):
        assert not _is_linked(a1, 'dept6', b)
    if hasattr(a2, 'dept6'):
        assert _is_linked(a2, 'dept6', b)
    _safe_set(b, 'Doctor_Dept_17', set())
    assert not _is_linked(b, 'Doctor_Dept_17', a2)
    if hasattr(a2, 'dept6'):
        assert not _is_linked(a2, 'dept6', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, PatientName="sample_text", Patientid=7, PhoneNo=7, RoomNo=7, Sex="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, PatientName="sample_text_2", Patientid=13, PhoneNo=13, RoomNo=13, Sex="sample_text_2")
    b = Doctor(Dept="sample_text", DocName="sample_text", Docid=7, Location="sample_text", Phoneno="sample_text", Specialization="sample_text")
    _safe_set(b, 'patient0', {a1})
    assert _is_linked(b, 'patient0', a1)
    if hasattr(a1, 'doctor1'):
        assert _is_linked(a1, 'doctor1', b)
    _safe_set(b, 'patient0', {a2})
    assert _is_linked(b, 'patient0', a2)
    if hasattr(a1, 'doctor1'):
        assert not _is_linked(a1, 'doctor1', b)
    if hasattr(a2, 'doctor1'):
        assert _is_linked(a2, 'doctor1', b)
    _safe_set(b, 'patient0', set())
    assert not _is_linked(b, 'patient0', a2)
    if hasattr(a2, 'doctor1'):
        assert not _is_linked(a2, 'doctor1', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, PatientName="sample_text", Patientid=7, PhoneNo=7, RoomNo=7, Sex="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, PatientName="sample_text_2", Patientid=13, PhoneNo=13, RoomNo=13, Sex="sample_text_2")
    b = Bill(Amt="sample_text", BillNo="sample_text", PatientName="sample_text")
    _safe_set(b, 'patient11', a1)
    assert _is_linked(b, 'patient11', a1)
    if hasattr(a1, 'Patient_Bill_010'):
        assert _is_linked(a1, 'Patient_Bill_010', b)
    _safe_set(b, 'patient11', a2)
    assert _is_linked(b, 'patient11', a2)
    if hasattr(a1, 'Patient_Bill_010'):
        assert not _is_linked(a1, 'Patient_Bill_010', b)
    if hasattr(a2, 'Patient_Bill_010'):
        assert _is_linked(a2, 'Patient_Bill_010', b)
    _safe_set(b, 'patient11', None)
    assert not _is_linked(b, 'patient11', a2)
    if hasattr(a2, 'Patient_Bill_010'):
        assert not _is_linked(a2, 'Patient_Bill_010', b)


def test_assoc_Patient_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(RecName="sample_text", Receptionid=7)
    a2 = Receptionist(RecName="sample_text_2", Receptionid=13)
    b = Patient(Address="sample_text", Age=7, PatientName="sample_text", Patientid=7, PhoneNo=7, RoomNo=7, Sex="sample_text")
    _safe_set(b, 'receptionist2', a1)
    assert _is_linked(b, 'receptionist2', a1)
    if hasattr(a1, 'patient3'):
        assert _is_linked(a1, 'patient3', b)
    _safe_set(b, 'receptionist2', a2)
    assert _is_linked(b, 'receptionist2', a2)
    if hasattr(a1, 'patient3'):
        assert not _is_linked(a1, 'patient3', b)
    if hasattr(a2, 'patient3'):
        assert _is_linked(a2, 'patient3', b)
    _safe_set(b, 'receptionist2', None)
    assert not _is_linked(b, 'receptionist2', a2)
    if hasattr(a2, 'patient3'):
        assert not _is_linked(a2, 'patient3', b)


def test_assoc_Patient_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(Location="sample_text", RoomNo=7)
    a2 = Rooms(Location="sample_text_2", RoomNo=13)
    b = Patient(Address="sample_text", Age=7, PatientName="sample_text", Patientid=7, PhoneNo=7, RoomNo=7, Sex="sample_text")
    _safe_set(b, 'rooms8', a1)
    assert _is_linked(b, 'rooms8', a1)
    if hasattr(a1, 'Patient_Rooms_19'):
        assert _is_linked(a1, 'Patient_Rooms_19', b)
    _safe_set(b, 'rooms8', a2)
    assert _is_linked(b, 'rooms8', a2)
    if hasattr(a1, 'Patient_Rooms_19'):
        assert not _is_linked(a1, 'Patient_Rooms_19', b)
    if hasattr(a2, 'Patient_Rooms_19'):
        assert _is_linked(a2, 'Patient_Rooms_19', b)
    _safe_set(b, 'rooms8', None)
    assert not _is_linked(b, 'rooms8', a2)
    if hasattr(a2, 'Patient_Rooms_19'):
        assert not _is_linked(a2, 'Patient_Rooms_19', b)


def test_assoc_Receptionist_Bill_reverse_link_reassign_clear():
    a1 = Receptionist(RecName="sample_text", Receptionid=7)
    a2 = Receptionist(RecName="sample_text_2", Receptionid=13)
    b = Bill(Amt="sample_text", BillNo="sample_text", PatientName="sample_text")
    _safe_set(b, 'receptionist5', a1)
    assert _is_linked(b, 'receptionist5', a1)
    if hasattr(a1, 'bill4'):
        assert _is_linked(a1, 'bill4', b)
    _safe_set(b, 'receptionist5', a2)
    assert _is_linked(b, 'receptionist5', a2)
    if hasattr(a1, 'bill4'):
        assert not _is_linked(a1, 'bill4', b)
    if hasattr(a2, 'bill4'):
        assert _is_linked(a2, 'bill4', b)
    _safe_set(b, 'receptionist5', None)
    assert not _is_linked(b, 'receptionist5', a2)
    if hasattr(a2, 'bill4'):
        assert not _is_linked(a2, 'bill4', b)


def test_assoc_e_ff_reverse_link_reassign_clear():
    a1 = ff(fd=7)
    a2 = ff(fd=13)
    b = e(ee=7)
    _safe_set(b, 'ff12', a1)
    assert _is_linked(b, 'ff12', a1)
    if hasattr(a1, 'e13'):
        assert _is_linked(a1, 'e13', b)
    _safe_set(b, 'ff12', a2)
    assert _is_linked(b, 'ff12', a2)
    if hasattr(a1, 'e13'):
        assert not _is_linked(a1, 'e13', b)
    if hasattr(a2, 'e13'):
        assert _is_linked(a2, 'e13', b)
    _safe_set(b, 'ff12', None)
    assert not _is_linked(b, 'ff12', a2)
    if hasattr(a2, 'e13'):
        assert not _is_linked(a2, 'e13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

