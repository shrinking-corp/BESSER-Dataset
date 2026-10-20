from python_code import myDsl_Greeting
from python_code import myDsl_Model

def test_myDsl_Greeting___init__():
    assert myDsl_Greeting.__init__(myDsl_Greeting('', myDsl_Greeting=myDsl_Model()), '', myDsl_Greeting=myDsl_Model()) == None


from python_code import myDsl_TypeA

def test_myDsl_TypeA___init__():
    assert myDsl_TypeA.__init__(myDsl_TypeA(''), '') == None


from python_code import myDsl_TypeB

def test_myDsl_TypeB___init__():
    assert myDsl_TypeB.__init__(myDsl_TypeB(''), '') == None

