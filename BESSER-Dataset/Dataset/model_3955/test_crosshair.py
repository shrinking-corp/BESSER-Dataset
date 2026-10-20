from python_code import SecCon_Comment
from python_code import SecCon_Element

def test_SecCon_Comment___init__():
    assert SecCon_Comment.__init__(SecCon_Comment('', SecCon_Comment=SecCon_Element(), SecCon_Comment3=set()), '', SecCon_Comment=SecCon_Element(), SecCon_Comment3=set()) == None


from python_code import SecCon_ContextScenario
from python_code import SecCon_Project

def test_SecCon_ContextScenario___init__():
    assert SecCon_ContextScenario.__init__(SecCon_ContextScenario('', SecCon_ContextScenario=SecCon_Project(), SecCon_ContextScenario93=set(), SecCon_ContextScenario95=set()), '', SecCon_ContextScenario=SecCon_Project(), SecCon_ContextScenario93=set(), SecCon_ContextScenario95=set()) == None


from python_code import SecCon_MultiplicityElement

def test_SecCon_MultiplicityElement___init__():
    assert SecCon_MultiplicityElement.__init__(SecCon_MultiplicityElement(False, False, 0, ''), False, False, 0, '') == None


from python_code import SecCon_NamedElement

def test_SecCon_NamedElement___init__():
    assert SecCon_NamedElement.__init__(SecCon_NamedElement(''), '') == None


from python_code import SecCon_Project
from python_code import SecCon_StateMachineScenario

def test_SecCon_StateMachineScenario___init__():
    assert SecCon_StateMachineScenario.__init__(SecCon_StateMachineScenario('', '', SecCon_StateMachineScenario89=SecCon_Project(), SecCon_StateMachineScenario=set(), SecCon_StateMachineScenario66=set(), SecCon_StateMachineScenario68=set()), '', '', SecCon_StateMachineScenario89=SecCon_Project(), SecCon_StateMachineScenario=set(), SecCon_StateMachineScenario66=set(), SecCon_StateMachineScenario68=set()) == None

