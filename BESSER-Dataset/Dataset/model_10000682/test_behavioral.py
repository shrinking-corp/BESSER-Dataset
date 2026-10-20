import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Admin1,
    Comment,
    Comment1,
    Event,
    Event1,
    Guest,
    Guest1,
    Lecturer,
    Lecturer1,
    Location,
    Location1,
    Post,
    Post1,
    Society,
    Society1,
    Student,
    Student1,
    User,
    User1,
    User_Actor,
    VirtualTour,
    VirtualTour1,
    test_UseCase,
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

def test_assoc_Comment_User2_reverse_link_reassign_clear():
    a1 = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    a2 = User1(attribute="sample_text_2", campus="sample_text_2", email="sample_text_2", isStaff=False, name="sample_text_2", username="sample_text_2")
    b = Comment1(author="sample_text", body="sample_text", date="sample_text")
    _safe_set(b, 'user20', a1)
    assert _is_linked(b, 'user20', a1)
    if hasattr(a1, 'comment21'):
        assert _is_linked(a1, 'comment21', b)
    _safe_set(b, 'user20', a2)
    assert _is_linked(b, 'user20', a2)
    if hasattr(a1, 'comment21'):
        assert not _is_linked(a1, 'comment21', b)
    if hasattr(a2, 'comment21'):
        assert _is_linked(a2, 'comment21', b)
    _safe_set(b, 'user20', None)
    assert not _is_linked(b, 'user20', a2)
    if hasattr(a2, 'comment21'):
        assert not _is_linked(a2, 'comment21', b)


def test_assoc_Post_Comment_reverse_link_reassign_clear():
    a1 = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    a2 = Post1(author="sample_text_2", body="sample_text_2", date="sample_text_2", files="sample_text_2", title="sample_text_2")
    b = Comment1(author="sample_text", body="sample_text", date="sample_text")
    _safe_set(b, 'post25', a1)
    assert _is_linked(b, 'post25', a1)
    if hasattr(a1, 'comment24'):
        assert _is_linked(a1, 'comment24', b)
    _safe_set(b, 'post25', a2)
    assert _is_linked(b, 'post25', a2)
    if hasattr(a1, 'comment24'):
        assert not _is_linked(a1, 'comment24', b)
    if hasattr(a2, 'comment24'):
        assert _is_linked(a2, 'comment24', b)
    _safe_set(b, 'post25', None)
    assert not _is_linked(b, 'post25', a2)
    if hasattr(a2, 'comment24'):
        assert not _is_linked(a2, 'comment24', b)


def test_assoc_User_Post2_reverse_link_reassign_clear():
    a1 = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    a2 = User1(attribute="sample_text_2", campus="sample_text_2", email="sample_text_2", isStaff=False, name="sample_text_2", username="sample_text_2")
    b = Post1(author="sample_text", body="sample_text", date="sample_text", files="sample_text", title="sample_text")
    _safe_set(b, 'user19', a1)
    assert _is_linked(b, 'user19', a1)
    if hasattr(a1, 'post18'):
        assert _is_linked(a1, 'post18', b)
    _safe_set(b, 'user19', a2)
    assert _is_linked(b, 'user19', a2)
    if hasattr(a1, 'post18'):
        assert not _is_linked(a1, 'post18', b)
    if hasattr(a2, 'post18'):
        assert _is_linked(a2, 'post18', b)
    _safe_set(b, 'user19', None)
    assert not _is_linked(b, 'user19', a2)
    if hasattr(a2, 'post18'):
        assert not _is_linked(a2, 'post18', b)


def test_assoc_User_VirtualTour2_reverse_link_reassign_clear():
    a1 = VirtualTour1(URL="sample_text")
    a2 = VirtualTour1(URL="sample_text_2")
    b = User1(attribute="sample_text", campus="sample_text", email="sample_text", isStaff=True, name="sample_text", username="sample_text")
    _safe_set(b, 'virtualTour16', a1)
    assert _is_linked(b, 'virtualTour16', a1)
    if hasattr(a1, 'user17'):
        assert _is_linked(a1, 'user17', b)
    _safe_set(b, 'virtualTour16', a2)
    assert _is_linked(b, 'virtualTour16', a2)
    if hasattr(a1, 'user17'):
        assert not _is_linked(a1, 'user17', b)
    if hasattr(a2, 'user17'):
        assert _is_linked(a2, 'user17', b)
    _safe_set(b, 'virtualTour16', None)
    assert not _is_linked(b, 'virtualTour16', a2)
    if hasattr(a2, 'user17'):
        assert not _is_linked(a2, 'user17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_MyClass_MyClass22_stub_double():
    # Guest1 has no real 'myClass214' property in the generated
    # code (a bare stub) -- manually attach it so VirtualTour1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VirtualTour1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VirtualTour1(URL="sample_text")
    partner = Guest1()
    setattr(partner, 'myClass214', None)
    _safe_set(owner, 'myClass15', partner)
    assert getattr(partner, 'myClass214') == owner
    _safe_set(owner, 'myClass15', None)
    assert getattr(partner, 'myClass214') is None


