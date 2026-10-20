from python_code import soa_Entities
from python_code import soa_EntitiesFeature
from python_code import soa_Model

def test_soa_Entities___init__():
    assert soa_Entities.__init__(soa_Entities('', soa_Entities=soa_Model(), soa_Entities17=soa_EntitiesFeature()), '', soa_Entities=soa_Model(), soa_Entities17=soa_EntitiesFeature()) == None


from python_code import soa_Enum

def test_soa_Enum___init__():
    assert soa_Enum.__init__(soa_Enum(''), '') == None


from python_code import soa_PrimitiveFeature

def test_soa_PrimitiveFeature___init__():
    assert soa_PrimitiveFeature.__init__(soa_PrimitiveFeature(''), '') == None

