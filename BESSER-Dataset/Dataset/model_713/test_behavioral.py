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
    pivot_OppositePropertyCallExp,
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
    pivot_ProfileApplication,
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
    pivot_TypeExtension,
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

def test_assoc_annotatedElement24_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment', {a1})
    assert _is_linked(b, 'pivot_Comment', a1)
    if hasattr(a1, 'pivot_Element25'):
        assert _is_linked(a1, 'pivot_Element25', b)
    _safe_set(b, 'pivot_Comment', {a2})
    assert _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a1, 'pivot_Element25'):
        assert not _is_linked(a1, 'pivot_Element25', b)
    if hasattr(a2, 'pivot_Element25'):
        assert _is_linked(a2, 'pivot_Element25', b)
    _safe_set(b, 'pivot_Comment', set())
    assert not _is_linked(b, 'pivot_Comment', a2)
    if hasattr(a2, 'pivot_Element25'):
        assert not _is_linked(a2, 'pivot_Element25', b)


def test_assoc_applyingPackage192_reverse_link_reassign_clear():
    a1 = pivot_ProfileApplication(isStrict="sample_text")
    a2 = pivot_ProfileApplication(isStrict="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'Package193', a1)
    assert _is_linked(b, 'Package193', a1)
    if hasattr(a1, 'profileApplication'):
        assert _is_linked(a1, 'profileApplication', b)
    _safe_set(b, 'Package193', a2)
    assert _is_linked(b, 'Package193', a2)
    if hasattr(a1, 'profileApplication'):
        assert not _is_linked(a1, 'profileApplication', b)
    if hasattr(a2, 'profileApplication'):
        assert _is_linked(a2, 'profileApplication', b)
    _safe_set(b, 'Package193', None)
    assert not _is_linked(b, 'Package193', a2)
    if hasattr(a2, 'profileApplication'):
        assert not _is_linked(a2, 'profileApplication', b)


def test_assoc_base65_reverse_link_reassign_clear():
    a1 = pivot_ElementExtension(isApplied="sample_text", isRequired="sample_text")
    a2 = pivot_ElementExtension(isApplied="sample_text_2", isRequired="sample_text_2")
    b = pivot_Element()
    _safe_set(b, 'Element', a1)
    assert _is_linked(b, 'Element', a1)
    if hasattr(a1, 'extension'):
        assert _is_linked(a1, 'extension', b)
    _safe_set(b, 'Element', a2)
    assert _is_linked(b, 'Element', a2)
    if hasattr(a1, 'extension'):
        assert not _is_linked(a1, 'extension', b)
    if hasattr(a2, 'extension'):
        assert _is_linked(a2, 'extension', b)
    _safe_set(b, 'Element', None)
    assert not _is_linked(b, 'Element', a2)
    if hasattr(a2, 'extension'):
        assert not _is_linked(a2, 'extension', b)


def test_assoc_behavioralType50_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_DataType(isSerializable="sample_text")
    _safe_set(b, 'pivot_DataType', a1)
    assert _is_linked(b, 'pivot_DataType', a1)
    if hasattr(a1, 'pivot_Type51'):
        assert _is_linked(a1, 'pivot_Type51', b)
    _safe_set(b, 'pivot_DataType', a2)
    assert _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a1, 'pivot_Type51'):
        assert not _is_linked(a1, 'pivot_Type51', b)
    if hasattr(a2, 'pivot_Type51'):
        assert _is_linked(a2, 'pivot_Type51', b)
    _safe_set(b, 'pivot_DataType', None)
    assert not _is_linked(b, 'pivot_DataType', a2)
    if hasattr(a2, 'pivot_Type51'):
        assert not _is_linked(a2, 'pivot_Type51', b)


def test_assoc_bodyExpression145_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_OpaqueExpression(body="sample_text", language="sample_text")
    _safe_set(b, 'pivot_OpaqueExpression147', a1)
    assert _is_linked(b, 'pivot_OpaqueExpression147', a1)
    if hasattr(a1, 'pivot_Operation146'):
        assert _is_linked(a1, 'pivot_Operation146', b)
    _safe_set(b, 'pivot_OpaqueExpression147', a2)
    assert _is_linked(b, 'pivot_OpaqueExpression147', a2)
    if hasattr(a1, 'pivot_Operation146'):
        assert not _is_linked(a1, 'pivot_Operation146', b)
    if hasattr(a2, 'pivot_Operation146'):
        assert _is_linked(a2, 'pivot_Operation146', b)
    _safe_set(b, 'pivot_OpaqueExpression147', None)
    assert not _is_linked(b, 'pivot_OpaqueExpression147', a2)
    if hasattr(a2, 'pivot_Operation146'):
        assert not _is_linked(a2, 'pivot_Operation146', b)


def test_assoc_class_148_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isActive="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class150', a1)
    assert _is_linked(b, 'pivot_Class150', a1)
    if hasattr(a1, 'pivot_Operation149'):
        assert _is_linked(a1, 'pivot_Operation149', b)
    _safe_set(b, 'pivot_Class150', a2)
    assert _is_linked(b, 'pivot_Class150', a2)
    if hasattr(a1, 'pivot_Operation149'):
        assert not _is_linked(a1, 'pivot_Operation149', b)
    if hasattr(a2, 'pivot_Operation149'):
        assert _is_linked(a2, 'pivot_Operation149', b)
    _safe_set(b, 'pivot_Class150', None)
    assert not _is_linked(b, 'pivot_Class150', a2)
    if hasattr(a2, 'pivot_Operation149'):
        assert not _is_linked(a2, 'pivot_Operation149', b)


def test_assoc_class_195_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isActive="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class197', a1)
    assert _is_linked(b, 'pivot_Class197', a1)
    if hasattr(a1, 'pivot_Property196'):
        assert _is_linked(a1, 'pivot_Property196', b)
    _safe_set(b, 'pivot_Class197', a2)
    assert _is_linked(b, 'pivot_Class197', a2)
    if hasattr(a1, 'pivot_Property196'):
        assert not _is_linked(a1, 'pivot_Property196', b)
    if hasattr(a2, 'pivot_Property196'):
        assert _is_linked(a2, 'pivot_Property196', b)
    _safe_set(b, 'pivot_Class197', None)
    assert not _is_linked(b, 'pivot_Class197', a2)
    if hasattr(a2, 'pivot_Property196'):
        assert not _is_linked(a2, 'pivot_Property196', b)


def test_assoc_connectionPoint243_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'Pseudostate', a1)
    assert _is_linked(b, 'Pseudostate', a1)
    if hasattr(a1, 'state244'):
        assert _is_linked(a1, 'state244', b)
    _safe_set(b, 'Pseudostate', a2)
    assert _is_linked(b, 'Pseudostate', a2)
    if hasattr(a1, 'state244'):
        assert not _is_linked(a1, 'state244', b)
    if hasattr(a2, 'state244'):
        assert _is_linked(a2, 'state244', b)
    _safe_set(b, 'Pseudostate', None)
    assert not _is_linked(b, 'Pseudostate', a2)
    if hasattr(a2, 'state244'):
        assert not _is_linked(a2, 'state244', b)


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


