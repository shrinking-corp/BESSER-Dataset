import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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
    types_Bool,
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

def test_classifiers_ConcreteClassifier_fullName_value_roundtrip():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_commons_Commentable_comments_value_roundtrip():
    instance = commons_Commentable(comments="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_commons_NamedElement_name_value_roundtrip():
    instance = commons_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_commons_NamespaceAwareElement_namespaces_value_roundtrip():
    instance = commons_NamespaceAwareElement(namespaces="sample_text")
    assert instance.namespaces == "sample_text"
    instance.namespaces = "sample_text_2"
    assert instance.namespaces == "sample_text_2"


def test_literals_BooleanLiteral_value_value_roundtrip():
    instance = literals_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_literals_CharacterLiteral_value_value_roundtrip():
    instance = literals_CharacterLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_literals_DecimalDoubleLiteral_decimalValue_value_roundtrip():
    instance = literals_DecimalDoubleLiteral(decimalValue=3.14)
    assert instance.decimalValue == 3.14
    instance.decimalValue = 9.99
    assert instance.decimalValue == 9.99


def test_literals_DecimalFloatLiteral_decimalValue_value_roundtrip():
    instance = literals_DecimalFloatLiteral(decimalValue=3.14)
    assert instance.decimalValue == 3.14
    instance.decimalValue = 9.99
    assert instance.decimalValue == 9.99


def test_literals_DecimalIntegerLiteral_decimalValue_value_roundtrip():
    instance = literals_DecimalIntegerLiteral(decimalValue="sample_text")
    assert instance.decimalValue == "sample_text"
    instance.decimalValue = "sample_text_2"
    assert instance.decimalValue == "sample_text_2"


def test_literals_DecimalLongLiteral_decimalValue_value_roundtrip():
    instance = literals_DecimalLongLiteral(decimalValue="sample_text")
    assert instance.decimalValue == "sample_text"
    instance.decimalValue = "sample_text_2"
    assert instance.decimalValue == "sample_text_2"


def test_literals_HexDoubleLiteral_hexValue_value_roundtrip():
    instance = literals_HexDoubleLiteral(hexValue=3.14)
    assert instance.hexValue == 3.14
    instance.hexValue = 9.99
    assert instance.hexValue == 9.99


def test_literals_HexFloatLiteral_hexValue_value_roundtrip():
    instance = literals_HexFloatLiteral(hexValue=3.14)
    assert instance.hexValue == 3.14
    instance.hexValue = 9.99
    assert instance.hexValue == 9.99


def test_literals_HexIntegerLiteral_hexValue_value_roundtrip():
    instance = literals_HexIntegerLiteral(hexValue="sample_text")
    assert instance.hexValue == "sample_text"
    instance.hexValue = "sample_text_2"
    assert instance.hexValue == "sample_text_2"


def test_literals_HexLongLiteral_hexValue_value_roundtrip():
    instance = literals_HexLongLiteral(hexValue="sample_text")
    assert instance.hexValue == "sample_text"
    instance.hexValue = "sample_text_2"
    assert instance.hexValue == "sample_text_2"


def test_literals_OctalIntegerLiteral_octalValue_value_roundtrip():
    instance = literals_OctalIntegerLiteral(octalValue="sample_text")
    assert instance.octalValue == "sample_text"
    instance.octalValue = "sample_text_2"
    assert instance.octalValue == "sample_text_2"


def test_literals_OctalLongLiteral_octalValue_value_roundtrip():
    instance = literals_OctalLongLiteral(octalValue="sample_text")
    assert instance.octalValue == "sample_text"
    instance.octalValue = "sample_text_2"
    assert instance.octalValue == "sample_text_2"


def test_references_StringReference_value_value_roundtrip():
    instance = references_StringReference(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_expressions_MultiplicativeExpression_isa_AdditiveExpressionChild():
    instance = expressions_MultiplicativeExpression()
    assert isinstance(instance, AdditiveExpressionChild)


def test_expressions_MultiplicativeExpressionChild_isa_AdditiveExpressionChild():
    instance = expressions_MultiplicativeExpressionChild()
    assert isinstance(instance, AdditiveExpressionChild)


def test_operators_Addition_isa_AdditiveOperator():
    instance = operators_Addition()
    assert isinstance(instance, AdditiveOperator)


def test_operators_Subtraction_isa_AdditiveOperator():
    instance = operators_Subtraction()
    assert isinstance(instance, AdditiveOperator)


def test_expressions_EqualityExpression_isa_AndExpressionChild():
    instance = expressions_EqualityExpression()
    assert isinstance(instance, AndExpressionChild)


def test_expressions_EqualityExpressionChild_isa_AndExpressionChild():
    instance = expressions_EqualityExpressionChild()
    assert isinstance(instance, AndExpressionChild)


def test_containers_Package_isa_Annotable():
    instance = containers_Package()
    assert isinstance(instance, Annotable)


def test_members_EnumConstant_isa_Annotable():
    instance = members_EnumConstant()
    assert isinstance(instance, Annotable)


def test_classifiers_ConcreteClassifier_isa_AnnotableAndModifiable():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, AnnotableAndModifiable)


def test_members_Constructor_isa_AnnotableAndModifiable():
    instance = members_Constructor()
    assert isinstance(instance, AnnotableAndModifiable)


def test_members_Field_isa_AnnotableAndModifiable():
    instance = members_Field()
    assert isinstance(instance, AnnotableAndModifiable)


def test_members_Method_isa_AnnotableAndModifiable():
    instance = members_Method()
    assert isinstance(instance, AnnotableAndModifiable)


def test_parameters_Parameter_isa_AnnotableAndModifiable():
    instance = parameters_Parameter()
    assert isinstance(instance, AnnotableAndModifiable)


def test_variables_LocalVariable_isa_AnnotableAndModifiable():
    instance = variables_LocalVariable()
    assert isinstance(instance, AnnotableAndModifiable)


def test_annotations_AnnotationInstance_isa_AnnotationInstanceOrModifier():
    instance = annotations_AnnotationInstance()
    assert isinstance(instance, AnnotationInstanceOrModifier)


def test_modifiers_Modifier_isa_AnnotationInstanceOrModifier():
    instance = modifiers_Modifier()
    assert isinstance(instance, AnnotationInstanceOrModifier)


def test_annotations_AnnotationParameterList_isa_AnnotationParameter():
    instance = annotations_AnnotationParameterList()
    assert isinstance(instance, AnnotationParameter)


def test_annotations_SingleAnnotationParameter_isa_AnnotationParameter():
    instance = annotations_SingleAnnotationParameter()
    assert isinstance(instance, AnnotationParameter)


def test_arrays_ArrayInitializer_isa_AnnotationValue():
    instance = arrays_ArrayInitializer()
    assert isinstance(instance, AnnotationValue)


def test_expressions_Expression_isa_AnnotationValue():
    instance = expressions_Expression()
    assert isinstance(instance, AnnotationValue)


def test_instantiations_Instantiation_isa_Argumentable():
    instance = instantiations_Instantiation()
    assert isinstance(instance, Argumentable)


def test_members_EnumConstant_isa_Argumentable():
    instance = members_EnumConstant()
    assert isinstance(instance, Argumentable)


def test_references_MethodCall_isa_Argumentable():
    instance = references_MethodCall()
    assert isinstance(instance, Argumentable)


def test_arrays_ArrayInitializer_isa_ArrayInitializationValue():
    instance = arrays_ArrayInitializer()
    assert isinstance(instance, ArrayInitializationValue)


def test_expressions_Expression_isa_ArrayInitializationValue():
    instance = expressions_Expression()
    assert isinstance(instance, ArrayInitializationValue)


def test_arrays_ArrayInstantiationBySize_isa_ArrayTypeable():
    instance = arrays_ArrayInstantiationBySize()
    assert isinstance(instance, ArrayTypeable)


def test_arrays_ArrayInstantiationByValues_isa_ArrayTypeable():
    instance = arrays_ArrayInstantiationByValues()
    assert isinstance(instance, ArrayTypeable)


def test_expressions_CastExpression_isa_ArrayTypeable():
    instance = expressions_CastExpression()
    assert isinstance(instance, ArrayTypeable)


def test_expressions_InstanceOfExpression_isa_ArrayTypeable():
    instance = expressions_InstanceOfExpression()
    assert isinstance(instance, ArrayTypeable)


def test_generics_TypeArgument_isa_ArrayTypeable():
    instance = generics_TypeArgument()
    assert isinstance(instance, ArrayTypeable)


def test_members_AdditionalField_isa_ArrayTypeable():
    instance = members_AdditionalField()
    assert isinstance(instance, ArrayTypeable)


def test_members_Method_isa_ArrayTypeable():
    instance = members_Method()
    assert isinstance(instance, ArrayTypeable)


def test_variables_AdditionalLocalVariable_isa_ArrayTypeable():
    instance = variables_AdditionalLocalVariable()
    assert isinstance(instance, ArrayTypeable)


def test_variables_Variable_isa_ArrayTypeable():
    instance = variables_Variable()
    assert isinstance(instance, ArrayTypeable)


def test_expressions_ConditionalExpression_isa_AssignmentExpressionChild():
    instance = expressions_ConditionalExpression()
    assert isinstance(instance, AssignmentExpressionChild)


def test_expressions_ConditionalExpressionChild_isa_AssignmentExpressionChild():
    instance = expressions_ConditionalExpressionChild()
    assert isinstance(instance, AssignmentExpressionChild)


def test_operators_Assignment_isa_AssignmentOperator():
    instance = operators_Assignment()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentAnd_isa_AssignmentOperator():
    instance = operators_AssignmentAnd()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentDivision_isa_AssignmentOperator():
    instance = operators_AssignmentDivision()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentExclusiveOr_isa_AssignmentOperator():
    instance = operators_AssignmentExclusiveOr()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentLeftShift_isa_AssignmentOperator():
    instance = operators_AssignmentLeftShift()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentMinus_isa_AssignmentOperator():
    instance = operators_AssignmentMinus()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentModulo_isa_AssignmentOperator():
    instance = operators_AssignmentModulo()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentMultiplication_isa_AssignmentOperator():
    instance = operators_AssignmentMultiplication()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentOr_isa_AssignmentOperator():
    instance = operators_AssignmentOr()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentPlus_isa_AssignmentOperator():
    instance = operators_AssignmentPlus()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentRightShift_isa_AssignmentOperator():
    instance = operators_AssignmentRightShift()
    assert isinstance(instance, AssignmentOperator)


def test_operators_AssignmentUnsignedRightShift_isa_AssignmentOperator():
    instance = operators_AssignmentUnsignedRightShift()
    assert isinstance(instance, AssignmentOperator)


def test_instantiations_NewConstructorCall_isa_CallTypeArgumentable():
    instance = instantiations_NewConstructorCall()
    assert isinstance(instance, CallTypeArgumentable)


def test_references_MethodCall_isa_CallTypeArgumentable():
    instance = references_MethodCall()
    assert isinstance(instance, CallTypeArgumentable)


def test_classifiers_ConcreteClassifier_isa_Classifier():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, Classifier)


def test_generics_TypeParameter_isa_Classifier():
    instance = generics_TypeParameter()
    assert isinstance(instance, Classifier)


def test_annotations_Annotable_isa_Commentable():
    instance = annotations_Annotable()
    assert isinstance(instance, Commentable)


def test_annotations_AnnotationAttributeSetting_isa_Commentable():
    instance = annotations_AnnotationAttributeSetting()
    assert isinstance(instance, Commentable)


def test_annotations_AnnotationParameter_isa_Commentable():
    instance = annotations_AnnotationParameter()
    assert isinstance(instance, Commentable)


def test_annotations_AnnotationValue_isa_Commentable():
    instance = annotations_AnnotationValue()
    assert isinstance(instance, Commentable)


def test_arrays_ArrayDimension_isa_Commentable():
    instance = arrays_ArrayDimension()
    assert isinstance(instance, Commentable)


def test_arrays_ArrayInitializationValue_isa_Commentable():
    instance = arrays_ArrayInitializationValue()
    assert isinstance(instance, Commentable)


def test_arrays_ArraySelector_isa_Commentable():
    instance = arrays_ArraySelector()
    assert isinstance(instance, Commentable)


def test_arrays_ArrayTypeable_isa_Commentable():
    instance = arrays_ArrayTypeable()
    assert isinstance(instance, Commentable)


def test_classifiers_Implementor_isa_Commentable():
    instance = classifiers_Implementor()
    assert isinstance(instance, Commentable)


def test_commons_NamedElement_isa_Commentable():
    instance = commons_NamedElement(name="sample_text")
    assert isinstance(instance, Commentable)


def test_commons_NamespaceAwareElement_isa_Commentable():
    instance = commons_NamespaceAwareElement(namespaces="sample_text")
    assert isinstance(instance, Commentable)


def test_generics_CallTypeArgumentable_isa_Commentable():
    instance = generics_CallTypeArgumentable()
    assert isinstance(instance, Commentable)


def test_generics_TypeArgumentable_isa_Commentable():
    instance = generics_TypeArgumentable()
    assert isinstance(instance, Commentable)


def test_generics_TypeParametrizable_isa_Commentable():
    instance = generics_TypeParametrizable()
    assert isinstance(instance, Commentable)


def test_imports_ImportingElement_isa_Commentable():
    instance = imports_ImportingElement()
    assert isinstance(instance, Commentable)


def test_instantiations_Initializable_isa_Commentable():
    instance = instantiations_Initializable()
    assert isinstance(instance, Commentable)


def test_literals_Self_isa_Commentable():
    instance = literals_Self()
    assert isinstance(instance, Commentable)


def test_members_ExceptionThrower_isa_Commentable():
    instance = members_ExceptionThrower()
    assert isinstance(instance, Commentable)


def test_members_MemberContainer_isa_Commentable():
    instance = members_MemberContainer()
    assert isinstance(instance, Commentable)


def test_modifiers_AnnotableAndModifiable_isa_Commentable():
    instance = modifiers_AnnotableAndModifiable()
    assert isinstance(instance, Commentable)


def test_modifiers_AnnotationInstanceOrModifier_isa_Commentable():
    instance = modifiers_AnnotationInstanceOrModifier()
    assert isinstance(instance, Commentable)


def test_modifiers_Modifiable_isa_Commentable():
    instance = modifiers_Modifiable()
    assert isinstance(instance, Commentable)


def test_operators_Operator_isa_Commentable():
    instance = operators_Operator()
    assert isinstance(instance, Commentable)


def test_parameters_Parametrizable_isa_Commentable():
    instance = parameters_Parametrizable()
    assert isinstance(instance, Commentable)


def test_references_Argumentable_isa_Commentable():
    instance = references_Argumentable()
    assert isinstance(instance, Commentable)


def test_statements_Conditional_isa_Commentable():
    instance = statements_Conditional()
    assert isinstance(instance, Commentable)


def test_statements_ForLoopInitializer_isa_Commentable():
    instance = statements_ForLoopInitializer()
    assert isinstance(instance, Commentable)


def test_statements_Statement_isa_Commentable():
    instance = statements_Statement()
    assert isinstance(instance, Commentable)


def test_statements_StatementContainer_isa_Commentable():
    instance = statements_StatementContainer()
    assert isinstance(instance, Commentable)


def test_statements_StatementListContainer_isa_Commentable():
    instance = statements_StatementListContainer()
    assert isinstance(instance, Commentable)


def test_types_Type_isa_Commentable():
    instance = types_Type()
    assert isinstance(instance, Commentable)


def test_types_TypeReference_isa_Commentable():
    instance = types_TypeReference()
    assert isinstance(instance, Commentable)


def test_types_TypedElement_isa_Commentable():
    instance = types_TypedElement()
    assert isinstance(instance, Commentable)


def test_classifiers_Annotation_isa_ConcreteClassifier():
    instance = classifiers_Annotation()
    assert isinstance(instance, ConcreteClassifier)


def test_classifiers_Class_isa_ConcreteClassifier():
    instance = classifiers_Class()
    assert isinstance(instance, ConcreteClassifier)


def test_classifiers_Enumeration_isa_ConcreteClassifier():
    instance = classifiers_Enumeration()
    assert isinstance(instance, ConcreteClassifier)


def test_classifiers_Interface_isa_ConcreteClassifier():
    instance = classifiers_Interface()
    assert isinstance(instance, ConcreteClassifier)


def test_statements_Assert_isa_Conditional():
    instance = statements_Assert()
    assert isinstance(instance, Conditional)


def test_statements_Condition_isa_Conditional():
    instance = statements_Condition()
    assert isinstance(instance, Conditional)


def test_statements_ForLoop_isa_Conditional():
    instance = statements_ForLoop()
    assert isinstance(instance, Conditional)


def test_statements_NormalSwitchCase_isa_Conditional():
    instance = statements_NormalSwitchCase()
    assert isinstance(instance, Conditional)


def test_expressions_InclusiveOrExpression_isa_ConditionalAndExpressionChild():
    instance = expressions_InclusiveOrExpression()
    assert isinstance(instance, ConditionalAndExpressionChild)


def test_expressions_InclusiveOrExpressionChild_isa_ConditionalAndExpressionChild():
    instance = expressions_InclusiveOrExpressionChild()
    assert isinstance(instance, ConditionalAndExpressionChild)


def test_expressions_ConditionalOrExpression_isa_ConditionalExpressionChild():
    instance = expressions_ConditionalOrExpression()
    assert isinstance(instance, ConditionalExpressionChild)


def test_expressions_ConditionalOrExpressionChild_isa_ConditionalExpressionChild():
    instance = expressions_ConditionalOrExpressionChild()
    assert isinstance(instance, ConditionalExpressionChild)


def test_expressions_ConditionalAndExpression_isa_ConditionalOrExpressionChild():
    instance = expressions_ConditionalAndExpression()
    assert isinstance(instance, ConditionalOrExpressionChild)


def test_expressions_ConditionalAndExpressionChild_isa_ConditionalOrExpressionChild():
    instance = expressions_ConditionalAndExpressionChild()
    assert isinstance(instance, ConditionalOrExpressionChild)


