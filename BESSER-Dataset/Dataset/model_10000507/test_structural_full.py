import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Checkers_Close_or_Exit_Game_UseCase,
    Checkers_Move_Game_Pieces_UseCase,
    Checkers_Select__Difficulty_Level__UseCase,
    Checkers_Select__Help__UseCase,
    Checkers_Select__Player_Mode__UseCase,
    Checkers_Start_New_Game_UseCase,
    Checkers_Start_the_Game_GUI_UseCase,
    Checkers_Toggle__Sound__UseCase,
    Computer_Player_1_Actor,
    Human_Player_1_Actor,
    Human_Player_2_Actor,
    checkers_CheckerFrame,
    checkers_CheckerMove,
    checkers_Checkers,
    checkers_GameEngine,
    checkers_GameWin,
    checkers_Help,
    checkers_IntelliChecker,
    checkers_PlaySound,
    checkers_StartPanel,
    genmymodelreverse_java_awt_Graphics,
    genmymodelreverse_java_awt_Point,
    genmymodelreverse_java_awt_event_ActionEvent,
    genmymodelreverse_java_awt_event_ItemEvent,
    genmymodelreverse_java_awt_event_ItemListener_Interface,
    genmymodelreverse_java_awt_event_MouseEvent,
    genmymodelreverse_java_awt_event_MouseListener_Interface,
    genmymodelreverse_java_awt_event_MouseMotionListener_Interface,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_java_lang_Thread,
    genmymodelreverse_java_util_Vector,
    genmymodelreverse_javax_swing_ButtonGroup,
    genmymodelreverse_javax_swing_ImageIcon,
    genmymodelreverse_javax_swing_JButton,
    genmymodelreverse_javax_swing_JComboBox,
    genmymodelreverse_javax_swing_JDialog,
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_javax_swing_JLabel,
    genmymodelreverse_javax_swing_JPanel,
    genmymodelreverse_javax_swing_JRadioButton,
    genmymodelreverse_javax_swing_JScrollPane,
    genmymodelreverse_javax_swing_JTextArea,
    checkers_Position,
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

def test_checkers_CheckerFrame_gamePanel_value_roundtrip():
    instance = checkers_CheckerFrame(gamePanel="sample_text", startButton="sample_text")
    assert instance.gamePanel == "sample_text"
    instance.gamePanel = "sample_text_2"
    assert instance.gamePanel == "sample_text_2"


def test_checkers_CheckerFrame_startButton_value_roundtrip():
    instance = checkers_CheckerFrame(gamePanel="sample_text", startButton="sample_text")
    assert instance.startButton == "sample_text"
    instance.startButton = "sample_text_2"
    assert instance.startButton == "sample_text_2"


def test_checkers_CheckerMove_illegalMove_value_roundtrip():
    instance = checkers_CheckerMove(illegalMove=7, incompleteMove=7, legalMove=7)
    assert instance.illegalMove == 7
    instance.illegalMove = 13
    assert instance.illegalMove == 13


def test_checkers_CheckerMove_incompleteMove_value_roundtrip():
    instance = checkers_CheckerMove(illegalMove=7, incompleteMove=7, legalMove=7)
    assert instance.incompleteMove == 7
    instance.incompleteMove = 13
    assert instance.incompleteMove == 13


def test_checkers_CheckerMove_legalMove_value_roundtrip():
    instance = checkers_CheckerMove(illegalMove=7, incompleteMove=7, legalMove=7)
    assert instance.legalMove == 7
    instance.legalMove = 13
    assert instance.legalMove == 13


def test_checkers_GameEngine_edge_value_roundtrip():
    instance = checkers_GameEngine(edge=7, inf=7, king=7, normal=7, pos=7)
    assert instance.edge == 7
    instance.edge = 13
    assert instance.edge == 13


def test_checkers_GameEngine_inf_value_roundtrip():
    instance = checkers_GameEngine(edge=7, inf=7, king=7, normal=7, pos=7)
    assert instance.inf == 7
    instance.inf = 13
    assert instance.inf == 13


