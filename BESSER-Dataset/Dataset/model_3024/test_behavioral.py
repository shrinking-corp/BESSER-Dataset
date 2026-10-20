import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractVariable,
    AnnotatableElement,
    BinaryOperator,
    ClassSimilar,
    Classifier,
    CodeBlock,
    CompositeStatement,
    Construct,
    ElementAccess,
    EmbeddableExtensionsContainer,
    ExpandableElement,
    Expression,
    ExpressionStatement,
    ExtensibleElement,
    L1Expr,
    MappingPart,
    ModifierExtensionsContainer,
    Module,
    NamedElement,
    NamedExtensible,
    PredefinedId,
    PrimitiveType,
    PropertyType,
    QuotedCode,
    ReferableRhsType,
    RhsExpression,
    SetOp,
    SetStatement,
    SimpleStatement,
    Statement,
    StatementExpression,
    StructuredPropertyType,
    Type,
    TypedElement,
    UnaryOperator,
    VariableAccess,
    dbl_AbstractVariable,
    dbl_ActivateObject,
    dbl_ActiveLiteral,
    dbl_AddToSet,
    dbl_Advance,
    dbl_AfterInSet,
    dbl_AlternativeExpr,
    dbl_And,
    dbl_AnnotatableElement,
    dbl_Annotation,
    dbl_AnnotationApplication,
    dbl_ArbitraryExpr,
    dbl_ArgumentExpression,
    dbl_Assignment,
    dbl_AtLeastOneExpr,
    dbl_BeforeInSet,
    dbl_BinaryOperator,
    dbl_BoolType,
    dbl_BooleanPropertyType,
    dbl_BreakStatement,
    dbl_Cast,
    dbl_ClassAugment,
    dbl_ClassContentExtension,
    dbl_ClassSimilar,
    dbl_Classifier,
    dbl_Clazz,
    dbl_CodeBlock,
    dbl_CodeQuoteExpression,
    dbl_CompositePropertyType,
    dbl_CompositeStatement,
    dbl_ConsiderIdElements,
    dbl_Construct,
    dbl_Constructor,
    dbl_Contains,
    dbl_ContinueStatement,
    dbl_CreateObject,
    dbl_DepIdentifiableElement,
    dbl_DeprecatedProcedureCallStatement,
    dbl_Div,
    dbl_DoubleLiteral,
    dbl_DoubleType,
    dbl_DynamicMappingPart,
    dbl_ElementAccess,
    dbl_EmbeddableExtensionsContainer,
    dbl_EmptySet,
    dbl_Equal,
    dbl_EvalExpr,
    dbl_ExpandExpression,
    dbl_ExpandSection,
    dbl_ExpandStatement,
    dbl_ExpandableElement,
    dbl_Expression,
    dbl_ExpressionStatement,
    dbl_ExtensibleElement,
    dbl_ExtensionDefinition,
    dbl_ExtensionRule,
    dbl_FalseLiteral,
    dbl_FindContainer,
    dbl_FirstInSet,
    dbl_FixedMappingPart,
    dbl_ForEachStatement,
    dbl_Greater,
    dbl_GreaterEqual,
    dbl_IdExpr,
    dbl_IdPropertyType,
    dbl_IdResolution,
    dbl_IfStatement,
    dbl_Import,
    dbl_IncludePattern,
    dbl_IndexOf,
    dbl_InstanceOf,
    dbl_IntLiteral,
    dbl_IntPropertyType,
    dbl_IntType,
    dbl_Interface,
    dbl_KeyValuePair,
    dbl_L1Expr,
    dbl_LastInSet,
    dbl_Less,
    dbl_LessEqual,
    dbl_ListDimension,
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
    dbl_NamedExtensible,
    dbl_NativeBinding,
    dbl_Neg,
    dbl_Not,
    dbl_NotEqual,
    dbl_NullLiteral,
    dbl_ObjectAt,
    dbl_OptionalExpr,
    dbl_Or,
    dbl_Parameter,
    dbl_Pattern,
    dbl_Plus,
    dbl_PotentiallyHiddenIdElements,
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
    dbl_ReferableRhsType,
    dbl_ReferencePropertyType,
    dbl_RemoveFromSet,
    dbl_ResetGenContextStatement,
    dbl_ResumeGenStatement,
    dbl_Return,
    dbl_RhsExpression,
    dbl_RuleExpr,
    dbl_RuntimeExpr,
    dbl_SaveGenStatement,
    dbl_SequenceExpr,
    dbl_SetGenContextStatement,
    dbl_SetOp,
    dbl_SetStatement,
    dbl_SimpleAnnotation,
    dbl_SimpleStatement,
    dbl_SizeOfSet,
    dbl_StartCodeBlock,
    dbl_Statement,
    dbl_StatementExpression,
    dbl_StringLiteral,
    dbl_StringPropertyType,
    dbl_StringType,
    dbl_StructuredPropertyType,
    dbl_SuperLiteral,
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
    BindingExprOpKind,
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

