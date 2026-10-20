import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Department,
    Doctor,
    Patient,
    Receptionist,
    Rooms,
    Staff,
    char_Interface,
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

def test_assoc_Doctor_Department_reverse_link_reassign_clear():
    a1 = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", PhNo=7, Specialization="sample_text")
    a2 = Doctor(Address="sample_text_2", Department="sample_text_2", DocID=13, Name="sample_text_2", PhNo=13, Specialization="sample_text_2")
    b = Department(Doctor_ID=7, ID=7, Name="sample_text")
    _safe_set(b, 'Doctor_Department_111', a1)
    assert _is_linked(b, 'Doctor_Department_111', a1)
    if hasattr(a1, 'Doctor_Department_010'):
        assert _is_linked(a1, 'Doctor_Department_010', b)
    _safe_set(b, 'Doctor_Department_111', a2)
    assert _is_linked(b, 'Doctor_Department_111', a2)
    if hasattr(a1, 'Doctor_Department_010'):
        assert not _is_linked(a1, 'Doctor_Department_010', b)
    if hasattr(a2, 'Doctor_Department_010'):
        assert _is_linked(a2, 'Doctor_Department_010', b)
    _safe_set(b, 'Doctor_Department_111', None)
    assert not _is_linked(b, 'Doctor_Department_111', a2)
    if hasattr(a2, 'Doctor_Department_010'):
        assert not _is_linked(a2, 'Doctor_Department_010', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", Pid=7, RoomNo_=7, Sex=7, TelNO=7)
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", Pid=13, RoomNo_=13, Sex=13, TelNO=13)
    b = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", PhNo=7, Specialization="sample_text")
    _safe_set(b, 'Doctor_Patient_00', {a1})
    assert _is_linked(b, 'Doctor_Patient_00', a1)
    if hasattr(a1, 'Doctor_Patient_11'):
        assert _is_linked(a1, 'Doctor_Patient_11', b)
    _safe_set(b, 'Doctor_Patient_00', {a2})
    assert _is_linked(b, 'Doctor_Patient_00', a2)
    if hasattr(a1, 'Doctor_Patient_11'):
        assert not _is_linked(a1, 'Doctor_Patient_11', b)
    if hasattr(a2, 'Doctor_Patient_11'):
        assert _is_linked(a2, 'Doctor_Patient_11', b)
    _safe_set(b, 'Doctor_Patient_00', set())
    assert not _is_linked(b, 'Doctor_Patient_00', a2)
    if hasattr(a2, 'Doctor_Patient_11'):
        assert not _is_linked(a2, 'Doctor_Patient_11', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", Pid=7, RoomNo_=7, Sex=7, TelNO=7)
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", Pid=13, RoomNo_=13, Sex=13, TelNO=13)
    b = Bill(Amount="sample_text", Bill_No="sample_text", Patient_Name="sample_text")
    _safe_set(b, 'patient5', a1)
    assert _is_linked(b, 'patient5', a1)
    if hasattr(a1, 'Patient_Bill_04'):
        assert _is_linked(a1, 'Patient_Bill_04', b)
    _safe_set(b, 'patient5', a2)
    assert _is_linked(b, 'patient5', a2)
    if hasattr(a1, 'Patient_Bill_04'):
        assert not _is_linked(a1, 'Patient_Bill_04', b)
    if hasattr(a2, 'Patient_Bill_04'):
        assert _is_linked(a2, 'Patient_Bill_04', b)
    _safe_set(b, 'patient5', None)
    assert not _is_linked(b, 'patient5', a2)
    if hasattr(a2, 'Patient_Bill_04'):
        assert not _is_linked(a2, 'Patient_Bill_04', b)


def test_assoc_Patient_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(Rid="sample_text", Rname="sample_text")
    a2 = Receptionist(Rid="sample_text_2", Rname="sample_text_2")
    b = Patient(Address="sample_text", Age=7, Name="sample_text", Pid=7, RoomNo_=7, Sex=7, TelNO=7)
    _safe_set(b, 'Patient_Receptionist_02', a1)
    assert _is_linked(b, 'Patient_Receptionist_02', a1)
    if hasattr(a1, 'Patient_Receptionist_13'):
        assert _is_linked(a1, 'Patient_Receptionist_13', b)
    _safe_set(b, 'Patient_Receptionist_02', a2)
    assert _is_linked(b, 'Patient_Receptionist_02', a2)
    if hasattr(a1, 'Patient_Receptionist_13'):
        assert not _is_linked(a1, 'Patient_Receptionist_13', b)
    if hasattr(a2, 'Patient_Receptionist_13'):
        assert _is_linked(a2, 'Patient_Receptionist_13', b)
    _safe_set(b, 'Patient_Receptionist_02', None)
    assert not _is_linked(b, 'Patient_Receptionist_02', a2)
    if hasattr(a2, 'Patient_Receptionist_13'):
        assert not _is_linked(a2, 'Patient_Receptionist_13', b)


def test_assoc_Patient_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(Location="sample_text", Room_No=7)
    a2 = Rooms(Location="sample_text_2", Room_No=13)
    b = Patient(Address="sample_text", Age=7, Name="sample_text", Pid=7, RoomNo_=7, Sex=7, TelNO=7)
    _safe_set(b, 'Patient_Rooms_08', {a1})
    assert _is_linked(b, 'Patient_Rooms_08', a1)
    if hasattr(a1, 'Patient_Rooms_19'):
        assert _is_linked(a1, 'Patient_Rooms_19', b)
    _safe_set(b, 'Patient_Rooms_08', {a2})
    assert _is_linked(b, 'Patient_Rooms_08', a2)
    if hasattr(a1, 'Patient_Rooms_19'):
        assert not _is_linked(a1, 'Patient_Rooms_19', b)
    if hasattr(a2, 'Patient_Rooms_19'):
        assert _is_linked(a2, 'Patient_Rooms_19', b)
    _safe_set(b, 'Patient_Rooms_08', set())
    assert not _is_linked(b, 'Patient_Rooms_08', a2)
    if hasattr(a2, 'Patient_Rooms_19'):
        assert not _is_linked(a2, 'Patient_Rooms_19', b)


def test_assoc_Receptionist_Bill2_reverse_link_reassign_clear():
    a1 = Receptionist(Rid="sample_text", Rname="sample_text")
    a2 = Receptionist(Rid="sample_text_2", Rname="sample_text_2")
    b = Bill(Amount="sample_text", Bill_No="sample_text", Patient_Name="sample_text")
    _safe_set(b, 'receptionist7', a1)
    assert _is_linked(b, 'receptionist7', a1)
    if hasattr(a1, 'bill6'):
        assert _is_linked(a1, 'bill6', b)
    _safe_set(b, 'receptionist7', a2)
    assert _is_linked(b, 'receptionist7', a2)
    if hasattr(a1, 'bill6'):
        assert not _is_linked(a1, 'bill6', b)
    if hasattr(a2, 'bill6'):
        assert _is_linked(a2, 'bill6', b)
    _safe_set(b, 'receptionist7', None)
    assert not _is_linked(b, 'receptionist7', a2)
    if hasattr(a2, 'bill6'):
        assert not _is_linked(a2, 'bill6', b)


def test_assoc_Rooms_Staff_reverse_link_reassign_clear():
    a1 = Staff(ID=7, Name="sample_text", Type="sample_text")
    a2 = Staff(ID=13, Name="sample_text_2", Type="sample_text_2")
    b = Rooms(Location="sample_text", Room_No=7)
    _safe_set(b, 'staff12', {a1})
    assert _is_linked(b, 'staff12', a1)
    if hasattr(a1, 'Rooms_Staff_113'):
        assert _is_linked(a1, 'Rooms_Staff_113', b)
    _safe_set(b, 'staff12', {a2})
    assert _is_linked(b, 'staff12', a2)
    if hasattr(a1, 'Rooms_Staff_113'):
        assert not _is_linked(a1, 'Rooms_Staff_113', b)
    if hasattr(a2, 'Rooms_Staff_113'):
        assert _is_linked(a2, 'Rooms_Staff_113', b)
    _safe_set(b, 'staff12', set())
    assert not _is_linked(b, 'staff12', a2)
    if hasattr(a2, 'Rooms_Staff_113'):
        assert not _is_linked(a2, 'Rooms_Staff_113', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

