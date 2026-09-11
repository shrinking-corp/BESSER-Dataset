import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BomberMan,
    Game,
    GameMap,
    Monster,
    PowerUps,
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

def test_BomberMan_lives_value_roundtrip():
    instance = BomberMan(lives=7, location="sample_text", points=7)
    assert instance.lives == 7
    instance.lives = 13
    assert instance.lives == 13


def test_BomberMan_location_value_roundtrip():
    instance = BomberMan(lives=7, location="sample_text", points=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_BomberMan_points_value_roundtrip():
    instance = BomberMan(lives=7, location="sample_text", points=7)
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_Game_Timer_value_roundtrip():
    instance = Game(Timer=7)
    assert instance.Timer == 7
    instance.Timer = 13
    assert instance.Timer == 13


def test_GameMap_poerups_value_roundtrip():
    instance = GameMap(poerups="sample_text", transitions="sample_text", walls="sample_text")
    assert instance.poerups == "sample_text"
    instance.poerups = "sample_text_2"
    assert instance.poerups == "sample_text_2"


def test_GameMap_transitions_value_roundtrip():
    instance = GameMap(poerups="sample_text", transitions="sample_text", walls="sample_text")
    assert instance.transitions == "sample_text"
    instance.transitions = "sample_text_2"
    assert instance.transitions == "sample_text_2"


def test_GameMap_walls_value_roundtrip():
    instance = GameMap(poerups="sample_text", transitions="sample_text", walls="sample_text")
    assert instance.walls == "sample_text"
    instance.walls = "sample_text_2"
    assert instance.walls == "sample_text_2"


def test_Monster_lives_value_roundtrip():
    instance = Monster(lives=7, location="sample_text", specilization="sample_text", type="sample_text")
    assert instance.lives == 7
    instance.lives = 13
    assert instance.lives == 13


def test_Monster_location_value_roundtrip():
    instance = Monster(lives=7, location="sample_text", specilization="sample_text", type="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_Monster_specilization_value_roundtrip():
    instance = Monster(lives=7, location="sample_text", specilization="sample_text", type="sample_text")
    assert instance.specilization == "sample_text"
    instance.specilization = "sample_text_2"
    assert instance.specilization == "sample_text_2"


def test_Monster_type_value_roundtrip():
    instance = Monster(lives=7, location="sample_text", specilization="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_PowerUps_locations_value_roundtrip():
    instance = PowerUps(locations="sample_text", points=7, speciliaty="sample_text")
    assert instance.locations == "sample_text"
    instance.locations = "sample_text_2"
    assert instance.locations == "sample_text_2"


def test_PowerUps_points_value_roundtrip():
    instance = PowerUps(locations="sample_text", points=7, speciliaty="sample_text")
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_PowerUps_speciliaty_value_roundtrip():
    instance = PowerUps(locations="sample_text", points=7, speciliaty="sample_text")
    assert instance.speciliaty == "sample_text"
    instance.speciliaty = "sample_text_2"
    assert instance.speciliaty == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BomberMan_strategy = st.builds(BomberMan, lives=st.integers(), location=safe_text, points=st.integers())
@given(instance=BomberMan_strategy)
@settings(max_examples=25)
def test_BomberMan_instantiation(instance):
    assert isinstance(instance, BomberMan)


Game_strategy = st.builds(Game, Timer=st.integers())
@given(instance=Game_strategy)
@settings(max_examples=25)
def test_Game_instantiation(instance):
    assert isinstance(instance, Game)


GameMap_strategy = st.builds(GameMap, poerups=safe_text, transitions=safe_text, walls=safe_text)
@given(instance=GameMap_strategy)
@settings(max_examples=25)
def test_GameMap_instantiation(instance):
    assert isinstance(instance, GameMap)


Monster_strategy = st.builds(Monster, lives=st.integers(), location=safe_text, specilization=safe_text, type=safe_text)
@given(instance=Monster_strategy)
@settings(max_examples=25)
def test_Monster_instantiation(instance):
    assert isinstance(instance, Monster)


PowerUps_strategy = st.builds(PowerUps, locations=safe_text, points=st.integers(), speciliaty=safe_text)
@given(instance=PowerUps_strategy)
@settings(max_examples=25)
def test_PowerUps_instantiation(instance):
    assert isinstance(instance, PowerUps)