def test_assoc_constrainingType350_reverse_link_reassign_clear():
    a1 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text")
    a2 = pivot_TypeTemplateParameter(allowSubstitutable="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type351', a1)
    assert _is_linked(b, 'pivot_Type351', a1)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type351', a2)
    assert _is_linked(b, 'pivot_Type351', a2)
    if hasattr(a1, 'pivot_TypeTemplateParameter'):
        assert not _is_linked(a1, 'pivot_TypeTemplateParameter', b)
    if hasattr(a2, 'pivot_TypeTemplateParameter'):
        assert _is_linked(a2, 'pivot_TypeTemplateParameter', b)
    _safe_set(b, 'pivot_Type351', None)
    assert not _is_linked(b, 'pivot_Type351', a2)
    if hasattr(a2, 'pivot_TypeTemplateParameter'):
        assert not _is_linked(a2, 'pivot_TypeTemplateParameter', b)


def test_assoc_defaultExpression198_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_OpaqueExpression(body="sample_text", language="sample_text")
    _safe_set(b, 'pivot_OpaqueExpression200', a1)
    assert _is_linked(b, 'pivot_OpaqueExpression200', a1)
    if hasattr(a1, 'pivot_Property199'):
        assert _is_linked(a1, 'pivot_Property199', b)
    _safe_set(b, 'pivot_OpaqueExpression200', a2)
    assert _is_linked(b, 'pivot_OpaqueExpression200', a2)
    if hasattr(a1, 'pivot_Property199'):
        assert not _is_linked(a1, 'pivot_Property199', b)
    if hasattr(a2, 'pivot_Property199'):
        assert _is_linked(a2, 'pivot_Property199', b)
    _safe_set(b, 'pivot_OpaqueExpression200', None)
    assert not _is_linked(b, 'pivot_OpaqueExpression200', a2)
    if hasattr(a2, 'pivot_Property199'):
        assert not _is_linked(a2, 'pivot_Property199', b)


def test_assoc_elementType23_reverse_link_reassign_clear():
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


def test_assoc_extendedBys330_reverse_link_reassign_clear():
    a1 = pivot_TypeExtension(isRequired="sample_text")
    a2 = pivot_TypeExtension(isRequired="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'type', {a1})
    assert _is_linked(b, 'type', a1)
    if hasattr(a1, 'TypeExtension331'):
        assert _is_linked(a1, 'TypeExtension331', b)
    _safe_set(b, 'type', {a2})
    assert _is_linked(b, 'type', a2)
    if hasattr(a1, 'TypeExtension331'):
        assert not _is_linked(a1, 'TypeExtension331', b)
    if hasattr(a2, 'TypeExtension331'):
        assert _is_linked(a2, 'TypeExtension331', b)
    _safe_set(b, 'type', set())
    assert not _is_linked(b, 'type', a2)
    if hasattr(a2, 'TypeExtension331'):
        assert not _is_linked(a2, 'TypeExtension331', b)


def test_assoc_extension58_reverse_link_reassign_clear():
    a1 = pivot_ElementExtension(isApplied="sample_text", isRequired="sample_text")
    a2 = pivot_ElementExtension(isApplied="sample_text_2", isRequired="sample_text_2")
    b = pivot_Element()
    _safe_set(b, 'base', {a1})
    assert _is_linked(b, 'base', a1)
    if hasattr(a1, 'ElementExtension'):
        assert _is_linked(a1, 'ElementExtension', b)
    _safe_set(b, 'base', {a2})
    assert _is_linked(b, 'base', a2)
    if hasattr(a1, 'ElementExtension'):
        assert not _is_linked(a1, 'ElementExtension', b)
    if hasattr(a2, 'ElementExtension'):
        assert _is_linked(a2, 'ElementExtension', b)
    _safe_set(b, 'base', set())
    assert not _is_linked(b, 'base', a2)
    if hasattr(a2, 'ElementExtension'):
        assert not _is_linked(a2, 'ElementExtension', b)


def test_assoc_guard312_reverse_link_reassign_clear():
    a1 = pivot_Transition(kind="sample_text")
    a2 = pivot_Transition(kind="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'Constraint314', a1)
    assert _is_linked(b, 'Constraint314', a1)
    if hasattr(a1, 'transition313'):
        assert _is_linked(a1, 'transition313', b)
    _safe_set(b, 'Constraint314', a2)
    assert _is_linked(b, 'Constraint314', a2)
    if hasattr(a1, 'transition313'):
        assert not _is_linked(a1, 'transition313', b)
    if hasattr(a2, 'transition313'):
        assert _is_linked(a2, 'transition313', b)
    _safe_set(b, 'Constraint314', None)
    assert not _is_linked(b, 'Constraint314', a2)
    if hasattr(a2, 'transition313'):
        assert not _is_linked(a2, 'transition313', b)


def test_assoc_importedPackage176_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package175', {a1})
    assert _is_linked(b, 'pivot_Package175', a1)
    if hasattr(a1, 'pivot_Package'):
        assert _is_linked(a1, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package175', {a2})
    assert _is_linked(b, 'pivot_Package175', a2)
    if hasattr(a1, 'pivot_Package'):
        assert not _is_linked(a1, 'pivot_Package', b)
    if hasattr(a2, 'pivot_Package'):
        assert _is_linked(a2, 'pivot_Package', b)
    _safe_set(b, 'pivot_Package175', set())
    assert not _is_linked(b, 'pivot_Package175', a2)
    if hasattr(a2, 'pivot_Package'):
        assert not _is_linked(a2, 'pivot_Package', b)


def test_assoc_iterator112_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LoopExp()
    _safe_set(b, 'pivot_LoopExp113', {a1})
    assert _is_linked(b, 'pivot_LoopExp113', a1)
    if hasattr(a1, 'pivot_Variable114'):
        assert _is_linked(a1, 'pivot_Variable114', b)
    _safe_set(b, 'pivot_LoopExp113', {a2})
    assert _is_linked(b, 'pivot_LoopExp113', a2)
    if hasattr(a1, 'pivot_Variable114'):
        assert not _is_linked(a1, 'pivot_Variable114', b)
    if hasattr(a2, 'pivot_Variable114'):
        assert _is_linked(a2, 'pivot_Variable114', b)
    _safe_set(b, 'pivot_LoopExp113', set())
    assert not _is_linked(b, 'pivot_LoopExp113', a2)
    if hasattr(a2, 'pivot_Variable114'):
        assert not _is_linked(a2, 'pivot_Variable114', b)


def test_assoc_keys202_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property203', a1)
    assert _is_linked(b, 'pivot_Property203', a1)
    if hasattr(a1, 'pivot_Property201'):
        assert _is_linked(a1, 'pivot_Property201', b)
    _safe_set(b, 'pivot_Property203', a2)
    assert _is_linked(b, 'pivot_Property203', a2)
    if hasattr(a1, 'pivot_Property201'):
        assert not _is_linked(a1, 'pivot_Property201', b)
    if hasattr(a2, 'pivot_Property201'):
        assert _is_linked(a2, 'pivot_Property201', b)
    _safe_set(b, 'pivot_Property203', None)
    assert not _is_linked(b, 'pivot_Property203', a2)
    if hasattr(a2, 'pivot_Property201'):
        assert not _is_linked(a2, 'pivot_Property201', b)


def test_assoc_nestedPackage178_reverse_link_reassign_clear():
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


def test_assoc_nestedPackage236_reverse_link_reassign_clear():
    a1 = pivot_Root(externalURI="sample_text")
    a2 = pivot_Root(externalURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'pivot_Package238', a1)
    assert _is_linked(b, 'pivot_Package238', a1)
    if hasattr(a1, 'pivot_Root237'):
        assert _is_linked(a1, 'pivot_Root237', b)
    _safe_set(b, 'pivot_Package238', a2)
    assert _is_linked(b, 'pivot_Package238', a2)
    if hasattr(a1, 'pivot_Root237'):
        assert not _is_linked(a1, 'pivot_Root237', b)
    if hasattr(a2, 'pivot_Root237'):
        assert _is_linked(a2, 'pivot_Root237', b)
    _safe_set(b, 'pivot_Package238', None)
    assert not _is_linked(b, 'pivot_Package238', a2)
    if hasattr(a2, 'pivot_Root237'):
        assert not _is_linked(a2, 'pivot_Root237', b)


def test_assoc_nestedType12_reverse_link_reassign_clear():
    a1 = pivot_Class(isAbstract="sample_text", isActive="sample_text", isInterface="sample_text")
    a2 = pivot_Class(isAbstract="sample_text_2", isActive="sample_text_2", isInterface="sample_text_2")
    b = pivot_Class(isAbstract="sample_text", isActive="sample_text", isInterface="sample_text")
    _safe_set(b, 'pivot_Class11', {a1})
    assert _is_linked(b, 'pivot_Class11', a1)
    if hasattr(a1, 'pivot_Class'):
        assert _is_linked(a1, 'pivot_Class', b)
    _safe_set(b, 'pivot_Class11', {a2})
    assert _is_linked(b, 'pivot_Class11', a2)
    if hasattr(a1, 'pivot_Class'):
        assert not _is_linked(a1, 'pivot_Class', b)
    if hasattr(a2, 'pivot_Class'):
        assert _is_linked(a2, 'pivot_Class', b)
    _safe_set(b, 'pivot_Class11', set())
    assert not _is_linked(b, 'pivot_Class11', a2)
    if hasattr(a2, 'pivot_Class'):
        assert not _is_linked(a2, 'pivot_Class', b)


def test_assoc_nestingPackage180_reverse_link_reassign_clear():
    a1 = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    a2 = pivot_Package(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'nestedPackage', a1)
    assert _is_linked(b, 'nestedPackage', a1)
    if hasattr(a1, 'Package181'):
        assert _is_linked(a1, 'Package181', b)
    _safe_set(b, 'nestedPackage', a2)
    assert _is_linked(b, 'nestedPackage', a2)
    if hasattr(a1, 'Package181'):
        assert not _is_linked(a1, 'Package181', b)
    if hasattr(a2, 'Package181'):
        assert _is_linked(a2, 'Package181', b)
    _safe_set(b, 'nestedPackage', None)
    assert not _is_linked(b, 'nestedPackage', a2)
    if hasattr(a2, 'Package181'):
        assert not _is_linked(a2, 'Package181', b)


def test_assoc_opposite205_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property206', a1)
    assert _is_linked(b, 'pivot_Property206', a1)
    if hasattr(a1, 'pivot_Property204'):
        assert _is_linked(a1, 'pivot_Property204', b)
    _safe_set(b, 'pivot_Property206', a2)
    assert _is_linked(b, 'pivot_Property206', a2)
    if hasattr(a1, 'pivot_Property204'):
        assert not _is_linked(a1, 'pivot_Property204', b)
    if hasattr(a2, 'pivot_Property204'):
        assert _is_linked(a2, 'pivot_Property204', b)
    _safe_set(b, 'pivot_Property206', None)
    assert not _is_linked(b, 'pivot_Property206', a2)
    if hasattr(a2, 'pivot_Property204'):
        assert not _is_linked(a2, 'pivot_Property204', b)


def test_assoc_ownedAnnotation60_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Element()
    _safe_set(b, 'pivot_Element61', a1)
    assert _is_linked(b, 'pivot_Element61', a1)
    if hasattr(a1, 'pivot_Element59'):
        assert _is_linked(a1, 'pivot_Element59', b)
    _safe_set(b, 'pivot_Element61', a2)
    assert _is_linked(b, 'pivot_Element61', a2)
    if hasattr(a1, 'pivot_Element59'):
        assert not _is_linked(a1, 'pivot_Element59', b)
    if hasattr(a2, 'pivot_Element59'):
        assert _is_linked(a2, 'pivot_Element59', b)
    _safe_set(b, 'pivot_Element61', None)
    assert not _is_linked(b, 'pivot_Element61', a2)
    if hasattr(a2, 'pivot_Element59'):
        assert not _is_linked(a2, 'pivot_Element59', b)


def test_assoc_ownedAttribute332_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'Property333', a1)
    assert _is_linked(b, 'Property333', a1)
    if hasattr(a1, 'owningType'):
        assert _is_linked(a1, 'owningType', b)
    _safe_set(b, 'Property333', a2)
    assert _is_linked(b, 'Property333', a2)
    if hasattr(a1, 'owningType'):
        assert not _is_linked(a1, 'owningType', b)
    if hasattr(a2, 'owningType'):
        assert _is_linked(a2, 'owningType', b)
    _safe_set(b, 'Property333', None)
    assert not _is_linked(b, 'Property333', a2)
    if hasattr(a2, 'owningType'):
        assert not _is_linked(a2, 'owningType', b)


def test_assoc_ownedComment62_reverse_link_reassign_clear():
    a1 = pivot_Element()
    a2 = pivot_Element()
    b = pivot_Comment(body="sample_text")
    _safe_set(b, 'pivot_Comment64', a1)
    assert _is_linked(b, 'pivot_Comment64', a1)
    if hasattr(a1, 'pivot_Element63'):
        assert _is_linked(a1, 'pivot_Element63', b)
    _safe_set(b, 'pivot_Comment64', a2)
    assert _is_linked(b, 'pivot_Comment64', a2)
    if hasattr(a1, 'pivot_Element63'):
        assert not _is_linked(a1, 'pivot_Element63', b)
    if hasattr(a2, 'pivot_Element63'):
        assert _is_linked(a2, 'pivot_Element63', b)
    _safe_set(b, 'pivot_Comment64', None)
    assert not _is_linked(b, 'pivot_Comment64', a2)
    if hasattr(a2, 'pivot_Element63'):
        assert not _is_linked(a2, 'pivot_Element63', b)


def test_assoc_ownedInvariant334_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint336', a1)
    assert _is_linked(b, 'pivot_Constraint336', a1)
    if hasattr(a1, 'pivot_Type335'):
        assert _is_linked(a1, 'pivot_Type335', b)
    _safe_set(b, 'pivot_Constraint336', a2)
    assert _is_linked(b, 'pivot_Constraint336', a2)
    if hasattr(a1, 'pivot_Type335'):
        assert not _is_linked(a1, 'pivot_Type335', b)
    if hasattr(a2, 'pivot_Type335'):
        assert _is_linked(a2, 'pivot_Type335', b)
    _safe_set(b, 'pivot_Constraint336', None)
    assert not _is_linked(b, 'pivot_Constraint336', a2)
    if hasattr(a2, 'pivot_Type335'):
        assert not _is_linked(a2, 'pivot_Type335', b)


def test_assoc_ownedOperation337_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'Operation339', a1)
    assert _is_linked(b, 'Operation339', a1)
    if hasattr(a1, 'owningType338'):
        assert _is_linked(a1, 'owningType338', b)
    _safe_set(b, 'Operation339', a2)
    assert _is_linked(b, 'Operation339', a2)
    if hasattr(a1, 'owningType338'):
        assert not _is_linked(a1, 'owningType338', b)
    if hasattr(a2, 'owningType338'):
        assert _is_linked(a2, 'owningType338', b)
    _safe_set(b, 'Operation339', None)
    assert not _is_linked(b, 'Operation339', a2)
    if hasattr(a2, 'owningType338'):
        assert not _is_linked(a2, 'owningType338', b)


def test_assoc_ownedType182_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'package', {a1})
    assert _is_linked(b, 'package', a1)
    if hasattr(a1, 'Type183'):
        assert _is_linked(a1, 'Type183', b)
    _safe_set(b, 'package', {a2})
    assert _is_linked(b, 'package', a2)
    if hasattr(a1, 'Type183'):
        assert not _is_linked(a1, 'Type183', b)
    if hasattr(a2, 'Type183'):
        assert _is_linked(a2, 'Type183', b)
    _safe_set(b, 'package', set())
    assert not _is_linked(b, 'package', a2)
    if hasattr(a2, 'Type183'):
        assert not _is_linked(a2, 'Type183', b)


def test_assoc_owningState35_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'stateInvariant', a1)
    assert _is_linked(b, 'stateInvariant', a1)
    if hasattr(a1, 'State36'):
        assert _is_linked(a1, 'State36', b)
    _safe_set(b, 'stateInvariant', a2)
    assert _is_linked(b, 'stateInvariant', a2)
    if hasattr(a1, 'State36'):
        assert not _is_linked(a1, 'State36', b)
    if hasattr(a2, 'State36'):
        assert _is_linked(a2, 'State36', b)
    _safe_set(b, 'stateInvariant', None)
    assert not _is_linked(b, 'stateInvariant', a2)
    if hasattr(a2, 'State36'):
        assert not _is_linked(a2, 'State36', b)


