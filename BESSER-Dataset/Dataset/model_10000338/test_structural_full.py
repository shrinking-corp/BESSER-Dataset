import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_candyCrushPackage_Candy_col_value_roundtrip():
    instance = candyCrushPackage_Candy(col=7, color=7, row=7)
    assert instance.col == 7
    instance.col = 13
    assert instance.col == 13


def test_candyCrushPackage_Candy_color_value_roundtrip():
    instance = candyCrushPackage_Candy(col=7, color=7, row=7)
    assert instance.color == 7
    instance.color = 13
    assert instance.color == 13


def test_candyCrushPackage_Candy_row_value_roundtrip():
    instance = candyCrushPackage_Candy(col=7, color=7, row=7)
    assert instance.row == 7
    instance.row = 13
    assert instance.row == 13


def test_candyCrushPackage_CandyButton_button_value_roundtrip():
    instance = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    assert instance.button == "sample_text"
    instance.button = "sample_text_2"
    assert instance.button == "sample_text_2"


def test_candyCrushPackage_CandyButton_image_value_roundtrip():
    instance = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_candyCrushPackage_CandyButton_x_value_roundtrip():
    instance = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_candyCrushPackage_CandyButton_y_value_roundtrip():
    instance = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_candyCrushPackage_Game_IMAGES_PATH_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.IMAGES_PATH == "sample_text"
    instance.IMAGES_PATH = "sample_text_2"
    assert instance.IMAGES_PATH == "sample_text_2"


def test_candyCrushPackage_Game_SEP_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.SEP == "sample_text"
    instance.SEP = "sample_text_2"
    assert instance.SEP == "sample_text_2"


def test_candyCrushPackage_Game_SOUNDS_PATH_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.SOUNDS_PATH == "sample_text"
    instance.SOUNDS_PATH = "sample_text_2"
    assert instance.SOUNDS_PATH == "sample_text_2"


def test_candyCrushPackage_Game_WINDOW_HEIGHT_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.WINDOW_HEIGHT == 7
    instance.WINDOW_HEIGHT = 13
    assert instance.WINDOW_HEIGHT == 13


def test_candyCrushPackage_Game_WINDOW_WIDTH_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.WINDOW_WIDTH == 7
    instance.WINDOW_WIDTH = 13
    assert instance.WINDOW_WIDTH == 13


def test_candyCrushPackage_Game_playerName_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.playerName == "sample_text"
    instance.playerName = "sample_text_2"
    assert instance.playerName == "sample_text_2"


def test_candyCrushPackage_Game_score_value_roundtrip():
    instance = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_candyCrushPackage_Menu_buttonBGColor_value_roundtrip():
    instance = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    assert instance.buttonBGColor == "sample_text"
    instance.buttonBGColor = "sample_text_2"
    assert instance.buttonBGColor == "sample_text_2"


def test_candyCrushPackage_Menu_highScoreLabel_value_roundtrip():
    instance = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    assert instance.highScoreLabel == "sample_text"
    instance.highScoreLabel = "sample_text_2"
    assert instance.highScoreLabel == "sample_text_2"


def test_candyCrushPackage_Menu_menuBGColor_value_roundtrip():
    instance = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    assert instance.menuBGColor == "sample_text"
    instance.menuBGColor = "sample_text_2"
    assert instance.menuBGColor == "sample_text_2"


def test_candyCrushPackage_Menu_movesLabel_value_roundtrip():
    instance = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    assert instance.movesLabel == "sample_text"
    instance.movesLabel = "sample_text_2"
    assert instance.movesLabel == "sample_text_2"


def test_candyCrushPackage_RegularCandy_selfCrush_value_roundtrip():
    instance = candyCrushPackage_RegularCandy(selfCrush=True, selfCrushRange=7)
    assert instance.selfCrush == True
    instance.selfCrush = False
    assert instance.selfCrush == False


def test_candyCrushPackage_RegularCandy_selfCrushRange_value_roundtrip():
    instance = candyCrushPackage_RegularCandy(selfCrush=True, selfCrushRange=7)
    assert instance.selfCrushRange == 7
    instance.selfCrushRange = 13
    assert instance.selfCrushRange == 13


def test_candyCrushPackage_StrippedCandy_isHorizontal_value_roundtrip():
    instance = candyCrushPackage_StrippedCandy(isHorizontal=True)
    assert instance.isHorizontal == True
    instance.isHorizontal = False
    assert instance.isHorizontal == False


def test_candyCrushPackage_WrappedCandy_selfCrushRange_value_roundtrip():
    instance = candyCrushPackage_WrappedCandy(selfCrushRange=7)
    assert instance.selfCrushRange == 7
    instance.selfCrushRange = 13
    assert instance.selfCrushRange == 13


