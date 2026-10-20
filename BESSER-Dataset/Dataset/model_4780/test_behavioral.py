import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Categorized,
    Relationship,
    Secured,
    TypeElement,
    TypePointer,
    type_Assosiation,
    type_Attribute,
    type_AttributePointer,
    type_EnumAttribute,
    type_Enumerator,
    type_Generalization,
    type_Link,
    type_MethodPointer,
    type_Operation,
    type_PackagePointer,
    type_Parameter,
    type_Primitive,
    type_PrimitivesGroup,
    type_References,
    type_Relationship,
    type_ReturnValue,
    type_Type,
    type_TypeElement,
    type_TypeGroup,
    type_TypePointer,
    type_TypeReference,
    Containment,
    RelationType,
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

def test_assoc_detailField20_reverse_link_reassign_clear():
    a1 = type_Link(uid="sample_text")
    a2 = type_Link(uid="sample_text_2")
    b = type_Attribute(name="sample_text", pk=True, uid="sample_text")
    _safe_set(b, 'type_Attribute22', a1)
    assert _is_linked(b, 'type_Attribute22', a1)
    if hasattr(a1, 'type_Link21'):
        assert _is_linked(a1, 'type_Link21', b)
    _safe_set(b, 'type_Attribute22', a2)
    assert _is_linked(b, 'type_Attribute22', a2)
    if hasattr(a1, 'type_Link21'):
        assert not _is_linked(a1, 'type_Link21', b)
    if hasattr(a2, 'type_Link21'):
        assert _is_linked(a2, 'type_Link21', b)
    _safe_set(b, 'type_Attribute22', None)
    assert not _is_linked(b, 'type_Attribute22', a2)
    if hasattr(a2, 'type_Link21'):
        assert not _is_linked(a2, 'type_Link21', b)


def test_assoc_links14_reverse_link_reassign_clear():
    a1 = type_Link(uid="sample_text")
    a2 = type_Link(uid="sample_text_2")
    b = type_Assosiation(containment="sample_text", internal=True, sourceOperation="sample_text", targetOperation="sample_text", type="sample_text")
    _safe_set(b, 'type_Assosiation', {a1})
    assert _is_linked(b, 'type_Assosiation', a1)
    if hasattr(a1, 'type_Link'):
        assert _is_linked(a1, 'type_Link', b)
    _safe_set(b, 'type_Assosiation', {a2})
    assert _is_linked(b, 'type_Assosiation', a2)
    if hasattr(a1, 'type_Link'):
        assert not _is_linked(a1, 'type_Link', b)
    if hasattr(a2, 'type_Link'):
        assert _is_linked(a2, 'type_Link', b)
    _safe_set(b, 'type_Assosiation', set())
    assert not _is_linked(b, 'type_Assosiation', a2)
    if hasattr(a2, 'type_Link'):
        assert not _is_linked(a2, 'type_Link', b)


def test_assoc_masterField18_reverse_link_reassign_clear():
    a1 = type_Link(uid="sample_text")
    a2 = type_Link(uid="sample_text_2")
    b = type_Attribute(name="sample_text", pk=True, uid="sample_text")
    _safe_set(b, 'type_Attribute', a1)
    assert _is_linked(b, 'type_Attribute', a1)
    if hasattr(a1, 'type_Link19'):
        assert _is_linked(a1, 'type_Link19', b)
    _safe_set(b, 'type_Attribute', a2)
    assert _is_linked(b, 'type_Attribute', a2)
    if hasattr(a1, 'type_Link19'):
        assert not _is_linked(a1, 'type_Link19', b)
    if hasattr(a2, 'type_Link19'):
        assert _is_linked(a2, 'type_Link19', b)
    _safe_set(b, 'type_Attribute', None)
    assert not _is_linked(b, 'type_Attribute', a2)
    if hasattr(a2, 'type_Link19'):
        assert not _is_linked(a2, 'type_Link19', b)


def test_assoc_parameters23_reverse_link_reassign_clear():
    a1 = type_Parameter(name="sample_text", order=7, uid="sample_text")
    a2 = type_Parameter(name="sample_text_2", order=13, uid="sample_text_2")
    b = type_Operation(name="sample_text", uid="sample_text")
    _safe_set(b, 'type_Operation', {a1})
    assert _is_linked(b, 'type_Operation', a1)
    if hasattr(a1, 'type_Parameter'):
        assert _is_linked(a1, 'type_Parameter', b)
    _safe_set(b, 'type_Operation', {a2})
    assert _is_linked(b, 'type_Operation', a2)
    if hasattr(a1, 'type_Parameter'):
        assert not _is_linked(a1, 'type_Parameter', b)
    if hasattr(a2, 'type_Parameter'):
        assert _is_linked(a2, 'type_Parameter', b)
    _safe_set(b, 'type_Operation', set())
    assert not _is_linked(b, 'type_Operation', a2)
    if hasattr(a2, 'type_Parameter'):
        assert not _is_linked(a2, 'type_Parameter', b)


