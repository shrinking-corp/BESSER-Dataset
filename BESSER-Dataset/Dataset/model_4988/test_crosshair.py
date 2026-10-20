from python_code import componentmodel_Component
from python_code import componentmodel_CompositeComponent

def test_componentmodel_Component___init__():
    assert componentmodel_Component.__init__(componentmodel_Component('\x00\x00', '', componentmodel_Component=set(), componentmodel_Component3=componentmodel_CompositeComponent()), '', '', componentmodel_Component=set(), componentmodel_Component3=componentmodel_CompositeComponent()) == None


from python_code import componentmodel_EnumProperty

def test_componentmodel_EnumProperty___init__():
    assert componentmodel_EnumProperty.__init__(componentmodel_EnumProperty(''), '') == None


from python_code import componentmodel_NumericProperty

def test_componentmodel_NumericProperty___init__():
    assert componentmodel_NumericProperty.__init__(componentmodel_NumericProperty(0.0, 0.0, 0.0), 0.0, 0.0, 0.0) == None


from python_code import componentmodel_PrimitiveComponent
from python_code import componentmodel_Property

def test_componentmodel_Property___init__():
    assert componentmodel_Property.__init__(componentmodel_Property('', '\x00', componentmodel_Property=componentmodel_PrimitiveComponent()), '\x00\x00', '', componentmodel_Property=componentmodel_PrimitiveComponent()) == None

