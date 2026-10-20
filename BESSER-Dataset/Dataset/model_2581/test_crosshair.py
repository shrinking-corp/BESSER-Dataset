from python_code import esper_Attributes
from python_code import esper_AttributesDefinition

def test_esper_AttributesDefinition___init__():
    assert esper_AttributesDefinition.__init__(esper_AttributesDefinition('', '\x00', esper_AttributesDefinition=esper_Attributes()), '\x00\x00', '', esper_AttributesDefinition=esper_Attributes()) == None


from python_code import esper_JoinFollowBy
from python_code import esper_Pattern

def test_esper_JoinFollowBy___init__():
    assert esper_JoinFollowBy.__init__(esper_JoinFollowBy('', esper_JoinFollowBy46=set(), esper_JoinFollowBy=esper_Pattern()), '', esper_JoinFollowBy46=set(), esper_JoinFollowBy=esper_Pattern()) == None


from python_code import esper_Name
from python_code import esper_RuleParts

def test_esper_Name___init__():
    assert esper_Name.__init__(esper_Name('', esper_Name=esper_RuleParts()), '', esper_Name=esper_RuleParts()) == None


from python_code import esper_Priority
from python_code import esper_RuleParts

def test_esper_Priority___init__():
    assert esper_Priority.__init__(esper_Priority(0, esper_Priority=esper_RuleParts()), 0, esper_Priority=esper_RuleParts()) == None


from python_code import esper_RuleParts
from python_code import esper_Select

def test_esper_Select___init__():
    assert esper_Select.__init__(esper_Select('', True, esper_Select=esper_RuleParts(), esper_Select22=set()), '', False, esper_Select=esper_RuleParts(), esper_Select22=set()) == None

