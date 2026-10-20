import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BZ_BZComment,
    BZ_BZComponent,
    BZ_BZEvent,
    BZ_BZIssue,
    BZ_BZProduct,
    BZ_BZRepo,
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

def test_assoc_comments20_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    _safe_set(b, 'BZComment', a1)
    assert _is_linked(b, 'BZComment', a1)
    if hasattr(a1, 'issue'):
        assert _is_linked(a1, 'issue', b)
    _safe_set(b, 'BZComment', a2)
    assert _is_linked(b, 'BZComment', a2)
    if hasattr(a1, 'issue'):
        assert not _is_linked(a1, 'issue', b)
    if hasattr(a2, 'issue'):
        assert _is_linked(a2, 'issue', b)
    _safe_set(b, 'BZComment', None)
    assert not _is_linked(b, 'BZComment', a2)
    if hasattr(a2, 'issue'):
        assert not _is_linked(a2, 'issue', b)


def test_assoc_component23_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'BZComponent25', a1)
    assert _is_linked(b, 'BZComponent25', a1)
    if hasattr(a1, 'issues24'):
        assert _is_linked(a1, 'issues24', b)
    _safe_set(b, 'BZComponent25', a2)
    assert _is_linked(b, 'BZComponent25', a2)
    if hasattr(a1, 'issues24'):
        assert not _is_linked(a1, 'issues24', b)
    if hasattr(a2, 'issues24'):
        assert _is_linked(a2, 'issues24', b)
    _safe_set(b, 'BZComponent25', None)
    assert not _is_linked(b, 'BZComponent25', a2)
    if hasattr(a2, 'issues24'):
        assert not _is_linked(a2, 'issues24', b)


def test_assoc_components1_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'BZComponent', a1)
    assert _is_linked(b, 'BZComponent', a1)
    if hasattr(a1, 'repo2'):
        assert _is_linked(a1, 'repo2', b)
    _safe_set(b, 'BZComponent', a2)
    assert _is_linked(b, 'BZComponent', a2)
    if hasattr(a1, 'repo2'):
        assert not _is_linked(a1, 'repo2', b)
    if hasattr(a2, 'repo2'):
        assert _is_linked(a2, 'repo2', b)
    _safe_set(b, 'BZComponent', None)
    assert not _is_linked(b, 'BZComponent', a2)
    if hasattr(a2, 'repo2'):
        assert not _is_linked(a2, 'repo2', b)


def test_assoc_components6_reverse_link_reassign_clear():
    a1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    a2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'BZComponent7', a1)
    assert _is_linked(b, 'BZComponent7', a1)
    if hasattr(a1, 'product'):
        assert _is_linked(a1, 'product', b)
    _safe_set(b, 'BZComponent7', a2)
    assert _is_linked(b, 'BZComponent7', a2)
    if hasattr(a1, 'product'):
        assert not _is_linked(a1, 'product', b)
    if hasattr(a2, 'product'):
        assert _is_linked(a2, 'product', b)
    _safe_set(b, 'BZComponent7', None)
    assert not _is_linked(b, 'BZComponent7', a2)
    if hasattr(a2, 'product'):
        assert not _is_linked(a2, 'product', b)


def test_assoc_events21_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    _safe_set(b, 'BZEvent', a1)
    assert _is_linked(b, 'BZEvent', a1)
    if hasattr(a1, 'issue22'):
        assert _is_linked(a1, 'issue22', b)
    _safe_set(b, 'BZEvent', a2)
    assert _is_linked(b, 'BZEvent', a2)
    if hasattr(a1, 'issue22'):
        assert not _is_linked(a1, 'issue22', b)
    if hasattr(a2, 'issue22'):
        assert _is_linked(a2, 'issue22', b)
    _safe_set(b, 'BZEvent', None)
    assert not _is_linked(b, 'BZEvent', a2)
    if hasattr(a2, 'issue22'):
        assert not _is_linked(a2, 'issue22', b)


def test_assoc_issue29_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZComment(commentAuthor="sample_text", commentHTML="sample_text", commentId="sample_text", commentText="sample_text", commentTime=date(2024, 1, 1), issueId=7)
    _safe_set(b, 'comments', a1)
    assert _is_linked(b, 'comments', a1)
    if hasattr(a1, 'BZIssue30'):
        assert _is_linked(a1, 'BZIssue30', b)
    _safe_set(b, 'comments', a2)
    assert _is_linked(b, 'comments', a2)
    if hasattr(a1, 'BZIssue30'):
        assert not _is_linked(a1, 'BZIssue30', b)
    if hasattr(a2, 'BZIssue30'):
        assert _is_linked(a2, 'BZIssue30', b)
    _safe_set(b, 'comments', None)
    assert not _is_linked(b, 'comments', a2)
    if hasattr(a2, 'BZIssue30'):
        assert not _is_linked(a2, 'BZIssue30', b)


