from python_code import QualityMetamodel_AggregatedValueMetric

def test_QualityMetamodel_AggregatedValueMetric___init__():
    assert QualityMetamodel_AggregatedValueMetric.__init__(QualityMetamodel_AggregatedValueMetric('', '', '', '', ''), '', '', '', '', '') == None


from python_code import QualityMetamodel_BooleanValueType

def test_QualityMetamodel_BooleanValueType___init__():
    assert QualityMetamodel_BooleanValueType.__init__(QualityMetamodel_BooleanValueType(''), '') == None


from python_code import QualityMetamodel_EnumerationItem
from python_code import QualityMetamodel_EnumerationMetric

def test_QualityMetamodel_EnumerationItem___init__():
    assert QualityMetamodel_EnumerationItem.__init__(QualityMetamodel_EnumerationItem('', QualityMetamodel_EnumerationItem=QualityMetamodel_EnumerationMetric(), QualityMetamodel_EnumerationItem26=QualityMetamodel_EnumerationMetric()), '', QualityMetamodel_EnumerationItem=QualityMetamodel_EnumerationMetric(), QualityMetamodel_EnumerationItem26=QualityMetamodel_EnumerationMetric()) == None


from python_code import QualityMetamodel_IntegerValueType

def test_QualityMetamodel_IntegerValueType___init__():
    assert QualityMetamodel_IntegerValueType.__init__(QualityMetamodel_IntegerValueType(''), '') == None


from python_code import QualityMetamodel_MetricProvider
from python_code import QualityMetamodel_QualityModel
from python_code import QualityMetamodel_SingleValue

def test_QualityMetamodel_MetricProvider___init__():
    assert QualityMetamodel_MetricProvider.__init__(QualityMetamodel_MetricProvider('', '', '\x00\x00', QualityMetamodel_MetricProvider=QualityMetamodel_QualityModel(), QualityMetamodel_MetricProvider16=QualityMetamodel_SingleValue()), '', '', '', QualityMetamodel_MetricProvider=QualityMetamodel_QualityModel(), QualityMetamodel_MetricProvider16=QualityMetamodel_SingleValue()) == None


from python_code import QualityMetamodel_QMM_OCL_BooleanExp

def test_QualityMetamodel_QMM_OCL_BooleanExp___init__():
    assert QualityMetamodel_QMM_OCL_BooleanExp.__init__(QualityMetamodel_QMM_OCL_BooleanExp(''), '') == None


from python_code import QualityMetamodel_QMM_OCL_IntegerExp

def test_QualityMetamodel_QMM_OCL_IntegerExp___init__():
    assert QualityMetamodel_QMM_OCL_IntegerExp.__init__(QualityMetamodel_QMM_OCL_IntegerExp(''), '') == None


from python_code import QualityMetamodel_QMM_OCL_Iterator
from python_code import QualityMetamodel_QMM_OCL_IteratorExp
from python_code import QualityMetamodel_QMM_OCL_OclExpression

def test_QualityMetamodel_QMM_OCL_IteratorExp___init__():
    assert QualityMetamodel_QMM_OCL_IteratorExp.__init__(QualityMetamodel_QMM_OCL_IteratorExp('', LoopExp119=QualityMetamodel_QMM_OCL_Iterator(), LoopExp=QualityMetamodel_QMM_OCL_OclExpression()), '', LoopExp119=QualityMetamodel_QMM_OCL_Iterator(), LoopExp=QualityMetamodel_QMM_OCL_OclExpression()) == None


from python_code import QualityMetamodel_QMM_OCL_LocatedElement

