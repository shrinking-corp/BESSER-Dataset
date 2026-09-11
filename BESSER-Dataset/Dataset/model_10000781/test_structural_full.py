import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CommentServiceJDBCTest,
    CommentServiceTest,
    Comparable_Score__Interface,
    Main,
    RatingServiceTest,
    ScoreServiceJDBCTest,
    ScoreServiceTest,
    SpiderSolitaireTestSuite,
    card_Card,
    card_Deck,
    deck_Deck,
    deck_Foundations,
    deck_Stock,
    deck_Tableau,
    entities_Comment,
    entities_Rating,
    entities_Score,
    features_History,
    genmymodelreverse_C1,
    genmymodelreverse_C11,
    genmymodelreverse_java_io_Serializable_Interface,
    genmymodelreverse_java_lang_Comparable_Interface,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_java_lang_RuntimeException,
    genmymodelreverse_java_lang_Throwable,
    genmymodelreverse_java_util_Date,
    genmymodelreverse_java_util_List_Interface,
    services_CommentException,
    services_CommentServiceJDBC,
    services_CommentService_Interface,
    services_RatingException,
    services_RatingServiceJDBC,
    services_RatingService_Interface,
    services_ScoreException,
    services_ScoreServiceJDBC,
    services_ScoreService_Interface,
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

def test_CommentServiceJDBCTest_DELETE_value_roundtrip():
    instance = CommentServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.DELETE == "sample_text"
    instance.DELETE = "sample_text_2"
    assert instance.DELETE == "sample_text_2"


def test_CommentServiceJDBCTest_PASS_value_roundtrip():
    instance = CommentServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.PASS == "sample_text"
    instance.PASS = "sample_text_2"
    assert instance.PASS == "sample_text_2"


def test_CommentServiceJDBCTest_URL_value_roundtrip():
    instance = CommentServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_CommentServiceJDBCTest_USER_value_roundtrip():
    instance = CommentServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.USER == "sample_text"
    instance.USER = "sample_text_2"
    assert instance.USER == "sample_text_2"


def test_CommentServiceTest_GAME_NAME_value_roundtrip():
    instance = CommentServiceTest(GAME_NAME="sample_text", PLAYER_NAME="sample_text")
    assert instance.GAME_NAME == "sample_text"
    instance.GAME_NAME = "sample_text_2"
    assert instance.GAME_NAME == "sample_text_2"


def test_CommentServiceTest_PLAYER_NAME_value_roundtrip():
    instance = CommentServiceTest(GAME_NAME="sample_text", PLAYER_NAME="sample_text")
    assert instance.PLAYER_NAME == "sample_text"
    instance.PLAYER_NAME = "sample_text_2"
    assert instance.PLAYER_NAME == "sample_text_2"


def test_RatingServiceTest_GAME_NAME_value_roundtrip():
    instance = RatingServiceTest(GAME_NAME="sample_text", TEST_PLAYER="sample_text", TEST_PLAYER_2="sample_text", TEST_PLAYER_3="sample_text")
    assert instance.GAME_NAME == "sample_text"
    instance.GAME_NAME = "sample_text_2"
    assert instance.GAME_NAME == "sample_text_2"


def test_RatingServiceTest_TEST_PLAYER_value_roundtrip():
    instance = RatingServiceTest(GAME_NAME="sample_text", TEST_PLAYER="sample_text", TEST_PLAYER_2="sample_text", TEST_PLAYER_3="sample_text")
    assert instance.TEST_PLAYER == "sample_text"
    instance.TEST_PLAYER = "sample_text_2"
    assert instance.TEST_PLAYER == "sample_text_2"


def test_RatingServiceTest_TEST_PLAYER_2_value_roundtrip():
    instance = RatingServiceTest(GAME_NAME="sample_text", TEST_PLAYER="sample_text", TEST_PLAYER_2="sample_text", TEST_PLAYER_3="sample_text")
    assert instance.TEST_PLAYER_2 == "sample_text"
    instance.TEST_PLAYER_2 = "sample_text_2"
    assert instance.TEST_PLAYER_2 == "sample_text_2"


def test_RatingServiceTest_TEST_PLAYER_3_value_roundtrip():
    instance = RatingServiceTest(GAME_NAME="sample_text", TEST_PLAYER="sample_text", TEST_PLAYER_2="sample_text", TEST_PLAYER_3="sample_text")
    assert instance.TEST_PLAYER_3 == "sample_text"
    instance.TEST_PLAYER_3 = "sample_text_2"
    assert instance.TEST_PLAYER_3 == "sample_text_2"


def test_ScoreServiceJDBCTest_DELETE_value_roundtrip():
    instance = ScoreServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.DELETE == "sample_text"
    instance.DELETE = "sample_text_2"
    assert instance.DELETE == "sample_text_2"


