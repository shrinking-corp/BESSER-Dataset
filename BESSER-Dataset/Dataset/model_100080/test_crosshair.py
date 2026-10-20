from python_code import builds_BooleanParameterDefinition

def test_builds_BooleanParameterDefinition___init__():
    assert builds_BooleanParameterDefinition.__init__(builds_BooleanParameterDefinition(True), False) == None


import datetime as _ch_datetime
from python_code import builds_BuildElement

def test_builds_BuildElement___init__():
    assert builds_BuildElement.__init__(builds_BuildElement('', '', '', '', _ch_datetime.date(1, 1, 1), builds_BuildElement=set()), '', '', '', '', _ch_datetime.date(1, 1, 1), builds_BuildElement=set()) == None

def test_builds_BuildElement_getServer():
    assert builds_BuildElement.getServer(builds_BuildElement('', '', '\x00\x00', '', _ch_datetime.date(1, 1, 1), builds_BuildElement=set())) == None

def test_builds_BuildElement_getLabel():
    assert builds_BuildElement.getLabel(builds_BuildElement('', '', '\x00\x00', '', _ch_datetime.date(1, 1, 1), builds_BuildElement=set())) == None


from python_code import builds_ChoiceParameterDefinition

def test_builds_ChoiceParameterDefinition___init__():
    assert builds_ChoiceParameterDefinition.__init__(builds_ChoiceParameterDefinition('', '\x00'), '\x00\x00', '') == None


from python_code import builds_PasswordParameterDefinition

def test_builds_PasswordParameterDefinition___init__():
    assert builds_PasswordParameterDefinition.__init__(builds_PasswordParameterDefinition(''), '') == None


from python_code import builds_StringParameterDefinition

def test_builds_StringParameterDefinition___init__():
    assert builds_StringParameterDefinition.__init__(builds_StringParameterDefinition(''), '') == None


from python_code import builds_TestCase
from python_code import builds_TestSuite

def test_builds_TestCase___init__():
    assert builds_TestCase.__init__(builds_TestCase('', False, '', '', '', TestCase=builds_TestSuite(), cases=builds_TestSuite()), '', False, '', '', '', TestCase=builds_TestSuite(), cases=builds_TestSuite()) == None


from python_code import builds_TestElement

def test_builds_TestElement___init__():
    assert builds_TestElement.__init__(builds_TestElement('\x00\x00', '', '', ''), '', '', '', '') == None

