from python_code import ORDB4ORA_ANSICharacterType

def test_ORDB4ORA_ANSICharacterType___init__():
    assert ORDB4ORA_ANSICharacterType.__init__(ORDB4ORA_ANSICharacterType(''), '') == None


from python_code import ORDB4ORA_ANSINumberType

def test_ORDB4ORA_ANSINumberType___init__():
    assert ORDB4ORA_ANSINumberType.__init__(ORDB4ORA_ANSINumberType(''), '') == None


from python_code import ORDB4ORA_AnyType

def test_ORDB4ORA_AnyType___init__():
    assert ORDB4ORA_AnyType.__init__(ORDB4ORA_AnyType(''), '') == None


from python_code import ORDB4ORA_BuiltInCharacterType

def test_ORDB4ORA_BuiltInCharacterType___init__():
    assert ORDB4ORA_BuiltInCharacterType.__init__(ORDB4ORA_BuiltInCharacterType('', '', 0, 0, 0), '', '', 0, 0, 0) == None


from python_code import ORDB4ORA_BuiltInNumberType

def test_ORDB4ORA_BuiltInNumberType___init__():
    assert ORDB4ORA_BuiltInNumberType.__init__(ORDB4ORA_BuiltInNumberType('', 0, 0, 0, 0), '', 0, 0, 0, 0) == None


from python_code import ORDB4ORA_CharacterFeature

def test_ORDB4ORA_CharacterFeature___init__():
    assert ORDB4ORA_CharacterFeature.__init__(ORDB4ORA_CharacterFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_Check

def test_ORDB4ORA_Check___init__():
    assert ORDB4ORA_Check.__init__(ORDB4ORA_Check(''), '') == None


from python_code import ORDB4ORA_DatetimeFeature

def test_ORDB4ORA_DatetimeFeature___init__():
    assert ORDB4ORA_DatetimeFeature.__init__(ORDB4ORA_DatetimeFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_DatetimeType

def test_ORDB4ORA_DatetimeType___init__():
    assert ORDB4ORA_DatetimeType.__init__(ORDB4ORA_DatetimeType('', 0, 0, 0, 0, 0, 0, 0, 0, 0), '', 0, 0, 0, 0, 0, 0, 0, 0, 0) == None


from python_code import ORDB4ORA_DerivedTable

def test_ORDB4ORA_DerivedTable___init__():
    assert ORDB4ORA_DerivedTable.__init__(ORDB4ORA_DerivedTable(''), '') == None


from python_code import ORDB4ORA_IntervalFeature

def test_ORDB4ORA_IntervalFeature___init__():
    assert ORDB4ORA_IntervalFeature.__init__(ORDB4ORA_IntervalFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_LOBType

def test_ORDB4ORA_LOBType___init__():
    assert ORDB4ORA_LOBType.__init__(ORDB4ORA_LOBType(''), '') == None


from python_code import ORDB4ORA_LongAndRawType

def test_ORDB4ORA_LongAndRawType___init__():
    assert ORDB4ORA_LongAndRawType.__init__(ORDB4ORA_LongAndRawType('', 0, 0), '\x00', 0, 0) == None


from python_code import ORDB4ORA_MediaType

def test_ORDB4ORA_MediaType___init__():
    assert ORDB4ORA_MediaType.__init__(ORDB4ORA_MediaType(''), '') == None


from python_code import ORDB4ORA_Datatype
from python_code import ORDB4ORA_NestedTableType

def test_ORDB4ORA_NestedTableType___init__():
    assert ORDB4ORA_NestedTableType.__init__(ORDB4ORA_NestedTableType('', ORDB4ORA_NestedTableType=ORDB4ORA_Datatype()), '', ORDB4ORA_NestedTableType=ORDB4ORA_Datatype()) == None


from python_code import ORDB4ORA_NumberFeature

def test_ORDB4ORA_NumberFeature___init__():
    assert ORDB4ORA_NumberFeature.__init__(ORDB4ORA_NumberFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_Datatype
from python_code import ORDB4ORA_Parameter

def test_ORDB4ORA_Parameter___init__():
    assert ORDB4ORA_Parameter.__init__(ORDB4ORA_Parameter('', ORDB4ORA_Parameter=ORDB4ORA_Datatype()), '', ORDB4ORA_Parameter=ORDB4ORA_Datatype()) == None


from python_code import ORDB4ORA_ROWIDType

def test_ORDB4ORA_ROWIDType___init__():
    assert ORDB4ORA_ROWIDType.__init__(ORDB4ORA_ROWIDType('', 0, 0), '\x00', 0, 0) == None


from python_code import ORDB4ORA_RawFeature

def test_ORDB4ORA_RawFeature___init__():
    assert ORDB4ORA_RawFeature.__init__(ORDB4ORA_RawFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_RowFeature

def test_ORDB4ORA_RowFeature___init__():
    assert ORDB4ORA_RowFeature.__init__(ORDB4ORA_RowFeature('', '\x00'), '\x00\x00', '') == None


from python_code import ORDB4ORA_SpacialType

def test_ORDB4ORA_SpacialType___init__():
    assert ORDB4ORA_SpacialType.__init__(ORDB4ORA_SpacialType(''), '') == None


from python_code import ORDB4ORA_Attribute
from python_code import ORDB4ORA_StoredNestedTable
from python_code import ORDB4ORA_TypedTable

def test_ORDB4ORA_StoredNestedTable___init__():
    assert ORDB4ORA_StoredNestedTable.__init__(ORDB4ORA_StoredNestedTable('', ORDB4ORA_StoredNestedTable=ORDB4ORA_Attribute(), storedNested=ORDB4ORA_TypedTable(), StoredNestedTable=ORDB4ORA_TypedTable()), '', ORDB4ORA_StoredNestedTable=ORDB4ORA_Attribute(), storedNested=ORDB4ORA_TypedTable(), StoredNestedTable=ORDB4ORA_TypedTable()) == None


from python_code import ORDB4ORA_Datatype
from python_code import ORDB4ORA_Varray

def test_ORDB4ORA_Varray___init__():
    assert ORDB4ORA_Varray.__init__(ORDB4ORA_Varray('', 0, ORDB4ORA_Varray=ORDB4ORA_Datatype()), '', 0, ORDB4ORA_Varray=ORDB4ORA_Datatype()) == None


from python_code import ORDB4ORA_XMLType

def test_ORDB4ORA_XMLType___init__():
    assert ORDB4ORA_XMLType.__init__(ORDB4ORA_XMLType(''), '') == None

