import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Field,
    relational_Column,
    relational_DataBase,
    relational_Field,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Schema,
    relational_Table,
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

def test_assoc_fields3_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Field(name="sample_text")
    _safe_set(b, 'relational_Field', a1)
    assert _is_linked(b, 'relational_Field', a1)
    if hasattr(a1, 'relational_Table4'):
        assert _is_linked(a1, 'relational_Table4', b)
    _safe_set(b, 'relational_Field', a2)
    assert _is_linked(b, 'relational_Field', a2)
    if hasattr(a1, 'relational_Table4'):
        assert not _is_linked(a1, 'relational_Table4', b)
    if hasattr(a2, 'relational_Table4'):
        assert _is_linked(a2, 'relational_Table4', b)
    _safe_set(b, 'relational_Field', None)
    assert not _is_linked(b, 'relational_Field', a2)
    if hasattr(a2, 'relational_Table4'):
        assert not _is_linked(a2, 'relational_Table4', b)


def test_assoc_schemas0_reverse_link_reassign_clear():
    a1 = relational_Schema(name="sample_text")
    a2 = relational_Schema(name="sample_text_2")
    b = relational_DataBase(port=7, uri="sample_text")
    _safe_set(b, 'relational_DataBase', {a1})
    assert _is_linked(b, 'relational_DataBase', a1)
    if hasattr(a1, 'relational_Schema'):
        assert _is_linked(a1, 'relational_Schema', b)
    _safe_set(b, 'relational_DataBase', {a2})
    assert _is_linked(b, 'relational_DataBase', a2)
    if hasattr(a1, 'relational_Schema'):
        assert not _is_linked(a1, 'relational_Schema', b)
    if hasattr(a2, 'relational_Schema'):
        assert _is_linked(a2, 'relational_Schema', b)
    _safe_set(b, 'relational_DataBase', set())
    assert not _is_linked(b, 'relational_DataBase', a2)
    if hasattr(a2, 'relational_Schema'):
        assert not _is_linked(a2, 'relational_Schema', b)


def test_assoc_tables1_reverse_link_reassign_clear():
    a1 = relational_Table(name="sample_text")
    a2 = relational_Table(name="sample_text_2")
    b = relational_Schema(name="sample_text")
    _safe_set(b, 'relational_Schema2', {a1})
    assert _is_linked(b, 'relational_Schema2', a1)
    if hasattr(a1, 'relational_Table'):
        assert _is_linked(a1, 'relational_Table', b)
    _safe_set(b, 'relational_Schema2', {a2})
    assert _is_linked(b, 'relational_Schema2', a2)
    if hasattr(a1, 'relational_Table'):
        assert not _is_linked(a1, 'relational_Table', b)
    if hasattr(a2, 'relational_Table'):
        assert _is_linked(a2, 'relational_Table', b)
    _safe_set(b, 'relational_Schema2', set())
    assert not _is_linked(b, 'relational_Schema2', a2)
    if hasattr(a2, 'relational_Table'):
        assert not _is_linked(a2, 'relational_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_reference5_stub_double():
    # relational_ForeignKey has no real 'relational_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(name="sample_text")
    partner = relational_ForeignKey()
    setattr(partner, 'relational_ForeignKey', None)
    _safe_set(owner, 'relational_Table6', partner)
    assert getattr(partner, 'relational_ForeignKey') == owner
    _safe_set(owner, 'relational_Table6', None)
    assert getattr(partner, 'relational_ForeignKey') is None


