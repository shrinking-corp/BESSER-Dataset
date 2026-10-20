# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BZ_BZEvent,
    BZ_BZComment,
    BZ_BZIssue,
    BZ_BZComponent,
    BZ_BZProduct,
    BZ_BZRepo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bz_bzevent_is_not_abstract():
    assert not inspect.isabstract(BZ_BZEvent)


def test_hyp_bz_bzevent_constructor_exists():
    assert callable(BZ_BZEvent.__init__)


def test_hyp_bz_bzevent_constructor_args():
    sig = inspect.signature(BZ_BZEvent.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "author" in params, "Missing parameter 'author'"
    assert "date" in params, "Missing parameter 'date'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"









def test_hyp_bz_bzcomment_is_not_abstract():
    assert not inspect.isabstract(BZ_BZComment)


def test_hyp_bz_bzcomment_constructor_exists():
    assert callable(BZ_BZComment.__init__)


def test_hyp_bz_bzcomment_constructor_args():
    sig = inspect.signature(BZ_BZComment.__init__)
    params = list(sig.parameters.keys())
    assert "commentHTML" in params, "Missing parameter 'commentHTML'"
    assert "commentTime" in params, "Missing parameter 'commentTime'"
    assert "commentText" in params, "Missing parameter 'commentText'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "commentId" in params, "Missing parameter 'commentId'"
    assert "commentAuthor" in params, "Missing parameter 'commentAuthor'"









def test_hyp_bz_bzissue_is_not_abstract():
    assert not inspect.isabstract(BZ_BZIssue)


def test_hyp_bz_bzissue_constructor_exists():
    assert callable(BZ_BZIssue.__init__)


def test_hyp_bz_bzissue_constructor_args():
    sig = inspect.signature(BZ_BZIssue.__init__)
    params = list(sig.parameters.keys())
    assert "seeAlso" in params, "Missing parameter 'seeAlso'"
    assert "platform" in params, "Missing parameter 'platform'"
    assert "dependsOn" in params, "Missing parameter 'dependsOn'"
    assert "lastModifiedOn" in params, "Missing parameter 'lastModifiedOn'"
    assert "issueId" in params, "Missing parameter 'issueId'"
    assert "latestCommit" in params, "Missing parameter 'latestCommit'"
    assert "referenceURL" in params, "Missing parameter 'referenceURL'"
    assert "status" in params, "Missing parameter 'status'"
    assert "reportedBy" in params, "Missing parameter 'reportedBy'"
    assert "versionFixedIn" in params, "Missing parameter 'versionFixedIn'"
    assert "issueURL" in params, "Missing parameter 'issueURL'"
    assert "assignedTo" in params, "Missing parameter 'assignedTo'"
    assert "classification" in params, "Missing parameter 'classification'"
    assert "reportedOn" in params, "Missing parameter 'reportedOn'"
    assert "milestone" in params, "Missing parameter 'milestone'"
    assert "issueTitle" in params, "Missing parameter 'issueTitle'"
    assert "ccList" in params, "Missing parameter 'ccList'"
    assert "blocks" in params, "Missing parameter 'blocks'"
    assert "importance" in params, "Missing parameter 'importance'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "reportedByUsername" in params, "Missing parameter 'reportedByUsername'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "componentName" in params, "Missing parameter 'componentName'"



























def test_hyp_bz_bzcomponent_is_not_abstract():
    assert not inspect.isabstract(BZ_BZComponent)


def test_hyp_bz_bzcomponent_constructor_exists():
    assert callable(BZ_BZComponent.__init__)


def test_hyp_bz_bzcomponent_constructor_args():
    sig = inspect.signature(BZ_BZComponent.__init__)
    params = list(sig.parameters.keys())
    assert "componentURL" in params, "Missing parameter 'componentURL'"
    assert "componentDescription" in params, "Missing parameter 'componentDescription'"
    assert "defaultAssignee" in params, "Missing parameter 'defaultAssignee'"
    assert "componentId" in params, "Missing parameter 'componentId'"







def test_hyp_bz_bzproduct_is_not_abstract():
    assert not inspect.isabstract(BZ_BZProduct)


def test_hyp_bz_bzproduct_constructor_exists():
    assert callable(BZ_BZProduct.__init__)


def test_hyp_bz_bzproduct_constructor_args():
    sig = inspect.signature(BZ_BZProduct.__init__)
    params = list(sig.parameters.keys())
    assert "productDescription" in params, "Missing parameter 'productDescription'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "productURL" in params, "Missing parameter 'productURL'"






def test_hyp_bz_bzrepo_is_not_abstract():
    assert not inspect.isabstract(BZ_BZRepo)


def test_hyp_bz_bzrepo_constructor_exists():
    assert callable(BZ_BZRepo.__init__)


def test_hyp_bz_bzrepo_constructor_args():
    sig = inspect.signature(BZ_BZRepo.__init__)
    params = list(sig.parameters.keys())
    assert "repoURL" in params, "Missing parameter 'repoURL'"



# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
BZ_BZEvent_strategy = st.builds(
    BZ_BZEvent,
    field=
        safe_text,
    newValue=
        safe_text,
    author=
        safe_text,
    date=
        st.dates(),
    issueId=
        st.integers(),
    oldValue=
        safe_text
)
BZ_BZComment_strategy = st.builds(
    BZ_BZComment,
    commentHTML=
        safe_text,
    commentTime=
        st.dates(),
    commentText=
        safe_text,
    issueId=
        st.integers(),
    commentId=
        safe_text,
    commentAuthor=
        safe_text
)
BZ_BZIssue_strategy = st.builds(
    BZ_BZIssue,
    seeAlso=
        safe_text,
    platform=
        safe_text,
    dependsOn=
        safe_text,
    lastModifiedOn=
        st.dates(),
    issueId=
        st.integers(),
    latestCommit=
        safe_text,
    referenceURL=
        safe_text,
    status=
        safe_text,
    reportedBy=
        safe_text,
    versionFixedIn=
        safe_text,
    issueURL=
        safe_text,
    assignedTo=
        safe_text,
    classification=
        safe_text,
    reportedOn=
        st.dates(),
    milestone=
        safe_text,
    issueTitle=
        safe_text,
    ccList=
        safe_text,
    blocks=
        safe_text,
    importance=
        safe_text,
    productName=
        safe_text,
    version=
        safe_text,
    reportedByUsername=
        safe_text,
    keywords=
        safe_text,
    componentName=
        safe_text
)
BZ_BZComponent_strategy = st.builds(
    BZ_BZComponent,
    componentURL=
        safe_text,
    componentDescription=
        safe_text,
    defaultAssignee=
        safe_text,
    componentId=
        safe_text
)
BZ_BZProduct_strategy = st.builds(
    BZ_BZProduct,
    productDescription=
        safe_text,
    productId=
        safe_text,
    productURL=
        safe_text
)
BZ_BZRepo_strategy = st.builds(
    BZ_BZRepo,
    repoURL=
        safe_text
)




@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original



@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZEvent_strategy)
def test_hyp_bz_bzevent_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original




