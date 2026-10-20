from python_code import drone_Coordinate
from python_code import drone_Position

def test_drone_Coordinate___init__():
    assert drone_Coordinate.__init__(drone_Coordinate(0.0, 0.0, 0.0, drone_Coordinate=drone_Position()), 0.0, 0.0, 0.0, drone_Coordinate=drone_Position()) == None


from python_code import drone_MeasureConversion
from python_code import drone_MeasureDimension

def test_drone_MeasureConversion___init__():
    assert drone_MeasureConversion.__init__(drone_MeasureConversion(0.0, drone_MeasureConversion=drone_MeasureDimension(), drone_MeasureConversion82=drone_MeasureDimension()), 0.0, drone_MeasureConversion=drone_MeasureDimension(), drone_MeasureConversion82=drone_MeasureDimension()) == None


from python_code import drone_Battery
from python_code import drone_MeasureDimension
from python_code import drone_MeasureValue
from python_code import drone_Robot
from python_code import drone_Size

def test_drone_MeasureValue___init__():
    assert drone_MeasureValue.__init__(drone_MeasureValue(0.0, drone_MeasureValue=drone_Robot(), drone_MeasureValue42=drone_Robot(), drone_MeasureValue51=drone_Size(), drone_MeasureValue54=drone_Size(), drone_MeasureValue57=drone_Size(), drone_MeasureValue60=drone_Battery(), drone_MeasureValue63=drone_Battery(), drone_MeasureValue66=drone_Battery(), drone_MeasureValue77=drone_MeasureDimension()), 0.0, drone_MeasureValue=drone_Robot(), drone_MeasureValue42=drone_Robot(), drone_MeasureValue51=drone_Size(), drone_MeasureValue54=drone_Size(), drone_MeasureValue57=drone_Size(), drone_MeasureValue60=drone_Battery(), drone_MeasureValue63=drone_Battery(), drone_MeasureValue66=drone_Battery(), drone_MeasureValue77=drone_MeasureDimension()) == None


from python_code import drone_NamedElement

def test_drone_NamedElement___init__():
    assert drone_NamedElement.__init__(drone_NamedElement(''), '') == None


from python_code import drone_StringValue

def test_drone_StringValue___init__():
    assert drone_StringValue.__init__(drone_StringValue(''), '') == None

