from python_code import prolog_Greeting
from python_code import prolog_Model

def test_prolog_Greeting___init__():
    assert prolog_Greeting.__init__(prolog_Greeting('', prolog_Greeting=prolog_Model()), '', prolog_Greeting=prolog_Model()) == None