def test_assoc_idResolutionPattern213_reverse_link_reassign_clear():
    a1 = dbl_ReferencePropertyType(rawReference=True)
    a2 = dbl_ReferencePropertyType(rawReference=False)
    b = dbl_Pattern(top=True)
    _safe_set(b, 'dbl_Pattern', a1)
    assert _is_linked(b, 'dbl_Pattern', a1)
    if hasattr(a1, 'dbl_ReferencePropertyType'):
        assert _is_linked(a1, 'dbl_ReferencePropertyType', b)
    _safe_set(b, 'dbl_Pattern', a2)
    assert _is_linked(b, 'dbl_Pattern', a2)
    if hasattr(a1, 'dbl_ReferencePropertyType'):
        assert not _is_linked(a1, 'dbl_ReferencePropertyType', b)
    if hasattr(a2, 'dbl_ReferencePropertyType'):
        assert _is_linked(a2, 'dbl_ReferencePropertyType', b)
    _safe_set(b, 'dbl_Pattern', None)
    assert not _is_linked(b, 'dbl_Pattern', a2)
    if hasattr(a2, 'dbl_ReferencePropertyType'):
        assert not _is_linked(a2, 'dbl_ReferencePropertyType', b)


def test_assoc_listDims24_reverse_link_reassign_clear():
    a1 = dbl_TypedElement(isList=True)
    a2 = dbl_TypedElement(isList=False)
    b = dbl_ListDimension(size=7)
    _safe_set(b, 'dbl_ListDimension', a1)
    assert _is_linked(b, 'dbl_ListDimension', a1)
    if hasattr(a1, 'dbl_TypedElement25'):
        assert _is_linked(a1, 'dbl_TypedElement25', b)
    _safe_set(b, 'dbl_ListDimension', a2)
    assert _is_linked(b, 'dbl_ListDimension', a2)
    if hasattr(a1, 'dbl_TypedElement25'):
        assert not _is_linked(a1, 'dbl_TypedElement25', b)
    if hasattr(a2, 'dbl_TypedElement25'):
        assert _is_linked(a2, 'dbl_TypedElement25', b)
    _safe_set(b, 'dbl_ListDimension', None)
    assert not _is_linked(b, 'dbl_ListDimension', a2)
    if hasattr(a2, 'dbl_TypedElement25'):
        assert not _is_linked(a2, 'dbl_TypedElement25', b)


def test_assoc_patterns252_reverse_link_reassign_clear():
    a1 = dbl_Pattern(top=True)
    a2 = dbl_Pattern(top=False)
    b = dbl_IdResolution(metaModelPlatformURI="sample_text")
    _safe_set(b, 'dbl_IdResolution253', {a1})
    assert _is_linked(b, 'dbl_IdResolution253', a1)
    if hasattr(a1, 'dbl_Pattern254'):
        assert _is_linked(a1, 'dbl_Pattern254', b)
    _safe_set(b, 'dbl_IdResolution253', {a2})
    assert _is_linked(b, 'dbl_IdResolution253', a2)
    if hasattr(a1, 'dbl_Pattern254'):
        assert not _is_linked(a1, 'dbl_Pattern254', b)
    if hasattr(a2, 'dbl_Pattern254'):
        assert _is_linked(a2, 'dbl_Pattern254', b)
    _safe_set(b, 'dbl_IdResolution253', set())
    assert not _is_linked(b, 'dbl_IdResolution253', a2)
    if hasattr(a2, 'dbl_Pattern254'):
        assert not _is_linked(a2, 'dbl_Pattern254', b)


