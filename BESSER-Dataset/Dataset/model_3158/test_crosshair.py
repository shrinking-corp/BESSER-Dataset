from python_code import model_Comment
from python_code import model_CommentableElement

def test_model_Comment___init__():
    assert model_Comment.__init__(model_Comment('', model_Comment=model_CommentableElement()), '', model_Comment=model_CommentableElement()) == None


from python_code import model_DecimalLiteralExpression

def test_model_DecimalLiteralExpression___init__():
    assert model_DecimalLiteralExpression.__init__(model_DecimalLiteralExpression(''), '') == None


from python_code import model_Expression
from python_code import model_FieldAssignment
from python_code import model_RecordLiteralExpression

def test_model_FieldAssignment___init__():
    assert model_FieldAssignment.__init__(model_FieldAssignment('', model_FieldAssignment=model_RecordLiteralExpression(), model_FieldAssignment49=model_Expression()), '', model_FieldAssignment=model_RecordLiteralExpression(), model_FieldAssignment49=model_Expression()) == None


from python_code import model_IntegerLiteralExpression

def test_model_IntegerLiteralExpression___init__():
    assert model_IntegerLiteralExpression.__init__(model_IntegerLiteralExpression(''), '') == None


from python_code import model_IntegerRangeLiteralExpression

def test_model_IntegerRangeLiteralExpression___init__():
    assert model_IntegerRangeLiteralExpression.__init__(model_IntegerRangeLiteralExpression(False, False), False, False) == None


from python_code import model_NamedElement

def test_model_NamedElement___init__():
    assert model_NamedElement.__init__(model_NamedElement(''), '') == None


from python_code import model_OpaqueExpression

def test_model_OpaqueExpression___init__():
    assert model_OpaqueExpression.__init__(model_OpaqueExpression(''), '') == None


from python_code import model_RationalLiteralExpression

def test_model_RationalLiteralExpression___init__():
    assert model_RationalLiteralExpression.__init__(model_RationalLiteralExpression('', '\x00'), '\x00\x00', '') == None


from python_code import model_RecordAccessExpression

def test_model_RecordAccessExpression___init__():
    assert model_RecordAccessExpression.__init__(model_RecordAccessExpression(''), '') == None

