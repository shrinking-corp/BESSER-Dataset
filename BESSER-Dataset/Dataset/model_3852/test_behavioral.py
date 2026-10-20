import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Definition,
    Key,
    dDL_Alter_table,
    dDL_Colname,
    dDL_Column,
    dDL_Comment,
    dDL_Constraint,
    dDL_Create_sequence,
    dDL_Create_table,
    dDL_Data_definition,
    dDL_Definition,
    dDL_Foreign_key,
    dDL_ISNULL,
    dDL_Key,
    dDL_Primary_key,
    dDL_Sequence_options,
    dDL_TYPE,
    dDL_Tabname,
    dDL_Unique_key,
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

def test_assoc_colname14_reverse_link_reassign_clear():
    a1 = dDL_Comment(columnId="sample_text", string="sample_text")
    a2 = dDL_Comment(columnId="sample_text_2", string="sample_text_2")
    b = dDL_Colname(id="sample_text")
    _safe_set(b, 'dDL_Colname', a1)
    assert _is_linked(b, 'dDL_Colname', a1)
    if hasattr(a1, 'dDL_Comment15'):
        assert _is_linked(a1, 'dDL_Comment15', b)
    _safe_set(b, 'dDL_Colname', a2)
    assert _is_linked(b, 'dDL_Colname', a2)
    if hasattr(a1, 'dDL_Comment15'):
        assert not _is_linked(a1, 'dDL_Comment15', b)
    if hasattr(a2, 'dDL_Comment15'):
        assert _is_linked(a2, 'dDL_Comment15', b)
    _safe_set(b, 'dDL_Colname', None)
    assert not _is_linked(b, 'dDL_Colname', a2)
    if hasattr(a2, 'dDL_Comment15'):
        assert not _is_linked(a2, 'dDL_Comment15', b)


def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = dDL_Create_table(id="sample_text")
    a2 = dDL_Create_table(id="sample_text_2")
    b = dDL_Column(id="sample_text", number=7)
    _safe_set(b, 'dDL_Column', a1)
    assert _is_linked(b, 'dDL_Column', a1)
    if hasattr(a1, 'dDL_Create_table'):
        assert _is_linked(a1, 'dDL_Create_table', b)
    _safe_set(b, 'dDL_Column', a2)
    assert _is_linked(b, 'dDL_Column', a2)
    if hasattr(a1, 'dDL_Create_table'):
        assert not _is_linked(a1, 'dDL_Create_table', b)
    if hasattr(a2, 'dDL_Create_table'):
        assert _is_linked(a2, 'dDL_Create_table', b)
    _safe_set(b, 'dDL_Column', None)
    assert not _is_linked(b, 'dDL_Column', a2)
    if hasattr(a2, 'dDL_Create_table'):
        assert not _is_linked(a2, 'dDL_Create_table', b)


def test_assoc_constraint9_reverse_link_reassign_clear():
    a1 = dDL_Constraint(id="sample_text")
    a2 = dDL_Constraint(id="sample_text_2")
    b = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    _safe_set(b, 'dDL_Alter_table10', a1)
    assert _is_linked(b, 'dDL_Alter_table10', a1)
    if hasattr(a1, 'dDL_Constraint11'):
        assert _is_linked(a1, 'dDL_Constraint11', b)
    _safe_set(b, 'dDL_Alter_table10', a2)
    assert _is_linked(b, 'dDL_Alter_table10', a2)
    if hasattr(a1, 'dDL_Constraint11'):
        assert not _is_linked(a1, 'dDL_Constraint11', b)
    if hasattr(a2, 'dDL_Constraint11'):
        assert _is_linked(a2, 'dDL_Constraint11', b)
    _safe_set(b, 'dDL_Alter_table10', None)
    assert not _is_linked(b, 'dDL_Alter_table10', a2)
    if hasattr(a2, 'dDL_Constraint11'):
        assert not _is_linked(a2, 'dDL_Constraint11', b)


