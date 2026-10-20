from python_code import model_AbstractMClassFieldDeclaration

def test_model_AbstractMClassFieldDeclaration___init__():
    assert model_AbstractMClassFieldDeclaration.__init__(model_AbstractMClassFieldDeclaration('', False), '', False) == None


from python_code import model_AbstractMDeclaredType
from python_code import model_AbstractMTypeContainer
from python_code import model_MDeclaredTypeReference

def test_model_AbstractMDeclaredType___init__():
    assert model_AbstractMDeclaredType.__init__(model_AbstractMDeclaredType('', AbstractMDeclaredType=model_AbstractMTypeContainer(), types=model_AbstractMTypeContainer(), model_AbstractMDeclaredType=model_MDeclaredTypeReference()), '', AbstractMDeclaredType=model_AbstractMTypeContainer(), types=model_AbstractMTypeContainer(), model_AbstractMDeclaredType=model_MDeclaredTypeReference()) == None


from python_code import model_AbstractMExternalType
from python_code import model_MExternalTypeReference
from python_code import model_MRoot

def test_model_AbstractMExternalType___init__():
    assert model_AbstractMExternalType.__init__(model_AbstractMExternalType('', externalTypes=model_MRoot(), model_AbstractMExternalType=model_MExternalTypeReference(), AbstractMExternalType=model_MRoot()), '', externalTypes=model_MRoot(), model_AbstractMExternalType=model_MExternalTypeReference(), AbstractMExternalType=model_MRoot()) == None


from python_code import model_AbstractModifiers

def test_model_AbstractModifiers___init__():
    assert model_AbstractModifiers.__init__(model_AbstractModifiers(False, '', False), False, '', False) == None


from python_code import model_AbstractCExpression
from python_code import model_CDeclarationStatement

def test_model_CDeclarationStatement___init__():
    assert model_CDeclarationStatement.__init__(model_CDeclarationStatement(True, model_CDeclarationStatement=model_AbstractCExpression()), False, model_CDeclarationStatement=model_AbstractCExpression()) == None


from python_code import model_CUnparsedExpression

def test_model_CUnparsedExpression___init__():
    assert model_CUnparsedExpression.__init__(model_CUnparsedExpression(''), '') == None


from python_code import model_CUnparsedStatement

def test_model_CUnparsedStatement___init__():
    assert model_CUnparsedStatement.__init__(model_CUnparsedStatement(''), '') == None


from python_code import model_MAbstractClassMethodDeclaration
from python_code import model_MAbstractDeclaredClass

def test_model_MAbstractClassMethodDeclaration___init__():
    assert model_MAbstractClassMethodDeclaration.__init__(model_MAbstractClassMethodDeclaration('', MAbstractClassMethodDeclaration=model_MAbstractDeclaredClass(), abstractMethods=model_MAbstractDeclaredClass()), '', MAbstractClassMethodDeclaration=model_MAbstractDeclaredClass(), abstractMethods=model_MAbstractDeclaredClass()) == None


from python_code import model_MConstructor
from python_code import model_MConstructorParameter

def test_model_MConstructorParameter___init__():
    assert model_MConstructorParameter.__init__(model_MConstructorParameter(True, MConstructorParameter=model_MConstructor(), parameters68=model_MConstructor()), False, MConstructorParameter=model_MConstructor(), parameters68=model_MConstructor()) == None


from python_code import model_MDeclaredClass
from python_code import model_MInstanceClassFieldDeclaration

def test_model_MInstanceClassFieldDeclaration___init__():
    assert model_MInstanceClassFieldDeclaration.__init__(model_MInstanceClassFieldDeclaration(True, MInstanceClassFieldDeclaration=model_MDeclaredClass(), instanceFields=model_MDeclaredClass()), False, MInstanceClassFieldDeclaration=model_MDeclaredClass(), instanceFields=model_MDeclaredClass()) == None


from python_code import model_AbstractMMethodImplementation
from python_code import model_MMethodImplementationParameter

def test_model_MMethodImplementationParameter___init__():
    assert model_MMethodImplementationParameter.__init__(model_MMethodImplementationParameter(False, '\x00', MMethodImplementationParameter=model_AbstractMMethodImplementation(), parameters62=model_AbstractMMethodImplementation()), False, '\x00', MMethodImplementationParameter=model_AbstractMMethodImplementation(), parameters62=model_AbstractMMethodImplementation()) == None


from python_code import model_MPrimitiveTypeReference

def test_model_MPrimitiveTypeReference___init__():
    assert model_MPrimitiveTypeReference.__init__(model_MPrimitiveTypeReference(''), '') == None


from python_code import model_MResource

def test_model_MResource___init__():
    assert model_MResource.__init__(model_MResource(''), '') == None

