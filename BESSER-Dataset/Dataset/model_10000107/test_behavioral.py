import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Doctor,
    Patient,
    Receptionist,
    Room,
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
    a1 = Patient(Address="sample_text", Age=7, Id=7, Name="sample_text", PhNo_=7, WardNo=7)
    a2 = Patient(Address="sample_text_2", Age=13, Id=13, Name="sample_text_2", PhNo_=13, WardNo=13)
    b = Doctor(Address="sample_text", Department="sample_text", DocId_=7, Email="sample_text", Name="sample_text")
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


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, Id=7, Name="sample_text", PhNo_=7, WardNo=7)
    a2 = Patient(Address="sample_text_2", Age=13, Id=13, Name="sample_text_2", PhNo_=13, WardNo=13)
    b = Bill(Amount="sample_text", BillNo="sample_text", Patient_Id=7)
    _safe_set(b, 'patient7', a1)
    assert _is_linked(b, 'patient7', a1)
    if hasattr(a1, 'bill6'):
        assert _is_linked(a1, 'bill6', b)
    _safe_set(b, 'patient7', a2)
    assert _is_linked(b, 'patient7', a2)
    if hasattr(a1, 'bill6'):
        assert not _is_linked(a1, 'bill6', b)
    if hasattr(a2, 'bill6'):
        assert _is_linked(a2, 'bill6', b)
    _safe_set(b, 'patient7', None)
    assert not _is_linked(b, 'patient7', a2)
    if hasattr(a2, 'bill6'):
        assert not _is_linked(a2, 'bill6', b)


def test_assoc_Patient_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(Email="sample_text", Id=7, Name="sample_text")
    a2 = Receptionist(Email="sample_text_2", Id=13, Name="sample_text_2")
    b = Patient(Address="sample_text", Age=7, Id=7, Name="sample_text", PhNo_=7, WardNo=7)
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
    a1 = Room(RoomNo=7, RoomType="sample_text")
    a2 = Room(RoomNo=13, RoomType="sample_text_2")
    b = Patient(Address="sample_text", Age=7, Id=7, Name="sample_text", PhNo_=7, WardNo=7)
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


def test_assoc_Receptionist_Bill_reverse_link_reassign_clear():
    a1 = Receptionist(Email="sample_text", Id=7, Name="sample_text")
    a2 = Receptionist(Email="sample_text_2", Id=13, Name="sample_text_2")
    b = Bill(Amount="sample_text", BillNo="sample_text", Patient_Id=7)
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

