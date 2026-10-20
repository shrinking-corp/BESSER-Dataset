from python_code import java__ArrayType
from python_code import java__TypeAccess

def test_java__ArrayType___init__():
    assert java__ArrayType.__init__(java__ArrayType(0, java__ArrayType=java__TypeAccess()), 0, java__ArrayType=java__TypeAccess()) == None


from python_code import java__Assignment
from python_code import java__Expression

def test_java__Assignment___init__():
    assert java__Assignment.__init__(java__Assignment('', java__Assignment=java__Expression(), java__Assignment83=java__Expression()), '', java__Assignment=java__Expression(), java__Assignment83=java__Expression()) == None


from python_code import java__BooleanLiteral

def test_java__BooleanLiteral___init__():
    assert java__BooleanLiteral.__init__(java__BooleanLiteral(True), False) == None


from python_code import java__CharacterLiteral

def test_java__CharacterLiteral___init__():
    assert java__CharacterLiteral.__init__(java__CharacterLiteral(''), '') == None


from python_code import java__Expression
from python_code import java__InfixExpression

def test_java__InfixExpression___init__():
    assert java__InfixExpression.__init__(java__InfixExpression('', java__InfixExpression=java__Expression(), java__InfixExpression191=set(), java__InfixExpression188=java__Expression()), '', java__InfixExpression=java__Expression(), java__InfixExpression191=set(), java__InfixExpression188=java__Expression()) == None


from python_code import java__Manifest
from python_code import java__ManifestEntry

def test_java__ManifestEntry___init__():
    assert java__ManifestEntry.__init__(java__ManifestEntry('', java__ManifestEntry=java__Manifest(), java__ManifestEntry211=set()), '', java__ManifestEntry=java__Manifest(), java__ManifestEntry211=set()) == None


from python_code import java__MethodRef
from python_code import java__MethodRefParameter
from python_code import java__TypeAccess

def test_java__MethodRefParameter___init__():
    assert java__MethodRefParameter.__init__(java__MethodRefParameter('', False, java__MethodRefParameter=java__MethodRef(), java__MethodRefParameter233=java__TypeAccess()), '', False, java__MethodRefParameter=java__MethodRef(), java__MethodRefParameter233=java__TypeAccess()) == None

