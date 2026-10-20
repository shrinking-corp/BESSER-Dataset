from python_code import smm_DimensionalMeasure
from python_code import smm_UnitOfMeasure

def test_smm_DimensionalMeasure___init__():
    assert smm_DimensionalMeasure.__init__(smm_DimensionalMeasure('', smm_DimensionalMeasure27=set(), smm_DimensionalMeasure30=set(), smm_DimensionalMeasure=set(), smm_DimensionalMeasure33=set(), smm_DimensionalMeasure35=set(), smm_DimensionalMeasure37=set(), smm_DimensionalMeasure39=smm_UnitOfMeasure()), '', smm_DimensionalMeasure27=set(), smm_DimensionalMeasure30=set(), smm_DimensionalMeasure=set(), smm_DimensionalMeasure33=set(), smm_DimensionalMeasure35=set(), smm_DimensionalMeasure37=set(), smm_DimensionalMeasure39=smm_UnitOfMeasure()) == None


from python_code import smm_DimensionalMeasurement

def test_smm_DimensionalMeasurement___init__():
    assert smm_DimensionalMeasurement.__init__(smm_DimensionalMeasurement(0.0, smm_DimensionalMeasurement=set(), smm_DimensionalMeasurement43=set(), smm_DimensionalMeasurement46=set(), smm_DimensionalMeasurement49=set(), smm_DimensionalMeasurement51=set(), smm_DimensionalMeasurement53=set()), 0.0, smm_DimensionalMeasurement=set(), smm_DimensionalMeasurement43=set(), smm_DimensionalMeasurement46=set(), smm_DimensionalMeasurement49=set(), smm_DimensionalMeasurement51=set(), smm_DimensionalMeasurement53=set()) == None


from python_code import smm_GradeInterval
from python_code import smm_GradeMeasure

def test_smm_GradeInterval___init__():
    assert smm_GradeInterval.__init__(smm_GradeInterval('', smm_GradeInterval=smm_GradeMeasure()), '', smm_GradeInterval=smm_GradeMeasure()) == None


from python_code import smm_Interval

def test_smm_Interval___init__():
    assert smm_Interval.__init__(smm_Interval(0.0, '', 0.0, ''), 0.0, '', 0.0, '') == None


from python_code import smm_OCLOperation

def test_smm_OCLOperation___init__():
    assert smm_OCLOperation.__init__(smm_OCLOperation('', '\x00'), '\x00\x00', '') == None


from python_code import smm_Observation
from python_code import smm_SmmModel

def test_smm_Observation___init__():
    assert smm_Observation.__init__(smm_Observation('\x00', '', '', smm_Observation=set(), smm_Observation127=set(), smm_Observation129=set(), smm_Observation131=set(), smm_Observation176=smm_SmmModel()), '', '', '', smm_Observation=set(), smm_Observation127=set(), smm_Observation129=set(), smm_Observation131=set(), smm_Observation176=smm_SmmModel()) == None


from python_code import smm_RankingInterval
from python_code import smm_RankingMeasure

def test_smm_RankingInterval___init__():
    assert smm_RankingInterval.__init__(smm_RankingInterval(0.0, interval=smm_RankingMeasure(), RankingInterval=smm_RankingMeasure()), 0.0, interval=smm_RankingMeasure(), RankingInterval=smm_RankingMeasure()) == None


from python_code import smm_SmmElement
from python_code import smm_SmmRelationship

def test_smm_SmmElement___init__():
    assert smm_SmmElement.__init__(smm_SmmElement('\x00', '', '', SmmElement=smm_SmmRelationship(), SmmElement179=smm_SmmRelationship(), smm_SmmElement=set(), smm_SmmElement168=set(), to=set(), from_=set()), '', '', '', SmmElement=smm_SmmRelationship(), SmmElement179=smm_SmmRelationship(), smm_SmmElement=set(), smm_SmmElement168=set(), to=set(), from_=set()) == None

