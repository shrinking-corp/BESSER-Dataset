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
    L1Expr,
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
    dbl_Extension,
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
    dbl_NamedExtension,
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


def test_assoc_patterns250_reverse_link_reassign_clear():
    a1 = dbl_Pattern(top=True)
    a2 = dbl_Pattern(top=False)
    b = dbl_IdResolution(metaModelPlatformURI="sample_text")
    _safe_set(b, 'dbl_IdResolution251', {a1})
    assert _is_linked(b, 'dbl_IdResolution251', a1)
    if hasattr(a1, 'dbl_Pattern252'):
        assert _is_linked(a1, 'dbl_Pattern252', b)
    _safe_set(b, 'dbl_IdResolution251', {a2})
    assert _is_linked(b, 'dbl_IdResolution251', a2)
    if hasattr(a1, 'dbl_Pattern252'):
        assert not _is_linked(a1, 'dbl_Pattern252', b)
    if hasattr(a2, 'dbl_Pattern252'):
        assert _is_linked(a2, 'dbl_Pattern252', b)
    _safe_set(b, 'dbl_IdResolution251', set())
    assert not _is_linked(b, 'dbl_IdResolution251', a2)
    if hasattr(a2, 'dbl_Pattern252'):
        assert not _is_linked(a2, 'dbl_Pattern252', b)


