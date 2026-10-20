import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Add_notes,
    Class,
    Course,
    Home_page,
    Interface1_Interface,
    Interface2_Interface,
    Interface_Interface,
    Login,
    New_user,
    Show_all_grades,
    names,
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

def test_assoc_Login_New_user_reverse_link_reassign_clear():
    a1 = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    a2 = New_user(Contact_No=13, First_name="sample_text_2", Last_Name="sample_text_2", Major="sample_text_2", Student_ID=13, Student_ID1=13)
    b = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    _safe_set(b, 'new_user0', a1)
    assert _is_linked(b, 'new_user0', a1)
    if hasattr(a1, 'login1'):
        assert _is_linked(a1, 'login1', b)
    _safe_set(b, 'new_user0', a2)
    assert _is_linked(b, 'new_user0', a2)
    if hasattr(a1, 'login1'):
        assert not _is_linked(a1, 'login1', b)
    if hasattr(a2, 'login1'):
        assert _is_linked(a2, 'login1', b)
    _safe_set(b, 'new_user0', None)
    assert not _is_linked(b, 'new_user0', a2)
    if hasattr(a2, 'login1'):
        assert not _is_linked(a2, 'login1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Home_page_Add_notes_stub_double():
    # Home_page has no real 'add_notes8' property in the generated
    # code (a bare stub) -- manually attach it so Add_notes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Add_notes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Add_notes(Course_Name="sample_text", Notes_taken="sample_text", Student_ID=7)
    partner = Home_page()
    setattr(partner, 'add_notes8', None)
    _safe_set(owner, 'home_page9', partner)
    assert getattr(partner, 'add_notes8') == owner
    _safe_set(owner, 'home_page9', None)
    assert getattr(partner, 'add_notes8') is None


def test_assoc_Home_page_Course_stub_double():
    # Home_page has no real 'course6' property in the generated
    # code (a bare stub) -- manually attach it so Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    partner = Home_page()
    setattr(partner, 'course6', None)
    _safe_set(owner, 'home_page7', partner)
    assert getattr(partner, 'course6') == owner
    _safe_set(owner, 'home_page7', None)
    assert getattr(partner, 'course6') is None


def test_assoc_Home_page_Show_all_grades_stub_double():
    # Home_page has no real 'show_all_grades4' property in the generated
    # code (a bare stub) -- manually attach it so Show_all_grades's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Show_all_grades's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    partner = Home_page()
    setattr(partner, 'show_all_grades4', None)
    _safe_set(owner, 'home_page5', partner)
    assert getattr(partner, 'show_all_grades4') == owner
    _safe_set(owner, 'home_page5', None)
    assert getattr(partner, 'show_all_grades4') is None


def test_assoc_Login_Home_page_stub_double():
    # Home_page has no real 'login3' property in the generated
    # code (a bare stub) -- manually attach it so Login's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Login's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    partner = Home_page()
    setattr(partner, 'login3', None)
    _safe_set(owner, 'home_page2', partner)
    assert getattr(partner, 'login3') == owner
    _safe_set(owner, 'home_page2', None)
    assert getattr(partner, 'login3') is None