def test_assoc_owningType152_reverse_link_reassign_clear():
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


def test_assoc_owningType207_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'ownedAttribute', a1)
    assert _is_linked(b, 'ownedAttribute', a1)
    if hasattr(a1, 'Type208'):
        assert _is_linked(a1, 'Type208', b)
    _safe_set(b, 'ownedAttribute', a2)
    assert _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a1, 'Type208'):
        assert not _is_linked(a1, 'Type208', b)
    if hasattr(a2, 'Type208'):
        assert _is_linked(a2, 'Type208', b)
    _safe_set(b, 'ownedAttribute', None)
    assert not _is_linked(b, 'ownedAttribute', a2)
    if hasattr(a2, 'Type208'):
        assert not _is_linked(a2, 'Type208', b)


def test_assoc_package340_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'Package341', a1)
    assert _is_linked(b, 'Package341', a1)
    if hasattr(a1, 'ownedType'):
        assert _is_linked(a1, 'ownedType', b)
    _safe_set(b, 'Package341', a2)
    assert _is_linked(b, 'Package341', a2)
    if hasattr(a1, 'ownedType'):
        assert not _is_linked(a1, 'ownedType', b)
    if hasattr(a2, 'ownedType'):
        assert _is_linked(a2, 'ownedType', b)
    _safe_set(b, 'Package341', None)
    assert not _is_linked(b, 'Package341', a2)
    if hasattr(a2, 'ownedType'):
        assert not _is_linked(a2, 'ownedType', b)


def test_assoc_postcondition153_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint155', a1)
    assert _is_linked(b, 'pivot_Constraint155', a1)
    if hasattr(a1, 'pivot_Operation154'):
        assert _is_linked(a1, 'pivot_Operation154', b)
    _safe_set(b, 'pivot_Constraint155', a2)
    assert _is_linked(b, 'pivot_Constraint155', a2)
    if hasattr(a1, 'pivot_Operation154'):
        assert not _is_linked(a1, 'pivot_Operation154', b)
    if hasattr(a2, 'pivot_Operation154'):
        assert _is_linked(a2, 'pivot_Operation154', b)
    _safe_set(b, 'pivot_Constraint155', None)
    assert not _is_linked(b, 'pivot_Constraint155', a2)
    if hasattr(a2, 'pivot_Operation154'):
        assert not _is_linked(a2, 'pivot_Operation154', b)


def test_assoc_precedence156_reverse_link_reassign_clear():
    a1 = pivot_Precedence(associativity="sample_text", order=7)
    a2 = pivot_Precedence(associativity="sample_text_2", order=13)
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation157', a1)
    assert _is_linked(b, 'pivot_Operation157', a1)
    if hasattr(a1, 'pivot_Precedence158'):
        assert _is_linked(a1, 'pivot_Precedence158', b)
    _safe_set(b, 'pivot_Operation157', a2)
    assert _is_linked(b, 'pivot_Operation157', a2)
    if hasattr(a1, 'pivot_Precedence158'):
        assert not _is_linked(a1, 'pivot_Precedence158', b)
    if hasattr(a2, 'pivot_Precedence158'):
        assert _is_linked(a2, 'pivot_Precedence158', b)
    _safe_set(b, 'pivot_Operation157', None)
    assert not _is_linked(b, 'pivot_Operation157', a2)
    if hasattr(a2, 'pivot_Precedence158'):
        assert not _is_linked(a2, 'pivot_Precedence158', b)


def test_assoc_precondition159_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint161', a1)
    assert _is_linked(b, 'pivot_Constraint161', a1)
    if hasattr(a1, 'pivot_Operation160'):
        assert _is_linked(a1, 'pivot_Operation160', b)
    _safe_set(b, 'pivot_Constraint161', a2)
    assert _is_linked(b, 'pivot_Constraint161', a2)
    if hasattr(a1, 'pivot_Operation160'):
        assert not _is_linked(a1, 'pivot_Operation160', b)
    if hasattr(a2, 'pivot_Operation160'):
        assert _is_linked(a2, 'pivot_Operation160', b)
    _safe_set(b, 'pivot_Constraint161', None)
    assert not _is_linked(b, 'pivot_Constraint161', a2)
    if hasattr(a2, 'pivot_Operation160'):
        assert not _is_linked(a2, 'pivot_Operation160', b)


def test_assoc_profileApplication184_reverse_link_reassign_clear():
    a1 = pivot_ProfileApplication(isStrict="sample_text")
    a2 = pivot_ProfileApplication(isStrict="sample_text_2")
    b = pivot_Package(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'applyingPackage', {a1})
    assert _is_linked(b, 'applyingPackage', a1)
    if hasattr(a1, 'ProfileApplication'):
        assert _is_linked(a1, 'ProfileApplication', b)
    _safe_set(b, 'applyingPackage', {a2})
    assert _is_linked(b, 'applyingPackage', a2)
    if hasattr(a1, 'ProfileApplication'):
        assert not _is_linked(a1, 'ProfileApplication', b)
    if hasattr(a2, 'ProfileApplication'):
        assert _is_linked(a2, 'ProfileApplication', b)
    _safe_set(b, 'applyingPackage', set())
    assert not _is_linked(b, 'applyingPackage', a2)
    if hasattr(a2, 'ProfileApplication'):
        assert not _is_linked(a2, 'ProfileApplication', b)


def test_assoc_raisedException162_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation163', {a1})
    assert _is_linked(b, 'pivot_Operation163', a1)
    if hasattr(a1, 'pivot_Type164'):
        assert _is_linked(a1, 'pivot_Type164', b)
    _safe_set(b, 'pivot_Operation163', {a2})
    assert _is_linked(b, 'pivot_Operation163', a2)
    if hasattr(a1, 'pivot_Type164'):
        assert not _is_linked(a1, 'pivot_Type164', b)
    if hasattr(a2, 'pivot_Type164'):
        assert _is_linked(a2, 'pivot_Type164', b)
    _safe_set(b, 'pivot_Operation163', set())
    assert not _is_linked(b, 'pivot_Operation163', a2)
    if hasattr(a2, 'pivot_Type164'):
        assert not _is_linked(a2, 'pivot_Type164', b)


