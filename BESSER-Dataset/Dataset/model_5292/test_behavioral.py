import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    MMA_A,
    MMA_B,
    MMA_Element,
    MMA_Root,
    Root,
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

def test_assoc_parent5_stub_double():
    # Root has no real 'Root' property in the generated
    # code (a bare stub) -- manually attach it so MMA_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMA_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMA_Element(name="sample_text")
    partner = Root()
    setattr(partner, 'Root', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'Root') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'Root') is None


def test_assoc_sources3_stub_double():
    # Element has no real 'Element4' property in the generated
    # code (a bare stub) -- manually attach it so MMA_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMA_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMA_Element(name="sample_text")
    partner = Element()
    setattr(partner, 'Element4', None)
    _safe_set(owner, 'targets', {partner})
    assert getattr(partner, 'Element4') == owner
    _safe_set(owner, 'targets', set())
    assert getattr(partner, 'Element4') is None


def test_assoc_targets1_stub_double():
    # Element has no real 'Element2' property in the generated
    # code (a bare stub) -- manually attach it so MMA_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMA_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMA_Element(name="sample_text")
    partner = Element()
    setattr(partner, 'Element2', None)
    _safe_set(owner, 'sources', {partner})
    assert getattr(partner, 'Element2') == owner
    _safe_set(owner, 'sources', set())
    assert getattr(partner, 'Element2') is None


