from python_code import types_Library
from python_code import types_Type

def test_types_Library___init__():
    assert types_Library.__init__(types_Library('', owningLibrary=set(), Library=types_Type()), '', owningLibrary=set(), Library=types_Type()) == None

