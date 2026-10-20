from python_code import smm_AggregatedMeasurement

def test_smm_AggregatedMeasurement___init__():
    assert smm_AggregatedMeasurement.__init__(smm_AggregatedMeasurement(False, smm_AggregatedMeasurement=set()), False, smm_AggregatedMeasurement=set()) == None


from python_code import smm_CollectiveMeasurement

def test_smm_CollectiveMeasurement___init__():
    assert smm_CollectiveMeasurement.__init__(smm_CollectiveMeasurement('\x00\x00', False, smm_CollectiveMeasurement=set()), '', True, smm_CollectiveMeasurement=set()) == None


from python_code import smm_DirectMeasure

def test_smm_DirectMeasure___init__():
    assert smm_DirectMeasure.__init__(smm_DirectMeasure(''), '') == None


from python_code import smm_Ranking
from python_code import smm_RankingInterval

def test_smm_RankingInterval___init__():
    assert smm_RankingInterval.__init__(smm_RankingInterval(0.0, False, 0.0, False, '', RankingInterval=smm_Ranking(), interval=smm_Ranking()), 0.0, False, 0.0, True, '', RankingInterval=smm_Ranking(), interval=smm_Ranking()) == None


from python_code import smm_ReScaledMeasurement

def test_smm_ReScaledMeasurement___init__():
    assert smm_ReScaledMeasurement.__init__(smm_ReScaledMeasurement(True), False) == None


from python_code import smm_RescaledMeasure

def test_smm_RescaledMeasure___init__():
    assert smm_RescaledMeasure.__init__(smm_RescaledMeasure(''), '') == None


from python_code import smm_SmmRelationship

def test_smm_SmmRelationship___init__():
    assert smm_SmmRelationship.__init__(smm_SmmRelationship()) == None

def test_smm_SmmRelationship_getFrom():
    assert smm_SmmRelationship.getFrom(smm_SmmRelationship()) == None

def test_smm_SmmRelationship_getTo():
    assert smm_SmmRelationship.getTo(smm_SmmRelationship()) == None

