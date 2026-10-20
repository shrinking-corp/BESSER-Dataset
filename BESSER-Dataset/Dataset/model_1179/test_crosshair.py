from python_code import simpleocl_BooleanExp

def test_simpleocl_BooleanExp___init__():
    assert simpleocl_BooleanExp.__init__(simpleocl_BooleanExp(''), '') == None


from python_code import simpleocl_EnumLiteralExp

def test_simpleocl_EnumLiteralExp___init__():
    assert simpleocl_EnumLiteralExp.__init__(simpleocl_EnumLiteralExp(''), '') == None


from python_code import simpleocl_IntegerExp

def test_simpleocl_IntegerExp___init__():
    assert simpleocl_IntegerExp.__init__(simpleocl_IntegerExp(''), '') == None


from python_code import simpleocl_IteratorExp

def test_simpleocl_IteratorExp___init__():
    assert simpleocl_IteratorExp.__init__(simpleocl_IteratorExp(''), '') == None


from python_code import simpleocl_IterateExp
from python_code import simpleocl_LetExp
from python_code import simpleocl_LocalVariable
from python_code import simpleocl_OclExpression

def test_simpleocl_LocalVariable___init__():
    assert simpleocl_LocalVariable.__init__(simpleocl_LocalVariable('', LocalVariable62=simpleocl_IterateExp(), LocalVariable64=simpleocl_LetExp(), LocalVariable=simpleocl_OclExpression(), variable=simpleocl_LetExp(), initializedVariable=simpleocl_OclExpression(), result=simpleocl_IterateExp()), '', LocalVariable62=simpleocl_IterateExp(), LocalVariable64=simpleocl_LetExp(), LocalVariable=simpleocl_OclExpression(), variable=simpleocl_LetExp(), initializedVariable=simpleocl_OclExpression(), result=simpleocl_IterateExp()) == None


from python_code import simpleocl_LocatedElement

def test_simpleocl_LocatedElement___init__():
    assert simpleocl_LocatedElement.__init__(simpleocl_LocatedElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import simpleocl_NamedElement

def test_simpleocl_NamedElement___init__():
    assert simpleocl_NamedElement.__init__(simpleocl_NamedElement(''), '') == None


from python_code import simpleocl_NavigationOrAttributeCall

def test_simpleocl_NavigationOrAttributeCall___init__():
    assert simpleocl_NavigationOrAttributeCall.__init__(simpleocl_NavigationOrAttributeCall(''), '') == None


from python_code import simpleocl_Module
from python_code import simpleocl_OclInstanceModel
from python_code import simpleocl_OclMetamodel

def test_simpleocl_OclMetamodel___init__():
    assert simpleocl_OclMetamodel.__init__(simpleocl_OclMetamodel('', simpleocl_OclMetamodel=simpleocl_Module(), metamodel=set(), OclMetamodel=simpleocl_OclInstanceModel()), '', simpleocl_OclMetamodel=simpleocl_Module(), metamodel=set(), OclMetamodel=simpleocl_OclInstanceModel()) == None


from python_code import simpleocl_OclModel
from python_code import simpleocl_OclModelElementExp

def test_simpleocl_OclModelElementExp___init__():
    assert simpleocl_OclModelElementExp.__init__(simpleocl_OclModelElementExp('', simpleocl_OclModelElementExp=simpleocl_OclModel()), '', simpleocl_OclModelElementExp=simpleocl_OclModel()) == None


from python_code import simpleocl_OclExpression
from python_code import simpleocl_OperationCall

def test_simpleocl_OperationCall___init__():
    assert simpleocl_OperationCall.__init__(simpleocl_OperationCall('', parentOperation=set(), OperationCall=simpleocl_OclExpression()), '', parentOperation=set(), OperationCall=simpleocl_OclExpression()) == None


from python_code import simpleocl_OclExpression
from python_code import simpleocl_OperatorCallExp

def test_simpleocl_OperatorCallExp___init__():
    assert simpleocl_OperatorCallExp.__init__(simpleocl_OperatorCallExp('', OperatorCallExp=simpleocl_OclExpression(), simpleocl_OperatorCallExp=simpleocl_OclExpression(), appliedOperator=simpleocl_OclExpression()), '', OperatorCallExp=simpleocl_OclExpression(), simpleocl_OperatorCallExp=simpleocl_OclExpression(), appliedOperator=simpleocl_OclExpression()) == None


from python_code import simpleocl_RealExp

def test_simpleocl_RealExp___init__():
    assert simpleocl_RealExp.__init__(simpleocl_RealExp(''), '') == None


from python_code import simpleocl_StaticNavigationOrAttributeCall

def test_simpleocl_StaticNavigationOrAttributeCall___init__():
    assert simpleocl_StaticNavigationOrAttributeCall.__init__(simpleocl_StaticNavigationOrAttributeCall(''), '') == None


from python_code import simpleocl_StaticOperationCall

def test_simpleocl_StaticOperationCall___init__():
    assert simpleocl_StaticOperationCall.__init__(simpleocl_StaticOperationCall('', simpleocl_StaticOperationCall=set()), '', simpleocl_StaticOperationCall=set()) == None


from python_code import simpleocl_StringExp

def test_simpleocl_StringExp___init__():
    assert simpleocl_StringExp.__init__(simpleocl_StringExp(''), '') == None

