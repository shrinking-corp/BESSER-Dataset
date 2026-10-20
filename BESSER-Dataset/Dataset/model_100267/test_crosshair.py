from python_code import PetriNet_Arc
from python_code import PetriNet_PetriNet

def test_PetriNet_Arc___init__():
    assert PetriNet_Arc.__init__(PetriNet_Arc(0, PetriNet_Arc=PetriNet_PetriNet()), 0, PetriNet_Arc=PetriNet_PetriNet()) == None


from python_code import PetriNet_IdentifiableElement

def test_PetriNet_IdentifiableElement___init__():
    assert PetriNet_IdentifiableElement.__init__(PetriNet_IdentifiableElement('', '\x00'), '\x00\x00', '') == None


from python_code import PetriNet_Place
from python_code import PetriNet_Token

def test_PetriNet_Token___init__():
    assert PetriNet_Token.__init__(PetriNet_Token('', PetriNet_Token=PetriNet_Place()), '', PetriNet_Token=PetriNet_Place()) == None


from python_code import PetriNet_PetriNet
from python_code import PetriNet_Place
from python_code import PetriNet_Type

def test_PetriNet_Type___init__():
    assert PetriNet_Type.__init__(PetriNet_Type('', PetriNet_Type=PetriNet_PetriNet(), PetriNet_Type8=set(), PetriNet_Type13=PetriNet_Place()), '', PetriNet_Type=PetriNet_PetriNet(), PetriNet_Type8=set(), PetriNet_Type13=PetriNet_Place()) == None

