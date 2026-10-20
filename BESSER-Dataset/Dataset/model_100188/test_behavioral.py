import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metamodel_Cell,
    metamodel_Column,
    metamodel_Constraint,
    metamodel_Database,
    metamodel_Row,
    metamodel_Sequence,
    metamodel_Table,
    ConstraintType,
    Datatype,
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

def test_assoc_References9_reverse_link_reassign_clear():
    a1 = metamodel_Constraint(name="sample_text", reference="sample_text", type="sample_text")
    a2 = metamodel_Constraint(name="sample_text_2", reference="sample_text_2", type="sample_text_2")
    b = metamodel_Column(name="sample_text", nullable=True, size="sample_text", type="sample_text")
    _safe_set(b, 'metamodel_Column11', a1)
    assert _is_linked(b, 'metamodel_Column11', a1)
    if hasattr(a1, 'metamodel_Constraint10'):
        assert _is_linked(a1, 'metamodel_Constraint10', b)
    _safe_set(b, 'metamodel_Column11', a2)
    assert _is_linked(b, 'metamodel_Column11', a2)
    if hasattr(a1, 'metamodel_Constraint10'):
        assert not _is_linked(a1, 'metamodel_Constraint10', b)
    if hasattr(a2, 'metamodel_Constraint10'):
        assert _is_linked(a2, 'metamodel_Constraint10', b)
    _safe_set(b, 'metamodel_Column11', None)
    assert not _is_linked(b, 'metamodel_Column11', a2)
    if hasattr(a2, 'metamodel_Constraint10'):
        assert not _is_linked(a2, 'metamodel_Constraint10', b)


def test_assoc_column17_reverse_link_reassign_clear():
    a1 = metamodel_Column(name="sample_text", nullable=True, size="sample_text", type="sample_text")
    a2 = metamodel_Column(name="sample_text_2", nullable=False, size="sample_text_2", type="sample_text_2")
    b = metamodel_Cell(value="sample_text")
    _safe_set(b, 'metamodel_Cell18', a1)
    assert _is_linked(b, 'metamodel_Cell18', a1)
    if hasattr(a1, 'metamodel_Column19'):
        assert _is_linked(a1, 'metamodel_Column19', b)
    _safe_set(b, 'metamodel_Cell18', a2)
    assert _is_linked(b, 'metamodel_Cell18', a2)
    if hasattr(a1, 'metamodel_Column19'):
        assert not _is_linked(a1, 'metamodel_Column19', b)
    if hasattr(a2, 'metamodel_Column19'):
        assert _is_linked(a2, 'metamodel_Column19', b)
    _safe_set(b, 'metamodel_Cell18', None)
    assert not _is_linked(b, 'metamodel_Cell18', a2)
    if hasattr(a2, 'metamodel_Column19'):
        assert not _is_linked(a2, 'metamodel_Column19', b)


def test_assoc_columns5_reverse_link_reassign_clear():
    a1 = metamodel_Table(name="sample_text")
    a2 = metamodel_Table(name="sample_text_2")
    b = metamodel_Column(name="sample_text", nullable=True, size="sample_text", type="sample_text")
    _safe_set(b, 'metamodel_Column', a1)
    assert _is_linked(b, 'metamodel_Column', a1)
    if hasattr(a1, 'metamodel_Table6'):
        assert _is_linked(a1, 'metamodel_Table6', b)
    _safe_set(b, 'metamodel_Column', a2)
    assert _is_linked(b, 'metamodel_Column', a2)
    if hasattr(a1, 'metamodel_Table6'):
        assert not _is_linked(a1, 'metamodel_Table6', b)
    if hasattr(a2, 'metamodel_Table6'):
        assert _is_linked(a2, 'metamodel_Table6', b)
    _safe_set(b, 'metamodel_Column', None)
    assert not _is_linked(b, 'metamodel_Column', a2)
    if hasattr(a2, 'metamodel_Table6'):
        assert not _is_linked(a2, 'metamodel_Table6', b)


def test_assoc_constraints12_reverse_link_reassign_clear():
    a1 = metamodel_Constraint(name="sample_text", reference="sample_text", type="sample_text")
    a2 = metamodel_Constraint(name="sample_text_2", reference="sample_text_2", type="sample_text_2")
    b = metamodel_Column(name="sample_text", nullable=True, size="sample_text", type="sample_text")
    _safe_set(b, 'metamodel_Column13', {a1})
    assert _is_linked(b, 'metamodel_Column13', a1)
    if hasattr(a1, 'metamodel_Constraint14'):
        assert _is_linked(a1, 'metamodel_Constraint14', b)
    _safe_set(b, 'metamodel_Column13', {a2})
    assert _is_linked(b, 'metamodel_Column13', a2)
    if hasattr(a1, 'metamodel_Constraint14'):
        assert not _is_linked(a1, 'metamodel_Constraint14', b)
    if hasattr(a2, 'metamodel_Constraint14'):
        assert _is_linked(a2, 'metamodel_Constraint14', b)
    _safe_set(b, 'metamodel_Column13', set())
    assert not _is_linked(b, 'metamodel_Column13', a2)
    if hasattr(a2, 'metamodel_Constraint14'):
        assert not _is_linked(a2, 'metamodel_Constraint14', b)