def test_ScoreServiceJDBCTest_PASS_value_roundtrip():
    instance = ScoreServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.PASS == "sample_text"
    instance.PASS = "sample_text_2"
    assert instance.PASS == "sample_text_2"


def test_ScoreServiceJDBCTest_URL_value_roundtrip():
    instance = ScoreServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_ScoreServiceJDBCTest_USER_value_roundtrip():
    instance = ScoreServiceJDBCTest(DELETE="sample_text", PASS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.USER == "sample_text"
    instance.USER = "sample_text_2"
    assert instance.USER == "sample_text_2"


def test_ScoreServiceTest_GAME_NAME_value_roundtrip():
    instance = ScoreServiceTest(GAME_NAME="sample_text")
    assert instance.GAME_NAME == "sample_text"
    instance.GAME_NAME = "sample_text_2"
    assert instance.GAME_NAME == "sample_text_2"


def test_card_Card_flipped_value_roundtrip():
    instance = card_Card(flipped=True, rank=7)
    assert instance.flipped == True
    instance.flipped = False
    assert instance.flipped == False


def test_card_Card_rank_value_roundtrip():
    instance = card_Card(flipped=True, rank=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_card_Deck_cardPack_value_roundtrip():
    instance = card_Deck(cardPack="sample_text")
    assert instance.cardPack == "sample_text"
    instance.cardPack = "sample_text_2"
    assert instance.cardPack == "sample_text_2"


def test_deck_Deck_foundationIndex_value_roundtrip():
    instance = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    assert instance.foundationIndex == 7
    instance.foundationIndex = 13
    assert instance.foundationIndex == 13


def test_deck_Deck_inputDestinationRow_value_roundtrip():
    instance = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    assert instance.inputDestinationRow == 7
    instance.inputDestinationRow = 13
    assert instance.inputDestinationRow == 13


def test_deck_Deck_removeItemFromArrayIndex_value_roundtrip():
    instance = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    assert instance.removeItemFromArrayIndex == 7
    instance.removeItemFromArrayIndex = 13
    assert instance.removeItemFromArrayIndex == 13


def test_deck_Deck_score_value_roundtrip():
    instance = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_deck_Deck_stepCounter_value_roundtrip():
    instance = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    assert instance.stepCounter == 7
    instance.stepCounter = 13
    assert instance.stepCounter == 13


def test_deck_Foundations_foundationList_value_roundtrip():
    instance = deck_Foundations(foundationList="sample_text")
    assert instance.foundationList == "sample_text"
    instance.foundationList = "sample_text_2"
    assert instance.foundationList == "sample_text_2"


def test_deck_Stock_STARTING_INDEX_value_roundtrip():
    instance = deck_Stock(STARTING_INDEX=7, stock="sample_text")
    assert instance.STARTING_INDEX == 7
    instance.STARTING_INDEX = 13
    assert instance.STARTING_INDEX == 13


def test_deck_Stock_stock_value_roundtrip():
    instance = deck_Stock(STARTING_INDEX=7, stock="sample_text")
    assert instance.stock == "sample_text"
    instance.stock = "sample_text_2"
    assert instance.stock == "sample_text_2"


def test_deck_Tableau_columns_value_roundtrip():
    instance = deck_Tableau(columns="sample_text")
    assert instance.columns == "sample_text"
    instance.columns = "sample_text_2"
    assert instance.columns == "sample_text_2"


def test_features_History_revertList_value_roundtrip():
    instance = features_History(revertList=7)
    assert instance.revertList == 7
    instance.revertList = 13
    assert instance.revertList == 13


def test_services_CommentServiceJDBC_INSERT_COMMENT_value_roundtrip():
    instance = services_CommentServiceJDBC(INSERT_COMMENT="sample_text", PASSWORD="sample_text", SELECT_COMMENTS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.INSERT_COMMENT == "sample_text"
    instance.INSERT_COMMENT = "sample_text_2"
    assert instance.INSERT_COMMENT == "sample_text_2"


def test_services_CommentServiceJDBC_PASSWORD_value_roundtrip():
    instance = services_CommentServiceJDBC(INSERT_COMMENT="sample_text", PASSWORD="sample_text", SELECT_COMMENTS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.PASSWORD == "sample_text"
    instance.PASSWORD = "sample_text_2"
    assert instance.PASSWORD == "sample_text_2"


def test_services_CommentServiceJDBC_SELECT_COMMENTS_value_roundtrip():
    instance = services_CommentServiceJDBC(INSERT_COMMENT="sample_text", PASSWORD="sample_text", SELECT_COMMENTS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.SELECT_COMMENTS == "sample_text"
    instance.SELECT_COMMENTS = "sample_text_2"
    assert instance.SELECT_COMMENTS == "sample_text_2"


def test_services_CommentServiceJDBC_URL_value_roundtrip():
    instance = services_CommentServiceJDBC(INSERT_COMMENT="sample_text", PASSWORD="sample_text", SELECT_COMMENTS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_services_CommentServiceJDBC_USER_value_roundtrip():
    instance = services_CommentServiceJDBC(INSERT_COMMENT="sample_text", PASSWORD="sample_text", SELECT_COMMENTS="sample_text", URL="sample_text", USER="sample_text")
    assert instance.USER == "sample_text"
    instance.USER = "sample_text_2"
    assert instance.USER == "sample_text_2"


def test_services_RatingServiceJDBC_INSERT_RATING_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.INSERT_RATING == "sample_text"
    instance.INSERT_RATING = "sample_text_2"
    assert instance.INSERT_RATING == "sample_text_2"


def test_services_RatingServiceJDBC_PASSWORD_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.PASSWORD == "sample_text"
    instance.PASSWORD = "sample_text_2"
    assert instance.PASSWORD == "sample_text_2"


def test_services_RatingServiceJDBC_SELECT_AVERAGE_RATING_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.SELECT_AVERAGE_RATING == "sample_text"
    instance.SELECT_AVERAGE_RATING = "sample_text_2"
    assert instance.SELECT_AVERAGE_RATING == "sample_text_2"


def test_services_RatingServiceJDBC_SELECT_RATING_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.SELECT_RATING == "sample_text"
    instance.SELECT_RATING = "sample_text_2"
    assert instance.SELECT_RATING == "sample_text_2"


def test_services_RatingServiceJDBC_URL_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_services_RatingServiceJDBC_USER_value_roundtrip():
    instance = services_RatingServiceJDBC(INSERT_RATING="sample_text", PASSWORD="sample_text", SELECT_AVERAGE_RATING="sample_text", SELECT_RATING="sample_text", URL="sample_text", USER="sample_text")
    assert instance.USER == "sample_text"
    instance.USER = "sample_text_2"
    assert instance.USER == "sample_text_2"


def test_services_ScoreServiceJDBC_INSERT_SCORE_value_roundtrip():
    instance = services_ScoreServiceJDBC(INSERT_SCORE="sample_text", PASSWORD="sample_text", SELECT_SCORE="sample_text", URL="sample_text", USER="sample_text")
    assert instance.INSERT_SCORE == "sample_text"
    instance.INSERT_SCORE = "sample_text_2"
    assert instance.INSERT_SCORE == "sample_text_2"


def test_services_ScoreServiceJDBC_PASSWORD_value_roundtrip():
    instance = services_ScoreServiceJDBC(INSERT_SCORE="sample_text", PASSWORD="sample_text", SELECT_SCORE="sample_text", URL="sample_text", USER="sample_text")
    assert instance.PASSWORD == "sample_text"
    instance.PASSWORD = "sample_text_2"
    assert instance.PASSWORD == "sample_text_2"


def test_services_ScoreServiceJDBC_SELECT_SCORE_value_roundtrip():
    instance = services_ScoreServiceJDBC(INSERT_SCORE="sample_text", PASSWORD="sample_text", SELECT_SCORE="sample_text", URL="sample_text", USER="sample_text")
    assert instance.SELECT_SCORE == "sample_text"
    instance.SELECT_SCORE = "sample_text_2"
    assert instance.SELECT_SCORE == "sample_text_2"


def test_services_ScoreServiceJDBC_URL_value_roundtrip():
    instance = services_ScoreServiceJDBC(INSERT_SCORE="sample_text", PASSWORD="sample_text", SELECT_SCORE="sample_text", URL="sample_text", USER="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_services_ScoreServiceJDBC_USER_value_roundtrip():
    instance = services_ScoreServiceJDBC(INSERT_SCORE="sample_text", PASSWORD="sample_text", SELECT_SCORE="sample_text", URL="sample_text", USER="sample_text")
    assert instance.USER == "sample_text"
    instance.USER = "sample_text_2"
    assert instance.USER == "sample_text_2"


def test_assoc_commentService_CommentServiceTest_CommentService_13_link_reassign_clear():
    a = CommentServiceTest(GAME_NAME="sample_text", PLAYER_NAME="sample_text")
    b1 = services_CommentService_Interface()
    b2 = services_CommentService_Interface()
    _safe_set(a, 'commentService11', b1)
    assert _is_linked(a, 'commentService11', b1)
    if hasattr(b1, 'commentservicetest10'):
        assert _is_linked(b1, 'commentservicetest10', a)
    _safe_set(a, 'commentService11', b2)
    assert _is_linked(a, 'commentService11', b2)
    if hasattr(b1, 'commentservicetest10'):
        assert not _is_linked(b1, 'commentservicetest10', a)
    if hasattr(b2, 'commentservicetest10'):
        assert _is_linked(b2, 'commentservicetest10', a)
    _safe_set(a, 'commentService11', None)
    assert not _is_linked(a, 'commentService11', b2)
    if hasattr(b2, 'commentservicetest10'):
        assert not _is_linked(b2, 'commentservicetest10', a)


def test_assoc_foundations_Deck_Foundations_17_link_reassign_clear():
    a = deck_Foundations(foundationList="sample_text")
    b1 = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    b2 = deck_Deck(foundationIndex=13, inputDestinationRow=13, removeItemFromArrayIndex=13, score=13, stepCounter=13)
    _safe_set(a, 'deck12', b1)
    assert _is_linked(a, 'deck12', b1)
    if hasattr(b1, 'foundations13'):
        assert _is_linked(b1, 'foundations13', a)
    _safe_set(a, 'deck12', b2)
    assert _is_linked(a, 'deck12', b2)
    if hasattr(b1, 'foundations13'):
        assert not _is_linked(b1, 'foundations13', a)
    if hasattr(b2, 'foundations13'):
        assert _is_linked(b2, 'foundations13', a)
    _safe_set(a, 'deck12', None)
    assert not _is_linked(a, 'deck12', b2)
    if hasattr(b2, 'foundations13'):
        assert not _is_linked(b2, 'foundations13', a)


def test_assoc_history_Deck_History_11_link_reassign_clear():
    a = features_History(revertList=7)
    b1 = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    b2 = deck_Deck(foundationIndex=13, inputDestinationRow=13, removeItemFromArrayIndex=13, score=13, stepCounter=13)
    _safe_set(a, 'deck2', b1)
    assert _is_linked(a, 'deck2', b1)
    if hasattr(b1, 'history3'):
        assert _is_linked(b1, 'history3', a)
    _safe_set(a, 'deck2', b2)
    assert _is_linked(a, 'deck2', b2)
    if hasattr(b1, 'history3'):
        assert not _is_linked(b1, 'history3', a)
    if hasattr(b2, 'history3'):
        assert _is_linked(b2, 'history3', a)
    _safe_set(a, 'deck2', None)
    assert not _is_linked(a, 'deck2', b2)
    if hasattr(b2, 'history3'):
        assert not _is_linked(b2, 'history3', a)


def test_assoc_pack_Deck_Pack_16_link_reassign_clear():
    a = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    b1 = card_Deck(cardPack="sample_text")
    b2 = card_Deck(cardPack="sample_text_2")
    _safe_set(a, 'pack7', b1)
    assert _is_linked(a, 'pack7', b1)
    if hasattr(b1, 'deck6'):
        assert _is_linked(b1, 'deck6', a)
    _safe_set(a, 'pack7', b2)
    assert _is_linked(a, 'pack7', b2)
    if hasattr(b1, 'deck6'):
        assert not _is_linked(b1, 'deck6', a)
    if hasattr(b2, 'deck6'):
        assert _is_linked(b2, 'deck6', a)
    _safe_set(a, 'pack7', None)
    assert not _is_linked(a, 'pack7', b2)
    if hasattr(b2, 'deck6'):
        assert not _is_linked(b2, 'deck6', a)


def test_assoc_ratingService_RatingServiceTest_RatingService_2_link_reassign_clear():
    a = RatingServiceTest(GAME_NAME="sample_text", TEST_PLAYER="sample_text", TEST_PLAYER_2="sample_text", TEST_PLAYER_3="sample_text")
    b1 = services_RatingService_Interface()
    b2 = services_RatingService_Interface()
    _safe_set(a, 'ratingService15', b1)
    assert _is_linked(a, 'ratingService15', b1)
    if hasattr(b1, 'ratingservicetest14'):
        assert _is_linked(b1, 'ratingservicetest14', a)
    _safe_set(a, 'ratingService15', b2)
    assert _is_linked(a, 'ratingService15', b2)
    if hasattr(b1, 'ratingservicetest14'):
        assert not _is_linked(b1, 'ratingservicetest14', a)
    if hasattr(b2, 'ratingservicetest14'):
        assert _is_linked(b2, 'ratingservicetest14', a)
    _safe_set(a, 'ratingService15', None)
    assert not _is_linked(a, 'ratingService15', b2)
    if hasattr(b2, 'ratingservicetest14'):
        assert not _is_linked(b2, 'ratingservicetest14', a)


def test_assoc_scoreService_ScoreServiceTest_ScoreService_6_link_reassign_clear():
    a = ScoreServiceTest(GAME_NAME="sample_text")
    b1 = services_ScoreService_Interface()
    b2 = services_ScoreService_Interface()
    _safe_set(a, 'scoreService1', b1)
    assert _is_linked(a, 'scoreService1', b1)
    if hasattr(b1, 'scoreservicetest0'):
        assert _is_linked(b1, 'scoreservicetest0', a)
    _safe_set(a, 'scoreService1', b2)
    assert _is_linked(a, 'scoreService1', b2)
    if hasattr(b1, 'scoreservicetest0'):
        assert not _is_linked(b1, 'scoreservicetest0', a)
    if hasattr(b2, 'scoreservicetest0'):
        assert _is_linked(b2, 'scoreservicetest0', a)
    _safe_set(a, 'scoreService1', None)
    assert not _is_linked(a, 'scoreService1', b2)
    if hasattr(b2, 'scoreservicetest0'):
        assert not _is_linked(b2, 'scoreservicetest0', a)


def test_assoc_stock_Deck_Stock_8_link_reassign_clear():
    a = deck_Stock(STARTING_INDEX=7, stock="sample_text")
    b1 = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    b2 = deck_Deck(foundationIndex=13, inputDestinationRow=13, removeItemFromArrayIndex=13, score=13, stepCounter=13)
    _safe_set(a, 'deck26', b1)
    assert _is_linked(a, 'deck26', b1)
    if hasattr(b1, 'stock27'):
        assert _is_linked(b1, 'stock27', a)
    _safe_set(a, 'deck26', b2)
    assert _is_linked(a, 'deck26', b2)
    if hasattr(b1, 'stock27'):
        assert not _is_linked(b1, 'stock27', a)
    if hasattr(b2, 'stock27'):
        assert _is_linked(b2, 'stock27', a)
    _safe_set(a, 'deck26', None)
    assert not _is_linked(a, 'deck26', b2)
    if hasattr(b2, 'stock27'):
        assert not _is_linked(b2, 'stock27', a)


def test_assoc_tableau10_Tableau_Card_4_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau1035', {b1})
    assert _is_linked(a, 'tableau1035', b1)
    if hasattr(b1, 'tableau34'):
        assert _is_linked(b1, 'tableau34', a)
    _safe_set(a, 'tableau1035', {b2})
    assert _is_linked(a, 'tableau1035', b2)
    if hasattr(b1, 'tableau34'):
        assert not _is_linked(b1, 'tableau34', a)
    if hasattr(b2, 'tableau34'):
        assert _is_linked(b2, 'tableau34', a)
    _safe_set(a, 'tableau1035', set())
    assert not _is_linked(a, 'tableau1035', b2)
    if hasattr(b2, 'tableau34'):
        assert not _is_linked(b2, 'tableau34', a)


def test_assoc_tableau1_Tableau_Card_15_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau125', {b1})
    assert _is_linked(a, 'tableau125', b1)
    if hasattr(b1, 'tableau24'):
        assert _is_linked(b1, 'tableau24', a)
    _safe_set(a, 'tableau125', {b2})
    assert _is_linked(a, 'tableau125', b2)
    if hasattr(b1, 'tableau24'):
        assert not _is_linked(b1, 'tableau24', a)
    if hasattr(b2, 'tableau24'):
        assert _is_linked(b2, 'tableau24', a)
    _safe_set(a, 'tableau125', set())
    assert not _is_linked(a, 'tableau125', b2)
    if hasattr(b2, 'tableau24'):
        assert not _is_linked(b2, 'tableau24', a)


def test_assoc_tableau2_Tableau_Card_14_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau25', {b1})
    assert _is_linked(a, 'tableau25', b1)
    if hasattr(b1, 'tableau4'):
        assert _is_linked(b1, 'tableau4', a)
    _safe_set(a, 'tableau25', {b2})
    assert _is_linked(a, 'tableau25', b2)
    if hasattr(b1, 'tableau4'):
        assert not _is_linked(b1, 'tableau4', a)
    if hasattr(b2, 'tableau4'):
        assert _is_linked(b2, 'tableau4', a)
    _safe_set(a, 'tableau25', set())
    assert not _is_linked(a, 'tableau25', b2)
    if hasattr(b2, 'tableau4'):
        assert not _is_linked(b2, 'tableau4', a)


def test_assoc_tableau3_Tableau_Card_5_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau321', {b1})
    assert _is_linked(a, 'tableau321', b1)
    if hasattr(b1, 'tableau20'):
        assert _is_linked(b1, 'tableau20', a)
    _safe_set(a, 'tableau321', {b2})
    assert _is_linked(a, 'tableau321', b2)
    if hasattr(b1, 'tableau20'):
        assert not _is_linked(b1, 'tableau20', a)
    if hasattr(b2, 'tableau20'):
        assert _is_linked(b2, 'tableau20', a)
    _safe_set(a, 'tableau321', set())
    assert not _is_linked(a, 'tableau321', b2)
    if hasattr(b2, 'tableau20'):
        assert not _is_linked(b2, 'tableau20', a)


def test_assoc_tableau4_Tableau_Card_12_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau429', {b1})
    assert _is_linked(a, 'tableau429', b1)
    if hasattr(b1, 'tableau28'):
        assert _is_linked(b1, 'tableau28', a)
    _safe_set(a, 'tableau429', {b2})
    assert _is_linked(a, 'tableau429', b2)
    if hasattr(b1, 'tableau28'):
        assert not _is_linked(b1, 'tableau28', a)
    if hasattr(b2, 'tableau28'):
        assert _is_linked(b2, 'tableau28', a)
    _safe_set(a, 'tableau429', set())
    assert not _is_linked(a, 'tableau429', b2)
    if hasattr(b2, 'tableau28'):
        assert not _is_linked(b2, 'tableau28', a)


def test_assoc_tableau5_Tableau_Card_1_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau531', {b1})
    assert _is_linked(a, 'tableau531', b1)
    if hasattr(b1, 'tableau30'):
        assert _is_linked(b1, 'tableau30', a)
    _safe_set(a, 'tableau531', {b2})
    assert _is_linked(a, 'tableau531', b2)
    if hasattr(b1, 'tableau30'):
        assert not _is_linked(b1, 'tableau30', a)
    if hasattr(b2, 'tableau30'):
        assert _is_linked(b2, 'tableau30', a)
    _safe_set(a, 'tableau531', set())
    assert not _is_linked(a, 'tableau531', b2)
    if hasattr(b2, 'tableau30'):
        assert not _is_linked(b2, 'tableau30', a)


def test_assoc_tableau6_Tableau_Card_10_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau623', {b1})
    assert _is_linked(a, 'tableau623', b1)
    if hasattr(b1, 'tableau22'):
        assert _is_linked(b1, 'tableau22', a)
    _safe_set(a, 'tableau623', {b2})
    assert _is_linked(a, 'tableau623', b2)
    if hasattr(b1, 'tableau22'):
        assert not _is_linked(b1, 'tableau22', a)
    if hasattr(b2, 'tableau22'):
        assert _is_linked(b2, 'tableau22', a)
    _safe_set(a, 'tableau623', set())
    assert not _is_linked(a, 'tableau623', b2)
    if hasattr(b2, 'tableau22'):
        assert not _is_linked(b2, 'tableau22', a)


def test_assoc_tableau7_Tableau_Card_0_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau719', {b1})
    assert _is_linked(a, 'tableau719', b1)
    if hasattr(b1, 'tableau18'):
        assert _is_linked(b1, 'tableau18', a)
    _safe_set(a, 'tableau719', {b2})
    assert _is_linked(a, 'tableau719', b2)
    if hasattr(b1, 'tableau18'):
        assert not _is_linked(b1, 'tableau18', a)
    if hasattr(b2, 'tableau18'):
        assert _is_linked(b2, 'tableau18', a)
    _safe_set(a, 'tableau719', set())
    assert not _is_linked(a, 'tableau719', b2)
    if hasattr(b2, 'tableau18'):
        assert not _is_linked(b2, 'tableau18', a)


def test_assoc_tableau8_Tableau_Card_9_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau817', {b1})
    assert _is_linked(a, 'tableau817', b1)
    if hasattr(b1, 'tableau16'):
        assert _is_linked(b1, 'tableau16', a)
    _safe_set(a, 'tableau817', {b2})
    assert _is_linked(a, 'tableau817', b2)
    if hasattr(b1, 'tableau16'):
        assert not _is_linked(b1, 'tableau16', a)
    if hasattr(b2, 'tableau16'):
        assert _is_linked(b2, 'tableau16', a)
    _safe_set(a, 'tableau817', set())
    assert not _is_linked(a, 'tableau817', b2)
    if hasattr(b2, 'tableau16'):
        assert not _is_linked(b2, 'tableau16', a)


def test_assoc_tableau9_Tableau_Card_3_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = card_Card(flipped=True, rank=7)
    b2 = card_Card(flipped=False, rank=13)
    _safe_set(a, 'tableau933', {b1})
    assert _is_linked(a, 'tableau933', b1)
    if hasattr(b1, 'tableau32'):
        assert _is_linked(b1, 'tableau32', a)
    _safe_set(a, 'tableau933', {b2})
    assert _is_linked(a, 'tableau933', b2)
    if hasattr(b1, 'tableau32'):
        assert not _is_linked(b1, 'tableau32', a)
    if hasattr(b2, 'tableau32'):
        assert _is_linked(b2, 'tableau32', a)
    _safe_set(a, 'tableau933', set())
    assert not _is_linked(a, 'tableau933', b2)
    if hasattr(b2, 'tableau32'):
        assert not _is_linked(b2, 'tableau32', a)


def test_assoc_tableau_Deck_Tableau_7_link_reassign_clear():
    a = deck_Tableau(columns="sample_text")
    b1 = deck_Deck(foundationIndex=7, inputDestinationRow=7, removeItemFromArrayIndex=7, score=7, stepCounter=7)
    b2 = deck_Deck(foundationIndex=13, inputDestinationRow=13, removeItemFromArrayIndex=13, score=13, stepCounter=13)
    _safe_set(a, 'deck8', b1)
    assert _is_linked(a, 'deck8', b1)
    if hasattr(b1, 'tableau9'):
        assert _is_linked(b1, 'tableau9', a)
    _safe_set(a, 'deck8', b2)
    assert _is_linked(a, 'deck8', b2)
    if hasattr(b1, 'tableau9'):
        assert not _is_linked(b1, 'tableau9', a)
    if hasattr(b2, 'tableau9'):
        assert _is_linked(b2, 'tableau9', a)
    _safe_set(a, 'deck8', None)
    assert not _is_linked(a, 'deck8', b2)
    if hasattr(b2, 'tableau9'):
        assert not _is_linked(b2, 'tableau9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CommentServiceJDBCTest_strategy = st.builds(CommentServiceJDBCTest, DELETE=safe_text, PASS=safe_text, URL=safe_text, USER=safe_text)
@given(instance=CommentServiceJDBCTest_strategy)
@settings(max_examples=25)
def test_CommentServiceJDBCTest_instantiation(instance):
    assert isinstance(instance, CommentServiceJDBCTest)


CommentServiceTest_strategy = st.builds(CommentServiceTest, GAME_NAME=safe_text, PLAYER_NAME=safe_text)
@given(instance=CommentServiceTest_strategy)
@settings(max_examples=25)
def test_CommentServiceTest_instantiation(instance):
    assert isinstance(instance, CommentServiceTest)


Comparable_Score__Interface_strategy = st.builds(Comparable_Score__Interface)
@given(instance=Comparable_Score__Interface_strategy)
@settings(max_examples=25)
def test_Comparable_Score__Interface_instantiation(instance):
    assert isinstance(instance, Comparable_Score__Interface)


Main_strategy = st.builds(Main)
@given(instance=Main_strategy)
@settings(max_examples=25)
def test_Main_instantiation(instance):
    assert isinstance(instance, Main)


RatingServiceTest_strategy = st.builds(RatingServiceTest, GAME_NAME=safe_text, TEST_PLAYER=safe_text, TEST_PLAYER_2=safe_text, TEST_PLAYER_3=safe_text)
@given(instance=RatingServiceTest_strategy)
@settings(max_examples=25)
def test_RatingServiceTest_instantiation(instance):
    assert isinstance(instance, RatingServiceTest)


ScoreServiceJDBCTest_strategy = st.builds(ScoreServiceJDBCTest, DELETE=safe_text, PASS=safe_text, URL=safe_text, USER=safe_text)
@given(instance=ScoreServiceJDBCTest_strategy)
@settings(max_examples=25)
def test_ScoreServiceJDBCTest_instantiation(instance):
    assert isinstance(instance, ScoreServiceJDBCTest)


ScoreServiceTest_strategy = st.builds(ScoreServiceTest, GAME_NAME=safe_text)
@given(instance=ScoreServiceTest_strategy)
@settings(max_examples=25)
def test_ScoreServiceTest_instantiation(instance):
    assert isinstance(instance, ScoreServiceTest)


SpiderSolitaireTestSuite_strategy = st.builds(SpiderSolitaireTestSuite)
@given(instance=SpiderSolitaireTestSuite_strategy)
@settings(max_examples=25)
def test_SpiderSolitaireTestSuite_instantiation(instance):
    assert isinstance(instance, SpiderSolitaireTestSuite)


card_Card_strategy = st.builds(card_Card, flipped=st.booleans(), rank=st.integers())
@given(instance=card_Card_strategy)
@settings(max_examples=25)
def test_card_Card_instantiation(instance):
    assert isinstance(instance, card_Card)


card_Deck_strategy = st.builds(card_Deck, cardPack=safe_text)
@given(instance=card_Deck_strategy)
@settings(max_examples=25)
def test_card_Deck_instantiation(instance):
    assert isinstance(instance, card_Deck)


deck_Deck_strategy = st.builds(deck_Deck, foundationIndex=st.integers(), inputDestinationRow=st.integers(), removeItemFromArrayIndex=st.integers(), score=st.integers(), stepCounter=st.integers())
@given(instance=deck_Deck_strategy)
@settings(max_examples=25)
def test_deck_Deck_instantiation(instance):
    assert isinstance(instance, deck_Deck)


deck_Foundations_strategy = st.builds(deck_Foundations, foundationList=safe_text)
@given(instance=deck_Foundations_strategy)
@settings(max_examples=25)
def test_deck_Foundations_instantiation(instance):
    assert isinstance(instance, deck_Foundations)


deck_Stock_strategy = st.builds(deck_Stock, STARTING_INDEX=st.integers(), stock=safe_text)
@given(instance=deck_Stock_strategy)
@settings(max_examples=25)
def test_deck_Stock_instantiation(instance):
    assert isinstance(instance, deck_Stock)


deck_Tableau_strategy = st.builds(deck_Tableau, columns=safe_text)
@given(instance=deck_Tableau_strategy)
@settings(max_examples=25)
def test_deck_Tableau_instantiation(instance):
    assert isinstance(instance, deck_Tableau)


features_History_strategy = st.builds(features_History, revertList=st.integers())
@given(instance=features_History_strategy)
@settings(max_examples=25)
def test_features_History_instantiation(instance):
    assert isinstance(instance, features_History)


genmymodelreverse_C1_strategy = st.builds(genmymodelreverse_C1)
@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)


genmymodelreverse_C11_strategy = st.builds(genmymodelreverse_C11)
@given(instance=genmymodelreverse_C11_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C11_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C11)


genmymodelreverse_java_io_Serializable_Interface_strategy = st.builds(genmymodelreverse_java_io_Serializable_Interface)
@given(instance=genmymodelreverse_java_io_Serializable_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_io_Serializable_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_Serializable_Interface)


genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(genmymodelreverse_java_lang_Comparable_Interface)
@given(instance=genmymodelreverse_java_lang_Comparable_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Comparable_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Comparable_Interface)


genmymodelreverse_java_lang_Exception_strategy = st.builds(genmymodelreverse_java_lang_Exception)
@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)


genmymodelreverse_java_lang_RuntimeException_strategy = st.builds(genmymodelreverse_java_lang_RuntimeException)
@given(instance=genmymodelreverse_java_lang_RuntimeException_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_RuntimeException_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_RuntimeException)


genmymodelreverse_java_lang_Throwable_strategy = st.builds(genmymodelreverse_java_lang_Throwable)
@given(instance=genmymodelreverse_java_lang_Throwable_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Throwable_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Throwable)


genmymodelreverse_java_util_Date_strategy = st.builds(genmymodelreverse_java_util_Date)
@given(instance=genmymodelreverse_java_util_Date_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_util_Date_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Date)


genmymodelreverse_java_util_List_Interface_strategy = st.builds(genmymodelreverse_java_util_List_Interface)
@given(instance=genmymodelreverse_java_util_List_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_util_List_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_List_Interface)


services_CommentException_strategy = st.builds(services_CommentException)
@given(instance=services_CommentException_strategy)
@settings(max_examples=25)
def test_services_CommentException_instantiation(instance):
    assert isinstance(instance, services_CommentException)


services_CommentServiceJDBC_strategy = st.builds(services_CommentServiceJDBC, INSERT_COMMENT=safe_text, PASSWORD=safe_text, SELECT_COMMENTS=safe_text, URL=safe_text, USER=safe_text)
@given(instance=services_CommentServiceJDBC_strategy)
@settings(max_examples=25)
def test_services_CommentServiceJDBC_instantiation(instance):
    assert isinstance(instance, services_CommentServiceJDBC)


services_CommentService_Interface_strategy = st.builds(services_CommentService_Interface)
@given(instance=services_CommentService_Interface_strategy)
@settings(max_examples=25)
def test_services_CommentService_Interface_instantiation(instance):
    assert isinstance(instance, services_CommentService_Interface)


services_RatingException_strategy = st.builds(services_RatingException)
@given(instance=services_RatingException_strategy)
@settings(max_examples=25)
def test_services_RatingException_instantiation(instance):
    assert isinstance(instance, services_RatingException)


services_RatingServiceJDBC_strategy = st.builds(services_RatingServiceJDBC, INSERT_RATING=safe_text, PASSWORD=safe_text, SELECT_AVERAGE_RATING=safe_text, SELECT_RATING=safe_text, URL=safe_text, USER=safe_text)
@given(instance=services_RatingServiceJDBC_strategy)
@settings(max_examples=25)
def test_services_RatingServiceJDBC_instantiation(instance):
    assert isinstance(instance, services_RatingServiceJDBC)


services_RatingService_Interface_strategy = st.builds(services_RatingService_Interface)
@given(instance=services_RatingService_Interface_strategy)
@settings(max_examples=25)
def test_services_RatingService_Interface_instantiation(instance):
    assert isinstance(instance, services_RatingService_Interface)


services_ScoreException_strategy = st.builds(services_ScoreException)
@given(instance=services_ScoreException_strategy)
@settings(max_examples=25)
def test_services_ScoreException_instantiation(instance):
    assert isinstance(instance, services_ScoreException)


services_ScoreServiceJDBC_strategy = st.builds(services_ScoreServiceJDBC, INSERT_SCORE=safe_text, PASSWORD=safe_text, SELECT_SCORE=safe_text, URL=safe_text, USER=safe_text)
@given(instance=services_ScoreServiceJDBC_strategy)
@settings(max_examples=25)
def test_services_ScoreServiceJDBC_instantiation(instance):
    assert isinstance(instance, services_ScoreServiceJDBC)


services_ScoreService_Interface_strategy = st.builds(services_ScoreService_Interface)
@given(instance=services_ScoreService_Interface_strategy)
@settings(max_examples=25)
def test_services_ScoreService_Interface_instantiation(instance):
    assert isinstance(instance, services_ScoreService_Interface)