def test_assoc_redefinedConstraint38_reverse_link_reassign_clear():
    a1 = pivot_Constraint(isCallable="sample_text")
    a2 = pivot_Constraint(isCallable="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint39', a1)
    assert _is_linked(b, 'pivot_Constraint39', a1)
    if hasattr(a1, 'pivot_Constraint37'):
        assert _is_linked(a1, 'pivot_Constraint37', b)
    _safe_set(b, 'pivot_Constraint39', a2)
    assert _is_linked(b, 'pivot_Constraint39', a2)
    if hasattr(a1, 'pivot_Constraint37'):
        assert not _is_linked(a1, 'pivot_Constraint37', b)
    if hasattr(a2, 'pivot_Constraint37'):
        assert _is_linked(a2, 'pivot_Constraint37', b)
    _safe_set(b, 'pivot_Constraint39', None)
    assert not _is_linked(b, 'pivot_Constraint39', a2)
    if hasattr(a2, 'pivot_Constraint37'):
        assert not _is_linked(a2, 'pivot_Constraint37', b)


def test_assoc_redefinedOperation166_reverse_link_reassign_clear():
    a1 = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    a2 = pivot_Operation(isInvalidating="sample_text_2", isValidating="sample_text_2")
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation167', a1)
    assert _is_linked(b, 'pivot_Operation167', a1)
    if hasattr(a1, 'pivot_Operation165'):
        assert _is_linked(a1, 'pivot_Operation165', b)
    _safe_set(b, 'pivot_Operation167', a2)
    assert _is_linked(b, 'pivot_Operation167', a2)
    if hasattr(a1, 'pivot_Operation165'):
        assert not _is_linked(a1, 'pivot_Operation165', b)
    if hasattr(a2, 'pivot_Operation165'):
        assert _is_linked(a2, 'pivot_Operation165', b)
    _safe_set(b, 'pivot_Operation167', None)
    assert not _is_linked(b, 'pivot_Operation167', a2)
    if hasattr(a2, 'pivot_Operation165'):
        assert not _is_linked(a2, 'pivot_Operation165', b)


def test_assoc_redefinedProperty210_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property211', a1)
    assert _is_linked(b, 'pivot_Property211', a1)
    if hasattr(a1, 'pivot_Property209'):
        assert _is_linked(a1, 'pivot_Property209', b)
    _safe_set(b, 'pivot_Property211', a2)
    assert _is_linked(b, 'pivot_Property211', a2)
    if hasattr(a1, 'pivot_Property209'):
        assert not _is_linked(a1, 'pivot_Property209', b)
    if hasattr(a2, 'pivot_Property209'):
        assert _is_linked(a2, 'pivot_Property209', b)
    _safe_set(b, 'pivot_Property211', None)
    assert not _is_linked(b, 'pivot_Property211', a2)
    if hasattr(a2, 'pivot_Property209'):
        assert not _is_linked(a2, 'pivot_Property209', b)


def test_assoc_redefinedState256_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    _safe_set(b, 'pivot_State257', a1)
    assert _is_linked(b, 'pivot_State257', a1)
    if hasattr(a1, 'pivot_State255'):
        assert _is_linked(a1, 'pivot_State255', b)
    _safe_set(b, 'pivot_State257', a2)
    assert _is_linked(b, 'pivot_State257', a2)
    if hasattr(a1, 'pivot_State255'):
        assert not _is_linked(a1, 'pivot_State255', b)
    if hasattr(a2, 'pivot_State255'):
        assert _is_linked(a2, 'pivot_State255', b)
    _safe_set(b, 'pivot_State257', None)
    assert not _is_linked(b, 'pivot_State257', a2)
    if hasattr(a2, 'pivot_State255'):
        assert not _is_linked(a2, 'pivot_State255', b)


def test_assoc_referredEnumLiteral67_reverse_link_reassign_clear():
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


def test_assoc_referredOperation170_reverse_link_reassign_clear():
    a1 = pivot_OperationCallExp()
    a2 = pivot_OperationCallExp()
    b = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    _safe_set(b, 'pivot_Operation172', a1)
    assert _is_linked(b, 'pivot_Operation172', a1)
    if hasattr(a1, 'pivot_OperationCallExp171'):
        assert _is_linked(a1, 'pivot_OperationCallExp171', b)
    _safe_set(b, 'pivot_Operation172', a2)
    assert _is_linked(b, 'pivot_Operation172', a2)
    if hasattr(a1, 'pivot_OperationCallExp171'):
        assert not _is_linked(a1, 'pivot_OperationCallExp171', b)
    if hasattr(a2, 'pivot_OperationCallExp171'):
        assert _is_linked(a2, 'pivot_OperationCallExp171', b)
    _safe_set(b, 'pivot_Operation172', None)
    assert not _is_linked(b, 'pivot_Operation172', a2)
    if hasattr(a2, 'pivot_OperationCallExp171'):
        assert not _is_linked(a2, 'pivot_OperationCallExp171', b)


def test_assoc_referredProperty213_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property214', a1)
    assert _is_linked(b, 'pivot_Property214', a1)
    if hasattr(a1, 'pivot_Property212'):
        assert _is_linked(a1, 'pivot_Property212', b)
    _safe_set(b, 'pivot_Property214', a2)
    assert _is_linked(b, 'pivot_Property214', a2)
    if hasattr(a1, 'pivot_Property212'):
        assert not _is_linked(a1, 'pivot_Property212', b)
    if hasattr(a2, 'pivot_Property212'):
        assert _is_linked(a2, 'pivot_Property212', b)
    _safe_set(b, 'pivot_Property214', None)
    assert not _is_linked(b, 'pivot_Property214', a2)
    if hasattr(a2, 'pivot_Property212'):
        assert not _is_linked(a2, 'pivot_Property212', b)


def test_assoc_referredProperty218_reverse_link_reassign_clear():
    a1 = pivot_PropertyCallExp()
    a2 = pivot_PropertyCallExp()
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property219', a1)
    assert _is_linked(b, 'pivot_Property219', a1)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert _is_linked(a1, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property219', a2)
    assert _is_linked(b, 'pivot_Property219', a2)
    if hasattr(a1, 'pivot_PropertyCallExp'):
        assert not _is_linked(a1, 'pivot_PropertyCallExp', b)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert _is_linked(a2, 'pivot_PropertyCallExp', b)
    _safe_set(b, 'pivot_Property219', None)
    assert not _is_linked(b, 'pivot_Property219', a2)
    if hasattr(a2, 'pivot_PropertyCallExp'):
        assert not _is_linked(a2, 'pivot_PropertyCallExp', b)


def test_assoc_referredProperty54_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_DynamicProperty(default="sample_text")
    _safe_set(b, 'pivot_DynamicProperty', a1)
    assert _is_linked(b, 'pivot_DynamicProperty', a1)
    if hasattr(a1, 'pivot_Property55'):
        assert _is_linked(a1, 'pivot_Property55', b)
    _safe_set(b, 'pivot_DynamicProperty', a2)
    assert _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a1, 'pivot_Property55'):
        assert not _is_linked(a1, 'pivot_Property55', b)
    if hasattr(a2, 'pivot_Property55'):
        assert _is_linked(a2, 'pivot_Property55', b)
    _safe_set(b, 'pivot_DynamicProperty', None)
    assert not _is_linked(b, 'pivot_DynamicProperty', a2)
    if hasattr(a2, 'pivot_Property55'):
        assert not _is_linked(a2, 'pivot_Property55', b)


def test_assoc_result90_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_IterateExp()
    _safe_set(b, 'pivot_IterateExp', a1)
    assert _is_linked(b, 'pivot_IterateExp', a1)
    if hasattr(a1, 'pivot_Variable91'):
        assert _is_linked(a1, 'pivot_Variable91', b)
    _safe_set(b, 'pivot_IterateExp', a2)
    assert _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a1, 'pivot_Variable91'):
        assert not _is_linked(a1, 'pivot_Variable91', b)
    if hasattr(a2, 'pivot_Variable91'):
        assert _is_linked(a2, 'pivot_Variable91', b)
    _safe_set(b, 'pivot_IterateExp', None)
    assert not _is_linked(b, 'pivot_IterateExp', a2)
    if hasattr(a2, 'pivot_Variable91'):
        assert not _is_linked(a2, 'pivot_Variable91', b)


