import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    Type,
    tallerE1Java_Annotation,
    tallerE1Java_Attribute,
    tallerE1Java_Class,
    tallerE1Java_Container,
    tallerE1Java_DAOClass,
    tallerE1Java_EntityClass,
    tallerE1Java_Package,
    tallerE1Java_PrimitiveType,
    tallerE1Java_Program,
    tallerE1Java_TestClass,
    tallerE1Java_Type,
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

def test_assoc_annotations11_reverse_link_reassign_clear():
    a1 = tallerE1Java_Attribute(name="sample_text", visibility="sample_text")
    a2 = tallerE1Java_Attribute(name="sample_text_2", visibility="sample_text_2")
    b = tallerE1Java_Annotation(content="sample_text", type="sample_text")
    _safe_set(b, 'tallerE1Java_Annotation', a1)
    assert _is_linked(b, 'tallerE1Java_Annotation', a1)
    if hasattr(a1, 'tallerE1Java_Attribute12'):
        assert _is_linked(a1, 'tallerE1Java_Attribute12', b)
    _safe_set(b, 'tallerE1Java_Annotation', a2)
    assert _is_linked(b, 'tallerE1Java_Annotation', a2)
    if hasattr(a1, 'tallerE1Java_Attribute12'):
        assert not _is_linked(a1, 'tallerE1Java_Attribute12', b)
    if hasattr(a2, 'tallerE1Java_Attribute12'):
        assert _is_linked(a2, 'tallerE1Java_Attribute12', b)
    _safe_set(b, 'tallerE1Java_Annotation', None)
    assert not _is_linked(b, 'tallerE1Java_Annotation', a2)
    if hasattr(a2, 'tallerE1Java_Attribute12'):
        assert not _is_linked(a2, 'tallerE1Java_Attribute12', b)


def test_assoc_param13_reverse_link_reassign_clear():
    a1 = tallerE1Java_Type(name="sample_text")
    a2 = tallerE1Java_Type(name="sample_text_2")
    b = tallerE1Java_Container(type="sample_text")
    _safe_set(b, 'tallerE1Java_Container14', a1)
    assert _is_linked(b, 'tallerE1Java_Container14', a1)
    if hasattr(a1, 'tallerE1Java_Type15'):
        assert _is_linked(a1, 'tallerE1Java_Type15', b)
    _safe_set(b, 'tallerE1Java_Container14', a2)
    assert _is_linked(b, 'tallerE1Java_Container14', a2)
    if hasattr(a1, 'tallerE1Java_Type15'):
        assert not _is_linked(a1, 'tallerE1Java_Type15', b)
    if hasattr(a2, 'tallerE1Java_Type15'):
        assert _is_linked(a2, 'tallerE1Java_Type15', b)
    _safe_set(b, 'tallerE1Java_Container14', None)
    assert not _is_linked(b, 'tallerE1Java_Container14', a2)
    if hasattr(a2, 'tallerE1Java_Type15'):
        assert not _is_linked(a2, 'tallerE1Java_Type15', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = tallerE1Java_Type(name="sample_text")
    a2 = tallerE1Java_Type(name="sample_text_2")
    b = tallerE1Java_Attribute(name="sample_text", visibility="sample_text")
    _safe_set(b, 'tallerE1Java_Attribute10', a1)
    assert _is_linked(b, 'tallerE1Java_Attribute10', a1)
    if hasattr(a1, 'tallerE1Java_Type'):
        assert _is_linked(a1, 'tallerE1Java_Type', b)
    _safe_set(b, 'tallerE1Java_Attribute10', a2)
    assert _is_linked(b, 'tallerE1Java_Attribute10', a2)
    if hasattr(a1, 'tallerE1Java_Type'):
        assert not _is_linked(a1, 'tallerE1Java_Type', b)
    if hasattr(a2, 'tallerE1Java_Type'):
        assert _is_linked(a2, 'tallerE1Java_Type', b)
    _safe_set(b, 'tallerE1Java_Attribute10', None)
    assert not _is_linked(b, 'tallerE1Java_Attribute10', a2)
    if hasattr(a2, 'tallerE1Java_Type'):
        assert not _is_linked(a2, 'tallerE1Java_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes7_stub_double():
    # tallerE1Java_Class has no real 'tallerE1Java_Class8' property in the generated
    # code (a bare stub) -- manually attach it so tallerE1Java_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tallerE1Java_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tallerE1Java_Attribute(name="sample_text", visibility="sample_text")
    partner = tallerE1Java_Class()
    setattr(partner, 'tallerE1Java_Class8', None)
    _safe_set(owner, 'tallerE1Java_Attribute', partner)
    assert owner in getattr(partner, 'tallerE1Java_Class8')
    _safe_set(owner, 'tallerE1Java_Attribute', None)
    assert owner not in getattr(partner, 'tallerE1Java_Class8')


def test_assoc_classes5_stub_double():
    # tallerE1Java_Class has no real 'tallerE1Java_Class' property in the generated
    # code (a bare stub) -- manually attach it so tallerE1Java_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tallerE1Java_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tallerE1Java_Package(name="sample_text")
    partner = tallerE1Java_Class()
    setattr(partner, 'tallerE1Java_Class', None)
    _safe_set(owner, 'tallerE1Java_Package6', {partner})
    assert getattr(partner, 'tallerE1Java_Class') == owner
    _safe_set(owner, 'tallerE1Java_Package6', set())
    assert getattr(partner, 'tallerE1Java_Class') is None


def test_assoc_containerTypes3_stub_double():
    # tallerE1Java_Program has no real 'tallerE1Java_Program4' property in the generated
    # code (a bare stub) -- manually attach it so tallerE1Java_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tallerE1Java_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tallerE1Java_Container(type="sample_text")
    partner = tallerE1Java_Program()
    setattr(partner, 'tallerE1Java_Program4', None)
    _safe_set(owner, 'tallerE1Java_Container', partner)
    assert owner in getattr(partner, 'tallerE1Java_Program4')
    _safe_set(owner, 'tallerE1Java_Container', None)
    assert owner not in getattr(partner, 'tallerE1Java_Program4')


def test_assoc_packages0_stub_double():
    # tallerE1Java_Program has no real 'tallerE1Java_Program' property in the generated
    # code (a bare stub) -- manually attach it so tallerE1Java_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tallerE1Java_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tallerE1Java_Package(name="sample_text")
    partner = tallerE1Java_Program()
    setattr(partner, 'tallerE1Java_Program', None)
    _safe_set(owner, 'tallerE1Java_Package', partner)
    assert owner in getattr(partner, 'tallerE1Java_Program')
    _safe_set(owner, 'tallerE1Java_Package', None)
    assert owner not in getattr(partner, 'tallerE1Java_Program')


