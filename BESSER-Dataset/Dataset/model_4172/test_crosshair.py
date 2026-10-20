from python_code import hello_Greeting
from python_code import hello_Model

def test_hello_Greeting___init__():
    assert hello_Greeting.__init__(hello_Greeting('', hello_Greeting=hello_Model()), '', hello_Greeting=hello_Model()) == None