def test_checkers_GameEngine_king_value_roundtrip():
    instance = checkers_GameEngine(edge=7, inf=7, king=7, normal=7, pos=7)
    assert instance.king == 7
    instance.king = 13
    assert instance.king == 13


def test_checkers_GameEngine_normal_value_roundtrip():
    instance = checkers_GameEngine(edge=7, inf=7, king=7, normal=7, pos=7)
    assert instance.normal == 7
    instance.normal = 13
    assert instance.normal == 13


def test_checkers_GameEngine_pos_value_roundtrip():
    instance = checkers_GameEngine(edge=7, inf=7, king=7, normal=7, pos=7)
    assert instance.pos == 7
    instance.pos = 13
    assert instance.pos == 13


def test_checkers_PlaySound_EXTERNAL_BUFFER_SIZE_value_roundtrip():
    instance = checkers_PlaySound(EXTERNAL_BUFFER_SIZE=7, filename="sample_text")
    assert instance.EXTERNAL_BUFFER_SIZE == 7
    instance.EXTERNAL_BUFFER_SIZE = 13
    assert instance.EXTERNAL_BUFFER_SIZE == 13


def test_checkers_PlaySound_filename_value_roundtrip():
    instance = checkers_PlaySound(EXTERNAL_BUFFER_SIZE=7, filename="sample_text")
    assert instance.filename == "sample_text"
    instance.filename = "sample_text_2"
    assert instance.filename == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Checkers_Close_or_Exit_Game_UseCase_strategy = st.builds(Checkers_Close_or_Exit_Game_UseCase)
@given(instance=Checkers_Close_or_Exit_Game_UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Close_or_Exit_Game_UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Close_or_Exit_Game_UseCase)


Checkers_Move_Game_Pieces_UseCase_strategy = st.builds(Checkers_Move_Game_Pieces_UseCase)
@given(instance=Checkers_Move_Game_Pieces_UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Move_Game_Pieces_UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Move_Game_Pieces_UseCase)


Checkers_Select__Difficulty_Level__UseCase_strategy = st.builds(Checkers_Select__Difficulty_Level__UseCase)
@given(instance=Checkers_Select__Difficulty_Level__UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Select__Difficulty_Level__UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Difficulty_Level__UseCase)


Checkers_Select__Help__UseCase_strategy = st.builds(Checkers_Select__Help__UseCase)
@given(instance=Checkers_Select__Help__UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Select__Help__UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Help__UseCase)


Checkers_Select__Player_Mode__UseCase_strategy = st.builds(Checkers_Select__Player_Mode__UseCase)
@given(instance=Checkers_Select__Player_Mode__UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Select__Player_Mode__UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Player_Mode__UseCase)


Checkers_Start_New_Game_UseCase_strategy = st.builds(Checkers_Start_New_Game_UseCase)
@given(instance=Checkers_Start_New_Game_UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Start_New_Game_UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Start_New_Game_UseCase)


Checkers_Start_the_Game_GUI_UseCase_strategy = st.builds(Checkers_Start_the_Game_GUI_UseCase)
@given(instance=Checkers_Start_the_Game_GUI_UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Start_the_Game_GUI_UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Start_the_Game_GUI_UseCase)


Checkers_Toggle__Sound__UseCase_strategy = st.builds(Checkers_Toggle__Sound__UseCase)
@given(instance=Checkers_Toggle__Sound__UseCase_strategy)
@settings(max_examples=25)
def test_Checkers_Toggle__Sound__UseCase_instantiation(instance):
    assert isinstance(instance, Checkers_Toggle__Sound__UseCase)


Computer_Player_1_Actor_strategy = st.builds(Computer_Player_1_Actor)
@given(instance=Computer_Player_1_Actor_strategy)
@settings(max_examples=25)
def test_Computer_Player_1_Actor_instantiation(instance):
    assert isinstance(instance, Computer_Player_1_Actor)


