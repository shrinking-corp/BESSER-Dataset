from python_code import units_BaseUnit
from python_code import units_UnitLiteral
from python_code import units_UnitRepository

def test_units_BaseUnit___init__():
    assert units_BaseUnit.__init__(units_BaseUnit('', units_BaseUnit=units_UnitRepository(), units_BaseUnit7=units_UnitLiteral()), '', units_BaseUnit=units_UnitRepository(), units_BaseUnit7=units_UnitLiteral()) == None


from python_code import units_Unit
from python_code import units_UnitCarryingElement

def test_units_UnitCarryingElement___init__():
    assert units_UnitCarryingElement.__init__(units_UnitCarryingElement('', units_UnitCarryingElement=units_Unit()), '', units_UnitCarryingElement=units_Unit()) == None


from python_code import units_Unit
from python_code import units_UnitPower

def test_units_UnitPower___init__():
    assert units_UnitPower.__init__(units_UnitPower(0, units_UnitPower=units_Unit()), 0, units_UnitPower=units_Unit()) == None

