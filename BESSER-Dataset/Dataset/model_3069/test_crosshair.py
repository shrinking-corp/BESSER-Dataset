from python_code import dom_AliasedExpression
from python_code import dom_Expression

def test_dom_AliasedExpression___init__():
    assert dom_AliasedExpression.__init__(dom_AliasedExpression('', dom_AliasedExpression=dom_Expression()), '', dom_AliasedExpression=dom_Expression()) == None


from python_code import dom_BetweenExpression
from python_code import dom_Expression

def test_dom_BetweenExpression___init__():
    assert dom_BetweenExpression.__init__(dom_BetweenExpression(False, '\x00', dom_BetweenExpression343=dom_Expression(), dom_BetweenExpression346=dom_Expression(), dom_BetweenExpression=dom_Expression()), False, '\x00', dom_BetweenExpression343=dom_Expression(), dom_BetweenExpression346=dom_Expression(), dom_BetweenExpression=dom_Expression()) == None


from python_code import dom_BinaryExpression
from python_code import dom_Expression

def test_dom_BinaryExpression___init__():
    assert dom_BinaryExpression.__init__(dom_BinaryExpression('', dom_BinaryExpression=dom_Expression(), dom_BinaryExpression331=dom_Expression()), '', dom_BinaryExpression=dom_Expression(), dom_BinaryExpression331=dom_Expression()) == None


from python_code import dom_BooleanLiteralValue

def test_dom_BooleanLiteralValue___init__():
    assert dom_BooleanLiteralValue.__init__(dom_BooleanLiteralValue(True), False) == None


from python_code import dom_CallableStatement

def test_dom_CallableStatement___init__():
    assert dom_CallableStatement.__init__(dom_CallableStatement(False, '', dom_CallableStatement=set(), dom_CallableStatement208=set()), False, '', dom_CallableStatement=set(), dom_CallableStatement208=set()) == None


from python_code import dom_CastFunction
from python_code import dom_Expression

def test_dom_CastFunction___init__():
    assert dom_CastFunction.__init__(dom_CastFunction('', '\x00', dom_CastFunction=dom_Expression()), '\x00\x00', '', dom_CastFunction=dom_Expression()) == None


from python_code import dom_DeleteStatement
from python_code import dom_Entity
from python_code import dom_Expression

def test_dom_DeleteStatement___init__():
    assert dom_DeleteStatement.__init__(dom_DeleteStatement('', dom_DeleteStatement=dom_Entity(), dom_DeleteStatement231=dom_Expression()), '', dom_DeleteStatement=dom_Entity(), dom_DeleteStatement231=dom_Expression()) == None


from python_code import dom_Entity
from python_code import dom_FromClass

def test_dom_FromClass___init__():
    assert dom_FromClass.__init__(dom_FromClass(True, dom_FromClass=dom_Entity()), False, dom_FromClass=dom_Entity()) == None


from python_code import dom_FunctionCall

def test_dom_FunctionCall___init__():
    assert dom_FunctionCall.__init__(dom_FunctionCall('', dom_FunctionCall=set()), '', dom_FunctionCall=set()) == None


from python_code import dom_IElementWithNoName

def test_dom_IElementWithNoName___init__():
    assert dom_IElementWithNoName.__init__(dom_IElementWithNoName(''), '') == None


from python_code import dom_InClass

def test_dom_InClass___init__():
    assert dom_InClass.__init__(dom_InClass('', '\x00'), '\x00\x00', '') == None


from python_code import dom_InCollection

def test_dom_InCollection___init__():
    assert dom_InCollection.__init__(dom_InCollection('', '\x00'), '\x00\x00', '') == None


from python_code import dom_InCollectionElements

def test_dom_InCollectionElements___init__():
    assert dom_InCollectionElements.__init__(dom_InCollectionElements('', '\x00'), '\x00\x00', '') == None


from python_code import dom_Expression
from python_code import dom_InExpression

def test_dom_InExpression___init__():
    assert dom_InExpression.__init__(dom_InExpression(False, '\x00', dom_InExpression=dom_Expression(), dom_InExpression338=dom_Expression()), False, '\x00', dom_InExpression=dom_Expression(), dom_InExpression338=dom_Expression()) == None


from python_code import dom_IntegerLiteralValue

def test_dom_IntegerLiteralValue___init__():
    assert dom_IntegerLiteralValue.__init__(dom_IntegerLiteralValue(''), '') == None


