from python_code import units_av_pc_BaseUnit
from python_code import units_av_pc_UnitLiteral
from python_code import units_av_pc_UnitRepository

def test_units_av_pc_BaseUnit___init__():
    assert units_av_pc_BaseUnit.__init__(units_av_pc_BaseUnit('', units_av_pc_BaseUnit7=units_av_pc_UnitLiteral(), units_av_pc_BaseUnit=units_av_pc_UnitRepository()), '', units_av_pc_BaseUnit7=units_av_pc_UnitLiteral(), units_av_pc_BaseUnit=units_av_pc_UnitRepository()) == None


from python_code import units_av_pc_Unit
from python_code import units_av_pc_UnitCarryingElement

def test_units_av_pc_UnitCarryingElement___init__():
    assert units_av_pc_UnitCarryingElement.__init__(units_av_pc_UnitCarryingElement('', units_av_pc_UnitCarryingElement=units_av_pc_Unit()), '', units_av_pc_UnitCarryingElement=units_av_pc_Unit()) == None


from python_code import units_av_pc_Unit
from python_code import units_av_pc_UnitPower

def test_units_av_pc_UnitPower___init__():
    assert units_av_pc_UnitPower.__init__(units_av_pc_UnitPower(0, units_av_pc_UnitPower=units_av_pc_Unit()), 0, units_av_pc_UnitPower=units_av_pc_Unit()) == None

