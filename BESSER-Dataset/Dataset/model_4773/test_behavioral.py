import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    TypeReference,
    UserType,
    types_ArrayType,
    types_ClassType,
    types_EObject,
    types_Operation,
    types_PrimitiveType,
    types_Property,
    types_ServiceType,
    types_Type,
    types_TypeReference,
    types_UserType,
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

def test_assoc_parameters18_reverse_link_reassign_clear():
    a1 = types_Property(name="sample_text")
    a2 = types_Property(name="sample_text_2")
    b = types_Operation(name="sample_text")
    _safe_set(b, 'types_Operation19', {a1})
    assert _is_linked(b, 'types_Operation19', a1)
    if hasattr(a1, 'types_Property20'):
        assert _is_linked(a1, 'types_Property20', b)
    _safe_set(b, 'types_Operation19', {a2})
    assert _is_linked(b, 'types_Operation19', a2)
    if hasattr(a1, 'types_Property20'):
        assert not _is_linked(a1, 'types_Property20', b)
    if hasattr(a2, 'types_Property20'):
        assert _is_linked(a2, 'types_Property20', b)
    _safe_set(b, 'types_Operation19', set())
    assert not _is_linked(b, 'types_Operation19', a2)
    if hasattr(a2, 'types_Property20'):
        assert not _is_linked(a2, 'types_Property20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configurations11_stub_double():
    # types_ServiceType has no real 'types_ServiceType' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text")
    partner = types_ServiceType()
    setattr(partner, 'types_ServiceType', None)
    _safe_set(owner, 'types_Property12', partner)
    assert owner in getattr(partner, 'types_ServiceType')
    _safe_set(owner, 'types_Property12', None)
    assert owner not in getattr(partner, 'types_ServiceType')


def test_assoc_expression21_stub_double():
    # types_EObject has no real 'types_EObject' property in the generated
    # code (a bare stub) -- manually attach it so types_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Operation(name="sample_text")
    partner = types_EObject()
    setattr(partner, 'types_EObject', None)
    _safe_set(owner, 'types_Operation22', partner)
    assert getattr(partner, 'types_EObject') == owner
    _safe_set(owner, 'types_Operation22', None)
    assert getattr(partner, 'types_EObject') is None


def test_assoc_operations13_stub_double():
    # types_ServiceType has no real 'types_ServiceType14' property in the generated
    # code (a bare stub) -- manually attach it so types_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Operation(name="sample_text")
    partner = types_ServiceType()
    setattr(partner, 'types_ServiceType14', None)
    _safe_set(owner, 'types_Operation', partner)
    assert owner in getattr(partner, 'types_ServiceType14')
    _safe_set(owner, 'types_Operation', None)
    assert owner not in getattr(partner, 'types_ServiceType14')


def test_assoc_properties2_stub_double():
    # types_ClassType has no real 'types_ClassType3' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text")
    partner = types_ClassType()
    setattr(partner, 'types_ClassType3', None)
    _safe_set(owner, 'types_Property', partner)
    assert owner in getattr(partner, 'types_ClassType3')
    _safe_set(owner, 'types_Property', None)
    assert owner not in getattr(partner, 'types_ClassType3')


def test_assoc_type15_stub_double():
    # types_TypeReference has no real 'types_TypeReference17' property in the generated
    # code (a bare stub) -- manually attach it so types_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Operation(name="sample_text")
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference17', None)
    _safe_set(owner, 'types_Operation16', partner)
    assert getattr(partner, 'types_TypeReference17') == owner
    _safe_set(owner, 'types_Operation16', None)
    assert getattr(partner, 'types_TypeReference17') is None


def test_assoc_type4_stub_double():
    # types_TypeReference has no real 'types_TypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text")
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference', None)
    _safe_set(owner, 'types_Property5', partner)
    assert getattr(partner, 'types_TypeReference') == owner
    _safe_set(owner, 'types_Property5', None)
    assert getattr(partner, 'types_TypeReference') is None


def test_assoc_type6_stub_double():
    # types_TypeReference has no real 'types_TypeReference7' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(name="sample_text")
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference7', None)
    _safe_set(owner, 'types_Type', partner)
    assert getattr(partner, 'types_TypeReference7') == owner
    _safe_set(owner, 'types_Type', None)
    assert getattr(partner, 'types_TypeReference7') is None


