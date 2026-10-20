from python_code import a_A
from python_code import a_Model

def test_a_A___init__():
    assert a_A.__init__(a_A('', a_A=a_Model()), '', a_A=a_Model()) == None


from python_code import a_Book
from python_code import a_Model

def test_a_Book___init__():
    assert a_Book.__init__(a_Book('', '', '\x00\x00', a_Book=a_Model()), '', '', '', a_Book=a_Model()) == None

