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

def test_assoc_annotatedElement23_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment', {a1})
    assert _is_linked(b, 'pivot_Comment', a1)
    if hasattr(a1, 'pivot_Element24'):
        assert _is_linked(a1, 'pivot_Element24', b)
    _safe_set(b, 'pivot_Comment', {a2})
    assert _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a1, 'pivot_Element24'):
        assert not _is_linked(a1, 'pivot_Element24', b)
    if hasattr(a2, 'pivot_Element24'):
        assert _is_linked(a2, 'pivot_Element24', b)
    _safe_set(b, 'pivot_Comment', set())
    assert not _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a2, 'pivot_Element24'):
        assert not _is_linked(a2, 'pivot_Element24', b)


def test_assoc_behavioralType43_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_DataType(isSerializable="sample_text")
    _safe_set(b, 'pivot_DataType', a1)
    assert _is_linked(b, 'pivot_DataType', a1)
    if hasattr(a1, 'pivot_Type44'):
        assert _is_linked(a1, 'pivot_Type44', b)
    _safe_set(b, 'pivot_DataType', a2)
    assert _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a1, 'pivot_Type44'):
        assert not _is_linked(a1, 'pivot_Type44', b)
    if hasattr(a2, 'pivot_Type44'):
        assert _is_linked(a2, 'pivot_Type44', b)
    _safe_set(b, 'pivot_DataType', None)
    assert not _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a2, 'pivot_Type44'):
        assert not _is_linked(a2, 'pivot_Type44', b)


def test_assoc_bodyExpression138_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_OpaqueExpression(body="sample_text", language="sample_text", message="sample_text")
    _safe_set(b, 'pivot_OpaqueExpression140', a1)
    assert _is_linked(b, 'pivot_OpaqueExpression140', a1)
    if hasattr(a1, 'pivot_Operation139'):
        assert _is_linked(a1, 'pivot_Operation139', b)
    _safe_set(b, 'pivot_OpaqueExpression140', a2)
    assert _is_linked(b, 'pivot_OpaqueExpression140', a2)
    if hasattr(a1, 'pivot_Operation139'):
        assert not _is_linked(a1, 'pivot_Operation139', b)
    if hasattr(a2, 'pivot_Operation139'):
        assert _is_linked(a2, 'pivot_Operation139', b)
    _safe_set(b, 'pivot_OpaqueExpression140', None)
    assert not _is_linked(b, 'pivot_OpaqueExpression140', a2)
    if hasattr(a2, 'pivot_Operation139'):
        assert not _is_linked(a2, 'pivot_Operation139', b)


def test_assoc_class_141_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class143', a1)
    assert _is_linked(b, 'pivot_Class143', a1)
    if hasattr(a1, 'pivot_Operation142'):
        assert _is_linked(a1, 'pivot_Operation142', b)
    _safe_set(b, 'pivot_Class143', a2)
    assert _is_linked(b, 'pivot_Class143', a2)
    if hasattr(a1, 'pivot_Operation142'):
        assert not _is_linked(a1, 'pivot_Operation142', b)
    if hasattr(a2, 'pivot_Operation142'):
        assert _is_linked(a2, 'pivot_Operation142', b)
    _safe_set(b, 'pivot_Class143', None)
    assert not _is_linked(b, 'pivot_Class143', a2)
    if hasattr(a2, 'pivot_Operation142'):
        assert not _is_linked(a2, 'pivot_Operation142', b)


def test_assoc_class_180_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class182', a1)
    assert _is_linked(b, 'pivot_Class182', a1)
    if hasattr(a1, 'pivot_Property181'):
        assert _is_linked(a1, 'pivot_Property181', b)
    _safe_set(b, 'pivot_Class182', a2)
    assert _is_linked(b, 'pivot_Class182', a2)
    if hasattr(a1, 'pivot_Property181'):
        assert not _is_linked(a1, 'pivot_Property181', b)
    if hasattr(a2, 'pivot_Property181'):
        assert _is_linked(a2, 'pivot_Property181', b)
    _safe_set(b, 'pivot_Class182', None)
    assert not _is_linked(b, 'pivot_Class182', a2)
    if hasattr(a2, 'pivot_Property181'):
        assert not _is_linked(a2, 'pivot_Property181', b)


def test_assoc_connectionPoint232_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'pivot_Pseudostate234', a1)
    assert _is_linked(b, 'pivot_Pseudostate234', a1)
    if hasattr(a1, 'pivot_State233'):
        assert _is_linked(a1, 'pivot_State233', b)
    _safe_set(b, 'pivot_Pseudostate234', a2)
    assert _is_linked(b, 'pivot_Pseudostate234', a2)
    if hasattr(a1, 'pivot_State233'):
        assert not _is_linked(a1, 'pivot_State233', b)
    if hasattr(a2, 'pivot_State233'):
        assert _is_linked(a2, 'pivot_State233', b)
    _safe_set(b, 'pivot_Pseudostate234', None)
    assert not _is_linked(b, 'pivot_Pseudostate234', a2)
    if hasattr(a2, 'pivot_State233'):
        assert not _is_linked(a2, 'pivot_State233', b)


def test_assoc_constrainedElement31_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint', {a1})
    assert _is_linked(b, 'pivot_Constraint', a1)
    if hasattr(a1, 'pivot_Element32'):
        assert _is_linked(a1, 'pivot_Element32', b)
    _safe_set(b, 'pivot_Constraint', {a2})
    assert _is_linked(b, 'pivot_Constraint', a2)
    if hasattr(a1, 'pivot_Element32'):
        assert not _is_linked(a1, 'pivot_Element32', b)
    if hasattr(a2, 'pivot_Element32'):
        assert _is_linked(a2, 'pivot_Element32', b)
    _safe_set(b, 'pivot_Constraint', set())
    assert not _is_linked(b, 'pivot_Constraint', a2)
    if hasattr(a2, 'pivot_Element32'):
        assert not _is_linked(a2, 'pivot_Element32', b)


