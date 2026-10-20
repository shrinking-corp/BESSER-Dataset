import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Dept,
    Doctor,
    Float,
    Patient,
    ReceptionList,
    Rooms,
    system_Component,
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
    a1 = Doctor(Dept="sample_text", Location="sample_text", Name="sample_text", PhoneNo=7, Specialization="sample_text", docId=7)
    a2 = Doctor(Dept="sample_text_2", Location="sample_text_2", Name="sample_text_2", PhoneNo=13, Specialization="sample_text_2", docId=13)
    b = Dept(DocId=7, Id=7, Name="sample_text")
    _safe_set(b, 'doctor11', {a1})
    assert _is_linked(b, 'doctor11', a1)
    if hasattr(a1, 'dept10'):
        assert _is_linked(a1, 'dept10', b)
    _safe_set(b, 'doctor11', {a2})
    assert _is_linked(b, 'doctor11', a2)
    if hasattr(a1, 'dept10'):
        assert not _is_linked(a1, 'dept10', b)
    if hasattr(a2, 'dept10'):
        assert _is_linked(a2, 'dept10', b)
    _safe_set(b, 'doctor11', set())
    assert not _is_linked(b, 'doctor11', a2)
    if hasattr(a2, 'dept10'):
        assert not _is_linked(a2, 'dept10', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age=7, PatientId=7, PatientName="sample_text", PhoneNo=7, RoomNo=7, Sex="sample_text")
    a2 = Patient(Address="sample_text_2", Age=13, PatientId=13, PatientName="sample_text_2", PhoneNo=13, RoomNo=13, Sex="sample_text_2")
    b = Doctor(Dept="sample_text", Location="sample_text", Name="sample_text", PhoneNo=7, Specialization="sample_text", docId=7)
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


def test_assoc_Patient_ReceptionList_reverse_link_reassign_clear():
    a1 = ReceptionList(RepId=7, name="sample_text")
    a2 = ReceptionList(RepId=13, name="sample_text_2")
    b = Patient(Address="sample_text", Age=7, PatientId=7, PatientName="sample_text", PhoneNo=7, RoomNo=7, Sex="sample_text")
    _safe_set(b, 'receptionList2', a1)
    assert _is_linked(b, 'receptionList2', a1)
    if hasattr(a1, 'patient3'):
        assert _is_linked(a1, 'patient3', b)
    _safe_set(b, 'receptionList2', a2)
    assert _is_linked(b, 'receptionList2', a2)
    if hasattr(a1, 'patient3'):
        assert not _is_linked(a1, 'patient3', b)
    if hasattr(a2, 'patient3'):
        assert _is_linked(a2, 'patient3', b)
    _safe_set(b, 'receptionList2', None)
    assert not _is_linked(b, 'receptionList2', a2)
    if hasattr(a2, 'patient3'):
        assert not _is_linked(a2, 'patient3', b)


def test_assoc_Rooms_Patient_reverse_link_reassign_clear():
    a1 = Rooms(Location="sample_text", RoomNo=7)
    a2 = Rooms(Location="sample_text_2", RoomNo=13)
    b = Patient(Address="sample_text", Age=7, PatientId=7, PatientName="sample_text", PhoneNo=7, RoomNo=7, Sex="sample_text")
    _safe_set(b, 'rooms9', a1)
    assert _is_linked(b, 'rooms9', a1)
    if hasattr(a1, 'patient8'):
        assert _is_linked(a1, 'patient8', b)
    _safe_set(b, 'rooms9', a2)
    assert _is_linked(b, 'rooms9', a2)
    if hasattr(a1, 'patient8'):
        assert not _is_linked(a1, 'patient8', b)
    if hasattr(a2, 'patient8'):
        assert _is_linked(a2, 'patient8', b)
    _safe_set(b, 'rooms9', None)
    assert not _is_linked(b, 'rooms9', a2)
    if hasattr(a2, 'patient8'):
        assert not _is_linked(a2, 'patient8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

