from python_code import DOM_ArrayCreation
from python_code import DOM_ArrayType
from python_code import DOM_Type

def test_DOM_ArrayType___init__():
    assert DOM_ArrayType.__init__(DOM_ArrayType('', DOM_ArrayType=DOM_ArrayCreation(), DOM_ArrayType346=DOM_Type(), DOM_ArrayType349=DOM_Type()), '', DOM_ArrayType=DOM_ArrayCreation(), DOM_ArrayType346=DOM_Type(), DOM_ArrayType349=DOM_Type()) == None


from python_code import DOM_BooleanLiteral

def test_DOM_BooleanLiteral___init__():
    assert DOM_BooleanLiteral.__init__(DOM_BooleanLiteral(''), '') == None


from python_code import DOM_CharacterLiteral

def test_DOM_CharacterLiteral___init__():
    assert DOM_CharacterLiteral.__init__(DOM_CharacterLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import DOM_Modifier

def test_DOM_Modifier___init__():
    assert DOM_Modifier.__init__(DOM_Modifier('', '', '', '', '', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import DOM_NumberLiteral

def test_DOM_NumberLiteral___init__():
    assert DOM_NumberLiteral.__init__(DOM_NumberLiteral(''), '') == None


from python_code import DOM_PrimitiveType

def test_DOM_PrimitiveType___init__():
    assert DOM_PrimitiveType.__init__(DOM_PrimitiveType(''), '') == None


from python_code import DOM_StringLiteral

def test_DOM_StringLiteral___init__():
    assert DOM_StringLiteral.__init__(DOM_StringLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import DOM_Javadoc
from python_code import DOM_TagElement

def test_DOM_TagElement___init__():
    assert DOM_TagElement.__init__(DOM_TagElement('\x00\x00', '', DOM_TagElement=set(), DOM_TagElement127=DOM_Javadoc()), '', '', DOM_TagElement=set(), DOM_TagElement127=DOM_Javadoc()) == None


from python_code import DOM_TextElement

def test_DOM_TextElement___init__():
    assert DOM_TextElement.__init__(DOM_TextElement(''), '') == None


from python_code import DOM_Type
from python_code import DOM_TypeDeclaration

def test_DOM_TypeDeclaration___init__():
    assert DOM_TypeDeclaration.__init__(DOM_TypeDeclaration('', DOM_TypeDeclaration=DOM_Type(), DOM_TypeDeclaration120=set(), DOM_TypeDeclaration123=set()), '', DOM_TypeDeclaration=DOM_Type(), DOM_TypeDeclaration120=set(), DOM_TypeDeclaration123=set()) == None


from python_code import DOM_Type
from python_code import DOM_WildcardType

def test_DOM_WildcardType___init__():
    assert DOM_WildcardType.__init__(DOM_WildcardType('', DOM_WildcardType=DOM_Type()), '', DOM_WildcardType=DOM_Type()) == None