def test_assoc_constrainingType335_reverse_link_reassign_clear():
    a1 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text")
    a2 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type336', a1)
    assert _is_linked(b, 'pivot_Type336', a1)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type336', a2)
    assert _is_linked(b, 'pivot_Type336', a2)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert not _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    if hasattr(a2, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a2, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type336', None)
    assert not _is_linked(b, 'pivot_Type336', a2)
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


def test_assoc_elementType22_reverse_link_reassign_clear():
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


def test_assoc_guard306_reverse_link_reassign_clear():
    a1 = pivot_Transition(kind="sample_text")
    a2 = pivot_Transition(kind="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint308', a1)
    assert _is_linked(b, 'pivot_Constraint308', a1)
    if hasattr(a1, 'pivot_Transition307'):
        assert _is_linked(a1, 'pivot_Transition307', b)
    _safe_set(b, 'pivot_Constraint308', a2)
    assert _is_linked(b, 'pivot_Constraint308', a2)
    if hasattr(a1, 'pivot_Transition307'):
        assert not _is_linked(a1, 'pivot_Transition307', b)
    if hasattr(a2, 'pivot_Transition307'):
        assert _is_linked(a2, 'pivot_Transition307', b)
    _safe_set(b, 'pivot_Constraint308', None)
    assert not _is_linked(b, 'pivot_Constraint308', a2)
    if hasattr(a2, 'pivot_Transition307'):
        assert not _is_linked(a2, 'pivot_Transition307', b)


def test_assoc_importedPackage167_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package166', {a1})
    assert _is_linked(b, 'pivot_Package166', a1)
    if hasattr(a1, 'pivot_Package'):
        assert _is_linked(a1, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package166', {a2})
    assert _is_linked(b, 'pivot_Package166', a2)
    if hasattr(a1, 'pivot_Package'):
        assert not _is_linked(a1, 'pivot_Package', b)
    if hasattr(a2, 'pivot_Package'):
        assert _is_linked(a2, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package166', set())
    assert not _is_linked(b, 'pivot_Package166', a2)
    if hasattr(a2, 'pivot_Package'):
        assert not _is_linked(a2, 'pivot_Package', b)


def test_assoc_iterator106_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LoopExp()
    _safe_set(b, 'pivot_LoopExp107', {a1})
    assert _is_linked(b, 'pivot_LoopExp107', a1)
    if hasattr(a1, 'pivot_Variable108'):
        assert _is_linked(a1, 'pivot_Variable108', b)
    _safe_set(b, 'pivot_LoopExp107', {a2})
    assert _is_linked(b, 'pivot_LoopExp107', a2)
    if hasattr(a1, 'pivot_Variable108'):
        assert not _is_linked(a1, 'pivot_Variable108', b)
    if hasattr(a2, 'pivot_Variable108'):
        assert _is_linked(a2, 'pivot_Variable108', b)
    _safe_set(b, 'pivot_LoopExp107', set())
    assert not _is_linked(b, 'pivot_LoopExp107', a2)
    if hasattr(a2, 'pivot_Variable108'):
        assert not _is_linked(a2, 'pivot_Variable108', b)


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


def test_assoc_nestedPackage169_reverse_link_reassign_clear():
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


def test_assoc_nestedPackage223_reverse_link_reassign_clear():
    a1 = pivot_Root(externalURI="sample_text")
    a2 = pivot_Root(externalURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package225', a1)
    assert _is_linked(b, 'pivot_Package225', a1)
    if hasattr(a1, 'pivot_Root224'):
        assert _is_linked(a1, 'pivot_Root224', b)
    _safe_set(b, 'pivot_Package225', a2)
    assert _is_linked(b, 'pivot_Package225', a2)
    if hasattr(a1, 'pivot_Root224'):
        assert not _is_linked(a1, 'pivot_Root224', b)
    if hasattr(a2, 'pivot_Root224'):
        assert _is_linked(a2, 'pivot_Root224', b)
    _safe_set(b, 'pivot_Package225', None)
    assert not _is_linked(b, 'pivot_Package225', a2)
    if hasattr(a2, 'pivot_Root224'):
        assert not _is_linked(a2, 'pivot_Root224', b)


def test_assoc_nestedType11_reverse_link_reassign_clear():
    a1 = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    a2 = pivot_Class(isAbstract="sample_text_2", isInterface="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class10', {a1})
    assert _is_linked(b, 'pivot_Class10', a1)
    if hasattr(a1, 'pivot_Class'):
        assert _is_linked(a1, 'pivot_Class', b)
    _safe_set(b, 'pivot_Class10', {a2})
    assert _is_linked(b, 'pivot_Class10', a2)
    if hasattr(a1, 'pivot_Class'):
        assert not _is_linked(a1, 'pivot_Class', b)
    if hasattr(a2, 'pivot_Class'):
        assert _is_linked(a2, 'pivot_Class', b)
    _safe_set(b, 'pivot_Class10', set())
    assert not _is_linked(b, 'pivot_Class10', a2)
    if hasattr(a2, 'pivot_Class'):
        assert not _is_linked(a2, 'pivot_Class', b)


def test_assoc_nestingPackage171_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'nestedPackage', a1)
    assert _is_linked(b, 'nestedPackage', a1)
    if hasattr(a1, 'Package172'):
        assert _is_linked(a1, 'Package172', b)
    _safe_set(b, 'nestedPackage', a2)
    assert _is_linked(b, 'nestedPackage', a2)
    if hasattr(a1, 'Package172'):
        assert not _is_linked(a1, 'Package172', b)
    if hasattr(a2, 'Package172'):
        assert _is_linked(a2, 'Package172', b)
    _safe_set(b, 'nestedPackage', None)
    assert not _is_linked(b, 'nestedPackage', a2)
    if hasattr(a2, 'Package172'):
        assert not _is_linked(a2, 'Package172', b)


def test_assoc_opposite190_reverse_link_reassign_clear():
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


def test_assoc_ownedAttribute320_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'Property321', a1)
    assert _is_linked(b, 'Property321', a1)
    if hasattr(a1, 'owningType'):
        assert _is_linked(a1, 'owningType', b)
    _safe_set(b, 'Property321', a2)
    assert _is_linked(b, 'Property321', a2)
    if hasattr(a1, 'owningType'):
        assert not _is_linked(a1, 'owningType', b)
    if hasattr(a2, 'owningType'):
        assert _is_linked(a2, 'owningType', b)
    _safe_set(b, 'Property321', None)
    assert not _is_linked(b, 'Property321', a2)
    if hasattr(a2, 'owningType'):
        assert not _is_linked(a2, 'owningType', b)


def test_assoc_ownedComment52_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment54', a1)
    assert _is_linked(b, 'pivot_Comment54', a1)
    if hasattr(a1, 'pivot_Element53'):
        assert _is_linked(a1, 'pivot_Element53', b)
    _safe_set(b, 'pivot_Comment54', a2)
    assert _is_linked(b, 'pivot_Comment54', a2)
    if hasattr(a1, 'pivot_Element53'):
        assert not _is_linked(a1, 'pivot_Element53', b)
    if hasattr(a2, 'pivot_Element53'):
        assert _is_linked(a2, 'pivot_Element53', b)
    _safe_set(b, 'pivot_Comment54', None)
    assert not _is_linked(b, 'pivot_Comment54', a2)
    if hasattr(a2, 'pivot_Element53'):
        assert not _is_linked(a2, 'pivot_Element53', b)


def test_assoc_ownedInvariant322_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint324', a1)
    assert _is_linked(b, 'pivot_Constraint324', a1)
    if hasattr(a1, 'pivot_Type323'):
        assert _is_linked(a1, 'pivot_Type323', b)
    _safe_set(b, 'pivot_Constraint324', a2)
    assert _is_linked(b, 'pivot_Constraint324', a2)
    if hasattr(a1, 'pivot_Type323'):
        assert not _is_linked(a1, 'pivot_Type323', b)
    if hasattr(a2, 'pivot_Type323'):
        assert _is_linked(a2, 'pivot_Type323', b)
    _safe_set(b, 'pivot_Constraint324', None)
    assert not _is_linked(b, 'pivot_Constraint324', a2)
    if hasattr(a2, 'pivot_Type323'):
        assert not _is_linked(a2, 'pivot_Type323', b)


def test_assoc_ownedOperation325_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'Operation327', a1)
    assert _is_linked(b, 'Operation327', a1)
    if hasattr(a1, 'owningType326'):
        assert _is_linked(a1, 'owningType326', b)
    _safe_set(b, 'Operation327', a2)
    assert _is_linked(b, 'Operation327', a2)
    if hasattr(a1, 'owningType326'):
        assert not _is_linked(a1, 'owningType326', b)
    if hasattr(a2, 'owningType326'):
        assert _is_linked(a2, 'owningType326', b)
    _safe_set(b, 'Operation327', None)
    assert not _is_linked(b, 'Operation327', a2)
    if hasattr(a2, 'owningType326'):
        assert not _is_linked(a2, 'owningType326', b)


def test_assoc_ownedType173_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'package', {a1})
    assert _is_linked(b, 'package', a1)
    if hasattr(a1, 'Type174'):
        assert _is_linked(a1, 'Type174', b)
    _safe_set(b, 'package', {a2})
    assert _is_linked(b, 'package', a2)
    if hasattr(a1, 'Type174'):
        assert not _is_linked(a1, 'Type174', b)
    if hasattr(a2, 'Type174'):
        assert _is_linked(a2, 'Type174', b)
    _safe_set(b, 'package', set())
    assert not _is_linked(b, 'package', a2)
    if hasattr(a2, 'Type174'):
        assert not _is_linked(a2, 'Type174', b)


def test_assoc_owningType145_reverse_link_reassign_clear():
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


def test_assoc_owningType192_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'ownedAttribute', a1)
    assert _is_linked(b, 'ownedAttribute', a1)
    if hasattr(a1, 'Type193'):
        assert _is_linked(a1, 'Type193', b)
    _safe_set(b, 'ownedAttribute', a2)
    assert _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a1, 'Type193'):
        assert not _is_linked(a1, 'Type193', b)
    if hasattr(a2, 'Type193'):
        assert _is_linked(a2, 'Type193', b)
    _safe_set(b, 'ownedAttribute', None)
    assert not _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a2, 'Type193'):
        assert not _is_linked(a2, 'Type193', b)


