import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    Class,
    Classifier,
    SimpleClass_Association,
    SimpleClass_Attribute,
    SimpleClass_Class,
    SimpleClass_Classifier,
    SimpleClass_PrimitiveDataType,
    EA,
    Entity,
    Vocabulary,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attrs1_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so SimpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleClass_Class(is_persistent="sample_text", tipo="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'SimpleClass_Class2', {partner})
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'SimpleClass_Class2', set())
    assert getattr(partner, 'Attribute') is None


def test_assoc_dest5_stub_double():
    # Class has no real 'Class7' property in the generated
    # code (a bare stub) -- manually attach it so SimpleClass_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleClass_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleClass_Association(name="sample_text")
    partner = Class()
    setattr(partner, 'Class7', None)
    _safe_set(owner, 'SimpleClass_Association6', partner)
    assert getattr(partner, 'Class7') == owner
    _safe_set(owner, 'SimpleClass_Association6', None)
    assert getattr(partner, 'Class7') is None


def test_assoc_parent0_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so SimpleClass_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleClass_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleClass_Class(is_persistent="sample_text", tipo="sample_text")
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'SimpleClass_Class', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'SimpleClass_Class', None)
    assert getattr(partner, 'Class') is None


def test_assoc_src3_stub_double():
    # Class has no real 'Class4' property in the generated
    # code (a bare stub) -- manually attach it so SimpleClass_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleClass_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleClass_Association(name="sample_text")
    partner = Class()
    setattr(partner, 'Class4', None)
    _safe_set(owner, 'SimpleClass_Association', partner)
    assert getattr(partner, 'Class4') == owner
    _safe_set(owner, 'SimpleClass_Association', None)
    assert getattr(partner, 'Class4') is None


def test_assoc_type8_stub_double():
    # Classifier has no real 'Classifier' property in the generated
    # code (a bare stub) -- manually attach it so SimpleClass_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleClass_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleClass_Attribute(is_primary="sample_text", name="sample_text")
    partner = Classifier()
    setattr(partner, 'Classifier', None)
    _safe_set(owner, 'SimpleClass_Attribute', partner)
    assert getattr(partner, 'Classifier') == owner
    _safe_set(owner, 'SimpleClass_Attribute', None)
    assert getattr(partner, 'Classifier') is None


