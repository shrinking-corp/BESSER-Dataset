from python_code import writers_Catalog
from python_code import writers_Writer

def test_writers_Writer___init__():
    assert writers_Writer.__init__(writers_Writer('', writers_Writer=writers_Catalog(), authors=set()), '', writers_Writer=writers_Catalog(), authors=set()) == None

