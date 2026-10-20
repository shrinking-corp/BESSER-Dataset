from python_code import b_B
from python_code import b_Model

def test_b_B___init__():
    assert b_B.__init__(b_B('', b_B=b_Model()), '', b_B=b_Model()) == None


from python_code import b_Model
from python_code import b_Y

def test_b_Y___init__():
    assert b_Y.__init__(b_Y('', '\x00', b_Y=b_Model()), '\x00\x00', '', b_Y=b_Model()) == None

