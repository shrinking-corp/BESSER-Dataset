from python_code import DDL_BitStringType

def test_DDL_BitStringType___init__():
    assert DDL_BitStringType.__init__(DDL_BitStringType(0), 0) == None


from python_code import DDL_CharacterStringType

def test_DDL_CharacterStringType___init__():
    assert DDL_CharacterStringType.__init__(DDL_CharacterStringType(0), 0) == None


from python_code import DDL_Ck
from python_code import DDL_Table

def test_DDL_Ck___init__():
    assert DDL_Ck.__init__(DDL_Ck('', DDL_Ck=DDL_Table()), '', DDL_Ck=DDL_Table()) == None


from python_code import DDL_Column
from python_code import DDL_Table
from python_code import DDL_Type

def test_DDL_Column___init__():
    assert DDL_Column.__init__(DDL_Column(True, DDL_Column11=DDL_Type(), DDL_Column=DDL_Table()), False, DDL_Column11=DDL_Type(), DDL_Column=DDL_Table()) == None


from python_code import DDL_Dec

def test_DDL_Dec___init__():
    assert DDL_Dec.__init__(DDL_Dec(0, 0), 0, 0) == None


from python_code import DDL_Decimal

def test_DDL_Decimal___init__():
    assert DDL_Decimal.__init__(DDL_Decimal(0, 0), 0, 0) == None


from python_code import DDL_Fk
from python_code import DDL_Table

def test_DDL_Fk___init__():
    assert DDL_Fk.__init__(DDL_Fk('', '\x00', DDL_Fk13=DDL_Table(), DDL_Fk=DDL_Table()), '\x00\x00', '', DDL_Fk13=DDL_Table(), DDL_Fk=DDL_Table()) == None


from python_code import DDL_Float

def test_DDL_Float___init__():
    assert DDL_Float.__init__(DDL_Float(0), 0) == None


from python_code import DDL_Interval

def test_DDL_Interval___init__():
    assert DDL_Interval.__init__(DDL_Interval('\x00\x00', '', 0, 0), '', '', 0, 0) == None


from python_code import DDL_NamedElement

def test_DDL_NamedElement___init__():
    assert DDL_NamedElement.__init__(DDL_NamedElement(''), '') == None


from python_code import DDL_NationalCharacterStringType

def test_DDL_NationalCharacterStringType___init__():
    assert DDL_NationalCharacterStringType.__init__(DDL_NationalCharacterStringType(0), 0) == None


from python_code import DDL_Numeric

def test_DDL_Numeric___init__():
    assert DDL_Numeric.__init__(DDL_Numeric(0, 0), 0, 0) == None


from python_code import DDL_Pk
from python_code import DDL_Table

def test_DDL_Pk___init__():
    assert DDL_Pk.__init__(DDL_Pk('', DDL_Pk=DDL_Table()), '', DDL_Pk=DDL_Table()) == None


from python_code import DDL_Time

def test_DDL_Time___init__():
    assert DDL_Time.__init__(DDL_Time(0, False), 0, False) == None


from python_code import DDL_TimeStamp

def test_DDL_TimeStamp___init__():
    assert DDL_TimeStamp.__init__(DDL_TimeStamp(0, False), 0, False) == None


from python_code import DDL_Check
from python_code import DDL_ValuesCheck

def test_DDL_ValuesCheck___init__():
    assert DDL_ValuesCheck.__init__(DDL_ValuesCheck('\x00\x00', '', '', '', DDL_ValuesCheck=DDL_Check()), '', '', '', '', DDL_ValuesCheck=DDL_Check()) == None