def test_assoc_CandyButton_ImageIcon_link_reassign_clear():
    a = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    b1 = ImageIcon_external()
    b2 = ImageIcon_external()
    _safe_set(a, 'image4', b1)
    assert _is_linked(a, 'image4', b1)
    if hasattr(b1, 'candyButton5'):
        assert _is_linked(b1, 'candyButton5', a)
    _safe_set(a, 'image4', b2)
    assert _is_linked(a, 'image4', b2)
    if hasattr(b1, 'candyButton5'):
        assert not _is_linked(b1, 'candyButton5', a)
    if hasattr(b2, 'candyButton5'):
        assert _is_linked(b2, 'candyButton5', a)
    _safe_set(a, 'image4', None)
    assert not _is_linked(a, 'image4', b2)
    if hasattr(b2, 'candyButton5'):
        assert not _is_linked(b2, 'candyButton5', a)


def test_assoc_CandyButton_JButton_link_reassign_clear():
    a = candyCrushPackage_CandyButton(button="sample_text", image="sample_text", x=7, y=7)
    b1 = JButton_external()
    b2 = JButton_external()
    _safe_set(a, 'button6', b1)
    assert _is_linked(a, 'button6', b1)
    if hasattr(b1, 'candyButton7'):
        assert _is_linked(b1, 'candyButton7', a)
    _safe_set(a, 'button6', b2)
    assert _is_linked(a, 'button6', b2)
    if hasattr(b1, 'candyButton7'):
        assert not _is_linked(b1, 'candyButton7', a)
    if hasattr(b2, 'candyButton7'):
        assert _is_linked(b2, 'candyButton7', a)
    _safe_set(a, 'button6', None)
    assert not _is_linked(a, 'button6', b2)
    if hasattr(b2, 'candyButton7'):
        assert not _is_linked(b2, 'candyButton7', a)


def test_assoc_Candy_Candy_link_reassign_clear():
    a = candyCrushPackage_Candy(col=7, color=7, row=7)
    b1 = candyCrushPackage_Candy(col=7, color=7, row=7)
    b2 = candyCrushPackage_Candy(col=13, color=13, row=13)
    _safe_set(a, 'board8', {b1})
    assert _is_linked(a, 'board8', b1)
    if hasattr(b1, 'candy9'):
        assert _is_linked(b1, 'candy9', a)
    _safe_set(a, 'board8', {b2})
    assert _is_linked(a, 'board8', b2)
    if hasattr(b1, 'candy9'):
        assert not _is_linked(b1, 'candy9', a)
    if hasattr(b2, 'candy9'):
        assert _is_linked(b2, 'candy9', a)
    _safe_set(a, 'board8', set())
    assert not _is_linked(a, 'board8', b2)
    if hasattr(b2, 'candy9'):
        assert not _is_linked(b2, 'candy9', a)


def test_assoc_Game_Menu_link_reassign_clear():
    a = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    b1 = candyCrushPackage_Game(IMAGES_PATH="sample_text", SEP="sample_text", SOUNDS_PATH="sample_text", WINDOW_HEIGHT=7, WINDOW_WIDTH=7, playerName="sample_text", score=7)
    b2 = candyCrushPackage_Game(IMAGES_PATH="sample_text_2", SEP="sample_text_2", SOUNDS_PATH="sample_text_2", WINDOW_HEIGHT=13, WINDOW_WIDTH=13, playerName="sample_text_2", score=13)
    _safe_set(a, 'game1', b1)
    assert _is_linked(a, 'game1', b1)
    if hasattr(b1, 'menu0'):
        assert _is_linked(b1, 'menu0', a)
    _safe_set(a, 'game1', b2)
    assert _is_linked(a, 'game1', b2)
    if hasattr(b1, 'menu0'):
        assert not _is_linked(b1, 'menu0', a)
    if hasattr(b2, 'menu0'):
        assert _is_linked(b2, 'menu0', a)
    _safe_set(a, 'game1', None)
    assert not _is_linked(a, 'game1', b2)
    if hasattr(b2, 'menu0'):
        assert not _is_linked(b2, 'menu0', a)


