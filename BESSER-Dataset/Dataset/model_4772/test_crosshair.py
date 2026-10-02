from python_code import model_EnumType

def test_model_EnumType___init__():
    assert model_EnumType.__init__(model_EnumType('', '\x00'), '\x00\x00', '') == None

def test_model_EnumType_addLiteral():
    assert model_EnumType.addLiteral(model_EnumType('', ''), '') == None

from python_code import model_MAssociationClass

def test_model_MAssociationClass___init__():
    assert model_MAssociationClass.__init__(model_MAssociationClass()) == None

def test_model_MAssociationClass_processWithVisitor():
    assert model_MAssociationClass.processWithVisitor(model_MAssociationClass(), '') == None

from python_code import model_MModelElement

def test_model_MModelElement___init__():
    assert model_MModelElement.__init__(model_MModelElement()) == None

def test_model_MModelElement_name():
    assert model_MModelElement.name(model_MModelElement()) == None

def test_model_MModelElement_processWithVisitor():
    assert model_MModelElement.processWithVisitor(model_MModelElement(), '') == None

from python_code import model_MModelElementEx

def test_model_MModelElementEx___init__():
    assert model_MModelElementEx.__init__(model_MModelElementEx(''), '') == None

def test_model_MModelElementEx_processWithVisitor():
    assert model_MModelElementEx.processWithVisitor(model_MModelElementEx(''), 0) == None

from python_code import model_TupleType

def test_model_TupleType___init__():
    assert model_TupleType.__init__(model_TupleType(''), '') == None
