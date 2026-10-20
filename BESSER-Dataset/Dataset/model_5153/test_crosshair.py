from python_code import mytest_A
from python_code import mytest_MyRoot

def test_mytest_A___init__():
    assert mytest_A.__init__(mytest_A('', mytest_A=mytest_MyRoot()), '', mytest_A=mytest_MyRoot()) == None


from python_code import mytest_B
from python_code import mytest_MyRoot

def test_mytest_B___init__():
    assert mytest_B.__init__(mytest_B('', mytest_B=mytest_MyRoot(), mytest_B5=mytest_MyRoot()), '', mytest_B=mytest_MyRoot(), mytest_B5=mytest_MyRoot()) == None