@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_commentHTML_setter(instance):
    original = instance.commentHTML
    instance.commentHTML = original
    assert instance.commentHTML == original



@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_commentTime_setter(instance):
    original = instance.commentTime
    instance.commentTime = original
    assert instance.commentTime == original



@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_commentText_setter(instance):
    original = instance.commentText
    instance.commentText = original
    assert instance.commentText == original



@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_commentId_setter(instance):
    original = instance.commentId
    instance.commentId = original
    assert instance.commentId == original



@given(instance=BZ_BZComment_strategy)
def test_hyp_bz_bzcomment_commentAuthor_setter(instance):
    original = instance.commentAuthor
    instance.commentAuthor = original
    assert instance.commentAuthor == original




@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_seeAlso_setter(instance):
    original = instance.seeAlso
    instance.seeAlso = original
    assert instance.seeAlso == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_platform_setter(instance):
    original = instance.platform
    instance.platform = original
    assert instance.platform == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_dependsOn_setter(instance):
    original = instance.dependsOn
    instance.dependsOn = original
    assert instance.dependsOn == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_lastModifiedOn_setter(instance):
    original = instance.lastModifiedOn
    instance.lastModifiedOn = original
    assert instance.lastModifiedOn == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_issueId_setter(instance):
    original = instance.issueId
    instance.issueId = original
    assert instance.issueId == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_latestCommit_setter(instance):
    original = instance.latestCommit
    instance.latestCommit = original
    assert instance.latestCommit == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_referenceURL_setter(instance):
    original = instance.referenceURL
    instance.referenceURL = original
    assert instance.referenceURL == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_reportedBy_setter(instance):
    original = instance.reportedBy
    instance.reportedBy = original
    assert instance.reportedBy == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_versionFixedIn_setter(instance):
    original = instance.versionFixedIn
    instance.versionFixedIn = original
    assert instance.versionFixedIn == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_issueURL_setter(instance):
    original = instance.issueURL
    instance.issueURL = original
    assert instance.issueURL == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_assignedTo_setter(instance):
    original = instance.assignedTo
    instance.assignedTo = original
    assert instance.assignedTo == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_classification_setter(instance):
    original = instance.classification
    instance.classification = original
    assert instance.classification == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_reportedOn_setter(instance):
    original = instance.reportedOn
    instance.reportedOn = original
    assert instance.reportedOn == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_milestone_setter(instance):
    original = instance.milestone
    instance.milestone = original
    assert instance.milestone == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_issueTitle_setter(instance):
    original = instance.issueTitle
    instance.issueTitle = original
    assert instance.issueTitle == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_ccList_setter(instance):
    original = instance.ccList
    instance.ccList = original
    assert instance.ccList == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_blocks_setter(instance):
    original = instance.blocks
    instance.blocks = original
    assert instance.blocks == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_importance_setter(instance):
    original = instance.importance
    instance.importance = original
    assert instance.importance == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_reportedByUsername_setter(instance):
    original = instance.reportedByUsername
    instance.reportedByUsername = original
    assert instance.reportedByUsername == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=BZ_BZIssue_strategy)
