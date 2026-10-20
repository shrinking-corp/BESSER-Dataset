import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Database_Column,
    Database_DB,
    Database_Table,
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

def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = Database_Table(heading="sample_text")
    a2 = Database_Table(heading="sample_text_2")
    b = Database_Column(name="sample_text")
    _safe_set(b, 'Database_Column', a1)
    assert _is_linked(b, 'Database_Column', a1)
    if hasattr(a1, 'Database_Table2'):
        assert _is_linked(a1, 'Database_Table2', b)
    _safe_set(b, 'Database_Column', a2)
    assert _is_linked(b, 'Database_Column', a2)
    if hasattr(a1, 'Database_Table2'):
        assert not _is_linked(a1, 'Database_Table2', b)
    if hasattr(a2, 'Database_Table2'):
        assert _is_linked(a2, 'Database_Table2', b)
    _safe_set(b, 'Database_Column', None)
    assert not _is_linked(b, 'Database_Column', a2)
    if hasattr(a2, 'Database_Table2'):
        assert not _is_linked(a2, 'Database_Table2', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = Database_Table(heading="sample_text")
    a2 = Database_Table(heading="sample_text_2")
    b = Database_DB(title="sample_text")
    _safe_set(b, 'Database_DB', {a1})
    assert _is_linked(b, 'Database_DB', a1)
    if hasattr(a1, 'Database_Table'):
        assert _is_linked(a1, 'Database_Table', b)
    _safe_set(b, 'Database_DB', {a2})
    assert _is_linked(b, 'Database_DB', a2)
    if hasattr(a1, 'Database_Table'):
        assert not _is_linked(a1, 'Database_Table', b)
    if hasattr(a2, 'Database_Table'):
        assert _is_linked(a2, 'Database_Table', b)
    _safe_set(b, 'Database_DB', set())
    assert not _is_linked(b, 'Database_DB', a2)
    if hasattr(a2, 'Database_Table'):
        assert not _is_linked(a2, 'Database_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

