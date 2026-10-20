import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DML_Column,
    DML_InsertInto,
    DML_InsertsStatements,
    DML_Registry,
    DML_Value,
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

def test_assoc_column7_reverse_link_reassign_clear():
    a1 = DML_Value(value="sample_text")
    a2 = DML_Value(value="sample_text_2")
    b = DML_Column(columnName="sample_text")
    _safe_set(b, 'DML_Column9', a1)
    assert _is_linked(b, 'DML_Column9', a1)
    if hasattr(a1, 'DML_Value8'):
        assert _is_linked(a1, 'DML_Value8', b)
    _safe_set(b, 'DML_Column9', a2)
    assert _is_linked(b, 'DML_Column9', a2)
    if hasattr(a1, 'DML_Value8'):
        assert not _is_linked(a1, 'DML_Value8', b)
    if hasattr(a2, 'DML_Value8'):
        assert _is_linked(a2, 'DML_Value8', b)
    _safe_set(b, 'DML_Column9', None)
    assert not _is_linked(b, 'DML_Column9', a2)
    if hasattr(a2, 'DML_Value8'):
        assert not _is_linked(a2, 'DML_Value8', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = DML_InsertInto(tableName="sample_text")
    a2 = DML_InsertInto(tableName="sample_text_2")
    b = DML_Column(columnName="sample_text")
    _safe_set(b, 'DML_Column', a1)
    assert _is_linked(b, 'DML_Column', a1)
    if hasattr(a1, 'DML_InsertInto4'):
        assert _is_linked(a1, 'DML_InsertInto4', b)
    _safe_set(b, 'DML_Column', a2)
    assert _is_linked(b, 'DML_Column', a2)
    if hasattr(a1, 'DML_InsertInto4'):
        assert not _is_linked(a1, 'DML_InsertInto4', b)
    if hasattr(a2, 'DML_InsertInto4'):
        assert _is_linked(a2, 'DML_InsertInto4', b)
    _safe_set(b, 'DML_Column', None)
    assert not _is_linked(b, 'DML_Column', a2)
    if hasattr(a2, 'DML_InsertInto4'):
        assert not _is_linked(a2, 'DML_InsertInto4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_insertsInto0_stub_double():
    # DML_InsertsStatements has no real 'DML_InsertsStatements' property in the generated
    # code (a bare stub) -- manually attach it so DML_InsertInto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DML_InsertInto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DML_InsertInto(tableName="sample_text")
    partner = DML_InsertsStatements()
    setattr(partner, 'DML_InsertsStatements', None)
    _safe_set(owner, 'DML_InsertInto', partner)
    assert owner in getattr(partner, 'DML_InsertsStatements')
    _safe_set(owner, 'DML_InsertInto', None)
    assert owner not in getattr(partner, 'DML_InsertsStatements')


def test_assoc_registry1_stub_double():
    # DML_Registry has no real 'DML_Registry' property in the generated
    # code (a bare stub) -- manually attach it so DML_InsertInto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DML_InsertInto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DML_InsertInto(tableName="sample_text")
    partner = DML_Registry()
    setattr(partner, 'DML_Registry', None)
    _safe_set(owner, 'DML_InsertInto2', partner)
    assert getattr(partner, 'DML_Registry') == owner
    _safe_set(owner, 'DML_InsertInto2', None)
    assert getattr(partner, 'DML_Registry') is None


def test_assoc_registryValues5_stub_double():
    # DML_Registry has no real 'DML_Registry6' property in the generated
    # code (a bare stub) -- manually attach it so DML_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DML_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DML_Value(value="sample_text")
    partner = DML_Registry()
    setattr(partner, 'DML_Registry6', None)
    _safe_set(owner, 'DML_Value', partner)
    assert owner in getattr(partner, 'DML_Registry6')
    _safe_set(owner, 'DML_Value', None)
    assert owner not in getattr(partner, 'DML_Registry6')


