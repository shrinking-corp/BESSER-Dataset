from python_code import QualityMetamodel_AggregatedValueMetric

def test_QualityMetamodel_AggregatedValueMetric___init__():
    assert QualityMetamodel_AggregatedValueMetric.__init__(QualityMetamodel_AggregatedValueMetric('', '', '', '', ''), '', '', '', '', '') == None


from python_code import QualityMetamodel_BooleanValueType

def test_QualityMetamodel_BooleanValueType___init__():
    assert QualityMetamodel_BooleanValueType.__init__(QualityMetamodel_BooleanValueType(''), '') == None


from python_code import QualityMetamodel_EnumerationItem
from python_code import QualityMetamodel_EnumerationMetric

def test_QualityMetamodel_EnumerationItem___init__():
    assert QualityMetamodel_EnumerationItem.__init__(QualityMetamodel_EnumerationItem('', QualityMetamodel_EnumerationItem=QualityMetamodel_EnumerationMetric(), QualityMetamodel_EnumerationItem24=QualityMetamodel_EnumerationMetric()), '', QualityMetamodel_EnumerationItem=QualityMetamodel_EnumerationMetric(), QualityMetamodel_EnumerationItem24=QualityMetamodel_EnumerationMetric()) == None


from python_code import QualityMetamodel_IntegerValueType

def test_QualityMetamodel_IntegerValueType___init__():
    assert QualityMetamodel_IntegerValueType.__init__(QualityMetamodel_IntegerValueType(''), '') == None


from python_code import QualityMetamodel_AggregatedValue
from python_code import QualityMetamodel_Operation

def test_QualityMetamodel_Operation___init__():
    assert QualityMetamodel_Operation.__init__(QualityMetamodel_Operation('\x00\x00', '', QualityMetamodel_Operation=QualityMetamodel_AggregatedValue(), QualityMetamodel_Operation19=set()), '', '', QualityMetamodel_Operation=QualityMetamodel_AggregatedValue(), QualityMetamodel_Operation19=set()) == None


from python_code import QualityMetamodel_RangeValueType

def test_QualityMetamodel_RangeValueType___init__():
    assert QualityMetamodel_RangeValueType.__init__(QualityMetamodel_RangeValueType('', '\x00'), '\x00\x00', '') == None


from python_code import QualityMetamodel_RealValueType

def test_QualityMetamodel_RealValueType___init__():
    assert QualityMetamodel_RealValueType.__init__(QualityMetamodel_RealValueType(''), '') == None


from python_code import QualityMetamodel_TextValueType

def test_QualityMetamodel_TextValueType___init__():
    assert QualityMetamodel_TextValueType.__init__(QualityMetamodel_TextValueType(''), '') == None

