from python_code import petrinet_Place
from python_code import petrinet_Token

def test_petrinet_Token___init__():
    assert petrinet_Token.__init__(petrinet_Token('', petrinet_Token=petrinet_Place()), '', petrinet_Token=petrinet_Place()) == None

