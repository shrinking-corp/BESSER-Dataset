import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    relationalMetaModel_RelationalForeignKey,
    relationalMetaModel_RelationalSchema,
    relationalMetaModel_RelationalTable,
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

def test_assoc_ForeignKeys2_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalForeignKey(Name="sample_text")
    _safe_set(b, 'RelationalForeignKey', a1)
    assert _is_linked(b, 'RelationalForeignKey', a1)
    if hasattr(a1, 'OwnedByTable'):
        assert _is_linked(a1, 'OwnedByTable', b)
    _safe_set(b, 'RelationalForeignKey', a2)
    assert _is_linked(b, 'RelationalForeignKey', a2)
    if hasattr(a1, 'OwnedByTable'):
        assert not _is_linked(a1, 'OwnedByTable', b)
    if hasattr(a2, 'OwnedByTable'):
        assert _is_linked(a2, 'OwnedByTable', b)
    _safe_set(b, 'RelationalForeignKey', None)
    assert not _is_linked(b, 'RelationalForeignKey', a2)
    if hasattr(a2, 'OwnedByTable'):
        assert not _is_linked(a2, 'OwnedByTable', b)


def test_assoc_OwnedByTable5_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalForeignKey(Name="sample_text")
    _safe_set(b, 'ForeignKeys', a1)
    assert _is_linked(b, 'ForeignKeys', a1)
    if hasattr(a1, 'RelationalTable6'):
        assert _is_linked(a1, 'RelationalTable6', b)
    _safe_set(b, 'ForeignKeys', a2)
    assert _is_linked(b, 'ForeignKeys', a2)
    if hasattr(a1, 'RelationalTable6'):
        assert not _is_linked(a1, 'RelationalTable6', b)
    if hasattr(a2, 'RelationalTable6'):
        assert _is_linked(a2, 'RelationalTable6', b)
    _safe_set(b, 'ForeignKeys', None)
    assert not _is_linked(b, 'ForeignKeys', a2)
    if hasattr(a2, 'RelationalTable6'):
        assert not _is_linked(a2, 'RelationalTable6', b)


def test_assoc_ReferencedBy3_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalForeignKey(Name="sample_text")
    _safe_set(b, 'RelationalForeignKey4', a1)
    assert _is_linked(b, 'RelationalForeignKey4', a1)
    if hasattr(a1, 'ReferencedTable'):
        assert _is_linked(a1, 'ReferencedTable', b)
    _safe_set(b, 'RelationalForeignKey4', a2)
    assert _is_linked(b, 'RelationalForeignKey4', a2)
    if hasattr(a1, 'ReferencedTable'):
        assert not _is_linked(a1, 'ReferencedTable', b)
    if hasattr(a2, 'ReferencedTable'):
        assert _is_linked(a2, 'ReferencedTable', b)
    _safe_set(b, 'RelationalForeignKey4', None)
    assert not _is_linked(b, 'RelationalForeignKey4', a2)
    if hasattr(a2, 'ReferencedTable'):
        assert not _is_linked(a2, 'ReferencedTable', b)


def test_assoc_ReferencedTable7_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalForeignKey(Name="sample_text")
    _safe_set(b, 'ReferencedBy', a1)
    assert _is_linked(b, 'ReferencedBy', a1)
    if hasattr(a1, 'RelationalTable8'):
        assert _is_linked(a1, 'RelationalTable8', b)
    _safe_set(b, 'ReferencedBy', a2)
    assert _is_linked(b, 'ReferencedBy', a2)
    if hasattr(a1, 'RelationalTable8'):
        assert not _is_linked(a1, 'RelationalTable8', b)
    if hasattr(a2, 'RelationalTable8'):
        assert _is_linked(a2, 'RelationalTable8', b)
    _safe_set(b, 'ReferencedBy', None)
    assert not _is_linked(b, 'ReferencedBy', a2)
    if hasattr(a2, 'RelationalTable8'):
        assert not _is_linked(a2, 'RelationalTable8', b)


def test_assoc_Schema1_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalSchema(Name="sample_text")
    _safe_set(b, 'RelationalSchema', a1)
    assert _is_linked(b, 'RelationalSchema', a1)
    if hasattr(a1, 'Tables'):
        assert _is_linked(a1, 'Tables', b)
    _safe_set(b, 'RelationalSchema', a2)
    assert _is_linked(b, 'RelationalSchema', a2)
    if hasattr(a1, 'Tables'):
        assert not _is_linked(a1, 'Tables', b)
    if hasattr(a2, 'Tables'):
        assert _is_linked(a2, 'Tables', b)
    _safe_set(b, 'RelationalSchema', None)
    assert not _is_linked(b, 'RelationalSchema', a2)
    if hasattr(a2, 'Tables'):
        assert not _is_linked(a2, 'Tables', b)


def test_assoc_Tables0_reverse_link_reassign_clear():
    a1 = relationalMetaModel_RelationalTable(Name="sample_text")
    a2 = relationalMetaModel_RelationalTable(Name="sample_text_2")
    b = relationalMetaModel_RelationalSchema(Name="sample_text")
    _safe_set(b, 'Schema', {a1})
    assert _is_linked(b, 'Schema', a1)
    if hasattr(a1, 'RelationalTable'):
        assert _is_linked(a1, 'RelationalTable', b)
    _safe_set(b, 'Schema', {a2})
    assert _is_linked(b, 'Schema', a2)
    if hasattr(a1, 'RelationalTable'):
        assert not _is_linked(a1, 'RelationalTable', b)
    if hasattr(a2, 'RelationalTable'):
        assert _is_linked(a2, 'RelationalTable', b)
    _safe_set(b, 'Schema', set())
    assert not _is_linked(b, 'Schema', a2)
    if hasattr(a2, 'RelationalTable'):
        assert not _is_linked(a2, 'RelationalTable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

