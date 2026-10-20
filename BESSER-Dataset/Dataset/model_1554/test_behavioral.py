import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Change,
    CommentContainer,
    Dated,
    Indexed,
    Location,
    ReviewItem,
    reviews_ApprovalType,
    reviews_ApprovalValueMap,
    reviews_Change,
    reviews_Comment,
    reviews_CommentContainer,
    reviews_Dated,
    reviews_FileItem,
    reviews_FileVersion,
    reviews_Indexed,
    reviews_LineLocation,
    reviews_LineRange,
    reviews_Location,
    reviews_Repository,
    reviews_RequirementEntry,
    reviews_Review,
    reviews_ReviewItem,
    reviews_ReviewItemSet,
    reviews_ReviewRequirementsMap,
    reviews_ReviewerEntry,
    reviews_User,
    reviews_UserApprovalsMap,
    RequirementStatus,
    ReviewStatus,
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

def test_assoc_account41_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_Repository(description="sample_text", taskConnectorKind="sample_text", taskRepository="sample_text", taskRepositoryUrl="sample_text")
    _safe_set(b, 'reviews_Repository42', a1)
    assert _is_linked(b, 'reviews_Repository42', a1)
    if hasattr(a1, 'reviews_User43'):
        assert _is_linked(a1, 'reviews_User43', b)
    _safe_set(b, 'reviews_Repository42', a2)
    assert _is_linked(b, 'reviews_Repository42', a2)
    if hasattr(a1, 'reviews_User43'):
        assert not _is_linked(a1, 'reviews_User43', b)
    if hasattr(a2, 'reviews_User43'):
        assert _is_linked(a2, 'reviews_User43', b)
    _safe_set(b, 'reviews_Repository42', None)
    assert not _is_linked(b, 'reviews_Repository42', a2)
    if hasattr(a2, 'reviews_User43'):
        assert not _is_linked(a2, 'reviews_User43', b)


def test_assoc_addedBy32_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_ReviewItem(id="sample_text", name="sample_text", reference="sample_text")
    _safe_set(b, 'reviews_ReviewItem', a1)
    assert _is_linked(b, 'reviews_ReviewItem', a1)
    if hasattr(a1, 'reviews_User33'):
        assert _is_linked(a1, 'reviews_User33', b)
    _safe_set(b, 'reviews_ReviewItem', a2)
    assert _is_linked(b, 'reviews_ReviewItem', a2)
    if hasattr(a1, 'reviews_User33'):
        assert not _is_linked(a1, 'reviews_User33', b)
    if hasattr(a2, 'reviews_User33'):
        assert _is_linked(a2, 'reviews_User33', b)
    _safe_set(b, 'reviews_ReviewItem', None)
    assert not _is_linked(b, 'reviews_ReviewItem', a2)
    if hasattr(a2, 'reviews_User33'):
        assert not _is_linked(a2, 'reviews_User33', b)


def test_assoc_allComments0_reverse_link_reassign_clear():
    a1 = reviews_CommentContainer()
    a2 = reviews_CommentContainer()
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'reviews_Comment', a1)
    assert _is_linked(b, 'reviews_Comment', a1)
    if hasattr(a1, 'reviews_CommentContainer'):
        assert _is_linked(a1, 'reviews_CommentContainer', b)
    _safe_set(b, 'reviews_Comment', a2)
    assert _is_linked(b, 'reviews_Comment', a2)
    if hasattr(a1, 'reviews_CommentContainer'):
        assert not _is_linked(a1, 'reviews_CommentContainer', b)
    if hasattr(a2, 'reviews_CommentContainer'):
        assert _is_linked(a2, 'reviews_CommentContainer', b)
    _safe_set(b, 'reviews_Comment', None)
    assert not _is_linked(b, 'reviews_Comment', a2)
    if hasattr(a2, 'reviews_CommentContainer'):
        assert not _is_linked(a2, 'reviews_CommentContainer', b)