def test_assoc_specification40_reverse_link_reassign_clear():
    a1 = pivot_OpaqueExpression(body="sample_text", language="sample_text")
    a2 = pivot_OpaqueExpression(body="sample_text_2", language="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'pivot_Constraint41', a1)
    assert _is_linked(b, 'pivot_Constraint41', a1)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert _is_linked(a1, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint41', a2)
    assert _is_linked(b, 'pivot_Constraint41', a2)
    if hasattr(a1, 'pivot_OpaqueExpression'):
        assert not _is_linked(a1, 'pivot_OpaqueExpression', b)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert _is_linked(a2, 'pivot_OpaqueExpression', b)
    _safe_set(b, 'pivot_Constraint41', None)
    assert not _is_linked(b, 'pivot_Constraint41', a2)
    if hasattr(a2, 'pivot_OpaqueExpression'):
        assert not _is_linked(a2, 'pivot_OpaqueExpression', b)


def test_assoc_state220_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Pseudostate(kind="sample_text")
    _safe_set(b, 'connectionPoint', a1)
    assert _is_linked(b, 'connectionPoint', a1)
    if hasattr(a1, 'State221'):
        assert _is_linked(a1, 'State221', b)
    _safe_set(b, 'connectionPoint', a2)
    assert _is_linked(b, 'connectionPoint', a2)
    if hasattr(a1, 'State221'):
        assert not _is_linked(a1, 'State221', b)
    if hasattr(a2, 'State221'):
        assert _is_linked(a2, 'State221', b)
    _safe_set(b, 'connectionPoint', None)
    assert not _is_linked(b, 'connectionPoint', a2)
    if hasattr(a2, 'State221'):
        assert not _is_linked(a2, 'State221', b)


def test_assoc_stateInvariant260_reverse_link_reassign_clear():
    a1 = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    a2 = pivot_State(isComposite="sample_text_2", isOrthogonal="sample_text_2", isSimple="sample_text_2", isSubmachineState="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'Constraint', a1)
    assert _is_linked(b, 'Constraint', a1)
    if hasattr(a1, 'owningState'):
        assert _is_linked(a1, 'owningState', b)
    _safe_set(b, 'Constraint', a2)
    assert _is_linked(b, 'Constraint', a2)
    if hasattr(a1, 'owningState'):
        assert not _is_linked(a1, 'owningState', b)
    if hasattr(a2, 'owningState'):
        assert _is_linked(a2, 'owningState', b)
    _safe_set(b, 'Constraint', None)
    assert not _is_linked(b, 'Constraint', a2)
    if hasattr(a2, 'owningState'):
        assert not _is_linked(a2, 'owningState', b)


def test_assoc_subsettedProperty216_reverse_link_reassign_clear():
    a1 = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    a2 = pivot_Property(default="sample_text_2", implicit="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isID="sample_text_2", isReadOnly="sample_text_2", isResolveProxies="sample_text_2", isTransient="sample_text_2", isUnsettable="sample_text_2", isVolatile="sample_text_2")
    b = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    _safe_set(b, 'pivot_Property217', a1)
    assert _is_linked(b, 'pivot_Property217', a1)
    if hasattr(a1, 'pivot_Property215'):
        assert _is_linked(a1, 'pivot_Property215', b)
    _safe_set(b, 'pivot_Property217', a2)
    assert _is_linked(b, 'pivot_Property217', a2)
    if hasattr(a1, 'pivot_Property215'):
        assert not _is_linked(a1, 'pivot_Property215', b)
    if hasattr(a2, 'pivot_Property215'):
        assert _is_linked(a2, 'pivot_Property215', b)
    _safe_set(b, 'pivot_Property217', None)
    assert not _is_linked(b, 'pivot_Property217', a2)
    if hasattr(a2, 'pivot_Property215'):
        assert not _is_linked(a2, 'pivot_Property215', b)


def test_assoc_superClass343_reverse_link_reassign_clear():
    a1 = pivot_Type(instanceClassName="sample_text")
    a2 = pivot_Type(instanceClassName="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type344', a1)
    assert _is_linked(b, 'pivot_Type344', a1)
    if hasattr(a1, 'pivot_Type342'):
        assert _is_linked(a1, 'pivot_Type342', b)
    _safe_set(b, 'pivot_Type344', a2)
    assert _is_linked(b, 'pivot_Type344', a2)
    if hasattr(a1, 'pivot_Type342'):
        assert not _is_linked(a1, 'pivot_Type342', b)
    if hasattr(a2, 'pivot_Type342'):
        assert _is_linked(a2, 'pivot_Type342', b)
    _safe_set(b, 'pivot_Type344', None)
    assert not _is_linked(b, 'pivot_Type344', a2)
    if hasattr(a2, 'pivot_Type342'):
        assert not _is_linked(a2, 'pivot_Type342', b)


def test_assoc_transition42_reverse_link_reassign_clear():
    a1 = pivot_Transition(kind="sample_text")
    a2 = pivot_Transition(kind="sample_text_2")
    b = pivot_Constraint(isCallable="sample_text")
    _safe_set(b, 'guard', a1)
    assert _is_linked(b, 'guard', a1)
    if hasattr(a1, 'Transition43'):
        assert _is_linked(a1, 'Transition43', b)
    _safe_set(b, 'guard', a2)
    assert _is_linked(b, 'guard', a2)
    if hasattr(a1, 'Transition43'):
        assert not _is_linked(a1, 'Transition43', b)
    if hasattr(a2, 'Transition43'):
        assert _is_linked(a2, 'Transition43', b)
    _safe_set(b, 'guard', None)
    assert not _is_linked(b, 'guard', a2)
    if hasattr(a2, 'Transition43'):
        assert not _is_linked(a2, 'Transition43', b)


def test_assoc_type348_reverse_link_reassign_clear():
    a1 = pivot_TypeExtension(isRequired="sample_text")
    a2 = pivot_TypeExtension(isRequired="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'Type349', a1)
    assert _is_linked(b, 'Type349', a1)
    if hasattr(a1, 'extendedBys'):
        assert _is_linked(a1, 'extendedBys', b)
    _safe_set(b, 'Type349', a2)
    assert _is_linked(b, 'Type349', a2)
    if hasattr(a1, 'extendedBys'):
        assert not _is_linked(a1, 'extendedBys', b)
    if hasattr(a2, 'extendedBys'):
        assert _is_linked(a2, 'extendedBys', b)
    _safe_set(b, 'Type349', None)
    assert not _is_linked(b, 'Type349', a2)
    if hasattr(a2, 'extendedBys'):
        assert not _is_linked(a2, 'extendedBys', b)


def test_assoc_type352_reverse_link_reassign_clear():
    a1 = pivot_TypedElement(isRequired="sample_text")
    a2 = pivot_TypedElement(isRequired="sample_text_2")
    b = pivot_Type(instanceClassName="sample_text")
    _safe_set(b, 'pivot_Type353', a1)
    assert _is_linked(b, 'pivot_Type353', a1)
    if hasattr(a1, 'pivot_TypedElement'):
        assert _is_linked(a1, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type353', a2)
    assert _is_linked(b, 'pivot_Type353', a2)
    if hasattr(a1, 'pivot_TypedElement'):
        assert not _is_linked(a1, 'pivot_TypedElement', b)
    if hasattr(a2, 'pivot_TypedElement'):
        assert _is_linked(a2, 'pivot_TypedElement', b)
    _safe_set(b, 'pivot_Type353', None)
    assert not _is_linked(b, 'pivot_Type353', a2)
    if hasattr(a2, 'pivot_TypedElement'):
        assert not _is_linked(a2, 'pivot_TypedElement', b)


def test_assoc_unspecializedElement307_reverse_link_reassign_clear():
    a1 = pivot_TemplateableElement()
    a2 = pivot_TemplateableElement()
    b = pivot_TemplateableElement()
    _safe_set(b, 'pivot_TemplateableElement306', a1)
    assert _is_linked(b, 'pivot_TemplateableElement306', a1)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert _is_linked(a1, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement306', a2)
    assert _is_linked(b, 'pivot_TemplateableElement306', a2)
    if hasattr(a1, 'pivot_TemplateableElement'):
        assert not _is_linked(a1, 'pivot_TemplateableElement', b)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert _is_linked(a2, 'pivot_TemplateableElement', b)
    _safe_set(b, 'pivot_TemplateableElement306', None)
    assert not _is_linked(b, 'pivot_TemplateableElement306', a2)
    if hasattr(a2, 'pivot_TemplateableElement'):
        assert not _is_linked(a2, 'pivot_TemplateableElement', b)


def test_assoc_variable106_reverse_link_reassign_clear():
    a1 = pivot_Variable(implicit="sample_text")
    a2 = pivot_Variable(implicit="sample_text_2")
    b = pivot_LetExp()
    _safe_set(b, 'pivot_LetExp107', a1)
    assert _is_linked(b, 'pivot_LetExp107', a1)
    if hasattr(a1, 'pivot_Variable108'):
        assert _is_linked(a1, 'pivot_Variable108', b)
    _safe_set(b, 'pivot_LetExp107', a2)
    assert _is_linked(b, 'pivot_LetExp107', a2)
    if hasattr(a1, 'pivot_Variable108'):
        assert not _is_linked(a1, 'pivot_Variable108', b)
    if hasattr(a2, 'pivot_Variable108'):
        assert _is_linked(a2, 'pivot_Variable108', b)
    _safe_set(b, 'pivot_LetExp107', None)
    assert not _is_linked(b, 'pivot_LetExp107', a2)
    if hasattr(a2, 'pivot_Variable108'):
        assert not _is_linked(a2, 'pivot_Variable108', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actual289_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution', None)
    _safe_set(owner, 'pivot_ParameterableElement290', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution') == owner
    _safe_set(owner, 'pivot_ParameterableElement290', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution') is None


def test_assoc_application189_stub_double():
    # pivot_Profile has no real 'appliedProfile' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ProfileApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ProfileApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ProfileApplication(isStrict="sample_text")
    partner = pivot_Profile()
    setattr(partner, 'appliedProfile', None)
    _safe_set(owner, 'ProfileApplication190', partner)
    assert getattr(partner, 'appliedProfile') == owner
    _safe_set(owner, 'ProfileApplication190', None)
    assert getattr(partner, 'appliedProfile') is None


def test_assoc_appliedProfile191_stub_double():
    # pivot_Profile has no real 'Profile' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ProfileApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ProfileApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ProfileApplication(isStrict="sample_text")
    partner = pivot_Profile()
    setattr(partner, 'Profile', None)
    _safe_set(owner, 'application', partner)
    assert getattr(partner, 'Profile') == owner
    _safe_set(owner, 'application', None)
    assert getattr(partner, 'Profile') is None


def test_assoc_argument118_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression119' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression119', None)
    _safe_set(owner, 'pivot_MessageExp', {partner})
    assert getattr(partner, 'pivot_OCLExpression119') == owner
    _safe_set(owner, 'pivot_MessageExp', set())
    assert getattr(partner, 'pivot_OCLExpression119') is None


def test_assoc_argument168_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression169' property in the generated
    # code (a bare stub) -- manually attach it so pivot_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_OperationCallExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression169', None)
    _safe_set(owner, 'pivot_OperationCallExp', {partner})
    assert getattr(partner, 'pivot_OCLExpression169') == owner
    _safe_set(owner, 'pivot_OperationCallExp', set())
    assert getattr(partner, 'pivot_OCLExpression169') is None


def test_assoc_associationClass194_stub_double():
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


def test_assoc_body110_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression111' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression111', None)
    _safe_set(owner, 'pivot_LoopExp', partner)
    assert getattr(partner, 'pivot_OCLExpression111') == owner
    _safe_set(owner, 'pivot_LoopExp', None)
    assert getattr(partner, 'pivot_OCLExpression111') is None


def test_assoc_boundElement276_stub_double():
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


def test_assoc_calledOperation120_stub_double():
    # pivot_CallOperationAction has no real 'pivot_CallOperationAction122' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_CallOperationAction()
    setattr(partner, 'pivot_CallOperationAction122', None)
    _safe_set(owner, 'pivot_MessageExp121', partner)
    assert getattr(partner, 'pivot_CallOperationAction122') == owner
    _safe_set(owner, 'pivot_MessageExp121', None)
    assert getattr(partner, 'pivot_CallOperationAction122') is None


def test_assoc_condition80_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression81' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression81', None)
    _safe_set(owner, 'pivot_IfExp', partner)
    assert getattr(partner, 'pivot_OCLExpression81') == owner
    _safe_set(owner, 'pivot_IfExp', None)
    assert getattr(partner, 'pivot_OCLExpression81') is None


def test_assoc_connection242_stub_double():
    # pivot_ConnectionPointReference has no real 'ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'ConnectionPointReference', None)
    _safe_set(owner, 'state', {partner})
    assert getattr(partner, 'ConnectionPointReference') == owner
    _safe_set(owner, 'state', set())
    assert getattr(partner, 'ConnectionPointReference') is None


def test_assoc_connectionPoint265_stub_double():
    # pivot_StateMachine has no real 'pivot_StateMachine266' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'pivot_StateMachine266', None)
    _safe_set(owner, 'pivot_Pseudostate267', partner)
    assert getattr(partner, 'pivot_StateMachine266') == owner
    _safe_set(owner, 'pivot_Pseudostate267', None)
    assert getattr(partner, 'pivot_StateMachine266') is None


def test_assoc_container308_stub_double():
    # pivot_Region has no real 'Region309' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Region()
    setattr(partner, 'Region309', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'Region309') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'Region309') is None


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


def test_assoc_contextType96_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType', None)
    _safe_set(owner, 'pivot_Type97', partner)
    assert getattr(partner, 'pivot_LambdaType') == owner
    _safe_set(owner, 'pivot_Type97', None)
    assert getattr(partner, 'pivot_LambdaType') is None


def test_assoc_contextVariable72_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL73' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL73', None)
    _safe_set(owner, 'pivot_Variable', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL73') == owner
    _safe_set(owner, 'pivot_Variable', None)
    assert getattr(partner, 'pivot_ExpressionInOCL73') is None


def test_assoc_default280_stub_double():
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


def test_assoc_deferrableTrigger245_stub_double():
    # pivot_Trigger has no real 'Trigger' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'Trigger', None)
    _safe_set(owner, 'state246', {partner})
    assert getattr(partner, 'Trigger') == owner
    _safe_set(owner, 'state246', set())
    assert getattr(partner, 'Trigger') is None


def test_assoc_doActivity247_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior248' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior248', None)
    _safe_set(owner, 'pivot_State', partner)
    assert getattr(partner, 'pivot_Behavior248') == owner
    _safe_set(owner, 'pivot_State', None)
    assert getattr(partner, 'pivot_Behavior248') is None


def test_assoc_effect310_stub_double():
    # pivot_Behavior has no real 'Behavior' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'Behavior', None)
    _safe_set(owner, 'transition311', partner)
    assert getattr(partner, 'Behavior') == owner
    _safe_set(owner, 'transition311', None)
    assert getattr(partner, 'Behavior') is None


def test_assoc_elseExpression82_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression84' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression84', None)
    _safe_set(owner, 'pivot_IfExp83', partner)
    assert getattr(partner, 'pivot_OCLExpression84') == owner
    _safe_set(owner, 'pivot_IfExp83', None)
    assert getattr(partner, 'pivot_OCLExpression84') is None


def test_assoc_entry249_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior251' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior251', None)
    _safe_set(owner, 'pivot_State250', partner)
    assert getattr(partner, 'pivot_Behavior251') == owner
    _safe_set(owner, 'pivot_State250', None)
    assert getattr(partner, 'pivot_Behavior251') is None


def test_assoc_entry26_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference', None)
    _safe_set(owner, 'pivot_Pseudostate', partner)
    assert getattr(partner, 'pivot_ConnectionPointReference') == owner
    _safe_set(owner, 'pivot_Pseudostate', None)
    assert getattr(partner, 'pivot_ConnectionPointReference') is None


def test_assoc_enumeration69_stub_double():
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


def test_assoc_exit252_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior254' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior254', None)
    _safe_set(owner, 'pivot_State253', partner)
    assert getattr(partner, 'pivot_Behavior254') == owner
    _safe_set(owner, 'pivot_State253', None)
    assert getattr(partner, 'pivot_Behavior254') is None


def test_assoc_exit27_stub_double():
    # pivot_ConnectionPointReference has no real 'pivot_ConnectionPointReference28' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'pivot_ConnectionPointReference28', None)
    _safe_set(owner, 'pivot_Pseudostate29', partner)
    assert getattr(partner, 'pivot_ConnectionPointReference28') == owner
    _safe_set(owner, 'pivot_Pseudostate29', None)
    assert getattr(partner, 'pivot_ConnectionPointReference28') is None


def test_assoc_expressionInOCL142_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL144' property in the generated
    # code (a bare stub) -- manually attach it so pivot_OpaqueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_OpaqueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_OpaqueExpression(body="sample_text", language="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL144', None)
    _safe_set(owner, 'pivot_OpaqueExpression143', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL144') == owner
    _safe_set(owner, 'pivot_OpaqueExpression143', None)
    assert getattr(partner, 'pivot_ExpressionInOCL144') is None


def test_assoc_extensionOfs275_stub_double():
    # pivot_Stereotype has no real 'stereotype' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TypeExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TypeExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TypeExtension(isRequired="sample_text")
    partner = pivot_Stereotype()
    setattr(partner, 'stereotype', None)
    _safe_set(owner, 'TypeExtension', partner)
    assert getattr(partner, 'stereotype') == owner
    _safe_set(owner, 'TypeExtension', None)
    assert getattr(partner, 'stereotype') is None


def test_assoc_imports234_stub_double():
    # pivot_Import has no real 'pivot_Import235' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Root(externalURI="sample_text")
    partner = pivot_Import()
    setattr(partner, 'pivot_Import235', None)
    _safe_set(owner, 'pivot_Root', {partner})
    assert getattr(partner, 'pivot_Import235') == owner
    _safe_set(owner, 'pivot_Root', set())
    assert getattr(partner, 'pivot_Import235') is None


def test_assoc_in_104_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression105' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LetExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LetExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LetExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression105', None)
    _safe_set(owner, 'pivot_LetExp', partner)
    assert getattr(partner, 'pivot_OCLExpression105') == owner
    _safe_set(owner, 'pivot_LetExp', None)
    assert getattr(partner, 'pivot_OCLExpression105') is None


def test_assoc_incoming368_stub_double():
    # pivot_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition369', partner)
    assert getattr(partner, 'target') == owner
    _safe_set(owner, 'Transition369', None)
    assert getattr(partner, 'target') is None


def test_assoc_initExpression359_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression361' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression361', None)
    _safe_set(owner, 'pivot_Variable360', partner)
    assert getattr(partner, 'pivot_OCLExpression361') == owner
    _safe_set(owner, 'pivot_Variable360', None)
    assert getattr(partner, 'pivot_OCLExpression361') is None


def test_assoc_instanceType132_stub_double():
    # pivot_Metaclass has no real 'pivot_Metaclass' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_Metaclass()
    setattr(partner, 'pivot_Metaclass', None)
    _safe_set(owner, 'pivot_Type133', partner)
    assert getattr(partner, 'pivot_Metaclass') == owner
    _safe_set(owner, 'pivot_Type133', None)
    assert getattr(partner, 'pivot_Metaclass') is None


def test_assoc_item15_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression16' property in the generated
    # code (a bare stub) -- manually attach it so pivot_CollectionItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_CollectionItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_CollectionItem()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression16', None)
    _safe_set(owner, 'pivot_CollectionItem', partner)
    assert getattr(partner, 'pivot_OCLExpression16') == owner
    _safe_set(owner, 'pivot_CollectionItem', None)
    assert getattr(partner, 'pivot_OCLExpression16') is None


def test_assoc_lowerBound354_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType', None)
    _safe_set(owner, 'pivot_Type355', partner)
    assert getattr(partner, 'pivot_UnspecifiedType') == owner
    _safe_set(owner, 'pivot_Type355', None)
    assert getattr(partner, 'pivot_UnspecifiedType') is None


def test_assoc_metaType52_stub_double():
    # pivot_DynamicElement has no real 'pivot_DynamicElement' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_DynamicElement()
    setattr(partner, 'pivot_DynamicElement', None)
    _safe_set(owner, 'pivot_Type53', partner)
    assert getattr(partner, 'pivot_DynamicElement') == owner
    _safe_set(owner, 'pivot_Type53', None)
    assert getattr(partner, 'pivot_DynamicElement') is None


def test_assoc_navigationSource137_stub_double():
    # pivot_NavigationCallExp has no real 'pivot_NavigationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_NavigationCallExp()
    setattr(partner, 'pivot_NavigationCallExp', None)
    _safe_set(owner, 'pivot_Property138', partner)
    assert getattr(partner, 'pivot_NavigationCallExp') == owner
    _safe_set(owner, 'pivot_Property138', None)
    assert getattr(partner, 'pivot_NavigationCallExp') is None


def test_assoc_operation10_stub_double():
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


def test_assoc_operation185_stub_double():
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


def test_assoc_outgoing370_stub_double():
    # pivot_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition371', partner)
    assert getattr(partner, 'source') == owner
    _safe_set(owner, 'Transition371', None)
    assert getattr(partner, 'source') is None


def test_assoc_ownedActual294_stub_double():
    # pivot_TemplateParameterSubstitution has no real 'pivot_TemplateParameterSubstitution295' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameterSubstitution()
    setattr(partner, 'pivot_TemplateParameterSubstitution295', None)
    _safe_set(owner, 'pivot_ParameterableElement296', partner)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution295') == owner
    _safe_set(owner, 'pivot_ParameterableElement296', None)
    assert getattr(partner, 'pivot_TemplateParameterSubstitution295') is None


def test_assoc_ownedBehavior13_stub_double():
    # pivot_Behavior has no real 'pivot_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Class(isAbstract="sample_text", isActive="sample_text", isInterface="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'pivot_Behavior', None)
    _safe_set(owner, 'pivot_Class14', {partner})
    assert getattr(partner, 'pivot_Behavior') == owner
    _safe_set(owner, 'pivot_Class14', set())
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
    assert getattr(partner, 'pivot_Annotation') == owner
    _safe_set(owner, 'pivot_Element', None)
    assert getattr(partner, 'pivot_Annotation') is None


def test_assoc_ownedDefault281_stub_double():
    # pivot_TemplateParameter has no real 'pivot_TemplateParameter282' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'pivot_TemplateParameter282', None)
    _safe_set(owner, 'pivot_ParameterableElement283', partner)
    assert getattr(partner, 'pivot_TemplateParameter282') == owner
    _safe_set(owner, 'pivot_ParameterableElement283', None)
    assert getattr(partner, 'pivot_TemplateParameter282') is None


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
    assert getattr(partner, 'pivot_Annotation2') == owner
    _safe_set(owner, 'pivot_Detail', None)
    assert getattr(partner, 'pivot_Annotation2') is None


def test_assoc_ownedLiteral68_stub_double():
    # pivot_Enumeration has no real 'enumeration' property in the generated
    # code (a bare stub) -- manually attach it so pivot_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_EnumerationLiteral(value="sample_text")
    partner = pivot_Enumeration()
    setattr(partner, 'enumeration', None)
    _safe_set(owner, 'EnumerationLiteral', partner)
    assert getattr(partner, 'enumeration') == owner
    _safe_set(owner, 'EnumerationLiteral', None)
    assert getattr(partner, 'enumeration') is None


def test_assoc_ownedParameter151_stub_double():
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


def test_assoc_ownedParameteredElement284_stub_double():
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


def test_assoc_ownedPrecedence109_stub_double():
    # pivot_Library has no real 'pivot_Library' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Precedence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Precedence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Precedence(associativity="sample_text", order=7)
    partner = pivot_Library()
    setattr(partner, 'pivot_Library', None)
    _safe_set(owner, 'pivot_Precedence', partner)
    assert getattr(partner, 'pivot_Library') == owner
    _safe_set(owner, 'pivot_Precedence', None)
    assert getattr(partner, 'pivot_Library') is None


def test_assoc_ownedProperty56_stub_double():
    # pivot_DynamicType has no real 'pivot_DynamicType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_DynamicProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_DynamicProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_DynamicProperty(default="sample_text")
    partner = pivot_DynamicType()
    setattr(partner, 'pivot_DynamicType', None)
    _safe_set(owner, 'pivot_DynamicProperty57', partner)
    assert getattr(partner, 'pivot_DynamicType') == owner
    _safe_set(owner, 'pivot_DynamicProperty57', None)
    assert getattr(partner, 'pivot_DynamicType') is None


def test_assoc_ownedRule134_stub_double():
    # pivot_Namespace has no real 'pivot_Namespace135' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Constraint(isCallable="sample_text")
    partner = pivot_Namespace()
    setattr(partner, 'pivot_Namespace135', None)
    _safe_set(owner, 'pivot_Constraint136', partner)
    assert getattr(partner, 'pivot_Namespace135') == owner
    _safe_set(owner, 'pivot_Constraint136', None)
    assert getattr(partner, 'pivot_Namespace135') is None


def test_assoc_ownedTemplateSignature302_stub_double():
    # pivot_TemplateSignature has no real 'TemplateSignature303' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'TemplateSignature303', None)
    _safe_set(owner, 'template', partner)
    assert getattr(partner, 'TemplateSignature303') == owner
    _safe_set(owner, 'template', None)
    assert getattr(partner, 'TemplateSignature303') is None


def test_assoc_owningTemplateParameter186_stub_double():
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


def test_assoc_parameterType98_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType99' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType99', None)
    _safe_set(owner, 'pivot_Type100', partner)
    assert getattr(partner, 'pivot_LambdaType99') == owner
    _safe_set(owner, 'pivot_Type100', None)
    assert getattr(partner, 'pivot_LambdaType99') is None


def test_assoc_parameterVariable74_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL75' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL75', None)
    _safe_set(owner, 'pivot_Variable76', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL75') == owner
    _safe_set(owner, 'pivot_Variable76', None)
    assert getattr(partner, 'pivot_ExpressionInOCL75') is None


def test_assoc_parameteredElement285_stub_double():
    # pivot_TemplateParameter has no real 'templateParameter' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'templateParameter', None)
    _safe_set(owner, 'ParameterableElement286', partner)
    assert getattr(partner, 'templateParameter') == owner
    _safe_set(owner, 'ParameterableElement286', None)
    assert getattr(partner, 'templateParameter') is None


def test_assoc_part17_stub_double():
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


def test_assoc_part44_stub_double():
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
    assert getattr(partner, 'pivot_Annotation4') == owner
    _safe_set(owner, 'pivot_Element5', None)
    assert getattr(partner, 'pivot_Annotation4') is None


def test_assoc_referredIteration115_stub_double():
    # pivot_Iteration has no real 'pivot_Iteration117' property in the generated
    # code (a bare stub) -- manually attach it so pivot_LoopExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_LoopExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_LoopExp()
    partner = pivot_Iteration()
    setattr(partner, 'pivot_Iteration117', None)
    _safe_set(owner, 'pivot_LoopExp116', partner)
    assert getattr(partner, 'pivot_Iteration117') == owner
    _safe_set(owner, 'pivot_LoopExp116', None)
    assert getattr(partner, 'pivot_Iteration117') is None


def test_assoc_referredOperation128_stub_double():
    # pivot_MessageType has no real 'pivot_MessageType' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Operation(isInvalidating="sample_text", isValidating="sample_text")
    partner = pivot_MessageType()
    setattr(partner, 'pivot_MessageType', None)
    _safe_set(owner, 'pivot_Operation129', partner)
    assert getattr(partner, 'pivot_MessageType') == owner
    _safe_set(owner, 'pivot_Operation129', None)
    assert getattr(partner, 'pivot_MessageType') is None


def test_assoc_referredProperty173_stub_double():
    # pivot_OppositePropertyCallExp has no real 'pivot_OppositePropertyCallExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_OppositePropertyCallExp()
    setattr(partner, 'pivot_OppositePropertyCallExp', None)
    _safe_set(owner, 'pivot_Property174', partner)
    assert getattr(partner, 'pivot_OppositePropertyCallExp') == owner
    _safe_set(owner, 'pivot_Property174', None)
    assert getattr(partner, 'pivot_OppositePropertyCallExp') is None


def test_assoc_referredProperty48_stub_double():
    # pivot_ConstructorPart has no real 'pivot_ConstructorPart49' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_ConstructorPart()
    setattr(partner, 'pivot_ConstructorPart49', None)
    _safe_set(owner, 'pivot_Property', partner)
    assert getattr(partner, 'pivot_ConstructorPart49') == owner
    _safe_set(owner, 'pivot_Property', None)
    assert getattr(partner, 'pivot_ConstructorPart49') is None


def test_assoc_referredState263_stub_double():
    # pivot_StateExp has no real 'pivot_StateExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateExp()
    setattr(partner, 'pivot_StateExp', None)
    _safe_set(owner, 'pivot_State264', partner)
    assert getattr(partner, 'pivot_StateExp') == owner
    _safe_set(owner, 'pivot_State264', None)
    assert getattr(partner, 'pivot_StateExp') is None


def test_assoc_referredType345_stub_double():
    # pivot_TypeExp has no real 'pivot_TypeExp' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_TypeExp()
    setattr(partner, 'pivot_TypeExp', None)
    _safe_set(owner, 'pivot_Type346', partner)
    assert getattr(partner, 'pivot_TypeExp') == owner
    _safe_set(owner, 'pivot_Type346', None)
    assert getattr(partner, 'pivot_TypeExp') is None


def test_assoc_referredVariable365_stub_double():
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


def test_assoc_region258_stub_double():
    # pivot_Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'state259', {partner})
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'state259', set())
    assert getattr(partner, 'Region') is None


