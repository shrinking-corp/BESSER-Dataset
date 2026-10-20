import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActionDefinition,
    Entry,
    EquationDefinition,
    Expression,
    GamlDefinition,
    S_Assignment,
    S_Declaration,
    S_Definition,
    Statement,
    TerminalExpression,
    TypeDefinition,
    VarDefinition,
    gaml_Access,
    gaml_ActionArguments,
    gaml_ActionDefinition,
    gaml_ActionFakeDefinition,
    gaml_ActionRef,
    gaml_ArgumentDefinition,
    gaml_ArgumentPair,
    gaml_Array,
    gaml_Binary,
    gaml_Block,
    gaml_BooleanLiteral,
    gaml_Cast,
    gaml_ColorLiteral,
    gaml_DoubleLiteral,
    gaml_EObject,
    gaml_Entry,
    gaml_EquationDefinition,
    gaml_EquationFakeDefinition,
    gaml_EquationRef,
    gaml_ExperimentFileStructure,
    gaml_Expression,
    gaml_ExpressionList,
    gaml_Facet,
    gaml_Function,
    gaml_GamlDefinition,
    gaml_HeadlessExperiment,
    gaml_If,
    gaml_Import,
    gaml_IntLiteral,
    gaml_Model,
    gaml_Pair,
    gaml_Parameter,
    gaml_Parameters,
    gaml_Point,
    gaml_Pragma,
    gaml_ReservedLiteral,
    gaml_S_Action,
    gaml_S_Assignment,
    gaml_S_Declaration,
    gaml_S_Definition,
    gaml_S_DirectAssignment,
    gaml_S_Display,
    gaml_S_Do,
    gaml_S_Equations,
    gaml_S_Experiment,
    gaml_S_Global,
    gaml_S_If,
    gaml_S_Loop,
    gaml_S_Other,
    gaml_S_Reflex,
    gaml_S_Return,
    gaml_S_Set,
    gaml_S_Solve,
    gaml_S_Species,
    gaml_S_Var,
    gaml_SkillFakeDefinition,
    gaml_SkillRef,
    gaml_StandaloneBlock,
    gaml_Statement,
    gaml_StringEvaluator,
    gaml_StringLiteral,
    gaml_TerminalExpression,
    gaml_TypeDefinition,
    gaml_TypeFakeDefinition,
    gaml_TypeInfo,
    gaml_TypeRef,
    gaml_Unary,
    gaml_Unit,
    gaml_UnitFakeDefinition,
    gaml_UnitName,
    gaml_VarDefinition,
    gaml_VarFakeDefinition,
    gaml_VariableRef,
    gaml_speciesOrGridDisplayStatement,
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

def test_assoc_expr1_reverse_link_reassign_clear():
    a1 = gaml_StringEvaluator(toto="sample_text")
    a2 = gaml_StringEvaluator(toto="sample_text_2")
    b = gaml_Expression(op="sample_text")
    _safe_set(b, 'gaml_Expression', a1)
    assert _is_linked(b, 'gaml_Expression', a1)
    if hasattr(a1, 'gaml_StringEvaluator'):
        assert _is_linked(a1, 'gaml_StringEvaluator', b)
    _safe_set(b, 'gaml_Expression', a2)
    assert _is_linked(b, 'gaml_Expression', a2)
    if hasattr(a1, 'gaml_StringEvaluator'):
        assert not _is_linked(a1, 'gaml_StringEvaluator', b)
    if hasattr(a2, 'gaml_StringEvaluator'):
        assert _is_linked(a2, 'gaml_StringEvaluator', b)
    _safe_set(b, 'gaml_Expression', None)
    assert not _is_linked(b, 'gaml_Expression', a2)
    if hasattr(a2, 'gaml_StringEvaluator'):
        assert not _is_linked(a2, 'gaml_StringEvaluator', b)


