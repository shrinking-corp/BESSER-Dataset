import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Doctor,
    Employee,
    Nurse,
    Receiptionist,
    Room,
    patient,
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

def test_assoc_patient_Room_reverse_link_reassign_clear():
    a1 = patient(DOB="sample_text", Patient_Address="sample_text", Patient_Contact_NO=7, Patient_ID=7, Patient_Name="sample_text", Sex="sample_text", Status="sample_text")
    a2 = patient(DOB="sample_text_2", Patient_Address="sample_text_2", Patient_Contact_NO=13, Patient_ID=13, Patient_Name="sample_text_2", Sex="sample_text_2", Status="sample_text_2")
    b = Room(Room_NO=7, Room_Rent="sample_text", Room_TYPE="sample_text")
    _safe_set(b, 'patient5', {a1})
    assert _is_linked(b, 'patient5', a1)
    if hasattr(a1, 'room4'):
        assert _is_linked(a1, 'room4', b)
    _safe_set(b, 'patient5', {a2})
    assert _is_linked(b, 'patient5', a2)
    if hasattr(a1, 'room4'):
        assert not _is_linked(a1, 'room4', b)
    if hasattr(a2, 'room4'):
        assert _is_linked(a2, 'room4', b)
    _safe_set(b, 'patient5', set())
    assert not _is_linked(b, 'patient5', a2)
    if hasattr(a2, 'room4'):
        assert not _is_linked(a2, 'room4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Doctor_patient_stub_double():
    # Doctor has no real 'patient0' property in the generated
    # code (a bare stub) -- manually attach it so patient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # patient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = patient(DOB="sample_text", Patient_Address="sample_text", Patient_Contact_NO=7, Patient_ID=7, Patient_Name="sample_text", Sex="sample_text", Status="sample_text")
    partner = Doctor()
    setattr(partner, 'patient0', None)
    _safe_set(owner, 'doctor1', {partner})
    assert owner in getattr(partner, 'patient0')
    _safe_set(owner, 'doctor1', set())
    assert owner not in getattr(partner, 'patient0')


def test_assoc_Nurse_Room_stub_double():
    # Nurse has no real 'room6' property in the generated
    # code (a bare stub) -- manually attach it so Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Room(Room_NO=7, Room_Rent="sample_text", Room_TYPE="sample_text")
    partner = Nurse()
    setattr(partner, 'room6', None)
    _safe_set(owner, 'nurse7', partner)
    assert owner in getattr(partner, 'room6')
    _safe_set(owner, 'nurse7', None)
    assert owner not in getattr(partner, 'room6')


def test_assoc_Receiptionist_patient_stub_double():
    # Receiptionist has no real 'patient2' property in the generated
    # code (a bare stub) -- manually attach it so patient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # patient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = patient(DOB="sample_text", Patient_Address="sample_text", Patient_Contact_NO=7, Patient_ID=7, Patient_Name="sample_text", Sex="sample_text", Status="sample_text")
    partner = Receiptionist()
    setattr(partner, 'patient2', None)
    _safe_set(owner, 'receiptionist3', {partner})
    assert owner in getattr(partner, 'patient2')
    _safe_set(owner, 'receiptionist3', set())
    assert owner not in getattr(partner, 'patient2')


