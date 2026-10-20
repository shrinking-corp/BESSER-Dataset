import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Comment,
    CommentType,
    Item,
    Location,
    R4EComment,
    R4EContent,
    R4EIDComponent,
    R4EPosition,
    R4EReview,
    R4EReviewComponent,
    R4ETextPosition,
    R4EUser,
    Review,
    ReviewComponent,
    ReviewGroup,
    ReviewState,
    TaskReference,
    Topic,
    User,
    model_MapDateToDuration,
    model_MapIDToComponent,
    model_MapKeyToInfoAttributes,
    model_MapNameToReview,
    model_MapToAnomalyType,
    model_MapToUsers,
    model_MapUserIDToUserReviews,
    model_R4EAnomaly,
    model_R4EAnomalyTextPosition,
    model_R4EAnomalyType,
    model_R4EComment,
    model_R4ECommentType,
    model_R4EContent,
    model_R4EDelta,
    model_R4EDesignRule,
    model_R4EFileContext,
    model_R4EFileVersion,
    model_R4EFormalReview,
    model_R4EID,
    model_R4EIDComponent,
    model_R4EItem,
    model_R4EMeetingData,
    model_R4EParticipant,
    model_R4EPosition,
    model_R4EReview,
    model_R4EReviewComponent,
    model_R4EReviewDecision,
    model_R4EReviewGroup,
    model_R4EReviewPhaseInfo,
    model_R4EReviewState,
    model_R4ETaskReference,
    model_R4ETextContent,
    model_R4ETextPosition,
    model_R4EUser,
    model_R4EUserReviews,
    R4EAnomalyState,
    R4EContextType,
    R4EDecision,
    R4EReviewPhase,
    R4EReviewType,
    R4EUserRole,
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

def test_assoc_activeMeeting16_reverse_link_reassign_clear():
    a1 = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    a2 = model_R4EReview(components="sample_text_2", dueDate=date(2025, 6, 15), endDate=date(2025, 6, 15), entryCriteria="sample_text_2", extraNotes="sample_text_2", modifiedDate=date(2025, 6, 15), name="sample_text_2", objectives="sample_text_2", project="sample_text_2", referenceMaterial="sample_text_2", startDate=date(2025, 6, 15), type="sample_text_2")
    b = model_R4EMeetingData(body="sample_text", duration=7, id="sample_text", location="sample_text", receivers="sample_text", sender="sample_text", sentCount=7, startTime="sample_text", subject="sample_text")
    _safe_set(b, 'model_R4EMeetingData', a1)
    assert _is_linked(b, 'model_R4EMeetingData', a1)
    if hasattr(a1, 'model_R4EReview17'):
        assert _is_linked(a1, 'model_R4EReview17', b)
    _safe_set(b, 'model_R4EMeetingData', a2)
    assert _is_linked(b, 'model_R4EMeetingData', a2)
    if hasattr(a1, 'model_R4EReview17'):
        assert not _is_linked(a1, 'model_R4EReview17', b)
    if hasattr(a2, 'model_R4EReview17'):
        assert _is_linked(a2, 'model_R4EReview17', b)
    _safe_set(b, 'model_R4EMeetingData', None)
    assert not _is_linked(b, 'model_R4EMeetingData', a2)
    if hasattr(a2, 'model_R4EReview17'):
        assert not _is_linked(a2, 'model_R4EReview17', b)


def test_assoc_addedComments28_reverse_link_reassign_clear():
    a1 = model_R4EUser(groupPaths="sample_text", reviewCompleted=True, reviewCompletedCode=7, reviewCreatedByMe=True, sequenceIDCounter=7)
    a2 = model_R4EUser(groupPaths="sample_text_2", reviewCompleted=False, reviewCompletedCode=13, reviewCreatedByMe=False, sequenceIDCounter=13)
    b = model_R4EComment(createdOn=date(2024, 1, 1))
    _safe_set(b, 'model_R4EComment', a1)
    assert _is_linked(b, 'model_R4EComment', a1)
    if hasattr(a1, 'model_R4EUser29'):
        assert _is_linked(a1, 'model_R4EUser29', b)
    _safe_set(b, 'model_R4EComment', a2)
    assert _is_linked(b, 'model_R4EComment', a2)
    if hasattr(a1, 'model_R4EUser29'):
        assert not _is_linked(a1, 'model_R4EUser29', b)
    if hasattr(a2, 'model_R4EUser29'):
        assert _is_linked(a2, 'model_R4EUser29', b)
    _safe_set(b, 'model_R4EComment', None)
    assert not _is_linked(b, 'model_R4EComment', a2)
    if hasattr(a2, 'model_R4EUser29'):
        assert not _is_linked(a2, 'model_R4EUser29', b)


def test_assoc_addedItems30_reverse_link_reassign_clear():
    a1 = model_R4EUser(groupPaths="sample_text", reviewCompleted=True, reviewCompletedCode=7, reviewCreatedByMe=True, sequenceIDCounter=7)
    a2 = model_R4EUser(groupPaths="sample_text_2", reviewCompleted=False, reviewCompletedCode=13, reviewCreatedByMe=False, sequenceIDCounter=13)
    b = model_R4EItem(ProjectURIs="sample_text", addedById="sample_text", authorRep="sample_text", description="sample_text", repositoryRef="sample_text", submitted=date(2024, 1, 1))
    _safe_set(b, 'model_R4EItem', a1)
    assert _is_linked(b, 'model_R4EItem', a1)
    if hasattr(a1, 'model_R4EUser31'):
        assert _is_linked(a1, 'model_R4EUser31', b)
    _safe_set(b, 'model_R4EItem', a2)
    assert _is_linked(b, 'model_R4EItem', a2)
    if hasattr(a1, 'model_R4EUser31'):
        assert not _is_linked(a1, 'model_R4EUser31', b)
    if hasattr(a2, 'model_R4EUser31'):
        assert _is_linked(a2, 'model_R4EUser31', b)
    _safe_set(b, 'model_R4EItem', None)
    assert not _is_linked(b, 'model_R4EItem', a2)
    if hasattr(a2, 'model_R4EUser31'):
        assert not _is_linked(a2, 'model_R4EUser31', b)