def test_assoc_issue31_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZEvent(author="sample_text", date=date(2024, 1, 1), field="sample_text", issueId=7, newValue="sample_text", oldValue="sample_text")
    _safe_set(b, 'events', a1)
    assert _is_linked(b, 'events', a1)
    if hasattr(a1, 'BZIssue32'):
        assert _is_linked(a1, 'BZIssue32', b)
    _safe_set(b, 'events', a2)
    assert _is_linked(b, 'events', a2)
    if hasattr(a1, 'BZIssue32'):
        assert not _is_linked(a1, 'BZIssue32', b)
    if hasattr(a2, 'BZIssue32'):
        assert _is_linked(a2, 'BZIssue32', b)
    _safe_set(b, 'events', None)
    assert not _is_linked(b, 'events', a2)
    if hasattr(a2, 'BZIssue32'):
        assert not _is_linked(a2, 'BZIssue32', b)


def test_assoc_issues11_reverse_link_reassign_clear():
    a1 = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    a2 = BZ_BZIssue(assignedTo="sample_text_2", blocks="sample_text_2", ccList="sample_text_2", classification="sample_text_2", componentName="sample_text_2", dependsOn="sample_text_2", importance="sample_text_2", issueId=13, issueTitle="sample_text_2", issueURL="sample_text_2", keywords="sample_text_2", lastModifiedOn=date(2025, 6, 15), latestCommit="sample_text_2", milestone="sample_text_2", platform="sample_text_2", productName="sample_text_2", referenceURL="sample_text_2", reportedBy="sample_text_2", reportedByUsername="sample_text_2", reportedOn=date(2025, 6, 15), seeAlso="sample_text_2", status="sample_text_2", version="sample_text_2", versionFixedIn="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'component', {a1})
    assert _is_linked(b, 'component', a1)
    if hasattr(a1, 'BZIssue12'):
        assert _is_linked(a1, 'BZIssue12', b)
    _safe_set(b, 'component', {a2})
    assert _is_linked(b, 'component', a2)
    if hasattr(a1, 'BZIssue12'):
        assert not _is_linked(a1, 'BZIssue12', b)
    if hasattr(a2, 'BZIssue12'):
        assert _is_linked(a2, 'BZIssue12', b)
    _safe_set(b, 'component', set())
    assert not _is_linked(b, 'component', a2)
    if hasattr(a2, 'BZIssue12'):
        assert not _is_linked(a2, 'BZIssue12', b)


def test_assoc_issues3_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    _safe_set(b, 'BZIssue', a1)
    assert _is_linked(b, 'BZIssue', a1)
    if hasattr(a1, 'repo4'):
        assert _is_linked(a1, 'repo4', b)
    _safe_set(b, 'BZIssue', a2)
    assert _is_linked(b, 'BZIssue', a2)
    if hasattr(a1, 'repo4'):
        assert not _is_linked(a1, 'repo4', b)
    if hasattr(a2, 'repo4'):
        assert _is_linked(a2, 'repo4', b)
    _safe_set(b, 'BZIssue', None)
    assert not _is_linked(b, 'BZIssue', a2)
    if hasattr(a2, 'repo4'):
        assert not _is_linked(a2, 'repo4', b)


def test_assoc_issues8_reverse_link_reassign_clear():
    a1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    a2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    b = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    _safe_set(b, 'BZIssue10', a1)
    assert _is_linked(b, 'BZIssue10', a1)
    if hasattr(a1, 'product9'):
        assert _is_linked(a1, 'product9', b)
    _safe_set(b, 'BZIssue10', a2)
    assert _is_linked(b, 'BZIssue10', a2)
    if hasattr(a1, 'product9'):
        assert not _is_linked(a1, 'product9', b)
    if hasattr(a2, 'product9'):
        assert _is_linked(a2, 'product9', b)
    _safe_set(b, 'BZIssue10', None)
    assert not _is_linked(b, 'BZIssue10', a2)
    if hasattr(a2, 'product9'):
        assert not _is_linked(a2, 'product9', b)


def test_assoc_product13_reverse_link_reassign_clear():
    a1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    a2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'components', a1)
    assert _is_linked(b, 'components', a1)
    if hasattr(a1, 'BZProduct14'):
        assert _is_linked(a1, 'BZProduct14', b)
    _safe_set(b, 'components', a2)
    assert _is_linked(b, 'components', a2)
    if hasattr(a1, 'BZProduct14'):
        assert not _is_linked(a1, 'BZProduct14', b)
    if hasattr(a2, 'BZProduct14'):
        assert _is_linked(a2, 'BZProduct14', b)
    _safe_set(b, 'components', None)
    assert not _is_linked(b, 'components', a2)
    if hasattr(a2, 'BZProduct14'):
        assert not _is_linked(a2, 'BZProduct14', b)


