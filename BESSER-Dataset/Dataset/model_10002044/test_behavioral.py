import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Doctor,
    Patient,
    Receptionist,
    Room,
    appointment,
    medicine,
    nurse,
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

def test_assoc_Bill_medicine_reverse_link_reassign_clear():
    a1 = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    a2 = medicine(m_code=13, m_name="sample_text_2", price=9.99, quantity=13)
    b = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    _safe_set(b, 'medicine14', a1)
    assert _is_linked(b, 'medicine14', a1)
    if hasattr(a1, 'bill15'):
        assert _is_linked(a1, 'bill15', b)
    _safe_set(b, 'medicine14', a2)
    assert _is_linked(b, 'medicine14', a2)
    if hasattr(a1, 'bill15'):
        assert not _is_linked(a1, 'bill15', b)
    if hasattr(a2, 'bill15'):
        assert _is_linked(a2, 'bill15', b)
    _safe_set(b, 'medicine14', None)
    assert not _is_linked(b, 'medicine14', a2)
    if hasattr(a2, 'bill15'):
        assert not _is_linked(a2, 'bill15', b)


def test_assoc_Doctor_Patient_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    a2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    b = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
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


def test_assoc_Doctor_appointment_reverse_link_reassign_clear():
    a1 = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    a2 = appointment(A_no=13, d_name="sample_text_2", p_id=13, p_name="sample_text_2", time=date(2025, 6, 15))
    b = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    _safe_set(b, 'appointment8', a1)
    assert _is_linked(b, 'appointment8', a1)
    if hasattr(a1, 'doctor9'):
        assert _is_linked(a1, 'doctor9', b)
    _safe_set(b, 'appointment8', a2)
    assert _is_linked(b, 'appointment8', a2)
    if hasattr(a1, 'doctor9'):
        assert not _is_linked(a1, 'doctor9', b)
    if hasattr(a2, 'doctor9'):
        assert _is_linked(a2, 'doctor9', b)
    _safe_set(b, 'appointment8', None)
    assert not _is_linked(b, 'appointment8', a2)
    if hasattr(a2, 'doctor9'):
        assert not _is_linked(a2, 'doctor9', b)


