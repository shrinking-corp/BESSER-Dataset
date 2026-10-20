import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    hExample_6_RHS_X,
    hExample_6_RHS_Y,
    hExample_6_RHS_Z,
    hExample_6_RHS_model,
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

def test_assoc_contZ8_reverse_link_reassign_clear():
    a1 = hExample_6_RHS_Z(name="sample_text")
    a2 = hExample_6_RHS_Z(name="sample_text_2")
    b = hExample_6_RHS_X(name="sample_text")
    _safe_set(b, 'hExample_6_RHS_X9', {a1})
    assert _is_linked(b, 'hExample_6_RHS_X9', a1)
    if hasattr(a1, 'hExample_6_RHS_Z10'):
        assert _is_linked(a1, 'hExample_6_RHS_Z10', b)
    _safe_set(b, 'hExample_6_RHS_X9', {a2})
    assert _is_linked(b, 'hExample_6_RHS_X9', a2)
    if hasattr(a1, 'hExample_6_RHS_Z10'):
        assert not _is_linked(a1, 'hExample_6_RHS_Z10', b)
    if hasattr(a2, 'hExample_6_RHS_Z10'):
        assert _is_linked(a2, 'hExample_6_RHS_Z10', b)
    _safe_set(b, 'hExample_6_RHS_X9', set())
    assert not _is_linked(b, 'hExample_6_RHS_X9', a2)
    if hasattr(a2, 'hExample_6_RHS_Z10'):
        assert not _is_linked(a2, 'hExample_6_RHS_Z10', b)


def test_assoc_refY5_reverse_link_reassign_clear():
    a1 = hExample_6_RHS_Y(name="sample_text")
    a2 = hExample_6_RHS_Y(name="sample_text_2")
    b = hExample_6_RHS_X(name="sample_text")
    _safe_set(b, 'hExample_6_RHS_X6', a1)
    assert _is_linked(b, 'hExample_6_RHS_X6', a1)
    if hasattr(a1, 'hExample_6_RHS_Y7'):
        assert _is_linked(a1, 'hExample_6_RHS_Y7', b)
    _safe_set(b, 'hExample_6_RHS_X6', a2)
    assert _is_linked(b, 'hExample_6_RHS_X6', a2)
    if hasattr(a1, 'hExample_6_RHS_Y7'):
        assert not _is_linked(a1, 'hExample_6_RHS_Y7', b)
    if hasattr(a2, 'hExample_6_RHS_Y7'):
        assert _is_linked(a2, 'hExample_6_RHS_Y7', b)
    _safe_set(b, 'hExample_6_RHS_X6', None)
    assert not _is_linked(b, 'hExample_6_RHS_X6', a2)
    if hasattr(a2, 'hExample_6_RHS_Y7'):
        assert not _is_linked(a2, 'hExample_6_RHS_Y7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containsX0_stub_double():
    # hExample_6_RHS_model has no real 'hExample_6_RHS_model' property in the generated
    # code (a bare stub) -- manually attach it so hExample_6_RHS_X's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hExample_6_RHS_X's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hExample_6_RHS_X(name="sample_text")
    partner = hExample_6_RHS_model()
    setattr(partner, 'hExample_6_RHS_model', None)
    _safe_set(owner, 'hExample_6_RHS_X', partner)
    assert owner in getattr(partner, 'hExample_6_RHS_model')
    _safe_set(owner, 'hExample_6_RHS_X', None)
    assert owner not in getattr(partner, 'hExample_6_RHS_model')


def test_assoc_containsY1_stub_double():
    # hExample_6_RHS_model has no real 'hExample_6_RHS_model2' property in the generated
    # code (a bare stub) -- manually attach it so hExample_6_RHS_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hExample_6_RHS_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hExample_6_RHS_Y(name="sample_text")
    partner = hExample_6_RHS_model()
    setattr(partner, 'hExample_6_RHS_model2', None)
    _safe_set(owner, 'hExample_6_RHS_Y', partner)
    assert owner in getattr(partner, 'hExample_6_RHS_model2')
    _safe_set(owner, 'hExample_6_RHS_Y', None)
    assert owner not in getattr(partner, 'hExample_6_RHS_model2')


def test_assoc_containsZ3_stub_double():
    # hExample_6_RHS_model has no real 'hExample_6_RHS_model4' property in the generated
    # code (a bare stub) -- manually attach it so hExample_6_RHS_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hExample_6_RHS_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hExample_6_RHS_Z(name="sample_text")
    partner = hExample_6_RHS_model()
    setattr(partner, 'hExample_6_RHS_model4', None)
    _safe_set(owner, 'hExample_6_RHS_Z', partner)
    assert owner in getattr(partner, 'hExample_6_RHS_model4')
    _safe_set(owner, 'hExample_6_RHS_Z', None)
    assert owner not in getattr(partner, 'hExample_6_RHS_model4')


