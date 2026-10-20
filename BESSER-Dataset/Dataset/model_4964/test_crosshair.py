from python_code import crom_l1_NamedElement

def test_crom_l1_NamedElement___init__():
    assert crom_l1_NamedElement.__init__(crom_l1_NamedElement(''), '') == None


from python_code import crom_l1_Operation
from python_code import crom_l1_Type

def test_crom_l1_Operation___init__():
    assert crom_l1_Operation.__init__(crom_l1_Operation('', crom_l1_Operation=set(), operations=crom_l1_Type(), Operation=crom_l1_Type()), '', crom_l1_Operation=set(), operations=crom_l1_Type(), Operation=crom_l1_Type()) == None

