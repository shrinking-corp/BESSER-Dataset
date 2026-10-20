import datetime as _ch_datetime
from python_code import tinylibrary_Book
from python_code import tinylibrary_Library
from python_code import tinylibrary_Writer

def test_tinylibrary_Book___init__():
    assert tinylibrary_Book.__init__(tinylibrary_Book('', '', '', '', _ch_datetime.date(1, 1, 1), '', tinylibrary_Book=tinylibrary_Library(), Book=tinylibrary_Writer(), books=set()), '', '', '\x00', '', _ch_datetime.date(1, 1, 1), '', tinylibrary_Book=tinylibrary_Library(), Book=tinylibrary_Writer(), books=set()) == None


from python_code import tinylibrary_Person

def test_tinylibrary_Person___init__():
    assert tinylibrary_Person.__init__(tinylibrary_Person('', '', '\x00\x00'), '', '', '') == None