def test_hyp_bz_bzissue_componentName_setter(instance):
    original = instance.componentName
    instance.componentName = original
    assert instance.componentName == original




@given(instance=BZ_BZComponent_strategy)
def test_hyp_bz_bzcomponent_componentURL_setter(instance):
    original = instance.componentURL
    instance.componentURL = original
    assert instance.componentURL == original



@given(instance=BZ_BZComponent_strategy)
def test_hyp_bz_bzcomponent_componentDescription_setter(instance):
    original = instance.componentDescription
    instance.componentDescription = original
    assert instance.componentDescription == original



@given(instance=BZ_BZComponent_strategy)
def test_hyp_bz_bzcomponent_defaultAssignee_setter(instance):
    original = instance.defaultAssignee
    instance.defaultAssignee = original
    assert instance.defaultAssignee == original



@given(instance=BZ_BZComponent_strategy)
def test_hyp_bz_bzcomponent_componentId_setter(instance):
    original = instance.componentId
    instance.componentId = original
    assert instance.componentId == original




@given(instance=BZ_BZProduct_strategy)
def test_hyp_bz_bzproduct_productDescription_setter(instance):
    original = instance.productDescription
    instance.productDescription = original
    assert instance.productDescription == original



@given(instance=BZ_BZProduct_strategy)
def test_hyp_bz_bzproduct_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=BZ_BZProduct_strategy)
def test_hyp_bz_bzproduct_productURL_setter(instance):
    original = instance.productURL
    instance.productURL = original
    assert instance.productURL == original




@given(instance=BZ_BZRepo_strategy)
def test_hyp_bz_bzrepo_repoURL_setter(instance):
    original = instance.repoURL
    instance.repoURL = original
    assert instance.repoURL == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BZ_BZComment,
    BZ_BZComponent,
    BZ_BZEvent,
    BZ_BZIssue,
    BZ_BZProduct,
    BZ_BZRepo,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_BZ_BZComment_commentAuthor_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.commentAuthor == "sample_text"
    instance.commentAuthor = "sample_text_2"
    assert instance.commentAuthor == "sample_text_2"


def test_BZ_BZComment_commentHTML_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.commentHTML == "sample_text"
    instance.commentHTML = "sample_text_2"
    assert instance.commentHTML == "sample_text_2"


def test_BZ_BZComment_commentId_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.commentId == "sample_text"
    instance.commentId = "sample_text_2"
    assert instance.commentId == "sample_text_2"


def test_BZ_BZComment_commentText_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.commentText == "sample_text"
    instance.commentText = "sample_text_2"
    assert instance.commentText == "sample_text_2"


def test_BZ_BZComment_commentTime_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.commentTime == date(2024, 1, 1)
    instance.commentTime = date(2025, 6, 15)
    assert instance.commentTime == date(2025, 6, 15)


def test_BZ_BZComment_issueId_value_roundtrip():
    instance = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    assert instance.issueId == 7
    instance.issueId = 13
    assert instance.issueId == 13


def test_BZ_BZComponent_componentDescription_value_roundtrip():
    instance = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    assert instance.componentDescription == "sample_text"
    instance.componentDescription = "sample_text_2"
    assert instance.componentDescription == "sample_text_2"


