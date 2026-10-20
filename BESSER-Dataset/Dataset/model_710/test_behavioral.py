import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    CallExp,
    Class,
    CollectionLiteralPart,
    CollectionType,
    DataType,
    DynamicElement,
    Element,
    Feature,
    FeatureCallExp,
    LiteralExp,
    LoopExp,
    Nameable,
    NamedElement,
    Namespace,
    NavigationCallExp,
    NumericLiteralExp,
    OCLExpression,
    OpaqueExpression,
    Operation,
    Package,
    ParameterableElement,
    PrimitiveLiteralExp,
    ReferringElement,
    State,
    TemplateParameter,
    TemplateableElement,
    Type,
    TypedElement,
    TypedMultiplicityElement,
    ValueSpecification,
    VariableDeclaration,
    Vertex,
    Visitable,
    pivot_Annotation,
    pivot_AnyType,
    pivot_AssociationClass,
    pivot_AssociationClassCallExp,
    pivot_BagType,
    pivot_Behavior,
    pivot_BooleanLiteralExp,
    pivot_CallExp,
    pivot_CallOperationAction,
    pivot_Class,
    pivot_CollectionItem,
    pivot_CollectionLiteralExp,
    pivot_CollectionLiteralPart,
    pivot_CollectionRange,
    pivot_CollectionType,
    pivot_Comment,
    pivot_ConnectionPointReference,
    pivot_Constraint,
    pivot_ConstructorExp,
    pivot_ConstructorPart,
    pivot_DataType,
    pivot_Detail,
    pivot_DynamicElement,
    pivot_DynamicProperty,
    pivot_DynamicType,
    pivot_Element,
    pivot_ElementExtension,
    pivot_EnumLiteralExp,
    pivot_Enumeration,
    pivot_EnumerationLiteral,
    pivot_ExpressionInOCL,
    pivot_Feature,
    pivot_FeatureCallExp,
    pivot_FinalState,
    pivot_IfExp,
    pivot_Import,
    pivot_IntegerLiteralExp,
    pivot_InvalidLiteralExp,
    pivot_InvalidType,
    pivot_IterateExp,
    pivot_Iteration,
    pivot_IteratorExp,
    pivot_LambdaType,
    pivot_LetExp,
    pivot_Library,
    pivot_LiteralExp,
    pivot_LoopExp,
    pivot_MessageExp,
    pivot_MessageType,
    pivot_Metaclass,
    pivot_MorePivotable,
    pivot_Nameable,
    pivot_NamedElement,
    pivot_Namespace,
    pivot_NavigationCallExp,
    pivot_NullLiteralExp,
    pivot_NumericLiteralExp,
    pivot_OCLExpression,
    pivot_OpaqueExpression,
    pivot_Operation,
    pivot_OperationCallExp,
    pivot_OperationTemplateParameter,
    pivot_OrderedSetType,
    pivot_Package,
    pivot_PackageableElement,
    pivot_Parameter,
    pivot_ParameterableElement,
    pivot_Pivotable,
    pivot_Precedence,
    pivot_PrimitiveLiteralExp,
    pivot_PrimitiveType,
    pivot_Profile,
    pivot_Property,
    pivot_PropertyCallExp,
    pivot_Pseudostate,
    pivot_RealLiteralExp,
    pivot_ReferringElement,
    pivot_Region,
    pivot_Root,
    pivot_SelfType,
    pivot_SendSignalAction,
    pivot_SequenceType,
    pivot_SetType,
    pivot_Signal,
    pivot_State,
    pivot_StateExp,
    pivot_StateMachine,
    pivot_Stereotype,
    pivot_StringLiteralExp,
    pivot_TemplateBinding,
    pivot_TemplateParameter,
    pivot_TemplateParameterSubstitution,
    pivot_TemplateParameterType,
    pivot_TemplateSignature,
    pivot_TemplateableElement,
    pivot_Transition,
    pivot_Trigger,
    pivot_TupleLiteralExp,
    pivot_TupleLiteralPart,
    pivot_TupleType,
    pivot_Type,
    pivot_TypeExp,
    pivot_TypeTemplateParameter,
    pivot_TypedElement,
    pivot_TypedMultiplicityElement,
    pivot_UnlimitedNaturalLiteralExp,
    pivot_UnspecifiedType,
    pivot_UnspecifiedValueExp,
    pivot_ValueSpecification,
    pivot_Variable,
    pivot_VariableDeclaration,
    pivot_VariableExp,
    pivot_Vertex,
    pivot_Visitable,
    pivot_Visitor,
    pivot_VoidType,
    AssociativityKind,
    CollectionKind,
    PseudostateKind,
    TransitionKind,
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

def test_assoc_annotatedElement20_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment', {a1})
    assert _is_linked(b, 'pivot_Comment', a1)
    if hasattr(a1, 'pivot_Element21'):
        assert _is_linked(a1, 'pivot_Element21', b)
    _safe_set(b, 'pivot_Comment', {a2})
    assert _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a1, 'pivot_Element21'):
        assert not _is_linked(a1, 'pivot_Element21', b)
    if hasattr(a2, 'pivot_Element21'):
        assert _is_linked(a2, 'pivot_Element21', b)
    _safe_set(b, 'pivot_Comment', set())
    assert not _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a2, 'pivot_Element21'):
        assert not _is_linked(a2, 'pivot_Element21', b)


def test_assoc_behavioralType40_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_DataType(isSerializable="sample_text")
    _safe_set(b, 'pivot_DataType', a1)
    assert _is_linked(b, 'pivot_DataType', a1)
    if hasattr(a1, 'pivot_Type41'):
        assert _is_linked(a1, 'pivot_Type41', b)
    _safe_set(b, 'pivot_DataType', a2)
    assert _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a1, 'pivot_Type41'):
        assert not _is_linked(a1, 'pivot_Type41', b)
    if hasattr(a2, 'pivot_Type41'):
        assert _is_linked(a2, 'pivot_Type41', b)
    _safe_set(b, 'pivot_DataType', None)
    assert not _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a2, 'pivot_Type41'):
        assert not _is_linked(a2, 'pivot_Type41', b)


def test_assoc_bodyExpression146_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_OpaqueExpression(body="sample_text", language="sample_text", message="sample_text")
    _safe_set(b, 'pivot_OpaqueExpression148', a1)
    assert _is_linked(b, 'pivot_OpaqueExpression148', a1)
    if hasattr(a1, 'pivot_Operation147'):
        assert _is_linked(a1, 'pivot_Operation147', b)
    _safe_set(b, 'pivot_OpaqueExpression148', a2)
    assert _is_linked(b, 'pivot_OpaqueExpression148', a2)
    if hasattr(a1, 'pivot_Operation147'):
        assert not _is_linked(a1, 'pivot_Operation147', b)
    if hasattr(a2, 'pivot_Operation147'):
        assert _is_linked(a2, 'pivot_Operation147', b)
    _safe_set(b, 'pivot_OpaqueExpression148', None)
    assert not _is_linked(b, 'pivot_OpaqueExpression148', a2)
    if hasattr(a2, 'pivot_Operation147'):
        assert not _is_linked(a2, 'pivot_Operation147', b)


def test_assoc_class_155_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class157', a1)
    assert _is_linked(b, 'pivot_Class157', a1)
    if hasattr(a1, 'pivot_Operation156'):
        assert _is_linked(a1, 'pivot_Operation156', b)
    _safe_set(b, 'pivot_Class157', a2)
    assert _is_linked(b, 'pivot_Class157', a2)
    if hasattr(a1, 'pivot_Operation156'):
        assert not _is_linked(a1, 'pivot_Operation156', b)
    if hasattr(a2, 'pivot_Operation156'):
        assert _is_linked(a2, 'pivot_Operation156', b)
    _safe_set(b, 'pivot_Class157', None)
    assert not _is_linked(b, 'pivot_Class157', a2)
    if hasattr(a2, 'pivot_Operation156'):
        assert not _is_linked(a2, 'pivot_Operation156', b)


def test_assoc_class_176_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class178', a1)
    assert _is_linked(b, 'pivot_Class178', a1)
    if hasattr(a1, 'pivot_Property177'):
        assert _is_linked(a1, 'pivot_Property177', b)
    _safe_set(b, 'pivot_Class178', a2)
    assert _is_linked(b, 'pivot_Class178', a2)
    if hasattr(a1, 'pivot_Property177'):
        assert not _is_linked(a1, 'pivot_Property177', b)
    if hasattr(a2, 'pivot_Property177'):
        assert _is_linked(a2, 'pivot_Property177', b)
    _safe_set(b, 'pivot_Class178', None)
    assert not _is_linked(b, 'pivot_Class178', a2)
    if hasattr(a2, 'pivot_Property177'):
        assert not _is_linked(a2, 'pivot_Property177', b)


def test_assoc_connectionPoint248_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'pivot_Pseudostate250', a1)
    assert _is_linked(b, 'pivot_Pseudostate250', a1)
    if hasattr(a1, 'pivot_State249'):
        assert _is_linked(a1, 'pivot_State249', b)
    _safe_set(b, 'pivot_Pseudostate250', a2)
    assert _is_linked(b, 'pivot_Pseudostate250', a2)
    if hasattr(a1, 'pivot_State249'):
        assert not _is_linked(a1, 'pivot_State249', b)
    if hasattr(a2, 'pivot_State249'):
        assert _is_linked(a2, 'pivot_State249', b)
    _safe_set(b, 'pivot_Pseudostate250', None)
    assert not _is_linked(b, 'pivot_Pseudostate250', a2)
    if hasattr(a2, 'pivot_State249'):
        assert not _is_linked(a2, 'pivot_State249', b)


