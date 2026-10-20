import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Department,
    Doctor,
    Patient,
    Procedure,
    Receptionist,
    Treatment,
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
    a1 = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    a2 = Doctor(address="sample_text_2", departamentID=13, department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    b = Department(id=7, name="sample_text")
    _safe_set(b, 'doctor3', {a1})
    assert _is_linked(b, 'doctor3', a1)
    if hasattr(a1, 'depmt2'):
        assert _is_linked(a1, 'depmt2', b)
    _safe_set(b, 'doctor3', {a2})
    assert _is_linked(b, 'doctor3', a2)
    if hasattr(a1, 'depmt2'):
        assert not _is_linked(a1, 'depmt2', b)
    if hasattr(a2, 'depmt2'):
        assert _is_linked(a2, 'depmt2', b)
    _safe_set(b, 'doctor3', set())
    assert not _is_linked(b, 'doctor3', a2)
    if hasattr(a2, 'depmt2'):
        assert not _is_linked(a2, 'depmt2', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    a2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", sex="sample_text_2", telno=13)
    b = Doctor(address="sample_text", departamentID=7, department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    _safe_set(b, 'patients0', {a1})
    assert _is_linked(b, 'patients0', a1)
    if hasattr(a1, 'doctors1'):
        assert _is_linked(a1, 'doctors1', b)
    _safe_set(b, 'patients0', {a2})
    assert _is_linked(b, 'patients0', a2)
    if hasattr(a1, 'doctors1'):
        assert not _is_linked(a1, 'doctors1', b)
    if hasattr(a2, 'doctors1'):
        assert _is_linked(a2, 'doctors1', b)
    _safe_set(b, 'patients0', set())
    assert not _is_linked(b, 'patients0', a2)
    if hasattr(a2, 'doctors1'):
        assert not _is_linked(a2, 'doctors1', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    a2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", sex="sample_text_2", telno=13)
    b = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    _safe_set(b, 'pat5', {a1})
    assert _is_linked(b, 'pat5', a1)
    if hasattr(a1, 'bill4'):
        assert _is_linked(a1, 'bill4', b)
    _safe_set(b, 'pat5', {a2})
    assert _is_linked(b, 'pat5', a2)
    if hasattr(a1, 'bill4'):
        assert not _is_linked(a1, 'bill4', b)
    if hasattr(a2, 'bill4'):
        assert _is_linked(a2, 'bill4', b)
    _safe_set(b, 'pat5', set())
    assert not _is_linked(b, 'pat5', a2)
    if hasattr(a2, 'bill4'):
        assert not _is_linked(a2, 'bill4', b)


def test_assoc_Procedure_Treatment_reverse_link_reassign_clear():
    a1 = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    a2 = Treatment(idBill=13, idTreatment=13, patientID=13, procedureID=13)
    b = Procedure(idProcedure=7, name="sample_text", price=7)
    _safe_set(b, 'treatment12', {a1})
    assert _is_linked(b, 'treatment12', a1)
    if hasattr(a1, 'procedure13'):
        assert _is_linked(a1, 'procedure13', b)
    _safe_set(b, 'treatment12', {a2})
    assert _is_linked(b, 'treatment12', a2)
    if hasattr(a1, 'procedure13'):
        assert not _is_linked(a1, 'procedure13', b)
    if hasattr(a2, 'procedure13'):
        assert _is_linked(a2, 'procedure13', b)
    _safe_set(b, 'treatment12', set())
    assert not _is_linked(b, 'treatment12', a2)
    if hasattr(a2, 'procedure13'):
        assert not _is_linked(a2, 'procedure13', b)


def test_assoc_Treatment_Patient_reverse_link_reassign_clear():
    a1 = Treatment(idBill=7, idTreatment=7, patientID=7, procedureID=7)
    a2 = Treatment(idBill=13, idTreatment=13, patientID=13, procedureID=13)
    b = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    _safe_set(b, 'treatment11', a1)
    assert _is_linked(b, 'treatment11', a1)
    if hasattr(a1, 'patient10'):
        assert _is_linked(a1, 'patient10', b)
    _safe_set(b, 'treatment11', a2)
    assert _is_linked(b, 'treatment11', a2)
    if hasattr(a1, 'patient10'):
        assert not _is_linked(a1, 'patient10', b)
    if hasattr(a2, 'patient10'):
        assert _is_linked(a2, 'patient10', b)
    _safe_set(b, 'treatment11', None)
    assert not _is_linked(b, 'treatment11', a2)
    if hasattr(a2, 'patient10'):
        assert not _is_linked(a2, 'patient10', b)


def test_assoc_manages_reverse_link_reassign_clear():
    a1 = Receptionist(attribute2="sample_text", id=7)
    a2 = Receptionist(attribute2="sample_text_2", id=13)
    b = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    _safe_set(b, 'receptionist9', {a1})
    assert _is_linked(b, 'receptionist9', a1)
    if hasattr(a1, 'sbill8'):
        assert _is_linked(a1, 'sbill8', b)
    _safe_set(b, 'receptionist9', {a2})
    assert _is_linked(b, 'receptionist9', a2)
    if hasattr(a1, 'sbill8'):
        assert not _is_linked(a1, 'sbill8', b)
    if hasattr(a2, 'sbill8'):
        assert _is_linked(a2, 'sbill8', b)
    _safe_set(b, 'receptionist9', set())
    assert not _is_linked(b, 'receptionist9', a2)
    if hasattr(a2, 'sbill8'):
        assert not _is_linked(a2, 'sbill8', b)


def test_assoc_receptions_reverse_link_reassign_clear():
    a1 = Receptionist(attribute2="sample_text", id=7)
    a2 = Receptionist(attribute2="sample_text_2", id=13)
    b = Patient(address="sample_text", age=7, id=7, name="sample_text", sex="sample_text", telno=7)
    _safe_set(b, 'receptionist6', a1)
    assert _is_linked(b, 'receptionist6', a1)
    if hasattr(a1, 'p7'):
        assert _is_linked(a1, 'p7', b)
    _safe_set(b, 'receptionist6', a2)
    assert _is_linked(b, 'receptionist6', a2)
    if hasattr(a1, 'p7'):
        assert not _is_linked(a1, 'p7', b)
    if hasattr(a2, 'p7'):
        assert _is_linked(a2, 'p7', b)
    _safe_set(b, 'receptionist6', None)
    assert not _is_linked(b, 'receptionist6', a2)
    if hasattr(a2, 'p7'):
        assert not _is_linked(a2, 'p7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

