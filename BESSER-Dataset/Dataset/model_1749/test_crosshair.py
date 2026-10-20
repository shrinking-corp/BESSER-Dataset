from python_code import model_Book
from python_code import model_Library

def test_model_Book___init__():
    assert model_Book.__init__(model_Book('', model_Book=model_Library(), model_Book2=set()), '', model_Book=model_Library(), model_Book2=set()) == None