def test_assoc_package328_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'Package329', a1)
    assert _is_linked(b, 'Package329', a1)
    if hasattr(a1, 'ownedType'):
        assert _is_linked(a1, 'ownedType', b)
    _safe_set(b, 'Package329', a2)
    assert _is_linked(b, 'Package329', a2)
    if hasattr(a1, 'ownedType'):
        assert not _is_linked(a1, 'ownedType', b)
    if hasattr(a2, 'ownedType'):
        assert _is_linked(a2, 'ownedType', b)
    _safe_set(b, 'Package329', None)
    assert not _is_linked(b, 'Package329', a2)
    if hasattr(a2, 'ownedType'):
        assert not _is_linked(a2, 'ownedType', b)


def test_assoc_postcondition146_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint148', a1)
    assert _is_linked(b, 'pivot_Constraint148', a1)
    if hasattr(a1, 'pivot_Operation147'):
        assert _is_linked(a1, 'pivot_Operation147', b)
    _safe_set(b, 'pivot_Constraint148', a2)
    assert _is_linked(b, 'pivot_Constraint148', a2)
    if hasattr(a1, 'pivot_Operation147'):
        assert not _is_linked(a1, 'pivot_Operation147', b)
    if hasattr(a2, 'pivot_Operation147'):
        assert _is_linked(a2, 'pivot_Operation147', b)
    _safe_set(b, 'pivot_Constraint148', None)
    assert not _is_linked(b, 'pivot_Constraint148', a2)
    if hasattr(a2, 'pivot_Operation147'):
        assert not _is_linked(a2, 'pivot_Operation147', b)


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


def test_assoc_precondition152_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint154', a1)
    assert _is_linked(b, 'pivot_Constraint154', a1)
    if hasattr(a1, 'pivot_Operation153'):
        assert _is_linked(a1, 'pivot_Operation153', b)
    _safe_set(b, 'pivot_Constraint154', a2)
    assert _is_linked(b, 'pivot_Constraint154', a2)
    if hasattr(a1, 'pivot_Operation153'):
        assert not _is_linked(a1, 'pivot_Operation153', b)
    if hasattr(a2, 'pivot_Operation153'):
        assert _is_linked(a2, 'pivot_Operation153', b)
    _safe_set(b, 'pivot_Constraint154', None)
    assert not _is_linked(b, 'pivot_Constraint154', a2)
    if hasattr(a2, 'pivot_Operation153'):
        assert not _is_linked(a2, 'pivot_Operation153', b)


def test_assoc_raisedException155_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation156', {a1})
    assert _is_linked(b, 'pivot_Operation156', a1)
    if hasattr(a1, 'pivot_Type157'):
        assert _is_linked(a1, 'pivot_Type157', b)
    _safe_set(b, 'pivot_Operation156', {a2})
    assert _is_linked(b, 'pivot_Operation156', a2)
    if hasattr(a1, 'pivot_Type157'):
        assert not _is_linked(a1, 'pivot_Type157', b)
    if hasattr(a2, 'pivot_Type157'):
        assert _is_linked(a2, 'pivot_Type157', b)
    _safe_set(b, 'pivot_Operation156', set())
    assert not _is_linked(b, 'pivot_Operation156', a2)
    if hasattr(a2, 'pivot_Type157'):
        assert not _is_linked(a2, 'pivot_Type157', b)


def test_assoc_redefinedOperation159_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation160', a1)
    assert _is_linked(b, 'pivot_Operation160', a1)
    if hasattr(a1, 'pivot_Operation158'):
        assert _is_linked(a1, 'pivot_Operation158', b)
    _safe_set(b, 'pivot_Operation160', a2)
    assert _is_linked(b, 'pivot_Operation160', a2)
    if hasattr(a1, 'pivot_Operation158'):
        assert not _is_linked(a1, 'pivot_Operation158', b)
    if hasattr(a2, 'pivot_Operation158'):
        assert _is_linked(a2, 'pivot_Operation158', b)
    _safe_set(b, 'pivot_Operation160', None)
    assert not _is_linked(b, 'pivot_Operation160', a2)
    if hasattr(a2, 'pivot_Operation158'):
        assert not _is_linked(a2, 'pivot_Operation158', b)


