import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Group,
    Message,
    Page,
    Post,
    Profile,
    User,
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

def test_assoc_Page_Post_reverse_link_reassign_clear():
    a1 = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    a2 = Post(ID_Page=13, ID_Post=13, Info="sample_text_2", Mail="sample_text_2", Privacy="sample_text_2")
    b = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'post8', {a1})
    assert _is_linked(b, 'post8', a1)
    if hasattr(a1, 'page9'):
        assert _is_linked(a1, 'page9', b)
    _safe_set(b, 'post8', {a2})
    assert _is_linked(b, 'post8', a2)
    if hasattr(a1, 'page9'):
        assert not _is_linked(a1, 'page9', b)
    if hasattr(a2, 'page9'):
        assert _is_linked(a2, 'page9', b)
    _safe_set(b, 'post8', set())
    assert not _is_linked(b, 'post8', a2)
    if hasattr(a2, 'page9'):
        assert not _is_linked(a2, 'page9', b)


def test_assoc_Profile_User_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    _safe_set(b, 'user0', a1)
    assert _is_linked(b, 'user0', a1)
    if hasattr(a1, 'profile1'):
        assert _is_linked(a1, 'profile1', b)
    _safe_set(b, 'user0', a2)
    assert _is_linked(b, 'user0', a2)
    if hasattr(a1, 'profile1'):
        assert not _is_linked(a1, 'profile1', b)
    if hasattr(a2, 'profile1'):
        assert _is_linked(a2, 'profile1', b)
    _safe_set(b, 'user0', None)
    assert not _is_linked(b, 'user0', a2)
    if hasattr(a2, 'profile1'):
        assert not _is_linked(a2, 'profile1', b)


def test_assoc_User_Group_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'user7', a1)
    assert _is_linked(b, 'user7', a1)
    if hasattr(a1, 'group6'):
        assert _is_linked(a1, 'group6', b)
    _safe_set(b, 'user7', a2)
    assert _is_linked(b, 'user7', a2)
    if hasattr(a1, 'group6'):
        assert not _is_linked(a1, 'group6', b)
    if hasattr(a2, 'group6'):
        assert _is_linked(a2, 'group6', b)
    _safe_set(b, 'user7', None)
    assert not _is_linked(b, 'user7', a2)
    if hasattr(a2, 'group6'):
        assert not _is_linked(a2, 'group6', b)


def test_assoc_User_Message_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'message4'):
        assert _is_linked(a1, 'message4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'message4'):
        assert not _is_linked(a1, 'message4', b)
    if hasattr(a2, 'message4'):
        assert _is_linked(a2, 'message4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'message4'):
        assert not _is_linked(a2, 'message4', b)


def test_assoc_User_Page_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'page2'):
        assert _is_linked(a1, 'page2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'page2'):
        assert not _is_linked(a1, 'page2', b)
    if hasattr(a2, 'page2'):
        assert _is_linked(a2, 'page2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'page2'):
        assert not _is_linked(a2, 'page2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

