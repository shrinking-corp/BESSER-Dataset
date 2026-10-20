from python_code import Category

def test_Category___init__():
    assert Category.__init__(Category('', '', 0), '\x00', '', 0) == None


from python_code import DistanceInfo

def test_DistanceInfo___init__():
    assert DistanceInfo.__init__(DistanceInfo('', '', '\x00\x00'), '', '', '') == None


from python_code import Location

def test_Location___init__():
    assert Location.__init__(Location('', '\x00'), '\x00\x00', '') == None


from python_code import Place

def test_Place___init__():
    assert Place.__init__(Place('', '\x00'), '\x00\x00', '') == None


from python_code import Category
from python_code import DistanceInfo
from python_code import PlaceDetail

def test_PlaceDetail___init__():
    assert PlaceDetail.__init__(PlaceDetail(DistanceInfo('', '', ''), Category('', '', 0)), DistanceInfo('', '', ''), Category('', '\x00', 0)) == None