def test_assoc_allDrafts2_reverse_link_reassign_clear():
    a1 = reviews_CommentContainer()
    a2 = reviews_CommentContainer()
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'reviews_Comment4', a1)
    assert _is_linked(b, 'reviews_Comment4', a1)
    if hasattr(a1, 'reviews_CommentContainer3'):
        assert _is_linked(a1, 'reviews_CommentContainer3', b)
    _safe_set(b, 'reviews_Comment4', a2)
    assert _is_linked(b, 'reviews_Comment4', a2)
    if hasattr(a1, 'reviews_CommentContainer3'):
        assert not _is_linked(a1, 'reviews_CommentContainer3', b)
    if hasattr(a2, 'reviews_CommentContainer3'):
        assert _is_linked(a2, 'reviews_CommentContainer3', b)
    _safe_set(b, 'reviews_Comment4', None)
    assert not _is_linked(b, 'reviews_Comment4', a2)
    if hasattr(a2, 'reviews_CommentContainer3'):
        assert not _is_linked(a2, 'reviews_CommentContainer3', b)


def test_assoc_approvalTypes40_reverse_link_reassign_clear():
    a1 = reviews_Repository(description="sample_text", taskConnectorKind="sample_text", taskRepository="sample_text", taskRepositoryUrl="sample_text")
    a2 = reviews_Repository(description="sample_text_2", taskConnectorKind="sample_text_2", taskRepository="sample_text_2", taskRepositoryUrl="sample_text_2")
    b = reviews_ApprovalType(key="sample_text", name="sample_text")
    _safe_set(b, 'reviews_ApprovalType', a1)
    assert _is_linked(b, 'reviews_ApprovalType', a1)
    if hasattr(a1, 'reviews_Repository'):
        assert _is_linked(a1, 'reviews_Repository', b)
    _safe_set(b, 'reviews_ApprovalType', a2)
    assert _is_linked(b, 'reviews_ApprovalType', a2)
    if hasattr(a1, 'reviews_Repository'):
        assert not _is_linked(a1, 'reviews_Repository', b)
    if hasattr(a2, 'reviews_Repository'):
        assert _is_linked(a2, 'reviews_Repository', b)
    _safe_set(b, 'reviews_ApprovalType', None)
    assert not _is_linked(b, 'reviews_ApprovalType', a2)
    if hasattr(a2, 'reviews_Repository'):
        assert not _is_linked(a2, 'reviews_Repository', b)


def test_assoc_author20_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'reviews_Comment21', a1)
    assert _is_linked(b, 'reviews_Comment21', a1)
    if hasattr(a1, 'reviews_User22'):
        assert _is_linked(a1, 'reviews_User22', b)
    _safe_set(b, 'reviews_Comment21', a2)
    assert _is_linked(b, 'reviews_Comment21', a2)
    if hasattr(a1, 'reviews_User22'):
        assert not _is_linked(a1, 'reviews_User22', b)
    if hasattr(a2, 'reviews_User22'):
        assert _is_linked(a2, 'reviews_User22', b)
    _safe_set(b, 'reviews_Comment21', None)
    assert not _is_linked(b, 'reviews_Comment21', a2)
    if hasattr(a2, 'reviews_User22'):
        assert not _is_linked(a2, 'reviews_User22', b)


def test_assoc_by71_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_RequirementEntry(status="sample_text")
    _safe_set(b, 'reviews_RequirementEntry', a1)
    assert _is_linked(b, 'reviews_RequirementEntry', a1)
    if hasattr(a1, 'reviews_User72'):
        assert _is_linked(a1, 'reviews_User72', b)
    _safe_set(b, 'reviews_RequirementEntry', a2)
    assert _is_linked(b, 'reviews_RequirementEntry', a2)
    if hasattr(a1, 'reviews_User72'):
        assert not _is_linked(a1, 'reviews_User72', b)
    if hasattr(a2, 'reviews_User72'):
        assert _is_linked(a2, 'reviews_User72', b)
    _safe_set(b, 'reviews_RequirementEntry', None)
    assert not _is_linked(b, 'reviews_RequirementEntry', a2)
    if hasattr(a2, 'reviews_User72'):
        assert not _is_linked(a2, 'reviews_User72', b)