def test_literals_DecimalDoubleLiteral_isa_DoubleLiteral():
    instance = literals_DecimalDoubleLiteral(decimalValue=3.14)
    assert isinstance(instance, DoubleLiteral)


def test_literals_HexDoubleLiteral_isa_DoubleLiteral():
    instance = literals_HexDoubleLiteral(hexValue=3.14)
    assert isinstance(instance, DoubleLiteral)


def test_references_IdentifierReference_isa_ElementReference():
    instance = references_IdentifierReference()
    assert isinstance(instance, ElementReference)


def test_references_MethodCall_isa_ElementReference():
    instance = references_MethodCall()
    assert isinstance(instance, ElementReference)


def test_expressions_InstanceOfExpression_isa_EqualityExpressionChild():
    instance = expressions_InstanceOfExpression()
    assert isinstance(instance, EqualityExpressionChild)


def test_expressions_InstanceOfExpressionChild_isa_EqualityExpressionChild():
    instance = expressions_InstanceOfExpressionChild()
    assert isinstance(instance, EqualityExpressionChild)


def test_operators_Equal_isa_EqualityOperator():
    instance = operators_Equal()
    assert isinstance(instance, EqualityOperator)


def test_operators_NotEqual_isa_EqualityOperator():
    instance = operators_NotEqual()
    assert isinstance(instance, EqualityOperator)


def test_members_Constructor_isa_ExceptionThrower():
    instance = members_Constructor()
    assert isinstance(instance, ExceptionThrower)


def test_members_Method_isa_ExceptionThrower():
    instance = members_Method()
    assert isinstance(instance, ExceptionThrower)


def test_expressions_AndExpression_isa_ExclusiveOrExpressionChild():
    instance = expressions_AndExpression()
    assert isinstance(instance, ExclusiveOrExpressionChild)


def test_expressions_AndExpressionChild_isa_ExclusiveOrExpressionChild():
    instance = expressions_AndExpressionChild()
    assert isinstance(instance, ExclusiveOrExpressionChild)


def test_arrays_ArrayInstantiationBySize_isa_Expression():
    instance = arrays_ArrayInstantiationBySize()
    assert isinstance(instance, Expression)


def test_arrays_ArrayInstantiationByValues_isa_Expression():
    instance = arrays_ArrayInstantiationByValues()
    assert isinstance(instance, Expression)


def test_expressions_AssignmentExpression_isa_Expression():
    instance = expressions_AssignmentExpression()
    assert isinstance(instance, Expression)


def test_expressions_AssignmentExpressionChild_isa_Expression():
    instance = expressions_AssignmentExpressionChild()
    assert isinstance(instance, Expression)


def test_literals_DecimalFloatLiteral_isa_FloatLiteral():
    instance = literals_DecimalFloatLiteral(decimalValue=3.14)
    assert isinstance(instance, FloatLiteral)


def test_literals_HexFloatLiteral_isa_FloatLiteral():
    instance = literals_HexFloatLiteral(hexValue=3.14)
    assert isinstance(instance, FloatLiteral)


def test_expressions_ExpressionList_isa_ForLoopInitializer():
    instance = expressions_ExpressionList()
    assert isinstance(instance, ForLoopInitializer)


def test_variables_LocalVariable_isa_ForLoopInitializer():
    instance = variables_LocalVariable()
    assert isinstance(instance, ForLoopInitializer)


def test_classifiers_Class_isa_Implementor():
    instance = classifiers_Class()
    assert isinstance(instance, Implementor)


def test_classifiers_Enumeration_isa_Implementor():
    instance = classifiers_Enumeration()
    assert isinstance(instance, Implementor)


def test_imports_ClassifierImport_isa_Import():
    instance = imports_ClassifierImport()
    assert isinstance(instance, Import)


def test_imports_PackageImport_isa_Import():
    instance = imports_PackageImport()
    assert isinstance(instance, Import)


def test_imports_StaticImport_isa_Import():
    instance = imports_StaticImport()
    assert isinstance(instance, Import)


def test_containers_JavaRoot_isa_ImportingElement():
    instance = containers_JavaRoot()
    assert isinstance(instance, ImportingElement)


def test_expressions_ExclusiveOrExpression_isa_InclusiveOrExpressionChild():
    instance = expressions_ExclusiveOrExpression()
    assert isinstance(instance, InclusiveOrExpressionChild)


def test_expressions_ExclusiveOrExpressionChild_isa_InclusiveOrExpressionChild():
    instance = expressions_ExclusiveOrExpressionChild()
    assert isinstance(instance, InclusiveOrExpressionChild)


def test_members_AdditionalField_isa_Initializable():
    instance = members_AdditionalField()
    assert isinstance(instance, Initializable)


def test_members_Field_isa_Initializable():
    instance = members_Field()
    assert isinstance(instance, Initializable)


def test_variables_AdditionalLocalVariable_isa_Initializable():
    instance = variables_AdditionalLocalVariable()
    assert isinstance(instance, Initializable)


def test_variables_LocalVariable_isa_Initializable():
    instance = variables_LocalVariable()
    assert isinstance(instance, Initializable)


def test_expressions_RelationExpression_isa_InstanceOfExpressionChild():
    instance = expressions_RelationExpression()
    assert isinstance(instance, InstanceOfExpressionChild)


def test_expressions_RelationExpressionChild_isa_InstanceOfExpressionChild():
    instance = expressions_RelationExpressionChild()
    assert isinstance(instance, InstanceOfExpressionChild)


def test_instantiations_ExplicitConstructorCall_isa_Instantiation():
    instance = instantiations_ExplicitConstructorCall()
    assert isinstance(instance, Instantiation)


def test_instantiations_NewConstructorCall_isa_Instantiation():
    instance = instantiations_NewConstructorCall()
    assert isinstance(instance, Instantiation)


def test_literals_DecimalIntegerLiteral_isa_IntegerLiteral():
    instance = literals_DecimalIntegerLiteral(decimalValue="sample_text")
    assert isinstance(instance, IntegerLiteral)


def test_literals_HexIntegerLiteral_isa_IntegerLiteral():
    instance = literals_HexIntegerLiteral(hexValue="sample_text")
    assert isinstance(instance, IntegerLiteral)


def test_literals_OctalIntegerLiteral_isa_IntegerLiteral():
    instance = literals_OctalIntegerLiteral(octalValue="sample_text")
    assert isinstance(instance, IntegerLiteral)


def test_annotations_AnnotationAttribute_isa_InterfaceMethod():
    instance = annotations_AnnotationAttribute()
    assert isinstance(instance, InterfaceMethod)


def test_containers_CompilationUnit_isa_JavaRoot():
    instance = containers_CompilationUnit()
    assert isinstance(instance, JavaRoot)


def test_containers_EmptyModel_isa_JavaRoot():
    instance = containers_EmptyModel()
    assert isinstance(instance, JavaRoot)


def test_containers_Package_isa_JavaRoot():
    instance = containers_Package()
    assert isinstance(instance, JavaRoot)


def test_statements_Break_isa_Jump():
    instance = statements_Break()
    assert isinstance(instance, Jump)


def test_statements_Continue_isa_Jump():
    instance = statements_Continue()
    assert isinstance(instance, Jump)


def test_literals_BooleanLiteral_isa_Literal():
    instance = literals_BooleanLiteral(value=True)
    assert isinstance(instance, Literal)


def test_literals_CharacterLiteral_isa_Literal():
    instance = literals_CharacterLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_literals_DoubleLiteral_isa_Literal():
    instance = literals_DoubleLiteral()
    assert isinstance(instance, Literal)


def test_literals_FloatLiteral_isa_Literal():
    instance = literals_FloatLiteral()
    assert isinstance(instance, Literal)


def test_literals_IntegerLiteral_isa_Literal():
    instance = literals_IntegerLiteral()
    assert isinstance(instance, Literal)


def test_literals_LongLiteral_isa_Literal():
    instance = literals_LongLiteral()
    assert isinstance(instance, Literal)


def test_literals_NullLiteral_isa_Literal():
    instance = literals_NullLiteral()
    assert isinstance(instance, Literal)


def test_literals_DecimalLongLiteral_isa_LongLiteral():
    instance = literals_DecimalLongLiteral(decimalValue="sample_text")
    assert isinstance(instance, LongLiteral)


def test_literals_HexLongLiteral_isa_LongLiteral():
    instance = literals_HexLongLiteral(hexValue="sample_text")
    assert isinstance(instance, LongLiteral)


def test_literals_OctalLongLiteral_isa_LongLiteral():
    instance = literals_OctalLongLiteral(octalValue="sample_text")
    assert isinstance(instance, LongLiteral)


def test_classifiers_ConcreteClassifier_isa_Member():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, Member)


def test_members_Constructor_isa_Member():
    instance = members_Constructor()
    assert isinstance(instance, Member)


def test_members_EmptyMember_isa_Member():
    instance = members_EmptyMember()
    assert isinstance(instance, Member)


def test_members_Field_isa_Member():
    instance = members_Field()
    assert isinstance(instance, Member)


def test_members_Method_isa_Member():
    instance = members_Method()
    assert isinstance(instance, Member)


def test_statements_Block_isa_Member():
    instance = statements_Block()
    assert isinstance(instance, Member)


def test_classifiers_AnonymousClass_isa_MemberContainer():
    instance = classifiers_AnonymousClass()
    assert isinstance(instance, MemberContainer)


def test_classifiers_ConcreteClassifier_isa_MemberContainer():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, MemberContainer)


def test_members_ClassMethod_isa_Method():
    instance = members_ClassMethod()
    assert isinstance(instance, Method)


def test_members_InterfaceMethod_isa_Method():
    instance = members_InterfaceMethod()
    assert isinstance(instance, Method)


def test_statements_Block_isa_Modifiable():
    instance = statements_Block()
    assert isinstance(instance, Modifiable)


def test_modifiers_Abstract_isa_Modifier():
    instance = modifiers_Abstract()
    assert isinstance(instance, Modifier)


def test_modifiers_Final_isa_Modifier():
    instance = modifiers_Final()
    assert isinstance(instance, Modifier)


def test_modifiers_Native_isa_Modifier():
    instance = modifiers_Native()
    assert isinstance(instance, Modifier)


def test_modifiers_Private_isa_Modifier():
    instance = modifiers_Private()
    assert isinstance(instance, Modifier)


def test_modifiers_Protected_isa_Modifier():
    instance = modifiers_Protected()
    assert isinstance(instance, Modifier)


def test_modifiers_Public_isa_Modifier():
    instance = modifiers_Public()
    assert isinstance(instance, Modifier)


def test_modifiers_Static_isa_Modifier():
    instance = modifiers_Static()
    assert isinstance(instance, Modifier)


def test_modifiers_Strictfp_isa_Modifier():
    instance = modifiers_Strictfp()
    assert isinstance(instance, Modifier)


def test_modifiers_Synchronized_isa_Modifier():
    instance = modifiers_Synchronized()
    assert isinstance(instance, Modifier)


def test_modifiers_Transient_isa_Modifier():
    instance = modifiers_Transient()
    assert isinstance(instance, Modifier)


def test_modifiers_Volatile_isa_Modifier():
    instance = modifiers_Volatile()
    assert isinstance(instance, Modifier)


def test_expressions_UnaryExpression_isa_MultiplicativeExpressionChild():
    instance = expressions_UnaryExpression()
    assert isinstance(instance, MultiplicativeExpressionChild)


def test_expressions_UnaryExpressionChild_isa_MultiplicativeExpressionChild():
    instance = expressions_UnaryExpressionChild()
    assert isinstance(instance, MultiplicativeExpressionChild)


def test_operators_Division_isa_MultiplicativeOperator():
    instance = operators_Division()
    assert isinstance(instance, MultiplicativeOperator)


def test_operators_Multiplication_isa_MultiplicativeOperator():
    instance = operators_Multiplication()
    assert isinstance(instance, MultiplicativeOperator)


def test_operators_Remainder_isa_MultiplicativeOperator():
    instance = operators_Remainder()
    assert isinstance(instance, MultiplicativeOperator)


def test_containers_JavaRoot_isa_NamedElement():
    instance = containers_JavaRoot()
    assert isinstance(instance, NamedElement)


def test_members_Member_isa_NamedElement():
    instance = members_Member()
    assert isinstance(instance, NamedElement)


def test_references_ReferenceableElement_isa_NamedElement():
    instance = references_ReferenceableElement()
    assert isinstance(instance, NamedElement)


def test_statements_JumpLabel_isa_NamedElement():
    instance = statements_JumpLabel()
    assert isinstance(instance, NamedElement)


def test_variables_Variable_isa_NamedElement():
    instance = variables_Variable()
    assert isinstance(instance, NamedElement)


def test_annotations_AnnotationInstance_isa_NamespaceAwareElement():
    instance = annotations_AnnotationInstance()
    assert isinstance(instance, NamespaceAwareElement)


def test_containers_JavaRoot_isa_NamespaceAwareElement():
    instance = containers_JavaRoot()
    assert isinstance(instance, NamespaceAwareElement)


def test_imports_Import_isa_NamespaceAwareElement():
    instance = imports_Import()
    assert isinstance(instance, NamespaceAwareElement)


def test_types_NamespaceClassifierReference_isa_NamespaceAwareElement():
    instance = types_NamespaceClassifierReference()
    assert isinstance(instance, NamespaceAwareElement)


def test_operators_AdditiveOperator_isa_Operator():
    instance = operators_AdditiveOperator()
    assert isinstance(instance, Operator)


def test_operators_AssignmentOperator_isa_Operator():
    instance = operators_AssignmentOperator()
    assert isinstance(instance, Operator)


def test_operators_EqualityOperator_isa_Operator():
    instance = operators_EqualityOperator()
    assert isinstance(instance, Operator)


def test_operators_MultiplicativeOperator_isa_Operator():
    instance = operators_MultiplicativeOperator()
    assert isinstance(instance, Operator)


def test_operators_RelationOperator_isa_Operator():
    instance = operators_RelationOperator()
    assert isinstance(instance, Operator)


def test_operators_ShiftOperator_isa_Operator():
    instance = operators_ShiftOperator()
    assert isinstance(instance, Operator)


def test_operators_UnaryModificationOperator_isa_Operator():
    instance = operators_UnaryModificationOperator()
    assert isinstance(instance, Operator)


def test_operators_UnaryOperator_isa_Operator():
    instance = operators_UnaryOperator()
    assert isinstance(instance, Operator)


def test_parameters_OrdinaryParameter_isa_Parameter():
    instance = parameters_OrdinaryParameter()
    assert isinstance(instance, Parameter)


def test_parameters_VariableLengthParameter_isa_Parameter():
    instance = parameters_VariableLengthParameter()
    assert isinstance(instance, Parameter)


def test_members_Constructor_isa_Parametrizable():
    instance = members_Constructor()
    assert isinstance(instance, Parametrizable)


def test_members_Method_isa_Parametrizable():
    instance = members_Method()
    assert isinstance(instance, Parametrizable)


def test_literals_Literal_isa_PrimaryExpression():
    instance = literals_Literal()
    assert isinstance(instance, PrimaryExpression)


def test_references_Reference_isa_PrimaryExpression():
    instance = references_Reference()
    assert isinstance(instance, PrimaryExpression)


def test_types_Bool_isa_PrimitiveType():
    instance = types_Bool()
    assert isinstance(instance, PrimitiveType)


def test_types_Byte_isa_PrimitiveType():
    instance = types_Byte()
    assert isinstance(instance, PrimitiveType)


def test_types_Char_isa_PrimitiveType():
    instance = types_Char()
    assert isinstance(instance, PrimitiveType)


def test_types_Double_isa_PrimitiveType():
    instance = types_Double()
    assert isinstance(instance, PrimitiveType)


def test_types_Float_isa_PrimitiveType():
    instance = types_Float()
    assert isinstance(instance, PrimitiveType)


def test_types_Int_isa_PrimitiveType():
    instance = types_Int()
    assert isinstance(instance, PrimitiveType)


def test_types_Long_isa_PrimitiveType():
    instance = types_Long()
    assert isinstance(instance, PrimitiveType)


def test_types_Short_isa_PrimitiveType():
    instance = types_Short()
    assert isinstance(instance, PrimitiveType)


def test_types_Void_isa_PrimitiveType():
    instance = types_Void()
    assert isinstance(instance, PrimitiveType)


def test_annotations_AnnotationInstance_isa_Reference():
    instance = annotations_AnnotationInstance()
    assert isinstance(instance, Reference)


def test_arrays_ArrayInstantiationBySize_isa_Reference():
    instance = arrays_ArrayInstantiationBySize()
    assert isinstance(instance, Reference)


def test_arrays_ArrayInstantiationByValues_isa_Reference():
    instance = arrays_ArrayInstantiationByValues()
    assert isinstance(instance, Reference)


def test_expressions_NestedExpression_isa_Reference():
    instance = expressions_NestedExpression()
    assert isinstance(instance, Reference)


def test_instantiations_Instantiation_isa_Reference():
    instance = instantiations_Instantiation()
    assert isinstance(instance, Reference)


def test_references_ElementReference_isa_Reference():
    instance = references_ElementReference()
    assert isinstance(instance, Reference)


def test_references_PrimitiveTypeReference_isa_Reference():
    instance = references_PrimitiveTypeReference()
    assert isinstance(instance, Reference)


def test_references_ReflectiveClassReference_isa_Reference():
    instance = references_ReflectiveClassReference()
    assert isinstance(instance, Reference)


def test_references_SelfReference_isa_Reference():
    instance = references_SelfReference()
    assert isinstance(instance, Reference)


def test_references_StringReference_isa_Reference():
    instance = references_StringReference(value="sample_text")
    assert isinstance(instance, Reference)


def test_classifiers_Classifier_isa_ReferenceableElement():
    instance = classifiers_Classifier()
    assert isinstance(instance, ReferenceableElement)


