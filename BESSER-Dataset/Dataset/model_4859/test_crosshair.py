from python_code import units_av_av_BaseUnit
from python_code import units_av_av_UnitLiteral
from python_code import units_av_av_UnitRepository

def test_units_av_av_BaseUnit___init__():
    assert units_av_av_BaseUnit.__init__(units_av_av_BaseUnit('', units_av_av_BaseUnit=units_av_av_UnitRepository(), units_av_av_BaseUnit7=units_av_av_UnitLiteral()), '', units_av_av_BaseUnit=units_av_av_UnitRepository(), units_av_av_BaseUnit7=units_av_av_UnitLiteral()) == None


from python_code import units_av_av_Unit
from python_code import units_av_av_UnitCarryingElement

def test_units_av_av_UnitCarryingElement___init__():
    assert units_av_av_UnitCarryingElement.__init__(units_av_av_UnitCarryingElement('', units_av_av_UnitCarryingElement=units_av_av_Unit()), '', units_av_av_UnitCarryingElement=units_av_av_Unit()) == None


from python_code import units_av_av_Unit
from python_code import units_av_av_UnitPower

def test_units_av_av_UnitPower___init__():
    assert units_av_av_UnitPower.__init__(units_av_av_UnitPower(0, units_av_av_UnitPower=units_av_av_Unit()), 0, units_av_av_UnitPower=units_av_av_Unit()) == None

