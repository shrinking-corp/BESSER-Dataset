from python_code import rule_IntegerLiteral

def test_rule_IntegerLiteral___init__():
    assert rule_IntegerLiteral.__init__(rule_IntegerLiteral(0), 0) == None


from python_code import rule_NeighborsExpression
from python_code import rule_PopulationRange
from python_code import rule_Rule

def test_rule_PopulationRange___init__():
    assert rule_PopulationRange.__init__(rule_PopulationRange(0, 0, rule_PopulationRange=rule_Rule(), rule_PopulationRange14=rule_NeighborsExpression()), 0, 0, rule_PopulationRange=rule_Rule(), rule_PopulationRange14=rule_NeighborsExpression()) == None