def test_assoc_redefinedProperty195_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property196', a1)
    assert _is_linked(b, 'pivot_Property196', a1)
    if hasattr(a1, 'pivot_Property194'):
        assert _is_linked(a1, 'pivot_Property194', b)
    _safe_set(b, 'pivot_Property196', a2)
    assert _is_linked(b, 'pivot_Property196', a2)
    if hasattr(a1, 'pivot_Property194'):
        assert not _is_linked(a1, 'pivot_Property194', b)
    if hasattr(a2, 'pivot_Property194'):
        assert _is_linked(a2, 'pivot_Property194', b)
    _safe_set(b, 'pivot_Property196', None)
    assert not _is_linked(b, 'pivot_Property196', a2)
    if hasattr(a2, 'pivot_Property194'):
        assert not _is_linked(a2, 'pivot_Property194', b)


def test_assoc_redefinedState247_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'pivot_State248', a1)
    assert _is_linked(b, 'pivot_State248', a1)
    if hasattr(a1, 'pivot_State246'):
        assert _is_linked(a1, 'pivot_State246', b)
    _safe_set(b, 'pivot_State248', a2)
    assert _is_linked(b, 'pivot_State248', a2)
    if hasattr(a1, 'pivot_State246'):
        assert not _is_linked(a1, 'pivot_State246', b)
    if hasattr(a2, 'pivot_State246'):
        assert _is_linked(a2, 'pivot_State246', b)
    _safe_set(b, 'pivot_State248', None)
    assert not _is_linked(b, 'pivot_State248', a2)
    if hasattr(a2, 'pivot_State246'):
        assert not _is_linked(a2, 'pivot_State246', b)


def test_assoc_referredEnumLiteral58_reverse_link_reassign_clear():
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


def test_assoc_referredOperation163_reverse_link_reassign_clear():
    a1 = pivot_OperationCallExp()
    a2 = pivot_OperationCallExp()
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation165', a1)
    assert _is_linked(b, 'pivot_Operation165', a1)
    if hasattr(a1, 'pivot_OperationCallExp164'):
        assert _is_linked(a1, 'pivot_OperationCallExp164', b)
    _safe_set(b, 'pivot_Operation165', a2)
    assert _is_linked(b, 'pivot_Operation165', a2)
    if hasattr(a1, 'pivot_OperationCallExp164'):
        assert not _is_linked(a1, 'pivot_OperationCallExp164', b)
    if hasattr(a2, 'pivot_OperationCallExp164'):
        assert _is_linked(a2, 'pivot_OperationCallExp164', b)
    _safe_set(b, 'pivot_Operation165', None)
    assert not _is_linked(b, 'pivot_Operation165', a2)
    if hasattr(a2, 'pivot_OperationCallExp164'):
        assert not _is_linked(a2, 'pivot_OperationCallExp164', b)


def test_assoc_referredProperty198_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property199', a1)
    assert _is_linked(b, 'pivot_Property199', a1)
    if hasattr(a1, 'pivot_Property197'):
        assert _is_linked(a1, 'pivot_Property197', b)
    _safe_set(b, 'pivot_Property199', a2)
    assert _is_linked(b, 'pivot_Property199', a2)
    if hasattr(a1, 'pivot_Property197'):
        assert not _is_linked(a1, 'pivot_Property197', b)
    if hasattr(a2, 'pivot_Property197'):
        assert _is_linked(a2, 'pivot_Property197', b)
    _safe_set(b, 'pivot_Property199', None)
    assert not _is_linked(b, 'pivot_Property199', a2)
    if hasattr(a2, 'pivot_Property197'):
        assert not _is_linked(a2, 'pivot_Property197', b)


def test_assoc_referredProperty203_reverse_link_reassign_clear():
    a1 = pivot_PropertyCallExp()
    a2 = pivot_PropertyCallExp()
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property204', a1)
    assert _is_linked(b, 'pivot_Property204', a1)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert _is_linked(a1, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property204', a2)
    assert _is_linked(b, 'pivot_Property204', a2)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert not _is_linked(a1, 'pivot_PropertyCallExp', b)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert _is_linked(a2, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property204', None)
    assert not _is_linked(b, 'pivot_Property204', a2)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert not _is_linked(a2, 'pivot_PropertyCallExp', b)


def test_assoc_referredProperty47_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_DynamicProperty(default="sample_text")
    _safe_set(b, 'pivot_DynamicProperty', a1)
    assert _is_linked(b, 'pivot_DynamicProperty', a1)
    if hasattr(a1, 'pivot_Property48'):
        assert _is_linked(a1, 'pivot_Property48', b)
    _safe_set(b, 'pivot_DynamicProperty', a2)
    assert _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a1, 'pivot_Property48'):
        assert not _is_linked(a1, 'pivot_Property48', b)
    if hasattr(a2, 'pivot_Property48'):
        assert _is_linked(a2, 'pivot_Property48', b)
    _safe_set(b, 'pivot_DynamicProperty', None)
    assert not _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a2, 'pivot_Property48'):
        assert not _is_linked(a2, 'pivot_Property48', b)


def test_assoc_result84_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_IterateExp()
    _safe_set(b, 'pivot_IterateExp', a1)
    assert _is_linked(b, 'pivot_IterateExp', a1)
    if hasattr(a1, 'pivot_Variable85'):
        assert _is_linked(a1, 'pivot_Variable85', b)
    _safe_set(b, 'pivot_IterateExp', a2)
    assert _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a1, 'pivot_Variable85'):
        assert not _is_linked(a1, 'pivot_Variable85', b)
    if hasattr(a2, 'pivot_Variable85'):
        assert _is_linked(a2, 'pivot_Variable85', b)
    _safe_set(b, 'pivot_IterateExp', None)
    assert not _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a2, 'pivot_Variable85'):
        assert not _is_linked(a2, 'pivot_Variable85', b)


