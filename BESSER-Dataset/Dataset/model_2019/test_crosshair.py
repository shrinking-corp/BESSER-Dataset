from python_code import executionTrace_AttributeValueSet

def test_executionTrace_AttributeValueSet___init__():
    assert executionTrace_AttributeValueSet.__init__(executionTrace_AttributeValueSet('', '\x00'), '\x00\x00', '') == None

from python_code import executionTrace_ExecutionTrace

def test_executionTrace_ExecutionTrace___init__():
    assert executionTrace_ExecutionTrace.__init__(executionTrace_ExecutionTrace('', '', '', executionTrace_ExecutionTrace=set()), '', '', '', executionTrace_ExecutionTrace=set()) == None

from python_code import executionTrace_ExpressionEvaluation

def test_executionTrace_ExpressionEvaluation___init__():
    assert executionTrace_ExpressionEvaluation.__init__(executionTrace_ExpressionEvaluation(''), '') == None

from python_code import executionTrace_InstanceLinkModification

def test_executionTrace_InstanceLinkModification___init__():
    assert executionTrace_InstanceLinkModification.__init__(executionTrace_InstanceLinkModification('', '\x00'), '\x00\x00', '') == None

from python_code import executionTrace_InstanceObjectModification

def test_executionTrace_InstanceObjectModification___init__():
    assert executionTrace_InstanceObjectModification.__init__(executionTrace_InstanceObjectModification(''), '') == None

from python_code import executionTrace_LinkCheck

def test_executionTrace_LinkCheck___init__():
    assert executionTrace_LinkCheck.__init__(executionTrace_LinkCheck(''), '') == None

from python_code import executionTrace_MapEntry

def test_executionTrace_MapEntry___init__():
    assert executionTrace_MapEntry.__init__(executionTrace_MapEntry('', '\x00'), '\x00\x00', '') == None

from python_code import executionTrace_StoryPatternLinkExecution

def test_executionTrace_StoryPatternLinkExecution___init__():
    assert executionTrace_StoryPatternLinkExecution.__init__(executionTrace_StoryPatternLinkExecution(''), '') == None

from python_code import executionTrace_StoryPatternMatching

def test_executionTrace_StoryPatternMatching___init__():
    assert executionTrace_StoryPatternMatching.__init__(executionTrace_StoryPatternMatching(True), False) == None

from python_code import executionTrace_StoryPatternObjectBindingRevoked

def test_executionTrace_StoryPatternObjectBindingRevoked___init__():
    assert executionTrace_StoryPatternObjectBindingRevoked.__init__(executionTrace_StoryPatternObjectBindingRevoked(''), '') == None

from python_code import executionTrace_StoryPatternObjectBound

def test_executionTrace_StoryPatternObjectBound___init__():
    assert executionTrace_StoryPatternObjectBound.__init__(executionTrace_StoryPatternObjectBound(''), '') == None

from python_code import executionTrace_VariableChanged

def test_executionTrace_VariableChanged___init__():
    assert executionTrace_VariableChanged.__init__(executionTrace_VariableChanged(''), '') == None

from python_code import executionTrace_VariableModification

def test_executionTrace_VariableModification___init__():
    assert executionTrace_VariableModification.__init__(executionTrace_VariableModification('', '\x00'), '\x00\x00', '') == None