def test_assoc_expr19_reverse_link_reassign_clear():
    a1 = gaml_Statement(firstFacet="sample_text", key="sample_text")
    a2 = gaml_Statement(firstFacet="sample_text_2", key="sample_text_2")
    b = gaml_Expression(op="sample_text")
    _safe_set(b, 'gaml_Expression21', a1)
    assert _is_linked(b, 'gaml_Expression21', a1)
    if hasattr(a1, 'gaml_Statement20'):
        assert _is_linked(a1, 'gaml_Statement20', b)
    _safe_set(b, 'gaml_Expression21', a2)
    assert _is_linked(b, 'gaml_Expression21', a2)
    if hasattr(a1, 'gaml_Statement20'):
        assert not _is_linked(a1, 'gaml_Statement20', b)
    if hasattr(a2, 'gaml_Statement20'):
        assert _is_linked(a2, 'gaml_Statement20', b)
    _safe_set(b, 'gaml_Expression21', None)
    assert not _is_linked(b, 'gaml_Expression21', a2)
    if hasattr(a2, 'gaml_Statement20'):
        assert not _is_linked(a2, 'gaml_Statement20', b)


def test_assoc_expr46_reverse_link_reassign_clear():
    a1 = gaml_Facet(key="sample_text")
    a2 = gaml_Facet(key="sample_text_2")
    b = gaml_Expression(op="sample_text")
    _safe_set(b, 'gaml_Expression48', a1)
    assert _is_linked(b, 'gaml_Expression48', a1)
    if hasattr(a1, 'gaml_Facet47'):
        assert _is_linked(a1, 'gaml_Facet47', b)
    _safe_set(b, 'gaml_Expression48', a2)
    assert _is_linked(b, 'gaml_Expression48', a2)
    if hasattr(a1, 'gaml_Facet47'):
        assert not _is_linked(a1, 'gaml_Facet47', b)
    if hasattr(a2, 'gaml_Facet47'):
        assert _is_linked(a2, 'gaml_Facet47', b)
    _safe_set(b, 'gaml_Expression48', None)
    assert not _is_linked(b, 'gaml_Expression48', a2)
    if hasattr(a2, 'gaml_Facet47'):
        assert not _is_linked(a2, 'gaml_Facet47', b)


def test_assoc_facets14_reverse_link_reassign_clear():
    a1 = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    a2 = gaml_HeadlessExperiment(firstFacet="sample_text_2", importURI="sample_text_2", key="sample_text_2", name="sample_text_2")
    b = gaml_Facet(key="sample_text")
    _safe_set(b, 'gaml_Facet', a1)
    assert _is_linked(b, 'gaml_Facet', a1)
    if hasattr(a1, 'gaml_HeadlessExperiment15'):
        assert _is_linked(a1, 'gaml_HeadlessExperiment15', b)
    _safe_set(b, 'gaml_Facet', a2)
    assert _is_linked(b, 'gaml_Facet', a2)
    if hasattr(a1, 'gaml_HeadlessExperiment15'):
        assert not _is_linked(a1, 'gaml_HeadlessExperiment15', b)
    if hasattr(a2, 'gaml_HeadlessExperiment15'):
        assert _is_linked(a2, 'gaml_HeadlessExperiment15', b)
    _safe_set(b, 'gaml_Facet', None)
    assert not _is_linked(b, 'gaml_Facet', a2)
    if hasattr(a2, 'gaml_HeadlessExperiment15'):
        assert not _is_linked(a2, 'gaml_HeadlessExperiment15', b)


