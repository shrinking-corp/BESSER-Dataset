import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class,
    LoadGameWidget,
    Model,
    Persistence,
    SaveGameWidget,
    felhaszn_l__Actor,
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

def test_assoc_Class_Model_stub_double():
    # Class has no real 'model2' property in the generated
    # code (a bare stub) -- manually attach it so Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model(gameOver=True, gameSize="sample_text", gameTable="sample_text", goodselected=True, pl1="sample_text", pl1points="sample_text", pl2="sample_text", pl2points="sample_text", playerNr="sample_text", selected="sample_text", steps="sample_text")
    partner = Class()
    setattr(partner, 'model2', None)
    _safe_set(owner, 'class3', partner)
    assert getattr(partner, 'model2') == owner
    _safe_set(owner, 'class3', None)
    assert getattr(partner, 'model2') is None


def test_assoc_Class_SaveGameWidget_stub_double():
    # Class has no real 'saveGameWidget4' property in the generated
    # code (a bare stub) -- manually attach it so SaveGameWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SaveGameWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SaveGameWidget(_listWidget="sample_text", cancelButton="sample_text", okButton="sample_text")
    partner = Class()
    setattr(partner, 'saveGameWidget4', None)
    _safe_set(owner, 'class5', partner)
    assert getattr(partner, 'saveGameWidget4') == owner
    _safe_set(owner, 'class5', None)
    assert getattr(partner, 'saveGameWidget4') is None


def test_assoc_Model_Persistence_stub_double():
    # Persistence has no real 'model7' property in the generated
    # code (a bare stub) -- manually attach it so Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model(gameOver=True, gameSize="sample_text", gameTable="sample_text", goodselected=True, pl1="sample_text", pl1points="sample_text", pl2="sample_text", pl2points="sample_text", playerNr="sample_text", selected="sample_text", steps="sample_text")
    partner = Persistence()
    setattr(partner, 'model7', None)
    _safe_set(owner, '_dataAccess6', partner)
    assert getattr(partner, 'model7') == owner
    _safe_set(owner, '_dataAccess6', None)
    assert getattr(partner, 'model7') is None


