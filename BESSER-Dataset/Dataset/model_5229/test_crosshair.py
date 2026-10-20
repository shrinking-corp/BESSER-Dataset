from python_code import ilp_LiteralExpression

def test_ilp_LiteralExpression___init__():
    assert ilp_LiteralExpression.__init__(ilp_LiteralExpression(''), '') == None


from python_code import ilp_IntegerLinearProgram
from python_code import ilp_Variable
from python_code import ilp_VariableExpression

def test_ilp_Variable___init__():
    assert ilp_Variable.__init__(ilp_Variable('', '\x00', ilp_Variable=ilp_IntegerLinearProgram(), ilp_Variable10=ilp_VariableExpression()), '\x00\x00', '', ilp_Variable=ilp_IntegerLinearProgram(), ilp_Variable10=ilp_VariableExpression()) == None

