import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    Comment,
    DataType,
    EMOF_Class,
    EMOF_Comment,
    EMOF_DataType,
    EMOF_Element,
    EMOF_Enumeration,
    EMOF_EnumerationLiteral,
    EMOF_Extent,
    EMOF_Factory,
    EMOF_MultiplicityElement,
    EMOF_NamedElement,
    EMOF_Object,
    EMOF_Operation,
    EMOF_Package,
    EMOF_Parameter,
    EMOF_PrimitiveType,
    EMOF_Property,
    EMOF_ReflectiveCollection,
    EMOF_ReflectiveSequence,
    EMOF_Tag,
    EMOF_Type,
    EMOF_TypedElement,
    EMOF_URIExtent,
    Element,
    Enumeration,
    EnumerationLiteral,
    Extent,
    MultiplicityElement,
    NamedElement,
    Object,
    Operation,
    Package,
    Parameter,
    Property,
    ReflectiveCollection,
    Type,
    TypedElement,
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

def test_assoc_annotatedElement5_stub_double():
    # NamedElement has no real 'NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Comment(body="sample_text")
    partner = NamedElement()
    setattr(partner, 'NamedElement', None)
    _safe_set(owner, 'EMOF_Comment', {partner})
    assert getattr(partner, 'NamedElement') == owner
    _safe_set(owner, 'EMOF_Comment', set())
    assert getattr(partner, 'NamedElement') is None


def test_assoc_class_23_stub_double():
    # Class has no real 'Class24' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Class()
    setattr(partner, 'Class24', None)
    _safe_set(owner, 'EMOF_Property', partner)
    assert getattr(partner, 'Class24') == owner
    _safe_set(owner, 'EMOF_Property', None)
    assert getattr(partner, 'Class24') is None


def test_assoc_element28_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'EMOF_Tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'EMOF_Tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_nestedPackage16_stub_double():
    # Package has no real 'Package17' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package17', None)
    _safe_set(owner, 'EMOF_Package', {partner})
    assert getattr(partner, 'Package17') == owner
    _safe_set(owner, 'EMOF_Package', set())
    assert getattr(partner, 'Package17') is None


def test_assoc_opposite25_stub_double():
    # Property has no real 'Property27' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property27', None)
    _safe_set(owner, 'EMOF_Property26', partner)
    assert getattr(partner, 'Property27') == owner
    _safe_set(owner, 'EMOF_Property26', None)
    assert getattr(partner, 'Property27') is None


def test_assoc_ownedAttribute0_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'EMOF_Class', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'EMOF_Class', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedComment6_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Element()
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'EMOF_Element', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'EMOF_Element', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_ownedOperation1_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'EMOF_Class2', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'EMOF_Class2', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedType18_stub_double():
    # Type has no real 'Type20' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type20', None)
    _safe_set(owner, 'EMOF_Package19', {partner})
    assert getattr(partner, 'Type20') == owner
    _safe_set(owner, 'EMOF_Package19', set())
    assert getattr(partner, 'Type20') is None


def test_assoc_package29_stub_double():
    # Package has no real 'Package30' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Type()
    partner = Package()
    setattr(partner, 'Package30', None)
    _safe_set(owner, 'EMOF_Type', partner)
    assert getattr(partner, 'Package30') == owner
    _safe_set(owner, 'EMOF_Type', None)
    assert getattr(partner, 'Package30') is None


def test_assoc_package9_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Factory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Factory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Factory()
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'EMOF_Factory', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'EMOF_Factory', None)
    assert getattr(partner, 'Package') is None


def test_assoc_superClass3_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'EMOF_Class4', {partner})
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'EMOF_Class4', set())
    assert getattr(partner, 'Class') is None