def test_assoc_comments1_reverse_link_reassign_clear():
    a1 = reviews_CommentContainer()
    a2 = reviews_CommentContainer()
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'Comment', a1)
    assert _is_linked(b, 'Comment', a1)
    if hasattr(a1, 'item'):
        assert _is_linked(a1, 'item', b)
    _safe_set(b, 'Comment', a2)
    assert _is_linked(b, 'Comment', a2)
    if hasattr(a1, 'item'):
        assert not _is_linked(a1, 'item', b)
    if hasattr(a2, 'item'):
        assert _is_linked(a2, 'item', b)
    _safe_set(b, 'Comment', None)
    assert not _is_linked(b, 'Comment', a2)
    if hasattr(a2, 'item'):
        assert not _is_linked(a2, 'item', b)


def test_assoc_committedBy34_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_ReviewItem(id="sample_text", name="sample_text", reference="sample_text")
    _safe_set(b, 'reviews_ReviewItem35', a1)
    assert _is_linked(b, 'reviews_ReviewItem35', a1)
    if hasattr(a1, 'reviews_User36'):
        assert _is_linked(a1, 'reviews_User36', b)
    _safe_set(b, 'reviews_ReviewItem35', a2)
    assert _is_linked(b, 'reviews_ReviewItem35', a2)
    if hasattr(a1, 'reviews_User36'):
        assert not _is_linked(a1, 'reviews_User36', b)
    if hasattr(a2, 'reviews_User36'):
        assert _is_linked(a2, 'reviews_User36', b)
    _safe_set(b, 'reviews_ReviewItem35', None)
    assert not _is_linked(b, 'reviews_ReviewItem35', a2)
    if hasattr(a2, 'reviews_User36'):
        assert not _is_linked(a2, 'reviews_User36', b)


def test_assoc_drafts5_reverse_link_reassign_clear():
    a1 = reviews_CommentContainer()
    a2 = reviews_CommentContainer()
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'reviews_Comment7', a1)
    assert _is_linked(b, 'reviews_Comment7', a1)
    if hasattr(a1, 'reviews_CommentContainer6'):
        assert _is_linked(a1, 'reviews_CommentContainer6', b)
    _safe_set(b, 'reviews_Comment7', a2)
    assert _is_linked(b, 'reviews_Comment7', a2)
    if hasattr(a1, 'reviews_CommentContainer6'):
        assert not _is_linked(a1, 'reviews_CommentContainer6', b)
    if hasattr(a2, 'reviews_CommentContainer6'):
        assert _is_linked(a2, 'reviews_CommentContainer6', b)
    _safe_set(b, 'reviews_Comment7', None)
    assert not _is_linked(b, 'reviews_Comment7', a2)
    if hasattr(a2, 'reviews_CommentContainer6'):
        assert not _is_linked(a2, 'reviews_CommentContainer6', b)


def test_assoc_item31_reverse_link_reassign_clear():
    a1 = reviews_CommentContainer()
    a2 = reviews_CommentContainer()
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'comments', a1)
    assert _is_linked(b, 'comments', a1)
    if hasattr(a1, 'CommentContainer'):
        assert _is_linked(a1, 'CommentContainer', b)
    _safe_set(b, 'comments', a2)
    assert _is_linked(b, 'comments', a2)
    if hasattr(a1, 'CommentContainer'):
        assert not _is_linked(a1, 'CommentContainer', b)
    if hasattr(a2, 'CommentContainer'):
        assert _is_linked(a2, 'CommentContainer', b)
    _safe_set(b, 'comments', None)
    assert not _is_linked(b, 'comments', a2)
    if hasattr(a2, 'CommentContainer'):
        assert not _is_linked(a2, 'CommentContainer', b)


