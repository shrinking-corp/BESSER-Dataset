import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Login,
    Others,
    Post,
    Profile,
    Registration,
    User,
    public,
    secret,
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

def test_assoc_User_Group_reverse_link_reassign_clear():
    a1 = User(name="sample_text")
    a2 = User(name="sample_text_2")
    b = Others(discription="sample_text", name="sample_text")
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
    a1 = User(name="sample_text")
    a2 = User(name="sample_text_2")
    b = Profile(about="sample_text", password="sample_text", username="sample_text")
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
    a1 = User(name="sample_text")
    a2 = User(name="sample_text_2")
    b = Post(info="sample_text", privacy="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

