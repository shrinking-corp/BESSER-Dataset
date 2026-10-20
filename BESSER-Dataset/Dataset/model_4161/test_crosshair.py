from python_code import scheme_Greeting
from python_code import scheme_Model

def test_scheme_Greeting___init__():
    assert scheme_Greeting.__init__(scheme_Greeting('', scheme_Greeting=scheme_Model()), '', scheme_Greeting=scheme_Model()) == None

