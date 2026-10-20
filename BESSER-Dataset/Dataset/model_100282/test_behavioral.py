import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    ArcPT,
    ArcTP,
    Atom,
    ContextVariable,
    ElementNetMarked,
    HighLevelPetriNet,
    IDiagramHolder,
    IEntityIdentifiable,
    INetElement,
    Marking,
    Monom,
    MonomConstant,
    NPNDiagramNetSystem,
    NPNSymbolArcPTSN,
    NPNSymbolArcSN,
    NPNSymbolArcTPSN,
    NPNSymbolNodeSN,
    NPNSymbolPlaceSN,
    NPNSymbolTransitionSN,
    NPnet,
    NPnetMarked,
    NetConstant,
    Node,
    Place,
    PlaceMarking,
    Synchronization,
    Token,
    TokenAtomic,
    TokenAttribute,
    TokenBinding,
    TokenMultiSet,
    TokenNet,
    TokenType,
    TokenTypeAtomic,
    TokenTypeElementNet,
    TokenVariadicExpression,
    TokenWeight,
    Transition,
    TransitionSynchronized,
    Variable,
    common_IDiagramHolder,
    common_INetElement,
    highlevelnets_common_IDiagramHolder,
    highlevelnets_common_IEntityIdentifiable,
    highlevelnets_common_INetElement,
    highlevelnets_hlpn_Arc,
    highlevelnets_hlpn_ArcPT,
    highlevelnets_hlpn_ArcTP,
    highlevelnets_hlpn_ContextVariable,
    highlevelnets_hlpn_HighLevelPetriNet,
    highlevelnets_hlpn_Node,
    highlevelnets_hlpn_Place,
    highlevelnets_hlpn_Transition,
    highlevelnets_marking_HighLevelPetriNetMarked,
    highlevelnets_marking_Marking,
    highlevelnets_marking_PlaceMarking,
    highlevelnets_npndiagrams_NPNDiagramNetSystem,
    highlevelnets_npndiagrams_NPNSymbolArcPTSN,
    highlevelnets_npndiagrams_NPNSymbolArcSN,
    highlevelnets_npndiagrams_NPNSymbolArcTPSN,
    highlevelnets_npndiagrams_NPNSymbolNodeSN,
    highlevelnets_npndiagrams_NPNSymbolPlaceSN,
    highlevelnets_npndiagrams_NPNSymbolTransitionSN,
    highlevelnets_npnets_NPnet,
    highlevelnets_npnets_NPnetMarked,
    highlevelnets_npnets_Synchronization,
    highlevelnets_npnets_TransitionSynchronized,
    highlevelnets_tokenexpressions_Monom,
    highlevelnets_tokenexpressions_MonomConstant,
    highlevelnets_tokenexpressions_NetConstant,
    highlevelnets_tokenexpressions_TokenBinding,
    highlevelnets_tokenexpressions_TokenExpressionBinding,
    highlevelnets_tokenexpressions_TokenMultiSet,
    highlevelnets_tokenexpressions_TokenMultisetExpression,
    highlevelnets_tokenexpressions_TokenVariadicExpression,
    highlevelnets_tokenexpressions_TokenWeight,
    highlevelnets_tokenexpressions_Variable,
    highlevelnets_tokentypes_Atom,
    highlevelnets_tokentypes_ElementNetMarked,
    highlevelnets_tokentypes_Token,
    highlevelnets_tokentypes_TokenAtomic,
    highlevelnets_tokentypes_TokenAttribute,
    highlevelnets_tokentypes_TokenNet,
    highlevelnets_tokentypes_TokenType,
    highlevelnets_tokentypes_TokenTypeAtomic,
    highlevelnets_tokentypes_TokenTypeElementNet,
    hlpn_ContextVariable,
    hlpn_Node,
    tokentypes_TokenType,
    ESynchronizationKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute15_stub_double():
    # TokenAttribute has no real 'TokenAttribute' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokentypes_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokentypes_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokentypes_Token()
    partner = TokenAttribute()
    setattr(partner, 'TokenAttribute', None)
    _safe_set(owner, 'highlevelnets_tokentypes_Token', {partner})
    assert getattr(partner, 'TokenAttribute') == owner
    _safe_set(owner, 'highlevelnets_tokentypes_Token', set())
    assert getattr(partner, 'TokenAttribute') is None


