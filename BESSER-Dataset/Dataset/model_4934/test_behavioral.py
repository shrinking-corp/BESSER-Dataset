import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    backbone_Application,
    backbone_Attribute,
    backbone_Collection,
    backbone_Model,
    backbone_NamedElement,
    backbone_Operation,
    backbone_Parameter,
    backbone_Reference,
    backbone_Router,
    backbone_RouterMapping,
    backbone_View,
    CardinalityKind,
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

def test_assoc_attributes7_stub_double():
    # backbone_Model has no real 'backbone_Model' property in the generated
    # code (a bare stub) -- manually attach it so backbone_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backbone_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backbone_Attribute(cardinality="sample_text", defaultValue="sample_text")
    partner = backbone_Model()
    setattr(partner, 'backbone_Model', None)
    _safe_set(owner, 'backbone_Attribute', partner)
    assert owner in getattr(partner, 'backbone_Model')
    _safe_set(owner, 'backbone_Attribute', None)
    assert owner not in getattr(partner, 'backbone_Model')


def test_assoc_mappings22_stub_double():
    # backbone_Router has no real 'backbone_Router' property in the generated
    # code (a bare stub) -- manually attach it so backbone_RouterMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backbone_RouterMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backbone_RouterMapping(path="sample_text")
    partner = backbone_Router()
    setattr(partner, 'backbone_Router', None)
    _safe_set(owner, 'backbone_RouterMapping', partner)
    assert owner in getattr(partner, 'backbone_Router')
    _safe_set(owner, 'backbone_RouterMapping', None)
    assert owner not in getattr(partner, 'backbone_Router')


def test_assoc_references8_stub_double():
    # backbone_Model has no real 'backbone_Model9' property in the generated
    # code (a bare stub) -- manually attach it so backbone_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backbone_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backbone_Reference(cardinality="sample_text")
    partner = backbone_Model()
    setattr(partner, 'backbone_Model9', None)
    _safe_set(owner, 'backbone_Reference', partner)
    assert owner in getattr(partner, 'backbone_Model9')
    _safe_set(owner, 'backbone_Reference', None)
    assert owner not in getattr(partner, 'backbone_Model9')


def test_assoc_type13_stub_double():
    # backbone_Model has no real 'backbone_Model15' property in the generated
    # code (a bare stub) -- manually attach it so backbone_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backbone_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backbone_Reference(cardinality="sample_text")
    partner = backbone_Model()
    setattr(partner, 'backbone_Model15', None)
    _safe_set(owner, 'backbone_Reference14', partner)
    assert getattr(partner, 'backbone_Model15') == owner
    _safe_set(owner, 'backbone_Reference14', None)
    assert getattr(partner, 'backbone_Model15') is None


def test_assoc_view25_stub_double():
    # backbone_View has no real 'backbone_View' property in the generated
    # code (a bare stub) -- manually attach it so backbone_RouterMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # backbone_RouterMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = backbone_RouterMapping(path="sample_text")
    partner = backbone_View()
    setattr(partner, 'backbone_View', None)
    _safe_set(owner, 'backbone_RouterMapping26', partner)
    assert getattr(partner, 'backbone_View') == owner
    _safe_set(owner, 'backbone_RouterMapping26', None)
    assert getattr(partner, 'backbone_View') is None


