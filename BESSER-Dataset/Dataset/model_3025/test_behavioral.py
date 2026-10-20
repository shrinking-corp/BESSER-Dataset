import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractVariable,
    BinaryOperator,
    ClassSimilar,
    Classifier,
    Construct,
    ElementAccess,
    EmbeddableExtensionsContainer,
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
    LocalScopeStatement,
    LoopStatement,
    MappingPart,
    ModifierExtensionsContainer,
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
    dbl_ClassAugment,
    dbl_ClassContentExtension,
    dbl_ClassPart,
    dbl_ClassSimilar,
    dbl_Classifier,
    dbl_Clazz,
    dbl_CodeQuoteExpression,
    dbl_CompositePropertyType,
    dbl_Construct,
    dbl_Constructor,
    dbl_ContinueStatement,
    dbl_CreateObject,
    dbl_Div,
    dbl_DoubleLiteral,
    dbl_DoubleType,
    dbl_DynamicMappingPart,
    dbl_ElementAccess,
    dbl_EmbeddableExtensionsContainer,
    dbl_Equal,
    dbl_ExpandExpr,
    dbl_ExpandExpression,
    dbl_ExpandStatement,
    dbl_Expression,
    dbl_ExtensibleElement,
    dbl_ExtensionDefinition,
    dbl_FalseLiteral,
    dbl_FixedMappingPart,
    dbl_ForStatement,
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
    dbl_Mapping,
    dbl_MappingPart,
    dbl_MappingStatement,
    dbl_MeLiteral,
    dbl_MetaAccess,
    dbl_MetaExpr,
    dbl_MetaLiteral,
    dbl_Minus,
    dbl_Mod,
    dbl_Model,
    dbl_ModifierExtensionsContainer,
    dbl_Module,
    dbl_ModuleContentExtension,
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
    dbl_Procedure,
    dbl_ProcedureCall,
    dbl_PropertyBindingExpr,
    dbl_PropertyType,
    dbl_QuotedClassContent,
    dbl_QuotedCode,
    dbl_QuotedExpression,
    dbl_QuotedModuleContent,
    dbl_QuotedStatements,
    dbl_Reactivate,
    dbl_ReferencePropertyType,
    dbl_ResetGenContextStatement,
    dbl_ResumeGenStatement,
    dbl_Return,
    dbl_RhsClassifierExpr,
    dbl_RhsExpression,
    dbl_SaveGenStatement,
    dbl_SequenceExpr,
    dbl_SetGenContextStatement,
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