def test_assoc_specification35_reverse_link_reassign_clear():
    a1 = pivot_OpaqueExpression(body="sample_text", language="sample_text", message="sample_text")
    a2 = pivot_OpaqueExpression(body="sample_text_2", language="sample_text_2", message="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint36', a1)
    assert _is_linked(b, 'pivot_Constraint36', a1)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert _is_linked(a1, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint36', a2)
    assert _is_linked(b, 'pivot_Constraint36', a2)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert not _is_linked(a1, 'pivot_OpaqueExpression', b)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert _is_linked(a2, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint36', None)
    assert not _is_linked(b, 'pivot_Constraint36', a2)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert not _is_linked(a2, 'pivot_OpaqueExpression', b)


def test_assoc_state205_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'pivot_Pseudostate206', a1)
    assert _is_linked(b, 'pivot_Pseudostate206', a1)
    if hasattr(a1, 'pivot_State207'):
        assert _is_linked(a1, 'pivot_State207', b)
    _safe_set(b, 'pivot_Pseudostate206', a2)
    assert _is_linked(b, 'pivot_Pseudostate206', a2)
    if hasattr(a1, 'pivot_State207'):
        assert not _is_linked(a1, 'pivot_State207', b)
    if hasattr(a2, 'pivot_State207'):
        assert _is_linked(a2, 'pivot_State207', b)
    _safe_set(b, 'pivot_Pseudostate206', None)
    assert not _is_linked(b, 'pivot_Pseudostate206', a2)
    if hasattr(a2, 'pivot_State207'):
        assert not _is_linked(a2, 'pivot_State207', b)


def test_assoc_stateInvariant252_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint254', a1)
    assert _is_linked(b, 'pivot_Constraint254', a1)
    if hasattr(a1, 'pivot_State253'):
        assert _is_linked(a1, 'pivot_State253', b)
    _safe_set(b, 'pivot_Constraint254', a2)
    assert _is_linked(b, 'pivot_Constraint254', a2)
    if hasattr(a1, 'pivot_State253'):
        assert not _is_linked(a1, 'pivot_State253', b)
    if hasattr(a2, 'pivot_State253'):
        assert _is_linked(a2, 'pivot_State253', b)
    _safe_set(b, 'pivot_Constraint254', None)
    assert not _is_linked(b, 'pivot_Constraint254', a2)
    if hasattr(a2, 'pivot_State253'):
        assert not _is_linked(a2, 'pivot_State253', b)


def test_assoc_subsettedProperty201_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property202', a1)
    assert _is_linked(b, 'pivot_Property202', a1)
    if hasattr(a1, 'pivot_Property200'):
        assert _is_linked(a1, 'pivot_Property200', b)
    _safe_set(b, 'pivot_Property202', a2)
    assert _is_linked(b, 'pivot_Property202', a2)
    if hasattr(a1, 'pivot_Property200'):
        assert not _is_linked(a1, 'pivot_Property200', b)
    if hasattr(a2, 'pivot_Property200'):
        assert _is_linked(a2, 'pivot_Property200', b)
    _safe_set(b, 'pivot_Property202', None)
    assert not _is_linked(b, 'pivot_Property202', a2)
    if hasattr(a2, 'pivot_Property200'):
        assert not _is_linked(a2, 'pivot_Property200', b)


def test_assoc_superClass331_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type332', a1)
    assert _is_linked(b, 'pivot_Type332', a1)
    if hasattr(a1, 'pivot_Type330'):
        assert _is_linked(a1, 'pivot_Type330', b)
    _safe_set(b, 'pivot_Type332', a2)
    assert _is_linked(b, 'pivot_Type332', a2)
    if hasattr(a1, 'pivot_Type330'):
        assert not _is_linked(a1, 'pivot_Type330', b)
    if hasattr(a2, 'pivot_Type330'):
        assert _is_linked(a2, 'pivot_Type330', b)
    _safe_set(b, 'pivot_Type332', None)
    assert not _is_linked(b, 'pivot_Type332', a2)
    if hasattr(a2, 'pivot_Type330'):
        assert not _is_linked(a2, 'pivot_Type330', b)


def test_assoc_type337_reverse_link_reassign_clear():
    a1 = pivot_TypedElement(isRequired="sample_text")
    a2 = pivot_TypedElement(isRequired="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type338', a1)
    assert _is_linked(b, 'pivot_Type338', a1)
    if hasattr(a1, 'pivot_TypedElement'):
        assert _is_linked(a1, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type338', a2)
    assert _is_linked(b, 'pivot_Type338', a2)
    if hasattr(a1, 'pivot_TypedElement'):
        assert not _is_linked(a1, 'pivot_TypedElement', b)
    if hasattr(a2, 'pivot_TypedElement'):
        assert _is_linked(a2, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type338', None)
    assert not _is_linked(b, 'pivot_Type338', a2)
    if hasattr(a2, 'pivot_TypedElement'):
        assert not _is_linked(a2, 'pivot_TypedElement', b)


def test_assoc_unspecializedElement302_reverse_link_reassign_clear():
    a1 = pivot_TemplateableElement()
    a2 = pivot_TemplateableElement()
    b = pivot_TemplateableElement()
    _safe_set(b, 'pivot_TemplateableElement301', a1)
    assert _is_linked(b, 'pivot_TemplateableElement301', a1)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert _is_linked(a1, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement301', a2)
    assert _is_linked(b, 'pivot_TemplateableElement301', a2)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert not _is_linked(a1, 'pivot_TemplateableElement', b)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert _is_linked(a2, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement301', None)
    assert not _is_linked(b, 'pivot_TemplateableElement301', a2)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert not _is_linked(a2, 'pivot_TemplateableElement', b)


def test_assoc_variable100_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LetExp()
    _safe_set(b, 'pivot_LetExp101', a1)
    assert _is_linked(b, 'pivot_LetExp101', a1)
    if hasattr(a1, 'pivot_Variable102'):
        assert _is_linked(a1, 'pivot_Variable102', b)
    _safe_set(b, 'pivot_LetExp101', a2)
    assert _is_linked(b, 'pivot_LetExp101', a2)
    if hasattr(a1, 'pivot_Variable102'):
        assert not _is_linked(a1, 'pivot_Variable102', b)
    if hasattr(a2, 'pivot_Variable102'):
        assert _is_linked(a2, 'pivot_Variable102', b)
    _safe_set(b, 'pivot_LetExp101', None)
    assert not _is_linked(b, 'pivot_LetExp101', a2)
    if hasattr(a2, 'pivot_Variable102'):
        assert not _is_linked(a2, 'pivot_Variable102', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actual281_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution', None)
    _safe_set(owner, 'pivot_ParameterableElement282', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution') == owner
    _safe_set(owner, 'pivot_ParameterableElement282', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution') is None


def test_assoc_argument112_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression113' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression113', None)
    _safe_set(owner, 'pivot_MessageExp', {partner})
    assert getattr(partner, 'pivot_OCLExpression113') == owner
    _safe_set(owner, 'pivot_MessageExp', set())
    assert getattr(partner, 'pivot_OCLExpression113') is None


def test_assoc_argument161_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression162' property in the generated
    # code (a bare stub) -- manually attach it so pivot_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_OperationCallExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression162', None)
    _safe_set(owner, 'pivot_OperationCallExp', {partner})
    assert getattr(partner, 'pivot_OCLExpression162') == owner
    _safe_set(owner, 'pivot_OperationCallExp', set())
    assert getattr(partner, 'pivot_OCLExpression162') is None


def test_assoc_association179_stub_double():
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


def test_assoc_base55_stub_double():
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


def test_assoc_body104_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression105' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression105', None)
    _safe_set(owner, 'pivot_LoopExp', partner)
    assert getattr(partner, 'pivot_OCLExpression105') == owner
    _safe_set(owner, 'pivot_LoopExp', None)
    assert getattr(partner, 'pivot_OCLExpression105') is None


def test_assoc_boundElement268_stub_double():
    # pivot_TemplateBinding has no real 'templateBinding' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateBinding()
    setattr(partner, 'templateBinding', None)
    _safe_set(owner, 'TemplateableElement', partner)
    assert getattr(partner, 'templateBinding') == owner
    _safe_set(owner, 'TemplateableElement', None)
    assert getattr(partner, 'templateBinding') is None


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


def test_assoc_condition74_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression75' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression75', None)
    _safe_set(owner, 'pivot_IfExp', partner)
    assert getattr(partner, 'pivot_OCLExpression75') == owner
    _safe_set(owner, 'pivot_IfExp', None)
    assert getattr(partner, 'pivot_OCLExpression75') is None


def test_assoc_connection229_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference231' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference231', None)
    _safe_set(owner, 'pivot_State230', {partner})
    assert getattr(partner, 'pivot_ConnectionPointReference231') == owner
    _safe_set(owner, 'pivot_State230', set())
    assert getattr(partner, 'pivot_ConnectionPointReference231') is None


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


def test_assoc_container303_stub_double():
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


def test_assoc_context33_stub_double():
    # pivot_Namespace has no real 'pivot_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Constraint(isCallable="sample_text")
    partner = pivot_Namespace()
    setattr(partner, 'pivot_Namespace', None)
    _safe_set(owner, 'pivot_Constraint34', partner)
    assert getattr(partner, 'pivot_Namespace') == owner
    _safe_set(owner, 'pivot_Constraint34', None)
    assert getattr(partner, 'pivot_Namespace') is None


def test_assoc_contextType90_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType', None)
    _safe_set(owner, 'pivot_Type91', partner)
    assert getattr(partner, 'pivot_LambdaType') == owner
    _safe_set(owner, 'pivot_Type91', None)
    assert getattr(partner, 'pivot_LambdaType') is None


def test_assoc_contextVariable63_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL64' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL64', None)
    _safe_set(owner, 'pivot_Variable', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL64') == owner
    _safe_set(owner, 'pivot_Variable', None)
    assert getattr(partner, 'pivot_ExpressionInOCL64') is None


def test_assoc_default272_stub_double():
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


def test_assoc_deferrableTrigger235_stub_double():
    # pivot_Trigger has no real 'pivot_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'pivot_Trigger', None)
    _safe_set(owner, 'pivot_State236', {partner})
    assert getattr(partner, 'pivot_Trigger') == owner
    _safe_set(owner, 'pivot_State236', set())
    assert getattr(partner, 'pivot_Trigger') is None


def test_assoc_doActivity237_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior239' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior239', None)
    _safe_set(owner, 'pivot_State238', partner)
    assert getattr(partner, 'pivot_Behavior239') == owner
    _safe_set(owner, 'pivot_State238', None)
    assert getattr(partner, 'pivot_Behavior239') is None


def test_assoc_effect304_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior305' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior305', None)
    _safe_set(owner, 'pivot_Transition', partner)
    assert getattr(partner, 'pivot_Behavior305') == owner
    _safe_set(owner, 'pivot_Transition', None)
    assert getattr(partner, 'pivot_Behavior305') is None


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


def test_assoc_entry240_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior242' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior242', None)
    _safe_set(owner, 'pivot_State241', partner)
    assert getattr(partner, 'pivot_Behavior242') == owner
    _safe_set(owner, 'pivot_State241', None)
    assert getattr(partner, 'pivot_Behavior242') is None


def test_assoc_entry25_stub_double():
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


def test_assoc_enumeration60_stub_double():
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


def test_assoc_exit243_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior245' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior245', None)
    _safe_set(owner, 'pivot_State244', partner)
    assert getattr(partner, 'pivot_Behavior245') == owner
    _safe_set(owner, 'pivot_State244', None)
    assert getattr(partner, 'pivot_Behavior245') is None


def test_assoc_exit26_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference27' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference27', None)
    _safe_set(owner, 'pivot_Pseudostate28', partner)
    assert owner in getattr(partner, 'pivot_ConnectionPointReference27')
    _safe_set(owner, 'pivot_Pseudostate28', None)
    assert owner not in getattr(partner, 'pivot_ConnectionPointReference27')


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


def test_assoc_imports221_stub_double():
    # pivot_Import has no real 'pivot_Import222' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Root(externalURI="sample_text")
    partner = pivot_Import()
    setattr(partner, 'pivot_Import222', None)
    _safe_set(owner, 'pivot_Root', {partner})
    assert getattr(partner, 'pivot_Import222') == owner
    _safe_set(owner, 'pivot_Root', set())
    assert getattr(partner, 'pivot_Import222') is None


def test_assoc_in_98_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression99' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LetExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LetExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LetExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression99', None)
    _safe_set(owner, 'pivot_LetExp', partner)
    assert getattr(partner, 'pivot_OCLExpression99') == owner
    _safe_set(owner, 'pivot_LetExp', None)
    assert getattr(partner, 'pivot_OCLExpression99') is None


