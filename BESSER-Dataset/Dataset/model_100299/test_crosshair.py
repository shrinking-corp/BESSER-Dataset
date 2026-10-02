from python_code import petrinet_GeometryLabel
from python_code import petrinet_Place

def test_petrinet_GeometryLabel___init__():
    assert petrinet_GeometryLabel.__init__(petrinet_GeometryLabel('', petrinet_GeometryLabel=petrinet_Place()), '', petrinet_GeometryLabel=petrinet_Place()) == None

from python_code import petrinet_Arc
from python_code import petrinet_Identity

def test_petrinet_Identity___init__():
    assert petrinet_Identity.__init__(petrinet_Identity('', petrinet_Identity=petrinet_Arc()), '', petrinet_Identity=petrinet_Arc()) == None

from python_code import petrinet_InputPlace
from python_code import petrinet_Place

def test_petrinet_InputPlace___init__():
    assert petrinet_InputPlace.__init__(petrinet_InputPlace(True, petrinet_InputPlace=petrinet_Place()), False, petrinet_InputPlace=petrinet_Place()) == None

from python_code import petrinet_Place
from python_code import petrinet_Token

def test_petrinet_Token___init__():
    assert petrinet_Token.__init__(petrinet_Token('', petrinet_Token=petrinet_Place()), '', petrinet_Token=petrinet_Place()) == None
