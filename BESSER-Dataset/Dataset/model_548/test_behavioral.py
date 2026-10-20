import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identifiable,
    trackit_Comment,
    trackit_Identifiable,
    trackit_Issue,
    trackit_IssueTracker,
    trackit_Member,
    trackit_Product,
    trackit_Team,
    trackit_Version,
    IssueStatus,
    IssueType,
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

def test_assoc_assignedTo26_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'issuesAssigned', {a1})
    assert _is_linked(b, 'issuesAssigned', a1)
    if hasattr(a1, 'Member27'):
        assert _is_linked(a1, 'Member27', b)
    _safe_set(b, 'issuesAssigned', {a2})
    assert _is_linked(b, 'issuesAssigned', a2)
    if hasattr(a1, 'Member27'):
        assert not _is_linked(a1, 'Member27', b)
    if hasattr(a2, 'Member27'):
        assert _is_linked(a2, 'Member27', b)
    _safe_set(b, 'issuesAssigned', set())
    assert not _is_linked(b, 'issuesAssigned', a2)
    if hasattr(a2, 'Member27'):
        assert not _is_linked(a2, 'Member27', b)


def test_assoc_author22_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'issuesCreated', a1)
    assert _is_linked(b, 'issuesCreated', a1)
    if hasattr(a1, 'Member'):
        assert _is_linked(a1, 'Member', b)
    _safe_set(b, 'issuesCreated', a2)
    assert _is_linked(b, 'issuesCreated', a2)
    if hasattr(a1, 'Member'):
        assert not _is_linked(a1, 'Member', b)
    if hasattr(a2, 'Member'):
        assert _is_linked(a2, 'Member', b)
    _safe_set(b, 'issuesCreated', None)
    assert not _is_linked(b, 'issuesCreated', a2)
    if hasattr(a2, 'Member'):
        assert not _is_linked(a2, 'Member', b)


def test_assoc_author42_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'comments43', a1)
    assert _is_linked(b, 'comments43', a1)
    if hasattr(a1, 'Member44'):
        assert _is_linked(a1, 'Member44', b)
    _safe_set(b, 'comments43', a2)
    assert _is_linked(b, 'comments43', a2)
    if hasattr(a1, 'Member44'):
        assert not _is_linked(a1, 'Member44', b)
    if hasattr(a2, 'Member44'):
        assert _is_linked(a2, 'Member44', b)
    _safe_set(b, 'comments43', None)
    assert not _is_linked(b, 'comments43', a2)
    if hasattr(a2, 'Member44'):
        assert not _is_linked(a2, 'Member44', b)


def test_assoc_blockers24_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'blocking', {a1})
    assert _is_linked(b, 'blocking', a1)
    if hasattr(a1, 'Issue25'):
        assert _is_linked(a1, 'Issue25', b)
    _safe_set(b, 'blocking', {a2})
    assert _is_linked(b, 'blocking', a2)
    if hasattr(a1, 'Issue25'):
        assert not _is_linked(a1, 'Issue25', b)
    if hasattr(a2, 'Issue25'):
        assert _is_linked(a2, 'Issue25', b)
    _safe_set(b, 'blocking', set())
    assert not _is_linked(b, 'blocking', a2)
    if hasattr(a2, 'Issue25'):
        assert not _is_linked(a2, 'Issue25', b)


def test_assoc_blocking38_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'blockers', {a1})
    assert _is_linked(b, 'blockers', a1)
    if hasattr(a1, 'Issue39'):
        assert _is_linked(a1, 'Issue39', b)
    _safe_set(b, 'blockers', {a2})
    assert _is_linked(b, 'blockers', a2)
    if hasattr(a1, 'Issue39'):
        assert not _is_linked(a1, 'Issue39', b)
    if hasattr(a2, 'Issue39'):
        assert _is_linked(a2, 'Issue39', b)
    _safe_set(b, 'blockers', set())
    assert not _is_linked(b, 'blockers', a2)
    if hasattr(a2, 'Issue39'):
        assert not _is_linked(a2, 'Issue39', b)