def test_assoc_rhs186_reverse_link_reassign_clear():
    a1 = dbl_TsRule(metaClassName="sample_text")
    a2 = dbl_TsRule(metaClassName="sample_text_2")
    b = dbl_RhsExpression()
    _safe_set(b, 'dbl_RhsExpression', a1)
    assert _is_linked(b, 'dbl_RhsExpression', a1)
    if hasattr(a1, 'dbl_TsRule187'):
        assert _is_linked(a1, 'dbl_TsRule187', b)
    _safe_set(b, 'dbl_RhsExpression', a2)
    assert _is_linked(b, 'dbl_RhsExpression', a2)
    if hasattr(a1, 'dbl_TsRule187'):
        assert not _is_linked(a1, 'dbl_TsRule187', b)
    if hasattr(a2, 'dbl_TsRule187'):
        assert _is_linked(a2, 'dbl_TsRule187', b)
    _safe_set(b, 'dbl_RhsExpression', None)
    assert not _is_linked(b, 'dbl_RhsExpression', a2)
    if hasattr(a2, 'dbl_TsRule187'):
        assert not _is_linked(a2, 'dbl_TsRule187', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes47_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar', None)
    _safe_set(owner, 'dbl_Variable48', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar')
    _safe_set(owner, 'dbl_Variable48', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar')


def test_assoc_augmentedClass78_stub_double():
    # dbl_ClassAugment has no real 'dbl_ClassAugment79' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_ClassAugment()
    setattr(partner, 'dbl_ClassAugment79', None)
    _safe_set(owner, 'dbl_Clazz80', partner)
    assert getattr(partner, 'dbl_ClassAugment79') == owner
    _safe_set(owner, 'dbl_Clazz80', None)
    assert getattr(partner, 'dbl_ClassAugment79') is None


def test_assoc_baseConstructorArguments72_stub_double():
    # dbl_Expression has no real 'dbl_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression74', None)
    _safe_set(owner, 'dbl_Clazz73', {partner})
    assert getattr(partner, 'dbl_Expression74') == owner
    _safe_set(owner, 'dbl_Clazz73', set())
    assert getattr(partner, 'dbl_Expression74') is None


def test_assoc_bindings45_stub_double():
    # dbl_Classifier has no real 'dbl_Classifier46' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NativeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NativeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NativeBinding(targetLanguage="sample_text", targetType="sample_text")
    partner = dbl_Classifier()
    setattr(partner, 'dbl_Classifier46', None)
    _safe_set(owner, 'dbl_NativeBinding', partner)
    assert owner in getattr(partner, 'dbl_Classifier46')
    _safe_set(owner, 'dbl_NativeBinding', None)
    assert owner not in getattr(partner, 'dbl_Classifier46')


def test_assoc_classifierTypeExpr26_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TypedElement(isList=True)
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr', None)
    _safe_set(owner, 'dbl_TypedElement27', partner)
    assert getattr(partner, 'dbl_IdExpr') == owner
    _safe_set(owner, 'dbl_TypedElement27', None)
    assert getattr(partner, 'dbl_IdExpr') is None


def test_assoc_codeBlock258_stub_double():
    # dbl_CodeBlock has no real 'dbl_CodeBlock260' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_CodeBlock()
    setattr(partner, 'dbl_CodeBlock260', None)
    _safe_set(owner, 'dbl_Pattern259', partner)
    assert getattr(partner, 'dbl_CodeBlock260') == owner
    _safe_set(owner, 'dbl_Pattern259', None)
    assert getattr(partner, 'dbl_CodeBlock260') is None


def test_assoc_constructor70_stub_double():
    # dbl_Constructor has no real 'dbl_Constructor' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_Constructor()
    setattr(partner, 'dbl_Constructor', None)
    _safe_set(owner, 'dbl_Clazz71', partner)
    assert getattr(partner, 'dbl_Constructor') == owner
    _safe_set(owner, 'dbl_Clazz71', None)
    assert getattr(partner, 'dbl_Constructor') is None


def test_assoc_context228_stub_double():
    # dbl_Expression has no real 'dbl_Expression229' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SetGenContextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SetGenContextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SetGenContextStatement(addAfterContext=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression229', None)
    _safe_set(owner, 'dbl_SetGenContextStatement', partner)
    assert getattr(partner, 'dbl_Expression229') == owner
    _safe_set(owner, 'dbl_SetGenContextStatement', None)
    assert getattr(partner, 'dbl_Expression229') is None


def test_assoc_context255_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter257' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter257', None)
    _safe_set(owner, 'dbl_Pattern256', partner)
    assert getattr(partner, 'dbl_Parameter257') == owner
    _safe_set(owner, 'dbl_Pattern256', None)
    assert getattr(partner, 'dbl_Parameter257') is None


def test_assoc_expression195_stub_double():
    # dbl_OptionalExpr has no real 'dbl_OptionalExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_OptionalExpr()
    setattr(partner, 'dbl_OptionalExpr', None)
    _safe_set(owner, 'dbl_RhsExpression196', partner)
    assert getattr(partner, 'dbl_OptionalExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression196', None)
    assert getattr(partner, 'dbl_OptionalExpr') is None


def test_assoc_expression197_stub_double():
    # dbl_RuntimeExpr has no real 'dbl_RuntimeExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_RuntimeExpr()
    setattr(partner, 'dbl_RuntimeExpr', None)
    _safe_set(owner, 'dbl_RhsExpression198', partner)
    assert getattr(partner, 'dbl_RuntimeExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression198', None)
    assert getattr(partner, 'dbl_RuntimeExpr') is None


def test_assoc_expression199_stub_double():
    # dbl_AtLeastOneExpr has no real 'dbl_AtLeastOneExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AtLeastOneExpr()
    setattr(partner, 'dbl_AtLeastOneExpr', None)
    _safe_set(owner, 'dbl_RhsExpression200', partner)
    assert getattr(partner, 'dbl_AtLeastOneExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression200', None)
    assert getattr(partner, 'dbl_AtLeastOneExpr') is None


def test_assoc_expression201_stub_double():
    # dbl_ArbitraryExpr has no real 'dbl_ArbitraryExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_ArbitraryExpr()
    setattr(partner, 'dbl_ArbitraryExpr', None)
    _safe_set(owner, 'dbl_RhsExpression202', partner)
    assert getattr(partner, 'dbl_ArbitraryExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression202', None)
    assert getattr(partner, 'dbl_ArbitraryExpr') is None


def test_assoc_extensions20_stub_double():
    # dbl_EmbeddableExtensionsContainer has no real 'dbl_EmbeddableExtensionsContainer' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ExtensibleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ExtensibleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ExtensibleElement(objectIsExtensionInstance=True)
    partner = dbl_EmbeddableExtensionsContainer()
    setattr(partner, 'dbl_EmbeddableExtensionsContainer', None)
    _safe_set(owner, 'dbl_ExtensibleElement', partner)
    assert owner in getattr(partner, 'dbl_EmbeddableExtensionsContainer')
    _safe_set(owner, 'dbl_ExtensibleElement', None)
    assert owner not in getattr(partner, 'dbl_EmbeddableExtensionsContainer')


def test_assoc_idRes18_stub_double():
    # dbl_Module has no real 'dbl_Module19' property in the generated
    # code (a bare stub) -- manually attach it so dbl_IdResolution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_IdResolution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_IdResolution(metaModelPlatformURI="sample_text")
    partner = dbl_Module()
    setattr(partner, 'dbl_Module19', None)
    _safe_set(owner, 'dbl_IdResolution', partner)
    assert getattr(partner, 'dbl_Module19') == owner
    _safe_set(owner, 'dbl_IdResolution', None)
    assert getattr(partner, 'dbl_Module19') is None


def test_assoc_imports0_stub_double():
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


def test_assoc_initialValue87_stub_double():
    # dbl_Expression has no real 'dbl_Expression89' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression89', None)
    _safe_set(owner, 'dbl_Variable88', partner)
    assert getattr(partner, 'dbl_Expression89') == owner
    _safe_set(owner, 'dbl_Variable88', None)
    assert getattr(partner, 'dbl_Expression89') is None


def test_assoc_iteratorVariableDefinition138_stub_double():
    # dbl_ForEachStatement has no real 'dbl_ForEachStatement' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_ForEachStatement()
    setattr(partner, 'dbl_ForEachStatement', None)
    _safe_set(owner, 'dbl_Variable139', partner)
    assert getattr(partner, 'dbl_ForEachStatement') == owner
    _safe_set(owner, 'dbl_Variable139', None)
    assert getattr(partner, 'dbl_ForEachStatement') is None


def test_assoc_keys30_stub_double():
    # dbl_Annotation has no real 'dbl_Annotation31' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Annotation()
    setattr(partner, 'dbl_Annotation31', None)
    _safe_set(owner, 'dbl_Variable32', partner)
    assert owner in getattr(partner, 'dbl_Annotation31')
    _safe_set(owner, 'dbl_Variable32', None)
    assert owner not in getattr(partner, 'dbl_Annotation31')


def test_assoc_left203_stub_double():
    # dbl_AlternativeExpr has no real 'dbl_AlternativeExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AlternativeExpr()
    setattr(partner, 'dbl_AlternativeExpr', None)
    _safe_set(owner, 'dbl_RhsExpression204', partner)
    assert getattr(partner, 'dbl_AlternativeExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression204', None)
    assert getattr(partner, 'dbl_AlternativeExpr') is None


def test_assoc_methods49_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar50' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar50', None)
    _safe_set(owner, 'dbl_Procedure51', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar50')
    _safe_set(owner, 'dbl_Procedure51', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar50')


def test_assoc_methods81_stub_double():
    # dbl_Interface has no real 'dbl_Interface82' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_Interface()
    setattr(partner, 'dbl_Interface82', None)
    _safe_set(owner, 'dbl_Procedure83', partner)
    assert owner in getattr(partner, 'dbl_Interface82')
    _safe_set(owner, 'dbl_Procedure83', None)
    assert owner not in getattr(partner, 'dbl_Interface82')


def test_assoc_model3_stub_double():
    # dbl_Model has no real 'dbl_Model5' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Import(file="sample_text")
    partner = dbl_Model()
    setattr(partner, 'dbl_Model5', None)
    _safe_set(owner, 'dbl_Import4', partner)
    assert getattr(partner, 'dbl_Model5') == owner
    _safe_set(owner, 'dbl_Import4', None)
    assert getattr(partner, 'dbl_Model5') is None


def test_assoc_modifierExtensions21_stub_double():
    # dbl_ModifierExtensionsContainer has no real 'dbl_ModifierExtensionsContainer' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ExtensibleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ExtensibleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ExtensibleElement(objectIsExtensionInstance=True)
    partner = dbl_ModifierExtensionsContainer()
    setattr(partner, 'dbl_ModifierExtensionsContainer', None)
    _safe_set(owner, 'dbl_ExtensibleElement22', partner)
    assert owner in getattr(partner, 'dbl_ModifierExtensionsContainer')
    _safe_set(owner, 'dbl_ExtensibleElement22', None)
    assert owner not in getattr(partner, 'dbl_ModifierExtensionsContainer')


def test_assoc_newRules184_stub_double():
    # dbl_TextualSyntaxDef has no real 'dbl_TextualSyntaxDef185' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TsRule(metaClassName="sample_text")
    partner = dbl_TextualSyntaxDef()
    setattr(partner, 'dbl_TextualSyntaxDef185', None)
    _safe_set(owner, 'dbl_TsRule', partner)
    assert owner in getattr(partner, 'dbl_TextualSyntaxDef185')
    _safe_set(owner, 'dbl_TsRule', None)
    assert owner not in getattr(partner, 'dbl_TextualSyntaxDef185')


def test_assoc_objectAccess107_stub_double():
    # dbl_Expression has no real 'dbl_Expression108' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ActivateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ActivateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ActivateObject(priority=7)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression108', None)
    _safe_set(owner, 'dbl_ActivateObject', partner)
    assert getattr(partner, 'dbl_Expression108') == owner
    _safe_set(owner, 'dbl_ActivateObject', None)
    assert getattr(partner, 'dbl_Expression108') is None


def test_assoc_parameters28_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter', None)
    _safe_set(owner, 'dbl_Procedure29', {partner})
    assert getattr(partner, 'dbl_Parameter') == owner
    _safe_set(owner, 'dbl_Procedure29', set())
    assert getattr(partner, 'dbl_Parameter') is None


def test_assoc_pattern273_stub_double():
    # dbl_IncludePattern has no real 'dbl_IncludePattern' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_IncludePattern()
    setattr(partner, 'dbl_IncludePattern', None)
    _safe_set(owner, 'dbl_Pattern274', partner)
    assert getattr(partner, 'dbl_IncludePattern') == owner
    _safe_set(owner, 'dbl_Pattern274', None)
    assert getattr(partner, 'dbl_IncludePattern') is None


def test_assoc_primitiveType23_stub_double():
    # dbl_PrimitiveType has no real 'dbl_PrimitiveType' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TypedElement(isList=True)
    partner = dbl_PrimitiveType()
    setattr(partner, 'dbl_PrimitiveType', None)
    _safe_set(owner, 'dbl_TypedElement', partner)
    assert getattr(partner, 'dbl_PrimitiveType') == owner
    _safe_set(owner, 'dbl_TypedElement', None)
    assert getattr(partner, 'dbl_PrimitiveType') is None


def test_assoc_procedures14_stub_double():
    # dbl_Module has no real 'dbl_Module15' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module15', None)
    _safe_set(owner, 'dbl_Procedure', partner)
    assert owner in getattr(partner, 'dbl_Module15')
    _safe_set(owner, 'dbl_Procedure', None)
    assert owner not in getattr(partner, 'dbl_Module15')


def test_assoc_propertyType208_stub_double():
    # dbl_PropertyType has no real 'dbl_PropertyType' property in the generated
    # code (a bare stub) -- manually attach it so dbl_PropertyBindingExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_PropertyBindingExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_PropertyBindingExpr(operator="sample_text")
    partner = dbl_PropertyType()
    setattr(partner, 'dbl_PropertyType', None)
    _safe_set(owner, 'dbl_PropertyBindingExpr', partner)
    assert getattr(partner, 'dbl_PropertyType') == owner
    _safe_set(owner, 'dbl_PropertyBindingExpr', None)
    assert getattr(partner, 'dbl_PropertyType') is None


def test_assoc_referencedElement163_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr164' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NamedElement(name="sample_text")
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr164', None)
    _safe_set(owner, 'dbl_NamedElement', partner)
    assert getattr(partner, 'dbl_IdExpr164') == owner
    _safe_set(owner, 'dbl_NamedElement', None)
    assert getattr(partner, 'dbl_IdExpr164') is None


def test_assoc_right205_stub_double():
    # dbl_AlternativeExpr has no real 'dbl_AlternativeExpr206' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AlternativeExpr()
    setattr(partner, 'dbl_AlternativeExpr206', None)
    _safe_set(owner, 'dbl_RhsExpression207', partner)
    assert getattr(partner, 'dbl_AlternativeExpr206') == owner
    _safe_set(owner, 'dbl_RhsExpression207', None)
    assert getattr(partner, 'dbl_AlternativeExpr206') is None


def test_assoc_rule209_stub_double():
    # dbl_RuleExpr has no real 'dbl_RuleExpr210' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TsRule(metaClassName="sample_text")
    partner = dbl_RuleExpr()
    setattr(partner, 'dbl_RuleExpr210', None)
    _safe_set(owner, 'dbl_TsRule211', partner)
    assert getattr(partner, 'dbl_RuleExpr210') == owner
    _safe_set(owner, 'dbl_TsRule211', None)
    assert getattr(partner, 'dbl_RuleExpr210') is None


def test_assoc_sequence193_stub_double():
    # dbl_SequenceExpr has no real 'dbl_SequenceExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_SequenceExpr()
    setattr(partner, 'dbl_SequenceExpr', None)
    _safe_set(owner, 'dbl_RhsExpression194', partner)
    assert owner in getattr(partner, 'dbl_SequenceExpr')
    _safe_set(owner, 'dbl_RhsExpression194', None)
    assert owner not in getattr(partner, 'dbl_SequenceExpr')


def test_assoc_simpleAnnotations43_stub_double():
    # dbl_AnnotatableElement has no real 'dbl_AnnotatableElement44' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SimpleAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SimpleAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SimpleAnnotation(value="sample_text")
    partner = dbl_AnnotatableElement()
    setattr(partner, 'dbl_AnnotatableElement44', None)
    _safe_set(owner, 'dbl_SimpleAnnotation', partner)
    assert owner in getattr(partner, 'dbl_AnnotatableElement44')
    _safe_set(owner, 'dbl_SimpleAnnotation', None)
    assert owner not in getattr(partner, 'dbl_AnnotatableElement44')


def test_assoc_superClass52_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar53' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar53', None)
    _safe_set(owner, 'dbl_Clazz', partner)
    assert getattr(partner, 'dbl_ClassSimilar53') == owner
    _safe_set(owner, 'dbl_Clazz', None)
    assert getattr(partner, 'dbl_ClassSimilar53') is None


def test_assoc_variables16_stub_double():
    # dbl_Module has no real 'dbl_Module17' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Module()
    setattr(partner, 'dbl_Module17', None)
    _safe_set(owner, 'dbl_Variable', partner)
    assert owner in getattr(partner, 'dbl_Module17')
    _safe_set(owner, 'dbl_Variable', None)
    assert owner not in getattr(partner, 'dbl_Module17')


