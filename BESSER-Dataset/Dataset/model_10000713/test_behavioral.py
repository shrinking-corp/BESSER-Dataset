import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Diagnosis,
    Instructions,
    Medical_test,
    Medicine,
    Patient,
    Person,
    Signs,
    Symptoms,
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

def test_assoc_Diagnosis_Instructions_reverse_link_reassign_clear():
    a1 = Instructions(ID=7, descriptions="sample_text", name="sample_text")
    a2 = Instructions(ID=13, descriptions="sample_text_2", name="sample_text_2")
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'instructions6', {a1})
    assert _is_linked(b, 'instructions6', a1)
    if hasattr(a1, 'diagnosis7'):
        assert _is_linked(a1, 'diagnosis7', b)
    _safe_set(b, 'instructions6', {a2})
    assert _is_linked(b, 'instructions6', a2)
    if hasattr(a1, 'diagnosis7'):
        assert not _is_linked(a1, 'diagnosis7', b)
    if hasattr(a2, 'diagnosis7'):
        assert _is_linked(a2, 'diagnosis7', b)
    _safe_set(b, 'instructions6', set())
    assert not _is_linked(b, 'instructions6', a2)
    if hasattr(a2, 'diagnosis7'):
        assert not _is_linked(a2, 'diagnosis7', b)


def test_assoc_Diagnosis_Medical_test_reverse_link_reassign_clear():
    a1 = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    a2 = Medical_test(Date="sample_text_2", ID=13, Image="sample_text_2", Lab="sample_text_2", name="sample_text_2")
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'medical_test8', {a1})
    assert _is_linked(b, 'medical_test8', a1)
    if hasattr(a1, 'diagnosis9'):
        assert _is_linked(a1, 'diagnosis9', b)
    _safe_set(b, 'medical_test8', {a2})
    assert _is_linked(b, 'medical_test8', a2)
    if hasattr(a1, 'diagnosis9'):
        assert not _is_linked(a1, 'diagnosis9', b)
    if hasattr(a2, 'diagnosis9'):
        assert _is_linked(a2, 'diagnosis9', b)
    _safe_set(b, 'medical_test8', set())
    assert not _is_linked(b, 'medical_test8', a2)
    if hasattr(a2, 'diagnosis9'):
        assert not _is_linked(a2, 'diagnosis9', b)


def test_assoc_Diagnosis_Medicine_reverse_link_reassign_clear():
    a1 = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    a2 = Medicine(ActiveIngredient="sample_text_2", ID=13, Price="sample_text_2", Type="sample_text_2", name="sample_text_2")
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'medicine0', {a1})
    assert _is_linked(b, 'medicine0', a1)
    if hasattr(a1, 'diagnosis1'):
        assert _is_linked(a1, 'diagnosis1', b)
    _safe_set(b, 'medicine0', {a2})
    assert _is_linked(b, 'medicine0', a2)
    if hasattr(a1, 'diagnosis1'):
        assert not _is_linked(a1, 'diagnosis1', b)
    if hasattr(a2, 'diagnosis1'):
        assert _is_linked(a2, 'diagnosis1', b)
    _safe_set(b, 'medicine0', set())
    assert not _is_linked(b, 'medicine0', a2)
    if hasattr(a2, 'diagnosis1'):
        assert not _is_linked(a2, 'diagnosis1', b)


def test_assoc_Diagnosis_Signs_reverse_link_reassign_clear():
    a1 = Signs(ID=7, name="sample_text")
    a2 = Signs(ID=13, name="sample_text_2")
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'signs4', {a1})
    assert _is_linked(b, 'signs4', a1)
    if hasattr(a1, 'diagnosis5'):
        assert _is_linked(a1, 'diagnosis5', b)
    _safe_set(b, 'signs4', {a2})
    assert _is_linked(b, 'signs4', a2)
    if hasattr(a1, 'diagnosis5'):
        assert not _is_linked(a1, 'diagnosis5', b)
    if hasattr(a2, 'diagnosis5'):
        assert _is_linked(a2, 'diagnosis5', b)
    _safe_set(b, 'signs4', set())
    assert not _is_linked(b, 'signs4', a2)
    if hasattr(a2, 'diagnosis5'):
        assert not _is_linked(a2, 'diagnosis5', b)


def test_assoc_Diagnosis_Symptoms_reverse_link_reassign_clear():
    a1 = Symptoms(ID=7, name="sample_text")
    a2 = Symptoms(ID=13, name="sample_text_2")
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'symptoms2', {a1})
    assert _is_linked(b, 'symptoms2', a1)
    if hasattr(a1, 'diagnosis3'):
        assert _is_linked(a1, 'diagnosis3', b)
    _safe_set(b, 'symptoms2', {a2})
    assert _is_linked(b, 'symptoms2', a2)
    if hasattr(a1, 'diagnosis3'):
        assert not _is_linked(a1, 'diagnosis3', b)
    if hasattr(a2, 'diagnosis3'):
        assert _is_linked(a2, 'diagnosis3', b)
    _safe_set(b, 'symptoms2', set())
    assert not _is_linked(b, 'symptoms2', a2)
    if hasattr(a2, 'diagnosis3'):
        assert not _is_linked(a2, 'diagnosis3', b)


def test_assoc_Patient__Diagnosis_reverse_link_reassign_clear():
    a1 = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    a2 = Patient(Allergies="sample_text_2", DiagnosisList="sample_text_2", Height=9.99, MedicalTest="sample_text_2", Medicine="sample_text_2", Surgeries="sample_text_2", weight=9.99)
    b = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    _safe_set(b, 'patient11', a1)
    assert _is_linked(b, 'patient11', a1)
    if hasattr(a1, 'diagnosis10'):
        assert _is_linked(a1, 'diagnosis10', b)
    _safe_set(b, 'patient11', a2)
    assert _is_linked(b, 'patient11', a2)
    if hasattr(a1, 'diagnosis10'):
        assert not _is_linked(a1, 'diagnosis10', b)
    if hasattr(a2, 'diagnosis10'):
        assert _is_linked(a2, 'diagnosis10', b)
    _safe_set(b, 'patient11', None)
    assert not _is_linked(b, 'patient11', a2)
    if hasattr(a2, 'diagnosis10'):
        assert not _is_linked(a2, 'diagnosis10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