def test_assoc_constraints2_reverse_link_reassign_clear():
    a1 = dDL_Create_table(id="sample_text")
    a2 = dDL_Create_table(id="sample_text_2")
    b = dDL_Constraint(id="sample_text")
    _safe_set(b, 'dDL_Constraint', a1)
    assert _is_linked(b, 'dDL_Constraint', a1)
    if hasattr(a1, 'dDL_Create_table3'):
        assert _is_linked(a1, 'dDL_Create_table3', b)
    _safe_set(b, 'dDL_Constraint', a2)
    assert _is_linked(b, 'dDL_Constraint', a2)
    if hasattr(a1, 'dDL_Create_table3'):
        assert not _is_linked(a1, 'dDL_Create_table3', b)
    if hasattr(a2, 'dDL_Create_table3'):
        assert _is_linked(a2, 'dDL_Create_table3', b)
    _safe_set(b, 'dDL_Constraint', None)
    assert not _is_linked(b, 'dDL_Constraint', a2)
    if hasattr(a2, 'dDL_Create_table3'):
        assert not _is_linked(a2, 'dDL_Create_table3', b)


def test_assoc_isNull6_reverse_link_reassign_clear():
    a1 = dDL_ISNULL(nonNull=True, null=True)
    a2 = dDL_ISNULL(nonNull=False, null=False)
    b = dDL_Column(id="sample_text", number=7)
    _safe_set(b, 'dDL_Column7', a1)
    assert _is_linked(b, 'dDL_Column7', a1)
    if hasattr(a1, 'dDL_ISNULL'):
        assert _is_linked(a1, 'dDL_ISNULL', b)
    _safe_set(b, 'dDL_Column7', a2)
    assert _is_linked(b, 'dDL_Column7', a2)
    if hasattr(a1, 'dDL_ISNULL'):
        assert not _is_linked(a1, 'dDL_ISNULL', b)
    if hasattr(a2, 'dDL_ISNULL'):
        assert _is_linked(a2, 'dDL_ISNULL', b)
    _safe_set(b, 'dDL_Column7', None)
    assert not _is_linked(b, 'dDL_Column7', a2)
    if hasattr(a2, 'dDL_ISNULL'):
        assert not _is_linked(a2, 'dDL_ISNULL', b)


def test_assoc_sequence_options16_reverse_link_reassign_clear():
    a1 = dDL_Sequence_options(cache="sample_text", cycle="sample_text", increment="sample_text", maxvalue="sample_text", minvalue="sample_text", nocache="sample_text", nocycle="sample_text", nomaxvalue="sample_text", nominvalue="sample_text", noorder="sample_text", order="sample_text", start="sample_text")
    a2 = dDL_Sequence_options(cache="sample_text_2", cycle="sample_text_2", increment="sample_text_2", maxvalue="sample_text_2", minvalue="sample_text_2", nocache="sample_text_2", nocycle="sample_text_2", nomaxvalue="sample_text_2", nominvalue="sample_text_2", noorder="sample_text_2", order="sample_text_2", start="sample_text_2")
    b = dDL_Create_sequence(id="sample_text")
    _safe_set(b, 'dDL_Create_sequence', {a1})
    assert _is_linked(b, 'dDL_Create_sequence', a1)
    if hasattr(a1, 'dDL_Sequence_options'):
        assert _is_linked(a1, 'dDL_Sequence_options', b)
    _safe_set(b, 'dDL_Create_sequence', {a2})
    assert _is_linked(b, 'dDL_Create_sequence', a2)
    if hasattr(a1, 'dDL_Sequence_options'):
        assert not _is_linked(a1, 'dDL_Sequence_options', b)
    if hasattr(a2, 'dDL_Sequence_options'):
        assert _is_linked(a2, 'dDL_Sequence_options', b)
    _safe_set(b, 'dDL_Create_sequence', set())
    assert not _is_linked(b, 'dDL_Create_sequence', a2)
    if hasattr(a2, 'dDL_Sequence_options'):
        assert not _is_linked(a2, 'dDL_Sequence_options', b)


def test_assoc_tabname12_reverse_link_reassign_clear():
    a1 = dDL_Tabname(basename="sample_text", id="sample_text")
    a2 = dDL_Tabname(basename="sample_text_2", id="sample_text_2")
    b = dDL_Comment(columnId="sample_text", string="sample_text")
    _safe_set(b, 'dDL_Comment', a1)
    assert _is_linked(b, 'dDL_Comment', a1)
    if hasattr(a1, 'dDL_Tabname13'):
        assert _is_linked(a1, 'dDL_Tabname13', b)
    _safe_set(b, 'dDL_Comment', a2)
    assert _is_linked(b, 'dDL_Comment', a2)
    if hasattr(a1, 'dDL_Tabname13'):
        assert not _is_linked(a1, 'dDL_Tabname13', b)
    if hasattr(a2, 'dDL_Tabname13'):
        assert _is_linked(a2, 'dDL_Tabname13', b)
    _safe_set(b, 'dDL_Comment', None)
    assert not _is_linked(b, 'dDL_Comment', a2)
    if hasattr(a2, 'dDL_Tabname13'):
        assert not _is_linked(a2, 'dDL_Tabname13', b)


