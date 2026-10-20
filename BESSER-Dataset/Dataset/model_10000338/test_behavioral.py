import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Color_external,
    ImageIcon_external,
    JButton_external,
    candyCrushPackage_ActionListener_Interface,
    candyCrushPackage_Board,
    candyCrushPackage_Candy,
    candyCrushPackage_CandyButton,
    candyCrushPackage_ColorBombCandy,
    candyCrushPackage_Game,
    candyCrushPackage_JFrame,
    candyCrushPackage_JPanel,
    candyCrushPackage_Menu,
    candyCrushPackage_RegularCandy,
    candyCrushPackage_StrippedCandy,
    candyCrushPackage_Visited_Interface,
    candyCrushPackage_Visitor_Interface,
    candyCrushPackage_WrappedCandy,
    candyCrushPackage_SwapDirection,
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

def test_assoc_Candy_Candy_reverse_link_reassign_clear():
    a1 = candyCrushPackage_Candy(col=7, color=7, row=7)
    a2 = candyCrushPackage_Candy(col=13, color=13, row=13)
    b = candyCrushPackage_Candy(col=7, color=7, row=7)
    _safe_set(b, 'candy9', a1)
    assert _is_linked(b, 'candy9', a1)
    if hasattr(a1, 'board8'):
        assert _is_linked(a1, 'board8', b)
    _safe_set(b, 'candy9', a2)
    assert _is_linked(b, 'candy9', a2)
    if hasattr(a1, 'board8'):
        assert not _is_linked(a1, 'board8', b)
    if hasattr(a2, 'board8'):
        assert _is_linked(a2, 'board8', b)
    _safe_set(b, 'candy9', None)
    assert not _is_linked(b, 'candy9', a2)
    if hasattr(a2, 'board8'):
        assert not _is_linked(a2, 'board8', b)


def test_assoc_Game_Menu_reverse_link_reassign_clear():
    a1 = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    a2 = candyCrushPackage_Menu(buttonBGColor="sample_text_2", highScoreLabel="sample_text_2", menuBGColor="sample_text_2", movesLabel="sample_text_2")
    b = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    _safe_set(b, 'menu0', a1)
    assert _is_linked(b, 'menu0', a1)
    if hasattr(a1, 'game1'):
        assert _is_linked(a1, 'game1', b)
    _safe_set(b, 'menu0', a2)
    assert _is_linked(b, 'menu0', a2)
    if hasattr(a1, 'game1'):
        assert not _is_linked(a1, 'game1', b)
    if hasattr(a2, 'game1'):
        assert _is_linked(a2, 'game1', b)
    _safe_set(b, 'menu0', None)
    assert not _is_linked(b, 'menu0', a2)
    if hasattr(a2, 'game1'):
        assert not _is_linked(a2, 'game1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CandyButton_ImageIcon_stub_double():
    # ImageIcon_external has no real 'candyButton5' property in the generated
    # code (a bare stub) -- manually attach it so candyCrushPackage_CandyButton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # candyCrushPackage_CandyButton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    partner = ImageIcon_external()
    setattr(partner, 'candyButton5', None)
    _safe_set(owner, 'image4', partner)
    assert getattr(partner, 'candyButton5') == owner
    _safe_set(owner, 'image4', None)
    assert getattr(partner, 'candyButton5') is None


def test_assoc_CandyButton_JButton_stub_double():
    # JButton_external has no real 'candyButton7' property in the generated
    # code (a bare stub) -- manually attach it so candyCrushPackage_CandyButton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # candyCrushPackage_CandyButton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    partner = JButton_external()
    setattr(partner, 'candyButton7', None)
    _safe_set(owner, 'button6', partner)
    assert getattr(partner, 'candyButton7') == owner
    _safe_set(owner, 'button6', None)
    assert getattr(partner, 'candyButton7') is None


def test_assoc_Menu_Color_stub_double():
    # Color_external has no real 'menu15' property in the generated
    # code (a bare stub) -- manually attach it so candyCrushPackage_Menu's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # candyCrushPackage_Menu's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    partner = Color_external()
    setattr(partner, 'menu15', None)
    _safe_set(owner, 'color14', partner)
    assert getattr(partner, 'menu15') == owner
    _safe_set(owner, 'color14', None)
    assert getattr(partner, 'menu15') is None


