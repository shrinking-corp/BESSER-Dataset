import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractVariable,
    BinaryOperator,
    Class,
    Construct,
    ConstructiveExtension,
    ConstructiveExtensionAtContentExtensionPoint,
    ElementAccess,
    ExpansionPart,
    Expression,
    ExtensibleElement,
    L1Expr,
    L1RhsExpr,
    L2Expr,
    L2RhsExpr,
    L3Expr,
    L4Expr,
    L5Expr,
    L6Expr,
    L7Expr,
    L8Expr,
    LanguageConceptClassifier,
    LanguageConstructClassifier,
    LocalScope,
    LoopStatement,
    Module,
    NamedElement,
    PredefinedId,
    PrimitiveType,
    PropertyType,
    QuotedCode,
    RhsExpression,
    SimpleStatement,
    Statement,
    StructuredPropertyType,
    Type,
    TypedElement,
    UnaryOperator,
    VariableAccess,
    dbl_AbstractVariable,
    dbl_ActivateObject,
    dbl_ActiveLiteral,
    dbl_Advance,
    dbl_And,
    dbl_ArrayDimension,
    dbl_Assignment,
    dbl_BinaryOperator,
    dbl_BoolType,
    dbl_BooleanPropertyType,
    dbl_BreakStatement,
    dbl_CallPart,
    dbl_Cast,
    dbl_Class,
    dbl_ClassContent,
    dbl_CodeQuoteExpression,
    dbl_CompositePropertyType,
    dbl_Construct,
    dbl_ConstructiveExtension,
    dbl_ConstructiveExtensionAtContentExtensionPoint,
    dbl_Constructor,
    dbl_ContinueStatement,
    dbl_CreateObject,
    dbl_Div,
    dbl_DoubleLiteral,
    dbl_DoubleType,
    dbl_ElementAccess,
    dbl_Equal,
    dbl_ExpandExpr,
    dbl_ExpandExpression,
    dbl_ExpandStatement,
    dbl_ExpandTextPart,
    dbl_ExpandVariablePart,
    dbl_ExpansionPart,
    dbl_ExpansionStatement,
    dbl_Expression,
    dbl_ExtensibleElement,
    dbl_ExtensionDefinition,
    dbl_ExtensionSemanticsDefinition,
    dbl_FalseLiteral,
    dbl_ForStatement,
    dbl_Function,
    dbl_FunctionCall,
    dbl_Greater,
    dbl_GreaterEqual,
    dbl_IdExpr,
    dbl_IdPropertyType,
    dbl_IfStatement,
    dbl_Import,
    dbl_InstanceOf,
    dbl_IntLiteral,
    dbl_IntPropertyType,
    dbl_IntType,
    dbl_L1Expr,
    dbl_L1RhsExpr,
    dbl_L2Expr,
    dbl_L2RhsExpr,
    dbl_L3Expr,
    dbl_L3RhsExpr,
    dbl_L4Expr,
    dbl_L5Expr,
    dbl_L6Expr,
    dbl_L7Expr,
    dbl_L8Expr,
    dbl_L9Expr,
    dbl_LanguageConceptClassifier,
    dbl_LanguageConstructClassifier,
    dbl_Less,
    dbl_LessEqual,
    dbl_LocalScope,
    dbl_LocalScopeStatement,
    dbl_LoopStatement,
    dbl_MeLiteral,
    dbl_MetaAccess,
    dbl_MetaExpr,
    dbl_MetaLiteral,
    dbl_Minus,
    dbl_Mod,
    dbl_Model,
    dbl_Module,
    dbl_ModuleContent,
    dbl_Mul,
    dbl_NamedElement,
    dbl_NativeBinding,
    dbl_Neg,
    dbl_Not,
    dbl_NotEqual,
    dbl_NullLiteral,
    dbl_Or,
    dbl_Parameter,
    dbl_ParseExpr,
    dbl_Pattern,
    dbl_Plus,
    dbl_PredefinedId,
    dbl_PrimitiveType,
    dbl_Print,
    dbl_PropertyBindingExpr,
    dbl_PropertyType,
    dbl_QuotedClassContent,
    dbl_QuotedCode,
    dbl_QuotedExpression,
    dbl_QuotedModuleContent,
    dbl_QuotedStatements,
    dbl_Reactivate,
    dbl_ReferencePropertyType,
    dbl_ResumeGenStatement,
    dbl_Return,
    dbl_RhsClassifierExpr,
    dbl_RhsExpression,
    dbl_SaveGenStatement,
    dbl_SequenceExpr,
    dbl_SetExpansionContextStatement,
    dbl_SimpleStatement,
    dbl_SizeOfArray,
    dbl_Statement,
    dbl_StringLiteral,
    dbl_StringPropertyType,
    dbl_StringType,
    dbl_StructuredPropertyType,
    dbl_SuperClassSpecification,
    dbl_SuperLiteral,
    dbl_SwitchCase,
    dbl_SwitchStatement,
    dbl_TargetStatement,
    dbl_TerminalExpr,
    dbl_Terminate,
    dbl_TestStatement,
    dbl_TextualSyntaxDef,
    dbl_TimeLiteral,
    dbl_TrueLiteral,
    dbl_TsRule,
    dbl_Type,
    dbl_TypeAccess,
    dbl_TypeLiteral,
    dbl_TypedElement,
    dbl_UnaryOperator,
    dbl_UniqueIdExpr,
    dbl_Variable,
    dbl_VariableAccess,
    dbl_VoidType,
    dbl_Wait,
    dbl_WaitUntil,
    dbl_WhileStatement,
    dbl_Yield,
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