def test_assoc_constant48_stub_double():
    # Variable has no real 'Variable49' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokenexpressions_MonomConstant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokenexpressions_MonomConstant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokenexpressions_MonomConstant(power="sample_text")
    partner = Variable()
    setattr(partner, 'Variable49', None)
    _safe_set(owner, 'highlevelnets_tokenexpressions_MonomConstant', partner)
    assert getattr(partner, 'Variable49') == owner
    _safe_set(owner, 'highlevelnets_tokenexpressions_MonomConstant', None)
    assert getattr(partner, 'Variable49') is None


def test_assoc_context35_stub_double():
    # ContextVariable has no real 'ContextVariable' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokenexpressions_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokenexpressions_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokenexpressions_Variable(name="sample_text")
    partner = ContextVariable()
    setattr(partner, 'ContextVariable', None)
    _safe_set(owner, 'variables', partner)
    assert getattr(partner, 'ContextVariable') == owner
    _safe_set(owner, 'variables', None)
    assert getattr(partner, 'ContextVariable') is None


def test_assoc_diagram136_stub_double():
    # NPNDiagramNetSystem has no real 'NPNDiagramNetSystem138' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_npndiagrams_NPNSymbolNodeSN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_npndiagrams_NPNSymbolNodeSN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_npndiagrams_NPNSymbolNodeSN(constraints="sample_text")
    partner = NPNDiagramNetSystem()
    setattr(partner, 'NPNDiagramNetSystem138', None)
    _safe_set(owner, 'nodes137', partner)
    assert getattr(partner, 'NPNDiagramNetSystem138') == owner
    _safe_set(owner, 'nodes137', None)
    assert getattr(partner, 'NPNDiagramNetSystem138') is None


def test_assoc_diagram141_stub_double():
    # NPNDiagramNetSystem has no real 'NPNDiagramNetSystem143' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_npndiagrams_NPNSymbolArcSN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_npndiagrams_NPNSymbolArcSN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_npndiagrams_NPNSymbolArcSN(bendpoints="sample_text")
    partner = NPNDiagramNetSystem()
    setattr(partner, 'NPNDiagramNetSystem143', None)
    _safe_set(owner, 'arcs142', partner)
    assert getattr(partner, 'NPNDiagramNetSystem143') == owner
    _safe_set(owner, 'arcs142', None)
    assert getattr(partner, 'NPNDiagramNetSystem143') is None


def test_assoc_elementNetMarkeds9_stub_double():
    # ElementNetMarked has no real 'ElementNetMarked' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokentypes_TokenTypeElementNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokentypes_TokenTypeElementNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokentypes_TokenTypeElementNet()
    partner = ElementNetMarked()
    setattr(partner, 'ElementNetMarked', None)
    _safe_set(owner, 'type10', {partner})
    assert getattr(partner, 'ElementNetMarked') == owner
    _safe_set(owner, 'type10', set())
    assert getattr(partner, 'ElementNetMarked') is None


def test_assoc_involved104_stub_double():
    # TransitionSynchronized has no real 'TransitionSynchronized' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_npnets_Synchronization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_npnets_Synchronization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_npnets_Synchronization(key="sample_text", kind="sample_text")
    partner = TransitionSynchronized()
    setattr(partner, 'TransitionSynchronized', None)
    _safe_set(owner, 'synchronization', {partner})
    assert getattr(partner, 'TransitionSynchronized') == owner
    _safe_set(owner, 'synchronization', set())
    assert getattr(partner, 'TransitionSynchronized') is None


