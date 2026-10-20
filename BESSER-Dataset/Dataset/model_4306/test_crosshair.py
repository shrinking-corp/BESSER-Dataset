from python_code import metrics_MetricSource

def test_metrics_MetricSource___init__():
    assert metrics_MetricSource.__init__(metrics_MetricSource('', '', '', '', '', metrics_MetricSource=set()), '', '', '', '\x00', '', metrics_MetricSource=set()) == None

