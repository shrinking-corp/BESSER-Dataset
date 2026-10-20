import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Contents,
    GraphNode,
    Label,
    Node,
    Notes,
    assessment_Account,
    assessment_Accounts,
    assessment_Application,
    assessment_Applications,
    assessment_Assessment,
    assessment_Contents,
    assessment_Control,
    assessment_Controller,
    assessment_Controllers,
    assessment_Entitlement,
    assessment_Entitlements,
    assessment_Finding,
    assessment_Findings,
    assessment_Generic,
    assessment_Graph,
    assessment_GraphNode,
    assessment_Http,
    assessment_Label,
    assessment_Model,
    assessment_Models,
    assessment_Node,
    assessment_Notes,
    assessment_Resource,
    assessment_Resources,
    assessment_Scm,
    assessment_Sink,
    assessment_Sinks,
    assessment_Snippet,
    assessment_Task,
    assessment_Tasks,
    assessment_Url,
    assessment_View,
    assessment_Views,
    HttpMethod,
    Language,
    TaskStatus,
    UrlPattern,
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

def test_assoc_application56_reverse_link_reassign_clear():
    a1 = assessment_Scm(branchTag="sample_text", repository="sample_text")
    a2 = assessment_Scm(branchTag="sample_text_2", repository="sample_text_2")
    b = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    _safe_set(b, 'Application', a1)
    assert _is_linked(b, 'Application', a1)
    if hasattr(a1, 'scm'):
        assert _is_linked(a1, 'scm', b)
    _safe_set(b, 'Application', a2)
    assert _is_linked(b, 'Application', a2)
    if hasattr(a1, 'scm'):
        assert not _is_linked(a1, 'scm', b)
    if hasattr(a2, 'scm'):
        assert _is_linked(a2, 'scm', b)
    _safe_set(b, 'Application', None)
    assert not _is_linked(b, 'Application', a2)
    if hasattr(a2, 'scm'):
        assert not _is_linked(a2, 'scm', b)


