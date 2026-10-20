from python_code import NQC_AssignmentStatement
from python_code import NQC_Expression
from python_code import NQC_VariableExpression

def test_NQC_AssignmentStatement___init__():
    assert NQC_AssignmentStatement.__init__(NQC_AssignmentStatement('', NQC_AssignmentStatement=NQC_VariableExpression(), NQC_AssignmentStatement32=NQC_Expression()), '', NQC_AssignmentStatement=NQC_VariableExpression(), NQC_AssignmentStatement32=NQC_Expression()) == None


from python_code import NQC_BinaryExpression
from python_code import NQC_Expression

def test_NQC_BinaryExpression___init__():
    assert NQC_BinaryExpression.__init__(NQC_BinaryExpression('', NQC_BinaryExpression=NQC_Expression(), NQC_BinaryExpression98=NQC_Expression()), '', NQC_BinaryExpression=NQC_Expression(), NQC_BinaryExpression98=NQC_Expression()) == None


from python_code import NQC_BooleanConstant

def test_NQC_BooleanConstant___init__():
    assert NQC_BooleanConstant.__init__(NQC_BooleanConstant(True), False) == None


from python_code import NQC_Case
from python_code import NQC_SwitchStatement

def test_NQC_Case___init__():
    assert NQC_Case.__init__(NQC_Case(False, NQC_Case=NQC_SwitchStatement(), NQC_Case85=set(), NQC_Case88=set()), False, NQC_Case=NQC_SwitchStatement(), NQC_Case85=set(), NQC_Case88=set()) == None


from python_code import NQC_GoToStatement
from python_code import NQC_Label
from python_code import NQC_Statement

def test_NQC_Label___init__():
    assert NQC_Label.__init__(NQC_Label('', NQC_Label=NQC_Statement(), NQC_Label56=NQC_GoToStatement()), '', NQC_Label=NQC_Statement(), NQC_Label56=NQC_GoToStatement()) == None


from python_code import NQC_Program

def test_NQC_Program___init__():
    assert NQC_Program.__init__(NQC_Program('', NQC_Program=set(), NQC_Program2=set(), NQC_Program4=set(), NQC_Program6=set()), '', NQC_Program=set(), NQC_Program2=set(), NQC_Program4=set(), NQC_Program6=set()) == None

