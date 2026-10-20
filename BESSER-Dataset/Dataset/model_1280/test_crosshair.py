from python_code import EAssociationEnd
from python_code import EEntity
from python_code import ocl_dm_EAssociationEnd

def test_ocl_dm_EAssociationEnd___init__():
    assert ocl_dm_EAssociationEnd.__init__(ocl_dm_EAssociationEnd('', '\x00', ocl_dm_EAssociationEnd5=EAssociationEnd(), ocl_dm_EAssociationEnd=EEntity()), '\x00\x00', '', ocl_dm_EAssociationEnd5=EAssociationEnd(), ocl_dm_EAssociationEnd=EEntity()) == None


from python_code import ocl_dm_EAttribute

def test_ocl_dm_EAttribute___init__():
    assert ocl_dm_EAttribute.__init__(ocl_dm_EAttribute('', '\x00'), '\x00\x00', '') == None


from python_code import ocl_dm_EEntity
from python_code import ocl_exp_ETypeExp
from python_code import ocl_type_ECollectionType

def test_ocl_dm_EEntity___init__():
    assert ocl_dm_EEntity.__init__(ocl_dm_EEntity('', ocl_dm_EEntity=set(), ocl_dm_EEntity2=set(), EClassifier36=ocl_type_ECollectionType(), EClassifier=ocl_exp_ETypeExp()), '', ocl_dm_EEntity=set(), ocl_dm_EEntity2=set(), EClassifier36=ocl_type_ECollectionType(), EClassifier=ocl_exp_ETypeExp()) == None


from python_code import ocl_exp_EBooleanLiteralExp

def test_ocl_exp_EBooleanLiteralExp___init__():
    assert ocl_exp_EBooleanLiteralExp.__init__(ocl_exp_EBooleanLiteralExp(''), '') == None


from python_code import ocl_exp_EIntegerLiteralExp

def test_ocl_exp_EIntegerLiteralExp___init__():
    assert ocl_exp_EIntegerLiteralExp.__init__(ocl_exp_EIntegerLiteralExp(''), '') == None


from python_code import ELoopExp
from python_code import EOclExpression
from python_code import ocl_exp_EIteratorExp
from python_code import ocl_exp_EOclExpression
from python_code import ocl_exp_EVariable

def test_ocl_exp_EIteratorExp___init__():
    assert ocl_exp_EIteratorExp.__init__(ocl_exp_EIteratorExp('', ELoopExp22=ocl_exp_EOclExpression(), ELoopExp=ocl_exp_EVariable('', iterator=ELoopExp(), initializedElement=EOclExpression())), '', ELoopExp22=ocl_exp_EOclExpression(), ELoopExp=ocl_exp_EVariable('', iterator=ELoopExp(), initializedElement=EOclExpression())) == None


from python_code import ocl_exp_EOperationCallExp

def test_ocl_exp_EOperationCallExp___init__():
    assert ocl_exp_EOperationCallExp.__init__(ocl_exp_EOperationCallExp('\x00', parentCall=set()), '', parentCall=set()) == None


from python_code import ocl_exp_EStringLiteralExp

def test_ocl_exp_EStringLiteralExp___init__():
    assert ocl_exp_EStringLiteralExp.__init__(ocl_exp_EStringLiteralExp(''), '') == None


from python_code import ELoopExp
from python_code import EOclExpression
from python_code import ocl_exp_ECallExp
from python_code import ocl_exp_EVariable

def test_ocl_exp_EVariable___init__():
    assert ocl_exp_EVariable.__init__(ocl_exp_EVariable('', iterator=ELoopExp(), initializedElement=EOclExpression()), '', iterator=ELoopExp(), initializedElement=ocl_exp_ECallExp()) == None


from python_code import ESignal
from python_code import ocl_exp_ETypeExp
from python_code import ocl_type_ECollectionType
from python_code import ocl_type_EMessageType

def test_ocl_type_EMessageType___init__():
    assert ocl_type_EMessageType.__init__(ocl_type_EMessageType('', ocl_type_EMessageType=ESignal(), EClassifier36=ocl_type_ECollectionType(), EClassifier=ocl_exp_ETypeExp()), '', ocl_type_EMessageType=ESignal(), EClassifier36=ocl_type_ECollectionType(), EClassifier=ocl_exp_ETypeExp()) == None

