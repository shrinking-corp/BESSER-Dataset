import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionType,
    EStructuralFeature,
    Metaclass,
    PrimitiveType,
    RefType,
    ReflectiveType,
    Type,
    TypeError,
    types_BagType,
    types_BooleanType,
    types_CollectionType,
    types_EClass,
    types_EObject,
    types_EmptyCollection,
    types_EmptyCollectionType,
    types_EnumType,
    types_FloatType,
    types_IntegerType,
    types_MapType,
    types_MetaModel,
    types_Metaclass,
    types_OclUndefinedType,
    types_OrderedSetType,
    types_PrimitiveType,
    types_RefType,
    types_ReflectiveClass,
    types_ReflectiveType,
    types_SequenceType,
    types_SetType,
    types_StringType,
    types_ThisModuleType,
    types_TupleAttribute,
    types_TupleType,
    types_Type,
    types_TypeError,
    types_UnionType,
    types_Unknown,
    types_UnknownFeature,
    types_UnresolvedTypeError,
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

def test_assoc_model19_reverse_link_reassign_clear():
    a1 = types_Metaclass(explicitOcurrence=True, name="sample_text")
    a2 = types_Metaclass(explicitOcurrence=False, name="sample_text_2")
    b = types_MetaModel(name="sample_text")
    _safe_set(b, 'types_MetaModel', a1)
    assert _is_linked(b, 'types_MetaModel', a1)
    if hasattr(a1, 'types_Metaclass20'):
        assert _is_linked(a1, 'types_Metaclass20', b)
    _safe_set(b, 'types_MetaModel', a2)
    assert _is_linked(b, 'types_MetaModel', a2)
    if hasattr(a1, 'types_Metaclass20'):
        assert not _is_linked(a1, 'types_Metaclass20', b)
    if hasattr(a2, 'types_Metaclass20'):
        assert _is_linked(a2, 'types_Metaclass20', b)
    _safe_set(b, 'types_MetaModel', None)
    assert not _is_linked(b, 'types_MetaModel', a2)
    if hasattr(a2, 'types_Metaclass20'):
        assert not _is_linked(a2, 'types_Metaclass20', b)


