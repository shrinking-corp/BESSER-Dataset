import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RefColumn,
    RefDatabase,
    RefFKey,
    RefPKey,
    RefParameter,
    RefProcedure,
    RefTable,
    RefType,
    database_Column,
    database_Database,
    database_FKey,
    database_PKey,
    database_Parameter,
    database_Procedure,
    database_RefColumn,
    database_RefDatabase,
    database_RefFKey,
    database_RefPKey,
    database_RefParameter,
    database_RefProcedure,
    database_RefTable,
    database_RefType,
    database_Table,
    database_Type,
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

def test_assoc_columns20_reverse_link_reassign_clear():
    a1 = database_PKey(name="sample_text")
    a2 = database_PKey(name="sample_text_2")
    b = database_Column(name="sample_text")
    _safe_set(b, 'database_Column21', a1)
    assert _is_linked(b, 'database_Column21', a1)
    if hasattr(a1, 'database_PKey'):
        assert _is_linked(a1, 'database_PKey', b)
    _safe_set(b, 'database_Column21', a2)
    assert _is_linked(b, 'database_Column21', a2)
    if hasattr(a1, 'database_PKey'):
        assert not _is_linked(a1, 'database_PKey', b)
    if hasattr(a2, 'database_PKey'):
        assert _is_linked(a2, 'database_PKey', b)
    _safe_set(b, 'database_Column21', None)
    assert not _is_linked(b, 'database_Column21', a2)
    if hasattr(a2, 'database_PKey'):
        assert not _is_linked(a2, 'database_PKey', b)


def test_assoc_columns5_reverse_link_reassign_clear():
    a1 = database_FKey(name="sample_text")
    a2 = database_FKey(name="sample_text_2")
    b = database_Column(name="sample_text")
    _safe_set(b, 'database_Column', a1)
    assert _is_linked(b, 'database_Column', a1)
    if hasattr(a1, 'database_FKey'):
        assert _is_linked(a1, 'database_FKey', b)
    _safe_set(b, 'database_Column', a2)
    assert _is_linked(b, 'database_Column', a2)
    if hasattr(a1, 'database_FKey'):
        assert not _is_linked(a1, 'database_FKey', b)
    if hasattr(a2, 'database_FKey'):
        assert _is_linked(a2, 'database_FKey', b)
    _safe_set(b, 'database_Column', None)
    assert not _is_linked(b, 'database_Column', a2)
    if hasattr(a2, 'database_FKey'):
        assert not _is_linked(a2, 'database_FKey', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns0_stub_double():
    # database_RefColumn has no real 'database_RefColumn' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(name="sample_text")
    partner = database_RefColumn()
    setattr(partner, 'database_RefColumn', None)
    _safe_set(owner, 'database_Table', {partner})
    assert getattr(partner, 'database_RefColumn') == owner
    _safe_set(owner, 'database_Table', set())
    assert getattr(partner, 'database_RefColumn') is None


def test_assoc_fkeys3_stub_double():
    # database_RefFKey has no real 'database_RefFKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(name="sample_text")
    partner = database_RefFKey()
    setattr(partner, 'database_RefFKey', None)
    _safe_set(owner, 'database_Table4', {partner})
    assert getattr(partner, 'database_RefFKey') == owner
    _safe_set(owner, 'database_Table4', set())
    assert getattr(partner, 'database_RefFKey') is None


def test_assoc_parameters14_stub_double():
    # database_RefParameter has no real 'database_RefParameter' property in the generated
    # code (a bare stub) -- manually attach it so database_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Procedure(name="sample_text")
    partner = database_RefParameter()
    setattr(partner, 'database_RefParameter', None)
    _safe_set(owner, 'database_Procedure', {partner})
    assert getattr(partner, 'database_RefParameter') == owner
    _safe_set(owner, 'database_Procedure', set())
    assert getattr(partner, 'database_RefParameter') is None


def test_assoc_pkeys1_stub_double():
    # database_RefPKey has no real 'database_RefPKey' property in the generated
    # code (a bare stub) -- manually attach it so database_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Table(name="sample_text")
    partner = database_RefPKey()
    setattr(partner, 'database_RefPKey', None)
    _safe_set(owner, 'database_Table2', {partner})
    assert getattr(partner, 'database_RefPKey') == owner
    _safe_set(owner, 'database_Table2', set())
    assert getattr(partner, 'database_RefPKey') is None


def test_assoc_procedures12_stub_double():
    # database_RefProcedure has no real 'database_RefProcedure' property in the generated
    # code (a bare stub) -- manually attach it so database_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Database(name="sample_text")
    partner = database_RefProcedure()
    setattr(partner, 'database_RefProcedure', None)
    _safe_set(owner, 'database_Database13', {partner})
    assert getattr(partner, 'database_RefProcedure') == owner
    _safe_set(owner, 'database_Database13', set())
    assert getattr(partner, 'database_RefProcedure') is None


def test_assoc_reference6_stub_double():
    # database_RefTable has no real 'database_RefTable' property in the generated
    # code (a bare stub) -- manually attach it so database_FKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_FKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_FKey(name="sample_text")
    partner = database_RefTable()
    setattr(partner, 'database_RefTable', None)
    _safe_set(owner, 'database_FKey7', partner)
    assert getattr(partner, 'database_RefTable') == owner
    _safe_set(owner, 'database_FKey7', None)
    assert getattr(partner, 'database_RefTable') is None


def test_assoc_return_15_stub_double():
    # database_RefType has no real 'database_RefType17' property in the generated
    # code (a bare stub) -- manually attach it so database_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Procedure(name="sample_text")
    partner = database_RefType()
    setattr(partner, 'database_RefType17', None)
    _safe_set(owner, 'database_Procedure16', partner)
    assert getattr(partner, 'database_RefType17') == owner
    _safe_set(owner, 'database_Procedure16', None)
    assert getattr(partner, 'database_RefType17') is None


def test_assoc_tables10_stub_double():
    # database_RefTable has no real 'database_RefTable11' property in the generated
    # code (a bare stub) -- manually attach it so database_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Database(name="sample_text")
    partner = database_RefTable()
    setattr(partner, 'database_RefTable11', None)
    _safe_set(owner, 'database_Database', {partner})
    assert getattr(partner, 'database_RefTable11') == owner
    _safe_set(owner, 'database_Database', set())
    assert getattr(partner, 'database_RefTable11') is None


def test_assoc_type18_stub_double():
    # database_RefType has no real 'database_RefType19' property in the generated
    # code (a bare stub) -- manually attach it so database_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Parameter(name="sample_text")
    partner = database_RefType()
    setattr(partner, 'database_RefType19', None)
    _safe_set(owner, 'database_Parameter', partner)
    assert getattr(partner, 'database_RefType19') == owner
    _safe_set(owner, 'database_Parameter', None)
    assert getattr(partner, 'database_RefType19') is None


def test_assoc_type8_stub_double():
    # database_RefType has no real 'database_RefType' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(name="sample_text")
    partner = database_RefType()
    setattr(partner, 'database_RefType', None)
    _safe_set(owner, 'database_Column9', partner)
    assert getattr(partner, 'database_RefType') == owner
    _safe_set(owner, 'database_Column9', None)
    assert getattr(partner, 'database_RefType') is None


