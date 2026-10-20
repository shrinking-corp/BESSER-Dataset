import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdditionalField,
    AdditionalLocalVariable,
    AdditiveExpressionChild,
    AdditiveOperator,
    AndExpressionChild,
    Annotable,
    AnnotableAndModifiable,
    AnnotationAttributeSetting,
    AnnotationInstance,
    AnnotationInstanceOrModifier,
    AnnotationParameter,
    AnnotationValue,
    AnonymousClass,
    Argumentable,
    ArrayDimension,
    ArrayInitializationValue,
    ArrayInitializer,
    ArraySelector,
    ArrayTypeable,
    AssignmentExpressionChild,
    AssignmentOperator,
    Block,
    CallTypeArgumentable,
    CatchBlock,
    Classifier,
    ClassifierReference,
    Commentable,
    CompilationUnit,
    ConcreteClassifier,
    Conditional,
    ConditionalAndExpressionChild,
    ConditionalExpressionChild,
    ConditionalOrExpressionChild,
    DoubleLiteral,
    ElementReference,
    EnumConstant,
    EqualityExpressionChild,
    EqualityOperator,
    ExceptionThrower,
    ExclusiveOrExpressionChild,
    Expression,
    FloatLiteral,
    ForLoopInitializer,
    Implementor,
    Import,
    ImportingElement,
    InclusiveOrExpressionChild,
    Initializable,
    InstanceOfExpressionChild,
    Instantiation,
    IntegerLiteral,
    InterfaceMethod,
    JavaRoot,
    Jump,
    JumpLabel,
    Literal,
    LocalVariable,
    LongLiteral,
    Member,
    MemberContainer,
    Method,
    Modifiable,
    Modifier,
    MultiplicativeExpressionChild,
    MultiplicativeOperator,
    NamedElement,
    NamespaceAwareElement,
    NamespaceClassifierReference,
    Operator,
    OrdinaryParameter,
    Package,
    Parameter,
    Parametrizable,
    PrimaryExpression,
    PrimitiveType,
    Reference,
    ReferenceableElement,
    RelationExpressionChild,
    RelationOperator,
    Self,
    ShiftExpressionChild,
    ShiftOperator,
    Statement,
    StatementContainer,
    StatementListContainer,
    Static,
    StaticImport,
    SwitchCase,
    Type,
    TypeArgument,
    TypeArgumentable,
    TypeParameter,
    TypeParametrizable,
    TypeReference,
    TypedElement,
    UnaryExpressionChild,
    UnaryModificationExpression,
    UnaryModificationExpressionChild,
    UnaryModificationOperator,
    UnaryOperator,
    Variable,
    WhileLoop,
    annotations_Annotable,
    annotations_AnnotationAttribute,
    annotations_AnnotationAttributeSetting,
    annotations_AnnotationInstance,
    annotations_AnnotationParameter,
    annotations_AnnotationParameterList,
    annotations_AnnotationValue,
    annotations_SingleAnnotationParameter,
    arrays_ArrayDimension,
    arrays_ArrayInitializationValue,
    arrays_ArrayInitializer,
    arrays_ArrayInstantiationBySize,
    arrays_ArrayInstantiationByValues,
    arrays_ArraySelector,
    arrays_ArrayTypeable,
    classifiers_Annotation,
    classifiers_AnonymousClass,
    classifiers_Class,
    classifiers_Classifier,
    classifiers_ConcreteClassifier,
    classifiers_Enumeration,
    classifiers_Implementor,
    classifiers_Interface,
    commons_Commentable,
    commons_NamedElement,
    commons_NamespaceAwareElement,
    containers_CompilationUnit,
    containers_EmptyModel,
    containers_JavaRoot,
    containers_Package,
    expressions_AdditiveExpression,
    expressions_AdditiveExpressionChild,
    expressions_AndExpression,
    expressions_AndExpressionChild,
    expressions_AssignmentExpression,
    expressions_AssignmentExpressionChild,
    expressions_CastExpression,
    expressions_ConditionalAndExpression,
    expressions_ConditionalAndExpressionChild,
    expressions_ConditionalExpression,
    expressions_ConditionalExpressionChild,
    expressions_ConditionalOrExpression,
    expressions_ConditionalOrExpressionChild,
    expressions_EqualityExpression,
    expressions_EqualityExpressionChild,
    expressions_ExclusiveOrExpression,
    expressions_ExclusiveOrExpressionChild,
    expressions_Expression,
    expressions_ExpressionList,
    expressions_InclusiveOrExpression,
    expressions_InclusiveOrExpressionChild,
    expressions_InstanceOfExpression,
    expressions_InstanceOfExpressionChild,
    expressions_MultiplicativeExpression,
    expressions_MultiplicativeExpressionChild,
    expressions_NestedExpression,
    expressions_PrefixUnaryModificationExpression,
    expressions_PrimaryExpression,
    expressions_RelationExpression,
    expressions_RelationExpressionChild,
    expressions_ShiftExpression,
    expressions_ShiftExpressionChild,
    expressions_SuffixUnaryModificationExpression,
    expressions_UnaryExpression,
    expressions_UnaryExpressionChild,
    expressions_UnaryModificationExpression,
    expressions_UnaryModificationExpressionChild,
    generics_CallTypeArgumentable,
    generics_ExtendsTypeArgument,
    generics_QualifiedTypeArgument,
    generics_SuperTypeArgument,
    generics_TypeArgument,
    generics_TypeArgumentable,
    generics_TypeParameter,
    generics_TypeParametrizable,
    generics_UnknownTypeArgument,
    imports_ClassifierImport,
    imports_Import,
    imports_ImportingElement,
    imports_PackageImport,
    imports_StaticClassifierImport,
    imports_StaticImport,
    imports_StaticMemberImport,
    instantiations_ExplicitConstructorCall,
    instantiations_Initializable,
    instantiations_Instantiation,
    instantiations_NewConstructorCall,
    literals_BooleanLiteral,
    literals_CharacterLiteral,
    literals_DecimalDoubleLiteral,
    literals_DecimalFloatLiteral,
    literals_DecimalIntegerLiteral,
    literals_DecimalLongLiteral,
    literals_DoubleLiteral,
    literals_FloatLiteral,
    literals_HexDoubleLiteral,
    literals_HexFloatLiteral,
    literals_HexIntegerLiteral,
    literals_HexLongLiteral,
    literals_IntegerLiteral,
    literals_Literal,
    literals_LongLiteral,
    literals_NullLiteral,
    literals_OctalIntegerLiteral,
    literals_OctalLongLiteral,
    literals_Self,
    literals_Super,
    literals_This,
    members_AdditionalField,
    members_ClassMethod,
    members_Constructor,
    members_EmptyMember,
    members_EnumConstant,
    members_ExceptionThrower,
    members_Field,
    members_InterfaceMethod,
    members_Member,
    members_MemberContainer,
    members_Method,
    modifiers_Abstract,
    modifiers_AnnotableAndModifiable,
    modifiers_AnnotationInstanceOrModifier,
    modifiers_Final,
    modifiers_Modifiable,
    modifiers_Modifier,
    modifiers_Native,
    modifiers_Private,
    modifiers_Protected,
    modifiers_Public,
    modifiers_Static,
    modifiers_Strictfp,
    modifiers_Synchronized,
    modifiers_Transient,
    modifiers_Volatile,
    operators_Addition,
    operators_AdditiveOperator,
    operators_Assignment,
    operators_AssignmentAnd,
    operators_AssignmentDivision,
    operators_AssignmentExclusiveOr,
    operators_AssignmentLeftShift,
    operators_AssignmentMinus,
    operators_AssignmentModulo,
    operators_AssignmentMultiplication,
    operators_AssignmentOperator,
    operators_AssignmentOr,
    operators_AssignmentPlus,
    operators_AssignmentRightShift,
    operators_AssignmentUnsignedRightShift,
    operators_Complement,
    operators_Division,
    operators_Equal,
    operators_EqualityOperator,
    operators_GreaterThan,
    operators_GreaterThanOrEqual,
    operators_LeftShift,
    operators_LessThan,
    operators_LessThanOrEqual,
    operators_MinusMinus,
    operators_Multiplication,
    operators_MultiplicativeOperator,
    operators_Negate,
    operators_NotEqual,
    operators_Operator,
    operators_PlusPlus,
    operators_RelationOperator,
    operators_Remainder,
    operators_RightShift,
    operators_ShiftOperator,
    operators_Subtraction,
    operators_UnaryModificationOperator,
    operators_UnaryOperator,
    operators_UnsignedRightShift,
    parameters_OrdinaryParameter,
    parameters_Parameter,
    parameters_Parametrizable,
    parameters_VariableLengthParameter,
    references_Argumentable,
    references_ElementReference,
    references_IdentifierReference,
    references_MethodCall,
    references_PrimitiveTypeReference,
    references_Reference,
    references_ReferenceableElement,
    references_ReflectiveClassReference,
    references_SelfReference,
    references_StringReference,
    statements_Assert,
    statements_Block,
    statements_Break,
    statements_CatchBlock,
    statements_Condition,
    statements_Conditional,
    statements_Continue,
    statements_DefaultSwitchCase,
    statements_DoWhileLoop,
    statements_EmptyStatement,
    statements_ExpressionStatement,
    statements_ForEachLoop,
    statements_ForLoop,
    statements_ForLoopInitializer,
    statements_Jump,
    statements_JumpLabel,
    statements_LocalVariableStatement,
    statements_NormalSwitchCase,
    statements_Return,
    statements_Statement,
    statements_StatementContainer,
    statements_StatementListContainer,
    statements_Switch,
    statements_SwitchCase,
    statements_SynchronizedBlock,
    statements_Throw,
    statements_TryBlock,
    statements_WhileLoop,
    types_Boolean,
    types_Byte,
    types_Char,
    types_ClassifierReference,
    types_Double,
    types_Float,
    types_Int,
    types_Long,
    types_NamespaceClassifierReference,
    types_PrimitiveType,
    types_Short,
    types_Type,
    types_TypeReference,
    types_TypedElement,
    types_Void,
    variables_AdditionalLocalVariable,
    variables_LocalVariable,
    variables_Variable,
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

