from python_code import miniJava_Boolean

def test_miniJava_Boolean___init__():
    assert miniJava_Boolean.__init__(miniJava_Boolean(True), False) == None


from python_code import miniJava_ArrayAssignment
from python_code import miniJava_Assignment
from python_code import miniJava_Class
from python_code import miniJava_ClassConstruction
from python_code import miniJava_ClassifierReference
from python_code import miniJava_ClassifierType
from python_code import miniJava_FunctionCall
from python_code import miniJava_Identifier
from python_code import miniJava_MainClass
from python_code import miniJava_MethodDeclaration
from python_code import miniJava_VariableDeclaration

def test_miniJava_Identifier___init__():
    assert miniJava_Identifier.__init__(miniJava_Identifier('', miniJava_Identifier=miniJava_MainClass(), miniJava_Identifier7=miniJava_MainClass(), miniJava_Identifier12=miniJava_Class(), miniJava_Identifier15=miniJava_Class(), miniJava_Identifier43=miniJava_ClassifierType(), miniJava_Identifier24=miniJava_VariableDeclaration(), miniJava_Identifier30=miniJava_MethodDeclaration(), miniJava_Identifier62=miniJava_Assignment(), miniJava_Identifier67=miniJava_ArrayAssignment(), miniJava_Identifier115=miniJava_ClassifierReference(), miniJava_Identifier119=miniJava_ClassConstruction(), miniJava_Identifier110=miniJava_FunctionCall()), '', miniJava_Identifier=miniJava_MainClass(), miniJava_Identifier7=miniJava_MainClass(), miniJava_Identifier12=miniJava_Class(), miniJava_Identifier15=miniJava_Class(), miniJava_Identifier43=miniJava_ClassifierType(), miniJava_Identifier24=miniJava_VariableDeclaration(), miniJava_Identifier30=miniJava_MethodDeclaration(), miniJava_Identifier62=miniJava_Assignment(), miniJava_Identifier67=miniJava_ArrayAssignment(), miniJava_Identifier115=miniJava_ClassifierReference(), miniJava_Identifier119=miniJava_ClassConstruction(), miniJava_Identifier110=miniJava_FunctionCall()) == None


from python_code import miniJava_IntLiteral

def test_miniJava_IntLiteral___init__():
    assert miniJava_IntLiteral.__init__(miniJava_IntLiteral(0), 0) == None