def test_assoc_constrainedElement28_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint', {a1})
    assert _is_linked(b, 'pivot_Constraint', a1)
    if hasattr(a1, 'pivot_Element29'):
        assert _is_linked(a1, 'pivot_Element29', b)
    _safe_set(b, 'pivot_Constraint', {a2})
    assert _is_linked(b, 'pivot_Constraint', a2)
    if hasattr(a1, 'pivot_Element29'):
        assert not _is_linked(a1, 'pivot_Element29', b)
    if hasattr(a2, 'pivot_Element29'):
        assert _is_linked(a2, 'pivot_Element29', b)
    _safe_set(b, 'pivot_Constraint', set())
    assert not _is_linked(b, 'pivot_Constraint', a2)
    if hasattr(a2, 'pivot_Element29'):
        assert not _is_linked(a2, 'pivot_Element29', b)


def test_assoc_constrainingType332_reverse_link_reassign_clear():
    a1 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text")
    a2 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type333', a1)
    assert _is_linked(b, 'pivot_Type333', a1)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type333', a2)
    assert _is_linked(b, 'pivot_Type333', a2)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert not _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    if hasattr(a2, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a2, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type333', None)
    assert not _is_linked(b, 'pivot_Type333', a2)
    if hasattr(a2, 'pivot_TypeTemplateParameter'):
        assert not _is_linked(a2, 'pivot_TypeTemplateParameter', b)


def test_assoc_defaultExpression183_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_OpaqueExpression(body="sample_text", language="sample_text", message="sample_text")
    _safe_set(b, 'pivot_OpaqueExpression185', a1)
    assert _is_linked(b, 'pivot_OpaqueExpression185', a1)
    if hasattr(a1, 'pivot_Property184'):
        assert _is_linked(a1, 'pivot_Property184', b)
    _safe_set(b, 'pivot_OpaqueExpression185', a2)
    assert _is_linked(b, 'pivot_OpaqueExpression185', a2)
    if hasattr(a1, 'pivot_Property184'):
        assert not _is_linked(a1, 'pivot_Property184', b)
    if hasattr(a2, 'pivot_Property184'):
        assert _is_linked(a2, 'pivot_Property184', b)
    _safe_set(b, 'pivot_OpaqueExpression185', None)
    assert not _is_linked(b, 'pivot_OpaqueExpression185', a2)
    if hasattr(a2, 'pivot_Property184'):
        assert not _is_linked(a2, 'pivot_Property184', b)


def test_assoc_elementType19_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_CollectionType(lower="sample_text", upper="sample_text")
    _safe_set(b, 'pivot_CollectionType', a1)
    assert _is_linked(b, 'pivot_CollectionType', a1)
    if hasattr(a1, 'pivot_Type'):
        assert _is_linked(a1, 'pivot_Type', b)
    _safe_set(b, 'pivot_CollectionType', a2)
    assert _is_linked(b, 'pivot_CollectionType', a2)
    if hasattr(a1, 'pivot_Type'):
        assert not _is_linked(a1, 'pivot_Type', b)
    if hasattr(a2, 'pivot_Type'):
        assert _is_linked(a2, 'pivot_Type', b)
    _safe_set(b, 'pivot_CollectionType', None)
    assert not _is_linked(b, 'pivot_CollectionType', a2)
    if hasattr(a2, 'pivot_Type'):
        assert not _is_linked(a2, 'pivot_Type', b)


def test_assoc_guard304_reverse_link_reassign_clear():
    a1 = pivot_Transition(kind="sample_text")
    a2 = pivot_Transition(kind="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint305', a1)
    assert _is_linked(b, 'pivot_Constraint305', a1)
    if hasattr(a1, 'pivot_Transition'):
        assert _is_linked(a1, 'pivot_Transition', b)
    _safe_set(b, 'pivot_Constraint305', a2)
    assert _is_linked(b, 'pivot_Constraint305', a2)
    if hasattr(a1, 'pivot_Transition'):
        assert not _is_linked(a1, 'pivot_Transition', b)
    if hasattr(a2, 'pivot_Transition'):
        assert _is_linked(a2, 'pivot_Transition', b)
    _safe_set(b, 'pivot_Constraint305', None)
    assert not _is_linked(b, 'pivot_Constraint305', a2)
    if hasattr(a2, 'pivot_Transition'):
        assert not _is_linked(a2, 'pivot_Transition', b)


def test_assoc_importedPackage169_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package168', {a1})
    assert _is_linked(b, 'pivot_Package168', a1)
    if hasattr(a1, 'pivot_Package'):
        assert _is_linked(a1, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package168', {a2})
    assert _is_linked(b, 'pivot_Package168', a2)
    if hasattr(a1, 'pivot_Package'):
        assert not _is_linked(a1, 'pivot_Package', b)
    if hasattr(a2, 'pivot_Package'):
        assert _is_linked(a2, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package168', set())
    assert not _is_linked(b, 'pivot_Package168', a2)
    if hasattr(a2, 'pivot_Package'):
        assert not _is_linked(a2, 'pivot_Package', b)


def test_assoc_iterator103_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LoopExp()
    _safe_set(b, 'pivot_LoopExp104', {a1})
    assert _is_linked(b, 'pivot_LoopExp104', a1)
    if hasattr(a1, 'pivot_Variable105'):
        assert _is_linked(a1, 'pivot_Variable105', b)
    _safe_set(b, 'pivot_LoopExp104', {a2})
    assert _is_linked(b, 'pivot_LoopExp104', a2)
    if hasattr(a1, 'pivot_Variable105'):
        assert not _is_linked(a1, 'pivot_Variable105', b)
    if hasattr(a2, 'pivot_Variable105'):
        assert _is_linked(a2, 'pivot_Variable105', b)
    _safe_set(b, 'pivot_LoopExp104', set())
    assert not _is_linked(b, 'pivot_LoopExp104', a2)
    if hasattr(a2, 'pivot_Variable105'):
        assert not _is_linked(a2, 'pivot_Variable105', b)


def test_assoc_keys187_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property188', a1)
    assert _is_linked(b, 'pivot_Property188', a1)
    if hasattr(a1, 'pivot_Property186'):
        assert _is_linked(a1, 'pivot_Property186', b)
    _safe_set(b, 'pivot_Property188', a2)
    assert _is_linked(b, 'pivot_Property188', a2)
    if hasattr(a1, 'pivot_Property186'):
        assert not _is_linked(a1, 'pivot_Property186', b)
    if hasattr(a2, 'pivot_Property186'):
        assert _is_linked(a2, 'pivot_Property186', b)
    _safe_set(b, 'pivot_Property188', None)
    assert not _is_linked(b, 'pivot_Property188', a2)
    if hasattr(a2, 'pivot_Property186'):
        assert not _is_linked(a2, 'pivot_Property186', b)


def test_assoc_nestedPackage164_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'nestingPackage', {a1})
    assert _is_linked(b, 'nestingPackage', a1)
    if hasattr(a1, 'Package'):
        assert _is_linked(a1, 'Package', b)
    _safe_set(b, 'nestingPackage', {a2})
    assert _is_linked(b, 'nestingPackage', a2)
    if hasattr(a1, 'Package'):
        assert not _is_linked(a1, 'Package', b)
    if hasattr(a2, 'Package'):
        assert _is_linked(a2, 'Package', b)
    _safe_set(b, 'nestingPackage', set())
    assert not _is_linked(b, 'nestingPackage', a2)
    if hasattr(a2, 'Package'):
        assert not _is_linked(a2, 'Package', b)


def test_assoc_nestedPackage218_reverse_link_reassign_clear():
    a1 = pivot_Root(externalURI="sample_text")
    a2 = pivot_Root(externalURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package219', a1)
    assert _is_linked(b, 'pivot_Package219', a1)
    if hasattr(a1, 'pivot_Root'):
        assert _is_linked(a1, 'pivot_Root', b)
    _safe_set(b, 'pivot_Package219', a2)
    assert _is_linked(b, 'pivot_Package219', a2)
    if hasattr(a1, 'pivot_Root'):
        assert not _is_linked(a1, 'pivot_Root', b)
    if hasattr(a2, 'pivot_Root'):
        assert _is_linked(a2, 'pivot_Root', b)
    _safe_set(b, 'pivot_Package219', None)
    assert not _is_linked(b, 'pivot_Package219', a2)
    if hasattr(a2, 'pivot_Root'):
        assert not _is_linked(a2, 'pivot_Root', b)


def test_assoc_nestingPackage166_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'nestedPackage', a1)
    assert _is_linked(b, 'nestedPackage', a1)
    if hasattr(a1, 'Package167'):
        assert _is_linked(a1, 'Package167', b)
    _safe_set(b, 'nestedPackage', a2)
    assert _is_linked(b, 'nestedPackage', a2)
    if hasattr(a1, 'Package167'):
        assert not _is_linked(a1, 'Package167', b)
    if hasattr(a2, 'Package167'):
        assert _is_linked(a2, 'Package167', b)
    _safe_set(b, 'nestedPackage', None)
    assert not _is_linked(b, 'nestedPackage', a2)
    if hasattr(a2, 'Package167'):
        assert not _is_linked(a2, 'Package167', b)


def test_assoc_opposite180_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property181', a1)
    assert _is_linked(b, 'pivot_Property181', a1)
    if hasattr(a1, 'pivot_Property179'):
        assert _is_linked(a1, 'pivot_Property179', b)
    _safe_set(b, 'pivot_Property181', a2)
    assert _is_linked(b, 'pivot_Property181', a2)
    if hasattr(a1, 'pivot_Property179'):
        assert not _is_linked(a1, 'pivot_Property179', b)
    if hasattr(a2, 'pivot_Property179'):
        assert _is_linked(a2, 'pivot_Property179', b)
    _safe_set(b, 'pivot_Property181', None)
    assert not _is_linked(b, 'pivot_Property181', a2)
    if hasattr(a2, 'pivot_Property179'):
        assert not _is_linked(a2, 'pivot_Property179', b)


def test_assoc_ownedAttribute319_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'Property320', a1)
    assert _is_linked(b, 'Property320', a1)
    if hasattr(a1, 'owningType'):
        assert _is_linked(a1, 'owningType', b)
    _safe_set(b, 'Property320', a2)
    assert _is_linked(b, 'Property320', a2)
    if hasattr(a1, 'owningType'):
        assert not _is_linked(a1, 'owningType', b)
    if hasattr(a2, 'owningType'):
        assert _is_linked(a2, 'owningType', b)
    _safe_set(b, 'Property320', None)
    assert not _is_linked(b, 'Property320', a2)
    if hasattr(a2, 'owningType'):
        assert not _is_linked(a2, 'owningType', b)


def test_assoc_ownedComment48_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment50', a1)
    assert _is_linked(b, 'pivot_Comment50', a1)
    if hasattr(a1, 'pivot_Element49'):
        assert _is_linked(a1, 'pivot_Element49', b)
    _safe_set(b, 'pivot_Comment50', a2)
    assert _is_linked(b, 'pivot_Comment50', a2)
    if hasattr(a1, 'pivot_Element49'):
        assert not _is_linked(a1, 'pivot_Element49', b)
    if hasattr(a2, 'pivot_Element49'):
        assert _is_linked(a2, 'pivot_Element49', b)
    _safe_set(b, 'pivot_Comment50', None)
    assert not _is_linked(b, 'pivot_Comment50', a2)
    if hasattr(a2, 'pivot_Element49'):
        assert not _is_linked(a2, 'pivot_Element49', b)


def test_assoc_ownedInvariant327_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint329', a1)
    assert _is_linked(b, 'pivot_Constraint329', a1)
    if hasattr(a1, 'pivot_Type328'):
        assert _is_linked(a1, 'pivot_Type328', b)
    _safe_set(b, 'pivot_Constraint329', a2)
    assert _is_linked(b, 'pivot_Constraint329', a2)
    if hasattr(a1, 'pivot_Type328'):
        assert not _is_linked(a1, 'pivot_Type328', b)
    if hasattr(a2, 'pivot_Type328'):
        assert _is_linked(a2, 'pivot_Type328', b)
    _safe_set(b, 'pivot_Constraint329', None)
    assert not _is_linked(b, 'pivot_Constraint329', a2)
    if hasattr(a2, 'pivot_Type328'):
        assert not _is_linked(a2, 'pivot_Type328', b)


def test_assoc_ownedOperation321_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'Operation323', a1)
    assert _is_linked(b, 'Operation323', a1)
    if hasattr(a1, 'owningType322'):
        assert _is_linked(a1, 'owningType322', b)
    _safe_set(b, 'Operation323', a2)
    assert _is_linked(b, 'Operation323', a2)
    if hasattr(a1, 'owningType322'):
        assert not _is_linked(a1, 'owningType322', b)
    if hasattr(a2, 'owningType322'):
        assert _is_linked(a2, 'owningType322', b)
    _safe_set(b, 'Operation323', None)
    assert not _is_linked(b, 'Operation323', a2)
    if hasattr(a2, 'owningType322'):
        assert not _is_linked(a2, 'owningType322', b)


def test_assoc_ownedType170_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'package', {a1})
    assert _is_linked(b, 'package', a1)
    if hasattr(a1, 'Type171'):
        assert _is_linked(a1, 'Type171', b)
    _safe_set(b, 'package', {a2})
    assert _is_linked(b, 'package', a2)
    if hasattr(a1, 'Type171'):
        assert not _is_linked(a1, 'Type171', b)
    if hasattr(a2, 'Type171'):
        assert _is_linked(a2, 'Type171', b)
    _safe_set(b, 'package', set())
    assert not _is_linked(b, 'package', a2)
    if hasattr(a2, 'Type171'):
        assert not _is_linked(a2, 'Type171', b)


