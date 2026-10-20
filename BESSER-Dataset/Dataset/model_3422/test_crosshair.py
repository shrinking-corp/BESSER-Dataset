from python_code import location_Location

def test_location_Location___init__():
    assert location_Location.__init__(location_Location('', '', '', '', '', '', '', float('inf'), 0.0, 0.0, '', '', '', location_Location=set()), '', '\x00', '', '', '', '', '', 0.0, 0.0, 0.0, '', '', '', location_Location=set()) == None

def test_location_Location_getAddress():
    assert location_Location.getAddress(location_Location('\x00', '', '', '', '', '', '', 0.0, 0.0, 0.0, '', '', '', location_Location=set())) == None

def test_location_Location_containsPoint():
    assert location_Location.containsPoint(location_Location('', '', '', '', '', '', '', 0.0, float('inf'), 0.0, '', '', '', location_Location=set()), 0) == None

def test_location_Location_getCoordinates():
    assert location_Location.getCoordinates(location_Location('\x00', '', '', '', '', '', '', 0.0, 0.0, 0.0, '', '', '', location_Location=set())) == None

def test_location_Location_locate():
    assert location_Location.locate(location_Location('', '', '', '', '', '', '', 0.0, float('inf'), 0.0, '', '', '', location_Location=set()), 0) == None

