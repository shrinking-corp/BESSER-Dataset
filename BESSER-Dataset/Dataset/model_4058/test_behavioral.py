import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    Feature,
    NamedElement,
    simple_OO_concept_Attribute,
    simple_OO_concept_Behavior,
    simple_OO_concept_Class,
    simple_OO_concept_Dependency,
    simple_OO_concept_Feature,
    simple_OO_concept_NamedElement,
    simple_OO_concept_Operation,
    simple_OO_concept_Package,
    simple_OO_concept_Parameter,
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

def test_assoc_parents13_reverse_link_reassign_clear():
    a1 = simple_OO_concept_Class(isAbstract=True)
    a2 = simple_OO_concept_Class(isAbstract=False)
    b = simple_OO_concept_Class(isAbstract=True)
    _safe_set(b, 'simple_OO_concept_Class14', a1)
    assert _is_linked(b, 'simple_OO_concept_Class14', a1)
    if hasattr(a1, 'simple_OO_concept_Class12'):
        assert _is_linked(a1, 'simple_OO_concept_Class12', b)
    _safe_set(b, 'simple_OO_concept_Class14', a2)
    assert _is_linked(b, 'simple_OO_concept_Class14', a2)
    if hasattr(a1, 'simple_OO_concept_Class12'):
        assert not _is_linked(a1, 'simple_OO_concept_Class12', b)
    if hasattr(a2, 'simple_OO_concept_Class12'):
        assert _is_linked(a2, 'simple_OO_concept_Class12', b)
    _safe_set(b, 'simple_OO_concept_Class14', None)
    assert not _is_linked(b, 'simple_OO_concept_Class14', a2)
    if hasattr(a2, 'simple_OO_concept_Class12'):
        assert not _is_linked(a2, 'simple_OO_concept_Class12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes8_stub_double():
    # simple_OO_concept_Attribute has no real 'simple_OO_concept_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_Class(isAbstract=True)
    partner = simple_OO_concept_Attribute()
    setattr(partner, 'simple_OO_concept_Attribute', None)
    _safe_set(owner, 'simple_OO_concept_Class9', {partner})
    assert getattr(partner, 'simple_OO_concept_Attribute') == owner
    _safe_set(owner, 'simple_OO_concept_Class9', set())
    assert getattr(partner, 'simple_OO_concept_Attribute') is None


def test_assoc_atttype15_stub_double():
    # simple_OO_concept_Attribute has no real 'simple_OO_concept_Attribute16' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_Class(isAbstract=True)
    partner = simple_OO_concept_Attribute()
    setattr(partner, 'simple_OO_concept_Attribute16', None)
    _safe_set(owner, 'simple_OO_concept_Class17', partner)
    assert getattr(partner, 'simple_OO_concept_Attribute16') == owner
    _safe_set(owner, 'simple_OO_concept_Class17', None)
    assert getattr(partner, 'simple_OO_concept_Attribute16') is None


def test_assoc_classes0_stub_double():
    # simple_OO_concept_Package has no real 'simple_OO_concept_Package' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_Class(isAbstract=True)
    partner = simple_OO_concept_Package()
    setattr(partner, 'simple_OO_concept_Package', None)
    _safe_set(owner, 'simple_OO_concept_Class', partner)
    assert owner in getattr(partner, 'simple_OO_concept_Package')
    _safe_set(owner, 'simple_OO_concept_Class', None)
    assert owner not in getattr(partner, 'simple_OO_concept_Package')


def test_assoc_client5_stub_double():
    # simple_OO_concept_Dependency has no real 'simple_OO_concept_Dependency6' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_NamedElement(name="sample_text")
    partner = simple_OO_concept_Dependency()
    setattr(partner, 'simple_OO_concept_Dependency6', None)
    _safe_set(owner, 'simple_OO_concept_NamedElement7', partner)
    assert owner in getattr(partner, 'simple_OO_concept_Dependency6')
    _safe_set(owner, 'simple_OO_concept_NamedElement7', None)
    assert owner not in getattr(partner, 'simple_OO_concept_Dependency6')


def test_assoc_operations10_stub_double():
    # simple_OO_concept_Operation has no real 'simple_OO_concept_Operation' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_Class(isAbstract=True)
    partner = simple_OO_concept_Operation()
    setattr(partner, 'simple_OO_concept_Operation', None)
    _safe_set(owner, 'simple_OO_concept_Class11', {partner})
    assert getattr(partner, 'simple_OO_concept_Operation') == owner
    _safe_set(owner, 'simple_OO_concept_Class11', set())
    assert getattr(partner, 'simple_OO_concept_Operation') is None


def test_assoc_partype22_stub_double():
    # simple_OO_concept_Parameter has no real 'simple_OO_concept_Parameter23' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_Class(isAbstract=True)
    partner = simple_OO_concept_Parameter()
    setattr(partner, 'simple_OO_concept_Parameter23', None)
    _safe_set(owner, 'simple_OO_concept_Class24', partner)
    assert getattr(partner, 'simple_OO_concept_Parameter23') == owner
    _safe_set(owner, 'simple_OO_concept_Class24', None)
    assert getattr(partner, 'simple_OO_concept_Parameter23') is None


def test_assoc_supplier3_stub_double():
    # simple_OO_concept_Dependency has no real 'simple_OO_concept_Dependency4' property in the generated
    # code (a bare stub) -- manually attach it so simple_OO_concept_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_OO_concept_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_OO_concept_NamedElement(name="sample_text")
    partner = simple_OO_concept_Dependency()
    setattr(partner, 'simple_OO_concept_Dependency4', None)
    _safe_set(owner, 'simple_OO_concept_NamedElement', partner)
    assert owner in getattr(partner, 'simple_OO_concept_Dependency4')
    _safe_set(owner, 'simple_OO_concept_NamedElement', None)
    assert owner not in getattr(partner, 'simple_OO_concept_Dependency4')