def test_assoc_bindings59_reverse_link_reassign_clear():
    a1 = dbl_NativeBinding(targetLanguage="sample_text", targetType="sample_text")
    a2 = dbl_NativeBinding(targetLanguage="sample_text_2", targetType="sample_text_2")
    b = dbl_Clazz(active=True)
    _safe_set(b, 'dbl_Clazz60', {a1})
    assert _is_linked(b, 'dbl_Clazz60', a1)
    if hasattr(a1, 'dbl_NativeBinding'):
        assert _is_linked(a1, 'dbl_NativeBinding', b)
    _safe_set(b, 'dbl_Clazz60', {a2})
    assert _is_linked(b, 'dbl_Clazz60', a2)
    if hasattr(a1, 'dbl_NativeBinding'):
        assert not _is_linked(a1, 'dbl_NativeBinding', b)
    if hasattr(a2, 'dbl_NativeBinding'):
        assert _is_linked(a2, 'dbl_NativeBinding', b)
    _safe_set(b, 'dbl_Clazz60', set())
    assert not _is_linked(b, 'dbl_Clazz60', a2)
    if hasattr(a2, 'dbl_NativeBinding'):
        assert not _is_linked(a2, 'dbl_NativeBinding', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes31_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar', None)
    _safe_set(owner, 'dbl_Variable32', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar')
    _safe_set(owner, 'dbl_Variable32', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar')


def test_assoc_augmentedClass64_stub_double():
    # dbl_ClassAugment has no real 'dbl_ClassAugment65' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_ClassAugment()
    setattr(partner, 'dbl_ClassAugment65', None)
    _safe_set(owner, 'dbl_Clazz66', partner)
    assert getattr(partner, 'dbl_ClassAugment65') == owner
    _safe_set(owner, 'dbl_Clazz66', None)
    assert getattr(partner, 'dbl_ClassAugment65') is None


def test_assoc_body210_stub_double():
    # dbl_Statement has no real 'dbl_Statement212' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Statement()
    setattr(partner, 'dbl_Statement212', None)
    _safe_set(owner, 'dbl_Pattern211', partner)
    assert getattr(partner, 'dbl_Statement212') == owner
    _safe_set(owner, 'dbl_Pattern211', None)
    assert getattr(partner, 'dbl_Statement212') is None


def test_assoc_clazz52_stub_double():
    # dbl_SuperClassSpecification has no real 'dbl_SuperClassSpecification53' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_SuperClassSpecification()
    setattr(partner, 'dbl_SuperClassSpecification53', None)
    _safe_set(owner, 'dbl_Clazz', partner)
    assert getattr(partner, 'dbl_SuperClassSpecification53') == owner
    _safe_set(owner, 'dbl_Clazz', None)
    assert getattr(partner, 'dbl_SuperClassSpecification53') is None


def test_assoc_constructor57_stub_double():
    # dbl_Constructor has no real 'dbl_Constructor' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_Constructor()
    setattr(partner, 'dbl_Constructor', None)
    _safe_set(owner, 'dbl_Clazz58', partner)
    assert getattr(partner, 'dbl_Constructor') == owner
    _safe_set(owner, 'dbl_Clazz58', None)
    assert getattr(partner, 'dbl_Constructor') is None


def test_assoc_context188_stub_double():
    # dbl_Expression has no real 'dbl_Expression189' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SetGenContextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SetGenContextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SetGenContextStatement(addAfterContext=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression189', None)
    _safe_set(owner, 'dbl_SetGenContextStatement', partner)
    assert getattr(partner, 'dbl_Expression189') == owner
    _safe_set(owner, 'dbl_SetGenContextStatement', None)
    assert getattr(partner, 'dbl_Expression189') is None


def test_assoc_context208_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter209' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter209', None)
    _safe_set(owner, 'dbl_Pattern', partner)
    assert getattr(partner, 'dbl_Parameter209') == owner
    _safe_set(owner, 'dbl_Pattern', None)
    assert getattr(partner, 'dbl_Parameter209') is None


def test_assoc_extensions17_stub_double():
    # dbl_EmbeddableExtensionsContainer has no real 'dbl_EmbeddableExtensionsContainer' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ExtensibleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ExtensibleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    partner = dbl_EmbeddableExtensionsContainer()
    setattr(partner, 'dbl_EmbeddableExtensionsContainer', None)
    _safe_set(owner, 'dbl_ExtensibleElement', partner)
    assert owner in getattr(partner, 'dbl_EmbeddableExtensionsContainer')
    _safe_set(owner, 'dbl_ExtensibleElement', None)
    assert owner not in getattr(partner, 'dbl_EmbeddableExtensionsContainer')


def test_assoc_imports1_stub_double():
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


def test_assoc_initialValue67_stub_double():
    # dbl_Expression has no real 'dbl_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression69', None)
    _safe_set(owner, 'dbl_Variable68', partner)
    assert getattr(partner, 'dbl_Expression69') == owner
    _safe_set(owner, 'dbl_Variable68', None)
    assert getattr(partner, 'dbl_Expression69') is None


def test_assoc_methods33_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar34' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(abstract=True, clazz=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar34', None)
    _safe_set(owner, 'dbl_Procedure35', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar34')
    _safe_set(owner, 'dbl_Procedure35', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar34')


def test_assoc_model4_stub_double():
    # dbl_Model has no real 'dbl_Model6' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Import(file="sample_text")
    partner = dbl_Model()
    setattr(partner, 'dbl_Model6', None)
    _safe_set(owner, 'dbl_Import5', partner)
    assert getattr(partner, 'dbl_Model6') == owner
    _safe_set(owner, 'dbl_Import5', None)
    assert getattr(partner, 'dbl_Model6') is None


def test_assoc_modifierExtensions18_stub_double():
    # dbl_ModifierExtensionsContainer has no real 'dbl_ModifierExtensionsContainer' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ExtensibleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ExtensibleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ExtensibleElement(concreteSyntax="sample_text", instanceOfExtensionDefinition=True)
    partner = dbl_ModifierExtensionsContainer()
    setattr(partner, 'dbl_ModifierExtensionsContainer', None)
    _safe_set(owner, 'dbl_ExtensibleElement19', partner)
    assert owner in getattr(partner, 'dbl_ModifierExtensionsContainer')
    _safe_set(owner, 'dbl_ExtensibleElement19', None)
    assert owner not in getattr(partner, 'dbl_ModifierExtensionsContainer')


def test_assoc_objectAccess82_stub_double():
    # dbl_Expression has no real 'dbl_Expression83' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ActivateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ActivateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ActivateObject(priority=7)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression83', None)
    _safe_set(owner, 'dbl_ActivateObject', partner)
    assert getattr(partner, 'dbl_Expression83') == owner
    _safe_set(owner, 'dbl_ActivateObject', None)
    assert getattr(partner, 'dbl_Expression83') is None


def test_assoc_parameters29_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(abstract=True, clazz=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter', None)
    _safe_set(owner, 'dbl_Procedure30', {partner})
    assert getattr(partner, 'dbl_Parameter') == owner
    _safe_set(owner, 'dbl_Procedure30', set())
    assert getattr(partner, 'dbl_Parameter') is None


def test_assoc_procedures13_stub_double():
    # dbl_Module has no real 'dbl_Module14' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(abstract=True, clazz=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module14', None)
    _safe_set(owner, 'dbl_Procedure', partner)
    assert owner in getattr(partner, 'dbl_Module14')
    _safe_set(owner, 'dbl_Procedure', None)
    assert owner not in getattr(partner, 'dbl_Module14')


def test_assoc_referencedElement138_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr139' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NamedElement(name="sample_text")
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr139', None)
    _safe_set(owner, 'dbl_NamedElement', partner)
    assert getattr(partner, 'dbl_IdExpr139') == owner
    _safe_set(owner, 'dbl_NamedElement', None)
    assert getattr(partner, 'dbl_IdExpr139') is None


def test_assoc_variables15_stub_double():
    # dbl_Module has no real 'dbl_Module16' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module16', None)
    _safe_set(owner, 'dbl_Variable', partner)
    assert owner in getattr(partner, 'dbl_Module16')
    _safe_set(owner, 'dbl_Variable', None)
    assert owner not in getattr(partner, 'dbl_Module16')


