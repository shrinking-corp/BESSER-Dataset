from python_code import Metrics_BooleanMetricValue
from python_code import Metrics_Metric

def test_Metrics_BooleanMetricValue___init__():
    assert Metrics_BooleanMetricValue.__init__(Metrics_BooleanMetricValue('\x00\x00', MetricValue=Metrics_Metric('', Metrics_Metric=set())), '', MetricValue=Metrics_Metric('', Metrics_Metric=set())) == None


from python_code import Metrics_DoubleMetricValue
from python_code import Metrics_Metric

def test_Metrics_DoubleMetricValue___init__():
    assert Metrics_DoubleMetricValue.__init__(Metrics_DoubleMetricValue('\x00\x00', MetricValue=Metrics_Metric('', Metrics_Metric=set())), '', MetricValue=Metrics_Metric('', Metrics_Metric=set())) == None


from python_code import Metrics_IntegerMetricValue
from python_code import Metrics_Metric

def test_Metrics_IntegerMetricValue___init__():
    assert Metrics_IntegerMetricValue.__init__(Metrics_IntegerMetricValue('\x00\x00', MetricValue=Metrics_Metric('', Metrics_Metric=set())), '', MetricValue=Metrics_Metric('', Metrics_Metric=set())) == None


from python_code import Metrics_Metric

def test_Metrics_Metric___init__():
    assert Metrics_Metric.__init__(Metrics_Metric('\x00', Metrics_Metric=set()), '', Metrics_Metric=set()) == None


from python_code import Metrics_MetricValue

def test_Metrics_MetricValue___init__():
    assert Metrics_MetricValue.__init__(Metrics_MetricValue(''), '') == None


from python_code import Metrics_Metric
from python_code import Metrics_StringMetricValue

def test_Metrics_StringMetricValue___init__():
    assert Metrics_StringMetricValue.__init__(Metrics_StringMetricValue('\x00\x00', MetricValue=Metrics_Metric('', Metrics_Metric=set())), '', MetricValue=Metrics_Metric('', Metrics_Metric=set())) == None

