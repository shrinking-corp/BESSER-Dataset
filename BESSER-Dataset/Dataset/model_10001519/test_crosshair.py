from python_code import Department

def test_Department___init__():
    assert Department.__init__(Department('', '', '', belongs_to3=set()), '', '', '', belongs_to3=set()) == None