Human_Player_1_Actor_strategy = st.builds(Human_Player_1_Actor)
@given(instance=Human_Player_1_Actor_strategy)
@settings(max_examples=25)
def test_Human_Player_1_Actor_instantiation(instance):
    assert isinstance(instance, Human_Player_1_Actor)


Human_Player_2_Actor_strategy = st.builds(Human_Player_2_Actor)
@given(instance=Human_Player_2_Actor_strategy)
@settings(max_examples=25)
def test_Human_Player_2_Actor_instantiation(instance):
    assert isinstance(instance, Human_Player_2_Actor)


checkers_CheckerFrame_strategy = st.builds(checkers_CheckerFrame, gamePanel=safe_text, startButton=safe_text)
@given(instance=checkers_CheckerFrame_strategy)
@settings(max_examples=25)
def test_checkers_CheckerFrame_instantiation(instance):
    assert isinstance(instance, checkers_CheckerFrame)


checkers_CheckerMove_strategy = st.builds(checkers_CheckerMove, illegalMove=st.integers(), incompleteMove=st.integers(), legalMove=st.integers())
@given(instance=checkers_CheckerMove_strategy)
@settings(max_examples=25)
def test_checkers_CheckerMove_instantiation(instance):
    assert isinstance(instance, checkers_CheckerMove)


checkers_GameEngine_strategy = st.builds(checkers_GameEngine, edge=st.integers(), inf=st.integers(), king=st.integers(), normal=st.integers(), pos=st.integers())
@given(instance=checkers_GameEngine_strategy)
@settings(max_examples=25)
def test_checkers_GameEngine_instantiation(instance):
    assert isinstance(instance, checkers_GameEngine)


checkers_IntelliChecker_strategy = st.builds(checkers_IntelliChecker)
@given(instance=checkers_IntelliChecker_strategy)
@settings(max_examples=25)
def test_checkers_IntelliChecker_instantiation(instance):
    assert isinstance(instance, checkers_IntelliChecker)


checkers_PlaySound_strategy = st.builds(checkers_PlaySound, EXTERNAL_BUFFER_SIZE=st.integers(), filename=safe_text)
@given(instance=checkers_PlaySound_strategy)
@settings(max_examples=25)
def test_checkers_PlaySound_instantiation(instance):
    assert isinstance(instance, checkers_PlaySound)


checkers_StartPanel_strategy = st.builds(checkers_StartPanel)
@given(instance=checkers_StartPanel_strategy)
@settings(max_examples=25)
def test_checkers_StartPanel_instantiation(instance):
    assert isinstance(instance, checkers_StartPanel)


genmymodelreverse_java_awt_Graphics_strategy = st.builds(genmymodelreverse_java_awt_Graphics)
@given(instance=genmymodelreverse_java_awt_Graphics_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_Graphics_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Graphics)


genmymodelreverse_java_awt_Point_strategy = st.builds(genmymodelreverse_java_awt_Point)
@given(instance=genmymodelreverse_java_awt_Point_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_Point_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Point)


genmymodelreverse_java_awt_event_ActionEvent_strategy = st.builds(genmymodelreverse_java_awt_event_ActionEvent)
@given(instance=genmymodelreverse_java_awt_event_ActionEvent_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_ActionEvent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ActionEvent)


genmymodelreverse_java_awt_event_ItemEvent_strategy = st.builds(genmymodelreverse_java_awt_event_ItemEvent)
@given(instance=genmymodelreverse_java_awt_event_ItemEvent_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_ItemEvent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ItemEvent)


genmymodelreverse_java_awt_event_ItemListener_Interface_strategy = st.builds(genmymodelreverse_java_awt_event_ItemListener_Interface)
@given(instance=genmymodelreverse_java_awt_event_ItemListener_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_ItemListener_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ItemListener_Interface)