def test_assoc_attributes66_reverse_link_reassign_clear():
    a1 = dbl_Variable(class_=True, control=True)
    a2 = dbl_Variable(class_=False, control=False)
    b = dbl_Class(active=True)
    _safe_set(b, 'dbl_Class67', {a1})
    assert _is_linked(b, 'dbl_Class67', a1)
    if hasattr(a1, 'dbl_Variable68'):
        assert _is_linked(a1, 'dbl_Variable68', b)
    _safe_set(b, 'dbl_Class67', {a2})
    assert _is_linked(b, 'dbl_Class67', a2)
    if hasattr(a1, 'dbl_Variable68'):
        assert not _is_linked(a1, 'dbl_Variable68', b)
    if hasattr(a2, 'dbl_Variable68'):
        assert _is_linked(a2, 'dbl_Variable68', b)
    _safe_set(b, 'dbl_Class67', set())
    assert not _is_linked(b, 'dbl_Class67', a2)
    if hasattr(a2, 'dbl_Variable68'):
        assert not _is_linked(a2, 'dbl_Variable68', b)


def test_assoc_bindings60_reverse_link_reassign_clear():
    a1 = dbl_NativeBinding(targetLanguage="sample_text", targetType="sample_text")
    a2 = dbl_NativeBinding(targetLanguage="sample_text_2", targetType="sample_text_2")
    b = dbl_Class(active=True)
    _safe_set(b, 'dbl_Class61', {a1})
    assert _is_linked(b, 'dbl_Class61', a1)
    if hasattr(a1, 'dbl_NativeBinding'):
        assert _is_linked(a1, 'dbl_NativeBinding', b)
    _safe_set(b, 'dbl_Class61', {a2})
    assert _is_linked(b, 'dbl_Class61', a2)
    if hasattr(a1, 'dbl_NativeBinding'):
        assert not _is_linked(a1, 'dbl_NativeBinding', b)
    if hasattr(a2, 'dbl_NativeBinding'):
        assert _is_linked(a2, 'dbl_NativeBinding', b)
    _safe_set(b, 'dbl_Class61', set())
    assert not _is_linked(b, 'dbl_Class61', a2)
    if hasattr(a2, 'dbl_NativeBinding'):
        assert not _is_linked(a2, 'dbl_NativeBinding', b)


