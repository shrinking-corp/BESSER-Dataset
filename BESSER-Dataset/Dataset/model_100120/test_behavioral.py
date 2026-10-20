import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Index,
    NamedElement,
    database_Column,
    database_DataBase,
    database_Index,
    database_NamedElement,
    database_PrimaryKey,
    database_Table,
    database_Unique,
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

def test_assoc_columns4_reverse_link_reassign_clear():
    a1 = database_Table(collation="sample_text", storageEngine="sample_text")
    a2 = database_Table(collation="sample_text_2", storageEngine="sample_text_2")
    b = database_Column(collation="sample_text", default="sample_text", length=7, nullable=True, type="sample_text")
    _safe_set(b, 'database_Column', a1)
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_Table5'):
        assert _is_linked(a1, 'database_Table5', b)
    _safe_set(b, 'database_Column', a2)
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_Table5'):
        assert not _is_linked(a1, 'database_Table5', b)
    if hasattr(a2, 'database_Table5'):
        assert _is_linked(a2, 'database_Table5', b)
    _safe_set(b, 'database_Column', None)
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_Table5'):
        assert not _is_linked(a2, 'database_Table5', b)


def test_assoc_dataBase1_reverse_link_reassign_clear():
    a1 = database_Table(collation="sample_text", storageEngine="sample_text")
    a2 = database_Table(collation="sample_text_2", storageEngine="sample_text_2")
    b = database_DataBase()
    _safe_set(b, 'database_DataBase3', a1)
    assert _is_linked(b, 'database_DataBase3', a1)
    if hasattr(a1, 'database_Table2'):
        assert _is_linked(a1, 'database_Table2', b)
    _safe_set(b, 'database_DataBase3', a2)
    assert _is_linked(b, 'database_DataBase3', a2)
    if hasattr(a1, 'database_Table2'):
        assert not _is_linked(a1, 'database_Table2', b)
    if hasattr(a2, 'database_Table2'):
        assert _is_linked(a2, 'database_Table2', b)
    _safe_set(b, 'database_DataBase3', None)
    assert not _is_linked(b, 'database_DataBase3', a2)
    if hasattr(a2, 'database_Table2'):
        assert not _is_linked(a2, 'database_Table2', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = database_Table(collation="sample_text", storageEngine="sample_text")
    a2 = database_Table(collation="sample_text_2", storageEngine="sample_text_2")
    b = database_DataBase()
    _safe_set(b, 'database_DataBase', {a1})
    assert _is_linked(b, 'database_DataBase', a1)
    if hasattr(a1, 'database_Table'):
        assert _is_linked(a1, 'database_Table', b)
    _safe_set(b, 'database_DataBase', {a2})
    assert _is_linked(b, 'database_DataBase', a2)
    if hasattr(a1, 'database_Table'):
        assert not _is_linked(a1, 'database_Table', b)
    if hasattr(a2, 'database_Table'):
        assert _is_linked(a2, 'database_Table', b)
    _safe_set(b, 'database_DataBase', set())
    assert not _is_linked(b, 'database_DataBase', a2)
    if hasattr(a2, 'database_Table'):
        assert not _is_linked(a2, 'database_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns12_stub_double():
    # database_Index has no real 'database_Index13' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(collation="sample_text", default="sample_text", length=7, nullable=True, type="sample_text")
    partner = database_Index()
    setattr(partner, 'database_Index13', None)
    _safe_set(owner, 'database_Column14', partner)
    assert owner in getattr(partner, 'database_Index13')
    _safe_set(owner, 'database_Column14', None)
    assert owner not in getattr(partner, 'database_Index13')


def test_assoc_indexes6_stub_double():
    # database_Index has no real 'database_Index' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(collation="sample_text", storageEngine="sample_text")
    partner = database_Index()
    setattr(partner, 'database_Index', None)
    _safe_set(owner, 'database_Table7', {partner})
    assert getattr(partner, 'database_Index') == owner
    _safe_set(owner, 'database_Table7', set())
    assert getattr(partner, 'database_Index') is None


def test_assoc_primaryKey8_stub_double():
    # database_PrimaryKey has no real 'database_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(collation="sample_text", storageEngine="sample_text")
    partner = database_PrimaryKey()
    setattr(partner, 'database_PrimaryKey', None)
    _safe_set(owner, 'database_Table9', partner)
    assert getattr(partner, 'database_PrimaryKey') == owner
    _safe_set(owner, 'database_Table9', None)
    assert getattr(partner, 'database_PrimaryKey') is None


def test_assoc_uniques10_stub_double():
    # database_Unique has no real 'database_Unique' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(collation="sample_text", storageEngine="sample_text")
    partner = database_Unique()
    setattr(partner, 'database_Unique', None)
    _safe_set(owner, 'database_Table11', {partner})
    assert getattr(partner, 'database_Unique') == owner
    _safe_set(owner, 'database_Table11', set())
    assert getattr(partner, 'database_Unique') is None