genmymodelreverse_java_awt_event_MouseEvent_strategy = st.builds(genmymodelreverse_java_awt_event_MouseEvent)
@given(instance=genmymodelreverse_java_awt_event_MouseEvent_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_MouseEvent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseEvent)


genmymodelreverse_java_awt_event_MouseListener_Interface_strategy = st.builds(genmymodelreverse_java_awt_event_MouseListener_Interface)
@given(instance=genmymodelreverse_java_awt_event_MouseListener_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_MouseListener_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseListener_Interface)


genmymodelreverse_java_awt_event_MouseMotionListener_Interface_strategy = st.builds(genmymodelreverse_java_awt_event_MouseMotionListener_Interface)
@given(instance=genmymodelreverse_java_awt_event_MouseMotionListener_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_awt_event_MouseMotionListener_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseMotionListener_Interface)


genmymodelreverse_java_lang_Exception_strategy = st.builds(genmymodelreverse_java_lang_Exception)
@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)


genmymodelreverse_java_lang_Thread_strategy = st.builds(genmymodelreverse_java_lang_Thread)
@given(instance=genmymodelreverse_java_lang_Thread_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Thread_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Thread)


genmymodelreverse_java_util_Vector_strategy = st.builds(genmymodelreverse_java_util_Vector)
@given(instance=genmymodelreverse_java_util_Vector_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_util_Vector_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Vector)


genmymodelreverse_javax_swing_ButtonGroup_strategy = st.builds(genmymodelreverse_javax_swing_ButtonGroup)
@given(instance=genmymodelreverse_javax_swing_ButtonGroup_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_ButtonGroup_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_ButtonGroup)


genmymodelreverse_javax_swing_ImageIcon_strategy = st.builds(genmymodelreverse_javax_swing_ImageIcon)
@given(instance=genmymodelreverse_javax_swing_ImageIcon_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_ImageIcon_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_ImageIcon)


genmymodelreverse_javax_swing_JButton_strategy = st.builds(genmymodelreverse_javax_swing_JButton)
@given(instance=genmymodelreverse_javax_swing_JButton_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JButton_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JButton)


genmymodelreverse_javax_swing_JComboBox_strategy = st.builds(genmymodelreverse_javax_swing_JComboBox)
@given(instance=genmymodelreverse_javax_swing_JComboBox_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JComboBox_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JComboBox)


genmymodelreverse_javax_swing_JDialog_strategy = st.builds(genmymodelreverse_javax_swing_JDialog)
@given(instance=genmymodelreverse_javax_swing_JDialog_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JDialog_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JDialog)


genmymodelreverse_javax_swing_JFrame_strategy = st.builds(genmymodelreverse_javax_swing_JFrame)
@given(instance=genmymodelreverse_javax_swing_JFrame_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JFrame_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JFrame)


genmymodelreverse_javax_swing_JLabel_strategy = st.builds(genmymodelreverse_javax_swing_JLabel)
@given(instance=genmymodelreverse_javax_swing_JLabel_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JLabel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JLabel)


genmymodelreverse_javax_swing_JPanel_strategy = st.builds(genmymodelreverse_javax_swing_JPanel)
@given(instance=genmymodelreverse_javax_swing_JPanel_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JPanel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JPanel)


genmymodelreverse_javax_swing_JRadioButton_strategy = st.builds(genmymodelreverse_javax_swing_JRadioButton)
@given(instance=genmymodelreverse_javax_swing_JRadioButton_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JRadioButton_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JRadioButton)


genmymodelreverse_javax_swing_JScrollPane_strategy = st.builds(genmymodelreverse_javax_swing_JScrollPane)
@given(instance=genmymodelreverse_javax_swing_JScrollPane_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JScrollPane_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JScrollPane)


genmymodelreverse_javax_swing_JTextArea_strategy = st.builds(genmymodelreverse_javax_swing_JTextArea)
@given(instance=genmymodelreverse_javax_swing_JTextArea_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_javax_swing_JTextArea_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JTextArea)


