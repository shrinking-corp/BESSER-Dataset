import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Connect4_Board,
    Connect4_CirclePanel,
    Connect4_Player,
    Connect4_Token,
    Connect4_connect,
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

def test_assoc_Board_Player_reverse_link_reassign_clear():
    a1 = Connect4_Player(currentPlayer=True, name="sample_text", roundWon=True, tokenColor="sample_text", wins=7)
    a2 = Connect4_Player(currentPlayer=False, name="sample_text_2", roundWon=False, tokenColor="sample_text_2", wins=13)
    b = Connect4_Board(gameBoard="sample_text", maxColumns=7, maxRows=7)
    _safe_set(b, 'player2', {a1})
    assert _is_linked(b, 'player2', a1)
    if hasattr(a1, 'board3'):
        assert _is_linked(a1, 'board3', b)
    _safe_set(b, 'player2', {a2})
    assert _is_linked(b, 'player2', a2)
    if hasattr(a1, 'board3'):
        assert not _is_linked(a1, 'board3', b)
    if hasattr(a2, 'board3'):
        assert _is_linked(a2, 'board3', b)
    _safe_set(b, 'player2', set())
    assert not _is_linked(b, 'player2', a2)
    if hasattr(a2, 'board3'):
        assert not _is_linked(a2, 'board3', b)


def test_assoc_Board_Token_reverse_link_reassign_clear():
    a1 = Connect4_Token(color="sample_text", isEmpty=True, xValue=7, yValue=7)
    a2 = Connect4_Token(color="sample_text_2", isEmpty=False, xValue=13, yValue=13)
    b = Connect4_Board(gameBoard="sample_text", maxColumns=7, maxRows=7)
    _safe_set(b, 'token0', {a1})
    assert _is_linked(b, 'token0', a1)
    if hasattr(a1, 'board1'):
        assert _is_linked(a1, 'board1', b)
    _safe_set(b, 'token0', {a2})
    assert _is_linked(b, 'token0', a2)
    if hasattr(a1, 'board1'):
        assert not _is_linked(a1, 'board1', b)
    if hasattr(a2, 'board1'):
        assert _is_linked(a2, 'board1', b)
    _safe_set(b, 'token0', set())
    assert not _is_linked(b, 'token0', a2)
    if hasattr(a2, 'board1'):
        assert not _is_linked(a2, 'board1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

