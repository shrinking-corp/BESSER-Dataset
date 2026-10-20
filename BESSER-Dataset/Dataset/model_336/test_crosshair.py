from python_code import extlibrary_Addressable

def test_extlibrary_Addressable___init__():
    assert extlibrary_Addressable.__init__(extlibrary_Addressable(''), '') == None


from python_code import extlibrary_AudioVisualItem

def test_extlibrary_AudioVisualItem___init__():
    assert extlibrary_AudioVisualItem.__init__(extlibrary_AudioVisualItem('', 0, False), '\x00', 0, False) == None


from python_code import extlibrary_Book
from python_code import extlibrary__15CRUW60EeGkd4g88tZXfA

def test_extlibrary_Book___init__():
    assert extlibrary_Book.__init__(extlibrary_Book('', 0, '\x00\x00', extlibrary_Book=extlibrary__15CRUW60EeGkd4g88tZXfA()), '', 0, '', extlibrary_Book=extlibrary__15CRUW60EeGkd4g88tZXfA()) == None


from python_code import extlibrary_BookOnTape
from python_code import extlibrary__15CRUW60EeGkd4g88tZXfA
from python_code import extlibrary__15N3gm60EeGkd4g88tZXfA

def test_extlibrary_BookOnTape___init__():
    assert extlibrary_BookOnTape.__init__(extlibrary_BookOnTape('', 0, False, extlibrary_BookOnTape=extlibrary__15N3gm60EeGkd4g88tZXfA(), extlibrary_BookOnTape22=extlibrary__15CRUW60EeGkd4g88tZXfA()), '\x00', 0, False, extlibrary_BookOnTape=extlibrary__15N3gm60EeGkd4g88tZXfA(), extlibrary_BookOnTape22=extlibrary__15CRUW60EeGkd4g88tZXfA()) == None


import datetime as _ch_datetime
from python_code import extlibrary_Item

def test_extlibrary_Item___init__():
    assert extlibrary_Item.__init__(extlibrary_Item(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import extlibrary_Lendable

def test_extlibrary_Lendable___init__():
    assert extlibrary_Lendable.__init__(extlibrary_Lendable(0, extlibrary_Lendable=set()), 0, extlibrary_Lendable=set()) == None


from python_code import extlibrary_Library
from python_code import extlibrary__148KsW60EeGkd4g88tZXfA

def test_extlibrary_Library___init__():
    assert extlibrary_Library.__init__(extlibrary_Library('', '', extlibrary_Library4=set(), extlibrary_Library6=set(), extlibrary_Library8=set(), extlibrary_Library10=set(), extlibrary_Library12=set(), extlibrary_Library14=extlibrary__148KsW60EeGkd4g88tZXfA(), extlibrary_Library=set()), '', '', extlibrary_Library4=set(), extlibrary_Library6=set(), extlibrary_Library8=set(), extlibrary_Library10=set(), extlibrary_Library12=set(), extlibrary_Library14=extlibrary__148KsW60EeGkd4g88tZXfA(), extlibrary_Library=set()) == None


import datetime as _ch_datetime
from python_code import extlibrary_Periodical

def test_extlibrary_Periodical___init__():
    assert extlibrary_Periodical.__init__(extlibrary_Periodical(_ch_datetime.date(1, 1, 1), '\x00', 0), _ch_datetime.date(1, 1, 2), '', 0) == None


from python_code import extlibrary_Person

def test_extlibrary_Person___init__():
    assert extlibrary_Person.__init__(extlibrary_Person('', '\x00'), '\x00\x00', '') == None


from python_code import extlibrary_VideoCassette

def test_extlibrary_VideoCassette___init__():
    assert extlibrary_VideoCassette.__init__(extlibrary_VideoCassette('', 0, False, extlibrary_VideoCassette=set()), '', 0, True, extlibrary_VideoCassette=set()) == None


from python_code import extlibrary_Writer

def test_extlibrary_Writer___init__():
    assert extlibrary_Writer.__init__(extlibrary_Writer('', extlibrary_Writer=set()), '', extlibrary_Writer=set()) == None

