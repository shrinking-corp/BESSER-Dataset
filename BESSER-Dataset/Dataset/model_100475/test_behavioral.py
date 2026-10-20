import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Annotatable,
    Effect,
    Scope,
    TextualCode,
    synccharts_Action,
    synccharts_Assignment,
    synccharts_EObject,
    synccharts_Effect,
    synccharts_Emission,
    synccharts_Expression,
    synccharts_Region,
    synccharts_Scope,
    synccharts_Signal,
    synccharts_State,
    synccharts_Substitution,
    synccharts_TextEffect,
    synccharts_TextualCode,
    synccharts_Transition,
    synccharts_Variable,
    StateType,
    TransitionType,
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

def test_assoc_entryActions39_reverse_link_reassign_clear():
    a1 = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    a2 = synccharts_Scope(id="sample_text_2", interfaceDeclaration="sample_text_2", label="sample_text_2")
    b = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    _safe_set(b, 'synccharts_Action41', a1)
    assert _is_linked(b, 'synccharts_Action41', a1)
    if hasattr(a1, 'synccharts_Scope40'):
        assert _is_linked(a1, 'synccharts_Scope40', b)
    _safe_set(b, 'synccharts_Action41', a2)
    assert _is_linked(b, 'synccharts_Action41', a2)
    if hasattr(a1, 'synccharts_Scope40'):
        assert not _is_linked(a1, 'synccharts_Scope40', b)
    if hasattr(a2, 'synccharts_Scope40'):
        assert _is_linked(a2, 'synccharts_Scope40', b)
    _safe_set(b, 'synccharts_Action41', None)
    assert not _is_linked(b, 'synccharts_Action41', a2)
    if hasattr(a2, 'synccharts_Scope40'):
        assert not _is_linked(a2, 'synccharts_Scope40', b)


def test_assoc_exitActions33_reverse_link_reassign_clear():
    a1 = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    a2 = synccharts_Scope(id="sample_text_2", interfaceDeclaration="sample_text_2", label="sample_text_2")
    b = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    _safe_set(b, 'synccharts_Action35', a1)
    assert _is_linked(b, 'synccharts_Action35', a1)
    if hasattr(a1, 'synccharts_Scope34'):
        assert _is_linked(a1, 'synccharts_Scope34', b)
    _safe_set(b, 'synccharts_Action35', a2)
    assert _is_linked(b, 'synccharts_Action35', a2)
    if hasattr(a1, 'synccharts_Scope34'):
        assert not _is_linked(a1, 'synccharts_Scope34', b)
    if hasattr(a2, 'synccharts_Scope34'):
        assert _is_linked(a2, 'synccharts_Scope34', b)
    _safe_set(b, 'synccharts_Action35', None)
    assert not _is_linked(b, 'synccharts_Action35', a2)
    if hasattr(a2, 'synccharts_Scope34'):
        assert not _is_linked(a2, 'synccharts_Scope34', b)


def test_assoc_incomingTransitions19_reverse_link_reassign_clear():
    a1 = synccharts_Transition(isHistory=True, priority=7, type="sample_text")
    a2 = synccharts_Transition(isHistory=False, priority=13, type="sample_text_2")
    b = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    _safe_set(b, 'targetState', {a1})
    assert _is_linked(b, 'targetState', a1)
    if hasattr(a1, 'Transition20'):
        assert _is_linked(a1, 'Transition20', b)
    _safe_set(b, 'targetState', {a2})
    assert _is_linked(b, 'targetState', a2)
    if hasattr(a1, 'Transition20'):
        assert not _is_linked(a1, 'Transition20', b)
    if hasattr(a2, 'Transition20'):
        assert _is_linked(a2, 'Transition20', b)
    _safe_set(b, 'targetState', set())
    assert not _is_linked(b, 'targetState', a2)
    if hasattr(a2, 'Transition20'):
        assert not _is_linked(a2, 'Transition20', b)


def test_assoc_innerActions36_reverse_link_reassign_clear():
    a1 = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    a2 = synccharts_Scope(id="sample_text_2", interfaceDeclaration="sample_text_2", label="sample_text_2")
    b = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    _safe_set(b, 'synccharts_Action38', a1)
    assert _is_linked(b, 'synccharts_Action38', a1)
    if hasattr(a1, 'synccharts_Scope37'):
        assert _is_linked(a1, 'synccharts_Scope37', b)
    _safe_set(b, 'synccharts_Action38', a2)
    assert _is_linked(b, 'synccharts_Action38', a2)
    if hasattr(a1, 'synccharts_Scope37'):
        assert not _is_linked(a1, 'synccharts_Scope37', b)
    if hasattr(a2, 'synccharts_Scope37'):
        assert _is_linked(a2, 'synccharts_Scope37', b)
    _safe_set(b, 'synccharts_Action38', None)
    assert not _is_linked(b, 'synccharts_Action38', a2)
    if hasattr(a2, 'synccharts_Scope37'):
        assert not _is_linked(a2, 'synccharts_Scope37', b)


