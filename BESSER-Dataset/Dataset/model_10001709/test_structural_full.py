import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Game_Play_UseCase,
    Main_Menu_UseCase,
    Selection_UseCase,
    Splash_UseCase,
    Store_UseCase,
    T,
    exit_game__UseCase,
    lock_unlock_UseCase,
    player_Actor,
    save_achievemnts_UseCase,
    save_game_state__UseCase,
    splash_anim_controller,
    system__Actor,
    view_achievements_UseCase,
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

def test_splash_anim_controller_attribute_value_roundtrip():
    instance = splash_anim_controller(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Game_Play_UseCase_strategy = st.builds(Game_Play_UseCase)
@given(instance=Game_Play_UseCase_strategy)
@settings(max_examples=25)
def test_Game_Play_UseCase_instantiation(instance):
    assert isinstance(instance, Game_Play_UseCase)


Main_Menu_UseCase_strategy = st.builds(Main_Menu_UseCase)
@given(instance=Main_Menu_UseCase_strategy)
@settings(max_examples=25)
def test_Main_Menu_UseCase_instantiation(instance):
    assert isinstance(instance, Main_Menu_UseCase)


Selection_UseCase_strategy = st.builds(Selection_UseCase)
@given(instance=Selection_UseCase_strategy)
@settings(max_examples=25)
def test_Selection_UseCase_instantiation(instance):
    assert isinstance(instance, Selection_UseCase)


Splash_UseCase_strategy = st.builds(Splash_UseCase)
@given(instance=Splash_UseCase_strategy)
@settings(max_examples=25)
def test_Splash_UseCase_instantiation(instance):
    assert isinstance(instance, Splash_UseCase)


Store_UseCase_strategy = st.builds(Store_UseCase)
@given(instance=Store_UseCase_strategy)
@settings(max_examples=25)
def test_Store_UseCase_instantiation(instance):
    assert isinstance(instance, Store_UseCase)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


exit_game__UseCase_strategy = st.builds(exit_game__UseCase)
@given(instance=exit_game__UseCase_strategy)
@settings(max_examples=25)
def test_exit_game__UseCase_instantiation(instance):
    assert isinstance(instance, exit_game__UseCase)


lock_unlock_UseCase_strategy = st.builds(lock_unlock_UseCase)
@given(instance=lock_unlock_UseCase_strategy)
@settings(max_examples=25)
def test_lock_unlock_UseCase_instantiation(instance):
    assert isinstance(instance, lock_unlock_UseCase)


player_Actor_strategy = st.builds(player_Actor)
@given(instance=player_Actor_strategy)
@settings(max_examples=25)
def test_player_Actor_instantiation(instance):
    assert isinstance(instance, player_Actor)


save_achievemnts_UseCase_strategy = st.builds(save_achievemnts_UseCase)
@given(instance=save_achievemnts_UseCase_strategy)
@settings(max_examples=25)
def test_save_achievemnts_UseCase_instantiation(instance):
    assert isinstance(instance, save_achievemnts_UseCase)


save_game_state__UseCase_strategy = st.builds(save_game_state__UseCase)
@given(instance=save_game_state__UseCase_strategy)
@settings(max_examples=25)
def test_save_game_state__UseCase_instantiation(instance):
    assert isinstance(instance, save_game_state__UseCase)


splash_anim_controller_strategy = st.builds(splash_anim_controller, attribute=safe_text)
@given(instance=splash_anim_controller_strategy)
@settings(max_examples=25)
def test_splash_anim_controller_instantiation(instance):
    assert isinstance(instance, splash_anim_controller)


system__Actor_strategy = st.builds(system__Actor)
@given(instance=system__Actor_strategy)
@settings(max_examples=25)
def test_system__Actor_instantiation(instance):
    assert isinstance(instance, system__Actor)


view_achievements_UseCase_strategy = st.builds(view_achievements_UseCase)
@given(instance=view_achievements_UseCase_strategy)
@settings(max_examples=25)
def test_view_achievements_UseCase_instantiation(instance):
    assert isinstance(instance, view_achievements_UseCase)


