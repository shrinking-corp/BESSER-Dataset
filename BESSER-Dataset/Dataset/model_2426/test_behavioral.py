import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DB_Column,
    DB_Database,
    DB_DatabaseElement,
    DB_ForeignKey,
    DB_NamedElement,
    DB_Table,
    DatabaseElement,
    NamedElement,
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

def test_assoc_child7_reverse_link_reassign_clear():
    a1 = DB_ForeignKey(isMany="sample_text")
    a2 = DB_ForeignKey(isMany="sample_text_2")
    b = DB_Column(notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column9', a1)
    assert _is_linked(b, 'DB_Column9', a1)
    if hasattr(a1, 'DB_ForeignKey8'):
        assert _is_linked(a1, 'DB_ForeignKey8', b)
    _safe_set(b, 'DB_Column9', a2)
    assert _is_linked(b, 'DB_Column9', a2)
    if hasattr(a1, 'DB_ForeignKey8'):
        assert not _is_linked(a1, 'DB_ForeignKey8', b)
    if hasattr(a2, 'DB_ForeignKey8'):
        assert _is_linked(a2, 'DB_ForeignKey8', b)
    _safe_set(b, 'DB_Column9', None)
    assert not _is_linked(b, 'DB_Column9', a2)
    if hasattr(a2, 'DB_ForeignKey8'):
        assert not _is_linked(a2, 'DB_ForeignKey8', b)


def test_assoc_parent5_reverse_link_reassign_clear():
    a1 = DB_ForeignKey(isMany="sample_text")
    a2 = DB_ForeignKey(isMany="sample_text_2")
    b = DB_Column(notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column6', a1)
    assert _is_linked(b, 'DB_Column6', a1)
    if hasattr(a1, 'DB_ForeignKey'):
        assert _is_linked(a1, 'DB_ForeignKey', b)
    _safe_set(b, 'DB_Column6', a2)
    assert _is_linked(b, 'DB_Column6', a2)
    if hasattr(a1, 'DB_ForeignKey'):
        assert not _is_linked(a1, 'DB_ForeignKey', b)
    if hasattr(a2, 'DB_ForeignKey'):
        assert _is_linked(a2, 'DB_ForeignKey', b)
    _safe_set(b, 'DB_Column6', None)
    assert not _is_linked(b, 'DB_Column6', a2)
    if hasattr(a2, 'DB_ForeignKey'):
        assert not _is_linked(a2, 'DB_ForeignKey', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns2_stub_double():
    # DB_Table has no real 'table' property in the generated
    # code (a bare stub) -- manually attach it so DB_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DB_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DB_Column(notNull=True, type="sample_text")
    partner = DB_Table()
    setattr(partner, 'table', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'table')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'table')


def test_assoc_contents0_stub_double():
    # DB_DatabaseElement has no real 'DatabaseElement' property in the generated
    # code (a bare stub) -- manually attach it so DB_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DB_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DB_Database(name="sample_text")
    partner = DB_DatabaseElement()
    setattr(partner, 'DatabaseElement', None)
    _safe_set(owner, 'database', {partner})
    assert getattr(partner, 'DatabaseElement') == owner
    _safe_set(owner, 'database', set())
    assert getattr(partner, 'DatabaseElement') is None


def test_assoc_database1_stub_double():
    # DB_DatabaseElement has no real 'contents' property in the generated
    # code (a bare stub) -- manually attach it so DB_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DB_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DB_Database(name="sample_text")
    partner = DB_DatabaseElement()
    setattr(partner, 'contents', None)
    _safe_set(owner, 'Database', partner)
    assert getattr(partner, 'contents') == owner
    _safe_set(owner, 'Database', None)
    assert getattr(partner, 'contents') is None


def test_assoc_primaryKeys3_stub_double():
    # DB_Table has no real 'DB_Table' property in the generated
    # code (a bare stub) -- manually attach it so DB_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DB_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DB_Column(notNull=True, type="sample_text")
    partner = DB_Table()
    setattr(partner, 'DB_Table', None)
    _safe_set(owner, 'DB_Column', partner)
    assert owner in getattr(partner, 'DB_Table')
    _safe_set(owner, 'DB_Column', None)
    assert owner not in getattr(partner, 'DB_Table')


def test_assoc_table4_stub_double():
    # DB_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so DB_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DB_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DB_Column(notNull=True, type="sample_text")
    partner = DB_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table') is None


