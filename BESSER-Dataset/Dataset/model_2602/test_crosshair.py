from python_code import model_Person
from python_code import model_PersonList
from python_code import model_Root

def test_model_Person___init__():
    assert model_Person.__init__(model_Person('', model_Person=model_PersonList(), model_Person2=model_Root()), '', model_Person=model_PersonList(), model_Person2=model_Root()) == None