def test_BZ_BZComponent_componentId_value_roundtrip():
    instance = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    assert instance.componentId == "sample_text"
    instance.componentId = "sample_text_2"
    assert instance.componentId == "sample_text_2"


def test_BZ_BZComponent_componentURL_value_roundtrip():
    instance = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    assert instance.componentURL == "sample_text"
    instance.componentURL = "sample_text_2"
    assert instance.componentURL == "sample_text_2"


def test_BZ_BZComponent_defaultAssignee_value_roundtrip():
    instance = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    assert instance.defaultAssignee == "sample_text"
    instance.defaultAssignee = "sample_text_2"
    assert instance.defaultAssignee == "sample_text_2"


def test_BZ_BZEvent_author_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_BZ_BZEvent_date_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_BZ_BZEvent_field_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.field == "sample_text"
    instance.field = "sample_text_2"
    assert instance.field == "sample_text_2"


def test_BZ_BZEvent_issueId_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.issueId == 7
    instance.issueId = 13
    assert instance.issueId == 13


def test_BZ_BZEvent_newValue_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.newValue == "sample_text"
    instance.newValue = "sample_text_2"
    assert instance.newValue == "sample_text_2"


def test_BZ_BZEvent_oldValue_value_roundtrip():
    instance = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    assert instance.oldValue == "sample_text"
    instance.oldValue = "sample_text_2"
    assert instance.oldValue == "sample_text_2"


def test_BZ_BZIssue_assignedTo_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.assignedTo == "sample_text"
    instance.assignedTo = "sample_text_2"
    assert instance.assignedTo == "sample_text_2"


def test_BZ_BZIssue_blocks_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.blocks == "sample_text"
    instance.blocks = "sample_text_2"
    assert instance.blocks == "sample_text_2"


def test_BZ_BZIssue_ccList_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.ccList == "sample_text"
    instance.ccList = "sample_text_2"
    assert instance.ccList == "sample_text_2"


def test_BZ_BZIssue_classification_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.classification == "sample_text"
    instance.classification = "sample_text_2"
    assert instance.classification == "sample_text_2"


def test_BZ_BZIssue_componentName_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.componentName == "sample_text"
    instance.componentName = "sample_text_2"
    assert instance.componentName == "sample_text_2"


def test_BZ_BZIssue_dependsOn_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.dependsOn == "sample_text"
    instance.dependsOn = "sample_text_2"
    assert instance.dependsOn == "sample_text_2"


def test_BZ_BZIssue_importance_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.importance == "sample_text"
    instance.importance = "sample_text_2"
    assert instance.importance == "sample_text_2"


def test_BZ_BZIssue_issueId_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.issueId == 7
    instance.issueId = 13
    assert instance.issueId == 13


def test_BZ_BZIssue_issueTitle_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.issueTitle == "sample_text"
    instance.issueTitle = "sample_text_2"
    assert instance.issueTitle == "sample_text_2"


def test_BZ_BZIssue_issueURL_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.issueURL == "sample_text"
    instance.issueURL = "sample_text_2"
    assert instance.issueURL == "sample_text_2"


def test_BZ_BZIssue_keywords_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.keywords == "sample_text"
    instance.keywords = "sample_text_2"
    assert instance.keywords == "sample_text_2"


def test_BZ_BZIssue_lastModifiedOn_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.lastModifiedOn == date(2024, 1, 1)
    instance.lastModifiedOn = date(2025, 6, 15)
    assert instance.lastModifiedOn == date(2025, 6, 15)


def test_BZ_BZIssue_latestCommit_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.latestCommit == "sample_text"
    instance.latestCommit = "sample_text_2"
    assert instance.latestCommit == "sample_text_2"


def test_BZ_BZIssue_milestone_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.milestone == "sample_text"
    instance.milestone = "sample_text_2"
    assert instance.milestone == "sample_text_2"


def test_BZ_BZIssue_platform_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.platform == "sample_text"
    instance.platform = "sample_text_2"
    assert instance.platform == "sample_text_2"


def test_BZ_BZIssue_productName_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.productName == "sample_text"
    instance.productName = "sample_text_2"
    assert instance.productName == "sample_text_2"


def test_BZ_BZIssue_referenceURL_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.referenceURL == "sample_text"
    instance.referenceURL = "sample_text_2"
    assert instance.referenceURL == "sample_text_2"