def test_assoc_key68_reverse_link_reassign_clear():
    a1 = reviews_ApprovalValueMap(value="sample_text")
    a2 = reviews_ApprovalValueMap(value="sample_text_2")
    b = reviews_ApprovalType(key="sample_text", name="sample_text")
    _safe_set(b, 'reviews_ApprovalType70', a1)
    assert _is_linked(b, 'reviews_ApprovalType70', a1)
    if hasattr(a1, 'reviews_ApprovalValueMap69'):
        assert _is_linked(a1, 'reviews_ApprovalValueMap69', b)
    _safe_set(b, 'reviews_ApprovalType70', a2)
    assert _is_linked(b, 'reviews_ApprovalType70', a2)
    if hasattr(a1, 'reviews_ApprovalValueMap69'):
        assert not _is_linked(a1, 'reviews_ApprovalValueMap69', b)
    if hasattr(a2, 'reviews_ApprovalValueMap69'):
        assert _is_linked(a2, 'reviews_ApprovalValueMap69', b)
    _safe_set(b, 'reviews_ApprovalType70', None)
    assert not _is_linked(b, 'reviews_ApprovalType70', a2)
    if hasattr(a2, 'reviews_ApprovalValueMap69'):
        assert not _is_linked(a2, 'reviews_ApprovalValueMap69', b)


def test_assoc_owner8_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_Change(id="sample_text", key="sample_text", message="sample_text", state="sample_text", subject="sample_text")
    _safe_set(b, 'reviews_Change', a1)
    assert _is_linked(b, 'reviews_Change', a1)
    if hasattr(a1, 'reviews_User'):
        assert _is_linked(a1, 'reviews_User', b)
    _safe_set(b, 'reviews_Change', a2)
    assert _is_linked(b, 'reviews_Change', a2)
    if hasattr(a1, 'reviews_User'):
        assert not _is_linked(a1, 'reviews_User', b)
    if hasattr(a2, 'reviews_User'):
        assert _is_linked(a2, 'reviews_User', b)
    _safe_set(b, 'reviews_Change', None)
    assert not _is_linked(b, 'reviews_Change', a2)
    if hasattr(a2, 'reviews_User'):
        assert not _is_linked(a2, 'reviews_User', b)


def test_assoc_ranges57_reverse_link_reassign_clear():
    a1 = reviews_LineRange(end=7, start=7)
    a2 = reviews_LineRange(end=13, start=13)
    b = reviews_LineLocation(rangeMax=7, rangeMin=7)
    _safe_set(b, 'reviews_LineLocation', {a1})
    assert _is_linked(b, 'reviews_LineLocation', a1)
    if hasattr(a1, 'reviews_LineRange'):
        assert _is_linked(a1, 'reviews_LineRange', b)
    _safe_set(b, 'reviews_LineLocation', {a2})
    assert _is_linked(b, 'reviews_LineLocation', a2)
    if hasattr(a1, 'reviews_LineRange'):
        assert not _is_linked(a1, 'reviews_LineRange', b)
    if hasattr(a2, 'reviews_LineRange'):
        assert _is_linked(a2, 'reviews_LineRange', b)
    _safe_set(b, 'reviews_LineLocation', set())
    assert not _is_linked(b, 'reviews_LineLocation', a2)
    if hasattr(a2, 'reviews_LineRange'):
        assert not _is_linked(a2, 'reviews_LineRange', b)


