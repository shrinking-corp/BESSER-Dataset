from python_code import OurPNVis_CanChange
from python_code import OurPNVis_Place

def test_OurPNVis_CanChange___init__():
    assert OurPNVis_CanChange.__init__(OurPNVis_CanChange(True, OurPNVis_CanChange=OurPNVis_Place()), False, OurPNVis_CanChange=OurPNVis_Place()) == None


from python_code import OurPNVis_Arc
from python_code import OurPNVis_Finished

def test_OurPNVis_Finished___init__():
    assert OurPNVis_Finished.__init__(OurPNVis_Finished(True, OurPNVis_Finished=OurPNVis_Arc()), False, OurPNVis_Finished=OurPNVis_Arc()) == None


from python_code import OurPNVis_Geometry
from python_code import OurPNVis_Place

def test_OurPNVis_Geometry___init__():
    assert OurPNVis_Geometry.__init__(OurPNVis_Geometry('', OurPNVis_Geometry=OurPNVis_Place()), '', OurPNVis_Geometry=OurPNVis_Place()) == None


from python_code import OurPNVis_Arc
from python_code import OurPNVis_KeepAnim

def test_OurPNVis_KeepAnim___init__():
    assert OurPNVis_KeepAnim.__init__(OurPNVis_KeepAnim(True, OurPNVis_KeepAnim=OurPNVis_Arc()), False, OurPNVis_KeepAnim=OurPNVis_Arc()) == None


from python_code import OurPNVis_Place
from python_code import OurPNVis_Shape

def test_OurPNVis_Shape___init__():
    assert OurPNVis_Shape.__init__(OurPNVis_Shape('', OurPNVis_Shape=OurPNVis_Place()), '', OurPNVis_Shape=OurPNVis_Place()) == None


from python_code import OurPNVis_Place
from python_code import OurPNVis_Tokens

def test_OurPNVis_Tokens___init__():
    assert OurPNVis_Tokens.__init__(OurPNVis_Tokens('', OurPNVis_Tokens=OurPNVis_Place()), '', OurPNVis_Tokens=OurPNVis_Place()) == None


from python_code import OurPNVis_Arc
from python_code import OurPNVis_ident

def test_OurPNVis_ident___init__():
    assert OurPNVis_ident.__init__(OurPNVis_ident('', OurPNVis_ident=OurPNVis_Arc()), '', OurPNVis_ident=OurPNVis_Arc()) == None

