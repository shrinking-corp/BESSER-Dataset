from python_code import CommentServiceJDBCTest

def test_CommentServiceJDBCTest___init__():
    assert CommentServiceJDBCTest.__init__(CommentServiceJDBCTest('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import CommentServiceTest
from python_code import services_CommentService_Interface

def test_CommentServiceTest___init__():
    assert CommentServiceTest.__init__(CommentServiceTest('', '\x00', commentService11=services_CommentService_Interface()), '\x00\x00', '', commentService11=services_CommentService_Interface()) == None


from python_code import RatingServiceTest
from python_code import services_RatingService_Interface

def test_RatingServiceTest___init__():
    assert RatingServiceTest.__init__(RatingServiceTest('\x00\x00', '', '', '', ratingService15=services_RatingService_Interface()), '', '', '', '', ratingService15=services_RatingService_Interface()) == None


from python_code import ScoreServiceJDBCTest

def test_ScoreServiceJDBCTest___init__():
    assert ScoreServiceJDBCTest.__init__(ScoreServiceJDBCTest('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ScoreServiceTest
from python_code import services_ScoreService_Interface

def test_ScoreServiceTest___init__():
    assert ScoreServiceTest.__init__(ScoreServiceTest('', scoreService1=services_ScoreService_Interface()), '', scoreService1=services_ScoreService_Interface()) == None


from python_code import entities_Comment
from python_code import genmymodelreverse_java_util_Date

def test_entities_Comment___init__():
    assert entities_Comment.__init__(entities_Comment('', '', '\x00\x00', genmymodelreverse_java_util_Date()), '', '', '', genmymodelreverse_java_util_Date()) == None


from python_code import entities_Rating
from python_code import genmymodelreverse_java_util_Date

def test_entities_Rating___init__():
    assert entities_Rating.__init__(entities_Rating('', '', 0, genmymodelreverse_java_util_Date()), '\x00', '', 0, genmymodelreverse_java_util_Date()) == None


from python_code import entities_Score
from python_code import genmymodelreverse_java_util_Date

def test_entities_Score___init__():
    assert entities_Score.__init__(entities_Score('', '', 0, genmymodelreverse_java_util_Date()), '\x00', '', 0, genmymodelreverse_java_util_Date()) == None


from python_code import services_CommentServiceJDBC

def test_services_CommentServiceJDBC___init__():
    assert services_CommentServiceJDBC.__init__(services_CommentServiceJDBC('', '', '', '', ''), '', '', '', '', '') == None


from python_code import services_RatingServiceJDBC

def test_services_RatingServiceJDBC___init__():
    assert services_RatingServiceJDBC.__init__(services_RatingServiceJDBC('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import services_ScoreServiceJDBC

def test_services_ScoreServiceJDBC___init__():
    assert services_ScoreServiceJDBC.__init__(services_ScoreServiceJDBC('', '', '', '', ''), '', '', '', '', '') == None

