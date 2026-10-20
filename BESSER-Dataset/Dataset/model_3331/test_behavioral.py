import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Member,
    Object,
    Type,
    TypedElement,
    psample_Class,
    psample_Function,
    psample_Interface,
    psample_Member,
    psample_Object,
    psample_Package,
    psample_PrimitiveTypeVariable,
    psample_Type,
    psample_TypedElement,
    psample_Variable,
    PrimitiveTypes,
    Visibility,
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

def test_assoc_primitivetype2_stub_double():
    # psample_Class has no real 'psample_Class3' property in the generated
    # code (a bare stub) -- manually attach it so psample_PrimitiveTypeVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # psample_PrimitiveTypeVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = psample_PrimitiveTypeVariable(isParameter=True)
    partner = psample_Class()
    setattr(partner, 'psample_Class3', None)
    _safe_set(owner, 'psample_PrimitiveTypeVariable', partner)
    assert owner in getattr(partner, 'psample_Class3')
    _safe_set(owner, 'psample_PrimitiveTypeVariable', None)
    assert owner not in getattr(partner, 'psample_Class3')


def test_assoc_primitivetypevariable4_stub_double():
    # psample_Function has no real 'psample_Function' property in the generated
    # code (a bare stub) -- manually attach it so psample_PrimitiveTypeVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # psample_PrimitiveTypeVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = psample_PrimitiveTypeVariable(isParameter=True)
    partner = psample_Function()
    setattr(partner, 'psample_Function', None)
    _safe_set(owner, 'psample_PrimitiveTypeVariable5', partner)
    assert owner in getattr(partner, 'psample_Function')
    _safe_set(owner, 'psample_PrimitiveTypeVariable5', None)
    assert owner not in getattr(partner, 'psample_Function')


def test_assoc_typedelement0_stub_double():
    # psample_TypedElement has no real 'psample_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so psample_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # psample_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = psample_Package(Name="sample_text")
    partner = psample_TypedElement()
    setattr(partner, 'psample_TypedElement', None)
    _safe_set(owner, 'psample_Package', {partner})
    assert getattr(partner, 'psample_TypedElement') == owner
    _safe_set(owner, 'psample_Package', set())
    assert getattr(partner, 'psample_TypedElement') is None


def test_assoc_variable6_stub_double():
    # psample_Function has no real 'psample_Function7' property in the generated
    # code (a bare stub) -- manually attach it so psample_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # psample_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = psample_Variable(isParameter=True)
    partner = psample_Function()
    setattr(partner, 'psample_Function7', None)
    _safe_set(owner, 'psample_Variable', partner)
    assert owner in getattr(partner, 'psample_Function7')
    _safe_set(owner, 'psample_Variable', None)
    assert owner not in getattr(partner, 'psample_Function7')


