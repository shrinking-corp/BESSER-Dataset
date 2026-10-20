from python_code import Algorithm

def test_Algorithm___init__():
    assert Algorithm.__init__(Algorithm(''), '') == None


from python_code import Building
from python_code import Controller

def test_Building___init__():
    assert Building.__init__(Building('', Controller(), elevatorBay6=set(), controller10=Controller()), '', Controller(), elevatorBay6=set(), controller10=Controller()) == None

