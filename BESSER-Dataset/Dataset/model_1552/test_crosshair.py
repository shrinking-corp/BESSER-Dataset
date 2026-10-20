import datetime as _ch_datetime
from python_code import reviews_Dated

def test_reviews_Dated___init__():
    assert reviews_Dated.__init__(reviews_Dated(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None


from python_code import reviews_FileItem
from python_code import reviews_FileVersion

def test_reviews_FileVersion___init__():
    assert reviews_FileVersion.__init__(reviews_FileVersion('', '', '', '', '', reviews_FileVersion=reviews_FileItem(), reviews_FileVersion51=reviews_FileItem(), reviews_FileVersion60=reviews_FileItem()), '', '', '', '', '', reviews_FileVersion=reviews_FileItem(), reviews_FileVersion51=reviews_FileItem(), reviews_FileVersion60=reviews_FileItem()) == None


from python_code import reviews_Indexed

def test_reviews_Indexed___init__():
    assert reviews_Indexed.__init__(reviews_Indexed(''), '') == None


from python_code import reviews_LineLocation

def test_reviews_LineLocation___init__():
    assert reviews_LineLocation.__init__(reviews_LineLocation(0, 0, reviews_LineLocation=set()), 0, 0, reviews_LineLocation=set()) == None


from python_code import reviews_FileItem
from python_code import reviews_Review
from python_code import reviews_ReviewItemSet

def test_reviews_ReviewItemSet___init__():
    assert reviews_ReviewItemSet.__init__(reviews_ReviewItemSet('', False, ReviewItemSet53=reviews_FileItem(), set=set(), sets=reviews_Review(), reviews_ReviewItemSet=set(), ReviewItemSet=reviews_Review()), '', True, ReviewItemSet53=reviews_FileItem(), set=set(), sets=reviews_Review(), reviews_ReviewItemSet=set(), ReviewItemSet=reviews_Review()) == None

