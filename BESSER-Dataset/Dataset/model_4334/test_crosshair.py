from python_code import qm_AnnotatedElement
from python_code import qm_Annotation

def test_qm_Annotation___init__():
    assert qm_Annotation.__init__(qm_Annotation('', '\x00', qm_Annotation=qm_AnnotatedElement()), '\x00\x00', '', qm_Annotation=qm_AnnotatedElement()) == None


from python_code import qm_DescribedElement

def test_qm_DescribedElement___init__():
    assert qm_DescribedElement.__init__(qm_DescribedElement(''), '') == None


from python_code import qm_FindingsMeasurementResult

def test_qm_FindingsMeasurementResult___init__():
    assert qm_FindingsMeasurementResult.__init__(qm_FindingsMeasurementResult(0, '\x00', qm_FindingsMeasurementResult=set()), 0, '', qm_FindingsMeasurementResult=set()) == None


from python_code import qm_Factor
from python_code import qm_Impact

def test_qm_Impact___init__():
    assert qm_Impact.__init__(qm_Impact('', '\x00', influences=qm_Factor(), Impact=qm_Factor(), qm_Impact=qm_Factor()), '\x00\x00', '', influences=qm_Factor(), Impact=qm_Factor(), qm_Impact=qm_Factor()) == None


from python_code import qm_LinearFunction

def test_qm_LinearFunction___init__():
    assert qm_LinearFunction.__init__(qm_LinearFunction(0.0, 0.0), 0.0, 0.0) == None


from python_code import qm_NamedElement

def test_qm_NamedElement___init__():
    assert qm_NamedElement.__init__(qm_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import qm_QualityModelElement

def test_qm_QualityModelElement___init__():
    assert qm_QualityModelElement.__init__(qm_QualityModelElement('', qm_QualityModelElement=set()), '', qm_QualityModelElement=set()) == None


import datetime as _ch_datetime
from python_code import qm_QualityModelResult

def test_qm_QualityModelResult___init__():
    assert qm_QualityModelResult.__init__(qm_QualityModelResult('', _ch_datetime.date(1, 1, 1), qm_QualityModelResult=set(), qm_QualityModelResult108=set()), '', _ch_datetime.date(1, 1, 1), qm_QualityModelResult=set(), qm_QualityModelResult108=set()) == None


from python_code import qm_Ranking

def test_qm_Ranking___init__():
    assert qm_Ranking.__init__(qm_Ranking(0, 0.0), 0, 0.0) == None


from python_code import qm_Result

def test_qm_Result___init__():
    assert qm_Result.__init__(qm_Result(''), '') == None


from python_code import qm_SingleMeasureEvaluationResult

def test_qm_SingleMeasureEvaluationResult___init__():
    assert qm_SingleMeasureEvaluationResult.__init__(qm_SingleMeasureEvaluationResult(0.0), 0.0) == None


from python_code import qm_TextAggregation

def test_qm_TextAggregation___init__():
    assert qm_TextAggregation.__init__(qm_TextAggregation(''), '') == None


from python_code import qm_TextEvaluation

def test_qm_TextEvaluation___init__():
    assert qm_TextEvaluation.__init__(qm_TextEvaluation(''), '') == None


from python_code import qm_Tool
from python_code import qm_ToolBasedInstrument

def test_qm_ToolBasedInstrument___init__():
    assert qm_ToolBasedInstrument.__init__(qm_ToolBasedInstrument('', qm_ToolBasedInstrument=qm_Tool()), '', qm_ToolBasedInstrument=qm_Tool()) == None