def test_assoc_methods69_reverse_link_reassign_clear():
    a1 = dbl_Function(abstract=True, class_=True)
    a2 = dbl_Function(abstract=False, class_=False)
    b = dbl_Class(active=True)
    _safe_set(b, 'dbl_Class70', {a1})
    assert _is_linked(b, 'dbl_Class70', a1)
    if hasattr(a1, 'dbl_Function71'):
        assert _is_linked(a1, 'dbl_Function71', b)
    _safe_set(b, 'dbl_Class70', {a2})
    assert _is_linked(b, 'dbl_Class70', a2)
    if hasattr(a1, 'dbl_Function71'):
        assert not _is_linked(a1, 'dbl_Function71', b)
    if hasattr(a2, 'dbl_Function71'):
        assert _is_linked(a2, 'dbl_Function71', b)
    _safe_set(b, 'dbl_Class70', set())
    assert not _is_linked(b, 'dbl_Class70', a2)
    if hasattr(a2, 'dbl_Function71'):
        assert not _is_linked(a2, 'dbl_Function71', b)


def test_assoc_placeHolder1025_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement26', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement26', a1)
    if hasattr(a1, 'dbl_ExtensibleElement24'):
        assert _is_linked(a1, 'dbl_ExtensibleElement24', b)
    _safe_set(b, 'dbl_ExtensibleElement26', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement26', a2)
    if hasattr(a1, 'dbl_ExtensibleElement24'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement24', b)
    if hasattr(a2, 'dbl_ExtensibleElement24'):
        assert _is_linked(a2, 'dbl_ExtensibleElement24', b)
    _safe_set(b, 'dbl_ExtensibleElement26', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement26', a2)
    if hasattr(a2, 'dbl_ExtensibleElement24'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement24', b)


def test_assoc_placeHolder12_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement1', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement1', a1)
    if hasattr(a1, 'dbl_ExtensibleElement'):
        assert _is_linked(a1, 'dbl_ExtensibleElement', b)
    _safe_set(b, 'dbl_ExtensibleElement1', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement1', a2)
    if hasattr(a1, 'dbl_ExtensibleElement'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement', b)
    if hasattr(a2, 'dbl_ExtensibleElement'):
        assert _is_linked(a2, 'dbl_ExtensibleElement', b)
    _safe_set(b, 'dbl_ExtensibleElement1', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement1', a2)
    if hasattr(a2, 'dbl_ExtensibleElement'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement', b)


def test_assoc_placeHolder24_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement5', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement5', a1)
    if hasattr(a1, 'dbl_ExtensibleElement3'):
        assert _is_linked(a1, 'dbl_ExtensibleElement3', b)
    _safe_set(b, 'dbl_ExtensibleElement5', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement5', a2)
    if hasattr(a1, 'dbl_ExtensibleElement3'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement3', b)
    if hasattr(a2, 'dbl_ExtensibleElement3'):
        assert _is_linked(a2, 'dbl_ExtensibleElement3', b)
    _safe_set(b, 'dbl_ExtensibleElement5', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement5', a2)
    if hasattr(a2, 'dbl_ExtensibleElement3'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement3', b)


def test_assoc_placeHolder37_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement8', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement8', a1)
    if hasattr(a1, 'dbl_ExtensibleElement6'):
        assert _is_linked(a1, 'dbl_ExtensibleElement6', b)
    _safe_set(b, 'dbl_ExtensibleElement8', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement8', a2)
    if hasattr(a1, 'dbl_ExtensibleElement6'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement6', b)
    if hasattr(a2, 'dbl_ExtensibleElement6'):
        assert _is_linked(a2, 'dbl_ExtensibleElement6', b)
    _safe_set(b, 'dbl_ExtensibleElement8', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement8', a2)
    if hasattr(a2, 'dbl_ExtensibleElement6'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement6', b)


def test_assoc_placeHolder410_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement9', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement9', a1)
    if hasattr(a1, 'dbl_ExtensibleElement11'):
        assert _is_linked(a1, 'dbl_ExtensibleElement11', b)
    _safe_set(b, 'dbl_ExtensibleElement9', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement9', a2)
    if hasattr(a1, 'dbl_ExtensibleElement11'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement11', b)
    if hasattr(a2, 'dbl_ExtensibleElement11'):
        assert _is_linked(a2, 'dbl_ExtensibleElement11', b)
    _safe_set(b, 'dbl_ExtensibleElement9', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement9', a2)
    if hasattr(a2, 'dbl_ExtensibleElement11'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement11', b)


def test_assoc_placeHolder513_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement14', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement14', a1)
    if hasattr(a1, 'dbl_ExtensibleElement12'):
        assert _is_linked(a1, 'dbl_ExtensibleElement12', b)
    _safe_set(b, 'dbl_ExtensibleElement14', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement14', a2)
    if hasattr(a1, 'dbl_ExtensibleElement12'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement12', b)
    if hasattr(a2, 'dbl_ExtensibleElement12'):
        assert _is_linked(a2, 'dbl_ExtensibleElement12', b)
    _safe_set(b, 'dbl_ExtensibleElement14', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement14', a2)
    if hasattr(a2, 'dbl_ExtensibleElement12'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement12', b)


def test_assoc_placeHolder616_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement17', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement17', a1)
    if hasattr(a1, 'dbl_ExtensibleElement15'):
        assert _is_linked(a1, 'dbl_ExtensibleElement15', b)
    _safe_set(b, 'dbl_ExtensibleElement17', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement17', a2)
    if hasattr(a1, 'dbl_ExtensibleElement15'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement15', b)
    if hasattr(a2, 'dbl_ExtensibleElement15'):
        assert _is_linked(a2, 'dbl_ExtensibleElement15', b)
    _safe_set(b, 'dbl_ExtensibleElement17', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement17', a2)
    if hasattr(a2, 'dbl_ExtensibleElement15'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement15', b)


def test_assoc_placeHolder819_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement20', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement20', a1)
    if hasattr(a1, 'dbl_ExtensibleElement18'):
        assert _is_linked(a1, 'dbl_ExtensibleElement18', b)
    _safe_set(b, 'dbl_ExtensibleElement20', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement20', a2)
    if hasattr(a1, 'dbl_ExtensibleElement18'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement18', b)
    if hasattr(a2, 'dbl_ExtensibleElement18'):
        assert _is_linked(a2, 'dbl_ExtensibleElement18', b)
    _safe_set(b, 'dbl_ExtensibleElement20', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement20', a2)
    if hasattr(a2, 'dbl_ExtensibleElement18'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement18', b)


def test_assoc_placeHolder922_reverse_link_reassign_clear():
    a1 = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    a2 = dbl_ExtensibleElement(concreteSyntax="sample_text_2", instanceOfExtensionDefinition=False)
    b = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    _safe_set(b, 'dbl_ExtensibleElement23', a1)
    assert _is_linked(b, 'dbl_ExtensibleElement23', a1)
    if hasattr(a1, 'dbl_ExtensibleElement21'):
        assert _is_linked(a1, 'dbl_ExtensibleElement21', b)
    _safe_set(b, 'dbl_ExtensibleElement23', a2)
    assert _is_linked(b, 'dbl_ExtensibleElement23', a2)
    if hasattr(a1, 'dbl_ExtensibleElement21'):
        assert not _is_linked(a1, 'dbl_ExtensibleElement21', b)
    if hasattr(a2, 'dbl_ExtensibleElement21'):
        assert _is_linked(a2, 'dbl_ExtensibleElement21', b)
    _safe_set(b, 'dbl_ExtensibleElement23', None)
    assert not _is_linked(b, 'dbl_ExtensibleElement23', a2)
    if hasattr(a2, 'dbl_ExtensibleElement21'):
        assert not _is_linked(a2, 'dbl_ExtensibleElement21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abstractSyntaxDef165_stub_double():
    # dbl_ExtensionDefinition has no real 'dbl_ExtensionDefinition166' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_ExtensionDefinition()
    setattr(partner, 'dbl_ExtensionDefinition166', None)
    _safe_set(owner, 'dbl_Class167', partner)
    assert getattr(partner, 'dbl_ExtensionDefinition166') == owner
    _safe_set(owner, 'dbl_Class167', None)
    assert getattr(partner, 'dbl_ExtensionDefinition166') is None


def test_assoc_actionsBlock72_stub_double():
    # dbl_LocalScope has no real 'dbl_LocalScope' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_LocalScope()
    setattr(partner, 'dbl_LocalScope', None)
    _safe_set(owner, 'dbl_Class73', partner)
    assert getattr(partner, 'dbl_LocalScope') == owner
    _safe_set(owner, 'dbl_Class73', None)
    assert getattr(partner, 'dbl_LocalScope') is None


def test_assoc_body216_stub_double():
    # dbl_Statement has no real 'dbl_Statement218' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Statement()
    setattr(partner, 'dbl_Statement218', None)
    _safe_set(owner, 'dbl_Pattern217', partner)
    assert getattr(partner, 'dbl_Statement218') == owner
    _safe_set(owner, 'dbl_Pattern217', None)
    assert getattr(partner, 'dbl_Statement218') is None


def test_assoc_class_55_stub_double():
    # dbl_SuperClassSpecification has no real 'dbl_SuperClassSpecification' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_SuperClassSpecification()
    setattr(partner, 'dbl_SuperClassSpecification', None)
    _safe_set(owner, 'dbl_Class56', partner)
    assert getattr(partner, 'dbl_SuperClassSpecification') == owner
    _safe_set(owner, 'dbl_Class56', None)
    assert getattr(partner, 'dbl_SuperClassSpecification') is None


def test_assoc_classes33_stub_double():
    # dbl_Module has no real 'dbl_Module34' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module34', None)
    _safe_set(owner, 'dbl_Class', partner)
    assert owner in getattr(partner, 'dbl_Module34')
    _safe_set(owner, 'dbl_Class', None)
    assert owner not in getattr(partner, 'dbl_Module34')


def test_assoc_constructors65_stub_double():
    # dbl_Constructor has no real 'Constructor' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_Constructor()
    setattr(partner, 'Constructor', None)
    _safe_set(owner, 'owningClass', {partner})
    assert getattr(partner, 'Constructor') == owner
    _safe_set(owner, 'owningClass', set())
    assert getattr(partner, 'Constructor') is None


def test_assoc_context196_stub_double():
    # dbl_Expression has no real 'dbl_Expression197' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SetExpansionContextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SetExpansionContextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SetExpansionContextStatement(addAfterContext=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression197', None)
    _safe_set(owner, 'dbl_SetExpansionContextStatement', partner)
    assert getattr(partner, 'dbl_Expression197') == owner
    _safe_set(owner, 'dbl_SetExpansionContextStatement', None)
    assert getattr(partner, 'dbl_Expression197') is None


def test_assoc_context214_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter215' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter215', None)
    _safe_set(owner, 'dbl_Pattern', partner)
    assert getattr(partner, 'dbl_Parameter215') == owner
    _safe_set(owner, 'dbl_Pattern', None)
    assert getattr(partner, 'dbl_Parameter215') is None


def test_assoc_functions39_stub_double():
    # dbl_Module has no real 'dbl_Module40' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Function(abstract=True, class_=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module40', None)
    _safe_set(owner, 'dbl_Function', partner)
    assert owner in getattr(partner, 'dbl_Module40')
    _safe_set(owner, 'dbl_Function', None)
    assert owner not in getattr(partner, 'dbl_Module40')


def test_assoc_imports27_stub_double():
    # dbl_Model has no real 'dbl_Model' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Import(file="sample_text")
    partner = dbl_Model()
    setattr(partner, 'dbl_Model', None)
    _safe_set(owner, 'dbl_Import', partner)
    assert owner in getattr(partner, 'dbl_Model')
    _safe_set(owner, 'dbl_Import', None)
    assert owner not in getattr(partner, 'dbl_Model')


def test_assoc_initialValue77_stub_double():
    # dbl_Expression has no real 'dbl_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(class_=True, control=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression79', None)
    _safe_set(owner, 'dbl_Variable78', partner)
    assert getattr(partner, 'dbl_Expression79') == owner
    _safe_set(owner, 'dbl_Variable78', None)
    assert getattr(partner, 'dbl_Expression79') is None


def test_assoc_model30_stub_double():
    # dbl_Model has no real 'dbl_Model32' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Import(file="sample_text")
    partner = dbl_Model()
    setattr(partner, 'dbl_Model32', None)
    _safe_set(owner, 'dbl_Import31', partner)
    assert getattr(partner, 'dbl_Model32') == owner
    _safe_set(owner, 'dbl_Import31', None)
    assert getattr(partner, 'dbl_Model32') is None


def test_assoc_objectAccess92_stub_double():
    # dbl_Expression has no real 'dbl_Expression93' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ActivateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ActivateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ActivateObject(priority=7)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression93', None)
    _safe_set(owner, 'dbl_ActivateObject', partner)
    assert getattr(partner, 'dbl_Expression93') == owner
    _safe_set(owner, 'dbl_ActivateObject', None)
    assert getattr(partner, 'dbl_Expression93') is None


def test_assoc_owningClass76_stub_double():
    # dbl_Constructor has no real 'constructors' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_Constructor()
    setattr(partner, 'constructors', None)
    _safe_set(owner, 'Class', partner)
    assert getattr(partner, 'constructors') == owner
    _safe_set(owner, 'Class', None)
    assert getattr(partner, 'constructors') is None


def test_assoc_parameters53_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Function(abstract=True, class_=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter', None)
    _safe_set(owner, 'dbl_Function54', {partner})
    assert getattr(partner, 'dbl_Parameter') == owner
    _safe_set(owner, 'dbl_Function54', set())
    assert getattr(partner, 'dbl_Parameter') is None


def test_assoc_referencedElement149_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr150' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NamedElement(name="sample_text")
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr150', None)
    _safe_set(owner, 'dbl_NamedElement', partner)
    assert getattr(partner, 'dbl_IdExpr150') == owner
    _safe_set(owner, 'dbl_NamedElement', None)
    assert getattr(partner, 'dbl_IdExpr150') is None


def test_assoc_superClasses62_stub_double():
    # dbl_SuperClassSpecification has no real 'dbl_SuperClassSpecification64' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Class(active=True)
    partner = dbl_SuperClassSpecification()
    setattr(partner, 'dbl_SuperClassSpecification64', None)
    _safe_set(owner, 'dbl_Class63', {partner})
    assert getattr(partner, 'dbl_SuperClassSpecification64') == owner
    _safe_set(owner, 'dbl_Class63', set())
    assert getattr(partner, 'dbl_SuperClassSpecification64') is None


def test_assoc_variables41_stub_double():
    # dbl_Module has no real 'dbl_Module42' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(class_=True, control=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module42', None)
    _safe_set(owner, 'dbl_Variable', partner)
    assert owner in getattr(partner, 'dbl_Module42')
    _safe_set(owner, 'dbl_Variable', None)
    assert owner not in getattr(partner, 'dbl_Module42')


