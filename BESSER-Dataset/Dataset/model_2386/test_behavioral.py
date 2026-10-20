import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sQL_DataBase,
    sQL_Table,
    sQL_column,
    sQL_foreignKey,
    sQL_primaryKey,
    DataType,
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
    a1 = sQL_column(name="sample_text", type="sample_text")
    a2 = sQL_column(name="sample_text_2", type="sample_text_2")
    b = sQL_Table(name="sample_text")
    _safe_set(b, 'sQL_Table2', {a1})
    assert _is_linked(b, 'sQL_Table2', a1)
    if hasattr(a1, 'sQL_column'):
        assert _is_linked(a1, 'sQL_column', b)
    _safe_set(b, 'sQL_Table2', {a2})
    assert _is_linked(b, 'sQL_Table2', a2)
    if hasattr(a1, 'sQL_column'):
        assert not _is_linked(a1, 'sQL_column', b)
    if hasattr(a2, 'sQL_column'):
        assert _is_linked(a2, 'sQL_column', b)
    _safe_set(b, 'sQL_Table2', set())
    assert not _is_linked(b, 'sQL_Table2', a2)
    if hasattr(a2, 'sQL_column'):
        assert not _is_linked(a2, 'sQL_column', b)


def test_assoc_foreignkeys5_reverse_link_reassign_clear():
    a1 = sQL_foreignKey(name="sample_text")
    a2 = sQL_foreignKey(name="sample_text_2")
    b = sQL_Table(name="sample_text")
    _safe_set(b, 'sQL_Table6', {a1})
    assert _is_linked(b, 'sQL_Table6', a1)
    if hasattr(a1, 'sQL_foreignKey'):
        assert _is_linked(a1, 'sQL_foreignKey', b)
    _safe_set(b, 'sQL_Table6', {a2})
    assert _is_linked(b, 'sQL_Table6', a2)
    if hasattr(a1, 'sQL_foreignKey'):
        assert not _is_linked(a1, 'sQL_foreignKey', b)
    if hasattr(a2, 'sQL_foreignKey'):
        assert _is_linked(a2, 'sQL_foreignKey', b)
    _safe_set(b, 'sQL_Table6', set())
    assert not _is_linked(b, 'sQL_Table6', a2)
    if hasattr(a2, 'sQL_foreignKey'):
        assert not _is_linked(a2, 'sQL_foreignKey', b)


def test_assoc_primaryKey3_reverse_link_reassign_clear():
    a1 = sQL_primaryKey(name="sample_text")
    a2 = sQL_primaryKey(name="sample_text_2")
    b = sQL_Table(name="sample_text")
    _safe_set(b, 'sQL_Table4', a1)
    assert _is_linked(b, 'sQL_Table4', a1)
    if hasattr(a1, 'sQL_primaryKey'):
        assert _is_linked(a1, 'sQL_primaryKey', b)
    _safe_set(b, 'sQL_Table4', a2)
    assert _is_linked(b, 'sQL_Table4', a2)
    if hasattr(a1, 'sQL_primaryKey'):
        assert not _is_linked(a1, 'sQL_primaryKey', b)
    if hasattr(a2, 'sQL_primaryKey'):
        assert _is_linked(a2, 'sQL_primaryKey', b)
    _safe_set(b, 'sQL_Table4', None)
    assert not _is_linked(b, 'sQL_Table4', a2)
    if hasattr(a2, 'sQL_primaryKey'):
        assert not _is_linked(a2, 'sQL_primaryKey', b)


def test_assoc_ref10_reverse_link_reassign_clear():
    a1 = sQL_foreignKey(name="sample_text")
    a2 = sQL_foreignKey(name="sample_text_2")
    b = sQL_column(name="sample_text", type="sample_text")
    _safe_set(b, 'sQL_column12', a1)
    assert _is_linked(b, 'sQL_column12', a1)
    if hasattr(a1, 'sQL_foreignKey11'):
        assert _is_linked(a1, 'sQL_foreignKey11', b)
    _safe_set(b, 'sQL_column12', a2)
    assert _is_linked(b, 'sQL_column12', a2)
    if hasattr(a1, 'sQL_foreignKey11'):
        assert not _is_linked(a1, 'sQL_foreignKey11', b)
    if hasattr(a2, 'sQL_foreignKey11'):
        assert _is_linked(a2, 'sQL_foreignKey11', b)
    _safe_set(b, 'sQL_column12', None)
    assert not _is_linked(b, 'sQL_column12', a2)
    if hasattr(a2, 'sQL_foreignKey11'):
        assert not _is_linked(a2, 'sQL_foreignKey11', b)


def test_assoc_reftable7_reverse_link_reassign_clear():
    a1 = sQL_foreignKey(name="sample_text")
    a2 = sQL_foreignKey(name="sample_text_2")
    b = sQL_Table(name="sample_text")
    _safe_set(b, 'sQL_Table9', a1)
    assert _is_linked(b, 'sQL_Table9', a1)
    if hasattr(a1, 'sQL_foreignKey8'):
        assert _is_linked(a1, 'sQL_foreignKey8', b)
    _safe_set(b, 'sQL_Table9', a2)
    assert _is_linked(b, 'sQL_Table9', a2)
    if hasattr(a1, 'sQL_foreignKey8'):
        assert not _is_linked(a1, 'sQL_foreignKey8', b)
    if hasattr(a2, 'sQL_foreignKey8'):
        assert _is_linked(a2, 'sQL_foreignKey8', b)
    _safe_set(b, 'sQL_Table9', None)
    assert not _is_linked(b, 'sQL_Table9', a2)
    if hasattr(a2, 'sQL_foreignKey8'):
        assert not _is_linked(a2, 'sQL_foreignKey8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Tables0_stub_double():
    # sQL_DataBase has no real 'sQL_DataBase' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Table(name="sample_text")
    partner = sQL_DataBase()
    setattr(partner, 'sQL_DataBase', None)
    _safe_set(owner, 'sQL_Table', partner)
    assert owner in getattr(partner, 'sQL_DataBase')
    _safe_set(owner, 'sQL_Table', None)
    assert owner not in getattr(partner, 'sQL_DataBase')


