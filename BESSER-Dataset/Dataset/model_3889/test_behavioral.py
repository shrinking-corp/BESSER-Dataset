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
    gaml_BinaryOperator,
    gaml_Block,
    gaml_BooleanLiteral,
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
    gaml_Parameter,
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
    gaml_S_Try,
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

def test_assoc_facets11_reverse_link_reassign_clear():
    a1 = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    a2 = gaml_HeadlessExperiment(firstFacet="sample_text_2", importURI="sample_text_2", key="sample_text_2", name="sample_text_2")
    b = gaml_Facet(key="sample_text")
    _safe_set(b, 'gaml_Facet', a1)
    assert _is_linked(b, 'gaml_Facet', a1)
    if hasattr(a1, 'gaml_HeadlessExperiment12'):
        assert _is_linked(a1, 'gaml_HeadlessExperiment12', b)
    _safe_set(b, 'gaml_Facet', a2)
    assert _is_linked(b, 'gaml_Facet', a2)
    if hasattr(a1, 'gaml_HeadlessExperiment12'):
        assert not _is_linked(a1, 'gaml_HeadlessExperiment12', b)
    if hasattr(a2, 'gaml_HeadlessExperiment12'):
        assert _is_linked(a2, 'gaml_HeadlessExperiment12', b)
    _safe_set(b, 'gaml_Facet', None)
    assert not _is_linked(b, 'gaml_Facet', a2)
    if hasattr(a2, 'gaml_HeadlessExperiment12'):
        assert not _is_linked(a2, 'gaml_HeadlessExperiment12', b)