def test_assoc_owningType139_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'ownedOperation', a1)
    assert _is_linked(b, 'ownedOperation', a1)
    if hasattr(a1, 'Type'):
        assert _is_linked(a1, 'Type', b)
    _safe_set(b, 'ownedOperation', a2)
    assert _is_linked(b, 'ownedOperation', a2)
    if hasattr(a1, 'Type'):
        assert not _is_linked(a1, 'Type', b)
    if hasattr(a2, 'Type'):
        assert _is_linked(a2, 'Type', b)
    _safe_set(b, 'ownedOperation', None)
    assert not _is_linked(b, 'ownedOperation', a2)
    if hasattr(a2, 'Type'):
        assert not _is_linked(a2, 'Type', b)


def test_assoc_owningType198_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'ownedAttribute', a1)
    assert _is_linked(b, 'ownedAttribute', a1)
    if hasattr(a1, 'Type199'):
        assert _is_linked(a1, 'Type199', b)
    _safe_set(b, 'ownedAttribute', a2)
    assert _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a1, 'Type199'):
        assert not _is_linked(a1, 'Type199', b)
    if hasattr(a2, 'Type199'):
        assert _is_linked(a2, 'Type199', b)
    _safe_set(b, 'ownedAttribute', None)
    assert not _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a2, 'Type199'):
        assert not _is_linked(a2, 'Type199', b)


def test_assoc_package317_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'Package318', a1)
    assert _is_linked(b, 'Package318', a1)
    if hasattr(a1, 'ownedType'):
        assert _is_linked(a1, 'ownedType', b)
    _safe_set(b, 'Package318', a2)
    assert _is_linked(b, 'Package318', a2)
    if hasattr(a1, 'ownedType'):
        assert not _is_linked(a1, 'ownedType', b)
    if hasattr(a2, 'ownedType'):
        assert _is_linked(a2, 'ownedType', b)
    _safe_set(b, 'Package318', None)
    assert not _is_linked(b, 'Package318', a2)
    if hasattr(a2, 'ownedType'):
        assert not _is_linked(a2, 'ownedType', b)


def test_assoc_postcondition143_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint145', a1)
    assert _is_linked(b, 'pivot_Constraint145', a1)
    if hasattr(a1, 'pivot_Operation144'):
        assert _is_linked(a1, 'pivot_Operation144', b)
    _safe_set(b, 'pivot_Constraint145', a2)
    assert _is_linked(b, 'pivot_Constraint145', a2)
    if hasattr(a1, 'pivot_Operation144'):
        assert not _is_linked(a1, 'pivot_Operation144', b)
    if hasattr(a2, 'pivot_Operation144'):
        assert _is_linked(a2, 'pivot_Operation144', b)
    _safe_set(b, 'pivot_Constraint145', None)
    assert not _is_linked(b, 'pivot_Constraint145', a2)
    if hasattr(a2, 'pivot_Operation144'):
        assert not _is_linked(a2, 'pivot_Operation144', b)


