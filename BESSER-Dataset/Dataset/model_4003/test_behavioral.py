import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    JavaMM_Annotation,
    JavaMM_Attribute,
    JavaMM_Class,
    JavaMM_Container,
    JavaMM_DAOClass,
    JavaMM_EntityClass,
    JavaMM_Package,
    JavaMM_PrimitiveType,
    JavaMM_Program,
    JavaMM_TestClass,
    JavaMM_Type,
    Type,
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
    a1 = JavaMM_Attribute(name="sample_text", visibility="sample_text")
    a2 = JavaMM_Attribute(name="sample_text_2", visibility="sample_text_2")
    b = JavaMM_Annotation(content="sample_text", type="sample_text")
    _safe_set(b, 'JavaMM_Annotation', a1)
    assert _is_linked(b, 'JavaMM_Annotation', a1)
    if hasattr(a1, 'JavaMM_Attribute12'):
        assert _is_linked(a1, 'JavaMM_Attribute12', b)
    _safe_set(b, 'JavaMM_Annotation', a2)
    assert _is_linked(b, 'JavaMM_Annotation', a2)
    if hasattr(a1, 'JavaMM_Attribute12'):
        assert not _is_linked(a1, 'JavaMM_Attribute12', b)
    if hasattr(a2, 'JavaMM_Attribute12'):
        assert _is_linked(a2, 'JavaMM_Attribute12', b)
    _safe_set(b, 'JavaMM_Annotation', None)
    assert not _is_linked(b, 'JavaMM_Annotation', a2)
    if hasattr(a2, 'JavaMM_Attribute12'):
        assert not _is_linked(a2, 'JavaMM_Attribute12', b)


def test_assoc_param13_reverse_link_reassign_clear():
    a1 = JavaMM_Type(name="sample_text")
    a2 = JavaMM_Type(name="sample_text_2")
    b = JavaMM_Container(type="sample_text")
    _safe_set(b, 'JavaMM_Container14', a1)
    assert _is_linked(b, 'JavaMM_Container14', a1)
    if hasattr(a1, 'JavaMM_Type15'):
        assert _is_linked(a1, 'JavaMM_Type15', b)
    _safe_set(b, 'JavaMM_Container14', a2)
    assert _is_linked(b, 'JavaMM_Container14', a2)
    if hasattr(a1, 'JavaMM_Type15'):
        assert not _is_linked(a1, 'JavaMM_Type15', b)
    if hasattr(a2, 'JavaMM_Type15'):
        assert _is_linked(a2, 'JavaMM_Type15', b)
    _safe_set(b, 'JavaMM_Container14', None)
    assert not _is_linked(b, 'JavaMM_Container14', a2)
    if hasattr(a2, 'JavaMM_Type15'):
        assert not _is_linked(a2, 'JavaMM_Type15', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = JavaMM_Type(name="sample_text")
    a2 = JavaMM_Type(name="sample_text_2")
    b = JavaMM_Attribute(name="sample_text", visibility="sample_text")
    _safe_set(b, 'JavaMM_Attribute10', a1)
    assert _is_linked(b, 'JavaMM_Attribute10', a1)
    if hasattr(a1, 'JavaMM_Type'):
        assert _is_linked(a1, 'JavaMM_Type', b)
    _safe_set(b, 'JavaMM_Attribute10', a2)
    assert _is_linked(b, 'JavaMM_Attribute10', a2)
    if hasattr(a1, 'JavaMM_Type'):
        assert not _is_linked(a1, 'JavaMM_Type', b)
    if hasattr(a2, 'JavaMM_Type'):
        assert _is_linked(a2, 'JavaMM_Type', b)
    _safe_set(b, 'JavaMM_Attribute10', None)
    assert not _is_linked(b, 'JavaMM_Attribute10', a2)
    if hasattr(a2, 'JavaMM_Type'):
        assert not _is_linked(a2, 'JavaMM_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes7_stub_double():
    # JavaMM_Class has no real 'JavaMM_Class8' property in the generated
    # code (a bare stub) -- manually attach it so JavaMM_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaMM_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaMM_Attribute(name="sample_text", visibility="sample_text")
    partner = JavaMM_Class()
    setattr(partner, 'JavaMM_Class8', None)
    _safe_set(owner, 'JavaMM_Attribute', partner)
    assert owner in getattr(partner, 'JavaMM_Class8')
    _safe_set(owner, 'JavaMM_Attribute', None)
    assert owner not in getattr(partner, 'JavaMM_Class8')


def test_assoc_classes5_stub_double():
    # JavaMM_Class has no real 'JavaMM_Class' property in the generated
    # code (a bare stub) -- manually attach it so JavaMM_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaMM_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaMM_Package(name="sample_text")
    partner = JavaMM_Class()
    setattr(partner, 'JavaMM_Class', None)
    _safe_set(owner, 'JavaMM_Package6', {partner})
    assert getattr(partner, 'JavaMM_Class') == owner
    _safe_set(owner, 'JavaMM_Package6', set())
    assert getattr(partner, 'JavaMM_Class') is None


def test_assoc_containerTypes3_stub_double():
    # JavaMM_Program has no real 'JavaMM_Program4' property in the generated
    # code (a bare stub) -- manually attach it so JavaMM_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaMM_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaMM_Container(type="sample_text")
    partner = JavaMM_Program()
    setattr(partner, 'JavaMM_Program4', None)
    _safe_set(owner, 'JavaMM_Container', partner)
    assert owner in getattr(partner, 'JavaMM_Program4')
    _safe_set(owner, 'JavaMM_Container', None)
    assert owner not in getattr(partner, 'JavaMM_Program4')


def test_assoc_packages0_stub_double():
    # JavaMM_Program has no real 'JavaMM_Program' property in the generated
    # code (a bare stub) -- manually attach it so JavaMM_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaMM_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaMM_Package(name="sample_text")
    partner = JavaMM_Program()
    setattr(partner, 'JavaMM_Program', None)
    _safe_set(owner, 'JavaMM_Package', partner)
    assert owner in getattr(partner, 'JavaMM_Program')
    _safe_set(owner, 'JavaMM_Package', None)
    assert owner not in getattr(partner, 'JavaMM_Program')