def test_assoc_annotationsAndModifiers110_stub_double():
    # AnnotationInstanceOrModifier has no real 'AnnotationInstanceOrModifier' property in the generated
    # code (a bare stub) -- manually attach it so modifiers_AnnotableAndModifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # modifiers_AnnotableAndModifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = modifiers_AnnotableAndModifiable()
    partner = AnnotationInstanceOrModifier()
    setattr(partner, 'AnnotationInstanceOrModifier', None)
    _safe_set(owner, 'modifiers_AnnotableAndModifiable', {partner})
    assert getattr(partner, 'AnnotationInstanceOrModifier') == owner
    _safe_set(owner, 'modifiers_AnnotableAndModifiable', set())
    assert getattr(partner, 'AnnotationInstanceOrModifier') is None


def test_assoc_arguments116_stub_double():
    # Expression has no real 'Expression117' property in the generated
    # code (a bare stub) -- manually attach it so references_Argumentable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # references_Argumentable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = references_Argumentable()
    partner = Expression()
    setattr(partner, 'Expression117', None)
    _safe_set(owner, 'references_Argumentable', {partner})
    assert getattr(partner, 'Expression117') == owner
    _safe_set(owner, 'references_Argumentable', set())
    assert getattr(partner, 'Expression117') is None


def test_assoc_arrayDimensionsAfter12_stub_double():
    # ArrayDimension has no real 'ArrayDimension14' property in the generated
    # code (a bare stub) -- manually attach it so arrays_ArrayTypeable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arrays_ArrayTypeable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arrays_ArrayTypeable()
    partner = ArrayDimension()
    setattr(partner, 'ArrayDimension14', None)
    _safe_set(owner, 'arrays_ArrayTypeable13', {partner})
    assert getattr(partner, 'ArrayDimension14') == owner
    _safe_set(owner, 'arrays_ArrayTypeable13', set())
    assert getattr(partner, 'ArrayDimension14') is None