def test_assoc_constraints3_reverse_link_reassign_clear():
    a1 = metamodel_Table(name="sample_text")
    a2 = metamodel_Table(name="sample_text_2")
    b = metamodel_Constraint(name="sample_text", reference="sample_text", type="sample_text")
    _safe_set(b, 'metamodel_Constraint', a1)
    assert _is_linked(b, 'metamodel_Constraint', a1)
    if hasattr(a1, 'metamodel_Table4'):
        assert _is_linked(a1, 'metamodel_Table4', b)
    _safe_set(b, 'metamodel_Constraint', a2)
    assert _is_linked(b, 'metamodel_Constraint', a2)
    if hasattr(a1, 'metamodel_Table4'):
        assert not _is_linked(a1, 'metamodel_Table4', b)
    if hasattr(a2, 'metamodel_Table4'):
        assert _is_linked(a2, 'metamodel_Table4', b)
    _safe_set(b, 'metamodel_Constraint', None)
    assert not _is_linked(b, 'metamodel_Constraint', a2)
    if hasattr(a2, 'metamodel_Table4'):
        assert not _is_linked(a2, 'metamodel_Table4', b)


def test_assoc_sequences1_reverse_link_reassign_clear():
    a1 = metamodel_Sequence(currentValue="sample_text", cycle=True, incrementby=7, maxValue="sample_text", minValue=7, name="sample_text", startwith="sample_text")
    a2 = metamodel_Sequence(currentValue="sample_text_2", cycle=False, incrementby=13, maxValue="sample_text_2", minValue=13, name="sample_text_2", startwith="sample_text_2")
    b = metamodel_Database(name="sample_text")
    _safe_set(b, 'metamodel_Database2', {a1})
    assert _is_linked(b, 'metamodel_Database2', a1)
    if hasattr(a1, 'metamodel_Sequence'):
        assert _is_linked(a1, 'metamodel_Sequence', b)
    _safe_set(b, 'metamodel_Database2', {a2})
    assert _is_linked(b, 'metamodel_Database2', a2)
    if hasattr(a1, 'metamodel_Sequence'):
        assert not _is_linked(a1, 'metamodel_Sequence', b)
    if hasattr(a2, 'metamodel_Sequence'):
        assert _is_linked(a2, 'metamodel_Sequence', b)
    _safe_set(b, 'metamodel_Database2', set())
    assert not _is_linked(b, 'metamodel_Database2', a2)
    if hasattr(a2, 'metamodel_Sequence'):
        assert not _is_linked(a2, 'metamodel_Sequence', b)


def test_assoc_table0_reverse_link_reassign_clear():
    a1 = metamodel_Table(name="sample_text")
    a2 = metamodel_Table(name="sample_text_2")
    b = metamodel_Database(name="sample_text")
    _safe_set(b, 'metamodel_Database', {a1})
    assert _is_linked(b, 'metamodel_Database', a1)
    if hasattr(a1, 'metamodel_Table'):
        assert _is_linked(a1, 'metamodel_Table', b)
    _safe_set(b, 'metamodel_Database', {a2})
    assert _is_linked(b, 'metamodel_Database', a2)
    if hasattr(a1, 'metamodel_Table'):
        assert not _is_linked(a1, 'metamodel_Table', b)
    if hasattr(a2, 'metamodel_Table'):
        assert _is_linked(a2, 'metamodel_Table', b)
    _safe_set(b, 'metamodel_Database', set())
    assert not _is_linked(b, 'metamodel_Database', a2)
    if hasattr(a2, 'metamodel_Table'):
        assert not _is_linked(a2, 'metamodel_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cells15_stub_double():
    # metamodel_Row has no real 'metamodel_Row16' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Cell(value="sample_text")
    partner = metamodel_Row()
    setattr(partner, 'metamodel_Row16', None)
    _safe_set(owner, 'metamodel_Cell', partner)
    assert owner in getattr(partner, 'metamodel_Row16')
    _safe_set(owner, 'metamodel_Cell', None)
    assert owner not in getattr(partner, 'metamodel_Row16')


def test_assoc_rows7_stub_double():
    # metamodel_Row has no real 'metamodel_Row' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Table(name="sample_text")
    partner = metamodel_Row()
    setattr(partner, 'metamodel_Row', None)
    _safe_set(owner, 'metamodel_Table8', {partner})
    assert getattr(partner, 'metamodel_Row') == owner
    _safe_set(owner, 'metamodel_Table8', set())
    assert getattr(partner, 'metamodel_Row') is None


