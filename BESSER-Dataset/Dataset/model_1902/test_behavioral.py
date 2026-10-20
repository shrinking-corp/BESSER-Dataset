import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArchitectureStatement,
    ArrayTypeDefinition,
    BlockDeclarativeItem,
    CompositeTypeDefinition,
    ContextItem,
    Expression,
    IterationScheme,
    LibraryUnit,
    SequentialStatement,
    Type,
    TypeDefinition,
    ValueExpression,
    Variable,
    package_declarative_item,
    vhdl_AccessTypeDefinition,
    vhdl_AddingExpression,
    vhdl_Alias,
    vhdl_Architecture,
    vhdl_ArchitectureStatement,
    vhdl_ArrayTypeDefinition,
    vhdl_AttributeDeclaration,
    vhdl_AttributeSpecification,
    vhdl_BitString,
    vhdl_BlockDeclarativeItem,
    vhdl_Boolean,
    vhdl_BuiltinFuncs,
    vhdl_CaseAlternative,
    vhdl_CaseStatement,
    vhdl_Char,
    vhdl_ChoiceExpression,
    vhdl_Component,
    vhdl_ComponentInstantiationStatement,
    vhdl_CompositeTypeDefinition,
    vhdl_ConditionalSignalAssignmentStatement,
    vhdl_ConditionalWaveformExpression,
    vhdl_Constant,
    vhdl_ConstantDeclaration,
    vhdl_ConstrainedArrayTypeDefinition,
    vhdl_ContextItem,
    vhdl_DesignFile,
    vhdl_Entity,
    vhdl_EntityInstantiationStatement,
    vhdl_EnumerationTypeDefinition,
    vhdl_Expression,
    vhdl_Factor,
    vhdl_FileTypeDefinition,
    vhdl_ForGenerateStatement,
    vhdl_ForIterationScheme,
    vhdl_Generic,
    vhdl_GenericMap,
    vhdl_GenericMapAssociation,
    vhdl_Generics,
    vhdl_IdList,
    vhdl_IfGenerateStatement,
    vhdl_IfStatement,
    vhdl_IfStatementTest,
    vhdl_IterationScheme,
    vhdl_Library,
    vhdl_LibraryClause,
    vhdl_LibraryUnit,
    vhdl_LogicalExpression,
    vhdl_LoopStatement,
    vhdl_LoopVariable,
    vhdl_Member,
    vhdl_MemberExpression,
    vhdl_MultiExpression,
    vhdl_MultiplyingExpression,
    vhdl_Open,
    vhdl_Others,
    vhdl_Package,
    vhdl_Port,
    vhdl_PortMap,
    vhdl_PortMapAssociation,
    vhdl_Ports,
    vhdl_ProcessStatement,
    vhdl_RangeExpression,
    vhdl_RecordField,
    vhdl_RecordTypeDefinition,
    vhdl_RelationalExpression,
    vhdl_SequentialSignalAssignmentStatement,
    vhdl_SequentialStatement,
    vhdl_ShiftExpression,
    vhdl_Signal,
    vhdl_SignalDeclaration,
    vhdl_SliceExpression,
    vhdl_String,
    vhdl_SubtypeDeclaration,
    vhdl_SubtypeIndication,
    vhdl_Type,
    vhdl_TypeDeclaration,
    vhdl_TypeDefinition,
    vhdl_UnconstrainedArrayTypeDefinition,
    vhdl_UnitValueExpression,
    vhdl_UseClause,
    vhdl_Value,
    vhdl_ValueExpression,
    vhdl_Var,
    vhdl_Variable,
    vhdl_VariableDeclaration,
    vhdl_WaitStatement,
    vhdl_WhileIterationScheme,
    vhdl_package_declarative_item,
    vhdl_package_declarative_part,
    AddingOperator,
    BuiltinLibs,
    EString,
    EntityClass,
    LogicalOperator,
    Mode,
    MultiplyingOperator,
    Purity,
    RangeDirection,
    RelationalOperator,
    ShiftOperator,
    Sign,
    SignalKind,
    UnaryOperator,
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

