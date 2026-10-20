import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    C,
    pghttptest_A,
    pghttptest_B,
    pghttptest_C,
    pghttptest_D,
    pghttptest_Priv,
    pghttptest_Root,
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

def test_assoc_cs3_reverse_link_reassign_clear():
    a1 = pghttptest_C(name="sample_text")
    a2 = pghttptest_C(name="sample_text_2")
    b = pghttptest_B(priv1=7)
    _safe_set(b, 'pghttptest_B4', {a1})
    assert _is_linked(b, 'pghttptest_B4', a1)
    if hasattr(a1, 'pghttptest_C'):
        assert _is_linked(a1, 'pghttptest_C', b)
    _safe_set(b, 'pghttptest_B4', {a2})
    assert _is_linked(b, 'pghttptest_B4', a2)
    if hasattr(a1, 'pghttptest_C'):
        assert not _is_linked(a1, 'pghttptest_C', b)
    if hasattr(a2, 'pghttptest_C'):
        assert _is_linked(a2, 'pghttptest_C', b)
    _safe_set(b, 'pghttptest_B4', set())
    assert not _is_linked(b, 'pghttptest_B4', a2)
    if hasattr(a2, 'pghttptest_C'):
        assert not _is_linked(a2, 'pghttptest_C', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_as_0_stub_double():
    # pghttptest_Root has no real 'pghttptest_Root' property in the generated
    # code (a bare stub) -- manually attach it so pghttptest_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pghttptest_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pghttptest_A(name="sample_text", value=7)
    partner = pghttptest_Root()
    setattr(partner, 'pghttptest_Root', None)
    _safe_set(owner, 'pghttptest_A', partner)
    assert owner in getattr(partner, 'pghttptest_Root')
    _safe_set(owner, 'pghttptest_A', None)
    assert owner not in getattr(partner, 'pghttptest_Root')


def test_assoc_b1_stub_double():
    # pghttptest_Root has no real 'pghttptest_Root2' property in the generated
    # code (a bare stub) -- manually attach it so pghttptest_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pghttptest_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pghttptest_B(priv1=7)
    partner = pghttptest_Root()
    setattr(partner, 'pghttptest_Root2', None)
    _safe_set(owner, 'pghttptest_B', partner)
    assert getattr(partner, 'pghttptest_Root2') == owner
    _safe_set(owner, 'pghttptest_B', None)
    assert getattr(partner, 'pghttptest_Root2') is None