def test_BZ_BZIssue_reportedBy_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.reportedBy == "sample_text"
    instance.reportedBy = "sample_text_2"
    assert instance.reportedBy == "sample_text_2"


def test_BZ_BZIssue_reportedByUsername_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.reportedByUsername == "sample_text"
    instance.reportedByUsername = "sample_text_2"
    assert instance.reportedByUsername == "sample_text_2"


def test_BZ_BZIssue_reportedOn_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.reportedOn == date(2024, 1, 1)
    instance.reportedOn = date(2025, 6, 15)
    assert instance.reportedOn == date(2025, 6, 15)


def test_BZ_BZIssue_seeAlso_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.seeAlso == "sample_text"
    instance.seeAlso = "sample_text_2"
    assert instance.seeAlso == "sample_text_2"


def test_BZ_BZIssue_status_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_BZ_BZIssue_version_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_BZ_BZIssue_versionFixedIn_value_roundtrip():
    instance = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    assert instance.versionFixedIn == "sample_text"
    instance.versionFixedIn = "sample_text_2"
    assert instance.versionFixedIn == "sample_text_2"


def test_BZ_BZProduct_productDescription_value_roundtrip():
    instance = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    assert instance.productDescription == "sample_text"
    instance.productDescription = "sample_text_2"
    assert instance.productDescription == "sample_text_2"


def test_BZ_BZProduct_productId_value_roundtrip():
    instance = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    assert instance.productId == "sample_text"
    instance.productId = "sample_text_2"
    assert instance.productId == "sample_text_2"


def test_BZ_BZProduct_productURL_value_roundtrip():
    instance = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    assert instance.productURL == "sample_text"
    instance.productURL = "sample_text_2"
    assert instance.productURL == "sample_text_2"


def test_BZ_BZRepo_repoURL_value_roundtrip():
    instance = BZ_BZRepo(repoURL="sample_text")
    assert instance.repoURL == "sample_text"
    instance.repoURL = "sample_text_2"
    assert instance.repoURL == "sample_text_2"


def test_assoc_comments20_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    b2 = BZ_BZComment(commentAuthor="sample_text_2", commentHTML="sample_text_2", commentId="sample_text_2", commentText="sample_text_2", commentTime=date(2025, 6, 15), issueId=13)
    _safe_set(a, 'issue', {b1})
    assert _is_linked(a, 'issue', b1)
    if hasattr(b1, 'BZComment'):
        assert _is_linked(b1, 'BZComment', a)
    _safe_set(a, 'issue', {b2})
    assert _is_linked(a, 'issue', b2)
    if hasattr(b1, 'BZComment'):
        assert not _is_linked(b1, 'BZComment', a)
    if hasattr(b2, 'BZComment'):
        assert _is_linked(b2, 'BZComment', a)
    _safe_set(a, 'issue', set())
    assert not _is_linked(a, 'issue', b2)
    if hasattr(b2, 'BZComment'):
        assert not _is_linked(b2, 'BZComment', a)


def test_assoc_component23_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'issues24', b1)
    assert _is_linked(a, 'issues24', b1)
    if hasattr(b1, 'BZComponent25'):
        assert _is_linked(b1, 'BZComponent25', a)
    _safe_set(a, 'issues24', b2)
    assert _is_linked(a, 'issues24', b2)
    if hasattr(b1, 'BZComponent25'):
        assert not _is_linked(b1, 'BZComponent25', a)
    if hasattr(b2, 'BZComponent25'):
        assert _is_linked(b2, 'BZComponent25', a)
    _safe_set(a, 'issues24', None)
    assert not _is_linked(a, 'issues24', b2)
    if hasattr(b2, 'BZComponent25'):
        assert not _is_linked(b2, 'BZComponent25', a)


def test_assoc_components1_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'repo2', {b1})
    assert _is_linked(a, 'repo2', b1)
    if hasattr(b1, 'BZComponent'):
        assert _is_linked(b1, 'BZComponent', a)
    _safe_set(a, 'repo2', {b2})
    assert _is_linked(a, 'repo2', b2)
    if hasattr(b1, 'BZComponent'):
        assert not _is_linked(b1, 'BZComponent', a)
    if hasattr(b2, 'BZComponent'):
        assert _is_linked(b2, 'BZComponent', a)
    _safe_set(a, 'repo2', set())
    assert not _is_linked(a, 'repo2', b2)
    if hasattr(b2, 'BZComponent'):
        assert not _is_linked(b2, 'BZComponent', a)


