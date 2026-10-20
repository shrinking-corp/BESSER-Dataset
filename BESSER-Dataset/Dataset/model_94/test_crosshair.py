from python_code import javaMM_ArrayType
from python_code import javaMM_TypeAccess

def test_javaMM_ArrayType___init__():
    assert javaMM_ArrayType.__init__(javaMM_ArrayType(0, javaMM_ArrayType=javaMM_TypeAccess()), 0, javaMM_ArrayType=javaMM_TypeAccess()) == None


from python_code import javaMM_Assignment
from python_code import javaMM_Expression

def test_javaMM_Assignment___init__():
    assert javaMM_Assignment.__init__(javaMM_Assignment('', javaMM_Assignment=javaMM_Expression(), javaMM_Assignment83=javaMM_Expression()), '', javaMM_Assignment=javaMM_Expression(), javaMM_Assignment83=javaMM_Expression()) == None

def test_javaMM_Assignment_noRedundantAssignment():
    assert javaMM_Assignment.noRedundantAssignment(javaMM_Assignment('', javaMM_Assignment=javaMM_Expression(), javaMM_Assignment83=javaMM_Expression()), 0, '\x00\x00') == None


from python_code import javaMM_BooleanLiteral

def test_javaMM_BooleanLiteral___init__():
    assert javaMM_BooleanLiteral.__init__(javaMM_BooleanLiteral(''), '') == None


from python_code import javaMM_CharacterLiteral

def test_javaMM_CharacterLiteral___init__():
    assert javaMM_CharacterLiteral.__init__(javaMM_CharacterLiteral(''), '') == None


from python_code import javaMM_ClassDeclaration
from python_code import javaMM_TypeAccess

def test_javaMM_ClassDeclaration___init__():
    assert javaMM_ClassDeclaration.__init__(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), javaMM_ClassDeclaration=javaMM_TypeAccess()) == None

def test_javaMM_ClassDeclaration_hasCompareTo():
    assert javaMM_ClassDeclaration.hasCompareTo(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess())) == None

def test_javaMM_ClassDeclaration_hasHashcode():
    assert javaMM_ClassDeclaration.hasHashcode(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess())) == None

def test_javaMM_ClassDeclaration_hashCodeAndEquals():
    assert javaMM_ClassDeclaration.hashCodeAndEquals(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_noObscuredVariables():
    assert javaMM_ClassDeclaration.noObscuredVariables(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_comparatorImplementsSerializable():
    assert javaMM_ClassDeclaration.comparatorImplementsSerializable(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_noCovariantEquals():
    assert javaMM_ClassDeclaration.noCovariantEquals(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_getMethods():
    assert javaMM_ClassDeclaration.getMethods(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess())) == None

def test_javaMM_ClassDeclaration_noRedundantInterfaceImpl():
    assert javaMM_ClassDeclaration.noRedundantInterfaceImpl(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_equalsAndCompareTo():
    assert javaMM_ClassDeclaration.equalsAndCompareTo(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_serialUIDInSerializableClass():
    assert javaMM_ClassDeclaration.serialUIDInSerializableClass(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_cloneInCloneable():
    assert javaMM_ClassDeclaration.cloneInCloneable(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_noCovariantCompareTo():
    assert javaMM_ClassDeclaration.noCovariantCompareTo(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), '', '') == None

def test_javaMM_ClassDeclaration_hasEquals():
    assert javaMM_ClassDeclaration.hasEquals(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess())) == None


from python_code import javaMM_Expression
from python_code import javaMM_IfStatement
from python_code import javaMM_Statement

def test_javaMM_IfStatement___init__():
    assert javaMM_IfStatement.__init__(javaMM_IfStatement(javaMM_IfStatement=javaMM_Expression(), javaMM_IfStatement179=javaMM_Statement(), javaMM_IfStatement182=javaMM_Statement()), javaMM_IfStatement=javaMM_Expression(), javaMM_IfStatement179=javaMM_Statement(), javaMM_IfStatement182=javaMM_Statement()) == None

def test_javaMM_IfStatement_noUselessControlFlow():
    assert javaMM_IfStatement.noUselessControlFlow(javaMM_IfStatement(javaMM_IfStatement=javaMM_Expression(), javaMM_IfStatement179=javaMM_Statement(), javaMM_IfStatement182=javaMM_Statement()), '', '') == None

def test_javaMM_IfStatement_noDeadCode():
    assert javaMM_IfStatement.noDeadCode(javaMM_IfStatement(javaMM_IfStatement=javaMM_Expression(), javaMM_IfStatement179=javaMM_Statement(), javaMM_IfStatement182=javaMM_Statement()), '', '') == None


from python_code import javaMM_Expression
from python_code import javaMM_InfixExpression

def test_javaMM_InfixExpression___init__():
    assert javaMM_InfixExpression.__init__(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()), '', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()) == None

def test_javaMM_InfixExpression_equalsNotOnStrings():
    assert javaMM_InfixExpression.equalsNotOnStrings(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()), '\x00', '') == None

def test_javaMM_InfixExpression_noRedundantComparison():
    assert javaMM_InfixExpression.noRedundantComparison(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()), '\x00', '') == None

def test_javaMM_InfixExpression_equalsNotOnLiterals():
    assert javaMM_InfixExpression.equalsNotOnLiterals(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()), '\x00', '') == None

def test_javaMM_InfixExpression_operatorIsEquality():
    assert javaMM_InfixExpression.operatorIsEquality(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set())) == None


from python_code import javaMM_Manifest
from python_code import javaMM_ManifestEntry

def test_javaMM_ManifestEntry___init__():
    assert javaMM_ManifestEntry.__init__(javaMM_ManifestEntry('', javaMM_ManifestEntry=javaMM_Manifest(), javaMM_ManifestEntry211=set()), '', javaMM_ManifestEntry=javaMM_Manifest(), javaMM_ManifestEntry211=set()) == None


from python_code import javaMM_Expression
from python_code import javaMM_MethodInvocation

def test_javaMM_MethodInvocation___init__():
    assert javaMM_MethodInvocation.__init__(javaMM_MethodInvocation(javaMM_MethodInvocation=javaMM_Expression()), javaMM_MethodInvocation=javaMM_Expression()) == None

def test_javaMM_MethodInvocation_doesNotCallFinalize():
    assert javaMM_MethodInvocation.doesNotCallFinalize(javaMM_MethodInvocation(javaMM_MethodInvocation=javaMM_Expression()), '', '') == None

def test_javaMM_MethodInvocation_doesNotCallRunFinalizers():
    assert javaMM_MethodInvocation.doesNotCallRunFinalizers(javaMM_MethodInvocation(javaMM_MethodInvocation=javaMM_Expression()), '', '') == None

def test_javaMM_MethodInvocation_doesNotCallExit():
    assert javaMM_MethodInvocation.doesNotCallExit(javaMM_MethodInvocation(javaMM_MethodInvocation=javaMM_Expression()), '', '') == None


from python_code import javaMM_MethodRef
from python_code import javaMM_MethodRefParameter
from python_code import javaMM_TypeAccess

def test_javaMM_MethodRefParameter___init__():
    assert javaMM_MethodRefParameter.__init__(javaMM_MethodRefParameter('', '\x00', javaMM_MethodRefParameter=javaMM_MethodRef(), javaMM_MethodRefParameter233=javaMM_TypeAccess()), '\x00\x00', '', javaMM_MethodRefParameter=javaMM_MethodRef(), javaMM_MethodRefParameter233=javaMM_TypeAccess()) == None

