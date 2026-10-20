from python_code import sADL_AbstractSadlEquation
from python_code import sADL_SadlResource
from python_code import sADL_SadlTypeReference

def test_sADL_AbstractSadlEquation___init__():
    assert sADL_AbstractSadlEquation.__init__(sADL_AbstractSadlEquation('', sADL_AbstractSadlEquation=sADL_SadlResource(), sADL_AbstractSadlEquation11=set(), sADL_AbstractSadlEquation13=sADL_SadlTypeReference()), '', sADL_AbstractSadlEquation=sADL_SadlResource(), sADL_AbstractSadlEquation11=set(), sADL_AbstractSadlEquation13=sADL_SadlTypeReference()) == None


from python_code import sADL_BinaryOperation
from python_code import sADL_Expression

def test_sADL_BinaryOperation___init__():
    assert sADL_BinaryOperation.__init__(sADL_BinaryOperation('', sADL_BinaryOperation=sADL_Expression(), sADL_BinaryOperation221=sADL_Expression()), '', sADL_BinaryOperation=sADL_Expression(), sADL_BinaryOperation221=sADL_Expression()) == None


from python_code import sADL_BooleanLiteral

def test_sADL_BooleanLiteral___init__():
    assert sADL_BooleanLiteral.__init__(sADL_BooleanLiteral(''), '') == None


from python_code import sADL_Constant

def test_sADL_Constant___init__():
    assert sADL_Constant.__init__(sADL_Constant(''), '') == None


from python_code import sADL_Declaration
from python_code import sADL_SadlTypeReference

def test_sADL_Declaration___init__():
    assert sADL_Declaration.__init__(sADL_Declaration('', '', '', '', sADL_Declaration=sADL_SadlTypeReference(), sADL_Declaration245=set()), '', '', '', '', sADL_Declaration=sADL_SadlTypeReference(), sADL_Declaration245=set()) == None


from python_code import sADL_ElementInList
from python_code import sADL_Expression

def test_sADL_ElementInList___init__():
    assert sADL_ElementInList.__init__(sADL_ElementInList(False, False, sADL_ElementInList=sADL_Expression()), False, False, sADL_ElementInList=sADL_Expression()) == None


from python_code import sADL_EndWriteStatement

def test_sADL_EndWriteStatement___init__():
    assert sADL_EndWriteStatement.__init__(sADL_EndWriteStatement(''), '') == None


from python_code import sADL_Expression
from python_code import sADL_ExpressionStatement

def test_sADL_ExpressionStatement___init__():
    assert sADL_ExpressionStatement.__init__(sADL_ExpressionStatement('', sADL_ExpressionStatement=sADL_Expression()), '', sADL_ExpressionStatement=sADL_Expression()) == None


from python_code import sADL_ExternalEquationStatement

def test_sADL_ExternalEquationStatement___init__():
    assert sADL_ExternalEquationStatement.__init__(sADL_ExternalEquationStatement('', '\x00'), '\x00\x00', '') == None


from python_code import sADL_Name

def test_sADL_Name___init__():
    assert sADL_Name.__init__(sADL_Name(False, sADL_Name=set()), False, sADL_Name=set()) == None


from python_code import sADL_NumberLiteral

def test_sADL_NumberLiteral___init__():
    assert sADL_NumberLiteral.__init__(sADL_NumberLiteral(''), '') == None


from python_code import sADL_PrintStatement

def test_sADL_PrintStatement___init__():
    assert sADL_PrintStatement.__init__(sADL_PrintStatement('', '\x00'), '\x00\x00', '') == None


from python_code import sADL_Expression
from python_code import sADL_PropOfSubject

def test_sADL_PropOfSubject___init__():
    assert sADL_PropOfSubject.__init__(sADL_PropOfSubject('', sADL_PropOfSubject=sADL_Expression(), sADL_PropOfSubject226=sADL_Expression()), '', sADL_PropOfSubject=sADL_Expression(), sADL_PropOfSubject226=sADL_Expression()) == None