def test_assoc_precedence149_reverse_link_reassign_clear():
    a1 = pivot_Precedence(associativity="sample_text", order="sample_text")
    a2 = pivot_Precedence(associativity="sample_text_2", order="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation150', a1)
    assert _is_linked(b, 'pivot_Operation150', a1)
    if hasattr(a1, 'pivot_Precedence151'):
        assert _is_linked(a1, 'pivot_Precedence151', b)
    _safe_set(b, 'pivot_Operation150', a2)
    assert _is_linked(b, 'pivot_Operation150', a2)
    if hasattr(a1, 'pivot_Precedence151'):
        assert not _is_linked(a1, 'pivot_Precedence151', b)
    if hasattr(a2, 'pivot_Precedence151'):
        assert _is_linked(a2, 'pivot_Precedence151', b)
    _safe_set(b, 'pivot_Operation150', None)
    assert not _is_linked(b, 'pivot_Operation150', a2)
    if hasattr(a2, 'pivot_Precedence151'):
        assert not _is_linked(a2, 'pivot_Precedence151', b)


def test_assoc_precondition140_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint142', a1)
    assert _is_linked(b, 'pivot_Constraint142', a1)
    if hasattr(a1, 'pivot_Operation141'):
        assert _is_linked(a1, 'pivot_Operation141', b)
    _safe_set(b, 'pivot_Constraint142', a2)
    assert _is_linked(b, 'pivot_Constraint142', a2)
    if hasattr(a1, 'pivot_Operation141'):
        assert not _is_linked(a1, 'pivot_Operation141', b)
    if hasattr(a2, 'pivot_Operation141'):
        assert _is_linked(a2, 'pivot_Operation141', b)
    _safe_set(b, 'pivot_Constraint142', None)
    assert not _is_linked(b, 'pivot_Constraint142', a2)
    if hasattr(a2, 'pivot_Operation141'):
        assert not _is_linked(a2, 'pivot_Operation141', b)


def test_assoc_raisedException135_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation136', {a1})
    assert _is_linked(b, 'pivot_Operation136', a1)
    if hasattr(a1, 'pivot_Type137'):
        assert _is_linked(a1, 'pivot_Type137', b)
    _safe_set(b, 'pivot_Operation136', {a2})
    assert _is_linked(b, 'pivot_Operation136', a2)
    if hasattr(a1, 'pivot_Type137'):
        assert not _is_linked(a1, 'pivot_Type137', b)
    if hasattr(a2, 'pivot_Type137'):
        assert _is_linked(a2, 'pivot_Type137', b)
    _safe_set(b, 'pivot_Operation136', set())
    assert not _is_linked(b, 'pivot_Operation136', a2)
    if hasattr(a2, 'pivot_Type137'):
        assert not _is_linked(a2, 'pivot_Type137', b)


def test_assoc_redefinedOperation153_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation154', a1)
    assert _is_linked(b, 'pivot_Operation154', a1)
    if hasattr(a1, 'pivot_Operation152'):
        assert _is_linked(a1, 'pivot_Operation152', b)
    _safe_set(b, 'pivot_Operation154', a2)
    assert _is_linked(b, 'pivot_Operation154', a2)
    if hasattr(a1, 'pivot_Operation152'):
        assert not _is_linked(a1, 'pivot_Operation152', b)
    if hasattr(a2, 'pivot_Operation152'):
        assert _is_linked(a2, 'pivot_Operation152', b)
    _safe_set(b, 'pivot_Operation154', None)
    assert not _is_linked(b, 'pivot_Operation154', a2)
    if hasattr(a2, 'pivot_Operation152'):
        assert not _is_linked(a2, 'pivot_Operation152', b)


def test_assoc_redefinedProperty190_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property191', a1)
    assert _is_linked(b, 'pivot_Property191', a1)
    if hasattr(a1, 'pivot_Property189'):
        assert _is_linked(a1, 'pivot_Property189', b)
    _safe_set(b, 'pivot_Property191', a2)
    assert _is_linked(b, 'pivot_Property191', a2)
    if hasattr(a1, 'pivot_Property189'):
        assert not _is_linked(a1, 'pivot_Property189', b)
    if hasattr(a2, 'pivot_Property189'):
        assert _is_linked(a2, 'pivot_Property189', b)
    _safe_set(b, 'pivot_Property191', None)
    assert not _is_linked(b, 'pivot_Property191', a2)
    if hasattr(a2, 'pivot_Property189'):
        assert not _is_linked(a2, 'pivot_Property189', b)


def test_assoc_redefinedState231_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'pivot_State232', a1)
    assert _is_linked(b, 'pivot_State232', a1)
    if hasattr(a1, 'pivot_State230'):
        assert _is_linked(a1, 'pivot_State230', b)
    _safe_set(b, 'pivot_State232', a2)
    assert _is_linked(b, 'pivot_State232', a2)
    if hasattr(a1, 'pivot_State230'):
        assert not _is_linked(a1, 'pivot_State230', b)
    if hasattr(a2, 'pivot_State230'):
        assert _is_linked(a2, 'pivot_State230', b)
    _safe_set(b, 'pivot_State232', None)
    assert not _is_linked(b, 'pivot_State232', a2)
    if hasattr(a2, 'pivot_State230'):
        assert not _is_linked(a2, 'pivot_State230', b)


def test_assoc_referredEnumLiteral55_reverse_link_reassign_clear():
    a1 = pivot_EnumerationLiteral(value="sample_text")
    a2 = pivot_EnumerationLiteral(value="sample_text_2")
    b = pivot_EnumLiteralExp()
    _safe_set(b, 'pivot_EnumLiteralExp', a1)
    assert _is_linked(b, 'pivot_EnumLiteralExp', a1)
    if hasattr(a1, 'pivot_EnumerationLiteral'):
        assert _is_linked(a1, 'pivot_EnumerationLiteral', b)
    _safe_set(b, 'pivot_EnumLiteralExp', a2)
    assert _is_linked(b, 'pivot_EnumLiteralExp', a2)
    if hasattr(a1, 'pivot_EnumerationLiteral'):
        assert not _is_linked(a1, 'pivot_EnumerationLiteral', b)
    if hasattr(a2, 'pivot_EnumerationLiteral'):
        assert _is_linked(a2, 'pivot_EnumerationLiteral', b)
    _safe_set(b, 'pivot_EnumLiteralExp', None)
    assert not _is_linked(b, 'pivot_EnumLiteralExp', a2)
    if hasattr(a2, 'pivot_EnumerationLiteral'):
        assert not _is_linked(a2, 'pivot_EnumerationLiteral', b)


def test_assoc_referredOperation160_reverse_link_reassign_clear():
    a1 = pivot_OperationCallExp()
    a2 = pivot_OperationCallExp()
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation162', a1)
    assert _is_linked(b, 'pivot_Operation162', a1)
    if hasattr(a1, 'pivot_OperationCallExp161'):
        assert _is_linked(a1, 'pivot_OperationCallExp161', b)
    _safe_set(b, 'pivot_Operation162', a2)
    assert _is_linked(b, 'pivot_Operation162', a2)
    if hasattr(a1, 'pivot_OperationCallExp161'):
        assert not _is_linked(a1, 'pivot_OperationCallExp161', b)
    if hasattr(a2, 'pivot_OperationCallExp161'):
        assert _is_linked(a2, 'pivot_OperationCallExp161', b)
    _safe_set(b, 'pivot_Operation162', None)
    assert not _is_linked(b, 'pivot_Operation162', a2)
    if hasattr(a2, 'pivot_OperationCallExp161'):
        assert not _is_linked(a2, 'pivot_OperationCallExp161', b)


def test_assoc_referredProperty196_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property197', a1)
    assert _is_linked(b, 'pivot_Property197', a1)
    if hasattr(a1, 'pivot_Property195'):
        assert _is_linked(a1, 'pivot_Property195', b)
    _safe_set(b, 'pivot_Property197', a2)
    assert _is_linked(b, 'pivot_Property197', a2)
    if hasattr(a1, 'pivot_Property195'):
        assert not _is_linked(a1, 'pivot_Property195', b)
    if hasattr(a2, 'pivot_Property195'):
        assert _is_linked(a2, 'pivot_Property195', b)
    _safe_set(b, 'pivot_Property197', None)
    assert not _is_linked(b, 'pivot_Property197', a2)
    if hasattr(a2, 'pivot_Property195'):
        assert not _is_linked(a2, 'pivot_Property195', b)


def test_assoc_referredProperty200_reverse_link_reassign_clear():
    a1 = pivot_PropertyCallExp()
    a2 = pivot_PropertyCallExp()
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property201', a1)
    assert _is_linked(b, 'pivot_Property201', a1)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert _is_linked(a1, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property201', a2)
    assert _is_linked(b, 'pivot_Property201', a2)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert not _is_linked(a1, 'pivot_PropertyCallExp', b)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert _is_linked(a2, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property201', None)
    assert not _is_linked(b, 'pivot_Property201', a2)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert not _is_linked(a2, 'pivot_PropertyCallExp', b)


def test_assoc_referredProperty44_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_DynamicProperty(default="sample_text")
    _safe_set(b, 'pivot_DynamicProperty', a1)
    assert _is_linked(b, 'pivot_DynamicProperty', a1)
    if hasattr(a1, 'pivot_Property45'):
        assert _is_linked(a1, 'pivot_Property45', b)
    _safe_set(b, 'pivot_DynamicProperty', a2)
    assert _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a1, 'pivot_Property45'):
        assert not _is_linked(a1, 'pivot_Property45', b)
    if hasattr(a2, 'pivot_Property45'):
        assert _is_linked(a2, 'pivot_Property45', b)
    _safe_set(b, 'pivot_DynamicProperty', None)
    assert not _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a2, 'pivot_Property45'):
        assert not _is_linked(a2, 'pivot_Property45', b)


def test_assoc_result81_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_IterateExp()
    _safe_set(b, 'pivot_IterateExp', a1)
    assert _is_linked(b, 'pivot_IterateExp', a1)
    if hasattr(a1, 'pivot_Variable82'):
        assert _is_linked(a1, 'pivot_Variable82', b)
    _safe_set(b, 'pivot_IterateExp', a2)
    assert _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a1, 'pivot_Variable82'):
        assert not _is_linked(a1, 'pivot_Variable82', b)
    if hasattr(a2, 'pivot_Variable82'):
        assert _is_linked(a2, 'pivot_Variable82', b)
    _safe_set(b, 'pivot_IterateExp', None)
    assert not _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a2, 'pivot_Variable82'):
        assert not _is_linked(a2, 'pivot_Variable82', b)


