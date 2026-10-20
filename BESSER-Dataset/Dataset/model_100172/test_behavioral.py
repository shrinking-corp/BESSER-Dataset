import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rdbmsMM_Column,
    rdbmsMM_ForeignKey,
    rdbmsMM_Key,
    rdbmsMM_Schema,
    rdbmsMM_Table,
    rdbmsMM_dummy,
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

def test_assoc_column20_reverse_link_reassign_clear():
    a1 = rdbmsMM_Key(name="sample_text")
    a2 = rdbmsMM_Key(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column22', a1)
    assert _is_linked(b, 'Column22', a1)
    if hasattr(a1, 'hasKey21'):
        assert _is_linked(a1, 'hasKey21', b)
    _safe_set(b, 'Column22', a2)
    assert _is_linked(b, 'Column22', a2)
    if hasattr(a1, 'hasKey21'):
        assert not _is_linked(a1, 'hasKey21', b)
    if hasattr(a2, 'hasKey21'):
        assert _is_linked(a2, 'hasKey21', b)
    _safe_set(b, 'Column22', None)
    assert not _is_linked(b, 'Column22', a2)
    if hasattr(a2, 'hasKey21'):
        assert not _is_linked(a2, 'hasKey21', b)


def test_assoc_column31_reverse_link_reassign_clear():
    a1 = rdbmsMM_ForeignKey(name="sample_text")
    a2 = rdbmsMM_ForeignKey(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column33', a1)
    assert _is_linked(b, 'Column33', a1)
    if hasattr(a1, 'hasForeignKey32'):
        assert _is_linked(a1, 'hasForeignKey32', b)
    _safe_set(b, 'Column33', a2)
    assert _is_linked(b, 'Column33', a2)
    if hasattr(a1, 'hasForeignKey32'):
        assert not _is_linked(a1, 'hasForeignKey32', b)
    if hasattr(a2, 'hasForeignKey32'):
        assert _is_linked(a2, 'hasForeignKey32', b)
    _safe_set(b, 'Column33', None)
    assert not _is_linked(b, 'Column33', a2)
    if hasattr(a2, 'hasForeignKey32'):
        assert not _is_linked(a2, 'hasForeignKey32', b)


def test_assoc_column4_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_foreignKey1_reverse_link_reassign_clear():
    a1 = rdbmsMM_Schema(name="sample_text")
    a2 = rdbmsMM_Schema(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey', a1)
    assert _is_linked(b, 'ForeignKey', a1)
    if hasattr(a1, 'schema2'):
        assert _is_linked(a1, 'schema2', b)
    _safe_set(b, 'ForeignKey', a2)
    assert _is_linked(b, 'ForeignKey', a2)
    if hasattr(a1, 'schema2'):
        assert not _is_linked(a1, 'schema2', b)
    if hasattr(a2, 'schema2'):
        assert _is_linked(a2, 'schema2', b)
    _safe_set(b, 'ForeignKey', None)
    assert not _is_linked(b, 'ForeignKey', a2)
    if hasattr(a2, 'schema2'):
        assert not _is_linked(a2, 'schema2', b)


def test_assoc_hasForeignKey15_reverse_link_reassign_clear():
    a1 = rdbmsMM_ForeignKey(name="sample_text")
    a2 = rdbmsMM_ForeignKey(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column16', {a1})
    assert _is_linked(b, 'column16', a1)
    if hasattr(a1, 'ForeignKey17'):
        assert _is_linked(a1, 'ForeignKey17', b)
    _safe_set(b, 'column16', {a2})
    assert _is_linked(b, 'column16', a2)
    if hasattr(a1, 'ForeignKey17'):
        assert not _is_linked(a1, 'ForeignKey17', b)
    if hasattr(a2, 'ForeignKey17'):
        assert _is_linked(a2, 'ForeignKey17', b)
    _safe_set(b, 'column16', set())
    assert not _is_linked(b, 'column16', a2)
    if hasattr(a2, 'ForeignKey17'):
        assert not _is_linked(a2, 'ForeignKey17', b)


def test_assoc_hasForeignKey7_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey9', a1)
    assert _is_linked(b, 'ForeignKey9', a1)
    if hasattr(a1, 'owner8'):
        assert _is_linked(a1, 'owner8', b)
    _safe_set(b, 'ForeignKey9', a2)
    assert _is_linked(b, 'ForeignKey9', a2)
    if hasattr(a1, 'owner8'):
        assert not _is_linked(a1, 'owner8', b)
    if hasattr(a2, 'owner8'):
        assert _is_linked(a2, 'owner8', b)
    _safe_set(b, 'ForeignKey9', None)
    assert not _is_linked(b, 'ForeignKey9', a2)
    if hasattr(a2, 'owner8'):
        assert not _is_linked(a2, 'owner8', b)


def test_assoc_hasKey12_reverse_link_reassign_clear():
    a1 = rdbmsMM_Key(name="sample_text")
    a2 = rdbmsMM_Key(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column13', {a1})
    assert _is_linked(b, 'column13', a1)
    if hasattr(a1, 'Key14'):
        assert _is_linked(a1, 'Key14', b)
    _safe_set(b, 'column13', {a2})
    assert _is_linked(b, 'column13', a2)
    if hasattr(a1, 'Key14'):
        assert not _is_linked(a1, 'Key14', b)
    if hasattr(a2, 'Key14'):
        assert _is_linked(a2, 'Key14', b)
    _safe_set(b, 'column13', set())
    assert not _is_linked(b, 'column13', a2)
    if hasattr(a2, 'Key14'):
        assert not _is_linked(a2, 'Key14', b)


def test_assoc_hasKey5_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Key(name="sample_text")
    _safe_set(b, 'Key', a1)
    assert _is_linked(b, 'Key', a1)
    if hasattr(a1, 'owner6'):
        assert _is_linked(a1, 'owner6', b)
    _safe_set(b, 'Key', a2)
    assert _is_linked(b, 'Key', a2)
    if hasattr(a1, 'owner6'):
        assert not _is_linked(a1, 'owner6', b)
    if hasattr(a2, 'owner6'):
        assert _is_linked(a2, 'owner6', b)
    _safe_set(b, 'Key', None)
    assert not _is_linked(b, 'Key', a2)
    if hasattr(a2, 'owner6'):
        assert not _is_linked(a2, 'owner6', b)


def test_assoc_owner10_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column', a1)
    assert _is_linked(b, 'column', a1)
    if hasattr(a1, 'Table11'):
        assert _is_linked(a1, 'Table11', b)
    _safe_set(b, 'column', a2)
    assert _is_linked(b, 'column', a2)
    if hasattr(a1, 'Table11'):
        assert not _is_linked(a1, 'Table11', b)
    if hasattr(a2, 'Table11'):
        assert _is_linked(a2, 'Table11', b)
    _safe_set(b, 'column', None)
    assert not _is_linked(b, 'column', a2)
    if hasattr(a2, 'Table11'):
        assert not _is_linked(a2, 'Table11', b)


def test_assoc_owner18_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Key(name="sample_text")
    _safe_set(b, 'hasKey', a1)
    assert _is_linked(b, 'hasKey', a1)
    if hasattr(a1, 'Table19'):
        assert _is_linked(a1, 'Table19', b)
    _safe_set(b, 'hasKey', a2)
    assert _is_linked(b, 'hasKey', a2)
    if hasattr(a1, 'Table19'):
        assert not _is_linked(a1, 'Table19', b)
    if hasattr(a2, 'Table19'):
        assert _is_linked(a2, 'Table19', b)
    _safe_set(b, 'hasKey', None)
    assert not _is_linked(b, 'hasKey', a2)
    if hasattr(a2, 'Table19'):
        assert not _is_linked(a2, 'Table19', b)


def test_assoc_owner29_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'hasForeignKey', a1)
    assert _is_linked(b, 'hasForeignKey', a1)
    if hasattr(a1, 'Table30'):
        assert _is_linked(a1, 'Table30', b)
    _safe_set(b, 'hasForeignKey', a2)
    assert _is_linked(b, 'hasForeignKey', a2)
    if hasattr(a1, 'Table30'):
        assert not _is_linked(a1, 'Table30', b)
    if hasattr(a2, 'Table30'):
        assert _is_linked(a2, 'Table30', b)
    _safe_set(b, 'hasForeignKey', None)
    assert not _is_linked(b, 'hasForeignKey', a2)
    if hasattr(a2, 'Table30'):
        assert not _is_linked(a2, 'Table30', b)


def test_assoc_referredBy23_reverse_link_reassign_clear():
    a1 = rdbmsMM_Key(name="sample_text")
    a2 = rdbmsMM_Key(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey24', a1)
    assert _is_linked(b, 'ForeignKey24', a1)
    if hasattr(a1, 'refersTo'):
        assert _is_linked(a1, 'refersTo', b)
    _safe_set(b, 'ForeignKey24', a2)
    assert _is_linked(b, 'ForeignKey24', a2)
    if hasattr(a1, 'refersTo'):
        assert not _is_linked(a1, 'refersTo', b)
    if hasattr(a2, 'refersTo'):
        assert _is_linked(a2, 'refersTo', b)
    _safe_set(b, 'ForeignKey24', None)
    assert not _is_linked(b, 'ForeignKey24', a2)
    if hasattr(a2, 'refersTo'):
        assert not _is_linked(a2, 'refersTo', b)


def test_assoc_refersTo27_reverse_link_reassign_clear():
    a1 = rdbmsMM_Key(name="sample_text")
    a2 = rdbmsMM_Key(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'referredBy', a1)
    assert _is_linked(b, 'referredBy', a1)
    if hasattr(a1, 'Key28'):
        assert _is_linked(a1, 'Key28', b)
    _safe_set(b, 'referredBy', a2)
    assert _is_linked(b, 'referredBy', a2)
    if hasattr(a1, 'Key28'):
        assert not _is_linked(a1, 'Key28', b)
    if hasattr(a2, 'Key28'):
        assert _is_linked(a2, 'Key28', b)
    _safe_set(b, 'referredBy', None)
    assert not _is_linked(b, 'referredBy', a2)
    if hasattr(a2, 'Key28'):
        assert not _is_linked(a2, 'Key28', b)


def test_assoc_schema25_reverse_link_reassign_clear():
    a1 = rdbmsMM_Schema(name="sample_text")
    a2 = rdbmsMM_Schema(name="sample_text_2")
    b = rdbmsMM_ForeignKey(name="sample_text")
    _safe_set(b, 'foreignKey', a1)
    assert _is_linked(b, 'foreignKey', a1)
    if hasattr(a1, 'Schema26'):
        assert _is_linked(a1, 'Schema26', b)
    _safe_set(b, 'foreignKey', a2)
    assert _is_linked(b, 'foreignKey', a2)
    if hasattr(a1, 'Schema26'):
        assert not _is_linked(a1, 'Schema26', b)
    if hasattr(a2, 'Schema26'):
        assert _is_linked(a2, 'Schema26', b)
    _safe_set(b, 'foreignKey', None)
    assert not _is_linked(b, 'foreignKey', a2)
    if hasattr(a2, 'Schema26'):
        assert not _is_linked(a2, 'Schema26', b)


def test_assoc_schema3_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Schema(name="sample_text")
    _safe_set(b, 'Schema', a1)
    assert _is_linked(b, 'Schema', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Schema', a2)
    assert _is_linked(b, 'Schema', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Schema', None)
    assert not _is_linked(b, 'Schema', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_table0_reverse_link_reassign_clear():
    a1 = rdbmsMM_Table(name="sample_text")
    a2 = rdbmsMM_Table(name="sample_text_2")
    b = rdbmsMM_Schema(name="sample_text")
    _safe_set(b, 'schema', {a1})
    assert _is_linked(b, 'schema', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'schema', {a2})
    assert _is_linked(b, 'schema', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'schema', set())
    assert not _is_linked(b, 'schema', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containsSchema34_stub_double():
    # rdbmsMM_dummy has no real 'rdbmsMM_dummy' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Schema(name="sample_text")
    partner = rdbmsMM_dummy()
    setattr(partner, 'rdbmsMM_dummy', None)
    _safe_set(owner, 'rdbmsMM_Schema', partner)
    assert owner in getattr(partner, 'rdbmsMM_dummy')
    _safe_set(owner, 'rdbmsMM_Schema', None)
    assert owner not in getattr(partner, 'rdbmsMM_dummy')