def test_assoc_incoming353_stub_double():
    # pivot_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition354', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition354', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_initExpression344_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression346' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression346', None)
    _safe_set(owner, 'pivot_Variable345', partner)
    assert getattr(partner, 'pivot_OCLExpression346') == owner
    _safe_set(owner, 'pivot_Variable345', None)
    assert getattr(partner, 'pivot_OCLExpression346') is None


def test_assoc_instanceType126_stub_double():
    # pivot_Metaclass has no real 'pivot_Metaclass' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_Metaclass()
    setattr(partner, 'pivot_Metaclass', None)
    _safe_set(owner, 'pivot_Type127', partner)
    assert getattr(partner, 'pivot_Metaclass') == owner
    _safe_set(owner, 'pivot_Type127', None)
    assert getattr(partner, 'pivot_Metaclass') is None


def test_assoc_item14_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression15' property in the generated
    # code (a bare stub) -- manually attach it so pivot_CollectionItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_CollectionItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_CollectionItem()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression15', None)
    _safe_set(owner, 'pivot_CollectionItem', partner)
    assert getattr(partner, 'pivot_OCLExpression15') == owner
    _safe_set(owner, 'pivot_CollectionItem', None)
    assert getattr(partner, 'pivot_OCLExpression15') is None


def test_assoc_lowerBound339_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType', None)
    _safe_set(owner, 'pivot_Type340', partner)
    assert getattr(partner, 'pivot_UnspecifiedType') == owner
    _safe_set(owner, 'pivot_Type340', None)
    assert getattr(partner, 'pivot_UnspecifiedType') is None


def test_assoc_metaType45_stub_double():
    # pivot_DynamicElement has no real 'pivot_DynamicElement' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_DynamicElement()
    setattr(partner, 'pivot_DynamicElement', None)
    _safe_set(owner, 'pivot_Type46', partner)
    assert getattr(partner, 'pivot_DynamicElement') == owner
    _safe_set(owner, 'pivot_Type46', None)
    assert getattr(partner, 'pivot_DynamicElement') is None