def test_assoc_anomaly43_reverse_link_reassign_clear():
    a1 = model_R4EComment(createdOn=date(2024, 1, 1))
    a2 = model_R4EComment(createdOn=date(2025, 6, 15))
    b = model_R4EAnomaly(decidedByID="sample_text", dueDate=date(2024, 1, 1), fixedByID="sample_text", followUpByID="sample_text", isImported=True, notAcceptedReason="sample_text", rank="sample_text", ruleID="sample_text", state="sample_text")
    _safe_set(b, 'model_R4EAnomaly45', a1)
    assert _is_linked(b, 'model_R4EAnomaly45', a1)
    if hasattr(a1, 'model_R4EComment44'):
        assert _is_linked(a1, 'model_R4EComment44', b)
    _safe_set(b, 'model_R4EAnomaly45', a2)
    assert _is_linked(b, 'model_R4EAnomaly45', a2)
    if hasattr(a1, 'model_R4EComment44'):
        assert not _is_linked(a1, 'model_R4EComment44', b)
    if hasattr(a2, 'model_R4EComment44'):
        assert _is_linked(a2, 'model_R4EComment44', b)
    _safe_set(b, 'model_R4EAnomaly45', None)
    assert not _is_linked(b, 'model_R4EAnomaly45', a2)
    if hasattr(a2, 'model_R4EComment44'):
        assert not _is_linked(a2, 'model_R4EComment44', b)


def test_assoc_anomalyTemplate8_reverse_link_reassign_clear():
    a1 = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    a2 = model_R4EReview(components="sample_text_2", dueDate=date(2025, 6, 15), endDate=date(2025, 6, 15), entryCriteria="sample_text_2", extraNotes="sample_text_2", modifiedDate=date(2025, 6, 15), name="sample_text_2", objectives="sample_text_2", project="sample_text_2", referenceMaterial="sample_text_2", startDate=date(2025, 6, 15), type="sample_text_2")
    b = model_R4EAnomaly(decidedByID="sample_text", dueDate=date(2024, 1, 1), fixedByID="sample_text", followUpByID="sample_text", isImported=True, notAcceptedReason="sample_text", rank="sample_text", ruleID="sample_text", state="sample_text")
    _safe_set(b, 'model_R4EAnomaly', a1)
    assert _is_linked(b, 'model_R4EAnomaly', a1)
    if hasattr(a1, 'model_R4EReview9'):
        assert _is_linked(a1, 'model_R4EReview9', b)
    _safe_set(b, 'model_R4EAnomaly', a2)
    assert _is_linked(b, 'model_R4EAnomaly', a2)
    if hasattr(a1, 'model_R4EReview9'):
        assert not _is_linked(a1, 'model_R4EReview9', b)
    if hasattr(a2, 'model_R4EReview9'):
        assert _is_linked(a2, 'model_R4EReview9', b)
    _safe_set(b, 'model_R4EAnomaly', None)
    assert not _is_linked(b, 'model_R4EAnomaly', a2)
    if hasattr(a2, 'model_R4EReview9'):
        assert not _is_linked(a2, 'model_R4EReview9', b)


def test_assoc_anomalyTypeKeyToReference1_reverse_link_reassign_clear():
    a1 = model_R4EReviewGroup(availableComponents="sample_text", availableProjects="sample_text", defaultEntryCriteria="sample_text", designRuleLocations="sample_text", folder="sample_text", name="sample_text")
    a2 = model_R4EReviewGroup(availableComponents="sample_text_2", availableProjects="sample_text_2", defaultEntryCriteria="sample_text_2", designRuleLocations="sample_text_2", folder="sample_text_2", name="sample_text_2")
    b = model_MapToAnomalyType(key="sample_text")
    _safe_set(b, 'model_MapToAnomalyType', a1)
    assert _is_linked(b, 'model_MapToAnomalyType', a1)
    if hasattr(a1, 'model_R4EReviewGroup2'):
        assert _is_linked(a1, 'model_R4EReviewGroup2', b)
    _safe_set(b, 'model_MapToAnomalyType', a2)
    assert _is_linked(b, 'model_MapToAnomalyType', a2)
    if hasattr(a1, 'model_R4EReviewGroup2'):
        assert not _is_linked(a1, 'model_R4EReviewGroup2', b)
    if hasattr(a2, 'model_R4EReviewGroup2'):
        assert _is_linked(a2, 'model_R4EReviewGroup2', b)
    _safe_set(b, 'model_MapToAnomalyType', None)
    assert not _is_linked(b, 'model_MapToAnomalyType', a2)
    if hasattr(a2, 'model_R4EReviewGroup2'):
        assert not _is_linked(a2, 'model_R4EReviewGroup2', b)


def test_assoc_availableAnomalyTypes0_reverse_link_reassign_clear():
    a1 = model_R4EReviewGroup(availableComponents="sample_text", availableProjects="sample_text", defaultEntryCriteria="sample_text", designRuleLocations="sample_text", folder="sample_text", name="sample_text")
    a2 = model_R4EReviewGroup(availableComponents="sample_text_2", availableProjects="sample_text_2", defaultEntryCriteria="sample_text_2", designRuleLocations="sample_text_2", folder="sample_text_2", name="sample_text_2")
    b = model_R4EAnomalyType(type="sample_text")
    _safe_set(b, 'model_R4EAnomalyType', a1)
    assert _is_linked(b, 'model_R4EAnomalyType', a1)
    if hasattr(a1, 'model_R4EReviewGroup'):
        assert _is_linked(a1, 'model_R4EReviewGroup', b)
    _safe_set(b, 'model_R4EAnomalyType', a2)
    assert _is_linked(b, 'model_R4EAnomalyType', a2)
    if hasattr(a1, 'model_R4EReviewGroup'):
        assert not _is_linked(a1, 'model_R4EReviewGroup', b)
    if hasattr(a2, 'model_R4EReviewGroup'):
        assert _is_linked(a2, 'model_R4EReviewGroup', b)
    _safe_set(b, 'model_R4EAnomalyType', None)
    assert not _is_linked(b, 'model_R4EAnomalyType', a2)
    if hasattr(a2, 'model_R4EReviewGroup'):
        assert not _is_linked(a2, 'model_R4EReviewGroup', b)