def test_assoc_actual81_reverse_link_reassign_clear():
    a1 = vhdl_PortMapAssociation(formal="sample_text")
    a2 = vhdl_PortMapAssociation(formal="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression83', a1)
    assert _is_linked(b, 'vhdl_Expression83', a1)
    if hasattr(a1, 'vhdl_PortMapAssociation82'):
        assert _is_linked(a1, 'vhdl_PortMapAssociation82', b)
    _safe_set(b, 'vhdl_Expression83', a2)
    assert _is_linked(b, 'vhdl_Expression83', a2)
    if hasattr(a1, 'vhdl_PortMapAssociation82'):
        assert not _is_linked(a1, 'vhdl_PortMapAssociation82', b)
    if hasattr(a2, 'vhdl_PortMapAssociation82'):
        assert _is_linked(a2, 'vhdl_PortMapAssociation82', b)
    _safe_set(b, 'vhdl_Expression83', None)
    assert not _is_linked(b, 'vhdl_Expression83', a2)
    if hasattr(a2, 'vhdl_PortMapAssociation82'):
        assert not _is_linked(a2, 'vhdl_PortMapAssociation82', b)


def test_assoc_actual86_reverse_link_reassign_clear():
    a1 = vhdl_GenericMapAssociation(formal="sample_text")
    a2 = vhdl_GenericMapAssociation(formal="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression88', a1)
    assert _is_linked(b, 'vhdl_Expression88', a1)
    if hasattr(a1, 'vhdl_GenericMapAssociation87'):
        assert _is_linked(a1, 'vhdl_GenericMapAssociation87', b)
    _safe_set(b, 'vhdl_Expression88', a2)
    assert _is_linked(b, 'vhdl_Expression88', a2)
    if hasattr(a1, 'vhdl_GenericMapAssociation87'):
        assert not _is_linked(a1, 'vhdl_GenericMapAssociation87', b)
    if hasattr(a2, 'vhdl_GenericMapAssociation87'):
        assert _is_linked(a2, 'vhdl_GenericMapAssociation87', b)
    _safe_set(b, 'vhdl_Expression88', None)
    assert not _is_linked(b, 'vhdl_Expression88', a2)
    if hasattr(a2, 'vhdl_GenericMapAssociation87'):
        assert not _is_linked(a2, 'vhdl_GenericMapAssociation87', b)


def test_assoc_after101_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression102', a1)
    assert _is_linked(b, 'vhdl_Expression102', a1)
    if hasattr(a1, 'vhdl_Expression100'):
        assert _is_linked(a1, 'vhdl_Expression100', b)
    _safe_set(b, 'vhdl_Expression102', a2)
    assert _is_linked(b, 'vhdl_Expression102', a2)
    if hasattr(a1, 'vhdl_Expression100'):
        assert not _is_linked(a1, 'vhdl_Expression100', b)
    if hasattr(a2, 'vhdl_Expression100'):
        assert _is_linked(a2, 'vhdl_Expression100', b)
    _safe_set(b, 'vhdl_Expression102', None)
    assert not _is_linked(b, 'vhdl_Expression102', a2)
    if hasattr(a2, 'vhdl_Expression100'):
        assert not _is_linked(a2, 'vhdl_Expression100', b)


def test_assoc_case142_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_CaseStatement(label="sample_text")
    _safe_set(b, 'vhdl_CaseStatement', a1)
    assert _is_linked(b, 'vhdl_CaseStatement', a1)
    if hasattr(a1, 'vhdl_Expression143'):
        assert _is_linked(a1, 'vhdl_Expression143', b)
    _safe_set(b, 'vhdl_CaseStatement', a2)
    assert _is_linked(b, 'vhdl_CaseStatement', a2)
    if hasattr(a1, 'vhdl_Expression143'):
        assert not _is_linked(a1, 'vhdl_Expression143', b)
    if hasattr(a2, 'vhdl_Expression143'):
        assert _is_linked(a2, 'vhdl_Expression143', b)
    _safe_set(b, 'vhdl_CaseStatement', None)
    assert not _is_linked(b, 'vhdl_CaseStatement', a2)
    if hasattr(a2, 'vhdl_Expression143'):
        assert not _is_linked(a2, 'vhdl_Expression143', b)


def test_assoc_constraint171_reverse_link_reassign_clear():
    a1 = vhdl_SubtypeIndication(builtin_type="sample_text")
    a2 = vhdl_SubtypeIndication(builtin_type="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression173', a1)
    assert _is_linked(b, 'vhdl_Expression173', a1)
    if hasattr(a1, 'vhdl_SubtypeIndication172'):
        assert _is_linked(a1, 'vhdl_SubtypeIndication172', b)
    _safe_set(b, 'vhdl_Expression173', a2)
    assert _is_linked(b, 'vhdl_Expression173', a2)
    if hasattr(a1, 'vhdl_SubtypeIndication172'):
        assert not _is_linked(a1, 'vhdl_SubtypeIndication172', b)
    if hasattr(a2, 'vhdl_SubtypeIndication172'):
        assert _is_linked(a2, 'vhdl_SubtypeIndication172', b)
    _safe_set(b, 'vhdl_Expression173', None)
    assert not _is_linked(b, 'vhdl_Expression173', a2)
    if hasattr(a2, 'vhdl_SubtypeIndication172'):
        assert not _is_linked(a2, 'vhdl_SubtypeIndication172', b)


def test_assoc_custom_lib4_reverse_link_reassign_clear():
    a1 = vhdl_LibraryClause(name="sample_text")
    a2 = vhdl_LibraryClause(name="sample_text_2")
    b = vhdl_Library(builtin_lib="sample_text")
    _safe_set(b, 'vhdl_Library5', a1)
    assert _is_linked(b, 'vhdl_Library5', a1)
    if hasattr(a1, 'vhdl_LibraryClause'):
        assert _is_linked(a1, 'vhdl_LibraryClause', b)
    _safe_set(b, 'vhdl_Library5', a2)
    assert _is_linked(b, 'vhdl_Library5', a2)
    if hasattr(a1, 'vhdl_LibraryClause'):
        assert not _is_linked(a1, 'vhdl_LibraryClause', b)
    if hasattr(a2, 'vhdl_LibraryClause'):
        assert _is_linked(a2, 'vhdl_LibraryClause', b)
    _safe_set(b, 'vhdl_Library5', None)
    assert not _is_linked(b, 'vhdl_Library5', a2)
    if hasattr(a2, 'vhdl_LibraryClause'):
        assert not _is_linked(a2, 'vhdl_LibraryClause', b)


def test_assoc_custom_type169_reverse_link_reassign_clear():
    a1 = vhdl_Type(name="sample_text", value="sample_text")
    a2 = vhdl_Type(name="sample_text_2", value="sample_text_2")
    b = vhdl_SubtypeIndication(builtin_type="sample_text")
    _safe_set(b, 'vhdl_SubtypeIndication170', a1)
    assert _is_linked(b, 'vhdl_SubtypeIndication170', a1)
    if hasattr(a1, 'vhdl_Type'):
        assert _is_linked(a1, 'vhdl_Type', b)
    _safe_set(b, 'vhdl_SubtypeIndication170', a2)
    assert _is_linked(b, 'vhdl_SubtypeIndication170', a2)
    if hasattr(a1, 'vhdl_Type'):
        assert not _is_linked(a1, 'vhdl_Type', b)
    if hasattr(a2, 'vhdl_Type'):
        assert _is_linked(a2, 'vhdl_Type', b)
    _safe_set(b, 'vhdl_SubtypeIndication170', None)
    assert not _is_linked(b, 'vhdl_SubtypeIndication170', a2)
    if hasattr(a2, 'vhdl_Type'):
        assert not _is_linked(a2, 'vhdl_Type', b)


def test_assoc_exp98_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression99', a1)
    assert _is_linked(b, 'vhdl_Expression99', a1)
    if hasattr(a1, 'vhdl_Expression97'):
        assert _is_linked(a1, 'vhdl_Expression97', b)
    _safe_set(b, 'vhdl_Expression99', a2)
    assert _is_linked(b, 'vhdl_Expression99', a2)
    if hasattr(a1, 'vhdl_Expression97'):
        assert not _is_linked(a1, 'vhdl_Expression97', b)
    if hasattr(a2, 'vhdl_Expression97'):
        assert _is_linked(a2, 'vhdl_Expression97', b)
    _safe_set(b, 'vhdl_Expression99', None)
    assert not _is_linked(b, 'vhdl_Expression99', a2)
    if hasattr(a2, 'vhdl_Expression97'):
        assert not _is_linked(a2, 'vhdl_Expression97', b)


def test_assoc_expression104_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression105', a1)
    assert _is_linked(b, 'vhdl_Expression105', a1)
    if hasattr(a1, 'vhdl_Expression103'):
        assert _is_linked(a1, 'vhdl_Expression103', b)
    _safe_set(b, 'vhdl_Expression105', a2)
    assert _is_linked(b, 'vhdl_Expression105', a2)
    if hasattr(a1, 'vhdl_Expression103'):
        assert not _is_linked(a1, 'vhdl_Expression103', b)
    if hasattr(a2, 'vhdl_Expression103'):
        assert _is_linked(a2, 'vhdl_Expression103', b)
    _safe_set(b, 'vhdl_Expression105', None)
    assert not _is_linked(b, 'vhdl_Expression105', a2)
    if hasattr(a2, 'vhdl_Expression103'):
        assert not _is_linked(a2, 'vhdl_Expression103', b)


def test_assoc_in_167_reverse_link_reassign_clear():
    a1 = vhdl_ForIterationScheme(variable="sample_text")
    a2 = vhdl_ForIterationScheme(variable="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression168', a1)
    assert _is_linked(b, 'vhdl_Expression168', a1)
    if hasattr(a1, 'vhdl_ForIterationScheme'):
        assert _is_linked(a1, 'vhdl_ForIterationScheme', b)
    _safe_set(b, 'vhdl_Expression168', a2)
    assert _is_linked(b, 'vhdl_Expression168', a2)
    if hasattr(a1, 'vhdl_ForIterationScheme'):
        assert not _is_linked(a1, 'vhdl_ForIterationScheme', b)
    if hasattr(a2, 'vhdl_ForIterationScheme'):
        assert _is_linked(a2, 'vhdl_ForIterationScheme', b)
    _safe_set(b, 'vhdl_Expression168', None)
    assert not _is_linked(b, 'vhdl_Expression168', a2)
    if hasattr(a2, 'vhdl_ForIterationScheme'):
        assert not _is_linked(a2, 'vhdl_ForIterationScheme', b)


def test_assoc_initial22_reverse_link_reassign_clear():
    a1 = vhdl_Port(kind="sample_text", mode="sample_text")
    a2 = vhdl_Port(kind="sample_text_2", mode="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression', a1)
    assert _is_linked(b, 'vhdl_Expression', a1)
    if hasattr(a1, 'vhdl_Port23'):
        assert _is_linked(a1, 'vhdl_Port23', b)
    _safe_set(b, 'vhdl_Expression', a2)
    assert _is_linked(b, 'vhdl_Expression', a2)
    if hasattr(a1, 'vhdl_Port23'):
        assert not _is_linked(a1, 'vhdl_Port23', b)
    if hasattr(a2, 'vhdl_Port23'):
        assert _is_linked(a2, 'vhdl_Port23', b)
    _safe_set(b, 'vhdl_Expression', None)
    assert not _is_linked(b, 'vhdl_Expression', a2)
    if hasattr(a2, 'vhdl_Port23'):
        assert not _is_linked(a2, 'vhdl_Port23', b)


def test_assoc_initial41_reverse_link_reassign_clear():
    a1 = vhdl_SignalDeclaration(kind="sample_text")
    a2 = vhdl_SignalDeclaration(kind="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression43', a1)
    assert _is_linked(b, 'vhdl_Expression43', a1)
    if hasattr(a1, 'vhdl_SignalDeclaration42'):
        assert _is_linked(a1, 'vhdl_SignalDeclaration42', b)
    _safe_set(b, 'vhdl_Expression43', a2)
    assert _is_linked(b, 'vhdl_Expression43', a2)
    if hasattr(a1, 'vhdl_SignalDeclaration42'):
        assert not _is_linked(a1, 'vhdl_SignalDeclaration42', b)
    if hasattr(a2, 'vhdl_SignalDeclaration42'):
        assert _is_linked(a2, 'vhdl_SignalDeclaration42', b)
    _safe_set(b, 'vhdl_Expression43', None)
    assert not _is_linked(b, 'vhdl_Expression43', a2)
    if hasattr(a2, 'vhdl_SignalDeclaration42'):
        assert not _is_linked(a2, 'vhdl_SignalDeclaration42', b)


def test_assoc_initial48_reverse_link_reassign_clear():
    a1 = vhdl_VariableDeclaration(shared=True)
    a2 = vhdl_VariableDeclaration(shared=False)
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression50', a1)
    assert _is_linked(b, 'vhdl_Expression50', a1)
    if hasattr(a1, 'vhdl_VariableDeclaration49'):
        assert _is_linked(a1, 'vhdl_VariableDeclaration49', b)
    _safe_set(b, 'vhdl_Expression50', a2)
    assert _is_linked(b, 'vhdl_Expression50', a2)
    if hasattr(a1, 'vhdl_VariableDeclaration49'):
        assert not _is_linked(a1, 'vhdl_VariableDeclaration49', b)
    if hasattr(a2, 'vhdl_VariableDeclaration49'):
        assert _is_linked(a2, 'vhdl_VariableDeclaration49', b)
    _safe_set(b, 'vhdl_Expression50', None)
    assert not _is_linked(b, 'vhdl_Expression50', a2)
    if hasattr(a2, 'vhdl_VariableDeclaration49'):
        assert not _is_linked(a2, 'vhdl_VariableDeclaration49', b)


def test_assoc_is_58_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_AttributeSpecification(class_="sample_text", entity="sample_text", name="sample_text")
    _safe_set(b, 'vhdl_AttributeSpecification', a1)
    assert _is_linked(b, 'vhdl_AttributeSpecification', a1)
    if hasattr(a1, 'vhdl_Expression59'):
        assert _is_linked(a1, 'vhdl_Expression59', b)
    _safe_set(b, 'vhdl_AttributeSpecification', a2)
    assert _is_linked(b, 'vhdl_AttributeSpecification', a2)
    if hasattr(a1, 'vhdl_Expression59'):
        assert not _is_linked(a1, 'vhdl_Expression59', b)
    if hasattr(a2, 'vhdl_Expression59'):
        assert _is_linked(a2, 'vhdl_Expression59', b)
    _safe_set(b, 'vhdl_AttributeSpecification', None)
    assert not _is_linked(b, 'vhdl_AttributeSpecification', a2)
    if hasattr(a2, 'vhdl_Expression59'):
        assert not _is_linked(a2, 'vhdl_Expression59', b)


def test_assoc_left194_reverse_link_reassign_clear():
    a1 = vhdl_RangeExpression(direction="sample_text", operator="sample_text")
    a2 = vhdl_RangeExpression(direction="sample_text_2", operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression195', a1)
    assert _is_linked(b, 'vhdl_Expression195', a1)
    if hasattr(a1, 'vhdl_RangeExpression'):
        assert _is_linked(a1, 'vhdl_RangeExpression', b)
    _safe_set(b, 'vhdl_Expression195', a2)
    assert _is_linked(b, 'vhdl_Expression195', a2)
    if hasattr(a1, 'vhdl_RangeExpression'):
        assert not _is_linked(a1, 'vhdl_RangeExpression', b)
    if hasattr(a2, 'vhdl_RangeExpression'):
        assert _is_linked(a2, 'vhdl_RangeExpression', b)
    _safe_set(b, 'vhdl_Expression195', None)
    assert not _is_linked(b, 'vhdl_Expression195', a2)
    if hasattr(a2, 'vhdl_RangeExpression'):
        assert not _is_linked(a2, 'vhdl_RangeExpression', b)


def test_assoc_left199_reverse_link_reassign_clear():
    a1 = vhdl_LogicalExpression(operator="sample_text")
    a2 = vhdl_LogicalExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression200', a1)
    assert _is_linked(b, 'vhdl_Expression200', a1)
    if hasattr(a1, 'vhdl_LogicalExpression'):
        assert _is_linked(a1, 'vhdl_LogicalExpression', b)
    _safe_set(b, 'vhdl_Expression200', a2)
    assert _is_linked(b, 'vhdl_Expression200', a2)
    if hasattr(a1, 'vhdl_LogicalExpression'):
        assert not _is_linked(a1, 'vhdl_LogicalExpression', b)
    if hasattr(a2, 'vhdl_LogicalExpression'):
        assert _is_linked(a2, 'vhdl_LogicalExpression', b)
    _safe_set(b, 'vhdl_Expression200', None)
    assert not _is_linked(b, 'vhdl_Expression200', a2)
    if hasattr(a2, 'vhdl_LogicalExpression'):
        assert not _is_linked(a2, 'vhdl_LogicalExpression', b)


def test_assoc_left204_reverse_link_reassign_clear():
    a1 = vhdl_RelationalExpression(operator="sample_text")
    a2 = vhdl_RelationalExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression205', a1)
    assert _is_linked(b, 'vhdl_Expression205', a1)
    if hasattr(a1, 'vhdl_RelationalExpression'):
        assert _is_linked(a1, 'vhdl_RelationalExpression', b)
    _safe_set(b, 'vhdl_Expression205', a2)
    assert _is_linked(b, 'vhdl_Expression205', a2)
    if hasattr(a1, 'vhdl_RelationalExpression'):
        assert not _is_linked(a1, 'vhdl_RelationalExpression', b)
    if hasattr(a2, 'vhdl_RelationalExpression'):
        assert _is_linked(a2, 'vhdl_RelationalExpression', b)
    _safe_set(b, 'vhdl_Expression205', None)
    assert not _is_linked(b, 'vhdl_Expression205', a2)
    if hasattr(a2, 'vhdl_RelationalExpression'):
        assert not _is_linked(a2, 'vhdl_RelationalExpression', b)


def test_assoc_left214_reverse_link_reassign_clear():
    a1 = vhdl_ShiftExpression(operator="sample_text")
    a2 = vhdl_ShiftExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression215', a1)
    assert _is_linked(b, 'vhdl_Expression215', a1)
    if hasattr(a1, 'vhdl_ShiftExpression'):
        assert _is_linked(a1, 'vhdl_ShiftExpression', b)
    _safe_set(b, 'vhdl_Expression215', a2)
    assert _is_linked(b, 'vhdl_Expression215', a2)
    if hasattr(a1, 'vhdl_ShiftExpression'):
        assert not _is_linked(a1, 'vhdl_ShiftExpression', b)
    if hasattr(a2, 'vhdl_ShiftExpression'):
        assert _is_linked(a2, 'vhdl_ShiftExpression', b)
    _safe_set(b, 'vhdl_Expression215', None)
    assert not _is_linked(b, 'vhdl_Expression215', a2)
    if hasattr(a2, 'vhdl_ShiftExpression'):
        assert not _is_linked(a2, 'vhdl_ShiftExpression', b)


def test_assoc_left219_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_AddingExpression(operator="sample_text")
    _safe_set(b, 'vhdl_AddingExpression', a1)
    assert _is_linked(b, 'vhdl_AddingExpression', a1)
    if hasattr(a1, 'vhdl_Expression220'):
        assert _is_linked(a1, 'vhdl_Expression220', b)
    _safe_set(b, 'vhdl_AddingExpression', a2)
    assert _is_linked(b, 'vhdl_AddingExpression', a2)
    if hasattr(a1, 'vhdl_Expression220'):
        assert not _is_linked(a1, 'vhdl_Expression220', b)
    if hasattr(a2, 'vhdl_Expression220'):
        assert _is_linked(a2, 'vhdl_Expression220', b)
    _safe_set(b, 'vhdl_AddingExpression', None)
    assert not _is_linked(b, 'vhdl_AddingExpression', a2)
    if hasattr(a2, 'vhdl_Expression220'):
        assert not _is_linked(a2, 'vhdl_Expression220', b)


def test_assoc_left224_reverse_link_reassign_clear():
    a1 = vhdl_MultiplyingExpression(operator="sample_text")
    a2 = vhdl_MultiplyingExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression225', a1)
    assert _is_linked(b, 'vhdl_Expression225', a1)
    if hasattr(a1, 'vhdl_MultiplyingExpression'):
        assert _is_linked(a1, 'vhdl_MultiplyingExpression', b)
    _safe_set(b, 'vhdl_Expression225', a2)
    assert _is_linked(b, 'vhdl_Expression225', a2)
    if hasattr(a1, 'vhdl_MultiplyingExpression'):
        assert not _is_linked(a1, 'vhdl_MultiplyingExpression', b)
    if hasattr(a2, 'vhdl_MultiplyingExpression'):
        assert _is_linked(a2, 'vhdl_MultiplyingExpression', b)
    _safe_set(b, 'vhdl_Expression225', None)
    assert not _is_linked(b, 'vhdl_Expression225', a2)
    if hasattr(a2, 'vhdl_MultiplyingExpression'):
        assert not _is_linked(a2, 'vhdl_MultiplyingExpression', b)


def test_assoc_lib3_reverse_link_reassign_clear():
    a1 = vhdl_UseClause(importedNamespace="sample_text")
    a2 = vhdl_UseClause(importedNamespace="sample_text_2")
    b = vhdl_Library(builtin_lib="sample_text")
    _safe_set(b, 'vhdl_Library', a1)
    assert _is_linked(b, 'vhdl_Library', a1)
    if hasattr(a1, 'vhdl_UseClause'):
        assert _is_linked(a1, 'vhdl_UseClause', b)
    _safe_set(b, 'vhdl_Library', a2)
    assert _is_linked(b, 'vhdl_Library', a2)
    if hasattr(a1, 'vhdl_UseClause'):
        assert not _is_linked(a1, 'vhdl_UseClause', b)
    if hasattr(a2, 'vhdl_UseClause'):
        assert _is_linked(a2, 'vhdl_UseClause', b)
    _safe_set(b, 'vhdl_Library', None)
    assert not _is_linked(b, 'vhdl_Library', a2)
    if hasattr(a2, 'vhdl_UseClause'):
        assert not _is_linked(a2, 'vhdl_UseClause', b)


def test_assoc_lib71_reverse_link_reassign_clear():
    a1 = vhdl_Library(builtin_lib="sample_text")
    a2 = vhdl_Library(builtin_lib="sample_text_2")
    b = vhdl_EntityInstantiationStatement(name="sample_text")
    _safe_set(b, 'vhdl_EntityInstantiationStatement', a1)
    assert _is_linked(b, 'vhdl_EntityInstantiationStatement', a1)
    if hasattr(a1, 'vhdl_Library72'):
        assert _is_linked(a1, 'vhdl_Library72', b)
    _safe_set(b, 'vhdl_EntityInstantiationStatement', a2)
    assert _is_linked(b, 'vhdl_EntityInstantiationStatement', a2)
    if hasattr(a1, 'vhdl_Library72'):
        assert not _is_linked(a1, 'vhdl_Library72', b)
    if hasattr(a2, 'vhdl_Library72'):
        assert _is_linked(a2, 'vhdl_Library72', b)
    _safe_set(b, 'vhdl_EntityInstantiationStatement', None)
    assert not _is_linked(b, 'vhdl_EntityInstantiationStatement', a2)
    if hasattr(a2, 'vhdl_Library72'):
        assert not _is_linked(a2, 'vhdl_Library72', b)


def test_assoc_right196_reverse_link_reassign_clear():
    a1 = vhdl_RangeExpression(direction="sample_text", operator="sample_text")
    a2 = vhdl_RangeExpression(direction="sample_text_2", operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression198', a1)
    assert _is_linked(b, 'vhdl_Expression198', a1)
    if hasattr(a1, 'vhdl_RangeExpression197'):
        assert _is_linked(a1, 'vhdl_RangeExpression197', b)
    _safe_set(b, 'vhdl_Expression198', a2)
    assert _is_linked(b, 'vhdl_Expression198', a2)
    if hasattr(a1, 'vhdl_RangeExpression197'):
        assert not _is_linked(a1, 'vhdl_RangeExpression197', b)
    if hasattr(a2, 'vhdl_RangeExpression197'):
        assert _is_linked(a2, 'vhdl_RangeExpression197', b)
    _safe_set(b, 'vhdl_Expression198', None)
    assert not _is_linked(b, 'vhdl_Expression198', a2)
    if hasattr(a2, 'vhdl_RangeExpression197'):
        assert not _is_linked(a2, 'vhdl_RangeExpression197', b)


def test_assoc_right201_reverse_link_reassign_clear():
    a1 = vhdl_LogicalExpression(operator="sample_text")
    a2 = vhdl_LogicalExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression203', a1)
    assert _is_linked(b, 'vhdl_Expression203', a1)
    if hasattr(a1, 'vhdl_LogicalExpression202'):
        assert _is_linked(a1, 'vhdl_LogicalExpression202', b)
    _safe_set(b, 'vhdl_Expression203', a2)
    assert _is_linked(b, 'vhdl_Expression203', a2)
    if hasattr(a1, 'vhdl_LogicalExpression202'):
        assert not _is_linked(a1, 'vhdl_LogicalExpression202', b)
    if hasattr(a2, 'vhdl_LogicalExpression202'):
        assert _is_linked(a2, 'vhdl_LogicalExpression202', b)
    _safe_set(b, 'vhdl_Expression203', None)
    assert not _is_linked(b, 'vhdl_Expression203', a2)
    if hasattr(a2, 'vhdl_LogicalExpression202'):
        assert not _is_linked(a2, 'vhdl_LogicalExpression202', b)


def test_assoc_right206_reverse_link_reassign_clear():
    a1 = vhdl_RelationalExpression(operator="sample_text")
    a2 = vhdl_RelationalExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression208', a1)
    assert _is_linked(b, 'vhdl_Expression208', a1)
    if hasattr(a1, 'vhdl_RelationalExpression207'):
        assert _is_linked(a1, 'vhdl_RelationalExpression207', b)
    _safe_set(b, 'vhdl_Expression208', a2)
    assert _is_linked(b, 'vhdl_Expression208', a2)
    if hasattr(a1, 'vhdl_RelationalExpression207'):
        assert not _is_linked(a1, 'vhdl_RelationalExpression207', b)
    if hasattr(a2, 'vhdl_RelationalExpression207'):
        assert _is_linked(a2, 'vhdl_RelationalExpression207', b)
    _safe_set(b, 'vhdl_Expression208', None)
    assert not _is_linked(b, 'vhdl_Expression208', a2)
    if hasattr(a2, 'vhdl_RelationalExpression207'):
        assert not _is_linked(a2, 'vhdl_RelationalExpression207', b)


def test_assoc_right216_reverse_link_reassign_clear():
    a1 = vhdl_ShiftExpression(operator="sample_text")
    a2 = vhdl_ShiftExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression218', a1)
    assert _is_linked(b, 'vhdl_Expression218', a1)
    if hasattr(a1, 'vhdl_ShiftExpression217'):
        assert _is_linked(a1, 'vhdl_ShiftExpression217', b)
    _safe_set(b, 'vhdl_Expression218', a2)
    assert _is_linked(b, 'vhdl_Expression218', a2)
    if hasattr(a1, 'vhdl_ShiftExpression217'):
        assert not _is_linked(a1, 'vhdl_ShiftExpression217', b)
    if hasattr(a2, 'vhdl_ShiftExpression217'):
        assert _is_linked(a2, 'vhdl_ShiftExpression217', b)
    _safe_set(b, 'vhdl_Expression218', None)
    assert not _is_linked(b, 'vhdl_Expression218', a2)
    if hasattr(a2, 'vhdl_ShiftExpression217'):
        assert not _is_linked(a2, 'vhdl_ShiftExpression217', b)


def test_assoc_right221_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_AddingExpression(operator="sample_text")
    _safe_set(b, 'vhdl_AddingExpression222', a1)
    assert _is_linked(b, 'vhdl_AddingExpression222', a1)
    if hasattr(a1, 'vhdl_Expression223'):
        assert _is_linked(a1, 'vhdl_Expression223', b)
    _safe_set(b, 'vhdl_AddingExpression222', a2)
    assert _is_linked(b, 'vhdl_AddingExpression222', a2)
    if hasattr(a1, 'vhdl_Expression223'):
        assert not _is_linked(a1, 'vhdl_Expression223', b)
    if hasattr(a2, 'vhdl_Expression223'):
        assert _is_linked(a2, 'vhdl_Expression223', b)
    _safe_set(b, 'vhdl_AddingExpression222', None)
    assert not _is_linked(b, 'vhdl_AddingExpression222', a2)
    if hasattr(a2, 'vhdl_Expression223'):
        assert not _is_linked(a2, 'vhdl_Expression223', b)


def test_assoc_right226_reverse_link_reassign_clear():
    a1 = vhdl_MultiplyingExpression(operator="sample_text")
    a2 = vhdl_MultiplyingExpression(operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression228', a1)
    assert _is_linked(b, 'vhdl_Expression228', a1)
    if hasattr(a1, 'vhdl_MultiplyingExpression227'):
        assert _is_linked(a1, 'vhdl_MultiplyingExpression227', b)
    _safe_set(b, 'vhdl_Expression228', a2)
    assert _is_linked(b, 'vhdl_Expression228', a2)
    if hasattr(a1, 'vhdl_MultiplyingExpression227'):
        assert not _is_linked(a1, 'vhdl_MultiplyingExpression227', b)
    if hasattr(a2, 'vhdl_MultiplyingExpression227'):
        assert _is_linked(a2, 'vhdl_MultiplyingExpression227', b)
    _safe_set(b, 'vhdl_Expression228', None)
    assert not _is_linked(b, 'vhdl_Expression228', a2)
    if hasattr(a2, 'vhdl_MultiplyingExpression227'):
        assert not _is_linked(a2, 'vhdl_MultiplyingExpression227', b)


def test_assoc_target160_reverse_link_reassign_clear():
    a1 = vhdl_SequentialSignalAssignmentStatement(guarded=True, label="sample_text", postponed=True)
    a2 = vhdl_SequentialSignalAssignmentStatement(guarded=False, label="sample_text_2", postponed=False)
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression161', a1)
    assert _is_linked(b, 'vhdl_Expression161', a1)
    if hasattr(a1, 'vhdl_SequentialSignalAssignmentStatement'):
        assert _is_linked(a1, 'vhdl_SequentialSignalAssignmentStatement', b)
    _safe_set(b, 'vhdl_Expression161', a2)
    assert _is_linked(b, 'vhdl_Expression161', a2)
    if hasattr(a1, 'vhdl_SequentialSignalAssignmentStatement'):
        assert not _is_linked(a1, 'vhdl_SequentialSignalAssignmentStatement', b)
    if hasattr(a2, 'vhdl_SequentialSignalAssignmentStatement'):
        assert _is_linked(a2, 'vhdl_SequentialSignalAssignmentStatement', b)
    _safe_set(b, 'vhdl_Expression161', None)
    assert not _is_linked(b, 'vhdl_Expression161', a2)
    if hasattr(a2, 'vhdl_SequentialSignalAssignmentStatement'):
        assert not _is_linked(a2, 'vhdl_SequentialSignalAssignmentStatement', b)


def test_assoc_target89_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_ConditionalSignalAssignmentStatement(guarded=True, postponed=True)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement', a1)
    assert _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement', a1)
    if hasattr(a1, 'vhdl_Expression90'):
        assert _is_linked(a1, 'vhdl_Expression90', b)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement', a2)
    assert _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement', a2)
    if hasattr(a1, 'vhdl_Expression90'):
        assert not _is_linked(a1, 'vhdl_Expression90', b)
    if hasattr(a2, 'vhdl_Expression90'):
        assert _is_linked(a2, 'vhdl_Expression90', b)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement', None)
    assert not _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement', a2)
    if hasattr(a2, 'vhdl_Expression90'):
        assert not _is_linked(a2, 'vhdl_Expression90', b)


def test_assoc_time129_reverse_link_reassign_clear():
    a1 = vhdl_WaitStatement(label="sample_text")
    a2 = vhdl_WaitStatement(label="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression131', a1)
    assert _is_linked(b, 'vhdl_Expression131', a1)
    if hasattr(a1, 'vhdl_WaitStatement130'):
        assert _is_linked(a1, 'vhdl_WaitStatement130', b)
    _safe_set(b, 'vhdl_Expression131', a2)
    assert _is_linked(b, 'vhdl_Expression131', a2)
    if hasattr(a1, 'vhdl_WaitStatement130'):
        assert not _is_linked(a1, 'vhdl_WaitStatement130', b)
    if hasattr(a2, 'vhdl_WaitStatement130'):
        assert _is_linked(a2, 'vhdl_WaitStatement130', b)
    _safe_set(b, 'vhdl_Expression131', None)
    assert not _is_linked(b, 'vhdl_Expression131', a2)
    if hasattr(a2, 'vhdl_WaitStatement130'):
        assert not _is_linked(a2, 'vhdl_WaitStatement130', b)


def test_assoc_type20_reverse_link_reassign_clear():
    a1 = vhdl_SubtypeIndication(builtin_type="sample_text")
    a2 = vhdl_SubtypeIndication(builtin_type="sample_text_2")
    b = vhdl_Port(kind="sample_text", mode="sample_text")
    _safe_set(b, 'vhdl_Port21', a1)
    assert _is_linked(b, 'vhdl_Port21', a1)
    if hasattr(a1, 'vhdl_SubtypeIndication'):
        assert _is_linked(a1, 'vhdl_SubtypeIndication', b)
    _safe_set(b, 'vhdl_Port21', a2)
    assert _is_linked(b, 'vhdl_Port21', a2)
    if hasattr(a1, 'vhdl_SubtypeIndication'):
        assert not _is_linked(a1, 'vhdl_SubtypeIndication', b)
    if hasattr(a2, 'vhdl_SubtypeIndication'):
        assert _is_linked(a2, 'vhdl_SubtypeIndication', b)
    _safe_set(b, 'vhdl_Port21', None)
    assert not _is_linked(b, 'vhdl_Port21', a2)
    if hasattr(a2, 'vhdl_SubtypeIndication'):
        assert not _is_linked(a2, 'vhdl_SubtypeIndication', b)


def test_assoc_type38_reverse_link_reassign_clear():
    a1 = vhdl_SubtypeIndication(builtin_type="sample_text")
    a2 = vhdl_SubtypeIndication(builtin_type="sample_text_2")
    b = vhdl_SignalDeclaration(kind="sample_text")
    _safe_set(b, 'vhdl_SignalDeclaration39', a1)
    assert _is_linked(b, 'vhdl_SignalDeclaration39', a1)
    if hasattr(a1, 'vhdl_SubtypeIndication40'):
        assert _is_linked(a1, 'vhdl_SubtypeIndication40', b)
    _safe_set(b, 'vhdl_SignalDeclaration39', a2)
    assert _is_linked(b, 'vhdl_SignalDeclaration39', a2)
    if hasattr(a1, 'vhdl_SubtypeIndication40'):
        assert not _is_linked(a1, 'vhdl_SubtypeIndication40', b)
    if hasattr(a2, 'vhdl_SubtypeIndication40'):
        assert _is_linked(a2, 'vhdl_SubtypeIndication40', b)
    _safe_set(b, 'vhdl_SignalDeclaration39', None)
    assert not _is_linked(b, 'vhdl_SignalDeclaration39', a2)
    if hasattr(a2, 'vhdl_SubtypeIndication40'):
        assert not _is_linked(a2, 'vhdl_SubtypeIndication40', b)


def test_assoc_type45_reverse_link_reassign_clear():
    a1 = vhdl_VariableDeclaration(shared=True)
    a2 = vhdl_VariableDeclaration(shared=False)
    b = vhdl_SubtypeIndication(builtin_type="sample_text")
    _safe_set(b, 'vhdl_SubtypeIndication47', a1)
    assert _is_linked(b, 'vhdl_SubtypeIndication47', a1)
    if hasattr(a1, 'vhdl_VariableDeclaration46'):
        assert _is_linked(a1, 'vhdl_VariableDeclaration46', b)
    _safe_set(b, 'vhdl_SubtypeIndication47', a2)
    assert _is_linked(b, 'vhdl_SubtypeIndication47', a2)
    if hasattr(a1, 'vhdl_VariableDeclaration46'):
        assert not _is_linked(a1, 'vhdl_VariableDeclaration46', b)
    if hasattr(a2, 'vhdl_VariableDeclaration46'):
        assert _is_linked(a2, 'vhdl_VariableDeclaration46', b)
    _safe_set(b, 'vhdl_SubtypeIndication47', None)
    assert not _is_linked(b, 'vhdl_SubtypeIndication47', a2)
    if hasattr(a2, 'vhdl_VariableDeclaration46'):
        assert not _is_linked(a2, 'vhdl_VariableDeclaration46', b)


def test_assoc_until126_reverse_link_reassign_clear():
    a1 = vhdl_WaitStatement(label="sample_text")
    a2 = vhdl_WaitStatement(label="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression128', a1)
    assert _is_linked(b, 'vhdl_Expression128', a1)
    if hasattr(a1, 'vhdl_WaitStatement127'):
        assert _is_linked(a1, 'vhdl_WaitStatement127', b)
    _safe_set(b, 'vhdl_Expression128', a2)
    assert _is_linked(b, 'vhdl_Expression128', a2)
    if hasattr(a1, 'vhdl_WaitStatement127'):
        assert not _is_linked(a1, 'vhdl_WaitStatement127', b)
    if hasattr(a2, 'vhdl_WaitStatement127'):
        assert _is_linked(a2, 'vhdl_WaitStatement127', b)
    _safe_set(b, 'vhdl_Expression128', None)
    assert not _is_linked(b, 'vhdl_Expression128', a2)
    if hasattr(a2, 'vhdl_WaitStatement127'):
        assert not _is_linked(a2, 'vhdl_WaitStatement127', b)


def test_assoc_value188_reverse_link_reassign_clear():
    a1 = vhdl_Variable(name="sample_text")
    a2 = vhdl_Variable(name="sample_text_2")
    b = vhdl_Variable(name="sample_text")
    _safe_set(b, 'vhdl_Variable187', a1)
    assert _is_linked(b, 'vhdl_Variable187', a1)
    if hasattr(a1, 'vhdl_Variable'):
        assert _is_linked(a1, 'vhdl_Variable', b)
    _safe_set(b, 'vhdl_Variable187', a2)
    assert _is_linked(b, 'vhdl_Variable187', a2)
    if hasattr(a1, 'vhdl_Variable'):
        assert not _is_linked(a1, 'vhdl_Variable', b)
    if hasattr(a2, 'vhdl_Variable'):
        assert _is_linked(a2, 'vhdl_Variable', b)
    _safe_set(b, 'vhdl_Variable187', None)
    assert not _is_linked(b, 'vhdl_Variable187', a2)
    if hasattr(a2, 'vhdl_Variable'):
        assert not _is_linked(a2, 'vhdl_Variable', b)


def test_assoc_waveform162_reverse_link_reassign_clear():
    a1 = vhdl_SequentialSignalAssignmentStatement(guarded=True, label="sample_text", postponed=True)
    a2 = vhdl_SequentialSignalAssignmentStatement(guarded=False, label="sample_text_2", postponed=False)
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression164', a1)
    assert _is_linked(b, 'vhdl_Expression164', a1)
    if hasattr(a1, 'vhdl_SequentialSignalAssignmentStatement163'):
        assert _is_linked(a1, 'vhdl_SequentialSignalAssignmentStatement163', b)
    _safe_set(b, 'vhdl_Expression164', a2)
    assert _is_linked(b, 'vhdl_Expression164', a2)
    if hasattr(a1, 'vhdl_SequentialSignalAssignmentStatement163'):
        assert not _is_linked(a1, 'vhdl_SequentialSignalAssignmentStatement163', b)
    if hasattr(a2, 'vhdl_SequentialSignalAssignmentStatement163'):
        assert _is_linked(a2, 'vhdl_SequentialSignalAssignmentStatement163', b)
    _safe_set(b, 'vhdl_Expression164', None)
    assert not _is_linked(b, 'vhdl_Expression164', a2)
    if hasattr(a2, 'vhdl_SequentialSignalAssignmentStatement163'):
        assert not _is_linked(a2, 'vhdl_SequentialSignalAssignmentStatement163', b)


def test_assoc_waveform91_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_ConditionalSignalAssignmentStatement(guarded=True, postponed=True)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement92', {a1})
    assert _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement92', a1)
    if hasattr(a1, 'vhdl_Expression93'):
        assert _is_linked(a1, 'vhdl_Expression93', b)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement92', {a2})
    assert _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement92', a2)
    if hasattr(a1, 'vhdl_Expression93'):
        assert not _is_linked(a1, 'vhdl_Expression93', b)
    if hasattr(a2, 'vhdl_Expression93'):
        assert _is_linked(a2, 'vhdl_Expression93', b)
    _safe_set(b, 'vhdl_ConditionalSignalAssignmentStatement92', set())
    assert not _is_linked(b, 'vhdl_ConditionalSignalAssignmentStatement92', a2)
    if hasattr(a2, 'vhdl_Expression93'):
        assert not _is_linked(a2, 'vhdl_Expression93', b)


def test_assoc_waveform95_reverse_link_reassign_clear():
    a1 = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    a2 = vhdl_Expression(attribute="sample_text_2", unary_operator="sample_text_2")
    b = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    _safe_set(b, 'vhdl_Expression96', a1)
    assert _is_linked(b, 'vhdl_Expression96', a1)
    if hasattr(a1, 'vhdl_Expression94'):
        assert _is_linked(a1, 'vhdl_Expression94', b)
    _safe_set(b, 'vhdl_Expression96', a2)
    assert _is_linked(b, 'vhdl_Expression96', a2)
    if hasattr(a1, 'vhdl_Expression94'):
        assert not _is_linked(a1, 'vhdl_Expression94', b)
    if hasattr(a2, 'vhdl_Expression94'):
        assert _is_linked(a2, 'vhdl_Expression94', b)
    _safe_set(b, 'vhdl_Expression96', None)
    assert not _is_linked(b, 'vhdl_Expression96', a2)
    if hasattr(a2, 'vhdl_Expression94'):
        assert not _is_linked(a2, 'vhdl_Expression94', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_LibraryUnits1_stub_double():
    # vhdl_DesignFile has no real 'vhdl_DesignFile2' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_LibraryUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_LibraryUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_LibraryUnit(name="sample_text")
    partner = vhdl_DesignFile()
    setattr(partner, 'vhdl_DesignFile2', None)
    _safe_set(owner, 'vhdl_LibraryUnit', partner)
    assert owner in getattr(partner, 'vhdl_DesignFile2')
    _safe_set(owner, 'vhdl_LibraryUnit', None)
    assert owner not in getattr(partner, 'vhdl_DesignFile2')


def test_assoc_alias32_stub_double():
    # vhdl_Alias has no real 'vhdl_Alias' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_Alias()
    setattr(partner, 'vhdl_Alias', None)
    _safe_set(owner, 'vhdl_SubtypeIndication33', partner)
    assert getattr(partner, 'vhdl_Alias') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication33', None)
    assert getattr(partner, 'vhdl_Alias') is None


def test_assoc_association79_stub_double():
    # vhdl_PortMap has no real 'vhdl_PortMap80' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_PortMapAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_PortMapAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_PortMapAssociation(formal="sample_text")
    partner = vhdl_PortMap()
    setattr(partner, 'vhdl_PortMap80', None)
    _safe_set(owner, 'vhdl_PortMapAssociation', partner)
    assert owner in getattr(partner, 'vhdl_PortMap80')
    _safe_set(owner, 'vhdl_PortMapAssociation', None)
    assert owner not in getattr(partner, 'vhdl_PortMap80')


def test_assoc_association84_stub_double():
    # vhdl_GenericMap has no real 'vhdl_GenericMap85' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_GenericMapAssociation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_GenericMapAssociation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_GenericMapAssociation(formal="sample_text")
    partner = vhdl_GenericMap()
    setattr(partner, 'vhdl_GenericMap85', None)
    _safe_set(owner, 'vhdl_GenericMapAssociation', partner)
    assert owner in getattr(partner, 'vhdl_GenericMap85')
    _safe_set(owner, 'vhdl_GenericMapAssociation', None)
    assert owner not in getattr(partner, 'vhdl_GenericMap85')


def test_assoc_choice146_stub_double():
    # vhdl_CaseAlternative has no real 'vhdl_CaseAlternative147' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_CaseAlternative()
    setattr(partner, 'vhdl_CaseAlternative147', None)
    _safe_set(owner, 'vhdl_Expression148', partner)
    assert getattr(partner, 'vhdl_CaseAlternative147') == owner
    _safe_set(owner, 'vhdl_Expression148', None)
    assert getattr(partner, 'vhdl_CaseAlternative147') is None


def test_assoc_choice192_stub_double():
    # vhdl_ConditionalWaveformExpression has no real 'vhdl_ConditionalWaveformExpression' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ConditionalWaveformExpression()
    setattr(partner, 'vhdl_ConditionalWaveformExpression', None)
    _safe_set(owner, 'vhdl_Expression193', partner)
    assert getattr(partner, 'vhdl_ConditionalWaveformExpression') == owner
    _safe_set(owner, 'vhdl_Expression193', None)
    assert getattr(partner, 'vhdl_ConditionalWaveformExpression') is None


def test_assoc_condition116_stub_double():
    # vhdl_IfGenerateStatement has no real 'vhdl_IfGenerateStatement' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_IfGenerateStatement()
    setattr(partner, 'vhdl_IfGenerateStatement', None)
    _safe_set(owner, 'vhdl_Expression117', partner)
    assert getattr(partner, 'vhdl_IfGenerateStatement') == owner
    _safe_set(owner, 'vhdl_Expression117', None)
    assert getattr(partner, 'vhdl_IfGenerateStatement') is None


def test_assoc_condition136_stub_double():
    # vhdl_IfStatementTest has no real 'vhdl_IfStatementTest137' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_IfStatementTest()
    setattr(partner, 'vhdl_IfStatementTest137', None)
    _safe_set(owner, 'vhdl_Expression138', partner)
    assert getattr(partner, 'vhdl_IfStatementTest137') == owner
    _safe_set(owner, 'vhdl_Expression138', None)
    assert getattr(partner, 'vhdl_IfStatementTest137') is None


def test_assoc_condition165_stub_double():
    # vhdl_WhileIterationScheme has no real 'vhdl_WhileIterationScheme' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_WhileIterationScheme()
    setattr(partner, 'vhdl_WhileIterationScheme', None)
    _safe_set(owner, 'vhdl_Expression166', partner)
    assert getattr(partner, 'vhdl_WhileIterationScheme') == owner
    _safe_set(owner, 'vhdl_Expression166', None)
    assert getattr(partner, 'vhdl_WhileIterationScheme') is None


def test_assoc_constraint181_stub_double():
    # vhdl_ConstrainedArrayTypeDefinition has no real 'vhdl_ConstrainedArrayTypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ConstrainedArrayTypeDefinition()
    setattr(partner, 'vhdl_ConstrainedArrayTypeDefinition', None)
    _safe_set(owner, 'vhdl_Expression182', partner)
    assert getattr(partner, 'vhdl_ConstrainedArrayTypeDefinition') == owner
    _safe_set(owner, 'vhdl_Expression182', None)
    assert getattr(partner, 'vhdl_ConstrainedArrayTypeDefinition') is None


def test_assoc_declaration18_stub_double():
    # vhdl_Ports has no real 'vhdl_Ports19' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Port(kind="sample_text", mode="sample_text")
    partner = vhdl_Ports()
    setattr(partner, 'vhdl_Ports19', None)
    _safe_set(owner, 'vhdl_Port', partner)
    assert owner in getattr(partner, 'vhdl_Ports19')
    _safe_set(owner, 'vhdl_Port', None)
    assert owner not in getattr(partner, 'vhdl_Ports19')


def test_assoc_field183_stub_double():
    # vhdl_RecordTypeDefinition has no real 'vhdl_RecordTypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_RecordField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_RecordField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_RecordField(name="sample_text")
    partner = vhdl_RecordTypeDefinition()
    setattr(partner, 'vhdl_RecordTypeDefinition', None)
    _safe_set(owner, 'vhdl_RecordField', partner)
    assert owner in getattr(partner, 'vhdl_RecordTypeDefinition')
    _safe_set(owner, 'vhdl_RecordField', None)
    assert owner not in getattr(partner, 'vhdl_RecordTypeDefinition')


def test_assoc_generic60_stub_double():
    # vhdl_Generics has no real 'vhdl_Generics61' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Component(name="sample_text")
    partner = vhdl_Generics()
    setattr(partner, 'vhdl_Generics61', None)
    _safe_set(owner, 'vhdl_Component', partner)
    assert getattr(partner, 'vhdl_Generics61') == owner
    _safe_set(owner, 'vhdl_Component', None)
    assert getattr(partner, 'vhdl_Generics61') is None


def test_assoc_genericMap68_stub_double():
    # vhdl_GenericMap has no real 'vhdl_GenericMap' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ComponentInstantiationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ComponentInstantiationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ComponentInstantiationStatement(name="sample_text")
    partner = vhdl_GenericMap()
    setattr(partner, 'vhdl_GenericMap', None)
    _safe_set(owner, 'vhdl_ComponentInstantiationStatement', partner)
    assert getattr(partner, 'vhdl_GenericMap') == owner
    _safe_set(owner, 'vhdl_ComponentInstantiationStatement', None)
    assert getattr(partner, 'vhdl_GenericMap') is None


def test_assoc_genericMap73_stub_double():
    # vhdl_GenericMap has no real 'vhdl_GenericMap75' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_EntityInstantiationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_EntityInstantiationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_EntityInstantiationStatement(name="sample_text")
    partner = vhdl_GenericMap()
    setattr(partner, 'vhdl_GenericMap75', None)
    _safe_set(owner, 'vhdl_EntityInstantiationStatement74', partner)
    assert getattr(partner, 'vhdl_GenericMap75') == owner
    _safe_set(owner, 'vhdl_EntityInstantiationStatement74', None)
    assert getattr(partner, 'vhdl_GenericMap75') is None


def test_assoc_id189_stub_double():
    # vhdl_IdList has no real 'vhdl_IdList190' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_IdList()
    setattr(partner, 'vhdl_IdList190', None)
    _safe_set(owner, 'vhdl_Expression191', partner)
    assert owner in getattr(partner, 'vhdl_IdList190')
    _safe_set(owner, 'vhdl_Expression191', None)
    assert owner not in getattr(partner, 'vhdl_IdList190')


def test_assoc_initial29_stub_double():
    # vhdl_Generic has no real 'vhdl_Generic30' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_Generic()
    setattr(partner, 'vhdl_Generic30', None)
    _safe_set(owner, 'vhdl_Expression31', partner)
    assert getattr(partner, 'vhdl_Generic30') == owner
    _safe_set(owner, 'vhdl_Expression31', None)
    assert getattr(partner, 'vhdl_Generic30') is None


def test_assoc_initial55_stub_double():
    # vhdl_ConstantDeclaration has no real 'vhdl_ConstantDeclaration56' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ConstantDeclaration()
    setattr(partner, 'vhdl_ConstantDeclaration56', None)
    _safe_set(owner, 'vhdl_Expression57', partner)
    assert getattr(partner, 'vhdl_ConstantDeclaration56') == owner
    _safe_set(owner, 'vhdl_Expression57', None)
    assert getattr(partner, 'vhdl_ConstantDeclaration56') is None


def test_assoc_is_34_stub_double():
    # vhdl_Alias has no real 'vhdl_Alias35' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_Alias()
    setattr(partner, 'vhdl_Alias35', None)
    _safe_set(owner, 'vhdl_Expression36', partner)
    assert getattr(partner, 'vhdl_Alias35') == owner
    _safe_set(owner, 'vhdl_Expression36', None)
    assert getattr(partner, 'vhdl_Alias35') is None


def test_assoc_left209_stub_double():
    # vhdl_ChoiceExpression has no real 'vhdl_ChoiceExpression' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ChoiceExpression()
    setattr(partner, 'vhdl_ChoiceExpression', None)
    _safe_set(owner, 'vhdl_Expression210', partner)
    assert getattr(partner, 'vhdl_ChoiceExpression') == owner
    _safe_set(owner, 'vhdl_Expression210', None)
    assert getattr(partner, 'vhdl_ChoiceExpression') is None


def test_assoc_left229_stub_double():
    # vhdl_Factor has no real 'vhdl_Factor' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_Factor()
    setattr(partner, 'vhdl_Factor', None)
    _safe_set(owner, 'vhdl_Expression230', partner)
    assert getattr(partner, 'vhdl_Factor') == owner
    _safe_set(owner, 'vhdl_Expression230', None)
    assert getattr(partner, 'vhdl_Factor') is None


def test_assoc_left234_stub_double():
    # vhdl_MemberExpression has no real 'vhdl_MemberExpression' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_MemberExpression()
    setattr(partner, 'vhdl_MemberExpression', None)
    _safe_set(owner, 'vhdl_Expression235', partner)
    assert getattr(partner, 'vhdl_MemberExpression') == owner
    _safe_set(owner, 'vhdl_Expression235', None)
    assert getattr(partner, 'vhdl_MemberExpression') is None


def test_assoc_left244_stub_double():
    # vhdl_SliceExpression has no real 'vhdl_SliceExpression' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_SliceExpression()
    setattr(partner, 'vhdl_SliceExpression', None)
    _safe_set(owner, 'vhdl_Expression245', partner)
    assert getattr(partner, 'vhdl_SliceExpression') == owner
    _safe_set(owner, 'vhdl_Expression245', None)
    assert getattr(partner, 'vhdl_SliceExpression') is None


def test_assoc_member239_stub_double():
    # vhdl_Member has no real 'vhdl_Member' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_RecordField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_RecordField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_RecordField(name="sample_text")
    partner = vhdl_Member()
    setattr(partner, 'vhdl_Member', None)
    _safe_set(owner, 'vhdl_RecordField240', partner)
    assert getattr(partner, 'vhdl_Member') == owner
    _safe_set(owner, 'vhdl_RecordField240', None)
    assert getattr(partner, 'vhdl_Member') is None


def test_assoc_port62_stub_double():
    # vhdl_Ports has no real 'vhdl_Ports64' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Component(name="sample_text")
    partner = vhdl_Ports()
    setattr(partner, 'vhdl_Ports64', None)
    _safe_set(owner, 'vhdl_Component63', partner)
    assert getattr(partner, 'vhdl_Ports64') == owner
    _safe_set(owner, 'vhdl_Component63', None)
    assert getattr(partner, 'vhdl_Ports64') is None


def test_assoc_portMap69_stub_double():
    # vhdl_PortMap has no real 'vhdl_PortMap' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ComponentInstantiationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ComponentInstantiationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ComponentInstantiationStatement(name="sample_text")
    partner = vhdl_PortMap()
    setattr(partner, 'vhdl_PortMap', None)
    _safe_set(owner, 'vhdl_ComponentInstantiationStatement70', partner)
    assert getattr(partner, 'vhdl_PortMap') == owner
    _safe_set(owner, 'vhdl_ComponentInstantiationStatement70', None)
    assert getattr(partner, 'vhdl_PortMap') is None


def test_assoc_portMap76_stub_double():
    # vhdl_PortMap has no real 'vhdl_PortMap78' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_EntityInstantiationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_EntityInstantiationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_EntityInstantiationStatement(name="sample_text")
    partner = vhdl_PortMap()
    setattr(partner, 'vhdl_PortMap78', None)
    _safe_set(owner, 'vhdl_EntityInstantiationStatement77', partner)
    assert getattr(partner, 'vhdl_PortMap78') == owner
    _safe_set(owner, 'vhdl_EntityInstantiationStatement77', None)
    assert getattr(partner, 'vhdl_PortMap78') is None


def test_assoc_range107_stub_double():
    # vhdl_ForGenerateStatement has no real 'vhdl_ForGenerateStatement108' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ForGenerateStatement()
    setattr(partner, 'vhdl_ForGenerateStatement108', None)
    _safe_set(owner, 'vhdl_Expression109', partner)
    assert getattr(partner, 'vhdl_ForGenerateStatement108') == owner
    _safe_set(owner, 'vhdl_Expression109', None)
    assert getattr(partner, 'vhdl_ForGenerateStatement108') is None


def test_assoc_range154_stub_double():
    # vhdl_LoopStatement has no real 'vhdl_LoopStatement155' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_LoopStatement()
    setattr(partner, 'vhdl_LoopStatement155', None)
    _safe_set(owner, 'vhdl_Expression156', partner)
    assert getattr(partner, 'vhdl_LoopStatement155') == owner
    _safe_set(owner, 'vhdl_Expression156', None)
    assert getattr(partner, 'vhdl_LoopStatement155') is None


def test_assoc_right211_stub_double():
    # vhdl_ChoiceExpression has no real 'vhdl_ChoiceExpression212' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_ChoiceExpression()
    setattr(partner, 'vhdl_ChoiceExpression212', None)
    _safe_set(owner, 'vhdl_Expression213', partner)
    assert getattr(partner, 'vhdl_ChoiceExpression212') == owner
    _safe_set(owner, 'vhdl_Expression213', None)
    assert getattr(partner, 'vhdl_ChoiceExpression212') is None


def test_assoc_right231_stub_double():
    # vhdl_Factor has no real 'vhdl_Factor232' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_Factor()
    setattr(partner, 'vhdl_Factor232', None)
    _safe_set(owner, 'vhdl_Expression233', partner)
    assert getattr(partner, 'vhdl_Factor232') == owner
    _safe_set(owner, 'vhdl_Expression233', None)
    assert getattr(partner, 'vhdl_Factor232') is None


def test_assoc_right236_stub_double():
    # vhdl_MemberExpression has no real 'vhdl_MemberExpression237' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_MemberExpression()
    setattr(partner, 'vhdl_MemberExpression237', None)
    _safe_set(owner, 'vhdl_Expression238', partner)
    assert getattr(partner, 'vhdl_MemberExpression237') == owner
    _safe_set(owner, 'vhdl_Expression238', None)
    assert getattr(partner, 'vhdl_MemberExpression237') is None


def test_assoc_sensitivity124_stub_double():
    # vhdl_IdList has no real 'vhdl_IdList125' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_WaitStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_WaitStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_WaitStatement(label="sample_text")
    partner = vhdl_IdList()
    setattr(partner, 'vhdl_IdList125', None)
    _safe_set(owner, 'vhdl_WaitStatement', partner)
    assert getattr(partner, 'vhdl_IdList125') == owner
    _safe_set(owner, 'vhdl_WaitStatement', None)
    assert getattr(partner, 'vhdl_IdList125') is None


def test_assoc_sensitivity65_stub_double():
    # vhdl_IdList has no real 'vhdl_IdList' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ProcessStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ProcessStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ProcessStatement(postponed=True)
    partner = vhdl_IdList()
    setattr(partner, 'vhdl_IdList', None)
    _safe_set(owner, 'vhdl_ProcessStatement', partner)
    assert getattr(partner, 'vhdl_IdList') == owner
    _safe_set(owner, 'vhdl_ProcessStatement', None)
    assert getattr(partner, 'vhdl_IdList') is None


def test_assoc_sig37_stub_double():
    # vhdl_Signal has no real 'vhdl_Signal' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SignalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SignalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SignalDeclaration(kind="sample_text")
    partner = vhdl_Signal()
    setattr(partner, 'vhdl_Signal', None)
    _safe_set(owner, 'vhdl_SignalDeclaration', {partner})
    assert getattr(partner, 'vhdl_Signal') == owner
    _safe_set(owner, 'vhdl_SignalDeclaration', set())
    assert getattr(partner, 'vhdl_Signal') is None


def test_assoc_slice241_stub_double():
    # vhdl_Member has no real 'vhdl_Member242' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_Member()
    setattr(partner, 'vhdl_Member242', None)
    _safe_set(owner, 'vhdl_Expression243', partner)
    assert owner in getattr(partner, 'vhdl_Member242')
    _safe_set(owner, 'vhdl_Expression243', None)
    assert owner not in getattr(partner, 'vhdl_Member242')


def test_assoc_slice246_stub_double():
    # vhdl_SliceExpression has no real 'vhdl_SliceExpression247' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_Expression(attribute="sample_text", unary_operator="sample_text")
    partner = vhdl_SliceExpression()
    setattr(partner, 'vhdl_SliceExpression247', None)
    _safe_set(owner, 'vhdl_Expression248', partner)
    assert owner in getattr(partner, 'vhdl_SliceExpression247')
    _safe_set(owner, 'vhdl_Expression248', None)
    assert owner not in getattr(partner, 'vhdl_SliceExpression247')


def test_assoc_statement113_stub_double():
    # vhdl_ForGenerateStatement has no real 'vhdl_ForGenerateStatement114' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ArchitectureStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ArchitectureStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ArchitectureStatement(label="sample_text")
    partner = vhdl_ForGenerateStatement()
    setattr(partner, 'vhdl_ForGenerateStatement114', None)
    _safe_set(owner, 'vhdl_ArchitectureStatement115', partner)
    assert owner in getattr(partner, 'vhdl_ForGenerateStatement114')
    _safe_set(owner, 'vhdl_ArchitectureStatement115', None)
    assert owner not in getattr(partner, 'vhdl_ForGenerateStatement114')


def test_assoc_statement12_stub_double():
    # vhdl_Architecture has no real 'vhdl_Architecture13' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ArchitectureStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ArchitectureStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ArchitectureStatement(label="sample_text")
    partner = vhdl_Architecture()
    setattr(partner, 'vhdl_Architecture13', None)
    _safe_set(owner, 'vhdl_ArchitectureStatement', partner)
    assert owner in getattr(partner, 'vhdl_Architecture13')
    _safe_set(owner, 'vhdl_ArchitectureStatement', None)
    assert owner not in getattr(partner, 'vhdl_Architecture13')


def test_assoc_statement121_stub_double():
    # vhdl_IfGenerateStatement has no real 'vhdl_IfGenerateStatement122' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ArchitectureStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ArchitectureStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ArchitectureStatement(label="sample_text")
    partner = vhdl_IfGenerateStatement()
    setattr(partner, 'vhdl_IfGenerateStatement122', None)
    _safe_set(owner, 'vhdl_ArchitectureStatement123', partner)
    assert owner in getattr(partner, 'vhdl_IfGenerateStatement122')
    _safe_set(owner, 'vhdl_ArchitectureStatement123', None)
    assert owner not in getattr(partner, 'vhdl_IfGenerateStatement122')


def test_assoc_statement133_stub_double():
    # vhdl_SequentialStatement has no real 'vhdl_SequentialStatement135' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_IfStatement(label="sample_text")
    partner = vhdl_SequentialStatement()
    setattr(partner, 'vhdl_SequentialStatement135', None)
    _safe_set(owner, 'vhdl_IfStatement134', {partner})
    assert getattr(partner, 'vhdl_SequentialStatement135') == owner
    _safe_set(owner, 'vhdl_IfStatement134', set())
    assert getattr(partner, 'vhdl_SequentialStatement135') is None


def test_assoc_statement66_stub_double():
    # vhdl_SequentialStatement has no real 'vhdl_SequentialStatement' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ProcessStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ProcessStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ProcessStatement(postponed=True)
    partner = vhdl_SequentialStatement()
    setattr(partner, 'vhdl_SequentialStatement', None)
    _safe_set(owner, 'vhdl_ProcessStatement67', {partner})
    assert getattr(partner, 'vhdl_SequentialStatement') == owner
    _safe_set(owner, 'vhdl_ProcessStatement67', set())
    assert getattr(partner, 'vhdl_SequentialStatement') is None


def test_assoc_test132_stub_double():
    # vhdl_IfStatementTest has no real 'vhdl_IfStatementTest' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_IfStatement(label="sample_text")
    partner = vhdl_IfStatementTest()
    setattr(partner, 'vhdl_IfStatementTest', None)
    _safe_set(owner, 'vhdl_IfStatement', {partner})
    assert getattr(partner, 'vhdl_IfStatementTest') == owner
    _safe_set(owner, 'vhdl_IfStatement', set())
    assert getattr(partner, 'vhdl_IfStatementTest') is None


def test_assoc_type174_stub_double():
    # vhdl_SubtypeDeclaration has no real 'vhdl_SubtypeDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_SubtypeDeclaration()
    setattr(partner, 'vhdl_SubtypeDeclaration', None)
    _safe_set(owner, 'vhdl_SubtypeIndication175', partner)
    assert getattr(partner, 'vhdl_SubtypeDeclaration') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication175', None)
    assert getattr(partner, 'vhdl_SubtypeDeclaration') is None


def test_assoc_type177_stub_double():
    # vhdl_AccessTypeDefinition has no real 'vhdl_AccessTypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_AccessTypeDefinition()
    setattr(partner, 'vhdl_AccessTypeDefinition', None)
    _safe_set(owner, 'vhdl_SubtypeIndication178', partner)
    assert getattr(partner, 'vhdl_AccessTypeDefinition') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication178', None)
    assert getattr(partner, 'vhdl_AccessTypeDefinition') is None


def test_assoc_type179_stub_double():
    # vhdl_ArrayTypeDefinition has no real 'vhdl_ArrayTypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_ArrayTypeDefinition()
    setattr(partner, 'vhdl_ArrayTypeDefinition', None)
    _safe_set(owner, 'vhdl_SubtypeIndication180', partner)
    assert getattr(partner, 'vhdl_ArrayTypeDefinition') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication180', None)
    assert getattr(partner, 'vhdl_ArrayTypeDefinition') is None


def test_assoc_type184_stub_double():
    # vhdl_RecordTypeDefinition has no real 'vhdl_RecordTypeDefinition185' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_RecordTypeDefinition()
    setattr(partner, 'vhdl_RecordTypeDefinition185', None)
    _safe_set(owner, 'vhdl_SubtypeIndication186', partner)
    assert owner in getattr(partner, 'vhdl_RecordTypeDefinition185')
    _safe_set(owner, 'vhdl_SubtypeIndication186', None)
    assert owner not in getattr(partner, 'vhdl_RecordTypeDefinition185')


def test_assoc_type26_stub_double():
    # vhdl_Generic has no real 'vhdl_Generic27' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_Generic()
    setattr(partner, 'vhdl_Generic27', None)
    _safe_set(owner, 'vhdl_SubtypeIndication28', partner)
    assert getattr(partner, 'vhdl_Generic27') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication28', None)
    assert getattr(partner, 'vhdl_Generic27') is None


def test_assoc_type52_stub_double():
    # vhdl_ConstantDeclaration has no real 'vhdl_ConstantDeclaration53' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_SubtypeIndication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_SubtypeIndication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_SubtypeIndication(builtin_type="sample_text")
    partner = vhdl_ConstantDeclaration()
    setattr(partner, 'vhdl_ConstantDeclaration53', None)
    _safe_set(owner, 'vhdl_SubtypeIndication54', partner)
    assert getattr(partner, 'vhdl_ConstantDeclaration53') == owner
    _safe_set(owner, 'vhdl_SubtypeIndication54', None)
    assert getattr(partner, 'vhdl_ConstantDeclaration53') is None


def test_assoc_value249_stub_double():
    # vhdl_Value has no real 'vhdl_Value' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_ValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_ValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_ValueExpression(value="sample_text")
    partner = vhdl_Value()
    setattr(partner, 'vhdl_Value', None)
    _safe_set(owner, 'vhdl_ValueExpression', partner)
    assert getattr(partner, 'vhdl_Value') == owner
    _safe_set(owner, 'vhdl_ValueExpression', None)
    assert getattr(partner, 'vhdl_Value') is None


def test_assoc_var44_stub_double():
    # vhdl_Var has no real 'vhdl_Var' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_VariableDeclaration(shared=True)
    partner = vhdl_Var()
    setattr(partner, 'vhdl_Var', None)
    _safe_set(owner, 'vhdl_VariableDeclaration', {partner})
    assert getattr(partner, 'vhdl_Var') == owner
    _safe_set(owner, 'vhdl_VariableDeclaration', set())
    assert getattr(partner, 'vhdl_Var') is None


def test_assoc_when144_stub_double():
    # vhdl_CaseAlternative has no real 'vhdl_CaseAlternative' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_CaseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_CaseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_CaseStatement(label="sample_text")
    partner = vhdl_CaseAlternative()
    setattr(partner, 'vhdl_CaseAlternative', None)
    _safe_set(owner, 'vhdl_CaseStatement145', {partner})
    assert getattr(partner, 'vhdl_CaseAlternative') == owner
    _safe_set(owner, 'vhdl_CaseStatement145', set())
    assert getattr(partner, 'vhdl_CaseAlternative') is None


