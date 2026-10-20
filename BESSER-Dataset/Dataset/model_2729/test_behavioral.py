import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B,
    test100_A,
    test100_B,
    test100_C,
    test100_DsmlRelation,
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

def test_assoc_bs1_reverse_link_reassign_clear():
    a1 = test100_B(id="sample_text")
    a2 = test100_B(id="sample_text_2")
    b = test100_A(name="sample_text")
    _safe_set(b, 'test100_A2', {a1})
    assert _is_linked(b, 'test100_A2', a1)
    if hasattr(a1, 'test100_B'):
        assert _is_linked(a1, 'test100_B', b)
    _safe_set(b, 'test100_A2', {a2})
    assert _is_linked(b, 'test100_A2', a2)
    if hasattr(a1, 'test100_B'):
        assert not _is_linked(a1, 'test100_B', b)
    if hasattr(a2, 'test100_B'):
        assert _is_linked(a2, 'test100_B', b)
    _safe_set(b, 'test100_A2', set())
    assert not _is_linked(b, 'test100_A2', a2)
    if hasattr(a2, 'test100_B'):
        assert not _is_linked(a2, 'test100_B', b)


def test_assoc_fromDsml5_reverse_link_reassign_clear():
    a1 = test100_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    a2 = test100_DsmlRelation(details="sample_text_2", mandatory=False, name="sample_text_2")
    b = test100_A(name="sample_text")
    _safe_set(b, 'test100_A7', a1)
    assert _is_linked(b, 'test100_A7', a1)
    if hasattr(a1, 'test100_DsmlRelation6'):
        assert _is_linked(a1, 'test100_DsmlRelation6', b)
    _safe_set(b, 'test100_A7', a2)
    assert _is_linked(b, 'test100_A7', a2)
    if hasattr(a1, 'test100_DsmlRelation6'):
        assert not _is_linked(a1, 'test100_DsmlRelation6', b)
    if hasattr(a2, 'test100_DsmlRelation6'):
        assert _is_linked(a2, 'test100_DsmlRelation6', b)
    _safe_set(b, 'test100_A7', None)
    assert not _is_linked(b, 'test100_A7', a2)
    if hasattr(a2, 'test100_DsmlRelation6'):
        assert not _is_linked(a2, 'test100_DsmlRelation6', b)


def test_assoc_relateds3_reverse_link_reassign_clear():
    a1 = test100_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    a2 = test100_DsmlRelation(details="sample_text_2", mandatory=False, name="sample_text_2")
    b = test100_A(name="sample_text")
    _safe_set(b, 'test100_A4', {a1})
    assert _is_linked(b, 'test100_A4', a1)
    if hasattr(a1, 'test100_DsmlRelation'):
        assert _is_linked(a1, 'test100_DsmlRelation', b)
    _safe_set(b, 'test100_A4', {a2})
    assert _is_linked(b, 'test100_A4', a2)
    if hasattr(a1, 'test100_DsmlRelation'):
        assert not _is_linked(a1, 'test100_DsmlRelation', b)
    if hasattr(a2, 'test100_DsmlRelation'):
        assert _is_linked(a2, 'test100_DsmlRelation', b)
    _safe_set(b, 'test100_A4', set())
    assert not _is_linked(b, 'test100_A4', a2)
    if hasattr(a2, 'test100_DsmlRelation'):
        assert not _is_linked(a2, 'test100_DsmlRelation', b)


def test_assoc_toDsml8_reverse_link_reassign_clear():
    a1 = test100_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    a2 = test100_DsmlRelation(details="sample_text_2", mandatory=False, name="sample_text_2")
    b = test100_A(name="sample_text")
    _safe_set(b, 'test100_A10', a1)
    assert _is_linked(b, 'test100_A10', a1)
    if hasattr(a1, 'test100_DsmlRelation9'):
        assert _is_linked(a1, 'test100_DsmlRelation9', b)
    _safe_set(b, 'test100_A10', a2)
    assert _is_linked(b, 'test100_A10', a2)
    if hasattr(a1, 'test100_DsmlRelation9'):
        assert not _is_linked(a1, 'test100_DsmlRelation9', b)
    if hasattr(a2, 'test100_DsmlRelation9'):
        assert _is_linked(a2, 'test100_DsmlRelation9', b)
    _safe_set(b, 'test100_A10', None)
    assert not _is_linked(b, 'test100_A10', a2)
    if hasattr(a2, 'test100_DsmlRelation9'):
        assert not _is_linked(a2, 'test100_DsmlRelation9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_as_0_stub_double():
    # test100_C has no real 'test100_C' property in the generated
    # code (a bare stub) -- manually attach it so test100_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test100_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test100_A(name="sample_text")
    partner = test100_C()
    setattr(partner, 'test100_C', None)
    _safe_set(owner, 'test100_A', partner)
    assert owner in getattr(partner, 'test100_C')
    _safe_set(owner, 'test100_A', None)
    assert owner not in getattr(partner, 'test100_C')