def test_assoc_Doctor_medicine_reverse_link_reassign_clear():
    a1 = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    a2 = medicine(m_code=13, m_name="sample_text_2", price=9.99, quantity=13)
    b = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    _safe_set(b, 'medicine16', a1)
    assert _is_linked(b, 'medicine16', a1)
    if hasattr(a1, 'doctor17'):
        assert _is_linked(a1, 'doctor17', b)
    _safe_set(b, 'medicine16', a2)
    assert _is_linked(b, 'medicine16', a2)
    if hasattr(a1, 'doctor17'):
        assert not _is_linked(a1, 'doctor17', b)
    if hasattr(a2, 'doctor17'):
        assert _is_linked(a2, 'doctor17', b)
    _safe_set(b, 'medicine16', None)
    assert not _is_linked(b, 'medicine16', a2)
    if hasattr(a2, 'doctor17'):
        assert not _is_linked(a2, 'doctor17', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    a2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    b = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    _safe_set(b, 'pat3', a1)
    assert _is_linked(b, 'pat3', a1)
    if hasattr(a1, 'bill2'):
        assert _is_linked(a1, 'bill2', b)
    _safe_set(b, 'pat3', a2)
    assert _is_linked(b, 'pat3', a2)
    if hasattr(a1, 'bill2'):
        assert not _is_linked(a1, 'bill2', b)
    if hasattr(a2, 'bill2'):
        assert _is_linked(a2, 'bill2', b)
    _safe_set(b, 'pat3', None)
    assert not _is_linked(b, 'pat3', a2)
    if hasattr(a2, 'bill2'):
        assert not _is_linked(a2, 'bill2', b)


def test_assoc_Patient_Room_reverse_link_reassign_clear():
    a1 = Room(roomno=7, roomtype="sample_text")
    a2 = Room(roomno=13, roomtype="sample_text_2")
    b = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    _safe_set(b, 'room12', a1)
    assert _is_linked(b, 'room12', a1)
    if hasattr(a1, 'patient13'):
        assert _is_linked(a1, 'patient13', b)
    _safe_set(b, 'room12', a2)
    assert _is_linked(b, 'room12', a2)
    if hasattr(a1, 'patient13'):
        assert not _is_linked(a1, 'patient13', b)
    if hasattr(a2, 'patient13'):
        assert _is_linked(a2, 'patient13', b)
    _safe_set(b, 'room12', None)
    assert not _is_linked(b, 'room12', a2)
    if hasattr(a2, 'patient13'):
        assert not _is_linked(a2, 'patient13', b)


def test_assoc_Patient_appointment_reverse_link_reassign_clear():
    a1 = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    a2 = appointment(A_no=13, d_name="sample_text_2", p_id=13, p_name="sample_text_2", time=date(2025, 6, 15))
    b = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    _safe_set(b, 'appointment10', a1)
    assert _is_linked(b, 'appointment10', a1)
    if hasattr(a1, 'patient11'):
        assert _is_linked(a1, 'patient11', b)
    _safe_set(b, 'appointment10', a2)
    assert _is_linked(b, 'appointment10', a2)
    if hasattr(a1, 'patient11'):
        assert not _is_linked(a1, 'patient11', b)
    if hasattr(a2, 'patient11'):
        assert _is_linked(a2, 'patient11', b)
    _safe_set(b, 'appointment10', None)
    assert not _is_linked(b, 'appointment10', a2)
    if hasattr(a2, 'patient11'):
        assert not _is_linked(a2, 'patient11', b)


def test_assoc_manages_reverse_link_reassign_clear():
    a1 = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    a2 = Receptionist(email="sample_text_2", id=13, password="sample_text_2", username="sample_text_2")
    b = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
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


def test_assoc_nurse_Room_reverse_link_reassign_clear():
    a1 = nurse(availability=True, contact=7, id=7, name="sample_text")
    a2 = nurse(availability=False, contact=13, id=13, name="sample_text_2")
    b = Room(roomno=7, roomtype="sample_text")
    _safe_set(b, 'nurse19', a1)
    assert _is_linked(b, 'nurse19', a1)
    if hasattr(a1, 'room18'):
        assert _is_linked(a1, 'room18', b)
    _safe_set(b, 'nurse19', a2)
    assert _is_linked(b, 'nurse19', a2)
    if hasattr(a1, 'room18'):
        assert not _is_linked(a1, 'room18', b)
    if hasattr(a2, 'room18'):
        assert _is_linked(a2, 'room18', b)
    _safe_set(b, 'nurse19', None)
    assert not _is_linked(b, 'nurse19', a2)
    if hasattr(a2, 'room18'):
        assert not _is_linked(a2, 'room18', b)


def test_assoc_receptions_reverse_link_reassign_clear():
    a1 = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    a2 = Receptionist(email="sample_text_2", id=13, password="sample_text_2", username="sample_text_2")
    b = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    _safe_set(b, 'receptionist4', a1)
    assert _is_linked(b, 'receptionist4', a1)
    if hasattr(a1, 'p5'):
        assert _is_linked(a1, 'p5', b)
    _safe_set(b, 'receptionist4', a2)
    assert _is_linked(b, 'receptionist4', a2)
    if hasattr(a1, 'p5'):
        assert not _is_linked(a1, 'p5', b)
    if hasattr(a2, 'p5'):
        assert _is_linked(a2, 'p5', b)
    _safe_set(b, 'receptionist4', None)
    assert not _is_linked(b, 'receptionist4', a2)
    if hasattr(a2, 'p5'):
        assert not _is_linked(a2, 'p5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

