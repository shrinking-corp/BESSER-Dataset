from python_code import QualityMetrics_Metric

def test_QualityMetrics_Metric___init__():
    assert QualityMetrics_Metric.__init__(QualityMetrics_Metric(''), '') == None


from python_code import QualityMetrics_Metrics

def test_QualityMetrics_Metrics___init__():
    assert QualityMetrics_Metrics.__init__(QualityMetrics_Metrics('', QualityMetrics_Metrics=set(), QualityMetrics_Metrics2=set(), QualityMetrics_Metrics4=set()), '', QualityMetrics_Metrics=set(), QualityMetrics_Metrics2=set(), QualityMetrics_Metrics4=set()) == None

