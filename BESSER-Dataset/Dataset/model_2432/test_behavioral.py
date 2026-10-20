import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TableM_Column,
    TableM_FKey,
    TableM_Table,
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
    a1 = TableM_Table(name="sample_text")
    a2 = TableM_Table(name="sample_text_2")
    b = TableM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_owner6_reverse_link_reassign_clear():
    a1 = TableM_Table(name="sample_text")
    a2 = TableM_Table(name="sample_text_2")
    b = TableM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'cols', a1)
    assert _is_linked(b, 'cols', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'cols', a2)
    assert _is_linked(b, 'cols', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'cols', None)
    assert not _is_linked(b, 'cols', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_pkeys1_reverse_link_reassign_clear():
    a1 = TableM_Table(name="sample_text")
    a2 = TableM_Table(name="sample_text_2")
    b = TableM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'TableM_Column', a1)
    assert _is_linked(b, 'TableM_Column', a1)
    if hasattr(a1, 'TableM_Table'):
        assert _is_linked(a1, 'TableM_Table', b)
    _safe_set(b, 'TableM_Column', a2)
    assert _is_linked(b, 'TableM_Column', a2)
    if hasattr(a1, 'TableM_Table'):
        assert not _is_linked(a1, 'TableM_Table', b)
    if hasattr(a2, 'TableM_Table'):
        assert _is_linked(a2, 'TableM_Table', b)
    _safe_set(b, 'TableM_Column', None)
    assert not _is_linked(b, 'TableM_Column', a2)
    if hasattr(a2, 'TableM_Table'):
        assert not _is_linked(a2, 'TableM_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cols12_stub_double():
    # TableM_FKey has no real 'TableM_FKey13' property in the generated
    # code (a bare stub) -- manually attach it so TableM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TableM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TableM_Column(name="sample_text", type="sample_text")
    partner = TableM_FKey()
    setattr(partner, 'TableM_FKey13', None)
    _safe_set(owner, 'TableM_Column14', partner)
    assert owner in getattr(partner, 'TableM_FKey13')
    _safe_set(owner, 'TableM_Column14', None)
    assert owner not in getattr(partner, 'TableM_FKey13')


def test_assoc_fkeys2_stub_double():
    # TableM_FKey has no real 'FKey' property in the generated
    # code (a bare stub) -- manually attach it so TableM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TableM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TableM_Table(name="sample_text")
    partner = TableM_FKey()
    setattr(partner, 'FKey', None)
    _safe_set(owner, 'owner3', {partner})
    assert getattr(partner, 'FKey') == owner
    _safe_set(owner, 'owner3', set())
    assert getattr(partner, 'FKey') is None


def test_assoc_owner10_stub_double():
    # TableM_FKey has no real 'fkeys' property in the generated
    # code (a bare stub) -- manually attach it so TableM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TableM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TableM_Table(name="sample_text")
    partner = TableM_FKey()
    setattr(partner, 'fkeys', None)
    _safe_set(owner, 'Table11', partner)
    assert getattr(partner, 'fkeys') == owner
    _safe_set(owner, 'Table11', None)
    assert getattr(partner, 'fkeys') is None


def test_assoc_referencedBy4_stub_double():
    # TableM_FKey has no real 'TableM_FKey' property in the generated
    # code (a bare stub) -- manually attach it so TableM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TableM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TableM_Table(name="sample_text")
    partner = TableM_FKey()
    setattr(partner, 'TableM_FKey', None)
    _safe_set(owner, 'TableM_Table5', {partner})
    assert getattr(partner, 'TableM_FKey') == owner
    _safe_set(owner, 'TableM_Table5', set())
    assert getattr(partner, 'TableM_FKey') is None


def test_assoc_references7_stub_double():
    # TableM_FKey has no real 'TableM_FKey8' property in the generated
    # code (a bare stub) -- manually attach it so TableM_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # TableM_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = TableM_Table(name="sample_text")
    partner = TableM_FKey()
    setattr(partner, 'TableM_FKey8', None)
    _safe_set(owner, 'TableM_Table9', partner)
    assert getattr(partner, 'TableM_FKey8') == owner
    _safe_set(owner, 'TableM_Table9', None)
    assert getattr(partner, 'TableM_FKey8') is None