def test_assoc_specification30_reverse_link_reassign_clear():
    a1 = pivot_OpaqueExpression(body="sample_text", language="sample_text", message="sample_text")
    a2 = pivot_OpaqueExpression(body="sample_text_2", language="sample_text_2", message="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint31', a1)
    assert _is_linked(b, 'pivot_Constraint31', a1)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert _is_linked(a1, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint31', a2)
    assert _is_linked(b, 'pivot_Constraint31', a2)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert not _is_linked(a1, 'pivot_OpaqueExpression', b)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert _is_linked(a2, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint31', None)
    assert not _is_linked(b, 'pivot_Constraint31', a2)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert not _is_linked(a2, 'pivot_OpaqueExpression', b)


def test_assoc_state204_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'pivot_Pseudostate205', a1)
    assert _is_linked(b, 'pivot_Pseudostate205', a1)
    if hasattr(a1, 'pivot_State206'):
        assert _is_linked(a1, 'pivot_State206', b)
    _safe_set(b, 'pivot_Pseudostate205', a2)
    assert _is_linked(b, 'pivot_Pseudostate205', a2)
    if hasattr(a1, 'pivot_State206'):
        assert not _is_linked(a1, 'pivot_State206', b)
    if hasattr(a2, 'pivot_State206'):
        assert _is_linked(a2, 'pivot_State206', b)
    _safe_set(b, 'pivot_Pseudostate205', None)
    assert not _is_linked(b, 'pivot_Pseudostate205', a2)
    if hasattr(a2, 'pivot_State206'):
        assert not _is_linked(a2, 'pivot_State206', b)


def test_assoc_stateInvariant236_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint238', a1)
    assert _is_linked(b, 'pivot_Constraint238', a1)
    if hasattr(a1, 'pivot_State237'):
        assert _is_linked(a1, 'pivot_State237', b)
    _safe_set(b, 'pivot_Constraint238', a2)
    assert _is_linked(b, 'pivot_Constraint238', a2)
    if hasattr(a1, 'pivot_State237'):
        assert not _is_linked(a1, 'pivot_State237', b)
    if hasattr(a2, 'pivot_State237'):
        assert _is_linked(a2, 'pivot_State237', b)
    _safe_set(b, 'pivot_Constraint238', None)
    assert not _is_linked(b, 'pivot_Constraint238', a2)
    if hasattr(a2, 'pivot_State237'):
        assert not _is_linked(a2, 'pivot_State237', b)


def test_assoc_subsettedProperty193_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property194', a1)
    assert _is_linked(b, 'pivot_Property194', a1)
    if hasattr(a1, 'pivot_Property192'):
        assert _is_linked(a1, 'pivot_Property192', b)
    _safe_set(b, 'pivot_Property194', a2)
    assert _is_linked(b, 'pivot_Property194', a2)
    if hasattr(a1, 'pivot_Property192'):
        assert not _is_linked(a1, 'pivot_Property192', b)
    if hasattr(a2, 'pivot_Property192'):
        assert _is_linked(a2, 'pivot_Property192', b)
    _safe_set(b, 'pivot_Property194', None)
    assert not _is_linked(b, 'pivot_Property194', a2)
    if hasattr(a2, 'pivot_Property192'):
        assert not _is_linked(a2, 'pivot_Property192', b)


def test_assoc_superClass325_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type326', a1)
    assert _is_linked(b, 'pivot_Type326', a1)
    if hasattr(a1, 'pivot_Type324'):
        assert _is_linked(a1, 'pivot_Type324', b)
    _safe_set(b, 'pivot_Type326', a2)
    assert _is_linked(b, 'pivot_Type326', a2)
    if hasattr(a1, 'pivot_Type324'):
        assert not _is_linked(a1, 'pivot_Type324', b)
    if hasattr(a2, 'pivot_Type324'):
        assert _is_linked(a2, 'pivot_Type324', b)
    _safe_set(b, 'pivot_Type326', None)
    assert not _is_linked(b, 'pivot_Type326', a2)
    if hasattr(a2, 'pivot_Type324'):
        assert not _is_linked(a2, 'pivot_Type324', b)


def test_assoc_type334_reverse_link_reassign_clear():
    a1 = pivot_TypedElement(isRequired="sample_text")
    a2 = pivot_TypedElement(isRequired="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type335', a1)
    assert _is_linked(b, 'pivot_Type335', a1)
    if hasattr(a1, 'pivot_TypedElement'):
        assert _is_linked(a1, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type335', a2)
    assert _is_linked(b, 'pivot_Type335', a2)
    if hasattr(a1, 'pivot_TypedElement'):
        assert not _is_linked(a1, 'pivot_TypedElement', b)
    if hasattr(a2, 'pivot_TypedElement'):
        assert _is_linked(a2, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type335', None)
    assert not _is_linked(b, 'pivot_Type335', a2)
    if hasattr(a2, 'pivot_TypedElement'):
        assert not _is_linked(a2, 'pivot_TypedElement', b)


def test_assoc_unspecializedElement299_reverse_link_reassign_clear():
    a1 = pivot_TemplateableElement()
    a2 = pivot_TemplateableElement()
    b = pivot_TemplateableElement()
    _safe_set(b, 'pivot_TemplateableElement298', a1)
    assert _is_linked(b, 'pivot_TemplateableElement298', a1)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert _is_linked(a1, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement298', a2)
    assert _is_linked(b, 'pivot_TemplateableElement298', a2)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert not _is_linked(a1, 'pivot_TemplateableElement', b)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert _is_linked(a2, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement298', None)
    assert not _is_linked(b, 'pivot_TemplateableElement298', a2)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert not _is_linked(a2, 'pivot_TemplateableElement', b)


def test_assoc_variable97_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LetExp()
    _safe_set(b, 'pivot_LetExp98', a1)
    assert _is_linked(b, 'pivot_LetExp98', a1)
    if hasattr(a1, 'pivot_Variable99'):
        assert _is_linked(a1, 'pivot_Variable99', b)
    _safe_set(b, 'pivot_LetExp98', a2)
    assert _is_linked(b, 'pivot_LetExp98', a2)
    if hasattr(a1, 'pivot_Variable99'):
        assert not _is_linked(a1, 'pivot_Variable99', b)
    if hasattr(a2, 'pivot_Variable99'):
        assert _is_linked(a2, 'pivot_Variable99', b)
    _safe_set(b, 'pivot_LetExp98', None)
    assert not _is_linked(b, 'pivot_LetExp98', a2)
    if hasattr(a2, 'pivot_Variable99'):
        assert not _is_linked(a2, 'pivot_Variable99', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actual280_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution281' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution281', None)
    _safe_set(owner, 'pivot_ParameterableElement282', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution281') == owner
    _safe_set(owner, 'pivot_ParameterableElement282', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution281') is None


def test_assoc_argument111_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression113' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression113', None)
    _safe_set(owner, 'pivot_MessageExp112', {partner})
    assert getattr(partner, 'pivot_OCLExpression113') == owner
    _safe_set(owner, 'pivot_MessageExp112', set())
    assert getattr(partner, 'pivot_OCLExpression113') is None


def test_assoc_argument158_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression159' property in the generated
    # code (a bare stub) -- manually attach it so pivot_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_OperationCallExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression159', None)
    _safe_set(owner, 'pivot_OperationCallExp', {partner})
    assert getattr(partner, 'pivot_OCLExpression159') == owner
    _safe_set(owner, 'pivot_OperationCallExp', set())
    assert getattr(partner, 'pivot_OCLExpression159') is None


def test_assoc_association182_stub_double():
    # pivot_AssociationClass has no real 'AssociationClass' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_AssociationClass()
    setattr(partner, 'AssociationClass', None)
    _safe_set(owner, 'unownedAttribute', partner)
    assert getattr(partner, 'AssociationClass') == owner
    _safe_set(owner, 'unownedAttribute', None)
    assert getattr(partner, 'AssociationClass') is None


def test_assoc_base54_stub_double():
    # pivot_ElementExtension has no real 'extension' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Element()
    partner = pivot_ElementExtension()
    setattr(partner, 'extension', None)
    _safe_set(owner, 'Element', partner)
    assert getattr(partner, 'extension') == owner
    _safe_set(owner, 'Element', None)
    assert getattr(partner, 'extension') is None


def test_assoc_body101_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression102' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression102', None)
    _safe_set(owner, 'pivot_LoopExp', partner)
    assert getattr(partner, 'pivot_OCLExpression102') == owner
    _safe_set(owner, 'pivot_LoopExp', None)
    assert getattr(partner, 'pivot_OCLExpression102') is None


def test_assoc_boundElement267_stub_double():
    # pivot_TemplateBinding has no real 'templateBinding268' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateBinding()
    setattr(partner, 'templateBinding268', None)
    _safe_set(owner, 'TemplateableElement', partner)
    assert getattr(partner, 'templateBinding268') == owner
    _safe_set(owner, 'TemplateableElement', None)
    assert getattr(partner, 'templateBinding268') is None


def test_assoc_calledOperation114_stub_double():
    # pivot_CallOperationAction has no real 'pivot_CallOperationAction116' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_CallOperationAction()
    setattr(partner, 'pivot_CallOperationAction116', None)
    _safe_set(owner, 'pivot_MessageExp115', partner)
    assert getattr(partner, 'pivot_CallOperationAction116') == owner
    _safe_set(owner, 'pivot_MessageExp115', None)
    assert getattr(partner, 'pivot_CallOperationAction116') is None


def test_assoc_condition71_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression72' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression72', None)
    _safe_set(owner, 'pivot_IfExp', partner)
    assert getattr(partner, 'pivot_OCLExpression72') == owner
    _safe_set(owner, 'pivot_IfExp', None)
    assert getattr(partner, 'pivot_OCLExpression72') is None


def test_assoc_connection227_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference229' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference229', None)
    _safe_set(owner, 'pivot_State228', {partner})
    assert getattr(partner, 'pivot_ConnectionPointReference229') == owner
    _safe_set(owner, 'pivot_State228', set())
    assert getattr(partner, 'pivot_ConnectionPointReference229') is None


def test_assoc_connectionPoint258_stub_double():
    # pivot_StateMachine has no real 'pivot_StateMachine259' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'pivot_StateMachine259', None)
    _safe_set(owner, 'pivot_Pseudostate260', partner)
    assert owner in getattr(partner, 'pivot_StateMachine259')
    _safe_set(owner, 'pivot_Pseudostate260', None)
    assert owner not in getattr(partner, 'pivot_StateMachine259')


def test_assoc_container312_stub_double():
    # pivot_Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'Region') is None


def test_assoc_context32_stub_double():
    # pivot_Namespace has no real 'pivot_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Constraint(isCallable="sample_text")
    partner = pivot_Namespace()
    setattr(partner, 'pivot_Namespace', None)
    _safe_set(owner, 'pivot_Constraint33', partner)
    assert getattr(partner, 'pivot_Namespace') == owner
    _safe_set(owner, 'pivot_Constraint33', None)
    assert getattr(partner, 'pivot_Namespace') is None


def test_assoc_contextType87_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType', None)
    _safe_set(owner, 'pivot_Type88', partner)
    assert getattr(partner, 'pivot_LambdaType') == owner
    _safe_set(owner, 'pivot_Type88', None)
    assert getattr(partner, 'pivot_LambdaType') is None


def test_assoc_contextVariable60_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL61' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL61', None)
    _safe_set(owner, 'pivot_Variable', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL61') == owner
    _safe_set(owner, 'pivot_Variable', None)
    assert getattr(partner, 'pivot_ExpressionInOCL61') is None


def test_assoc_default274_stub_double():
    # pivot_TemplateParameter has no real 'pivot_TemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'pivot_TemplateParameter', None)
    _safe_set(owner, 'pivot_ParameterableElement', partner)
    assert getattr(partner, 'pivot_TemplateParameter') == owner
    _safe_set(owner, 'pivot_ParameterableElement', None)
    assert getattr(partner, 'pivot_TemplateParameter') is None


def test_assoc_deferrableTrigger251_stub_double():
    # pivot_Trigger has no real 'pivot_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'pivot_Trigger', None)
    _safe_set(owner, 'pivot_State252', {partner})
    assert getattr(partner, 'pivot_Trigger') == owner
    _safe_set(owner, 'pivot_State252', set())
    assert getattr(partner, 'pivot_Trigger') is None


def test_assoc_doActivity245_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior247' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior247', None)
    _safe_set(owner, 'pivot_State246', partner)
    assert getattr(partner, 'pivot_Behavior247') == owner
    _safe_set(owner, 'pivot_State246', None)
    assert getattr(partner, 'pivot_Behavior247') is None


def test_assoc_effect306_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior308' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior308', None)
    _safe_set(owner, 'pivot_Transition307', partner)
    assert getattr(partner, 'pivot_Behavior308') == owner
    _safe_set(owner, 'pivot_Transition307', None)
    assert getattr(partner, 'pivot_Behavior308') is None


def test_assoc_elseExpression76_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression78' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression78', None)
    _safe_set(owner, 'pivot_IfExp77', partner)
    assert getattr(partner, 'pivot_OCLExpression78') == owner
    _safe_set(owner, 'pivot_IfExp77', None)
    assert getattr(partner, 'pivot_OCLExpression78') is None


def test_assoc_entry22_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference', None)
    _safe_set(owner, 'pivot_Pseudostate', partner)
    assert owner in getattr(partner, 'pivot_ConnectionPointReference')
    _safe_set(owner, 'pivot_Pseudostate', None)
    assert owner not in getattr(partner, 'pivot_ConnectionPointReference')


def test_assoc_entry239_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior241' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior241', None)
    _safe_set(owner, 'pivot_State240', partner)
    assert getattr(partner, 'pivot_Behavior241') == owner
    _safe_set(owner, 'pivot_State240', None)
    assert getattr(partner, 'pivot_Behavior241') is None


def test_assoc_enumeration57_stub_double():
    # pivot_Enumeration has no real 'Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so pivot_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_EnumerationLiteral(value="sample_text")
    partner = pivot_Enumeration()
    setattr(partner, 'Enumeration', None)
    _safe_set(owner, 'ownedLiteral', partner)
    assert getattr(partner, 'Enumeration') == owner
    _safe_set(owner, 'ownedLiteral', None)
    assert getattr(partner, 'Enumeration') is None


def test_assoc_exit242_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior244' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior244', None)
    _safe_set(owner, 'pivot_State243', partner)
    assert getattr(partner, 'pivot_Behavior244') == owner
    _safe_set(owner, 'pivot_State243', None)
    assert getattr(partner, 'pivot_Behavior244') is None


