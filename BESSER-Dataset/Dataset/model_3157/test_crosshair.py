from python_code import TTMCConstraint_DecimalLiteralExpression

def test_TTMCConstraint_DecimalLiteralExpression___init__():
    assert TTMCConstraint_DecimalLiteralExpression.__init__(TTMCConstraint_DecimalLiteralExpression(''), '') == None


from python_code import TTMCConstraint_Expression
from python_code import TTMCConstraint_FieldAssignment
from python_code import TTMCConstraint_RecordLiteralExpression

def test_TTMCConstraint_FieldAssignment___init__():
    assert TTMCConstraint_FieldAssignment.__init__(TTMCConstraint_FieldAssignment('', TTMCConstraint_FieldAssignment=TTMCConstraint_RecordLiteralExpression(), TTMCConstraint_FieldAssignment58=TTMCConstraint_Expression()), '', TTMCConstraint_FieldAssignment=TTMCConstraint_RecordLiteralExpression(), TTMCConstraint_FieldAssignment58=TTMCConstraint_Expression()) == None


from python_code import TTMCConstraint_IntegerLiteralExpression

def test_TTMCConstraint_IntegerLiteralExpression___init__():
    assert TTMCConstraint_IntegerLiteralExpression.__init__(TTMCConstraint_IntegerLiteralExpression(''), '') == None


from python_code import TTMCConstraint_NamedElement

def test_TTMCConstraint_NamedElement___init__():
    assert TTMCConstraint_NamedElement.__init__(TTMCConstraint_NamedElement(''), '') == None


from python_code import TTMCConstraint_RationalLiteralExpression

def test_TTMCConstraint_RationalLiteralExpression___init__():
    assert TTMCConstraint_RationalLiteralExpression.__init__(TTMCConstraint_RationalLiteralExpression('', '\x00'), '\x00\x00', '') == None


from python_code import TTMCConstraint_RecordAccessExpression

def test_TTMCConstraint_RecordAccessExpression___init__():
    assert TTMCConstraint_RecordAccessExpression.__init__(TTMCConstraint_RecordAccessExpression(''), '') == None


from python_code import TTMCConstraint_TupleAccessExpression

def test_TTMCConstraint_TupleAccessExpression___init__():
    assert TTMCConstraint_TupleAccessExpression.__init__(TTMCConstraint_TupleAccessExpression(''), '') == None