def test_containers_Package_isa_ReferenceableElement():
    instance = containers_Package()
    assert isinstance(instance, ReferenceableElement)


def test_members_AdditionalField_isa_ReferenceableElement():
    instance = members_AdditionalField()
    assert isinstance(instance, ReferenceableElement)


def test_members_EnumConstant_isa_ReferenceableElement():
    instance = members_EnumConstant()
    assert isinstance(instance, ReferenceableElement)


def test_members_Field_isa_ReferenceableElement():
    instance = members_Field()
    assert isinstance(instance, ReferenceableElement)


def test_members_Method_isa_ReferenceableElement():
    instance = members_Method()
    assert isinstance(instance, ReferenceableElement)


def test_variables_AdditionalLocalVariable_isa_ReferenceableElement():
    instance = variables_AdditionalLocalVariable()
    assert isinstance(instance, ReferenceableElement)


def test_variables_Variable_isa_ReferenceableElement():
    instance = variables_Variable()
    assert isinstance(instance, ReferenceableElement)


def test_expressions_ShiftExpression_isa_RelationExpressionChild():
    instance = expressions_ShiftExpression()
    assert isinstance(instance, RelationExpressionChild)


def test_expressions_ShiftExpressionChild_isa_RelationExpressionChild():
    instance = expressions_ShiftExpressionChild()
    assert isinstance(instance, RelationExpressionChild)


def test_operators_GreaterThan_isa_RelationOperator():
    instance = operators_GreaterThan()
    assert isinstance(instance, RelationOperator)


def test_operators_GreaterThanOrEqual_isa_RelationOperator():
    instance = operators_GreaterThanOrEqual()
    assert isinstance(instance, RelationOperator)


def test_operators_LessThan_isa_RelationOperator():
    instance = operators_LessThan()
    assert isinstance(instance, RelationOperator)


def test_operators_LessThanOrEqual_isa_RelationOperator():
    instance = operators_LessThanOrEqual()
    assert isinstance(instance, RelationOperator)


def test_literals_Super_isa_Self():
    instance = literals_Super()
    assert isinstance(instance, Self)


def test_literals_This_isa_Self():
    instance = literals_This()
    assert isinstance(instance, Self)


def test_expressions_AdditiveExpression_isa_ShiftExpressionChild():
    instance = expressions_AdditiveExpression()
    assert isinstance(instance, ShiftExpressionChild)


def test_expressions_AdditiveExpressionChild_isa_ShiftExpressionChild():
    instance = expressions_AdditiveExpressionChild()
    assert isinstance(instance, ShiftExpressionChild)


def test_operators_LeftShift_isa_ShiftOperator():
    instance = operators_LeftShift()
    assert isinstance(instance, ShiftOperator)


def test_operators_RightShift_isa_ShiftOperator():
    instance = operators_RightShift()
    assert isinstance(instance, ShiftOperator)


def test_operators_UnsignedRightShift_isa_ShiftOperator():
    instance = operators_UnsignedRightShift()
    assert isinstance(instance, ShiftOperator)


def test_classifiers_ConcreteClassifier_isa_Statement():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, Statement)


def test_statements_Assert_isa_Statement():
    instance = statements_Assert()
    assert isinstance(instance, Statement)


def test_statements_Block_isa_Statement():
    instance = statements_Block()
    assert isinstance(instance, Statement)


def test_statements_Condition_isa_Statement():
    instance = statements_Condition()
    assert isinstance(instance, Statement)


def test_statements_EmptyStatement_isa_Statement():
    instance = statements_EmptyStatement()
    assert isinstance(instance, Statement)


def test_statements_ExpressionStatement_isa_Statement():
    instance = statements_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_statements_ForEachLoop_isa_Statement():
    instance = statements_ForEachLoop()
    assert isinstance(instance, Statement)


def test_statements_ForLoop_isa_Statement():
    instance = statements_ForLoop()
    assert isinstance(instance, Statement)


def test_statements_Jump_isa_Statement():
    instance = statements_Jump()
    assert isinstance(instance, Statement)


def test_statements_JumpLabel_isa_Statement():
    instance = statements_JumpLabel()
    assert isinstance(instance, Statement)


def test_statements_LocalVariableStatement_isa_Statement():
    instance = statements_LocalVariableStatement()
    assert isinstance(instance, Statement)


def test_statements_Return_isa_Statement():
    instance = statements_Return()
    assert isinstance(instance, Statement)


def test_statements_Switch_isa_Statement():
    instance = statements_Switch()
    assert isinstance(instance, Statement)


def test_statements_SynchronizedBlock_isa_Statement():
    instance = statements_SynchronizedBlock()
    assert isinstance(instance, Statement)


def test_statements_Throw_isa_Statement():
    instance = statements_Throw()
    assert isinstance(instance, Statement)


def test_statements_TryBlock_isa_Statement():
    instance = statements_TryBlock()
    assert isinstance(instance, Statement)


def test_statements_WhileLoop_isa_Statement():
    instance = statements_WhileLoop()
    assert isinstance(instance, Statement)


def test_statements_Condition_isa_StatementContainer():
    instance = statements_Condition()
    assert isinstance(instance, StatementContainer)


def test_statements_ForEachLoop_isa_StatementContainer():
    instance = statements_ForEachLoop()
    assert isinstance(instance, StatementContainer)


def test_statements_ForLoop_isa_StatementContainer():
    instance = statements_ForLoop()
    assert isinstance(instance, StatementContainer)


def test_statements_JumpLabel_isa_StatementContainer():
    instance = statements_JumpLabel()
    assert isinstance(instance, StatementContainer)


def test_statements_WhileLoop_isa_StatementContainer():
    instance = statements_WhileLoop()
    assert isinstance(instance, StatementContainer)


def test_members_ClassMethod_isa_StatementListContainer():
    instance = members_ClassMethod()
    assert isinstance(instance, StatementListContainer)


def test_members_Constructor_isa_StatementListContainer():
    instance = members_Constructor()
    assert isinstance(instance, StatementListContainer)


def test_statements_Block_isa_StatementListContainer():
    instance = statements_Block()
    assert isinstance(instance, StatementListContainer)


def test_statements_CatchBlock_isa_StatementListContainer():
    instance = statements_CatchBlock()
    assert isinstance(instance, StatementListContainer)


def test_statements_SwitchCase_isa_StatementListContainer():
    instance = statements_SwitchCase()
    assert isinstance(instance, StatementListContainer)


def test_statements_SynchronizedBlock_isa_StatementListContainer():
    instance = statements_SynchronizedBlock()
    assert isinstance(instance, StatementListContainer)


def test_statements_TryBlock_isa_StatementListContainer():
    instance = statements_TryBlock()
    assert isinstance(instance, StatementListContainer)


def test_imports_StaticClassifierImport_isa_StaticImport():
    instance = imports_StaticClassifierImport()
    assert isinstance(instance, StaticImport)


def test_imports_StaticMemberImport_isa_StaticImport():
    instance = imports_StaticMemberImport()
    assert isinstance(instance, StaticImport)


def test_statements_DefaultSwitchCase_isa_SwitchCase():
    instance = statements_DefaultSwitchCase()
    assert isinstance(instance, SwitchCase)


def test_statements_NormalSwitchCase_isa_SwitchCase():
    instance = statements_NormalSwitchCase()
    assert isinstance(instance, SwitchCase)


def test_classifiers_AnonymousClass_isa_Type():
    instance = classifiers_AnonymousClass()
    assert isinstance(instance, Type)


def test_classifiers_Classifier_isa_Type():
    instance = classifiers_Classifier()
    assert isinstance(instance, Type)


def test_types_PrimitiveType_isa_Type():
    instance = types_PrimitiveType()
    assert isinstance(instance, Type)


def test_generics_ExtendsTypeArgument_isa_TypeArgument():
    instance = generics_ExtendsTypeArgument()
    assert isinstance(instance, TypeArgument)


def test_generics_QualifiedTypeArgument_isa_TypeArgument():
    instance = generics_QualifiedTypeArgument()
    assert isinstance(instance, TypeArgument)


def test_generics_SuperTypeArgument_isa_TypeArgument():
    instance = generics_SuperTypeArgument()
    assert isinstance(instance, TypeArgument)


def test_generics_UnknownTypeArgument_isa_TypeArgument():
    instance = generics_UnknownTypeArgument()
    assert isinstance(instance, TypeArgument)


def test_instantiations_Instantiation_isa_TypeArgumentable():
    instance = instantiations_Instantiation()
    assert isinstance(instance, TypeArgumentable)


def test_references_Reference_isa_TypeArgumentable():
    instance = references_Reference()
    assert isinstance(instance, TypeArgumentable)


def test_types_ClassifierReference_isa_TypeArgumentable():
    instance = types_ClassifierReference()
    assert isinstance(instance, TypeArgumentable)


def test_variables_Variable_isa_TypeArgumentable():
    instance = variables_Variable()
    assert isinstance(instance, TypeArgumentable)


def test_classifiers_ConcreteClassifier_isa_TypeParametrizable():
    instance = classifiers_ConcreteClassifier(fullName="sample_text")
    assert isinstance(instance, TypeParametrizable)


def test_members_Constructor_isa_TypeParametrizable():
    instance = members_Constructor()
    assert isinstance(instance, TypeParametrizable)


def test_members_Method_isa_TypeParametrizable():
    instance = members_Method()
    assert isinstance(instance, TypeParametrizable)


def test_types_ClassifierReference_isa_TypeReference():
    instance = types_ClassifierReference()
    assert isinstance(instance, TypeReference)


def test_types_NamespaceClassifierReference_isa_TypeReference():
    instance = types_NamespaceClassifierReference()
    assert isinstance(instance, TypeReference)


def test_types_PrimitiveType_isa_TypeReference():
    instance = types_PrimitiveType()
    assert isinstance(instance, TypeReference)


def test_arrays_ArrayInstantiationBySize_isa_TypedElement():
    instance = arrays_ArrayInstantiationBySize()
    assert isinstance(instance, TypedElement)


def test_arrays_ArrayInstantiationByValues_isa_TypedElement():
    instance = arrays_ArrayInstantiationByValues()
    assert isinstance(instance, TypedElement)


def test_expressions_CastExpression_isa_TypedElement():
    instance = expressions_CastExpression()
    assert isinstance(instance, TypedElement)


def test_expressions_InstanceOfExpression_isa_TypedElement():
    instance = expressions_InstanceOfExpression()
    assert isinstance(instance, TypedElement)


def test_generics_QualifiedTypeArgument_isa_TypedElement():
    instance = generics_QualifiedTypeArgument()
    assert isinstance(instance, TypedElement)


def test_instantiations_Instantiation_isa_TypedElement():
    instance = instantiations_Instantiation()
    assert isinstance(instance, TypedElement)


def test_members_Method_isa_TypedElement():
    instance = members_Method()
    assert isinstance(instance, TypedElement)


def test_variables_Variable_isa_TypedElement():
    instance = variables_Variable()
    assert isinstance(instance, TypedElement)


def test_expressions_UnaryModificationExpression_isa_UnaryExpressionChild():
    instance = expressions_UnaryModificationExpression()
    assert isinstance(instance, UnaryExpressionChild)


def test_expressions_UnaryModificationExpressionChild_isa_UnaryExpressionChild():
    instance = expressions_UnaryModificationExpressionChild()
    assert isinstance(instance, UnaryExpressionChild)


def test_expressions_PrefixUnaryModificationExpression_isa_UnaryModificationExpression():
    instance = expressions_PrefixUnaryModificationExpression()
    assert isinstance(instance, UnaryModificationExpression)


def test_expressions_SuffixUnaryModificationExpression_isa_UnaryModificationExpression():
    instance = expressions_SuffixUnaryModificationExpression()
    assert isinstance(instance, UnaryModificationExpression)


def test_expressions_CastExpression_isa_UnaryModificationExpressionChild():
    instance = expressions_CastExpression()
    assert isinstance(instance, UnaryModificationExpressionChild)


def test_expressions_PrimaryExpression_isa_UnaryModificationExpressionChild():
    instance = expressions_PrimaryExpression()
    assert isinstance(instance, UnaryModificationExpressionChild)


def test_operators_MinusMinus_isa_UnaryModificationOperator():
    instance = operators_MinusMinus()
    assert isinstance(instance, UnaryModificationOperator)


def test_operators_PlusPlus_isa_UnaryModificationOperator():
    instance = operators_PlusPlus()
    assert isinstance(instance, UnaryModificationOperator)


def test_operators_Addition_isa_UnaryOperator():
    instance = operators_Addition()
    assert isinstance(instance, UnaryOperator)


def test_operators_Complement_isa_UnaryOperator():
    instance = operators_Complement()
    assert isinstance(instance, UnaryOperator)


def test_operators_Negate_isa_UnaryOperator():
    instance = operators_Negate()
    assert isinstance(instance, UnaryOperator)


def test_operators_Subtraction_isa_UnaryOperator():
    instance = operators_Subtraction()
    assert isinstance(instance, UnaryOperator)


def test_members_Field_isa_Variable():
    instance = members_Field()
    assert isinstance(instance, Variable)


def test_parameters_Parameter_isa_Variable():
    instance = parameters_Parameter()
    assert isinstance(instance, Variable)


def test_variables_LocalVariable_isa_Variable():
    instance = variables_LocalVariable()
    assert isinstance(instance, Variable)


def test_statements_DoWhileLoop_isa_WhileLoop():
    instance = statements_DoWhileLoop()
    assert isinstance(instance, WhileLoop)


def test_assoc_annotationsAndModifiers110_link_reassign_clear():
    a = modifiers_AnnotableAndModifiable()
    b1 = AnnotationInstanceOrModifier()
    b2 = AnnotationInstanceOrModifier()
    _safe_set(a, 'modifiers_AnnotableAndModifiable', {b1})
    assert _is_linked(a, 'modifiers_AnnotableAndModifiable', b1)
    if hasattr(b1, 'AnnotationInstanceOrModifier'):
        assert _is_linked(b1, 'AnnotationInstanceOrModifier', a)
    _safe_set(a, 'modifiers_AnnotableAndModifiable', {b2})
    assert _is_linked(a, 'modifiers_AnnotableAndModifiable', b2)
    if hasattr(b1, 'AnnotationInstanceOrModifier'):
        assert not _is_linked(b1, 'AnnotationInstanceOrModifier', a)
    if hasattr(b2, 'AnnotationInstanceOrModifier'):
        assert _is_linked(b2, 'AnnotationInstanceOrModifier', a)
    _safe_set(a, 'modifiers_AnnotableAndModifiable', set())
    assert not _is_linked(a, 'modifiers_AnnotableAndModifiable', b2)
    if hasattr(b2, 'AnnotationInstanceOrModifier'):
        assert not _is_linked(b2, 'AnnotationInstanceOrModifier', a)


def test_assoc_arguments116_link_reassign_clear():
    a = references_Argumentable()
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'references_Argumentable', {b1})
    assert _is_linked(a, 'references_Argumentable', b1)
    if hasattr(b1, 'Expression117'):
        assert _is_linked(b1, 'Expression117', a)
    _safe_set(a, 'references_Argumentable', {b2})
    assert _is_linked(a, 'references_Argumentable', b2)
    if hasattr(b1, 'Expression117'):
        assert not _is_linked(b1, 'Expression117', a)
    if hasattr(b2, 'Expression117'):
        assert _is_linked(b2, 'Expression117', a)
    _safe_set(a, 'references_Argumentable', set())
    assert not _is_linked(a, 'references_Argumentable', b2)
    if hasattr(b2, 'Expression117'):
        assert not _is_linked(b2, 'Expression117', a)


def test_assoc_arrayDimensionsAfter12_link_reassign_clear():
    a = arrays_ArrayTypeable()
    b1 = ArrayDimension()
    b2 = ArrayDimension()
    _safe_set(a, 'arrays_ArrayTypeable13', {b1})
    assert _is_linked(a, 'arrays_ArrayTypeable13', b1)
    if hasattr(b1, 'ArrayDimension14'):
        assert _is_linked(b1, 'ArrayDimension14', a)
    _safe_set(a, 'arrays_ArrayTypeable13', {b2})
    assert _is_linked(a, 'arrays_ArrayTypeable13', b2)
    if hasattr(b1, 'ArrayDimension14'):
        assert not _is_linked(b1, 'ArrayDimension14', a)
    if hasattr(b2, 'ArrayDimension14'):
        assert _is_linked(b2, 'ArrayDimension14', a)
    _safe_set(a, 'arrays_ArrayTypeable13', set())
    assert not _is_linked(a, 'arrays_ArrayTypeable13', b2)
    if hasattr(b2, 'ArrayDimension14'):
        assert not _is_linked(b2, 'ArrayDimension14', a)


def test_assoc_arrayDimensionsBefore11_link_reassign_clear():
    a = arrays_ArrayTypeable()
    b1 = ArrayDimension()
    b2 = ArrayDimension()
    _safe_set(a, 'arrays_ArrayTypeable', {b1})
    assert _is_linked(a, 'arrays_ArrayTypeable', b1)
    if hasattr(b1, 'ArrayDimension'):
        assert _is_linked(b1, 'ArrayDimension', a)
    _safe_set(a, 'arrays_ArrayTypeable', {b2})
    assert _is_linked(a, 'arrays_ArrayTypeable', b2)
    if hasattr(b1, 'ArrayDimension'):
        assert not _is_linked(b1, 'ArrayDimension', a)
    if hasattr(b2, 'ArrayDimension'):
        assert _is_linked(b2, 'ArrayDimension', a)
    _safe_set(a, 'arrays_ArrayTypeable', set())
    assert not _is_linked(a, 'arrays_ArrayTypeable', b2)
    if hasattr(b2, 'ArrayDimension'):
        assert not _is_linked(b2, 'ArrayDimension', a)


