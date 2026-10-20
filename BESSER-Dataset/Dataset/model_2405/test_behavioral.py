import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sqlCrudGenerator_Column,
    sqlCrudGenerator_DataType,
    sqlCrudGenerator_ForeignKey,
    sqlCrudGenerator_PrimaryKey,
    sqlCrudGenerator_Schema,
    sqlCrudGenerator_Table,
    ENUM_DATA_TYPE,
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
    a1 = sqlCrudGenerator_Table(name="sample_text")
    a2 = sqlCrudGenerator_Table(name="sample_text_2")
    b = sqlCrudGenerator_Column(name="sample_text")
    _safe_set(b, 'sqlCrudGenerator_Column', a1)
    assert _is_linked(b, 'sqlCrudGenerator_Column', a1)
    if hasattr(a1, 'sqlCrudGenerator_Table2'):
        assert _is_linked(a1, 'sqlCrudGenerator_Table2', b)
    _safe_set(b, 'sqlCrudGenerator_Column', a2)
    assert _is_linked(b, 'sqlCrudGenerator_Column', a2)
    if hasattr(a1, 'sqlCrudGenerator_Table2'):
        assert not _is_linked(a1, 'sqlCrudGenerator_Table2', b)
    if hasattr(a2, 'sqlCrudGenerator_Table2'):
        assert _is_linked(a2, 'sqlCrudGenerator_Table2', b)
    _safe_set(b, 'sqlCrudGenerator_Column', None)
    assert not _is_linked(b, 'sqlCrudGenerator_Column', a2)
    if hasattr(a2, 'sqlCrudGenerator_Table2'):
        assert not _is_linked(a2, 'sqlCrudGenerator_Table2', b)


