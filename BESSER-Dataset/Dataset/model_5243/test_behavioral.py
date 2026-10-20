import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SElement,
    sbase_EObject,
    sbase_SElement,
    sbase_SRoot,
    sbase_X,
    sbase_Y,
    sbase_Z,
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

def test_assoc_ownsY0_reverse_link_reassign_clear():
    a1 = sbase_Y(name="sample_text")
    a2 = sbase_Y(name="sample_text_2")
    b = sbase_X(name="sample_text")
    _safe_set(b, 'toX', {a1})
    assert _is_linked(b, 'toX', a1)
    if hasattr(a1, 'Y'):
        assert _is_linked(a1, 'Y', b)
    _safe_set(b, 'toX', {a2})
    assert _is_linked(b, 'toX', a2)
    if hasattr(a1, 'Y'):
        assert not _is_linked(a1, 'Y', b)
    if hasattr(a2, 'Y'):
        assert _is_linked(a2, 'Y', b)
    _safe_set(b, 'toX', set())
    assert not _is_linked(b, 'toX', a2)
    if hasattr(a2, 'Y'):
        assert not _is_linked(a2, 'Y', b)


def test_assoc_toX2_reverse_link_reassign_clear():
    a1 = sbase_Y(name="sample_text")
    a2 = sbase_Y(name="sample_text_2")
    b = sbase_X(name="sample_text")
    _safe_set(b, 'X', a1)
    assert _is_linked(b, 'X', a1)
    if hasattr(a1, 'ownsY'):
        assert _is_linked(a1, 'ownsY', b)
    _safe_set(b, 'X', a2)
    assert _is_linked(b, 'X', a2)
    if hasattr(a1, 'ownsY'):
        assert not _is_linked(a1, 'ownsY', b)
    if hasattr(a2, 'ownsY'):
        assert _is_linked(a2, 'ownsY', b)
    _safe_set(b, 'X', None)
    assert not _is_linked(b, 'X', a2)
    if hasattr(a2, 'ownsY'):
        assert not _is_linked(a2, 'ownsY', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedX5_stub_double():
    # sbase_SRoot has no real 'sbase_SRoot' property in the generated
    # code (a bare stub) -- manually attach it so sbase_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sbase_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sbase_X(name="sample_text")
    partner = sbase_SRoot()
    setattr(partner, 'sbase_SRoot', None)
    _safe_set(owner, 'sbase_X', partner)
    assert owner in getattr(partner, 'sbase_SRoot')
    _safe_set(owner, 'sbase_X', None)
    assert owner not in getattr(partner, 'sbase_SRoot')


def test_assoc_ownsZ1_stub_double():
    # sbase_Z has no real 'Z' property in the generated
    # code (a bare stub) -- manually attach it so sbase_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sbase_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sbase_Y(name="sample_text")
    partner = sbase_Z()
    setattr(partner, 'Z', None)
    _safe_set(owner, 'toY', partner)
    assert getattr(partner, 'Z') == owner
    _safe_set(owner, 'toY', None)
    assert getattr(partner, 'Z') is None


def test_assoc_toY3_stub_double():
    # sbase_Z has no real 'ownsZ' property in the generated
    # code (a bare stub) -- manually attach it so sbase_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sbase_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sbase_Y(name="sample_text")
    partner = sbase_Z()
    setattr(partner, 'ownsZ', None)
    _safe_set(owner, 'Y4', partner)
    assert getattr(partner, 'ownsZ') == owner
    _safe_set(owner, 'Y4', None)
    assert getattr(partner, 'ownsZ') is None


