from python_code import SQL2003_ARRAY

def test_SQL2003_ARRAY___init__():
    assert SQL2003_ARRAY.__init__(SQL2003_ARRAY(''), '') == None


from python_code import SQL2003_BinaryStringType

def test_SQL2003_BinaryStringType___init__():
    assert SQL2003_BinaryStringType.__init__(SQL2003_BinaryStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_BooleanType

def test_SQL2003_BooleanType___init__():
    assert SQL2003_BooleanType.__init__(SQL2003_BooleanType(''), '') == None


from python_code import SQL2003_CharacterStringType

def test_SQL2003_CharacterStringType___init__():
    assert SQL2003_CharacterStringType.__init__(SQL2003_CharacterStringType('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_ConstructedType

def test_SQL2003_ConstructedType___init__():
    assert SQL2003_ConstructedType.__init__(SQL2003_ConstructedType(''), '') == None


from python_code import SQL2003_DatetimeFeature

def test_SQL2003_DatetimeFeature___init__():
    assert SQL2003_DatetimeFeature.__init__(SQL2003_DatetimeFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_DatetimeType

def test_SQL2003_DatetimeType___init__():
    assert SQL2003_DatetimeType.__init__(SQL2003_DatetimeType(''), '') == None


from python_code import SQL2003_DerivedTable

def test_SQL2003_DerivedTable___init__():
    assert SQL2003_DerivedTable.__init__(SQL2003_DerivedTable(''), '') == None


from python_code import SQL2003_IntervalFeature

def test_SQL2003_IntervalFeature___init__():
    assert SQL2003_IntervalFeature.__init__(SQL2003_IntervalFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_IntervalType

def test_SQL2003_IntervalType___init__():
    assert SQL2003_IntervalType.__init__(SQL2003_IntervalType(''), '') == None


from python_code import SQL2003_NumericFeature

def test_SQL2003_NumericFeature___init__():
    assert SQL2003_NumericFeature.__init__(SQL2003_NumericFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_NumericType

def test_SQL2003_NumericType___init__():
    assert SQL2003_NumericType.__init__(SQL2003_NumericType(''), '') == None


from python_code import SQL2003_DataType
from python_code import SQL2003_Parameter

def test_SQL2003_Parameter___init__():
    assert SQL2003_Parameter.__init__(SQL2003_Parameter('', SQL2003_Parameter=SQL2003_DataType()), '', SQL2003_Parameter=SQL2003_DataType()) == None


from python_code import SQL2003_ReferentialConstraint
from python_code import SQL2003_UniqueConstraint

def test_SQL2003_ReferentialConstraint___init__():
    assert SQL2003_ReferentialConstraint.__init__(SQL2003_ReferentialConstraint('', '', '\x00\x00', SQL2003_ReferentialConstraint=SQL2003_UniqueConstraint()), '', '', '', SQL2003_ReferentialConstraint=SQL2003_UniqueConstraint()) == None


from python_code import SQL2003_StringFeature

def test_SQL2003_StringFeature___init__():
    assert SQL2003_StringFeature.__init__(SQL2003_StringFeature('', '\x00'), '\x00\x00', '') == None


from python_code import SQL2003_TableCheckConstraint

def test_SQL2003_TableCheckConstraint___init__():
    assert SQL2003_TableCheckConstraint.__init__(SQL2003_TableCheckConstraint(''), '') == None


from python_code import SQL2003_TableConstraint

def test_SQL2003_TableConstraint___init__():
    assert SQL2003_TableConstraint.__init__(SQL2003_TableConstraint(''), '') == None


from python_code import SQL2003_UserDefinedType

def test_SQL2003_UserDefinedType___init__():
    assert SQL2003_UserDefinedType.__init__(SQL2003_UserDefinedType(''), '') == None


from python_code import SQL2003_XMLType

def test_SQL2003_XMLType___init__():
    assert SQL2003_XMLType.__init__(SQL2003_XMLType(''), '') == None

