from python_code import bookstore_Ent
from python_code import bookstore_Model

def test_bookstore_Ent___init__():
    assert bookstore_Ent.__init__(bookstore_Ent('', bookstore_Ent=bookstore_Model()), '', bookstore_Ent=bookstore_Model()) == None