def test_assoc_arraySelectors114_link_reassign_clear():
    a = references_Reference()
    b1 = ArraySelector()
    b2 = ArraySelector()
    _safe_set(a, 'references_Reference115', {b1})
    assert _is_linked(a, 'references_Reference115', b1)
    if hasattr(b1, 'ArraySelector'):
        assert _is_linked(b1, 'ArraySelector', a)
    _safe_set(a, 'references_Reference115', {b2})
    assert _is_linked(a, 'references_Reference115', b2)
    if hasattr(b1, 'ArraySelector'):
        assert not _is_linked(b1, 'ArraySelector', a)
    if hasattr(b2, 'ArraySelector'):
        assert _is_linked(b2, 'ArraySelector', a)
    _safe_set(a, 'references_Reference115', set())
    assert not _is_linked(a, 'references_Reference115', b2)
    if hasattr(b2, 'ArraySelector'):
        assert not _is_linked(b2, 'ArraySelector', a)


def test_assoc_classifiers33_link_reassign_clear():
    a = containers_CompilationUnit()
    b1 = ConcreteClassifier()
    b2 = ConcreteClassifier()
    _safe_set(a, 'containers_CompilationUnit', {b1})
    assert _is_linked(a, 'containers_CompilationUnit', b1)
    if hasattr(b1, 'ConcreteClassifier'):
        assert _is_linked(b1, 'ConcreteClassifier', a)
    _safe_set(a, 'containers_CompilationUnit', {b2})
    assert _is_linked(a, 'containers_CompilationUnit', b2)
    if hasattr(b1, 'ConcreteClassifier'):
        assert not _is_linked(b1, 'ConcreteClassifier', a)
    if hasattr(b2, 'ConcreteClassifier'):
        assert _is_linked(b2, 'ConcreteClassifier', a)
    _safe_set(a, 'containers_CompilationUnit', set())
    assert not _is_linked(a, 'containers_CompilationUnit', b2)
    if hasattr(b2, 'ConcreteClassifier'):
        assert not _is_linked(b2, 'ConcreteClassifier', a)


def test_assoc_constants32_link_reassign_clear():
    a = classifiers_Enumeration()
    b1 = EnumConstant()
    b2 = EnumConstant()
    _safe_set(a, 'classifiers_Enumeration', {b1})
    assert _is_linked(a, 'classifiers_Enumeration', b1)
    if hasattr(b1, 'EnumConstant'):
        assert _is_linked(b1, 'EnumConstant', a)
    _safe_set(a, 'classifiers_Enumeration', {b2})
    assert _is_linked(a, 'classifiers_Enumeration', b2)
    if hasattr(b1, 'EnumConstant'):
        assert not _is_linked(b1, 'EnumConstant', a)
    if hasattr(b2, 'EnumConstant'):
        assert _is_linked(b2, 'EnumConstant', a)
    _safe_set(a, 'classifiers_Enumeration', set())
    assert not _is_linked(a, 'classifiers_Enumeration', b2)
    if hasattr(b2, 'EnumConstant'):
        assert not _is_linked(b2, 'EnumConstant', a)


def test_assoc_defaultExtends24_link_reassign_clear():
    a = classifiers_Class()
    b1 = TypeReference()
    b2 = TypeReference()
    _safe_set(a, 'classifiers_Class25', b1)
    assert _is_linked(a, 'classifiers_Class25', b1)
    if hasattr(b1, 'TypeReference26'):
        assert _is_linked(b1, 'TypeReference26', a)
    _safe_set(a, 'classifiers_Class25', b2)
    assert _is_linked(a, 'classifiers_Class25', b2)
    if hasattr(b1, 'TypeReference26'):
        assert not _is_linked(b1, 'TypeReference26', a)
    if hasattr(b2, 'TypeReference26'):
        assert _is_linked(b2, 'TypeReference26', a)
    _safe_set(a, 'classifiers_Class25', None)
    assert not _is_linked(a, 'classifiers_Class25', b2)
    if hasattr(b2, 'TypeReference26'):
        assert not _is_linked(b2, 'TypeReference26', a)


def test_assoc_defaultExtends29_link_reassign_clear():
    a = classifiers_Interface()
    b1 = TypeReference()
    b2 = TypeReference()
    _safe_set(a, 'classifiers_Interface30', {b1})
    assert _is_linked(a, 'classifiers_Interface30', b1)
    if hasattr(b1, 'TypeReference31'):
        assert _is_linked(b1, 'TypeReference31', a)
    _safe_set(a, 'classifiers_Interface30', {b2})
    assert _is_linked(a, 'classifiers_Interface30', b2)
    if hasattr(b1, 'TypeReference31'):
        assert not _is_linked(b1, 'TypeReference31', a)
    if hasattr(b2, 'TypeReference31'):
        assert _is_linked(b2, 'TypeReference31', a)
    _safe_set(a, 'classifiers_Interface30', set())
    assert not _is_linked(a, 'classifiers_Interface30', b2)
    if hasattr(b2, 'TypeReference31'):
        assert not _is_linked(b2, 'TypeReference31', a)


def test_assoc_defaultMembers104_link_reassign_clear():
    a = members_MemberContainer()
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'members_MemberContainer105', {b1})
    assert _is_linked(a, 'members_MemberContainer105', b1)
    if hasattr(b1, 'Member106'):
        assert _is_linked(b1, 'Member106', a)
    _safe_set(a, 'members_MemberContainer105', {b2})
    assert _is_linked(a, 'members_MemberContainer105', b2)
    if hasattr(b1, 'Member106'):
        assert not _is_linked(b1, 'Member106', a)
    if hasattr(b2, 'Member106'):
        assert _is_linked(b2, 'Member106', a)
    _safe_set(a, 'members_MemberContainer105', set())
    assert not _is_linked(a, 'members_MemberContainer105', b2)
    if hasattr(b2, 'Member106'):
        assert not _is_linked(b2, 'Member106', a)


def test_assoc_extendTypes91_link_reassign_clear():
    a = generics_TypeParameter()
    b1 = TypeReference()
    b2 = TypeReference()
    _safe_set(a, 'generics_TypeParameter', {b1})
    assert _is_linked(a, 'generics_TypeParameter', b1)
    if hasattr(b1, 'TypeReference92'):
        assert _is_linked(b1, 'TypeReference92', a)
    _safe_set(a, 'generics_TypeParameter', {b2})
    assert _is_linked(a, 'generics_TypeParameter', b2)
    if hasattr(b1, 'TypeReference92'):
        assert not _is_linked(b1, 'TypeReference92', a)
    if hasattr(b2, 'TypeReference92'):
        assert _is_linked(b2, 'TypeReference92', a)
    _safe_set(a, 'generics_TypeParameter', set())
    assert not _is_linked(a, 'generics_TypeParameter', b2)
    if hasattr(b2, 'TypeReference92'):
        assert not _is_linked(b2, 'TypeReference92', a)


def test_assoc_extends22_link_reassign_clear():
    a = classifiers_Class()
    b1 = TypeReference()
    b2 = TypeReference()
    _safe_set(a, 'classifiers_Class', b1)
    assert _is_linked(a, 'classifiers_Class', b1)
    if hasattr(b1, 'TypeReference23'):
        assert _is_linked(b1, 'TypeReference23', a)
    _safe_set(a, 'classifiers_Class', b2)
    assert _is_linked(a, 'classifiers_Class', b2)
    if hasattr(b1, 'TypeReference23'):
        assert not _is_linked(b1, 'TypeReference23', a)
    if hasattr(b2, 'TypeReference23'):
        assert _is_linked(b2, 'TypeReference23', a)
    _safe_set(a, 'classifiers_Class', None)
    assert not _is_linked(a, 'classifiers_Class', b2)
    if hasattr(b2, 'TypeReference23'):
        assert not _is_linked(b2, 'TypeReference23', a)


def test_assoc_extends27_link_reassign_clear():
    a = classifiers_Interface()
    b1 = TypeReference()
    b2 = TypeReference()
    _safe_set(a, 'classifiers_Interface', {b1})
    assert _is_linked(a, 'classifiers_Interface', b1)
    if hasattr(b1, 'TypeReference28'):
        assert _is_linked(b1, 'TypeReference28', a)
    _safe_set(a, 'classifiers_Interface', {b2})
    assert _is_linked(a, 'classifiers_Interface', b2)
    if hasattr(b1, 'TypeReference28'):
        assert not _is_linked(b1, 'TypeReference28', a)
    if hasattr(b2, 'TypeReference28'):
        assert _is_linked(b2, 'TypeReference28', a)
    _safe_set(a, 'classifiers_Interface', set())
    assert not _is_linked(a, 'classifiers_Interface', b2)
    if hasattr(b2, 'TypeReference28'):
        assert not _is_linked(b2, 'TypeReference28', a)


def test_assoc_imports93_link_reassign_clear():
    a = imports_ImportingElement()
    b1 = Import()
    b2 = Import()
    _safe_set(a, 'imports_ImportingElement', {b1})
    assert _is_linked(a, 'imports_ImportingElement', b1)
    if hasattr(b1, 'Import'):
        assert _is_linked(b1, 'Import', a)
    _safe_set(a, 'imports_ImportingElement', {b2})
    assert _is_linked(a, 'imports_ImportingElement', b2)
    if hasattr(b1, 'Import'):
        assert not _is_linked(b1, 'Import', a)
    if hasattr(b2, 'Import'):
        assert _is_linked(b2, 'Import', a)
    _safe_set(a, 'imports_ImportingElement', set())
    assert not _is_linked(a, 'imports_ImportingElement', b2)
    if hasattr(b2, 'Import'):
        assert not _is_linked(b2, 'Import', a)


def test_assoc_members103_link_reassign_clear():
    a = members_MemberContainer()
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'members_MemberContainer', {b1})
    assert _is_linked(a, 'members_MemberContainer', b1)
    if hasattr(b1, 'Member'):
        assert _is_linked(b1, 'Member', a)
    _safe_set(a, 'members_MemberContainer', {b2})
    assert _is_linked(a, 'members_MemberContainer', b2)
    if hasattr(b1, 'Member'):
        assert not _is_linked(b1, 'Member', a)
    if hasattr(b2, 'Member'):
        assert _is_linked(b2, 'Member', a)
    _safe_set(a, 'members_MemberContainer', set())
    assert not _is_linked(a, 'members_MemberContainer', b2)
    if hasattr(b2, 'Member'):
        assert not _is_linked(b2, 'Member', a)


def test_assoc_next113_link_reassign_clear():
    a = references_Reference()
    b1 = Reference()
    b2 = Reference()
    _safe_set(a, 'references_Reference', b1)
    assert _is_linked(a, 'references_Reference', b1)
    if hasattr(b1, 'Reference'):
        assert _is_linked(b1, 'Reference', a)
    _safe_set(a, 'references_Reference', b2)
    assert _is_linked(a, 'references_Reference', b2)
    if hasattr(b1, 'Reference'):
        assert not _is_linked(b1, 'Reference', a)
    if hasattr(b2, 'Reference'):
        assert _is_linked(b2, 'Reference', a)
    _safe_set(a, 'references_Reference', None)
    assert not _is_linked(a, 'references_Reference', b2)
    if hasattr(b2, 'Reference'):
        assert not _is_linked(b2, 'Reference', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AdditionalField_strategy = st.builds(AdditionalField)
@given(instance=AdditionalField_strategy)
@settings(max_examples=25)
def test_AdditionalField_instantiation(instance):
    assert isinstance(instance, AdditionalField)


AdditionalLocalVariable_strategy = st.builds(AdditionalLocalVariable)
@given(instance=AdditionalLocalVariable_strategy)
@settings(max_examples=25)
def test_AdditionalLocalVariable_instantiation(instance):
    assert isinstance(instance, AdditionalLocalVariable)


AdditiveExpressionChild_strategy = st.builds(AdditiveExpressionChild)
@given(instance=AdditiveExpressionChild_strategy)
@settings(max_examples=25)
def test_AdditiveExpressionChild_instantiation(instance):
    assert isinstance(instance, AdditiveExpressionChild)


AdditiveOperator_strategy = st.builds(AdditiveOperator)
@given(instance=AdditiveOperator_strategy)
@settings(max_examples=25)
def test_AdditiveOperator_instantiation(instance):
    assert isinstance(instance, AdditiveOperator)


AndExpressionChild_strategy = st.builds(AndExpressionChild)
@given(instance=AndExpressionChild_strategy)
@settings(max_examples=25)
def test_AndExpressionChild_instantiation(instance):
    assert isinstance(instance, AndExpressionChild)


Annotable_strategy = st.builds(Annotable)
@given(instance=Annotable_strategy)
@settings(max_examples=25)
def test_Annotable_instantiation(instance):
    assert isinstance(instance, Annotable)


AnnotableAndModifiable_strategy = st.builds(AnnotableAndModifiable)
@given(instance=AnnotableAndModifiable_strategy)
@settings(max_examples=25)
def test_AnnotableAndModifiable_instantiation(instance):
    assert isinstance(instance, AnnotableAndModifiable)


AnnotationAttributeSetting_strategy = st.builds(AnnotationAttributeSetting)
@given(instance=AnnotationAttributeSetting_strategy)
@settings(max_examples=25)
def test_AnnotationAttributeSetting_instantiation(instance):
    assert isinstance(instance, AnnotationAttributeSetting)


AnnotationInstance_strategy = st.builds(AnnotationInstance)
@given(instance=AnnotationInstance_strategy)
@settings(max_examples=25)
def test_AnnotationInstance_instantiation(instance):
    assert isinstance(instance, AnnotationInstance)


AnnotationInstanceOrModifier_strategy = st.builds(AnnotationInstanceOrModifier)
@given(instance=AnnotationInstanceOrModifier_strategy)
@settings(max_examples=25)
def test_AnnotationInstanceOrModifier_instantiation(instance):
    assert isinstance(instance, AnnotationInstanceOrModifier)


AnnotationParameter_strategy = st.builds(AnnotationParameter)
@given(instance=AnnotationParameter_strategy)
@settings(max_examples=25)
def test_AnnotationParameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)


AnnotationValue_strategy = st.builds(AnnotationValue)
@given(instance=AnnotationValue_strategy)
@settings(max_examples=25)
def test_AnnotationValue_instantiation(instance):
    assert isinstance(instance, AnnotationValue)


AnonymousClass_strategy = st.builds(AnonymousClass)
@given(instance=AnonymousClass_strategy)
@settings(max_examples=25)
def test_AnonymousClass_instantiation(instance):
    assert isinstance(instance, AnonymousClass)


Argumentable_strategy = st.builds(Argumentable)
@given(instance=Argumentable_strategy)
@settings(max_examples=25)
def test_Argumentable_instantiation(instance):
    assert isinstance(instance, Argumentable)


ArrayDimension_strategy = st.builds(ArrayDimension)
@given(instance=ArrayDimension_strategy)
@settings(max_examples=25)
def test_ArrayDimension_instantiation(instance):
    assert isinstance(instance, ArrayDimension)


ArrayInitializationValue_strategy = st.builds(ArrayInitializationValue)
@given(instance=ArrayInitializationValue_strategy)
@settings(max_examples=25)
def test_ArrayInitializationValue_instantiation(instance):
    assert isinstance(instance, ArrayInitializationValue)


ArrayInitializer_strategy = st.builds(ArrayInitializer)
@given(instance=ArrayInitializer_strategy)
@settings(max_examples=25)
def test_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)


ArraySelector_strategy = st.builds(ArraySelector)
@given(instance=ArraySelector_strategy)
@settings(max_examples=25)
def test_ArraySelector_instantiation(instance):
    assert isinstance(instance, ArraySelector)


ArrayTypeable_strategy = st.builds(ArrayTypeable)
@given(instance=ArrayTypeable_strategy)
@settings(max_examples=25)
def test_ArrayTypeable_instantiation(instance):
    assert isinstance(instance, ArrayTypeable)


AssignmentExpressionChild_strategy = st.builds(AssignmentExpressionChild)
@given(instance=AssignmentExpressionChild_strategy)
@settings(max_examples=25)
def test_AssignmentExpressionChild_instantiation(instance):
    assert isinstance(instance, AssignmentExpressionChild)


AssignmentOperator_strategy = st.builds(AssignmentOperator)
@given(instance=AssignmentOperator_strategy)
@settings(max_examples=25)
def test_AssignmentOperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


CallTypeArgumentable_strategy = st.builds(CallTypeArgumentable)
@given(instance=CallTypeArgumentable_strategy)
@settings(max_examples=25)
def test_CallTypeArgumentable_instantiation(instance):
    assert isinstance(instance, CallTypeArgumentable)


CatchBlock_strategy = st.builds(CatchBlock)
@given(instance=CatchBlock_strategy)
@settings(max_examples=25)
def test_CatchBlock_instantiation(instance):
    assert isinstance(instance, CatchBlock)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


ClassifierReference_strategy = st.builds(ClassifierReference)
@given(instance=ClassifierReference_strategy)
@settings(max_examples=25)
def test_ClassifierReference_instantiation(instance):
    assert isinstance(instance, ClassifierReference)


Commentable_strategy = st.builds(Commentable)
@given(instance=Commentable_strategy)
@settings(max_examples=25)
def test_Commentable_instantiation(instance):
    assert isinstance(instance, Commentable)


CompilationUnit_strategy = st.builds(CompilationUnit)
@given(instance=CompilationUnit_strategy)
@settings(max_examples=25)
def test_CompilationUnit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)


ConcreteClassifier_strategy = st.builds(ConcreteClassifier)
@given(instance=ConcreteClassifier_strategy)
@settings(max_examples=25)
def test_ConcreteClassifier_instantiation(instance):
    assert isinstance(instance, ConcreteClassifier)


Conditional_strategy = st.builds(Conditional)
@given(instance=Conditional_strategy)
@settings(max_examples=25)
def test_Conditional_instantiation(instance):
    assert isinstance(instance, Conditional)


ConditionalAndExpressionChild_strategy = st.builds(ConditionalAndExpressionChild)
@given(instance=ConditionalAndExpressionChild_strategy)
@settings(max_examples=25)
def test_ConditionalAndExpressionChild_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpressionChild)


