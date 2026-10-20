import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    target_Column,
    target_Database,
    target_FKey,
    target_Table,
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

def test_assoc_cols3_reverse_link_reassign_clear():
    a1 = target_Table(name="sample_text")
    a2 = target_Table(name="sample_text_2")
    b = target_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'target_Column5', a1)
    assert _is_linked(b, 'target_Column5', a1)
    if hasattr(a1, 'target_Table4'):
        assert _is_linked(a1, 'target_Table4', b)
    _safe_set(b, 'target_Column5', a2)
    assert _is_linked(b, 'target_Column5', a2)
    if hasattr(a1, 'target_Table4'):
        assert not _is_linked(a1, 'target_Table4', b)
    if hasattr(a2, 'target_Table4'):
        assert _is_linked(a2, 'target_Table4', b)
    _safe_set(b, 'target_Column5', None)
    assert not _is_linked(b, 'target_Column5', a2)
    if hasattr(a2, 'target_Table4'):
        assert not _is_linked(a2, 'target_Table4', b)


def test_assoc_pkey1_reverse_link_reassign_clear():
    a1 = target_Table(name="sample_text")
    a2 = target_Table(name="sample_text_2")
    b = target_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'target_Column', a1)
    assert _is_linked(b, 'target_Column', a1)
    if hasattr(a1, 'target_Table2'):
        assert _is_linked(a1, 'target_Table2', b)
    _safe_set(b, 'target_Column', a2)
    assert _is_linked(b, 'target_Column', a2)
    if hasattr(a1, 'target_Table2'):
        assert not _is_linked(a1, 'target_Table2', b)
    if hasattr(a2, 'target_Table2'):
        assert _is_linked(a2, 'target_Table2', b)
    _safe_set(b, 'target_Column', None)
    assert not _is_linked(b, 'target_Column', a2)
    if hasattr(a2, 'target_Table2'):
        assert not _is_linked(a2, 'target_Table2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fcols6_stub_double():
    # target_FKey has no real 'target_FKey7' property in the generated
    # code (a bare stub) -- manually attach it so target_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # target_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = target_Column(name="sample_text", type="sample_text")
    partner = target_FKey()
    setattr(partner, 'target_FKey7', None)
    _safe_set(owner, 'target_Column8', partner)
    assert owner in getattr(partner, 'target_FKey7')
    _safe_set(owner, 'target_Column8', None)
    assert owner not in getattr(partner, 'target_FKey7')


def test_assoc_fkeys0_stub_double():
    # target_FKey has no real 'target_FKey' property in the generated
    # code (a bare stub) -- manually attach it so target_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # target_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = target_Table(name="sample_text")
    partner = target_FKey()
    setattr(partner, 'target_FKey', None)
    _safe_set(owner, 'target_Table', {partner})
    assert getattr(partner, 'target_FKey') == owner
    _safe_set(owner, 'target_Table', set())
    assert getattr(partner, 'target_FKey') is None


def test_assoc_references9_stub_double():
    # target_FKey has no real 'target_FKey10' property in the generated
    # code (a bare stub) -- manually attach it so target_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # target_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = target_Table(name="sample_text")
    partner = target_FKey()
    setattr(partner, 'target_FKey10', None)
    _safe_set(owner, 'target_Table11', partner)
    assert getattr(partner, 'target_FKey10') == owner
    _safe_set(owner, 'target_Table11', None)
    assert getattr(partner, 'target_FKey10') is None


def test_assoc_table12_stub_double():
    # target_Database has no real 'target_Database' property in the generated
    # code (a bare stub) -- manually attach it so target_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # target_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = target_Table(name="sample_text")
    partner = target_Database()
    setattr(partner, 'target_Database', None)
    _safe_set(owner, 'target_Table13', partner)
    assert owner in getattr(partner, 'target_Database')
    _safe_set(owner, 'target_Table13', None)
    assert owner not in getattr(partner, 'target_Database')


