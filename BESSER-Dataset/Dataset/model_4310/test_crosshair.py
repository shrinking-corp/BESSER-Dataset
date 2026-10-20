from python_code import metricDSL_Constant

def test_metricDSL_Constant___init__():
    assert metricDSL_Constant.__init__(metricDSL_Constant(0.0), 0.0) == None


from python_code import metricDSL_InternalMetric
from python_code import metricDSL_MetricDefinition

def test_metricDSL_InternalMetric___init__():
    assert metricDSL_InternalMetric.__init__(metricDSL_InternalMetric('\x00\x00', '', metricDSL_InternalMetric=set(), metricDSL_InternalMetric3=metricDSL_MetricDefinition()), '', '', metricDSL_InternalMetric=set(), metricDSL_InternalMetric3=metricDSL_MetricDefinition()) == None


from python_code import metricDSL_MetricModel

def test_metricDSL_MetricModel___init__():
    assert metricDSL_MetricModel.__init__(metricDSL_MetricModel('\x00', metricDSL_MetricModel=set()), '', metricDSL_MetricModel=set()) == None


from python_code import metricDSL_Parameter

def test_metricDSL_Parameter___init__():
    assert metricDSL_Parameter.__init__(metricDSL_Parameter('', '', 0.0), '', '', 0.0) == None

