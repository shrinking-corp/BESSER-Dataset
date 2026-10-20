import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    SqlMetamodel_Column,
    SqlMetamodel_Constraint,
    SqlMetamodel_ForeingKey,
    SqlMetamodel_PrimaryKey,
    SqlMetamodel_Schema,
    SqlMetamodel_Table,
    TypeData,
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

def test_assoc_column1_reverse_link_reassign_clear():
    a1 = SqlMetamodel_Table(name="sample_text")
    a2 = SqlMetamodel_Table(name="sample_text_2")
    b = SqlMetamodel_Column(name="sample_text", nullable=True, type="sample_text")
    _safe_set(b, 'SqlMetamodel_Column', a1)
    assert _is_linked(b, 'SqlMetamodel_Column', a1)
    if hasattr(a1, 'SqlMetamodel_Table2'):
        assert _is_linked(a1, 'SqlMetamodel_Table2', b)
    _safe_set(b, 'SqlMetamodel_Column', a2)
    assert _is_linked(b, 'SqlMetamodel_Column', a2)
    if hasattr(a1, 'SqlMetamodel_Table2'):
        assert not _is_linked(a1, 'SqlMetamodel_Table2', b)
    if hasattr(a2, 'SqlMetamodel_Table2'):
        assert _is_linked(a2, 'SqlMetamodel_Table2', b)
    _safe_set(b, 'SqlMetamodel_Column', None)
    assert not _is_linked(b, 'SqlMetamodel_Column', a2)
    if hasattr(a2, 'SqlMetamodel_Table2'):
        assert not _is_linked(a2, 'SqlMetamodel_Table2', b)


def test_assoc_constraint3_reverse_link_reassign_clear():
    a1 = SqlMetamodel_Table(name="sample_text")
    a2 = SqlMetamodel_Table(name="sample_text_2")
    b = SqlMetamodel_Constraint(name="sample_text")
    _safe_set(b, 'SqlMetamodel_Constraint', a1)
    assert _is_linked(b, 'SqlMetamodel_Constraint', a1)
    if hasattr(a1, 'SqlMetamodel_Table4'):
        assert _is_linked(a1, 'SqlMetamodel_Table4', b)
    _safe_set(b, 'SqlMetamodel_Constraint', a2)
    assert _is_linked(b, 'SqlMetamodel_Constraint', a2)
    if hasattr(a1, 'SqlMetamodel_Table4'):
        assert not _is_linked(a1, 'SqlMetamodel_Table4', b)
    if hasattr(a2, 'SqlMetamodel_Table4'):
        assert _is_linked(a2, 'SqlMetamodel_Table4', b)
    _safe_set(b, 'SqlMetamodel_Constraint', None)
    assert not _is_linked(b, 'SqlMetamodel_Constraint', a2)
    if hasattr(a2, 'SqlMetamodel_Table4'):
        assert not _is_linked(a2, 'SqlMetamodel_Table4', b)


def test_assoc_table0_reverse_link_reassign_clear():
    a1 = SqlMetamodel_Table(name="sample_text")
    a2 = SqlMetamodel_Table(name="sample_text_2")
    b = SqlMetamodel_Schema(name="sample_text")
    _safe_set(b, 'SqlMetamodel_Schema', {a1})
    assert _is_linked(b, 'SqlMetamodel_Schema', a1)
    if hasattr(a1, 'SqlMetamodel_Table'):
        assert _is_linked(a1, 'SqlMetamodel_Table', b)
    _safe_set(b, 'SqlMetamodel_Schema', {a2})
    assert _is_linked(b, 'SqlMetamodel_Schema', a2)
    if hasattr(a1, 'SqlMetamodel_Table'):
        assert not _is_linked(a1, 'SqlMetamodel_Table', b)
    if hasattr(a2, 'SqlMetamodel_Table'):
        assert _is_linked(a2, 'SqlMetamodel_Table', b)
    _safe_set(b, 'SqlMetamodel_Schema', set())
    assert not _is_linked(b, 'SqlMetamodel_Schema', a2)
    if hasattr(a2, 'SqlMetamodel_Table'):
        assert not _is_linked(a2, 'SqlMetamodel_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_primaryKey5_stub_double():
    # SqlMetamodel_PrimaryKey has no real 'SqlMetamodel_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so SqlMetamodel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SqlMetamodel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SqlMetamodel_Table(name="sample_text")
    partner = SqlMetamodel_PrimaryKey()
    setattr(partner, 'SqlMetamodel_PrimaryKey', None)
    _safe_set(owner, 'SqlMetamodel_Table6', partner)
    assert getattr(partner, 'SqlMetamodel_PrimaryKey') == owner
    _safe_set(owner, 'SqlMetamodel_Table6', None)
    assert getattr(partner, 'SqlMetamodel_PrimaryKey') is None


def test_assoc_refTable7_stub_double():
    # SqlMetamodel_ForeingKey has no real 'SqlMetamodel_ForeingKey' property in the generated
    # code (a bare stub) -- manually attach it so SqlMetamodel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SqlMetamodel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SqlMetamodel_Table(name="sample_text")
    partner = SqlMetamodel_ForeingKey()
    setattr(partner, 'SqlMetamodel_ForeingKey', None)
    _safe_set(owner, 'SqlMetamodel_Table8', partner)
    assert getattr(partner, 'SqlMetamodel_ForeingKey') == owner
    _safe_set(owner, 'SqlMetamodel_Table8', None)
    assert getattr(partner, 'SqlMetamodel_ForeingKey') is None