from python_code import dom_Expression
from python_code import dom_LikeExpression

def test_dom_LikeExpression___init__():
    assert dom_LikeExpression.__init__(dom_LikeExpression(False, '\x00', dom_LikeExpression=dom_Expression(), dom_LikeExpression351=dom_Expression(), dom_LikeExpression354=dom_Expression()), False, '\x00', dom_LikeExpression=dom_Expression(), dom_LikeExpression351=dom_Expression(), dom_LikeExpression354=dom_Expression()) == None


from python_code import dom_ComplexType
from python_code import dom_Mapper

def test_dom_Mapper___init__():
    assert dom_Mapper.__init__(dom_Mapper(False, False, False, dom_Mapper=dom_ComplexType(), dom_Mapper52=dom_ComplexType(), dom_Mapper55=set()), False, False, True, dom_Mapper=dom_ComplexType(), dom_Mapper52=dom_ComplexType(), dom_Mapper55=set()) == None


from python_code import dom_Expression
from python_code import dom_MemberOfExpression

def test_dom_MemberOfExpression___init__():
    assert dom_MemberOfExpression.__init__(dom_MemberOfExpression(False, '', '\x00\x00', dom_MemberOfExpression=dom_Expression()), False, '', '', dom_MemberOfExpression=dom_Expression()) == None


from python_code import dom_PresentableFeature

def test_dom_PresentableFeature___init__():
    assert dom_PresentableFeature.__init__(dom_PresentableFeature(''), '') == None


from python_code import dom_ApplicationSession
from python_code import dom_Property
from python_code import dom_SimpleType

def test_dom_Property___init__():
    assert dom_Property.__init__(dom_Property('', '\x00', dom_Property=dom_SimpleType(), dom_Property200=dom_ApplicationSession()), '\x00\x00', '', dom_Property=dom_SimpleType(), dom_Property200=dom_ApplicationSession()) == None


from python_code import dom_Expression
from python_code import dom_QuantifiedExpression

def test_dom_QuantifiedExpression___init__():
    assert dom_QuantifiedExpression.__init__(dom_QuantifiedExpression('', '\x00', dom_QuantifiedExpression=dom_Expression()), '\x00\x00', '', dom_QuantifiedExpression=dom_Expression()) == None


from python_code import dom_RealLiteralValue

def test_dom_RealLiteralValue___init__():
    assert dom_RealLiteralValue.__init__(dom_RealLiteralValue(''), '') == None


from python_code import dom_SelectClass

def test_dom_SelectClass___init__():
    assert dom_SelectClass.__init__(dom_SelectClass('', dom_SelectClass=set()), '', dom_SelectClass=set()) == None


from python_code import dom_SelectObject

def test_dom_SelectObject___init__():
    assert dom_SelectObject.__init__(dom_SelectObject(''), '') == None


from python_code import dom_SelectProperties

def test_dom_SelectProperties___init__():
    assert dom_SelectProperties.__init__(dom_SelectProperties(False, dom_SelectProperties=set()), False, dom_SelectProperties=set()) == None


from python_code import dom_Expression
from python_code import dom_SelectStatement
from python_code import dom_SortOrderElement

def test_dom_SortOrderElement___init__():
    assert dom_SortOrderElement.__init__(dom_SortOrderElement('', dom_SortOrderElement=dom_SelectStatement(), dom_SortOrderElement261=dom_Expression()), '', dom_SortOrderElement=dom_SelectStatement(), dom_SortOrderElement261=dom_Expression()) == None


from python_code import dom_Expression
from python_code import dom_UnaryExpression

def test_dom_UnaryExpression___init__():
    assert dom_UnaryExpression.__init__(dom_UnaryExpression('', dom_UnaryExpression=dom_Expression()), '', dom_UnaryExpression=dom_Expression()) == None


from python_code import dom_Entity
from python_code import dom_Expression
from python_code import dom_UpdateStatement

def test_dom_UpdateStatement___init__():
    assert dom_UpdateStatement.__init__(dom_UpdateStatement(False, '\x00', dom_UpdateStatement=dom_Entity(), dom_UpdateStatement236=set(), dom_UpdateStatement238=dom_Expression()), False, '', dom_UpdateStatement=dom_Entity(), dom_UpdateStatement236=set(), dom_UpdateStatement238=dom_Expression()) == None

