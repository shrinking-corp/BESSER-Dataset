from python_code import familyright_Daughter
from python_code import familyright_Family

def test_familyright_Daughter___init__():
    assert familyright_Daughter.__init__(familyright_Daughter('', 0, daughters=familyright_Family(), Daughter=familyright_Family()), '', 0, daughters=familyright_Family(), Daughter=familyright_Family()) == None


from python_code import familyright_Family
from python_code import familyright_Father

def test_familyright_Father___init__():
    assert familyright_Father.__init__(familyright_Father('', 0, '\x00\x00', father=familyright_Family(), Father=familyright_Family()), '', 0, '', father=familyright_Family(), Father=familyright_Family()) == None


from python_code import familyright_Family
from python_code import familyright_Mother

def test_familyright_Mother___init__():
    assert familyright_Mother.__init__(familyright_Mother('', 0, '\x00\x00', Mother=familyright_Family(), mother=familyright_Family()), '', 0, '', Mother=familyright_Family(), mother=familyright_Family()) == None


from python_code import familyright_Family
from python_code import familyright_Son

def test_familyright_Son___init__():
    assert familyright_Son.__init__(familyright_Son('', 0, Son=familyright_Family(), sons=familyright_Family()), '', 0, Son=familyright_Family(), sons=familyright_Family()) == None

