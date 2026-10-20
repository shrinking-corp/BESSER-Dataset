from python_code import myDsl_Greeting
from python_code import myDsl_Model

def test_myDsl_Greeting___init__():
    assert myDsl_Greeting.__init__(myDsl_Greeting('', myDsl_Greeting=myDsl_Model()), '', myDsl_Greeting=myDsl_Model()) == None

