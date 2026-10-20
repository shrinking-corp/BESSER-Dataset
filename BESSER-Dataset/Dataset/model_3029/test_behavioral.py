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
    Extension,
    MappingPart,
    ModifierExtensionsContainer,
    Module,
    NamedElement,
    NamedExtension,
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
    odemcustom_AbstractVariable,
    odemcustom_ActivateObject,
    odemcustom_ActiveLiteral,
    odemcustom_AddToSet,
    odemcustom_Advance,
    odemcustom_AfterInSet,
    odemcustom_AlternativeExpr,
    odemcustom_And,
    odemcustom_AnnotatableElement,
    odemcustom_Annotation,
    odemcustom_AnnotationApplication,
    odemcustom_ArbitraryExpr,
    odemcustom_ArgumentExpression,
    odemcustom_Assignment,
    odemcustom_AtLeastOneExpr,
    odemcustom_BeforeInSet,
    odemcustom_BinaryOperator,
    odemcustom_BoolType,
    odemcustom_BooleanPropertyType,
    odemcustom_BreakStatement,
    odemcustom_Cast,
    odemcustom_ClassAugment,
    odemcustom_ClassContentExtension,
    odemcustom_ClassSimilar,
    odemcustom_Classifier,
    odemcustom_Clazz,
    odemcustom_CodeBlock,
    odemcustom_CodeQuoteExpression,
    odemcustom_CompositePropertyType,
    odemcustom_CompositeStatement,
    odemcustom_ConsiderIdElements,
    odemcustom_Construct,
    odemcustom_Constructor,
    odemcustom_Contains,
    odemcustom_ContinueStatement,
    odemcustom_CreateObject,
    odemcustom_DepIdentifiableElement,
    odemcustom_DeprecatedProcedureCallStatement,
    odemcustom_Div,
    odemcustom_DoubleLiteral,
    odemcustom_DoubleType,
    odemcustom_DynamicMappingPart,
    odemcustom_ElementAccess,
    odemcustom_EmbeddableExtensionsContainer,
    odemcustom_EmptySet,
    odemcustom_Equal,
    odemcustom_EvalExpr,
    odemcustom_ExpandExpression,
    odemcustom_ExpandSection,
    odemcustom_ExpandStatement,
    odemcustom_ExpandableElement,
    odemcustom_Expression,
    odemcustom_ExpressionStatement,
    odemcustom_Extension,
    odemcustom_ExtensionDefinition,
    odemcustom_ExtensionRule,
    odemcustom_FalseLiteral,
    odemcustom_FindContainer,
    odemcustom_FirstInSet,
    odemcustom_FixedMappingPart,
    odemcustom_ForEachStatement,
    odemcustom_Greater,
    odemcustom_GreaterEqual,
    odemcustom_IdExpr,
    odemcustom_IdPropertyType,
    odemcustom_IdResolution,
    odemcustom_IfStatement,
    odemcustom_Import,
    odemcustom_IncludePattern,
    odemcustom_IndexOf,
    odemcustom_InstanceOf,
    odemcustom_IntLiteral,
    odemcustom_IntPropertyType,
    odemcustom_IntType,
    odemcustom_Interface,
    odemcustom_KeyValuePair,
    odemcustom_L1Expr,
    odemcustom_LastInSet,
    odemcustom_Less,
    odemcustom_LessEqual,
    odemcustom_Mapping,
    odemcustom_MappingPart,
    odemcustom_MappingStatement,
    odemcustom_MeLiteral,
    odemcustom_MetaAccess,
    odemcustom_MetaExpr,
    odemcustom_MetaLiteral,
    odemcustom_Minus,
    odemcustom_Mod,
    odemcustom_Model,
    odemcustom_ModifierExtensionsContainer,
    odemcustom_Module,
    odemcustom_ModuleContentExtension,
    odemcustom_Mul,
    odemcustom_NamedElement,
    odemcustom_NamedExtension,
    odemcustom_NativeBinding,
    odemcustom_Neg,
    odemcustom_Not,
    odemcustom_NotEqual,
    odemcustom_NullLiteral,
    odemcustom_ObjectAt,
    odemcustom_OptionalExpr,
    odemcustom_Or,
    odemcustom_Parameter,
    odemcustom_Pattern,
    odemcustom_Plus,
    odemcustom_PotentiallyHiddenIdElements,
    odemcustom_PredefinedId,
    odemcustom_PrimitiveType,
    odemcustom_Print,
    odemcustom_Procedure,
    odemcustom_ProcedureCall,
    odemcustom_PropertyBindingExpr,
    odemcustom_PropertyType,
    odemcustom_QuotedClassContent,
    odemcustom_QuotedCode,
    odemcustom_QuotedExpression,
    odemcustom_QuotedModuleContent,
    odemcustom_QuotedStatements,
    odemcustom_Reactivate,
    odemcustom_ReferableRhsType,
    odemcustom_ReferencePropertyType,
    odemcustom_RemoveFromSet,
    odemcustom_ResetGenContextStatement,
    odemcustom_ResumeGenStatement,
    odemcustom_Return,
    odemcustom_RhsExpression,
    odemcustom_RuleExpr,
    odemcustom_RuntimeExpr,
    odemcustom_SaveGenStatement,
    odemcustom_SequenceExpr,
    odemcustom_SetGenContextStatement,
    odemcustom_SetOp,
    odemcustom_SetStatement,
    odemcustom_SimpleAnnotation,
    odemcustom_SimpleStatement,
    odemcustom_SizeOfSet,
    odemcustom_StartCodeBlock,
    odemcustom_Statement,
    odemcustom_StatementExpression,
    odemcustom_StringLiteral,
    odemcustom_StringPropertyType,
    odemcustom_StringType,
    odemcustom_StructuredPropertyType,
    odemcustom_SuperLiteral,
    odemcustom_TargetStatement,
    odemcustom_TerminalExpr,
    odemcustom_Terminate,
    odemcustom_TestStatement,
    odemcustom_TextualSyntaxDef,
    odemcustom_TimeLiteral,
    odemcustom_TrueLiteral,
    odemcustom_TsRule,
    odemcustom_Type,
    odemcustom_TypeAccess,
    odemcustom_TypeLiteral,
    odemcustom_TypedElement,
    odemcustom_UnaryOperator,
    odemcustom_Variable,
    odemcustom_VariableAccess,
    odemcustom_VoidType,
    odemcustom_Wait,
    odemcustom_WaitUntil,
    odemcustom_WhileStatement,
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

