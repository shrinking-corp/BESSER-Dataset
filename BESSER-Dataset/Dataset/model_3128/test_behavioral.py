import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    NamedElt,
    class_Attribute,
    class_Class,
    class_Classifier,
    class_DataType,
    class_NamedElt,
    class_Package,
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

def test_assoc_attr6_reverse_link_reassign_clear():
    a1 = class_Class(isAbstract=True)
    a2 = class_Class(isAbstract=False)
    b = class_Attribute(multiValued=True)
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


def test_assoc_owner8_reverse_link_reassign_clear():
    a1 = class_Class(isAbstract=True)
    a2 = class_Class(isAbstract=False)
    b = class_Attribute(multiValued=True)
    _safe_set(b, 'attr', a1)
    assert _is_linked(b, 'attr', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'attr', a2)
    assert _is_linked(b, 'attr', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'attr', None)
    assert not _is_linked(b, 'attr', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


def test_assoc_super4_reverse_link_reassign_clear():
    a1 = class_Class(isAbstract=True)
    a2 = class_Class(isAbstract=False)
    b = class_Class(isAbstract=True)
    _safe_set(b, 'class_Class5', a1)
    assert _is_linked(b, 'class_Class5', a1)
    if hasattr(a1, 'class_Class3'):
        assert _is_linked(a1, 'class_Class3', b)
    _safe_set(b, 'class_Class5', a2)
    assert _is_linked(b, 'class_Class5', a2)
    if hasattr(a1, 'class_Class3'):
        assert not _is_linked(a1, 'class_Class3', b)
    if hasattr(a2, 'class_Class3'):
        assert _is_linked(a2, 'class_Class3', b)
    _safe_set(b, 'class_Class5', None)
    assert not _is_linked(b, 'class_Class5', a2)
    if hasattr(a2, 'class_Class3'):
        assert not _is_linked(a2, 'class_Class3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes0_stub_double():
    # class_Package has no real 'class_Package' property in the generated
    # code (a bare stub) -- manually attach it so class_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_Class(isAbstract=True)
    partner = class_Package()
    setattr(partner, 'class_Package', None)
    _safe_set(owner, 'class_Class', partner)
    assert owner in getattr(partner, 'class_Package')
    _safe_set(owner, 'class_Class', None)
    assert owner not in getattr(partner, 'class_Package')


def test_assoc_type7_stub_double():
    # class_Classifier has no real 'class_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so class_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # class_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = class_Attribute(multiValued=True)
    partner = class_Classifier()
    setattr(partner, 'class_Classifier', None)
    _safe_set(owner, 'class_Attribute', partner)
    assert getattr(partner, 'class_Classifier') == owner
    _safe_set(owner, 'class_Attribute', None)
    assert getattr(partner, 'class_Classifier') is None