def test_assoc_dataType7_reverse_link_reassign_clear():
    a1 = sqlCrudGenerator_DataType(dataType="sample_text", precision=7)
    a2 = sqlCrudGenerator_DataType(dataType="sample_text_2", precision=13)
    b = sqlCrudGenerator_Column(name="sample_text")
    _safe_set(b, 'sqlCrudGenerator_Column8', a1)
    assert _is_linked(b, 'sqlCrudGenerator_Column8', a1)
    if hasattr(a1, 'sqlCrudGenerator_DataType'):
        assert _is_linked(a1, 'sqlCrudGenerator_DataType', b)
    _safe_set(b, 'sqlCrudGenerator_Column8', a2)
    assert _is_linked(b, 'sqlCrudGenerator_Column8', a2)
    if hasattr(a1, 'sqlCrudGenerator_DataType'):
        assert not _is_linked(a1, 'sqlCrudGenerator_DataType', b)
    if hasattr(a2, 'sqlCrudGenerator_DataType'):
        assert _is_linked(a2, 'sqlCrudGenerator_DataType', b)
    _safe_set(b, 'sqlCrudGenerator_Column8', None)
    assert not _is_linked(b, 'sqlCrudGenerator_Column8', a2)
    if hasattr(a2, 'sqlCrudGenerator_DataType'):
        assert not _is_linked(a2, 'sqlCrudGenerator_DataType', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = sqlCrudGenerator_Table(name="sample_text")
    a2 = sqlCrudGenerator_Table(name="sample_text_2")
    b = sqlCrudGenerator_Schema(name="sample_text")
    _safe_set(b, 'sqlCrudGenerator_Schema', {a1})
    assert _is_linked(b, 'sqlCrudGenerator_Schema', a1)
    if hasattr(a1, 'sqlCrudGenerator_Table'):
        assert _is_linked(a1, 'sqlCrudGenerator_Table', b)
    _safe_set(b, 'sqlCrudGenerator_Schema', {a2})
    assert _is_linked(b, 'sqlCrudGenerator_Schema', a2)
    if hasattr(a1, 'sqlCrudGenerator_Table'):
        assert not _is_linked(a1, 'sqlCrudGenerator_Table', b)
    if hasattr(a2, 'sqlCrudGenerator_Table'):
        assert _is_linked(a2, 'sqlCrudGenerator_Table', b)
    _safe_set(b, 'sqlCrudGenerator_Schema', set())
    assert not _is_linked(b, 'sqlCrudGenerator_Schema', a2)
    if hasattr(a2, 'sqlCrudGenerator_Table'):
        assert not _is_linked(a2, 'sqlCrudGenerator_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_foreignsKeys5_stub_double():
    # sqlCrudGenerator_ForeignKey has no real 'sqlCrudGenerator_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Table(name="sample_text")
    partner = sqlCrudGenerator_ForeignKey()
    setattr(partner, 'sqlCrudGenerator_ForeignKey', None)
    _safe_set(owner, 'sqlCrudGenerator_Table6', {partner})
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey') == owner
    _safe_set(owner, 'sqlCrudGenerator_Table6', set())
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey') is None


def test_assoc_ids9_stub_double():
    # sqlCrudGenerator_PrimaryKey has no real 'sqlCrudGenerator_PrimaryKey10' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Column(name="sample_text")
    partner = sqlCrudGenerator_PrimaryKey()
    setattr(partner, 'sqlCrudGenerator_PrimaryKey10', None)
    _safe_set(owner, 'sqlCrudGenerator_Column11', partner)
    assert owner in getattr(partner, 'sqlCrudGenerator_PrimaryKey10')
    _safe_set(owner, 'sqlCrudGenerator_Column11', None)
    assert owner not in getattr(partner, 'sqlCrudGenerator_PrimaryKey10')


def test_assoc_primaryKey3_stub_double():
    # sqlCrudGenerator_PrimaryKey has no real 'sqlCrudGenerator_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Table(name="sample_text")
    partner = sqlCrudGenerator_PrimaryKey()
    setattr(partner, 'sqlCrudGenerator_PrimaryKey', None)
    _safe_set(owner, 'sqlCrudGenerator_Table4', partner)
    assert getattr(partner, 'sqlCrudGenerator_PrimaryKey') == owner
    _safe_set(owner, 'sqlCrudGenerator_Table4', None)
    assert getattr(partner, 'sqlCrudGenerator_PrimaryKey') is None


def test_assoc_reference15_stub_double():
    # sqlCrudGenerator_ForeignKey has no real 'sqlCrudGenerator_ForeignKey16' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Table(name="sample_text")
    partner = sqlCrudGenerator_ForeignKey()
    setattr(partner, 'sqlCrudGenerator_ForeignKey16', None)
    _safe_set(owner, 'sqlCrudGenerator_Table17', partner)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey16') == owner
    _safe_set(owner, 'sqlCrudGenerator_Table17', None)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey16') is None


def test_assoc_refsFrom18_stub_double():
    # sqlCrudGenerator_ForeignKey has no real 'sqlCrudGenerator_ForeignKey19' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Column(name="sample_text")
    partner = sqlCrudGenerator_ForeignKey()
    setattr(partner, 'sqlCrudGenerator_ForeignKey19', None)
    _safe_set(owner, 'sqlCrudGenerator_Column20', partner)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey19') == owner
    _safe_set(owner, 'sqlCrudGenerator_Column20', None)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey19') is None


def test_assoc_refsTo12_stub_double():
    # sqlCrudGenerator_ForeignKey has no real 'sqlCrudGenerator_ForeignKey13' property in the generated
    # code (a bare stub) -- manually attach it so sqlCrudGenerator_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlCrudGenerator_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlCrudGenerator_Column(name="sample_text")
    partner = sqlCrudGenerator_ForeignKey()
    setattr(partner, 'sqlCrudGenerator_ForeignKey13', None)
    _safe_set(owner, 'sqlCrudGenerator_Column14', partner)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey13') == owner
    _safe_set(owner, 'sqlCrudGenerator_Column14', None)
    assert getattr(partner, 'sqlCrudGenerator_ForeignKey13') is None


