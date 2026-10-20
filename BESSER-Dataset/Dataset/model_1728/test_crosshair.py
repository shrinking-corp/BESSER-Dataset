from python_code import extlibraryprofile_Addressable

def test_extlibraryprofile_Addressable___init__():
    assert extlibraryprofile_Addressable.__init__(extlibraryprofile_Addressable(''), '') == None


from python_code import extlibraryprofile_AudioVisualItem

def test_extlibraryprofile_AudioVisualItem___init__():
    assert extlibraryprofile_AudioVisualItem.__init__(extlibraryprofile_AudioVisualItem('', '\x00'), '\x00\x00', '') == None


from python_code import extlibraryprofile_Book

def test_extlibraryprofile_Book___init__():
    assert extlibraryprofile_Book.__init__(extlibraryprofile_Book('', '\x00'), '\x00\x00', '') == None


from python_code import extlibraryprofile_Class
from python_code import extlibraryprofile_Item

def test_extlibraryprofile_Item___init__():
    assert extlibraryprofile_Item.__init__(extlibraryprofile_Item('', '\x00', extlibraryprofile_Item=extlibraryprofile_Class()), '\x00\x00', '', extlibraryprofile_Item=extlibraryprofile_Class()) == None


from python_code import extlibraryprofile_Lendable

def test_extlibraryprofile_Lendable___init__():
    assert extlibraryprofile_Lendable.__init__(extlibraryprofile_Lendable(''), '') == None


from python_code import extlibraryprofile_Library
from python_code import extlibraryprofile_Package

def test_extlibraryprofile_Library___init__():
    assert extlibraryprofile_Library.__init__(extlibraryprofile_Library('', extlibraryprofile_Library=extlibraryprofile_Package()), '', extlibraryprofile_Library=extlibraryprofile_Package()) == None


from python_code import extlibraryprofile_Periodical

def test_extlibraryprofile_Periodical___init__():
    assert extlibraryprofile_Periodical.__init__(extlibraryprofile_Periodical(''), '') == None


from python_code import extlibraryprofile_BookOnTape
from python_code import extlibraryprofile_Class
from python_code import extlibraryprofile_Person

def test_extlibraryprofile_Person___init__():
    assert extlibraryprofile_Person.__init__(extlibraryprofile_Person('\x00\x00', '', extlibraryprofile_Person=set(), extlibraryprofile_Person5=extlibraryprofile_BookOnTape(), extlibraryprofile_Person8=extlibraryprofile_Class()), '', '', extlibraryprofile_Person=set(), extlibraryprofile_Person5=extlibraryprofile_BookOnTape(), extlibraryprofile_Person8=extlibraryprofile_Class()) == None


from python_code import extlibraryprofile_BookOnTape
from python_code import extlibraryprofile_Writer

def test_extlibraryprofile_Writer___init__():
    assert extlibraryprofile_Writer.__init__(extlibraryprofile_Writer('', extlibraryprofile_Writer=extlibraryprofile_BookOnTape()), '', extlibraryprofile_Writer=extlibraryprofile_BookOnTape()) == None

