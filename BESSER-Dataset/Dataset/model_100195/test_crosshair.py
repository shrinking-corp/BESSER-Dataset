from python_code import SQL2003_V3_ARRAY

def test_SQL2003_V3_ARRAY___init__():
    assert SQL2003_V3_ARRAY.__init__(SQL2003_V3_ARRAY(''), '') == None


from python_code import SQL2003_V3_BinaryStringType

def test_SQL2003_V3_BinaryStringType___init__():
    assert SQL2003_V3_BinaryStringType.__init__(SQL2003_V3_BinaryStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_BooleanType

def test_SQL2003_V3_BooleanType___init__():
    assert SQL2003_V3_BooleanType.__init__(SQL2003_V3_BooleanType(''), '') == None


from python_code import SQL2003_V3_CharacterStringType

def test_SQL2003_V3_CharacterStringType___init__():
    assert SQL2003_V3_CharacterStringType.__init__(SQL2003_V3_CharacterStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_ConstructedType

def test_SQL2003_V3_ConstructedType___init__():
    assert SQL2003_V3_ConstructedType.__init__(SQL2003_V3_ConstructedType(''), '') == None


from python_code import SQL2003_V3_DatetimeFeature

def test_SQL2003_V3_DatetimeFeature___init__():
    assert SQL2003_V3_DatetimeFeature.__init__(SQL2003_V3_DatetimeFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_DatetimeType

def test_SQL2003_V3_DatetimeType___init__():
    assert SQL2003_V3_DatetimeType.__init__(SQL2003_V3_DatetimeType(''), '') == None


from python_code import SQL2003_V3_DerivedTable

def test_SQL2003_V3_DerivedTable___init__():
    assert SQL2003_V3_DerivedTable.__init__(SQL2003_V3_DerivedTable(''), '') == None


from python_code import SQL2003_V3_IntervalFeature

def test_SQL2003_V3_IntervalFeature___init__():
    assert SQL2003_V3_IntervalFeature.__init__(SQL2003_V3_IntervalFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_IntervalType

def test_SQL2003_V3_IntervalType___init__():
    assert SQL2003_V3_IntervalType.__init__(SQL2003_V3_IntervalType(''), '') == None


from python_code import SQL2003_V3_NumericFeature

def test_SQL2003_V3_NumericFeature___init__():
    assert SQL2003_V3_NumericFeature.__init__(SQL2003_V3_NumericFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_NumericType

def test_SQL2003_V3_NumericType___init__():
    assert SQL2003_V3_NumericType.__init__(SQL2003_V3_NumericType(''), '') == None


from python_code import SQL2003_V3_DataType
from python_code import SQL2003_V3_Parameter

def test_SQL2003_V3_Parameter___init__():
    assert SQL2003_V3_Parameter.__init__(SQL2003_V3_Parameter('', SQL2003_V3_Parameter=SQL2003_V3_DataType()), '', SQL2003_V3_Parameter=SQL2003_V3_DataType()) == None


from python_code import SQL2003_V3_ReferentialConstraint
from python_code import SQL2003_V3_UniqueConstraint

def test_SQL2003_V3_ReferentialConstraint___init__():
    assert SQL2003_V3_ReferentialConstraint.__init__(SQL2003_V3_ReferentialConstraint('', '', '\x00\x00', SQL2003_V3_ReferentialConstraint=SQL2003_V3_UniqueConstraint()), '', '', '', SQL2003_V3_ReferentialConstraint=SQL2003_V3_UniqueConstraint()) == None


from python_code import SQL2003_V3_StringFeature

def test_SQL2003_V3_StringFeature___init__():
    assert SQL2003_V3_StringFeature.__init__(SQL2003_V3_StringFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V3_TableCheckConstraint

def test_SQL2003_V3_TableCheckConstraint___init__():
    assert SQL2003_V3_TableCheckConstraint.__init__(SQL2003_V3_TableCheckConstraint(''), '') == None


from python_code import SQL2003_V3_TableConstraint

def test_SQL2003_V3_TableConstraint___init__():
    assert SQL2003_V3_TableConstraint.__init__(SQL2003_V3_TableConstraint(''), '') == None


from python_code import SQL2003_V3_UserDefinedType

def test_SQL2003_V3_UserDefinedType___init__():
    assert SQL2003_V3_UserDefinedType.__init__(SQL2003_V3_UserDefinedType(''), '') == None


from python_code import SQL2003_V3_XMLType

def test_SQL2003_V3_XMLType___init__():
    assert SQL2003_V3_XMLType.__init__(SQL2003_V3_XMLType(''), '') == None

