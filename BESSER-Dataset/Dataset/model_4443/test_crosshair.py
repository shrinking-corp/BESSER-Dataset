from python_code import ioT_ComparisonCondition
from python_code import ioT_Condition

def test_ioT_ComparisonCondition___init__():
    assert ioT_ComparisonCondition.__init__(ioT_ComparisonCondition('', ioT_ComparisonCondition=ioT_Condition(), ioT_ComparisonCondition58=ioT_Condition()), '', ioT_ComparisonCondition=ioT_Condition(), ioT_ComparisonCondition58=ioT_Condition()) == None


from python_code import ioT_LiteralBool

def test_ioT_LiteralBool___init__():
    assert ioT_LiteralBool.__init__(ioT_LiteralBool(''), '') == None


from python_code import ioT_LiteralNumber

def test_ioT_LiteralNumber___init__():
    assert ioT_LiteralNumber.__init__(ioT_LiteralNumber(0), 0) == None


from python_code import ioT_Method
from python_code import ioT_SensorGetMethod

def test_ioT_Method___init__():
    assert ioT_Method.__init__(ioT_Method('', '\x00', ioT_Method=ioT_SensorGetMethod()), '\x00\x00', '', ioT_Method=ioT_SensorGetMethod()) == None


from python_code import ioT_SensorGroup

def test_ioT_SensorGroup___init__():
    assert ioT_SensorGroup.__init__(ioT_SensorGroup('', ioT_SensorGroup=set()), '', ioT_SensorGroup=set()) == None

