from python_code import iOTConnector_Num

def test_iOTConnector_Num___init__():
    assert iOTConnector_Num.__init__(iOTConnector_Num(0), 0) == None


from python_code import iOTConnector_Program
from python_code import iOTConnector_Webserver

def test_iOTConnector_Webserver___init__():
    assert iOTConnector_Webserver.__init__(iOTConnector_Webserver('', 0, iOTConnector_Webserver=iOTConnector_Program()), '', 0, iOTConnector_Webserver=iOTConnector_Program()) == None


from python_code import iOTConnector_Program
from python_code import iOTConnector_Wifi

def test_iOTConnector_Wifi___init__():
    assert iOTConnector_Wifi.__init__(iOTConnector_Wifi('', '\x00', iOTConnector_Wifi=iOTConnector_Program()), '\x00\x00', '', iOTConnector_Wifi=iOTConnector_Program()) == None

