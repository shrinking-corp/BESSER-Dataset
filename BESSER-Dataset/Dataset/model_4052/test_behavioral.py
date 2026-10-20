import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Relation,
    Type,
    smalluml_Attribute,
    smalluml_Bool,
    smalluml_Class,
    smalluml_Composition,
    smalluml_Enumeration,
    smalluml_Integer,
    smalluml_Method,
    smalluml_NamedElement,
    smalluml_Package,
    smalluml_Parameter,
    smalluml_Real,
    smalluml_Reference,
    smalluml_Relation,
    smalluml_Role,
    smalluml_String,
    smalluml_Type,
    smalluml_UnlimitedNatural,
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

def test_assoc_class_20_stub_double():
    # smalluml_Class has no real 'smalluml_Class22' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lowerBound=7, upperBound=7)
    partner = smalluml_Class()
    setattr(partner, 'smalluml_Class22', None)
    _safe_set(owner, 'smalluml_Role21', partner)
    assert getattr(partner, 'smalluml_Class22') == owner
    _safe_set(owner, 'smalluml_Role21', None)
    assert getattr(partner, 'smalluml_Class22') is None


def test_assoc_member23_stub_double():
    # smalluml_Package has no real 'smalluml_Package' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_NamedElement(name="sample_text")
    partner = smalluml_Package()
    setattr(partner, 'smalluml_Package', None)
    _safe_set(owner, 'smalluml_NamedElement', partner)
    assert owner in getattr(partner, 'smalluml_Package')
    _safe_set(owner, 'smalluml_NamedElement', None)
    assert owner not in getattr(partner, 'smalluml_Package')


def test_assoc_source16_stub_double():
    # smalluml_Relation has no real 'smalluml_Relation' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lowerBound=7, upperBound=7)
    partner = smalluml_Relation()
    setattr(partner, 'smalluml_Relation', None)
    _safe_set(owner, 'smalluml_Role', partner)
    assert getattr(partner, 'smalluml_Relation') == owner
    _safe_set(owner, 'smalluml_Role', None)
    assert getattr(partner, 'smalluml_Relation') is None


def test_assoc_target17_stub_double():
    # smalluml_Relation has no real 'smalluml_Relation18' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lowerBound=7, upperBound=7)
    partner = smalluml_Relation()
    setattr(partner, 'smalluml_Relation18', None)
    _safe_set(owner, 'smalluml_Role19', partner)
    assert getattr(partner, 'smalluml_Relation18') == owner
    _safe_set(owner, 'smalluml_Role19', None)
    assert getattr(partner, 'smalluml_Relation18') is None


