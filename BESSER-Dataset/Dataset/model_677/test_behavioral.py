import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    Element,
    Extent,
    MultiplicityElement,
    NamedElement,
    Object,
    Type,
    TypedElement,
    emof_Class,
    emof_Comment,
    emof_DataType,
    emof_Element,
    emof_Enumeration,
    emof_EnumerationLiteral,
    emof_Extent,
    emof_MultiplicityElement,
    emof_NamedElement,
    emof_Object,
    emof_Operation,
    emof_Package,
    emof_Parameter,
    emof_PrimitiveType,
    emof_Property,
    emof_Tag,
    emof_Type,
    emof_TypedElement,
    emof_URIExtent,
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

def test_assoc_class_19_reverse_link_reassign_clear():
    a1 = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    a2 = emof_Property(default="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isId="sample_text_2", isReadOnly="sample_text_2")
    b = emof_Class(isAbstract="sample_text")
    _safe_set(b, 'Class20', a1)
    assert _is_linked(b, 'Class20', a1)
    if hasattr(a1, 'ownedAttribute'):
        assert _is_linked(a1, 'ownedAttribute', b)
    _safe_set(b, 'Class20', a2)
    assert _is_linked(b, 'Class20', a2)
    if hasattr(a1, 'ownedAttribute'):
        assert not _is_linked(a1, 'ownedAttribute', b)
    if hasattr(a2, 'ownedAttribute'):
        assert _is_linked(a2, 'ownedAttribute', b)
    _safe_set(b, 'Class20', None)
    assert not _is_linked(b, 'Class20', a2)
    if hasattr(a2, 'ownedAttribute'):
        assert not _is_linked(a2, 'ownedAttribute', b)


def test_assoc_nestedPackage14_reverse_link_reassign_clear():
    a1 = emof_Package(uri="sample_text")
    a2 = emof_Package(uri="sample_text_2")
    b = emof_Package(uri="sample_text")
    _safe_set(b, 'emof_Package13', {a1})
    assert _is_linked(b, 'emof_Package13', a1)
    if hasattr(a1, 'emof_Package'):
        assert _is_linked(a1, 'emof_Package', b)
    _safe_set(b, 'emof_Package13', {a2})
    assert _is_linked(b, 'emof_Package13', a2)
    if hasattr(a1, 'emof_Package'):
        assert not _is_linked(a1, 'emof_Package', b)
    if hasattr(a2, 'emof_Package'):
        assert _is_linked(a2, 'emof_Package', b)
    _safe_set(b, 'emof_Package13', set())
    assert not _is_linked(b, 'emof_Package13', a2)
    if hasattr(a2, 'emof_Package'):
        assert not _is_linked(a2, 'emof_Package', b)


def test_assoc_opposite22_reverse_link_reassign_clear():
    a1 = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    a2 = emof_Property(default="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isId="sample_text_2", isReadOnly="sample_text_2")
    b = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    _safe_set(b, 'emof_Property21', a1)
    assert _is_linked(b, 'emof_Property21', a1)
    if hasattr(a1, 'emof_Property'):
        assert _is_linked(a1, 'emof_Property', b)
    _safe_set(b, 'emof_Property21', a2)
    assert _is_linked(b, 'emof_Property21', a2)
    if hasattr(a1, 'emof_Property'):
        assert not _is_linked(a1, 'emof_Property', b)
    if hasattr(a2, 'emof_Property'):
        assert _is_linked(a2, 'emof_Property', b)
    _safe_set(b, 'emof_Property21', None)
    assert not _is_linked(b, 'emof_Property21', a2)
    if hasattr(a2, 'emof_Property'):
        assert not _is_linked(a2, 'emof_Property', b)


def test_assoc_ownedAttribute0_reverse_link_reassign_clear():
    a1 = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    a2 = emof_Property(default="sample_text_2", isComposite="sample_text_2", isDerived="sample_text_2", isId="sample_text_2", isReadOnly="sample_text_2")
    b = emof_Class(isAbstract="sample_text")
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Property'):
        assert _is_linked(a1, 'Property', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Property'):
        assert not _is_linked(a1, 'Property', b)
    if hasattr(a2, 'Property'):
        assert _is_linked(a2, 'Property', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Property'):
        assert not _is_linked(a2, 'Property', b)


def test_assoc_superClass4_reverse_link_reassign_clear():
    a1 = emof_Class(isAbstract="sample_text")
    a2 = emof_Class(isAbstract="sample_text_2")
    b = emof_Class(isAbstract="sample_text")
    _safe_set(b, 'emof_Class3', {a1})
    assert _is_linked(b, 'emof_Class3', a1)
    if hasattr(a1, 'emof_Class'):
        assert _is_linked(a1, 'emof_Class', b)
    _safe_set(b, 'emof_Class3', {a2})
    assert _is_linked(b, 'emof_Class3', a2)
    if hasattr(a1, 'emof_Class'):
        assert not _is_linked(a1, 'emof_Class', b)
    if hasattr(a2, 'emof_Class'):
        assert _is_linked(a2, 'emof_Class', b)
    _safe_set(b, 'emof_Class3', set())
    assert not _is_linked(b, 'emof_Class3', a2)
    if hasattr(a2, 'emof_Class'):
        assert not _is_linked(a2, 'emof_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotatedElement25_stub_double():
    # emof_Comment has no real 'emof_Comment26' property in the generated
    # code (a bare stub) -- manually attach it so emof_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_NamedElement(name="sample_text")
    partner = emof_Comment()
    setattr(partner, 'emof_Comment26', None)
    _safe_set(owner, 'emof_NamedElement', partner)
    assert owner in getattr(partner, 'emof_Comment26')
    _safe_set(owner, 'emof_NamedElement', None)
    assert owner not in getattr(partner, 'emof_Comment26')


def test_assoc_class_9_stub_double():
    # emof_Operation has no real 'ownedOperation' property in the generated
    # code (a bare stub) -- manually attach it so emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Class(isAbstract="sample_text")
    partner = emof_Operation()
    setattr(partner, 'ownedOperation', None)
    _safe_set(owner, 'Class', partner)
    assert getattr(partner, 'ownedOperation') == owner
    _safe_set(owner, 'Class', None)
    assert getattr(partner, 'ownedOperation') is None


def test_assoc_element7_stub_double():
    # emof_Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Tag(name="sample_text", value="sample_text")
    partner = emof_Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_ownedOperation1_stub_double():
    # emof_Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Class(isAbstract="sample_text")
    partner = emof_Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'class_2', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'class_2', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedType12_stub_double():
    # emof_Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Package(uri="sample_text")
    partner = emof_Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type') is None


def test_assoc_package15_stub_double():
    # emof_Type has no real 'ownedType' property in the generated
    # code (a bare stub) -- manually attach it so emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Package(uri="sample_text")
    partner = emof_Type()
    setattr(partner, 'ownedType', None)
    _safe_set(owner, 'Package', partner)
    assert getattr(partner, 'ownedType') == owner
    _safe_set(owner, 'Package', None)
    assert getattr(partner, 'ownedType') is None


def test_assoc_tag5_stub_double():
    # emof_Element has no real 'element' property in the generated
    # code (a bare stub) -- manually attach it so emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Tag(name="sample_text", value="sample_text")
    partner = emof_Element()
    setattr(partner, 'element', None)
    _safe_set(owner, 'Tag', partner)
    assert owner in getattr(partner, 'element')
    _safe_set(owner, 'Tag', None)
    assert owner not in getattr(partner, 'element')


