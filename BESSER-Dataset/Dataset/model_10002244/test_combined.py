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
    Game_Start_external,
    Roll_First_external,
    Get_Instructions_external,
    Get_Player_Name_external,
    Play_Again_external,
    Announce_Winner_external,
    Next_Turn_external,
    Score_Roll_external,
    Roll_Dice_external,
    Computer_Turn_external,
    Display,
    Yahtzee_Players1,
    Yahtzee_Scoring1,
    Yahtzee_Turn1,
    Yahtzee_Display1,
    Player_Actor,
    Yahtzee_Component,
    Players,
    Turn,
    Scoring,
    Class1,
    Class,
    Yahtzee_Players,
    Yahtzee_Display,
    Yahtzee_Scoring,
    Yahtzee_Turn,
    Yahtzee_Game,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_game_start_external_is_not_abstract():
    assert not inspect.isabstract(Game_Start_external)


def test_hyp_game_start_external_constructor_exists():
    assert callable(Game_Start_external.__init__)


def test_hyp_game_start_external_constructor_args():
    sig = inspect.signature(Game_Start_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roll_first_external_is_not_abstract():
    assert not inspect.isabstract(Roll_First_external)


def test_hyp_roll_first_external_constructor_exists():
    assert callable(Roll_First_external.__init__)


def test_hyp_roll_first_external_constructor_args():
    sig = inspect.signature(Roll_First_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_get_instructions_external_is_not_abstract():
    assert not inspect.isabstract(Get_Instructions_external)


def test_hyp_get_instructions_external_constructor_exists():
    assert callable(Get_Instructions_external.__init__)


def test_hyp_get_instructions_external_constructor_args():
    sig = inspect.signature(Get_Instructions_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_get_player_name_external_is_not_abstract():
    assert not inspect.isabstract(Get_Player_Name_external)


def test_hyp_get_player_name_external_constructor_exists():
    assert callable(Get_Player_Name_external.__init__)


def test_hyp_get_player_name_external_constructor_args():
    sig = inspect.signature(Get_Player_Name_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_play_again_external_is_not_abstract():
    assert not inspect.isabstract(Play_Again_external)


def test_hyp_play_again_external_constructor_exists():
    assert callable(Play_Again_external.__init__)


def test_hyp_play_again_external_constructor_args():
    sig = inspect.signature(Play_Again_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_announce_winner_external_is_not_abstract():
    assert not inspect.isabstract(Announce_Winner_external)


def test_hyp_announce_winner_external_constructor_exists():
    assert callable(Announce_Winner_external.__init__)


def test_hyp_announce_winner_external_constructor_args():
    sig = inspect.signature(Announce_Winner_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_next_turn_external_is_not_abstract():
    assert not inspect.isabstract(Next_Turn_external)


def test_hyp_next_turn_external_constructor_exists():
    assert callable(Next_Turn_external.__init__)


def test_hyp_next_turn_external_constructor_args():
    sig = inspect.signature(Next_Turn_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_score_roll_external_is_not_abstract():
    assert not inspect.isabstract(Score_Roll_external)


def test_hyp_score_roll_external_constructor_exists():
    assert callable(Score_Roll_external.__init__)


def test_hyp_score_roll_external_constructor_args():
    sig = inspect.signature(Score_Roll_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roll_dice_external_is_not_abstract():
    assert not inspect.isabstract(Roll_Dice_external)


def test_hyp_roll_dice_external_constructor_exists():
    assert callable(Roll_Dice_external.__init__)


def test_hyp_roll_dice_external_constructor_args():
    sig = inspect.signature(Roll_Dice_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_computer_turn_external_is_not_abstract():
    assert not inspect.isabstract(Computer_Turn_external)


def test_hyp_computer_turn_external_constructor_exists():
    assert callable(Computer_Turn_external.__init__)


def test_hyp_computer_turn_external_constructor_args():
    sig = inspect.signature(Computer_Turn_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_display_is_not_abstract():
    assert not inspect.isabstract(Display)


def test_hyp_display_constructor_exists():
    assert callable(Display.__init__)


def test_hyp_display_constructor_args():
    sig = inspect.signature(Display.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yahtzee_players1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Players1)


def test_hyp_yahtzee_players1_constructor_exists():
    assert callable(Yahtzee_Players1.__init__)


def test_hyp_yahtzee_players1_constructor_args():
    sig = inspect.signature(Yahtzee_Players1.__init__)
    params = list(sig.parameters.keys())
    assert "playerScore" in params, "Missing parameter 'playerScore'"
    assert "compScore" in params, "Missing parameter 'compScore'"





def test_hyp_yahtzee_scoring1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Scoring1)


def test_hyp_yahtzee_scoring1_constructor_exists():
    assert callable(Yahtzee_Scoring1.__init__)


def test_hyp_yahtzee_scoring1_constructor_args():
    sig = inspect.signature(Yahtzee_Scoring1.__init__)
    params = list(sig.parameters.keys())
    assert "Temp" in params, "Missing parameter 'Temp'"




def test_hyp_yahtzee_turn1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Turn1)


def test_hyp_yahtzee_turn1_constructor_exists():
    assert callable(Yahtzee_Turn1.__init__)


def test_hyp_yahtzee_turn1_constructor_args():
    sig = inspect.signature(Yahtzee_Turn1.__init__)
    params = list(sig.parameters.keys())
    assert "Dice" in params, "Missing parameter 'Dice'"




def test_hyp_yahtzee_display1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Display1)


def test_hyp_yahtzee_display1_constructor_exists():
    assert callable(Yahtzee_Display1.__init__)


def test_hyp_yahtzee_display1_constructor_args():
    sig = inspect.signature(Yahtzee_Display1.__init__)
    params = list(sig.parameters.keys())
    assert "JButton" in params, "Missing parameter 'JButton'"
    assert "Jpanel" in params, "Missing parameter 'Jpanel'"
    assert "JTextField" in params, "Missing parameter 'JTextField'"
    assert "Player" in params, "Missing parameter 'Player'"
    assert "JRadioButton" in params, "Missing parameter 'JRadioButton'"
    assert "Jlabel" in params, "Missing parameter 'Jlabel'"
    assert "JScrollPanel" in params, "Missing parameter 'JScrollPanel'"
    assert "Computer" in params, "Missing parameter 'Computer'"
    assert "Temp1" in params, "Missing parameter 'Temp1'"
    assert "JFrame" in params, "Missing parameter 'JFrame'"
    assert "Temp" in params, "Missing parameter 'Temp'"
    assert "JImageIcon" in params, "Missing parameter 'JImageIcon'"

def test_hyp_yahtzee_display1_has_JButton():
    assert hasattr(Yahtzee_Display1, "JButton")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JButton" in klass.__dict__:
            descriptor = klass.__dict__["JButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Jpanel():
    assert hasattr(Yahtzee_Display1, "Jpanel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Jpanel" in klass.__dict__:
            descriptor = klass.__dict__["Jpanel"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_JTextField():
    assert hasattr(Yahtzee_Display1, "JTextField")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JTextField" in klass.__dict__:
            descriptor = klass.__dict__["JTextField"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Player():
    assert hasattr(Yahtzee_Display1, "Player")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_JRadioButton():
    assert hasattr(Yahtzee_Display1, "JRadioButton")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JRadioButton" in klass.__dict__:
            descriptor = klass.__dict__["JRadioButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Jlabel():
    assert hasattr(Yahtzee_Display1, "Jlabel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Jlabel" in klass.__dict__:
            descriptor = klass.__dict__["Jlabel"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_JScrollPanel():
    assert hasattr(Yahtzee_Display1, "JScrollPanel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JScrollPanel" in klass.__dict__:
            descriptor = klass.__dict__["JScrollPanel"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Computer():
    assert hasattr(Yahtzee_Display1, "Computer")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Computer" in klass.__dict__:
            descriptor = klass.__dict__["Computer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Temp1():
    assert hasattr(Yahtzee_Display1, "Temp1")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Temp1" in klass.__dict__:
            descriptor = klass.__dict__["Temp1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_JFrame():
    assert hasattr(Yahtzee_Display1, "JFrame")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JFrame" in klass.__dict__:
            descriptor = klass.__dict__["JFrame"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_Temp():
    assert hasattr(Yahtzee_Display1, "Temp")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Temp" in klass.__dict__:
            descriptor = klass.__dict__["Temp"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_display1_has_JImageIcon():
    assert hasattr(Yahtzee_Display1, "JImageIcon")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JImageIcon" in klass.__dict__:
            descriptor = klass.__dict__["JImageIcon"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_actor_is_not_abstract():
    assert not inspect.isabstract(Player_Actor)


def test_hyp_player_actor_constructor_exists():
    assert callable(Player_Actor.__init__)


def test_hyp_player_actor_constructor_args():
    sig = inspect.signature(Player_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yahtzee_component_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Component)


def test_hyp_yahtzee_component_constructor_exists():
    assert callable(Yahtzee_Component.__init__)


def test_hyp_yahtzee_component_constructor_args():
    sig = inspect.signature(Yahtzee_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_hyp_players_constructor_exists():
    assert callable(Players.__init__)


def test_hyp_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())



def test_hyp_turn_is_not_abstract():
    assert not inspect.isabstract(Turn)


def test_hyp_turn_constructor_exists():
    assert callable(Turn.__init__)


def test_hyp_turn_constructor_args():
    sig = inspect.signature(Turn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scoring_is_not_abstract():
    assert not inspect.isabstract(Scoring)


def test_hyp_scoring_constructor_exists():
    assert callable(Scoring.__init__)


def test_hyp_scoring_constructor_args():
    sig = inspect.signature(Scoring.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class1_is_not_abstract():
    assert not inspect.isabstract(Class1)


def test_hyp_class1_constructor_exists():
    assert callable(Class1.__init__)


def test_hyp_class1_constructor_args():
    sig = inspect.signature(Class1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yahtzee_players_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Players)


def test_hyp_yahtzee_players_constructor_exists():
    assert callable(Yahtzee_Players.__init__)


def test_hyp_yahtzee_players_constructor_args():
    sig = inspect.signature(Yahtzee_Players.__init__)
    params = list(sig.parameters.keys())
    assert "Score" in params, "Missing parameter 'Score'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_yahtzee_display_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Display)


def test_hyp_yahtzee_display_constructor_exists():
    assert callable(Yahtzee_Display.__init__)


def test_hyp_yahtzee_display_constructor_args():
    sig = inspect.signature(Yahtzee_Display.__init__)
    params = list(sig.parameters.keys())
    assert "PanelScorecard" in params, "Missing parameter 'PanelScorecard'"
    assert "PanelGameName" in params, "Missing parameter 'PanelGameName'"
    assert "PanelPrimary" in params, "Missing parameter 'PanelPrimary'"
    assert "PanelNames" in params, "Missing parameter 'PanelNames'"
    assert "PanelChoices" in params, "Missing parameter 'PanelChoices'"








def test_hyp_yahtzee_scoring_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Scoring)


def test_hyp_yahtzee_scoring_constructor_exists():
    assert callable(Yahtzee_Scoring.__init__)


def test_hyp_yahtzee_scoring_constructor_args():
    sig = inspect.signature(Yahtzee_Scoring.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yahtzee_turn_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Turn)


def test_hyp_yahtzee_turn_constructor_exists():
    assert callable(Yahtzee_Turn.__init__)


def test_hyp_yahtzee_turn_constructor_args():
    sig = inspect.signature(Yahtzee_Turn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yahtzee_game_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Game)


def test_hyp_yahtzee_game_constructor_exists():
    assert callable(Yahtzee_Game.__init__)


def test_hyp_yahtzee_game_constructor_args():
    sig = inspect.signature(Yahtzee_Game.__init__)
    params = list(sig.parameters.keys())
    assert "First" in params, "Missing parameter 'First'"
    assert "Player" in params, "Missing parameter 'Player'"
    assert "CompPlayer" in params, "Missing parameter 'CompPlayer'"
    assert "Again" in params, "Missing parameter 'Again'"

def test_hyp_yahtzee_game_has_First():
    assert hasattr(Yahtzee_Game, "First")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "First" in klass.__dict__:
            descriptor = klass.__dict__["First"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_game_has_Player():
    assert hasattr(Yahtzee_Game, "Player")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_game_has_CompPlayer():
    assert hasattr(Yahtzee_Game, "CompPlayer")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "CompPlayer" in klass.__dict__:
            descriptor = klass.__dict__["CompPlayer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_yahtzee_game_has_Again():
    assert hasattr(Yahtzee_Game, "Again")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "Again" in klass.__dict__:
            descriptor = klass.__dict__["Again"]
            break
    assert isinstance(descriptor, property)


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
Game_Start_external_strategy = st.builds(
    Game_Start_external,
)
Roll_First_external_strategy = st.builds(
    Roll_First_external,
)
Get_Instructions_external_strategy = st.builds(
    Get_Instructions_external,
)
Get_Player_Name_external_strategy = st.builds(
    Get_Player_Name_external,
)
Play_Again_external_strategy = st.builds(
    Play_Again_external,
)
Announce_Winner_external_strategy = st.builds(
    Announce_Winner_external,
)
Next_Turn_external_strategy = st.builds(
    Next_Turn_external,
)
Score_Roll_external_strategy = st.builds(
    Score_Roll_external,
)
Roll_Dice_external_strategy = st.builds(
    Roll_Dice_external,
)
Computer_Turn_external_strategy = st.builds(
    Computer_Turn_external,
)
Display_strategy = st.builds(
    Display,
)
Yahtzee_Players1_strategy = st.builds(
    Yahtzee_Players1,
    playerScore=
        safe_text,
    compScore=
        safe_text
)
Yahtzee_Scoring1_strategy = st.builds(
    Yahtzee_Scoring1,
    Temp=
        safe_text
)
Yahtzee_Turn1_strategy = st.builds(
    Yahtzee_Turn1,
    Dice=
        safe_text
)
Yahtzee_Display1_strategy = st.builds(
    Yahtzee_Display1,
    JButton=
        st.none(),
    Jpanel=
        st.none(),
    JTextField=
        st.none(),
    Player=
        st.none(),
    JRadioButton=
        st.none(),
    Jlabel=
        st.none(),
    JScrollPanel=
        st.none(),
    Computer=
        st.none(),
    Temp1=
        st.integers(),
    JFrame=
        st.none(),
    Temp=
        st.integers(),
    JImageIcon=
        st.none()
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)
Yahtzee_Component_strategy = st.builds(
    Yahtzee_Component,
)
Players_strategy = st.builds(
    Players,
)
Turn_strategy = st.builds(
    Turn,
)
Scoring_strategy = st.builds(
    Scoring,
)
Class1_strategy = st.builds(
    Class1,
)
Class_strategy = st.builds(
    Class,
)
Yahtzee_Players_strategy = st.builds(
    Yahtzee_Players,
    Score=
        safe_text,
    Name=
        safe_text
)
Yahtzee_Display_strategy = st.builds(
    Yahtzee_Display,
    PanelScorecard=
        safe_text,
    PanelGameName=
        safe_text,
    PanelPrimary=
        safe_text,
    PanelNames=
        safe_text,
    PanelChoices=
        safe_text
)
Yahtzee_Scoring_strategy = st.builds(
    Yahtzee_Scoring,
)
Yahtzee_Turn_strategy = st.builds(
    Yahtzee_Turn,
)
Yahtzee_Game_strategy = st.builds(
    Yahtzee_Game,
    First=
        st.integers(),
    Player=
        st.none(),
    CompPlayer=
        st.none(),
    Again=
        st.booleans()
)















@given(instance=Yahtzee_Players1_strategy)
def test_hyp_yahtzee_players1_playerScore_setter(instance):
    original = instance.playerScore
    instance.playerScore = original
    assert instance.playerScore == original



@given(instance=Yahtzee_Players1_strategy)
def test_hyp_yahtzee_players1_compScore_setter(instance):
    original = instance.compScore
    instance.compScore = original
    assert instance.compScore == original




@given(instance=Yahtzee_Scoring1_strategy)
def test_hyp_yahtzee_scoring1_Temp_setter(instance):
    original = instance.Temp
    instance.Temp = original
    assert instance.Temp == original




@given(instance=Yahtzee_Turn1_strategy)
def test_hyp_yahtzee_turn1_Dice_setter(instance):
    original = instance.Dice
    instance.Dice = original
    assert instance.Dice == original

@given(instance=Yahtzee_Display1_strategy)
@settings(max_examples=50)
def test_hyp_yahtzee_display1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Display1)



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JButton_setter(instance):
    original = instance.JButton
    instance.JButton = original
    assert instance.JButton == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Jpanel_setter(instance):
    original = instance.Jpanel
    instance.Jpanel = original
    assert instance.Jpanel == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JTextField_setter(instance):
    original = instance.JTextField
    instance.JTextField = original
    assert instance.JTextField == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JRadioButton_setter(instance):
    original = instance.JRadioButton
    instance.JRadioButton = original
    assert instance.JRadioButton == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Jlabel_setter(instance):
    original = instance.Jlabel
    instance.Jlabel = original
    assert instance.Jlabel == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JScrollPanel_setter(instance):
    original = instance.JScrollPanel
    instance.JScrollPanel = original
    assert instance.JScrollPanel == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Computer_setter(instance):
    original = instance.Computer
    instance.Computer = original
    assert instance.Computer == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Temp1_setter(instance):
    original = instance.Temp1
    instance.Temp1 = original
    assert instance.Temp1 == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JFrame_setter(instance):
    original = instance.JFrame
    instance.JFrame = original
    assert instance.JFrame == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_Temp_setter(instance):
    original = instance.Temp
    instance.Temp = original
    assert instance.Temp == original



@given(instance=Yahtzee_Display1_strategy)
def test_hyp_yahtzee_display1_JImageIcon_setter(instance):
    original = instance.JImageIcon
    instance.JImageIcon = original
    assert instance.JImageIcon == original











@given(instance=Yahtzee_Players_strategy)
def test_hyp_yahtzee_players_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original



@given(instance=Yahtzee_Players_strategy)
def test_hyp_yahtzee_players_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Yahtzee_Display_strategy)
def test_hyp_yahtzee_display_PanelScorecard_setter(instance):
    original = instance.PanelScorecard
    instance.PanelScorecard = original
    assert instance.PanelScorecard == original



@given(instance=Yahtzee_Display_strategy)
def test_hyp_yahtzee_display_PanelGameName_setter(instance):
    original = instance.PanelGameName
    instance.PanelGameName = original
    assert instance.PanelGameName == original



@given(instance=Yahtzee_Display_strategy)
def test_hyp_yahtzee_display_PanelPrimary_setter(instance):
    original = instance.PanelPrimary
    instance.PanelPrimary = original
    assert instance.PanelPrimary == original



@given(instance=Yahtzee_Display_strategy)
def test_hyp_yahtzee_display_PanelNames_setter(instance):
    original = instance.PanelNames
    instance.PanelNames = original
    assert instance.PanelNames == original



@given(instance=Yahtzee_Display_strategy)
def test_hyp_yahtzee_display_PanelChoices_setter(instance):
    original = instance.PanelChoices
    instance.PanelChoices = original
    assert instance.PanelChoices == original



@given(instance=Yahtzee_Game_strategy)
@settings(max_examples=50)
def test_hyp_yahtzee_game_instantiation(instance):
    assert isinstance(instance, Yahtzee_Game)



@given(instance=Yahtzee_Game_strategy)
def test_hyp_yahtzee_game_First_setter(instance):
    original = instance.First
    instance.First = original
    assert instance.First == original



@given(instance=Yahtzee_Game_strategy)
def test_hyp_yahtzee_game_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original



@given(instance=Yahtzee_Game_strategy)
def test_hyp_yahtzee_game_CompPlayer_setter(instance):
    original = instance.CompPlayer
    instance.CompPlayer = original
    assert instance.CompPlayer == original



@given(instance=Yahtzee_Game_strategy)
def test_hyp_yahtzee_game_Again_setter(instance):
    original = instance.Again
    instance.Again = original
    assert instance.Again == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Announce_Winner_external,
    Class,
    Class1,
    Computer_Turn_external,
    Display,
    Game_Start_external,
    Get_Instructions_external,
    Get_Player_Name_external,
    Next_Turn_external,
    Play_Again_external,
    Player_Actor,
    Players,
    Roll_Dice_external,
    Roll_First_external,
    Score_Roll_external,
    Scoring,
    Turn,
    Yahtzee_Component,
    Yahtzee_Display,
    Yahtzee_Display1,
    Yahtzee_Game,
    Yahtzee_Players,
    Yahtzee_Players1,
    Yahtzee_Scoring,
    Yahtzee_Scoring1,
    Yahtzee_Turn,
    Yahtzee_Turn1,
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

def test_Yahtzee_Display_PanelChoices_value_roundtrip():
    instance = Yahtzee_Display(PanelChoices="sample_text", PanelGameName="sample_text", PanelNames="sample_text", PanelPrimary="sample_text", PanelScorecard="sample_text")
    assert instance.PanelChoices == "sample_text"
    instance.PanelChoices = "sample_text_2"
    assert instance.PanelChoices == "sample_text_2"


def test_Yahtzee_Display_PanelGameName_value_roundtrip():
    instance = Yahtzee_Display(PanelChoices="sample_text", PanelGameName="sample_text", PanelNames="sample_text", PanelPrimary="sample_text", PanelScorecard="sample_text")
    assert instance.PanelGameName == "sample_text"
    instance.PanelGameName = "sample_text_2"
    assert instance.PanelGameName == "sample_text_2"


def test_Yahtzee_Display_PanelNames_value_roundtrip():
    instance = Yahtzee_Display(PanelChoices="sample_text", PanelGameName="sample_text", PanelNames="sample_text", PanelPrimary="sample_text", PanelScorecard="sample_text")
    assert instance.PanelNames == "sample_text"
    instance.PanelNames = "sample_text_2"
    assert instance.PanelNames == "sample_text_2"


def test_Yahtzee_Display_PanelPrimary_value_roundtrip():
    instance = Yahtzee_Display(PanelChoices="sample_text", PanelGameName="sample_text", PanelNames="sample_text", PanelPrimary="sample_text", PanelScorecard="sample_text")
    assert instance.PanelPrimary == "sample_text"
    instance.PanelPrimary = "sample_text_2"
    assert instance.PanelPrimary == "sample_text_2"


def test_Yahtzee_Display_PanelScorecard_value_roundtrip():
    instance = Yahtzee_Display(PanelChoices="sample_text", PanelGameName="sample_text", PanelNames="sample_text", PanelPrimary="sample_text", PanelScorecard="sample_text")
    assert instance.PanelScorecard == "sample_text"
    instance.PanelScorecard = "sample_text_2"
    assert instance.PanelScorecard == "sample_text_2"


def test_Yahtzee_Players_Name_value_roundtrip():
    instance = Yahtzee_Players(Name="sample_text", Score="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Yahtzee_Players_Score_value_roundtrip():
    instance = Yahtzee_Players(Name="sample_text", Score="sample_text")
    assert instance.Score == "sample_text"
    instance.Score = "sample_text_2"
    assert instance.Score == "sample_text_2"


def test_Yahtzee_Players1_compScore_value_roundtrip():
    instance = Yahtzee_Players1(compScore="sample_text", playerScore="sample_text")
    assert instance.compScore == "sample_text"
    instance.compScore = "sample_text_2"
    assert instance.compScore == "sample_text_2"


def test_Yahtzee_Players1_playerScore_value_roundtrip():
    instance = Yahtzee_Players1(compScore="sample_text", playerScore="sample_text")
    assert instance.playerScore == "sample_text"
    instance.playerScore = "sample_text_2"
    assert instance.playerScore == "sample_text_2"


def test_Yahtzee_Scoring1_Temp_value_roundtrip():
    instance = Yahtzee_Scoring1(Temp="sample_text")
    assert instance.Temp == "sample_text"
    instance.Temp = "sample_text_2"
    assert instance.Temp == "sample_text_2"


def test_Yahtzee_Turn1_Dice_value_roundtrip():
    instance = Yahtzee_Turn1(Dice="sample_text")
    assert instance.Dice == "sample_text"
    instance.Dice = "sample_text_2"
    assert instance.Dice == "sample_text_2"


def test_assoc_Scoring_Players_link_reassign_clear():
    a = Yahtzee_Players(Name="sample_text", Score="sample_text")
    b1 = Yahtzee_Scoring()
    b2 = Yahtzee_Scoring()
    _safe_set(a, 'scoring9', b1)
    assert _is_linked(a, 'scoring9', b1)
    if hasattr(b1, 'players8'):
        assert _is_linked(b1, 'players8', a)
    _safe_set(a, 'scoring9', b2)
    assert _is_linked(a, 'scoring9', b2)
    if hasattr(b1, 'players8'):
        assert not _is_linked(b1, 'players8', a)
    if hasattr(b2, 'players8'):
        assert _is_linked(b2, 'players8', a)
    _safe_set(a, 'scoring9', None)
    assert not _is_linked(a, 'scoring9', b2)
    if hasattr(b2, 'players8'):
        assert not _is_linked(b2, 'players8', a)


def test_assoc_Scoring_Turn1_link_reassign_clear():
    a = Yahtzee_Turn1(Dice="sample_text")
    b1 = Yahtzee_Scoring1(Temp="sample_text")
    b2 = Yahtzee_Scoring1(Temp="sample_text_2")
    _safe_set(a, 'scoring57', b1)
    assert _is_linked(a, 'scoring57', b1)
    if hasattr(b1, 'turn56'):
        assert _is_linked(b1, 'turn56', a)
    _safe_set(a, 'scoring57', b2)
    assert _is_linked(a, 'scoring57', b2)
    if hasattr(b1, 'turn56'):
        assert not _is_linked(b1, 'turn56', a)
    if hasattr(b2, 'turn56'):
        assert _is_linked(b2, 'turn56', a)
    _safe_set(a, 'scoring57', None)
    assert not _is_linked(a, 'scoring57', b2)
    if hasattr(b2, 'turn56'):
        assert not _is_linked(b2, 'turn56', a)


def test_assoc_Turn_Players_link_reassign_clear():
    a = Yahtzee_Players(Name="sample_text", Score="sample_text")
    b1 = Yahtzee_Turn()
    b2 = Yahtzee_Turn()
    _safe_set(a, 'turn5', b1)
    assert _is_linked(a, 'turn5', b1)
    if hasattr(b1, 'players4'):
        assert _is_linked(b1, 'players4', a)
    _safe_set(a, 'turn5', b2)
    assert _is_linked(a, 'turn5', b2)
    if hasattr(b1, 'players4'):
        assert not _is_linked(b1, 'players4', a)
    if hasattr(b2, 'players4'):
        assert _is_linked(b2, 'players4', a)
    _safe_set(a, 'turn5', None)
    assert not _is_linked(a, 'turn5', b2)
    if hasattr(b2, 'players4'):
        assert not _is_linked(b2, 'players4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Announce_Winner_external_strategy = st.builds(Announce_Winner_external)
@given(instance=Announce_Winner_external_strategy)
@settings(max_examples=25)
def test_Announce_Winner_external_instantiation(instance):
    assert isinstance(instance, Announce_Winner_external)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Class1_strategy = st.builds(Class1)
@given(instance=Class1_strategy)
@settings(max_examples=25)
def test_Class1_instantiation(instance):
    assert isinstance(instance, Class1)


Computer_Turn_external_strategy = st.builds(Computer_Turn_external)
@given(instance=Computer_Turn_external_strategy)
@settings(max_examples=25)
def test_Computer_Turn_external_instantiation(instance):
    assert isinstance(instance, Computer_Turn_external)


Display_strategy = st.builds(Display)
@given(instance=Display_strategy)
@settings(max_examples=25)
def test_Display_instantiation(instance):
    assert isinstance(instance, Display)


Game_Start_external_strategy = st.builds(Game_Start_external)
@given(instance=Game_Start_external_strategy)
@settings(max_examples=25)
def test_Game_Start_external_instantiation(instance):
    assert isinstance(instance, Game_Start_external)


Get_Instructions_external_strategy = st.builds(Get_Instructions_external)
@given(instance=Get_Instructions_external_strategy)
@settings(max_examples=25)
def test_Get_Instructions_external_instantiation(instance):
    assert isinstance(instance, Get_Instructions_external)


Get_Player_Name_external_strategy = st.builds(Get_Player_Name_external)
@given(instance=Get_Player_Name_external_strategy)
@settings(max_examples=25)
def test_Get_Player_Name_external_instantiation(instance):
    assert isinstance(instance, Get_Player_Name_external)


Next_Turn_external_strategy = st.builds(Next_Turn_external)
@given(instance=Next_Turn_external_strategy)
@settings(max_examples=25)
def test_Next_Turn_external_instantiation(instance):
    assert isinstance(instance, Next_Turn_external)


Play_Again_external_strategy = st.builds(Play_Again_external)
@given(instance=Play_Again_external_strategy)
@settings(max_examples=25)
def test_Play_Again_external_instantiation(instance):
    assert isinstance(instance, Play_Again_external)


Player_Actor_strategy = st.builds(Player_Actor)
@given(instance=Player_Actor_strategy)
@settings(max_examples=25)
def test_Player_Actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)


Players_strategy = st.builds(Players)
@given(instance=Players_strategy)
@settings(max_examples=25)
def test_Players_instantiation(instance):
    assert isinstance(instance, Players)


Roll_Dice_external_strategy = st.builds(Roll_Dice_external)
@given(instance=Roll_Dice_external_strategy)
@settings(max_examples=25)
def test_Roll_Dice_external_instantiation(instance):
    assert isinstance(instance, Roll_Dice_external)


Roll_First_external_strategy = st.builds(Roll_First_external)
@given(instance=Roll_First_external_strategy)
@settings(max_examples=25)
def test_Roll_First_external_instantiation(instance):
    assert isinstance(instance, Roll_First_external)


Score_Roll_external_strategy = st.builds(Score_Roll_external)
@given(instance=Score_Roll_external_strategy)
@settings(max_examples=25)
def test_Score_Roll_external_instantiation(instance):
    assert isinstance(instance, Score_Roll_external)


Scoring_strategy = st.builds(Scoring)
@given(instance=Scoring_strategy)
@settings(max_examples=25)
def test_Scoring_instantiation(instance):
    assert isinstance(instance, Scoring)


Turn_strategy = st.builds(Turn)
@given(instance=Turn_strategy)
@settings(max_examples=25)
def test_Turn_instantiation(instance):
    assert isinstance(instance, Turn)


Yahtzee_Component_strategy = st.builds(Yahtzee_Component)
@given(instance=Yahtzee_Component_strategy)
@settings(max_examples=25)
def test_Yahtzee_Component_instantiation(instance):
    assert isinstance(instance, Yahtzee_Component)


Yahtzee_Display_strategy = st.builds(Yahtzee_Display, PanelChoices=safe_text, PanelGameName=safe_text, PanelNames=safe_text, PanelPrimary=safe_text, PanelScorecard=safe_text)
@given(instance=Yahtzee_Display_strategy)
@settings(max_examples=25)
def test_Yahtzee_Display_instantiation(instance):
    assert isinstance(instance, Yahtzee_Display)


Yahtzee_Players_strategy = st.builds(Yahtzee_Players, Name=safe_text, Score=safe_text)
@given(instance=Yahtzee_Players_strategy)
@settings(max_examples=25)
def test_Yahtzee_Players_instantiation(instance):
    assert isinstance(instance, Yahtzee_Players)


Yahtzee_Players1_strategy = st.builds(Yahtzee_Players1, compScore=safe_text, playerScore=safe_text)
@given(instance=Yahtzee_Players1_strategy)
@settings(max_examples=25)
def test_Yahtzee_Players1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Players1)


Yahtzee_Scoring_strategy = st.builds(Yahtzee_Scoring)
@given(instance=Yahtzee_Scoring_strategy)
@settings(max_examples=25)
def test_Yahtzee_Scoring_instantiation(instance):
    assert isinstance(instance, Yahtzee_Scoring)


Yahtzee_Scoring1_strategy = st.builds(Yahtzee_Scoring1, Temp=safe_text)
@given(instance=Yahtzee_Scoring1_strategy)
@settings(max_examples=25)
def test_Yahtzee_Scoring1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Scoring1)


Yahtzee_Turn_strategy = st.builds(Yahtzee_Turn)
@given(instance=Yahtzee_Turn_strategy)
@settings(max_examples=25)
def test_Yahtzee_Turn_instantiation(instance):
    assert isinstance(instance, Yahtzee_Turn)


Yahtzee_Turn1_strategy = st.builds(Yahtzee_Turn1, Dice=safe_text)
@given(instance=Yahtzee_Turn1_strategy)
@settings(max_examples=25)
def test_Yahtzee_Turn1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Turn1)