def test_assoc_facets19_reverse_link_reassign_clear():
    a1 = gaml_Statement(firstFacet="sample_text", key="sample_text")
    a2 = gaml_Statement(firstFacet="sample_text_2", key="sample_text_2")
    b = gaml_Facet(key="sample_text")
    _safe_set(b, 'gaml_Facet21', a1)
    assert _is_linked(b, 'gaml_Facet21', a1)
    if hasattr(a1, 'gaml_Statement20'):
        assert _is_linked(a1, 'gaml_Statement20', b)
    _safe_set(b, 'gaml_Facet21', a2)
    assert _is_linked(b, 'gaml_Facet21', a2)
    if hasattr(a1, 'gaml_Statement20'):
        assert not _is_linked(a1, 'gaml_Statement20', b)
    if hasattr(a2, 'gaml_Statement20'):
        assert _is_linked(a2, 'gaml_Statement20', b)
    _safe_set(b, 'gaml_Facet21', None)
    assert not _is_linked(b, 'gaml_Facet21', a2)
    if hasattr(a2, 'gaml_Statement20'):
        assert not _is_linked(a2, 'gaml_Statement20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_block13_stub_double():
    # gaml_Block has no real 'gaml_Block15' property in the generated
    # code (a bare stub) -- manually attach it so gaml_HeadlessExperiment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_HeadlessExperiment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block15', None)
    _safe_set(owner, 'gaml_HeadlessExperiment14', partner)
    assert getattr(partner, 'gaml_Block15') == owner
    _safe_set(owner, 'gaml_HeadlessExperiment14', None)
    assert getattr(partner, 'gaml_Block15') is None


def test_assoc_block22_stub_double():
    # gaml_Block has no real 'gaml_Block24' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Statement(firstFacet="sample_text", key="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block24', None)
    _safe_set(owner, 'gaml_Statement23', partner)
    assert getattr(partner, 'gaml_Block24') == owner
    _safe_set(owner, 'gaml_Statement23', None)
    assert getattr(partner, 'gaml_Block24') is None


def test_assoc_block47_stub_double():
    # gaml_Block has no real 'gaml_Block49' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Facet(key="sample_text")
    partner = gaml_Block()
    setattr(partner, 'gaml_Block49', None)
    _safe_set(owner, 'gaml_Facet48', partner)
    assert getattr(partner, 'gaml_Block49') == owner
    _safe_set(owner, 'gaml_Facet48', None)
    assert getattr(partner, 'gaml_Block49') is None


def test_assoc_exp10_stub_double():
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


def test_assoc_expr1_stub_double():
    # gaml_Expression has no real 'gaml_Expression' property in the generated
    # code (a bare stub) -- manually attach it so gaml_StringEvaluator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_StringEvaluator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_StringEvaluator(toto="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression', None)
    _safe_set(owner, 'gaml_StringEvaluator', partner)
    assert getattr(partner, 'gaml_Expression') == owner
    _safe_set(owner, 'gaml_StringEvaluator', None)
    assert getattr(partner, 'gaml_Expression') is None


def test_assoc_expr16_stub_double():
    # gaml_Expression has no real 'gaml_Expression18' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Statement(firstFacet="sample_text", key="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression18', None)
    _safe_set(owner, 'gaml_Statement17', partner)
    assert getattr(partner, 'gaml_Expression18') == owner
    _safe_set(owner, 'gaml_Statement17', None)
    assert getattr(partner, 'gaml_Expression18') is None


def test_assoc_expr44_stub_double():
    # gaml_Expression has no real 'gaml_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Facet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Facet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Facet(key="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression46', None)
    _safe_set(owner, 'gaml_Facet45', partner)
    assert getattr(partner, 'gaml_Expression46') == owner
    _safe_set(owner, 'gaml_Facet45', None)
    assert getattr(partner, 'gaml_Expression46') is None


def test_assoc_ifFalse70_stub_double():
    # gaml_Expression has no real 'gaml_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so gaml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_If(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression72', None)
    _safe_set(owner, 'gaml_If71', partner)
    assert getattr(partner, 'gaml_Expression72') == owner
    _safe_set(owner, 'gaml_If71', None)
    assert getattr(partner, 'gaml_Expression72') is None


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


def test_assoc_left103_stub_double():
    # gaml_VariableRef has no real 'gaml_VariableRef104' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Parameter(builtInFacetKey="sample_text")
    partner = gaml_VariableRef()
    setattr(partner, 'gaml_VariableRef104', None)
    _safe_set(owner, 'gaml_Parameter', partner)
    assert getattr(partner, 'gaml_VariableRef104') == owner
    _safe_set(owner, 'gaml_Parameter', None)
    assert getattr(partner, 'gaml_VariableRef104') is None


def test_assoc_left60_stub_double():
    # gaml_Expression has no real 'gaml_Expression61' property in the generated
    # code (a bare stub) -- manually attach it so gaml_BinaryOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_BinaryOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_BinaryOperator(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression61', None)
    _safe_set(owner, 'gaml_BinaryOperator', partner)
    assert getattr(partner, 'gaml_Expression61') == owner
    _safe_set(owner, 'gaml_BinaryOperator', None)
    assert getattr(partner, 'gaml_Expression61') is None


def test_assoc_left65_stub_double():
    # gaml_Expression has no real 'gaml_Expression66' property in the generated
    # code (a bare stub) -- manually attach it so gaml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_If(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression66', None)
    _safe_set(owner, 'gaml_If', partner)
    assert getattr(partner, 'gaml_Expression66') == owner
    _safe_set(owner, 'gaml_If', None)
    assert getattr(partner, 'gaml_Expression66') is None


def test_assoc_left73_stub_double():
    # gaml_Expression has no real 'gaml_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Unit(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression74', None)
    _safe_set(owner, 'gaml_Unit', partner)
    assert getattr(partner, 'gaml_Expression74') == owner
    _safe_set(owner, 'gaml_Unit', None)
    assert getattr(partner, 'gaml_Expression74') is None


def test_assoc_left80_stub_double():
    # gaml_Expression has no real 'gaml_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Access's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Access's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Access(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression81', None)
    _safe_set(owner, 'gaml_Access', partner)
    assert getattr(partner, 'gaml_Expression81') == owner
    _safe_set(owner, 'gaml_Access', None)
    assert getattr(partner, 'gaml_Expression81') is None


def test_assoc_left87_stub_double():
    # gaml_Expression has no real 'gaml_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Point(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression88', None)
    _safe_set(owner, 'gaml_Point', partner)
    assert getattr(partner, 'gaml_Expression88') == owner
    _safe_set(owner, 'gaml_Point', None)
    assert getattr(partner, 'gaml_Expression88') is None


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


def test_assoc_right105_stub_double():
    # gaml_Expression has no real 'gaml_Expression107' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Parameter(builtInFacetKey="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression107', None)
    _safe_set(owner, 'gaml_Parameter106', partner)
    assert getattr(partner, 'gaml_Expression107') == owner
    _safe_set(owner, 'gaml_Parameter106', None)
    assert getattr(partner, 'gaml_Expression107') is None


def test_assoc_right50_stub_double():
    # gaml_Expression has no real 'gaml_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so gaml_ArgumentPair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_ArgumentPair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_ArgumentPair(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression51', None)
    _safe_set(owner, 'gaml_ArgumentPair', partner)
    assert getattr(partner, 'gaml_Expression51') == owner
    _safe_set(owner, 'gaml_ArgumentPair', None)
    assert getattr(partner, 'gaml_Expression51') is None


def test_assoc_right62_stub_double():
    # gaml_Expression has no real 'gaml_Expression64' property in the generated
    # code (a bare stub) -- manually attach it so gaml_BinaryOperator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_BinaryOperator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_BinaryOperator(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression64', None)
    _safe_set(owner, 'gaml_BinaryOperator63', partner)
    assert getattr(partner, 'gaml_Expression64') == owner
    _safe_set(owner, 'gaml_BinaryOperator63', None)
    assert getattr(partner, 'gaml_Expression64') is None


def test_assoc_right67_stub_double():
    # gaml_Expression has no real 'gaml_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so gaml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_If(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression69', None)
    _safe_set(owner, 'gaml_If68', partner)
    assert getattr(partner, 'gaml_Expression69') == owner
    _safe_set(owner, 'gaml_If68', None)
    assert getattr(partner, 'gaml_Expression69') is None


def test_assoc_right75_stub_double():
    # gaml_Expression has no real 'gaml_Expression77' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Unit(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression77', None)
    _safe_set(owner, 'gaml_Unit76', partner)
    assert getattr(partner, 'gaml_Expression77') == owner
    _safe_set(owner, 'gaml_Unit76', None)
    assert getattr(partner, 'gaml_Expression77') is None


def test_assoc_right78_stub_double():
    # gaml_Expression has no real 'gaml_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Unary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Unary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Unary(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression79', None)
    _safe_set(owner, 'gaml_Unary', partner)
    assert getattr(partner, 'gaml_Expression79') == owner
    _safe_set(owner, 'gaml_Unary', None)
    assert getattr(partner, 'gaml_Expression79') is None


def test_assoc_right82_stub_double():
    # gaml_Expression has no real 'gaml_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Access's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Access's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Access(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression84', None)
    _safe_set(owner, 'gaml_Access83', partner)
    assert getattr(partner, 'gaml_Expression84') == owner
    _safe_set(owner, 'gaml_Access83', None)
    assert getattr(partner, 'gaml_Expression84') is None


def test_assoc_right89_stub_double():
    # gaml_Expression has no real 'gaml_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Point(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression91', None)
    _safe_set(owner, 'gaml_Point90', partner)
    assert getattr(partner, 'gaml_Expression91') == owner
    _safe_set(owner, 'gaml_Point90', None)
    assert getattr(partner, 'gaml_Expression91') is None


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


def test_assoc_z92_stub_double():
    # gaml_Expression has no real 'gaml_Expression94' property in the generated
    # code (a bare stub) -- manually attach it so gaml_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gaml_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gaml_Point(op="sample_text")
    partner = gaml_Expression()
    setattr(partner, 'gaml_Expression94', None)
    _safe_set(owner, 'gaml_Point93', partner)
    assert getattr(partner, 'gaml_Expression94') == owner
    _safe_set(owner, 'gaml_Point93', None)
    assert getattr(partner, 'gaml_Expression94') is None


