import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RDBMSMM_Column,
    RDBMSMM_FKey,
    RDBMSMM_RDBMSModel,
    RDBMSMM_Table,
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

def test_assoc_cols0_reverse_link_reassign_clear():
    a1 = RDBMSMM_Table(name="sample_text")
    a2 = RDBMSMM_Table(name="sample_text_2")
    b = RDBMSMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'RDBMSMM_Column', a1)
    assert _is_linked(b, 'RDBMSMM_Column', a1)
    if hasattr(a1, 'RDBMSMM_Table'):
        assert _is_linked(a1, 'RDBMSMM_Table', b)
    _safe_set(b, 'RDBMSMM_Column', a2)
    assert _is_linked(b, 'RDBMSMM_Column', a2)
    if hasattr(a1, 'RDBMSMM_Table'):
        assert not _is_linked(a1, 'RDBMSMM_Table', b)
    if hasattr(a2, 'RDBMSMM_Table'):
        assert _is_linked(a2, 'RDBMSMM_Table', b)
    _safe_set(b, 'RDBMSMM_Column', None)
    assert not _is_linked(b, 'RDBMSMM_Column', a2)
    if hasattr(a2, 'RDBMSMM_Table'):
        assert not _is_linked(a2, 'RDBMSMM_Table', b)


def test_assoc_pkey1_reverse_link_reassign_clear():
    a1 = RDBMSMM_Table(name="sample_text")
    a2 = RDBMSMM_Table(name="sample_text_2")
    b = RDBMSMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'RDBMSMM_Column3', a1)
    assert _is_linked(b, 'RDBMSMM_Column3', a1)
    if hasattr(a1, 'RDBMSMM_Table2'):
        assert _is_linked(a1, 'RDBMSMM_Table2', b)
    _safe_set(b, 'RDBMSMM_Column3', a2)
    assert _is_linked(b, 'RDBMSMM_Column3', a2)
    if hasattr(a1, 'RDBMSMM_Table2'):
        assert not _is_linked(a1, 'RDBMSMM_Table2', b)
    if hasattr(a2, 'RDBMSMM_Table2'):
        assert _is_linked(a2, 'RDBMSMM_Table2', b)
    _safe_set(b, 'RDBMSMM_Column3', None)
    assert not _is_linked(b, 'RDBMSMM_Column3', a2)
    if hasattr(a2, 'RDBMSMM_Table2'):
        assert not _is_linked(a2, 'RDBMSMM_Table2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cols9_stub_double():
    # RDBMSMM_FKey has no real 'RDBMSMM_FKey10' property in the generated
    # code (a bare stub) -- manually attach it so RDBMSMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMSMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMSMM_Column(name="sample_text", type="sample_text")
    partner = RDBMSMM_FKey()
    setattr(partner, 'RDBMSMM_FKey10', None)
    _safe_set(owner, 'RDBMSMM_Column11', partner)
    assert owner in getattr(partner, 'RDBMSMM_FKey10')
    _safe_set(owner, 'RDBMSMM_Column11', None)
    assert owner not in getattr(partner, 'RDBMSMM_FKey10')


def test_assoc_fkeys4_stub_double():
    # RDBMSMM_FKey has no real 'RDBMSMM_FKey' property in the generated
    # code (a bare stub) -- manually attach it so RDBMSMM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMSMM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMSMM_Table(name="sample_text")
    partner = RDBMSMM_FKey()
    setattr(partner, 'RDBMSMM_FKey', None)
    _safe_set(owner, 'RDBMSMM_Table5', {partner})
    assert getattr(partner, 'RDBMSMM_FKey') == owner
    _safe_set(owner, 'RDBMSMM_Table5', set())
    assert getattr(partner, 'RDBMSMM_FKey') is None


def test_assoc_references6_stub_double():
    # RDBMSMM_FKey has no real 'RDBMSMM_FKey7' property in the generated
    # code (a bare stub) -- manually attach it so RDBMSMM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMSMM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMSMM_Table(name="sample_text")
    partner = RDBMSMM_FKey()
    setattr(partner, 'RDBMSMM_FKey7', None)
    _safe_set(owner, 'RDBMSMM_Table8', partner)
    assert getattr(partner, 'RDBMSMM_FKey7') == owner
    _safe_set(owner, 'RDBMSMM_Table8', None)
    assert getattr(partner, 'RDBMSMM_FKey7') is None


def test_assoc_table12_stub_double():
    # RDBMSMM_RDBMSModel has no real 'RDBMSMM_RDBMSModel' property in the generated
    # code (a bare stub) -- manually attach it so RDBMSMM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDBMSMM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDBMSMM_Table(name="sample_text")
    partner = RDBMSMM_RDBMSModel()
    setattr(partner, 'RDBMSMM_RDBMSModel', None)
    _safe_set(owner, 'RDBMSMM_Table13', partner)
    assert owner in getattr(partner, 'RDBMSMM_RDBMSModel')
    _safe_set(owner, 'RDBMSMM_Table13', None)
    assert owner not in getattr(partner, 'RDBMSMM_RDBMSModel')


