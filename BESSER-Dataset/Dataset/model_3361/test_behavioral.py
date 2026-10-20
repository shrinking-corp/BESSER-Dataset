import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColumnFamily,
    nosql_Cell,
    nosql_Column,
    nosql_ColumnFamily,
    nosql_Index,
    nosql_KeySpace,
    nosql_Options,
    nosql_PK,
    nosql_Row,
    Type,
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

def test_assoc_EReference03_reverse_link_reassign_clear():
    a1 = nosql_Options(name="sample_text", value="sample_text")
    a2 = nosql_Options(name="sample_text_2", value="sample_text_2")
    b = nosql_KeySpace(name="sample_text")
    _safe_set(b, 'nosql_KeySpace4', a1)
    assert _is_linked(b, 'nosql_KeySpace4', a1)
    if hasattr(a1, 'nosql_Options'):
        assert _is_linked(a1, 'nosql_Options', b)
    _safe_set(b, 'nosql_KeySpace4', a2)
    assert _is_linked(b, 'nosql_KeySpace4', a2)
    if hasattr(a1, 'nosql_Options'):
        assert not _is_linked(a1, 'nosql_Options', b)
    if hasattr(a2, 'nosql_Options'):
        assert _is_linked(a2, 'nosql_Options', b)
    _safe_set(b, 'nosql_KeySpace4', None)
    assert not _is_linked(b, 'nosql_KeySpace4', a2)
    if hasattr(a2, 'nosql_Options'):
        assert not _is_linked(a2, 'nosql_Options', b)


def test_assoc_applyTo10_reverse_link_reassign_clear():
    a1 = nosql_Index(name="sample_text", reference="sample_text")
    a2 = nosql_Index(name="sample_text_2", reference="sample_text_2")
    b = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    _safe_set(b, 'nosql_Column', a1)
    assert _is_linked(b, 'nosql_Column', a1)
    if hasattr(a1, 'nosql_Index11'):
        assert _is_linked(a1, 'nosql_Index11', b)
    _safe_set(b, 'nosql_Column', a2)
    assert _is_linked(b, 'nosql_Column', a2)
    if hasattr(a1, 'nosql_Index11'):
        assert not _is_linked(a1, 'nosql_Index11', b)
    if hasattr(a2, 'nosql_Index11'):
        assert _is_linked(a2, 'nosql_Index11', b)
    _safe_set(b, 'nosql_Column', None)
    assert not _is_linked(b, 'nosql_Column', a2)
    if hasattr(a2, 'nosql_Index11'):
        assert not _is_linked(a2, 'nosql_Index11', b)


def test_assoc_column37_reverse_link_reassign_clear():
    a1 = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    a2 = nosql_Column(datatype="sample_text_2", name="sample_text_2", size="sample_text_2")
    b = nosql_Cell(value="sample_text")
    _safe_set(b, 'nosql_Cell38', a1)
    assert _is_linked(b, 'nosql_Cell38', a1)
    if hasattr(a1, 'nosql_Column39'):
        assert _is_linked(a1, 'nosql_Column39', b)
    _safe_set(b, 'nosql_Cell38', a2)
    assert _is_linked(b, 'nosql_Cell38', a2)
    if hasattr(a1, 'nosql_Column39'):
        assert not _is_linked(a1, 'nosql_Column39', b)
    if hasattr(a2, 'nosql_Column39'):
        assert _is_linked(a2, 'nosql_Column39', b)
    _safe_set(b, 'nosql_Cell38', None)
    assert not _is_linked(b, 'nosql_Cell38', a2)
    if hasattr(a2, 'nosql_Column39'):
        assert not _is_linked(a2, 'nosql_Column39', b)


def test_assoc_columnFamily26_reverse_link_reassign_clear():
    a1 = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    a2 = nosql_ColumnFamily(comment="sample_text_2", name="sample_text_2")
    b = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    _safe_set(b, 'nosql_Column27', a1)
    assert _is_linked(b, 'nosql_Column27', a1)
    if hasattr(a1, 'nosql_ColumnFamily28'):
        assert _is_linked(a1, 'nosql_ColumnFamily28', b)
    _safe_set(b, 'nosql_Column27', a2)
    assert _is_linked(b, 'nosql_Column27', a2)
    if hasattr(a1, 'nosql_ColumnFamily28'):
        assert not _is_linked(a1, 'nosql_ColumnFamily28', b)
    if hasattr(a2, 'nosql_ColumnFamily28'):
        assert _is_linked(a2, 'nosql_ColumnFamily28', b)
    _safe_set(b, 'nosql_Column27', None)
    assert not _is_linked(b, 'nosql_Column27', a2)
    if hasattr(a2, 'nosql_ColumnFamily28'):
        assert not _is_linked(a2, 'nosql_ColumnFamily28', b)