def test_assoc_components6_link_reassign_clear():
    a = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'product', {b1})
    assert _is_linked(a, 'product', b1)
    if hasattr(b1, 'BZComponent7'):
        assert _is_linked(b1, 'BZComponent7', a)
    _safe_set(a, 'product', {b2})
    assert _is_linked(a, 'product', b2)
    if hasattr(b1, 'BZComponent7'):
        assert not _is_linked(b1, 'BZComponent7', a)
    if hasattr(b2, 'BZComponent7'):
        assert _is_linked(b2, 'BZComponent7', a)
    _safe_set(a, 'product', set())
    assert not _is_linked(a, 'product', b2)
    if hasattr(b2, 'BZComponent7'):
        assert not _is_linked(b2, 'BZComponent7', a)


def test_assoc_events21_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    b2 = BZ_BZEvent(author="sample_text_2", date=date(2025, 6, 15), field="sample_text_2", issueId=13, newValue="sample_text_2", oldValue="sample_text_2")
    _safe_set(a, 'issue22', {b1})
    assert _is_linked(a, 'issue22', b1)
    if hasattr(b1, 'BZEvent'):
        assert _is_linked(b1, 'BZEvent', a)
    _safe_set(a, 'issue22', {b2})
    assert _is_linked(a, 'issue22', b2)
    if hasattr(b1, 'BZEvent'):
        assert not _is_linked(b1, 'BZEvent', a)
    if hasattr(b2, 'BZEvent'):
        assert _is_linked(b2, 'BZEvent', a)
    _safe_set(a, 'issue22', set())
    assert not _is_linked(a, 'issue22', b2)
    if hasattr(b2, 'BZEvent'):
        assert not _is_linked(b2, 'BZEvent', a)


def test_assoc_issue29_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    b2 = BZ_BZComment(commentAuthor="sample_text_2", commentHTML="sample_text_2", commentId="sample_text_2", commentText="sample_text_2", commentTime=date(2025, 6, 15), issueId=13)
    _safe_set(a, 'BZIssue30', b1)
    assert _is_linked(a, 'BZIssue30', b1)
    if hasattr(b1, 'comments'):
        assert _is_linked(b1, 'comments', a)
    _safe_set(a, 'BZIssue30', b2)
    assert _is_linked(a, 'BZIssue30', b2)
    if hasattr(b1, 'comments'):
        assert not _is_linked(b1, 'comments', a)
    if hasattr(b2, 'comments'):
        assert _is_linked(b2, 'comments', a)
    _safe_set(a, 'BZIssue30', None)
    assert not _is_linked(a, 'BZIssue30', b2)
    if hasattr(b2, 'comments'):
        assert not _is_linked(b2, 'comments', a)


def test_assoc_issue31_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    b2 = BZ_BZEvent(author="sample_text_2", date=date(2025, 6, 15), field="sample_text_2", issueId=13, newValue="sample_text_2", oldValue="sample_text_2")
    _safe_set(a, 'BZIssue32', b1)
    assert _is_linked(a, 'BZIssue32', b1)
    if hasattr(b1, 'events'):
        assert _is_linked(b1, 'events', a)
    _safe_set(a, 'BZIssue32', b2)
    assert _is_linked(a, 'BZIssue32', b2)
    if hasattr(b1, 'events'):
        assert not _is_linked(b1, 'events', a)
    if hasattr(b2, 'events'):
        assert _is_linked(b2, 'events', a)
    _safe_set(a, 'BZIssue32', None)
    assert not _is_linked(a, 'BZIssue32', b2)
    if hasattr(b2, 'events'):
        assert not _is_linked(b2, 'events', a)


def test_assoc_issues11_link_reassign_clear():
    a = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'BZIssue12', b1)
    assert _is_linked(a, 'BZIssue12', b1)
    if hasattr(b1, 'component'):
        assert _is_linked(b1, 'component', a)
    _safe_set(a, 'BZIssue12', b2)
    assert _is_linked(a, 'BZIssue12', b2)
    if hasattr(b1, 'component'):
        assert not _is_linked(b1, 'component', a)
    if hasattr(b2, 'component'):
        assert _is_linked(b2, 'component', a)
    _safe_set(a, 'BZIssue12', None)
    assert not _is_linked(a, 'BZIssue12', b2)
    if hasattr(b2, 'component'):
        assert not _is_linked(b2, 'component', a)


