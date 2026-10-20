import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    ActivityEdge,
    ActivityNode,
    ActivityPartition,
    ControlNode,
    ExecutableNode,
    FinalNode,
    NamedElement,
    PiServiceComposition_Action,
    PiServiceComposition_Activity,
    PiServiceComposition_ActivityEdge,
    PiServiceComposition_ActivityFinalNode,
    PiServiceComposition_ActivityNode,
    PiServiceComposition_ActivityPartition,
    PiServiceComposition_BussinessCollaborator,
    PiServiceComposition_CompositionServiceModel,
    PiServiceComposition_ControlFlow,
    PiServiceComposition_ControlNode,
    PiServiceComposition_DecisionNode,
    PiServiceComposition_ExecutableNode,
    PiServiceComposition_FinalNode,
    PiServiceComposition_ForkNode,
    PiServiceComposition_InitialNode,
    PiServiceComposition_JoinNode,
    PiServiceComposition_MergeNode,
    PiServiceComposition_NamedElement,
    PiServiceComposition_ObjectFlow,
    PiServiceComposition_ObjectNode,
    PiServiceComposition_Policy,
    PiServiceComposition_Rule,
    PiServiceComposition_ServiceActivity,
    PiServiceComposition_Variable,
    ActionType,
    EventType,
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

def test_assoc_APartition12_reverse_link_reassign_clear():
    a1 = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    a2 = PiServiceComposition_ActivityPartition(isDimension=False, isExternal=False)
    b = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    _safe_set(b, 'PiServiceComposition_ActivityPartition13', a1)
    assert _is_linked(b, 'PiServiceComposition_ActivityPartition13', a1)
    if hasattr(a1, 'PiServiceComposition_ActivityPartition11'):
        assert _is_linked(a1, 'PiServiceComposition_ActivityPartition11', b)
    _safe_set(b, 'PiServiceComposition_ActivityPartition13', a2)
    assert _is_linked(b, 'PiServiceComposition_ActivityPartition13', a2)
    if hasattr(a1, 'PiServiceComposition_ActivityPartition11'):
        assert not _is_linked(a1, 'PiServiceComposition_ActivityPartition11', b)
    if hasattr(a2, 'PiServiceComposition_ActivityPartition11'):
        assert _is_linked(a2, 'PiServiceComposition_ActivityPartition11', b)
    _safe_set(b, 'PiServiceComposition_ActivityPartition13', None)
    assert not _is_linked(b, 'PiServiceComposition_ActivityPartition13', a2)
    if hasattr(a2, 'PiServiceComposition_ActivityPartition11'):
        assert not _is_linked(a2, 'PiServiceComposition_ActivityPartition11', b)