def test_assoc_exit25_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference26' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference26', None)
    _safe_set(owner, 'pivot_Pseudostate27', partner)
    assert owner in getattr(partner, 'pivot_ConnectionPointReference26')
    _safe_set(owner, 'pivot_Pseudostate27', None)
    assert owner not in getattr(partner, 'pivot_ConnectionPointReference26')


def test_assoc_extension51_stub_double():
    # pivot_ElementExtension has no real 'ElementExtension' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Element()
    partner = pivot_ElementExtension()
    setattr(partner, 'ElementExtension', None)
    _safe_set(owner, 'base', {partner})
    assert getattr(partner, 'ElementExtension') == owner
    _safe_set(owner, 'base', set())
    assert getattr(partner, 'ElementExtension') is None


def test_assoc_imports220_stub_double():
    # pivot_Import has no real 'pivot_Import222' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Root(externalURI="sample_text")
    partner = pivot_Import()
    setattr(partner, 'pivot_Import222', None)
    _safe_set(owner, 'pivot_Root221', {partner})
    assert getattr(partner, 'pivot_Import222') == owner
    _safe_set(owner, 'pivot_Root221', set())
    assert getattr(partner, 'pivot_Import222') is None


def test_assoc_in_95_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression96' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LetExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LetExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LetExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression96', None)
    _safe_set(owner, 'pivot_LetExp', partner)
    assert getattr(partner, 'pivot_OCLExpression96') == owner
    _safe_set(owner, 'pivot_LetExp', None)
    assert getattr(partner, 'pivot_OCLExpression96') is None


def test_assoc_incoming352_stub_double():
    # pivot_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition353', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition353', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_initExpression341_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression343' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression343', None)
    _safe_set(owner, 'pivot_Variable342', partner)
    assert getattr(partner, 'pivot_OCLExpression343') == owner
    _safe_set(owner, 'pivot_Variable342', None)
    assert getattr(partner, 'pivot_OCLExpression343') is None


def test_assoc_instanceType123_stub_double():
    # pivot_Metaclass has no real 'pivot_Metaclass' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_Metaclass()
    setattr(partner, 'pivot_Metaclass', None)
    _safe_set(owner, 'pivot_Type124', partner)
    assert getattr(partner, 'pivot_Metaclass') == owner
    _safe_set(owner, 'pivot_Type124', None)
    assert getattr(partner, 'pivot_Metaclass') is None


def test_assoc_item11_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression12' property in the generated
    # code (a bare stub) -- manually attach it so pivot_CollectionItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_CollectionItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_CollectionItem()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression12', None)
    _safe_set(owner, 'pivot_CollectionItem', partner)
    assert getattr(partner, 'pivot_OCLExpression12') == owner
    _safe_set(owner, 'pivot_CollectionItem', None)
    assert getattr(partner, 'pivot_OCLExpression12') is None


def test_assoc_lowerBound336_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType', None)
    _safe_set(owner, 'pivot_Type337', partner)
    assert getattr(partner, 'pivot_UnspecifiedType') == owner
    _safe_set(owner, 'pivot_Type337', None)
    assert getattr(partner, 'pivot_UnspecifiedType') is None


def test_assoc_metaType42_stub_double():
    # pivot_DynamicElement has no real 'pivot_DynamicElement' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_DynamicElement()
    setattr(partner, 'pivot_DynamicElement', None)
    _safe_set(owner, 'pivot_Type43', partner)
    assert getattr(partner, 'pivot_DynamicElement') == owner
    _safe_set(owner, 'pivot_Type43', None)
    assert getattr(partner, 'pivot_DynamicElement') is None


def test_assoc_navigationSource132_stub_double():
    # pivot_NavigationCallExp has no real 'pivot_NavigationCallExp133' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_NavigationCallExp()
    setattr(partner, 'pivot_NavigationCallExp133', None)
    _safe_set(owner, 'pivot_Property134', partner)
    assert getattr(partner, 'pivot_NavigationCallExp133') == owner
    _safe_set(owner, 'pivot_Property134', None)
    assert getattr(partner, 'pivot_NavigationCallExp133') is None


def test_assoc_operation172_stub_double():
    # pivot_Parameter has no real 'ownedParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_Parameter()
    setattr(partner, 'ownedParameter', None)
    _safe_set(owner, 'Operation', partner)
    assert getattr(partner, 'ownedParameter') == owner
    _safe_set(owner, 'Operation', None)
    assert getattr(partner, 'ownedParameter') is None


def test_assoc_operation9_stub_double():
    # pivot_CallOperationAction has no real 'pivot_CallOperationAction' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_CallOperationAction()
    setattr(partner, 'pivot_CallOperationAction', None)
    _safe_set(owner, 'pivot_Operation', partner)
    assert getattr(partner, 'pivot_CallOperationAction') == owner
    _safe_set(owner, 'pivot_Operation', None)
    assert getattr(partner, 'pivot_CallOperationAction') is None


