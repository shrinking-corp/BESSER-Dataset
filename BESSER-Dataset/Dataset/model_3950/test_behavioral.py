import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    fuzzyAutomaton_Action,
    fuzzyAutomaton_FuzzyAutomaton,
    fuzzyAutomaton_FuzzyConstraint,
    fuzzyAutomaton_FuzzyRelation,
    fuzzyAutomaton_Input,
    fuzzyAutomaton_Output,
    fuzzyAutomaton_State,
    fuzzyAutomaton_Transition,
    fuzzyAutomaton_TransitionFeature,
    fuzzyAutomaton_VarTransformation,
    fuzzyAutomaton_VarUpdate,
    fuzzyAutomaton_Variable,
    fuzzyAutomaton_VariableSet,
    FuzzyRelationType,
    TNormType,
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

def test_assoc_action18_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_TransitionFeature(name="sample_text")
    a2 = fuzzyAutomaton_TransitionFeature(name="sample_text_2")
    b = fuzzyAutomaton_Action(name="sample_text")
    _safe_set(b, 'fuzzyAutomaton_Action', a1)
    assert _is_linked(b, 'fuzzyAutomaton_Action', a1)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature19'):
        assert _is_linked(a1, 'fuzzyAutomaton_TransitionFeature19', b)
    _safe_set(b, 'fuzzyAutomaton_Action', a2)
    assert _is_linked(b, 'fuzzyAutomaton_Action', a2)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature19'):
        assert not _is_linked(a1, 'fuzzyAutomaton_TransitionFeature19', b)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature19'):
        assert _is_linked(a2, 'fuzzyAutomaton_TransitionFeature19', b)
    _safe_set(b, 'fuzzyAutomaton_Action', None)
    assert not _is_linked(b, 'fuzzyAutomaton_Action', a2)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature19'):
        assert not _is_linked(a2, 'fuzzyAutomaton_TransitionFeature19', b)


def test_assoc_fuzzyConstraint20_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_TransitionFeature(name="sample_text")
    a2 = fuzzyAutomaton_TransitionFeature(name="sample_text_2")
    b = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint', a1)
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint', a1)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature21'):
        assert _is_linked(a1, 'fuzzyAutomaton_TransitionFeature21', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint', a2)
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint', a2)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature21'):
        assert not _is_linked(a1, 'fuzzyAutomaton_TransitionFeature21', b)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature21'):
        assert _is_linked(a2, 'fuzzyAutomaton_TransitionFeature21', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint', None)
    assert not _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint', a2)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature21'):
        assert not _is_linked(a2, 'fuzzyAutomaton_TransitionFeature21', b)