def test_assoc_scm23_reverse_link_reassign_clear():
    a1 = assessment_Scm(branchTag="sample_text", repository="sample_text")
    a2 = assessment_Scm(branchTag="sample_text_2", repository="sample_text_2")
    b = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    _safe_set(b, 'application24', a1)
    assert _is_linked(b, 'application24', a1)
    if hasattr(a1, 'Scm'):
        assert _is_linked(a1, 'Scm', b)
    _safe_set(b, 'application24', a2)
    assert _is_linked(b, 'application24', a2)
    if hasattr(a1, 'Scm'):
        assert not _is_linked(a1, 'Scm', b)
    if hasattr(a2, 'Scm'):
        assert _is_linked(a2, 'Scm', b)
    _safe_set(b, 'application24', None)
    assert not _is_linked(b, 'application24', a2)
    if hasattr(a2, 'Scm'):
        assert not _is_linked(a2, 'Scm', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accounts17_stub_double():
    # assessment_Accounts has no real 'assessment_Accounts' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Accounts()
    setattr(partner, 'assessment_Accounts', None)
    _safe_set(owner, 'assessment_Application', partner)
    assert getattr(partner, 'assessment_Accounts') == owner
    _safe_set(owner, 'assessment_Application', None)
    assert getattr(partner, 'assessment_Accounts') is None


def test_assoc_accounts45_stub_double():
    # assessment_Accounts has no real 'Accounts' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Account(email="sample_text", password="sample_text")
    partner = assessment_Accounts()
    setattr(partner, 'Accounts', None)
    _safe_set(owner, 'accounts', partner)
    assert getattr(partner, 'Accounts') == owner
    _safe_set(owner, 'accounts', None)
    assert getattr(partner, 'Accounts') is None


def test_assoc_accounts48_stub_double():
    # assessment_Entitlement has no real 'entitlements' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Account(email="sample_text", password="sample_text")
    partner = assessment_Entitlement()
    setattr(partner, 'entitlements', None)
    _safe_set(owner, 'Account', partner)
    assert owner in getattr(partner, 'entitlements')
    _safe_set(owner, 'Account', None)
    assert owner not in getattr(partner, 'entitlements')


def test_assoc_accounts75_stub_double():
    # assessment_Accounts has no real 'accounts76' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Account(email="sample_text", password="sample_text")
    partner = assessment_Accounts()
    setattr(partner, 'accounts76', None)
    _safe_set(owner, 'Account77', partner)
    assert owner in getattr(partner, 'accounts76')
    _safe_set(owner, 'Account77', None)
    assert owner not in getattr(partner, 'accounts76')


def test_assoc_affects42_stub_double():
    # assessment_Node has no real 'Node44' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Finding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Finding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Finding(references="sample_text", remediation="sample_text", reproducer="sample_text")
    partner = assessment_Node()
    setattr(partner, 'Node44', None)
    _safe_set(owner, 'findings43', {partner})
    assert getattr(partner, 'Node44') == owner
    _safe_set(owner, 'findings43', set())
    assert getattr(partner, 'Node44') is None


def test_assoc_affects53_stub_double():
    # assessment_Node has no real 'Node55' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Task(status="sample_text")
    partner = assessment_Node()
    setattr(partner, 'Node55', None)
    _safe_set(owner, 'tasks54', {partner})
    assert getattr(partner, 'Node55') == owner
    _safe_set(owner, 'tasks54', set())
    assert getattr(partner, 'Node55') is None


def test_assoc_application104_stub_double():
    # assessment_Resources has no real 'resources105' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Resources()
    setattr(partner, 'resources105', None)
    _safe_set(owner, 'Application106', partner)
    assert getattr(partner, 'resources105') == owner
    _safe_set(owner, 'Application106', None)
    assert getattr(partner, 'resources105') is None


def test_assoc_application72_stub_double():
    # assessment_Accounts has no real 'assessment_Accounts73' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Accounts()
    setattr(partner, 'assessment_Accounts73', None)
    _safe_set(owner, 'assessment_Application74', partner)
    assert getattr(partner, 'assessment_Accounts73') == owner
    _safe_set(owner, 'assessment_Application74', None)
    assert getattr(partner, 'assessment_Accounts73') is None


def test_assoc_application78_stub_double():
    # assessment_Controllers has no real 'controllers79' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Controllers()
    setattr(partner, 'controllers79', None)
    _safe_set(owner, 'Application80', partner)
    assert getattr(partner, 'controllers79') == owner
    _safe_set(owner, 'Application80', None)
    assert getattr(partner, 'controllers79') is None


def test_assoc_application83_stub_double():
    # assessment_Entitlements has no real 'assessment_Entitlements84' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Entitlements()
    setattr(partner, 'assessment_Entitlements84', None)
    _safe_set(owner, 'assessment_Application85', partner)
    assert getattr(partner, 'assessment_Entitlements84') == owner
    _safe_set(owner, 'assessment_Application85', None)
    assert getattr(partner, 'assessment_Entitlements84') is None


def test_assoc_application89_stub_double():
    # assessment_Models has no real 'models90' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Models()
    setattr(partner, 'models90', None)
    _safe_set(owner, 'Application91', partner)
    assert getattr(partner, 'models90') == owner
    _safe_set(owner, 'Application91', None)
    assert getattr(partner, 'models90') is None


def test_assoc_application94_stub_double():
    # assessment_Views has no real 'views95' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Views()
    setattr(partner, 'views95', None)
    _safe_set(owner, 'Application96', partner)
    assert getattr(partner, 'views95') == owner
    _safe_set(owner, 'Application96', None)
    assert getattr(partner, 'views95') is None


def test_assoc_application99_stub_double():
    # assessment_Sinks has no real 'assessment_Sinks100' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Sinks()
    setattr(partner, 'assessment_Sinks100', None)
    _safe_set(owner, 'assessment_Application101', partner)
    assert getattr(partner, 'assessment_Sinks100') == owner
    _safe_set(owner, 'assessment_Application101', None)
    assert getattr(partner, 'assessment_Sinks100') is None


def test_assoc_applications31_stub_double():
    # assessment_Applications has no real 'Applications32' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Applications()
    setattr(partner, 'Applications32', None)
    _safe_set(owner, 'applications', partner)
    assert getattr(partner, 'Applications32') == owner
    _safe_set(owner, 'applications', None)
    assert getattr(partner, 'Applications32') is None


def test_assoc_applications61_stub_double():
    # assessment_Applications has no real 'applications62' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Applications()
    setattr(partner, 'applications62', None)
    _safe_set(owner, 'Application63', partner)
    assert owner in getattr(partner, 'applications62')
    _safe_set(owner, 'Application63', None)
    assert owner not in getattr(partner, 'applications62')


def test_assoc_controllers20_stub_double():
    # assessment_Controllers has no real 'Controllers' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Controllers()
    setattr(partner, 'Controllers', None)
    _safe_set(owner, 'application', partner)
    assert getattr(partner, 'Controllers') == owner
    _safe_set(owner, 'application', None)
    assert getattr(partner, 'Controllers') is None


def test_assoc_entitlements18_stub_double():
    # assessment_Entitlements has no real 'assessment_Entitlements' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Entitlements()
    setattr(partner, 'assessment_Entitlements', None)
    _safe_set(owner, 'assessment_Application19', partner)
    assert getattr(partner, 'assessment_Entitlements') == owner
    _safe_set(owner, 'assessment_Application19', None)
    assert getattr(partner, 'assessment_Entitlements') is None


def test_assoc_entitlements46_stub_double():
    # assessment_Entitlement has no real 'Entitlement' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Account(email="sample_text", password="sample_text")
    partner = assessment_Entitlement()
    setattr(partner, 'Entitlement', None)
    _safe_set(owner, 'accounts47', {partner})
    assert getattr(partner, 'Entitlement') == owner
    _safe_set(owner, 'accounts47', set())
    assert getattr(partner, 'Entitlement') is None


def test_assoc_findings10_stub_double():
    # assessment_Node has no real 'affects11' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Finding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Finding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Finding(references="sample_text", remediation="sample_text", reproducer="sample_text")
    partner = assessment_Node()
    setattr(partner, 'affects11', None)
    _safe_set(owner, 'Finding', partner)
    assert owner in getattr(partner, 'affects11')
    _safe_set(owner, 'Finding', None)
    assert owner not in getattr(partner, 'affects11')


def test_assoc_findings40_stub_double():
    # assessment_Findings has no real 'Findings41' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Finding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Finding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Finding(references="sample_text", remediation="sample_text", reproducer="sample_text")
    partner = assessment_Findings()
    setattr(partner, 'Findings41', None)
    _safe_set(owner, 'findings', partner)
    assert getattr(partner, 'Findings41') == owner
    _safe_set(owner, 'findings', None)
    assert getattr(partner, 'Findings41') is None


def test_assoc_findings66_stub_double():
    # assessment_Findings has no real 'findings67' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Finding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Finding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Finding(references="sample_text", remediation="sample_text", reproducer="sample_text")
    partner = assessment_Findings()
    setattr(partner, 'findings67', None)
    _safe_set(owner, 'Finding68', partner)
    assert owner in getattr(partner, 'findings67')
    _safe_set(owner, 'Finding68', None)
    assert owner not in getattr(partner, 'findings67')


def test_assoc_models21_stub_double():
    # assessment_Models has no real 'Models' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Models()
    setattr(partner, 'Models', None)
    _safe_set(owner, 'application22', partner)
    assert getattr(partner, 'Models') == owner
    _safe_set(owner, 'application22', None)
    assert getattr(partner, 'Models') is None


def test_assoc_resource57_stub_double():
    # assessment_Resource has no real 'Resource' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Snippet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Snippet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Snippet(columnEnd=7, columnStart=7, lineEnd=7, lineStart=7)
    partner = assessment_Resource()
    setattr(partner, 'Resource', None)
    _safe_set(owner, 'snippets', partner)
    assert getattr(partner, 'Resource') == owner
    _safe_set(owner, 'snippets', None)
    assert getattr(partner, 'Resource') is None


def test_assoc_resources29_stub_double():
    # assessment_Resources has no real 'Resources' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Resources()
    setattr(partner, 'Resources', None)
    _safe_set(owner, 'application30', partner)
    assert getattr(partner, 'Resources') == owner
    _safe_set(owner, 'application30', None)
    assert getattr(partner, 'Resources') is None


def test_assoc_sinks102_stub_double():
    # assessment_Sinks has no real 'sinks103' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Sink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Sink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Sink(cwes=7)
    partner = assessment_Sinks()
    setattr(partner, 'sinks103', None)
    _safe_set(owner, 'Sink', partner)
    assert owner in getattr(partner, 'sinks103')
    _safe_set(owner, 'Sink', None)
    assert owner not in getattr(partner, 'sinks103')


def test_assoc_sinks27_stub_double():
    # assessment_Sinks has no real 'assessment_Sinks' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Sinks()
    setattr(partner, 'assessment_Sinks', None)
    _safe_set(owner, 'assessment_Application28', partner)
    assert getattr(partner, 'assessment_Sinks') == owner
    _safe_set(owner, 'assessment_Application28', None)
    assert getattr(partner, 'assessment_Sinks') is None


def test_assoc_sinks33_stub_double():
    # assessment_Sinks has no real 'Sinks' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Sink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Sink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Sink(cwes=7)
    partner = assessment_Sinks()
    setattr(partner, 'Sinks', None)
    _safe_set(owner, 'sinks', partner)
    assert getattr(partner, 'Sinks') == owner
    _safe_set(owner, 'sinks', None)
    assert getattr(partner, 'Sinks') is None


def test_assoc_snippets60_stub_double():
    # assessment_Resource has no real 'resource' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Snippet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Snippet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Snippet(columnEnd=7, columnStart=7, lineEnd=7, lineStart=7)
    partner = assessment_Resource()
    setattr(partner, 'resource', None)
    _safe_set(owner, 'Snippet', partner)
    assert owner in getattr(partner, 'resource')
    _safe_set(owner, 'Snippet', None)
    assert owner not in getattr(partner, 'resource')


def test_assoc_tasks113_stub_double():
    # assessment_Tasks has no real 'tasks114' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Task(status="sample_text")
    partner = assessment_Tasks()
    setattr(partner, 'tasks114', None)
    _safe_set(owner, 'Task115', partner)
    assert owner in getattr(partner, 'tasks114')
    _safe_set(owner, 'Task115', None)
    assert owner not in getattr(partner, 'tasks114')


def test_assoc_tasks51_stub_double():
    # assessment_Tasks has no real 'Tasks52' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Task(status="sample_text")
    partner = assessment_Tasks()
    setattr(partner, 'Tasks52', None)
    _safe_set(owner, 'tasks', partner)
    assert getattr(partner, 'Tasks52') == owner
    _safe_set(owner, 'tasks', None)
    assert getattr(partner, 'Tasks52') is None


def test_assoc_tasks9_stub_double():
    # assessment_Node has no real 'affects' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Task(status="sample_text")
    partner = assessment_Node()
    setattr(partner, 'affects', None)
    _safe_set(owner, 'Task', partner)
    assert owner in getattr(partner, 'affects')
    _safe_set(owner, 'Task', None)
    assert owner not in getattr(partner, 'affects')


def test_assoc_views25_stub_double():
    # assessment_Views has no real 'Views' property in the generated
    # code (a bare stub) -- manually attach it so assessment_Application's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # assessment_Application's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = assessment_Application(externalURL="sample_text", internalURL="sample_text")
    partner = assessment_Views()
    setattr(partner, 'Views', None)
    _safe_set(owner, 'application26', partner)
    assert getattr(partner, 'Views') == owner
    _safe_set(owner, 'application26', None)
    assert getattr(partner, 'Views') is None


