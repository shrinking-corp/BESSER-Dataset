from python_code import ioT_FetchDataCondition

def test_ioT_FetchDataCondition___init__():
    assert ioT_FetchDataCondition.__init__(ioT_FetchDataCondition(''), '') == None


from python_code import ioT_Method
from python_code import ioT_SensorGetMethod

def test_ioT_Method___init__():
    assert ioT_Method.__init__(ioT_Method('', '\x00', ioT_Method=ioT_SensorGetMethod()), '\x00\x00', '', ioT_Method=ioT_SensorGetMethod()) == None


from python_code import ioT_SensorGroup

def test_ioT_SensorGroup___init__():
    assert ioT_SensorGroup.__init__(ioT_SensorGroup('', ioT_SensorGroup=set()), '', ioT_SensorGroup=set()) == None

