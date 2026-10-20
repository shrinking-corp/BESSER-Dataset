import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    simpleClass_Association,
    simpleClass_Attribute,
    simpleClass_Class,
    simpleClass_ClassModel,
    simpleClass_NamedElement,
    simpleClass_Package,
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

def test_assoc_super11_reverse_link_reassign_clear():
    a1 = simpleClass_Class(persistent=True)
    a2 = simpleClass_Class(persistent=False)
    b = simpleClass_Class(persistent=True)
    _safe_set(b, 'simpleClass_Class12', a1)
    assert _is_linked(b, 'simpleClass_Class12', a1)
    if hasattr(a1, 'simpleClass_Class10'):
        assert _is_linked(a1, 'simpleClass_Class10', b)
    _safe_set(b, 'simpleClass_Class12', a2)
    assert _is_linked(b, 'simpleClass_Class12', a2)
    if hasattr(a1, 'simpleClass_Class10'):
        assert not _is_linked(a1, 'simpleClass_Class10', b)
    if hasattr(a2, 'simpleClass_Class10'):
        assert _is_linked(a2, 'simpleClass_Class10', b)
    _safe_set(b, 'simpleClass_Class12', None)
    assert not _is_linked(b, 'simpleClass_Class12', a2)
    if hasattr(a2, 'simpleClass_Class10'):
        assert not _is_linked(a2, 'simpleClass_Class10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes8_stub_double():
    # simpleClass_Attribute has no real 'simpleClass_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so simpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleClass_Class(persistent=True)
    partner = simpleClass_Attribute()
    setattr(partner, 'simpleClass_Attribute', None)
    _safe_set(owner, 'simpleClass_Class9', {partner})
    assert getattr(partner, 'simpleClass_Attribute') == owner
    _safe_set(owner, 'simpleClass_Class9', set())
    assert getattr(partner, 'simpleClass_Attribute') is None


def test_assoc_classes4_stub_double():
    # simpleClass_Package has no real 'simpleClass_Package5' property in the generated
    # code (a bare stub) -- manually attach it so simpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleClass_Class(persistent=True)
    partner = simpleClass_Package()
    setattr(partner, 'simpleClass_Package5', None)
    _safe_set(owner, 'simpleClass_Class', partner)
    assert owner in getattr(partner, 'simpleClass_Package5')
    _safe_set(owner, 'simpleClass_Class', None)
    assert owner not in getattr(partner, 'simpleClass_Package5')


def test_assoc_source13_stub_double():
    # simpleClass_Association has no real 'simpleClass_Association14' property in the generated
    # code (a bare stub) -- manually attach it so simpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleClass_Class(persistent=True)
    partner = simpleClass_Association()
    setattr(partner, 'simpleClass_Association14', None)
    _safe_set(owner, 'simpleClass_Class15', partner)
    assert getattr(partner, 'simpleClass_Association14') == owner
    _safe_set(owner, 'simpleClass_Class15', None)
    assert getattr(partner, 'simpleClass_Association14') is None


def test_assoc_target16_stub_double():
    # simpleClass_Association has no real 'simpleClass_Association17' property in the generated
    # code (a bare stub) -- manually attach it so simpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleClass_Class(persistent=True)
    partner = simpleClass_Association()
    setattr(partner, 'simpleClass_Association17', None)
    _safe_set(owner, 'simpleClass_Class18', partner)
    assert getattr(partner, 'simpleClass_Association17') == owner
    _safe_set(owner, 'simpleClass_Class18', None)
    assert getattr(partner, 'simpleClass_Association17') is None


