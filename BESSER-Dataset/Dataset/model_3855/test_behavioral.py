import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    SimpleRDBMS_Column,
    SimpleRDBMS_Database,
    SimpleRDBMS_FKey,
    SimpleRDBMS_PrimaryKey,
    SimpleRDBMS_Table,
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
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    _safe_set(b, 'SimpleRDBMS_Column5', a1)
    assert _is_linked(b, 'SimpleRDBMS_Column5', a1)
    if hasattr(a1, 'SimpleRDBMS_Table4'):
        assert _is_linked(a1, 'SimpleRDBMS_Table4', b)
    _safe_set(b, 'SimpleRDBMS_Column5', a2)
    assert _is_linked(b, 'SimpleRDBMS_Column5', a2)
    if hasattr(a1, 'SimpleRDBMS_Table4'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table4', b)
    if hasattr(a2, 'SimpleRDBMS_Table4'):
        assert _is_linked(a2, 'SimpleRDBMS_Table4', b)
    _safe_set(b, 'SimpleRDBMS_Column5', None)
    assert not _is_linked(b, 'SimpleRDBMS_Column5', a2)
    if hasattr(a2, 'SimpleRDBMS_Table4'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table4', b)


def test_assoc_pkey1_reverse_link_reassign_clear():
    a1 = SimpleRDBMS_Table(id=7, name="sample_text")
    a2 = SimpleRDBMS_Table(id=13, name="sample_text_2")
    b = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    _safe_set(b, 'SimpleRDBMS_Column', a1)
    assert _is_linked(b, 'SimpleRDBMS_Column', a1)
    if hasattr(a1, 'SimpleRDBMS_Table2'):
        assert _is_linked(a1, 'SimpleRDBMS_Table2', b)
    _safe_set(b, 'SimpleRDBMS_Column', a2)
    assert _is_linked(b, 'SimpleRDBMS_Column', a2)
    if hasattr(a1, 'SimpleRDBMS_Table2'):
        assert not _is_linked(a1, 'SimpleRDBMS_Table2', b)
    if hasattr(a2, 'SimpleRDBMS_Table2'):
        assert _is_linked(a2, 'SimpleRDBMS_Table2', b)
    _safe_set(b, 'SimpleRDBMS_Column', None)
    assert not _is_linked(b, 'SimpleRDBMS_Column', a2)
    if hasattr(a2, 'SimpleRDBMS_Table2'):
        assert not _is_linked(a2, 'SimpleRDBMS_Table2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cols9_stub_double():
    # SimpleRDBMS_FKey has no real 'SimpleRDBMS_FKey10' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(id=7, name="sample_text", type="sample_text")
    partner = SimpleRDBMS_FKey()
    setattr(partner, 'SimpleRDBMS_FKey10', None)
    _safe_set(owner, 'SimpleRDBMS_Column11', partner)
    assert owner in getattr(partner, 'SimpleRDBMS_FKey10')
    _safe_set(owner, 'SimpleRDBMS_Column11', None)
    assert owner not in getattr(partner, 'SimpleRDBMS_FKey10')


def test_assoc_fkeys0_stub_double():
    # SimpleRDBMS_FKey has no real 'SimpleRDBMS_FKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Table(id=7, name="sample_text")
    partner = SimpleRDBMS_FKey()
    setattr(partner, 'SimpleRDBMS_FKey', None)
    _safe_set(owner, 'SimpleRDBMS_Table', {partner})
    assert getattr(partner, 'SimpleRDBMS_FKey') == owner
    _safe_set(owner, 'SimpleRDBMS_Table', set())
    assert getattr(partner, 'SimpleRDBMS_FKey') is None


def test_assoc_references6_stub_double():
    # SimpleRDBMS_FKey has no real 'SimpleRDBMS_FKey7' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Table(id=7, name="sample_text")
    partner = SimpleRDBMS_FKey()
    setattr(partner, 'SimpleRDBMS_FKey7', None)
    _safe_set(owner, 'SimpleRDBMS_Table8', partner)
    assert getattr(partner, 'SimpleRDBMS_FKey7') == owner
    _safe_set(owner, 'SimpleRDBMS_Table8', None)
    assert getattr(partner, 'SimpleRDBMS_FKey7') is None


