from python_code import EmigOcl_BooleanExp

def test_EmigOcl_BooleanExp___init__():
    assert EmigOcl_BooleanExp.__init__(EmigOcl_BooleanExp(''), '') == None


from python_code import EmigOcl_EnumLiteralExp

def test_EmigOcl_EnumLiteralExp___init__():
    assert EmigOcl_EnumLiteralExp.__init__(EmigOcl_EnumLiteralExp(''), '') == None


from python_code import EmigOcl_IntegerExp

def test_EmigOcl_IntegerExp___init__():
    assert EmigOcl_IntegerExp.__init__(EmigOcl_IntegerExp(''), '') == None


from python_code import EmigOcl_IteratorExp

def test_EmigOcl_IteratorExp___init__():
    assert EmigOcl_IteratorExp.__init__(EmigOcl_IteratorExp(''), '') == None


from python_code import EmigOcl_IterateExp
from python_code import EmigOcl_LetExp
from python_code import EmigOcl_LocalVariable
from python_code import EmigOcl_OclExpression

def test_EmigOcl_LocalVariable___init__():
    assert EmigOcl_LocalVariable.__init__(EmigOcl_LocalVariable('', LocalVariable=EmigOcl_OclExpression(), LocalVariable50=EmigOcl_IterateExp(), LocalVariable52=EmigOcl_LetExp(), variable=EmigOcl_LetExp(), initializedVariable=EmigOcl_OclExpression(), result=EmigOcl_IterateExp()), '', LocalVariable=EmigOcl_OclExpression(), LocalVariable50=EmigOcl_IterateExp(), LocalVariable52=EmigOcl_LetExp(), variable=EmigOcl_LetExp(), initializedVariable=EmigOcl_OclExpression(), result=EmigOcl_IterateExp()) == None


from python_code import EmigOcl_LocatedElement

def test_EmigOcl_LocatedElement___init__():
    assert EmigOcl_LocatedElement.__init__(EmigOcl_LocatedElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import EmigOcl_Module

def test_EmigOcl_Module___init__():
    assert EmigOcl_Module.__init__(EmigOcl_Module('', EmigOcl_Module=set(), EmigOcl_Module2=set()), '', EmigOcl_Module=set(), EmigOcl_Module2=set()) == None


from python_code import EmigOcl_NavigationOrAttributeCall

def test_EmigOcl_NavigationOrAttributeCall___init__():
    assert EmigOcl_NavigationOrAttributeCall.__init__(EmigOcl_NavigationOrAttributeCall(''), '') == None


from python_code import EmigOcl_OclExpression
from python_code import EmigOcl_OperationCall

def test_EmigOcl_OperationCall___init__():
    assert EmigOcl_OperationCall.__init__(EmigOcl_OperationCall('', OperationCall=EmigOcl_OclExpression(), parentOperation=set()), '', OperationCall=EmigOcl_OclExpression(), parentOperation=set()) == None


from python_code import EmigOcl_OclExpression
from python_code import EmigOcl_OperatorCallExp

def test_EmigOcl_OperatorCallExp___init__():
    assert EmigOcl_OperatorCallExp.__init__(EmigOcl_OperatorCallExp('', EmigOcl_OperatorCallExp=EmigOcl_OclExpression()), '', EmigOcl_OperatorCallExp=EmigOcl_OclExpression()) == None


from python_code import EmigOcl_RealExp

def test_EmigOcl_RealExp___init__():
    assert EmigOcl_RealExp.__init__(EmigOcl_RealExp(''), '') == None


from python_code import EmigOcl_StaticNavigationOrAttributeCall

def test_EmigOcl_StaticNavigationOrAttributeCall___init__():
    assert EmigOcl_StaticNavigationOrAttributeCall.__init__(EmigOcl_StaticNavigationOrAttributeCall(''), '') == None


from python_code import EmigOcl_StaticOperationCall

def test_EmigOcl_StaticOperationCall___init__():
    assert EmigOcl_StaticOperationCall.__init__(EmigOcl_StaticOperationCall('', EmigOcl_StaticOperationCall=set()), '', EmigOcl_StaticOperationCall=set()) == None


from python_code import EmigOcl_StringExp

def test_EmigOcl_StringExp___init__():
    assert EmigOcl_StringExp.__init__(EmigOcl_StringExp(''), '') == None

