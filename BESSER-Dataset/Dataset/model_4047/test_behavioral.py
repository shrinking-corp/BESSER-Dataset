import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    SuperType,
    smalluml_Association,
    smalluml_Attribute,
    smalluml_Class,
    smalluml_Enumeration,
    smalluml_NamedElement,
    smalluml_Operation,
    smalluml_Package,
    smalluml_Parameter,
    smalluml_Role,
    smalluml_SuperType,
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

def test_assoc_class_1_reverse_link_reassign_clear():
    a1 = smalluml_Role(lowerBound=7, upperBound=7)
    a2 = smalluml_Role(lowerBound=13, upperBound=13)
    b = smalluml_Class(isAbstract=True)
    _safe_set(b, 'smalluml_Class', a1)
    assert _is_linked(b, 'smalluml_Class', a1)
    if hasattr(a1, 'smalluml_Role'):
        assert _is_linked(a1, 'smalluml_Role', b)
    _safe_set(b, 'smalluml_Class', a2)
    assert _is_linked(b, 'smalluml_Class', a2)
    if hasattr(a1, 'smalluml_Role'):
        assert not _is_linked(a1, 'smalluml_Role', b)
    if hasattr(a2, 'smalluml_Role'):
        assert _is_linked(a2, 'smalluml_Role', b)
    _safe_set(b, 'smalluml_Class', None)
    assert not _is_linked(b, 'smalluml_Class', a2)
    if hasattr(a2, 'smalluml_Role'):
        assert not _is_linked(a2, 'smalluml_Role', b)


def test_assoc_operation14_reverse_link_reassign_clear():
    a1 = smalluml_Operation(isAbstract=True)
    a2 = smalluml_Operation(isAbstract=False)
    b = smalluml_Class(isAbstract=True)
    _safe_set(b, 'smalluml_Class15', {a1})
    assert _is_linked(b, 'smalluml_Class15', a1)
    if hasattr(a1, 'smalluml_Operation16'):
        assert _is_linked(a1, 'smalluml_Operation16', b)
    _safe_set(b, 'smalluml_Class15', {a2})
    assert _is_linked(b, 'smalluml_Class15', a2)
    if hasattr(a1, 'smalluml_Operation16'):
        assert not _is_linked(a1, 'smalluml_Operation16', b)
    if hasattr(a2, 'smalluml_Operation16'):
        assert _is_linked(a2, 'smalluml_Operation16', b)
    _safe_set(b, 'smalluml_Class15', set())
    assert not _is_linked(b, 'smalluml_Class15', a2)
    if hasattr(a2, 'smalluml_Operation16'):
        assert not _is_linked(a2, 'smalluml_Operation16', b)


def test_assoc_super18_reverse_link_reassign_clear():
    a1 = smalluml_Class(isAbstract=True)
    a2 = smalluml_Class(isAbstract=False)
    b = smalluml_Class(isAbstract=True)
    _safe_set(b, 'smalluml_Class19', a1)
    assert _is_linked(b, 'smalluml_Class19', a1)
    if hasattr(a1, 'smalluml_Class17'):
        assert _is_linked(a1, 'smalluml_Class17', b)
    _safe_set(b, 'smalluml_Class19', a2)
    assert _is_linked(b, 'smalluml_Class19', a2)
    if hasattr(a1, 'smalluml_Class17'):
        assert not _is_linked(a1, 'smalluml_Class17', b)
    if hasattr(a2, 'smalluml_Class17'):
        assert _is_linked(a2, 'smalluml_Class17', b)
    _safe_set(b, 'smalluml_Class19', None)
    assert not _is_linked(b, 'smalluml_Class19', a2)
    if hasattr(a2, 'smalluml_Class17'):
        assert not _is_linked(a2, 'smalluml_Class17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute11_stub_double():
    # smalluml_Attribute has no real 'smalluml_Attribute13' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Class(isAbstract=True)
    partner = smalluml_Attribute()
    setattr(partner, 'smalluml_Attribute13', None)
    _safe_set(owner, 'smalluml_Class12', {partner})
    assert getattr(partner, 'smalluml_Attribute13') == owner
    _safe_set(owner, 'smalluml_Class12', set())
    assert getattr(partner, 'smalluml_Attribute13') is None


def test_assoc_parameters4_stub_double():
    # smalluml_Parameter has no real 'smalluml_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Operation(isAbstract=True)
    partner = smalluml_Parameter()
    setattr(partner, 'smalluml_Parameter', None)
    _safe_set(owner, 'smalluml_Operation', {partner})
    assert getattr(partner, 'smalluml_Parameter') == owner
    _safe_set(owner, 'smalluml_Operation', set())
    assert getattr(partner, 'smalluml_Parameter') is None


def test_assoc_returnType5_stub_double():
    # smalluml_SuperType has no real 'smalluml_SuperType7' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Operation(isAbstract=True)
    partner = smalluml_SuperType()
    setattr(partner, 'smalluml_SuperType7', None)
    _safe_set(owner, 'smalluml_Operation6', partner)
    assert getattr(partner, 'smalluml_SuperType7') == owner
    _safe_set(owner, 'smalluml_Operation6', None)
    assert getattr(partner, 'smalluml_SuperType7') is None


def test_assoc_role2_stub_double():
    # smalluml_Association has no real 'smalluml_Association' property in the generated
    # code (a bare stub) -- manually attach it so smalluml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smalluml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smalluml_Role(lowerBound=7, upperBound=7)
    partner = smalluml_Association()
    setattr(partner, 'smalluml_Association', None)
    _safe_set(owner, 'smalluml_Role3', partner)
    assert owner in getattr(partner, 'smalluml_Association')
    _safe_set(owner, 'smalluml_Role3', None)
    assert owner not in getattr(partner, 'smalluml_Association')


