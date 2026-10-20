from python_code import oogen_OOBoolLiteral

def test_oogen_OOBoolLiteral___init__():
    assert oogen_OOBoolLiteral.__init__(oogen_OOBoolLiteral(True), False) == None


from python_code import oogen_OOComment
from python_code import oogen_OOCommentOwner

def test_oogen_OOComment___init__():
    assert oogen_OOComment.__init__(oogen_OOComment('', False, oogen_OOComment=oogen_OOCommentOwner(), oogen_OOComment144=oogen_OOCommentOwner()), '', False, oogen_OOComment=oogen_OOCommentOwner(), oogen_OOComment144=oogen_OOCommentOwner()) == None


from python_code import oogen_OODoubleLiteral

def test_oogen_OODoubleLiteral___init__():
    assert oogen_OODoubleLiteral.__init__(oogen_OODoubleLiteral(0.0), 0.0) == None


from python_code import oogen_OOExpression
from python_code import oogen_OOFieldReferenceExpression

def test_oogen_OOFieldReferenceExpression___init__():
    assert oogen_OOFieldReferenceExpression.__init__(oogen_OOFieldReferenceExpression('', oogen_OOFieldReferenceExpression=oogen_OOExpression()), '', oogen_OOFieldReferenceExpression=oogen_OOExpression()) == None


from python_code import oogen_OOFloatLiteral

def test_oogen_OOFloatLiteral___init__():
    assert oogen_OOFloatLiteral.__init__(oogen_OOFloatLiteral(0.0), 0.0) == None


from python_code import oogen_OOExpression
from python_code import oogen_OOFunctionCallExpression

def test_oogen_OOFunctionCallExpression___init__():
    assert oogen_OOFunctionCallExpression.__init__(oogen_OOFunctionCallExpression('', oogen_OOFunctionCallExpression=set(), oogen_OOFunctionCallExpression128=oogen_OOExpression()), '', oogen_OOFunctionCallExpression=set(), oogen_OOFunctionCallExpression128=oogen_OOExpression()) == None


from python_code import oogen_OOIntegerLiteral

def test_oogen_OOIntegerLiteral___init__():
    assert oogen_OOIntegerLiteral.__init__(oogen_OOIntegerLiteral(0), 0) == None


from python_code import oogen_OOLanguageSpecificExpression
from python_code import oogen_OOLanguageSpecificSnippet

def test_oogen_OOLanguageSpecificSnippet___init__():
    assert oogen_OOLanguageSpecificSnippet.__init__(oogen_OOLanguageSpecificSnippet('', '\x00', oogen_OOLanguageSpecificSnippet=oogen_OOLanguageSpecificExpression()), '\x00\x00', '', oogen_OOLanguageSpecificSnippet=oogen_OOLanguageSpecificExpression()) == None


from python_code import oogen_OOLogicalLiteral

def test_oogen_OOLogicalLiteral___init__():
    assert oogen_OOLogicalLiteral.__init__(oogen_OOLogicalLiteral(True), False) == None


from python_code import oogen_OOLongLiteral

def test_oogen_OOLongLiteral___init__():
    assert oogen_OOLongLiteral.__init__(oogen_OOLongLiteral(''), '') == None


from python_code import oogen_OONewClass

def test_oogen_OONewClass___init__():
    assert oogen_OONewClass.__init__(oogen_OONewClass('', oogen_OONewClass=set()), '', oogen_OONewClass=set()) == None


from python_code import oogen_OOStringLiteral

def test_oogen_OOStringLiteral___init__():
    assert oogen_OOStringLiteral.__init__(oogen_OOStringLiteral(''), '') == None


from python_code import oogen_OOTwoOperandAssignableExpression

def test_oogen_OOTwoOperandAssignableExpression___init__():
    assert oogen_OOTwoOperandAssignableExpression.__init__(oogen_OOTwoOperandAssignableExpression(True), False) == None

