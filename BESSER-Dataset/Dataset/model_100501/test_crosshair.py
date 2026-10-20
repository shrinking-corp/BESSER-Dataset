from python_code import core_Assumption
from python_code import core_Requirement

def test_core_Assumption___init__():
    assert core_Assumption.__init__(core_Assumption('', Assumption=core_Requirement(), Assumption96=core_Requirement(), assumptions=core_Requirement(), imageAssumption=core_Requirement()), '', Assumption=core_Requirement(), Assumption96=core_Requirement(), assumptions=core_Requirement(), imageAssumption=core_Requirement()) == None


from python_code import core_IdentifiedElement

def test_core_IdentifiedElement___init__():
    assert core_IdentifiedElement.__init__(core_IdentifiedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import core_RequirementsCoverageData

def test_core_RequirementsCoverageData___init__():
    assert core_RequirementsCoverageData.__init__(core_RequirementsCoverageData(0, '\x00'), 0, '\x00') == None


from python_code import core_TraceModelElementReference

def test_core_TraceModelElementReference___init__():
    assert core_TraceModelElementReference.__init__(core_TraceModelElementReference(True), False) == None

def test_core_TraceModelElementReference_merge():
    assert core_TraceModelElementReference.merge(core_TraceModelElementReference(False), 0) == None


from python_code import core_VerifiableElement

def test_core_VerifiableElement___init__():
    assert core_VerifiableElement.__init__(core_VerifiableElement(''), '') == None

