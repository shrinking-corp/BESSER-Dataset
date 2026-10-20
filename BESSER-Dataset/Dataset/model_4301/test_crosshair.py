from python_code import metrics_IdentifierDataKind

def test_metrics_IdentifierDataKind___init__():
    assert metrics_IdentifierDataKind.__init__(metrics_IdentifierDataKind('', '', '\x00\x00'), '', '', '') == None


from python_code import metrics_MappingCSV

def test_metrics_MappingCSV___init__():
    assert metrics_MappingCSV.__init__(metrics_MappingCSV('', '\x00'), '\x00\x00', '') == None


from python_code import metrics_MappingRDBMS

def test_metrics_MappingRDBMS___init__():
    assert metrics_MappingRDBMS.__init__(metrics_MappingRDBMS('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import metrics_MappingXLS

def test_metrics_MappingXLS___init__():
    assert metrics_MappingXLS.__init__(metrics_MappingXLS('', '\x00'), '\x00\x00', '') == None


from python_code import metrics_Expression
from python_code import metrics_MetricRetentionRule
from python_code import metrics_MetricRetentionRules

def test_metrics_MetricRetentionRule___init__():
    assert metrics_MetricRetentionRule.__init__(metrics_MetricRetentionRule('', '', '\x00\x00', metrics_MetricRetentionRule=metrics_Expression(), metrics_MetricRetentionRule26=metrics_MetricRetentionRules()), '', '', '', metrics_MetricRetentionRule=metrics_Expression(), metrics_MetricRetentionRule26=metrics_MetricRetentionRules()) == None


from python_code import metrics_MetricValueRange

def test_metrics_MetricValueRange___init__():
    assert metrics_MetricValueRange.__init__(metrics_MetricValueRange('\x00\x00', '', metrics_MetricValueRange=set()), '', '', metrics_MetricValueRange=set()) == None

