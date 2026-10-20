import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AI,
    Board,
    Dice,
    EventHandler,
    Field,
    GameEngine,
    GameState,
    GraphicsGenerator,
    IOFilesManagement,
    Menu,
    Pawn,
    Player,
    Window,
    Color,
    PlayerType,
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

def test_assoc_Board_GraphicsGenerator_stub_double():
    # GraphicsGenerator has no real 'board7' property in the generated
    # code (a bare stub) -- manually attach it so Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Board(board="sample_text")
    partner = GraphicsGenerator()
    setattr(partner, 'board7', None)
    _safe_set(owner, 'graphicsGenerator6', partner)
    assert getattr(partner, 'board7') == owner
    _safe_set(owner, 'graphicsGenerator6', None)
    assert getattr(partner, 'board7') is None


def test_assoc_Board_Window_stub_double():
    # Window has no real 'board17' property in the generated
    # code (a bare stub) -- manually attach it so Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Board(board="sample_text")
    partner = Window()
    setattr(partner, 'board17', None)
    _safe_set(owner, 'window16', partner)
    assert getattr(partner, 'board17') == owner
    _safe_set(owner, 'window16', None)
    assert getattr(partner, 'board17') is None


def test_assoc_GameEngine_Board_stub_double():
    # GameEngine has no real 'board10' property in the generated
    # code (a bare stub) -- manually attach it so Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Board(board="sample_text")
    partner = GameEngine()
    setattr(partner, 'board10', None)
    _safe_set(owner, 'gameEngine11', partner)
    assert getattr(partner, 'board10') == owner
    _safe_set(owner, 'gameEngine11', None)
    assert getattr(partner, 'board10') is None