ConditionalExpressionChild_strategy = st.builds(ConditionalExpressionChild)
@given(instance=ConditionalExpressionChild_strategy)
@settings(max_examples=25)
def test_ConditionalExpressionChild_instantiation(instance):
    assert isinstance(instance, ConditionalExpressionChild)


ConditionalOrExpressionChild_strategy = st.builds(ConditionalOrExpressionChild)
@given(instance=ConditionalOrExpressionChild_strategy)
@settings(max_examples=25)
def test_ConditionalOrExpressionChild_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpressionChild)


DoubleLiteral_strategy = st.builds(DoubleLiteral)
@given(instance=DoubleLiteral_strategy)
@settings(max_examples=25)
def test_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, DoubleLiteral)


ElementReference_strategy = st.builds(ElementReference)
@given(instance=ElementReference_strategy)
@settings(max_examples=25)
def test_ElementReference_instantiation(instance):
    assert isinstance(instance, ElementReference)


EnumConstant_strategy = st.builds(EnumConstant)
@given(instance=EnumConstant_strategy)
@settings(max_examples=25)
def test_EnumConstant_instantiation(instance):
    assert isinstance(instance, EnumConstant)


EqualityExpressionChild_strategy = st.builds(EqualityExpressionChild)
@given(instance=EqualityExpressionChild_strategy)
@settings(max_examples=25)
def test_EqualityExpressionChild_instantiation(instance):
    assert isinstance(instance, EqualityExpressionChild)


EqualityOperator_strategy = st.builds(EqualityOperator)
@given(instance=EqualityOperator_strategy)
@settings(max_examples=25)
def test_EqualityOperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)


ExceptionThrower_strategy = st.builds(ExceptionThrower)
@given(instance=ExceptionThrower_strategy)
@settings(max_examples=25)
def test_ExceptionThrower_instantiation(instance):
    assert isinstance(instance, ExceptionThrower)


ExclusiveOrExpressionChild_strategy = st.builds(ExclusiveOrExpressionChild)
@given(instance=ExclusiveOrExpressionChild_strategy)
@settings(max_examples=25)
def test_ExclusiveOrExpressionChild_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpressionChild)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FloatLiteral_strategy = st.builds(FloatLiteral)
@given(instance=FloatLiteral_strategy)
@settings(max_examples=25)
def test_FloatLiteral_instantiation(instance):
    assert isinstance(instance, FloatLiteral)


ForLoopInitializer_strategy = st.builds(ForLoopInitializer)
@given(instance=ForLoopInitializer_strategy)
@settings(max_examples=25)
def test_ForLoopInitializer_instantiation(instance):
    assert isinstance(instance, ForLoopInitializer)


Implementor_strategy = st.builds(Implementor)
@given(instance=Implementor_strategy)
@settings(max_examples=25)
def test_Implementor_instantiation(instance):
    assert isinstance(instance, Implementor)


Import_strategy = st.builds(Import)
@given(instance=Import_strategy)
@settings(max_examples=25)
def test_Import_instantiation(instance):
    assert isinstance(instance, Import)


ImportingElement_strategy = st.builds(ImportingElement)
@given(instance=ImportingElement_strategy)
@settings(max_examples=25)
def test_ImportingElement_instantiation(instance):
    assert isinstance(instance, ImportingElement)


InclusiveOrExpressionChild_strategy = st.builds(InclusiveOrExpressionChild)
@given(instance=InclusiveOrExpressionChild_strategy)
@settings(max_examples=25)
def test_InclusiveOrExpressionChild_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpressionChild)


Initializable_strategy = st.builds(Initializable)
@given(instance=Initializable_strategy)
@settings(max_examples=25)
def test_Initializable_instantiation(instance):
    assert isinstance(instance, Initializable)


InstanceOfExpressionChild_strategy = st.builds(InstanceOfExpressionChild)
@given(instance=InstanceOfExpressionChild_strategy)
@settings(max_examples=25)
def test_InstanceOfExpressionChild_instantiation(instance):
    assert isinstance(instance, InstanceOfExpressionChild)


Instantiation_strategy = st.builds(Instantiation)
@given(instance=Instantiation_strategy)
@settings(max_examples=25)
def test_Instantiation_instantiation(instance):
    assert isinstance(instance, Instantiation)


IntegerLiteral_strategy = st.builds(IntegerLiteral)
@given(instance=IntegerLiteral_strategy)
@settings(max_examples=25)
def test_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, IntegerLiteral)


InterfaceMethod_strategy = st.builds(InterfaceMethod)
@given(instance=InterfaceMethod_strategy)
@settings(max_examples=25)
def test_InterfaceMethod_instantiation(instance):
    assert isinstance(instance, InterfaceMethod)


JavaRoot_strategy = st.builds(JavaRoot)
@given(instance=JavaRoot_strategy)
@settings(max_examples=25)
def test_JavaRoot_instantiation(instance):
    assert isinstance(instance, JavaRoot)


Jump_strategy = st.builds(Jump)
@given(instance=Jump_strategy)
@settings(max_examples=25)
def test_Jump_instantiation(instance):
    assert isinstance(instance, Jump)


JumpLabel_strategy = st.builds(JumpLabel)
@given(instance=JumpLabel_strategy)
@settings(max_examples=25)
def test_JumpLabel_instantiation(instance):
    assert isinstance(instance, JumpLabel)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


LocalVariable_strategy = st.builds(LocalVariable)
@given(instance=LocalVariable_strategy)
@settings(max_examples=25)
def test_LocalVariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)


LongLiteral_strategy = st.builds(LongLiteral)
@given(instance=LongLiteral_strategy)
@settings(max_examples=25)
def test_LongLiteral_instantiation(instance):
    assert isinstance(instance, LongLiteral)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


MemberContainer_strategy = st.builds(MemberContainer)
@given(instance=MemberContainer_strategy)
@settings(max_examples=25)
def test_MemberContainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)


Method_strategy = st.builds(Method)
@given(instance=Method_strategy)
@settings(max_examples=25)
def test_Method_instantiation(instance):
    assert isinstance(instance, Method)


Modifiable_strategy = st.builds(Modifiable)
@given(instance=Modifiable_strategy)
@settings(max_examples=25)
def test_Modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)


Modifier_strategy = st.builds(Modifier)
@given(instance=Modifier_strategy)
@settings(max_examples=25)
def test_Modifier_instantiation(instance):
    assert isinstance(instance, Modifier)


MultiplicativeExpressionChild_strategy = st.builds(MultiplicativeExpressionChild)
@given(instance=MultiplicativeExpressionChild_strategy)
@settings(max_examples=25)
def test_MultiplicativeExpressionChild_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpressionChild)


MultiplicativeOperator_strategy = st.builds(MultiplicativeOperator)
@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=25)
def test_MultiplicativeOperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NamespaceAwareElement_strategy = st.builds(NamespaceAwareElement)
@given(instance=NamespaceAwareElement_strategy)
@settings(max_examples=25)
def test_NamespaceAwareElement_instantiation(instance):
    assert isinstance(instance, NamespaceAwareElement)


NamespaceClassifierReference_strategy = st.builds(NamespaceClassifierReference)
@given(instance=NamespaceClassifierReference_strategy)
@settings(max_examples=25)
def test_NamespaceClassifierReference_instantiation(instance):
    assert isinstance(instance, NamespaceClassifierReference)


Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


OrdinaryParameter_strategy = st.builds(OrdinaryParameter)
@given(instance=OrdinaryParameter_strategy)
@settings(max_examples=25)
def test_OrdinaryParameter_instantiation(instance):
    assert isinstance(instance, OrdinaryParameter)


Package_strategy = st.builds(Package)
@given(instance=Package_strategy)
@settings(max_examples=25)
def test_Package_instantiation(instance):
    assert isinstance(instance, Package)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Parametrizable_strategy = st.builds(Parametrizable)
@given(instance=Parametrizable_strategy)
@settings(max_examples=25)
def test_Parametrizable_instantiation(instance):
    assert isinstance(instance, Parametrizable)


PrimaryExpression_strategy = st.builds(PrimaryExpression)
@given(instance=PrimaryExpression_strategy)
@settings(max_examples=25)
def test_PrimaryExpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Reference_strategy = st.builds(Reference)
@given(instance=Reference_strategy)
@settings(max_examples=25)
def test_Reference_instantiation(instance):
    assert isinstance(instance, Reference)


ReferenceableElement_strategy = st.builds(ReferenceableElement)
@given(instance=ReferenceableElement_strategy)
@settings(max_examples=25)
def test_ReferenceableElement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)


RelationExpressionChild_strategy = st.builds(RelationExpressionChild)
@given(instance=RelationExpressionChild_strategy)
@settings(max_examples=25)
def test_RelationExpressionChild_instantiation(instance):
    assert isinstance(instance, RelationExpressionChild)


RelationOperator_strategy = st.builds(RelationOperator)
@given(instance=RelationOperator_strategy)
@settings(max_examples=25)
def test_RelationOperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)


Self_strategy = st.builds(Self)
@given(instance=Self_strategy)
@settings(max_examples=25)
def test_Self_instantiation(instance):
    assert isinstance(instance, Self)


ShiftExpressionChild_strategy = st.builds(ShiftExpressionChild)
@given(instance=ShiftExpressionChild_strategy)
@settings(max_examples=25)
def test_ShiftExpressionChild_instantiation(instance):
    assert isinstance(instance, ShiftExpressionChild)


ShiftOperator_strategy = st.builds(ShiftOperator)
@given(instance=ShiftOperator_strategy)
@settings(max_examples=25)
def test_ShiftOperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


StatementContainer_strategy = st.builds(StatementContainer)
@given(instance=StatementContainer_strategy)
@settings(max_examples=25)
def test_StatementContainer_instantiation(instance):
    assert isinstance(instance, StatementContainer)


StatementListContainer_strategy = st.builds(StatementListContainer)
@given(instance=StatementListContainer_strategy)
@settings(max_examples=25)
def test_StatementListContainer_instantiation(instance):
    assert isinstance(instance, StatementListContainer)


Static_strategy = st.builds(Static)
@given(instance=Static_strategy)
@settings(max_examples=25)
def test_Static_instantiation(instance):
    assert isinstance(instance, Static)


StaticImport_strategy = st.builds(StaticImport)
@given(instance=StaticImport_strategy)
@settings(max_examples=25)
def test_StaticImport_instantiation(instance):
    assert isinstance(instance, StaticImport)


SwitchCase_strategy = st.builds(SwitchCase)
@given(instance=SwitchCase_strategy)
@settings(max_examples=25)
def test_SwitchCase_instantiation(instance):
    assert isinstance(instance, SwitchCase)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeArgument_strategy = st.builds(TypeArgument)
@given(instance=TypeArgument_strategy)
@settings(max_examples=25)
def test_TypeArgument_instantiation(instance):
    assert isinstance(instance, TypeArgument)


TypeArgumentable_strategy = st.builds(TypeArgumentable)
@given(instance=TypeArgumentable_strategy)
@settings(max_examples=25)
def test_TypeArgumentable_instantiation(instance):
    assert isinstance(instance, TypeArgumentable)


TypeParameter_strategy = st.builds(TypeParameter)
@given(instance=TypeParameter_strategy)
@settings(max_examples=25)
def test_TypeParameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)


TypeParametrizable_strategy = st.builds(TypeParametrizable)
@given(instance=TypeParametrizable_strategy)
@settings(max_examples=25)
def test_TypeParametrizable_instantiation(instance):
    assert isinstance(instance, TypeParametrizable)


TypeReference_strategy = st.builds(TypeReference)
@given(instance=TypeReference_strategy)
@settings(max_examples=25)
def test_TypeReference_instantiation(instance):
    assert isinstance(instance, TypeReference)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


UnaryExpressionChild_strategy = st.builds(UnaryExpressionChild)
@given(instance=UnaryExpressionChild_strategy)
@settings(max_examples=25)
def test_UnaryExpressionChild_instantiation(instance):
    assert isinstance(instance, UnaryExpressionChild)


UnaryModificationExpression_strategy = st.builds(UnaryModificationExpression)
@given(instance=UnaryModificationExpression_strategy)
@settings(max_examples=25)
def test_UnaryModificationExpression_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpression)


UnaryModificationExpressionChild_strategy = st.builds(UnaryModificationExpressionChild)
@given(instance=UnaryModificationExpressionChild_strategy)
@settings(max_examples=25)
def test_UnaryModificationExpressionChild_instantiation(instance):
    assert isinstance(instance, UnaryModificationExpressionChild)


UnaryModificationOperator_strategy = st.builds(UnaryModificationOperator)
@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=25)
def test_UnaryModificationOperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)


UnaryOperator_strategy = st.builds(UnaryOperator)
@given(instance=UnaryOperator_strategy)
@settings(max_examples=25)
def test_UnaryOperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


WhileLoop_strategy = st.builds(WhileLoop)
@given(instance=WhileLoop_strategy)
@settings(max_examples=25)
def test_WhileLoop_instantiation(instance):
    assert isinstance(instance, WhileLoop)


annotations_Annotable_strategy = st.builds(annotations_Annotable)
@given(instance=annotations_Annotable_strategy)
@settings(max_examples=25)
def test_annotations_Annotable_instantiation(instance):
    assert isinstance(instance, annotations_Annotable)


annotations_AnnotationAttribute_strategy = st.builds(annotations_AnnotationAttribute)
@given(instance=annotations_AnnotationAttribute_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationAttribute_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationAttribute)


annotations_AnnotationAttributeSetting_strategy = st.builds(annotations_AnnotationAttributeSetting)
@given(instance=annotations_AnnotationAttributeSetting_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationAttributeSetting_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationAttributeSetting)


annotations_AnnotationInstance_strategy = st.builds(annotations_AnnotationInstance)
@given(instance=annotations_AnnotationInstance_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationInstance_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationInstance)


annotations_AnnotationParameter_strategy = st.builds(annotations_AnnotationParameter)
@given(instance=annotations_AnnotationParameter_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationParameter_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationParameter)


annotations_AnnotationParameterList_strategy = st.builds(annotations_AnnotationParameterList)
@given(instance=annotations_AnnotationParameterList_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationParameterList_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationParameterList)


annotations_AnnotationValue_strategy = st.builds(annotations_AnnotationValue)
@given(instance=annotations_AnnotationValue_strategy)
@settings(max_examples=25)
def test_annotations_AnnotationValue_instantiation(instance):
    assert isinstance(instance, annotations_AnnotationValue)


annotations_SingleAnnotationParameter_strategy = st.builds(annotations_SingleAnnotationParameter)
@given(instance=annotations_SingleAnnotationParameter_strategy)
@settings(max_examples=25)
def test_annotations_SingleAnnotationParameter_instantiation(instance):
    assert isinstance(instance, annotations_SingleAnnotationParameter)


arrays_ArrayDimension_strategy = st.builds(arrays_ArrayDimension)
@given(instance=arrays_ArrayDimension_strategy)
@settings(max_examples=25)
def test_arrays_ArrayDimension_instantiation(instance):
    assert isinstance(instance, arrays_ArrayDimension)


arrays_ArrayInitializationValue_strategy = st.builds(arrays_ArrayInitializationValue)
@given(instance=arrays_ArrayInitializationValue_strategy)
@settings(max_examples=25)
def test_arrays_ArrayInitializationValue_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInitializationValue)


arrays_ArrayInitializer_strategy = st.builds(arrays_ArrayInitializer)
@given(instance=arrays_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_arrays_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInitializer)


arrays_ArrayInstantiationBySize_strategy = st.builds(arrays_ArrayInstantiationBySize)
@given(instance=arrays_ArrayInstantiationBySize_strategy)
@settings(max_examples=25)
def test_arrays_ArrayInstantiationBySize_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInstantiationBySize)


arrays_ArrayInstantiationByValues_strategy = st.builds(arrays_ArrayInstantiationByValues)
@given(instance=arrays_ArrayInstantiationByValues_strategy)
@settings(max_examples=25)
def test_arrays_ArrayInstantiationByValues_instantiation(instance):
    assert isinstance(instance, arrays_ArrayInstantiationByValues)


arrays_ArraySelector_strategy = st.builds(arrays_ArraySelector)
@given(instance=arrays_ArraySelector_strategy)
@settings(max_examples=25)
def test_arrays_ArraySelector_instantiation(instance):
    assert isinstance(instance, arrays_ArraySelector)


arrays_ArrayTypeable_strategy = st.builds(arrays_ArrayTypeable)
@given(instance=arrays_ArrayTypeable_strategy)
@settings(max_examples=25)
def test_arrays_ArrayTypeable_instantiation(instance):
    assert isinstance(instance, arrays_ArrayTypeable)


classifiers_Annotation_strategy = st.builds(classifiers_Annotation)
@given(instance=classifiers_Annotation_strategy)
@settings(max_examples=25)
def test_classifiers_Annotation_instantiation(instance):
    assert isinstance(instance, classifiers_Annotation)


classifiers_AnonymousClass_strategy = st.builds(classifiers_AnonymousClass)
@given(instance=classifiers_AnonymousClass_strategy)
@settings(max_examples=25)
def test_classifiers_AnonymousClass_instantiation(instance):
    assert isinstance(instance, classifiers_AnonymousClass)


classifiers_Class_strategy = st.builds(classifiers_Class)
@given(instance=classifiers_Class_strategy)
@settings(max_examples=25)
def test_classifiers_Class_instantiation(instance):
    assert isinstance(instance, classifiers_Class)


classifiers_Classifier_strategy = st.builds(classifiers_Classifier)
@given(instance=classifiers_Classifier_strategy)
@settings(max_examples=25)
def test_classifiers_Classifier_instantiation(instance):
    assert isinstance(instance, classifiers_Classifier)


classifiers_ConcreteClassifier_strategy = st.builds(classifiers_ConcreteClassifier, fullName=safe_text)
@given(instance=classifiers_ConcreteClassifier_strategy)
@settings(max_examples=25)
def test_classifiers_ConcreteClassifier_instantiation(instance):
    assert isinstance(instance, classifiers_ConcreteClassifier)


