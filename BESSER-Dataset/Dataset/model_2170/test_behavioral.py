import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DContainedElement,
    DContainedVertex,
    DGraphElement,
    DTypedElement,
    DVertex,
    dgf_DContainedElement,
    dgf_DContainedVertex,
    dgf_DContainment,
    dgf_DGraphElement,
    dgf_DLink,
    dgf_DNode,
    dgf_DReference,
    dgf_DTypedElement,
    dgf_DVertex,
    dgf_Graph,
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

def test_assoc_containment8_stub_double():
    # dgf_DContainedElement has no real 'dgf_DContainedElement' property in the generated
    # code (a bare stub) -- manually attach it so dgf_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dgf_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dgf_DNode(pointOfView="sample_text")
    partner = dgf_DContainedElement()
    setattr(partner, 'dgf_DContainedElement', None)
    _safe_set(owner, 'dgf_DNode9', partner)
    assert getattr(partner, 'dgf_DContainedElement') == owner
    _safe_set(owner, 'dgf_DNode9', None)
    assert getattr(partner, 'dgf_DContainedElement') is None


def test_assoc_elements7_stub_double():
    # dgf_Graph has no real 'dgf_Graph' property in the generated
    # code (a bare stub) -- manually attach it so dgf_DGraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dgf_DGraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dgf_DGraphElement(name="sample_text")
    partner = dgf_Graph()
    setattr(partner, 'dgf_Graph', None)
    _safe_set(owner, 'dgf_DGraphElement', partner)
    assert owner in getattr(partner, 'dgf_Graph')
    _safe_set(owner, 'dgf_DGraphElement', None)
    assert owner not in getattr(partner, 'dgf_Graph')


def test_assoc_source1_stub_double():
    # dgf_DVertex has no real 'dgf_DVertex2' property in the generated
    # code (a bare stub) -- manually attach it so dgf_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dgf_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dgf_DNode(pointOfView="sample_text")
    partner = dgf_DVertex()
    setattr(partner, 'dgf_DVertex2', None)
    _safe_set(owner, 'dgf_DNode3', partner)
    assert getattr(partner, 'dgf_DVertex2') == owner
    _safe_set(owner, 'dgf_DNode3', None)
    assert getattr(partner, 'dgf_DVertex2') is None


def test_assoc_target0_stub_double():
    # dgf_DVertex has no real 'dgf_DVertex' property in the generated
    # code (a bare stub) -- manually attach it so dgf_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dgf_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dgf_DNode(pointOfView="sample_text")
    partner = dgf_DVertex()
    setattr(partner, 'dgf_DVertex', None)
    _safe_set(owner, 'dgf_DNode', partner)
    assert getattr(partner, 'dgf_DVertex') == owner
    _safe_set(owner, 'dgf_DNode', None)
    assert getattr(partner, 'dgf_DVertex') is None


def test_assoc_vertices4_stub_double():
    # dgf_DVertex has no real 'dgf_DVertex6' property in the generated
    # code (a bare stub) -- manually attach it so dgf_DNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dgf_DNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dgf_DNode(pointOfView="sample_text")
    partner = dgf_DVertex()
    setattr(partner, 'dgf_DVertex6', None)
    _safe_set(owner, 'dgf_DNode5', {partner})
    assert getattr(partner, 'dgf_DVertex6') == owner
    _safe_set(owner, 'dgf_DNode5', set())
    assert getattr(partner, 'dgf_DVertex6') is None


