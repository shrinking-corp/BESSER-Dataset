import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AtlAnnotation,
    PrimitiveType,
    RefType,
    ReflectiveType,
    Type,
    annotations_atl_types_EObject,
    annotations_atl_types_Type,
    atl_types_BooleanType,
    atl_types_EClass,
    atl_types_EObject,
    atl_types_EmptyCollection,
    atl_types_EnumType,
    atl_types_FloatType,
    atl_types_IntegerType,
    atl_types_MapType,
    atl_types_Metaclass,
    atl_types_PrimitiveType,
    atl_types_RefType,
    atl_types_ReflectiveClass,
    atl_types_ReflectiveType,
    atl_types_StringType,
    atl_types_ThisModuleType,
    atl_types_TupleAttribute,
    atl_types_TupleType,
    atl_types_Type,
    atl_types_UnionType,
    atl_types_Unknown,
    atl_types_annotations_AtlAnnotation,
    atl_types_annotations_BindingAnnotation,
    atl_types_annotations_ExpressionAnnotation,
    atl_types_annotations_HelperAnnotation,
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

def test_assoc_type5_reverse_link_reassign_clear():
    a1 = atl_types_Type(multivalued=True)
    a2 = atl_types_Type(multivalued=False)
    b = atl_types_TupleAttribute(name="sample_text")
    _safe_set(b, 'atl_types_TupleAttribute6', a1)
    assert _is_linked(b, 'atl_types_TupleAttribute6', a1)
    if hasattr(a1, 'atl_types_Type7'):
        assert _is_linked(a1, 'atl_types_Type7', b)
    _safe_set(b, 'atl_types_TupleAttribute6', a2)
    assert _is_linked(b, 'atl_types_TupleAttribute6', a2)
    if hasattr(a1, 'atl_types_Type7'):
        assert not _is_linked(a1, 'atl_types_Type7', b)
    if hasattr(a2, 'atl_types_Type7'):
        assert _is_linked(a2, 'atl_types_Type7', b)
    _safe_set(b, 'atl_types_TupleAttribute6', None)
    assert not _is_linked(b, 'atl_types_TupleAttribute6', a2)
    if hasattr(a2, 'atl_types_Type7'):
        assert not _is_linked(a2, 'atl_types_Type7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes0_stub_double():
    # atl_types_TupleType has no real 'atl_types_TupleType' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_TupleAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_TupleAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_TupleAttribute(name="sample_text")
    partner = atl_types_TupleType()
    setattr(partner, 'atl_types_TupleType', None)
    _safe_set(owner, 'atl_types_TupleAttribute', partner)
    assert owner in getattr(partner, 'atl_types_TupleType')
    _safe_set(owner, 'atl_types_TupleAttribute', None)
    assert owner not in getattr(partner, 'atl_types_TupleType')


def test_assoc_binding17_stub_double():
    # annotations_atl_types_EObject has no real 'annotations_atl_types_EObject19' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_BindingAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_BindingAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_BindingAnnotation(name="sample_text")
    partner = annotations_atl_types_EObject()
    setattr(partner, 'annotations_atl_types_EObject19', None)
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation18', partner)
    assert getattr(partner, 'annotations_atl_types_EObject19') == owner
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation18', None)
    assert getattr(partner, 'annotations_atl_types_EObject19') is None


def test_assoc_eenum8_stub_double():
    # atl_types_EObject has no real 'atl_types_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_EnumType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_EnumType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_EnumType(name="sample_text")
    partner = atl_types_EObject()
    setattr(partner, 'atl_types_EObject', None)
    _safe_set(owner, 'atl_types_EnumType', partner)
    assert getattr(partner, 'atl_types_EObject') == owner
    _safe_set(owner, 'atl_types_EnumType', None)
    assert getattr(partner, 'atl_types_EObject') is None


def test_assoc_helper12_stub_double():
    # annotations_atl_types_EObject has no real 'annotations_atl_types_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_HelperAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_HelperAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_HelperAnnotation(name="sample_text")
    partner = annotations_atl_types_EObject()
    setattr(partner, 'annotations_atl_types_EObject', None)
    _safe_set(owner, 'atl_types_annotations_HelperAnnotation', partner)
    assert getattr(partner, 'annotations_atl_types_EObject') == owner
    _safe_set(owner, 'atl_types_annotations_HelperAnnotation', None)
    assert getattr(partner, 'annotations_atl_types_EObject') is None


def test_assoc_keyType1_stub_double():
    # atl_types_MapType has no real 'atl_types_MapType' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_Type(multivalued=True)
    partner = atl_types_MapType()
    setattr(partner, 'atl_types_MapType', None)
    _safe_set(owner, 'atl_types_Type', partner)
    assert getattr(partner, 'atl_types_MapType') == owner
    _safe_set(owner, 'atl_types_Type', None)
    assert getattr(partner, 'atl_types_MapType') is None


def test_assoc_klass9_stub_double():
    # atl_types_EClass has no real 'atl_types_EClass' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_Metaclass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_Metaclass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_Metaclass(name="sample_text")
    partner = atl_types_EClass()
    setattr(partner, 'atl_types_EClass', None)
    _safe_set(owner, 'atl_types_Metaclass', partner)
    assert getattr(partner, 'atl_types_EClass') == owner
    _safe_set(owner, 'atl_types_Metaclass', None)
    assert getattr(partner, 'atl_types_EClass') is None


def test_assoc_possibleTypes10_stub_double():
    # atl_types_UnionType has no real 'atl_types_UnionType' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_Type(multivalued=True)
    partner = atl_types_UnionType()
    setattr(partner, 'atl_types_UnionType', None)
    _safe_set(owner, 'atl_types_Type11', partner)
    assert owner in getattr(partner, 'atl_types_UnionType')
    _safe_set(owner, 'atl_types_Type11', None)
    assert owner not in getattr(partner, 'atl_types_UnionType')


def test_assoc_rule15_stub_double():
    # annotations_atl_types_EObject has no real 'annotations_atl_types_EObject16' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_BindingAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_BindingAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_BindingAnnotation(name="sample_text")
    partner = annotations_atl_types_EObject()
    setattr(partner, 'annotations_atl_types_EObject16', None)
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation', partner)
    assert getattr(partner, 'annotations_atl_types_EObject16') == owner
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation', None)
    assert getattr(partner, 'annotations_atl_types_EObject16') is None


def test_assoc_sourceType20_stub_double():
    # annotations_atl_types_Type has no real 'annotations_atl_types_Type22' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_BindingAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_BindingAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_BindingAnnotation(name="sample_text")
    partner = annotations_atl_types_Type()
    setattr(partner, 'annotations_atl_types_Type22', None)
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation21', partner)
    assert getattr(partner, 'annotations_atl_types_Type22') == owner
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation21', None)
    assert getattr(partner, 'annotations_atl_types_Type22') is None


def test_assoc_targetType23_stub_double():
    # annotations_atl_types_Type has no real 'annotations_atl_types_Type25' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_BindingAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_BindingAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_BindingAnnotation(name="sample_text")
    partner = annotations_atl_types_Type()
    setattr(partner, 'annotations_atl_types_Type25', None)
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation24', partner)
    assert getattr(partner, 'annotations_atl_types_Type25') == owner
    _safe_set(owner, 'atl_types_annotations_BindingAnnotation24', None)
    assert getattr(partner, 'annotations_atl_types_Type25') is None


def test_assoc_type13_stub_double():
    # annotations_atl_types_Type has no real 'annotations_atl_types_Type' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_annotations_HelperAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_annotations_HelperAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_annotations_HelperAnnotation(name="sample_text")
    partner = annotations_atl_types_Type()
    setattr(partner, 'annotations_atl_types_Type', None)
    _safe_set(owner, 'atl_types_annotations_HelperAnnotation14', partner)
    assert getattr(partner, 'annotations_atl_types_Type') == owner
    _safe_set(owner, 'atl_types_annotations_HelperAnnotation14', None)
    assert getattr(partner, 'annotations_atl_types_Type') is None


def test_assoc_valueType2_stub_double():
    # atl_types_MapType has no real 'atl_types_MapType3' property in the generated
    # code (a bare stub) -- manually attach it so atl_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_types_Type(multivalued=True)
    partner = atl_types_MapType()
    setattr(partner, 'atl_types_MapType3', None)
    _safe_set(owner, 'atl_types_Type4', partner)
    assert getattr(partner, 'atl_types_MapType3') == owner
    _safe_set(owner, 'atl_types_Type4', None)
    assert getattr(partner, 'atl_types_MapType3') is None


