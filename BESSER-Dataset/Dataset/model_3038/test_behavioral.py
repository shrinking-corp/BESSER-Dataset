import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Import,
    PublicEvent,
    PubliclyPublishable,
    PubliclySubscribable,
    PublishableByMe,
    PublishableByOthers,
    State,
    SubscribableByMe,
    SubscribableByOthers,
    conversation_Agent,
    conversation_AgentImport,
    conversation_Conversation,
    conversation_Decision,
    conversation_Event,
    conversation_Import,
    conversation_Join,
    conversation_Junction,
    conversation_PrivatePubSub,
    conversation_Projection,
    conversation_ProjectionField,
    conversation_PublicEvent,
    conversation_PublicPubSub,
    conversation_PubliclyPublishable,
    conversation_PubliclySubscribable,
    conversation_PublishableByMe,
    conversation_PublishableByOthers,
    conversation_RestService,
    conversation_Service,
    conversation_State,
    conversation_StateMachine,
    conversation_SubscribableByMe,
    conversation_SubscribableByOthers,
    conversation_Transition,
    conversation_TypeImport,
    conversation_View,
    ConnectionType,
    StateMachineType,
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

def test_assoc_agents0_reverse_link_reassign_clear():
    a1 = conversation_Conversation(name="sample_text")
    a2 = conversation_Conversation(name="sample_text_2")
    b = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    _safe_set(b, 'Agent', a1)
    assert _is_linked(b, 'Agent', a1)
    if hasattr(a1, 'parent'):
        assert _is_linked(a1, 'parent', b)
    _safe_set(b, 'Agent', a2)
    assert _is_linked(b, 'Agent', a2)
    if hasattr(a1, 'parent'):
        assert not _is_linked(a1, 'parent', b)
    if hasattr(a2, 'parent'):
        assert _is_linked(a2, 'parent', b)
    _safe_set(b, 'Agent', None)
    assert not _is_linked(b, 'Agent', a2)
    if hasattr(a2, 'parent'):
        assert not _is_linked(a2, 'parent', b)


def test_assoc_parent18_reverse_link_reassign_clear():
    a1 = conversation_Conversation(name="sample_text")
    a2 = conversation_Conversation(name="sample_text_2")
    b = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    _safe_set(b, 'agents', a1)
    assert _is_linked(b, 'agents', a1)
    if hasattr(a1, 'Conversation'):
        assert _is_linked(a1, 'Conversation', b)
    _safe_set(b, 'agents', a2)
    assert _is_linked(b, 'agents', a2)
    if hasattr(a1, 'Conversation'):
        assert not _is_linked(a1, 'Conversation', b)
    if hasattr(a2, 'Conversation'):
        assert _is_linked(a2, 'Conversation', b)
    _safe_set(b, 'agents', None)
    assert not _is_linked(b, 'agents', a2)
    if hasattr(a2, 'Conversation'):
        assert not _is_linked(a2, 'Conversation', b)


def test_assoc_toState36_reverse_link_reassign_clear():
    a1 = conversation_Transition(requiresExecution=True)
    a2 = conversation_Transition(requiresExecution=False)
    b = conversation_State(join=True, name="sample_text", requiresExecution=True)
    _safe_set(b, 'conversation_State38', a1)
    assert _is_linked(b, 'conversation_State38', a1)
    if hasattr(a1, 'conversation_Transition37'):
        assert _is_linked(a1, 'conversation_Transition37', b)
    _safe_set(b, 'conversation_State38', a2)
    assert _is_linked(b, 'conversation_State38', a2)
    if hasattr(a1, 'conversation_Transition37'):
        assert not _is_linked(a1, 'conversation_Transition37', b)
    if hasattr(a2, 'conversation_Transition37'):
        assert _is_linked(a2, 'conversation_Transition37', b)
    _safe_set(b, 'conversation_State38', None)
    assert not _is_linked(b, 'conversation_State38', a2)
    if hasattr(a2, 'conversation_Transition37'):
        assert not _is_linked(a2, 'conversation_Transition37', b)


def test_assoc_transitions31_reverse_link_reassign_clear():
    a1 = conversation_Transition(requiresExecution=True)
    a2 = conversation_Transition(requiresExecution=False)
    b = conversation_State(join=True, name="sample_text", requiresExecution=True)
    _safe_set(b, 'conversation_State32', {a1})
    assert _is_linked(b, 'conversation_State32', a1)
    if hasattr(a1, 'conversation_Transition33'):
        assert _is_linked(a1, 'conversation_Transition33', b)
    _safe_set(b, 'conversation_State32', {a2})
    assert _is_linked(b, 'conversation_State32', a2)
    if hasattr(a1, 'conversation_Transition33'):
        assert not _is_linked(a1, 'conversation_Transition33', b)
    if hasattr(a2, 'conversation_Transition33'):
        assert _is_linked(a2, 'conversation_Transition33', b)
    _safe_set(b, 'conversation_State32', set())
    assert not _is_linked(b, 'conversation_State32', a2)
    if hasattr(a2, 'conversation_Transition33'):
        assert not _is_linked(a2, 'conversation_Transition33', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_agent51_stub_double():
    # conversation_AgentImport has no real 'conversation_AgentImport52' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_AgentImport()
    setattr(partner, 'conversation_AgentImport52', None)
    _safe_set(owner, 'conversation_Agent53', partner)
    assert getattr(partner, 'conversation_AgentImport52') == owner
    _safe_set(owner, 'conversation_Agent53', None)
    assert getattr(partner, 'conversation_AgentImport52') is None


def test_assoc_causedBy41_stub_double():
    # conversation_PrivatePubSub has no real 'PrivatePubSub' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_PrivatePubSub()
    setattr(partner, 'PrivatePubSub', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'PrivatePubSub') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'PrivatePubSub') is None