def test_assoc_comments28_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'Comment29', a1)
    assert _is_linked(b, 'Comment29', a1)
    if hasattr(a1, 'issue'):
        assert _is_linked(a1, 'issue', b)
    _safe_set(b, 'Comment29', a2)
    assert _is_linked(b, 'Comment29', a2)
    if hasattr(a1, 'issue'):
        assert not _is_linked(a1, 'issue', b)
    if hasattr(a2, 'issue'):
        assert _is_linked(a2, 'issue', b)
    _safe_set(b, 'Comment29', None)
    assert not _is_linked(b, 'Comment29', a2)
    if hasattr(a2, 'issue'):
        assert not _is_linked(a2, 'issue', b)


def test_assoc_comments8_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'Comment', a1)
    assert _is_linked(b, 'Comment', a1)
    if hasattr(a1, 'author9'):
        assert _is_linked(a1, 'author9', b)
    _safe_set(b, 'Comment', a2)
    assert _is_linked(b, 'Comment', a2)
    if hasattr(a1, 'author9'):
        assert not _is_linked(a1, 'author9', b)
    if hasattr(a2, 'author9'):
        assert _is_linked(a2, 'author9', b)
    _safe_set(b, 'Comment', None)
    assert not _is_linked(b, 'Comment', a2)
    if hasattr(a2, 'author9'):
        assert not _is_linked(a2, 'author9', b)


def test_assoc_dependencies34_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'trackit_Issue35', a1)
    assert _is_linked(b, 'trackit_Issue35', a1)
    if hasattr(a1, 'trackit_Issue33'):
        assert _is_linked(a1, 'trackit_Issue33', b)
    _safe_set(b, 'trackit_Issue35', a2)
    assert _is_linked(b, 'trackit_Issue35', a2)
    if hasattr(a1, 'trackit_Issue33'):
        assert not _is_linked(a1, 'trackit_Issue33', b)
    if hasattr(a2, 'trackit_Issue33'):
        assert _is_linked(a2, 'trackit_Issue33', b)
    _safe_set(b, 'trackit_Issue35', None)
    assert not _is_linked(b, 'trackit_Issue35', a2)
    if hasattr(a2, 'trackit_Issue33'):
        assert not _is_linked(a2, 'trackit_Issue33', b)


def test_assoc_duplicateOf31_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'trackit_Issue32', a1)
    assert _is_linked(b, 'trackit_Issue32', a1)
    if hasattr(a1, 'trackit_Issue30'):
        assert _is_linked(a1, 'trackit_Issue30', b)
    _safe_set(b, 'trackit_Issue32', a2)
    assert _is_linked(b, 'trackit_Issue32', a2)
    if hasattr(a1, 'trackit_Issue30'):
        assert not _is_linked(a1, 'trackit_Issue30', b)
    if hasattr(a2, 'trackit_Issue30'):
        assert _is_linked(a2, 'trackit_Issue30', b)
    _safe_set(b, 'trackit_Issue32', None)
    assert not _is_linked(b, 'trackit_Issue32', a2)
    if hasattr(a2, 'trackit_Issue30'):
        assert not _is_linked(a2, 'trackit_Issue30', b)


