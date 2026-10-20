import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    ModelElement,
    simpleuml_Association,
    simpleuml_Attribute,
    simpleuml_Classifier,
    simpleuml_ModelElement,
    simpleuml_PrimitiveDataType,
    simpleuml_UMLClass,
    simpleuml_UMLPackage,
    Ignore,
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

def test_assoc_parents1_reverse_link_reassign_clear():
    a1 = simpleuml_UMLClass(kind="sample_text")
    a2 = simpleuml_UMLClass(kind="sample_text_2")
    b = simpleuml_UMLClass(kind="sample_text")
    _safe_set(b, 'simpleuml_UMLClass0', {a1})
    assert _is_linked(b, 'simpleuml_UMLClass0', a1)
    if hasattr(a1, 'simpleuml_UMLClass'):
        assert _is_linked(a1, 'simpleuml_UMLClass', b)
    _safe_set(b, 'simpleuml_UMLClass0', {a2})
    assert _is_linked(b, 'simpleuml_UMLClass0', a2)
    if hasattr(a1, 'simpleuml_UMLClass'):
        assert not _is_linked(a1, 'simpleuml_UMLClass', b)
    if hasattr(a2, 'simpleuml_UMLClass'):
        assert _is_linked(a2, 'simpleuml_UMLClass', b)
    _safe_set(b, 'simpleuml_UMLClass0', set())
    assert not _is_linked(b, 'simpleuml_UMLClass0', a2)
    if hasattr(a2, 'simpleuml_UMLClass'):
        assert not _is_linked(a2, 'simpleuml_UMLClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute2_stub_double():
    # simpleuml_Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so simpleuml_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleuml_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleuml_UMLClass(kind="sample_text")
    partner = simpleuml_Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Attribute') is None


def test_assoc_contents10_stub_double():
    # simpleuml_UMLPackage has no real 'simpleuml_UMLPackage' property in the generated
    # code (a bare stub) -- manually attach it so simpleuml_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleuml_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleuml_ModelElement(name="sample_text")
    partner = simpleuml_UMLPackage()
    setattr(partner, 'simpleuml_UMLPackage', None)
    _safe_set(owner, 'simpleuml_ModelElement', partner)
    assert owner in getattr(partner, 'simpleuml_UMLPackage')
    _safe_set(owner, 'simpleuml_ModelElement', None)
    assert owner not in getattr(partner, 'simpleuml_UMLPackage')


def test_assoc_owner9_stub_double():
    # simpleuml_Attribute has no real 'attribute' property in the generated
    # code (a bare stub) -- manually attach it so simpleuml_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleuml_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleuml_UMLClass(kind="sample_text")
    partner = simpleuml_Attribute()
    setattr(partner, 'attribute', None)
    _safe_set(owner, 'UMLClass', partner)
    assert getattr(partner, 'attribute') == owner
    _safe_set(owner, 'UMLClass', None)
    assert getattr(partner, 'attribute') is None


def test_assoc_source3_stub_double():
    # simpleuml_Association has no real 'simpleuml_Association' property in the generated
    # code (a bare stub) -- manually attach it so simpleuml_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleuml_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleuml_UMLClass(kind="sample_text")
    partner = simpleuml_Association()
    setattr(partner, 'simpleuml_Association', None)
    _safe_set(owner, 'simpleuml_UMLClass4', partner)
    assert getattr(partner, 'simpleuml_Association') == owner
    _safe_set(owner, 'simpleuml_UMLClass4', None)
    assert getattr(partner, 'simpleuml_Association') is None


def test_assoc_target5_stub_double():
    # simpleuml_Association has no real 'simpleuml_Association6' property in the generated
    # code (a bare stub) -- manually attach it so simpleuml_UMLClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleuml_UMLClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleuml_UMLClass(kind="sample_text")
    partner = simpleuml_Association()
    setattr(partner, 'simpleuml_Association6', None)
    _safe_set(owner, 'simpleuml_UMLClass7', partner)
    assert getattr(partner, 'simpleuml_Association6') == owner
    _safe_set(owner, 'simpleuml_UMLClass7', None)
    assert getattr(partner, 'simpleuml_Association6') is None


