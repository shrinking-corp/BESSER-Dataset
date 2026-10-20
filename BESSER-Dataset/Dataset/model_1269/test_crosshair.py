from python_code import columnFamilyDataModel_Collection

def test_columnFamilyDataModel_Collection___init__():
    assert columnFamilyDataModel_Collection.__init__(columnFamilyDataModel_Collection(''), '') == None


from python_code import columnFamilyDataModel_Map

def test_columnFamilyDataModel_Map___init__():
    assert columnFamilyDataModel_Map.__init__(columnFamilyDataModel_Map(''), '') == None


from python_code import columnFamilyDataModel_SimpleType

def test_columnFamilyDataModel_SimpleType___init__():
    assert columnFamilyDataModel_SimpleType.__init__(columnFamilyDataModel_SimpleType(''), '') == None


from python_code import columnFamilyDataModel_Tuple

def test_columnFamilyDataModel_Tuple___init__():
    assert columnFamilyDataModel_Tuple.__init__(columnFamilyDataModel_Tuple(''), '') == None


from python_code import columnFamilyDataModel_UserDefinedType

def test_columnFamilyDataModel_UserDefinedType___init__():
    assert columnFamilyDataModel_UserDefinedType.__init__(columnFamilyDataModel_UserDefinedType('\x00', columnFamilyDataModel_UserDefinedType=set()), '', columnFamilyDataModel_UserDefinedType=set()) == None