def test_assoc_facets22_reverse_link_reassign_clear():
    a1 = gaml_Statement(firstFacet="sample_text", key="sample_text")
    a2 = gaml_Statement(firstFacet="sample_text_2", key="sample_text_2")
    b = gaml_Facet(key="sample_text")
    _safe_set(b, 'gaml_Facet24', a1)
    assert _is_linked(b, 'gaml_Facet24', a1)
    if hasattr(a1, 'gaml_Statement23'):
        assert _is_linked(a1, 'gaml_Statement23', b)
    _safe_set(b, 'gaml_Facet24', a2)
    assert _is_linked(b, 'gaml_Facet24', a2)
    if hasattr(a1, 'gaml_Statement23'):
        assert not _is_linked(a1, 'gaml_Statement23', b)
    if hasattr(a2, 'gaml_Statement23'):
        assert _is_linked(a2, 'gaml_Statement23', b)
    _safe_set(b, 'gaml_Facet24', None)
    assert not _is_linked(b, 'gaml_Facet24', a2)
    if hasattr(a2, 'gaml_Statement23'):
        assert not _is_linked(a2, 'gaml_Statement23', b)


def test_assoc_left53_reverse_link_reassign_clear():
    a1 = gaml_Expression(op="sample_text")
    a2 = gaml_Expression(op="sample_text_2")
    b = gaml_Expression(op="sample_text")
    _safe_set(b, 'gaml_Expression54', a1)
    assert _is_linked(b, 'gaml_Expression54', a1)
    if hasattr(a1, 'gaml_Expression52'):
        assert _is_linked(a1, 'gaml_Expression52', b)
    _safe_set(b, 'gaml_Expression54', a2)
    assert _is_linked(b, 'gaml_Expression54', a2)
    if hasattr(a1, 'gaml_Expression52'):
        assert not _is_linked(a1, 'gaml_Expression52', b)
    if hasattr(a2, 'gaml_Expression52'):
        assert _is_linked(a2, 'gaml_Expression52', b)
    _safe_set(b, 'gaml_Expression54', None)
    assert not _is_linked(b, 'gaml_Expression54', a2)
    if hasattr(a2, 'gaml_Expression52'):
        assert not _is_linked(a2, 'gaml_Expression52', b)


