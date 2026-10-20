from python_code import dmx_DmxArchetype

def test_dmx_DmxArchetype___init__():
    assert dmx_DmxArchetype.__init__(dmx_DmxArchetype(''), '') == None


from python_code import dmx_DExpression
from python_code import dmx_DmxBinaryOperation

def test_dmx_DmxBinaryOperation___init__():
    assert dmx_DmxBinaryOperation.__init__(dmx_DmxBinaryOperation('', dmx_DmxBinaryOperation=dmx_DExpression(), dmx_DmxBinaryOperation51=dmx_DExpression()), '', dmx_DmxBinaryOperation=dmx_DExpression(), dmx_DmxBinaryOperation51=dmx_DExpression()) == None


from python_code import dmx_DmxBooleanLiteral

def test_dmx_DmxBooleanLiteral___init__():
    assert dmx_DmxBooleanLiteral.__init__(dmx_DmxBooleanLiteral(True), False) == None


from python_code import dmx_DNamedElement
from python_code import dmx_DmxContextReference

def test_dmx_DmxContextReference___init__():
    assert dmx_DmxContextReference.__init__(dmx_DmxContextReference(False, False, dmx_DmxContextReference=dmx_DNamedElement()), False, False, dmx_DmxContextReference=dmx_DNamedElement()) == None


import datetime as _ch_datetime
from python_code import dmx_DmxDateLiteral

def test_dmx_DmxDateLiteral___init__():
    assert dmx_DmxDateLiteral.__init__(dmx_DmxDateLiteral(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import dmx_DmxDecimalLiteral

def test_dmx_DmxDecimalLiteral___init__():
    assert dmx_DmxDecimalLiteral.__init__(dmx_DmxDecimalLiteral(''), '') == None


from python_code import dmx_DExpression
from python_code import dmx_DNavigableMember
from python_code import dmx_DmxCallArguments
from python_code import dmx_DmxMemberNavigation

def test_dmx_DmxMemberNavigation___init__():
    assert dmx_DmxMemberNavigation.__init__(dmx_DmxMemberNavigation(False, False, dmx_DmxMemberNavigation=dmx_DNavigableMember(), dmx_DmxMemberNavigation36=dmx_DExpression(), dmx_DmxMemberNavigation39=dmx_DmxCallArguments()), False, False, dmx_DmxMemberNavigation=dmx_DNavigableMember(), dmx_DmxMemberNavigation36=dmx_DExpression(), dmx_DmxMemberNavigation39=dmx_DmxCallArguments()) == None


from python_code import dmx_DmxNaturalLiteral

def test_dmx_DmxNaturalLiteral___init__():
    assert dmx_DmxNaturalLiteral.__init__(dmx_DmxNaturalLiteral(0), 0) == None


from python_code import dmx_DNavigableMember
from python_code import dmx_DmxStaticReference
from python_code import dmx_IStaticReferenceTarget

def test_dmx_DmxStaticReference___init__():
    assert dmx_DmxStaticReference.__init__(dmx_DmxStaticReference('', False, dmx_DmxStaticReference=dmx_IStaticReferenceTarget(), dmx_DmxStaticReference68=dmx_DNavigableMember()), '', False, dmx_DmxStaticReference=dmx_IStaticReferenceTarget(), dmx_DmxStaticReference68=dmx_DNavigableMember()) == None


from python_code import dmx_DmxStringLiteral

def test_dmx_DmxStringLiteral___init__():
    assert dmx_DmxStringLiteral.__init__(dmx_DmxStringLiteral(''), '') == None


from python_code import dmx_DExpression
from python_code import dmx_DmxModel
from python_code import dmx_DmxTest

def test_dmx_DmxTest___init__():
    assert dmx_DmxTest.__init__(dmx_DmxTest('', dmx_DmxTest=dmx_DmxModel(), dmx_DmxTest4=set(), dmx_DmxTest6=dmx_DExpression()), '', dmx_DmxTest=dmx_DmxModel(), dmx_DmxTest4=set(), dmx_DmxTest6=dmx_DExpression()) == None


from python_code import dmx_DExpression
from python_code import dmx_DmxUnaryOperation

def test_dmx_DmxUnaryOperation___init__():
    assert dmx_DmxUnaryOperation.__init__(dmx_DmxUnaryOperation('', dmx_DmxUnaryOperation=dmx_DExpression()), '', dmx_DmxUnaryOperation=dmx_DExpression()) == None


from python_code import dmx_DmxUrlLiteral

def test_dmx_DmxUrlLiteral___init__():
    assert dmx_DmxUrlLiteral.__init__(dmx_DmxUrlLiteral('', '\x00'), '\x00\x00', '') == None