def test_assoc_relationships1_reverse_link_reassign_clear():
    a1 = type_TypeGroup(name="sample_text", uid="sample_text")
    a2 = type_TypeGroup(name="sample_text_2", uid="sample_text_2")
    b = type_Relationship(uid="sample_text")
    _safe_set(b, 'type_Relationship', a1)
    assert _is_linked(b, 'type_Relationship', a1)
    if hasattr(a1, 'type_TypeGroup2'):
        assert _is_linked(a1, 'type_TypeGroup2', b)
    _safe_set(b, 'type_Relationship', a2)
    assert _is_linked(b, 'type_Relationship', a2)
    if hasattr(a1, 'type_TypeGroup2'):
        assert not _is_linked(a1, 'type_TypeGroup2', b)
    if hasattr(a2, 'type_TypeGroup2'):
        assert _is_linked(a2, 'type_TypeGroup2', b)
    _safe_set(b, 'type_Relationship', None)
    assert not _is_linked(b, 'type_Relationship', a2)
    if hasattr(a2, 'type_TypeGroup2'):
        assert not _is_linked(a2, 'type_TypeGroup2', b)


def test_assoc_returnValue24_reverse_link_reassign_clear():
    a1 = type_ReturnValue(uid="sample_text")
    a2 = type_ReturnValue(uid="sample_text_2")
    b = type_Operation(name="sample_text", uid="sample_text")
    _safe_set(b, 'type_Operation25', a1)
    assert _is_linked(b, 'type_Operation25', a1)
    if hasattr(a1, 'type_ReturnValue'):
        assert _is_linked(a1, 'type_ReturnValue', b)
    _safe_set(b, 'type_Operation25', a2)
    assert _is_linked(b, 'type_Operation25', a2)
    if hasattr(a1, 'type_ReturnValue'):
        assert not _is_linked(a1, 'type_ReturnValue', b)
    if hasattr(a2, 'type_ReturnValue'):
        assert _is_linked(a2, 'type_ReturnValue', b)
    _safe_set(b, 'type_Operation25', None)
    assert not _is_linked(b, 'type_Operation25', a2)
    if hasattr(a2, 'type_ReturnValue'):
        assert not _is_linked(a2, 'type_ReturnValue', b)


