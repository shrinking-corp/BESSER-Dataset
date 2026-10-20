from python_code import myDsl_Greeting
from python_code import myDsl_Model

def test_myDsl_Greeting___init__():
    assert myDsl_Greeting.__init__(myDsl_Greeting('\x00', myDsl_Greeting=myDsl_Model(), myDsl_Greeting2=set()), '', myDsl_Greeting=myDsl_Model(), myDsl_Greeting2=set()) == None

