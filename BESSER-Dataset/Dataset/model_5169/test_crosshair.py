from python_code import b_B
from python_code import b_Model

def test_b_B___init__():
    assert b_B.__init__(b_B('', b_B=b_Model()), '', b_B=b_Model()) == None

