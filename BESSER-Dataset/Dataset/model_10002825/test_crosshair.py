from python_code import Contact

def test_Contact___init__():
    assert Contact.__init__(Contact('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Hotel
from python_code import HotelBusiness

def test_Hotel___init__():
    assert Hotel.__init__(Hotel('', hotelBusiness1=HotelBusiness(), roomType2=set(), booking9=set()), '', hotelBusiness1=HotelBusiness(), roomType2=set(), booking9=set()) == None

