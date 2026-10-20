from python_code import myDsl_AbstractGreeting
from python_code import myDsl_GreetingReference
from python_code import myDsl_Model

def test_myDsl_AbstractGreeting___init__():
    assert myDsl_AbstractGreeting.__init__(myDsl_AbstractGreeting('', myDsl_AbstractGreeting=myDsl_Model(), myDsl_AbstractGreeting2=myDsl_GreetingReference()), '', myDsl_AbstractGreeting=myDsl_Model(), myDsl_AbstractGreeting2=myDsl_GreetingReference()) == None