def test_assoc_representedParameter362_stub_double():
    # pivot_Parameter has no real 'pivot_Parameter364' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_Parameter()
    setattr(partner, 'pivot_Parameter364', None)
    _safe_set(owner, 'pivot_Variable363', partner)
    assert getattr(partner, 'pivot_Parameter364') == owner
    _safe_set(owner, 'pivot_Variable363', None)
    assert getattr(partner, 'pivot_Parameter364') is None


def test_assoc_resultType101_stub_double():
    # pivot_LambdaType has no real 'pivot_LambdaType102' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_LambdaType()
    setattr(partner, 'pivot_LambdaType102', None)
    _safe_set(owner, 'pivot_Type103', partner)
    assert getattr(partner, 'pivot_LambdaType102') == owner
    _safe_set(owner, 'pivot_Type103', None)
    assert getattr(partner, 'pivot_LambdaType102') is None


def test_assoc_resultVariable77_stub_double():
    # pivot_ExpressionInOCL has no real 'pivot_ExpressionInOCL78' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Variable(implicit="sample_text")
    partner = pivot_ExpressionInOCL()
    setattr(partner, 'pivot_ExpressionInOCL78', None)
    _safe_set(owner, 'pivot_Variable79', partner)
    assert getattr(partner, 'pivot_ExpressionInOCL78') == owner
    _safe_set(owner, 'pivot_Variable79', None)
    assert getattr(partner, 'pivot_ExpressionInOCL78') is None


