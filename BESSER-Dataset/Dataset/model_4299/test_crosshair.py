from python_code import metrics_IdentifierDataKind

def test_metrics_IdentifierDataKind___init__():
    assert metrics_IdentifierDataKind.__init__(metrics_IdentifierDataKind('', '\x00'), '\x00\x00', '') == None


from python_code import metrics_MappingRecordXLS

def test_metrics_MappingRecordXLS___init__():
    assert metrics_MappingRecordXLS.__init__(metrics_MappingRecordXLS('', '\x00'), '\x00\x00', '') == None


from python_code import metrics_MappingXLS

def test_metrics_MappingXLS___init__():
    assert metrics_MappingXLS.__init__(metrics_MappingXLS('', '', '', metrics_MappingXLS=set()), '', '', '', metrics_MappingXLS=set()) == None


from python_code import metrics_MetricValueRange

def test_metrics_MetricValueRange___init__():
    assert metrics_MetricValueRange.__init__(metrics_MetricValueRange('\x00\x00', '', metrics_MetricValueRange=set()), '', '', metrics_MetricValueRange=set()) == None