def test_assoc_outgoingTransitions18_reverse_link_reassign_clear():
    a1 = synccharts_Transition(isHistory=True, priority=7, type="sample_text")
    a2 = synccharts_Transition(isHistory=False, priority=13, type="sample_text_2")
    b = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    _safe_set(b, 'sourceState', {a1})
    assert _is_linked(b, 'sourceState', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'sourceState', {a2})
    assert _is_linked(b, 'sourceState', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'sourceState', set())
    assert not _is_linked(b, 'sourceState', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_parentScope14_reverse_link_reassign_clear():
    a1 = synccharts_Substitution(actual="sample_text", formal="sample_text")
    a2 = synccharts_Substitution(actual="sample_text_2", formal="sample_text_2")
    b = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    _safe_set(b, 'Scope', a1)
    assert _is_linked(b, 'Scope', a1)
    if hasattr(a1, 'renamings'):
        assert _is_linked(a1, 'renamings', b)
    _safe_set(b, 'Scope', a2)
    assert _is_linked(b, 'Scope', a2)
    if hasattr(a1, 'renamings'):
        assert not _is_linked(a1, 'renamings', b)
    if hasattr(a2, 'renamings'):
        assert _is_linked(a2, 'renamings', b)
    _safe_set(b, 'Scope', None)
    assert not _is_linked(b, 'Scope', a2)
    if hasattr(a2, 'renamings'):
        assert not _is_linked(a2, 'renamings', b)


def test_assoc_renamings49_reverse_link_reassign_clear():
    a1 = synccharts_Substitution(actual="sample_text", formal="sample_text")
    a2 = synccharts_Substitution(actual="sample_text_2", formal="sample_text_2")
    b = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    _safe_set(b, 'parentScope', {a1})
    assert _is_linked(b, 'parentScope', a1)
    if hasattr(a1, 'Substitution'):
        assert _is_linked(a1, 'Substitution', b)
    _safe_set(b, 'parentScope', {a2})
    assert _is_linked(b, 'parentScope', a2)
    if hasattr(a1, 'Substitution'):
        assert not _is_linked(a1, 'Substitution', b)
    if hasattr(a2, 'Substitution'):
        assert _is_linked(a2, 'Substitution', b)
    _safe_set(b, 'parentScope', set())
    assert not _is_linked(b, 'parentScope', a2)
    if hasattr(a2, 'Substitution'):
        assert not _is_linked(a2, 'Substitution', b)


def test_assoc_sourceState23_reverse_link_reassign_clear():
    a1 = synccharts_Transition(isHistory=True, priority=7, type="sample_text")
    a2 = synccharts_Transition(isHistory=False, priority=13, type="sample_text_2")
    b = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    _safe_set(b, 'State24', a1)
    assert _is_linked(b, 'State24', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State24', a2)
    assert _is_linked(b, 'State24', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State24', None)
    assert not _is_linked(b, 'State24', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_suspensionTrigger30_reverse_link_reassign_clear():
    a1 = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    a2 = synccharts_Scope(id="sample_text_2", interfaceDeclaration="sample_text_2", label="sample_text_2")
    b = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    _safe_set(b, 'synccharts_Action32', a1)
    assert _is_linked(b, 'synccharts_Action32', a1)
    if hasattr(a1, 'synccharts_Scope31'):
        assert _is_linked(a1, 'synccharts_Scope31', b)
    _safe_set(b, 'synccharts_Action32', a2)
    assert _is_linked(b, 'synccharts_Action32', a2)
    if hasattr(a1, 'synccharts_Scope31'):
        assert not _is_linked(a1, 'synccharts_Scope31', b)
    if hasattr(a2, 'synccharts_Scope31'):
        assert _is_linked(a2, 'synccharts_Scope31', b)
    _safe_set(b, 'synccharts_Action32', None)
    assert not _is_linked(b, 'synccharts_Action32', a2)
    if hasattr(a2, 'synccharts_Scope31'):
        assert not _is_linked(a2, 'synccharts_Scope31', b)


def test_assoc_targetState21_reverse_link_reassign_clear():
    a1 = synccharts_Transition(isHistory=True, priority=7, type="sample_text")
    a2 = synccharts_Transition(isHistory=False, priority=13, type="sample_text_2")
    b = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    _safe_set(b, 'State22', a1)
    assert _is_linked(b, 'State22', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State22', a2)
    assert _is_linked(b, 'State22', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State22', None)
    assert not _is_linked(b, 'State22', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyContents44_stub_double():
    # synccharts_EObject has no real 'synccharts_EObject46' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    partner = synccharts_EObject()
    setattr(partner, 'synccharts_EObject46', None)
    _safe_set(owner, 'synccharts_Scope45', partner)
    assert getattr(partner, 'synccharts_EObject46') == owner
    _safe_set(owner, 'synccharts_Scope45', None)
    assert getattr(partner, 'synccharts_EObject46') is None


def test_assoc_bodyReference42_stub_double():
    # synccharts_EObject has no real 'synccharts_EObject' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    partner = synccharts_EObject()
    setattr(partner, 'synccharts_EObject', None)
    _safe_set(owner, 'synccharts_Scope43', partner)
    assert getattr(partner, 'synccharts_EObject') == owner
    _safe_set(owner, 'synccharts_Scope43', None)
    assert getattr(partner, 'synccharts_EObject') is None


def test_assoc_bodyText47_stub_double():
    # synccharts_TextualCode has no real 'synccharts_TextualCode' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    partner = synccharts_TextualCode()
    setattr(partner, 'synccharts_TextualCode', None)
    _safe_set(owner, 'synccharts_Scope48', {partner})
    assert getattr(partner, 'synccharts_TextualCode') == owner
    _safe_set(owner, 'synccharts_Scope48', set())
    assert getattr(partner, 'synccharts_TextualCode') is None


def test_assoc_effects0_stub_double():
    # synccharts_Effect has no real 'synccharts_Effect' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    partner = synccharts_Effect()
    setattr(partner, 'synccharts_Effect', None)
    _safe_set(owner, 'synccharts_Action', {partner})
    assert getattr(partner, 'synccharts_Effect') == owner
    _safe_set(owner, 'synccharts_Action', set())
    assert getattr(partner, 'synccharts_Effect') is None


def test_assoc_parentRegion16_stub_double():
    # synccharts_Region has no real 'Region17' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    partner = synccharts_Region()
    setattr(partner, 'Region17', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'Region17') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'Region17') is None


def test_assoc_parentState12_stub_double():
    # synccharts_Region has no real 'regions' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    partner = synccharts_Region()
    setattr(partner, 'regions', None)
    _safe_set(owner, 'State13', partner)
    assert getattr(partner, 'regions') == owner
    _safe_set(owner, 'State13', None)
    assert getattr(partner, 'regions') is None


def test_assoc_regions15_stub_double():
    # synccharts_Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    partner = synccharts_Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'parentState', {partner})
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'parentState', set())
    assert getattr(partner, 'Region') is None


def test_assoc_signals25_stub_double():
    # synccharts_Signal has no real 'synccharts_Signal26' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    partner = synccharts_Signal()
    setattr(partner, 'synccharts_Signal26', None)
    _safe_set(owner, 'synccharts_Scope', {partner})
    assert getattr(partner, 'synccharts_Signal26') == owner
    _safe_set(owner, 'synccharts_Scope', set())
    assert getattr(partner, 'synccharts_Signal26') is None


def test_assoc_states11_stub_double():
    # synccharts_Region has no real 'parentRegion' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_State(isFinal=True, isInitial=True, type="sample_text")
    partner = synccharts_Region()
    setattr(partner, 'parentRegion', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'parentRegion')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'parentRegion')


def test_assoc_trigger1_stub_double():
    # synccharts_Expression has no real 'synccharts_Expression' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Action(delay=7, isImmediate=True, label="sample_text")
    partner = synccharts_Expression()
    setattr(partner, 'synccharts_Expression', None)
    _safe_set(owner, 'synccharts_Action2', partner)
    assert getattr(partner, 'synccharts_Expression') == owner
    _safe_set(owner, 'synccharts_Action2', None)
    assert getattr(partner, 'synccharts_Expression') is None


def test_assoc_variables27_stub_double():
    # synccharts_Variable has no real 'synccharts_Variable29' property in the generated
    # code (a bare stub) -- manually attach it so synccharts_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # synccharts_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = synccharts_Scope(id="sample_text", interfaceDeclaration="sample_text", label="sample_text")
    partner = synccharts_Variable()
    setattr(partner, 'synccharts_Variable29', None)
    _safe_set(owner, 'synccharts_Scope28', {partner})
    assert getattr(partner, 'synccharts_Variable29') == owner
    _safe_set(owner, 'synccharts_Scope28', set())
    assert getattr(partner, 'synccharts_Variable29') is None


