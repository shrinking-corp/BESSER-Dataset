from python_code import jsm_AbstractMClassFieldDeclaration

def test_jsm_AbstractMClassFieldDeclaration___init__():
    assert jsm_AbstractMClassFieldDeclaration.__init__(jsm_AbstractMClassFieldDeclaration('', False), '', False) == None


from python_code import jsm_AbstractMDeclaredType
from python_code import jsm_AbstractMTypeContainer
from python_code import jsm_MDeclaredTypeReference

def test_jsm_AbstractMDeclaredType___init__():
    assert jsm_AbstractMDeclaredType.__init__(jsm_AbstractMDeclaredType('', types=jsm_AbstractMTypeContainer(), jsm_AbstractMDeclaredType=jsm_MDeclaredTypeReference(), AbstractMDeclaredType=jsm_AbstractMTypeContainer()), '', types=jsm_AbstractMTypeContainer(), jsm_AbstractMDeclaredType=jsm_MDeclaredTypeReference(), AbstractMDeclaredType=jsm_AbstractMTypeContainer()) == None


from python_code import jsm_AbstractMExternalType
from python_code import jsm_MExternalTypeReference
from python_code import jsm_MRoot

def test_jsm_AbstractMExternalType___init__():
    assert jsm_AbstractMExternalType.__init__(jsm_AbstractMExternalType('', jsm_AbstractMExternalType=jsm_MExternalTypeReference(), externalTypes=jsm_MRoot(), AbstractMExternalType=jsm_MRoot()), '', jsm_AbstractMExternalType=jsm_MExternalTypeReference(), externalTypes=jsm_MRoot(), AbstractMExternalType=jsm_MRoot()) == None


from python_code import jsm_AbstractModifiers

def test_jsm_AbstractModifiers___init__():
    assert jsm_AbstractModifiers.__init__(jsm_AbstractModifiers('', False, False), '\x00', False, False) == None


from python_code import jsm_AbstractCExpression
from python_code import jsm_CDeclarationStatement

def test_jsm_CDeclarationStatement___init__():
    assert jsm_CDeclarationStatement.__init__(jsm_CDeclarationStatement(True, jsm_CDeclarationStatement=jsm_AbstractCExpression()), False, jsm_CDeclarationStatement=jsm_AbstractCExpression()) == None


from python_code import jsm_CUnparsedExpression

def test_jsm_CUnparsedExpression___init__():
    assert jsm_CUnparsedExpression.__init__(jsm_CUnparsedExpression(''), '') == None


from python_code import jsm_CUnparsedStatement

def test_jsm_CUnparsedStatement___init__():
    assert jsm_CUnparsedStatement.__init__(jsm_CUnparsedStatement(''), '') == None


from python_code import jsm_MAbstractClassMethodDeclaration
from python_code import jsm_MAbstractDeclaredClass

def test_jsm_MAbstractClassMethodDeclaration___init__():
    assert jsm_MAbstractClassMethodDeclaration.__init__(jsm_MAbstractClassMethodDeclaration('', MAbstractClassMethodDeclaration=jsm_MAbstractDeclaredClass(), abstractMethods=jsm_MAbstractDeclaredClass()), '', MAbstractClassMethodDeclaration=jsm_MAbstractDeclaredClass(), abstractMethods=jsm_MAbstractDeclaredClass()) == None


from python_code import jsm_MConstructor
from python_code import jsm_MConstructorParameter

def test_jsm_MConstructorParameter___init__():
    assert jsm_MConstructorParameter.__init__(jsm_MConstructorParameter(True, MConstructorParameter=jsm_MConstructor(), parameters68=jsm_MConstructor()), False, MConstructorParameter=jsm_MConstructor(), parameters68=jsm_MConstructor()) == None


from python_code import jsm_MDeclaredClass
from python_code import jsm_MInstanceClassFieldDeclaration

def test_jsm_MInstanceClassFieldDeclaration___init__():
    assert jsm_MInstanceClassFieldDeclaration.__init__(jsm_MInstanceClassFieldDeclaration(True, MInstanceClassFieldDeclaration=jsm_MDeclaredClass(), instanceFields=jsm_MDeclaredClass()), False, MInstanceClassFieldDeclaration=jsm_MDeclaredClass(), instanceFields=jsm_MDeclaredClass()) == None


from python_code import jsm_AbstractMMethodImplementation
from python_code import jsm_MMethodImplementationParameter

def test_jsm_MMethodImplementationParameter___init__():
    assert jsm_MMethodImplementationParameter.__init__(jsm_MMethodImplementationParameter(False, '\x00', parameters62=jsm_AbstractMMethodImplementation(), MMethodImplementationParameter=jsm_AbstractMMethodImplementation()), False, '\x00', parameters62=jsm_AbstractMMethodImplementation(), MMethodImplementationParameter=jsm_AbstractMMethodImplementation()) == None


from python_code import jsm_MPrimitiveTypeReference

def test_jsm_MPrimitiveTypeReference___init__():
    assert jsm_MPrimitiveTypeReference.__init__(jsm_MPrimitiveTypeReference(''), '') == None


from python_code import jsm_MResource

def test_jsm_MResource___init__():
    assert jsm_MResource.__init__(jsm_MResource(''), '') == None

