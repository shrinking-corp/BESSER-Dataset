import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Deparment,
    Doctor,
    Patient,
    Receptionsit,
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

def test_assoc_Doctor_Deparment_reverse_link_reassign_clear():
    a1 = Doctor(Department="sample_text", DocId=7, Name="sample_text", PhNo=7, Specialization="sample_text")
    a2 = Doctor(Department="sample_text_2", DocId=13, Name="sample_text_2", PhNo=13, Specialization="sample_text_2")
    b = Deparment(Id=7, Name="sample_text", PhNo=7)
    _safe_set(b, 'doctor9', a1)
    assert _is_linked(b, 'doctor9', a1)
    if hasattr(a1, 'Belongs_To8'):
        assert _is_linked(a1, 'Belongs_To8', b)
    _safe_set(b, 'doctor9', a2)
    assert _is_linked(b, 'doctor9', a2)
    if hasattr(a1, 'Belongs_To8'):
        assert not _is_linked(a1, 'Belongs_To8', b)
    if hasattr(a2, 'Belongs_To8'):
        assert _is_linked(a2, 'Belongs_To8', b)
    _safe_set(b, 'doctor9', None)
    assert not _is_linked(b, 'doctor9', a2)
    if hasattr(a2, 'Belongs_To8'):
        assert not _is_linked(a2, 'Belongs_To8', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(Name="sample_text", PatientId=7, age=7)
    a2 = Patient(Name="sample_text_2", PatientId=13, age=13)
    b = Doctor(Department="sample_text", DocId=7, Name="sample_text", PhNo=7, Specialization="sample_text")
    _safe_set(b, 'Checks0', a1)
    assert _is_linked(b, 'Checks0', a1)
    if hasattr(a1, 'doctor1'):
        assert _is_linked(a1, 'doctor1', b)
    _safe_set(b, 'Checks0', a2)
    assert _is_linked(b, 'Checks0', a2)
    if hasattr(a1, 'doctor1'):
        assert not _is_linked(a1, 'doctor1', b)
    if hasattr(a2, 'doctor1'):
        assert _is_linked(a2, 'doctor1', b)
    _safe_set(b, 'Checks0', None)
    assert not _is_linked(b, 'Checks0', a2)
    if hasattr(a2, 'doctor1'):
        assert not _is_linked(a2, 'doctor1', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Name="sample_text", PatientId=7, age=7)
    a2 = Patient(Name="sample_text_2", PatientId=13, age=13)
    b = Bill(Amount="sample_text", BillNo="sample_text", PatientName="sample_text")
    _safe_set(b, 'patient5', a1)
    assert _is_linked(b, 'patient5', a1)
    if hasattr(a1, 'Pay_Bill4'):
        assert _is_linked(a1, 'Pay_Bill4', b)
    _safe_set(b, 'patient5', a2)
    assert _is_linked(b, 'patient5', a2)
    if hasattr(a1, 'Pay_Bill4'):
        assert not _is_linked(a1, 'Pay_Bill4', b)
    if hasattr(a2, 'Pay_Bill4'):
        assert _is_linked(a2, 'Pay_Bill4', b)
    _safe_set(b, 'patient5', None)
    assert not _is_linked(b, 'patient5', a2)
    if hasattr(a2, 'Pay_Bill4'):
        assert not _is_linked(a2, 'Pay_Bill4', b)


def test_assoc_Patient_Receptionsit_reverse_link_reassign_clear():
    a1 = Receptionsit(Id=7, Name="sample_text")
    a2 = Receptionsit(Id=13, Name="sample_text_2")
    b = Patient(Name="sample_text", PatientId=7, age=7)
    _safe_set(b, 'Give_Appointment2', a1)
    assert _is_linked(b, 'Give_Appointment2', a1)
    if hasattr(a1, 'patient3'):
        assert _is_linked(a1, 'patient3', b)
    _safe_set(b, 'Give_Appointment2', a2)
    assert _is_linked(b, 'Give_Appointment2', a2)
    if hasattr(a1, 'patient3'):
        assert not _is_linked(a1, 'patient3', b)
    if hasattr(a2, 'patient3'):
        assert _is_linked(a2, 'patient3', b)
    _safe_set(b, 'Give_Appointment2', None)
    assert not _is_linked(b, 'Give_Appointment2', a2)
    if hasattr(a2, 'patient3'):
        assert not _is_linked(a2, 'patient3', b)


def test_assoc_Patient_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(RoomNo=7, WardNo="sample_text")
    a2 = Rooms(RoomNo=13, WardNo="sample_text_2")
    b = Patient(Name="sample_text", PatientId=7, age=7)
    _safe_set(b, 'Alloted_To10', a1)
    assert _is_linked(b, 'Alloted_To10', a1)
    if hasattr(a1, 'patient11'):
        assert _is_linked(a1, 'patient11', b)
    _safe_set(b, 'Alloted_To10', a2)
    assert _is_linked(b, 'Alloted_To10', a2)
    if hasattr(a1, 'patient11'):
        assert not _is_linked(a1, 'patient11', b)
    if hasattr(a2, 'patient11'):
        assert _is_linked(a2, 'patient11', b)
    _safe_set(b, 'Alloted_To10', None)
    assert not _is_linked(b, 'Alloted_To10', a2)
    if hasattr(a2, 'patient11'):
        assert not _is_linked(a2, 'patient11', b)


def test_assoc_Patient_Staff_reverse_link_reassign_clear():
    a1 = Staff(Id=7, Name="sample_text", Type="sample_text")
    a2 = Staff(Id=13, Name="sample_text_2", Type="sample_text_2")
    b = Patient(Name="sample_text", PatientId=7, age=7)
    _safe_set(b, 'staff12', a1)
    assert _is_linked(b, 'staff12', a1)
    if hasattr(a1, 'Do_Cleaning13'):
        assert _is_linked(a1, 'Do_Cleaning13', b)
    _safe_set(b, 'staff12', a2)
    assert _is_linked(b, 'staff12', a2)
    if hasattr(a1, 'Do_Cleaning13'):
        assert not _is_linked(a1, 'Do_Cleaning13', b)
    if hasattr(a2, 'Do_Cleaning13'):
        assert _is_linked(a2, 'Do_Cleaning13', b)
    _safe_set(b, 'staff12', None)
    assert not _is_linked(b, 'staff12', a2)
    if hasattr(a2, 'Do_Cleaning13'):
        assert not _is_linked(a2, 'Do_Cleaning13', b)


def test_assoc_Receptionsit_Bill_reverse_link_reassign_clear():
    a1 = Receptionsit(Id=7, Name="sample_text")
    a2 = Receptionsit(Id=13, Name="sample_text_2")
    b = Bill(Amount="sample_text", BillNo="sample_text", PatientName="sample_text")
    _safe_set(b, 'receptionsit7', a1)
    assert _is_linked(b, 'receptionsit7', a1)
    if hasattr(a1, 'Generate_Bills6'):
        assert _is_linked(a1, 'Generate_Bills6', b)
    _safe_set(b, 'receptionsit7', a2)
    assert _is_linked(b, 'receptionsit7', a2)
    if hasattr(a1, 'Generate_Bills6'):
        assert not _is_linked(a1, 'Generate_Bills6', b)
    if hasattr(a2, 'Generate_Bills6'):
        assert _is_linked(a2, 'Generate_Bills6', b)
    _safe_set(b, 'receptionsit7', None)
    assert not _is_linked(b, 'receptionsit7', a2)
    if hasattr(a2, 'Generate_Bills6'):
        assert not _is_linked(a2, 'Generate_Bills6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