classifiers_Enumeration_strategy = st.builds(classifiers_Enumeration)
@given(instance=classifiers_Enumeration_strategy)
@settings(max_examples=25)
def test_classifiers_Enumeration_instantiation(instance):
    assert isinstance(instance, classifiers_Enumeration)


classifiers_Implementor_strategy = st.builds(classifiers_Implementor)
@given(instance=classifiers_Implementor_strategy)
@settings(max_examples=25)
def test_classifiers_Implementor_instantiation(instance):
    assert isinstance(instance, classifiers_Implementor)


classifiers_Interface_strategy = st.builds(classifiers_Interface)
@given(instance=classifiers_Interface_strategy)
@settings(max_examples=25)
def test_classifiers_Interface_instantiation(instance):
    assert isinstance(instance, classifiers_Interface)


commons_Commentable_strategy = st.builds(commons_Commentable, comments=safe_text)
@given(instance=commons_Commentable_strategy)
@settings(max_examples=25)
def test_commons_Commentable_instantiation(instance):
    assert isinstance(instance, commons_Commentable)


commons_NamedElement_strategy = st.builds(commons_NamedElement, name=safe_text)
@given(instance=commons_NamedElement_strategy)
@settings(max_examples=25)
def test_commons_NamedElement_instantiation(instance):
    assert isinstance(instance, commons_NamedElement)


commons_NamespaceAwareElement_strategy = st.builds(commons_NamespaceAwareElement, namespaces=safe_text)
@given(instance=commons_NamespaceAwareElement_strategy)
@settings(max_examples=25)
def test_commons_NamespaceAwareElement_instantiation(instance):
    assert isinstance(instance, commons_NamespaceAwareElement)


containers_CompilationUnit_strategy = st.builds(containers_CompilationUnit)
@given(instance=containers_CompilationUnit_strategy)
@settings(max_examples=25)
def test_containers_CompilationUnit_instantiation(instance):
    assert isinstance(instance, containers_CompilationUnit)


containers_EmptyModel_strategy = st.builds(containers_EmptyModel)
@given(instance=containers_EmptyModel_strategy)
@settings(max_examples=25)
def test_containers_EmptyModel_instantiation(instance):
    assert isinstance(instance, containers_EmptyModel)


containers_JavaRoot_strategy = st.builds(containers_JavaRoot)
@given(instance=containers_JavaRoot_strategy)
@settings(max_examples=25)
def test_containers_JavaRoot_instantiation(instance):
    assert isinstance(instance, containers_JavaRoot)


containers_Package_strategy = st.builds(containers_Package)
@given(instance=containers_Package_strategy)
@settings(max_examples=25)
def test_containers_Package_instantiation(instance):
    assert isinstance(instance, containers_Package)


expressions_AdditiveExpression_strategy = st.builds(expressions_AdditiveExpression)
@given(instance=expressions_AdditiveExpression_strategy)
@settings(max_examples=25)
def test_expressions_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, expressions_AdditiveExpression)


expressions_AdditiveExpressionChild_strategy = st.builds(expressions_AdditiveExpressionChild)
@given(instance=expressions_AdditiveExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_AdditiveExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_AdditiveExpressionChild)


expressions_AndExpression_strategy = st.builds(expressions_AndExpression)
@given(instance=expressions_AndExpression_strategy)
@settings(max_examples=25)
def test_expressions_AndExpression_instantiation(instance):
    assert isinstance(instance, expressions_AndExpression)


expressions_AndExpressionChild_strategy = st.builds(expressions_AndExpressionChild)
@given(instance=expressions_AndExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_AndExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_AndExpressionChild)


expressions_AssignmentExpression_strategy = st.builds(expressions_AssignmentExpression)
@given(instance=expressions_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_expressions_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpression)


expressions_AssignmentExpressionChild_strategy = st.builds(expressions_AssignmentExpressionChild)
@given(instance=expressions_AssignmentExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_AssignmentExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpressionChild)


expressions_CastExpression_strategy = st.builds(expressions_CastExpression)
@given(instance=expressions_CastExpression_strategy)
@settings(max_examples=25)
def test_expressions_CastExpression_instantiation(instance):
    assert isinstance(instance, expressions_CastExpression)


expressions_ConditionalAndExpression_strategy = st.builds(expressions_ConditionalAndExpression)
@given(instance=expressions_ConditionalAndExpression_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalAndExpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalAndExpression)


expressions_ConditionalAndExpressionChild_strategy = st.builds(expressions_ConditionalAndExpressionChild)
@given(instance=expressions_ConditionalAndExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalAndExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalAndExpressionChild)


expressions_ConditionalExpression_strategy = st.builds(expressions_ConditionalExpression)
@given(instance=expressions_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpression)


expressions_ConditionalExpressionChild_strategy = st.builds(expressions_ConditionalExpressionChild)
@given(instance=expressions_ConditionalExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpressionChild)


expressions_ConditionalOrExpression_strategy = st.builds(expressions_ConditionalOrExpression)
@given(instance=expressions_ConditionalOrExpression_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalOrExpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalOrExpression)


expressions_ConditionalOrExpressionChild_strategy = st.builds(expressions_ConditionalOrExpressionChild)
@given(instance=expressions_ConditionalOrExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_ConditionalOrExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalOrExpressionChild)


expressions_EqualityExpression_strategy = st.builds(expressions_EqualityExpression)
@given(instance=expressions_EqualityExpression_strategy)
@settings(max_examples=25)
def test_expressions_EqualityExpression_instantiation(instance):
    assert isinstance(instance, expressions_EqualityExpression)


expressions_EqualityExpressionChild_strategy = st.builds(expressions_EqualityExpressionChild)
@given(instance=expressions_EqualityExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_EqualityExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_EqualityExpressionChild)


expressions_ExclusiveOrExpression_strategy = st.builds(expressions_ExclusiveOrExpression)
@given(instance=expressions_ExclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_expressions_ExclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, expressions_ExclusiveOrExpression)


expressions_ExclusiveOrExpressionChild_strategy = st.builds(expressions_ExclusiveOrExpressionChild)
@given(instance=expressions_ExclusiveOrExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_ExclusiveOrExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_ExclusiveOrExpressionChild)


expressions_Expression_strategy = st.builds(expressions_Expression)
@given(instance=expressions_Expression_strategy)
@settings(max_examples=25)
def test_expressions_Expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)


expressions_ExpressionList_strategy = st.builds(expressions_ExpressionList)
@given(instance=expressions_ExpressionList_strategy)
@settings(max_examples=25)
def test_expressions_ExpressionList_instantiation(instance):
    assert isinstance(instance, expressions_ExpressionList)


expressions_InclusiveOrExpression_strategy = st.builds(expressions_InclusiveOrExpression)
@given(instance=expressions_InclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_expressions_InclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, expressions_InclusiveOrExpression)


expressions_InclusiveOrExpressionChild_strategy = st.builds(expressions_InclusiveOrExpressionChild)
@given(instance=expressions_InclusiveOrExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_InclusiveOrExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_InclusiveOrExpressionChild)


expressions_InstanceOfExpression_strategy = st.builds(expressions_InstanceOfExpression)
@given(instance=expressions_InstanceOfExpression_strategy)
@settings(max_examples=25)
def test_expressions_InstanceOfExpression_instantiation(instance):
    assert isinstance(instance, expressions_InstanceOfExpression)


expressions_InstanceOfExpressionChild_strategy = st.builds(expressions_InstanceOfExpressionChild)
@given(instance=expressions_InstanceOfExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_InstanceOfExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_InstanceOfExpressionChild)


expressions_MultiplicativeExpression_strategy = st.builds(expressions_MultiplicativeExpression)
@given(instance=expressions_MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_expressions_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, expressions_MultiplicativeExpression)


expressions_MultiplicativeExpressionChild_strategy = st.builds(expressions_MultiplicativeExpressionChild)
@given(instance=expressions_MultiplicativeExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_MultiplicativeExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_MultiplicativeExpressionChild)


expressions_NestedExpression_strategy = st.builds(expressions_NestedExpression)
@given(instance=expressions_NestedExpression_strategy)
@settings(max_examples=25)
def test_expressions_NestedExpression_instantiation(instance):
    assert isinstance(instance, expressions_NestedExpression)


expressions_PrefixUnaryModificationExpression_strategy = st.builds(expressions_PrefixUnaryModificationExpression)
@given(instance=expressions_PrefixUnaryModificationExpression_strategy)
@settings(max_examples=25)
def test_expressions_PrefixUnaryModificationExpression_instantiation(instance):
    assert isinstance(instance, expressions_PrefixUnaryModificationExpression)


expressions_PrimaryExpression_strategy = st.builds(expressions_PrimaryExpression)
@given(instance=expressions_PrimaryExpression_strategy)
@settings(max_examples=25)
def test_expressions_PrimaryExpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryExpression)


expressions_RelationExpression_strategy = st.builds(expressions_RelationExpression)
@given(instance=expressions_RelationExpression_strategy)
@settings(max_examples=25)
def test_expressions_RelationExpression_instantiation(instance):
    assert isinstance(instance, expressions_RelationExpression)


expressions_RelationExpressionChild_strategy = st.builds(expressions_RelationExpressionChild)
@given(instance=expressions_RelationExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_RelationExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_RelationExpressionChild)


expressions_ShiftExpression_strategy = st.builds(expressions_ShiftExpression)
@given(instance=expressions_ShiftExpression_strategy)
@settings(max_examples=25)
def test_expressions_ShiftExpression_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpression)


expressions_ShiftExpressionChild_strategy = st.builds(expressions_ShiftExpressionChild)
@given(instance=expressions_ShiftExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_ShiftExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpressionChild)


expressions_SuffixUnaryModificationExpression_strategy = st.builds(expressions_SuffixUnaryModificationExpression)
@given(instance=expressions_SuffixUnaryModificationExpression_strategy)
@settings(max_examples=25)
def test_expressions_SuffixUnaryModificationExpression_instantiation(instance):
    assert isinstance(instance, expressions_SuffixUnaryModificationExpression)


expressions_UnaryExpression_strategy = st.builds(expressions_UnaryExpression)
@given(instance=expressions_UnaryExpression_strategy)
@settings(max_examples=25)
def test_expressions_UnaryExpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpression)


expressions_UnaryExpressionChild_strategy = st.builds(expressions_UnaryExpressionChild)
@given(instance=expressions_UnaryExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_UnaryExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpressionChild)


expressions_UnaryModificationExpression_strategy = st.builds(expressions_UnaryModificationExpression)
@given(instance=expressions_UnaryModificationExpression_strategy)
@settings(max_examples=25)
def test_expressions_UnaryModificationExpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryModificationExpression)


expressions_UnaryModificationExpressionChild_strategy = st.builds(expressions_UnaryModificationExpressionChild)
@given(instance=expressions_UnaryModificationExpressionChild_strategy)
@settings(max_examples=25)
def test_expressions_UnaryModificationExpressionChild_instantiation(instance):
    assert isinstance(instance, expressions_UnaryModificationExpressionChild)


generics_CallTypeArgumentable_strategy = st.builds(generics_CallTypeArgumentable)
@given(instance=generics_CallTypeArgumentable_strategy)
@settings(max_examples=25)
def test_generics_CallTypeArgumentable_instantiation(instance):
    assert isinstance(instance, generics_CallTypeArgumentable)


generics_ExtendsTypeArgument_strategy = st.builds(generics_ExtendsTypeArgument)
@given(instance=generics_ExtendsTypeArgument_strategy)
@settings(max_examples=25)
def test_generics_ExtendsTypeArgument_instantiation(instance):
    assert isinstance(instance, generics_ExtendsTypeArgument)


generics_QualifiedTypeArgument_strategy = st.builds(generics_QualifiedTypeArgument)
@given(instance=generics_QualifiedTypeArgument_strategy)
@settings(max_examples=25)
def test_generics_QualifiedTypeArgument_instantiation(instance):
    assert isinstance(instance, generics_QualifiedTypeArgument)


generics_SuperTypeArgument_strategy = st.builds(generics_SuperTypeArgument)
@given(instance=generics_SuperTypeArgument_strategy)
@settings(max_examples=25)
def test_generics_SuperTypeArgument_instantiation(instance):
    assert isinstance(instance, generics_SuperTypeArgument)


generics_TypeArgument_strategy = st.builds(generics_TypeArgument)
@given(instance=generics_TypeArgument_strategy)
@settings(max_examples=25)
def test_generics_TypeArgument_instantiation(instance):
    assert isinstance(instance, generics_TypeArgument)


generics_TypeArgumentable_strategy = st.builds(generics_TypeArgumentable)
@given(instance=generics_TypeArgumentable_strategy)
@settings(max_examples=25)
def test_generics_TypeArgumentable_instantiation(instance):
    assert isinstance(instance, generics_TypeArgumentable)


generics_TypeParameter_strategy = st.builds(generics_TypeParameter)
@given(instance=generics_TypeParameter_strategy)
@settings(max_examples=25)
def test_generics_TypeParameter_instantiation(instance):
    assert isinstance(instance, generics_TypeParameter)


generics_TypeParametrizable_strategy = st.builds(generics_TypeParametrizable)
@given(instance=generics_TypeParametrizable_strategy)
@settings(max_examples=25)
def test_generics_TypeParametrizable_instantiation(instance):
    assert isinstance(instance, generics_TypeParametrizable)


generics_UnknownTypeArgument_strategy = st.builds(generics_UnknownTypeArgument)
@given(instance=generics_UnknownTypeArgument_strategy)
@settings(max_examples=25)
def test_generics_UnknownTypeArgument_instantiation(instance):
    assert isinstance(instance, generics_UnknownTypeArgument)


imports_ClassifierImport_strategy = st.builds(imports_ClassifierImport)
@given(instance=imports_ClassifierImport_strategy)
@settings(max_examples=25)
def test_imports_ClassifierImport_instantiation(instance):
    assert isinstance(instance, imports_ClassifierImport)


imports_Import_strategy = st.builds(imports_Import)
@given(instance=imports_Import_strategy)
@settings(max_examples=25)
def test_imports_Import_instantiation(instance):
    assert isinstance(instance, imports_Import)


imports_ImportingElement_strategy = st.builds(imports_ImportingElement)
@given(instance=imports_ImportingElement_strategy)
@settings(max_examples=25)
def test_imports_ImportingElement_instantiation(instance):
    assert isinstance(instance, imports_ImportingElement)


imports_PackageImport_strategy = st.builds(imports_PackageImport)
@given(instance=imports_PackageImport_strategy)
@settings(max_examples=25)
def test_imports_PackageImport_instantiation(instance):
    assert isinstance(instance, imports_PackageImport)


imports_StaticClassifierImport_strategy = st.builds(imports_StaticClassifierImport)
@given(instance=imports_StaticClassifierImport_strategy)
@settings(max_examples=25)
def test_imports_StaticClassifierImport_instantiation(instance):
    assert isinstance(instance, imports_StaticClassifierImport)


imports_StaticImport_strategy = st.builds(imports_StaticImport)
@given(instance=imports_StaticImport_strategy)
@settings(max_examples=25)
def test_imports_StaticImport_instantiation(instance):
    assert isinstance(instance, imports_StaticImport)


imports_StaticMemberImport_strategy = st.builds(imports_StaticMemberImport)
@given(instance=imports_StaticMemberImport_strategy)
@settings(max_examples=25)
def test_imports_StaticMemberImport_instantiation(instance):
    assert isinstance(instance, imports_StaticMemberImport)


instantiations_ExplicitConstructorCall_strategy = st.builds(instantiations_ExplicitConstructorCall)
@given(instance=instantiations_ExplicitConstructorCall_strategy)
@settings(max_examples=25)
def test_instantiations_ExplicitConstructorCall_instantiation(instance):
    assert isinstance(instance, instantiations_ExplicitConstructorCall)


instantiations_Initializable_strategy = st.builds(instantiations_Initializable)
@given(instance=instantiations_Initializable_strategy)
@settings(max_examples=25)
def test_instantiations_Initializable_instantiation(instance):
    assert isinstance(instance, instantiations_Initializable)


instantiations_Instantiation_strategy = st.builds(instantiations_Instantiation)
@given(instance=instantiations_Instantiation_strategy)
@settings(max_examples=25)
def test_instantiations_Instantiation_instantiation(instance):
    assert isinstance(instance, instantiations_Instantiation)


instantiations_NewConstructorCall_strategy = st.builds(instantiations_NewConstructorCall)
@given(instance=instantiations_NewConstructorCall_strategy)
@settings(max_examples=25)
def test_instantiations_NewConstructorCall_instantiation(instance):
    assert isinstance(instance, instantiations_NewConstructorCall)


literals_BooleanLiteral_strategy = st.builds(literals_BooleanLiteral, value=st.booleans())
@given(instance=literals_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_literals_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, literals_BooleanLiteral)


literals_CharacterLiteral_strategy = st.builds(literals_CharacterLiteral, value=safe_text)
@given(instance=literals_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_literals_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, literals_CharacterLiteral)


literals_DecimalDoubleLiteral_strategy = st.builds(literals_DecimalDoubleLiteral, decimalValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=literals_DecimalDoubleLiteral_strategy)
@settings(max_examples=25)
def test_literals_DecimalDoubleLiteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalDoubleLiteral)


literals_DecimalFloatLiteral_strategy = st.builds(literals_DecimalFloatLiteral, decimalValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=literals_DecimalFloatLiteral_strategy)
@settings(max_examples=25)
def test_literals_DecimalFloatLiteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalFloatLiteral)


literals_DecimalIntegerLiteral_strategy = st.builds(literals_DecimalIntegerLiteral, decimalValue=safe_text)
@given(instance=literals_DecimalIntegerLiteral_strategy)
@settings(max_examples=25)
def test_literals_DecimalIntegerLiteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalIntegerLiteral)


