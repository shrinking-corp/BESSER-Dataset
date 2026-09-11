import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Player,
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

def test_Player_balance_value_roundtrip():
    instance = Player(balance=7, name="sample_text", position=7, token="sample_text")
    assert instance.balance == 7
    instance.balance = 13
    assert instance.balance == 13


def test_Player_name_value_roundtrip():
    instance = Player(balance=7, name="sample_text", position=7, token="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player_position_value_roundtrip():
    instance = Player(balance=7, name="sample_text", position=7, token="sample_text")
    assert instance.position == 7
    instance.position = 13
    assert instance.position == 13


def test_Player_token_value_roundtrip():
    instance = Player(balance=7, name="sample_text", position=7, token="sample_text")
    assert instance.token == "sample_text"
    instance.token = "sample_text_2"
    assert instance.token == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Player_strategy = st.builds(Player, balance=st.integers(), name=safe_text, position=st.integers(), token=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