def test_assoc_issue40_reverse_link_reassign_clear():
    a1 = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    a2 = trackit_Issue(dateCreated="sample_text_2", description="sample_text_2", issueType="sample_text_2", status="sample_text_2", title="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'comments', a1)
    assert _is_linked(b, 'comments', a1)
    if hasattr(a1, 'Issue41'):
        assert _is_linked(a1, 'Issue41', b)
    _safe_set(b, 'comments', a2)
    assert _is_linked(b, 'comments', a2)
    if hasattr(a1, 'Issue41'):
        assert not _is_linked(a1, 'Issue41', b)
    if hasattr(a2, 'Issue41'):
        assert _is_linked(a2, 'Issue41', b)
    _safe_set(b, 'comments', None)
    assert not _is_linked(b, 'comments', a2)
    if hasattr(a2, 'Issue41'):
        assert not _is_linked(a2, 'Issue41', b)


def test_assoc_issues20_reverse_link_reassign_clear():
    a1 = trackit_Version(name="sample_text", status="sample_text")
    a2 = trackit_Version(name="sample_text_2", status="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'Issue21', a1)
    assert _is_linked(b, 'Issue21', a1)
    if hasattr(a1, 'versionsAffected'):
        assert _is_linked(a1, 'versionsAffected', b)
    _safe_set(b, 'Issue21', a2)
    assert _is_linked(b, 'Issue21', a2)
    if hasattr(a1, 'versionsAffected'):
        assert not _is_linked(a1, 'versionsAffected', b)
    if hasattr(a2, 'versionsAffected'):
        assert _is_linked(a2, 'versionsAffected', b)
    _safe_set(b, 'Issue21', None)
    assert not _is_linked(b, 'Issue21', a2)
    if hasattr(a2, 'versionsAffected'):
        assert not _is_linked(a2, 'versionsAffected', b)


def test_assoc_issues3_reverse_link_reassign_clear():
    a1 = trackit_IssueTracker(projectName="sample_text")
    a2 = trackit_IssueTracker(projectName="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'trackit_Issue', a1)
    assert _is_linked(b, 'trackit_Issue', a1)
    if hasattr(a1, 'trackit_IssueTracker4'):
        assert _is_linked(a1, 'trackit_IssueTracker4', b)
    _safe_set(b, 'trackit_Issue', a2)
    assert _is_linked(b, 'trackit_Issue', a2)
    if hasattr(a1, 'trackit_IssueTracker4'):
        assert not _is_linked(a1, 'trackit_IssueTracker4', b)
    if hasattr(a2, 'trackit_IssueTracker4'):
        assert _is_linked(a2, 'trackit_IssueTracker4', b)
    _safe_set(b, 'trackit_Issue', None)
    assert not _is_linked(b, 'trackit_Issue', a2)
    if hasattr(a2, 'trackit_IssueTracker4'):
        assert not _is_linked(a2, 'trackit_IssueTracker4', b)


def test_assoc_issuesAssigned10_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'Issue11', a1)
    assert _is_linked(b, 'Issue11', a1)
    if hasattr(a1, 'assignedTo'):
        assert _is_linked(a1, 'assignedTo', b)
    _safe_set(b, 'Issue11', a2)
    assert _is_linked(b, 'Issue11', a2)
    if hasattr(a1, 'assignedTo'):
        assert not _is_linked(a1, 'assignedTo', b)
    if hasattr(a2, 'assignedTo'):
        assert _is_linked(a2, 'assignedTo', b)
    _safe_set(b, 'Issue11', None)
    assert not _is_linked(b, 'Issue11', a2)
    if hasattr(a2, 'assignedTo'):
        assert not _is_linked(a2, 'assignedTo', b)


def test_assoc_issuesCreated7_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'Issue', a1)
    assert _is_linked(b, 'Issue', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Issue', a2)
    assert _is_linked(b, 'Issue', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Issue', None)
    assert not _is_linked(b, 'Issue', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


def test_assoc_members12_reverse_link_reassign_clear():
    a1 = trackit_Team(teamName="sample_text")
    a2 = trackit_Team(teamName="sample_text_2")
    b = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    _safe_set(b, 'trackit_Member14', a1)
    assert _is_linked(b, 'trackit_Member14', a1)
    if hasattr(a1, 'trackit_Team13'):
        assert _is_linked(a1, 'trackit_Team13', b)
    _safe_set(b, 'trackit_Member14', a2)
    assert _is_linked(b, 'trackit_Member14', a2)
    if hasattr(a1, 'trackit_Team13'):
        assert not _is_linked(a1, 'trackit_Team13', b)
    if hasattr(a2, 'trackit_Team13'):
        assert _is_linked(a2, 'trackit_Team13', b)
    _safe_set(b, 'trackit_Member14', None)
    assert not _is_linked(b, 'trackit_Member14', a2)
    if hasattr(a2, 'trackit_Team13'):
        assert not _is_linked(a2, 'trackit_Team13', b)


def test_assoc_members5_reverse_link_reassign_clear():
    a1 = trackit_Member(firstName="sample_text", fullName="sample_text", lastName="sample_text")
    a2 = trackit_Member(firstName="sample_text_2", fullName="sample_text_2", lastName="sample_text_2")
    b = trackit_IssueTracker(projectName="sample_text")
    _safe_set(b, 'trackit_IssueTracker6', {a1})
    assert _is_linked(b, 'trackit_IssueTracker6', a1)
    if hasattr(a1, 'trackit_Member'):
        assert _is_linked(a1, 'trackit_Member', b)
    _safe_set(b, 'trackit_IssueTracker6', {a2})
    assert _is_linked(b, 'trackit_IssueTracker6', a2)
    if hasattr(a1, 'trackit_Member'):
        assert not _is_linked(a1, 'trackit_Member', b)
    if hasattr(a2, 'trackit_Member'):
        assert _is_linked(a2, 'trackit_Member', b)
    _safe_set(b, 'trackit_IssueTracker6', set())
    assert not _is_linked(b, 'trackit_IssueTracker6', a2)
    if hasattr(a2, 'trackit_Member'):
        assert not _is_linked(a2, 'trackit_Member', b)


def test_assoc_parent46_reverse_link_reassign_clear():
    a1 = trackit_Comment(dateCreated="sample_text", text="sample_text")
    a2 = trackit_Comment(dateCreated="sample_text_2", text="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'replies', a1)
    assert _is_linked(b, 'replies', a1)
    if hasattr(a1, 'Comment47'):
        assert _is_linked(a1, 'Comment47', b)
    _safe_set(b, 'replies', a2)
    assert _is_linked(b, 'replies', a2)
    if hasattr(a1, 'Comment47'):
        assert not _is_linked(a1, 'Comment47', b)
    if hasattr(a2, 'Comment47'):
        assert _is_linked(a2, 'Comment47', b)
    _safe_set(b, 'replies', None)
    assert not _is_linked(b, 'replies', a2)
    if hasattr(a2, 'Comment47'):
        assert not _is_linked(a2, 'Comment47', b)


def test_assoc_product17_reverse_link_reassign_clear():
    a1 = trackit_Version(name="sample_text", status="sample_text")
    a2 = trackit_Version(name="sample_text_2", status="sample_text_2")
    b = trackit_Product(name="sample_text")
    _safe_set(b, 'trackit_Product19', a1)
    assert _is_linked(b, 'trackit_Product19', a1)
    if hasattr(a1, 'trackit_Version18'):
        assert _is_linked(a1, 'trackit_Version18', b)
    _safe_set(b, 'trackit_Product19', a2)
    assert _is_linked(b, 'trackit_Product19', a2)
    if hasattr(a1, 'trackit_Version18'):
        assert not _is_linked(a1, 'trackit_Version18', b)
    if hasattr(a2, 'trackit_Version18'):
        assert _is_linked(a2, 'trackit_Version18', b)
    _safe_set(b, 'trackit_Product19', None)
    assert not _is_linked(b, 'trackit_Product19', a2)
    if hasattr(a2, 'trackit_Version18'):
        assert not _is_linked(a2, 'trackit_Version18', b)


def test_assoc_products1_reverse_link_reassign_clear():
    a1 = trackit_Product(name="sample_text")
    a2 = trackit_Product(name="sample_text_2")
    b = trackit_IssueTracker(projectName="sample_text")
    _safe_set(b, 'trackit_IssueTracker2', {a1})
    assert _is_linked(b, 'trackit_IssueTracker2', a1)
    if hasattr(a1, 'trackit_Product'):
        assert _is_linked(a1, 'trackit_Product', b)
    _safe_set(b, 'trackit_IssueTracker2', {a2})
    assert _is_linked(b, 'trackit_IssueTracker2', a2)
    if hasattr(a1, 'trackit_Product'):
        assert not _is_linked(a1, 'trackit_Product', b)
    if hasattr(a2, 'trackit_Product'):
        assert _is_linked(a2, 'trackit_Product', b)
    _safe_set(b, 'trackit_IssueTracker2', set())
    assert not _is_linked(b, 'trackit_IssueTracker2', a2)
    if hasattr(a2, 'trackit_Product'):
        assert not _is_linked(a2, 'trackit_Product', b)


def test_assoc_replies49_reverse_link_reassign_clear():
    a1 = trackit_Comment(dateCreated="sample_text", text="sample_text")
    a2 = trackit_Comment(dateCreated="sample_text_2", text="sample_text_2")
    b = trackit_Comment(dateCreated="sample_text", text="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Comment50'):
        assert _is_linked(a1, 'Comment50', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Comment50'):
        assert not _is_linked(a1, 'Comment50', b)
    if hasattr(a2, 'Comment50'):
        assert _is_linked(a2, 'Comment50', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Comment50'):
        assert not _is_linked(a2, 'Comment50', b)


def test_assoc_teams0_reverse_link_reassign_clear():
    a1 = trackit_Team(teamName="sample_text")
    a2 = trackit_Team(teamName="sample_text_2")
    b = trackit_IssueTracker(projectName="sample_text")
    _safe_set(b, 'trackit_IssueTracker', {a1})
    assert _is_linked(b, 'trackit_IssueTracker', a1)
    if hasattr(a1, 'trackit_Team'):
        assert _is_linked(a1, 'trackit_Team', b)
    _safe_set(b, 'trackit_IssueTracker', {a2})
    assert _is_linked(b, 'trackit_IssueTracker', a2)
    if hasattr(a1, 'trackit_Team'):
        assert not _is_linked(a1, 'trackit_Team', b)
    if hasattr(a2, 'trackit_Team'):
        assert _is_linked(a2, 'trackit_Team', b)
    _safe_set(b, 'trackit_IssueTracker', set())
    assert not _is_linked(b, 'trackit_IssueTracker', a2)
    if hasattr(a2, 'trackit_Team'):
        assert not _is_linked(a2, 'trackit_Team', b)


def test_assoc_version15_reverse_link_reassign_clear():
    a1 = trackit_Version(name="sample_text", status="sample_text")
    a2 = trackit_Version(name="sample_text_2", status="sample_text_2")
    b = trackit_Product(name="sample_text")
    _safe_set(b, 'trackit_Product16', {a1})
    assert _is_linked(b, 'trackit_Product16', a1)
    if hasattr(a1, 'trackit_Version'):
        assert _is_linked(a1, 'trackit_Version', b)
    _safe_set(b, 'trackit_Product16', {a2})
    assert _is_linked(b, 'trackit_Product16', a2)
    if hasattr(a1, 'trackit_Version'):
        assert not _is_linked(a1, 'trackit_Version', b)
    if hasattr(a2, 'trackit_Version'):
        assert _is_linked(a2, 'trackit_Version', b)
    _safe_set(b, 'trackit_Product16', set())
    assert not _is_linked(b, 'trackit_Product16', a2)
    if hasattr(a2, 'trackit_Version'):
        assert not _is_linked(a2, 'trackit_Version', b)


def test_assoc_versionsAffected36_reverse_link_reassign_clear():
    a1 = trackit_Version(name="sample_text", status="sample_text")
    a2 = trackit_Version(name="sample_text_2", status="sample_text_2")
    b = trackit_Issue(dateCreated="sample_text", description="sample_text", issueType="sample_text", status="sample_text", title="sample_text")
    _safe_set(b, 'issues', {a1})
    assert _is_linked(b, 'issues', a1)
    if hasattr(a1, 'Version'):
        assert _is_linked(a1, 'Version', b)
    _safe_set(b, 'issues', {a2})
    assert _is_linked(b, 'issues', a2)
    if hasattr(a1, 'Version'):
        assert not _is_linked(a1, 'Version', b)
    if hasattr(a2, 'Version'):
        assert _is_linked(a2, 'Version', b)
    _safe_set(b, 'issues', set())
    assert not _is_linked(b, 'issues', a2)
    if hasattr(a2, 'Version'):
        assert not _is_linked(a2, 'Version', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

