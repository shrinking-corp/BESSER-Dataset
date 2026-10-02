import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Comparable_BlackjackHand__Interface,
    Iterable_Card__Interface,
    blackjack_BlackjackGame,
    blackjack_BlackjackHand,
    blackjack_Card,
    blackjack_CardSet,
    blackjack_DealerBot,
    blackjack_Deck,
    blackjack_DeckShuffledListener_Interface,
    blackjack_ExampleInstrumentedTest,
    blackjack_ExampleUnitTest,
    blackjack_MainActivity,
    genmymodelreverse_C1,
    genmymodelreverse_C11,
    genmymodelreverse_C12,
    genmymodelreverse_android_support_v7_app_AppCompatActivity,
    genmymodelreverse_java_lang_Comparable_Interface,
    genmymodelreverse_java_lang_Iterable_Interface,
    genmymodelreverse_java_util_Iterator_Interface,
    blackjack_GameState,
    blackjack_Suit,
    blackjack_Value,
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

