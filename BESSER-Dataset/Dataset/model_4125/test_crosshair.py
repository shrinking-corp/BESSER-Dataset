from python_code import model_IPerson
from python_code import model_IPersonList

def test_model_IPerson___init__():
    assert model_IPerson.__init__(model_IPerson('', model_IPerson=model_IPersonList()), '', model_IPerson=model_IPersonList()) == None

