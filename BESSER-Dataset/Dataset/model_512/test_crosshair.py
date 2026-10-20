from python_code import familyleft2_Family
from python_code import familyleft2_Father

def test_familyleft2_Father___init__():
    assert familyleft2_Father.__init__(familyleft2_Father('', father=familyleft2_Family(), Father=familyleft2_Family()), '', father=familyleft2_Family(), Father=familyleft2_Family()) == None


from python_code import familyleft2_Family
from python_code import familyleft2_Mother

def test_familyleft2_Mother___init__():
    assert familyleft2_Mother.__init__(familyleft2_Mother('', mother=familyleft2_Family(), Mother=familyleft2_Family()), '', mother=familyleft2_Family(), Mother=familyleft2_Family()) == None


from python_code import familyleft2_Person

def test_familyleft2_Person___init__():
    assert familyleft2_Person.__init__(familyleft2_Person('', 0, False), '\x00', 0, False) == None

