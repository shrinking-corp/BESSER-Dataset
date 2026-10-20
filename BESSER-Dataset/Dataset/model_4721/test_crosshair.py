from python_code import ca_rule_IntegerLiteral

def test_ca_rule_IntegerLiteral___init__():
    assert ca_rule_IntegerLiteral.__init__(ca_rule_IntegerLiteral(0), 0) == None


from python_code import ca_rule_NeighborsExpression
from python_code import ca_rule_PopulationRange
from python_code import ca_rule_Rule

def test_ca_rule_PopulationRange___init__():
    assert ca_rule_PopulationRange.__init__(ca_rule_PopulationRange(0, 0, ca_rule_PopulationRange=ca_rule_Rule(), ca_rule_PopulationRange14=ca_rule_NeighborsExpression()), 0, 0, ca_rule_PopulationRange=ca_rule_Rule(), ca_rule_PopulationRange14=ca_rule_NeighborsExpression()) == None

