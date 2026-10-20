from python_code import OCLinEmig_BooleanExp

def test_OCLinEmig_BooleanExp___init__():
    assert OCLinEmig_BooleanExp.__init__(OCLinEmig_BooleanExp(''), '') == None


from python_code import OCLinEmig_EnumLiteralExp

def test_OCLinEmig_EnumLiteralExp___init__():
    assert OCLinEmig_EnumLiteralExp.__init__(OCLinEmig_EnumLiteralExp(''), '') == None


from python_code import OCLinEmig_IntegerExp

def test_OCLinEmig_IntegerExp___init__():
    assert OCLinEmig_IntegerExp.__init__(OCLinEmig_IntegerExp(''), '') == None


from python_code import OCLinEmig_IteratorExp

def test_OCLinEmig_IteratorExp___init__():
    assert OCLinEmig_IteratorExp.__init__(OCLinEmig_IteratorExp(''), '') == None


from python_code import OCLinEmig_LocatedElement

def test_OCLinEmig_LocatedElement___init__():
    assert OCLinEmig_LocatedElement.__init__(OCLinEmig_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import OCLinEmig_Module

def test_OCLinEmig_Module___init__():
    assert OCLinEmig_Module.__init__(OCLinEmig_Module('', OCLinEmig_Module=set()), '', OCLinEmig_Module=set()) == None


from python_code import OCLinEmig_NavigationOrAttributeCallExp

def test_OCLinEmig_NavigationOrAttributeCallExp___init__():
    assert OCLinEmig_NavigationOrAttributeCallExp.__init__(OCLinEmig_NavigationOrAttributeCallExp(''), '') == None


from python_code import OCLinEmig_OclExpression
from python_code import OCLinEmig_OperationCallExp

def test_OCLinEmig_OperationCallExp___init__():
    assert OCLinEmig_OperationCallExp.__init__(OCLinEmig_OperationCallExp('', OperationCallExp=OCLinEmig_OclExpression(), parentOperation=set()), '', OperationCallExp=OCLinEmig_OclExpression(), parentOperation=set()) == None


from python_code import OCLinEmig_RealExp

def test_OCLinEmig_RealExp___init__():
    assert OCLinEmig_RealExp.__init__(OCLinEmig_RealExp(''), '') == None


from python_code import OCLinEmig_StringExp

def test_OCLinEmig_StringExp___init__():
    assert OCLinEmig_StringExp.__init__(OCLinEmig_StringExp(''), '') == None