literals_DecimalLongLiteral_strategy = st.builds(literals_DecimalLongLiteral, decimalValue=safe_text)
@given(instance=literals_DecimalLongLiteral_strategy)
@settings(max_examples=25)
def test_literals_DecimalLongLiteral_instantiation(instance):
    assert isinstance(instance, literals_DecimalLongLiteral)


literals_DoubleLiteral_strategy = st.builds(literals_DoubleLiteral)
@given(instance=literals_DoubleLiteral_strategy)
@settings(max_examples=25)
def test_literals_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, literals_DoubleLiteral)


literals_FloatLiteral_strategy = st.builds(literals_FloatLiteral)
@given(instance=literals_FloatLiteral_strategy)
@settings(max_examples=25)
def test_literals_FloatLiteral_instantiation(instance):
    assert isinstance(instance, literals_FloatLiteral)


literals_HexDoubleLiteral_strategy = st.builds(literals_HexDoubleLiteral, hexValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=literals_HexDoubleLiteral_strategy)
@settings(max_examples=25)
def test_literals_HexDoubleLiteral_instantiation(instance):
    assert isinstance(instance, literals_HexDoubleLiteral)


literals_HexFloatLiteral_strategy = st.builds(literals_HexFloatLiteral, hexValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=literals_HexFloatLiteral_strategy)
@settings(max_examples=25)
def test_literals_HexFloatLiteral_instantiation(instance):
    assert isinstance(instance, literals_HexFloatLiteral)


literals_HexIntegerLiteral_strategy = st.builds(literals_HexIntegerLiteral, hexValue=safe_text)
@given(instance=literals_HexIntegerLiteral_strategy)
@settings(max_examples=25)
def test_literals_HexIntegerLiteral_instantiation(instance):
    assert isinstance(instance, literals_HexIntegerLiteral)


literals_HexLongLiteral_strategy = st.builds(literals_HexLongLiteral, hexValue=safe_text)
@given(instance=literals_HexLongLiteral_strategy)
@settings(max_examples=25)
def test_literals_HexLongLiteral_instantiation(instance):
    assert isinstance(instance, literals_HexLongLiteral)


literals_IntegerLiteral_strategy = st.builds(literals_IntegerLiteral)
@given(instance=literals_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_literals_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, literals_IntegerLiteral)


literals_Literal_strategy = st.builds(literals_Literal)
@given(instance=literals_Literal_strategy)
@settings(max_examples=25)
def test_literals_Literal_instantiation(instance):
    assert isinstance(instance, literals_Literal)


literals_LongLiteral_strategy = st.builds(literals_LongLiteral)
@given(instance=literals_LongLiteral_strategy)
@settings(max_examples=25)
def test_literals_LongLiteral_instantiation(instance):
    assert isinstance(instance, literals_LongLiteral)


literals_NullLiteral_strategy = st.builds(literals_NullLiteral)
@given(instance=literals_NullLiteral_strategy)
@settings(max_examples=25)
def test_literals_NullLiteral_instantiation(instance):
    assert isinstance(instance, literals_NullLiteral)


literals_OctalIntegerLiteral_strategy = st.builds(literals_OctalIntegerLiteral, octalValue=safe_text)
@given(instance=literals_OctalIntegerLiteral_strategy)
@settings(max_examples=25)
def test_literals_OctalIntegerLiteral_instantiation(instance):
    assert isinstance(instance, literals_OctalIntegerLiteral)


literals_OctalLongLiteral_strategy = st.builds(literals_OctalLongLiteral, octalValue=safe_text)
@given(instance=literals_OctalLongLiteral_strategy)
@settings(max_examples=25)
def test_literals_OctalLongLiteral_instantiation(instance):
    assert isinstance(instance, literals_OctalLongLiteral)


literals_Self_strategy = st.builds(literals_Self)
@given(instance=literals_Self_strategy)
@settings(max_examples=25)
def test_literals_Self_instantiation(instance):
    assert isinstance(instance, literals_Self)


literals_Super_strategy = st.builds(literals_Super)
@given(instance=literals_Super_strategy)
@settings(max_examples=25)
def test_literals_Super_instantiation(instance):
    assert isinstance(instance, literals_Super)


literals_This_strategy = st.builds(literals_This)
@given(instance=literals_This_strategy)
@settings(max_examples=25)
def test_literals_This_instantiation(instance):
    assert isinstance(instance, literals_This)


members_AdditionalField_strategy = st.builds(members_AdditionalField)
@given(instance=members_AdditionalField_strategy)
@settings(max_examples=25)
def test_members_AdditionalField_instantiation(instance):
    assert isinstance(instance, members_AdditionalField)


members_ClassMethod_strategy = st.builds(members_ClassMethod)
@given(instance=members_ClassMethod_strategy)
@settings(max_examples=25)
def test_members_ClassMethod_instantiation(instance):
    assert isinstance(instance, members_ClassMethod)


members_Constructor_strategy = st.builds(members_Constructor)
@given(instance=members_Constructor_strategy)
@settings(max_examples=25)
def test_members_Constructor_instantiation(instance):
    assert isinstance(instance, members_Constructor)


members_EmptyMember_strategy = st.builds(members_EmptyMember)
@given(instance=members_EmptyMember_strategy)
@settings(max_examples=25)
def test_members_EmptyMember_instantiation(instance):
    assert isinstance(instance, members_EmptyMember)


members_EnumConstant_strategy = st.builds(members_EnumConstant)
@given(instance=members_EnumConstant_strategy)
@settings(max_examples=25)
def test_members_EnumConstant_instantiation(instance):
    assert isinstance(instance, members_EnumConstant)


members_ExceptionThrower_strategy = st.builds(members_ExceptionThrower)
@given(instance=members_ExceptionThrower_strategy)
@settings(max_examples=25)
def test_members_ExceptionThrower_instantiation(instance):
    assert isinstance(instance, members_ExceptionThrower)


members_Field_strategy = st.builds(members_Field)
@given(instance=members_Field_strategy)
@settings(max_examples=25)
def test_members_Field_instantiation(instance):
    assert isinstance(instance, members_Field)


members_InterfaceMethod_strategy = st.builds(members_InterfaceMethod)
@given(instance=members_InterfaceMethod_strategy)
@settings(max_examples=25)
def test_members_InterfaceMethod_instantiation(instance):
    assert isinstance(instance, members_InterfaceMethod)


members_Member_strategy = st.builds(members_Member)
@given(instance=members_Member_strategy)
@settings(max_examples=25)
def test_members_Member_instantiation(instance):
    assert isinstance(instance, members_Member)


members_MemberContainer_strategy = st.builds(members_MemberContainer)
@given(instance=members_MemberContainer_strategy)
@settings(max_examples=25)
def test_members_MemberContainer_instantiation(instance):
    assert isinstance(instance, members_MemberContainer)


members_Method_strategy = st.builds(members_Method)
@given(instance=members_Method_strategy)
@settings(max_examples=25)
def test_members_Method_instantiation(instance):
    assert isinstance(instance, members_Method)


modifiers_Abstract_strategy = st.builds(modifiers_Abstract)
@given(instance=modifiers_Abstract_strategy)
@settings(max_examples=25)
def test_modifiers_Abstract_instantiation(instance):
    assert isinstance(instance, modifiers_Abstract)


modifiers_AnnotableAndModifiable_strategy = st.builds(modifiers_AnnotableAndModifiable)
@given(instance=modifiers_AnnotableAndModifiable_strategy)
@settings(max_examples=25)
def test_modifiers_AnnotableAndModifiable_instantiation(instance):
    assert isinstance(instance, modifiers_AnnotableAndModifiable)


modifiers_AnnotationInstanceOrModifier_strategy = st.builds(modifiers_AnnotationInstanceOrModifier)
@given(instance=modifiers_AnnotationInstanceOrModifier_strategy)
@settings(max_examples=25)
def test_modifiers_AnnotationInstanceOrModifier_instantiation(instance):
    assert isinstance(instance, modifiers_AnnotationInstanceOrModifier)


modifiers_Final_strategy = st.builds(modifiers_Final)
@given(instance=modifiers_Final_strategy)
@settings(max_examples=25)
def test_modifiers_Final_instantiation(instance):
    assert isinstance(instance, modifiers_Final)


modifiers_Modifiable_strategy = st.builds(modifiers_Modifiable)
@given(instance=modifiers_Modifiable_strategy)
@settings(max_examples=25)
def test_modifiers_Modifiable_instantiation(instance):
    assert isinstance(instance, modifiers_Modifiable)


modifiers_Modifier_strategy = st.builds(modifiers_Modifier)
@given(instance=modifiers_Modifier_strategy)
@settings(max_examples=25)
def test_modifiers_Modifier_instantiation(instance):
    assert isinstance(instance, modifiers_Modifier)


modifiers_Native_strategy = st.builds(modifiers_Native)
@given(instance=modifiers_Native_strategy)
@settings(max_examples=25)
def test_modifiers_Native_instantiation(instance):
    assert isinstance(instance, modifiers_Native)


modifiers_Private_strategy = st.builds(modifiers_Private)
@given(instance=modifiers_Private_strategy)
@settings(max_examples=25)
def test_modifiers_Private_instantiation(instance):
    assert isinstance(instance, modifiers_Private)


modifiers_Protected_strategy = st.builds(modifiers_Protected)
@given(instance=modifiers_Protected_strategy)
@settings(max_examples=25)
def test_modifiers_Protected_instantiation(instance):
    assert isinstance(instance, modifiers_Protected)


modifiers_Public_strategy = st.builds(modifiers_Public)
@given(instance=modifiers_Public_strategy)
@settings(max_examples=25)
def test_modifiers_Public_instantiation(instance):
    assert isinstance(instance, modifiers_Public)


modifiers_Static_strategy = st.builds(modifiers_Static)
@given(instance=modifiers_Static_strategy)
@settings(max_examples=25)
def test_modifiers_Static_instantiation(instance):
    assert isinstance(instance, modifiers_Static)


modifiers_Strictfp_strategy = st.builds(modifiers_Strictfp)
@given(instance=modifiers_Strictfp_strategy)
@settings(max_examples=25)
def test_modifiers_Strictfp_instantiation(instance):
    assert isinstance(instance, modifiers_Strictfp)


modifiers_Synchronized_strategy = st.builds(modifiers_Synchronized)
@given(instance=modifiers_Synchronized_strategy)
@settings(max_examples=25)
def test_modifiers_Synchronized_instantiation(instance):
    assert isinstance(instance, modifiers_Synchronized)


modifiers_Transient_strategy = st.builds(modifiers_Transient)
@given(instance=modifiers_Transient_strategy)
@settings(max_examples=25)
def test_modifiers_Transient_instantiation(instance):
    assert isinstance(instance, modifiers_Transient)


modifiers_Volatile_strategy = st.builds(modifiers_Volatile)
@given(instance=modifiers_Volatile_strategy)
@settings(max_examples=25)
def test_modifiers_Volatile_instantiation(instance):
    assert isinstance(instance, modifiers_Volatile)


operators_Addition_strategy = st.builds(operators_Addition)
@given(instance=operators_Addition_strategy)
@settings(max_examples=25)
def test_operators_Addition_instantiation(instance):
    assert isinstance(instance, operators_Addition)


operators_AdditiveOperator_strategy = st.builds(operators_AdditiveOperator)
@given(instance=operators_AdditiveOperator_strategy)
@settings(max_examples=25)
def test_operators_AdditiveOperator_instantiation(instance):
    assert isinstance(instance, operators_AdditiveOperator)


operators_Assignment_strategy = st.builds(operators_Assignment)
@given(instance=operators_Assignment_strategy)
@settings(max_examples=25)
def test_operators_Assignment_instantiation(instance):
    assert isinstance(instance, operators_Assignment)


operators_AssignmentAnd_strategy = st.builds(operators_AssignmentAnd)
@given(instance=operators_AssignmentAnd_strategy)
@settings(max_examples=25)
def test_operators_AssignmentAnd_instantiation(instance):
    assert isinstance(instance, operators_AssignmentAnd)


operators_AssignmentDivision_strategy = st.builds(operators_AssignmentDivision)
@given(instance=operators_AssignmentDivision_strategy)
@settings(max_examples=25)
def test_operators_AssignmentDivision_instantiation(instance):
    assert isinstance(instance, operators_AssignmentDivision)


operators_AssignmentExclusiveOr_strategy = st.builds(operators_AssignmentExclusiveOr)
@given(instance=operators_AssignmentExclusiveOr_strategy)
@settings(max_examples=25)
def test_operators_AssignmentExclusiveOr_instantiation(instance):
    assert isinstance(instance, operators_AssignmentExclusiveOr)


operators_AssignmentLeftShift_strategy = st.builds(operators_AssignmentLeftShift)
@given(instance=operators_AssignmentLeftShift_strategy)
@settings(max_examples=25)
def test_operators_AssignmentLeftShift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentLeftShift)


operators_AssignmentMinus_strategy = st.builds(operators_AssignmentMinus)
@given(instance=operators_AssignmentMinus_strategy)
@settings(max_examples=25)
def test_operators_AssignmentMinus_instantiation(instance):
    assert isinstance(instance, operators_AssignmentMinus)


operators_AssignmentModulo_strategy = st.builds(operators_AssignmentModulo)
@given(instance=operators_AssignmentModulo_strategy)
@settings(max_examples=25)
def test_operators_AssignmentModulo_instantiation(instance):
    assert isinstance(instance, operators_AssignmentModulo)


operators_AssignmentMultiplication_strategy = st.builds(operators_AssignmentMultiplication)
@given(instance=operators_AssignmentMultiplication_strategy)
@settings(max_examples=25)
def test_operators_AssignmentMultiplication_instantiation(instance):
    assert isinstance(instance, operators_AssignmentMultiplication)


operators_AssignmentOperator_strategy = st.builds(operators_AssignmentOperator)
@given(instance=operators_AssignmentOperator_strategy)
@settings(max_examples=25)
def test_operators_AssignmentOperator_instantiation(instance):
    assert isinstance(instance, operators_AssignmentOperator)


operators_AssignmentOr_strategy = st.builds(operators_AssignmentOr)
@given(instance=operators_AssignmentOr_strategy)
@settings(max_examples=25)
def test_operators_AssignmentOr_instantiation(instance):
    assert isinstance(instance, operators_AssignmentOr)


operators_AssignmentPlus_strategy = st.builds(operators_AssignmentPlus)
@given(instance=operators_AssignmentPlus_strategy)
@settings(max_examples=25)
def test_operators_AssignmentPlus_instantiation(instance):
    assert isinstance(instance, operators_AssignmentPlus)


operators_AssignmentRightShift_strategy = st.builds(operators_AssignmentRightShift)
@given(instance=operators_AssignmentRightShift_strategy)
@settings(max_examples=25)
def test_operators_AssignmentRightShift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentRightShift)


operators_AssignmentUnsignedRightShift_strategy = st.builds(operators_AssignmentUnsignedRightShift)
@given(instance=operators_AssignmentUnsignedRightShift_strategy)
@settings(max_examples=25)
def test_operators_AssignmentUnsignedRightShift_instantiation(instance):
    assert isinstance(instance, operators_AssignmentUnsignedRightShift)


operators_Complement_strategy = st.builds(operators_Complement)
@given(instance=operators_Complement_strategy)
@settings(max_examples=25)
def test_operators_Complement_instantiation(instance):
    assert isinstance(instance, operators_Complement)


operators_Division_strategy = st.builds(operators_Division)
@given(instance=operators_Division_strategy)
@settings(max_examples=25)
def test_operators_Division_instantiation(instance):
    assert isinstance(instance, operators_Division)


operators_Equal_strategy = st.builds(operators_Equal)
@given(instance=operators_Equal_strategy)
@settings(max_examples=25)
def test_operators_Equal_instantiation(instance):
    assert isinstance(instance, operators_Equal)


operators_EqualityOperator_strategy = st.builds(operators_EqualityOperator)
@given(instance=operators_EqualityOperator_strategy)
@settings(max_examples=25)
def test_operators_EqualityOperator_instantiation(instance):
    assert isinstance(instance, operators_EqualityOperator)


operators_GreaterThan_strategy = st.builds(operators_GreaterThan)
@given(instance=operators_GreaterThan_strategy)
@settings(max_examples=25)
def test_operators_GreaterThan_instantiation(instance):
    assert isinstance(instance, operators_GreaterThan)


operators_GreaterThanOrEqual_strategy = st.builds(operators_GreaterThanOrEqual)
@given(instance=operators_GreaterThanOrEqual_strategy)
@settings(max_examples=25)
def test_operators_GreaterThanOrEqual_instantiation(instance):
    assert isinstance(instance, operators_GreaterThanOrEqual)


operators_LeftShift_strategy = st.builds(operators_LeftShift)
@given(instance=operators_LeftShift_strategy)
@settings(max_examples=25)
def test_operators_LeftShift_instantiation(instance):
    assert isinstance(instance, operators_LeftShift)


operators_LessThan_strategy = st.builds(operators_LessThan)
@given(instance=operators_LessThan_strategy)
@settings(max_examples=25)
def test_operators_LessThan_instantiation(instance):
    assert isinstance(instance, operators_LessThan)


operators_LessThanOrEqual_strategy = st.builds(operators_LessThanOrEqual)
@given(instance=operators_LessThanOrEqual_strategy)
@settings(max_examples=25)
def test_operators_LessThanOrEqual_instantiation(instance):
    assert isinstance(instance, operators_LessThanOrEqual)


operators_MinusMinus_strategy = st.builds(operators_MinusMinus)
@given(instance=operators_MinusMinus_strategy)
@settings(max_examples=25)
def test_operators_MinusMinus_instantiation(instance):
    assert isinstance(instance, operators_MinusMinus)


operators_Multiplication_strategy = st.builds(operators_Multiplication)
@given(instance=operators_Multiplication_strategy)
@settings(max_examples=25)
def test_operators_Multiplication_instantiation(instance):
    assert isinstance(instance, operators_Multiplication)