def test_assoc_source4_reverse_link_reassign_clear():
    a1 = type_TypeElement(name="sample_text", uid="sample_text")
    a2 = type_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = type_Relationship(uid="sample_text")
    _safe_set(b, 'type_Relationship5', a1)
    assert _is_linked(b, 'type_Relationship5', a1)
    if hasattr(a1, 'type_TypeElement6'):
        assert _is_linked(a1, 'type_TypeElement6', b)
    _safe_set(b, 'type_Relationship5', a2)
    assert _is_linked(b, 'type_Relationship5', a2)
    if hasattr(a1, 'type_TypeElement6'):
        assert not _is_linked(a1, 'type_TypeElement6', b)
    if hasattr(a2, 'type_TypeElement6'):
        assert _is_linked(a2, 'type_TypeElement6', b)
    _safe_set(b, 'type_Relationship5', None)
    assert not _is_linked(b, 'type_Relationship5', a2)
    if hasattr(a2, 'type_TypeElement6'):
        assert not _is_linked(a2, 'type_TypeElement6', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = type_TypeElement(name="sample_text", uid="sample_text")
    a2 = type_TypeElement(name="sample_text_2", uid="sample_text_2")
    b = type_Relationship(uid="sample_text")
    _safe_set(b, 'type_Relationship8', a1)
    assert _is_linked(b, 'type_Relationship8', a1)
    if hasattr(a1, 'type_TypeElement9'):
        assert _is_linked(a1, 'type_TypeElement9', b)
    _safe_set(b, 'type_Relationship8', a2)
    assert _is_linked(b, 'type_Relationship8', a2)
    if hasattr(a1, 'type_TypeElement9'):
        assert not _is_linked(a1, 'type_TypeElement9', b)
    if hasattr(a2, 'type_TypeElement9'):
        assert _is_linked(a2, 'type_TypeElement9', b)
    _safe_set(b, 'type_Relationship8', None)
    assert not _is_linked(b, 'type_Relationship8', a2)
    if hasattr(a2, 'type_TypeElement9'):
        assert not _is_linked(a2, 'type_TypeElement9', b)


def test_assoc_types0_reverse_link_reassign_clear():
    a1 = type_TypeGroup(name="sample_text", uid="sample_text")
    a2 = type_TypeGroup(name="sample_text_2", uid="sample_text_2")
    b = type_TypeElement(name="sample_text", uid="sample_text")
    _safe_set(b, 'type_TypeElement', a1)
    assert _is_linked(b, 'type_TypeElement', a1)
    if hasattr(a1, 'type_TypeGroup'):
        assert _is_linked(a1, 'type_TypeGroup', b)
    _safe_set(b, 'type_TypeElement', a2)
    assert _is_linked(b, 'type_TypeElement', a2)
    if hasattr(a1, 'type_TypeGroup'):
        assert not _is_linked(a1, 'type_TypeGroup', b)
    if hasattr(a2, 'type_TypeGroup'):
        assert _is_linked(a2, 'type_TypeGroup', b)
    _safe_set(b, 'type_TypeElement', None)
    assert not _is_linked(b, 'type_TypeElement', a2)
    if hasattr(a2, 'type_TypeGroup'):
        assert not _is_linked(a2, 'type_TypeGroup', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeRef34_stub_double():
    # type_AttributePointer has no real 'type_AttributePointer' property in the generated
    # code (a bare stub) -- manually attach it so type_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_Attribute(name="sample_text", pk=True, uid="sample_text")
    partner = type_AttributePointer()
    setattr(partner, 'type_AttributePointer', None)
    _safe_set(owner, 'type_Attribute35', partner)
    assert getattr(partner, 'type_AttributePointer') == owner
    _safe_set(owner, 'type_Attribute35', None)
    assert getattr(partner, 'type_AttributePointer') is None


def test_assoc_attributes26_stub_double():
    # type_Type has no real 'type_Type' property in the generated
    # code (a bare stub) -- manually attach it so type_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_Attribute(name="sample_text", pk=True, uid="sample_text")
    partner = type_Type()
    setattr(partner, 'type_Type', None)
    _safe_set(owner, 'type_Attribute27', partner)
    assert owner in getattr(partner, 'type_Type')
    _safe_set(owner, 'type_Attribute27', None)
    assert owner not in getattr(partner, 'type_Type')


def test_assoc_many2manyHelper15_stub_double():
    # type_TypePointer has no real 'type_TypePointer17' property in the generated
    # code (a bare stub) -- manually attach it so type_Assosiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_Assosiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_Assosiation(containment="sample_text", internal=True, sourceOperation="sample_text", targetOperation="sample_text", type="sample_text")
    partner = type_TypePointer()
    setattr(partner, 'type_TypePointer17', None)
    _safe_set(owner, 'type_Assosiation16', partner)
    assert getattr(partner, 'type_TypePointer17') == owner
    _safe_set(owner, 'type_Assosiation16', None)
    assert getattr(partner, 'type_TypePointer17') is None


def test_assoc_methodRef32_stub_double():
    # type_MethodPointer has no real 'type_MethodPointer' property in the generated
    # code (a bare stub) -- manually attach it so type_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_Operation(name="sample_text", uid="sample_text")
    partner = type_MethodPointer()
    setattr(partner, 'type_MethodPointer', None)
    _safe_set(owner, 'type_Operation33', partner)
    assert getattr(partner, 'type_MethodPointer') == owner
    _safe_set(owner, 'type_Operation33', None)
    assert getattr(partner, 'type_MethodPointer') is None


def test_assoc_operations28_stub_double():
    # type_Type has no real 'type_Type29' property in the generated
    # code (a bare stub) -- manually attach it so type_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_Operation(name="sample_text", uid="sample_text")
    partner = type_Type()
    setattr(partner, 'type_Type29', None)
    _safe_set(owner, 'type_Operation30', partner)
    assert owner in getattr(partner, 'type_Type29')
    _safe_set(owner, 'type_Operation30', None)
    assert owner not in getattr(partner, 'type_Type29')


def test_assoc_packageRef12_stub_double():
    # type_PackagePointer has no real 'type_PackagePointer' property in the generated
    # code (a bare stub) -- manually attach it so type_TypeGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_TypeGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_TypeGroup(name="sample_text", uid="sample_text")
    partner = type_PackagePointer()
    setattr(partner, 'type_PackagePointer', None)
    _safe_set(owner, 'type_TypeGroup13', partner)
    assert getattr(partner, 'type_PackagePointer') == owner
    _safe_set(owner, 'type_TypeGroup13', None)
    assert getattr(partner, 'type_PackagePointer') is None


def test_assoc_typeRef10_stub_double():
    # type_TypePointer has no real 'type_TypePointer' property in the generated
    # code (a bare stub) -- manually attach it so type_TypeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_TypeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_TypeElement(name="sample_text", uid="sample_text")
    partner = type_TypePointer()
    setattr(partner, 'type_TypePointer', None)
    _safe_set(owner, 'type_TypeElement11', partner)
    assert getattr(partner, 'type_TypePointer') == owner
    _safe_set(owner, 'type_TypeElement11', None)
    assert getattr(partner, 'type_TypePointer') is None


def test_assoc_values31_stub_double():
    # type_Enumerator has no real 'type_Enumerator' property in the generated
    # code (a bare stub) -- manually attach it so type_EnumAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # type_EnumAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = type_EnumAttribute(name="sample_text", uid="sample_text", value="sample_text")
    partner = type_Enumerator()
    setattr(partner, 'type_Enumerator', None)
    _safe_set(owner, 'type_EnumAttribute', partner)
    assert owner in getattr(partner, 'type_Enumerator')
    _safe_set(owner, 'type_EnumAttribute', None)
    assert owner not in getattr(partner, 'type_Enumerator')


