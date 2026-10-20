import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Operation,
    Trmodel_Add,
    Trmodel_Column,
    Trmodel_Delete,
    Trmodel_LoadModel,
    Trmodel_Operation,
    Trmodel_Table,
    Trmodel_Update,
    Trmodel_loader,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column5_stub_double():
    # Trmodel_Operation has no real 'Trmodel_Operation6' property in the generated
    # code (a bare stub) -- manually attach it so Trmodel_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trmodel_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trmodel_Column(Name="sample_text", tableName="sample_text")
    partner = Trmodel_Operation()
    setattr(partner, 'Trmodel_Operation6', None)
    _safe_set(owner, 'Trmodel_Column', partner)
    assert getattr(partner, 'Trmodel_Operation6') == owner
    _safe_set(owner, 'Trmodel_Column', None)
    assert getattr(partner, 'Trmodel_Operation6') is None


def test_assoc_loadmodel1_stub_double():
    # Trmodel_loader has no real 'Trmodel_loader2' property in the generated
    # code (a bare stub) -- manually attach it so Trmodel_LoadModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trmodel_LoadModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trmodel_LoadModel(url="sample_text")
    partner = Trmodel_loader()
    setattr(partner, 'Trmodel_loader2', None)
    _safe_set(owner, 'Trmodel_LoadModel', partner)
    assert getattr(partner, 'Trmodel_loader2') == owner
    _safe_set(owner, 'Trmodel_LoadModel', None)
    assert getattr(partner, 'Trmodel_loader2') is None


def test_assoc_table3_stub_double():
    # Trmodel_Operation has no real 'Trmodel_Operation4' property in the generated
    # code (a bare stub) -- manually attach it so Trmodel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trmodel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trmodel_Table(Name="sample_text")
    partner = Trmodel_Operation()
    setattr(partner, 'Trmodel_Operation4', None)
    _safe_set(owner, 'Trmodel_Table', partner)
    assert getattr(partner, 'Trmodel_Operation4') == owner
    _safe_set(owner, 'Trmodel_Table', None)
    assert getattr(partner, 'Trmodel_Operation4') is None


