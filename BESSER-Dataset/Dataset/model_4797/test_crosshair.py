from python_code import alldatatypes_BigDecimals

def test_alldatatypes_BigDecimals___init__():
    assert alldatatypes_BigDecimals.__init__(alldatatypes_BigDecimals('', '', '', '', ''), '', '', '', '', '') == None


from python_code import alldatatypes_BigIntegers

def test_alldatatypes_BigIntegers___init__():
    assert alldatatypes_BigIntegers.__init__(alldatatypes_BigIntegers('', '', '', '', ''), '', '', '', '', '') == None


from python_code import alldatatypes_Booleans

def test_alldatatypes_Booleans___init__():
    assert alldatatypes_Booleans.__init__(alldatatypes_Booleans(False, False, False, False), False, False, False, True) == None


import datetime as _ch_datetime
from python_code import alldatatypes_Dates

def test_alldatatypes_Dates___init__():
    assert alldatatypes_Dates.__init__(alldatatypes_Dates(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 3), _ch_datetime.date(1, 1, 1)), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None


from python_code import alldatatypes_Doubles

def test_alldatatypes_Doubles___init__():
    assert alldatatypes_Doubles.__init__(alldatatypes_Doubles(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import alldatatypes_Element

def test_alldatatypes_Element___init__():
    assert alldatatypes_Element.__init__(alldatatypes_Element('', '\x00'), '\x00\x00', '') == None


from python_code import alldatatypes_Enums

def test_alldatatypes_Enums___init__():
    assert alldatatypes_Enums.__init__(alldatatypes_Enums('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None


from python_code import alldatatypes_Floats

def test_alldatatypes_Floats___init__():
    assert alldatatypes_Floats.__init__(alldatatypes_Floats(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import alldatatypes_Integers

def test_alldatatypes_Integers___init__():
    assert alldatatypes_Integers.__init__(alldatatypes_Integers(0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0) == None


from python_code import alldatatypes_Longs

def test_alldatatypes_Longs___init__():
    assert alldatatypes_Longs.__init__(alldatatypes_Longs('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import alldatatypes_Root

def test_alldatatypes_Root___init__():
    assert alldatatypes_Root.__init__(alldatatypes_Root(alldatatypes_Root=set()), alldatatypes_Root=set()) == None

def test_alldatatypes_Root_getAllTypes():
    assert alldatatypes_Root.getAllTypes(alldatatypes_Root(alldatatypes_Root=set())) == None


from python_code import alldatatypes_Shorts

def test_alldatatypes_Shorts___init__():
    assert alldatatypes_Shorts.__init__(alldatatypes_Shorts('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import alldatatypes_Strings

def test_alldatatypes_Strings___init__():
    assert alldatatypes_Strings.__init__(alldatatypes_Strings('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None

