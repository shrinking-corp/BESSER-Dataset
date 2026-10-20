from python_code import metric_AggregatedIntegerMetric

def test_metric_AggregatedIntegerMetric___init__():
    assert metric_AggregatedIntegerMetric.__init__(metric_AggregatedIntegerMetric('', '', '', 0.0, 0.0), '', '', '\x00', 0.0, 0.0) == None


from python_code import metric_AggregatedRealMetric

def test_metric_AggregatedRealMetric___init__():
    assert metric_AggregatedRealMetric.__init__(metric_AggregatedRealMetric(0.0, 0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0, 0.0) == None


from python_code import metric_Container
from python_code import metric_Metric

def test_metric_Metric___init__():
    assert metric_Metric.__init__(metric_Metric('', '', '\x00\x00', metric_Metric=metric_Container()), '', '', '', metric_Metric=metric_Container()) == None


from python_code import metric_SimpleMetric

def test_metric_SimpleMetric___init__():
    assert metric_SimpleMetric.__init__(metric_SimpleMetric(''), '') == None