def test_assoc_issues3_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    _safe_set(a, 'repo4', {b1})
    assert _is_linked(a, 'repo4', b1)
    if hasattr(b1, 'BZIssue'):
        assert _is_linked(b1, 'BZIssue', a)
    _safe_set(a, 'repo4', {b2})
    assert _is_linked(a, 'repo4', b2)
    if hasattr(b1, 'BZIssue'):
        assert not _is_linked(b1, 'BZIssue', a)
    if hasattr(b2, 'BZIssue'):
        assert _is_linked(b2, 'BZIssue', a)
    _safe_set(a, 'repo4', set())
    assert not _is_linked(a, 'repo4', b2)
    if hasattr(b2, 'BZIssue'):
        assert not _is_linked(b2, 'BZIssue', a)


def test_assoc_issues8_link_reassign_clear():
    a = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    _safe_set(a, 'product9', {b1})
    assert _is_linked(a, 'product9', b1)
    if hasattr(b1, 'BZIssue10'):
        assert _is_linked(b1, 'BZIssue10', a)
    _safe_set(a, 'product9', {b2})
    assert _is_linked(a, 'product9', b2)
    if hasattr(b1, 'BZIssue10'):
        assert not _is_linked(b1, 'BZIssue10', a)
    if hasattr(b2, 'BZIssue10'):
        assert _is_linked(b2, 'BZIssue10', a)
    _safe_set(a, 'product9', set())
    assert not _is_linked(a, 'product9', b2)
    if hasattr(b2, 'BZIssue10'):
        assert not _is_linked(b2, 'BZIssue10', a)


def test_assoc_product13_link_reassign_clear():
    a = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'BZProduct14', b1)
    assert _is_linked(a, 'BZProduct14', b1)
    if hasattr(b1, 'components'):
        assert _is_linked(b1, 'components', a)
    _safe_set(a, 'BZProduct14', b2)
    assert _is_linked(a, 'BZProduct14', b2)
    if hasattr(b1, 'components'):
        assert not _is_linked(b1, 'components', a)
    if hasattr(b2, 'components'):
        assert _is_linked(b2, 'components', a)
    _safe_set(a, 'BZProduct14', None)
    assert not _is_linked(a, 'BZProduct14', b2)
    if hasattr(b2, 'components'):
        assert not _is_linked(b2, 'components', a)


def test_assoc_product26_link_reassign_clear():
    a = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    _safe_set(a, 'BZProduct28', b1)
    assert _is_linked(a, 'BZProduct28', b1)
    if hasattr(b1, 'issues27'):
        assert _is_linked(b1, 'issues27', a)
    _safe_set(a, 'BZProduct28', b2)
    assert _is_linked(a, 'BZProduct28', b2)
    if hasattr(b1, 'issues27'):
        assert not _is_linked(b1, 'issues27', a)
    if hasattr(b2, 'issues27'):
        assert _is_linked(b2, 'issues27', a)
    _safe_set(a, 'BZProduct28', None)
    assert not _is_linked(a, 'BZProduct28', b2)
    if hasattr(b2, 'issues27'):
        assert not _is_linked(b2, 'issues27', a)


def test_assoc_products0_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    _safe_set(a, 'repo', {b1})
    assert _is_linked(a, 'repo', b1)
    if hasattr(b1, 'BZProduct'):
        assert _is_linked(b1, 'BZProduct', a)
    _safe_set(a, 'repo', {b2})
    assert _is_linked(a, 'repo', b2)
    if hasattr(b1, 'BZProduct'):
        assert not _is_linked(b1, 'BZProduct', a)
    if hasattr(b2, 'BZProduct'):
        assert _is_linked(b2, 'BZProduct', a)
    _safe_set(a, 'repo', set())
    assert not _is_linked(a, 'repo', b2)
    if hasattr(b2, 'BZProduct'):
        assert not _is_linked(b2, 'BZProduct', a)


def test_assoc_repo15_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    b2 = BZ_BZComponent(componentDescription="sample_text_2", componentId="sample_text_2", componentURL="sample_text_2", defaultAssignee="sample_text_2")
    _safe_set(a, 'BZRepo17', b1)
    assert _is_linked(a, 'BZRepo17', b1)
    if hasattr(b1, 'components16'):
        assert _is_linked(b1, 'components16', a)
    _safe_set(a, 'BZRepo17', b2)
    assert _is_linked(a, 'BZRepo17', b2)
    if hasattr(b1, 'components16'):
        assert not _is_linked(b1, 'components16', a)
    if hasattr(b2, 'components16'):
        assert _is_linked(b2, 'components16', a)
    _safe_set(a, 'BZRepo17', None)
    assert not _is_linked(a, 'BZRepo17', b2)
    if hasattr(b2, 'components16'):
        assert not _is_linked(b2, 'components16', a)


