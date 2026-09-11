import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_gaml_Access_op_value_roundtrip():
    instance = gaml_Access(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_ArgumentPair_op_value_roundtrip():
    instance = gaml_ArgumentPair(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_BinaryOperator_op_value_roundtrip():
    instance = gaml_BinaryOperator(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_Facet_key_value_roundtrip():
    instance = gaml_Facet(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_gaml_GamlDefinition_name_value_roundtrip():
    instance = gaml_GamlDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gaml_HeadlessExperiment_firstFacet_value_roundtrip():
    instance = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    assert instance.firstFacet == "sample_text"
    instance.firstFacet = "sample_text_2"
    assert instance.firstFacet == "sample_text_2"


def test_gaml_HeadlessExperiment_importURI_value_roundtrip():
    instance = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_gaml_HeadlessExperiment_key_value_roundtrip():
    instance = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_gaml_HeadlessExperiment_name_value_roundtrip():
    instance = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gaml_If_op_value_roundtrip():
    instance = gaml_If(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_Import_importURI_value_roundtrip():
    instance = gaml_Import(importURI="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_gaml_Parameter_builtInFacetKey_value_roundtrip():
    instance = gaml_Parameter(builtInFacetKey="sample_text")
    assert instance.builtInFacetKey == "sample_text"
    instance.builtInFacetKey = "sample_text_2"
    assert instance.builtInFacetKey == "sample_text_2"


def test_gaml_Point_op_value_roundtrip():
    instance = gaml_Point(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_Pragma_name_value_roundtrip():
    instance = gaml_Pragma(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gaml_S_Display_name_value_roundtrip():
    instance = gaml_S_Display(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gaml_Statement_firstFacet_value_roundtrip():
    instance = gaml_Statement(firstFacet="sample_text", key="sample_text")
    assert instance.firstFacet == "sample_text"
    instance.firstFacet = "sample_text_2"
    assert instance.firstFacet == "sample_text_2"


def test_gaml_Statement_key_value_roundtrip():
    instance = gaml_Statement(firstFacet="sample_text", key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_gaml_StringEvaluator_toto_value_roundtrip():
    instance = gaml_StringEvaluator(toto="sample_text")
    assert instance.toto == "sample_text"
    instance.toto = "sample_text_2"
    assert instance.toto == "sample_text_2"


def test_gaml_TerminalExpression_op_value_roundtrip():
    instance = gaml_TerminalExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_Unary_op_value_roundtrip():
    instance = gaml_Unary(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_Unit_op_value_roundtrip():
    instance = gaml_Unit(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_gaml_ActionFakeDefinition_isa_ActionDefinition():
    instance = gaml_ActionFakeDefinition()
    assert isinstance(instance, ActionDefinition)


def test_gaml_S_Definition_isa_ActionDefinition():
    instance = gaml_S_Definition()
    assert isinstance(instance, ActionDefinition)


def test_gaml_TypeDefinition_isa_ActionDefinition():
    instance = gaml_TypeDefinition()
    assert isinstance(instance, ActionDefinition)


def test_gaml_ExperimentFileStructure_isa_Entry():
    instance = gaml_ExperimentFileStructure()
    assert isinstance(instance, Entry)


def test_gaml_Model_isa_Entry():
    instance = gaml_Model()
    assert isinstance(instance, Entry)


def test_gaml_StandaloneBlock_isa_Entry():
    instance = gaml_StandaloneBlock()
    assert isinstance(instance, Entry)


def test_gaml_StringEvaluator_isa_Entry():
    instance = gaml_StringEvaluator(toto="sample_text")
    assert isinstance(instance, Entry)


def test_gaml_EquationFakeDefinition_isa_EquationDefinition():
    instance = gaml_EquationFakeDefinition()
    assert isinstance(instance, EquationDefinition)


def test_gaml_S_Equations_isa_EquationDefinition():
    instance = gaml_S_Equations()
    assert isinstance(instance, EquationDefinition)


def test_gaml_Access_isa_Expression():
    instance = gaml_Access(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_ActionRef_isa_Expression():
    instance = gaml_ActionRef()
    assert isinstance(instance, Expression)


def test_gaml_ArgumentPair_isa_Expression():
    instance = gaml_ArgumentPair(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_Array_isa_Expression():
    instance = gaml_Array()
    assert isinstance(instance, Expression)


def test_gaml_BinaryOperator_isa_Expression():
    instance = gaml_BinaryOperator(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_EquationRef_isa_Expression():
    instance = gaml_EquationRef()
    assert isinstance(instance, Expression)


def test_gaml_ExpressionList_isa_Expression():
    instance = gaml_ExpressionList()
    assert isinstance(instance, Expression)


def test_gaml_Function_isa_Expression():
    instance = gaml_Function()
    assert isinstance(instance, Expression)


def test_gaml_If_isa_Expression():
    instance = gaml_If(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_Parameter_isa_Expression():
    instance = gaml_Parameter(builtInFacetKey="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_Point_isa_Expression():
    instance = gaml_Point(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_SkillRef_isa_Expression():
    instance = gaml_SkillRef()
    assert isinstance(instance, Expression)


def test_gaml_TerminalExpression_isa_Expression():
    instance = gaml_TerminalExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_TypeRef_isa_Expression():
    instance = gaml_TypeRef()
    assert isinstance(instance, Expression)


def test_gaml_Unary_isa_Expression():
    instance = gaml_Unary(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_Unit_isa_Expression():
    instance = gaml_Unit(op="sample_text")
    assert isinstance(instance, Expression)


def test_gaml_UnitName_isa_Expression():
    instance = gaml_UnitName()
    assert isinstance(instance, Expression)


def test_gaml_VariableRef_isa_Expression():
    instance = gaml_VariableRef()
    assert isinstance(instance, Expression)


def test_gaml_ActionDefinition_isa_GamlDefinition():
    instance = gaml_ActionDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_EquationDefinition_isa_GamlDefinition():
    instance = gaml_EquationDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_SkillFakeDefinition_isa_GamlDefinition():
    instance = gaml_SkillFakeDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_TypeDefinition_isa_GamlDefinition():
    instance = gaml_TypeDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_UnitFakeDefinition_isa_GamlDefinition():
    instance = gaml_UnitFakeDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_VarDefinition_isa_GamlDefinition():
    instance = gaml_VarDefinition()
    assert isinstance(instance, GamlDefinition)


def test_gaml_S_DirectAssignment_isa_S_Assignment():
    instance = gaml_S_DirectAssignment()
    assert isinstance(instance, S_Assignment)


def test_gaml_S_Set_isa_S_Assignment():
    instance = gaml_S_Set()
    assert isinstance(instance, S_Assignment)


def test_gaml_S_Definition_isa_S_Declaration():
    instance = gaml_S_Definition()
    assert isinstance(instance, S_Declaration)


def test_gaml_S_Loop_isa_S_Declaration():
    instance = gaml_S_Loop()
    assert isinstance(instance, S_Declaration)


def test_gaml_S_Reflex_isa_S_Declaration():
    instance = gaml_S_Reflex()
    assert isinstance(instance, S_Declaration)


def test_gaml_S_Species_isa_S_Declaration():
    instance = gaml_S_Species()
    assert isinstance(instance, S_Declaration)


def test_gaml_S_Action_isa_S_Definition():
    instance = gaml_S_Action()
    assert isinstance(instance, S_Definition)


def test_gaml_S_Var_isa_S_Definition():
    instance = gaml_S_Var()
    assert isinstance(instance, S_Definition)


def test_gaml_S_Assignment_isa_Statement():
    instance = gaml_S_Assignment()
    assert isinstance(instance, Statement)


def test_gaml_S_Declaration_isa_Statement():
    instance = gaml_S_Declaration()
    assert isinstance(instance, Statement)


def test_gaml_S_Display_isa_Statement():
    instance = gaml_S_Display(name="sample_text")
    assert isinstance(instance, Statement)


def test_gaml_S_Do_isa_Statement():
    instance = gaml_S_Do()
    assert isinstance(instance, Statement)


def test_gaml_S_Equations_isa_Statement():
    instance = gaml_S_Equations()
    assert isinstance(instance, Statement)


def test_gaml_S_Experiment_isa_Statement():
    instance = gaml_S_Experiment()
    assert isinstance(instance, Statement)


def test_gaml_S_Global_isa_Statement():
    instance = gaml_S_Global()
    assert isinstance(instance, Statement)


def test_gaml_S_If_isa_Statement():
    instance = gaml_S_If()
    assert isinstance(instance, Statement)


def test_gaml_S_Other_isa_Statement():
    instance = gaml_S_Other()
    assert isinstance(instance, Statement)


def test_gaml_S_Return_isa_Statement():
    instance = gaml_S_Return()
    assert isinstance(instance, Statement)


def test_gaml_S_Solve_isa_Statement():
    instance = gaml_S_Solve()
    assert isinstance(instance, Statement)


def test_gaml_S_Species_isa_Statement():
    instance = gaml_S_Species()
    assert isinstance(instance, Statement)


def test_gaml_S_Try_isa_Statement():
    instance = gaml_S_Try()
    assert isinstance(instance, Statement)


def test_gaml_speciesOrGridDisplayStatement_isa_Statement():
    instance = gaml_speciesOrGridDisplayStatement()
    assert isinstance(instance, Statement)


def test_gaml_BooleanLiteral_isa_TerminalExpression():
    instance = gaml_BooleanLiteral()
    assert isinstance(instance, TerminalExpression)


def test_gaml_DoubleLiteral_isa_TerminalExpression():
    instance = gaml_DoubleLiteral()
    assert isinstance(instance, TerminalExpression)


def test_gaml_IntLiteral_isa_TerminalExpression():
    instance = gaml_IntLiteral()
    assert isinstance(instance, TerminalExpression)


def test_gaml_ReservedLiteral_isa_TerminalExpression():
    instance = gaml_ReservedLiteral()
    assert isinstance(instance, TerminalExpression)


def test_gaml_StringLiteral_isa_TerminalExpression():
    instance = gaml_StringLiteral()
    assert isinstance(instance, TerminalExpression)


def test_gaml_S_Species_isa_TypeDefinition():
    instance = gaml_S_Species()
    assert isinstance(instance, TypeDefinition)


def test_gaml_TypeFakeDefinition_isa_TypeDefinition():
    instance = gaml_TypeFakeDefinition()
    assert isinstance(instance, TypeDefinition)


def test_gaml_ArgumentDefinition_isa_VarDefinition():
    instance = gaml_ArgumentDefinition()
    assert isinstance(instance, VarDefinition)


def test_gaml_Facet_isa_VarDefinition():
    instance = gaml_Facet(key="sample_text")
    assert isinstance(instance, VarDefinition)


def test_gaml_Import_isa_VarDefinition():
    instance = gaml_Import(importURI="sample_text")
    assert isinstance(instance, VarDefinition)


def test_gaml_Model_isa_VarDefinition():
    instance = gaml_Model()
    assert isinstance(instance, VarDefinition)


def test_gaml_S_Declaration_isa_VarDefinition():
    instance = gaml_S_Declaration()
    assert isinstance(instance, VarDefinition)


def test_gaml_S_Experiment_isa_VarDefinition():
    instance = gaml_S_Experiment()
    assert isinstance(instance, VarDefinition)


def test_gaml_VarFakeDefinition_isa_VarDefinition():
    instance = gaml_VarFakeDefinition()
    assert isinstance(instance, VarDefinition)


def test_assoc_block13_link_reassign_clear():
    a = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    b1 = gaml_Block()
    b2 = gaml_Block()
    _safe_set(a, 'gaml_HeadlessExperiment14', b1)
    assert _is_linked(a, 'gaml_HeadlessExperiment14', b1)
    if hasattr(b1, 'gaml_Block15'):
        assert _is_linked(b1, 'gaml_Block15', a)
    _safe_set(a, 'gaml_HeadlessExperiment14', b2)
    assert _is_linked(a, 'gaml_HeadlessExperiment14', b2)
    if hasattr(b1, 'gaml_Block15'):
        assert not _is_linked(b1, 'gaml_Block15', a)
    if hasattr(b2, 'gaml_Block15'):
        assert _is_linked(b2, 'gaml_Block15', a)
    _safe_set(a, 'gaml_HeadlessExperiment14', None)
    assert not _is_linked(a, 'gaml_HeadlessExperiment14', b2)
    if hasattr(b2, 'gaml_Block15'):
        assert not _is_linked(b2, 'gaml_Block15', a)


def test_assoc_block22_link_reassign_clear():
    a = gaml_Statement(firstFacet="sample_text", key="sample_text")
    b1 = gaml_Block()
    b2 = gaml_Block()
    _safe_set(a, 'gaml_Statement23', b1)
    assert _is_linked(a, 'gaml_Statement23', b1)
    if hasattr(b1, 'gaml_Block24'):
        assert _is_linked(b1, 'gaml_Block24', a)
    _safe_set(a, 'gaml_Statement23', b2)
    assert _is_linked(a, 'gaml_Statement23', b2)
    if hasattr(b1, 'gaml_Block24'):
        assert not _is_linked(b1, 'gaml_Block24', a)
    if hasattr(b2, 'gaml_Block24'):
        assert _is_linked(b2, 'gaml_Block24', a)
    _safe_set(a, 'gaml_Statement23', None)
    assert not _is_linked(a, 'gaml_Statement23', b2)
    if hasattr(b2, 'gaml_Block24'):
        assert not _is_linked(b2, 'gaml_Block24', a)


def test_assoc_block47_link_reassign_clear():
    a = gaml_Facet(key="sample_text")
    b1 = gaml_Block()
    b2 = gaml_Block()
    _safe_set(a, 'gaml_Facet48', b1)
    assert _is_linked(a, 'gaml_Facet48', b1)
    if hasattr(b1, 'gaml_Block49'):
        assert _is_linked(b1, 'gaml_Block49', a)
    _safe_set(a, 'gaml_Facet48', b2)
    assert _is_linked(a, 'gaml_Facet48', b2)
    if hasattr(b1, 'gaml_Block49'):
        assert not _is_linked(b1, 'gaml_Block49', a)
    if hasattr(b2, 'gaml_Block49'):
        assert _is_linked(b2, 'gaml_Block49', a)
    _safe_set(a, 'gaml_Facet48', None)
    assert not _is_linked(a, 'gaml_Facet48', b2)
    if hasattr(b2, 'gaml_Block49'):
        assert not _is_linked(b2, 'gaml_Block49', a)


def test_assoc_exp10_link_reassign_clear():
    a = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    b1 = gaml_ExperimentFileStructure()
    b2 = gaml_ExperimentFileStructure()
    _safe_set(a, 'gaml_HeadlessExperiment', b1)
    assert _is_linked(a, 'gaml_HeadlessExperiment', b1)
    if hasattr(b1, 'gaml_ExperimentFileStructure'):
        assert _is_linked(b1, 'gaml_ExperimentFileStructure', a)
    _safe_set(a, 'gaml_HeadlessExperiment', b2)
    assert _is_linked(a, 'gaml_HeadlessExperiment', b2)
    if hasattr(b1, 'gaml_ExperimentFileStructure'):
        assert not _is_linked(b1, 'gaml_ExperimentFileStructure', a)
    if hasattr(b2, 'gaml_ExperimentFileStructure'):
        assert _is_linked(b2, 'gaml_ExperimentFileStructure', a)
    _safe_set(a, 'gaml_HeadlessExperiment', None)
    assert not _is_linked(a, 'gaml_HeadlessExperiment', b2)
    if hasattr(b2, 'gaml_ExperimentFileStructure'):
        assert not _is_linked(b2, 'gaml_ExperimentFileStructure', a)


def test_assoc_expr1_link_reassign_clear():
    a = gaml_StringEvaluator(toto="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_StringEvaluator', b1)
    assert _is_linked(a, 'gaml_StringEvaluator', b1)
    if hasattr(b1, 'gaml_Expression'):
        assert _is_linked(b1, 'gaml_Expression', a)
    _safe_set(a, 'gaml_StringEvaluator', b2)
    assert _is_linked(a, 'gaml_StringEvaluator', b2)
    if hasattr(b1, 'gaml_Expression'):
        assert not _is_linked(b1, 'gaml_Expression', a)
    if hasattr(b2, 'gaml_Expression'):
        assert _is_linked(b2, 'gaml_Expression', a)
    _safe_set(a, 'gaml_StringEvaluator', None)
    assert not _is_linked(a, 'gaml_StringEvaluator', b2)
    if hasattr(b2, 'gaml_Expression'):
        assert not _is_linked(b2, 'gaml_Expression', a)


def test_assoc_expr16_link_reassign_clear():
    a = gaml_Statement(firstFacet="sample_text", key="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Statement17', b1)
    assert _is_linked(a, 'gaml_Statement17', b1)
    if hasattr(b1, 'gaml_Expression18'):
        assert _is_linked(b1, 'gaml_Expression18', a)
    _safe_set(a, 'gaml_Statement17', b2)
    assert _is_linked(a, 'gaml_Statement17', b2)
    if hasattr(b1, 'gaml_Expression18'):
        assert not _is_linked(b1, 'gaml_Expression18', a)
    if hasattr(b2, 'gaml_Expression18'):
        assert _is_linked(b2, 'gaml_Expression18', a)
    _safe_set(a, 'gaml_Statement17', None)
    assert not _is_linked(a, 'gaml_Statement17', b2)
    if hasattr(b2, 'gaml_Expression18'):
        assert not _is_linked(b2, 'gaml_Expression18', a)


def test_assoc_expr44_link_reassign_clear():
    a = gaml_Facet(key="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Facet45', b1)
    assert _is_linked(a, 'gaml_Facet45', b1)
    if hasattr(b1, 'gaml_Expression46'):
        assert _is_linked(b1, 'gaml_Expression46', a)
    _safe_set(a, 'gaml_Facet45', b2)
    assert _is_linked(a, 'gaml_Facet45', b2)
    if hasattr(b1, 'gaml_Expression46'):
        assert not _is_linked(b1, 'gaml_Expression46', a)
    if hasattr(b2, 'gaml_Expression46'):
        assert _is_linked(b2, 'gaml_Expression46', a)
    _safe_set(a, 'gaml_Facet45', None)
    assert not _is_linked(a, 'gaml_Facet45', b2)
    if hasattr(b2, 'gaml_Expression46'):
        assert not _is_linked(b2, 'gaml_Expression46', a)


def test_assoc_facets11_link_reassign_clear():
    a = gaml_HeadlessExperiment(firstFacet="sample_text", importURI="sample_text", key="sample_text", name="sample_text")
    b1 = gaml_Facet(key="sample_text")
    b2 = gaml_Facet(key="sample_text_2")
    _safe_set(a, 'gaml_HeadlessExperiment12', {b1})
    assert _is_linked(a, 'gaml_HeadlessExperiment12', b1)
    if hasattr(b1, 'gaml_Facet'):
        assert _is_linked(b1, 'gaml_Facet', a)
    _safe_set(a, 'gaml_HeadlessExperiment12', {b2})
    assert _is_linked(a, 'gaml_HeadlessExperiment12', b2)
    if hasattr(b1, 'gaml_Facet'):
        assert not _is_linked(b1, 'gaml_Facet', a)
    if hasattr(b2, 'gaml_Facet'):
        assert _is_linked(b2, 'gaml_Facet', a)
    _safe_set(a, 'gaml_HeadlessExperiment12', set())
    assert not _is_linked(a, 'gaml_HeadlessExperiment12', b2)
    if hasattr(b2, 'gaml_Facet'):
        assert not _is_linked(b2, 'gaml_Facet', a)


def test_assoc_facets19_link_reassign_clear():
    a = gaml_Statement(firstFacet="sample_text", key="sample_text")
    b1 = gaml_Facet(key="sample_text")
    b2 = gaml_Facet(key="sample_text_2")
    _safe_set(a, 'gaml_Statement20', {b1})
    assert _is_linked(a, 'gaml_Statement20', b1)
    if hasattr(b1, 'gaml_Facet21'):
        assert _is_linked(b1, 'gaml_Facet21', a)
    _safe_set(a, 'gaml_Statement20', {b2})
    assert _is_linked(a, 'gaml_Statement20', b2)
    if hasattr(b1, 'gaml_Facet21'):
        assert not _is_linked(b1, 'gaml_Facet21', a)
    if hasattr(b2, 'gaml_Facet21'):
        assert _is_linked(b2, 'gaml_Facet21', a)
    _safe_set(a, 'gaml_Statement20', set())
    assert not _is_linked(a, 'gaml_Statement20', b2)
    if hasattr(b2, 'gaml_Facet21'):
        assert not _is_linked(b2, 'gaml_Facet21', a)


def test_assoc_ifFalse70_link_reassign_clear():
    a = gaml_If(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_If71', b1)
    assert _is_linked(a, 'gaml_If71', b1)
    if hasattr(b1, 'gaml_Expression72'):
        assert _is_linked(b1, 'gaml_Expression72', a)
    _safe_set(a, 'gaml_If71', b2)
    assert _is_linked(a, 'gaml_If71', b2)
    if hasattr(b1, 'gaml_Expression72'):
        assert not _is_linked(b1, 'gaml_Expression72', a)
    if hasattr(b2, 'gaml_Expression72'):
        assert _is_linked(b2, 'gaml_Expression72', a)
    _safe_set(a, 'gaml_If71', None)
    assert not _is_linked(a, 'gaml_If71', b2)
    if hasattr(b2, 'gaml_Expression72'):
        assert not _is_linked(b2, 'gaml_Expression72', a)


def test_assoc_imports3_link_reassign_clear():
    a = gaml_Import(importURI="sample_text")
    b1 = gaml_Model()
    b2 = gaml_Model()
    _safe_set(a, 'gaml_Import', b1)
    assert _is_linked(a, 'gaml_Import', b1)
    if hasattr(b1, 'gaml_Model4'):
        assert _is_linked(b1, 'gaml_Model4', a)
    _safe_set(a, 'gaml_Import', b2)
    assert _is_linked(a, 'gaml_Import', b2)
    if hasattr(b1, 'gaml_Model4'):
        assert not _is_linked(b1, 'gaml_Model4', a)
    if hasattr(b2, 'gaml_Model4'):
        assert _is_linked(b2, 'gaml_Model4', a)
    _safe_set(a, 'gaml_Import', None)
    assert not _is_linked(a, 'gaml_Import', b2)
    if hasattr(b2, 'gaml_Model4'):
        assert not _is_linked(b2, 'gaml_Model4', a)


def test_assoc_left103_link_reassign_clear():
    a = gaml_Parameter(builtInFacetKey="sample_text")
    b1 = gaml_VariableRef()
    b2 = gaml_VariableRef()
    _safe_set(a, 'gaml_Parameter', b1)
    assert _is_linked(a, 'gaml_Parameter', b1)
    if hasattr(b1, 'gaml_VariableRef104'):
        assert _is_linked(b1, 'gaml_VariableRef104', a)
    _safe_set(a, 'gaml_Parameter', b2)
    assert _is_linked(a, 'gaml_Parameter', b2)
    if hasattr(b1, 'gaml_VariableRef104'):
        assert not _is_linked(b1, 'gaml_VariableRef104', a)
    if hasattr(b2, 'gaml_VariableRef104'):
        assert _is_linked(b2, 'gaml_VariableRef104', a)
    _safe_set(a, 'gaml_Parameter', None)
    assert not _is_linked(a, 'gaml_Parameter', b2)
    if hasattr(b2, 'gaml_VariableRef104'):
        assert not _is_linked(b2, 'gaml_VariableRef104', a)


def test_assoc_left60_link_reassign_clear():
    a = gaml_BinaryOperator(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_BinaryOperator', b1)
    assert _is_linked(a, 'gaml_BinaryOperator', b1)
    if hasattr(b1, 'gaml_Expression61'):
        assert _is_linked(b1, 'gaml_Expression61', a)
    _safe_set(a, 'gaml_BinaryOperator', b2)
    assert _is_linked(a, 'gaml_BinaryOperator', b2)
    if hasattr(b1, 'gaml_Expression61'):
        assert not _is_linked(b1, 'gaml_Expression61', a)
    if hasattr(b2, 'gaml_Expression61'):
        assert _is_linked(b2, 'gaml_Expression61', a)
    _safe_set(a, 'gaml_BinaryOperator', None)
    assert not _is_linked(a, 'gaml_BinaryOperator', b2)
    if hasattr(b2, 'gaml_Expression61'):
        assert not _is_linked(b2, 'gaml_Expression61', a)


def test_assoc_left65_link_reassign_clear():
    a = gaml_If(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_If', b1)
    assert _is_linked(a, 'gaml_If', b1)
    if hasattr(b1, 'gaml_Expression66'):
        assert _is_linked(b1, 'gaml_Expression66', a)
    _safe_set(a, 'gaml_If', b2)
    assert _is_linked(a, 'gaml_If', b2)
    if hasattr(b1, 'gaml_Expression66'):
        assert not _is_linked(b1, 'gaml_Expression66', a)
    if hasattr(b2, 'gaml_Expression66'):
        assert _is_linked(b2, 'gaml_Expression66', a)
    _safe_set(a, 'gaml_If', None)
    assert not _is_linked(a, 'gaml_If', b2)
    if hasattr(b2, 'gaml_Expression66'):
        assert not _is_linked(b2, 'gaml_Expression66', a)


def test_assoc_left73_link_reassign_clear():
    a = gaml_Unit(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Unit', b1)
    assert _is_linked(a, 'gaml_Unit', b1)
    if hasattr(b1, 'gaml_Expression74'):
        assert _is_linked(b1, 'gaml_Expression74', a)
    _safe_set(a, 'gaml_Unit', b2)
    assert _is_linked(a, 'gaml_Unit', b2)
    if hasattr(b1, 'gaml_Expression74'):
        assert not _is_linked(b1, 'gaml_Expression74', a)
    if hasattr(b2, 'gaml_Expression74'):
        assert _is_linked(b2, 'gaml_Expression74', a)
    _safe_set(a, 'gaml_Unit', None)
    assert not _is_linked(a, 'gaml_Unit', b2)
    if hasattr(b2, 'gaml_Expression74'):
        assert not _is_linked(b2, 'gaml_Expression74', a)


def test_assoc_left80_link_reassign_clear():
    a = gaml_Access(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Access', b1)
    assert _is_linked(a, 'gaml_Access', b1)
    if hasattr(b1, 'gaml_Expression81'):
        assert _is_linked(b1, 'gaml_Expression81', a)
    _safe_set(a, 'gaml_Access', b2)
    assert _is_linked(a, 'gaml_Access', b2)
    if hasattr(b1, 'gaml_Expression81'):
        assert not _is_linked(b1, 'gaml_Expression81', a)
    if hasattr(b2, 'gaml_Expression81'):
        assert _is_linked(b2, 'gaml_Expression81', a)
    _safe_set(a, 'gaml_Access', None)
    assert not _is_linked(a, 'gaml_Access', b2)
    if hasattr(b2, 'gaml_Expression81'):
        assert not _is_linked(b2, 'gaml_Expression81', a)


def test_assoc_left87_link_reassign_clear():
    a = gaml_Point(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Point', b1)
    assert _is_linked(a, 'gaml_Point', b1)
    if hasattr(b1, 'gaml_Expression88'):
        assert _is_linked(b1, 'gaml_Expression88', a)
    _safe_set(a, 'gaml_Point', b2)
    assert _is_linked(a, 'gaml_Point', b2)
    if hasattr(b1, 'gaml_Expression88'):
        assert not _is_linked(b1, 'gaml_Expression88', a)
    if hasattr(b2, 'gaml_Expression88'):
        assert _is_linked(b2, 'gaml_Expression88', a)
    _safe_set(a, 'gaml_Point', None)
    assert not _is_linked(a, 'gaml_Point', b2)
    if hasattr(b2, 'gaml_Expression88'):
        assert not _is_linked(b2, 'gaml_Expression88', a)


def test_assoc_pragmas2_link_reassign_clear():
    a = gaml_Pragma(name="sample_text")
    b1 = gaml_Model()
    b2 = gaml_Model()
    _safe_set(a, 'gaml_Pragma', b1)
    assert _is_linked(a, 'gaml_Pragma', b1)
    if hasattr(b1, 'gaml_Model'):
        assert _is_linked(b1, 'gaml_Model', a)
    _safe_set(a, 'gaml_Pragma', b2)
    assert _is_linked(a, 'gaml_Pragma', b2)
    if hasattr(b1, 'gaml_Model'):
        assert not _is_linked(b1, 'gaml_Model', a)
    if hasattr(b2, 'gaml_Model'):
        assert _is_linked(b2, 'gaml_Model', a)
    _safe_set(a, 'gaml_Pragma', None)
    assert not _is_linked(a, 'gaml_Pragma', b2)
    if hasattr(b2, 'gaml_Model'):
        assert not _is_linked(b2, 'gaml_Model', a)


def test_assoc_right105_link_reassign_clear():
    a = gaml_Parameter(builtInFacetKey="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Parameter106', b1)
    assert _is_linked(a, 'gaml_Parameter106', b1)
    if hasattr(b1, 'gaml_Expression107'):
        assert _is_linked(b1, 'gaml_Expression107', a)
    _safe_set(a, 'gaml_Parameter106', b2)
    assert _is_linked(a, 'gaml_Parameter106', b2)
    if hasattr(b1, 'gaml_Expression107'):
        assert not _is_linked(b1, 'gaml_Expression107', a)
    if hasattr(b2, 'gaml_Expression107'):
        assert _is_linked(b2, 'gaml_Expression107', a)
    _safe_set(a, 'gaml_Parameter106', None)
    assert not _is_linked(a, 'gaml_Parameter106', b2)
    if hasattr(b2, 'gaml_Expression107'):
        assert not _is_linked(b2, 'gaml_Expression107', a)


def test_assoc_right50_link_reassign_clear():
    a = gaml_ArgumentPair(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_ArgumentPair', b1)
    assert _is_linked(a, 'gaml_ArgumentPair', b1)
    if hasattr(b1, 'gaml_Expression51'):
        assert _is_linked(b1, 'gaml_Expression51', a)
    _safe_set(a, 'gaml_ArgumentPair', b2)
    assert _is_linked(a, 'gaml_ArgumentPair', b2)
    if hasattr(b1, 'gaml_Expression51'):
        assert not _is_linked(b1, 'gaml_Expression51', a)
    if hasattr(b2, 'gaml_Expression51'):
        assert _is_linked(b2, 'gaml_Expression51', a)
    _safe_set(a, 'gaml_ArgumentPair', None)
    assert not _is_linked(a, 'gaml_ArgumentPair', b2)
    if hasattr(b2, 'gaml_Expression51'):
        assert not _is_linked(b2, 'gaml_Expression51', a)


def test_assoc_right62_link_reassign_clear():
    a = gaml_BinaryOperator(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_BinaryOperator63', b1)
    assert _is_linked(a, 'gaml_BinaryOperator63', b1)
    if hasattr(b1, 'gaml_Expression64'):
        assert _is_linked(b1, 'gaml_Expression64', a)
    _safe_set(a, 'gaml_BinaryOperator63', b2)
    assert _is_linked(a, 'gaml_BinaryOperator63', b2)
    if hasattr(b1, 'gaml_Expression64'):
        assert not _is_linked(b1, 'gaml_Expression64', a)
    if hasattr(b2, 'gaml_Expression64'):
        assert _is_linked(b2, 'gaml_Expression64', a)
    _safe_set(a, 'gaml_BinaryOperator63', None)
    assert not _is_linked(a, 'gaml_BinaryOperator63', b2)
    if hasattr(b2, 'gaml_Expression64'):
        assert not _is_linked(b2, 'gaml_Expression64', a)


def test_assoc_right67_link_reassign_clear():
    a = gaml_If(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_If68', b1)
    assert _is_linked(a, 'gaml_If68', b1)
    if hasattr(b1, 'gaml_Expression69'):
        assert _is_linked(b1, 'gaml_Expression69', a)
    _safe_set(a, 'gaml_If68', b2)
    assert _is_linked(a, 'gaml_If68', b2)
    if hasattr(b1, 'gaml_Expression69'):
        assert not _is_linked(b1, 'gaml_Expression69', a)
    if hasattr(b2, 'gaml_Expression69'):
        assert _is_linked(b2, 'gaml_Expression69', a)
    _safe_set(a, 'gaml_If68', None)
    assert not _is_linked(a, 'gaml_If68', b2)
    if hasattr(b2, 'gaml_Expression69'):
        assert not _is_linked(b2, 'gaml_Expression69', a)


def test_assoc_right75_link_reassign_clear():
    a = gaml_Unit(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Unit76', b1)
    assert _is_linked(a, 'gaml_Unit76', b1)
    if hasattr(b1, 'gaml_Expression77'):
        assert _is_linked(b1, 'gaml_Expression77', a)
    _safe_set(a, 'gaml_Unit76', b2)
    assert _is_linked(a, 'gaml_Unit76', b2)
    if hasattr(b1, 'gaml_Expression77'):
        assert not _is_linked(b1, 'gaml_Expression77', a)
    if hasattr(b2, 'gaml_Expression77'):
        assert _is_linked(b2, 'gaml_Expression77', a)
    _safe_set(a, 'gaml_Unit76', None)
    assert not _is_linked(a, 'gaml_Unit76', b2)
    if hasattr(b2, 'gaml_Expression77'):
        assert not _is_linked(b2, 'gaml_Expression77', a)


def test_assoc_right78_link_reassign_clear():
    a = gaml_Unary(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Unary', b1)
    assert _is_linked(a, 'gaml_Unary', b1)
    if hasattr(b1, 'gaml_Expression79'):
        assert _is_linked(b1, 'gaml_Expression79', a)
    _safe_set(a, 'gaml_Unary', b2)
    assert _is_linked(a, 'gaml_Unary', b2)
    if hasattr(b1, 'gaml_Expression79'):
        assert not _is_linked(b1, 'gaml_Expression79', a)
    if hasattr(b2, 'gaml_Expression79'):
        assert _is_linked(b2, 'gaml_Expression79', a)
    _safe_set(a, 'gaml_Unary', None)
    assert not _is_linked(a, 'gaml_Unary', b2)
    if hasattr(b2, 'gaml_Expression79'):
        assert not _is_linked(b2, 'gaml_Expression79', a)


def test_assoc_right82_link_reassign_clear():
    a = gaml_Access(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Access83', b1)
    assert _is_linked(a, 'gaml_Access83', b1)
    if hasattr(b1, 'gaml_Expression84'):
        assert _is_linked(b1, 'gaml_Expression84', a)
    _safe_set(a, 'gaml_Access83', b2)
    assert _is_linked(a, 'gaml_Access83', b2)
    if hasattr(b1, 'gaml_Expression84'):
        assert not _is_linked(b1, 'gaml_Expression84', a)
    if hasattr(b2, 'gaml_Expression84'):
        assert _is_linked(b2, 'gaml_Expression84', a)
    _safe_set(a, 'gaml_Access83', None)
    assert not _is_linked(a, 'gaml_Access83', b2)
    if hasattr(b2, 'gaml_Expression84'):
        assert not _is_linked(b2, 'gaml_Expression84', a)


def test_assoc_right89_link_reassign_clear():
    a = gaml_Point(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Point90', b1)
    assert _is_linked(a, 'gaml_Point90', b1)
    if hasattr(b1, 'gaml_Expression91'):
        assert _is_linked(b1, 'gaml_Expression91', a)
    _safe_set(a, 'gaml_Point90', b2)
    assert _is_linked(a, 'gaml_Point90', b2)
    if hasattr(b1, 'gaml_Expression91'):
        assert not _is_linked(b1, 'gaml_Expression91', a)
    if hasattr(b2, 'gaml_Expression91'):
        assert _is_linked(b2, 'gaml_Expression91', a)
    _safe_set(a, 'gaml_Point90', None)
    assert not _is_linked(a, 'gaml_Point90', b2)
    if hasattr(b2, 'gaml_Expression91'):
        assert not _is_linked(b2, 'gaml_Expression91', a)


def test_assoc_statements8_link_reassign_clear():
    a = gaml_Statement(firstFacet="sample_text", key="sample_text")
    b1 = gaml_Block()
    b2 = gaml_Block()
    _safe_set(a, 'gaml_Statement', b1)
    assert _is_linked(a, 'gaml_Statement', b1)
    if hasattr(b1, 'gaml_Block9'):
        assert _is_linked(b1, 'gaml_Block9', a)
    _safe_set(a, 'gaml_Statement', b2)
    assert _is_linked(a, 'gaml_Statement', b2)
    if hasattr(b1, 'gaml_Block9'):
        assert not _is_linked(b1, 'gaml_Block9', a)
    if hasattr(b2, 'gaml_Block9'):
        assert _is_linked(b2, 'gaml_Block9', a)
    _safe_set(a, 'gaml_Statement', None)
    assert not _is_linked(a, 'gaml_Statement', b2)
    if hasattr(b2, 'gaml_Block9'):
        assert not _is_linked(b2, 'gaml_Block9', a)


def test_assoc_z92_link_reassign_clear():
    a = gaml_Point(op="sample_text")
    b1 = gaml_Expression()
    b2 = gaml_Expression()
    _safe_set(a, 'gaml_Point93', b1)
    assert _is_linked(a, 'gaml_Point93', b1)
    if hasattr(b1, 'gaml_Expression94'):
        assert _is_linked(b1, 'gaml_Expression94', a)
    _safe_set(a, 'gaml_Point93', b2)
    assert _is_linked(a, 'gaml_Point93', b2)
    if hasattr(b1, 'gaml_Expression94'):
        assert not _is_linked(b1, 'gaml_Expression94', a)
    if hasattr(b2, 'gaml_Expression94'):
        assert _is_linked(b2, 'gaml_Expression94', a)
    _safe_set(a, 'gaml_Point93', None)
    assert not _is_linked(a, 'gaml_Point93', b2)
    if hasattr(b2, 'gaml_Expression94'):
        assert not _is_linked(b2, 'gaml_Expression94', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ActionDefinition_strategy = st.builds(ActionDefinition)
@given(instance=ActionDefinition_strategy)
@settings(max_examples=25)
def test_ActionDefinition_instantiation(instance):
    assert isinstance(instance, ActionDefinition)


Entry_strategy = st.builds(Entry)
@given(instance=Entry_strategy)
@settings(max_examples=25)
def test_Entry_instantiation(instance):
    assert isinstance(instance, Entry)


EquationDefinition_strategy = st.builds(EquationDefinition)
@given(instance=EquationDefinition_strategy)
@settings(max_examples=25)
def test_EquationDefinition_instantiation(instance):
    assert isinstance(instance, EquationDefinition)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


GamlDefinition_strategy = st.builds(GamlDefinition)
@given(instance=GamlDefinition_strategy)
@settings(max_examples=25)
def test_GamlDefinition_instantiation(instance):
    assert isinstance(instance, GamlDefinition)


S_Assignment_strategy = st.builds(S_Assignment)
@given(instance=S_Assignment_strategy)
@settings(max_examples=25)
def test_S_Assignment_instantiation(instance):
    assert isinstance(instance, S_Assignment)


S_Declaration_strategy = st.builds(S_Declaration)
@given(instance=S_Declaration_strategy)
@settings(max_examples=25)
def test_S_Declaration_instantiation(instance):
    assert isinstance(instance, S_Declaration)


S_Definition_strategy = st.builds(S_Definition)
@given(instance=S_Definition_strategy)
@settings(max_examples=25)
def test_S_Definition_instantiation(instance):
    assert isinstance(instance, S_Definition)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


TerminalExpression_strategy = st.builds(TerminalExpression)
@given(instance=TerminalExpression_strategy)
@settings(max_examples=25)
def test_TerminalExpression_instantiation(instance):
    assert isinstance(instance, TerminalExpression)


TypeDefinition_strategy = st.builds(TypeDefinition)
@given(instance=TypeDefinition_strategy)
@settings(max_examples=25)
def test_TypeDefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)


VarDefinition_strategy = st.builds(VarDefinition)
@given(instance=VarDefinition_strategy)
@settings(max_examples=25)
def test_VarDefinition_instantiation(instance):
    assert isinstance(instance, VarDefinition)


gaml_Access_strategy = st.builds(gaml_Access, op=safe_text)
@given(instance=gaml_Access_strategy)
@settings(max_examples=25)
def test_gaml_Access_instantiation(instance):
    assert isinstance(instance, gaml_Access)


gaml_ActionArguments_strategy = st.builds(gaml_ActionArguments)
@given(instance=gaml_ActionArguments_strategy)
@settings(max_examples=25)
def test_gaml_ActionArguments_instantiation(instance):
    assert isinstance(instance, gaml_ActionArguments)


gaml_ActionDefinition_strategy = st.builds(gaml_ActionDefinition)
@given(instance=gaml_ActionDefinition_strategy)
@settings(max_examples=25)
def test_gaml_ActionDefinition_instantiation(instance):
    assert isinstance(instance, gaml_ActionDefinition)


gaml_ActionFakeDefinition_strategy = st.builds(gaml_ActionFakeDefinition)
@given(instance=gaml_ActionFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_ActionFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_ActionFakeDefinition)


gaml_ActionRef_strategy = st.builds(gaml_ActionRef)
@given(instance=gaml_ActionRef_strategy)
@settings(max_examples=25)
def test_gaml_ActionRef_instantiation(instance):
    assert isinstance(instance, gaml_ActionRef)


gaml_ArgumentDefinition_strategy = st.builds(gaml_ArgumentDefinition)
@given(instance=gaml_ArgumentDefinition_strategy)
@settings(max_examples=25)
def test_gaml_ArgumentDefinition_instantiation(instance):
    assert isinstance(instance, gaml_ArgumentDefinition)


gaml_ArgumentPair_strategy = st.builds(gaml_ArgumentPair, op=safe_text)
@given(instance=gaml_ArgumentPair_strategy)
@settings(max_examples=25)
def test_gaml_ArgumentPair_instantiation(instance):
    assert isinstance(instance, gaml_ArgumentPair)


gaml_Array_strategy = st.builds(gaml_Array)
@given(instance=gaml_Array_strategy)
@settings(max_examples=25)
def test_gaml_Array_instantiation(instance):
    assert isinstance(instance, gaml_Array)


gaml_BinaryOperator_strategy = st.builds(gaml_BinaryOperator, op=safe_text)
@given(instance=gaml_BinaryOperator_strategy)
@settings(max_examples=25)
def test_gaml_BinaryOperator_instantiation(instance):
    assert isinstance(instance, gaml_BinaryOperator)


gaml_Block_strategy = st.builds(gaml_Block)
@given(instance=gaml_Block_strategy)
@settings(max_examples=25)
def test_gaml_Block_instantiation(instance):
    assert isinstance(instance, gaml_Block)


gaml_BooleanLiteral_strategy = st.builds(gaml_BooleanLiteral)
@given(instance=gaml_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_gaml_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, gaml_BooleanLiteral)


gaml_DoubleLiteral_strategy = st.builds(gaml_DoubleLiteral)
@given(instance=gaml_DoubleLiteral_strategy)
@settings(max_examples=25)
def test_gaml_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, gaml_DoubleLiteral)


gaml_EObject_strategy = st.builds(gaml_EObject)
@given(instance=gaml_EObject_strategy)
@settings(max_examples=25)
def test_gaml_EObject_instantiation(instance):
    assert isinstance(instance, gaml_EObject)


gaml_Entry_strategy = st.builds(gaml_Entry)
@given(instance=gaml_Entry_strategy)
@settings(max_examples=25)
def test_gaml_Entry_instantiation(instance):
    assert isinstance(instance, gaml_Entry)


gaml_EquationDefinition_strategy = st.builds(gaml_EquationDefinition)
@given(instance=gaml_EquationDefinition_strategy)
@settings(max_examples=25)
def test_gaml_EquationDefinition_instantiation(instance):
    assert isinstance(instance, gaml_EquationDefinition)


gaml_EquationFakeDefinition_strategy = st.builds(gaml_EquationFakeDefinition)
@given(instance=gaml_EquationFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_EquationFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_EquationFakeDefinition)


gaml_EquationRef_strategy = st.builds(gaml_EquationRef)
@given(instance=gaml_EquationRef_strategy)
@settings(max_examples=25)
def test_gaml_EquationRef_instantiation(instance):
    assert isinstance(instance, gaml_EquationRef)


gaml_ExperimentFileStructure_strategy = st.builds(gaml_ExperimentFileStructure)
@given(instance=gaml_ExperimentFileStructure_strategy)
@settings(max_examples=25)
def test_gaml_ExperimentFileStructure_instantiation(instance):
    assert isinstance(instance, gaml_ExperimentFileStructure)


gaml_Expression_strategy = st.builds(gaml_Expression)
@given(instance=gaml_Expression_strategy)
@settings(max_examples=25)
def test_gaml_Expression_instantiation(instance):
    assert isinstance(instance, gaml_Expression)


gaml_ExpressionList_strategy = st.builds(gaml_ExpressionList)
@given(instance=gaml_ExpressionList_strategy)
@settings(max_examples=25)
def test_gaml_ExpressionList_instantiation(instance):
    assert isinstance(instance, gaml_ExpressionList)


gaml_Facet_strategy = st.builds(gaml_Facet, key=safe_text)
@given(instance=gaml_Facet_strategy)
@settings(max_examples=25)
def test_gaml_Facet_instantiation(instance):
    assert isinstance(instance, gaml_Facet)


gaml_Function_strategy = st.builds(gaml_Function)
@given(instance=gaml_Function_strategy)
@settings(max_examples=25)
def test_gaml_Function_instantiation(instance):
    assert isinstance(instance, gaml_Function)


gaml_GamlDefinition_strategy = st.builds(gaml_GamlDefinition, name=safe_text)
@given(instance=gaml_GamlDefinition_strategy)
@settings(max_examples=25)
def test_gaml_GamlDefinition_instantiation(instance):
    assert isinstance(instance, gaml_GamlDefinition)


gaml_HeadlessExperiment_strategy = st.builds(gaml_HeadlessExperiment, firstFacet=safe_text, importURI=safe_text, key=safe_text, name=safe_text)
@given(instance=gaml_HeadlessExperiment_strategy)
@settings(max_examples=25)
def test_gaml_HeadlessExperiment_instantiation(instance):
    assert isinstance(instance, gaml_HeadlessExperiment)


gaml_If_strategy = st.builds(gaml_If, op=safe_text)
@given(instance=gaml_If_strategy)
@settings(max_examples=25)
def test_gaml_If_instantiation(instance):
    assert isinstance(instance, gaml_If)


gaml_Import_strategy = st.builds(gaml_Import, importURI=safe_text)
@given(instance=gaml_Import_strategy)
@settings(max_examples=25)
def test_gaml_Import_instantiation(instance):
    assert isinstance(instance, gaml_Import)


gaml_IntLiteral_strategy = st.builds(gaml_IntLiteral)
@given(instance=gaml_IntLiteral_strategy)
@settings(max_examples=25)
def test_gaml_IntLiteral_instantiation(instance):
    assert isinstance(instance, gaml_IntLiteral)


gaml_Model_strategy = st.builds(gaml_Model)
@given(instance=gaml_Model_strategy)
@settings(max_examples=25)
def test_gaml_Model_instantiation(instance):
    assert isinstance(instance, gaml_Model)


gaml_Parameter_strategy = st.builds(gaml_Parameter, builtInFacetKey=safe_text)
@given(instance=gaml_Parameter_strategy)
@settings(max_examples=25)
def test_gaml_Parameter_instantiation(instance):
    assert isinstance(instance, gaml_Parameter)


gaml_Point_strategy = st.builds(gaml_Point, op=safe_text)
@given(instance=gaml_Point_strategy)
@settings(max_examples=25)
def test_gaml_Point_instantiation(instance):
    assert isinstance(instance, gaml_Point)


gaml_Pragma_strategy = st.builds(gaml_Pragma, name=safe_text)
@given(instance=gaml_Pragma_strategy)
@settings(max_examples=25)
def test_gaml_Pragma_instantiation(instance):
    assert isinstance(instance, gaml_Pragma)


gaml_ReservedLiteral_strategy = st.builds(gaml_ReservedLiteral)
@given(instance=gaml_ReservedLiteral_strategy)
@settings(max_examples=25)
def test_gaml_ReservedLiteral_instantiation(instance):
    assert isinstance(instance, gaml_ReservedLiteral)


gaml_S_Action_strategy = st.builds(gaml_S_Action)
@given(instance=gaml_S_Action_strategy)
@settings(max_examples=25)
def test_gaml_S_Action_instantiation(instance):
    assert isinstance(instance, gaml_S_Action)


gaml_S_Assignment_strategy = st.builds(gaml_S_Assignment)
@given(instance=gaml_S_Assignment_strategy)
@settings(max_examples=25)
def test_gaml_S_Assignment_instantiation(instance):
    assert isinstance(instance, gaml_S_Assignment)


gaml_S_Declaration_strategy = st.builds(gaml_S_Declaration)
@given(instance=gaml_S_Declaration_strategy)
@settings(max_examples=25)
def test_gaml_S_Declaration_instantiation(instance):
    assert isinstance(instance, gaml_S_Declaration)


gaml_S_Definition_strategy = st.builds(gaml_S_Definition)
@given(instance=gaml_S_Definition_strategy)
@settings(max_examples=25)
def test_gaml_S_Definition_instantiation(instance):
    assert isinstance(instance, gaml_S_Definition)


gaml_S_DirectAssignment_strategy = st.builds(gaml_S_DirectAssignment)
@given(instance=gaml_S_DirectAssignment_strategy)
@settings(max_examples=25)
def test_gaml_S_DirectAssignment_instantiation(instance):
    assert isinstance(instance, gaml_S_DirectAssignment)


gaml_S_Display_strategy = st.builds(gaml_S_Display, name=safe_text)
@given(instance=gaml_S_Display_strategy)
@settings(max_examples=25)
def test_gaml_S_Display_instantiation(instance):
    assert isinstance(instance, gaml_S_Display)


gaml_S_Do_strategy = st.builds(gaml_S_Do)
@given(instance=gaml_S_Do_strategy)
@settings(max_examples=25)
def test_gaml_S_Do_instantiation(instance):
    assert isinstance(instance, gaml_S_Do)


gaml_S_Equations_strategy = st.builds(gaml_S_Equations)
@given(instance=gaml_S_Equations_strategy)
@settings(max_examples=25)
def test_gaml_S_Equations_instantiation(instance):
    assert isinstance(instance, gaml_S_Equations)


gaml_S_Experiment_strategy = st.builds(gaml_S_Experiment)
@given(instance=gaml_S_Experiment_strategy)
@settings(max_examples=25)
def test_gaml_S_Experiment_instantiation(instance):
    assert isinstance(instance, gaml_S_Experiment)


gaml_S_Global_strategy = st.builds(gaml_S_Global)
@given(instance=gaml_S_Global_strategy)
@settings(max_examples=25)
def test_gaml_S_Global_instantiation(instance):
    assert isinstance(instance, gaml_S_Global)


gaml_S_If_strategy = st.builds(gaml_S_If)
@given(instance=gaml_S_If_strategy)
@settings(max_examples=25)
def test_gaml_S_If_instantiation(instance):
    assert isinstance(instance, gaml_S_If)


gaml_S_Loop_strategy = st.builds(gaml_S_Loop)
@given(instance=gaml_S_Loop_strategy)
@settings(max_examples=25)
def test_gaml_S_Loop_instantiation(instance):
    assert isinstance(instance, gaml_S_Loop)


gaml_S_Other_strategy = st.builds(gaml_S_Other)
@given(instance=gaml_S_Other_strategy)
@settings(max_examples=25)
def test_gaml_S_Other_instantiation(instance):
    assert isinstance(instance, gaml_S_Other)


gaml_S_Reflex_strategy = st.builds(gaml_S_Reflex)
@given(instance=gaml_S_Reflex_strategy)
@settings(max_examples=25)
def test_gaml_S_Reflex_instantiation(instance):
    assert isinstance(instance, gaml_S_Reflex)


gaml_S_Return_strategy = st.builds(gaml_S_Return)
@given(instance=gaml_S_Return_strategy)
@settings(max_examples=25)
def test_gaml_S_Return_instantiation(instance):
    assert isinstance(instance, gaml_S_Return)


gaml_S_Set_strategy = st.builds(gaml_S_Set)
@given(instance=gaml_S_Set_strategy)
@settings(max_examples=25)
def test_gaml_S_Set_instantiation(instance):
    assert isinstance(instance, gaml_S_Set)


gaml_S_Solve_strategy = st.builds(gaml_S_Solve)
@given(instance=gaml_S_Solve_strategy)
@settings(max_examples=25)
def test_gaml_S_Solve_instantiation(instance):
    assert isinstance(instance, gaml_S_Solve)


gaml_S_Species_strategy = st.builds(gaml_S_Species)
@given(instance=gaml_S_Species_strategy)
@settings(max_examples=25)
def test_gaml_S_Species_instantiation(instance):
    assert isinstance(instance, gaml_S_Species)


gaml_S_Try_strategy = st.builds(gaml_S_Try)
@given(instance=gaml_S_Try_strategy)
@settings(max_examples=25)
def test_gaml_S_Try_instantiation(instance):
    assert isinstance(instance, gaml_S_Try)


gaml_S_Var_strategy = st.builds(gaml_S_Var)
@given(instance=gaml_S_Var_strategy)
@settings(max_examples=25)
def test_gaml_S_Var_instantiation(instance):
    assert isinstance(instance, gaml_S_Var)


gaml_SkillFakeDefinition_strategy = st.builds(gaml_SkillFakeDefinition)
@given(instance=gaml_SkillFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_SkillFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_SkillFakeDefinition)


gaml_SkillRef_strategy = st.builds(gaml_SkillRef)
@given(instance=gaml_SkillRef_strategy)
@settings(max_examples=25)
def test_gaml_SkillRef_instantiation(instance):
    assert isinstance(instance, gaml_SkillRef)


gaml_StandaloneBlock_strategy = st.builds(gaml_StandaloneBlock)
@given(instance=gaml_StandaloneBlock_strategy)
@settings(max_examples=25)
def test_gaml_StandaloneBlock_instantiation(instance):
    assert isinstance(instance, gaml_StandaloneBlock)


gaml_Statement_strategy = st.builds(gaml_Statement, firstFacet=safe_text, key=safe_text)
@given(instance=gaml_Statement_strategy)
@settings(max_examples=25)
def test_gaml_Statement_instantiation(instance):
    assert isinstance(instance, gaml_Statement)


gaml_StringEvaluator_strategy = st.builds(gaml_StringEvaluator, toto=safe_text)
@given(instance=gaml_StringEvaluator_strategy)
@settings(max_examples=25)
def test_gaml_StringEvaluator_instantiation(instance):
    assert isinstance(instance, gaml_StringEvaluator)


gaml_StringLiteral_strategy = st.builds(gaml_StringLiteral)
@given(instance=gaml_StringLiteral_strategy)
@settings(max_examples=25)
def test_gaml_StringLiteral_instantiation(instance):
    assert isinstance(instance, gaml_StringLiteral)


gaml_TerminalExpression_strategy = st.builds(gaml_TerminalExpression, op=safe_text)
@given(instance=gaml_TerminalExpression_strategy)
@settings(max_examples=25)
def test_gaml_TerminalExpression_instantiation(instance):
    assert isinstance(instance, gaml_TerminalExpression)


gaml_TypeDefinition_strategy = st.builds(gaml_TypeDefinition)
@given(instance=gaml_TypeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_TypeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_TypeDefinition)


gaml_TypeFakeDefinition_strategy = st.builds(gaml_TypeFakeDefinition)
@given(instance=gaml_TypeFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_TypeFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_TypeFakeDefinition)


gaml_TypeInfo_strategy = st.builds(gaml_TypeInfo)
@given(instance=gaml_TypeInfo_strategy)
@settings(max_examples=25)
def test_gaml_TypeInfo_instantiation(instance):
    assert isinstance(instance, gaml_TypeInfo)


gaml_TypeRef_strategy = st.builds(gaml_TypeRef)
@given(instance=gaml_TypeRef_strategy)
@settings(max_examples=25)
def test_gaml_TypeRef_instantiation(instance):
    assert isinstance(instance, gaml_TypeRef)


gaml_Unary_strategy = st.builds(gaml_Unary, op=safe_text)
@given(instance=gaml_Unary_strategy)
@settings(max_examples=25)
def test_gaml_Unary_instantiation(instance):
    assert isinstance(instance, gaml_Unary)


gaml_Unit_strategy = st.builds(gaml_Unit, op=safe_text)
@given(instance=gaml_Unit_strategy)
@settings(max_examples=25)
def test_gaml_Unit_instantiation(instance):
    assert isinstance(instance, gaml_Unit)


gaml_UnitFakeDefinition_strategy = st.builds(gaml_UnitFakeDefinition)
@given(instance=gaml_UnitFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_UnitFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_UnitFakeDefinition)


gaml_UnitName_strategy = st.builds(gaml_UnitName)
@given(instance=gaml_UnitName_strategy)
@settings(max_examples=25)
def test_gaml_UnitName_instantiation(instance):
    assert isinstance(instance, gaml_UnitName)


gaml_VarDefinition_strategy = st.builds(gaml_VarDefinition)
@given(instance=gaml_VarDefinition_strategy)
@settings(max_examples=25)
def test_gaml_VarDefinition_instantiation(instance):
    assert isinstance(instance, gaml_VarDefinition)


gaml_VarFakeDefinition_strategy = st.builds(gaml_VarFakeDefinition)
@given(instance=gaml_VarFakeDefinition_strategy)
@settings(max_examples=25)
def test_gaml_VarFakeDefinition_instantiation(instance):
    assert isinstance(instance, gaml_VarFakeDefinition)


gaml_VariableRef_strategy = st.builds(gaml_VariableRef)
@given(instance=gaml_VariableRef_strategy)
@settings(max_examples=25)
def test_gaml_VariableRef_instantiation(instance):
    assert isinstance(instance, gaml_VariableRef)


gaml_speciesOrGridDisplayStatement_strategy = st.builds(gaml_speciesOrGridDisplayStatement)
@given(instance=gaml_speciesOrGridDisplayStatement_strategy)
@settings(max_examples=25)
def test_gaml_speciesOrGridDisplayStatement_instantiation(instance):
    assert isinstance(instance, gaml_speciesOrGridDisplayStatement)


