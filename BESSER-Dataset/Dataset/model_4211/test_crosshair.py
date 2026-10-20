from python_code import myDsl_Greeting
from python_code import myDsl_Person

def test_myDsl_Person___init__():
    assert myDsl_Person.__init__(myDsl_Person('', myDsl_Person=myDsl_Greeting()), '', myDsl_Person=myDsl_Greeting()) == None