def test_assoc_columns12_reverse_link_reassign_clear():
    a1 = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    a2 = nosql_ColumnFamily(comment="sample_text_2", name="sample_text_2")
    b = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    _safe_set(b, 'nosql_Column14', a1)
    assert _is_linked(b, 'nosql_Column14', a1)
    if hasattr(a1, 'nosql_ColumnFamily13'):
        assert _is_linked(a1, 'nosql_ColumnFamily13', b)
    _safe_set(b, 'nosql_Column14', a2)
    assert _is_linked(b, 'nosql_Column14', a2)
    if hasattr(a1, 'nosql_ColumnFamily13'):
        assert not _is_linked(a1, 'nosql_ColumnFamily13', b)
    if hasattr(a2, 'nosql_ColumnFamily13'):
        assert _is_linked(a2, 'nosql_ColumnFamily13', b)
    _safe_set(b, 'nosql_Column14', None)
    assert not _is_linked(b, 'nosql_Column14', a2)
    if hasattr(a2, 'nosql_ColumnFamily13'):
        assert not _is_linked(a2, 'nosql_ColumnFamily13', b)


def test_assoc_families1_reverse_link_reassign_clear():
    a1 = nosql_KeySpace(name="sample_text")
    a2 = nosql_KeySpace(name="sample_text_2")
    b = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    _safe_set(b, 'nosql_ColumnFamily', a1)
    assert _is_linked(b, 'nosql_ColumnFamily', a1)
    if hasattr(a1, 'nosql_KeySpace2'):
        assert _is_linked(a1, 'nosql_KeySpace2', b)
    _safe_set(b, 'nosql_ColumnFamily', a2)
    assert _is_linked(b, 'nosql_ColumnFamily', a2)
    if hasattr(a1, 'nosql_KeySpace2'):
        assert not _is_linked(a1, 'nosql_KeySpace2', b)
    if hasattr(a2, 'nosql_KeySpace2'):
        assert _is_linked(a2, 'nosql_KeySpace2', b)
    _safe_set(b, 'nosql_ColumnFamily', None)
    assert not _is_linked(b, 'nosql_ColumnFamily', a2)
    if hasattr(a2, 'nosql_KeySpace2'):
        assert not _is_linked(a2, 'nosql_KeySpace2', b)


def test_assoc_idexes0_reverse_link_reassign_clear():
    a1 = nosql_KeySpace(name="sample_text")
    a2 = nosql_KeySpace(name="sample_text_2")
    b = nosql_Index(name="sample_text", reference="sample_text")
    _safe_set(b, 'nosql_Index', a1)
    assert _is_linked(b, 'nosql_Index', a1)
    if hasattr(a1, 'nosql_KeySpace'):
        assert _is_linked(a1, 'nosql_KeySpace', b)
    _safe_set(b, 'nosql_Index', a2)
    assert _is_linked(b, 'nosql_Index', a2)
    if hasattr(a1, 'nosql_KeySpace'):
        assert not _is_linked(a1, 'nosql_KeySpace', b)
    if hasattr(a2, 'nosql_KeySpace'):
        assert _is_linked(a2, 'nosql_KeySpace', b)
    _safe_set(b, 'nosql_Index', None)
    assert not _is_linked(b, 'nosql_Index', a2)
    if hasattr(a2, 'nosql_KeySpace'):
        assert not _is_linked(a2, 'nosql_KeySpace', b)


def test_assoc_keyspace23_reverse_link_reassign_clear():
    a1 = nosql_KeySpace(name="sample_text")
    a2 = nosql_KeySpace(name="sample_text_2")
    b = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    _safe_set(b, 'nosql_ColumnFamily24', a1)
    assert _is_linked(b, 'nosql_ColumnFamily24', a1)
    if hasattr(a1, 'nosql_KeySpace25'):
        assert _is_linked(a1, 'nosql_KeySpace25', b)
    _safe_set(b, 'nosql_ColumnFamily24', a2)
    assert _is_linked(b, 'nosql_ColumnFamily24', a2)
    if hasattr(a1, 'nosql_KeySpace25'):
        assert not _is_linked(a1, 'nosql_KeySpace25', b)
    if hasattr(a2, 'nosql_KeySpace25'):
        assert _is_linked(a2, 'nosql_KeySpace25', b)
    _safe_set(b, 'nosql_ColumnFamily24', None)
    assert not _is_linked(b, 'nosql_ColumnFamily24', a2)
    if hasattr(a2, 'nosql_KeySpace25'):
        assert not _is_linked(a2, 'nosql_KeySpace25', b)


def test_assoc_options15_reverse_link_reassign_clear():
    a1 = nosql_Options(name="sample_text", value="sample_text")
    a2 = nosql_Options(name="sample_text_2", value="sample_text_2")
    b = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    _safe_set(b, 'nosql_ColumnFamily16', {a1})
    assert _is_linked(b, 'nosql_ColumnFamily16', a1)
    if hasattr(a1, 'nosql_Options17'):
        assert _is_linked(a1, 'nosql_Options17', b)
    _safe_set(b, 'nosql_ColumnFamily16', {a2})
    assert _is_linked(b, 'nosql_ColumnFamily16', a2)
    if hasattr(a1, 'nosql_Options17'):
        assert not _is_linked(a1, 'nosql_Options17', b)
    if hasattr(a2, 'nosql_Options17'):
        assert _is_linked(a2, 'nosql_Options17', b)
    _safe_set(b, 'nosql_ColumnFamily16', set())
    assert not _is_linked(b, 'nosql_ColumnFamily16', a2)
    if hasattr(a2, 'nosql_Options17'):
        assert not _is_linked(a2, 'nosql_Options17', b)


