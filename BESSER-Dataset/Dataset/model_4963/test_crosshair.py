from python_code import crom_l1_NamedElement

def test_crom_l1_NamedElement___init__():
    assert crom_l1_NamedElement.__init__(crom_l1_NamedElement(''), '') == None


from python_code import crom_l1_Operation
from python_code import crom_l1_Type

def test_crom_l1_Operation___init__():
    assert crom_l1_Operation.__init__(crom_l1_Operation('', operations=crom_l1_Type(), crom_l1_Operation=set(), Operation=crom_l1_Type()), '', operations=crom_l1_Type(), crom_l1_Operation=set(), Operation=crom_l1_Type()) == None


from python_code import crom_l1_AbstractRole
from python_code import crom_l1_CompartmentType
from python_code import crom_l1_Part

def test_crom_l1_Part___init__():
    assert crom_l1_Part.__init__(crom_l1_Part(0, 0, crom_l1_Part=crom_l1_AbstractRole(), parts=crom_l1_CompartmentType(), Part=crom_l1_CompartmentType()), 0, 0, crom_l1_Part=crom_l1_AbstractRole(), parts=crom_l1_CompartmentType(), Part=crom_l1_CompartmentType()) == None


from python_code import crom_l1_RoleGroup

def test_crom_l1_RoleGroup___init__():
    assert crom_l1_RoleGroup.__init__(crom_l1_RoleGroup(0, 0, crom_l1_RoleGroup=set()), 0, 0, crom_l1_RoleGroup=set()) == None

