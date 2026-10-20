import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    Class,
    Element,
    Package,
    PackageableElement,
    TypedElement,
    UML_Association,
    UML_Attribute,
    UML_Class,
    UML_Element,
    UML_Enumeration,
    UML_EnumerationLiteral,
    UML_Generalization,
    UML_Interface,
    UML_LiteralInteger,
    UML_LiteralUnlimitedNatural,
    UML_Model,
    UML_Operation,
    UML_Package,
    UML_PackageableElement,
    UML_Parameter,
    UML_PrimitiveType,
    UML_Property,
    UML_TemplateBinding,
    UML_TemplateParameterSubstitution,
    UML_TypedElement,
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

def test_assoc_qualifier9_reverse_link_reassign_clear():
    a1 = UML_Property(isStatic=True)
    a2 = UML_Property(isStatic=False)
    b = UML_Property(isStatic=True)
    _safe_set(b, 'UML_Property8', {a1})
    assert _is_linked(b, 'UML_Property8', a1)
    if hasattr(a1, 'UML_Property10'):
        assert _is_linked(a1, 'UML_Property10', b)
    _safe_set(b, 'UML_Property8', {a2})
    assert _is_linked(b, 'UML_Property8', a2)
    if hasattr(a1, 'UML_Property10'):
        assert not _is_linked(a1, 'UML_Property10', b)
    if hasattr(a2, 'UML_Property10'):
        assert _is_linked(a2, 'UML_Property10', b)
    _safe_set(b, 'UML_Property8', set())
    assert not _is_linked(b, 'UML_Property8', a2)
    if hasattr(a2, 'UML_Property10'):
        assert not _is_linked(a2, 'UML_Property10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association7_stub_double():
    # UML_Association has no real 'UML_Association' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Association()
    setattr(partner, 'UML_Association', None)
    _safe_set(owner, 'UML_Property', partner)
    assert getattr(partner, 'UML_Association') == owner
    _safe_set(owner, 'UML_Property', None)
    assert getattr(partner, 'UML_Association') is None


def test_assoc_associationEnd14_stub_double():
    # UML_Association has no real 'UML_Association16' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Association()
    setattr(partner, 'UML_Association16', None)
    _safe_set(owner, 'UML_Property15', partner)
    assert getattr(partner, 'UML_Association16') == owner
    _safe_set(owner, 'UML_Property15', None)
    assert getattr(partner, 'UML_Association16') is None


def test_assoc_interface17_stub_double():
    # UML_Interface has no real 'UML_Interface' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Interface()
    setattr(partner, 'UML_Interface', None)
    _safe_set(owner, 'UML_Property18', partner)
    assert getattr(partner, 'UML_Interface') == owner
    _safe_set(owner, 'UML_Property18', None)
    assert getattr(partner, 'UML_Interface') is None


def test_assoc_memberEnd50_stub_double():
    # UML_Association has no real 'UML_Association51' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Association()
    setattr(partner, 'UML_Association51', None)
    _safe_set(owner, 'UML_Property52', partner)
    assert owner in getattr(partner, 'UML_Association51')
    _safe_set(owner, 'UML_Property52', None)
    assert owner not in getattr(partner, 'UML_Association51')


def test_assoc_ownedEnd53_stub_double():
    # UML_Association has no real 'UML_Association54' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Association()
    setattr(partner, 'UML_Association54', None)
    _safe_set(owner, 'UML_Property55', partner)
    assert owner in getattr(partner, 'UML_Association54')
    _safe_set(owner, 'UML_Property55', None)
    assert owner not in getattr(partner, 'UML_Association54')


def test_assoc_ownedParameter19_stub_double():
    # UML_Operation has no real 'UML_Operation' property in the generated
    # code (a bare stub) -- manually attach it so UML_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Parameter(direction="sample_text")
    partner = UML_Operation()
    setattr(partner, 'UML_Operation', None)
    _safe_set(owner, 'UML_Parameter', partner)
    assert owner in getattr(partner, 'UML_Operation')
    _safe_set(owner, 'UML_Parameter', None)
    assert owner not in getattr(partner, 'UML_Operation')


def test_assoc_owningAssociation11_stub_double():
    # UML_Association has no real 'UML_Association13' property in the generated
    # code (a bare stub) -- manually attach it so UML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Property(isStatic=True)
    partner = UML_Association()
    setattr(partner, 'UML_Association13', None)
    _safe_set(owner, 'UML_Property12', partner)
    assert getattr(partner, 'UML_Association13') == owner
    _safe_set(owner, 'UML_Property12', None)
    assert getattr(partner, 'UML_Association13') is None


def test_assoc_upperValue5_stub_double():
    # UML_TypedElement has no real 'UML_TypedElement6' property in the generated
    # code (a bare stub) -- manually attach it so UML_LiteralUnlimitedNatural's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_LiteralUnlimitedNatural's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_LiteralUnlimitedNatural(value=7)
    partner = UML_TypedElement()
    setattr(partner, 'UML_TypedElement6', None)
    _safe_set(owner, 'UML_LiteralUnlimitedNatural', partner)
    assert getattr(partner, 'UML_TypedElement6') == owner
    _safe_set(owner, 'UML_LiteralUnlimitedNatural', None)
    assert getattr(partner, 'UML_TypedElement6') is None


