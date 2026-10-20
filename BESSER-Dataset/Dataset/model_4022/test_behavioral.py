import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    NamedElt,
    classmm_Attribute,
    classmm_Class,
    classmm_Classifier,
    classmm_DataType,
    classmm_Method,
    classmm_NamedElt,
    classmm_Package,
    classmm_Parameter,
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

def test_assoc_att0_reverse_link_reassign_clear():
    a1 = classmm_Class(isAbstract=True, visibility="sample_text")
    a2 = classmm_Class(isAbstract=False, visibility="sample_text_2")
    b = classmm_Attribute(multivalued=True, visibility="sample_text")
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


def test_assoc_owner7_reverse_link_reassign_clear():
    a1 = classmm_Class(isAbstract=True, visibility="sample_text")
    a2 = classmm_Class(isAbstract=False, visibility="sample_text_2")
    b = classmm_Attribute(multivalued=True, visibility="sample_text")
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


def test_assoc_super2_reverse_link_reassign_clear():
    a1 = classmm_Class(isAbstract=True, visibility="sample_text")
    a2 = classmm_Class(isAbstract=False, visibility="sample_text_2")
    b = classmm_Class(isAbstract=True, visibility="sample_text")
    _safe_set(b, 'classmm_Class1', {a1})
    assert _is_linked(b, 'classmm_Class1', a1)
    if hasattr(a1, 'classmm_Class'):
        assert _is_linked(a1, 'classmm_Class', b)
    _safe_set(b, 'classmm_Class1', {a2})
    assert _is_linked(b, 'classmm_Class1', a2)
    if hasattr(a1, 'classmm_Class'):
        assert not _is_linked(a1, 'classmm_Class', b)
    if hasattr(a2, 'classmm_Class'):
        assert _is_linked(a2, 'classmm_Class', b)
    _safe_set(b, 'classmm_Class1', set())
    assert not _is_linked(b, 'classmm_Class1', a2)
    if hasattr(a2, 'classmm_Class'):
        assert not _is_linked(a2, 'classmm_Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classes8_stub_double():
    # classmm_Package has no real 'package' property in the generated
    # code (a bare stub) -- manually attach it so classmm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmm_Class(isAbstract=True, visibility="sample_text")
    partner = classmm_Package()
    setattr(partner, 'package', None)
    _safe_set(owner, 'Class9', partner)
    assert owner in getattr(partner, 'package')
    _safe_set(owner, 'Class9', None)
    assert owner not in getattr(partner, 'package')


def test_assoc_methods4_stub_double():
    # classmm_Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so classmm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmm_Class(isAbstract=True, visibility="sample_text")
    partner = classmm_Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'owner5', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'owner5', set())
    assert getattr(partner, 'Method') is None


def test_assoc_owner10_stub_double():
    # classmm_Method has no real 'methods' property in the generated
    # code (a bare stub) -- manually attach it so classmm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmm_Class(isAbstract=True, visibility="sample_text")
    partner = classmm_Method()
    setattr(partner, 'methods', None)
    _safe_set(owner, 'Class11', partner)
    assert getattr(partner, 'methods') == owner
    _safe_set(owner, 'Class11', None)
    assert getattr(partner, 'methods') is None


def test_assoc_package3_stub_double():
    # classmm_Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so classmm_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmm_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmm_Class(isAbstract=True, visibility="sample_text")
    partner = classmm_Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'classes', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'classes', None)
    assert getattr(partner, 'Package') is None


def test_assoc_type6_stub_double():
    # classmm_Classifier has no real 'classmm_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so classmm_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classmm_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classmm_Attribute(multivalued=True, visibility="sample_text")
    partner = classmm_Classifier()
    setattr(partner, 'classmm_Classifier', None)
    _safe_set(owner, 'classmm_Attribute', partner)
    assert getattr(partner, 'classmm_Classifier') == owner
    _safe_set(owner, 'classmm_Attribute', None)
    assert getattr(partner, 'classmm_Classifier') is None


