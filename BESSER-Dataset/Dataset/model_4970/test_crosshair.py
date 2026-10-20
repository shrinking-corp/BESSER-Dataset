from python_code import umlsimp_Model
from python_code import umlsimp_ModelElement

def test_umlsimp_ModelElement___init__():
    assert umlsimp_ModelElement.__init__(umlsimp_ModelElement('', umlsimp_ModelElement=umlsimp_Model()), '', umlsimp_ModelElement=umlsimp_Model()) == None


from python_code import umlsimp_Class
from python_code import umlsimp_Property

def test_umlsimp_Property___init__():
    assert umlsimp_Property.__init__(umlsimp_Property('', properties=umlsimp_Class(), Property=umlsimp_Class()), '', properties=umlsimp_Class(), Property=umlsimp_Class()) == None

