from python_code import myDsl2_Greeting
from python_code import myDsl2_Model

def test_myDsl2_Greeting___init__():
    assert myDsl2_Greeting.__init__(myDsl2_Greeting('', myDsl2_Greeting=myDsl2_Model()), '', myDsl2_Greeting=myDsl2_Model()) == None