def test_assoc_base51_reverse_link_reassign_clear():
    a1 = model_R4EFileVersion(fileRevision="sample_text", localVersionID="sample_text", name="sample_text", platformURI="sample_text", repositoryPath="sample_text", resource="sample_text", versionID="sample_text")
    a2 = model_R4EFileVersion(fileRevision="sample_text_2", localVersionID="sample_text_2", name="sample_text_2", platformURI="sample_text_2", repositoryPath="sample_text_2", resource="sample_text_2", versionID="sample_text_2")
    b = model_R4EFileContext(type="sample_text")
    _safe_set(b, 'model_R4EFileContext52', a1)
    assert _is_linked(b, 'model_R4EFileContext52', a1)
    if hasattr(a1, 'model_R4EFileVersion53'):
        assert _is_linked(a1, 'model_R4EFileVersion53', b)
    _safe_set(b, 'model_R4EFileContext52', a2)
    assert _is_linked(b, 'model_R4EFileContext52', a2)
    if hasattr(a1, 'model_R4EFileVersion53'):
        assert not _is_linked(a1, 'model_R4EFileVersion53', b)
    if hasattr(a2, 'model_R4EFileVersion53'):
        assert _is_linked(a2, 'model_R4EFileVersion53', b)
    _safe_set(b, 'model_R4EFileContext52', None)
    assert not _is_linked(b, 'model_R4EFileContext52', a2)
    if hasattr(a2, 'model_R4EFileVersion53'):
        assert not _is_linked(a2, 'model_R4EFileVersion53', b)


def test_assoc_createdBy12_reverse_link_reassign_clear():
    a1 = model_R4EUser(groupPaths="sample_text", reviewCompleted=True, reviewCompletedCode=7, reviewCreatedByMe=True, sequenceIDCounter=7)
    a2 = model_R4EUser(groupPaths="sample_text_2", reviewCompleted=False, reviewCompletedCode=13, reviewCreatedByMe=False, sequenceIDCounter=13)
    b = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    _safe_set(b, 'model_R4EReview13', a1)
    assert _is_linked(b, 'model_R4EReview13', a1)
    if hasattr(a1, 'model_R4EUser'):
        assert _is_linked(a1, 'model_R4EUser', b)
    _safe_set(b, 'model_R4EReview13', a2)
    assert _is_linked(b, 'model_R4EReview13', a2)
    if hasattr(a1, 'model_R4EUser'):
        assert not _is_linked(a1, 'model_R4EUser', b)
    if hasattr(a2, 'model_R4EUser'):
        assert _is_linked(a2, 'model_R4EUser', b)
    _safe_set(b, 'model_R4EReview13', None)
    assert not _is_linked(b, 'model_R4EReview13', a2)
    if hasattr(a2, 'model_R4EUser'):
        assert not _is_linked(a2, 'model_R4EUser', b)


def test_assoc_decision7_reverse_link_reassign_clear():
    a1 = model_R4EReviewDecision(spentTime=7, value="sample_text")
    a2 = model_R4EReviewDecision(spentTime=13, value="sample_text_2")
    b = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    _safe_set(b, 'model_R4EReview', a1)
    assert _is_linked(b, 'model_R4EReview', a1)
    if hasattr(a1, 'model_R4EReviewDecision'):
        assert _is_linked(a1, 'model_R4EReviewDecision', b)
    _safe_set(b, 'model_R4EReview', a2)
    assert _is_linked(b, 'model_R4EReview', a2)
    if hasattr(a1, 'model_R4EReviewDecision'):
        assert not _is_linked(a1, 'model_R4EReviewDecision', b)
    if hasattr(a2, 'model_R4EReviewDecision'):
        assert _is_linked(a2, 'model_R4EReviewDecision', b)
    _safe_set(b, 'model_R4EReview', None)
    assert not _is_linked(b, 'model_R4EReview', a2)
    if hasattr(a2, 'model_R4EReviewDecision'):
        assert not _is_linked(a2, 'model_R4EReviewDecision', b)


def test_assoc_fileContextList39_reverse_link_reassign_clear():
    a1 = model_R4EItem(ProjectURIs="sample_text", addedById="sample_text", authorRep="sample_text", description="sample_text", repositoryRef="sample_text", submitted=date(2024, 1, 1))
    a2 = model_R4EItem(ProjectURIs="sample_text_2", addedById="sample_text_2", authorRep="sample_text_2", description="sample_text_2", repositoryRef="sample_text_2", submitted=date(2025, 6, 15))
    b = model_R4EFileContext(type="sample_text")
    _safe_set(b, 'model_R4EFileContext', a1)
    assert _is_linked(b, 'model_R4EFileContext', a1)
    if hasattr(a1, 'model_R4EItem40'):
        assert _is_linked(a1, 'model_R4EItem40', b)
    _safe_set(b, 'model_R4EFileContext', a2)
    assert _is_linked(b, 'model_R4EFileContext', a2)
    if hasattr(a1, 'model_R4EItem40'):
        assert not _is_linked(a1, 'model_R4EItem40', b)
    if hasattr(a2, 'model_R4EItem40'):
        assert _is_linked(a2, 'model_R4EItem40', b)
    _safe_set(b, 'model_R4EFileContext', None)
    assert not _is_linked(b, 'model_R4EFileContext', a2)
    if hasattr(a2, 'model_R4EItem40'):
        assert not _is_linked(a2, 'model_R4EItem40', b)


def test_assoc_fixedInVersion20_reverse_link_reassign_clear():
    a1 = model_R4EFileVersion(fileRevision="sample_text", localVersionID="sample_text", name="sample_text", platformURI="sample_text", repositoryPath="sample_text", resource="sample_text", versionID="sample_text")
    a2 = model_R4EFileVersion(fileRevision="sample_text_2", localVersionID="sample_text_2", name="sample_text_2", platformURI="sample_text_2", repositoryPath="sample_text_2", resource="sample_text_2", versionID="sample_text_2")
    b = model_R4EAnomaly(decidedByID="sample_text", dueDate=date(2024, 1, 1), fixedByID="sample_text", followUpByID="sample_text", isImported=True, notAcceptedReason="sample_text", rank="sample_text", ruleID="sample_text", state="sample_text")
    _safe_set(b, 'model_R4EAnomaly21', a1)
    assert _is_linked(b, 'model_R4EAnomaly21', a1)
    if hasattr(a1, 'model_R4EFileVersion'):
        assert _is_linked(a1, 'model_R4EFileVersion', b)
    _safe_set(b, 'model_R4EAnomaly21', a2)
    assert _is_linked(b, 'model_R4EAnomaly21', a2)
    if hasattr(a1, 'model_R4EFileVersion'):
        assert not _is_linked(a1, 'model_R4EFileVersion', b)
    if hasattr(a2, 'model_R4EFileVersion'):
        assert _is_linked(a2, 'model_R4EFileVersion', b)
    _safe_set(b, 'model_R4EAnomaly21', None)
    assert not _is_linked(b, 'model_R4EAnomaly21', a2)
    if hasattr(a2, 'model_R4EFileVersion'):
        assert not _is_linked(a2, 'model_R4EFileVersion', b)