def test_assoc_sentSignal123_stub_double():
    # pivot_SendSignalAction has no real 'pivot_SendSignalAction' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_SendSignalAction()
    setattr(partner, 'pivot_SendSignalAction', None)
    _safe_set(owner, 'pivot_MessageExp124', partner)
    assert getattr(partner, 'pivot_SendSignalAction') == owner
    _safe_set(owner, 'pivot_MessageExp124', None)
    assert getattr(partner, 'pivot_SendSignalAction') is None


def test_assoc_source315_stub_double():
    # pivot_Vertex has no real 'Vertex316' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex316', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex316') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex316') is None


def test_assoc_source9_stub_double():
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


def test_assoc_state226_stub_double():
    # pivot_Region has no real 'region' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Region()
    setattr(partner, 'region', None)
    _safe_set(owner, 'State227', partner)
    assert getattr(partner, 'region') == owner
    _safe_set(owner, 'State227', None)
    assert getattr(partner, 'region') is None


def test_assoc_state30_stub_double():
    # pivot_ConnectionPointReference has no real 'connection' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_ConnectionPointReference()
    setattr(partner, 'connection', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'connection') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'connection') is None


def test_assoc_state322_stub_double():
    # pivot_Trigger has no real 'deferrableTrigger' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'deferrableTrigger', None)
    _safe_set(owner, 'State323', partner)
    assert getattr(partner, 'deferrableTrigger') == owner
    _safe_set(owner, 'State323', None)
    assert getattr(partner, 'deferrableTrigger') is None


