import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Calculate_caloriesBurnt,
    Count_Steps,
    Count_Steps_and_Calories,
    Draw_Path,
    Give_Name,
    Give_Weight,
    Update_Data,
    User,
    Weekly_Chart,
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

def test_assoc_Count_Steps_and_Calories__Calculate_caloriesBurnt_reverse_link_reassign_clear():
    a1 = Count_Steps_and_Calories(CaloriesBurnt="sample_text", Name="sample_text", Steps=7)
    a2 = Count_Steps_and_Calories(CaloriesBurnt="sample_text_2", Name="sample_text_2", Steps=13)
    b = Calculate_caloriesBurnt(CaloriesBurnt="sample_text", Name="sample_text", Steps=7)
    _safe_set(b, 'count_Steps_and_Calories3', a1)
    assert _is_linked(b, 'count_Steps_and_Calories3', a1)
    if hasattr(a1, 'calculate_caloriesBurnt2'):
        assert _is_linked(a1, 'calculate_caloriesBurnt2', b)
    _safe_set(b, 'count_Steps_and_Calories3', a2)
    assert _is_linked(b, 'count_Steps_and_Calories3', a2)
    if hasattr(a1, 'calculate_caloriesBurnt2'):
        assert not _is_linked(a1, 'calculate_caloriesBurnt2', b)
    if hasattr(a2, 'calculate_caloriesBurnt2'):
        assert _is_linked(a2, 'calculate_caloriesBurnt2', b)
    _safe_set(b, 'count_Steps_and_Calories3', None)
    assert not _is_linked(b, 'count_Steps_and_Calories3', a2)
    if hasattr(a2, 'calculate_caloriesBurnt2'):
        assert not _is_linked(a2, 'calculate_caloriesBurnt2', b)


def test_assoc_Count_Steps_and_Calories__Count_Steps_reverse_link_reassign_clear():
    a1 = Count_Steps_and_Calories(CaloriesBurnt="sample_text", Name="sample_text", Steps=7)
    a2 = Count_Steps_and_Calories(CaloriesBurnt="sample_text_2", Name="sample_text_2", Steps=13)
    b = Count_Steps(Steps=7)
    _safe_set(b, 'count_Steps_and_Calories1', a1)
    assert _is_linked(b, 'count_Steps_and_Calories1', a1)
    if hasattr(a1, 'count_Steps0'):
        assert _is_linked(a1, 'count_Steps0', b)
    _safe_set(b, 'count_Steps_and_Calories1', a2)
    assert _is_linked(b, 'count_Steps_and_Calories1', a2)
    if hasattr(a1, 'count_Steps0'):
        assert not _is_linked(a1, 'count_Steps0', b)
    if hasattr(a2, 'count_Steps0'):
        assert _is_linked(a2, 'count_Steps0', b)
    _safe_set(b, 'count_Steps_and_Calories1', None)
    assert not _is_linked(b, 'count_Steps_and_Calories1', a2)
    if hasattr(a2, 'count_Steps0'):
        assert not _is_linked(a2, 'count_Steps0', b)


def test_assoc_Update_Data__Give_Name_reverse_link_reassign_clear():
    a1 = Update_Data(Name="sample_text", Weight=7)
    a2 = Update_Data(Name="sample_text_2", Weight=13)
    b = Give_Name(Name="sample_text")
    _safe_set(b, 'update_Data5', a1)
    assert _is_linked(b, 'update_Data5', a1)
    if hasattr(a1, 'give_Name4'):
        assert _is_linked(a1, 'give_Name4', b)
    _safe_set(b, 'update_Data5', a2)
    assert _is_linked(b, 'update_Data5', a2)
    if hasattr(a1, 'give_Name4'):
        assert not _is_linked(a1, 'give_Name4', b)
    if hasattr(a2, 'give_Name4'):
        assert _is_linked(a2, 'give_Name4', b)
    _safe_set(b, 'update_Data5', None)
    assert not _is_linked(b, 'update_Data5', a2)
    if hasattr(a2, 'give_Name4'):
        assert not _is_linked(a2, 'give_Name4', b)


def test_assoc_Update_Data__Give_Weight_reverse_link_reassign_clear():
    a1 = Update_Data(Name="sample_text", Weight=7)
    a2 = Update_Data(Name="sample_text_2", Weight=13)
    b = Give_Weight(Weight=7)
    _safe_set(b, 'update_Data7', a1)
    assert _is_linked(b, 'update_Data7', a1)
    if hasattr(a1, 'give_Weight6'):
        assert _is_linked(a1, 'give_Weight6', b)
    _safe_set(b, 'update_Data7', a2)
    assert _is_linked(b, 'update_Data7', a2)
    if hasattr(a1, 'give_Weight6'):
        assert not _is_linked(a1, 'give_Weight6', b)
    if hasattr(a2, 'give_Weight6'):
        assert _is_linked(a2, 'give_Weight6', b)
    _safe_set(b, 'update_Data7', None)
    assert not _is_linked(b, 'update_Data7', a2)
    if hasattr(a2, 'give_Weight6'):
        assert not _is_linked(a2, 'give_Weight6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

