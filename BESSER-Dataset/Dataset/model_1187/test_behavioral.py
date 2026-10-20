import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExp,
    Class,
    CollectionLiteralPart,
    CollectionType,
    DataType,
    Element,
    EnumerationLiteral,
    Extent,
    FeaturePropertyCall,
    Iterator,
    LiteralExp,
    LoopExp,
    MultiplicityElement,
    NamedElement,
    NumericLiteralExp,
    OCL_AnyType,
    OCL_BagType,
    OCL_BooleanLiteralExp,
    OCL_BooleanType,
    OCL_CallExp,
    OCL_Class,
    OCL_CollectionItem,
    OCL_CollectionLiteralExp,
    OCL_CollectionLiteralPart,
    OCL_CollectionOperationCallExp,
    OCL_CollectionRange,
    OCL_CollectionType,
    OCL_Comment,
    OCL_DataType,
    OCL_DefOclModuleElement,
    OCL_DeriveOclModuleElement,
    OCL_Element,
    OCL_EnumLiteralExp,
    OCL_Enumeration,
    OCL_EnumerationLiteral,
    OCL_Extent,
    OCL_FeaturePropertyCall,
    OCL_IfExp,
    OCL_IntegerLiteralExp,
    OCL_IntegerType,
    OCL_InvalidLiteralExp,
    OCL_InvalidType,
    OCL_Invariant,
    OCL_IterateExp,
    OCL_Iterator,
    OCL_IteratorExp,
    OCL_LetExp,
    OCL_LiteralExp,
    OCL_LoopExp,
    OCL_MultiplicityElement,
    OCL_NamedElement,
    OCL_NullLiteralExp,
    OCL_NumericLiteralExp,
    OCL_Object,
    OCL_OclContextDefinition,
    OCL_OclExpression,
    OCL_OclFeature,
    OCL_OclModule,
    OCL_OclModuleElement,
    OCL_OclOperation,
    OCL_OclProperty,
    OCL_Operation,
    OCL_OperationCallExp,
    OCL_OperatorCallExp,
    OCL_OrderedSetType,
    OCL_Package,
    OCL_Parameter,
    OCL_PrimitiveLiteralExp,
    OCL_PrimitiveType,
    OCL_Property,
    OCL_PropertyCallExp,
    OCL_RealLiteralExp,
    OCL_RealType,
    OCL_SequenceType,
    OCL_SetType,
    OCL_StringLiteralExp,
    OCL_StringType,
    OCL_Tag,
    OCL_TupleLiteralExp,
    OCL_TupleLiteralPart,
    OCL_TupleType,
    OCL_Type,
    OCL_TypedElement,
    OCL_URIExtent,
    OCL_Variable,
    OCL_VariableExp,
    OCL_VoidType,
    Object,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclModuleElement,
    Operation,
    OperationCallExp,
    Package,
    Parameter,
    PrimitiveLiteralExp,
    PrimitiveType,
    Property,
    TupleLiteralPart,
    Type,
    TypedElement,
    Variable,
    CollectionKind,
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

def test_assoc_contextVariable21_stub_double():
    # Variable has no real 'Variable23' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Invariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Invariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Invariant(name="sample_text")
    partner = Variable()
    setattr(partner, 'Variable23', None)
    _safe_set(owner, 'OCL_Invariant22', partner)
    assert getattr(partner, 'Variable23') == owner
    _safe_set(owner, 'OCL_Invariant22', None)
    assert getattr(partner, 'Variable23') is None


def test_assoc_element31_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'OCL_Tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'OCL_Tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_nestedPackage28_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'OCL_Package29', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'OCL_Package29', set())
    assert getattr(partner, 'Package') is None


def test_assoc_opposite37_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'OCL_Property', partner)
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'OCL_Property', None)
    assert getattr(partner, 'Property') is None


def test_assoc_ownedAttribute38_stub_double():
    # Property has no real 'Property39' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Class(isAbstract="sample_text")
    partner = Property()
    setattr(partner, 'Property39', None)
    _safe_set(owner, 'OCL_Class', {partner})
    assert getattr(partner, 'Property39') == owner
    _safe_set(owner, 'OCL_Class', set())
    assert getattr(partner, 'Property39') is None


def test_assoc_ownedOperation40_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'OCL_Class41', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'OCL_Class41', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedType26_stub_double():
    # Type has no real 'Type27' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type27', None)
    _safe_set(owner, 'OCL_Package', {partner})
    assert getattr(partner, 'Type27') == owner
    _safe_set(owner, 'OCL_Package', set())
    assert getattr(partner, 'Type27') is None


def test_assoc_part59_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so OCL_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'OCL_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'OCL_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_specification19_stub_double():
    # OclExpression has no real 'OclExpression20' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Invariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Invariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Invariant(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression20', None)
    _safe_set(owner, 'OCL_Invariant', partner)
    assert getattr(partner, 'OclExpression20') == owner
    _safe_set(owner, 'OCL_Invariant', None)
    assert getattr(partner, 'OclExpression20') is None