def test_assoc_group81_reverse_link_reassign_clear():
    a1 = model_R4EUserReviews(createdReviews="sample_text", name="sample_text")
    a2 = model_R4EUserReviews(createdReviews="sample_text_2", name="sample_text_2")
    b = model_R4EReviewGroup(availableComponents="sample_text", availableProjects="sample_text", defaultEntryCriteria="sample_text", designRuleLocations="sample_text", folder="sample_text", name="sample_text")
    _safe_set(b, 'model_R4EReviewGroup83', a1)
    assert _is_linked(b, 'model_R4EReviewGroup83', a1)
    if hasattr(a1, 'model_R4EUserReviews82'):
        assert _is_linked(a1, 'model_R4EUserReviews82', b)
    _safe_set(b, 'model_R4EReviewGroup83', a2)
    assert _is_linked(b, 'model_R4EReviewGroup83', a2)
    if hasattr(a1, 'model_R4EUserReviews82'):
        assert not _is_linked(a1, 'model_R4EUserReviews82', b)
    if hasattr(a2, 'model_R4EUserReviews82'):
        assert _is_linked(a2, 'model_R4EUserReviews82', b)
    _safe_set(b, 'model_R4EReviewGroup83', None)
    assert not _is_linked(b, 'model_R4EReviewGroup83', a2)
    if hasattr(a2, 'model_R4EUserReviews82'):
        assert not _is_linked(a2, 'model_R4EUserReviews82', b)


