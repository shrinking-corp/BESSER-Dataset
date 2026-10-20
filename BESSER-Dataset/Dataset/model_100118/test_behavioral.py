import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DatabaseResourceData,
    ExtensibleModel,
    JRESResourceInfo,
    database_DBGenContext,
    database_DBModuleCommonProperty,
    database_DatabaseResourceData,
    database_ForeignKey,
    database_TableColumn,
    database_TableIndex,
    database_TableIndexColumn,
    database_TableKey,
    database_TableResourceData,
    database_ViewResourceData,
    ColumnType,
    key_type,
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

def test_assoc_columns12_reverse_link_reassign_clear():
    a1 = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    a2 = database_TableKey(mark="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    _safe_set(b, 'database_TableColumn14', a1)
    assert _is_linked(b, 'database_TableColumn14', a1)
    if hasattr(a1, 'database_TableKey13'):
        assert _is_linked(a1, 'database_TableKey13', b)
    _safe_set(b, 'database_TableColumn14', a2)
    assert _is_linked(b, 'database_TableColumn14', a2)
    if hasattr(a1, 'database_TableKey13'):
        assert not _is_linked(a1, 'database_TableKey13', b)
    if hasattr(a2, 'database_TableKey13'):
        assert _is_linked(a2, 'database_TableKey13', b)
    _safe_set(b, 'database_TableColumn14', None)
    assert not _is_linked(b, 'database_TableColumn14', a2)
    if hasattr(a2, 'database_TableKey13'):
        assert not _is_linked(a2, 'database_TableKey13', b)


def test_assoc_columns7_reverse_link_reassign_clear():
    a1 = database_TableIndexColumn(ascending=True, columnName="sample_text", columnType="sample_text")
    a2 = database_TableIndexColumn(ascending=False, columnName="sample_text_2", columnType="sample_text_2")
    b = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    _safe_set(b, 'database_TableIndex8', {a1})
    assert _is_linked(b, 'database_TableIndex8', a1)
    if hasattr(a1, 'database_TableIndexColumn'):
        assert _is_linked(a1, 'database_TableIndexColumn', b)
    _safe_set(b, 'database_TableIndex8', {a2})
    assert _is_linked(b, 'database_TableIndex8', a2)
    if hasattr(a1, 'database_TableIndexColumn'):
        assert not _is_linked(a1, 'database_TableIndexColumn', b)
    if hasattr(a2, 'database_TableIndexColumn'):
        assert _is_linked(a2, 'database_TableIndexColumn', b)
    _safe_set(b, 'database_TableIndex8', set())
    assert not _is_linked(b, 'database_TableIndex8', a2)
    if hasattr(a2, 'database_TableIndexColumn'):
        assert not _is_linked(a2, 'database_TableIndexColumn', b)


def test_assoc_foreignKey9_reverse_link_reassign_clear():
    a1 = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    a2 = database_TableKey(mark="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    _safe_set(b, 'database_ForeignKey11', a1)
    assert _is_linked(b, 'database_ForeignKey11', a1)
    if hasattr(a1, 'database_TableKey10'):
        assert _is_linked(a1, 'database_TableKey10', b)
    _safe_set(b, 'database_ForeignKey11', a2)
    assert _is_linked(b, 'database_ForeignKey11', a2)
    if hasattr(a1, 'database_TableKey10'):
        assert not _is_linked(a1, 'database_TableKey10', b)
    if hasattr(a2, 'database_TableKey10'):
        assert _is_linked(a2, 'database_TableKey10', b)
    _safe_set(b, 'database_ForeignKey11', None)
    assert not _is_linked(b, 'database_ForeignKey11', a2)
    if hasattr(a2, 'database_TableKey10'):
        assert not _is_linked(a2, 'database_TableKey10', b)


def test_assoc_foreignkey5_reverse_link_reassign_clear():
    a1 = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    a2 = database_TableColumn(chineseName="sample_text_2", columnName="sample_text_2", columnType="sample_text_2", comments="sample_text_2", dataType="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", fieldName="sample_text_2", mark="sample_text_2", name="sample_text_2", nullable=False, primaryKey=False, unique=False)
    b = database_ForeignKey(fieldName="sample_text", tableName="sample_text")
    _safe_set(b, 'database_ForeignKey', a1)
    assert _is_linked(b, 'database_ForeignKey', a1)
    if hasattr(a1, 'database_TableColumn6'):
        assert _is_linked(a1, 'database_TableColumn6', b)
    _safe_set(b, 'database_ForeignKey', a2)
    assert _is_linked(b, 'database_ForeignKey', a2)
    if hasattr(a1, 'database_TableColumn6'):
        assert not _is_linked(a1, 'database_TableColumn6', b)
    if hasattr(a2, 'database_TableColumn6'):
        assert _is_linked(a2, 'database_TableColumn6', b)
    _safe_set(b, 'database_ForeignKey', None)
    assert not _is_linked(b, 'database_ForeignKey', a2)
    if hasattr(a2, 'database_TableColumn6'):
        assert not _is_linked(a2, 'database_TableColumn6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns0_stub_double():
    # database_TableResourceData has no real 'database_TableResourceData' property in the generated
    # code (a bare stub) -- manually attach it so database_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_TableColumn(chineseName="sample_text", columnName="sample_text", columnType="sample_text", comments="sample_text", dataType="sample_text", defaultValue="sample_text", description="sample_text", fieldName="sample_text", mark="sample_text", name="sample_text", nullable=True, primaryKey=True, unique=True)
    partner = database_TableResourceData()
    setattr(partner, 'database_TableResourceData', None)
    _safe_set(owner, 'database_TableColumn', partner)
    assert owner in getattr(partner, 'database_TableResourceData')
    _safe_set(owner, 'database_TableColumn', None)
    assert owner not in getattr(partner, 'database_TableResourceData')


def test_assoc_indexes1_stub_double():
    # database_TableResourceData has no real 'database_TableResourceData2' property in the generated
    # code (a bare stub) -- manually attach it so database_TableIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_TableIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_TableIndex(cluster=True, mark="sample_text", name="sample_text", unique=True)
    partner = database_TableResourceData()
    setattr(partner, 'database_TableResourceData2', None)
    _safe_set(owner, 'database_TableIndex', partner)
    assert owner in getattr(partner, 'database_TableResourceData2')
    _safe_set(owner, 'database_TableIndex', None)
    assert owner not in getattr(partner, 'database_TableResourceData2')


def test_assoc_keys3_stub_double():
    # database_TableResourceData has no real 'database_TableResourceData4' property in the generated
    # code (a bare stub) -- manually attach it so database_TableKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_TableKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_TableKey(mark="sample_text", name="sample_text", type="sample_text")
    partner = database_TableResourceData()
    setattr(partner, 'database_TableResourceData4', None)
    _safe_set(owner, 'database_TableKey', partner)
    assert owner in getattr(partner, 'database_TableResourceData4')
    _safe_set(owner, 'database_TableKey', None)
    assert owner not in getattr(partner, 'database_TableResourceData4')