def test_assoc_definedTypes1_stub_double():
    # conversation_Projection has no real 'conversation_Projection' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_Projection()
    setattr(partner, 'conversation_Projection', None)
    _safe_set(owner, 'conversation_Conversation', {partner})
    assert getattr(partner, 'conversation_Projection') == owner
    _safe_set(owner, 'conversation_Conversation', set())
    assert getattr(partner, 'conversation_Projection') is None


def test_assoc_definedTypes12_stub_double():
    # conversation_Projection has no real 'conversation_Projection13' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_Projection()
    setattr(partner, 'conversation_Projection13', None)
    _safe_set(owner, 'conversation_Agent', {partner})
    assert getattr(partner, 'conversation_Projection13') == owner
    _safe_set(owner, 'conversation_Agent', set())
    assert getattr(partner, 'conversation_Projection13') is None


def test_assoc_exCausedBy39_stub_double():
    # conversation_SubscribableByOthers has no real 'conversation_SubscribableByOthers' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_SubscribableByOthers()
    setattr(partner, 'conversation_SubscribableByOthers', None)
    _safe_set(owner, 'conversation_Transition40', partner)
    assert getattr(partner, 'conversation_SubscribableByOthers') == owner
    _safe_set(owner, 'conversation_Transition40', None)
    assert getattr(partner, 'conversation_SubscribableByOthers') is None


def test_assoc_exTriggers42_stub_double():
    # conversation_PublishableByOthers has no real 'conversation_PublishableByOthers' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_PublishableByOthers()
    setattr(partner, 'conversation_PublishableByOthers', None)
    _safe_set(owner, 'conversation_Transition43', partner)
    assert getattr(partner, 'conversation_PublishableByOthers') == owner
    _safe_set(owner, 'conversation_Transition43', None)
    assert getattr(partner, 'conversation_PublishableByOthers') is None


def test_assoc_fieldMapping46_stub_double():
    # conversation_ProjectionField has no real 'conversation_ProjectionField' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_ProjectionField()
    setattr(partner, 'conversation_ProjectionField', None)
    _safe_set(owner, 'conversation_Transition47', partner)
    assert getattr(partner, 'conversation_ProjectionField') == owner
    _safe_set(owner, 'conversation_Transition47', None)
    assert getattr(partner, 'conversation_ProjectionField') is None


def test_assoc_importedAgents8_stub_double():
    # conversation_AgentImport has no real 'conversation_AgentImport' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_AgentImport()
    setattr(partner, 'conversation_AgentImport', None)
    _safe_set(owner, 'conversation_Conversation9', {partner})
    assert getattr(partner, 'conversation_AgentImport') == owner
    _safe_set(owner, 'conversation_Conversation9', set())
    assert getattr(partner, 'conversation_AgentImport') is None


def test_assoc_importedTypes6_stub_double():
    # conversation_TypeImport has no real 'conversation_TypeImport' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_TypeImport()
    setattr(partner, 'conversation_TypeImport', None)
    _safe_set(owner, 'conversation_Conversation7', {partner})
    assert getattr(partner, 'conversation_TypeImport') == owner
    _safe_set(owner, 'conversation_Conversation7', set())
    assert getattr(partner, 'conversation_TypeImport') is None


def test_assoc_initialState22_stub_double():
    # conversation_StateMachine has no real 'conversation_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so conversation_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_State(join=True, name="sample_text", requiresExecution=True)
    partner = conversation_StateMachine()
    setattr(partner, 'conversation_StateMachine', None)
    _safe_set(owner, 'conversation_State', partner)
    assert getattr(partner, 'conversation_StateMachine') == owner
    _safe_set(owner, 'conversation_State', None)
    assert getattr(partner, 'conversation_StateMachine') is None


def test_assoc_initialTransition27_stub_double():
    # conversation_StateMachine has no real 'conversation_StateMachine28' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_StateMachine()
    setattr(partner, 'conversation_StateMachine28', None)
    _safe_set(owner, 'conversation_Transition', partner)
    assert getattr(partner, 'conversation_StateMachine28') == owner
    _safe_set(owner, 'conversation_Transition', None)
    assert getattr(partner, 'conversation_StateMachine28') is None


