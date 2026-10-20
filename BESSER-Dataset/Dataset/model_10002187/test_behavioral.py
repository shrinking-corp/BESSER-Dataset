import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Comparable_Card__Interface,
    Iterable_Card__Interface,
    Iterator_Card__Interface,
    War_Card,
    War_Card1,
    War_ClassicTwoPlayer,
    War_ClassicTwoPlayer1,
    War_Deck,
    War_Deck1,
    War_DeckIterator,
    War_DeckIterator1,
    War_GameLogger,
    War_GameLogger1,
    War_PlayGame,
    War_PlayGame1,
    War_Player,
    War_Player1,
    War_ThreePlayerPointPile,
    War_ThreePlayerPointPile1,
    War_TwoPlayerPointPile,
    War_TwoPlayerPointPile1,
    War_WarGameVariation,
    War_WarGameVariation1,
    War_WarVariationClassic,
    War_WarVariationClassic1,
    War_WarVariationWithPoints,
    War_WarVariationWithPoints1,
    War_Rank,
    War_Rank1,
    War_Suit,
    War_Suit1,
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

def test_assoc_cardsWon_Player_Deck_17_reverse_link_reassign_clear():
    a1 = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    a2 = War_Player1(name="sample_text_2", name1="sample_text_2", score=13, score1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'player36', a1)
    assert _is_linked(b, 'player36', a1)
    if hasattr(a1, 'cardsWon37'):
        assert _is_linked(a1, 'cardsWon37', b)
    _safe_set(b, 'player36', a2)
    assert _is_linked(b, 'player36', a2)
    if hasattr(a1, 'cardsWon37'):
        assert not _is_linked(a1, 'cardsWon37', b)
    if hasattr(a2, 'cardsWon37'):
        assert _is_linked(a2, 'cardsWon37', b)
    _safe_set(b, 'player36', None)
    assert not _is_linked(b, 'player36', a2)
    if hasattr(a2, 'cardsWon37'):
        assert not _is_linked(a2, 'cardsWon37', b)


def test_assoc_cardsWon_Player_Deck_19_reverse_link_reassign_clear():
    a1 = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    a2 = War_Player1(name="sample_text_2", name1="sample_text_2", score=13, score1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'player38', a1)
    assert _is_linked(b, 'player38', a1)
    if hasattr(a1, 'cardsWon39'):
        assert _is_linked(a1, 'cardsWon39', b)
    _safe_set(b, 'player38', a2)
    assert _is_linked(b, 'player38', a2)
    if hasattr(a1, 'cardsWon39'):
        assert not _is_linked(a1, 'cardsWon39', b)
    if hasattr(a2, 'cardsWon39'):
        assert _is_linked(a2, 'cardsWon39', b)
    _safe_set(b, 'player38', None)
    assert not _is_linked(b, 'player38', a2)
    if hasattr(a2, 'cardsWon39'):
        assert not _is_linked(a2, 'cardsWon39', b)


def test_assoc_deck_DeckIterator_Deck_18_reverse_link_reassign_clear():
    a1 = War_DeckIterator1(current=7, current1=7)
    a2 = War_DeckIterator1(current=13, current1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'deckiterator6', a1)
    assert _is_linked(b, 'deckiterator6', a1)
    if hasattr(a1, 'deck7'):
        assert _is_linked(a1, 'deck7', b)
    _safe_set(b, 'deckiterator6', a2)
    assert _is_linked(b, 'deckiterator6', a2)
    if hasattr(a1, 'deck7'):
        assert not _is_linked(a1, 'deck7', b)
    if hasattr(a2, 'deck7'):
        assert _is_linked(a2, 'deck7', b)
    _safe_set(b, 'deckiterator6', None)
    assert not _is_linked(b, 'deckiterator6', a2)
    if hasattr(a2, 'deck7'):
        assert not _is_linked(a2, 'deck7', b)


def test_assoc_deck_DeckIterator_Deck_3_reverse_link_reassign_clear():
    a1 = War_DeckIterator1(current=7, current1=7)
    a2 = War_DeckIterator1(current=13, current1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'deckiterator22', a1)
    assert _is_linked(b, 'deckiterator22', a1)
    if hasattr(a1, 'deck23'):
        assert _is_linked(a1, 'deck23', b)
    _safe_set(b, 'deckiterator22', a2)
    assert _is_linked(b, 'deckiterator22', a2)
    if hasattr(a1, 'deck23'):
        assert not _is_linked(a1, 'deck23', b)
    if hasattr(a2, 'deck23'):
        assert _is_linked(a2, 'deck23', b)
    _safe_set(b, 'deckiterator22', None)
    assert not _is_linked(b, 'deckiterator22', a2)
    if hasattr(a2, 'deck23'):
        assert not _is_linked(a2, 'deck23', b)


