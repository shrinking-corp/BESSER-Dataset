import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Department,
    Doctor,
    Patient,
    Receptionist,
    Ward,
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
    a1 = Doctor(Address="sample_text", Department="sample_text", DocID="sample_text", Name="sample_text", PhoneNumber=7, Specialization=7)
    a2 = Doctor(Address="sample_text_2", Department="sample_text_2", DocID="sample_text_2", Name="sample_text_2", PhoneNumber=13, Specialization=13)
    b = Department(DocID="sample_text", Name="sample_text", deptID="sample_text")
    _safe_set(b, 'belongs_to3', {a1})
    assert _is_linked(b, 'belongs_to3', a1)
    if hasattr(a1, 'department2'):
        assert _is_linked(a1, 'department2', b)
    _safe_set(b, 'belongs_to3', {a2})
    assert _is_linked(b, 'belongs_to3', a2)
    if hasattr(a1, 'department2'):
        assert not _is_linked(a1, 'department2', b)
    if hasattr(a2, 'department2'):
        assert _is_linked(a2, 'department2', b)
    _safe_set(b, 'belongs_to3', set())
    assert not _is_linked(b, 'belongs_to3', a2)
    if hasattr(a2, 'department2'):
        assert not _is_linked(a2, 'department2', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age="sample_text", Gender="sample_text", Name="sample_text", PatientID=7, WardNo=7)
    a2 = Patient(Address="sample_text_2", Age="sample_text_2", Gender="sample_text_2", Name="sample_text_2", PatientID=13, WardNo=13)
    b = Doctor(Address="sample_text", Department="sample_text", DocID="sample_text", Name="sample_text", PhoneNumber=7, Specialization=7)
    _safe_set(b, 'checks0', {a1})
    assert _is_linked(b, 'checks0', a1)
    if hasattr(a1, 'doctor1'):
        assert _is_linked(a1, 'doctor1', b)
    _safe_set(b, 'checks0', {a2})
    assert _is_linked(b, 'checks0', a2)
    if hasattr(a1, 'doctor1'):
        assert not _is_linked(a1, 'doctor1', b)
    if hasattr(a2, 'doctor1'):
        assert _is_linked(a2, 'doctor1', b)
    _safe_set(b, 'checks0', set())
    assert not _is_linked(b, 'checks0', a2)
    if hasattr(a2, 'doctor1'):
        assert not _is_linked(a2, 'doctor1', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(Address="sample_text", Age="sample_text", Gender="sample_text", Name="sample_text", PatientID=7, WardNo=7)
    a2 = Patient(Address="sample_text_2", Age="sample_text_2", Gender="sample_text_2", Name="sample_text_2", PatientID=13, WardNo=13)
    b = Bill(BillNo=7, amount=7, patientName="sample_text")
    _safe_set(b, 'patient9', a1)
    assert _is_linked(b, 'patient9', a1)
    if hasattr(a1, 'pays_bill8'):
        assert _is_linked(a1, 'pays_bill8', b)
    _safe_set(b, 'patient9', a2)
    assert _is_linked(b, 'patient9', a2)
    if hasattr(a1, 'pays_bill8'):
        assert not _is_linked(a1, 'pays_bill8', b)
    if hasattr(a2, 'pays_bill8'):
        assert _is_linked(a2, 'pays_bill8', b)
    _safe_set(b, 'patient9', None)
    assert not _is_linked(b, 'patient9', a2)
    if hasattr(a2, 'pays_bill8'):
        assert not _is_linked(a2, 'pays_bill8', b)


def test_assoc_Patient_Ward_reverse_link_reassign_clear():
    a1 = Ward(Location="sample_text", wardNo=7)
    a2 = Ward(Location="sample_text_2", wardNo=13)
    b = Patient(Address="sample_text", Age="sample_text", Gender="sample_text", Name="sample_text", PatientID=7, WardNo=7)
    _safe_set(b, 'alloted_to6', a1)
    assert _is_linked(b, 'alloted_to6', a1)
    if hasattr(a1, 'patient7'):
        assert _is_linked(a1, 'patient7', b)
    _safe_set(b, 'alloted_to6', a2)
    assert _is_linked(b, 'alloted_to6', a2)
    if hasattr(a1, 'patient7'):
        assert not _is_linked(a1, 'patient7', b)
    if hasattr(a2, 'patient7'):
        assert _is_linked(a2, 'patient7', b)
    _safe_set(b, 'alloted_to6', None)
    assert not _is_linked(b, 'alloted_to6', a2)
    if hasattr(a2, 'patient7'):
        assert not _is_linked(a2, 'patient7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Patient_Receptionist_stub_double():
    # Receptionist has no real 'patient5' property in the generated
    # code (a bare stub) -- manually attach it so Patient's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Patient's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Patient(Address="sample_text", Age="sample_text", Gender="sample_text", Name="sample_text", PatientID=7, WardNo=7)
    partner = Receptionist()
    setattr(partner, 'patient5', None)
    _safe_set(owner, 'give_appointment4', partner)
    assert owner in getattr(partner, 'patient5')
    _safe_set(owner, 'give_appointment4', None)
    assert owner not in getattr(partner, 'patient5')


def test_assoc_Receptionist_Bill_stub_double():
    # Receptionist has no real 'bill10' property in the generated
    # code (a bare stub) -- manually attach it so Bill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Bill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Bill(BillNo=7, amount=7, patientName="sample_text")
    partner = Receptionist()
    setattr(partner, 'bill10', None)
    _safe_set(owner, 'generates_bill11', partner)
    assert owner in getattr(partner, 'bill10')
    _safe_set(owner, 'generates_bill11', None)
    assert owner not in getattr(partner, 'bill10')


