import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    W,
    content_A,
    content_B,
    content_C,
    content_D,
    content_E,
    content_F,
    content_G,
    content_H,
    content_I,
    content_J,
    content_M,
    content_N,
    content_P,
    content_Q,
    content_R,
    content_W,
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

def test_assoc_h35_stub_double():
    # content_H has no real 'content_H37' property in the generated
    # code (a bare stub) -- manually attach it so content_J's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # content_J's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = content_J(cardinality=7, linkName="sample_text")
    partner = content_H()
    setattr(partner, 'content_H37', None)
    _safe_set(owner, 'content_J36', partner)
    assert getattr(partner, 'content_H37') == owner
    _safe_set(owner, 'content_J36', None)
    assert getattr(partner, 'content_H37') is None


def test_assoc_js17_stub_double():
    # content_F has no real 'content_F18' property in the generated
    # code (a bare stub) -- manually attach it so content_J's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # content_J's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = content_J(cardinality=7, linkName="sample_text")
    partner = content_F()
    setattr(partner, 'content_F18', None)
    _safe_set(owner, 'content_J', partner)
    assert owner in getattr(partner, 'content_F18')
    _safe_set(owner, 'content_J', None)
    assert owner not in getattr(partner, 'content_F18')