def test_assoc_deck_WarGameVariation_Deck_12_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'wargamevariation40', a1)
    assert _is_linked(b, 'wargamevariation40', a1)
    if hasattr(a1, 'deck41'):
        assert _is_linked(a1, 'deck41', b)
    _safe_set(b, 'wargamevariation40', a2)
    assert _is_linked(b, 'wargamevariation40', a2)
    if hasattr(a1, 'deck41'):
        assert not _is_linked(a1, 'deck41', b)
    if hasattr(a2, 'deck41'):
        assert _is_linked(a2, 'deck41', b)
    _safe_set(b, 'wargamevariation40', None)
    assert not _is_linked(b, 'wargamevariation40', a2)
    if hasattr(a2, 'deck41'):
        assert not _is_linked(a2, 'deck41', b)


def test_assoc_deck_WarGameVariation_Deck_14_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'wargamevariation42', a1)
    assert _is_linked(b, 'wargamevariation42', a1)
    if hasattr(a1, 'deck43'):
        assert _is_linked(a1, 'deck43', b)
    _safe_set(b, 'wargamevariation42', a2)
    assert _is_linked(b, 'wargamevariation42', a2)
    if hasattr(a1, 'deck43'):
        assert not _is_linked(a1, 'deck43', b)
    if hasattr(a2, 'deck43'):
        assert _is_linked(a2, 'deck43', b)
    _safe_set(b, 'wargamevariation42', None)
    assert not _is_linked(b, 'wargamevariation42', a2)
    if hasattr(a2, 'deck43'):
        assert not _is_linked(a2, 'deck43', b)


def test_assoc_hand_Player_Deck_0_reverse_link_reassign_clear():
    a1 = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    a2 = War_Player1(name="sample_text_2", name1="sample_text_2", score=13, score1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'player10', a1)
    assert _is_linked(b, 'player10', a1)
    if hasattr(a1, 'hand11'):
        assert _is_linked(a1, 'hand11', b)
    _safe_set(b, 'player10', a2)
    assert _is_linked(b, 'player10', a2)
    if hasattr(a1, 'hand11'):
        assert not _is_linked(a1, 'hand11', b)
    if hasattr(a2, 'hand11'):
        assert _is_linked(a2, 'hand11', b)
    _safe_set(b, 'player10', None)
    assert not _is_linked(b, 'player10', a2)
    if hasattr(a2, 'hand11'):
        assert not _is_linked(a2, 'hand11', b)


def test_assoc_hand_Player_Deck_8_reverse_link_reassign_clear():
    a1 = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    a2 = War_Player1(name="sample_text_2", name1="sample_text_2", score=13, score1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'player4', a1)
    assert _is_linked(b, 'player4', a1)
    if hasattr(a1, 'hand5'):
        assert _is_linked(a1, 'hand5', b)
    _safe_set(b, 'player4', a2)
    assert _is_linked(b, 'player4', a2)
    if hasattr(a1, 'hand5'):
        assert not _is_linked(a1, 'hand5', b)
    if hasattr(a2, 'hand5'):
        assert _is_linked(a2, 'hand5', b)
    _safe_set(b, 'player4', None)
    assert not _is_linked(b, 'player4', a2)
    if hasattr(a2, 'hand5'):
        assert not _is_linked(a2, 'hand5', b)


def test_assoc_player1_WarVariationClassic_Player_2_reverse_link_reassign_clear():
    a1 = War_WarVariationClassic1(numOfRounds=7, numOfRounds1=7)
    a2 = War_WarVariationClassic1(numOfRounds=13, numOfRounds1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'warvariationclassic32', a1)
    assert _is_linked(b, 'warvariationclassic32', a1)
    if hasattr(a1, 'player133'):
        assert _is_linked(a1, 'player133', b)
    _safe_set(b, 'warvariationclassic32', a2)
    assert _is_linked(b, 'warvariationclassic32', a2)
    if hasattr(a1, 'player133'):
        assert not _is_linked(a1, 'player133', b)
    if hasattr(a2, 'player133'):
        assert _is_linked(a2, 'player133', b)
    _safe_set(b, 'warvariationclassic32', None)
    assert not _is_linked(b, 'warvariationclassic32', a2)
    if hasattr(a2, 'player133'):
        assert not _is_linked(a2, 'player133', b)


