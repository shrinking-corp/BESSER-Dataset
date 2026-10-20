from python_code import mytest_A
from python_code import mytest_B
from python_code import mytest_MyRoot

def test_mytest_A___init__():
    assert mytest_A.__init__(mytest_A('', a=mytest_B(), A=mytest_B(), mytest_A=mytest_MyRoot()), '', a=mytest_B(), A=mytest_B(), mytest_A=mytest_MyRoot()) == None

