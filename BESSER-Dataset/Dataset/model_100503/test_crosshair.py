from python_code import rdal_IdentifiedElement

def test_rdal_IdentifiedElement___init__():
    assert rdal_IdentifiedElement.__init__(rdal_IdentifiedElement('', '', '', rdal_IdentifiedElement=set()), '', '', '', rdal_IdentifiedElement=set()) == None


from python_code import rdal_PrioritizedSatDesignElementRef

def test_rdal_PrioritizedSatDesignElementRef___init__():
    assert rdal_PrioritizedSatDesignElementRef.__init__(rdal_PrioritizedSatDesignElementRef('', '\x00'), '\x00\x00', '') == None


from python_code import rdal_NonFunctionalProperty
from python_code import rdal_QualityObjective
from python_code import rdal_Sensitivity

def test_rdal_QualityObjective___init__():
    assert rdal_QualityObjective.__init__(rdal_QualityObjective('\x00', 0.0, rdal_QualityObjective=rdal_NonFunctionalProperty(), rdal_QualityObjective138=rdal_Sensitivity()), '', 0.0, rdal_QualityObjective=rdal_NonFunctionalProperty(), rdal_QualityObjective138=rdal_Sensitivity()) == None


from python_code import rdal_RequirementsCoverageData

def test_rdal_RequirementsCoverageData___init__():
    assert rdal_RequirementsCoverageData.__init__(rdal_RequirementsCoverageData(0, '\x00'), 0, '\x00') == None


from python_code import rdal_SatisfiableElement

def test_rdal_SatisfiableElement___init__():
    assert rdal_SatisfiableElement.__init__(rdal_SatisfiableElement(''), '') == None


from python_code import rdal_TraceDesignElementRef

def test_rdal_TraceDesignElementRef___init__():
    assert rdal_TraceDesignElementRef.__init__(rdal_TraceDesignElementRef(True), False) == None

def test_rdal_TraceDesignElementRef_merge():
    assert rdal_TraceDesignElementRef.merge(rdal_TraceDesignElementRef(False), 0) == None


from python_code import rdal_VerifiableElement

def test_rdal_VerifiableElement___init__():
    assert rdal_VerifiableElement.__init__(rdal_VerifiableElement(''), '') == None