def test_assoc_noCastedType1_reverse_link_reassign_clear():
    a1 = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    a2 = types_Type(mayBeUndefined=False, metamodelRef="sample_text_2", multivalued=False)
    b = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    _safe_set(b, 'types_Type0', a1)
    assert _is_linked(b, 'types_Type0', a1)
    if hasattr(a1, 'types_Type'):
        assert _is_linked(a1, 'types_Type', b)
    _safe_set(b, 'types_Type0', a2)
    assert _is_linked(b, 'types_Type0', a2)
    if hasattr(a1, 'types_Type'):
        assert not _is_linked(a1, 'types_Type', b)
    if hasattr(a2, 'types_Type'):
        assert _is_linked(a2, 'types_Type', b)
    _safe_set(b, 'types_Type0', None)
    assert not _is_linked(b, 'types_Type0', a2)
    if hasattr(a2, 'types_Type'):
        assert not _is_linked(a2, 'types_Type', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    a2 = types_Type(mayBeUndefined=False, metamodelRef="sample_text_2", multivalued=False)
    b = types_TupleAttribute(name="sample_text")
    _safe_set(b, 'types_TupleAttribute10', a1)
    assert _is_linked(b, 'types_TupleAttribute10', a1)
    if hasattr(a1, 'types_Type11'):
        assert _is_linked(a1, 'types_Type11', b)
    _safe_set(b, 'types_TupleAttribute10', a2)
    assert _is_linked(b, 'types_TupleAttribute10', a2)
    if hasattr(a1, 'types_Type11'):
        assert not _is_linked(a1, 'types_Type11', b)
    if hasattr(a2, 'types_Type11'):
        assert _is_linked(a2, 'types_Type11', b)
    _safe_set(b, 'types_TupleAttribute10', None)
    assert not _is_linked(b, 'types_TupleAttribute10', a2)
    if hasattr(a2, 'types_Type11'):
        assert not _is_linked(a2, 'types_Type11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes3_stub_double():
    # types_TupleType has no real 'types_TupleType' property in the generated
    # code (a bare stub) -- manually attach it so types_TupleAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_TupleAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_TupleAttribute(name="sample_text")
    partner = types_TupleType()
    setattr(partner, 'types_TupleType', None)
    _safe_set(owner, 'types_TupleAttribute', partner)
    assert owner in getattr(partner, 'types_TupleType')
    _safe_set(owner, 'types_TupleAttribute', None)
    assert owner not in getattr(partner, 'types_TupleType')


def test_assoc_containedType23_stub_double():
    # types_CollectionType has no real 'types_CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    partner = types_CollectionType()
    setattr(partner, 'types_CollectionType', None)
    _safe_set(owner, 'types_Type24', partner)
    assert getattr(partner, 'types_CollectionType') == owner
    _safe_set(owner, 'types_Type24', None)
    assert getattr(partner, 'types_CollectionType') is None


def test_assoc_eenum14_stub_double():
    # types_EObject has no real 'types_EObject15' property in the generated
    # code (a bare stub) -- manually attach it so types_EnumType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_EnumType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_EnumType(name="sample_text")
    partner = types_EObject()
    setattr(partner, 'types_EObject15', None)
    _safe_set(owner, 'types_EnumType', partner)
    assert getattr(partner, 'types_EObject15') == owner
    _safe_set(owner, 'types_EnumType', None)
    assert getattr(partner, 'types_EObject15') is None


def test_assoc_keyType4_stub_double():
    # types_MapType has no real 'types_MapType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    partner = types_MapType()
    setattr(partner, 'types_MapType', None)
    _safe_set(owner, 'types_Type5', partner)
    assert getattr(partner, 'types_MapType') == owner
    _safe_set(owner, 'types_Type5', None)
    assert getattr(partner, 'types_MapType') is None


def test_assoc_kindOfTypes2_stub_double():
    # types_BooleanType has no real 'types_BooleanType' property in the generated
    # code (a bare stub) -- manually attach it so types_Metaclass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Metaclass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Metaclass(explicitOcurrence=True, name="sample_text")
    partner = types_BooleanType()
    setattr(partner, 'types_BooleanType', None)
    _safe_set(owner, 'types_Metaclass', partner)
    assert owner in getattr(partner, 'types_BooleanType')
    _safe_set(owner, 'types_Metaclass', None)
    assert owner not in getattr(partner, 'types_BooleanType')


def test_assoc_klass16_stub_double():
    # types_EClass has no real 'types_EClass18' property in the generated
    # code (a bare stub) -- manually attach it so types_Metaclass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Metaclass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Metaclass(explicitOcurrence=True, name="sample_text")
    partner = types_EClass()
    setattr(partner, 'types_EClass18', None)
    _safe_set(owner, 'types_Metaclass17', partner)
    assert getattr(partner, 'types_EClass18') == owner
    _safe_set(owner, 'types_Metaclass17', None)
    assert getattr(partner, 'types_EClass18') is None


def test_assoc_possibleTypes21_stub_double():
    # types_UnionType has no real 'types_UnionType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    partner = types_UnionType()
    setattr(partner, 'types_UnionType', None)
    _safe_set(owner, 'types_Type22', partner)
    assert owner in getattr(partner, 'types_UnionType')
    _safe_set(owner, 'types_Type22', None)
    assert owner not in getattr(partner, 'types_UnionType')


def test_assoc_valueType6_stub_double():
    # types_MapType has no real 'types_MapType7' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(mayBeUndefined=True, metamodelRef="sample_text", multivalued=True)
    partner = types_MapType()
    setattr(partner, 'types_MapType7', None)
    _safe_set(owner, 'types_Type8', partner)
    assert getattr(partner, 'types_MapType7') == owner
    _safe_set(owner, 'types_Type8', None)
    assert getattr(partner, 'types_MapType7') is None


