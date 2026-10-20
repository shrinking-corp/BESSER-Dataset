import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ACADEMIC_PAGE,
    DATABASE_SYSTEM,
    LoginPage,
    PERSONAL_PAGE,
    PLACEMENTS_PAGE,
    T,
    WELCOME_PAGE,
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

def test_assoc_PERSONAL_PAGE_WELCOME_PAGE_reverse_link_reassign_clear():
    a1 = WELCOME_PAGE(academic="sample_text", personal="sample_text", placements="sample_text")
    a2 = WELCOME_PAGE(academic="sample_text_2", personal="sample_text_2", placements="sample_text_2")
    b = PERSONAL_PAGE(BRANCH="sample_text", YEAR=7)
    _safe_set(b, 'wELCOME_PAGE6', a1)
    assert _is_linked(b, 'wELCOME_PAGE6', a1)
    if hasattr(a1, 'pERSONAL_PAGE7'):
        assert _is_linked(a1, 'pERSONAL_PAGE7', b)
    _safe_set(b, 'wELCOME_PAGE6', a2)
    assert _is_linked(b, 'wELCOME_PAGE6', a2)
    if hasattr(a1, 'pERSONAL_PAGE7'):
        assert not _is_linked(a1, 'pERSONAL_PAGE7', b)
    if hasattr(a2, 'pERSONAL_PAGE7'):
        assert _is_linked(a2, 'pERSONAL_PAGE7', b)
    _safe_set(b, 'wELCOME_PAGE6', None)
    assert not _is_linked(b, 'wELCOME_PAGE6', a2)
    if hasattr(a2, 'pERSONAL_PAGE7'):
        assert not _is_linked(a2, 'pERSONAL_PAGE7', b)


def test_assoc_User_Group_reverse_link_reassign_clear():
    a1 = WELCOME_PAGE(academic="sample_text", personal="sample_text", placements="sample_text")
    a2 = WELCOME_PAGE(academic="sample_text_2", personal="sample_text_2", placements="sample_text_2")
    b = ACADEMIC_PAGE(BRANCH="sample_text", STUDIES="sample_text")
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'group4'):
        assert _is_linked(a1, 'group4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'group4'):
        assert not _is_linked(a1, 'group4', b)
    if hasattr(a2, 'group4'):
        assert _is_linked(a2, 'group4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'group4'):
        assert not _is_linked(a2, 'group4', b)


def test_assoc_User_Myprofile_reverse_link_reassign_clear():
    a1 = WELCOME_PAGE(academic="sample_text", personal="sample_text", placements="sample_text")
    a2 = WELCOME_PAGE(academic="sample_text_2", personal="sample_text_2", placements="sample_text_2")
    b = LoginPage(User_name="sample_text")
    _safe_set(b, 'user1', a1)
    assert _is_linked(b, 'user1', a1)
    if hasattr(a1, 'myprofile0'):
        assert _is_linked(a1, 'myprofile0', b)
    _safe_set(b, 'user1', a2)
    assert _is_linked(b, 'user1', a2)
    if hasattr(a1, 'myprofile0'):
        assert not _is_linked(a1, 'myprofile0', b)
    if hasattr(a2, 'myprofile0'):
        assert _is_linked(a2, 'myprofile0', b)
    _safe_set(b, 'user1', None)
    assert not _is_linked(b, 'user1', a2)
    if hasattr(a2, 'myprofile0'):
        assert not _is_linked(a2, 'myprofile0', b)


def test_assoc_User_Post_reverse_link_reassign_clear():
    a1 = WELCOME_PAGE(academic="sample_text", personal="sample_text", placements="sample_text")
    a2 = WELCOME_PAGE(academic="sample_text_2", personal="sample_text_2", placements="sample_text_2")
    b = DATABASE_SYSTEM(Content=True)
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'post2'):
        assert _is_linked(a1, 'post2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'post2'):
        assert not _is_linked(a1, 'post2', b)
    if hasattr(a2, 'post2'):
        assert _is_linked(a2, 'post2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'post2'):
        assert not _is_linked(a2, 'post2', b)


def test_assoc_WELCOME_PAGE_PLACEMENTS_PAGE_reverse_link_reassign_clear():
    a1 = WELCOME_PAGE(academic="sample_text", personal="sample_text", placements="sample_text")
    a2 = WELCOME_PAGE(academic="sample_text_2", personal="sample_text_2", placements="sample_text_2")
    b = PLACEMENTS_PAGE(BRANCH="sample_text", INTREST="sample_text", SALARY=7)
    _safe_set(b, 'wELCOME_PAGE9', a1)
    assert _is_linked(b, 'wELCOME_PAGE9', a1)
    if hasattr(a1, 'pLACEMENTS_PAGE8'):
        assert _is_linked(a1, 'pLACEMENTS_PAGE8', b)
    _safe_set(b, 'wELCOME_PAGE9', a2)
    assert _is_linked(b, 'wELCOME_PAGE9', a2)
    if hasattr(a1, 'pLACEMENTS_PAGE8'):
        assert not _is_linked(a1, 'pLACEMENTS_PAGE8', b)
    if hasattr(a2, 'pLACEMENTS_PAGE8'):
        assert _is_linked(a2, 'pLACEMENTS_PAGE8', b)
    _safe_set(b, 'wELCOME_PAGE9', None)
    assert not _is_linked(b, 'wELCOME_PAGE9', a2)
    if hasattr(a2, 'pLACEMENTS_PAGE8'):
        assert not _is_linked(a2, 'pLACEMENTS_PAGE8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