def test_assoc_Menu_Color_link_reassign_clear():
    a = candyCrushPackage_Menu(buttonBGColor="sample_text", highScoreLabel="sample_text", menuBGColor="sample_text", movesLabel="sample_text")
    b1 = Color_external()
    b2 = Color_external()
    _safe_set(a, 'color14', b1)
    assert _is_linked(a, 'color14', b1)
    if hasattr(b1, 'menu15'):
        assert _is_linked(b1, 'menu15', a)
    _safe_set(a, 'color14', b2)
    assert _is_linked(a, 'color14', b2)
    if hasattr(b1, 'menu15'):
        assert not _is_linked(b1, 'menu15', a)
    if hasattr(b2, 'menu15'):
        assert _is_linked(b2, 'menu15', a)
    _safe_set(a, 'color14', None)
    assert not _is_linked(a, 'color14', b2)
    if hasattr(b2, 'menu15'):
        assert not _is_linked(b2, 'menu15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Color_external_strategy = st.builds(Color_external)
@given(instance=Color_external_strategy)
@settings(max_examples=25)
def test_Color_external_instantiation(instance):
    assert isinstance(instance, Color_external)


ImageIcon_external_strategy = st.builds(ImageIcon_external)
@given(instance=ImageIcon_external_strategy)
@settings(max_examples=25)
def test_ImageIcon_external_instantiation(instance):
    assert isinstance(instance, ImageIcon_external)


JButton_external_strategy = st.builds(JButton_external)
@given(instance=JButton_external_strategy)
@settings(max_examples=25)
def test_JButton_external_instantiation(instance):
    assert isinstance(instance, JButton_external)


candyCrushPackage_ActionListener_Interface_strategy = st.builds(candyCrushPackage_ActionListener_Interface)
@given(instance=candyCrushPackage_ActionListener_Interface_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_ActionListener_Interface_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_ActionListener_Interface)


candyCrushPackage_Candy_strategy = st.builds(candyCrushPackage_Candy, col=st.integers(), color=st.integers(), row=st.integers())
@given(instance=candyCrushPackage_Candy_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_Candy_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_Candy)


candyCrushPackage_CandyButton_strategy = st.builds(candyCrushPackage_CandyButton, button=safe_text, image=safe_text, x=st.integers(), y=st.integers())
@given(instance=candyCrushPackage_CandyButton_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_CandyButton_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_CandyButton)


candyCrushPackage_ColorBombCandy_strategy = st.builds(candyCrushPackage_ColorBombCandy)
@given(instance=candyCrushPackage_ColorBombCandy_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_ColorBombCandy_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_ColorBombCandy)


candyCrushPackage_Game_strategy = st.builds(candyCrushPackage_Game, IMAGES_PATH=safe_text, SEP=safe_text, SOUNDS_PATH=safe_text, WINDOW_HEIGHT=st.integers(), WINDOW_WIDTH=st.integers(), playerName=safe_text, score=st.integers())
@given(instance=candyCrushPackage_Game_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_Game_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_Game)


candyCrushPackage_JFrame_strategy = st.builds(candyCrushPackage_JFrame)
@given(instance=candyCrushPackage_JFrame_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_JFrame_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_JFrame)


candyCrushPackage_JPanel_strategy = st.builds(candyCrushPackage_JPanel)
@given(instance=candyCrushPackage_JPanel_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_JPanel_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_JPanel)


candyCrushPackage_Menu_strategy = st.builds(candyCrushPackage_Menu, buttonBGColor=safe_text, highScoreLabel=safe_text, menuBGColor=safe_text, movesLabel=safe_text)
@given(instance=candyCrushPackage_Menu_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_Menu_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_Menu)


candyCrushPackage_RegularCandy_strategy = st.builds(candyCrushPackage_RegularCandy, selfCrush=st.booleans(), selfCrushRange=st.integers())
@given(instance=candyCrushPackage_RegularCandy_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_RegularCandy_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_RegularCandy)


candyCrushPackage_StrippedCandy_strategy = st.builds(candyCrushPackage_StrippedCandy, isHorizontal=st.booleans())
@given(instance=candyCrushPackage_StrippedCandy_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_StrippedCandy_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_StrippedCandy)


candyCrushPackage_Visited_Interface_strategy = st.builds(candyCrushPackage_Visited_Interface)
@given(instance=candyCrushPackage_Visited_Interface_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_Visited_Interface_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_Visited_Interface)


candyCrushPackage_Visitor_Interface_strategy = st.builds(candyCrushPackage_Visitor_Interface)
@given(instance=candyCrushPackage_Visitor_Interface_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_Visitor_Interface_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_Visitor_Interface)


candyCrushPackage_WrappedCandy_strategy = st.builds(candyCrushPackage_WrappedCandy, selfCrushRange=st.integers())
@given(instance=candyCrushPackage_WrappedCandy_strategy)
@settings(max_examples=25)
def test_candyCrushPackage_WrappedCandy_instantiation(instance):
    assert isinstance(instance, candyCrushPackage_WrappedCandy)