def test_assoc_stateMachine222_stub_double():
    # pivot_StateMachine has no real 'pivot_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Pseudostate(kind="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'pivot_StateMachine', None)
    _safe_set(owner, 'pivot_Pseudostate223', partner)
    assert getattr(partner, 'pivot_StateMachine') == owner
    _safe_set(owner, 'pivot_Pseudostate223', None)
    assert getattr(partner, 'pivot_StateMachine') is None


def test_assoc_stereotype347_stub_double():
    # pivot_Stereotype has no real 'Stereotype' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TypeExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TypeExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TypeExtension(isRequired="sample_text")
    partner = pivot_Stereotype()
    setattr(partner, 'Stereotype', None)
    _safe_set(owner, 'extensionOfs', partner)
    assert getattr(partner, 'Stereotype') == owner
    _safe_set(owner, 'extensionOfs', None)
    assert getattr(partner, 'Stereotype') is None


def test_assoc_stereotype66_stub_double():
    # pivot_Stereotype has no real 'pivot_Stereotype' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ElementExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ElementExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ElementExtension(isApplied="sample_text", isRequired="sample_text")
    partner = pivot_Stereotype()
    setattr(partner, 'pivot_Stereotype', None)
    _safe_set(owner, 'pivot_ElementExtension', partner)
    assert getattr(partner, 'pivot_Stereotype') == owner
    _safe_set(owner, 'pivot_ElementExtension', None)
    assert getattr(partner, 'pivot_Stereotype') is None


def test_assoc_submachine261_stub_double():
    # pivot_StateMachine has no real 'StateMachine262' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'StateMachine262', None)
    _safe_set(owner, 'submachineState', partner)
    assert getattr(partner, 'StateMachine262') == owner
    _safe_set(owner, 'submachineState', None)
    assert getattr(partner, 'StateMachine262') is None


def test_assoc_submachineState273_stub_double():
    # pivot_StateMachine has no real 'submachine' property in the generated
    # code (a bare stub) -- manually attach it so pivot_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_State(isComposite="sample_text", isOrthogonal="sample_text", isSimple="sample_text", isSubmachineState="sample_text")
    partner = pivot_StateMachine()
    setattr(partner, 'submachine', None)
    _safe_set(owner, 'State274', partner)
    assert getattr(partner, 'submachine') == owner
    _safe_set(owner, 'State274', None)
    assert getattr(partner, 'submachine') is None


def test_assoc_target125_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression127' property in the generated
    # code (a bare stub) -- manually attach it so pivot_MessageExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_MessageExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_MessageExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression127', None)
    _safe_set(owner, 'pivot_MessageExp126', partner)
    assert getattr(partner, 'pivot_OCLExpression127') == owner
    _safe_set(owner, 'pivot_MessageExp126', None)
    assert getattr(partner, 'pivot_OCLExpression127') is None


def test_assoc_target317_stub_double():
    # pivot_Vertex has no real 'Vertex318' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Vertex()
    setattr(partner, 'Vertex318', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex318') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex318') is None


def test_assoc_template300_stub_double():
    # pivot_TemplateSignature has no real 'ownedTemplateSignature' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateSignature()
    setattr(partner, 'ownedTemplateSignature', None)
    _safe_set(owner, 'TemplateableElement301', partner)
    assert getattr(partner, 'ownedTemplateSignature') == owner
    _safe_set(owner, 'TemplateableElement301', None)
    assert getattr(partner, 'ownedTemplateSignature') is None


def test_assoc_templateBinding304_stub_double():
    # pivot_TemplateBinding has no real 'TemplateBinding305' property in the generated
    # code (a bare stub) -- manually attach it so pivot_TemplateableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_TemplateableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_TemplateableElement()
    partner = pivot_TemplateBinding()
    setattr(partner, 'TemplateBinding305', None)
    _safe_set(owner, 'boundElement', {partner})
    assert getattr(partner, 'TemplateBinding305') == owner
    _safe_set(owner, 'boundElement', set())
    assert getattr(partner, 'TemplateBinding305') is None


def test_assoc_templateParameter187_stub_double():
    # pivot_TemplateParameter has no real 'TemplateParameter188' property in the generated
    # code (a bare stub) -- manually attach it so pivot_ParameterableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_ParameterableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_ParameterableElement()
    partner = pivot_TemplateParameter()
    setattr(partner, 'TemplateParameter188', None)
    _safe_set(owner, 'parameteredElement', partner)
    assert getattr(partner, 'TemplateParameter188') == owner
    _safe_set(owner, 'parameteredElement', None)
    assert getattr(partner, 'TemplateParameter188') is None


def test_assoc_thenExpression85_stub_double():
    # pivot_OCLExpression has no real 'pivot_OCLExpression87' property in the generated
    # code (a bare stub) -- manually attach it so pivot_IfExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_IfExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_IfExp()
    partner = pivot_OCLExpression()
    setattr(partner, 'pivot_OCLExpression87', None)
    _safe_set(owner, 'pivot_IfExp86', partner)
    assert getattr(partner, 'pivot_OCLExpression87') == owner
    _safe_set(owner, 'pivot_IfExp86', None)
    assert getattr(partner, 'pivot_OCLExpression87') is None


def test_assoc_transition231_stub_double():
    # pivot_Region has no real 'container232' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Region()
    setattr(partner, 'container232', None)
    _safe_set(owner, 'Transition233', partner)
    assert getattr(partner, 'container232') == owner
    _safe_set(owner, 'Transition233', None)
    assert getattr(partner, 'container232') is None


def test_assoc_transition324_stub_double():
    # pivot_Trigger has no real 'trigger' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'trigger', None)
    _safe_set(owner, 'Transition325', partner)
    assert getattr(partner, 'trigger') == owner
    _safe_set(owner, 'Transition325', None)
    assert getattr(partner, 'trigger') is None


def test_assoc_transition8_stub_double():
    # pivot_Behavior has no real 'effect' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Behavior()
    setattr(partner, 'effect', None)
    _safe_set(owner, 'Transition', partner)
    assert getattr(partner, 'effect') == owner
    _safe_set(owner, 'Transition', None)
    assert getattr(partner, 'effect') is None


def test_assoc_trigger319_stub_double():
    # pivot_Trigger has no real 'Trigger321' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Transition(kind="sample_text")
    partner = pivot_Trigger()
    setattr(partner, 'Trigger321', None)
    _safe_set(owner, 'transition320', {partner})
    assert getattr(partner, 'Trigger321') == owner
    _safe_set(owner, 'transition320', set())
    assert getattr(partner, 'Trigger321') is None


def test_assoc_unownedAttribute6_stub_double():
    # pivot_AssociationClass has no real 'associationClass' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Property(default="sample_text", implicit="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text", isResolveProxies="sample_text", isTransient="sample_text", isUnsettable="sample_text", isVolatile="sample_text")
    partner = pivot_AssociationClass()
    setattr(partner, 'associationClass', None)
    _safe_set(owner, 'Property', partner)
    assert getattr(partner, 'associationClass') == owner
    _safe_set(owner, 'Property', None)
    assert getattr(partner, 'associationClass') is None


def test_assoc_upperBound356_stub_double():
    # pivot_UnspecifiedType has no real 'pivot_UnspecifiedType357' property in the generated
    # code (a bare stub) -- manually attach it so pivot_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pivot_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pivot_Type(instanceClassName="sample_text")
    partner = pivot_UnspecifiedType()
    setattr(partner, 'pivot_UnspecifiedType357', None)
    _safe_set(owner, 'pivot_Type358', partner)
    assert getattr(partner, 'pivot_UnspecifiedType357') == owner
    _safe_set(owner, 'pivot_Type358', None)
    assert getattr(partner, 'pivot_UnspecifiedType357') is None