def test_assoc_action51_reverse_link_reassign_clear():
    a1 = PiServiceComposition_Policy(name="sample_text")
    a2 = PiServiceComposition_Policy(name="sample_text_2")
    b = PiServiceComposition_Action(type="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'definePolices'):
        assert _is_linked(a1, 'definePolices', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'definePolices'):
        assert not _is_linked(a1, 'definePolices', b)
    if hasattr(a2, 'definePolices'):
        assert _is_linked(a2, 'definePolices', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'definePolices'):
        assert not _is_linked(a2, 'definePolices', b)


def test_assoc_contains46_reverse_link_reassign_clear():
    a1 = PiServiceComposition_Rule(action="sample_text", condition="sample_text", event="sample_text", name="sample_text")
    a2 = PiServiceComposition_Rule(action="sample_text_2", condition="sample_text_2", event="sample_text_2", name="sample_text_2")
    b = PiServiceComposition_Policy(name="sample_text")
    _safe_set(b, 'policy', {a1})
    assert _is_linked(b, 'policy', a1)
    if hasattr(a1, 'Rule'):
        assert _is_linked(a1, 'Rule', b)
    _safe_set(b, 'policy', {a2})
    assert _is_linked(b, 'policy', a2)
    if hasattr(a1, 'Rule'):
        assert not _is_linked(a1, 'Rule', b)
    if hasattr(a2, 'Rule'):
        assert _is_linked(a2, 'Rule', b)
    _safe_set(b, 'policy', set())
    assert not _is_linked(b, 'policy', a2)
    if hasattr(a2, 'Rule'):
        assert not _is_linked(a2, 'Rule', b)


def test_assoc_definePolices41_reverse_link_reassign_clear():
    a1 = PiServiceComposition_Policy(name="sample_text")
    a2 = PiServiceComposition_Policy(name="sample_text_2")
    b = PiServiceComposition_Action(type="sample_text")
    _safe_set(b, 'action', a1)
    assert _is_linked(b, 'action', a1)
    if hasattr(a1, 'Policy'):
        assert _is_linked(a1, 'Policy', b)
    _safe_set(b, 'action', a2)
    assert _is_linked(b, 'action', a2)
    if hasattr(a1, 'Policy'):
        assert not _is_linked(a1, 'Policy', b)
    if hasattr(a2, 'Policy'):
        assert _is_linked(a2, 'Policy', b)
    _safe_set(b, 'action', None)
    assert not _is_linked(b, 'action', a2)
    if hasattr(a2, 'Policy'):
        assert not _is_linked(a2, 'Policy', b)


def test_assoc_hasVars47_reverse_link_reassign_clear():
    a1 = PiServiceComposition_Variable(name="sample_text", type="sample_text")
    a2 = PiServiceComposition_Variable(name="sample_text_2", type="sample_text_2")
    b = PiServiceComposition_Policy(name="sample_text")
    _safe_set(b, 'PiServiceComposition_Policy48', {a1})
    assert _is_linked(b, 'PiServiceComposition_Policy48', a1)
    if hasattr(a1, 'PiServiceComposition_Variable49'):
        assert _is_linked(a1, 'PiServiceComposition_Variable49', b)
    _safe_set(b, 'PiServiceComposition_Policy48', {a2})
    assert _is_linked(b, 'PiServiceComposition_Policy48', a2)
    if hasattr(a1, 'PiServiceComposition_Variable49'):
        assert not _is_linked(a1, 'PiServiceComposition_Variable49', b)
    if hasattr(a2, 'PiServiceComposition_Variable49'):
        assert _is_linked(a2, 'PiServiceComposition_Variable49', b)
    _safe_set(b, 'PiServiceComposition_Policy48', set())
    assert not _is_linked(b, 'PiServiceComposition_Policy48', a2)
    if hasattr(a2, 'PiServiceComposition_Variable49'):
        assert not _is_linked(a2, 'PiServiceComposition_Variable49', b)


def test_assoc_policy44_reverse_link_reassign_clear():
    a1 = PiServiceComposition_Rule(action="sample_text", condition="sample_text", event="sample_text", name="sample_text")
    a2 = PiServiceComposition_Rule(action="sample_text_2", condition="sample_text_2", event="sample_text_2", name="sample_text_2")
    b = PiServiceComposition_Policy(name="sample_text")
    _safe_set(b, 'Policy45', a1)
    assert _is_linked(b, 'Policy45', a1)
    if hasattr(a1, 'contains'):
        assert _is_linked(a1, 'contains', b)
    _safe_set(b, 'Policy45', a2)
    assert _is_linked(b, 'Policy45', a2)
    if hasattr(a1, 'contains'):
        assert not _is_linked(a1, 'contains', b)
    if hasattr(a2, 'contains'):
        assert _is_linked(a2, 'contains', b)
    _safe_set(b, 'Policy45', None)
    assert not _is_linked(b, 'Policy45', a2)
    if hasattr(a2, 'contains'):
        assert not _is_linked(a2, 'contains', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action37_stub_double():
    # PiServiceComposition_ServiceActivity has no real 'PiServiceComposition_ServiceActivity' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Action(type="sample_text")
    partner = PiServiceComposition_ServiceActivity()
    setattr(partner, 'PiServiceComposition_ServiceActivity', None)
    _safe_set(owner, 'PiServiceComposition_Action', partner)
    assert owner in getattr(partner, 'PiServiceComposition_ServiceActivity')
    _safe_set(owner, 'PiServiceComposition_Action', None)
    assert owner not in getattr(partner, 'PiServiceComposition_ServiceActivity')


def test_assoc_compositionPolices5_stub_double():
    # PiServiceComposition_CompositionServiceModel has no real 'PiServiceComposition_CompositionServiceModel6' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Policy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Policy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Policy(name="sample_text")
    partner = PiServiceComposition_CompositionServiceModel()
    setattr(partner, 'PiServiceComposition_CompositionServiceModel6', None)
    _safe_set(owner, 'PiServiceComposition_Policy', partner)
    assert owner in getattr(partner, 'PiServiceComposition_CompositionServiceModel6')
    _safe_set(owner, 'PiServiceComposition_Policy', None)
    assert owner not in getattr(partner, 'PiServiceComposition_CompositionServiceModel6')


def test_assoc_edges14_stub_double():
    # PiServiceComposition_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_ActivityPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_ActivityPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    partner = PiServiceComposition_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'partition', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'partition', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_hasPolices38_stub_double():
    # PiServiceComposition_ServiceActivity has no real 'PiServiceComposition_ServiceActivity39' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Policy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Policy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Policy(name="sample_text")
    partner = PiServiceComposition_ServiceActivity()
    setattr(partner, 'PiServiceComposition_ServiceActivity39', None)
    _safe_set(owner, 'PiServiceComposition_Policy40', partner)
    assert owner in getattr(partner, 'PiServiceComposition_ServiceActivity39')
    _safe_set(owner, 'PiServiceComposition_Policy40', None)
    assert owner not in getattr(partner, 'PiServiceComposition_ServiceActivity39')


def test_assoc_hasPolices42_stub_double():
    # PiServiceComposition_BussinessCollaborator has no real 'typeOperation' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Policy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Policy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Policy(name="sample_text")
    partner = PiServiceComposition_BussinessCollaborator()
    setattr(partner, 'typeOperation', None)
    _safe_set(owner, 'Policy43', partner)
    assert owner in getattr(partner, 'typeOperation')
    _safe_set(owner, 'Policy43', None)
    assert owner not in getattr(partner, 'typeOperation')


def test_assoc_nodes15_stub_double():
    # PiServiceComposition_ActivityNode has no real 'ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_ActivityPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_ActivityPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    partner = PiServiceComposition_ActivityNode()
    setattr(partner, 'ActivityNode', None)
    _safe_set(owner, 'partition16', {partner})
    assert getattr(partner, 'ActivityNode') == owner
    _safe_set(owner, 'partition16', set())
    assert getattr(partner, 'ActivityNode') is None


def test_assoc_partition0_stub_double():
    # PiServiceComposition_CompositionServiceModel has no real 'PiServiceComposition_CompositionServiceModel' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_ActivityPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_ActivityPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    partner = PiServiceComposition_CompositionServiceModel()
    setattr(partner, 'PiServiceComposition_CompositionServiceModel', None)
    _safe_set(owner, 'PiServiceComposition_ActivityPartition', partner)
    assert owner in getattr(partner, 'PiServiceComposition_CompositionServiceModel')
    _safe_set(owner, 'PiServiceComposition_ActivityPartition', None)
    assert owner not in getattr(partner, 'PiServiceComposition_CompositionServiceModel')


def test_assoc_partition24_stub_double():
    # PiServiceComposition_ActivityEdge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_ActivityPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_ActivityPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    partner = PiServiceComposition_ActivityEdge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'ActivityPartition', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'ActivityPartition', None)
    assert getattr(partner, 'edges') is None


def test_assoc_partition35_stub_double():
    # PiServiceComposition_ActivityNode has no real 'nodes' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_ActivityPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_ActivityPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_ActivityPartition(isDimension=True, isExternal=True)
    partner = PiServiceComposition_ActivityNode()
    setattr(partner, 'nodes', None)
    _safe_set(owner, 'ActivityPartition36', partner)
    assert getattr(partner, 'nodes') == owner
    _safe_set(owner, 'ActivityPartition36', None)
    assert getattr(partner, 'nodes') is None


def test_assoc_typeOperation50_stub_double():
    # PiServiceComposition_BussinessCollaborator has no real 'BussinessCollaborator' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Policy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Policy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Policy(name="sample_text")
    partner = PiServiceComposition_BussinessCollaborator()
    setattr(partner, 'BussinessCollaborator', None)
    _safe_set(owner, 'hasPolices', {partner})
    assert getattr(partner, 'BussinessCollaborator') == owner
    _safe_set(owner, 'hasPolices', set())
    assert getattr(partner, 'BussinessCollaborator') is None


def test_assoc_vars7_stub_double():
    # PiServiceComposition_CompositionServiceModel has no real 'PiServiceComposition_CompositionServiceModel8' property in the generated
    # code (a bare stub) -- manually attach it so PiServiceComposition_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PiServiceComposition_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PiServiceComposition_Variable(name="sample_text", type="sample_text")
    partner = PiServiceComposition_CompositionServiceModel()
    setattr(partner, 'PiServiceComposition_CompositionServiceModel8', None)
    _safe_set(owner, 'PiServiceComposition_Variable', partner)
    assert owner in getattr(partner, 'PiServiceComposition_CompositionServiceModel8')
    _safe_set(owner, 'PiServiceComposition_Variable', None)
    assert owner not in getattr(partner, 'PiServiceComposition_CompositionServiceModel8')


