from python_code import myDslA_Greeting
from python_code import myDslA_Model

def test_myDslA_Greeting___init__():
    assert myDslA_Greeting.__init__(myDslA_Greeting('', myDslA_Greeting=myDslA_Model()), '', myDslA_Greeting=myDslA_Model()) == None

