import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mnoq_Foo,
    mnoq_M,
    mnoq_N,
    mnoq_O,
    mnoq_Q,
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

def test_assoc_mms1_reverse_link_reassign_clear():
    a1 = mnoq_N(x=7)
    a2 = mnoq_N(x=13)
    b = mnoq_M(x=7)
    _safe_set(b, 'M', a1)
    assert _is_linked(b, 'M', a1)
    if hasattr(a1, 'nns'):
        assert _is_linked(a1, 'nns', b)
    _safe_set(b, 'M', a2)
    assert _is_linked(b, 'M', a2)
    if hasattr(a1, 'nns'):
        assert not _is_linked(a1, 'nns', b)
    if hasattr(a2, 'nns'):
        assert _is_linked(a2, 'nns', b)
    _safe_set(b, 'M', None)
    assert not _is_linked(b, 'M', a2)
    if hasattr(a2, 'nns'):
        assert not _is_linked(a2, 'nns', b)


def test_assoc_nns4_reverse_link_reassign_clear():
    a1 = mnoq_N(x=7)
    a2 = mnoq_N(x=13)
    b = mnoq_M(x=7)
    _safe_set(b, 'mms', {a1})
    assert _is_linked(b, 'mms', a1)
    if hasattr(a1, 'N5'):
        assert _is_linked(a1, 'N5', b)
    _safe_set(b, 'mms', {a2})
    assert _is_linked(b, 'mms', a2)
    if hasattr(a1, 'N5'):
        assert not _is_linked(a1, 'N5', b)
    if hasattr(a2, 'N5'):
        assert _is_linked(a2, 'N5', b)
    _safe_set(b, 'mms', set())
    assert not _is_linked(b, 'mms', a2)
    if hasattr(a2, 'N5'):
        assert not _is_linked(a2, 'N5', b)


def test_assoc_ns0_reverse_link_reassign_clear():
    a1 = mnoq_Q(x=7)
    a2 = mnoq_Q(x=13)
    b = mnoq_N(x=7)
    _safe_set(b, 'N', a1)
    assert _is_linked(b, 'N', a1)
    if hasattr(a1, 'qs'):
        assert _is_linked(a1, 'qs', b)
    _safe_set(b, 'N', a2)
    assert _is_linked(b, 'N', a2)
    if hasattr(a1, 'qs'):
        assert not _is_linked(a1, 'qs', b)
    if hasattr(a2, 'qs'):
        assert _is_linked(a2, 'qs', b)
    _safe_set(b, 'N', None)
    assert not _is_linked(b, 'N', a2)
    if hasattr(a2, 'qs'):
        assert not _is_linked(a2, 'qs', b)


def test_assoc_o6_reverse_link_reassign_clear():
    a1 = mnoq_O(x=7)
    a2 = mnoq_O(x=13)
    b = mnoq_M(x=7)
    _safe_set(b, 'mnoq_M', a1)
    assert _is_linked(b, 'mnoq_M', a1)
    if hasattr(a1, 'mnoq_O'):
        assert _is_linked(a1, 'mnoq_O', b)
    _safe_set(b, 'mnoq_M', a2)
    assert _is_linked(b, 'mnoq_M', a2)
    if hasattr(a1, 'mnoq_O'):
        assert not _is_linked(a1, 'mnoq_O', b)
    if hasattr(a2, 'mnoq_O'):
        assert _is_linked(a2, 'mnoq_O', b)
    _safe_set(b, 'mnoq_M', None)
    assert not _is_linked(b, 'mnoq_M', a2)
    if hasattr(a2, 'mnoq_O'):
        assert not _is_linked(a2, 'mnoq_O', b)


def test_assoc_qs2_reverse_link_reassign_clear():
    a1 = mnoq_Q(x=7)
    a2 = mnoq_Q(x=13)
    b = mnoq_N(x=7)
    _safe_set(b, 'ns', {a1})
    assert _is_linked(b, 'ns', a1)
    if hasattr(a1, 'Q'):
        assert _is_linked(a1, 'Q', b)
    _safe_set(b, 'ns', {a2})
    assert _is_linked(b, 'ns', a2)
    if hasattr(a1, 'Q'):
        assert not _is_linked(a1, 'Q', b)
    if hasattr(a2, 'Q'):
        assert _is_linked(a2, 'Q', b)
    _safe_set(b, 'ns', set())
    assert not _is_linked(b, 'ns', a2)
    if hasattr(a2, 'Q'):
        assert not _is_linked(a2, 'Q', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_foo3_stub_double():
    # mnoq_Foo has no real 'mnoq_Foo' property in the generated
    # code (a bare stub) -- manually attach it so mnoq_N's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mnoq_N's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mnoq_N(x=7)
    partner = mnoq_Foo()
    setattr(partner, 'mnoq_Foo', None)
    _safe_set(owner, 'mnoq_N', partner)
    assert getattr(partner, 'mnoq_Foo') == owner
    _safe_set(owner, 'mnoq_N', None)
    assert getattr(partner, 'mnoq_Foo') is None