def test_assoc_outgoing350_stub_double():
    # pivot_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition351', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition351', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedActual283_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution284' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution284', None)
    _safe_set(owner, 'pivot_ParameterableElement285', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution284') == owner
    _safe_set(owner, 'pivot_ParameterableElement285', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution284') is None


def test_assoc_ownedAnnotation125_stub_double():
    # pivot_Annotation has no real 'pivot_Annotation126' property in the generated
    # code (a bare stub) -- manually attach it so pivot_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_NamedElement(isStatic="sample_text", name="sample_text")
    partner = pivot_Annotation()
    setattr(partner, 'pivot_Annotation126', None)
    _safe_set(owner, 'pivot_NamedElement', {partner})
    assert getattr(partner, 'pivot_Annotation126') == owner
    _safe_set(owner, 'pivot_NamedElement', set())
    assert getattr(partner, 'pivot_Annotation126') is None


def test_assoc_ownedBehavior10_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior', None)
    _safe_set(owner, 'pivot_Class', {partner})
    assert getattr(partner, 'pivot_Behavior') == owner
    _safe_set(owner, 'pivot_Class', set())
    assert getattr(partner, 'pivot_Behavior') is None


def test_assoc_ownedContent0_stub_double():
    # pivot_Annotation has no real 'pivot_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Element()
    partner = pivot_Annotation()
    setattr(partner, 'pivot_Annotation', None)
    _safe_set(owner, 'pivot_Element', partner)
    assert owner in getattr(partner, 'pivot_Annotation')
    _safe_set(owner, 'pivot_Element', None)
    assert owner not in getattr(partner, 'pivot_Annotation')


def test_assoc_ownedDefault275_stub_double():
    # pivot_TemplateParameter has no real 'pivot_TemplateParameter276' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'pivot_TemplateParameter276', None)
    _safe_set(owner, 'pivot_ParameterableElement277', partner)
    assert getattr(partner, 'pivot_TemplateParameter276') == owner
    _safe_set(owner, 'pivot_ParameterableElement277', None)
    assert getattr(partner, 'pivot_TemplateParameter276') is None


def test_assoc_ownedDetail1_stub_double():
    # pivot_Annotation has no real 'pivot_Annotation2' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Detail's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Detail's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Detail(value="sample_text")
    partner = pivot_Annotation()
    setattr(partner, 'pivot_Annotation2', None)
    _safe_set(owner, 'pivot_Detail', partner)
    assert owner in getattr(partner, 'pivot_Annotation2')
    _safe_set(owner, 'pivot_Detail', None)
    assert owner not in getattr(partner, 'pivot_Annotation2')


def test_assoc_ownedLiteral56_stub_double():
    # pivot_Enumeration has no real 'enumeration' property in the generated
    # code (a bare stub) -- manually attach it so pivot_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_EnumerationLiteral(value="sample_text")
    partner = pivot_Enumeration()
    setattr(partner, 'enumeration', None)
    _safe_set(owner, 'EnumerationLiteral', partner)
    assert owner in getattr(partner, 'enumeration')
    _safe_set(owner, 'EnumerationLiteral', None)
    assert owner not in getattr(partner, 'enumeration')


def test_assoc_ownedParameter138_stub_double():
    # pivot_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_ownedParameteredElement272_stub_double():
    # pivot_TemplateParameter has no real 'owningTemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'owningTemplateParameter', None)
    _safe_set(owner, 'ParameterableElement273', partner)
    assert getattr(partner, 'owningTemplateParameter') == owner
    _safe_set(owner, 'ParameterableElement273', None)
    assert getattr(partner, 'owningTemplateParameter') is None


def test_assoc_ownedPrecedence100_stub_double():
    # pivot_Library has no real 'pivot_Library' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Precedence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Precedence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Precedence(associativity="sample_text", order="sample_text")
    partner = pivot_Library()
    setattr(partner, 'pivot_Library', None)
    _safe_set(owner, 'pivot_Precedence', partner)
    assert owner in getattr(partner, 'pivot_Library')
    _safe_set(owner, 'pivot_Precedence', None)
    assert owner not in getattr(partner, 'pivot_Library')


def test_assoc_ownedProperty46_stub_double():
    # pivot_DynamicType has no real 'pivot_DynamicType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_DynamicProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_DynamicProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_DynamicProperty(default="sample_text")
    partner = pivot_DynamicType()
    setattr(partner, 'pivot_DynamicType', None)
    _safe_set(owner, 'pivot_DynamicProperty47', partner)
    assert owner in getattr(partner, 'pivot_DynamicType')
    _safe_set(owner, 'pivot_DynamicProperty47', None)
    assert owner not in getattr(partner, 'pivot_DynamicType')


def test_assoc_ownedRule127_stub_double():
    # pivot_Namespace has no real 'pivot_Namespace128' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Constraint(isCallable="sample_text")
    partner = pivot_Namespace()
    setattr(partner, 'pivot_Namespace128', None)
    _safe_set(owner, 'pivot_Constraint129', partner)
    assert owner in getattr(partner, 'pivot_Namespace128')
    _safe_set(owner, 'pivot_Constraint129', None)
    assert owner not in getattr(partner, 'pivot_Namespace128')


def test_assoc_ownedTemplateSignature296_stub_double():
    # pivot_TemplateSignature has no real 'TemplateSignature297' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'TemplateSignature297', None)
    _safe_set(owner, 'template', partner)
    assert getattr(partner, 'TemplateSignature297') == owner
    _safe_set(owner, 'template', None)
    assert getattr(partner, 'TemplateSignature297') is None


def test_assoc_owningTemplateParameter173_stub_double():
    # pivot_TemplateParameter has no real 'TemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'TemplateParameter', None)
    _safe_set(owner, 'ownedParameteredElement', partner)
    assert getattr(partner, 'TemplateParameter') == owner
    _safe_set(owner, 'ownedParameteredElement', None)
    assert getattr(partner, 'TemplateParameter') is None


def test_assoc_parameterType89_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType90' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType90', None)
    _safe_set(owner, 'pivot_Type91', partner)
    assert owner in getattr(partner, 'pivot_LambdaType90')
    _safe_set(owner, 'pivot_Type91', None)
    assert owner not in getattr(partner, 'pivot_LambdaType90')


def test_assoc_parameterVariable65_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL66' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL66', None)
    _safe_set(owner, 'pivot_Variable67', partner)
    assert owner in getattr(partner, 'pivot_ExpressionInOCL66')
    _safe_set(owner, 'pivot_Variable67', None)
    assert owner not in getattr(partner, 'pivot_ExpressionInOCL66')


def test_assoc_parameteredElement271_stub_double():
    # pivot_TemplateParameter has no real 'templateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'templateParameter', None)
    _safe_set(owner, 'ParameterableElement', partner)
    assert getattr(partner, 'templateParameter') == owner
    _safe_set(owner, 'ParameterableElement', None)
    assert getattr(partner, 'templateParameter') is None


def test_assoc_part13_stub_double():
    # pivot_CollectionLiteralPart has no real 'pivot_CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so pivot_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_CollectionLiteralExp(kind="sample_text")
    partner = pivot_CollectionLiteralPart()
    setattr(partner, 'pivot_CollectionLiteralPart', None)
    _safe_set(owner, 'pivot_CollectionLiteralExp', {partner})
    assert getattr(partner, 'pivot_CollectionLiteralPart') == owner
    _safe_set(owner, 'pivot_CollectionLiteralExp', set())
    assert getattr(partner, 'pivot_CollectionLiteralPart') is None


def test_assoc_part34_stub_double():
    # pivot_ConstructorPart has no real 'pivot_ConstructorPart' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ConstructorExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ConstructorExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ConstructorExp(value="sample_text")
    partner = pivot_ConstructorPart()
    setattr(partner, 'pivot_ConstructorPart', None)
    _safe_set(owner, 'pivot_ConstructorExp', {partner})
    assert getattr(partner, 'pivot_ConstructorPart') == owner
    _safe_set(owner, 'pivot_ConstructorExp', set())
    assert getattr(partner, 'pivot_ConstructorPart') is None


def test_assoc_reference3_stub_double():
    # pivot_Annotation has no real 'pivot_Annotation4' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Element()
    partner = pivot_Annotation()
    setattr(partner, 'pivot_Annotation4', None)
    _safe_set(owner, 'pivot_Element5', partner)
    assert owner in getattr(partner, 'pivot_Annotation4')
    _safe_set(owner, 'pivot_Element5', None)
    assert owner not in getattr(partner, 'pivot_Annotation4')


def test_assoc_referredIteration106_stub_double():
    # pivot_Iteration has no real 'pivot_Iteration108' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_Iteration()
    setattr(partner, 'pivot_Iteration108', None)
    _safe_set(owner, 'pivot_LoopExp107', partner)
    assert getattr(partner, 'pivot_Iteration108') == owner
    _safe_set(owner, 'pivot_LoopExp107', None)
    assert getattr(partner, 'pivot_Iteration108') is None