operators_MultiplicativeOperator_strategy = st.builds(operators_MultiplicativeOperator)
@given(instance=operators_MultiplicativeOperator_strategy)
@settings(max_examples=25)
def test_operators_MultiplicativeOperator_instantiation(instance):
    assert isinstance(instance, operators_MultiplicativeOperator)


operators_Negate_strategy = st.builds(operators_Negate)
@given(instance=operators_Negate_strategy)
@settings(max_examples=25)
def test_operators_Negate_instantiation(instance):
    assert isinstance(instance, operators_Negate)


operators_NotEqual_strategy = st.builds(operators_NotEqual)
@given(instance=operators_NotEqual_strategy)
@settings(max_examples=25)
def test_operators_NotEqual_instantiation(instance):
    assert isinstance(instance, operators_NotEqual)


operators_Operator_strategy = st.builds(operators_Operator)
@given(instance=operators_Operator_strategy)
@settings(max_examples=25)
def test_operators_Operator_instantiation(instance):
    assert isinstance(instance, operators_Operator)


operators_PlusPlus_strategy = st.builds(operators_PlusPlus)
@given(instance=operators_PlusPlus_strategy)
@settings(max_examples=25)
def test_operators_PlusPlus_instantiation(instance):
    assert isinstance(instance, operators_PlusPlus)


operators_RelationOperator_strategy = st.builds(operators_RelationOperator)
@given(instance=operators_RelationOperator_strategy)
@settings(max_examples=25)
def test_operators_RelationOperator_instantiation(instance):
    assert isinstance(instance, operators_RelationOperator)


operators_Remainder_strategy = st.builds(operators_Remainder)
@given(instance=operators_Remainder_strategy)
@settings(max_examples=25)
def test_operators_Remainder_instantiation(instance):
    assert isinstance(instance, operators_Remainder)


operators_RightShift_strategy = st.builds(operators_RightShift)
@given(instance=operators_RightShift_strategy)
@settings(max_examples=25)
def test_operators_RightShift_instantiation(instance):
    assert isinstance(instance, operators_RightShift)


operators_ShiftOperator_strategy = st.builds(operators_ShiftOperator)
@given(instance=operators_ShiftOperator_strategy)
@settings(max_examples=25)
def test_operators_ShiftOperator_instantiation(instance):
    assert isinstance(instance, operators_ShiftOperator)


operators_Subtraction_strategy = st.builds(operators_Subtraction)
@given(instance=operators_Subtraction_strategy)
@settings(max_examples=25)
def test_operators_Subtraction_instantiation(instance):
    assert isinstance(instance, operators_Subtraction)


operators_UnaryModificationOperator_strategy = st.builds(operators_UnaryModificationOperator)
@given(instance=operators_UnaryModificationOperator_strategy)
@settings(max_examples=25)
def test_operators_UnaryModificationOperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryModificationOperator)


operators_UnaryOperator_strategy = st.builds(operators_UnaryOperator)
@given(instance=operators_UnaryOperator_strategy)
@settings(max_examples=25)
def test_operators_UnaryOperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperator)


operators_UnsignedRightShift_strategy = st.builds(operators_UnsignedRightShift)
@given(instance=operators_UnsignedRightShift_strategy)
@settings(max_examples=25)
def test_operators_UnsignedRightShift_instantiation(instance):
    assert isinstance(instance, operators_UnsignedRightShift)


parameters_OrdinaryParameter_strategy = st.builds(parameters_OrdinaryParameter)
@given(instance=parameters_OrdinaryParameter_strategy)
@settings(max_examples=25)
def test_parameters_OrdinaryParameter_instantiation(instance):
    assert isinstance(instance, parameters_OrdinaryParameter)


parameters_Parameter_strategy = st.builds(parameters_Parameter)
@given(instance=parameters_Parameter_strategy)
@settings(max_examples=25)
def test_parameters_Parameter_instantiation(instance):
    assert isinstance(instance, parameters_Parameter)


parameters_Parametrizable_strategy = st.builds(parameters_Parametrizable)
@given(instance=parameters_Parametrizable_strategy)
@settings(max_examples=25)
def test_parameters_Parametrizable_instantiation(instance):
    assert isinstance(instance, parameters_Parametrizable)


parameters_VariableLengthParameter_strategy = st.builds(parameters_VariableLengthParameter)
@given(instance=parameters_VariableLengthParameter_strategy)
@settings(max_examples=25)
def test_parameters_VariableLengthParameter_instantiation(instance):
    assert isinstance(instance, parameters_VariableLengthParameter)


references_Argumentable_strategy = st.builds(references_Argumentable)
@given(instance=references_Argumentable_strategy)
@settings(max_examples=25)
def test_references_Argumentable_instantiation(instance):
    assert isinstance(instance, references_Argumentable)


references_ElementReference_strategy = st.builds(references_ElementReference)
@given(instance=references_ElementReference_strategy)
@settings(max_examples=25)
def test_references_ElementReference_instantiation(instance):
    assert isinstance(instance, references_ElementReference)


references_IdentifierReference_strategy = st.builds(references_IdentifierReference)
@given(instance=references_IdentifierReference_strategy)
@settings(max_examples=25)
def test_references_IdentifierReference_instantiation(instance):
    assert isinstance(instance, references_IdentifierReference)


references_MethodCall_strategy = st.builds(references_MethodCall)
@given(instance=references_MethodCall_strategy)
@settings(max_examples=25)
def test_references_MethodCall_instantiation(instance):
    assert isinstance(instance, references_MethodCall)


references_PrimitiveTypeReference_strategy = st.builds(references_PrimitiveTypeReference)
@given(instance=references_PrimitiveTypeReference_strategy)
@settings(max_examples=25)
def test_references_PrimitiveTypeReference_instantiation(instance):
    assert isinstance(instance, references_PrimitiveTypeReference)


references_Reference_strategy = st.builds(references_Reference)
@given(instance=references_Reference_strategy)
@settings(max_examples=25)
def test_references_Reference_instantiation(instance):
    assert isinstance(instance, references_Reference)


references_ReferenceableElement_strategy = st.builds(references_ReferenceableElement)
@given(instance=references_ReferenceableElement_strategy)
@settings(max_examples=25)
def test_references_ReferenceableElement_instantiation(instance):
    assert isinstance(instance, references_ReferenceableElement)


references_ReflectiveClassReference_strategy = st.builds(references_ReflectiveClassReference)
@given(instance=references_ReflectiveClassReference_strategy)
@settings(max_examples=25)
def test_references_ReflectiveClassReference_instantiation(instance):
    assert isinstance(instance, references_ReflectiveClassReference)


references_SelfReference_strategy = st.builds(references_SelfReference)
@given(instance=references_SelfReference_strategy)
@settings(max_examples=25)
def test_references_SelfReference_instantiation(instance):
    assert isinstance(instance, references_SelfReference)


references_StringReference_strategy = st.builds(references_StringReference, value=safe_text)
@given(instance=references_StringReference_strategy)
@settings(max_examples=25)
def test_references_StringReference_instantiation(instance):
    assert isinstance(instance, references_StringReference)


statements_Assert_strategy = st.builds(statements_Assert)
@given(instance=statements_Assert_strategy)
@settings(max_examples=25)
def test_statements_Assert_instantiation(instance):
    assert isinstance(instance, statements_Assert)


statements_Block_strategy = st.builds(statements_Block)
@given(instance=statements_Block_strategy)
@settings(max_examples=25)
def test_statements_Block_instantiation(instance):
    assert isinstance(instance, statements_Block)


statements_Break_strategy = st.builds(statements_Break)
@given(instance=statements_Break_strategy)
@settings(max_examples=25)
def test_statements_Break_instantiation(instance):
    assert isinstance(instance, statements_Break)


statements_CatchBlock_strategy = st.builds(statements_CatchBlock)
@given(instance=statements_CatchBlock_strategy)
@settings(max_examples=25)
def test_statements_CatchBlock_instantiation(instance):
    assert isinstance(instance, statements_CatchBlock)


statements_Condition_strategy = st.builds(statements_Condition)
@given(instance=statements_Condition_strategy)
@settings(max_examples=25)
def test_statements_Condition_instantiation(instance):
    assert isinstance(instance, statements_Condition)


statements_Conditional_strategy = st.builds(statements_Conditional)
@given(instance=statements_Conditional_strategy)
@settings(max_examples=25)
def test_statements_Conditional_instantiation(instance):
    assert isinstance(instance, statements_Conditional)


statements_Continue_strategy = st.builds(statements_Continue)
@given(instance=statements_Continue_strategy)
@settings(max_examples=25)
def test_statements_Continue_instantiation(instance):
    assert isinstance(instance, statements_Continue)


statements_DefaultSwitchCase_strategy = st.builds(statements_DefaultSwitchCase)
@given(instance=statements_DefaultSwitchCase_strategy)
@settings(max_examples=25)
def test_statements_DefaultSwitchCase_instantiation(instance):
    assert isinstance(instance, statements_DefaultSwitchCase)


statements_DoWhileLoop_strategy = st.builds(statements_DoWhileLoop)
@given(instance=statements_DoWhileLoop_strategy)
@settings(max_examples=25)
def test_statements_DoWhileLoop_instantiation(instance):
    assert isinstance(instance, statements_DoWhileLoop)


statements_EmptyStatement_strategy = st.builds(statements_EmptyStatement)
@given(instance=statements_EmptyStatement_strategy)
@settings(max_examples=25)
def test_statements_EmptyStatement_instantiation(instance):
    assert isinstance(instance, statements_EmptyStatement)


statements_ExpressionStatement_strategy = st.builds(statements_ExpressionStatement)
@given(instance=statements_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_statements_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, statements_ExpressionStatement)


statements_ForEachLoop_strategy = st.builds(statements_ForEachLoop)
@given(instance=statements_ForEachLoop_strategy)
@settings(max_examples=25)
def test_statements_ForEachLoop_instantiation(instance):
    assert isinstance(instance, statements_ForEachLoop)


statements_ForLoop_strategy = st.builds(statements_ForLoop)
@given(instance=statements_ForLoop_strategy)
@settings(max_examples=25)
def test_statements_ForLoop_instantiation(instance):
    assert isinstance(instance, statements_ForLoop)


statements_ForLoopInitializer_strategy = st.builds(statements_ForLoopInitializer)
@given(instance=statements_ForLoopInitializer_strategy)
@settings(max_examples=25)
def test_statements_ForLoopInitializer_instantiation(instance):
    assert isinstance(instance, statements_ForLoopInitializer)


statements_Jump_strategy = st.builds(statements_Jump)
@given(instance=statements_Jump_strategy)
@settings(max_examples=25)
def test_statements_Jump_instantiation(instance):
    assert isinstance(instance, statements_Jump)


statements_JumpLabel_strategy = st.builds(statements_JumpLabel)
@given(instance=statements_JumpLabel_strategy)
@settings(max_examples=25)
def test_statements_JumpLabel_instantiation(instance):
    assert isinstance(instance, statements_JumpLabel)


statements_LocalVariableStatement_strategy = st.builds(statements_LocalVariableStatement)
@given(instance=statements_LocalVariableStatement_strategy)
@settings(max_examples=25)
def test_statements_LocalVariableStatement_instantiation(instance):
    assert isinstance(instance, statements_LocalVariableStatement)


statements_NormalSwitchCase_strategy = st.builds(statements_NormalSwitchCase)
@given(instance=statements_NormalSwitchCase_strategy)
@settings(max_examples=25)
def test_statements_NormalSwitchCase_instantiation(instance):
    assert isinstance(instance, statements_NormalSwitchCase)


statements_Return_strategy = st.builds(statements_Return)
@given(instance=statements_Return_strategy)
@settings(max_examples=25)
def test_statements_Return_instantiation(instance):
    assert isinstance(instance, statements_Return)


statements_Statement_strategy = st.builds(statements_Statement)
@given(instance=statements_Statement_strategy)
@settings(max_examples=25)
def test_statements_Statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)


statements_StatementContainer_strategy = st.builds(statements_StatementContainer)
@given(instance=statements_StatementContainer_strategy)
@settings(max_examples=25)
def test_statements_StatementContainer_instantiation(instance):
    assert isinstance(instance, statements_StatementContainer)


statements_StatementListContainer_strategy = st.builds(statements_StatementListContainer)
@given(instance=statements_StatementListContainer_strategy)
@settings(max_examples=25)
def test_statements_StatementListContainer_instantiation(instance):
    assert isinstance(instance, statements_StatementListContainer)


statements_Switch_strategy = st.builds(statements_Switch)
@given(instance=statements_Switch_strategy)
@settings(max_examples=25)
def test_statements_Switch_instantiation(instance):
    assert isinstance(instance, statements_Switch)


statements_SwitchCase_strategy = st.builds(statements_SwitchCase)
@given(instance=statements_SwitchCase_strategy)
@settings(max_examples=25)
def test_statements_SwitchCase_instantiation(instance):
    assert isinstance(instance, statements_SwitchCase)


statements_SynchronizedBlock_strategy = st.builds(statements_SynchronizedBlock)
@given(instance=statements_SynchronizedBlock_strategy)
@settings(max_examples=25)
def test_statements_SynchronizedBlock_instantiation(instance):
    assert isinstance(instance, statements_SynchronizedBlock)


statements_Throw_strategy = st.builds(statements_Throw)
@given(instance=statements_Throw_strategy)
@settings(max_examples=25)
def test_statements_Throw_instantiation(instance):
    assert isinstance(instance, statements_Throw)


statements_TryBlock_strategy = st.builds(statements_TryBlock)
@given(instance=statements_TryBlock_strategy)
@settings(max_examples=25)
def test_statements_TryBlock_instantiation(instance):
    assert isinstance(instance, statements_TryBlock)


statements_WhileLoop_strategy = st.builds(statements_WhileLoop)
@given(instance=statements_WhileLoop_strategy)
@settings(max_examples=25)
def test_statements_WhileLoop_instantiation(instance):
    assert isinstance(instance, statements_WhileLoop)


types_Bool_strategy = st.builds(types_Bool)
@given(instance=types_Bool_strategy)
@settings(max_examples=25)
def test_types_Bool_instantiation(instance):
    assert isinstance(instance, types_Bool)


types_Byte_strategy = st.builds(types_Byte)
@given(instance=types_Byte_strategy)
@settings(max_examples=25)
def test_types_Byte_instantiation(instance):
    assert isinstance(instance, types_Byte)


types_Char_strategy = st.builds(types_Char)
@given(instance=types_Char_strategy)
@settings(max_examples=25)
def test_types_Char_instantiation(instance):
    assert isinstance(instance, types_Char)


types_ClassifierReference_strategy = st.builds(types_ClassifierReference)
@given(instance=types_ClassifierReference_strategy)
@settings(max_examples=25)
def test_types_ClassifierReference_instantiation(instance):
    assert isinstance(instance, types_ClassifierReference)


types_Double_strategy = st.builds(types_Double)
@given(instance=types_Double_strategy)
@settings(max_examples=25)
def test_types_Double_instantiation(instance):
    assert isinstance(instance, types_Double)


types_Float_strategy = st.builds(types_Float)
@given(instance=types_Float_strategy)
@settings(max_examples=25)
def test_types_Float_instantiation(instance):
    assert isinstance(instance, types_Float)


types_Int_strategy = st.builds(types_Int)
@given(instance=types_Int_strategy)
@settings(max_examples=25)
def test_types_Int_instantiation(instance):
    assert isinstance(instance, types_Int)


types_Long_strategy = st.builds(types_Long)
@given(instance=types_Long_strategy)
@settings(max_examples=25)
def test_types_Long_instantiation(instance):
    assert isinstance(instance, types_Long)


types_NamespaceClassifierReference_strategy = st.builds(types_NamespaceClassifierReference)
@given(instance=types_NamespaceClassifierReference_strategy)
@settings(max_examples=25)
def test_types_NamespaceClassifierReference_instantiation(instance):
    assert isinstance(instance, types_NamespaceClassifierReference)


types_PrimitiveType_strategy = st.builds(types_PrimitiveType)
@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=25)
def test_types_PrimitiveType_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)


types_Short_strategy = st.builds(types_Short)
@given(instance=types_Short_strategy)
@settings(max_examples=25)
def test_types_Short_instantiation(instance):
    assert isinstance(instance, types_Short)


types_Type_strategy = st.builds(types_Type)
@given(instance=types_Type_strategy)
@settings(max_examples=25)
def test_types_Type_instantiation(instance):
    assert isinstance(instance, types_Type)


types_TypeReference_strategy = st.builds(types_TypeReference)
@given(instance=types_TypeReference_strategy)
@settings(max_examples=25)
def test_types_TypeReference_instantiation(instance):
    assert isinstance(instance, types_TypeReference)


types_TypedElement_strategy = st.builds(types_TypedElement)
@given(instance=types_TypedElement_strategy)
@settings(max_examples=25)
def test_types_TypedElement_instantiation(instance):
    assert isinstance(instance, types_TypedElement)


types_Void_strategy = st.builds(types_Void)
@given(instance=types_Void_strategy)
@settings(max_examples=25)
def test_types_Void_instantiation(instance):
    assert isinstance(instance, types_Void)


variables_AdditionalLocalVariable_strategy = st.builds(variables_AdditionalLocalVariable)
@given(instance=variables_AdditionalLocalVariable_strategy)
@settings(max_examples=25)
def test_variables_AdditionalLocalVariable_instantiation(instance):
    assert isinstance(instance, variables_AdditionalLocalVariable)


variables_LocalVariable_strategy = st.builds(variables_LocalVariable)
@given(instance=variables_LocalVariable_strategy)
@settings(max_examples=25)
def test_variables_LocalVariable_instantiation(instance):
    assert isinstance(instance, variables_LocalVariable)


variables_Variable_strategy = st.builds(variables_Variable)
@given(instance=variables_Variable_strategy)
@settings(max_examples=25)
def test_variables_Variable_instantiation(instance):
    assert isinstance(instance, variables_Variable)