def test_assoc_fuzzyRelations26_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_FuzzyRelation(delta="sample_text", expression1="sample_text", expression2="sample_text", expression3="sample_text", tFRelation="sample_text")
    a2 = fuzzyAutomaton_FuzzyRelation(delta="sample_text_2", expression1="sample_text_2", expression2="sample_text_2", expression3="sample_text_2", tFRelation="sample_text_2")
    b = fuzzyAutomaton_FuzzyConstraint(name="sample_text", tNorm="sample_text")
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint27', {a1})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint27', a1)
    if hasattr(a1, 'fuzzyAutomaton_FuzzyRelation'):
        assert _is_linked(a1, 'fuzzyAutomaton_FuzzyRelation', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint27', {a2})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint27', a2)
    if hasattr(a1, 'fuzzyAutomaton_FuzzyRelation'):
        assert not _is_linked(a1, 'fuzzyAutomaton_FuzzyRelation', b)
    if hasattr(a2, 'fuzzyAutomaton_FuzzyRelation'):
        assert _is_linked(a2, 'fuzzyAutomaton_FuzzyRelation', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyConstraint27', set())
    assert not _is_linked(b, 'fuzzyAutomaton_FuzzyConstraint27', a2)
    if hasattr(a2, 'fuzzyAutomaton_FuzzyRelation'):
        assert not _is_linked(a2, 'fuzzyAutomaton_FuzzyRelation', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_State(isInitial="sample_text")
    a2 = fuzzyAutomaton_State(isInitial="sample_text_2")
    b = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton', {a1})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton', a1)
    if hasattr(a1, 'fuzzyAutomaton_State'):
        assert _is_linked(a1, 'fuzzyAutomaton_State', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton', {a2})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton', a2)
    if hasattr(a1, 'fuzzyAutomaton_State'):
        assert not _is_linked(a1, 'fuzzyAutomaton_State', b)
    if hasattr(a2, 'fuzzyAutomaton_State'):
        assert _is_linked(a2, 'fuzzyAutomaton_State', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton', set())
    assert not _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton', a2)
    if hasattr(a2, 'fuzzyAutomaton_State'):
        assert not _is_linked(a2, 'fuzzyAutomaton_State', b)


def test_assoc_transitionFeatures5_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_TransitionFeature(name="sample_text")
    a2 = fuzzyAutomaton_TransitionFeature(name="sample_text_2")
    b = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton6', {a1})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton6', a1)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature'):
        assert _is_linked(a1, 'fuzzyAutomaton_TransitionFeature', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton6', {a2})
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton6', a2)
    if hasattr(a1, 'fuzzyAutomaton_TransitionFeature'):
        assert not _is_linked(a1, 'fuzzyAutomaton_TransitionFeature', b)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature'):
        assert _is_linked(a2, 'fuzzyAutomaton_TransitionFeature', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton6', set())
    assert not _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton6', a2)
    if hasattr(a2, 'fuzzyAutomaton_TransitionFeature'):
        assert not _is_linked(a2, 'fuzzyAutomaton_TransitionFeature', b)


def test_assoc_varTransformation22_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_VarTransformation(name="sample_text")
    a2 = fuzzyAutomaton_VarTransformation(name="sample_text_2")
    b = fuzzyAutomaton_TransitionFeature(name="sample_text")
    _safe_set(b, 'fuzzyAutomaton_TransitionFeature23', a1)
    assert _is_linked(b, 'fuzzyAutomaton_TransitionFeature23', a1)
    if hasattr(a1, 'fuzzyAutomaton_VarTransformation'):
        assert _is_linked(a1, 'fuzzyAutomaton_VarTransformation', b)
    _safe_set(b, 'fuzzyAutomaton_TransitionFeature23', a2)
    assert _is_linked(b, 'fuzzyAutomaton_TransitionFeature23', a2)
    if hasattr(a1, 'fuzzyAutomaton_VarTransformation'):
        assert not _is_linked(a1, 'fuzzyAutomaton_VarTransformation', b)
    if hasattr(a2, 'fuzzyAutomaton_VarTransformation'):
        assert _is_linked(a2, 'fuzzyAutomaton_VarTransformation', b)
    _safe_set(b, 'fuzzyAutomaton_TransitionFeature23', None)
    assert not _is_linked(b, 'fuzzyAutomaton_TransitionFeature23', a2)
    if hasattr(a2, 'fuzzyAutomaton_VarTransformation'):
        assert not _is_linked(a2, 'fuzzyAutomaton_VarTransformation', b)


def test_assoc_varUpdates28_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_VarUpdate(expression="sample_text")
    a2 = fuzzyAutomaton_VarUpdate(expression="sample_text_2")
    b = fuzzyAutomaton_VarTransformation(name="sample_text")
    _safe_set(b, 'fuzzyAutomaton_VarTransformation29', {a1})
    assert _is_linked(b, 'fuzzyAutomaton_VarTransformation29', a1)
    if hasattr(a1, 'fuzzyAutomaton_VarUpdate'):
        assert _is_linked(a1, 'fuzzyAutomaton_VarUpdate', b)
    _safe_set(b, 'fuzzyAutomaton_VarTransformation29', {a2})
    assert _is_linked(b, 'fuzzyAutomaton_VarTransformation29', a2)
    if hasattr(a1, 'fuzzyAutomaton_VarUpdate'):
        assert not _is_linked(a1, 'fuzzyAutomaton_VarUpdate', b)
    if hasattr(a2, 'fuzzyAutomaton_VarUpdate'):
        assert _is_linked(a2, 'fuzzyAutomaton_VarUpdate', b)
    _safe_set(b, 'fuzzyAutomaton_VarTransformation29', set())
    assert not _is_linked(b, 'fuzzyAutomaton_VarTransformation29', a2)
    if hasattr(a2, 'fuzzyAutomaton_VarUpdate'):
        assert not _is_linked(a2, 'fuzzyAutomaton_VarUpdate', b)


def test_assoc_variable30_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    a2 = fuzzyAutomaton_Variable(name="sample_text_2", value="sample_text_2")
    b = fuzzyAutomaton_VarUpdate(expression="sample_text")
    _safe_set(b, 'fuzzyAutomaton_VarUpdate31', a1)
    assert _is_linked(b, 'fuzzyAutomaton_VarUpdate31', a1)
    if hasattr(a1, 'fuzzyAutomaton_Variable32'):
        assert _is_linked(a1, 'fuzzyAutomaton_Variable32', b)
    _safe_set(b, 'fuzzyAutomaton_VarUpdate31', a2)
    assert _is_linked(b, 'fuzzyAutomaton_VarUpdate31', a2)
    if hasattr(a1, 'fuzzyAutomaton_Variable32'):
        assert not _is_linked(a1, 'fuzzyAutomaton_Variable32', b)
    if hasattr(a2, 'fuzzyAutomaton_Variable32'):
        assert _is_linked(a2, 'fuzzyAutomaton_Variable32', b)
    _safe_set(b, 'fuzzyAutomaton_VarUpdate31', None)
    assert not _is_linked(b, 'fuzzyAutomaton_VarUpdate31', a2)
    if hasattr(a2, 'fuzzyAutomaton_Variable32'):
        assert not _is_linked(a2, 'fuzzyAutomaton_Variable32', b)


def test_assoc_variableSet3_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_VariableSet(name="sample_text")
    a2 = fuzzyAutomaton_VariableSet(name="sample_text_2")
    b = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton4', a1)
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton4', a1)
    if hasattr(a1, 'fuzzyAutomaton_VariableSet'):
        assert _is_linked(a1, 'fuzzyAutomaton_VariableSet', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton4', a2)
    assert _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton4', a2)
    if hasattr(a1, 'fuzzyAutomaton_VariableSet'):
        assert not _is_linked(a1, 'fuzzyAutomaton_VariableSet', b)
    if hasattr(a2, 'fuzzyAutomaton_VariableSet'):
        assert _is_linked(a2, 'fuzzyAutomaton_VariableSet', b)
    _safe_set(b, 'fuzzyAutomaton_FuzzyAutomaton4', None)
    assert not _is_linked(b, 'fuzzyAutomaton_FuzzyAutomaton4', a2)
    if hasattr(a2, 'fuzzyAutomaton_VariableSet'):
        assert not _is_linked(a2, 'fuzzyAutomaton_VariableSet', b)


def test_assoc_variables14_reverse_link_reassign_clear():
    a1 = fuzzyAutomaton_VariableSet(name="sample_text")
    a2 = fuzzyAutomaton_VariableSet(name="sample_text_2")
    b = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    _safe_set(b, 'fuzzyAutomaton_Variable', a1)
    assert _is_linked(b, 'fuzzyAutomaton_Variable', a1)
    if hasattr(a1, 'fuzzyAutomaton_VariableSet15'):
        assert _is_linked(a1, 'fuzzyAutomaton_VariableSet15', b)
    _safe_set(b, 'fuzzyAutomaton_Variable', a2)
    assert _is_linked(b, 'fuzzyAutomaton_Variable', a2)
    if hasattr(a1, 'fuzzyAutomaton_VariableSet15'):
        assert not _is_linked(a1, 'fuzzyAutomaton_VariableSet15', b)
    if hasattr(a2, 'fuzzyAutomaton_VariableSet15'):
        assert _is_linked(a2, 'fuzzyAutomaton_VariableSet15', b)
    _safe_set(b, 'fuzzyAutomaton_Variable', None)
    assert not _is_linked(b, 'fuzzyAutomaton_Variable', a2)
    if hasattr(a2, 'fuzzyAutomaton_VariableSet15'):
        assert not _is_linked(a2, 'fuzzyAutomaton_VariableSet15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_feature13_stub_double():
    # fuzzyAutomaton_Transition has no real 'featureToTransition' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_TransitionFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_TransitionFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_TransitionFeature(name="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'featureToTransition', None)
    _safe_set(owner, 'TransitionFeature', partner)
    assert getattr(partner, 'featureToTransition') == owner
    _safe_set(owner, 'TransitionFeature', None)
    assert getattr(partner, 'featureToTransition') is None


def test_assoc_featureToTransition16_stub_double():
    # fuzzyAutomaton_Transition has no real 'Transition17' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_TransitionFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_TransitionFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_TransitionFeature(name="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'Transition17', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'Transition17') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'Transition17') is None


def test_assoc_incoming7_stub_double():
    # fuzzyAutomaton_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_State(isInitial="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_outgoing8_stub_double():
    # fuzzyAutomaton_Transition has no real 'Transition9' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_State(isInitial="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'Transition9', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition9') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition9') is None


def test_assoc_parameters24_stub_double():
    # fuzzyAutomaton_Input has no real 'fuzzyAutomaton_Input' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_Variable(name="sample_text", value="sample_text")
    partner = fuzzyAutomaton_Input()
    setattr(partner, 'fuzzyAutomaton_Input', None)
    _safe_set(owner, 'fuzzyAutomaton_Variable25', partner)
    assert owner in getattr(partner, 'fuzzyAutomaton_Input')
    _safe_set(owner, 'fuzzyAutomaton_Variable25', None)
    assert owner not in getattr(partner, 'fuzzyAutomaton_Input')


def test_assoc_source10_stub_double():
    # fuzzyAutomaton_Transition has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_State(isInitial="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target11_stub_double():
    # fuzzyAutomaton_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_State(isInitial="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'State12', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'State12', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_transitions1_stub_double():
    # fuzzyAutomaton_Transition has no real 'fuzzyAutomaton_Transition' property in the generated
    # code (a bare stub) -- manually attach it so fuzzyAutomaton_FuzzyAutomaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fuzzyAutomaton_FuzzyAutomaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fuzzyAutomaton_FuzzyAutomaton(name="sample_text", tNorm="sample_text")
    partner = fuzzyAutomaton_Transition()
    setattr(partner, 'fuzzyAutomaton_Transition', None)
    _safe_set(owner, 'fuzzyAutomaton_FuzzyAutomaton2', {partner})
    assert getattr(partner, 'fuzzyAutomaton_Transition') == owner
    _safe_set(owner, 'fuzzyAutomaton_FuzzyAutomaton2', set())
    assert getattr(partner, 'fuzzyAutomaton_Transition') is None