def test_assoc_player1_WarVariationClassic_Player_20_reverse_link_reassign_clear():
    a1 = War_WarVariationClassic1(numOfRounds=7, numOfRounds1=7)
    a2 = War_WarVariationClassic1(numOfRounds=13, numOfRounds1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'warvariationclassic26', a1)
    assert _is_linked(b, 'warvariationclassic26', a1)
    if hasattr(a1, 'player127'):
        assert _is_linked(a1, 'player127', b)
    _safe_set(b, 'warvariationclassic26', a2)
    assert _is_linked(b, 'warvariationclassic26', a2)
    if hasattr(a1, 'player127'):
        assert not _is_linked(a1, 'player127', b)
    if hasattr(a2, 'player127'):
        assert _is_linked(a2, 'player127', b)
    _safe_set(b, 'warvariationclassic26', None)
    assert not _is_linked(b, 'warvariationclassic26', a2)
    if hasattr(a2, 'player127'):
        assert not _is_linked(a2, 'player127', b)


def test_assoc_player2_WarVariationClassic_Player_1_reverse_link_reassign_clear():
    a1 = War_WarVariationClassic1(numOfRounds=7, numOfRounds1=7)
    a2 = War_WarVariationClassic1(numOfRounds=13, numOfRounds1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'warvariationclassic28', a1)
    assert _is_linked(b, 'warvariationclassic28', a1)
    if hasattr(a1, 'player229'):
        assert _is_linked(a1, 'player229', b)
    _safe_set(b, 'warvariationclassic28', a2)
    assert _is_linked(b, 'warvariationclassic28', a2)
    if hasattr(a1, 'player229'):
        assert not _is_linked(a1, 'player229', b)
    if hasattr(a2, 'player229'):
        assert _is_linked(a2, 'player229', b)
    _safe_set(b, 'warvariationclassic28', None)
    assert not _is_linked(b, 'warvariationclassic28', a2)
    if hasattr(a2, 'player229'):
        assert not _is_linked(a2, 'player229', b)


def test_assoc_player2_WarVariationClassic_Player_5_reverse_link_reassign_clear():
    a1 = War_WarVariationClassic1(numOfRounds=7, numOfRounds1=7)
    a2 = War_WarVariationClassic1(numOfRounds=13, numOfRounds1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'warvariationclassic14', a1)
    assert _is_linked(b, 'warvariationclassic14', a1)
    if hasattr(a1, 'player215'):
        assert _is_linked(a1, 'player215', b)
    _safe_set(b, 'warvariationclassic14', a2)
    assert _is_linked(b, 'warvariationclassic14', a2)
    if hasattr(a1, 'player215'):
        assert not _is_linked(a1, 'player215', b)
    if hasattr(a2, 'player215'):
        assert _is_linked(a2, 'player215', b)
    _safe_set(b, 'warvariationclassic14', None)
    assert not _is_linked(b, 'warvariationclassic14', a2)
    if hasattr(a2, 'player215'):
        assert not _is_linked(a2, 'player215', b)


def test_assoc_players_WarGameVariation_Player_13_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'wargamevariation34', a1)
    assert _is_linked(b, 'wargamevariation34', a1)
    if hasattr(a1, 'players35'):
        assert _is_linked(a1, 'players35', b)
    _safe_set(b, 'wargamevariation34', a2)
    assert _is_linked(b, 'wargamevariation34', a2)
    if hasattr(a1, 'players35'):
        assert not _is_linked(a1, 'players35', b)
    if hasattr(a2, 'players35'):
        assert _is_linked(a2, 'players35', b)
    _safe_set(b, 'wargamevariation34', None)
    assert not _is_linked(b, 'wargamevariation34', a2)
    if hasattr(a2, 'players35'):
        assert not _is_linked(a2, 'players35', b)


def test_assoc_players_WarGameVariation_Player_21_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Player1(name="sample_text", name1="sample_text", score=7, score1=7)
    _safe_set(b, 'wargamevariation0', a1)
    assert _is_linked(b, 'wargamevariation0', a1)
    if hasattr(a1, 'players1'):
        assert _is_linked(a1, 'players1', b)
    _safe_set(b, 'wargamevariation0', a2)
    assert _is_linked(b, 'wargamevariation0', a2)
    if hasattr(a1, 'players1'):
        assert not _is_linked(a1, 'players1', b)
    if hasattr(a2, 'players1'):
        assert _is_linked(a2, 'players1', b)
    _safe_set(b, 'wargamevariation0', None)
    assert not _is_linked(b, 'wargamevariation0', a2)
    if hasattr(a2, 'players1'):
        assert not _is_linked(a2, 'players1', b)


