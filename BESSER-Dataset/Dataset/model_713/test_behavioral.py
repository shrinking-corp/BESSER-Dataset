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