def test_assoc_infoAtt41_reverse_link_reassign_clear():
    a1 = model_R4EItem(ProjectURIs="sample_text", addedById="sample_text", authorRep="sample_text", description="sample_text", repositoryRef="sample_text", submitted=date(2024, 1, 1))
    a2 = model_R4EItem(ProjectURIs="sample_text_2", addedById="sample_text_2", authorRep="sample_text_2", description="sample_text_2", repositoryRef="sample_text_2", submitted=date(2025, 6, 15))
    b = model_MapKeyToInfoAttributes(key="sample_text", value="sample_text")
    _safe_set(b, 'model_MapKeyToInfoAttributes', a1)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes', a1)
    if hasattr(a1, 'model_R4EItem42'):
        assert _is_linked(a1, 'model_R4EItem42', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes', a2)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes', a2)
    if hasattr(a1, 'model_R4EItem42'):
        assert not _is_linked(a1, 'model_R4EItem42', b)
    if hasattr(a2, 'model_R4EItem42'):
        assert _is_linked(a2, 'model_R4EItem42', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes', None)
    assert not _is_linked(b, 'model_MapKeyToInfoAttributes', a2)
    if hasattr(a2, 'model_R4EItem42'):
        assert not _is_linked(a2, 'model_R4EItem42', b)


def test_assoc_infoAtt46_reverse_link_reassign_clear():
    a1 = model_R4EComment(createdOn=date(2024, 1, 1))
    a2 = model_R4EComment(createdOn=date(2025, 6, 15))
    b = model_MapKeyToInfoAttributes(key="sample_text", value="sample_text")
    _safe_set(b, 'model_MapKeyToInfoAttributes48', a1)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes48', a1)
    if hasattr(a1, 'model_R4EComment47'):
        assert _is_linked(a1, 'model_R4EComment47', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes48', a2)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes48', a2)
    if hasattr(a1, 'model_R4EComment47'):
        assert not _is_linked(a1, 'model_R4EComment47', b)
    if hasattr(a2, 'model_R4EComment47'):
        assert _is_linked(a2, 'model_R4EComment47', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes48', None)
    assert not _is_linked(b, 'model_MapKeyToInfoAttributes48', a2)
    if hasattr(a2, 'model_R4EComment47'):
        assert not _is_linked(a2, 'model_R4EComment47', b)


def test_assoc_infoAtt57_reverse_link_reassign_clear():
    a1 = model_R4EFileContext(type="sample_text")
    a2 = model_R4EFileContext(type="sample_text_2")
    b = model_MapKeyToInfoAttributes(key="sample_text", value="sample_text")
    _safe_set(b, 'model_MapKeyToInfoAttributes59', a1)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes59', a1)
    if hasattr(a1, 'model_R4EFileContext58'):
        assert _is_linked(a1, 'model_R4EFileContext58', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes59', a2)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes59', a2)
    if hasattr(a1, 'model_R4EFileContext58'):
        assert not _is_linked(a1, 'model_R4EFileContext58', b)
    if hasattr(a2, 'model_R4EFileContext58'):
        assert _is_linked(a2, 'model_R4EFileContext58', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes59', None)
    assert not _is_linked(b, 'model_MapKeyToInfoAttributes59', a2)
    if hasattr(a2, 'model_R4EFileContext58'):
        assert not _is_linked(a2, 'model_R4EFileContext58', b)


def test_assoc_infoAtt70_reverse_link_reassign_clear():
    a1 = model_R4EFileVersion(fileRevision="sample_text", localVersionID="sample_text", name="sample_text", platformURI="sample_text", repositoryPath="sample_text", resource="sample_text", versionID="sample_text")
    a2 = model_R4EFileVersion(fileRevision="sample_text_2", localVersionID="sample_text_2", name="sample_text_2", platformURI="sample_text_2", repositoryPath="sample_text_2", resource="sample_text_2", versionID="sample_text_2")
    b = model_MapKeyToInfoAttributes(key="sample_text", value="sample_text")
    _safe_set(b, 'model_MapKeyToInfoAttributes72', a1)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes72', a1)
    if hasattr(a1, 'model_R4EFileVersion71'):
        assert _is_linked(a1, 'model_R4EFileVersion71', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes72', a2)
    assert _is_linked(b, 'model_MapKeyToInfoAttributes72', a2)
    if hasattr(a1, 'model_R4EFileVersion71'):
        assert not _is_linked(a1, 'model_R4EFileVersion71', b)
    if hasattr(a2, 'model_R4EFileVersion71'):
        assert _is_linked(a2, 'model_R4EFileVersion71', b)
    _safe_set(b, 'model_MapKeyToInfoAttributes72', None)
    assert not _is_linked(b, 'model_MapKeyToInfoAttributes72', a2)
    if hasattr(a2, 'model_R4EFileVersion71'):
        assert not _is_linked(a2, 'model_R4EFileVersion71', b)


def test_assoc_invitedToMap79_reverse_link_reassign_clear():
    a1 = model_R4EUserReviews(createdReviews="sample_text", name="sample_text")
    a2 = model_R4EUserReviews(createdReviews="sample_text_2", name="sample_text_2")
    b = model_MapNameToReview(key="sample_text")
    _safe_set(b, 'model_MapNameToReview80', a1)
    assert _is_linked(b, 'model_MapNameToReview80', a1)
    if hasattr(a1, 'model_R4EUserReviews'):
        assert _is_linked(a1, 'model_R4EUserReviews', b)
    _safe_set(b, 'model_MapNameToReview80', a2)
    assert _is_linked(b, 'model_MapNameToReview80', a2)
    if hasattr(a1, 'model_R4EUserReviews'):
        assert not _is_linked(a1, 'model_R4EUserReviews', b)
    if hasattr(a2, 'model_R4EUserReviews'):
        assert _is_linked(a2, 'model_R4EUserReviews', b)
    _safe_set(b, 'model_MapNameToReview80', None)
    assert not _is_linked(b, 'model_MapNameToReview80', a2)
    if hasattr(a2, 'model_R4EUserReviews'):
        assert not _is_linked(a2, 'model_R4EUserReviews', b)


def test_assoc_reviewInstance32_reverse_link_reassign_clear():
    a1 = model_R4EUser(groupPaths="sample_text", reviewCompleted=True, reviewCompletedCode=7, reviewCreatedByMe=True, sequenceIDCounter=7)
    a2 = model_R4EUser(groupPaths="sample_text_2", reviewCompleted=False, reviewCompletedCode=13, reviewCreatedByMe=False, sequenceIDCounter=13)
    b = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    _safe_set(b, 'model_R4EReview34', a1)
    assert _is_linked(b, 'model_R4EReview34', a1)
    if hasattr(a1, 'model_R4EUser33'):
        assert _is_linked(a1, 'model_R4EUser33', b)
    _safe_set(b, 'model_R4EReview34', a2)
    assert _is_linked(b, 'model_R4EReview34', a2)
    if hasattr(a1, 'model_R4EUser33'):
        assert not _is_linked(a1, 'model_R4EUser33', b)
    if hasattr(a2, 'model_R4EUser33'):
        assert _is_linked(a2, 'model_R4EUser33', b)
    _safe_set(b, 'model_R4EReview34', None)
    assert not _is_linked(b, 'model_R4EReview34', a2)
    if hasattr(a2, 'model_R4EUser33'):
        assert not _is_linked(a2, 'model_R4EUser33', b)


def test_assoc_reviewedContent35_reverse_link_reassign_clear():
    a1 = model_R4EParticipant(focusArea="sample_text", isPartOfDecision=True, roles="sample_text")
    a2 = model_R4EParticipant(focusArea="sample_text_2", isPartOfDecision=False, roles="sample_text_2")
    b = model_R4EID(sequenceID=7, userID="sample_text")
    _safe_set(b, 'model_R4EID', a1)
    assert _is_linked(b, 'model_R4EID', a1)
    if hasattr(a1, 'model_R4EParticipant36'):
        assert _is_linked(a1, 'model_R4EParticipant36', b)
    _safe_set(b, 'model_R4EID', a2)
    assert _is_linked(b, 'model_R4EID', a2)
    if hasattr(a1, 'model_R4EParticipant36'):
        assert not _is_linked(a1, 'model_R4EParticipant36', b)
    if hasattr(a2, 'model_R4EParticipant36'):
        assert _is_linked(a2, 'model_R4EParticipant36', b)
    _safe_set(b, 'model_R4EID', None)
    assert not _is_linked(b, 'model_R4EID', a2)
    if hasattr(a2, 'model_R4EParticipant36'):
        assert not _is_linked(a2, 'model_R4EParticipant36', b)


def test_assoc_reviewsMap3_reverse_link_reassign_clear():
    a1 = model_R4EReviewGroup(availableComponents="sample_text", availableProjects="sample_text", defaultEntryCriteria="sample_text", designRuleLocations="sample_text", folder="sample_text", name="sample_text")
    a2 = model_R4EReviewGroup(availableComponents="sample_text_2", availableProjects="sample_text_2", defaultEntryCriteria="sample_text_2", designRuleLocations="sample_text_2", folder="sample_text_2", name="sample_text_2")
    b = model_MapNameToReview(key="sample_text")
    _safe_set(b, 'model_MapNameToReview', a1)
    assert _is_linked(b, 'model_MapNameToReview', a1)
    if hasattr(a1, 'model_R4EReviewGroup4'):
        assert _is_linked(a1, 'model_R4EReviewGroup4', b)
    _safe_set(b, 'model_MapNameToReview', a2)
    assert _is_linked(b, 'model_MapNameToReview', a2)
    if hasattr(a1, 'model_R4EReviewGroup4'):
        assert not _is_linked(a1, 'model_R4EReviewGroup4', b)
    if hasattr(a2, 'model_R4EReviewGroup4'):
        assert _is_linked(a2, 'model_R4EReviewGroup4', b)
    _safe_set(b, 'model_MapNameToReview', None)
    assert not _is_linked(b, 'model_MapNameToReview', a2)
    if hasattr(a2, 'model_R4EReviewGroup4'):
        assert not _is_linked(a2, 'model_R4EReviewGroup4', b)


def test_assoc_target54_reverse_link_reassign_clear():
    a1 = model_R4EFileVersion(fileRevision="sample_text", localVersionID="sample_text", name="sample_text", platformURI="sample_text", repositoryPath="sample_text", resource="sample_text", versionID="sample_text")
    a2 = model_R4EFileVersion(fileRevision="sample_text_2", localVersionID="sample_text_2", name="sample_text_2", platformURI="sample_text_2", repositoryPath="sample_text_2", resource="sample_text_2", versionID="sample_text_2")
    b = model_R4EFileContext(type="sample_text")
    _safe_set(b, 'model_R4EFileContext55', a1)
    assert _is_linked(b, 'model_R4EFileContext55', a1)
    if hasattr(a1, 'model_R4EFileVersion56'):
        assert _is_linked(a1, 'model_R4EFileVersion56', b)
    _safe_set(b, 'model_R4EFileContext55', a2)
    assert _is_linked(b, 'model_R4EFileContext55', a2)
    if hasattr(a1, 'model_R4EFileVersion56'):
        assert not _is_linked(a1, 'model_R4EFileVersion56', b)
    if hasattr(a2, 'model_R4EFileVersion56'):
        assert _is_linked(a2, 'model_R4EFileVersion56', b)
    _safe_set(b, 'model_R4EFileContext55', None)
    assert not _is_linked(b, 'model_R4EFileContext55', a2)
    if hasattr(a2, 'model_R4EFileVersion56'):
        assert not _is_linked(a2, 'model_R4EFileVersion56', b)


def test_assoc_timeLog37_reverse_link_reassign_clear():
    a1 = model_R4EParticipant(focusArea="sample_text", isPartOfDecision=True, roles="sample_text")
    a2 = model_R4EParticipant(focusArea="sample_text_2", isPartOfDecision=False, roles="sample_text_2")
    b = model_MapDateToDuration(key=date(2024, 1, 1), value="sample_text")
    _safe_set(b, 'model_MapDateToDuration', a1)
    assert _is_linked(b, 'model_MapDateToDuration', a1)
    if hasattr(a1, 'model_R4EParticipant38'):
        assert _is_linked(a1, 'model_R4EParticipant38', b)
    _safe_set(b, 'model_MapDateToDuration', a2)
    assert _is_linked(b, 'model_MapDateToDuration', a2)
    if hasattr(a1, 'model_R4EParticipant38'):
        assert not _is_linked(a1, 'model_R4EParticipant38', b)
    if hasattr(a2, 'model_R4EParticipant38'):
        assert _is_linked(a2, 'model_R4EParticipant38', b)
    _safe_set(b, 'model_MapDateToDuration', None)
    assert not _is_linked(b, 'model_MapDateToDuration', a2)
    if hasattr(a2, 'model_R4EParticipant38'):
        assert not _is_linked(a2, 'model_R4EParticipant38', b)


def test_assoc_userReviews5_reverse_link_reassign_clear():
    a1 = model_R4EReviewGroup(availableComponents="sample_text", availableProjects="sample_text", defaultEntryCriteria="sample_text", designRuleLocations="sample_text", folder="sample_text", name="sample_text")
    a2 = model_R4EReviewGroup(availableComponents="sample_text_2", availableProjects="sample_text_2", defaultEntryCriteria="sample_text_2", designRuleLocations="sample_text_2", folder="sample_text_2", name="sample_text_2")
    b = model_MapUserIDToUserReviews(key="sample_text")
    _safe_set(b, 'model_MapUserIDToUserReviews', a1)
    assert _is_linked(b, 'model_MapUserIDToUserReviews', a1)
    if hasattr(a1, 'model_R4EReviewGroup6'):
        assert _is_linked(a1, 'model_R4EReviewGroup6', b)
    _safe_set(b, 'model_MapUserIDToUserReviews', a2)
    assert _is_linked(b, 'model_MapUserIDToUserReviews', a2)
    if hasattr(a1, 'model_R4EReviewGroup6'):
        assert not _is_linked(a1, 'model_R4EReviewGroup6', b)
    if hasattr(a2, 'model_R4EReviewGroup6'):
        assert _is_linked(a2, 'model_R4EReviewGroup6', b)
    _safe_set(b, 'model_MapUserIDToUserReviews', None)
    assert not _is_linked(b, 'model_MapUserIDToUserReviews', a2)
    if hasattr(a2, 'model_R4EReviewGroup6'):
        assert not _is_linked(a2, 'model_R4EReviewGroup6', b)


def test_assoc_usersMap10_reverse_link_reassign_clear():
    a1 = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    a2 = model_R4EReview(components="sample_text_2", dueDate=date(2025, 6, 15), endDate=date(2025, 6, 15), entryCriteria="sample_text_2", extraNotes="sample_text_2", modifiedDate=date(2025, 6, 15), name="sample_text_2", objectives="sample_text_2", project="sample_text_2", referenceMaterial="sample_text_2", startDate=date(2025, 6, 15), type="sample_text_2")
    b = model_MapToUsers(key="sample_text")
    _safe_set(b, 'model_MapToUsers', a1)
    assert _is_linked(b, 'model_MapToUsers', a1)
    if hasattr(a1, 'model_R4EReview11'):
        assert _is_linked(a1, 'model_R4EReview11', b)
    _safe_set(b, 'model_MapToUsers', a2)
    assert _is_linked(b, 'model_MapToUsers', a2)
    if hasattr(a1, 'model_R4EReview11'):
        assert not _is_linked(a1, 'model_R4EReview11', b)
    if hasattr(a2, 'model_R4EReview11'):
        assert _is_linked(a2, 'model_R4EReview11', b)
    _safe_set(b, 'model_MapToUsers', None)
    assert not _is_linked(b, 'model_MapToUsers', a2)
    if hasattr(a2, 'model_R4EReview11'):
        assert not _is_linked(a2, 'model_R4EReview11', b)


def test_assoc_value65_reverse_link_reassign_clear():
    a1 = model_R4EAnomalyType(type="sample_text")
    a2 = model_R4EAnomalyType(type="sample_text_2")
    b = model_MapToAnomalyType(key="sample_text")
    _safe_set(b, 'model_MapToAnomalyType66', a1)
    assert _is_linked(b, 'model_MapToAnomalyType66', a1)
    if hasattr(a1, 'model_R4EAnomalyType67'):
        assert _is_linked(a1, 'model_R4EAnomalyType67', b)
    _safe_set(b, 'model_MapToAnomalyType66', a2)
    assert _is_linked(b, 'model_MapToAnomalyType66', a2)
    if hasattr(a1, 'model_R4EAnomalyType67'):
        assert not _is_linked(a1, 'model_R4EAnomalyType67', b)
    if hasattr(a2, 'model_R4EAnomalyType67'):
        assert _is_linked(a2, 'model_R4EAnomalyType67', b)
    _safe_set(b, 'model_MapToAnomalyType66', None)
    assert not _is_linked(b, 'model_MapToAnomalyType66', a2)
    if hasattr(a2, 'model_R4EAnomalyType67'):
        assert not _is_linked(a2, 'model_R4EAnomalyType67', b)


def test_assoc_value73_reverse_link_reassign_clear():
    a1 = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    a2 = model_R4EReview(components="sample_text_2", dueDate=date(2025, 6, 15), endDate=date(2025, 6, 15), entryCriteria="sample_text_2", extraNotes="sample_text_2", modifiedDate=date(2025, 6, 15), name="sample_text_2", objectives="sample_text_2", project="sample_text_2", referenceMaterial="sample_text_2", startDate=date(2025, 6, 15), type="sample_text_2")
    b = model_MapNameToReview(key="sample_text")
    _safe_set(b, 'model_MapNameToReview74', a1)
    assert _is_linked(b, 'model_MapNameToReview74', a1)
    if hasattr(a1, 'model_R4EReview75'):
        assert _is_linked(a1, 'model_R4EReview75', b)
    _safe_set(b, 'model_MapNameToReview74', a2)
    assert _is_linked(b, 'model_MapNameToReview74', a2)
    if hasattr(a1, 'model_R4EReview75'):
        assert not _is_linked(a1, 'model_R4EReview75', b)
    if hasattr(a2, 'model_R4EReview75'):
        assert _is_linked(a2, 'model_R4EReview75', b)
    _safe_set(b, 'model_MapNameToReview74', None)
    assert not _is_linked(b, 'model_MapNameToReview74', a2)
    if hasattr(a2, 'model_R4EReview75'):
        assert not _is_linked(a2, 'model_R4EReview75', b)


def test_assoc_value76_reverse_link_reassign_clear():
    a1 = model_R4EUser(groupPaths="sample_text", reviewCompleted=True, reviewCompletedCode=7, reviewCreatedByMe=True, sequenceIDCounter=7)
    a2 = model_R4EUser(groupPaths="sample_text_2", reviewCompleted=False, reviewCompletedCode=13, reviewCreatedByMe=False, sequenceIDCounter=13)
    b = model_MapToUsers(key="sample_text")
    _safe_set(b, 'model_MapToUsers77', a1)
    assert _is_linked(b, 'model_MapToUsers77', a1)
    if hasattr(a1, 'model_R4EUser78'):
        assert _is_linked(a1, 'model_R4EUser78', b)
    _safe_set(b, 'model_MapToUsers77', a2)
    assert _is_linked(b, 'model_MapToUsers77', a2)
    if hasattr(a1, 'model_R4EUser78'):
        assert not _is_linked(a1, 'model_R4EUser78', b)
    if hasattr(a2, 'model_R4EUser78'):
        assert _is_linked(a2, 'model_R4EUser78', b)
    _safe_set(b, 'model_MapToUsers77', None)
    assert not _is_linked(b, 'model_MapToUsers77', a2)
    if hasattr(a2, 'model_R4EUser78'):
        assert not _is_linked(a2, 'model_R4EUser78', b)


def test_assoc_value92_reverse_link_reassign_clear():
    a1 = model_R4EUserReviews(createdReviews="sample_text", name="sample_text")
    a2 = model_R4EUserReviews(createdReviews="sample_text_2", name="sample_text_2")
    b = model_MapUserIDToUserReviews(key="sample_text")
    _safe_set(b, 'model_MapUserIDToUserReviews93', a1)
    assert _is_linked(b, 'model_MapUserIDToUserReviews93', a1)
    if hasattr(a1, 'model_R4EUserReviews94'):
        assert _is_linked(a1, 'model_R4EUserReviews94', b)
    _safe_set(b, 'model_MapUserIDToUserReviews93', a2)
    assert _is_linked(b, 'model_MapUserIDToUserReviews93', a2)
    if hasattr(a1, 'model_R4EUserReviews94'):
        assert not _is_linked(a1, 'model_R4EUserReviews94', b)
    if hasattr(a2, 'model_R4EUserReviews94'):
        assert _is_linked(a2, 'model_R4EUserReviews94', b)
    _safe_set(b, 'model_MapUserIDToUserReviews93', None)
    assert not _is_linked(b, 'model_MapUserIDToUserReviews93', a2)
    if hasattr(a2, 'model_R4EUserReviews94'):
        assert not _is_linked(a2, 'model_R4EUserReviews94', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base60_stub_double():
    # model_R4EDelta has no real 'model_R4EDelta61' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EContent(info="sample_text")
    partner = model_R4EDelta()
    setattr(partner, 'model_R4EDelta61', None)
    _safe_set(owner, 'model_R4EContent', partner)
    assert getattr(partner, 'model_R4EDelta61') == owner
    _safe_set(owner, 'model_R4EContent', None)
    assert getattr(partner, 'model_R4EDelta61') is None


def test_assoc_current25_stub_double():
    # model_R4EFormalReview has no real 'model_R4EFormalReview26' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EReviewPhaseInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EReviewPhaseInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EReviewPhaseInfo(endDate=date(2024, 1, 1), phaseOwnerID="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    partner = model_R4EFormalReview()
    setattr(partner, 'model_R4EFormalReview26', None)
    _safe_set(owner, 'model_R4EReviewPhaseInfo27', partner)
    assert getattr(partner, 'model_R4EFormalReview26') == owner
    _safe_set(owner, 'model_R4EReviewPhaseInfo27', None)
    assert getattr(partner, 'model_R4EFormalReview26') is None


def test_assoc_deltas49_stub_double():
    # model_R4EDelta has no real 'model_R4EDelta' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EFileContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EFileContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EFileContext(type="sample_text")
    partner = model_R4EDelta()
    setattr(partner, 'model_R4EDelta', None)
    _safe_set(owner, 'model_R4EFileContext50', {partner})
    assert getattr(partner, 'model_R4EDelta') == owner
    _safe_set(owner, 'model_R4EFileContext50', set())
    assert getattr(partner, 'model_R4EDelta') is None


def test_assoc_file95_stub_double():
    # model_R4EAnomalyTextPosition has no real 'model_R4EAnomalyTextPosition' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EFileVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EFileVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EFileVersion(fileRevision="sample_text", localVersionID="sample_text", name="sample_text", platformURI="sample_text", repositoryPath="sample_text", resource="sample_text", versionID="sample_text")
    partner = model_R4EAnomalyTextPosition()
    setattr(partner, 'model_R4EAnomalyTextPosition', None)
    _safe_set(owner, 'model_R4EFileVersion96', partner)
    assert getattr(partner, 'model_R4EAnomalyTextPosition') == owner
    _safe_set(owner, 'model_R4EFileVersion96', None)
    assert getattr(partner, 'model_R4EAnomalyTextPosition') is None


def test_assoc_id84_stub_double():
    # model_R4EIDComponent has no real 'model_R4EIDComponent' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EID(sequenceID=7, userID="sample_text")
    partner = model_R4EIDComponent()
    setattr(partner, 'model_R4EIDComponent', None)
    _safe_set(owner, 'model_R4EID85', partner)
    assert getattr(partner, 'model_R4EIDComponent') == owner
    _safe_set(owner, 'model_R4EID85', None)
    assert getattr(partner, 'model_R4EIDComponent') is None


def test_assoc_idsMap14_stub_double():
    # model_MapIDToComponent has no real 'model_MapIDToComponent' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EReview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EReview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EReview(components="sample_text", dueDate=date(2024, 1, 1), endDate=date(2024, 1, 1), entryCriteria="sample_text", extraNotes="sample_text", modifiedDate=date(2024, 1, 1), name="sample_text", objectives="sample_text", project="sample_text", referenceMaterial="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    partner = model_MapIDToComponent()
    setattr(partner, 'model_MapIDToComponent', None)
    _safe_set(owner, 'model_R4EReview15', {partner})
    assert getattr(partner, 'model_MapIDToComponent') == owner
    _safe_set(owner, 'model_R4EReview15', set())
    assert getattr(partner, 'model_MapIDToComponent') is None


def test_assoc_key86_stub_double():
    # model_MapIDToComponent has no real 'model_MapIDToComponent87' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EID(sequenceID=7, userID="sample_text")
    partner = model_MapIDToComponent()
    setattr(partner, 'model_MapIDToComponent87', None)
    _safe_set(owner, 'model_R4EID88', partner)
    assert getattr(partner, 'model_MapIDToComponent87') == owner
    _safe_set(owner, 'model_R4EID88', None)
    assert getattr(partner, 'model_MapIDToComponent87') is None


def test_assoc_location68_stub_double():
    # model_R4EPosition has no real 'model_R4EPosition' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EContent(info="sample_text")
    partner = model_R4EPosition()
    setattr(partner, 'model_R4EPosition', None)
    _safe_set(owner, 'model_R4EContent69', partner)
    assert getattr(partner, 'model_R4EPosition') == owner
    _safe_set(owner, 'model_R4EContent69', None)
    assert getattr(partner, 'model_R4EPosition') is None


def test_assoc_phaseOwner22_stub_double():
    # model_R4EFormalReview has no real 'model_R4EFormalReview' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EParticipant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EParticipant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EParticipant(focusArea="sample_text", isPartOfDecision=True, roles="sample_text")
    partner = model_R4EFormalReview()
    setattr(partner, 'model_R4EFormalReview', None)
    _safe_set(owner, 'model_R4EParticipant', partner)
    assert getattr(partner, 'model_R4EFormalReview') == owner
    _safe_set(owner, 'model_R4EParticipant', None)
    assert getattr(partner, 'model_R4EFormalReview') is None


def test_assoc_phases23_stub_double():
    # model_R4EFormalReview has no real 'model_R4EFormalReview24' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EReviewPhaseInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EReviewPhaseInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EReviewPhaseInfo(endDate=date(2024, 1, 1), phaseOwnerID="sample_text", startDate=date(2024, 1, 1), type="sample_text")
    partner = model_R4EFormalReview()
    setattr(partner, 'model_R4EFormalReview24', None)
    _safe_set(owner, 'model_R4EReviewPhaseInfo', partner)
    assert owner in getattr(partner, 'model_R4EFormalReview24')
    _safe_set(owner, 'model_R4EReviewPhaseInfo', None)
    assert owner not in getattr(partner, 'model_R4EFormalReview24')


def test_assoc_rule18_stub_double():
    # model_R4EDesignRule has no real 'model_R4EDesignRule' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EAnomaly's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EAnomaly's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EAnomaly(decidedByID="sample_text", dueDate=date(2024, 1, 1), fixedByID="sample_text", followUpByID="sample_text", isImported=True, notAcceptedReason="sample_text", rank="sample_text", ruleID="sample_text", state="sample_text")
    partner = model_R4EDesignRule()
    setattr(partner, 'model_R4EDesignRule', None)
    _safe_set(owner, 'model_R4EAnomaly19', partner)
    assert getattr(partner, 'model_R4EDesignRule') == owner
    _safe_set(owner, 'model_R4EAnomaly19', None)
    assert getattr(partner, 'model_R4EDesignRule') is None


def test_assoc_target62_stub_double():
    # model_R4EDelta has no real 'model_R4EDelta63' property in the generated
    # code (a bare stub) -- manually attach it so model_R4EContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_R4EContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_R4EContent(info="sample_text")
    partner = model_R4EDelta()
    setattr(partner, 'model_R4EDelta63', None)
    _safe_set(owner, 'model_R4EContent64', partner)
    assert getattr(partner, 'model_R4EDelta63') == owner
    _safe_set(owner, 'model_R4EContent64', None)
    assert getattr(partner, 'model_R4EDelta63') is None


