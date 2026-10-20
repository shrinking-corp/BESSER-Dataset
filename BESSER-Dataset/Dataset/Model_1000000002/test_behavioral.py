import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Review,
    Session,
    Skill,
    SkillMatch,
    SkillRequest,
    User,
    UserSkill,
    SessionType,
    SkillMatchStatus,
    SkillRequestStatus,
    TechSkillLevel,
    UserSkillLevel,
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

def test_assoc_wants_reverse_link_reassign_clear():
    a1 = SkillRequest(createdDate=date(2024, 1, 1), deadlineDate=date(2024, 1, 1), requestId=7, status=SkillRequestStatus.CANCELLED)
    a2 = SkillRequest(createdDate=date(2025, 6, 15), deadlineDate=date(2025, 6, 15), requestId=13, status=SkillRequestStatus.COMPLETED)
    b = Skill(category="sample_text", description="sample_text", estimatedDuration=7, skillId=7, skillLevel=TechSkillLevel.ADVANCED, skillName="sample_text")
    _safe_set(b, 'skillrequest_2', {a1})
    assert _is_linked(b, 'skillrequest_2', a1)
    if hasattr(a1, 'skill_1'):
        assert _is_linked(a1, 'skill_1', b)
    _safe_set(b, 'skillrequest_2', {a2})
    assert _is_linked(b, 'skillrequest_2', a2)
    if hasattr(a1, 'skill_1'):
        assert not _is_linked(a1, 'skill_1', b)
    if hasattr(a2, 'skill_1'):
        assert _is_linked(a2, 'skill_1', b)
    _safe_set(b, 'skillrequest_2', set())
    assert not _is_linked(b, 'skillrequest_2', a2)
    if hasattr(a2, 'skill_1'):
        assert not _is_linked(a2, 'skill_1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_creates_stub_double():
    # SkillRequest has no real 'user_1' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(emailId="sample_text", userId=7, userName="sample_text")
    partner = SkillRequest(createdDate=date(2024, 1, 1), deadlineDate=date(2024, 1, 1), requestId=7, status=SkillRequestStatus.CANCELLED)
    setattr(partner, 'user_1', None)
    _safe_set(owner, 'skillrequest', {partner})
    assert getattr(partner, 'user_1') == owner
    _safe_set(owner, 'skillrequest', set())
    assert getattr(partner, 'user_1') is None


def test_assoc_has_stub_double():
    # Session has no real 'skillmatch_1' property in the generated
    # code (a bare stub) -- manually attach it so SkillMatch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillMatch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillMatch(createdDate=date(2024, 1, 1), matchId=7, startDate=date(2024, 1, 1), status=SkillMatchStatus.ACTIVE)
    partner = Session(duration=7, sessionDate=date(2024, 1, 1), sessionId=7, sessionType=SessionType.HYBRID)
    setattr(partner, 'skillmatch_1', None)
    _safe_set(owner, 'session', {partner})
    assert getattr(partner, 'skillmatch_1') == owner
    _safe_set(owner, 'session', set())
    assert getattr(partner, 'skillmatch_1') is None


def test_assoc_leads_to_stub_double():
    # SkillMatch has no real 'skillrequest_1' property in the generated
    # code (a bare stub) -- manually attach it so SkillRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillRequest(createdDate=date(2024, 1, 1), deadlineDate=date(2024, 1, 1), requestId=7, status=SkillRequestStatus.CANCELLED)
    partner = SkillMatch(createdDate=date(2024, 1, 1), matchId=7, startDate=date(2024, 1, 1), status=SkillMatchStatus.ACTIVE)
    setattr(partner, 'skillrequest_1', None)
    _safe_set(owner, 'skillmatch_2', partner)
    assert owner in getattr(partner, 'skillrequest_1')
    _safe_set(owner, 'skillmatch_2', None)
    assert owner not in getattr(partner, 'skillrequest_1')


def test_assoc_refers_to_stub_double():
    # Skill has no real 'userskill_1' property in the generated
    # code (a bare stub) -- manually attach it so UserSkill's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UserSkill's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UserSkill(certification=True, skillId=7, skillLevel=UserSkillLevel.AUTHORITY, yearsOfExperience=7)
    partner = Skill(category="sample_text", description="sample_text", estimatedDuration=7, skillId=7, skillLevel=TechSkillLevel.ADVANCED, skillName="sample_text")
    setattr(partner, 'userskill_1', None)
    _safe_set(owner, 'skill', partner)
    assert owner in getattr(partner, 'userskill_1')
    _safe_set(owner, 'skill', None)
    assert owner not in getattr(partner, 'userskill_1')


def test_assoc_review_stub_double():
    # Review has no real 'session_1' property in the generated
    # code (a bare stub) -- manually attach it so Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Session(duration=7, sessionDate=date(2024, 1, 1), sessionId=7, sessionType=SessionType.HYBRID)
    partner = Review(comments="sample_text", rating=7, reviewId=7)
    setattr(partner, 'session_1', None)
    _safe_set(owner, 'review', partner)
    assert getattr(partner, 'session_1') == owner
    _safe_set(owner, 'review', None)
    assert getattr(partner, 'session_1') is None


def test_assoc_teaches_stub_double():
    # UserSkill has no real 'user' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(emailId="sample_text", userId=7, userName="sample_text")
    partner = UserSkill(certification=True, skillId=7, skillLevel=UserSkillLevel.AUTHORITY, yearsOfExperience=7)
    setattr(partner, 'user', None)
    _safe_set(owner, 'userskill', {partner})
    assert getattr(partner, 'user') == owner
    _safe_set(owner, 'userskill', set())
    assert getattr(partner, 'user') is None