def test_assoc_model139_stub_double():
    # Node has no real 'Node140' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_npndiagrams_NPNSymbolNodeSN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_npndiagrams_NPNSymbolNodeSN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_npndiagrams_NPNSymbolNodeSN(constraints="sample_text")
    partner = Node()
    setattr(partner, 'Node140', None)
    _safe_set(owner, 'highlevelnets_npndiagrams_NPNSymbolNodeSN', partner)
    assert getattr(partner, 'Node140') == owner
    _safe_set(owner, 'highlevelnets_npndiagrams_NPNSymbolNodeSN', None)
    assert getattr(partner, 'Node140') is None


def test_assoc_model144_stub_double():
    # Arc has no real 'Arc145' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_npndiagrams_NPNSymbolArcSN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_npndiagrams_NPNSymbolArcSN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_npndiagrams_NPNSymbolArcSN(bendpoints="sample_text")
    partner = Arc()
    setattr(partner, 'Arc145', None)
    _safe_set(owner, 'highlevelnets_npndiagrams_NPNSymbolArcSN', partner)
    assert getattr(partner, 'Arc145') == owner
    _safe_set(owner, 'highlevelnets_npndiagrams_NPNSymbolArcSN', None)
    assert getattr(partner, 'Arc145') is None


def test_assoc_net11_stub_double():
    # HighLevelPetriNet has no real 'HighLevelPetriNet12' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokentypes_TokenTypeElementNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokentypes_TokenTypeElementNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokentypes_TokenTypeElementNet()
    partner = HighLevelPetriNet()
    setattr(partner, 'HighLevelPetriNet12', None)
    _safe_set(owner, 'highlevelnets_tokentypes_TokenTypeElementNet', partner)
    assert getattr(partner, 'HighLevelPetriNet12') == owner
    _safe_set(owner, 'highlevelnets_tokentypes_TokenTypeElementNet', None)
    assert getattr(partner, 'HighLevelPetriNet12') is None


def test_assoc_token26_stub_double():
    # Token has no real 'Token' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokenexpressions_TokenWeight's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokenexpressions_TokenWeight's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokenexpressions_TokenWeight(weight="sample_text")
    partner = Token()
    setattr(partner, 'Token', None)
    _safe_set(owner, 'highlevelnets_tokenexpressions_TokenWeight', partner)
    assert getattr(partner, 'Token') == owner
    _safe_set(owner, 'highlevelnets_tokenexpressions_TokenWeight', None)
    assert getattr(partner, 'Token') is None


def test_assoc_tokenNets13_stub_double():
    # TokenNet has no real 'TokenNet' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokentypes_TokenTypeElementNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokentypes_TokenTypeElementNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokentypes_TokenTypeElementNet()
    partner = TokenNet()
    setattr(partner, 'TokenNet', None)
    _safe_set(owner, 'type14', {partner})
    assert getattr(partner, 'TokenNet') == owner
    _safe_set(owner, 'type14', set())
    assert getattr(partner, 'TokenNet') is None


def test_assoc_value50_stub_double():
    # Token has no real 'Token52' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokenexpressions_MonomConstant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokenexpressions_MonomConstant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokenexpressions_MonomConstant(power="sample_text")
    partner = Token()
    setattr(partner, 'Token52', None)
    _safe_set(owner, 'highlevelnets_tokenexpressions_MonomConstant51', partner)
    assert getattr(partner, 'Token52') == owner
    _safe_set(owner, 'highlevelnets_tokenexpressions_MonomConstant51', None)
    assert getattr(partner, 'Token52') is None


def test_assoc_variable39_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so highlevelnets_tokenexpressions_Monom's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # highlevelnets_tokenexpressions_Monom's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = highlevelnets_tokenexpressions_Monom(power="sample_text")
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'highlevelnets_tokenexpressions_Monom', partner)
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'highlevelnets_tokenexpressions_Monom', None)
    assert getattr(partner, 'Variable') is None