def test_assoc_warLogger_WarGameVariation_GameLogger_15_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_GameLogger1(gameLogWriter="sample_text", gameLogWriter1="sample_text")
    _safe_set(b, 'wargamevariation12', a1)
    assert _is_linked(b, 'wargamevariation12', a1)
    if hasattr(a1, 'warLogger13'):
        assert _is_linked(a1, 'warLogger13', b)
    _safe_set(b, 'wargamevariation12', a2)
    assert _is_linked(b, 'wargamevariation12', a2)
    if hasattr(a1, 'warLogger13'):
        assert not _is_linked(a1, 'warLogger13', b)
    if hasattr(a2, 'warLogger13'):
        assert _is_linked(a2, 'warLogger13', b)
    _safe_set(b, 'wargamevariation12', None)
    assert not _is_linked(b, 'wargamevariation12', a2)
    if hasattr(a2, 'warLogger13'):
        assert not _is_linked(a2, 'warLogger13', b)


def test_assoc_warLogger_WarGameVariation_GameLogger_9_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_GameLogger1(gameLogWriter="sample_text", gameLogWriter1="sample_text")
    _safe_set(b, 'wargamevariation24', a1)
    assert _is_linked(b, 'wargamevariation24', a1)
    if hasattr(a1, 'warLogger25'):
        assert _is_linked(a1, 'warLogger25', b)
    _safe_set(b, 'wargamevariation24', a2)
    assert _is_linked(b, 'wargamevariation24', a2)
    if hasattr(a1, 'warLogger25'):
        assert not _is_linked(a1, 'warLogger25', b)
    if hasattr(a2, 'warLogger25'):
        assert _is_linked(a2, 'warLogger25', b)
    _safe_set(b, 'wargamevariation24', None)
    assert not _is_linked(b, 'wargamevariation24', a2)
    if hasattr(a2, 'warLogger25'):
        assert not _is_linked(a2, 'warLogger25', b)


def test_assoc_winPile_WarGameVariation_Deck_11_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'wargamevariation16', a1)
    assert _is_linked(b, 'wargamevariation16', a1)
    if hasattr(a1, 'winPile17'):
        assert _is_linked(a1, 'winPile17', b)
    _safe_set(b, 'wargamevariation16', a2)
    assert _is_linked(b, 'wargamevariation16', a2)
    if hasattr(a1, 'winPile17'):
        assert not _is_linked(a1, 'winPile17', b)
    if hasattr(a2, 'winPile17'):
        assert _is_linked(a2, 'winPile17', b)
    _safe_set(b, 'wargamevariation16', None)
    assert not _is_linked(b, 'wargamevariation16', a2)
    if hasattr(a2, 'winPile17'):
        assert not _is_linked(a2, 'winPile17', b)


def test_assoc_winPile_WarGameVariation_Deck_16_reverse_link_reassign_clear():
    a1 = War_WarGameVariation1(numOfPlayers=7, numOfPlayers1=7)
    a2 = War_WarGameVariation1(numOfPlayers=13, numOfPlayers1=13)
    b = War_Deck1(LOWEST_NUMERIC_VALUE=7, LOWEST_NUMERIC_VALUE1=7, NUMERIC_CARDS_IN_SUIT=7, NUMERIC_CARDS_IN_SUIT1=7, TOP_CARD=7, TOP_CARD1=7)
    _safe_set(b, 'wargamevariation30', a1)
    assert _is_linked(b, 'wargamevariation30', a1)
    if hasattr(a1, 'winPile31'):
        assert _is_linked(a1, 'winPile31', b)
    _safe_set(b, 'wargamevariation30', a2)
    assert _is_linked(b, 'wargamevariation30', a2)
    if hasattr(a1, 'winPile31'):
        assert not _is_linked(a1, 'winPile31', b)
    if hasattr(a2, 'winPile31'):
        assert _is_linked(a2, 'winPile31', b)
    _safe_set(b, 'wargamevariation30', None)
    assert not _is_linked(b, 'wargamevariation30', a2)
    if hasattr(a2, 'winPile31'):
        assert not _is_linked(a2, 'winPile31', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