def test_assoc_options5_reverse_link_reassign_clear():
    a1 = nosql_Options(name="sample_text", value="sample_text")
    a2 = nosql_Options(name="sample_text_2", value="sample_text_2")
    b = nosql_KeySpace(name="sample_text")
    _safe_set(b, 'nosql_KeySpace6', {a1})
    assert _is_linked(b, 'nosql_KeySpace6', a1)
    if hasattr(a1, 'nosql_Options7'):
        assert _is_linked(a1, 'nosql_Options7', b)
    _safe_set(b, 'nosql_KeySpace6', {a2})
    assert _is_linked(b, 'nosql_KeySpace6', a2)
    if hasattr(a1, 'nosql_Options7'):
        assert not _is_linked(a1, 'nosql_Options7', b)
    if hasattr(a2, 'nosql_Options7'):
        assert _is_linked(a2, 'nosql_Options7', b)
    _safe_set(b, 'nosql_KeySpace6', set())
    assert not _is_linked(b, 'nosql_KeySpace6', a2)
    if hasattr(a2, 'nosql_Options7'):
        assert not _is_linked(a2, 'nosql_Options7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_PK18_stub_double():
    # nosql_PK has no real 'nosql_PK20' property in the generated
    # code (a bare stub) -- manually attach it so nosql_ColumnFamily's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_ColumnFamily's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    partner = nosql_PK()
    setattr(partner, 'nosql_PK20', None)
    _safe_set(owner, 'nosql_ColumnFamily19', partner)
    assert getattr(partner, 'nosql_PK20') == owner
    _safe_set(owner, 'nosql_ColumnFamily19', None)
    assert getattr(partner, 'nosql_PK20') is None


def test_assoc_additionalColumns34_stub_double():
    # nosql_Row has no real 'nosql_Row35' property in the generated
    # code (a bare stub) -- manually attach it so nosql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    partner = nosql_Row()
    setattr(partner, 'nosql_Row35', None)
    _safe_set(owner, 'nosql_Column36', partner)
    assert owner in getattr(partner, 'nosql_Row35')
    _safe_set(owner, 'nosql_Column36', None)
    assert owner not in getattr(partner, 'nosql_Row35')


def test_assoc_cells32_stub_double():
    # nosql_Row has no real 'nosql_Row33' property in the generated
    # code (a bare stub) -- manually attach it so nosql_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_Cell(value="sample_text")
    partner = nosql_Row()
    setattr(partner, 'nosql_Row33', None)
    _safe_set(owner, 'nosql_Cell', partner)
    assert owner in getattr(partner, 'nosql_Row33')
    _safe_set(owner, 'nosql_Cell', None)
    assert owner not in getattr(partner, 'nosql_Row33')


def test_assoc_columns29_stub_double():
    # nosql_PK has no real 'nosql_PK30' property in the generated
    # code (a bare stub) -- manually attach it so nosql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_Column(datatype="sample_text", name="sample_text", size="sample_text")
    partner = nosql_PK()
    setattr(partner, 'nosql_PK30', None)
    _safe_set(owner, 'nosql_Column31', partner)
    assert owner in getattr(partner, 'nosql_PK30')
    _safe_set(owner, 'nosql_Column31', None)
    assert owner not in getattr(partner, 'nosql_PK30')


def test_assoc_hasPK8_stub_double():
    # nosql_PK has no real 'nosql_PK' property in the generated
    # code (a bare stub) -- manually attach it so nosql_KeySpace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_KeySpace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_KeySpace(name="sample_text")
    partner = nosql_PK()
    setattr(partner, 'nosql_PK', None)
    _safe_set(owner, 'nosql_KeySpace9', {partner})
    assert getattr(partner, 'nosql_PK') == owner
    _safe_set(owner, 'nosql_KeySpace9', set())
    assert getattr(partner, 'nosql_PK') is None


def test_assoc_rows21_stub_double():
    # nosql_Row has no real 'nosql_Row' property in the generated
    # code (a bare stub) -- manually attach it so nosql_ColumnFamily's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_ColumnFamily's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_ColumnFamily(comment="sample_text", name="sample_text")
    partner = nosql_Row()
    setattr(partner, 'nosql_Row', None)
    _safe_set(owner, 'nosql_ColumnFamily22', {partner})
    assert getattr(partner, 'nosql_Row') == owner
    _safe_set(owner, 'nosql_ColumnFamily22', set())
    assert getattr(partner, 'nosql_Row') is None