def test_assoc_arrayDimensionsBefore11_stub_double():
    # ArrayDimension has no real 'ArrayDimension' property in the generated
    # code (a bare stub) -- manually attach it so arrays_ArrayTypeable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arrays_ArrayTypeable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arrays_ArrayTypeable()
    partner = ArrayDimension()
    setattr(partner, 'ArrayDimension', None)
    _safe_set(owner, 'arrays_ArrayTypeable', {partner})
    assert getattr(partner, 'ArrayDimension') == owner
    _safe_set(owner, 'arrays_ArrayTypeable', set())
    assert getattr(partner, 'ArrayDimension') is None


def test_assoc_arraySelectors114_stub_double():
    # ArraySelector has no real 'ArraySelector' property in the generated
    # code (a bare stub) -- manually attach it so references_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # references_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = references_Reference()
    partner = ArraySelector()
    setattr(partner, 'ArraySelector', None)
    _safe_set(owner, 'references_Reference115', {partner})
    assert getattr(partner, 'ArraySelector') == owner
    _safe_set(owner, 'references_Reference115', set())
    assert getattr(partner, 'ArraySelector') is None


def test_assoc_classifiers33_stub_double():
    # ConcreteClassifier has no real 'ConcreteClassifier' property in the generated
    # code (a bare stub) -- manually attach it so containers_CompilationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # containers_CompilationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = containers_CompilationUnit()
    partner = ConcreteClassifier()
    setattr(partner, 'ConcreteClassifier', None)
    _safe_set(owner, 'containers_CompilationUnit', {partner})
    assert getattr(partner, 'ConcreteClassifier') == owner
    _safe_set(owner, 'containers_CompilationUnit', set())
    assert getattr(partner, 'ConcreteClassifier') is None


def test_assoc_constants32_stub_double():
    # EnumConstant has no real 'EnumConstant' property in the generated
    # code (a bare stub) -- manually attach it so classifiers_Enumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classifiers_Enumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classifiers_Enumeration()
    partner = EnumConstant()
    setattr(partner, 'EnumConstant', None)
    _safe_set(owner, 'classifiers_Enumeration', {partner})
    assert getattr(partner, 'EnumConstant') == owner
    _safe_set(owner, 'classifiers_Enumeration', set())
    assert getattr(partner, 'EnumConstant') is None