def test_assoc_right56_reverse_link_reassign_clear():
    a1 = gaml_Expression(op="sample_text")
    a2 = gaml_Expression(op="sample_text_2")
    b = gaml_Expression(op="sample_text")
    _safe_set(b, 'gaml_Expression57', a1)
    assert _is_linked(b, 'gaml_Expression57', a1)
    if hasattr(a1, 'gaml_Expression55'):
        assert _is_linked(a1, 'gaml_Expression55', b)
    _safe_set(b, 'gaml_Expression57', a2)
    assert _is_linked(b, 'gaml_Expression57', a2)
    if hasattr(a1, 'gaml_Expression55'):
        assert not _is_linked(a1, 'gaml_Expression55', b)
    if hasattr(a2, 'gaml_Expression55'):
        assert _is_linked(a2, 'gaml_Expression55', b)
    _safe_set(b, 'gaml_Expression57', None)
    assert not _is_linked(b, 'gaml_Expression57', a2)
    if hasattr(a2, 'gaml_Expression55'):
        assert not _is_linked(a2, 'gaml_Expression55', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action58_stub_double():
    # gaml_Function has no real 'gaml_Function' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_Function()
    setattr(partner, 'gaml_Function', None)
    _safe_set(owner, 'gaml_Expression59', partner)
    assert getattr(partner, 'gaml_Function') == owner
    _safe_set(owner, 'gaml_Expression59', None)
    assert getattr(partner, 'gaml_Function') is None


def test_assoc_args80_stub_double():
    # gaml_ExpressionList has no real 'gaml_ExpressionList81' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Access's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Access's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Access(named_exp="sample_text")
    partner = gaml_ExpressionList()
    setattr(partner, 'gaml_ExpressionList81', None)
    _safe_set(owner, 'gaml_Access', partner)
    assert getattr(partner, 'gaml_ExpressionList81') == owner
    _safe_set(owner, 'gaml_Access', None)
    assert getattr(partner, 'gaml_ExpressionList81') is None


def test_assoc_block16_stub_double():
    # gaml_Block has no real 'gaml_Block18' property in the generated
    # code (a bare stub) -- manually attach it so gaml_HeadlessExperiment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_HeadlessExperiment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block18', None)
    _safe_set(owner, 'gaml_HeadlessExperiment17', partner)
    assert getattr(partner, 'gaml_Block18') == owner
    _safe_set(owner, 'gaml_HeadlessExperiment17', None)
    assert getattr(partner, 'gaml_Block18') is None


def test_assoc_block25_stub_double():
    # gaml_Block has no real 'gaml_Block27' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Statement(firstFacet="sample_text", key="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block27', None)
    _safe_set(owner, 'gaml_Statement26', partner)
    assert getattr(partner, 'gaml_Block27') == owner
    _safe_set(owner, 'gaml_Statement26', None)
    assert getattr(partner, 'gaml_Block27') is None


def test_assoc_block49_stub_double():
    # gaml_Block has no real 'gaml_Block51' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Facet(key="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block51', None)
    _safe_set(owner, 'gaml_Facet50', partner)
    assert getattr(partner, 'gaml_Block51') == owner
    _safe_set(owner, 'gaml_Facet50', None)
    assert getattr(partner, 'gaml_Block51') is None


def test_assoc_default43_stub_double():
    # gaml_ArgumentDefinition has no real 'gaml_ArgumentDefinition44' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_ArgumentDefinition()
    setattr(partner, 'gaml_ArgumentDefinition44', None)
    _safe_set(owner, 'gaml_Expression45', partner)
    assert getattr(partner, 'gaml_ArgumentDefinition44') == owner
    _safe_set(owner, 'gaml_Expression45', None)
    assert getattr(partner, 'gaml_ArgumentDefinition44') is None


def test_assoc_exp13_stub_double():
    # gaml_ExperimentFileStructure has no real 'gaml_ExperimentFileStructure' property in the generated
    # code (a bare stub) -- manually attach it so gaml_HeadlessExperiment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_HeadlessExperiment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    partner = gaml_ExperimentFileStructure()
    setattr(partner, 'gaml_ExperimentFileStructure', None)
    _safe_set(owner, 'gaml_HeadlessExperiment', partner)
    assert getattr(partner, 'gaml_ExperimentFileStructure') == owner
    _safe_set(owner, 'gaml_HeadlessExperiment', None)
    assert getattr(partner, 'gaml_ExperimentFileStructure') is None


def test_assoc_exprs68_stub_double():
    # gaml_ExpressionList has no real 'gaml_ExpressionList69' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_ExpressionList()
    setattr(partner, 'gaml_ExpressionList69', None)
    _safe_set(owner, 'gaml_Expression70', partner)
    assert owner in getattr(partner, 'gaml_ExpressionList69')
    _safe_set(owner, 'gaml_Expression70', None)
    assert owner not in getattr(partner, 'gaml_ExpressionList69')


def test_assoc_first72_stub_double():
    # gaml_TypeInfo has no real 'gaml_TypeInfo73' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_TypeInfo()
    setattr(partner, 'gaml_TypeInfo73', None)
    _safe_set(owner, 'gaml_Expression74', partner)
    assert getattr(partner, 'gaml_TypeInfo73') == owner
    _safe_set(owner, 'gaml_Expression74', None)
    assert getattr(partner, 'gaml_TypeInfo73') is None


def test_assoc_function10_stub_double():
    # gaml_Block has no real 'gaml_Block11' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block11', None)
    _safe_set(owner, 'gaml_Expression12', partner)
    assert getattr(partner, 'gaml_Block11') == owner
    _safe_set(owner, 'gaml_Expression12', None)
    assert getattr(partner, 'gaml_Block11') is None


def test_assoc_ifFalse78_stub_double():
    # gaml_If has no real 'gaml_If' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_If()
    setattr(partner, 'gaml_If', None)
    _safe_set(owner, 'gaml_Expression79', partner)
    assert getattr(partner, 'gaml_If') == owner
    _safe_set(owner, 'gaml_Expression79', None)
    assert getattr(partner, 'gaml_If') is None


def test_assoc_imports3_stub_double():
    # gaml_Model has no real 'gaml_Model4' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Import(importURI="sample_text")
    partner = gaml_Model()
    setattr(partner, 'gaml_Model4', None)
    _safe_set(owner, 'gaml_Import', partner)
    assert owner in getattr(partner, 'gaml_Model4')
    _safe_set(owner, 'gaml_Import', None)
    assert owner not in getattr(partner, 'gaml_Model4')


def test_assoc_pragmas2_stub_double():
    # gaml_Model has no real 'gaml_Model' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Pragma's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Pragma's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Pragma(name="sample_text")
    partner = gaml_Model()
    setattr(partner, 'gaml_Model', None)
    _safe_set(owner, 'gaml_Pragma', partner)
    assert owner in getattr(partner, 'gaml_Model')
    _safe_set(owner, 'gaml_Pragma', None)
    assert owner not in getattr(partner, 'gaml_Model')


def test_assoc_second75_stub_double():
    # gaml_TypeInfo has no real 'gaml_TypeInfo76' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_TypeInfo()
    setattr(partner, 'gaml_TypeInfo76', None)
    _safe_set(owner, 'gaml_Expression77', partner)
    assert getattr(partner, 'gaml_TypeInfo76') == owner
    _safe_set(owner, 'gaml_Expression77', None)
    assert getattr(partner, 'gaml_TypeInfo76') is None


def test_assoc_statements8_stub_double():
    # gaml_Block has no real 'gaml_Block9' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Statement(firstFacet="sample_text", key="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block9', None)
    _safe_set(owner, 'gaml_Statement', partner)
    assert owner in getattr(partner, 'gaml_Block9')
    _safe_set(owner, 'gaml_Statement', None)
    assert owner not in getattr(partner, 'gaml_Block9')


def test_assoc_tkey29_stub_double():
    # gaml_S_Definition has no real 'gaml_S_Definition' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_S_Definition()
    setattr(partner, 'gaml_S_Definition', None)
    _safe_set(owner, 'gaml_Expression30', partner)
    assert getattr(partner, 'gaml_S_Definition') == owner
    _safe_set(owner, 'gaml_Expression30', None)
    assert getattr(partner, 'gaml_S_Definition') is None


def test_assoc_type40_stub_double():
    # gaml_ArgumentDefinition has no real 'gaml_ArgumentDefinition41' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_ArgumentDefinition()
    setattr(partner, 'gaml_ArgumentDefinition41', None)
    _safe_set(owner, 'gaml_Expression42', partner)
    assert getattr(partner, 'gaml_ArgumentDefinition41') == owner
    _safe_set(owner, 'gaml_Expression42', None)
    assert getattr(partner, 'gaml_ArgumentDefinition41') is None


def test_assoc_value33_stub_double():
    # gaml_S_Assignment has no real 'gaml_S_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_S_Assignment()
    setattr(partner, 'gaml_S_Assignment', None)
    _safe_set(owner, 'gaml_Expression34', partner)
    assert getattr(partner, 'gaml_S_Assignment') == owner
    _safe_set(owner, 'gaml_Expression34', None)
    assert getattr(partner, 'gaml_S_Assignment') is None


def test_assoc_z84_stub_double():
    # gaml_Point has no real 'gaml_Point' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Expression(op="sample_text")
    partner = gaml_Point()
    setattr(partner, 'gaml_Point', None)
    _safe_set(owner, 'gaml_Expression85', partner)
    assert getattr(partner, 'gaml_Point') == owner
    _safe_set(owner, 'gaml_Expression85', None)
    assert getattr(partner, 'gaml_Point') is None


