from python_code import units_BaseUnit
from python_code import units_UnitRepository

def test_units_BaseUnit___init__():
    assert units_BaseUnit.__init__(units_BaseUnit('', units_BaseUnit=units_UnitRepository()), '', units_BaseUnit=units_UnitRepository()) == None


from python_code import units_Unit
from python_code import units_UnitPower

def test_units_UnitPower___init__():
    assert units_UnitPower.__init__(units_UnitPower(0, units_UnitPower=units_Unit()), 0, units_UnitPower=units_Unit()) == None

