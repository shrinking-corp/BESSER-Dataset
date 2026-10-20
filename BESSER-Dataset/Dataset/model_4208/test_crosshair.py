from python_code import myDsl_Conditional

def test_myDsl_Conditional___init__():
    assert myDsl_Conditional.__init__(myDsl_Conditional(0, 0), 0, 0) == None


from python_code import myDsl_Greeting
from python_code import myDsl_Model

def test_myDsl_Greeting___init__():
    assert myDsl_Greeting.__init__(myDsl_Greeting(0, '\x00', myDsl_Greeting=myDsl_Model()), 0, '\x00', myDsl_Greeting=myDsl_Model()) == None


from python_code import myDsl_Operation

def test_myDsl_Operation___init__():
    assert myDsl_Operation.__init__(myDsl_Operation('', 0), '', 0) == None

