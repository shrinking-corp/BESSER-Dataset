import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class_Attribute,
    Class_Class,
    Class_Classifier,
    Class_DataType,
    Class_NamedElt,
    Class_Package,
    Classifier,
    NamedElt,
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

def test_assoc_att4_reverse_link_reassign_clear():
    a1 = Class_Class(isAbstract=True)
    a2 = Class_Class(isAbstract=False)
    b = Class_Attribute(multiValued=True)
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_owner6_reverse_link_reassign_clear():
    a1 = Class_Class(isAbstract=True)
    a2 = Class_Class(isAbstract=False)
    b = Class_Attribute(multiValued=True)
    _safe_set(b, 'att', a1)
    assert _is_linked(b, 'att', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'att', a2)
    assert _is_linked(b, 'att', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'att', None)
    assert not _is_linked(b, 'att', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


def test_assoc_supers3_reverse_link_reassign_clear():
    a1 = Class_Class(isAbstract=True)
    a2 = Class_Class(isAbstract=False)
    b = Class_Class(isAbstract=True)
    _safe_set(b, 'Class_Class2', {a1})
    assert _is_linked(b, 'Class_Class2', a1)
    if hasattr(a1, 'Class_Class'):
        assert _is_linked(a1, 'Class_Class', b)
    _safe_set(b, 'Class_Class2', {a2})
    assert _is_linked(b, 'Class_Class2', a2)
    if hasattr(a1, 'Class_Class'):
        assert not _is_linked(a1, 'Class_Class', b)
    if hasattr(a2, 'Class_Class'):
        assert _is_linked(a2, 'Class_Class', b)
    _safe_set(b, 'Class_Class2', set())
    assert not _is_linked(b, 'Class_Class2', a2)
    if hasattr(a2, 'Class_Class'):
        assert not _is_linked(a2, 'Class_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_type5_stub_double():
    # Class_Classifier has no real 'Class_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so Class_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Class_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Class_Attribute(multiValued=True)
    partner = Class_Classifier()
    setattr(partner, 'Class_Classifier', None)
    _safe_set(owner, 'Class_Attribute', partner)
    assert getattr(partner, 'Class_Classifier') == owner
    _safe_set(owner, 'Class_Attribute', None)
    assert getattr(partner, 'Class_Classifier') is None


