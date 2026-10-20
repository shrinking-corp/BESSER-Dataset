from python_code import imported_model_Book
from python_code import imported_model_Library

def test_imported_model_Book___init__():
    assert imported_model_Book.__init__(imported_model_Book(0, imported_model_Book=imported_model_Library()), 0, imported_model_Book=imported_model_Library()) == None

