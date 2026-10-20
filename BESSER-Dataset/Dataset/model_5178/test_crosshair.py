from python_code import b_B
from python_code import b_Model

def test_b_B___init__():
    assert b_B.__init__(b_B('', b_B=b_Model()), '', b_B=b_Model()) == None


from python_code import b_Ebook
from python_code import b_Model

def test_b_Ebook___init__():
    assert b_Ebook.__init__(b_Ebook('\x00\x00', '', '', '', b_Ebook=b_Model()), '', '', '', '', b_Ebook=b_Model()) == None

