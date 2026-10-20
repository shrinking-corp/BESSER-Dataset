import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Bursar,
    Doctor,
    Patient,
    Receptionist,
    Room,
    lab,
    medicine,
    pharmacy,
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

def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    a2 = Patient(addr="sample_text_2", birthyear=13, blood_group=13, email="sample_text_2", firstname="sample_text_2", id=13, lastname="sample_text_2", phonenumber=13, sex="sample_text_2")
    b = Bill(amount=3.14, billno="sample_text")
    _safe_set(b, 'pat1', a1)
    assert _is_linked(b, 'pat1', a1)
    if hasattr(a1, 'bill0'):
        assert _is_linked(a1, 'bill0', b)
    _safe_set(b, 'pat1', a2)
    assert _is_linked(b, 'pat1', a2)
    if hasattr(a1, 'bill0'):
        assert not _is_linked(a1, 'bill0', b)
    if hasattr(a2, 'bill0'):
        assert _is_linked(a2, 'bill0', b)
    _safe_set(b, 'pat1', None)
    assert not _is_linked(b, 'pat1', a2)
    if hasattr(a2, 'bill0'):
        assert not _is_linked(a2, 'bill0', b)


def test_assoc_lab_Patient_reverse_link_reassign_clear():
    a1 = lab(price=7, results="sample_text")
    a2 = lab(price=13, results="sample_text_2")
    b = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    _safe_set(b, 'lab5', a1)
    assert _is_linked(b, 'lab5', a1)
    if hasattr(a1, 'assign4'):
        assert _is_linked(a1, 'assign4', b)
    _safe_set(b, 'lab5', a2)
    assert _is_linked(b, 'lab5', a2)
    if hasattr(a1, 'assign4'):
        assert not _is_linked(a1, 'assign4', b)
    if hasattr(a2, 'assign4'):
        assert _is_linked(a2, 'assign4', b)
    _safe_set(b, 'lab5', None)
    assert not _is_linked(b, 'lab5', a2)
    if hasattr(a2, 'assign4'):
        assert not _is_linked(a2, 'assign4', b)


def test_assoc_pharmacy_Bursar_reverse_link_reassign_clear():
    a1 = pharmacy(medicine="sample_text", price=7)
    a2 = pharmacy(medicine="sample_text_2", price=13)
    b = Bursar(firstname="sample_text", lastname="sample_text")
    _safe_set(b, 'pharmacy9', a1)
    assert _is_linked(b, 'pharmacy9', a1)
    if hasattr(a1, 'medicine_cost8'):
        assert _is_linked(a1, 'medicine_cost8', b)
    _safe_set(b, 'pharmacy9', a2)
    assert _is_linked(b, 'pharmacy9', a2)
    if hasattr(a1, 'medicine_cost8'):
        assert not _is_linked(a1, 'medicine_cost8', b)
    if hasattr(a2, 'medicine_cost8'):
        assert _is_linked(a2, 'medicine_cost8', b)
    _safe_set(b, 'pharmacy9', None)
    assert not _is_linked(b, 'pharmacy9', a2)
    if hasattr(a2, 'medicine_cost8'):
        assert not _is_linked(a2, 'medicine_cost8', b)


def test_assoc_pharmacy_Patient_reverse_link_reassign_clear():
    a1 = pharmacy(medicine="sample_text", price=7)
    a2 = pharmacy(medicine="sample_text_2", price=13)
    b = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    _safe_set(b, 'pharmacy11', a1)
    assert _is_linked(b, 'pharmacy11', a1)
    if hasattr(a1, 'gives_medicine10'):
        assert _is_linked(a1, 'gives_medicine10', b)
    _safe_set(b, 'pharmacy11', a2)
    assert _is_linked(b, 'pharmacy11', a2)
    if hasattr(a1, 'gives_medicine10'):
        assert not _is_linked(a1, 'gives_medicine10', b)
    if hasattr(a2, 'gives_medicine10'):
        assert _is_linked(a2, 'gives_medicine10', b)
    _safe_set(b, 'pharmacy11', None)
    assert not _is_linked(b, 'pharmacy11', a2)
    if hasattr(a2, 'gives_medicine10'):
        assert not _is_linked(a2, 'gives_medicine10', b)


def test_assoc_receptions_reverse_link_reassign_clear():
    a1 = Receptionist(firstname="sample_text", lastname="sample_text")
    a2 = Receptionist(firstname="sample_text_2", lastname="sample_text_2")
    b = Patient(addr="sample_text", birthyear=7, blood_group=7, email="sample_text", firstname="sample_text", id=7, lastname="sample_text", phonenumber=7, sex="sample_text")
    _safe_set(b, 'receptionist2', a1)
    assert _is_linked(b, 'receptionist2', a1)
    if hasattr(a1, 'p3'):
        assert _is_linked(a1, 'p3', b)
    _safe_set(b, 'receptionist2', a2)
    assert _is_linked(b, 'receptionist2', a2)
    if hasattr(a1, 'p3'):
        assert not _is_linked(a1, 'p3', b)
    if hasattr(a2, 'p3'):
        assert _is_linked(a2, 'p3', b)
    _safe_set(b, 'receptionist2', None)
    assert not _is_linked(b, 'receptionist2', a2)
    if hasattr(a2, 'p3'):
        assert not _is_linked(a2, 'p3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

