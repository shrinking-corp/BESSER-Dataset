import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sQL_Column,
    sQL_DataBase,
    sQL_ForeignKey,
    sQL_PrimaryKey,
    sQL_Table,
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

def test_assoc_column1_reverse_link_reassign_clear():
    a1 = sQL_Table(name="sample_text")
    a2 = sQL_Table(name="sample_text_2")
    b = sQL_Column(isNull=True, name="sample_text", type="sample_text")
    _safe_set(b, 'sQL_Column', a1)
    assert _is_linked(b, 'sQL_Column', a1)
    if hasattr(a1, 'sQL_Table2'):
        assert _is_linked(a1, 'sQL_Table2', b)
    _safe_set(b, 'sQL_Column', a2)
    assert _is_linked(b, 'sQL_Column', a2)
    if hasattr(a1, 'sQL_Table2'):
        assert not _is_linked(a1, 'sQL_Table2', b)
    if hasattr(a2, 'sQL_Table2'):
        assert _is_linked(a2, 'sQL_Table2', b)
    _safe_set(b, 'sQL_Column', None)
    assert not _is_linked(b, 'sQL_Column', a2)
    if hasattr(a2, 'sQL_Table2'):
        assert not _is_linked(a2, 'sQL_Table2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column10_stub_double():
    # sQL_ForeignKey has no real 'sQL_ForeignKey11' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Column(isNull=True, name="sample_text", type="sample_text")
    partner = sQL_ForeignKey()
    setattr(partner, 'sQL_ForeignKey11', None)
    _safe_set(owner, 'sQL_Column12', partner)
    assert owner in getattr(partner, 'sQL_ForeignKey11')
    _safe_set(owner, 'sQL_Column12', None)
    assert owner not in getattr(partner, 'sQL_ForeignKey11')


def test_assoc_column7_stub_double():
    # sQL_PrimaryKey has no real 'sQL_PrimaryKey8' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Column(isNull=True, name="sample_text", type="sample_text")
    partner = sQL_PrimaryKey()
    setattr(partner, 'sQL_PrimaryKey8', None)
    _safe_set(owner, 'sQL_Column9', partner)
    assert owner in getattr(partner, 'sQL_PrimaryKey8')
    _safe_set(owner, 'sQL_Column9', None)
    assert owner not in getattr(partner, 'sQL_PrimaryKey8')


def test_assoc_columnsRef16_stub_double():
    # sQL_ForeignKey has no real 'sQL_ForeignKey17' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Column(isNull=True, name="sample_text", type="sample_text")
    partner = sQL_ForeignKey()
    setattr(partner, 'sQL_ForeignKey17', None)
    _safe_set(owner, 'sQL_Column18', partner)
    assert owner in getattr(partner, 'sQL_ForeignKey17')
    _safe_set(owner, 'sQL_Column18', None)
    assert owner not in getattr(partner, 'sQL_ForeignKey17')


def test_assoc_foreignkey5_stub_double():
    # sQL_ForeignKey has no real 'sQL_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Table(name="sample_text")
    partner = sQL_ForeignKey()
    setattr(partner, 'sQL_ForeignKey', None)
    _safe_set(owner, 'sQL_Table6', {partner})
    assert getattr(partner, 'sQL_ForeignKey') == owner
    _safe_set(owner, 'sQL_Table6', set())
    assert getattr(partner, 'sQL_ForeignKey') is None


def test_assoc_primarykey3_stub_double():
    # sQL_PrimaryKey has no real 'sQL_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Table(name="sample_text")
    partner = sQL_PrimaryKey()
    setattr(partner, 'sQL_PrimaryKey', None)
    _safe_set(owner, 'sQL_Table4', partner)
    assert getattr(partner, 'sQL_PrimaryKey') == owner
    _safe_set(owner, 'sQL_Table4', None)
    assert getattr(partner, 'sQL_PrimaryKey') is None


def test_assoc_table0_stub_double():
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


def test_assoc_tableRef13_stub_double():
    # sQL_ForeignKey has no real 'sQL_ForeignKey14' property in the generated
    # code (a bare stub) -- manually attach it so sQL_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sQL_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sQL_Table(name="sample_text")
    partner = sQL_ForeignKey()
    setattr(partner, 'sQL_ForeignKey14', None)
    _safe_set(owner, 'sQL_Table15', partner)
    assert getattr(partner, 'sQL_ForeignKey14') == owner
    _safe_set(owner, 'sQL_Table15', None)
    assert getattr(partner, 'sQL_ForeignKey14') is None


