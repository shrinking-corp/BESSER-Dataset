from python_code import extendedpetrinet_GeometryLabel
from python_code import extendedpetrinet_Place

def test_extendedpetrinet_GeometryLabel___init__():
    assert extendedpetrinet_GeometryLabel.__init__(extendedpetrinet_GeometryLabel('', extendedpetrinet_GeometryLabel=extendedpetrinet_Place()), '', extendedpetrinet_GeometryLabel=extendedpetrinet_Place()) == None


from python_code import extendedpetrinet_Arc
from python_code import extendedpetrinet_Identity

def test_extendedpetrinet_Identity___init__():
    assert extendedpetrinet_Identity.__init__(extendedpetrinet_Identity(0, extendedpetrinet_Identity=extendedpetrinet_Arc()), 0, extendedpetrinet_Identity=extendedpetrinet_Arc()) == None


from python_code import extendedpetrinet_InputPlaceAppearance
from python_code import extendedpetrinet_Place

def test_extendedpetrinet_InputPlaceAppearance___init__():
    assert extendedpetrinet_InputPlaceAppearance.__init__(extendedpetrinet_InputPlaceAppearance('', extendedpetrinet_InputPlaceAppearance=extendedpetrinet_Place()), '', extendedpetrinet_InputPlaceAppearance=extendedpetrinet_Place()) == None


from python_code import extendedpetrinet_InteractiveInput
from python_code import extendedpetrinet_Place

def test_extendedpetrinet_InteractiveInput___init__():
    assert extendedpetrinet_InteractiveInput.__init__(extendedpetrinet_InteractiveInput(True, extendedpetrinet_InteractiveInput=extendedpetrinet_Place()), False, extendedpetrinet_InteractiveInput=extendedpetrinet_Place()) == None


from python_code import extendedpetrinet_Place
from python_code import extendedpetrinet_Token

def test_extendedpetrinet_Token___init__():
    assert extendedpetrinet_Token.__init__(extendedpetrinet_Token('', extendedpetrinet_Token=extendedpetrinet_Place()), '', extendedpetrinet_Token=extendedpetrinet_Place()) == None

