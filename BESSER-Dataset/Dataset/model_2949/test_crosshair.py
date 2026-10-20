from python_code import domainmodel_DataType
from python_code import domainmodel_Type

def test_domainmodel_DataType___init__():
    assert domainmodel_DataType.__init__(domainmodel_DataType('', domainmodel_DataType=domainmodel_Type()), '', domainmodel_DataType=domainmodel_Type()) == None

