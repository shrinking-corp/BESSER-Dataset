from python_code import operators_Marker
from python_code import operators_NetXResource
from python_code import operators_ResourceForecast
from python_code import operators_ResourceMonitor
from python_code import operators_Value

def test_operators_Marker___init__():
    assert operators_Marker.__init__(operators_Marker('', '\x00', operators_Marker=operators_Value(), operators_Marker10=operators_NetXResource(), operators_Marker68=operators_ResourceMonitor(), operators_Marker66=operators_ResourceForecast()), '\x00\x00', '', operators_Marker=operators_Value(), operators_Marker10=operators_NetXResource(), operators_Marker68=operators_ResourceMonitor(), operators_Marker66=operators_ResourceForecast()) == None


from python_code import operators_ToleranceMarker

def test_operators_ToleranceMarker___init__():
    assert operators_ToleranceMarker.__init__(operators_ToleranceMarker('', '\x00'), '\x00\x00', '') == None


from python_code import operators_Operator
from python_code import operators_Warehouse

def test_operators_Warehouse___init__():
    assert operators_Warehouse.__init__(operators_Warehouse('', '', operators_Warehouse=operators_Operator(), operators_Warehouse78=set(), operators_Warehouse81=set()), '', '', operators_Warehouse=operators_Operator(), operators_Warehouse78=set(), operators_Warehouse81=set()) == None

