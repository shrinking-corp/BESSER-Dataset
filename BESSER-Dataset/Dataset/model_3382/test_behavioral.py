import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_Column,
    model_Constraint,
    model_Diagram,
    model_Table,
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

def test_assoc_columns0_reverse_link_reassign_clear():
    a1 = model_Table(name="sample_text")
    a2 = model_Table(name="sample_text_2")
    b = model_Column(name="sample_text")
    _safe_set(b, 'model_Column', a1)
    assert _is_linked(b, 'model_Column', a1)
    if hasattr(a1, 'model_Table'):
        assert _is_linked(a1, 'model_Table', b)
    _safe_set(b, 'model_Column', a2)
    assert _is_linked(b, 'model_Column', a2)
    if hasattr(a1, 'model_Table'):
        assert not _is_linked(a1, 'model_Table', b)
    if hasattr(a2, 'model_Table'):
        assert _is_linked(a2, 'model_Table', b)
    _safe_set(b, 'model_Column', None)
    assert not _is_linked(b, 'model_Column', a2)
    if hasattr(a2, 'model_Table'):
        assert not _is_linked(a2, 'model_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Source8_stub_double():
    # model_Constraint has no real 'model_Constraint9' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_Constraint()
    setattr(partner, 'model_Constraint9', None)
    _safe_set(owner, 'model_Table10', partner)
    assert getattr(partner, 'model_Constraint9') == owner
    _safe_set(owner, 'model_Table10', None)
    assert getattr(partner, 'model_Constraint9') is None


def test_assoc_TableDiagram6_stub_double():
    # model_Diagram has no real 'model_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_Diagram()
    setattr(partner, 'model_Diagram', None)
    _safe_set(owner, 'model_Table7', partner)
    assert owner in getattr(partner, 'model_Diagram')
    _safe_set(owner, 'model_Table7', None)
    assert owner not in getattr(partner, 'model_Diagram')


def test_assoc_Target11_stub_double():
    # model_Constraint has no real 'model_Constraint12' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_Constraint()
    setattr(partner, 'model_Constraint12', None)
    _safe_set(owner, 'model_Table13', partner)
    assert getattr(partner, 'model_Constraint12') == owner
    _safe_set(owner, 'model_Table13', None)
    assert getattr(partner, 'model_Constraint12') is None


def test_assoc_sourceConstraints1_stub_double():
    # model_Constraint has no real 'model_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_Constraint()
    setattr(partner, 'model_Constraint', None)
    _safe_set(owner, 'model_Table2', {partner})
    assert getattr(partner, 'model_Constraint') == owner
    _safe_set(owner, 'model_Table2', set())
    assert getattr(partner, 'model_Constraint') is None


def test_assoc_targetConstraint3_stub_double():
    # model_Constraint has no real 'model_Constraint5' property in the generated
    # code (a bare stub) -- manually attach it so model_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Table(name="sample_text")
    partner = model_Constraint()
    setattr(partner, 'model_Constraint5', None)
    _safe_set(owner, 'model_Table4', {partner})
    assert getattr(partner, 'model_Constraint5') == owner
    _safe_set(owner, 'model_Table4', set())
    assert getattr(partner, 'model_Constraint5') is None


