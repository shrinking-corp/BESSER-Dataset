from python_code import safetyDSL_ArchElementToArchElement
from python_code import safetyDSL_ArchitecturalElement
from python_code import safetyDSL_ModuleClassRelation
from python_code import safetyDSL_SafetyCriticalViewpoint

def test_safetyDSL_ArchitecturalElement___init__():
    assert safetyDSL_ArchitecturalElement.__init__(safetyDSL_ArchitecturalElement('', safetyDSL_ArchitecturalElement=safetyDSL_SafetyCriticalViewpoint(), safetyDSL_ArchitecturalElement68=safetyDSL_ModuleClassRelation(), safetyDSL_ArchitecturalElement48=safetyDSL_ArchElementToArchElement(), safetyDSL_ArchitecturalElement51=safetyDSL_ArchElementToArchElement()), '', safetyDSL_ArchitecturalElement=safetyDSL_SafetyCriticalViewpoint(), safetyDSL_ArchitecturalElement68=safetyDSL_ModuleClassRelation(), safetyDSL_ArchitecturalElement48=safetyDSL_ArchElementToArchElement(), safetyDSL_ArchitecturalElement51=safetyDSL_ArchElementToArchElement()) == None


from python_code import safetyDSL_HazardElement
from python_code import safetyDSL_HazardViewpoint

def test_safetyDSL_HazardElement___init__():
    assert safetyDSL_HazardElement.__init__(safetyDSL_HazardElement('', safetyDSL_HazardElement=safetyDSL_HazardViewpoint()), '', safetyDSL_HazardElement=safetyDSL_HazardViewpoint()) == None


from python_code import safetyDSL_Monitor
from python_code import safetyDSL_SafetyCritical
from python_code import safetyDSL_SafetyTactic
from python_code import safetyDSL_SafetyTacticViewpoint

def test_safetyDSL_SafetyTactic___init__():
    assert safetyDSL_SafetyTactic.__init__(safetyDSL_SafetyTactic('\x00\x00', '', safetyDSL_SafetyTactic37=safetyDSL_SafetyCritical(), safetyDSL_SafetyTactic46=safetyDSL_Monitor(), safetyDSL_SafetyTactic=safetyDSL_SafetyTacticViewpoint(), safetyDSL_SafetyTactic26=set()), '', '', safetyDSL_SafetyTactic37=safetyDSL_SafetyCritical(), safetyDSL_SafetyTactic46=safetyDSL_Monitor(), safetyDSL_SafetyTactic=safetyDSL_SafetyTacticViewpoint(), safetyDSL_SafetyTactic26=set()) == None


from python_code import safetyDSL_SafetyFramework
from python_code import safetyDSL_SafetyViewpoint

def test_safetyDSL_SafetyViewpoint___init__():
    assert safetyDSL_SafetyViewpoint.__init__(safetyDSL_SafetyViewpoint('', safetyDSL_SafetyViewpoint=safetyDSL_SafetyFramework()), '', safetyDSL_SafetyViewpoint=safetyDSL_SafetyFramework()) == None


from python_code import safetyDSL_SafetyCritical
from python_code import safetyDSL_State

def test_safetyDSL_State___init__():
    assert safetyDSL_State.__init__(safetyDSL_State('', safetyDSL_State=safetyDSL_SafetyCritical()), '', safetyDSL_State=safetyDSL_SafetyCritical()) == None