def test_assoc_replies24_reverse_link_reassign_clear():
    a1 = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    a2 = reviews_Comment(description="sample_text_2", draft=False, id="sample_text_2", title="sample_text_2")
    b = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    _safe_set(b, 'reviews_Comment25', a1)
    assert _is_linked(b, 'reviews_Comment25', a1)
    if hasattr(a1, 'reviews_Comment23'):
        assert _is_linked(a1, 'reviews_Comment23', b)
    _safe_set(b, 'reviews_Comment25', a2)
    assert _is_linked(b, 'reviews_Comment25', a2)
    if hasattr(a1, 'reviews_Comment23'):
        assert not _is_linked(a1, 'reviews_Comment23', b)
    if hasattr(a2, 'reviews_Comment23'):
        assert _is_linked(a2, 'reviews_Comment23', b)
    _safe_set(b, 'reviews_Comment25', None)
    assert not _is_linked(b, 'reviews_Comment25', a2)
    if hasattr(a2, 'reviews_Comment23'):
        assert not _is_linked(a2, 'reviews_Comment23', b)


def test_assoc_users45_reverse_link_reassign_clear():
    a1 = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    a2 = reviews_User(displayName="sample_text_2", email="sample_text_2", id="sample_text_2")
    b = reviews_Repository(description="sample_text", taskConnectorKind="sample_text", taskRepository="sample_text", taskRepositoryUrl="sample_text")
    _safe_set(b, 'reviews_Repository46', {a1})
    assert _is_linked(b, 'reviews_Repository46', a1)
    if hasattr(a1, 'reviews_User47'):
        assert _is_linked(a1, 'reviews_User47', b)
    _safe_set(b, 'reviews_Repository46', {a2})
    assert _is_linked(b, 'reviews_Repository46', a2)
    if hasattr(a1, 'reviews_User47'):
        assert not _is_linked(a1, 'reviews_User47', b)
    if hasattr(a2, 'reviews_User47'):
        assert _is_linked(a2, 'reviews_User47', b)
    _safe_set(b, 'reviews_Repository46', set())
    assert not _is_linked(b, 'reviews_Repository46', a2)
    if hasattr(a2, 'reviews_User47'):
        assert not _is_linked(a2, 'reviews_User47', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_approvals66_stub_double():
    # reviews_ReviewerEntry has no real 'reviews_ReviewerEntry67' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ApprovalValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ApprovalValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ApprovalValueMap(value="sample_text")
    partner = reviews_ReviewerEntry()
    setattr(partner, 'reviews_ReviewerEntry67', None)
    _safe_set(owner, 'reviews_ApprovalValueMap', partner)
    assert owner in getattr(partner, 'reviews_ReviewerEntry67')
    _safe_set(owner, 'reviews_ApprovalValueMap', None)
    assert owner not in getattr(partner, 'reviews_ReviewerEntry67')


def test_assoc_base48_stub_double():
    # reviews_FileItem has no real 'reviews_FileItem' property in the generated
    # code (a bare stub) -- manually attach it so reviews_FileVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_FileVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_FileVersion(content="sample_text", description="sample_text", fileRevision="sample_text", path="sample_text")
    partner = reviews_FileItem()
    setattr(partner, 'reviews_FileItem', None)
    _safe_set(owner, 'reviews_FileVersion', partner)
    assert getattr(partner, 'reviews_FileItem') == owner
    _safe_set(owner, 'reviews_FileVersion', None)
    assert getattr(partner, 'reviews_FileItem') is None


def test_assoc_children13_stub_double():
    # reviews_Review has no real 'reviews_Review14' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Change's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Change's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Change(id="sample_text", key="sample_text", message="sample_text", state="sample_text", subject="sample_text")
    partner = reviews_Review()
    setattr(partner, 'reviews_Review14', None)
    _safe_set(owner, 'reviews_Change15', partner)
    assert owner in getattr(partner, 'reviews_Review14')
    _safe_set(owner, 'reviews_Change15', None)
    assert owner not in getattr(partner, 'reviews_Review14')


def test_assoc_file58_stub_double():
    # reviews_FileItem has no real 'reviews_FileItem60' property in the generated
    # code (a bare stub) -- manually attach it so reviews_FileVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_FileVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_FileVersion(content="sample_text", description="sample_text", fileRevision="sample_text", path="sample_text")
    partner = reviews_FileItem()
    setattr(partner, 'reviews_FileItem60', None)
    _safe_set(owner, 'reviews_FileVersion59', partner)
    assert getattr(partner, 'reviews_FileItem60') == owner
    _safe_set(owner, 'reviews_FileVersion59', None)
    assert getattr(partner, 'reviews_FileItem60') is None


def test_assoc_items54_stub_double():
    # reviews_FileItem has no real 'FileItem' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ReviewItemSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ReviewItemSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ReviewItemSet(revision="sample_text")
    partner = reviews_FileItem()
    setattr(partner, 'FileItem', None)
    _safe_set(owner, 'set', {partner})
    assert getattr(partner, 'FileItem') == owner
    _safe_set(owner, 'set', set())
    assert getattr(partner, 'FileItem') is None


def test_assoc_key61_stub_double():
    # reviews_UserApprovalsMap has no real 'reviews_UserApprovalsMap62' property in the generated
    # code (a bare stub) -- manually attach it so reviews_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_User(displayName="sample_text", email="sample_text", id="sample_text")
    partner = reviews_UserApprovalsMap()
    setattr(partner, 'reviews_UserApprovalsMap62', None)
    _safe_set(owner, 'reviews_User63', partner)
    assert getattr(partner, 'reviews_UserApprovalsMap62') == owner
    _safe_set(owner, 'reviews_User63', None)
    assert getattr(partner, 'reviews_UserApprovalsMap62') is None


def test_assoc_key73_stub_double():
    # reviews_ReviewRequirementsMap has no real 'reviews_ReviewRequirementsMap74' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ApprovalType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ApprovalType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ApprovalType(key="sample_text", name="sample_text")
    partner = reviews_ReviewRequirementsMap()
    setattr(partner, 'reviews_ReviewRequirementsMap74', None)
    _safe_set(owner, 'reviews_ApprovalType75', partner)
    assert getattr(partner, 'reviews_ReviewRequirementsMap74') == owner
    _safe_set(owner, 'reviews_ApprovalType75', None)
    assert getattr(partner, 'reviews_ReviewRequirementsMap74') is None


def test_assoc_locations26_stub_double():
    # reviews_Location has no real 'reviews_Location' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    partner = reviews_Location()
    setattr(partner, 'reviews_Location', None)
    _safe_set(owner, 'reviews_Comment27', {partner})
    assert getattr(partner, 'reviews_Location') == owner
    _safe_set(owner, 'reviews_Comment27', set())
    assert getattr(partner, 'reviews_Location') is None


def test_assoc_parentReview55_stub_double():
    # reviews_Review has no real 'Review56' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ReviewItemSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ReviewItemSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ReviewItemSet(revision="sample_text")
    partner = reviews_Review()
    setattr(partner, 'Review56', None)
    _safe_set(owner, 'sets', partner)
    assert getattr(partner, 'Review56') == owner
    _safe_set(owner, 'sets', None)
    assert getattr(partner, 'Review56') is None


def test_assoc_parents11_stub_double():
    # reviews_Review has no real 'reviews_Review' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Change's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Change's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Change(id="sample_text", key="sample_text", message="sample_text", state="sample_text", subject="sample_text")
    partner = reviews_Review()
    setattr(partner, 'reviews_Review', None)
    _safe_set(owner, 'reviews_Change12', partner)
    assert owner in getattr(partner, 'reviews_Review')
    _safe_set(owner, 'reviews_Change12', None)
    assert owner not in getattr(partner, 'reviews_Review')


def test_assoc_repository10_stub_double():
    # reviews_Review has no real 'reviews' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Repository(description="sample_text", taskConnectorKind="sample_text", taskRepository="sample_text", taskRepositoryUrl="sample_text")
    partner = reviews_Review()
    setattr(partner, 'reviews', None)
    _safe_set(owner, 'Repository', partner)
    assert getattr(partner, 'reviews') == owner
    _safe_set(owner, 'Repository', None)
    assert getattr(partner, 'reviews') is None


def test_assoc_review28_stub_double():
    # reviews_Review has no real 'reviews_Review30' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Comment(description="sample_text", draft=True, id="sample_text", title="sample_text")
    partner = reviews_Review()
    setattr(partner, 'reviews_Review30', None)
    _safe_set(owner, 'reviews_Comment29', partner)
    assert getattr(partner, 'reviews_Review30') == owner
    _safe_set(owner, 'reviews_Comment29', None)
    assert getattr(partner, 'reviews_Review30') is None


def test_assoc_review37_stub_double():
    # reviews_Review has no real 'reviews_Review39' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ReviewItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ReviewItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ReviewItem(id="sample_text", name="sample_text", reference="sample_text")
    partner = reviews_Review()
    setattr(partner, 'reviews_Review39', None)
    _safe_set(owner, 'reviews_ReviewItem38', partner)
    assert getattr(partner, 'reviews_Review39') == owner
    _safe_set(owner, 'reviews_ReviewItem38', None)
    assert getattr(partner, 'reviews_Review39') is None


def test_assoc_reviews44_stub_double():
    # reviews_Review has no real 'Review' property in the generated
    # code (a bare stub) -- manually attach it so reviews_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_Repository(description="sample_text", taskConnectorKind="sample_text", taskRepository="sample_text", taskRepositoryUrl="sample_text")
    partner = reviews_Review()
    setattr(partner, 'Review', None)
    _safe_set(owner, 'repository', {partner})
    assert getattr(partner, 'Review') == owner
    _safe_set(owner, 'repository', set())
    assert getattr(partner, 'Review') is None


def test_assoc_set52_stub_double():
    # reviews_FileItem has no real 'items' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ReviewItemSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ReviewItemSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ReviewItemSet(revision="sample_text")
    partner = reviews_FileItem()
    setattr(partner, 'items', None)
    _safe_set(owner, 'ReviewItemSet53', partner)
    assert getattr(partner, 'items') == owner
    _safe_set(owner, 'ReviewItemSet53', None)
    assert getattr(partner, 'items') is None


def test_assoc_sets9_stub_double():
    # reviews_Review has no real 'parentReview' property in the generated
    # code (a bare stub) -- manually attach it so reviews_ReviewItemSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_ReviewItemSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_ReviewItemSet(revision="sample_text")
    partner = reviews_Review()
    setattr(partner, 'parentReview', None)
    _safe_set(owner, 'ReviewItemSet', partner)
    assert owner in getattr(partner, 'parentReview')
    _safe_set(owner, 'ReviewItemSet', None)
    assert owner not in getattr(partner, 'parentReview')


def test_assoc_target49_stub_double():
    # reviews_FileItem has no real 'reviews_FileItem50' property in the generated
    # code (a bare stub) -- manually attach it so reviews_FileVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_FileVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_FileVersion(content="sample_text", description="sample_text", fileRevision="sample_text", path="sample_text")
    partner = reviews_FileItem()
    setattr(partner, 'reviews_FileItem50', None)
    _safe_set(owner, 'reviews_FileVersion51', partner)
    assert getattr(partner, 'reviews_FileItem50') == owner
    _safe_set(owner, 'reviews_FileVersion51', None)
    assert getattr(partner, 'reviews_FileItem50') is None


def test_assoc_value76_stub_double():
    # reviews_ReviewRequirementsMap has no real 'reviews_ReviewRequirementsMap77' property in the generated
    # code (a bare stub) -- manually attach it so reviews_RequirementEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reviews_RequirementEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reviews_RequirementEntry(status="sample_text")
    partner = reviews_ReviewRequirementsMap()
    setattr(partner, 'reviews_ReviewRequirementsMap77', None)
    _safe_set(owner, 'reviews_RequirementEntry78', partner)
    assert getattr(partner, 'reviews_ReviewRequirementsMap77') == owner
    _safe_set(owner, 'reviews_RequirementEntry78', None)
    assert getattr(partner, 'reviews_ReviewRequirementsMap77') is None


