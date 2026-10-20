from python_code import SQL2003_V2_ARRAY

def test_SQL2003_V2_ARRAY___init__():
    assert SQL2003_V2_ARRAY.__init__(SQL2003_V2_ARRAY(''), '') == None


from python_code import SQL2003_V2_BinaryStringType

def test_SQL2003_V2_BinaryStringType___init__():
    assert SQL2003_V2_BinaryStringType.__init__(SQL2003_V2_BinaryStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_BooleanType

def test_SQL2003_V2_BooleanType___init__():
    assert SQL2003_V2_BooleanType.__init__(SQL2003_V2_BooleanType(''), '') == None


from python_code import SQL2003_V2_CharacterStringType

def test_SQL2003_V2_CharacterStringType___init__():
    assert SQL2003_V2_CharacterStringType.__init__(SQL2003_V2_CharacterStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_ConstructedType

def test_SQL2003_V2_ConstructedType___init__():
    assert SQL2003_V2_ConstructedType.__init__(SQL2003_V2_ConstructedType(''), '') == None


from python_code import SQL2003_V2_DatetimeFeature

def test_SQL2003_V2_DatetimeFeature___init__():
    assert SQL2003_V2_DatetimeFeature.__init__(SQL2003_V2_DatetimeFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_DatetimeType

def test_SQL2003_V2_DatetimeType___init__():
    assert SQL2003_V2_DatetimeType.__init__(SQL2003_V2_DatetimeType(''), '') == None


from python_code import SQL2003_V2_DerivedTable

def test_SQL2003_V2_DerivedTable___init__():
    assert SQL2003_V2_DerivedTable.__init__(SQL2003_V2_DerivedTable(''), '') == None


from python_code import SQL2003_V2_IntervalFeature

def test_SQL2003_V2_IntervalFeature___init__():
    assert SQL2003_V2_IntervalFeature.__init__(SQL2003_V2_IntervalFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_IntervalType

def test_SQL2003_V2_IntervalType___init__():
    assert SQL2003_V2_IntervalType.__init__(SQL2003_V2_IntervalType(''), '') == None


from python_code import SQL2003_V2_NumericFeature

def test_SQL2003_V2_NumericFeature___init__():
    assert SQL2003_V2_NumericFeature.__init__(SQL2003_V2_NumericFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_NumericType

def test_SQL2003_V2_NumericType___init__():
    assert SQL2003_V2_NumericType.__init__(SQL2003_V2_NumericType(''), '') == None


from python_code import SQL2003_V2_DataType
from python_code import SQL2003_V2_Parameter

def test_SQL2003_V2_Parameter___init__():
    assert SQL2003_V2_Parameter.__init__(SQL2003_V2_Parameter('', SQL2003_V2_Parameter=SQL2003_V2_DataType()), '', SQL2003_V2_Parameter=SQL2003_V2_DataType()) == None


from python_code import SQL2003_V2_ReferentialConstraint
from python_code import SQL2003_V2_UniqueConstraint

def test_SQL2003_V2_ReferentialConstraint___init__():
    assert SQL2003_V2_ReferentialConstraint.__init__(SQL2003_V2_ReferentialConstraint('', '', '\x00\x00', SQL2003_V2_ReferentialConstraint=SQL2003_V2_UniqueConstraint()), '', '', '', SQL2003_V2_ReferentialConstraint=SQL2003_V2_UniqueConstraint()) == None


from python_code import SQL2003_V2_StringFeature

def test_SQL2003_V2_StringFeature___init__():
    assert SQL2003_V2_StringFeature.__init__(SQL2003_V2_StringFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_V2_TableCheckConstraint

def test_SQL2003_V2_TableCheckConstraint___init__():
    assert SQL2003_V2_TableCheckConstraint.__init__(SQL2003_V2_TableCheckConstraint(''), '') == None


from python_code import SQL2003_V2_TableConstraint

def test_SQL2003_V2_TableConstraint___init__():
    assert SQL2003_V2_TableConstraint.__init__(SQL2003_V2_TableConstraint(''), '') == None


from python_code import SQL2003_V2_UserDefinedType

def test_SQL2003_V2_UserDefinedType___init__():
    assert SQL2003_V2_UserDefinedType.__init__(SQL2003_V2_UserDefinedType(''), '') == None


from python_code import SQL2003_V2_XMLType

def test_SQL2003_V2_XMLType___init__():
    assert SQL2003_V2_XMLType.__init__(SQL2003_V2_XMLType(''), '') == None