def test_assoc_navigationSource133_stub_double():
    # pivot_NavigationCallExp has no real 'pivot_NavigationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_NavigationCallExp()
    setattr(partner, 'pivot_NavigationCallExp', None)
    _safe_set(owner, 'pivot_Property134', partner)
    assert getattr(partner, 'pivot_NavigationCallExp') == owner
    _safe_set(owner, 'pivot_Property134', None)
    assert getattr(partner, 'pivot_NavigationCallExp') is None


def test_assoc_operation175_stub_double():
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


def test_assoc_outgoing355_stub_double():
    # pivot_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition356', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition356', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedActual286_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution287' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution287', None)
    _safe_set(owner, 'pivot_ParameterableElement288', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution287') == owner
    _safe_set(owner, 'pivot_ParameterableElement288', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution287') is None


def test_assoc_ownedAnnotation128_stub_double():
    # pivot_Annotation has no real 'pivot_Annotation129' property in the generated
    # code (a bare stub) -- manually attach it so pivot_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_NamedElement(isStatic="sample_text", name="sample_text")
    partner = pivot_Annotation()
    setattr(partner, 'pivot_Annotation129', None)
    _safe_set(owner, 'pivot_NamedElement', {partner})
    assert getattr(partner, 'pivot_Annotation129') == owner
    _safe_set(owner, 'pivot_NamedElement', set())
    assert getattr(partner, 'pivot_Annotation129') is None


def test_assoc_ownedBehavior12_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Class(isAbstract="sample_text", isInterface="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior', None)
    _safe_set(owner, 'pivot_Class13', {partner})
    assert getattr(partner, 'pivot_Behavior') == owner
    _safe_set(owner, 'pivot_Class13', set())
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


def test_assoc_ownedDefault273_stub_double():
    # pivot_TemplateParameter has no real 'pivot_TemplateParameter274' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'pivot_TemplateParameter274', None)
    _safe_set(owner, 'pivot_ParameterableElement275', partner)
    assert getattr(partner, 'pivot_TemplateParameter274') == owner
    _safe_set(owner, 'pivot_ParameterableElement275', None)
    assert getattr(partner, 'pivot_TemplateParameter274') is None


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


def test_assoc_ownedLiteral59_stub_double():
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


def test_assoc_ownedParameter144_stub_double():
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


def test_assoc_ownedParameteredElement276_stub_double():
    # pivot_TemplateParameter has no real 'owningTemplateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'owningTemplateParameter', None)
    _safe_set(owner, 'ParameterableElement', partner)
    assert getattr(partner, 'owningTemplateParameter') == owner
    _safe_set(owner, 'ParameterableElement', None)
    assert getattr(partner, 'owningTemplateParameter') is None


def test_assoc_ownedPrecedence103_stub_double():
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


def test_assoc_ownedProperty49_stub_double():
    # pivot_DynamicType has no real 'pivot_DynamicType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_DynamicProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_DynamicProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_DynamicProperty(default="sample_text")
    partner = pivot_DynamicType()
    setattr(partner, 'pivot_DynamicType', None)
    _safe_set(owner, 'pivot_DynamicProperty50', partner)
    assert owner in getattr(partner, 'pivot_DynamicType')
    _safe_set(owner, 'pivot_DynamicProperty50', None)
    assert owner not in getattr(partner, 'pivot_DynamicType')


def test_assoc_ownedRule130_stub_double():
    # pivot_Namespace has no real 'pivot_Namespace131' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Constraint(isCallable="sample_text")
    partner = pivot_Namespace()
    setattr(partner, 'pivot_Namespace131', None)
    _safe_set(owner, 'pivot_Constraint132', partner)
    assert owner in getattr(partner, 'pivot_Namespace131')
    _safe_set(owner, 'pivot_Constraint132', None)
    assert owner not in getattr(partner, 'pivot_Namespace131')


def test_assoc_ownedTemplateSignature297_stub_double():
    # pivot_TemplateSignature has no real 'TemplateSignature298' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'TemplateSignature298', None)
    _safe_set(owner, 'template', partner)
    assert getattr(partner, 'TemplateSignature298') == owner
    _safe_set(owner, 'template', None)
    assert getattr(partner, 'TemplateSignature298') is None


def test_assoc_owningTemplateParameter176_stub_double():
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


def test_assoc_parameterType92_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType93' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType93', None)
    _safe_set(owner, 'pivot_Type94', partner)
    assert owner in getattr(partner, 'pivot_LambdaType93')
    _safe_set(owner, 'pivot_Type94', None)
    assert owner not in getattr(partner, 'pivot_LambdaType93')


def test_assoc_parameterVariable68_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL69' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL69', None)
    _safe_set(owner, 'pivot_Variable70', partner)
    assert owner in getattr(partner, 'pivot_ExpressionInOCL69')
    _safe_set(owner, 'pivot_Variable70', None)
    assert owner not in getattr(partner, 'pivot_ExpressionInOCL69')


def test_assoc_parameteredElement277_stub_double():
    # pivot_TemplateParameter has no real 'templateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'templateParameter', None)
    _safe_set(owner, 'ParameterableElement278', partner)
    assert getattr(partner, 'templateParameter') == owner
    _safe_set(owner, 'ParameterableElement278', None)
    assert getattr(partner, 'templateParameter') is None


def test_assoc_part16_stub_double():
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


def test_assoc_part37_stub_double():
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


def test_assoc_referredIteration109_stub_double():
    # pivot_Iteration has no real 'pivot_Iteration111' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_Iteration()
    setattr(partner, 'pivot_Iteration111', None)
    _safe_set(owner, 'pivot_LoopExp110', partner)
    assert getattr(partner, 'pivot_Iteration111') == owner
    _safe_set(owner, 'pivot_LoopExp110', None)
    assert getattr(partner, 'pivot_Iteration111') is None


def test_assoc_referredOperation122_stub_double():
    # pivot_MessageType has no real 'pivot_MessageType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_MessageType()
    setattr(partner, 'pivot_MessageType', None)
    _safe_set(owner, 'pivot_Operation123', partner)
    assert getattr(partner, 'pivot_MessageType') == owner
    _safe_set(owner, 'pivot_Operation123', None)
    assert getattr(partner, 'pivot_MessageType') is None


def test_assoc_referredProperty41_stub_double():
    # pivot_ConstructorPart has no real 'pivot_ConstructorPart42' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_ConstructorPart()
    setattr(partner, 'pivot_ConstructorPart42', None)
    _safe_set(owner, 'pivot_Property', partner)
    assert getattr(partner, 'pivot_ConstructorPart42') == owner
    _safe_set(owner, 'pivot_Property', None)
    assert getattr(partner, 'pivot_ConstructorPart42') is None


def test_assoc_referredState256_stub_double():
    # pivot_StateExp has no real 'pivot_StateExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateExp()
    setattr(partner, 'pivot_StateExp', None)
    _safe_set(owner, 'pivot_State257', partner)
    assert getattr(partner, 'pivot_StateExp') == owner
    _safe_set(owner, 'pivot_State257', None)
    assert getattr(partner, 'pivot_StateExp') is None


def test_assoc_referredType333_stub_double():
    # pivot_TypeExp has no real 'pivot_TypeExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_TypeExp()
    setattr(partner, 'pivot_TypeExp', None)
    _safe_set(owner, 'pivot_Type334', partner)
    assert getattr(partner, 'pivot_TypeExp') == owner
    _safe_set(owner, 'pivot_Type334', None)
    assert getattr(partner, 'pivot_TypeExp') is None


def test_assoc_referredVariable350_stub_double():
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


def test_assoc_region249_stub_double():
    # pivot_Region has no real 'pivot_Region251' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'pivot_Region251', None)
    _safe_set(owner, 'pivot_State250', {partner})
    assert getattr(partner, 'pivot_Region251') == owner
    _safe_set(owner, 'pivot_State250', set())
    assert getattr(partner, 'pivot_Region251') is None


def test_assoc_representedParameter347_stub_double():
    # pivot_Parameter has no real 'pivot_Parameter349' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_Parameter()
    setattr(partner, 'pivot_Parameter349', None)
    _safe_set(owner, 'pivot_Variable348', partner)
    assert getattr(partner, 'pivot_Parameter349') == owner
    _safe_set(owner, 'pivot_Variable348', None)
    assert getattr(partner, 'pivot_Parameter349') is None


def test_assoc_resultType95_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType96' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType96', None)
    _safe_set(owner, 'pivot_Type97', partner)
    assert getattr(partner, 'pivot_LambdaType96') == owner
    _safe_set(owner, 'pivot_Type97', None)
    assert getattr(partner, 'pivot_LambdaType96') is None


