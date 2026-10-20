from python_code import myDsl1_Greeting
from python_code import myDsl1_Model

def test_myDsl1_Greeting___init__():
    assert myDsl1_Greeting.__init__(myDsl1_Greeting('', myDsl1_Greeting=myDsl1_Model()), '', myDsl1_Greeting=myDsl1_Model()) == None

