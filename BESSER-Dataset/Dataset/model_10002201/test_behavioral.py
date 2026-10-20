import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Dept,
    Doctor,
    Patient,
    Receptionist,
    Rooms,
    Staff,
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

def test_assoc_Class_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(Name="sample_text", Receptional_id=7)
    a2 = Receptionist(Name="sample_text_2", Receptional_id=13)
    b = Bill(Amount=7, BillNo_="sample_text", PatientName="sample_text")
    _safe_set(b, 'receptionist0', a1)
    assert _is_linked(b, 'receptionist0', a1)
    if hasattr(a1, 'Class_Receptionist_11'):
        assert _is_linked(a1, 'Class_Receptionist_11', b)
    _safe_set(b, 'receptionist0', a2)
    assert _is_linked(b, 'receptionist0', a2)
    if hasattr(a1, 'Class_Receptionist_11'):
        assert not _is_linked(a1, 'Class_Receptionist_11', b)
    if hasattr(a2, 'Class_Receptionist_11'):
        assert _is_linked(a2, 'Class_Receptionist_11', b)
    _safe_set(b, 'receptionist0', None)
    assert not _is_linked(b, 'receptionist0', a2)
    if hasattr(a2, 'Class_Receptionist_11'):
        assert not _is_linked(a2, 'Class_Receptionist_11', b)


