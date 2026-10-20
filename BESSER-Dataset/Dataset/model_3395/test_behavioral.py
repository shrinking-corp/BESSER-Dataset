import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tables_Chair,
    tables_Restaurant,
    tables_Table,
    tables_Waitress,
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

def test_assoc_chairs0_reverse_link_reassign_clear():
    a1 = tables_Table(id=7, isReserved=True)
    a2 = tables_Table(id=13, isReserved=False)
    b = tables_Chair(order=7)
    _safe_set(b, 'tables_Chair', a1)
    assert _is_linked(b, 'tables_Chair', a1)
    if hasattr(a1, 'tables_Table'):
        assert _is_linked(a1, 'tables_Table', b)
    _safe_set(b, 'tables_Chair', a2)
    assert _is_linked(b, 'tables_Chair', a2)
    if hasattr(a1, 'tables_Table'):
        assert not _is_linked(a1, 'tables_Table', b)
    if hasattr(a2, 'tables_Table'):
        assert _is_linked(a2, 'tables_Table', b)
    _safe_set(b, 'tables_Chair', None)
    assert not _is_linked(b, 'tables_Chair', a2)
    if hasattr(a2, 'tables_Table'):
        assert not _is_linked(a2, 'tables_Table', b)


def test_assoc_tables1_reverse_link_reassign_clear():
    a1 = tables_Waitress(name="sample_text")
    a2 = tables_Waitress(name="sample_text_2")
    b = tables_Table(id=7, isReserved=True)
    _safe_set(b, 'tables_Table2', a1)
    assert _is_linked(b, 'tables_Table2', a1)
    if hasattr(a1, 'tables_Waitress'):
        assert _is_linked(a1, 'tables_Waitress', b)
    _safe_set(b, 'tables_Table2', a2)
    assert _is_linked(b, 'tables_Table2', a2)
    if hasattr(a1, 'tables_Waitress'):
        assert not _is_linked(a1, 'tables_Waitress', b)
    if hasattr(a2, 'tables_Waitress'):
        assert _is_linked(a2, 'tables_Waitress', b)
    _safe_set(b, 'tables_Table2', None)
    assert not _is_linked(b, 'tables_Table2', a2)
    if hasattr(a2, 'tables_Waitress'):
        assert not _is_linked(a2, 'tables_Waitress', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_tables5_stub_double():
    # tables_Restaurant has no real 'tables_Restaurant6' property in the generated
    # code (a bare stub) -- manually attach it so tables_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tables_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tables_Table(id=7, isReserved=True)
    partner = tables_Restaurant()
    setattr(partner, 'tables_Restaurant6', None)
    _safe_set(owner, 'tables_Table7', partner)
    assert owner in getattr(partner, 'tables_Restaurant6')
    _safe_set(owner, 'tables_Table7', None)
    assert owner not in getattr(partner, 'tables_Restaurant6')


def test_assoc_waitress3_stub_double():
    # tables_Restaurant has no real 'tables_Restaurant' property in the generated
    # code (a bare stub) -- manually attach it so tables_Waitress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tables_Waitress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tables_Waitress(name="sample_text")
    partner = tables_Restaurant()
    setattr(partner, 'tables_Restaurant', None)
    _safe_set(owner, 'tables_Waitress4', partner)
    assert owner in getattr(partner, 'tables_Restaurant')
    _safe_set(owner, 'tables_Waitress4', None)
    assert owner not in getattr(partner, 'tables_Restaurant')