def test_QualityMetamodel_QMM_OCL_LocatedElement___init__():
    assert QualityMetamodel_QMM_OCL_LocatedElement.__init__(QualityMetamodel_QMM_OCL_LocatedElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import QualityMetamodel_QMM_OCL_NamedElement

def test_QualityMetamodel_QMM_OCL_NamedElement___init__():
    assert QualityMetamodel_QMM_OCL_NamedElement.__init__(QualityMetamodel_QMM_OCL_NamedElement(''), '') == None


from python_code import QualityMetamodel_QMM_OCL_NavigationOrAttributeCall
from python_code import QualityMetamodel_QMM_OCL_PropertyCallExp

def test_QualityMetamodel_QMM_OCL_NavigationOrAttributeCall___init__():
    assert QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.__init__(QualityMetamodel_QMM_OCL_NavigationOrAttributeCall('', PropertyCall=QualityMetamodel_QMM_OCL_PropertyCallExp()), '', PropertyCall=QualityMetamodel_QMM_OCL_PropertyCallExp()) == None


from python_code import OclFeatureDefinition
from python_code import QualityMetamodel_QMM_OCL_OclFeature

def test_QualityMetamodel_QMM_OCL_OclFeature___init__():
    assert QualityMetamodel_QMM_OCL_OclFeature.__init__(QualityMetamodel_QMM_OCL_OclFeature('', feature=OclFeatureDefinition()), '', feature=OclFeatureDefinition()) == None


from python_code import OclContextDefinition
from python_code import OclFeature
from python_code import QualityMetamodel_QMM_OCL_Module
from python_code import QualityMetamodel_QMM_OCL_OclFeatureDefinition

def test_QualityMetamodel_QMM_OCL_OclFeatureDefinition___init__():
    assert QualityMetamodel_QMM_OCL_OclFeatureDefinition.__init__(QualityMetamodel_QMM_OCL_OclFeatureDefinition('', definition=OclFeature(), definition168=OclContextDefinition(), ModuleElement=QualityMetamodel_QMM_OCL_Module()), '\x00', definition=OclFeature(), definition168=OclContextDefinition(), ModuleElement=QualityMetamodel_QMM_OCL_Module()) == None


from python_code import QualityMetamodel_QMM_OCL_OperationCall
from python_code import QualityMetamodel_QMM_OCL_PropertyCallExp

def test_QualityMetamodel_QMM_OCL_OperationCall___init__():
    assert QualityMetamodel_QMM_OCL_OperationCall.__init__(QualityMetamodel_QMM_OCL_OperationCall('', parentOperation=set(), PropertyCall=QualityMetamodel_QMM_OCL_PropertyCallExp()), '\x00', parentOperation=set(), PropertyCall=QualityMetamodel_QMM_OCL_PropertyCallExp()) == None


from python_code import QualityMetamodel_QMM_OCL_RealExp

def test_QualityMetamodel_QMM_OCL_RealExp___init__():
    assert QualityMetamodel_QMM_OCL_RealExp.__init__(QualityMetamodel_QMM_OCL_RealExp(''), '') == None


from python_code import QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall
from python_code import QualityMetamodel_QMM_OCL_StaticPropertyCallExp

def test_QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall___init__():
    assert QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall.__init__(QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall('', StaticPropertyCall=QualityMetamodel_QMM_OCL_StaticPropertyCallExp()), '', StaticPropertyCall=QualityMetamodel_QMM_OCL_StaticPropertyCallExp()) == None


from python_code import QualityMetamodel_QMM_OCL_StaticOperationCall
from python_code import QualityMetamodel_QMM_OCL_StaticPropertyCallExp

def test_QualityMetamodel_QMM_OCL_StaticOperationCall___init__():
    assert QualityMetamodel_QMM_OCL_StaticOperationCall.__init__(QualityMetamodel_QMM_OCL_StaticOperationCall('', QualityMetamodel_QMM_OCL_StaticOperationCall=set(), StaticPropertyCall=QualityMetamodel_QMM_OCL_StaticPropertyCallExp()), '\x00', QualityMetamodel_QMM_OCL_StaticOperationCall=set(), StaticPropertyCall=QualityMetamodel_QMM_OCL_StaticPropertyCallExp()) == None


from python_code import QualityMetamodel_QMM_OCL_StringExp

def test_QualityMetamodel_QMM_OCL_StringExp___init__():
    assert QualityMetamodel_QMM_OCL_StringExp.__init__(QualityMetamodel_QMM_OCL_StringExp(''), '') == None


from python_code import OclType
from python_code import QualityMetamodel_QMM_OCL_TupleTypeAttribute
from python_code import TupleType

def test_QualityMetamodel_QMM_OCL_TupleTypeAttribute___init__():
    assert QualityMetamodel_QMM_OCL_TupleTypeAttribute.__init__(QualityMetamodel_QMM_OCL_TupleTypeAttribute('', tupleTypeAttribute=OclType(), attributes=TupleType()), '', tupleTypeAttribute=OclType(), attributes=TupleType()) == None


from python_code import OclType
from python_code import QualityMetamodel_QMM_OCL_VariableDeclaration

def test_QualityMetamodel_QMM_OCL_VariableDeclaration___init__():
    assert QualityMetamodel_QMM_OCL_VariableDeclaration.__init__(QualityMetamodel_QMM_OCL_VariableDeclaration('', referredVariable=set(), variableDeclaration=OclType()), '', referredVariable=set(), variableDeclaration=OclType()) == None


from python_code import QualityMetamodel_RangeValueType

def test_QualityMetamodel_RangeValueType___init__():
    assert QualityMetamodel_RangeValueType.__init__(QualityMetamodel_RangeValueType('', '\x00'), '\x00\x00', '') == None


from python_code import QualityMetamodel_RealValueType

def test_QualityMetamodel_RealValueType___init__():
    assert QualityMetamodel_RealValueType.__init__(QualityMetamodel_RealValueType(''), '') == None


from python_code import QualityMetamodel_TextValueType

def test_QualityMetamodel_TextValueType___init__():
    assert QualityMetamodel_TextValueType.__init__(QualityMetamodel_TextValueType(''), '') == None

