from python_code import assessment_Account
from python_code import assessment_Accounts
from python_code import assessment_Entitlement

def test_assessment_Account___init__():
    assert assessment_Account.__init__(assessment_Account('\x00\x00', '', accounts=assessment_Accounts(), accounts47=set(), Account=assessment_Entitlement(), Account77=assessment_Accounts()), '', '', accounts=assessment_Accounts(), accounts47=set(), Account=assessment_Entitlement(), Account77=assessment_Accounts()) == None


from python_code import assessment_Contents

def test_assessment_Contents___init__():
    assert assessment_Contents.__init__(assessment_Contents(''), '') == None


from python_code import assessment_Finding
from python_code import assessment_Findings
from python_code import assessment_Node

def test_assessment_Finding___init__():
    assert assessment_Finding.__init__(assessment_Finding('', '', '', Finding=assessment_Node(), findings=assessment_Findings(), findings43=set(), Finding68=assessment_Findings()), '', '', '', Finding=assessment_Node(), findings=assessment_Findings(), findings43=set(), Finding68=assessment_Findings()) == None


from python_code import assessment_Http

def test_assessment_Http___init__():
    assert assessment_Http.__init__(assessment_Http('', '\x00'), '\x00\x00', '') == None


from python_code import assessment_Label

def test_assessment_Label___init__():
    assert assessment_Label.__init__(assessment_Label(''), '') == None


from python_code import assessment_Notes

def test_assessment_Notes___init__():
    assert assessment_Notes.__init__(assessment_Notes(''), '') == None


from python_code import assessment_Sink
from python_code import assessment_Sinks

def test_assessment_Sink___init__():
    assert assessment_Sink.__init__(assessment_Sink(0, sinks=assessment_Sinks(), Sink=assessment_Sinks()), 0, sinks=assessment_Sinks(), Sink=assessment_Sinks()) == None


from python_code import assessment_Resource
from python_code import assessment_Snippet

def test_assessment_Snippet___init__():
    assert assessment_Snippet.__init__(assessment_Snippet(0, 0, 0, 0, Snippet=assessment_Resource(), snippets=assessment_Resource()), 0, 0, 0, 0, Snippet=assessment_Resource(), snippets=assessment_Resource()) == None


from python_code import assessment_Node
from python_code import assessment_Task
from python_code import assessment_Tasks

def test_assessment_Task___init__():
    assert assessment_Task.__init__(assessment_Task('', Task=assessment_Node(), tasks=assessment_Tasks(), tasks54=set(), Task115=assessment_Tasks()), '', Task=assessment_Node(), tasks=assessment_Tasks(), tasks54=set(), Task115=assessment_Tasks()) == None


from python_code import assessment_Url

def test_assessment_Url___init__():
    assert assessment_Url.__init__(assessment_Url('', '\x00'), '\x00\x00', '') == None