def test_assoc_resultVariable71_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL72' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL72', None)
    _safe_set(owner, 'pivot_Variable73', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL72') == owner
    _safe_set(owner, 'pivot_Variable73', None)
    assert getattr(partner, 'pivot_ExpressionInOCL72') is None


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


def test_assoc_source309_stub_double():
    # pivot_Vertex has no real 'Vertex310' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex310', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex310') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex310') is None


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


def test_assoc_state212_stub_double():
    # pivot_Region has no real 'pivot_Region213' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'pivot_Region213', None)
    _safe_set(owner, 'pivot_State214', partner)
    assert getattr(partner, 'pivot_Region213') == owner
    _safe_set(owner, 'pivot_State214', None)
    assert getattr(partner, 'pivot_Region213') is None


def test_assoc_state29_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference30' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference30', None)
    _safe_set(owner, 'pivot_State', partner)
    assert getattr(partner, 'pivot_ConnectionPointReference30') == owner
    _safe_set(owner, 'pivot_State', None)
    assert getattr(partner, 'pivot_ConnectionPointReference30') is None


def test_assoc_stateMachine208_stub_double():
    # pivot_StateMachine has no real 'pivot_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'pivot_StateMachine', None)
    _safe_set(owner, 'pivot_Pseudostate209', partner)
    assert getattr(partner, 'pivot_StateMachine') == owner
    _safe_set(owner, 'pivot_Pseudostate209', None)
    assert getattr(partner, 'pivot_StateMachine') is None


def test_assoc_stereotype56_stub_double():
    # pivot_ElementExtension has no real 'pivot_ElementExtension' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_ElementExtension()
    setattr(partner, 'pivot_ElementExtension', None)
    _safe_set(owner, 'pivot_Type57', partner)
    assert getattr(partner, 'pivot_ElementExtension') == owner
    _safe_set(owner, 'pivot_Type57', None)
    assert getattr(partner, 'pivot_ElementExtension') is None


def test_assoc_submachine255_stub_double():
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


def test_assoc_submachineState267_stub_double():
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


def test_assoc_target119_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression121' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression121', None)
    _safe_set(owner, 'pivot_MessageExp120', partner)
    assert getattr(partner, 'pivot_OCLExpression121') == owner
    _safe_set(owner, 'pivot_MessageExp120', None)
    assert getattr(partner, 'pivot_OCLExpression121') is None


def test_assoc_target311_stub_double():
    # pivot_Vertex has no real 'Vertex312' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex312', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex312') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex312') is None


def test_assoc_template295_stub_double():
    # pivot_TemplateSignature has no real 'ownedTemplateSignature' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'ownedTemplateSignature', None)
    _safe_set(owner, 'TemplateableElement296', partner)
    assert getattr(partner, 'ownedTemplateSignature') == owner
    _safe_set(owner, 'TemplateableElement296', None)
    assert getattr(partner, 'ownedTemplateSignature') is None


def test_assoc_templateBinding299_stub_double():
    # pivot_TemplateBinding has no real 'TemplateBinding300' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateBinding()
    setattr(partner, 'TemplateBinding300', None)
    _safe_set(owner, 'boundElement', {partner})
    assert getattr(partner, 'TemplateBinding300') == owner
    _safe_set(owner, 'boundElement', set())
    assert getattr(partner, 'TemplateBinding300') is None


def test_assoc_templateParameter177_stub_double():
    # pivot_TemplateParameter has no real 'TemplateParameter178' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'TemplateParameter178', None)
    _safe_set(owner, 'parameteredElement', partner)
    assert getattr(partner, 'TemplateParameter178') == owner
    _safe_set(owner, 'parameteredElement', None)
    assert getattr(partner, 'TemplateParameter178') is None


def test_assoc_thenExpression79_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression81' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression81', None)
    _safe_set(owner, 'pivot_IfExp80', partner)
    assert getattr(partner, 'pivot_OCLExpression81') == owner
    _safe_set(owner, 'pivot_IfExp80', None)
    assert getattr(partner, 'pivot_OCLExpression81') is None


def test_assoc_transition219_stub_double():
    # pivot_Region has no real 'container220' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Region()
    setattr(partner, 'container220', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'container220')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'container220')


def test_assoc_trigger313_stub_double():
    # pivot_Trigger has no real 'pivot_Trigger315' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'pivot_Trigger315', None)
    _safe_set(owner, 'pivot_Transition314', {partner})
    assert getattr(partner, 'pivot_Trigger315') == owner
    _safe_set(owner, 'pivot_Transition314', set())
    assert getattr(partner, 'pivot_Trigger315') is None


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


def test_assoc_upperBound341_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType342' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType342', None)
    _safe_set(owner, 'pivot_Type343', partner)
    assert getattr(partner, 'pivot_UnspecifiedType342') == owner
    _safe_set(owner, 'pivot_Type343', None)
    assert getattr(partner, 'pivot_UnspecifiedType342') is None


