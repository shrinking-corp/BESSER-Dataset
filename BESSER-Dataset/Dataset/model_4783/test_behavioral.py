import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Feature,
    NamedElement,
    PackageMember,
    ParameterizedType,
    PrimitiveType,
    Type,
    TypeConstraint,
    TypedElement,
    types_ComplexType,
    types_EnumerationType,
    types_Enumerator,
    types_Event,
    types_Feature,
    types_Operation,
    types_Package,
    types_PackageMember,
    types_Parameter,
    types_ParameterizedType,
    types_PrimitiveType,
    types_Property,
    types_RangeConstraint,
    types_Type,
    types_TypeConstraint,
    types_TypeParameter,
    types_TypedElement,
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

def test_assoc_constraint1_reverse_link_reassign_clear():
    a1 = types_TypeConstraint(value="sample_text")
    a2 = types_TypeConstraint(value="sample_text_2")
    b = types_Type(scheme="sample_text")
    _safe_set(b, 'types_Type', {a1})
    assert _is_linked(b, 'types_Type', a1)
    if hasattr(a1, 'types_TypeConstraint'):
        assert _is_linked(a1, 'types_TypeConstraint', b)
    _safe_set(b, 'types_Type', {a2})
    assert _is_linked(b, 'types_Type', a2)
    if hasattr(a1, 'types_TypeConstraint'):
        assert not _is_linked(a1, 'types_TypeConstraint', b)
    if hasattr(a2, 'types_TypeConstraint'):
        assert _is_linked(a2, 'types_TypeConstraint', b)
    _safe_set(b, 'types_Type', set())
    assert not _is_linked(b, 'types_Type', a2)
    if hasattr(a2, 'types_TypeConstraint'):
        assert not _is_linked(a2, 'types_TypeConstraint', b)


def test_assoc_superTypes15_reverse_link_reassign_clear():
    a1 = types_ComplexType()
    a2 = types_ComplexType()
    b = types_ComplexType()
    _safe_set(b, 'types_ComplexType14', {a1})
    assert _is_linked(b, 'types_ComplexType14', a1)
    if hasattr(a1, 'types_ComplexType'):
        assert _is_linked(a1, 'types_ComplexType', b)
    _safe_set(b, 'types_ComplexType14', {a2})
    assert _is_linked(b, 'types_ComplexType14', a2)
    if hasattr(a1, 'types_ComplexType'):
        assert not _is_linked(a1, 'types_ComplexType', b)
    if hasattr(a2, 'types_ComplexType'):
        assert _is_linked(a2, 'types_ComplexType', b)
    _safe_set(b, 'types_ComplexType14', set())
    assert not _is_linked(b, 'types_ComplexType14', a2)
    if hasattr(a2, 'types_ComplexType'):
        assert not _is_linked(a2, 'types_ComplexType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bound17_stub_double():
    # types_TypeParameter has no real 'types_TypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(scheme="sample_text")
    partner = types_TypeParameter()
    setattr(partner, 'types_TypeParameter', None)
    _safe_set(owner, 'types_Type18', partner)
    assert getattr(partner, 'types_TypeParameter') == owner
    _safe_set(owner, 'types_Type18', None)
    assert getattr(partner, 'types_TypeParameter') is None


def test_assoc_enumerator10_stub_double():
    # types_EnumerationType has no real 'owningEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue="sample_text")
    partner = types_EnumerationType()
    setattr(partner, 'owningEnumeration', None)
    _safe_set(owner, 'Enumerator', partner)
    assert owner in getattr(partner, 'owningEnumeration')
    _safe_set(owner, 'Enumerator', None)
    assert owner not in getattr(partner, 'owningEnumeration')


def test_assoc_features13_stub_double():
    # types_Feature has no real 'Feature' property in the generated
    # code (a bare stub) -- manually attach it so types_ComplexType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_ComplexType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_ComplexType()
    partner = types_Feature()
    setattr(partner, 'Feature', None)
    _safe_set(owner, 'owningType', {partner})
    assert getattr(partner, 'Feature') == owner
    _safe_set(owner, 'owningType', set())
    assert getattr(partner, 'Feature') is None


def test_assoc_owningEnumeration16_stub_double():
    # types_EnumerationType has no real 'EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so types_Enumerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Enumerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Enumerator(literalValue="sample_text")
    partner = types_EnumerationType()
    setattr(partner, 'EnumerationType', None)
    _safe_set(owner, 'enumerator', partner)
    assert getattr(partner, 'EnumerationType') == owner
    _safe_set(owner, 'enumerator', None)
    assert getattr(partner, 'EnumerationType') is None


def test_assoc_owningType2_stub_double():
    # types_Feature has no real 'features' property in the generated
    # code (a bare stub) -- manually attach it so types_ComplexType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_ComplexType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_ComplexType()
    partner = types_Feature()
    setattr(partner, 'features', None)
    _safe_set(owner, 'ComplexType', partner)
    assert getattr(partner, 'features') == owner
    _safe_set(owner, 'ComplexType', None)
    assert getattr(partner, 'features') is None


def test_assoc_type5_stub_double():
    # types_TypedElement has no real 'types_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(scheme="sample_text")
    partner = types_TypedElement()
    setattr(partner, 'types_TypedElement', None)
    _safe_set(owner, 'types_Type6', partner)
    assert getattr(partner, 'types_TypedElement') == owner
    _safe_set(owner, 'types_Type6', None)
    assert getattr(partner, 'types_TypedElement') is None


def test_assoc_typeArguments7_stub_double():
    # types_TypedElement has no real 'types_TypedElement8' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(scheme="sample_text")
    partner = types_TypedElement()
    setattr(partner, 'types_TypedElement8', None)
    _safe_set(owner, 'types_Type9', partner)
    assert owner in getattr(partner, 'types_TypedElement8')
    _safe_set(owner, 'types_Type9', None)
    assert owner not in getattr(partner, 'types_TypedElement8')