from python_code import sADL_Expression
from python_code import sADL_QueryStatement
from python_code import sADL_SadlResource

def test_sADL_QueryStatement___init__():
    assert sADL_QueryStatement.__init__(sADL_QueryStatement('', sADL_QueryStatement188=sADL_Expression(), sADL_QueryStatement=sADL_SadlResource(), sADL_QueryStatement185=set()), '', sADL_QueryStatement188=sADL_Expression(), sADL_QueryStatement=sADL_SadlResource(), sADL_QueryStatement185=set()) == None


from python_code import sADL_ReadStatement

def test_sADL_ReadStatement___init__():
    assert sADL_ReadStatement.__init__(sADL_ReadStatement('', '\x00'), '\x00\x00', '') == None


from python_code import sADL_SadlBooleanLiteral

def test_sADL_SadlBooleanLiteral___init__():
    assert sADL_SadlBooleanLiteral.__init__(sADL_SadlBooleanLiteral(True), False) == None


from python_code import sADL_SadlConstantLiteral

def test_sADL_SadlConstantLiteral___init__():
    assert sADL_SadlConstantLiteral.__init__(sADL_SadlConstantLiteral(''), '') == None


from python_code import sADL_SadlDefaultValue
from python_code import sADL_SadlExplicitValue

def test_sADL_SadlDefaultValue___init__():
    assert sADL_SadlDefaultValue.__init__(sADL_SadlDefaultValue(0, sADL_SadlDefaultValue=sADL_SadlExplicitValue()), 0, sADL_SadlDefaultValue=sADL_SadlExplicitValue()) == None


from python_code import sADL_SadlDifferentFrom
from python_code import sADL_SadlResource
from python_code import sADL_SadlTypeReference

def test_sADL_SadlDifferentFrom___init__():
    assert sADL_SadlDifferentFrom.__init__(sADL_SadlDifferentFrom(False, sADL_SadlDifferentFrom=sADL_SadlResource(), sADL_SadlDifferentFrom123=sADL_SadlTypeReference(), sADL_SadlDifferentFrom126=set()), False, sADL_SadlDifferentFrom=sADL_SadlResource(), sADL_SadlDifferentFrom123=sADL_SadlTypeReference(), sADL_SadlDifferentFrom126=set()) == None


from python_code import sADL_SadlIsFunctional

def test_sADL_SadlIsFunctional___init__():
    assert sADL_SadlIsFunctional.__init__(sADL_SadlIsFunctional(True), False) == None


from python_code import sADL_SadlNestedInstance

def test_sADL_SadlNestedInstance___init__():
    assert sADL_SadlNestedInstance.__init__(sADL_SadlNestedInstance(''), '') == None


from python_code import sADL_SadlNumberLiteral

