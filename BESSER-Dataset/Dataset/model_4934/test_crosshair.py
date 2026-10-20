from python_code import backbone_Attribute
from python_code import backbone_Model

def test_backbone_Attribute___init__():
    assert backbone_Attribute.__init__(backbone_Attribute('', '\x00', backbone_Attribute=backbone_Model()), '\x00\x00', '', backbone_Attribute=backbone_Model()) == None


from python_code import backbone_NamedElement

def test_backbone_NamedElement___init__():
    assert backbone_NamedElement.__init__(backbone_NamedElement(''), '') == None


from python_code import backbone_Model
from python_code import backbone_Reference

def test_backbone_Reference___init__():
    assert backbone_Reference.__init__(backbone_Reference('', backbone_Reference14=backbone_Model(), backbone_Reference=backbone_Model()), '', backbone_Reference14=backbone_Model(), backbone_Reference=backbone_Model()) == None


from python_code import backbone_Router
from python_code import backbone_RouterMapping
from python_code import backbone_View

def test_backbone_RouterMapping___init__():
    assert backbone_RouterMapping.__init__(backbone_RouterMapping('', backbone_RouterMapping=backbone_Router(), backbone_RouterMapping26=backbone_View()), '', backbone_RouterMapping=backbone_Router(), backbone_RouterMapping26=backbone_View()) == None

