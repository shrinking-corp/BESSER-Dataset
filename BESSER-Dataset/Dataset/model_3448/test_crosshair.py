from python_code import test_Employee

def test_test_Employee___init__():
    assert test_Employee.__init__(test_Employee(''), '') == None


from python_code import test_Student

def test_test_Student___init__():
    assert test_Student.__init__(test_Student(''), '') == None


from python_code import test_University

def test_test_University___init__():
    assert test_University.__init__(test_University('', test_University=set()), '', test_University=set()) == None

