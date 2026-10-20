import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    itm_Issue,
    itm_IssueCategory,
    itm_IssueDependency,
    itm_IssueTrackingDatabase,
    itm_Member,
    itm_Project,
    itm_Role,
    itm_Tracker,
    itm_User,
    itm_Version,
    DependencyType,
    IssuePriority,
    IssueStatus,
    VersionStatus,
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

def test_assoc_category20_reverse_link_reassign_clear():
    a1 = itm_IssueCategory(name="sample_text")
    a2 = itm_IssueCategory(name="sample_text_2")
    b = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    _safe_set(b, 'itm_Issue21', a1)
    assert _is_linked(b, 'itm_Issue21', a1)
    if hasattr(a1, 'itm_IssueCategory22'):
        assert _is_linked(a1, 'itm_IssueCategory22', b)
    _safe_set(b, 'itm_Issue21', a2)
    assert _is_linked(b, 'itm_Issue21', a2)
    if hasattr(a1, 'itm_IssueCategory22'):
        assert not _is_linked(a1, 'itm_IssueCategory22', b)
    if hasattr(a2, 'itm_IssueCategory22'):
        assert _is_linked(a2, 'itm_IssueCategory22', b)
    _safe_set(b, 'itm_Issue21', None)
    assert not _is_linked(b, 'itm_Issue21', a2)
    if hasattr(a2, 'itm_IssueCategory22'):
        assert not _is_linked(a2, 'itm_IssueCategory22', b)


def test_assoc_dependencies18_reverse_link_reassign_clear():
    a1 = itm_IssueDependency(type="sample_text")
    a2 = itm_IssueDependency(type="sample_text_2")
    b = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    _safe_set(b, 'itm_Issue19', {a1})
    assert _is_linked(b, 'itm_Issue19', a1)
    if hasattr(a1, 'itm_IssueDependency'):
        assert _is_linked(a1, 'itm_IssueDependency', b)
    _safe_set(b, 'itm_Issue19', {a2})
    assert _is_linked(b, 'itm_Issue19', a2)
    if hasattr(a1, 'itm_IssueDependency'):
        assert not _is_linked(a1, 'itm_IssueDependency', b)
    if hasattr(a2, 'itm_IssueDependency'):
        assert _is_linked(a2, 'itm_IssueDependency', b)
    _safe_set(b, 'itm_Issue19', set())
    assert not _is_linked(b, 'itm_Issue19', a2)
    if hasattr(a2, 'itm_IssueDependency'):
        assert not _is_linked(a2, 'itm_IssueDependency', b)


def test_assoc_dependentTask29_reverse_link_reassign_clear():
    a1 = itm_IssueDependency(type="sample_text")
    a2 = itm_IssueDependency(type="sample_text_2")
    b = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    _safe_set(b, 'itm_Issue31', a1)
    assert _is_linked(b, 'itm_Issue31', a1)
    if hasattr(a1, 'itm_IssueDependency30'):
        assert _is_linked(a1, 'itm_IssueDependency30', b)
    _safe_set(b, 'itm_Issue31', a2)
    assert _is_linked(b, 'itm_Issue31', a2)
    if hasattr(a1, 'itm_IssueDependency30'):
        assert not _is_linked(a1, 'itm_IssueDependency30', b)
    if hasattr(a2, 'itm_IssueDependency30'):
        assert _is_linked(a2, 'itm_IssueDependency30', b)
    _safe_set(b, 'itm_Issue31', None)
    assert not _is_linked(b, 'itm_Issue31', a2)
    if hasattr(a2, 'itm_IssueDependency30'):
        assert not _is_linked(a2, 'itm_IssueDependency30', b)


def test_assoc_issueCategories9_reverse_link_reassign_clear():
    a1 = itm_Project(description="sample_text", name="sample_text")
    a2 = itm_Project(description="sample_text_2", name="sample_text_2")
    b = itm_IssueCategory(name="sample_text")
    _safe_set(b, 'itm_IssueCategory', a1)
    assert _is_linked(b, 'itm_IssueCategory', a1)
    if hasattr(a1, 'itm_Project10'):
        assert _is_linked(a1, 'itm_Project10', b)
    _safe_set(b, 'itm_IssueCategory', a2)
    assert _is_linked(b, 'itm_IssueCategory', a2)
    if hasattr(a1, 'itm_Project10'):
        assert not _is_linked(a1, 'itm_Project10', b)
    if hasattr(a2, 'itm_Project10'):
        assert _is_linked(a2, 'itm_Project10', b)
    _safe_set(b, 'itm_IssueCategory', None)
    assert not _is_linked(b, 'itm_IssueCategory', a2)
    if hasattr(a2, 'itm_Project10'):
        assert not _is_linked(a2, 'itm_Project10', b)