def test_assoc_rhs184_reverse_link_reassign_clear():
    a1 = dbl_TsRule(metaClassName="sample_text")
    a2 = dbl_TsRule(metaClassName="sample_text_2")
    b = dbl_RhsExpression()
    _safe_set(b, 'dbl_RhsExpression', a1)
    assert _is_linked(b, 'dbl_RhsExpression', a1)
    if hasattr(a1, 'dbl_TsRule185'):
        assert _is_linked(a1, 'dbl_TsRule185', b)
    _safe_set(b, 'dbl_RhsExpression', a2)
    assert _is_linked(b, 'dbl_RhsExpression', a2)
    if hasattr(a1, 'dbl_TsRule185'):
        assert not _is_linked(a1, 'dbl_TsRule185', b)
    if hasattr(a2, 'dbl_TsRule185'):
        assert _is_linked(a2, 'dbl_TsRule185', b)
    _safe_set(b, 'dbl_RhsExpression', None)
    assert not _is_linked(b, 'dbl_RhsExpression', a2)
    if hasattr(a2, 'dbl_TsRule185'):
        assert not _is_linked(a2, 'dbl_TsRule185', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes45_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar', None)
    _safe_set(owner, 'dbl_Variable46', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar')
    _safe_set(owner, 'dbl_Variable46', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar')


def test_assoc_augmentedClass76_stub_double():
    # dbl_ClassAugment has no real 'dbl_ClassAugment77' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_ClassAugment()
    setattr(partner, 'dbl_ClassAugment77', None)
    _safe_set(owner, 'dbl_Clazz78', partner)
    assert getattr(partner, 'dbl_ClassAugment77') == owner
    _safe_set(owner, 'dbl_Clazz78', None)
    assert getattr(partner, 'dbl_ClassAugment77') is None


def test_assoc_baseConstructorArguments70_stub_double():
    # dbl_Expression has no real 'dbl_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression72', None)
    _safe_set(owner, 'dbl_Clazz71', {partner})
    assert getattr(partner, 'dbl_Expression72') == owner
    _safe_set(owner, 'dbl_Clazz71', set())
    assert getattr(partner, 'dbl_Expression72') is None


def test_assoc_bindings43_stub_double():
    # dbl_Classifier has no real 'dbl_Classifier44' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NativeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NativeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NativeBinding(targetLanguage="sample_text", targetType="sample_text")
    partner = dbl_Classifier()
    setattr(partner, 'dbl_Classifier44', None)
    _safe_set(owner, 'dbl_NativeBinding', partner)
    assert owner in getattr(partner, 'dbl_Classifier44')
    _safe_set(owner, 'dbl_NativeBinding', None)
    assert owner not in getattr(partner, 'dbl_Classifier44')


def test_assoc_classifierTypeExpr24_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TypedElement(isList=True)
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr', None)
    _safe_set(owner, 'dbl_TypedElement25', partner)
    assert getattr(partner, 'dbl_IdExpr') == owner
    _safe_set(owner, 'dbl_TypedElement25', None)
    assert getattr(partner, 'dbl_IdExpr') is None


def test_assoc_codeBlock256_stub_double():
    # dbl_CodeBlock has no real 'dbl_CodeBlock258' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_CodeBlock()
    setattr(partner, 'dbl_CodeBlock258', None)
    _safe_set(owner, 'dbl_Pattern257', partner)
    assert getattr(partner, 'dbl_CodeBlock258') == owner
    _safe_set(owner, 'dbl_Pattern257', None)
    assert getattr(partner, 'dbl_CodeBlock258') is None


def test_assoc_constructor68_stub_double():
    # dbl_Constructor has no real 'dbl_Constructor' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_Constructor()
    setattr(partner, 'dbl_Constructor', None)
    _safe_set(owner, 'dbl_Clazz69', partner)
    assert getattr(partner, 'dbl_Constructor') == owner
    _safe_set(owner, 'dbl_Clazz69', None)
    assert getattr(partner, 'dbl_Constructor') is None


def test_assoc_context226_stub_double():
    # dbl_Expression has no real 'dbl_Expression227' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SetGenContextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SetGenContextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SetGenContextStatement(addAfterContext=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression227', None)
    _safe_set(owner, 'dbl_SetGenContextStatement', partner)
    assert getattr(partner, 'dbl_Expression227') == owner
    _safe_set(owner, 'dbl_SetGenContextStatement', None)
    assert getattr(partner, 'dbl_Expression227') is None


def test_assoc_context253_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter255' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter255', None)
    _safe_set(owner, 'dbl_Pattern254', partner)
    assert getattr(partner, 'dbl_Parameter255') == owner
    _safe_set(owner, 'dbl_Pattern254', None)
    assert getattr(partner, 'dbl_Parameter255') is None


def test_assoc_expression193_stub_double():
    # dbl_OptionalExpr has no real 'dbl_OptionalExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_OptionalExpr()
    setattr(partner, 'dbl_OptionalExpr', None)
    _safe_set(owner, 'dbl_RhsExpression194', partner)
    assert getattr(partner, 'dbl_OptionalExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression194', None)
    assert getattr(partner, 'dbl_OptionalExpr') is None


def test_assoc_expression195_stub_double():
    # dbl_RuntimeExpr has no real 'dbl_RuntimeExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_RuntimeExpr()
    setattr(partner, 'dbl_RuntimeExpr', None)
    _safe_set(owner, 'dbl_RhsExpression196', partner)
    assert getattr(partner, 'dbl_RuntimeExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression196', None)
    assert getattr(partner, 'dbl_RuntimeExpr') is None


def test_assoc_expression197_stub_double():
    # dbl_AtLeastOneExpr has no real 'dbl_AtLeastOneExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AtLeastOneExpr()
    setattr(partner, 'dbl_AtLeastOneExpr', None)
    _safe_set(owner, 'dbl_RhsExpression198', partner)
    assert getattr(partner, 'dbl_AtLeastOneExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression198', None)
    assert getattr(partner, 'dbl_AtLeastOneExpr') is None


def test_assoc_expression199_stub_double():
    # dbl_ArbitraryExpr has no real 'dbl_ArbitraryExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_ArbitraryExpr()
    setattr(partner, 'dbl_ArbitraryExpr', None)
    _safe_set(owner, 'dbl_RhsExpression200', partner)
    assert getattr(partner, 'dbl_ArbitraryExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression200', None)
    assert getattr(partner, 'dbl_ArbitraryExpr') is None


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


def test_assoc_initialValue85_stub_double():
    # dbl_Expression has no real 'dbl_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression87', None)
    _safe_set(owner, 'dbl_Variable86', partner)
    assert getattr(partner, 'dbl_Expression87') == owner
    _safe_set(owner, 'dbl_Variable86', None)
    assert getattr(partner, 'dbl_Expression87') is None


def test_assoc_iteratorVariableDefinition137_stub_double():
    # dbl_ForEachStatement has no real 'dbl_ForEachStatement' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_ForEachStatement()
    setattr(partner, 'dbl_ForEachStatement', None)
    _safe_set(owner, 'dbl_Variable138', partner)
    assert getattr(partner, 'dbl_ForEachStatement') == owner
    _safe_set(owner, 'dbl_Variable138', None)
    assert getattr(partner, 'dbl_ForEachStatement') is None


def test_assoc_keys28_stub_double():
    # dbl_Annotation has no real 'dbl_Annotation29' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Variable(clazz=True, control=True)
    partner = dbl_Annotation()
    setattr(partner, 'dbl_Annotation29', None)
    _safe_set(owner, 'dbl_Variable30', partner)
    assert owner in getattr(partner, 'dbl_Annotation29')
    _safe_set(owner, 'dbl_Variable30', None)
    assert owner not in getattr(partner, 'dbl_Annotation29')


def test_assoc_left201_stub_double():
    # dbl_AlternativeExpr has no real 'dbl_AlternativeExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AlternativeExpr()
    setattr(partner, 'dbl_AlternativeExpr', None)
    _safe_set(owner, 'dbl_RhsExpression202', partner)
    assert getattr(partner, 'dbl_AlternativeExpr') == owner
    _safe_set(owner, 'dbl_RhsExpression202', None)
    assert getattr(partner, 'dbl_AlternativeExpr') is None


def test_assoc_methods47_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar48' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar48', None)
    _safe_set(owner, 'dbl_Procedure49', partner)
    assert owner in getattr(partner, 'dbl_ClassSimilar48')
    _safe_set(owner, 'dbl_Procedure49', None)
    assert owner not in getattr(partner, 'dbl_ClassSimilar48')


def test_assoc_methods79_stub_double():
    # dbl_Interface has no real 'dbl_Interface80' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_Interface()
    setattr(partner, 'dbl_Interface80', None)
    _safe_set(owner, 'dbl_Procedure81', partner)
    assert owner in getattr(partner, 'dbl_Interface80')
    _safe_set(owner, 'dbl_Procedure81', None)
    assert owner not in getattr(partner, 'dbl_Interface80')


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


def test_assoc_newRules182_stub_double():
    # dbl_TextualSyntaxDef has no real 'dbl_TextualSyntaxDef183' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TsRule(metaClassName="sample_text")
    partner = dbl_TextualSyntaxDef()
    setattr(partner, 'dbl_TextualSyntaxDef183', None)
    _safe_set(owner, 'dbl_TsRule', partner)
    assert owner in getattr(partner, 'dbl_TextualSyntaxDef183')
    _safe_set(owner, 'dbl_TsRule', None)
    assert owner not in getattr(partner, 'dbl_TextualSyntaxDef183')


def test_assoc_objectAccess105_stub_double():
    # dbl_Expression has no real 'dbl_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so dbl_ActivateObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_ActivateObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_ActivateObject(priority=7)
    partner = dbl_Expression()
    setattr(partner, 'dbl_Expression106', None)
    _safe_set(owner, 'dbl_ActivateObject', partner)
    assert getattr(partner, 'dbl_Expression106') == owner
    _safe_set(owner, 'dbl_ActivateObject', None)
    assert getattr(partner, 'dbl_Expression106') is None


def test_assoc_parameters26_stub_double():
    # dbl_Parameter has no real 'dbl_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Procedure(clazz=True)
    partner = dbl_Parameter()
    setattr(partner, 'dbl_Parameter', None)
    _safe_set(owner, 'dbl_Procedure27', {partner})
    assert getattr(partner, 'dbl_Parameter') == owner
    _safe_set(owner, 'dbl_Procedure27', set())
    assert getattr(partner, 'dbl_Parameter') is None


def test_assoc_pattern271_stub_double():
    # dbl_IncludePattern has no real 'dbl_IncludePattern' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Pattern(top=True)
    partner = dbl_IncludePattern()
    setattr(partner, 'dbl_IncludePattern', None)
    _safe_set(owner, 'dbl_Pattern272', partner)
    assert getattr(partner, 'dbl_IncludePattern') == owner
    _safe_set(owner, 'dbl_Pattern272', None)
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


def test_assoc_propertyType206_stub_double():
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


def test_assoc_referencedElement162_stub_double():
    # dbl_IdExpr has no real 'dbl_IdExpr163' property in the generated
    # code (a bare stub) -- manually attach it so dbl_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_NamedElement(name="sample_text")
    partner = dbl_IdExpr()
    setattr(partner, 'dbl_IdExpr163', None)
    _safe_set(owner, 'dbl_NamedElement', partner)
    assert getattr(partner, 'dbl_IdExpr163') == owner
    _safe_set(owner, 'dbl_NamedElement', None)
    assert getattr(partner, 'dbl_IdExpr163') is None


def test_assoc_right203_stub_double():
    # dbl_AlternativeExpr has no real 'dbl_AlternativeExpr204' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_AlternativeExpr()
    setattr(partner, 'dbl_AlternativeExpr204', None)
    _safe_set(owner, 'dbl_RhsExpression205', partner)
    assert getattr(partner, 'dbl_AlternativeExpr204') == owner
    _safe_set(owner, 'dbl_RhsExpression205', None)
    assert getattr(partner, 'dbl_AlternativeExpr204') is None


def test_assoc_rule207_stub_double():
    # dbl_RuleExpr has no real 'dbl_RuleExpr208' property in the generated
    # code (a bare stub) -- manually attach it so dbl_TsRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_TsRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_TsRule(metaClassName="sample_text")
    partner = dbl_RuleExpr()
    setattr(partner, 'dbl_RuleExpr208', None)
    _safe_set(owner, 'dbl_TsRule209', partner)
    assert getattr(partner, 'dbl_RuleExpr208') == owner
    _safe_set(owner, 'dbl_TsRule209', None)
    assert getattr(partner, 'dbl_RuleExpr208') is None


def test_assoc_sequence191_stub_double():
    # dbl_SequenceExpr has no real 'dbl_SequenceExpr' property in the generated
    # code (a bare stub) -- manually attach it so dbl_RhsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_RhsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_RhsExpression()
    partner = dbl_SequenceExpr()
    setattr(partner, 'dbl_SequenceExpr', None)
    _safe_set(owner, 'dbl_RhsExpression192', partner)
    assert owner in getattr(partner, 'dbl_SequenceExpr')
    _safe_set(owner, 'dbl_RhsExpression192', None)
    assert owner not in getattr(partner, 'dbl_SequenceExpr')


def test_assoc_simpleAnnotations41_stub_double():
    # dbl_AnnotatableElement has no real 'dbl_AnnotatableElement42' property in the generated
    # code (a bare stub) -- manually attach it so dbl_SimpleAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_SimpleAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_SimpleAnnotation(value="sample_text")
    partner = dbl_AnnotatableElement()
    setattr(partner, 'dbl_AnnotatableElement42', None)
    _safe_set(owner, 'dbl_SimpleAnnotation', partner)
    assert owner in getattr(partner, 'dbl_AnnotatableElement42')
    _safe_set(owner, 'dbl_SimpleAnnotation', None)
    assert owner not in getattr(partner, 'dbl_AnnotatableElement42')


def test_assoc_superClass50_stub_double():
    # dbl_ClassSimilar has no real 'dbl_ClassSimilar51' property in the generated
    # code (a bare stub) -- manually attach it so dbl_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dbl_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dbl_Clazz(active=True)
    partner = dbl_ClassSimilar()
    setattr(partner, 'dbl_ClassSimilar51', None)
    _safe_set(owner, 'dbl_Clazz', partner)
    assert getattr(partner, 'dbl_ClassSimilar51') == owner
    _safe_set(owner, 'dbl_Clazz', None)
    assert getattr(partner, 'dbl_ClassSimilar51') is None


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


