from python_code import metric_Metric

def test_metric_Metric___init__():
    assert metric_Metric.__init__(metric_Metric()) == None

def test_metric_Metric_getReport():
    assert metric_Metric.getReport(metric_Metric()) == None

