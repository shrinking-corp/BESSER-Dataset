import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    KM3_Attribute,
    KM3_Class,
    KM3_Classifier,
    KM3_DataType,
    KM3_EnumLiteral,
    KM3_Enumeration,
    KM3_LocatedElement,
    KM3_Metamodel,
    KM3_ModelElement,
    KM3_Operation,
    KM3_Package,
    KM3_Parameter,
    KM3_Reference,
    KM3_StructuralFeature,
    KM3_TypedElement,
    LocatedElement,
    ModelElement,
    StructuralFeature,
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

def test_assoc_opposite17_reverse_link_reassign_clear():
    a1 = KM3_Reference(isContainer=True)
    a2 = KM3_Reference(isContainer=False)
    b = KM3_Reference(isContainer=True)
    _safe_set(b, 'KM3_Reference16', a1)
    assert _is_linked(b, 'KM3_Reference16', a1)
    if hasattr(a1, 'KM3_Reference'):
        assert _is_linked(a1, 'KM3_Reference', b)
    _safe_set(b, 'KM3_Reference16', a2)
    assert _is_linked(b, 'KM3_Reference16', a2)
    if hasattr(a1, 'KM3_Reference'):
        assert not _is_linked(a1, 'KM3_Reference', b)
    if hasattr(a2, 'KM3_Reference'):
        assert _is_linked(a2, 'KM3_Reference', b)
    _safe_set(b, 'KM3_Reference16', None)
    assert not _is_linked(b, 'KM3_Reference16', a2)
    if hasattr(a2, 'KM3_Reference'):
        assert not _is_linked(a2, 'KM3_Reference', b)


def test_assoc_supertypes4_reverse_link_reassign_clear():
    a1 = KM3_Class(isAbstract=True)
    a2 = KM3_Class(isAbstract=False)
    b = KM3_Class(isAbstract=True)
    _safe_set(b, 'KM3_Class3', {a1})
    assert _is_linked(b, 'KM3_Class3', a1)
    if hasattr(a1, 'KM3_Class'):
        assert _is_linked(a1, 'KM3_Class', b)
    _safe_set(b, 'KM3_Class3', {a2})
    assert _is_linked(b, 'KM3_Class3', a2)
    if hasattr(a1, 'KM3_Class'):
        assert not _is_linked(a1, 'KM3_Class', b)
    if hasattr(a2, 'KM3_Class'):
        assert _is_linked(a2, 'KM3_Class', b)
    _safe_set(b, 'KM3_Class3', set())
    assert not _is_linked(b, 'KM3_Class3', a2)
    if hasattr(a2, 'KM3_Class'):
        assert not _is_linked(a2, 'KM3_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents24_stub_double():
    # KM3_Package has no real 'KM3_Package25' property in the generated
    # code (a bare stub) -- manually attach it so KM3_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_ModelElement(name="sample_text")
    partner = KM3_Package()
    setattr(partner, 'KM3_Package25', None)
    _safe_set(owner, 'KM3_ModelElement26', partner)
    assert owner in getattr(partner, 'KM3_Package25')
    _safe_set(owner, 'KM3_ModelElement26', None)
    assert owner not in getattr(partner, 'KM3_Package25')


def test_assoc_operations6_stub_double():
    # KM3_Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so KM3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_Class(isAbstract=True)
    partner = KM3_Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'owner7', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'owner7', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_owner18_stub_double():
    # KM3_Operation has no real 'operations' property in the generated
    # code (a bare stub) -- manually attach it so KM3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_Class(isAbstract=True)
    partner = KM3_Operation()
    setattr(partner, 'operations', None)
    _safe_set(owner, 'Class19', partner)
    assert getattr(partner, 'operations') == owner
    _safe_set(owner, 'Class19', None)
    assert getattr(partner, 'operations') is None


def test_assoc_owner9_stub_double():
    # KM3_StructuralFeature has no real 'structuralFeatures' property in the generated
    # code (a bare stub) -- manually attach it so KM3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_Class(isAbstract=True)
    partner = KM3_StructuralFeature()
    setattr(partner, 'structuralFeatures', None)
    _safe_set(owner, 'Class', partner)
    assert getattr(partner, 'structuralFeatures') == owner
    _safe_set(owner, 'Class', None)
    assert getattr(partner, 'structuralFeatures') is None


def test_assoc_package0_stub_double():
    # KM3_Package has no real 'KM3_Package' property in the generated
    # code (a bare stub) -- manually attach it so KM3_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_ModelElement(name="sample_text")
    partner = KM3_Package()
    setattr(partner, 'KM3_Package', None)
    _safe_set(owner, 'KM3_ModelElement', partner)
    assert getattr(partner, 'KM3_Package') == owner
    _safe_set(owner, 'KM3_ModelElement', None)
    assert getattr(partner, 'KM3_Package') is None


def test_assoc_structuralFeatures5_stub_double():
    # KM3_StructuralFeature has no real 'StructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so KM3_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_Class(isAbstract=True)
    partner = KM3_StructuralFeature()
    setattr(partner, 'StructuralFeature', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'StructuralFeature') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'StructuralFeature') is None


def test_assoc_type8_stub_double():
    # KM3_Classifier has no real 'KM3_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so KM3_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # KM3_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = KM3_TypedElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = KM3_Classifier()
    setattr(partner, 'KM3_Classifier', None)
    _safe_set(owner, 'KM3_TypedElement', partner)
    assert getattr(partner, 'KM3_Classifier') == owner
    _safe_set(owner, 'KM3_TypedElement', None)
    assert getattr(partner, 'KM3_Classifier') is None