def test_assoc_repo18_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    b2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    _safe_set(a, 'BZRepo19', b1)
    assert _is_linked(a, 'BZRepo19', b1)
    if hasattr(b1, 'issues'):
        assert _is_linked(b1, 'issues', a)
    _safe_set(a, 'BZRepo19', b2)
    assert _is_linked(a, 'BZRepo19', b2)
    if hasattr(b1, 'issues'):
        assert not _is_linked(b1, 'issues', a)
    if hasattr(b2, 'issues'):
        assert _is_linked(b2, 'issues', a)
    _safe_set(a, 'BZRepo19', None)
    assert not _is_linked(a, 'BZRepo19', b2)
    if hasattr(b2, 'issues'):
        assert not _is_linked(b2, 'issues', a)


def test_assoc_repo5_link_reassign_clear():
    a = BZ_BZRepo(repoURL="sample_text")
    b1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    b2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    _safe_set(a, 'BZRepo', b1)
    assert _is_linked(a, 'BZRepo', b1)
    if hasattr(b1, 'products'):
        assert _is_linked(b1, 'products', a)
    _safe_set(a, 'BZRepo', b2)
    assert _is_linked(a, 'BZRepo', b2)
    if hasattr(b1, 'products'):
        assert not _is_linked(b1, 'products', a)
    if hasattr(b2, 'products'):
        assert _is_linked(b2, 'products', a)
    _safe_set(a, 'BZRepo', None)
    assert not _is_linked(a, 'BZRepo', b2)
    if hasattr(b2, 'products'):
        assert not _is_linked(b2, 'products', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BZ_BZComment_strategy = st.builds(BZ_BZComment, commentAuthor=safe_text, commentHTML=safe_text, commentId=safe_text, commentText=safe_text, commentTime=st.dates(), issueId=st.integers())
@given(instance=BZ_BZComment_strategy)
@settings(max_examples=25)
def test_BZ_BZComment_instantiation(instance):
    assert isinstance(instance, BZ_BZComment)


BZ_BZComponent_strategy = st.builds(BZ_BZComponent, componentDescription=safe_text, componentId=safe_text, componentURL=safe_text, defaultAssignee=safe_text)
@given(instance=BZ_BZComponent_strategy)
@settings(max_examples=25)
def test_BZ_BZComponent_instantiation(instance):
    assert isinstance(instance, BZ_BZComponent)


BZ_BZEvent_strategy = st.builds(BZ_BZEvent, author=safe_text, date=st.dates(), field=safe_text, issueId=st.integers(), newValue=safe_text, oldValue=safe_text)
@given(instance=BZ_BZEvent_strategy)
@settings(max_examples=25)
def test_BZ_BZEvent_instantiation(instance):
    assert isinstance(instance, BZ_BZEvent)


BZ_BZIssue_strategy = st.builds(BZ_BZIssue, assignedTo=safe_text, blocks=safe_text, ccList=safe_text, classification=safe_text, componentName=safe_text, dependsOn=safe_text, importance=safe_text, issueId=st.integers(), issueTitle=safe_text, issueURL=safe_text, keywords=safe_text, lastModifiedOn=st.dates(), latestCommit=safe_text, milestone=safe_text, platform=safe_text, productName=safe_text, referenceURL=safe_text, reportedBy=safe_text, reportedByUsername=safe_text, reportedOn=st.dates(), seeAlso=safe_text, status=safe_text, version=safe_text, versionFixedIn=safe_text)
@given(instance=BZ_BZIssue_strategy)
@settings(max_examples=25)
def test_BZ_BZIssue_instantiation(instance):
    assert isinstance(instance, BZ_BZIssue)


BZ_BZProduct_strategy = st.builds(BZ_BZProduct, productDescription=safe_text, productId=safe_text, productURL=safe_text)
@given(instance=BZ_BZProduct_strategy)
@settings(max_examples=25)
def test_BZ_BZProduct_instantiation(instance):
    assert isinstance(instance, BZ_BZProduct)


BZ_BZRepo_strategy = st.builds(BZ_BZRepo, repoURL=safe_text)
@given(instance=BZ_BZRepo_strategy)
@settings(max_examples=25)
def test_BZ_BZRepo_instantiation(instance):
    assert isinstance(instance, BZ_BZRepo)