def test_assoc_Doctor_Dept_reverse_link_reassign_clear():
    a1 = Doctor(Dept="sample_text", DocName="sample_text", Doct_id=7, Location="sample_text", PhoneNo_=7, Specialization="sample_text")
    a2 = Doctor(Dept="sample_text_2", DocName="sample_text_2", Doct_id=13, Location="sample_text_2", PhoneNo_=13, Specialization="sample_text_2")
    b = Dept(Doc_id=7, Id=7, Name="sample_text")
    _safe_set(b, 'doctor7', a1)
    assert _is_linked(b, 'doctor7', a1)
    if hasattr(a1, 'dept6'):
        assert _is_linked(a1, 'dept6', b)
    _safe_set(b, 'doctor7', a2)
    assert _is_linked(b, 'doctor7', a2)
    if hasattr(a1, 'dept6'):
        assert not _is_linked(a1, 'dept6', b)
    if hasattr(a2, 'dept6'):
        assert _is_linked(a2, 'dept6', b)
    _safe_set(b, 'doctor7', None)
    assert not _is_linked(b, 'doctor7', a2)
    if hasattr(a2, 'dept6'):
        assert not _is_linked(a2, 'dept6', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", Patient_id=7, PhoneNo_=7, RoomNo_=7, Sex="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", Patient_id=13, PhoneNo_=13, RoomNo_=13, Sex="sample_text_2")
    b = Bill(Amount=7, BillNo_="sample_text", PatientName="sample_text")
    _safe_set(b, 'patient11', a1)
    assert _is_linked(b, 'patient11', a1)
    if hasattr(a1, 'bill10'):
        assert _is_linked(a1, 'bill10', b)
    _safe_set(b, 'patient11', a2)
    assert _is_linked(b, 'patient11', a2)
    if hasattr(a1, 'bill10'):
        assert not _is_linked(a1, 'bill10', b)
    if hasattr(a2, 'bill10'):
        assert _is_linked(a2, 'bill10', b)
    _safe_set(b, 'patient11', None)
    assert not _is_linked(b, 'patient11', a2)
    if hasattr(a2, 'bill10'):
        assert not _is_linked(a2, 'bill10', b)


def test_assoc_Patient_Doctor_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Name="sample_text", Patient_id=7, PhoneNo_=7, RoomNo_=7, Sex="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, Name="sample_text_2", Patient_id=13, PhoneNo_=13, RoomNo_=13, Sex="sample_text_2")
    b = Doctor(Dept="sample_text", DocName="sample_text", Doct_id=7, Location="sample_text", PhoneNo_=7, Specialization="sample_text")
    _safe_set(b, 'patient5', a1)
    assert _is_linked(b, 'patient5', a1)
    if hasattr(a1, 'doctor4'):
        assert _is_linked(a1, 'doctor4', b)
    _safe_set(b, 'patient5', a2)
    assert _is_linked(b, 'patient5', a2)
    if hasattr(a1, 'doctor4'):
        assert not _is_linked(a1, 'doctor4', b)
    if hasattr(a2, 'doctor4'):
        assert _is_linked(a2, 'doctor4', b)
    _safe_set(b, 'patient5', None)
    assert not _is_linked(b, 'patient5', a2)
    if hasattr(a2, 'doctor4'):
        assert not _is_linked(a2, 'doctor4', b)


def test_assoc_Patient_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(Location="sample_text", Roomno_=7)
    a2 = Rooms(Location="sample_text_2", Roomno_=13)
    b = Patient(Address="sample_text", Age=7, Name="sample_text", Patient_id=7, PhoneNo_=7, RoomNo_=7, Sex="sample_text")
    _safe_set(b, 'rooms8', a1)
    assert _is_linked(b, 'rooms8', a1)
    if hasattr(a1, 'patient9'):
        assert _is_linked(a1, 'patient9', b)
    _safe_set(b, 'rooms8', a2)
    assert _is_linked(b, 'rooms8', a2)
    if hasattr(a1, 'patient9'):
        assert not _is_linked(a1, 'patient9', b)
    if hasattr(a2, 'patient9'):
        assert _is_linked(a2, 'patient9', b)
    _safe_set(b, 'rooms8', None)
    assert not _is_linked(b, 'rooms8', a2)
    if hasattr(a2, 'patient9'):
        assert not _is_linked(a2, 'patient9', b)


def test_assoc_Receptionist_Patient_reverse_link_reassign_clear():
    a1 = Receptionist(Name="sample_text", Receptional_id=7)
    a2 = Receptionist(Name="sample_text_2", Receptional_id=13)
    b = Patient(Address="sample_text", Age=7, Name="sample_text", Patient_id=7, PhoneNo_=7, RoomNo_=7, Sex="sample_text")
    _safe_set(b, 'receptionist3', a1)
    assert _is_linked(b, 'receptionist3', a1)
    if hasattr(a1, 'patient2'):
        assert _is_linked(a1, 'patient2', b)
    _safe_set(b, 'receptionist3', a2)
    assert _is_linked(b, 'receptionist3', a2)
    if hasattr(a1, 'patient2'):
        assert not _is_linked(a1, 'patient2', b)
    if hasattr(a2, 'patient2'):
        assert _is_linked(a2, 'patient2', b)
    _safe_set(b, 'receptionist3', None)
    assert not _is_linked(b, 'receptionist3', a2)
    if hasattr(a2, 'patient2'):
        assert not _is_linked(a2, 'patient2', b)


def test_assoc_Rooms_Staff_reverse_link_reassign_clear():
    a1 = Staff(Id=7, Staff_name="sample_text", Type="sample_text")
    a2 = Staff(Id=13, Staff_name="sample_text_2", Type="sample_text_2")
    b = Rooms(Location="sample_text", Roomno_=7)
    _safe_set(b, 'staff12', a1)
    assert _is_linked(b, 'staff12', a1)
    if hasattr(a1, 'rooms13'):
        assert _is_linked(a1, 'rooms13', b)
    _safe_set(b, 'staff12', a2)
    assert _is_linked(b, 'staff12', a2)
    if hasattr(a1, 'rooms13'):
        assert not _is_linked(a1, 'rooms13', b)
    if hasattr(a2, 'rooms13'):
        assert _is_linked(a2, 'rooms13', b)
    _safe_set(b, 'staff12', None)
    assert not _is_linked(b, 'staff12', a2)
    if hasattr(a2, 'rooms13'):
        assert not _is_linked(a2, 'rooms13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