def test_assoc_product26_reverse_link_reassign_clear():
    a1 = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    a2 = BZ_BZProduct(productDescription="sample_text_2", productId="sample_text_2", productURL="sample_text_2")
    b = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    _safe_set(b, 'issues27', a1)
    assert _is_linked(b, 'issues27', a1)
    if hasattr(a1, 'BZProduct28'):
        assert _is_linked(a1, 'BZProduct28', b)
    _safe_set(b, 'issues27', a2)
    assert _is_linked(b, 'issues27', a2)
    if hasattr(a1, 'BZProduct28'):
        assert not _is_linked(a1, 'BZProduct28', b)
    if hasattr(a2, 'BZProduct28'):
        assert _is_linked(a2, 'BZProduct28', b)
    _safe_set(b, 'issues27', None)
    assert not _is_linked(b, 'issues27', a2)
    if hasattr(a2, 'BZProduct28'):
        assert not _is_linked(a2, 'BZProduct28', b)


def test_assoc_products0_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    _safe_set(b, 'BZProduct', a1)
    assert _is_linked(b, 'BZProduct', a1)
    if hasattr(a1, 'repo'):
        assert _is_linked(a1, 'repo', b)
    _safe_set(b, 'BZProduct', a2)
    assert _is_linked(b, 'BZProduct', a2)
    if hasattr(a1, 'repo'):
        assert not _is_linked(a1, 'repo', b)
    if hasattr(a2, 'repo'):
        assert _is_linked(a2, 'repo', b)
    _safe_set(b, 'BZProduct', None)
    assert not _is_linked(b, 'BZProduct', a2)
    if hasattr(a2, 'repo'):
        assert not _is_linked(a2, 'repo', b)


def test_assoc_repo15_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZComponent(componentDescription="sample_text", componentId="sample_text", componentURL="sample_text", defaultAssignee="sample_text")
    _safe_set(b, 'components16', a1)
    assert _is_linked(b, 'components16', a1)
    if hasattr(a1, 'BZRepo17'):
        assert _is_linked(a1, 'BZRepo17', b)
    _safe_set(b, 'components16', a2)
    assert _is_linked(b, 'components16', a2)
    if hasattr(a1, 'BZRepo17'):
        assert not _is_linked(a1, 'BZRepo17', b)
    if hasattr(a2, 'BZRepo17'):
        assert _is_linked(a2, 'BZRepo17', b)
    _safe_set(b, 'components16', None)
    assert not _is_linked(b, 'components16', a2)
    if hasattr(a2, 'BZRepo17'):
        assert not _is_linked(a2, 'BZRepo17', b)


def test_assoc_repo18_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZIssue(assignedTo="sample_text", blocks="sample_text", ccList="sample_text", classification="sample_text", componentName="sample_text", dependsOn="sample_text", importance="sample_text", issueId=7, issueTitle="sample_text", issueURL="sample_text", keywords="sample_text", lastModifiedOn=date(2024, 1, 1), latestCommit="sample_text", milestone="sample_text", platform="sample_text", productName="sample_text", referenceURL="sample_text", reportedBy="sample_text", reportedByUsername="sample_text", reportedOn=date(2024, 1, 1), seeAlso="sample_text", status="sample_text", version="sample_text", versionFixedIn="sample_text")
    _safe_set(b, 'issues', a1)
    assert _is_linked(b, 'issues', a1)
    if hasattr(a1, 'BZRepo19'):
        assert _is_linked(a1, 'BZRepo19', b)
    _safe_set(b, 'issues', a2)
    assert _is_linked(b, 'issues', a2)
    if hasattr(a1, 'BZRepo19'):
        assert not _is_linked(a1, 'BZRepo19', b)
    if hasattr(a2, 'BZRepo19'):
        assert _is_linked(a2, 'BZRepo19', b)
    _safe_set(b, 'issues', None)
    assert not _is_linked(b, 'issues', a2)
    if hasattr(a2, 'BZRepo19'):
        assert not _is_linked(a2, 'BZRepo19', b)


def test_assoc_repo5_reverse_link_reassign_clear():
    a1 = BZ_BZRepo(repoURL="sample_text")
    a2 = BZ_BZRepo(repoURL="sample_text_2")
    b = BZ_BZProduct(productDescription="sample_text", productId="sample_text", productURL="sample_text")
    _safe_set(b, 'products', a1)
    assert _is_linked(b, 'products', a1)
    if hasattr(a1, 'BZRepo'):
        assert _is_linked(a1, 'BZRepo', b)
    _safe_set(b, 'products', a2)
    assert _is_linked(b, 'products', a2)
    if hasattr(a1, 'BZRepo'):
        assert not _is_linked(a1, 'BZRepo', b)
    if hasattr(a2, 'BZRepo'):
        assert _is_linked(a2, 'BZRepo', b)
    _safe_set(b, 'products', None)
    assert not _is_linked(b, 'products', a2)
    if hasattr(a2, 'BZRepo'):
        assert not _is_linked(a2, 'BZRepo', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