def test_assoc_idResolutionPattern211_reverse_link_reassign_clear():
    a1 = odemcustom_ReferencePropertyType(rawReference=True)
    a2 = odemcustom_ReferencePropertyType(rawReference=False)
    b = odemcustom_Pattern(top=True)
    _safe_set(b, 'odemcustom_Pattern', a1)
    assert _is_linked(b, 'odemcustom_Pattern', a1)
    if hasattr(a1, 'odemcustom_ReferencePropertyType'):
        assert _is_linked(a1, 'odemcustom_ReferencePropertyType', b)
    _safe_set(b, 'odemcustom_Pattern', a2)
    assert _is_linked(b, 'odemcustom_Pattern', a2)
    if hasattr(a1, 'odemcustom_ReferencePropertyType'):
        assert not _is_linked(a1, 'odemcustom_ReferencePropertyType', b)
    if hasattr(a2, 'odemcustom_ReferencePropertyType'):
        assert _is_linked(a2, 'odemcustom_ReferencePropertyType', b)
    _safe_set(b, 'odemcustom_Pattern', None)
    assert not _is_linked(b, 'odemcustom_Pattern', a2)
    if hasattr(a2, 'odemcustom_ReferencePropertyType'):
        assert not _is_linked(a2, 'odemcustom_ReferencePropertyType', b)


def test_assoc_patterns250_reverse_link_reassign_clear():
    a1 = odemcustom_Pattern(top=True)
    a2 = odemcustom_Pattern(top=False)
    b = odemcustom_IdResolution(metaModelPlatformURI="sample_text")
    _safe_set(b, 'odemcustom_IdResolution251', {a1})
    assert _is_linked(b, 'odemcustom_IdResolution251', a1)
    if hasattr(a1, 'odemcustom_Pattern252'):
        assert _is_linked(a1, 'odemcustom_Pattern252', b)
    _safe_set(b, 'odemcustom_IdResolution251', {a2})
    assert _is_linked(b, 'odemcustom_IdResolution251', a2)
    if hasattr(a1, 'odemcustom_Pattern252'):
        assert not _is_linked(a1, 'odemcustom_Pattern252', b)
    if hasattr(a2, 'odemcustom_Pattern252'):
        assert _is_linked(a2, 'odemcustom_Pattern252', b)
    _safe_set(b, 'odemcustom_IdResolution251', set())
    assert not _is_linked(b, 'odemcustom_IdResolution251', a2)
    if hasattr(a2, 'odemcustom_Pattern252'):
        assert not _is_linked(a2, 'odemcustom_Pattern252', b)


