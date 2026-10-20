from python_code import mydsl_Greeting
from python_code import mydsl_Model

def test_mydsl_Greeting___init__():
    assert mydsl_Greeting.__init__(mydsl_Greeting('', mydsl_Greeting=mydsl_Model()), '', mydsl_Greeting=mydsl_Model()) == None

