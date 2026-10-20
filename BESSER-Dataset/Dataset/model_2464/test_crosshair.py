from python_code import operators_Equipment
from python_code import operators_ExpansionExperience
from python_code import operators_Operator

def test_operators_ExpansionExperience___init__():
    assert operators_ExpansionExperience.__init__(operators_ExpansionExperience('', operators_ExpansionExperience=operators_Equipment(), operators_ExpansionExperience64=operators_Operator()), '', operators_ExpansionExperience=operators_Equipment(), operators_ExpansionExperience64=operators_Operator()) == None


from python_code import operators_Equipment
from python_code import operators_Function
from python_code import operators_Marker
from python_code import operators_ResourceForecast
from python_code import operators_ResourceMonitor
from python_code import operators_Value

def test_operators_Marker___init__():
    assert operators_Marker.__init__(operators_Marker('', '\x00', operators_Marker=operators_Equipment(), operators_Marker13=operators_Function(), operators_Marker82=operators_ResourceForecast(), operators_Marker84=operators_ResourceMonitor(), operators_Marker16=operators_Value()), '\x00\x00', '', operators_Marker=operators_Equipment(), operators_Marker13=operators_Function(), operators_Marker82=operators_ResourceForecast(), operators_Marker84=operators_ResourceMonitor(), operators_Marker16=operators_Value()) == None