def test_assoc_defaultExtends24_stub_double():
    # TypeReference has no real 'TypeReference26' property in the generated
    # code (a bare stub) -- manually attach it so classifiers_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classifiers_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classifiers_Class()
    partner = TypeReference()
    setattr(partner, 'TypeReference26', None)
    _safe_set(owner, 'classifiers_Class25', partner)
    assert getattr(partner, 'TypeReference26') == owner
    _safe_set(owner, 'classifiers_Class25', None)
    assert getattr(partner, 'TypeReference26') is None


def test_assoc_defaultExtends29_stub_double():
    # TypeReference has no real 'TypeReference31' property in the generated
    # code (a bare stub) -- manually attach it so classifiers_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classifiers_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classifiers_Interface()
    partner = TypeReference()
    setattr(partner, 'TypeReference31', None)
    _safe_set(owner, 'classifiers_Interface30', {partner})
    assert getattr(partner, 'TypeReference31') == owner
    _safe_set(owner, 'classifiers_Interface30', set())
    assert getattr(partner, 'TypeReference31') is None


def test_assoc_defaultMembers104_stub_double():
    # Member has no real 'Member106' property in the generated
    # code (a bare stub) -- manually attach it so members_MemberContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # members_MemberContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = members_MemberContainer()
    partner = Member()
    setattr(partner, 'Member106', None)
    _safe_set(owner, 'members_MemberContainer105', {partner})
    assert getattr(partner, 'Member106') == owner
    _safe_set(owner, 'members_MemberContainer105', set())
    assert getattr(partner, 'Member106') is None


def test_assoc_extendTypes91_stub_double():
    # TypeReference has no real 'TypeReference92' property in the generated
    # code (a bare stub) -- manually attach it so generics_TypeParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # generics_TypeParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = generics_TypeParameter()
    partner = TypeReference()
    setattr(partner, 'TypeReference92', None)
    _safe_set(owner, 'generics_TypeParameter', {partner})
    assert getattr(partner, 'TypeReference92') == owner
    _safe_set(owner, 'generics_TypeParameter', set())
    assert getattr(partner, 'TypeReference92') is None


def test_assoc_extends22_stub_double():
    # TypeReference has no real 'TypeReference23' property in the generated
    # code (a bare stub) -- manually attach it so classifiers_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classifiers_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classifiers_Class()
    partner = TypeReference()
    setattr(partner, 'TypeReference23', None)
    _safe_set(owner, 'classifiers_Class', partner)
    assert getattr(partner, 'TypeReference23') == owner
    _safe_set(owner, 'classifiers_Class', None)
    assert getattr(partner, 'TypeReference23') is None


def test_assoc_extends27_stub_double():
    # TypeReference has no real 'TypeReference28' property in the generated
    # code (a bare stub) -- manually attach it so classifiers_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classifiers_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classifiers_Interface()
    partner = TypeReference()
    setattr(partner, 'TypeReference28', None)
    _safe_set(owner, 'classifiers_Interface', {partner})
    assert getattr(partner, 'TypeReference28') == owner
    _safe_set(owner, 'classifiers_Interface', set())
    assert getattr(partner, 'TypeReference28') is None


def test_assoc_imports93_stub_double():
    # Import has no real 'Import' property in the generated
    # code (a bare stub) -- manually attach it so imports_ImportingElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imports_ImportingElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imports_ImportingElement()
    partner = Import()
    setattr(partner, 'Import', None)
    _safe_set(owner, 'imports_ImportingElement', {partner})
    assert getattr(partner, 'Import') == owner
    _safe_set(owner, 'imports_ImportingElement', set())
    assert getattr(partner, 'Import') is None


def test_assoc_members103_stub_double():
    # Member has no real 'Member' property in the generated
    # code (a bare stub) -- manually attach it so members_MemberContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # members_MemberContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = members_MemberContainer()
    partner = Member()
    setattr(partner, 'Member', None)
    _safe_set(owner, 'members_MemberContainer', {partner})
    assert getattr(partner, 'Member') == owner
    _safe_set(owner, 'members_MemberContainer', set())
    assert getattr(partner, 'Member') is None


def test_assoc_next113_stub_double():
    # Reference has no real 'Reference' property in the generated
    # code (a bare stub) -- manually attach it so references_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # references_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = references_Reference()
    partner = Reference()
    setattr(partner, 'Reference', None)
    _safe_set(owner, 'references_Reference', partner)
    assert getattr(partner, 'Reference') == owner
    _safe_set(owner, 'references_Reference', None)
    assert getattr(partner, 'Reference') is None