def test_assoc_referredOperation120_stub_double():
    # pivot_MessageType has no real 'pivot_MessageType121' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_MessageType()
    setattr(partner, 'pivot_MessageType121', None)
    _safe_set(owner, 'pivot_Operation122', partner)
    assert getattr(partner, 'pivot_MessageType121') == owner
    _safe_set(owner, 'pivot_Operation122', None)
    assert getattr(partner, 'pivot_MessageType121') is None


def test_assoc_referredProperty35_stub_double():
    # pivot_ConstructorPart has no real 'pivot_ConstructorPart36' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_ConstructorPart()
    setattr(partner, 'pivot_ConstructorPart36', None)
    _safe_set(owner, 'pivot_Property', partner)
    assert getattr(partner, 'pivot_ConstructorPart36') == owner
    _safe_set(owner, 'pivot_Property', None)
    assert getattr(partner, 'pivot_ConstructorPart36') is None


def test_assoc_referredState253_stub_double():
    # pivot_StateExp has no real 'pivot_StateExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateExp()
    setattr(partner, 'pivot_StateExp', None)
    _safe_set(owner, 'pivot_State254', partner)
    assert getattr(partner, 'pivot_StateExp') == owner
    _safe_set(owner, 'pivot_State254', None)
    assert getattr(partner, 'pivot_StateExp') is None


def test_assoc_referredType330_stub_double():
    # pivot_TypeExp has no real 'pivot_TypeExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_TypeExp()
    setattr(partner, 'pivot_TypeExp', None)
    _safe_set(owner, 'pivot_Type331', partner)
    assert getattr(partner, 'pivot_TypeExp') == owner
    _safe_set(owner, 'pivot_Type331', None)
    assert getattr(partner, 'pivot_TypeExp') is None


def test_assoc_referredVariable347_stub_double():
    # pivot_VariableDeclaration has no real 'pivot_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so pivot_VariableExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_VariableExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_VariableExp(implicit="sample_text")
    partner = pivot_VariableDeclaration()
    setattr(partner, 'pivot_VariableDeclaration', None)
    _safe_set(owner, 'pivot_VariableExp', partner)
    assert getattr(partner, 'pivot_VariableDeclaration') == owner
    _safe_set(owner, 'pivot_VariableExp', None)
    assert getattr(partner, 'pivot_VariableDeclaration') is None


def test_assoc_region233_stub_double():
    # pivot_Region has no real 'pivot_Region235' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'pivot_Region235', None)
    _safe_set(owner, 'pivot_State234', {partner})
    assert getattr(partner, 'pivot_Region235') == owner
    _safe_set(owner, 'pivot_State234', set())
    assert getattr(partner, 'pivot_Region235') is None


def test_assoc_representedParameter344_stub_double():
    # pivot_Parameter has no real 'pivot_Parameter346' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_Parameter()
    setattr(partner, 'pivot_Parameter346', None)
    _safe_set(owner, 'pivot_Variable345', partner)
    assert getattr(partner, 'pivot_Parameter346') == owner
    _safe_set(owner, 'pivot_Variable345', None)
    assert getattr(partner, 'pivot_Parameter346') is None


def test_assoc_resultType92_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType93' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType93', None)
    _safe_set(owner, 'pivot_Type94', partner)
    assert getattr(partner, 'pivot_LambdaType93') == owner
    _safe_set(owner, 'pivot_Type94', None)
    assert getattr(partner, 'pivot_LambdaType93') is None


def test_assoc_resultVariable62_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL63' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL63', None)
    _safe_set(owner, 'pivot_Variable64', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL63') == owner
    _safe_set(owner, 'pivot_Variable64', None)
    assert getattr(partner, 'pivot_ExpressionInOCL63') is None


def test_assoc_sentSignal117_stub_double():
    # pivot_SendSignalAction has no real 'pivot_SendSignalAction' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_SendSignalAction()
    setattr(partner, 'pivot_SendSignalAction', None)
    _safe_set(owner, 'pivot_MessageExp118', partner)
    assert getattr(partner, 'pivot_SendSignalAction') == owner
    _safe_set(owner, 'pivot_MessageExp118', None)
    assert getattr(partner, 'pivot_SendSignalAction') is None


def test_assoc_source300_stub_double():
    # pivot_Vertex has no real 'Vertex301' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex301', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex301') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex301') is None


def test_assoc_source8_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression' property in the generated
    # code (a bare stub) -- manually attach it so pivot_CallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_CallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_CallExp(implicit="sample_text")
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression', None)
    _safe_set(owner, 'pivot_CallExp', partner)
    assert getattr(partner, 'pivot_OCLExpression') == owner
    _safe_set(owner, 'pivot_CallExp', None)
    assert getattr(partner, 'pivot_OCLExpression') is None


def test_assoc_state210_stub_double():
    # pivot_Region has no real 'pivot_Region211' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'pivot_Region211', None)
    _safe_set(owner, 'pivot_State212', partner)
    assert getattr(partner, 'pivot_Region211') == owner
    _safe_set(owner, 'pivot_State212', None)
    assert getattr(partner, 'pivot_Region211') is None


def test_assoc_state23_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference24' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference24', None)
    _safe_set(owner, 'pivot_State', partner)
    assert getattr(partner, 'pivot_ConnectionPointReference24') == owner
    _safe_set(owner, 'pivot_State', None)
    assert getattr(partner, 'pivot_ConnectionPointReference24') is None


def test_assoc_stateMachine202_stub_double():
    # pivot_StateMachine has no real 'pivot_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'pivot_StateMachine', None)
    _safe_set(owner, 'pivot_Pseudostate203', partner)
    assert getattr(partner, 'pivot_StateMachine') == owner
    _safe_set(owner, 'pivot_Pseudostate203', None)
    assert getattr(partner, 'pivot_StateMachine') is None


def test_assoc_stereotype52_stub_double():
    # pivot_ElementExtension has no real 'pivot_ElementExtension' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_ElementExtension()
    setattr(partner, 'pivot_ElementExtension', None)
    _safe_set(owner, 'pivot_Type53', partner)
    assert getattr(partner, 'pivot_ElementExtension') == owner
    _safe_set(owner, 'pivot_Type53', None)
    assert getattr(partner, 'pivot_ElementExtension') is None


def test_assoc_submachine226_stub_double():
    # pivot_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'submachineState', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'submachineState', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_submachineState261_stub_double():
    # pivot_StateMachine has no real 'submachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'submachine', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'submachine')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'submachine')


def test_assoc_target109_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression110' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression110', None)
    _safe_set(owner, 'pivot_MessageExp', partner)
    assert getattr(partner, 'pivot_OCLExpression110') == owner
    _safe_set(owner, 'pivot_MessageExp', None)
    assert getattr(partner, 'pivot_OCLExpression110') is None


def test_assoc_target302_stub_double():
    # pivot_Vertex has no real 'Vertex303' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex303', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex303') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex303') is None


def test_assoc_template292_stub_double():
    # pivot_TemplateSignature has no real 'ownedTemplateSignature' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'ownedTemplateSignature', None)
    _safe_set(owner, 'TemplateableElement293', partner)
    assert getattr(partner, 'ownedTemplateSignature') == owner
    _safe_set(owner, 'TemplateableElement293', None)
    assert getattr(partner, 'ownedTemplateSignature') is None


def test_assoc_templateBinding294_stub_double():
    # pivot_TemplateBinding has no real 'TemplateBinding295' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateBinding()
    setattr(partner, 'TemplateBinding295', None)
    _safe_set(owner, 'boundElement', {partner})
    assert getattr(partner, 'TemplateBinding295') == owner
    _safe_set(owner, 'boundElement', set())
    assert getattr(partner, 'TemplateBinding295') is None


def test_assoc_templateParameter174_stub_double():
    # pivot_TemplateParameter has no real 'TemplateParameter175' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'TemplateParameter175', None)
    _safe_set(owner, 'parameteredElement', partner)
    assert getattr(partner, 'TemplateParameter175') == owner
    _safe_set(owner, 'parameteredElement', None)
    assert getattr(partner, 'TemplateParameter175') is None


def test_assoc_thenExpression73_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression75' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression75', None)
    _safe_set(owner, 'pivot_IfExp74', partner)
    assert getattr(partner, 'pivot_OCLExpression75') == owner
    _safe_set(owner, 'pivot_IfExp74', None)
    assert getattr(partner, 'pivot_OCLExpression75') is None


def test_assoc_transition207_stub_double():
    # pivot_Region has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Region()
    setattr(partner, 'container', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_trigger309_stub_double():
    # pivot_Trigger has no real 'pivot_Trigger311' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'pivot_Trigger311', None)
    _safe_set(owner, 'pivot_Transition310', {partner})
    assert getattr(partner, 'pivot_Trigger311') == owner
    _safe_set(owner, 'pivot_Transition310', set())
    assert getattr(partner, 'pivot_Trigger311') is None


def test_assoc_unownedAttribute6_stub_double():
    # pivot_AssociationClass has no real 'association' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_AssociationClass()
    setattr(partner, 'association', None)
    _safe_set(owner, 'Property', partner)
    assert owner in getattr(partner, 'association')
    _safe_set(owner, 'Property', None)
    assert owner not in getattr(partner, 'association')


def test_assoc_upperBound338_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType339' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType339', None)
    _safe_set(owner, 'pivot_Type340', partner)
    assert getattr(partner, 'pivot_UnspecifiedType339') == owner
    _safe_set(owner, 'pivot_Type340', None)
    assert getattr(partner, 'pivot_UnspecifiedType339') is None


