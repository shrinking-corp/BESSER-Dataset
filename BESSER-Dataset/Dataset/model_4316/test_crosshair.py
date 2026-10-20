from python_code import metrics_Addon
from python_code import metrics_Metric
from python_code import metrics_MetricAggregationRules
from python_code import metrics_MetricRetentionRules

def test_metrics_Metric___init__():
    assert metrics_Metric.__init__(metrics_Metric('', metrics_Metric=metrics_Addon(), metrics_Metric8=metrics_MetricAggregationRules(), metrics_Metric11=metrics_MetricRetentionRules()), '', metrics_Metric=metrics_Addon(), metrics_Metric8=metrics_MetricAggregationRules(), metrics_Metric11=metrics_MetricRetentionRules()) == None


from python_code import metrics_EObject
from python_code import metrics_MetricAggregationRule
from python_code import metrics_MetricAggregationRules

def test_metrics_MetricAggregationRule___init__():
    assert metrics_MetricAggregationRule.__init__(metrics_MetricAggregationRule('', '\x00', metrics_MetricAggregationRule16=metrics_MetricAggregationRules(), metrics_MetricAggregationRule=metrics_EObject()), '\x00\x00', '', metrics_MetricAggregationRule16=metrics_MetricAggregationRules(), metrics_MetricAggregationRule=metrics_EObject()) == None


from python_code import metrics_MetricRetentionPeriods

def test_metrics_MetricRetentionPeriods___init__():
    assert metrics_MetricRetentionPeriods.__init__(metrics_MetricRetentionPeriods(''), '') == None


from python_code import metrics_MetricRetentionRule
from python_code import metrics_MetricRetentionRules

def test_metrics_MetricRetentionRule___init__():
    assert metrics_MetricRetentionRule.__init__(metrics_MetricRetentionRule('', '\x00', metrics_MetricRetentionRule=metrics_MetricRetentionRules()), '\x00\x00', '', metrics_MetricRetentionRule=metrics_MetricRetentionRules()) == None


from python_code import metrics_Addon
from python_code import metrics_MetricAggregationRules
from python_code import metrics_MetricRetentionRules
from python_code import metrics_MetricSource

def test_metrics_MetricSource___init__():
    assert metrics_MetricSource.__init__(metrics_MetricSource('', metrics_MetricSource23=metrics_MetricRetentionRules(), metrics_MetricSource=metrics_Addon(), metrics_MetricSource20=metrics_MetricAggregationRules()), '', metrics_MetricSource23=metrics_MetricRetentionRules(), metrics_MetricSource=metrics_Addon(), metrics_MetricSource20=metrics_MetricAggregationRules()) == None

