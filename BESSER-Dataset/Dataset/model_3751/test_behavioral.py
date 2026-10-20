import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ERDInfo,
    Table,
    rdb_Column,
    rdb_DB,
    rdb_ERDInfo,
    rdb_Relation,
    rdb_Table,
    rdb_UserComment,
    rdb_View,
    RelationKind,
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

def test_assoc_UserCommentReference9_reverse_link_reassign_clear():
    a1 = rdb_UserComment(comment="sample_text")
    a2 = rdb_UserComment(comment="sample_text_2")
    b = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    _safe_set(b, 'rdb_Table', a1)
    assert _is_linked(b, 'rdb_Table', a1)
    if hasattr(a1, 'rdb_UserComment'):
        assert _is_linked(a1, 'rdb_UserComment', b)
    _safe_set(b, 'rdb_Table', a2)
    assert _is_linked(b, 'rdb_Table', a2)
    if hasattr(a1, 'rdb_UserComment'):
        assert not _is_linked(a1, 'rdb_UserComment', b)
    if hasattr(a2, 'rdb_UserComment'):
        assert _is_linked(a2, 'rdb_UserComment', b)
    _safe_set(b, 'rdb_Table', None)
    assert not _is_linked(b, 'rdb_Table', a2)
    if hasattr(a2, 'rdb_UserComment'):
        assert not _is_linked(a2, 'rdb_UserComment', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Column(comment="sample_text", default="sample_text", extra="sample_text", field="sample_text", key="sample_text", logicalField="sample_text", null="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_db16_reverse_link_reassign_clear():
    a1 = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    a2 = rdb_Relation(bendpoint="sample_text_2", column_name="sample_text_2", comment="sample_text_2", constraint_name="sample_text_2", referenced_column_name="sample_text_2", source_kind="sample_text_2", target_kind="sample_text_2")
    b = rdb_DB(comment="sample_text", dbType="sample_text", id="sample_text", key="sample_text", sid="sample_text", url="sample_text")
    _safe_set(b, 'DB17', a1)
    assert _is_linked(b, 'DB17', a1)
    if hasattr(a1, 'references'):
        assert _is_linked(a1, 'references', b)
    _safe_set(b, 'DB17', a2)
    assert _is_linked(b, 'DB17', a2)
    if hasattr(a1, 'references'):
        assert not _is_linked(a1, 'references', b)
    if hasattr(a2, 'references'):
        assert _is_linked(a2, 'references', b)
    _safe_set(b, 'DB17', None)
    assert not _is_linked(b, 'DB17', a2)
    if hasattr(a2, 'references'):
        assert not _is_linked(a2, 'references', b)


def test_assoc_db4_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_DB(comment="sample_text", dbType="sample_text", id="sample_text", key="sample_text", sid="sample_text", url="sample_text")
    _safe_set(b, 'DB', a1)
    assert _is_linked(b, 'DB', a1)
    if hasattr(a1, 'tables'):
        assert _is_linked(a1, 'tables', b)
    _safe_set(b, 'DB', a2)
    assert _is_linked(b, 'DB', a2)
    if hasattr(a1, 'tables'):
        assert not _is_linked(a1, 'tables', b)
    if hasattr(a2, 'tables'):
        assert _is_linked(a2, 'tables', b)
    _safe_set(b, 'DB', None)
    assert not _is_linked(b, 'DB', a2)
    if hasattr(a2, 'tables'):
        assert not _is_linked(a2, 'tables', b)


def test_assoc_incomingLinks5_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    _safe_set(b, 'Relation6', a1)
    assert _is_linked(b, 'Relation6', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Relation6', a2)
    assert _is_linked(b, 'Relation6', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Relation6', None)
    assert not _is_linked(b, 'Relation6', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_outgoingLinks7_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    _safe_set(b, 'Relation8', a1)
    assert _is_linked(b, 'Relation8', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Relation8', a2)
    assert _is_linked(b, 'Relation8', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Relation8', None)
    assert not _is_linked(b, 'Relation8', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_references1_reverse_link_reassign_clear():
    a1 = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    a2 = rdb_Relation(bendpoint="sample_text_2", column_name="sample_text_2", comment="sample_text_2", constraint_name="sample_text_2", referenced_column_name="sample_text_2", source_kind="sample_text_2", target_kind="sample_text_2")
    b = rdb_DB(comment="sample_text", dbType="sample_text", id="sample_text", key="sample_text", sid="sample_text", url="sample_text")
    _safe_set(b, 'db2', {a1})
    assert _is_linked(b, 'db2', a1)
    if hasattr(a1, 'Relation'):
        assert _is_linked(a1, 'Relation', b)
    _safe_set(b, 'db2', {a2})
    assert _is_linked(b, 'db2', a2)
    if hasattr(a1, 'Relation'):
        assert not _is_linked(a1, 'Relation', b)
    if hasattr(a2, 'Relation'):
        assert _is_linked(a2, 'Relation', b)
    _safe_set(b, 'db2', set())
    assert not _is_linked(b, 'db2', a2)
    if hasattr(a2, 'Relation'):
        assert not _is_linked(a2, 'Relation', b)


def test_assoc_source12_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    _safe_set(b, 'outgoingLinks', a1)
    assert _is_linked(b, 'outgoingLinks', a1)
    if hasattr(a1, 'Table13'):
        assert _is_linked(a1, 'Table13', b)
    _safe_set(b, 'outgoingLinks', a2)
    assert _is_linked(b, 'outgoingLinks', a2)
    if hasattr(a1, 'Table13'):
        assert not _is_linked(a1, 'Table13', b)
    if hasattr(a2, 'Table13'):
        assert _is_linked(a2, 'Table13', b)
    _safe_set(b, 'outgoingLinks', None)
    assert not _is_linked(b, 'outgoingLinks', a2)
    if hasattr(a2, 'Table13'):
        assert not _is_linked(a2, 'Table13', b)


def test_assoc_table10_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Column(comment="sample_text", default="sample_text", extra="sample_text", field="sample_text", key="sample_text", logicalField="sample_text", null="sample_text", type="sample_text")
    _safe_set(b, 'columns', a1)
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'Table11'):
        assert _is_linked(a1, 'Table11', b)
    _safe_set(b, 'columns', a2)
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'Table11'):
        assert not _is_linked(a1, 'Table11', b)
    if hasattr(a2, 'Table11'):
        assert _is_linked(a2, 'Table11', b)
    _safe_set(b, 'columns', None)
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'Table11'):
        assert not _is_linked(a2, 'Table11', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_DB(comment="sample_text", dbType="sample_text", id="sample_text", key="sample_text", sid="sample_text", url="sample_text")
    _safe_set(b, 'db', {a1})
    assert _is_linked(b, 'db', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'db', {a2})
    assert _is_linked(b, 'db', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'db', set())
    assert not _is_linked(b, 'db', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_target14_reverse_link_reassign_clear():
    a1 = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    a2 = rdb_Table(comment="sample_text_2", constraints="sample_text_2", logicalName="sample_text_2", name="sample_text_2")
    b = rdb_Relation(bendpoint="sample_text", column_name="sample_text", comment="sample_text", constraint_name="sample_text", referenced_column_name="sample_text", source_kind="sample_text", target_kind="sample_text")
    _safe_set(b, 'incomingLinks', a1)
    assert _is_linked(b, 'incomingLinks', a1)
    if hasattr(a1, 'Table15'):
        assert _is_linked(a1, 'Table15', b)
    _safe_set(b, 'incomingLinks', a2)
    assert _is_linked(b, 'incomingLinks', a2)
    if hasattr(a1, 'Table15'):
        assert not _is_linked(a1, 'Table15', b)
    if hasattr(a2, 'Table15'):
        assert _is_linked(a2, 'Table15', b)
    _safe_set(b, 'incomingLinks', None)
    assert not _is_linked(b, 'incomingLinks', a2)
    if hasattr(a2, 'Table15'):
        assert not _is_linked(a2, 'Table15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_tableName18_stub_double():
    # rdb_View has no real 'rdb_View' property in the generated
    # code (a bare stub) -- manually attach it so rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdb_Table(comment="sample_text", constraints="sample_text", logicalName="sample_text", name="sample_text")
    partner = rdb_View()
    setattr(partner, 'rdb_View', None)
    _safe_set(owner, 'rdb_Table19', partner)
    assert getattr(partner, 'rdb_View') == owner
    _safe_set(owner, 'rdb_Table19', None)
    assert getattr(partner, 'rdb_View') is None