def test_sADL_SadlNumberLiteral___init__():
    assert sADL_SadlNumberLiteral.__init__(sADL_SadlNumberLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import sADL_SadlPrimitiveDataType

def test_sADL_SadlPrimitiveDataType___init__():
    assert sADL_SadlPrimitiveDataType.__init__(sADL_SadlPrimitiveDataType('', False), '', False) == None


from python_code import sADL_SadlClassOrPropertyDeclaration
from python_code import sADL_SadlProperty
from python_code import sADL_SadlResource
from python_code import sADL_SadlTypeReference

def test_sADL_SadlProperty___init__():
    assert sADL_SadlProperty.__init__(sADL_SadlProperty(False, sADL_SadlProperty=sADL_SadlResource(), sADL_SadlProperty53=set(), sADL_SadlProperty55=sADL_SadlTypeReference(), sADL_SadlProperty58=sADL_SadlTypeReference(), sADL_SadlProperty61=sADL_SadlResource(), sADL_SadlProperty64=set(), sADL_SadlProperty111=sADL_SadlClassOrPropertyDeclaration()), False, sADL_SadlProperty=sADL_SadlResource(), sADL_SadlProperty53=set(), sADL_SadlProperty55=sADL_SadlTypeReference(), sADL_SadlProperty58=sADL_SadlTypeReference(), sADL_SadlProperty61=sADL_SadlResource(), sADL_SadlProperty64=set(), sADL_SadlProperty111=sADL_SadlClassOrPropertyDeclaration()) == None


from python_code import sADL_SadlResource
from python_code import sADL_SadlSameAs
from python_code import sADL_SadlTypeReference

def test_sADL_SadlSameAs___init__():
    assert sADL_SadlSameAs.__init__(sADL_SadlSameAs(True, sADL_SadlSameAs=sADL_SadlResource(), sADL_SadlSameAs118=sADL_SadlTypeReference()), False, sADL_SadlSameAs=sADL_SadlResource(), sADL_SadlSameAs118=sADL_SadlTypeReference()) == None


from python_code import sADL_SadlResource
from python_code import sADL_SadlSimpleTypeReference

def test_sADL_SadlSimpleTypeReference___init__():
    assert sADL_SadlSimpleTypeReference.__init__(sADL_SadlSimpleTypeReference(True, sADL_SadlSimpleTypeReference=sADL_SadlResource()), False, sADL_SadlSimpleTypeReference=sADL_SadlResource()) == None


from python_code import sADL_SadlStringLiteral

def test_sADL_SadlStringLiteral___init__():
    assert sADL_SadlStringLiteral.__init__(sADL_SadlStringLiteral(''), '') == None


from python_code import sADL_SadlExplicitValueLiteral
from python_code import sADL_SadlUnaryExpression

def test_sADL_SadlUnaryExpression___init__():
    assert sADL_SadlUnaryExpression.__init__(sADL_SadlUnaryExpression('', sADL_SadlUnaryExpression=sADL_SadlExplicitValueLiteral()), '', sADL_SadlUnaryExpression=sADL_SadlExplicitValueLiteral()) == None


from python_code import sADL_Expression
from python_code import sADL_SelectExpression

def test_sADL_SelectExpression___init__():
    assert sADL_SelectExpression.__init__(sADL_SelectExpression('', False, sADL_SelectExpression211=set(), sADL_SelectExpression=set(), sADL_SelectExpression208=sADL_Expression()), '', True, sADL_SelectExpression211=set(), sADL_SelectExpression=set(), sADL_SelectExpression208=sADL_Expression()) == None


from python_code import sADL_StartWriteStatement

def test_sADL_StartWriteStatement___init__():
    assert sADL_StartWriteStatement.__init__(sADL_StartWriteStatement('', '\x00'), '\x00\x00', '') == None


from python_code import sADL_StringLiteral

def test_sADL_StringLiteral___init__():
    assert sADL_StringLiteral.__init__(sADL_StringLiteral(''), '') == None


from python_code import sADL_Expression
from python_code import sADL_SadlResource
from python_code import sADL_SubjHasProp

def test_sADL_SubjHasProp___init__():
    assert sADL_SubjHasProp.__init__(sADL_SubjHasProp(True, sADL_SubjHasProp=sADL_Expression(), sADL_SubjHasProp231=sADL_SadlResource(), sADL_SubjHasProp234=sADL_Expression()), False, sADL_SubjHasProp=sADL_Expression(), sADL_SubjHasProp231=sADL_SadlResource(), sADL_SubjHasProp234=sADL_Expression()) == None


from python_code import sADL_Expression
from python_code import sADL_UnaryExpression

def test_sADL_UnaryExpression___init__():
    assert sADL_UnaryExpression.__init__(sADL_UnaryExpression('', sADL_UnaryExpression=sADL_Expression()), '', sADL_UnaryExpression=sADL_Expression()) == None


from python_code import sADL_Expression
from python_code import sADL_UnitExpression

def test_sADL_UnitExpression___init__():
    assert sADL_UnitExpression.__init__(sADL_UnitExpression('', sADL_UnitExpression=sADL_Expression()), '', sADL_UnitExpression=sADL_Expression()) == None

