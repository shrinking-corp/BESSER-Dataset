from python_code import metric_AggregatedIntegerMetric

def test_metric_AggregatedIntegerMetric___init__():
    assert metric_AggregatedIntegerMetric.__init__(metric_AggregatedIntegerMetric('', 0.0, 0.0, '', ''), '', 0.0, 0.0, '', '') == None


from python_code import metric_AggregatedRealMetric

def test_metric_AggregatedRealMetric___init__():
    assert metric_AggregatedRealMetric.__init__(metric_AggregatedRealMetric(0.0, 0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0, 0.0) == None


from python_code import metric_Container

def test_metric_Container___init__():
    assert metric_Container.__init__(metric_Container('', metric_Container=set()), '', metric_Container=set()) == None


from python_code import metric_SimpleMetric

def test_metric_SimpleMetric___init__():
    assert metric_SimpleMetric.__init__(metric_SimpleMetric(''), '') == None