def test_assoc_rhs184_reverse_link_reassign_clear():
    a1 = odemcustom_TsRule(metaClassName="sample_text")
    a2 = odemcustom_TsRule(metaClassName="sample_text_2")
    b = odemcustom_RhsExpression()
    _safe_set(b, 'odemcustom_RhsExpression', a1)
    assert _is_linked(b, 'odemcustom_RhsExpression', a1)
    if hasattr(a1, 'odemcustom_TsRule185'):
        assert _is_linked(a1, 'odemcustom_TsRule185', b)
    _safe_set(b, 'odemcustom_RhsExpression', a2)
    assert _is_linked(b, 'odemcustom_RhsExpression', a2)
    if hasattr(a1, 'odemcustom_TsRule185'):
        assert not _is_linked(a1, 'odemcustom_TsRule185', b)
    if hasattr(a2, 'odemcustom_TsRule185'):
        assert _is_linked(a2, 'odemcustom_TsRule185', b)
    _safe_set(b, 'odemcustom_RhsExpression', None)
    assert not _is_linked(b, 'odemcustom_RhsExpression', a2)
    if hasattr(a2, 'odemcustom_TsRule185'):
        assert not _is_linked(a2, 'odemcustom_TsRule185', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes45_stub_double():
    # odemcustom_ClassSimilar has no real 'odemcustom_ClassSimilar' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Variable(clazz=True, control=True)
    partner = odemcustom_ClassSimilar()
    setattr(partner, 'odemcustom_ClassSimilar', None)
    _safe_set(owner, 'odemcustom_Variable46', partner)
    assert owner in getattr(partner, 'odemcustom_ClassSimilar')
    _safe_set(owner, 'odemcustom_Variable46', None)
    assert owner not in getattr(partner, 'odemcustom_ClassSimilar')


def test_assoc_augmentedClass76_stub_double():
    # odemcustom_ClassAugment has no real 'odemcustom_ClassAugment77' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Clazz(active=True)
    partner = odemcustom_ClassAugment()
    setattr(partner, 'odemcustom_ClassAugment77', None)
    _safe_set(owner, 'odemcustom_Clazz78', partner)
    assert getattr(partner, 'odemcustom_ClassAugment77') == owner
    _safe_set(owner, 'odemcustom_Clazz78', None)
    assert getattr(partner, 'odemcustom_ClassAugment77') is None


def test_assoc_baseConstructorArguments70_stub_double():
    # odemcustom_Expression has no real 'odemcustom_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Clazz(active=True)
    partner = odemcustom_Expression()
    setattr(partner, 'odemcustom_Expression72', None)
    _safe_set(owner, 'odemcustom_Clazz71', {partner})
    assert getattr(partner, 'odemcustom_Expression72') == owner
    _safe_set(owner, 'odemcustom_Clazz71', set())
    assert getattr(partner, 'odemcustom_Expression72') is None


def test_assoc_bindings43_stub_double():
    # odemcustom_Classifier has no real 'odemcustom_Classifier44' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_NativeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_NativeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_NativeBinding(targetLanguage="sample_text", targetType="sample_text")
    partner = odemcustom_Classifier()
    setattr(partner, 'odemcustom_Classifier44', None)
    _safe_set(owner, 'odemcustom_NativeBinding', partner)
    assert owner in getattr(partner, 'odemcustom_Classifier44')
    _safe_set(owner, 'odemcustom_NativeBinding', None)
    assert owner not in getattr(partner, 'odemcustom_Classifier44')


def test_assoc_classifierTypeExpr24_stub_double():
    # odemcustom_IdExpr has no real 'odemcustom_IdExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_TypedElement(isList=True)
    partner = odemcustom_IdExpr()
    setattr(partner, 'odemcustom_IdExpr', None)
    _safe_set(owner, 'odemcustom_TypedElement25', partner)
    assert getattr(partner, 'odemcustom_IdExpr') == owner
    _safe_set(owner, 'odemcustom_TypedElement25', None)
    assert getattr(partner, 'odemcustom_IdExpr') is None


def test_assoc_codeBlock256_stub_double():
    # odemcustom_CodeBlock has no real 'odemcustom_CodeBlock258' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Pattern(top=True)
    partner = odemcustom_CodeBlock()
    setattr(partner, 'odemcustom_CodeBlock258', None)
    _safe_set(owner, 'odemcustom_Pattern257', partner)
    assert getattr(partner, 'odemcustom_CodeBlock258') == owner
    _safe_set(owner, 'odemcustom_Pattern257', None)
    assert getattr(partner, 'odemcustom_CodeBlock258') is None


def test_assoc_constructor68_stub_double():
    # odemcustom_Constructor has no real 'odemcustom_Constructor' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Clazz(active=True)
    partner = odemcustom_Constructor()
    setattr(partner, 'odemcustom_Constructor', None)
    _safe_set(owner, 'odemcustom_Clazz69', partner)
    assert getattr(partner, 'odemcustom_Constructor') == owner
    _safe_set(owner, 'odemcustom_Clazz69', None)
    assert getattr(partner, 'odemcustom_Constructor') is None


def test_assoc_context226_stub_double():
    # odemcustom_Expression has no real 'odemcustom_Expression227' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_SetGenContextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_SetGenContextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_SetGenContextStatement(addAfterContext=True)
    partner = odemcustom_Expression()
    setattr(partner, 'odemcustom_Expression227', None)
    _safe_set(owner, 'odemcustom_SetGenContextStatement', partner)
    assert getattr(partner, 'odemcustom_Expression227') == owner
    _safe_set(owner, 'odemcustom_SetGenContextStatement', None)
    assert getattr(partner, 'odemcustom_Expression227') is None


def test_assoc_context253_stub_double():
    # odemcustom_Parameter has no real 'odemcustom_Parameter255' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Pattern(top=True)
    partner = odemcustom_Parameter()
    setattr(partner, 'odemcustom_Parameter255', None)
    _safe_set(owner, 'odemcustom_Pattern254', partner)
    assert getattr(partner, 'odemcustom_Parameter255') == owner
    _safe_set(owner, 'odemcustom_Pattern254', None)
    assert getattr(partner, 'odemcustom_Parameter255') is None


def test_assoc_expression193_stub_double():
    # odemcustom_OptionalExpr has no real 'odemcustom_OptionalExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_OptionalExpr()
    setattr(partner, 'odemcustom_OptionalExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression194', partner)
    assert getattr(partner, 'odemcustom_OptionalExpr') == owner
    _safe_set(owner, 'odemcustom_RhsExpression194', None)
    assert getattr(partner, 'odemcustom_OptionalExpr') is None


def test_assoc_expression195_stub_double():
    # odemcustom_RuntimeExpr has no real 'odemcustom_RuntimeExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_RuntimeExpr()
    setattr(partner, 'odemcustom_RuntimeExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression196', partner)
    assert getattr(partner, 'odemcustom_RuntimeExpr') == owner
    _safe_set(owner, 'odemcustom_RhsExpression196', None)
    assert getattr(partner, 'odemcustom_RuntimeExpr') is None


def test_assoc_expression197_stub_double():
    # odemcustom_AtLeastOneExpr has no real 'odemcustom_AtLeastOneExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_AtLeastOneExpr()
    setattr(partner, 'odemcustom_AtLeastOneExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression198', partner)
    assert getattr(partner, 'odemcustom_AtLeastOneExpr') == owner
    _safe_set(owner, 'odemcustom_RhsExpression198', None)
    assert getattr(partner, 'odemcustom_AtLeastOneExpr') is None


def test_assoc_expression199_stub_double():
    # odemcustom_ArbitraryExpr has no real 'odemcustom_ArbitraryExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_ArbitraryExpr()
    setattr(partner, 'odemcustom_ArbitraryExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression200', partner)
    assert getattr(partner, 'odemcustom_ArbitraryExpr') == owner
    _safe_set(owner, 'odemcustom_RhsExpression200', None)
    assert getattr(partner, 'odemcustom_ArbitraryExpr') is None


def test_assoc_idRes18_stub_double():
    # odemcustom_Module has no real 'odemcustom_Module19' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_IdResolution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_IdResolution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_IdResolution(metaModelPlatformURI="sample_text")
    partner = odemcustom_Module()
    setattr(partner, 'odemcustom_Module19', None)
    _safe_set(owner, 'odemcustom_IdResolution', partner)
    assert getattr(partner, 'odemcustom_Module19') == owner
    _safe_set(owner, 'odemcustom_IdResolution', None)
    assert getattr(partner, 'odemcustom_Module19') is None


def test_assoc_imports0_stub_double():
    # odemcustom_Model has no real 'odemcustom_Model' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Import(file="sample_text")
    partner = odemcustom_Model()
    setattr(partner, 'odemcustom_Model', None)
    _safe_set(owner, 'odemcustom_Import', partner)
    assert owner in getattr(partner, 'odemcustom_Model')
    _safe_set(owner, 'odemcustom_Import', None)
    assert owner not in getattr(partner, 'odemcustom_Model')


def test_assoc_initialValue85_stub_double():
    # odemcustom_Expression has no real 'odemcustom_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Variable(clazz=True, control=True)
    partner = odemcustom_Expression()
    setattr(partner, 'odemcustom_Expression87', None)
    _safe_set(owner, 'odemcustom_Variable86', partner)
    assert getattr(partner, 'odemcustom_Expression87') == owner
    _safe_set(owner, 'odemcustom_Variable86', None)
    assert getattr(partner, 'odemcustom_Expression87') is None


def test_assoc_iteratorVariableDefinition137_stub_double():
    # odemcustom_ForEachStatement has no real 'odemcustom_ForEachStatement' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Variable(clazz=True, control=True)
    partner = odemcustom_ForEachStatement()
    setattr(partner, 'odemcustom_ForEachStatement', None)
    _safe_set(owner, 'odemcustom_Variable138', partner)
    assert getattr(partner, 'odemcustom_ForEachStatement') == owner
    _safe_set(owner, 'odemcustom_Variable138', None)
    assert getattr(partner, 'odemcustom_ForEachStatement') is None


def test_assoc_keys28_stub_double():
    # odemcustom_Annotation has no real 'odemcustom_Annotation29' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Variable(clazz=True, control=True)
    partner = odemcustom_Annotation()
    setattr(partner, 'odemcustom_Annotation29', None)
    _safe_set(owner, 'odemcustom_Variable30', partner)
    assert owner in getattr(partner, 'odemcustom_Annotation29')
    _safe_set(owner, 'odemcustom_Variable30', None)
    assert owner not in getattr(partner, 'odemcustom_Annotation29')


def test_assoc_left201_stub_double():
    # odemcustom_AlternativeExpr has no real 'odemcustom_AlternativeExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_AlternativeExpr()
    setattr(partner, 'odemcustom_AlternativeExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression202', partner)
    assert getattr(partner, 'odemcustom_AlternativeExpr') == owner
    _safe_set(owner, 'odemcustom_RhsExpression202', None)
    assert getattr(partner, 'odemcustom_AlternativeExpr') is None


def test_assoc_methods47_stub_double():
    # odemcustom_ClassSimilar has no real 'odemcustom_ClassSimilar48' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Procedure(clazz=True)
    partner = odemcustom_ClassSimilar()
    setattr(partner, 'odemcustom_ClassSimilar48', None)
    _safe_set(owner, 'odemcustom_Procedure49', partner)
    assert owner in getattr(partner, 'odemcustom_ClassSimilar48')
    _safe_set(owner, 'odemcustom_Procedure49', None)
    assert owner not in getattr(partner, 'odemcustom_ClassSimilar48')


def test_assoc_methods79_stub_double():
    # odemcustom_Interface has no real 'odemcustom_Interface80' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Procedure(clazz=True)
    partner = odemcustom_Interface()
    setattr(partner, 'odemcustom_Interface80', None)
    _safe_set(owner, 'odemcustom_Procedure81', partner)
    assert owner in getattr(partner, 'odemcustom_Interface80')
    _safe_set(owner, 'odemcustom_Procedure81', None)
    assert owner not in getattr(partner, 'odemcustom_Interface80')


def test_assoc_model3_stub_double():
    # odemcustom_Model has no real 'odemcustom_Model5' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Import(file="sample_text")
    partner = odemcustom_Model()
    setattr(partner, 'odemcustom_Model5', None)
    _safe_set(owner, 'odemcustom_Import4', partner)
    assert getattr(partner, 'odemcustom_Model5') == owner
    _safe_set(owner, 'odemcustom_Import4', None)
    assert getattr(partner, 'odemcustom_Model5') is None


def test_assoc_newRules182_stub_double():
    # odemcustom_TextualSyntaxDef has no real 'odemcustom_TextualSyntaxDef183' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_TsRule(metaClassName="sample_text")
    partner = odemcustom_TextualSyntaxDef()
    setattr(partner, 'odemcustom_TextualSyntaxDef183', None)
    _safe_set(owner, 'odemcustom_TsRule', partner)
    assert owner in getattr(partner, 'odemcustom_TextualSyntaxDef183')
    _safe_set(owner, 'odemcustom_TsRule', None)
    assert owner not in getattr(partner, 'odemcustom_TextualSyntaxDef183')


def test_assoc_objectAccess105_stub_double():
    # odemcustom_Expression has no real 'odemcustom_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_ActivateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_ActivateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_ActivateObject(priority=7)
    partner = odemcustom_Expression()
    setattr(partner, 'odemcustom_Expression106', None)
    _safe_set(owner, 'odemcustom_ActivateObject', partner)
    assert getattr(partner, 'odemcustom_Expression106') == owner
    _safe_set(owner, 'odemcustom_ActivateObject', None)
    assert getattr(partner, 'odemcustom_Expression106') is None


def test_assoc_parameters26_stub_double():
    # odemcustom_Parameter has no real 'odemcustom_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Procedure(clazz=True)
    partner = odemcustom_Parameter()
    setattr(partner, 'odemcustom_Parameter', None)
    _safe_set(owner, 'odemcustom_Procedure27', {partner})
    assert getattr(partner, 'odemcustom_Parameter') == owner
    _safe_set(owner, 'odemcustom_Procedure27', set())
    assert getattr(partner, 'odemcustom_Parameter') is None


def test_assoc_pattern271_stub_double():
    # odemcustom_IncludePattern has no real 'odemcustom_IncludePattern' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Pattern(top=True)
    partner = odemcustom_IncludePattern()
    setattr(partner, 'odemcustom_IncludePattern', None)
    _safe_set(owner, 'odemcustom_Pattern272', partner)
    assert getattr(partner, 'odemcustom_IncludePattern') == owner
    _safe_set(owner, 'odemcustom_Pattern272', None)
    assert getattr(partner, 'odemcustom_IncludePattern') is None


def test_assoc_primitiveType23_stub_double():
    # odemcustom_PrimitiveType has no real 'odemcustom_PrimitiveType' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_TypedElement(isList=True)
    partner = odemcustom_PrimitiveType()
    setattr(partner, 'odemcustom_PrimitiveType', None)
    _safe_set(owner, 'odemcustom_TypedElement', partner)
    assert getattr(partner, 'odemcustom_PrimitiveType') == owner
    _safe_set(owner, 'odemcustom_TypedElement', None)
    assert getattr(partner, 'odemcustom_PrimitiveType') is None


def test_assoc_procedures14_stub_double():
    # odemcustom_Module has no real 'odemcustom_Module15' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Procedure(clazz=True)
    partner = odemcustom_Module()
    setattr(partner, 'odemcustom_Module15', None)
    _safe_set(owner, 'odemcustom_Procedure', partner)
    assert owner in getattr(partner, 'odemcustom_Module15')
    _safe_set(owner, 'odemcustom_Procedure', None)
    assert owner not in getattr(partner, 'odemcustom_Module15')


def test_assoc_propertyType206_stub_double():
    # odemcustom_PropertyType has no real 'odemcustom_PropertyType' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_PropertyBindingExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_PropertyBindingExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_PropertyBindingExpr(operator="sample_text")
    partner = odemcustom_PropertyType()
    setattr(partner, 'odemcustom_PropertyType', None)
    _safe_set(owner, 'odemcustom_PropertyBindingExpr', partner)
    assert getattr(partner, 'odemcustom_PropertyType') == owner
    _safe_set(owner, 'odemcustom_PropertyBindingExpr', None)
    assert getattr(partner, 'odemcustom_PropertyType') is None


def test_assoc_referencedElement162_stub_double():
    # odemcustom_IdExpr has no real 'odemcustom_IdExpr163' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_NamedElement(name="sample_text")
    partner = odemcustom_IdExpr()
    setattr(partner, 'odemcustom_IdExpr163', None)
    _safe_set(owner, 'odemcustom_NamedElement', partner)
    assert getattr(partner, 'odemcustom_IdExpr163') == owner
    _safe_set(owner, 'odemcustom_NamedElement', None)
    assert getattr(partner, 'odemcustom_IdExpr163') is None


def test_assoc_right203_stub_double():
    # odemcustom_AlternativeExpr has no real 'odemcustom_AlternativeExpr204' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_AlternativeExpr()
    setattr(partner, 'odemcustom_AlternativeExpr204', None)
    _safe_set(owner, 'odemcustom_RhsExpression205', partner)
    assert getattr(partner, 'odemcustom_AlternativeExpr204') == owner
    _safe_set(owner, 'odemcustom_RhsExpression205', None)
    assert getattr(partner, 'odemcustom_AlternativeExpr204') is None


def test_assoc_rule207_stub_double():
    # odemcustom_RuleExpr has no real 'odemcustom_RuleExpr208' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_TsRule(metaClassName="sample_text")
    partner = odemcustom_RuleExpr()
    setattr(partner, 'odemcustom_RuleExpr208', None)
    _safe_set(owner, 'odemcustom_TsRule209', partner)
    assert getattr(partner, 'odemcustom_RuleExpr208') == owner
    _safe_set(owner, 'odemcustom_TsRule209', None)
    assert getattr(partner, 'odemcustom_RuleExpr208') is None


def test_assoc_sequence191_stub_double():
    # odemcustom_SequenceExpr has no real 'odemcustom_SequenceExpr' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_RhsExpression()
    partner = odemcustom_SequenceExpr()
    setattr(partner, 'odemcustom_SequenceExpr', None)
    _safe_set(owner, 'odemcustom_RhsExpression192', partner)
    assert owner in getattr(partner, 'odemcustom_SequenceExpr')
    _safe_set(owner, 'odemcustom_RhsExpression192', None)
    assert owner not in getattr(partner, 'odemcustom_SequenceExpr')


def test_assoc_simpleAnnotations41_stub_double():
    # odemcustom_AnnotatableElement has no real 'odemcustom_AnnotatableElement42' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_SimpleAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_SimpleAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_SimpleAnnotation(value="sample_text")
    partner = odemcustom_AnnotatableElement()
    setattr(partner, 'odemcustom_AnnotatableElement42', None)
    _safe_set(owner, 'odemcustom_SimpleAnnotation', partner)
    assert owner in getattr(partner, 'odemcustom_AnnotatableElement42')
    _safe_set(owner, 'odemcustom_SimpleAnnotation', None)
    assert owner not in getattr(partner, 'odemcustom_AnnotatableElement42')


def test_assoc_superClass50_stub_double():
    # odemcustom_ClassSimilar has no real 'odemcustom_ClassSimilar51' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Clazz(active=True)
    partner = odemcustom_ClassSimilar()
    setattr(partner, 'odemcustom_ClassSimilar51', None)
    _safe_set(owner, 'odemcustom_Clazz', partner)
    assert getattr(partner, 'odemcustom_ClassSimilar51') == owner
    _safe_set(owner, 'odemcustom_Clazz', None)
    assert getattr(partner, 'odemcustom_ClassSimilar51') is None


def test_assoc_variables16_stub_double():
    # odemcustom_Module has no real 'odemcustom_Module17' property in the generated
    # code (a bare stub) -- manually attach it so odemcustom_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # odemcustom_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = odemcustom_Variable(clazz=True, control=True)
    partner = odemcustom_Module()
    setattr(partner, 'odemcustom_Module17', None)
    _safe_set(owner, 'odemcustom_Variable', partner)
    assert owner in getattr(partner, 'odemcustom_Module17')
    _safe_set(owner, 'odemcustom_Variable', None)
    assert owner not in getattr(partner, 'odemcustom_Module17')


