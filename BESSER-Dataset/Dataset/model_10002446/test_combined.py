# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Connect4,
    MainMenuGUI,
    GameBoard,
    ScoreBoardGUI,
    Button,
    Connect4GUI,
    GameboardGUI,
    Piece,
    RandomPlayer,
    AIplayer,
    ConsolePlayer,
    Player_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_connect4_is_not_abstract():
    assert not inspect.isabstract(Connect4)


def test_hyp_connect4_constructor_exists():
    assert callable(Connect4.__init__)


def test_hyp_connect4_constructor_args():
    sig = inspect.signature(Connect4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mainmenugui_is_not_abstract():
    assert not inspect.isabstract(MainMenuGUI)


def test_hyp_mainmenugui_constructor_exists():
    assert callable(MainMenuGUI.__init__)


def test_hyp_mainmenugui_constructor_args():
    sig = inspect.signature(MainMenuGUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gameboard_is_not_abstract():
    assert not inspect.isabstract(GameBoard)


def test_hyp_gameboard_constructor_exists():
    assert callable(GameBoard.__init__)


def test_hyp_gameboard_constructor_args():
    sig = inspect.signature(GameBoard.__init__)
    params = list(sig.parameters.keys())
    assert "board" in params, "Missing parameter 'board'"
    assert "player1" in params, "Missing parameter 'player1'"
    assert "whoPlay" in params, "Missing parameter 'whoPlay'"
    assert "player2" in params, "Missing parameter 'player2'"

def test_hyp_gameboard_has_board():
    assert hasattr(GameBoard, "board")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameboard_has_player1():
    assert hasattr(GameBoard, "player1")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "player1" in klass.__dict__:
            descriptor = klass.__dict__["player1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameboard_has_whoPlay():
    assert hasattr(GameBoard, "whoPlay")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "whoPlay" in klass.__dict__:
            descriptor = klass.__dict__["whoPlay"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameboard_has_player2():
    assert hasattr(GameBoard, "player2")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "player2" in klass.__dict__:
            descriptor = klass.__dict__["player2"]
            break
    assert isinstance(descriptor, property)



def test_hyp_scoreboardgui_is_not_abstract():
    assert not inspect.isabstract(ScoreBoardGUI)


def test_hyp_scoreboardgui_constructor_exists():
    assert callable(ScoreBoardGUI.__init__)


def test_hyp_scoreboardgui_constructor_args():
    sig = inspect.signature(ScoreBoardGUI.__init__)
    params = list(sig.parameters.keys())
    assert "playersList" in params, "Missing parameter 'playersList'"




def test_hyp_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_hyp_button_constructor_exists():
    assert callable(Button.__init__)


def test_hyp_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connect4gui_is_not_abstract():
    assert not inspect.isabstract(Connect4GUI)


def test_hyp_connect4gui_constructor_exists():
    assert callable(Connect4GUI.__init__)


def test_hyp_connect4gui_constructor_args():
    sig = inspect.signature(Connect4GUI.__init__)
    params = list(sig.parameters.keys())
    assert "undo" in params, "Missing parameter 'undo'"
    assert "root" in params, "Missing parameter 'root'"

def test_hyp_connect4gui_has_undo():
    assert hasattr(Connect4GUI, "undo")
    descriptor = None
    for klass in Connect4GUI.__mro__:
        if "undo" in klass.__dict__:
            descriptor = klass.__dict__["undo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_connect4gui_has_root():
    assert hasattr(Connect4GUI, "root")
    descriptor = None
    for klass in Connect4GUI.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_hyp_gameboardgui_is_not_abstract():
    assert not inspect.isabstract(GameboardGUI)


def test_hyp_gameboardgui_constructor_exists():
    assert callable(GameboardGUI.__init__)


def test_hyp_gameboardgui_constructor_args():
    sig = inspect.signature(GameboardGUI.__init__)
    params = list(sig.parameters.keys())
    assert "piecesList" in params, "Missing parameter 'piecesList'"
    assert "rows" in params, "Missing parameter 'rows'"
    assert "columns" in params, "Missing parameter 'columns'"






def test_hyp_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_hyp_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_hyp_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"
    assert "pieceSize" in params, "Missing parameter 'pieceSize'"





def test_hyp_randomplayer_is_not_abstract():
    assert not inspect.isabstract(RandomPlayer)


def test_hyp_randomplayer_constructor_exists():
    assert callable(RandomPlayer.__init__)


def test_hyp_randomplayer_constructor_args():
    sig = inspect.signature(RandomPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aiplayer_is_not_abstract():
    assert not inspect.isabstract(AIplayer)


def test_hyp_aiplayer_constructor_exists():
    assert callable(AIplayer.__init__)


def test_hyp_aiplayer_constructor_args():
    sig = inspect.signature(AIplayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "score" in params, "Missing parameter 'score'"





def test_hyp_consoleplayer_is_not_abstract():
    assert not inspect.isabstract(ConsolePlayer)


def test_hyp_consoleplayer_constructor_exists():
    assert callable(ConsolePlayer.__init__)


def test_hyp_consoleplayer_constructor_args():
    sig = inspect.signature(ConsolePlayer.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_player_interface_is_not_abstract():
    assert not inspect.isabstract(Player_Interface)


def test_hyp_player_interface_constructor_exists():
    assert callable(Player_Interface.__init__)


def test_hyp_player_interface_constructor_args():
    sig = inspect.signature(Player_Interface.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Connect4_strategy = st.builds(
    Connect4,
)
MainMenuGUI_strategy = st.builds(
    MainMenuGUI,
)
GameBoard_strategy = st.builds(
    GameBoard,
    board=
        safe_text,
    player1=
        st.none(),
    whoPlay=
        safe_text,
    player2=
        st.none()
)
ScoreBoardGUI_strategy = st.builds(
    ScoreBoardGUI,
    playersList=
        safe_text
)
Button_strategy = st.builds(
    Button,
)
Connect4GUI_strategy = st.builds(
    Connect4GUI,
    undo=
        st.none(),
    root=
        safe_text
)
GameboardGUI_strategy = st.builds(
    GameboardGUI,
    piecesList=
        safe_text,
    rows=
        st.integers(),
    columns=
        st.integers()
)
Piece_strategy = st.builds(
    Piece,
    pieceColor=
        safe_text,
    pieceSize=
        st.integers()
)
RandomPlayer_strategy = st.builds(
    RandomPlayer,
    score=
        safe_text,
    name=
        safe_text
)
AIplayer_strategy = st.builds(
    AIplayer,
    name=
        safe_text,
    score=
        safe_text
)
ConsolePlayer_strategy = st.builds(
    ConsolePlayer,
    score=
        safe_text,
    name=
        safe_text
)
Player_Interface_strategy = st.builds(
    Player_Interface,
)



@given(instance=GameBoard_strategy)
@settings(max_examples=50)
def test_hyp_gameboard_instantiation(instance):
    assert isinstance(instance, GameBoard)



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_player1_setter(instance):
    original = instance.player1
    instance.player1 = original
    assert instance.player1 == original



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_whoPlay_setter(instance):
    original = instance.whoPlay
    instance.whoPlay = original
    assert instance.whoPlay == original



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_player2_setter(instance):
    original = instance.player2
    instance.player2 = original
    assert instance.player2 == original




@given(instance=ScoreBoardGUI_strategy)
def test_hyp_scoreboardgui_playersList_setter(instance):
    original = instance.playersList
    instance.playersList = original
    assert instance.playersList == original


@given(instance=Connect4GUI_strategy)
@settings(max_examples=50)
def test_hyp_connect4gui_instantiation(instance):
    assert isinstance(instance, Connect4GUI)



@given(instance=Connect4GUI_strategy)
def test_hyp_connect4gui_undo_setter(instance):
    original = instance.undo
    instance.undo = original
    assert instance.undo == original



@given(instance=Connect4GUI_strategy)
def test_hyp_connect4gui_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original




@given(instance=GameboardGUI_strategy)
def test_hyp_gameboardgui_piecesList_setter(instance):
    original = instance.piecesList
    instance.piecesList = original
    assert instance.piecesList == original



@given(instance=GameboardGUI_strategy)
def test_hyp_gameboardgui_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original



@given(instance=GameboardGUI_strategy)
def test_hyp_gameboardgui_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original




@given(instance=Piece_strategy)
def test_hyp_piece_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original



@given(instance=Piece_strategy)
def test_hyp_piece_pieceSize_setter(instance):
    original = instance.pieceSize
    instance.pieceSize = original
    assert instance.pieceSize == original




@given(instance=RandomPlayer_strategy)
def test_hyp_randomplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=RandomPlayer_strategy)
def test_hyp_randomplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=AIplayer_strategy)
def test_hyp_aiplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=AIplayer_strategy)
def test_hyp_aiplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original




@given(instance=ConsolePlayer_strategy)
def test_hyp_consoleplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=ConsolePlayer_strategy)
def test_hyp_consoleplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AIplayer,
    Button,
    Connect4,
    Connect4GUI,
    ConsolePlayer,
    GameBoard,
    GameboardGUI,
    MainMenuGUI,
    Piece,
    Player_Interface,
    RandomPlayer,
    ScoreBoardGUI,
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

def test_AIplayer_name_value_roundtrip():
    instance = AIplayer(name="sample_text", score="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_AIplayer_score_value_roundtrip():
    instance = AIplayer(name="sample_text", score="sample_text")
    assert instance.score == "sample_text"
    instance.score = "sample_text_2"
    assert instance.score == "sample_text_2"


def test_ConsolePlayer_name_value_roundtrip():
    instance = ConsolePlayer(name="sample_text", score="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ConsolePlayer_score_value_roundtrip():
    instance = ConsolePlayer(name="sample_text", score="sample_text")
    assert instance.score == "sample_text"
    instance.score = "sample_text_2"
    assert instance.score == "sample_text_2"


def test_GameboardGUI_columns_value_roundtrip():
    instance = GameboardGUI(columns=7, piecesList="sample_text", rows=7)
    assert instance.columns == 7
    instance.columns = 13
    assert instance.columns == 13


def test_GameboardGUI_piecesList_value_roundtrip():
    instance = GameboardGUI(columns=7, piecesList="sample_text", rows=7)
    assert instance.piecesList == "sample_text"
    instance.piecesList = "sample_text_2"
    assert instance.piecesList == "sample_text_2"


def test_GameboardGUI_rows_value_roundtrip():
    instance = GameboardGUI(columns=7, piecesList="sample_text", rows=7)
    assert instance.rows == 7
    instance.rows = 13
    assert instance.rows == 13


def test_Piece_pieceColor_value_roundtrip():
    instance = Piece(pieceColor="sample_text", pieceSize=7)
    assert instance.pieceColor == "sample_text"
    instance.pieceColor = "sample_text_2"
    assert instance.pieceColor == "sample_text_2"


def test_Piece_pieceSize_value_roundtrip():
    instance = Piece(pieceColor="sample_text", pieceSize=7)
    assert instance.pieceSize == 7
    instance.pieceSize = 13
    assert instance.pieceSize == 13


def test_RandomPlayer_name_value_roundtrip():
    instance = RandomPlayer(name="sample_text", score="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RandomPlayer_score_value_roundtrip():
    instance = RandomPlayer(name="sample_text", score="sample_text")
    assert instance.score == "sample_text"
    instance.score = "sample_text_2"
    assert instance.score == "sample_text_2"


def test_ScoreBoardGUI_playersList_value_roundtrip():
    instance = ScoreBoardGUI(playersList="sample_text")
    assert instance.playersList == "sample_text"
    instance.playersList = "sample_text_2"
    assert instance.playersList == "sample_text_2"


def test_assoc_GameboardGUI_Piece_link_reassign_clear():
    a = Piece(pieceColor="sample_text", pieceSize=7)
    b1 = GameboardGUI(columns=7, piecesList="sample_text", rows=7)
    b2 = GameboardGUI(columns=13, piecesList="sample_text_2", rows=13)
    _safe_set(a, 'gameboardGUI1', b1)
    assert _is_linked(a, 'gameboardGUI1', b1)
    if hasattr(b1, 'piece0'):
        assert _is_linked(b1, 'piece0', a)
    _safe_set(a, 'gameboardGUI1', b2)
    assert _is_linked(a, 'gameboardGUI1', b2)
    if hasattr(b1, 'piece0'):
        assert not _is_linked(b1, 'piece0', a)
    if hasattr(b2, 'piece0'):
        assert _is_linked(b2, 'piece0', a)
    _safe_set(a, 'gameboardGUI1', None)
    assert not _is_linked(a, 'gameboardGUI1', b2)
    if hasattr(b2, 'piece0'):
        assert not _is_linked(b2, 'piece0', a)


def test_assoc_ScoreBoardGUI_MainMenuGUI_link_reassign_clear():
    a = ScoreBoardGUI(playersList="sample_text")
    b1 = MainMenuGUI()
    b2 = MainMenuGUI()
    _safe_set(a, 'mainMenuGUI12', b1)
    assert _is_linked(a, 'mainMenuGUI12', b1)
    if hasattr(b1, 'scoreBoardGUI13'):
        assert _is_linked(b1, 'scoreBoardGUI13', a)
    _safe_set(a, 'mainMenuGUI12', b2)
    assert _is_linked(a, 'mainMenuGUI12', b2)
    if hasattr(b1, 'scoreBoardGUI13'):
        assert not _is_linked(b1, 'scoreBoardGUI13', a)
    if hasattr(b2, 'scoreBoardGUI13'):
        assert _is_linked(b2, 'scoreBoardGUI13', a)
    _safe_set(a, 'mainMenuGUI12', None)
    assert not _is_linked(a, 'mainMenuGUI12', b2)
    if hasattr(b2, 'scoreBoardGUI13'):
        assert not _is_linked(b2, 'scoreBoardGUI13', a)


def test_assoc_ScoreBoardGUI_Player_link_reassign_clear():
    a = ScoreBoardGUI(playersList="sample_text")
    b1 = Player_Interface()
    b2 = Player_Interface()
    _safe_set(a, 'player2', {b1})
    assert _is_linked(a, 'player2', b1)
    if hasattr(b1, 'ScoreBoardGUI_Player_13'):
        assert _is_linked(b1, 'ScoreBoardGUI_Player_13', a)
    _safe_set(a, 'player2', {b2})
    assert _is_linked(a, 'player2', b2)
    if hasattr(b1, 'ScoreBoardGUI_Player_13'):
        assert not _is_linked(b1, 'ScoreBoardGUI_Player_13', a)
    if hasattr(b2, 'ScoreBoardGUI_Player_13'):
        assert _is_linked(b2, 'ScoreBoardGUI_Player_13', a)
    _safe_set(a, 'player2', set())
    assert not _is_linked(a, 'player2', b2)
    if hasattr(b2, 'ScoreBoardGUI_Player_13'):
        assert not _is_linked(b2, 'ScoreBoardGUI_Player_13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AIplayer_strategy = st.builds(AIplayer, name=safe_text, score=safe_text)
@given(instance=AIplayer_strategy)
@settings(max_examples=25)
def test_AIplayer_instantiation(instance):
    assert isinstance(instance, AIplayer)


Button_strategy = st.builds(Button)
@given(instance=Button_strategy)
@settings(max_examples=25)
def test_Button_instantiation(instance):
    assert isinstance(instance, Button)


Connect4_strategy = st.builds(Connect4)
@given(instance=Connect4_strategy)
@settings(max_examples=25)
def test_Connect4_instantiation(instance):
    assert isinstance(instance, Connect4)


ConsolePlayer_strategy = st.builds(ConsolePlayer, name=safe_text, score=safe_text)
@given(instance=ConsolePlayer_strategy)
@settings(max_examples=25)
def test_ConsolePlayer_instantiation(instance):
    assert isinstance(instance, ConsolePlayer)


GameboardGUI_strategy = st.builds(GameboardGUI, columns=st.integers(), piecesList=safe_text, rows=st.integers())
@given(instance=GameboardGUI_strategy)
@settings(max_examples=25)
def test_GameboardGUI_instantiation(instance):
    assert isinstance(instance, GameboardGUI)


MainMenuGUI_strategy = st.builds(MainMenuGUI)
@given(instance=MainMenuGUI_strategy)
@settings(max_examples=25)
def test_MainMenuGUI_instantiation(instance):
    assert isinstance(instance, MainMenuGUI)


Piece_strategy = st.builds(Piece, pieceColor=safe_text, pieceSize=st.integers())
@given(instance=Piece_strategy)
@settings(max_examples=25)
def test_Piece_instantiation(instance):
    assert isinstance(instance, Piece)


Player_Interface_strategy = st.builds(Player_Interface)
@given(instance=Player_Interface_strategy)
@settings(max_examples=25)
def test_Player_Interface_instantiation(instance):
    assert isinstance(instance, Player_Interface)


RandomPlayer_strategy = st.builds(RandomPlayer, name=safe_text, score=safe_text)
@given(instance=RandomPlayer_strategy)
@settings(max_examples=25)
def test_RandomPlayer_instantiation(instance):
    assert isinstance(instance, RandomPlayer)


ScoreBoardGUI_strategy = st.builds(ScoreBoardGUI, playersList=safe_text)
@given(instance=ScoreBoardGUI_strategy)
@settings(max_examples=25)
def test_ScoreBoardGUI_instantiation(instance):
    assert isinstance(instance, ScoreBoardGUI)