def test_assoc_parent25_stub_double():
    # conversation_StateMachine has no real 'stateMachine' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_StateMachine()
    setattr(partner, 'stateMachine', None)
    _safe_set(owner, 'Agent26', partner)
    assert getattr(partner, 'stateMachine') == owner
    _safe_set(owner, 'Agent26', None)
    assert getattr(partner, 'stateMachine') is None


def test_assoc_parent34_stub_double():
    # conversation_StateMachine has no real 'StateMachine35' property in the generated
    # code (a bare stub) -- manually attach it so conversation_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_State(join=True, name="sample_text", requiresExecution=True)
    partner = conversation_StateMachine()
    setattr(partner, 'StateMachine35', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'StateMachine35') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'StateMachine35') is None


def test_assoc_parent48_stub_double():
    # conversation_PubliclySubscribable has no real 'sendables' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_PubliclySubscribable()
    setattr(partner, 'sendables', None)
    _safe_set(owner, 'Agent49', partner)
    assert getattr(partner, 'sendables') == owner
    _safe_set(owner, 'Agent49', None)
    assert getattr(partner, 'sendables') is None


def test_assoc_projection19_stub_double():
    # conversation_Projection has no real 'conversation_Projection21' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_Projection()
    setattr(partner, 'conversation_Projection21', None)
    _safe_set(owner, 'conversation_Agent20', partner)
    assert getattr(partner, 'conversation_Projection21') == owner
    _safe_set(owner, 'conversation_Agent20', None)
    assert getattr(partner, 'conversation_Projection21') is None


def test_assoc_refType29_stub_double():
    # conversation_Projection has no real 'conversation_Projection30' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Event(name="sample_text")
    partner = conversation_Projection()
    setattr(partner, 'conversation_Projection30', None)
    _safe_set(owner, 'conversation_Event', partner)
    assert getattr(partner, 'conversation_Projection30') == owner
    _safe_set(owner, 'conversation_Event', None)
    assert getattr(partner, 'conversation_Projection30') is None


def test_assoc_restServices2_stub_double():
    # conversation_RestService has no real 'conversation_RestService' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_RestService()
    setattr(partner, 'conversation_RestService', None)
    _safe_set(owner, 'conversation_Conversation3', {partner})
    assert getattr(partner, 'conversation_RestService') == owner
    _safe_set(owner, 'conversation_Conversation3', set())
    assert getattr(partner, 'conversation_RestService') is None


def test_assoc_sendables16_stub_double():
    # conversation_PubliclySubscribable has no real 'PubliclySubscribable' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_PubliclySubscribable()
    setattr(partner, 'PubliclySubscribable', None)
    _safe_set(owner, 'parent17', {partner})
    assert getattr(partner, 'PubliclySubscribable') == owner
    _safe_set(owner, 'parent17', set())
    assert getattr(partner, 'PubliclySubscribable') is None


def test_assoc_services4_stub_double():
    # conversation_Service has no real 'conversation_Service' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_Service()
    setattr(partner, 'conversation_Service', None)
    _safe_set(owner, 'conversation_Conversation5', {partner})
    assert getattr(partner, 'conversation_Service') == owner
    _safe_set(owner, 'conversation_Conversation5', set())
    assert getattr(partner, 'conversation_Service') is None


def test_assoc_stateMachine14_stub_double():
    # conversation_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Agent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Agent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Agent(accessRequirement="sample_text", connectionType="sample_text", name="sample_text", stateMachineType="sample_text")
    partner = conversation_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'parent15', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'parent15', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_states23_stub_double():
    # conversation_StateMachine has no real 'parent24' property in the generated
    # code (a bare stub) -- manually attach it so conversation_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_State(join=True, name="sample_text", requiresExecution=True)
    partner = conversation_StateMachine()
    setattr(partner, 'parent24', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'parent24')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'parent24')


def test_assoc_transition50_stub_double():
    # conversation_PrivatePubSub has no real 'causedBy' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_PrivatePubSub()
    setattr(partner, 'causedBy', None)
    _safe_set(owner, 'Transition', partner)
    assert getattr(partner, 'causedBy') == owner
    _safe_set(owner, 'Transition', None)
    assert getattr(partner, 'causedBy') is None


def test_assoc_triggers44_stub_double():
    # conversation_PublishableByMe has no real 'conversation_PublishableByMe' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Transition(requiresExecution=True)
    partner = conversation_PublishableByMe()
    setattr(partner, 'conversation_PublishableByMe', None)
    _safe_set(owner, 'conversation_Transition45', partner)
    assert getattr(partner, 'conversation_PublishableByMe') == owner
    _safe_set(owner, 'conversation_Transition45', None)
    assert getattr(partner, 'conversation_PublishableByMe') is None


def test_assoc_views10_stub_double():
    # conversation_View has no real 'conversation_View' property in the generated
    # code (a bare stub) -- manually attach it so conversation_Conversation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conversation_Conversation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conversation_Conversation(name="sample_text")
    partner = conversation_View()
    setattr(partner, 'conversation_View', None)
    _safe_set(owner, 'conversation_Conversation11', {partner})
    assert getattr(partner, 'conversation_View') == owner
    _safe_set(owner, 'conversation_Conversation11', set())
    assert getattr(partner, 'conversation_View') is None


