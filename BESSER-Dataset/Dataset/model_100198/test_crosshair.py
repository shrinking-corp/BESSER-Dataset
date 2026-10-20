from python_code import sqlDSL_SEnum
from python_code import sqlDSL_SEnumLiteral

def test_sqlDSL_SEnumLiteral___init__():
    assert sqlDSL_SEnumLiteral.__init__(sqlDSL_SEnumLiteral('', 0, sqlDSL_SEnumLiteral=sqlDSL_SEnum()), '', 0, sqlDSL_SEnumLiteral=sqlDSL_SEnum()) == None