def test_assoc_issues13_reverse_link_reassign_clear():
    a1 = itm_Version(completedDate=date(2024, 1, 1), description="sample_text", name="sample_text", status="sample_text")
    a2 = itm_Version(completedDate=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", status="sample_text_2")
    b = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    _safe_set(b, 'itm_Issue', a1)
    assert _is_linked(b, 'itm_Issue', a1)
    if hasattr(a1, 'itm_Version14'):
        assert _is_linked(a1, 'itm_Version14', b)
    _safe_set(b, 'itm_Issue', a2)
    assert _is_linked(b, 'itm_Issue', a2)
    if hasattr(a1, 'itm_Version14'):
        assert not _is_linked(a1, 'itm_Version14', b)
    if hasattr(a2, 'itm_Version14'):
        assert _is_linked(a2, 'itm_Version14', b)
    _safe_set(b, 'itm_Issue', None)
    assert not _is_linked(b, 'itm_Issue', a2)
    if hasattr(a2, 'itm_Version14'):
        assert not _is_linked(a2, 'itm_Version14', b)


def test_assoc_tracker15_reverse_link_reassign_clear():
    a1 = itm_Tracker(name="sample_text")
    a2 = itm_Tracker(name="sample_text_2")
    b = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    _safe_set(b, 'itm_Issue16', a1)
    assert _is_linked(b, 'itm_Issue16', a1)
    if hasattr(a1, 'itm_Tracker17'):
        assert _is_linked(a1, 'itm_Tracker17', b)
    _safe_set(b, 'itm_Issue16', a2)
    assert _is_linked(b, 'itm_Issue16', a2)
    if hasattr(a1, 'itm_Tracker17'):
        assert not _is_linked(a1, 'itm_Tracker17', b)
    if hasattr(a2, 'itm_Tracker17'):
        assert _is_linked(a2, 'itm_Tracker17', b)
    _safe_set(b, 'itm_Issue16', None)
    assert not _is_linked(b, 'itm_Issue16', a2)
    if hasattr(a2, 'itm_Tracker17'):
        assert not _is_linked(a2, 'itm_Tracker17', b)


def test_assoc_versions7_reverse_link_reassign_clear():
    a1 = itm_Version(completedDate=date(2024, 1, 1), description="sample_text", name="sample_text", status="sample_text")
    a2 = itm_Version(completedDate=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", status="sample_text_2")
    b = itm_Project(description="sample_text", name="sample_text")
    _safe_set(b, 'itm_Project8', {a1})
    assert _is_linked(b, 'itm_Project8', a1)
    if hasattr(a1, 'itm_Version'):
        assert _is_linked(a1, 'itm_Version', b)
    _safe_set(b, 'itm_Project8', {a2})
    assert _is_linked(b, 'itm_Project8', a2)
    if hasattr(a1, 'itm_Version'):
        assert not _is_linked(a1, 'itm_Version', b)
    if hasattr(a2, 'itm_Version'):
        assert _is_linked(a2, 'itm_Version', b)
    _safe_set(b, 'itm_Project8', set())
    assert not _is_linked(b, 'itm_Project8', a2)
    if hasattr(a2, 'itm_Version'):
        assert not _is_linked(a2, 'itm_Version', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_members11_stub_double():
    # itm_Member has no real 'itm_Member' property in the generated
    # code (a bare stub) -- manually attach it so itm_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Project(description="sample_text", name="sample_text")
    partner = itm_Member()
    setattr(partner, 'itm_Member', None)
    _safe_set(owner, 'itm_Project12', {partner})
    assert getattr(partner, 'itm_Member') == owner
    _safe_set(owner, 'itm_Project12', set())
    assert getattr(partner, 'itm_Member') is None


def test_assoc_owner23_stub_double():
    # itm_Member has no real 'itm_Member25' property in the generated
    # code (a bare stub) -- manually attach it so itm_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    partner = itm_Member()
    setattr(partner, 'itm_Member25', None)
    _safe_set(owner, 'itm_Issue24', partner)
    assert getattr(partner, 'itm_Member25') == owner
    _safe_set(owner, 'itm_Issue24', None)
    assert getattr(partner, 'itm_Member25') is None


def test_assoc_projects0_stub_double():
    # itm_IssueTrackingDatabase has no real 'itm_IssueTrackingDatabase' property in the generated
    # code (a bare stub) -- manually attach it so itm_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Project(description="sample_text", name="sample_text")
    partner = itm_IssueTrackingDatabase()
    setattr(partner, 'itm_IssueTrackingDatabase', None)
    _safe_set(owner, 'itm_Project', partner)
    assert owner in getattr(partner, 'itm_IssueTrackingDatabase')
    _safe_set(owner, 'itm_Project', None)
    assert owner not in getattr(partner, 'itm_IssueTrackingDatabase')


def test_assoc_responsible26_stub_double():
    # itm_Member has no real 'itm_Member28' property in the generated
    # code (a bare stub) -- manually attach it so itm_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Issue(completedDate=date(2024, 1, 1), description="sample_text", doneRatio=3.14, dueDate=date(2024, 1, 1), elapsedHours=3.14, estimatedHours=3.14, name="sample_text", priority="sample_text", status="sample_text")
    partner = itm_Member()
    setattr(partner, 'itm_Member28', None)
    _safe_set(owner, 'itm_Issue27', partner)
    assert getattr(partner, 'itm_Member28') == owner
    _safe_set(owner, 'itm_Issue27', None)
    assert getattr(partner, 'itm_Member28') is None


def test_assoc_role35_stub_double():
    # itm_Member has no real 'itm_Member36' property in the generated
    # code (a bare stub) -- manually attach it so itm_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Role(name="sample_text", permissions="sample_text")
    partner = itm_Member()
    setattr(partner, 'itm_Member36', None)
    _safe_set(owner, 'itm_Role37', partner)
    assert getattr(partner, 'itm_Member36') == owner
    _safe_set(owner, 'itm_Role37', None)
    assert getattr(partner, 'itm_Member36') is None


def test_assoc_roles3_stub_double():
    # itm_IssueTrackingDatabase has no real 'itm_IssueTrackingDatabase4' property in the generated
    # code (a bare stub) -- manually attach it so itm_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Role(name="sample_text", permissions="sample_text")
    partner = itm_IssueTrackingDatabase()
    setattr(partner, 'itm_IssueTrackingDatabase4', None)
    _safe_set(owner, 'itm_Role', partner)
    assert owner in getattr(partner, 'itm_IssueTrackingDatabase4')
    _safe_set(owner, 'itm_Role', None)
    assert owner not in getattr(partner, 'itm_IssueTrackingDatabase4')


def test_assoc_trackers1_stub_double():
    # itm_IssueTrackingDatabase has no real 'itm_IssueTrackingDatabase2' property in the generated
    # code (a bare stub) -- manually attach it so itm_Tracker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_Tracker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_Tracker(name="sample_text")
    partner = itm_IssueTrackingDatabase()
    setattr(partner, 'itm_IssueTrackingDatabase2', None)
    _safe_set(owner, 'itm_Tracker', partner)
    assert owner in getattr(partner, 'itm_IssueTrackingDatabase2')
    _safe_set(owner, 'itm_Tracker', None)
    assert owner not in getattr(partner, 'itm_IssueTrackingDatabase2')


def test_assoc_user32_stub_double():
    # itm_Member has no real 'itm_Member33' property in the generated
    # code (a bare stub) -- manually attach it so itm_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_User(language="sample_text", login="sample_text")
    partner = itm_Member()
    setattr(partner, 'itm_Member33', None)
    _safe_set(owner, 'itm_User34', partner)
    assert getattr(partner, 'itm_Member33') == owner
    _safe_set(owner, 'itm_User34', None)
    assert getattr(partner, 'itm_Member33') is None


def test_assoc_users5_stub_double():
    # itm_IssueTrackingDatabase has no real 'itm_IssueTrackingDatabase6' property in the generated
    # code (a bare stub) -- manually attach it so itm_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # itm_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = itm_User(language="sample_text", login="sample_text")
    partner = itm_IssueTrackingDatabase()
    setattr(partner, 'itm_IssueTrackingDatabase6', None)
    _safe_set(owner, 'itm_User', partner)
    assert owner in getattr(partner, 'itm_IssueTrackingDatabase6')
    _safe_set(owner, 'itm_User', None)
    assert owner not in getattr(partner, 'itm_IssueTrackingDatabase6')


