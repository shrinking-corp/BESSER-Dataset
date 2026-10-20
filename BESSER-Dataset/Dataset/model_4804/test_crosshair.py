from python_code import model_IHost
from python_code import model_INetwork

def test_model_IHost___init__():
    assert model_IHost.__init__(model_IHost('\x00\x00', '', model_IHost=model_INetwork(), model_IHost3=set()), '', '', model_IHost=model_INetwork(), model_IHost3=set()) == None

