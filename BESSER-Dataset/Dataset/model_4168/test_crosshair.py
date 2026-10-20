from python_code import comp_Greeting
from python_code import comp_Model

def test_comp_Greeting___init__():
    assert comp_Greeting.__init__(comp_Greeting('', comp_Greeting=comp_Model()), '', comp_Greeting=comp_Model()) == None