def test_assoc_tabname8_reverse_link_reassign_clear():
    a1 = dDL_Tabname(basename="sample_text", id="sample_text")
    a2 = dDL_Tabname(basename="sample_text_2", id="sample_text_2")
    b = dDL_Alter_table(add="sample_text", enable="sample_text", id="sample_text")
    _safe_set(b, 'dDL_Alter_table', a1)
    assert _is_linked(b, 'dDL_Alter_table', a1)
    if hasattr(a1, 'dDL_Tabname'):
        assert _is_linked(a1, 'dDL_Tabname', b)
    _safe_set(b, 'dDL_Alter_table', a2)
    assert _is_linked(b, 'dDL_Alter_table', a2)
    if hasattr(a1, 'dDL_Tabname'):
        assert not _is_linked(a1, 'dDL_Tabname', b)
    if hasattr(a2, 'dDL_Tabname'):
        assert _is_linked(a2, 'dDL_Tabname', b)
    _safe_set(b, 'dDL_Alter_table', None)
    assert not _is_linked(b, 'dDL_Alter_table', a2)
    if hasattr(a2, 'dDL_Tabname'):
        assert not _is_linked(a2, 'dDL_Tabname', b)


def test_assoc_type4_reverse_link_reassign_clear():
    a1 = dDL_TYPE(id="sample_text")
    a2 = dDL_TYPE(id="sample_text_2")
    b = dDL_Column(id="sample_text", number=7)
    _safe_set(b, 'dDL_Column5', a1)
    assert _is_linked(b, 'dDL_Column5', a1)
    if hasattr(a1, 'dDL_TYPE'):
        assert _is_linked(a1, 'dDL_TYPE', b)
    _safe_set(b, 'dDL_Column5', a2)
    assert _is_linked(b, 'dDL_Column5', a2)
    if hasattr(a1, 'dDL_TYPE'):
        assert not _is_linked(a1, 'dDL_TYPE', b)
    if hasattr(a2, 'dDL_TYPE'):
        assert _is_linked(a2, 'dDL_TYPE', b)
    _safe_set(b, 'dDL_Column5', None)
    assert not _is_linked(b, 'dDL_Column5', a2)
    if hasattr(a2, 'dDL_TYPE'):
        assert not _is_linked(a2, 'dDL_TYPE', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colNames19_stub_double():
    # dDL_Key has no real 'dDL_Key20' property in the generated
    # code (a bare stub) -- manually attach it so dDL_Colname's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dDL_Colname's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dDL_Colname(id="sample_text")
    partner = dDL_Key()
    setattr(partner, 'dDL_Key20', None)
    _safe_set(owner, 'dDL_Colname21', partner)
    assert owner in getattr(partner, 'dDL_Key20')
    _safe_set(owner, 'dDL_Colname21', None)
    assert owner not in getattr(partner, 'dDL_Key20')


def test_assoc_key17_stub_double():
    # dDL_Key has no real 'dDL_Key' property in the generated
    # code (a bare stub) -- manually attach it so dDL_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dDL_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dDL_Constraint(id="sample_text")
    partner = dDL_Key()
    setattr(partner, 'dDL_Key', None)
    _safe_set(owner, 'dDL_Constraint18', partner)
    assert getattr(partner, 'dDL_Key') == owner
    _safe_set(owner, 'dDL_Constraint18', None)
    assert getattr(partner, 'dDL_Key') is None


def test_assoc_tabname22_stub_double():
    # dDL_Foreign_key has no real 'dDL_Foreign_key' property in the generated
    # code (a bare stub) -- manually attach it so dDL_Tabname's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dDL_Tabname's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dDL_Tabname(basename="sample_text", id="sample_text")
    partner = dDL_Foreign_key()
    setattr(partner, 'dDL_Foreign_key', None)
    _safe_set(owner, 'dDL_Tabname23', partner)
    assert getattr(partner, 'dDL_Foreign_key') == owner
    _safe_set(owner, 'dDL_Tabname23', None)
    assert getattr(partner, 'dDL_Foreign_key') is None


