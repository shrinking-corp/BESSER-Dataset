from python_code import activator_Greeting
from python_code import activator_Model

def test_activator_Greeting___init__():
    assert activator_Greeting.__init__(activator_Greeting('', activator_Greeting=activator_Model()), '', activator_Greeting=activator_Model()) == None

