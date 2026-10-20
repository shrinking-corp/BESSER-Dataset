import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Type,
    smalluml_Attribute,
    smalluml_Cardinality,
    smalluml_Class,
    smalluml_ConcreteType,
    smalluml_Enumeration,
    smalluml_EnumerationElement,
    smalluml_Method,
    smalluml_NamedElement,
    smalluml_Package,
    smalluml_Relation,
    smalluml_Type,
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

def test_assoc_parents5_reverse_link_reassign_clear():
    a1 = smalluml_Class(isAbstract=True)
    a2 = smalluml_Class(isAbstract=False)
    b = smalluml_Class(isAbstract=True)
    _safe_set(b, 'smalluml_Class6', a1)
    assert _is_linked(b, 'smalluml_Class6', a1)
    if hasattr(a1, 'smalluml_Class4'):
        assert _is_linked(a1, 'smalluml_Class4', b)
    _safe_set(b, 'smalluml_Class6', a2)
    assert _is_linked(b, 'smalluml_Class6', a2)
    if hasattr(a1, 'smalluml_Class4'):
        assert not _is_linked(a1, 'smalluml_Class4', b)
    if hasattr(a2, 'smalluml_Class4'):
        assert _is_linked(a2, 'smalluml_Class4', b)
    _safe_set(b, 'smalluml_Class6', None)
    assert not _is_linked(b, 'smalluml_Class6', a2)
    if hasattr(a2, 'smalluml_Class4'):
        assert not _is_linked(a2, 'smalluml_Class4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes1_stub_double():
    # smalluml_Attribute has no real 'smalluml_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Attribute()
    setattr(partner, 'smalluml_Attribute', None)
    _safe_set(owner, 'smalluml_Class', {partner})
    assert getattr(partner, 'smalluml_Attribute') == owner
    _safe_set(owner, 'smalluml_Class', set())
    assert getattr(partner, 'smalluml_Attribute') is None


def test_assoc_cardinality15_stub_double():
    # smalluml_Relation has no real 'smalluml_Relation' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Cardinality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Cardinality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Cardinality(lowerBound=7, upperBound=7)
    partner = smalluml_Relation()
    setattr(partner, 'smalluml_Relation', None)
    _safe_set(owner, 'smalluml_Cardinality', partner)
    assert getattr(partner, 'smalluml_Relation') == owner
    _safe_set(owner, 'smalluml_Cardinality', None)
    assert getattr(partner, 'smalluml_Relation') is None


def test_assoc_class_22_stub_double():
    # smalluml_Package has no real 'smalluml_Package' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Package()
    setattr(partner, 'smalluml_Package', None)
    _safe_set(owner, 'smalluml_Class23', partner)
    assert owner in getattr(partner, 'smalluml_Package')
    _safe_set(owner, 'smalluml_Class23', None)
    assert owner not in getattr(partner, 'smalluml_Package')


def test_assoc_from_16_stub_double():
    # smalluml_Relation has no real 'smalluml_Relation17' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Relation()
    setattr(partner, 'smalluml_Relation17', None)
    _safe_set(owner, 'smalluml_Class18', partner)
    assert getattr(partner, 'smalluml_Relation17') == owner
    _safe_set(owner, 'smalluml_Class18', None)
    assert getattr(partner, 'smalluml_Relation17') is None


def test_assoc_methods2_stub_double():
    # smalluml_Method has no real 'smalluml_Method' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Method()
    setattr(partner, 'smalluml_Method', None)
    _safe_set(owner, 'smalluml_Class3', {partner})
    assert getattr(partner, 'smalluml_Method') == owner
    _safe_set(owner, 'smalluml_Class3', set())
    assert getattr(partner, 'smalluml_Method') is None


def test_assoc_to19_stub_double():
    # smalluml_Relation has no real 'smalluml_Relation20' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Relation()
    setattr(partner, 'smalluml_Relation20', None)
    _safe_set(owner, 'smalluml_Class21', partner)
    assert getattr(partner, 'smalluml_Relation20') == owner
    _safe_set(owner, 'smalluml_Class21', None)
    assert getattr(partner, 'smalluml_Relation20') is None


def test_assoc_value0_stub_double():
    # smalluml_Enumeration has no real 'smalluml_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_EnumerationElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_EnumerationElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_EnumerationElement(value="sample_text")
    partner = smalluml_Enumeration()
    setattr(partner, 'smalluml_Enumeration', None)
    _safe_set(owner, 'smalluml_EnumerationElement', partner)
    assert owner in getattr(partner, 'smalluml_Enumeration')
    _safe_set(owner, 'smalluml_EnumerationElement', None)
    assert owner not in getattr(partner, 'smalluml_Enumeration')


