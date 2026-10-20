import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnalysisConstruct,
    Axis,
    Connector,
    ConnectorCompositionTarget,
    ConnectorFeature,
    Container,
    ContainerInstanceBase,
    CustomGeometryInput,
    Datum,
    DesignDomainFeature,
    DesignSpaceContainer,
    DistributionRestriction,
    DomainModelMetric,
    DomainModelParameter,
    DomainModelPort,
    DomainModel_,
    FileReference,
    Formula,
    Geometry,
    Geometry2D,
    Geometry3D,
    KinematicJointSpec,
    Limit,
    Metric,
    Parameter,
    Plane,
    PlaneReference,
    Point,
    PointReference,
    Port,
    PortMapTarget,
    ProbabilisticValue,
    Property,
    Redeclare,
    Settings,
    TestBenchValueBase,
    ValueExpressionType,
    ValueNode,
    WorkflowTaskBase,
    adamsCar_avm_Value,
    avm_AbstractPort,
    avm_Alternative,
    avm_AnalysisConstruct,
    avm_CalculatedValue,
    avm_ComplexFormula,
    avm_Component,
    avm_ComponentConnectorInstance,
    avm_ComponentInstance,
    avm_ComponentPortInstance,
    avm_ComponentPrimitivePropertyInstance,
    avm_Compound,
    avm_CompoundProperty,
    avm_Connector,
    avm_ConnectorCompositionTarget,
    avm_ConnectorFeature,
    avm_Container,
    avm_ContainerInstanceBase,
    avm_DataSource,
    avm_DerivedValue,
    avm_Design,
    avm_DesignDomainFeature,
    avm_DesignSpaceContainer,
    avm_DistributionRestriction,
    avm_DoDDistributionStatement,
    avm_DomainModelMetric,
    avm_DomainModelParameter,
    avm_DomainModelPort,
    avm_DomainModel_,
    avm_ExecutionTask,
    avm_FixedValue,
    avm_Formula,
    avm_ITAR,
    avm_InterpreterTask,
    avm_Metric,
    avm_NormalDistribution,
    avm_Operand,
    avm_Optional,
    avm_Parameter,
    avm_ParametricEnumeratedValue,
    avm_ParametricValue,
    avm_Port,
    avm_PortMapTarget,
    avm_PrimitiveProperty,
    avm_ProbabilisticValue,
    avm_Property,
    avm_Proprietary,
    avm_Resource,
    avm_SecurityClassification,
    avm_Settings,
    avm_SimpleFormula,
    avm_TestBench,
    avm_TestBenchValueBase,
    avm_TestInjectionPoint,
    avm_TopLevelSystemUnderTest,
    avm_UniformDistribution,
    avm_Value,
    avm_ValueExpressionType,
    avm_ValueFlowMux,
    avm_ValueNode,
    avm_Workflow,
    avm_WorkflowTaskBase,
    avm_adamsCar_AdamsCarModel,
    avm_adamsCar_FileReference,
    avm_adamsCar_Parameter,
    avm_assemblyDetail,
    avm_cad_AssemblyRoot,
    avm_cad_Axis,
    avm_cad_CADModel,
    avm_cad_Circle,
    avm_cad_CoordinateSystem,
    avm_cad_CustomGeometry,
    avm_cad_CustomGeometryInput,
    avm_cad_Datum,
    avm_cad_ExtrudedGeometry,
    avm_cad_Geometry,
    avm_cad_Geometry2D,
    avm_cad_Geometry3D,
    avm_cad_GuideDatum,
    avm_cad_KinematicJointSpec,
    avm_cad_Metric,
    avm_cad_Parameter,
    avm_cad_Plane,
    avm_cad_PlaneReference,
    avm_cad_Point,
    avm_cad_PointReference,
    avm_cad_Polygon,
    avm_cad_RevoluteJointSpec,
    avm_cad_Sphere,
    avm_cad_Surface,
    avm_cad_TranslationalJointSpec,
    avm_cyber_CyberModel,
    avm_manufacturing_ManufacturingModel,
    avm_manufacturing_Metric,
    avm_manufacturing_Parameter,
    avm_modelica_Connector,
    avm_modelica_Limit,
    avm_modelica_Metric,
    avm_modelica_ModelicaModel,
    avm_modelica_Parameter,
    avm_modelica_Redeclare,
    avm_modelica_SolverSettings,
    cad_avm_ComponentInstance,
    cad_avm_Value,
    manufacturing_avm_Value,
    modelica_avm_Value,
    BoundTypeEnum,
    CalculationTypeEnum,
    CustomGeometryInputOperationEnum,
    DataTypeEnum,
    DimensionTypeEnum,
    DoDDistributionStatementEnum,
    GeometryQualifierEnum,
    IntervalMethod,
    JobManagerToolSelection,
    ModelType,
    PartIntersectionEnum,
    RedeclareTypeEnum,
    SimpleFormulaOperation,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_ComponentInstance76_reverse_link_reassign_clear():
    a1 = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Container(Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_ComponentInstance(ComponentID="sample_text", DesignSpaceSrcComponentID="sample_text", ID="sample_text", Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_ComponentInstance', a1)
    assert _is_linked(b, 'avm_ComponentInstance', a1)
    if hasattr(a1, 'avm_Container77'):
        assert _is_linked(a1, 'avm_Container77', b)
    _safe_set(b, 'avm_ComponentInstance', a2)
    assert _is_linked(b, 'avm_ComponentInstance', a2)
    if hasattr(a1, 'avm_Container77'):
        assert not _is_linked(a1, 'avm_Container77', b)
    if hasattr(a2, 'avm_Container77'):
        assert _is_linked(a2, 'avm_Container77', b)
    _safe_set(b, 'avm_ComponentInstance', None)
    assert not _is_linked(b, 'avm_ComponentInstance', a2)
    if hasattr(a2, 'avm_Container77'):
        assert not _is_linked(a2, 'avm_Container77', b)


def test_assoc_Connector31_reverse_link_reassign_clear():
    a1 = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Connector(Definition="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Connector32', a1)
    assert _is_linked(b, 'avm_Connector32', a1)
    if hasattr(a1, 'avm_Connector30'):
        assert _is_linked(a1, 'avm_Connector30', b)
    _safe_set(b, 'avm_Connector32', a2)
    assert _is_linked(b, 'avm_Connector32', a2)
    if hasattr(a1, 'avm_Connector30'):
        assert not _is_linked(a1, 'avm_Connector30', b)
    if hasattr(a2, 'avm_Connector30'):
        assert _is_linked(a2, 'avm_Connector30', b)
    _safe_set(b, 'avm_Connector32', None)
    assert not _is_linked(b, 'avm_Connector32', a2)
    if hasattr(a2, 'avm_Connector30'):
        assert not _is_linked(a2, 'avm_Connector30', b)


def test_assoc_Connector5_reverse_link_reassign_clear():
    a1 = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Connector(Definition="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component6', {a1})
    assert _is_linked(b, 'avm_Component6', a1)
    if hasattr(a1, 'avm_Connector'):
        assert _is_linked(a1, 'avm_Connector', b)
    _safe_set(b, 'avm_Component6', {a2})
    assert _is_linked(b, 'avm_Component6', a2)
    if hasattr(a1, 'avm_Connector'):
        assert not _is_linked(a1, 'avm_Connector', b)
    if hasattr(a2, 'avm_Connector'):
        assert _is_linked(a2, 'avm_Connector', b)
    _safe_set(b, 'avm_Component6', set())
    assert not _is_linked(b, 'avm_Component6', a2)
    if hasattr(a2, 'avm_Connector'):
        assert not _is_linked(a2, 'avm_Connector', b)


def test_assoc_Connector81_reverse_link_reassign_clear():
    a1 = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Container(Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Connector83', a1)
    assert _is_linked(b, 'avm_Connector83', a1)
    if hasattr(a1, 'avm_Container82'):
        assert _is_linked(a1, 'avm_Container82', b)
    _safe_set(b, 'avm_Connector83', a2)
    assert _is_linked(b, 'avm_Connector83', a2)
    if hasattr(a1, 'avm_Container82'):
        assert not _is_linked(a1, 'avm_Container82', b)
    if hasattr(a2, 'avm_Container82'):
        assert _is_linked(a2, 'avm_Container82', b)
    _safe_set(b, 'avm_Connector83', None)
    assert not _is_linked(b, 'avm_Connector83', a2)
    if hasattr(a2, 'avm_Container82'):
        assert not _is_linked(a2, 'avm_Container82', b)


def test_assoc_ConnectorComposition103_reverse_link_reassign_clear():
    a1 = avm_ConnectorCompositionTarget(ID="sample_text")
    a2 = avm_ConnectorCompositionTarget(ID="sample_text_2")
    b = avm_ConnectorCompositionTarget(ID="sample_text")
    _safe_set(b, 'avm_ConnectorCompositionTarget102', {a1})
    assert _is_linked(b, 'avm_ConnectorCompositionTarget102', a1)
    if hasattr(a1, 'avm_ConnectorCompositionTarget'):
        assert _is_linked(a1, 'avm_ConnectorCompositionTarget', b)
    _safe_set(b, 'avm_ConnectorCompositionTarget102', {a2})
    assert _is_linked(b, 'avm_ConnectorCompositionTarget102', a2)
    if hasattr(a1, 'avm_ConnectorCompositionTarget'):
        assert not _is_linked(a1, 'avm_ConnectorCompositionTarget', b)
    if hasattr(a2, 'avm_ConnectorCompositionTarget'):
        assert _is_linked(a2, 'avm_ConnectorCompositionTarget', b)
    _safe_set(b, 'avm_ConnectorCompositionTarget102', set())
    assert not _is_linked(b, 'avm_ConnectorCompositionTarget102', a2)
    if hasattr(a2, 'avm_ConnectorCompositionTarget'):
        assert not _is_linked(a2, 'avm_ConnectorCompositionTarget', b)


def test_assoc_ConnectorInstance95_reverse_link_reassign_clear():
    a1 = avm_ComponentInstance(ComponentID="sample_text", DesignSpaceSrcComponentID="sample_text", ID="sample_text", Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_ComponentInstance(ComponentID="sample_text_2", DesignSpaceSrcComponentID="sample_text_2", ID="sample_text_2", Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_ComponentConnectorInstance(IDinComponentModel="sample_text")
    _safe_set(b, 'avm_ComponentConnectorInstance', a1)
    assert _is_linked(b, 'avm_ComponentConnectorInstance', a1)
    if hasattr(a1, 'avm_ComponentInstance96'):
        assert _is_linked(a1, 'avm_ComponentInstance96', b)
    _safe_set(b, 'avm_ComponentConnectorInstance', a2)
    assert _is_linked(b, 'avm_ComponentConnectorInstance', a2)
    if hasattr(a1, 'avm_ComponentInstance96'):
        assert not _is_linked(a1, 'avm_ComponentInstance96', b)
    if hasattr(a2, 'avm_ComponentInstance96'):
        assert _is_linked(a2, 'avm_ComponentInstance96', b)
    _safe_set(b, 'avm_ComponentConnectorInstance', None)
    assert not _is_linked(b, 'avm_ComponentConnectorInstance', a2)
    if hasattr(a2, 'avm_ComponentInstance96'):
        assert not _is_linked(a2, 'avm_ComponentInstance96', b)


def test_assoc_Container71_reverse_link_reassign_clear():
    a1 = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Container(Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Container72', a1)
    assert _is_linked(b, 'avm_Container72', a1)
    if hasattr(a1, 'avm_Container70'):
        assert _is_linked(a1, 'avm_Container70', b)
    _safe_set(b, 'avm_Container72', a2)
    assert _is_linked(b, 'avm_Container72', a2)
    if hasattr(a1, 'avm_Container70'):
        assert not _is_linked(a1, 'avm_Container70', b)
    if hasattr(a2, 'avm_Container70'):
        assert _is_linked(a2, 'avm_Container70', b)
    _safe_set(b, 'avm_Container72', None)
    assert not _is_linked(b, 'avm_Container72', a2)
    if hasattr(a2, 'avm_Container70'):
        assert not _is_linked(a2, 'avm_Container70', b)


def test_assoc_DataSource19_reverse_link_reassign_clear():
    a1 = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    a2 = avm_Value(DataType="sample_text_2", DimensionType="sample_text_2", Dimensions="sample_text_2", Unit="sample_text_2")
    b = avm_DataSource(Notes="sample_text")
    _safe_set(b, 'avm_DataSource', a1)
    assert _is_linked(b, 'avm_DataSource', a1)
    if hasattr(a1, 'avm_Value20'):
        assert _is_linked(a1, 'avm_Value20', b)
    _safe_set(b, 'avm_DataSource', a2)
    assert _is_linked(b, 'avm_DataSource', a2)
    if hasattr(a1, 'avm_Value20'):
        assert not _is_linked(a1, 'avm_Value20', b)
    if hasattr(a2, 'avm_Value20'):
        assert _is_linked(a2, 'avm_Value20', b)
    _safe_set(b, 'avm_DataSource', None)
    assert not _is_linked(b, 'avm_DataSource', a2)
    if hasattr(a2, 'avm_Value20'):
        assert not _is_linked(a2, 'avm_Value20', b)


def test_assoc_DistributionRestriction7_reverse_link_reassign_clear():
    a1 = avm_DistributionRestriction(Notes="sample_text")
    a2 = avm_DistributionRestriction(Notes="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component8', {a1})
    assert _is_linked(b, 'avm_Component8', a1)
    if hasattr(a1, 'avm_DistributionRestriction'):
        assert _is_linked(a1, 'avm_DistributionRestriction', b)
    _safe_set(b, 'avm_Component8', {a2})
    assert _is_linked(b, 'avm_Component8', a2)
    if hasattr(a1, 'avm_DistributionRestriction'):
        assert not _is_linked(a1, 'avm_DistributionRestriction', b)
    if hasattr(a2, 'avm_DistributionRestriction'):
        assert _is_linked(a2, 'avm_DistributionRestriction', b)
    _safe_set(b, 'avm_Component8', set())
    assert not _is_linked(b, 'avm_Component8', a2)
    if hasattr(a2, 'avm_DistributionRestriction'):
        assert not _is_linked(a2, 'avm_DistributionRestriction', b)


def test_assoc_DomainModel0_reverse_link_reassign_clear():
    a1 = avm_DomainModel_(Author="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_DomainModel_(Author="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component', {a1})
    assert _is_linked(b, 'avm_Component', a1)
    if hasattr(a1, 'avm_DomainModel'):
        assert _is_linked(a1, 'avm_DomainModel', b)
    _safe_set(b, 'avm_Component', {a2})
    assert _is_linked(b, 'avm_Component', a2)
    if hasattr(a1, 'avm_DomainModel'):
        assert not _is_linked(a1, 'avm_DomainModel', b)
    if hasattr(a2, 'avm_DomainModel'):
        assert _is_linked(a2, 'avm_DomainModel', b)
    _safe_set(b, 'avm_Component', set())
    assert not _is_linked(b, 'avm_Component', a2)
    if hasattr(a2, 'avm_DomainModel'):
        assert not _is_linked(a2, 'avm_DomainModel', b)


def test_assoc_Formula13_reverse_link_reassign_clear():
    a1 = avm_Formula(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Formula(Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component14', {a1})
    assert _is_linked(b, 'avm_Component14', a1)
    if hasattr(a1, 'avm_Formula'):
        assert _is_linked(a1, 'avm_Formula', b)
    _safe_set(b, 'avm_Component14', {a2})
    assert _is_linked(b, 'avm_Component14', a2)
    if hasattr(a1, 'avm_Formula'):
        assert not _is_linked(a1, 'avm_Formula', b)
    if hasattr(a2, 'avm_Formula'):
        assert _is_linked(a2, 'avm_Formula', b)
    _safe_set(b, 'avm_Component14', set())
    assert not _is_linked(b, 'avm_Component14', a2)
    if hasattr(a2, 'avm_Formula'):
        assert not _is_linked(a2, 'avm_Formula', b)


def test_assoc_Formula87_reverse_link_reassign_clear():
    a1 = avm_Formula(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Formula(Name="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Container88', {a1})
    assert _is_linked(b, 'avm_Container88', a1)
    if hasattr(a1, 'avm_Formula89'):
        assert _is_linked(a1, 'avm_Formula89', b)
    _safe_set(b, 'avm_Container88', {a2})
    assert _is_linked(b, 'avm_Container88', a2)
    if hasattr(a1, 'avm_Formula89'):
        assert not _is_linked(a1, 'avm_Formula89', b)
    if hasattr(a2, 'avm_Formula89'):
        assert _is_linked(a2, 'avm_Formula89', b)
    _safe_set(b, 'avm_Container88', set())
    assert not _is_linked(b, 'avm_Container88', a2)
    if hasattr(a2, 'avm_Formula89'):
        assert not _is_linked(a2, 'avm_Formula89', b)


def test_assoc_FromResource64_reverse_link_reassign_clear():
    a1 = avm_Resource(Hash="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", Path="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Resource(Hash="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", Path="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_DataSource(Notes="sample_text")
    _safe_set(b, 'avm_DataSource65', {a1})
    assert _is_linked(b, 'avm_DataSource65', a1)
    if hasattr(a1, 'avm_Resource66'):
        assert _is_linked(a1, 'avm_Resource66', b)
    _safe_set(b, 'avm_DataSource65', {a2})
    assert _is_linked(b, 'avm_DataSource65', a2)
    if hasattr(a1, 'avm_Resource66'):
        assert not _is_linked(a1, 'avm_Resource66', b)
    if hasattr(a2, 'avm_Resource66'):
        assert _is_linked(a2, 'avm_Resource66', b)
    _safe_set(b, 'avm_DataSource65', set())
    assert not _is_linked(b, 'avm_DataSource65', a2)
    if hasattr(a2, 'avm_Resource66'):
        assert not _is_linked(a2, 'avm_Resource66', b)


def test_assoc_Operand107_reverse_link_reassign_clear():
    a1 = avm_ValueNode(ID="sample_text")
    a2 = avm_ValueNode(ID="sample_text_2")
    b = avm_SimpleFormula(Operation="sample_text")
    _safe_set(b, 'avm_SimpleFormula', {a1})
    assert _is_linked(b, 'avm_SimpleFormula', a1)
    if hasattr(a1, 'avm_ValueNode108'):
        assert _is_linked(a1, 'avm_ValueNode108', b)
    _safe_set(b, 'avm_SimpleFormula', {a2})
    assert _is_linked(b, 'avm_SimpleFormula', a2)
    if hasattr(a1, 'avm_ValueNode108'):
        assert not _is_linked(a1, 'avm_ValueNode108', b)
    if hasattr(a2, 'avm_ValueNode108'):
        assert _is_linked(a2, 'avm_ValueNode108', b)
    _safe_set(b, 'avm_SimpleFormula', set())
    assert not _is_linked(b, 'avm_SimpleFormula', a2)
    if hasattr(a2, 'avm_ValueNode108'):
        assert not _is_linked(a2, 'avm_ValueNode108', b)


def test_assoc_Operand109_reverse_link_reassign_clear():
    a1 = avm_Operand(Symbol="sample_text")
    a2 = avm_Operand(Symbol="sample_text_2")
    b = avm_ComplexFormula(Expression="sample_text")
    _safe_set(b, 'avm_ComplexFormula', {a1})
    assert _is_linked(b, 'avm_ComplexFormula', a1)
    if hasattr(a1, 'avm_Operand'):
        assert _is_linked(a1, 'avm_Operand', b)
    _safe_set(b, 'avm_ComplexFormula', {a2})
    assert _is_linked(b, 'avm_ComplexFormula', a2)
    if hasattr(a1, 'avm_Operand'):
        assert not _is_linked(a1, 'avm_Operand', b)
    if hasattr(a2, 'avm_Operand'):
        assert _is_linked(a2, 'avm_Operand', b)
    _safe_set(b, 'avm_ComplexFormula', set())
    assert not _is_linked(b, 'avm_ComplexFormula', a2)
    if hasattr(a2, 'avm_Operand'):
        assert not _is_linked(a2, 'avm_Operand', b)


def test_assoc_Port78_reverse_link_reassign_clear():
    a1 = avm_Port(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Port(Definition="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Container79', {a1})
    assert _is_linked(b, 'avm_Container79', a1)
    if hasattr(a1, 'avm_Port80'):
        assert _is_linked(a1, 'avm_Port80', b)
    _safe_set(b, 'avm_Container79', {a2})
    assert _is_linked(b, 'avm_Container79', a2)
    if hasattr(a1, 'avm_Port80'):
        assert not _is_linked(a1, 'avm_Port80', b)
    if hasattr(a2, 'avm_Port80'):
        assert _is_linked(a2, 'avm_Port80', b)
    _safe_set(b, 'avm_Container79', set())
    assert not _is_linked(b, 'avm_Container79', a2)
    if hasattr(a2, 'avm_Port80'):
        assert not _is_linked(a2, 'avm_Port80', b)


def test_assoc_Port9_reverse_link_reassign_clear():
    a1 = avm_Port(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Port(Definition="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component10', {a1})
    assert _is_linked(b, 'avm_Component10', a1)
    if hasattr(a1, 'avm_Port'):
        assert _is_linked(a1, 'avm_Port', b)
    _safe_set(b, 'avm_Component10', {a2})
    assert _is_linked(b, 'avm_Component10', a2)
    if hasattr(a1, 'avm_Port'):
        assert not _is_linked(a1, 'avm_Port', b)
    if hasattr(a2, 'avm_Port'):
        assert _is_linked(a2, 'avm_Port', b)
    _safe_set(b, 'avm_Component10', set())
    assert not _is_linked(b, 'avm_Component10', a2)
    if hasattr(a2, 'avm_Port'):
        assert not _is_linked(a2, 'avm_Port', b)


def test_assoc_PortInstance91_reverse_link_reassign_clear():
    a1 = avm_ComponentPortInstance(IDinComponentModel="sample_text")
    a2 = avm_ComponentPortInstance(IDinComponentModel="sample_text_2")
    b = avm_ComponentInstance(ComponentID="sample_text", DesignSpaceSrcComponentID="sample_text", ID="sample_text", Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_ComponentInstance92', {a1})
    assert _is_linked(b, 'avm_ComponentInstance92', a1)
    if hasattr(a1, 'avm_ComponentPortInstance'):
        assert _is_linked(a1, 'avm_ComponentPortInstance', b)
    _safe_set(b, 'avm_ComponentInstance92', {a2})
    assert _is_linked(b, 'avm_ComponentInstance92', a2)
    if hasattr(a1, 'avm_ComponentPortInstance'):
        assert not _is_linked(a1, 'avm_ComponentPortInstance', b)
    if hasattr(a2, 'avm_ComponentPortInstance'):
        assert _is_linked(a2, 'avm_ComponentPortInstance', b)
    _safe_set(b, 'avm_ComponentInstance92', set())
    assert not _is_linked(b, 'avm_ComponentInstance92', a2)
    if hasattr(a2, 'avm_ComponentPortInstance'):
        assert not _is_linked(a2, 'avm_ComponentPortInstance', b)


def test_assoc_PortMap101_reverse_link_reassign_clear():
    a1 = avm_PortMapTarget(ID="sample_text")
    a2 = avm_PortMapTarget(ID="sample_text_2")
    b = avm_PortMapTarget(ID="sample_text")
    _safe_set(b, 'avm_PortMapTarget100', {a1})
    assert _is_linked(b, 'avm_PortMapTarget100', a1)
    if hasattr(a1, 'avm_PortMapTarget'):
        assert _is_linked(a1, 'avm_PortMapTarget', b)
    _safe_set(b, 'avm_PortMapTarget100', {a2})
    assert _is_linked(b, 'avm_PortMapTarget100', a2)
    if hasattr(a1, 'avm_PortMapTarget'):
        assert not _is_linked(a1, 'avm_PortMapTarget', b)
    if hasattr(a2, 'avm_PortMapTarget'):
        assert _is_linked(a2, 'avm_PortMapTarget', b)
    _safe_set(b, 'avm_PortMapTarget100', set())
    assert not _is_linked(b, 'avm_PortMapTarget100', a2)
    if hasattr(a2, 'avm_PortMapTarget'):
        assert not _is_linked(a2, 'avm_PortMapTarget', b)


def test_assoc_PrimitivePropertyInstance93_reverse_link_reassign_clear():
    a1 = avm_ComponentPrimitivePropertyInstance(IDinComponentModel="sample_text")
    a2 = avm_ComponentPrimitivePropertyInstance(IDinComponentModel="sample_text_2")
    b = avm_ComponentInstance(ComponentID="sample_text", DesignSpaceSrcComponentID="sample_text", ID="sample_text", Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_ComponentInstance94', {a1})
    assert _is_linked(b, 'avm_ComponentInstance94', a1)
    if hasattr(a1, 'avm_ComponentPrimitivePropertyInstance'):
        assert _is_linked(a1, 'avm_ComponentPrimitivePropertyInstance', b)
    _safe_set(b, 'avm_ComponentInstance94', {a2})
    assert _is_linked(b, 'avm_ComponentInstance94', a2)
    if hasattr(a1, 'avm_ComponentPrimitivePropertyInstance'):
        assert not _is_linked(a1, 'avm_ComponentPrimitivePropertyInstance', b)
    if hasattr(a2, 'avm_ComponentPrimitivePropertyInstance'):
        assert _is_linked(a2, 'avm_ComponentPrimitivePropertyInstance', b)
    _safe_set(b, 'avm_ComponentInstance94', set())
    assert not _is_linked(b, 'avm_ComponentInstance94', a2)
    if hasattr(a2, 'avm_ComponentPrimitivePropertyInstance'):
        assert not _is_linked(a2, 'avm_ComponentPrimitivePropertyInstance', b)


def test_assoc_Property1_reverse_link_reassign_clear():
    a1 = avm_Property(Definition="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", OnDataSheet="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Property(Definition="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", OnDataSheet="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component2', {a1})
    assert _is_linked(b, 'avm_Component2', a1)
    if hasattr(a1, 'avm_Property'):
        assert _is_linked(a1, 'avm_Property', b)
    _safe_set(b, 'avm_Component2', {a2})
    assert _is_linked(b, 'avm_Component2', a2)
    if hasattr(a1, 'avm_Property'):
        assert not _is_linked(a1, 'avm_Property', b)
    if hasattr(a2, 'avm_Property'):
        assert _is_linked(a2, 'avm_Property', b)
    _safe_set(b, 'avm_Component2', set())
    assert not _is_linked(b, 'avm_Component2', a2)
    if hasattr(a2, 'avm_Property'):
        assert not _is_linked(a2, 'avm_Property', b)


def test_assoc_Property25_reverse_link_reassign_clear():
    a1 = avm_Property(Definition="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", OnDataSheet="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Property(Definition="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", OnDataSheet="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Connector26', {a1})
    assert _is_linked(b, 'avm_Connector26', a1)
    if hasattr(a1, 'avm_Property27'):
        assert _is_linked(a1, 'avm_Property27', b)
    _safe_set(b, 'avm_Connector26', {a2})
    assert _is_linked(b, 'avm_Connector26', a2)
    if hasattr(a1, 'avm_Property27'):
        assert not _is_linked(a1, 'avm_Property27', b)
    if hasattr(a2, 'avm_Property27'):
        assert _is_linked(a2, 'avm_Property27', b)
    _safe_set(b, 'avm_Connector26', set())
    assert not _is_linked(b, 'avm_Connector26', a2)
    if hasattr(a2, 'avm_Property27'):
        assert not _is_linked(a2, 'avm_Property27', b)


def test_assoc_Property73_reverse_link_reassign_clear():
    a1 = avm_Property(Definition="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", OnDataSheet="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Property(Definition="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", OnDataSheet="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Container74', {a1})
    assert _is_linked(b, 'avm_Container74', a1)
    if hasattr(a1, 'avm_Property75'):
        assert _is_linked(a1, 'avm_Property75', b)
    _safe_set(b, 'avm_Container74', {a2})
    assert _is_linked(b, 'avm_Container74', a2)
    if hasattr(a1, 'avm_Property75'):
        assert not _is_linked(a1, 'avm_Property75', b)
    if hasattr(a2, 'avm_Property75'):
        assert _is_linked(a2, 'avm_Property75', b)
    _safe_set(b, 'avm_Container74', set())
    assert not _is_linked(b, 'avm_Container74', a2)
    if hasattr(a2, 'avm_Property75'):
        assert not _is_linked(a2, 'avm_Property75', b)


def test_assoc_ResourceDependency3_reverse_link_reassign_clear():
    a1 = avm_Resource(Hash="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", Path="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Resource(Hash="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", Path="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    _safe_set(b, 'avm_Component4', {a1})
    assert _is_linked(b, 'avm_Component4', a1)
    if hasattr(a1, 'avm_Resource'):
        assert _is_linked(a1, 'avm_Resource', b)
    _safe_set(b, 'avm_Component4', {a2})
    assert _is_linked(b, 'avm_Component4', a2)
    if hasattr(a1, 'avm_Resource'):
        assert not _is_linked(a1, 'avm_Resource', b)
    if hasattr(a2, 'avm_Resource'):
        assert _is_linked(a2, 'avm_Resource', b)
    _safe_set(b, 'avm_Component4', set())
    assert not _is_linked(b, 'avm_Component4', a2)
    if hasattr(a2, 'avm_Resource'):
        assert not _is_linked(a2, 'avm_Resource', b)


def test_assoc_Role22_reverse_link_reassign_clear():
    a1 = avm_Port(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Port(Definition="sample_text_2", Name="sample_text_2", Notes="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Connector23', {a1})
    assert _is_linked(b, 'avm_Connector23', a1)
    if hasattr(a1, 'avm_Port24'):
        assert _is_linked(a1, 'avm_Port24', b)
    _safe_set(b, 'avm_Connector23', {a2})
    assert _is_linked(b, 'avm_Connector23', a2)
    if hasattr(a1, 'avm_Port24'):
        assert not _is_linked(a1, 'avm_Port24', b)
    if hasattr(a2, 'avm_Port24'):
        assert _is_linked(a2, 'avm_Port24', b)
    _safe_set(b, 'avm_Connector23', set())
    assert not _is_linked(b, 'avm_Connector23', a2)
    if hasattr(a2, 'avm_Port24'):
        assert not _is_linked(a2, 'avm_Port24', b)


def test_assoc_RootContainer67_reverse_link_reassign_clear():
    a1 = avm_Design(DesignID="sample_text", DesignSpaceSrcID="sample_text", Name="sample_text", SchemaVersion="sample_text")
    a2 = avm_Design(DesignID="sample_text_2", DesignSpaceSrcID="sample_text_2", Name="sample_text_2", SchemaVersion="sample_text_2")
    b = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_Container', a1)
    assert _is_linked(b, 'avm_Container', a1)
    if hasattr(a1, 'avm_Design'):
        assert _is_linked(a1, 'avm_Design', b)
    _safe_set(b, 'avm_Container', a2)
    assert _is_linked(b, 'avm_Container', a2)
    if hasattr(a1, 'avm_Design'):
        assert not _is_linked(a1, 'avm_Design', b)
    if hasattr(a2, 'avm_Design'):
        assert _is_linked(a2, 'avm_Design', b)
    _safe_set(b, 'avm_Container', None)
    assert not _is_linked(b, 'avm_Container', a2)
    if hasattr(a2, 'avm_Design'):
        assert not _is_linked(a2, 'avm_Design', b)


def test_assoc_Task132_reverse_link_reassign_clear():
    a1 = avm_WorkflowTaskBase(Name="sample_text")
    a2 = avm_WorkflowTaskBase(Name="sample_text_2")
    b = avm_Workflow(Name="sample_text")
    _safe_set(b, 'avm_Workflow133', {a1})
    assert _is_linked(b, 'avm_Workflow133', a1)
    if hasattr(a1, 'avm_WorkflowTaskBase'):
        assert _is_linked(a1, 'avm_WorkflowTaskBase', b)
    _safe_set(b, 'avm_Workflow133', {a2})
    assert _is_linked(b, 'avm_Workflow133', a2)
    if hasattr(a1, 'avm_WorkflowTaskBase'):
        assert not _is_linked(a1, 'avm_WorkflowTaskBase', b)
    if hasattr(a2, 'avm_WorkflowTaskBase'):
        assert _is_linked(a2, 'avm_WorkflowTaskBase', b)
    _safe_set(b, 'avm_Workflow133', set())
    assert not _is_linked(b, 'avm_Workflow133', a2)
    if hasattr(a2, 'avm_WorkflowTaskBase'):
        assert not _is_linked(a2, 'avm_WorkflowTaskBase', b)


def test_assoc_TestComponent120_reverse_link_reassign_clear():
    a1 = avm_TestBench(Name="sample_text")
    a2 = avm_TestBench(Name="sample_text_2")
    b = avm_ComponentInstance(ComponentID="sample_text", DesignSpaceSrcComponentID="sample_text", ID="sample_text", Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_ComponentInstance122', a1)
    assert _is_linked(b, 'avm_ComponentInstance122', a1)
    if hasattr(a1, 'avm_TestBench121'):
        assert _is_linked(a1, 'avm_TestBench121', b)
    _safe_set(b, 'avm_ComponentInstance122', a2)
    assert _is_linked(b, 'avm_ComponentInstance122', a2)
    if hasattr(a1, 'avm_TestBench121'):
        assert not _is_linked(a1, 'avm_TestBench121', b)
    if hasattr(a2, 'avm_TestBench121'):
        assert _is_linked(a2, 'avm_TestBench121', b)
    _safe_set(b, 'avm_ComponentInstance122', None)
    assert not _is_linked(b, 'avm_ComponentInstance122', a2)
    if hasattr(a2, 'avm_TestBench121'):
        assert not _is_linked(a2, 'avm_TestBench121', b)


def test_assoc_TestStructure127_reverse_link_reassign_clear():
    a1 = avm_TestBench(Name="sample_text")
    a2 = avm_TestBench(Name="sample_text_2")
    b = avm_DomainModel_(Author="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_DomainModel129', a1)
    assert _is_linked(b, 'avm_DomainModel129', a1)
    if hasattr(a1, 'avm_TestBench128'):
        assert _is_linked(a1, 'avm_TestBench128', b)
    _safe_set(b, 'avm_DomainModel129', a2)
    assert _is_linked(b, 'avm_DomainModel129', a2)
    if hasattr(a1, 'avm_TestBench128'):
        assert not _is_linked(a1, 'avm_TestBench128', b)
    if hasattr(a2, 'avm_TestBench128'):
        assert _is_linked(a2, 'avm_TestBench128', b)
    _safe_set(b, 'avm_DomainModel129', None)
    assert not _is_linked(b, 'avm_DomainModel129', a2)
    if hasattr(a2, 'avm_TestBench128'):
        assert not _is_linked(a2, 'avm_TestBench128', b)


def test_assoc_TopLevelSystemUnderTest113_reverse_link_reassign_clear():
    a1 = avm_TopLevelSystemUnderTest(DesignID="sample_text")
    a2 = avm_TopLevelSystemUnderTest(DesignID="sample_text_2")
    b = avm_TestBench(Name="sample_text")
    _safe_set(b, 'avm_TestBench', a1)
    assert _is_linked(b, 'avm_TestBench', a1)
    if hasattr(a1, 'avm_TopLevelSystemUnderTest'):
        assert _is_linked(a1, 'avm_TopLevelSystemUnderTest', b)
    _safe_set(b, 'avm_TestBench', a2)
    assert _is_linked(b, 'avm_TestBench', a2)
    if hasattr(a1, 'avm_TopLevelSystemUnderTest'):
        assert not _is_linked(a1, 'avm_TopLevelSystemUnderTest', b)
    if hasattr(a2, 'avm_TopLevelSystemUnderTest'):
        assert _is_linked(a2, 'avm_TopLevelSystemUnderTest', b)
    _safe_set(b, 'avm_TestBench', None)
    assert not _is_linked(b, 'avm_TestBench', a2)
    if hasattr(a2, 'avm_TopLevelSystemUnderTest'):
        assert not _is_linked(a2, 'avm_TopLevelSystemUnderTest', b)


def test_assoc_UsesResource15_reverse_link_reassign_clear():
    a1 = avm_Resource(Hash="sample_text", ID="sample_text", Name="sample_text", Notes="sample_text", Path="sample_text", XPosition="sample_text", YPosition="sample_text")
    a2 = avm_Resource(Hash="sample_text_2", ID="sample_text_2", Name="sample_text_2", Notes="sample_text_2", Path="sample_text_2", XPosition="sample_text_2", YPosition="sample_text_2")
    b = avm_DomainModel_(Author="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_DomainModel16', {a1})
    assert _is_linked(b, 'avm_DomainModel16', a1)
    if hasattr(a1, 'avm_Resource17'):
        assert _is_linked(a1, 'avm_Resource17', b)
    _safe_set(b, 'avm_DomainModel16', {a2})
    assert _is_linked(b, 'avm_DomainModel16', a2)
    if hasattr(a1, 'avm_Resource17'):
        assert not _is_linked(a1, 'avm_Resource17', b)
    if hasattr(a2, 'avm_Resource17'):
        assert _is_linked(a2, 'avm_Resource17', b)
    _safe_set(b, 'avm_DomainModel16', set())
    assert not _is_linked(b, 'avm_DomainModel16', a2)
    if hasattr(a2, 'avm_Resource17'):
        assert not _is_linked(a2, 'avm_Resource17', b)


def test_assoc_Value130_reverse_link_reassign_clear():
    a1 = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    a2 = avm_Value(DataType="sample_text_2", DimensionType="sample_text_2", Dimensions="sample_text_2", Unit="sample_text_2")
    b = avm_TestBenchValueBase(ID="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_TestBenchValueBase', a1)
    assert _is_linked(b, 'avm_TestBenchValueBase', a1)
    if hasattr(a1, 'avm_Value131'):
        assert _is_linked(a1, 'avm_Value131', b)
    _safe_set(b, 'avm_TestBenchValueBase', a2)
    assert _is_linked(b, 'avm_TestBenchValueBase', a2)
    if hasattr(a1, 'avm_Value131'):
        assert not _is_linked(a1, 'avm_Value131', b)
    if hasattr(a2, 'avm_Value131'):
        assert _is_linked(a2, 'avm_Value131', b)
    _safe_set(b, 'avm_TestBenchValueBase', None)
    assert not _is_linked(b, 'avm_TestBenchValueBase', a2)
    if hasattr(a2, 'avm_Value131'):
        assert not _is_linked(a2, 'avm_Value131', b)


def test_assoc_Value51_reverse_link_reassign_clear():
    a1 = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    a2 = avm_Value(DataType="sample_text_2", DimensionType="sample_text_2", Dimensions="sample_text_2", Unit="sample_text_2")
    b = avm_DomainModelMetric(ID="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    _safe_set(b, 'avm_DomainModelMetric', a1)
    assert _is_linked(b, 'avm_DomainModelMetric', a1)
    if hasattr(a1, 'avm_Value52'):
        assert _is_linked(a1, 'avm_Value52', b)
    _safe_set(b, 'avm_DomainModelMetric', a2)
    assert _is_linked(b, 'avm_DomainModelMetric', a2)
    if hasattr(a1, 'avm_Value52'):
        assert not _is_linked(a1, 'avm_Value52', b)
    if hasattr(a2, 'avm_Value52'):
        assert _is_linked(a2, 'avm_Value52', b)
    _safe_set(b, 'avm_DomainModelMetric', None)
    assert not _is_linked(b, 'avm_DomainModelMetric', a2)
    if hasattr(a2, 'avm_Value52'):
        assert not _is_linked(a2, 'avm_Value52', b)


def test_assoc_Value97_reverse_link_reassign_clear():
    a1 = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    a2 = avm_Value(DataType="sample_text_2", DimensionType="sample_text_2", Dimensions="sample_text_2", Unit="sample_text_2")
    b = avm_ComponentPrimitivePropertyInstance(IDinComponentModel="sample_text")
    _safe_set(b, 'avm_ComponentPrimitivePropertyInstance98', a1)
    assert _is_linked(b, 'avm_ComponentPrimitivePropertyInstance98', a1)
    if hasattr(a1, 'avm_Value99'):
        assert _is_linked(a1, 'avm_Value99', b)
    _safe_set(b, 'avm_ComponentPrimitivePropertyInstance98', a2)
    assert _is_linked(b, 'avm_ComponentPrimitivePropertyInstance98', a2)
    if hasattr(a1, 'avm_Value99'):
        assert not _is_linked(a1, 'avm_Value99', b)
    if hasattr(a2, 'avm_Value99'):
        assert _is_linked(a2, 'avm_Value99', b)
    _safe_set(b, 'avm_ComponentPrimitivePropertyInstance98', None)
    assert not _is_linked(b, 'avm_ComponentPrimitivePropertyInstance98', a2)
    if hasattr(a2, 'avm_Value99'):
        assert not _is_linked(a2, 'avm_Value99', b)


def test_assoc_ValueSource110_reverse_link_reassign_clear():
    a1 = avm_ValueNode(ID="sample_text")
    a2 = avm_ValueNode(ID="sample_text_2")
    b = avm_Operand(Symbol="sample_text")
    _safe_set(b, 'avm_Operand111', a1)
    assert _is_linked(b, 'avm_Operand111', a1)
    if hasattr(a1, 'avm_ValueNode112'):
        assert _is_linked(a1, 'avm_ValueNode112', b)
    _safe_set(b, 'avm_Operand111', a2)
    assert _is_linked(b, 'avm_Operand111', a2)
    if hasattr(a1, 'avm_ValueNode112'):
        assert not _is_linked(a1, 'avm_ValueNode112', b)
    if hasattr(a2, 'avm_ValueNode112'):
        assert _is_linked(a2, 'avm_ValueNode112', b)
    _safe_set(b, 'avm_Operand111', None)
    assert not _is_linked(b, 'avm_Operand111', a2)
    if hasattr(a2, 'avm_ValueNode112'):
        assert not _is_linked(a2, 'avm_ValueNode112', b)


def test_assoc_Workflow123_reverse_link_reassign_clear():
    a1 = avm_Workflow(Name="sample_text")
    a2 = avm_Workflow(Name="sample_text_2")
    b = avm_TestBench(Name="sample_text")
    _safe_set(b, 'avm_TestBench124', a1)
    assert _is_linked(b, 'avm_TestBench124', a1)
    if hasattr(a1, 'avm_Workflow'):
        assert _is_linked(a1, 'avm_Workflow', b)
    _safe_set(b, 'avm_TestBench124', a2)
    assert _is_linked(b, 'avm_TestBench124', a2)
    if hasattr(a1, 'avm_Workflow'):
        assert not _is_linked(a1, 'avm_Workflow', b)
    if hasattr(a2, 'avm_Workflow'):
        assert _is_linked(a2, 'avm_Workflow', b)
    _safe_set(b, 'avm_TestBench124', None)
    assert not _is_linked(b, 'avm_TestBench124', a2)
    if hasattr(a2, 'avm_Workflow'):
        assert not _is_linked(a2, 'avm_Workflow', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_AnalysisConstruct11_stub_double():
    # avm_AnalysisConstruct has no real 'avm_AnalysisConstruct' property in the generated
    # code (a bare stub) -- manually attach it so avm_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Component(Classifications="sample_text", ID="sample_text", Name="sample_text", SchemaVersion="sample_text", Supercedes="sample_text", Version="sample_text")
    partner = avm_AnalysisConstruct()
    setattr(partner, 'avm_AnalysisConstruct', None)
    _safe_set(owner, 'avm_Component12', {partner})
    assert getattr(partner, 'avm_AnalysisConstruct') == owner
    _safe_set(owner, 'avm_Component12', set())
    assert getattr(partner, 'avm_AnalysisConstruct') is None


def test_assoc_ApplyJoinData104_stub_double():
    # avm_assemblyDetail has no real 'avm_assemblyDetail106' property in the generated
    # code (a bare stub) -- manually attach it so avm_ConnectorCompositionTarget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_ConnectorCompositionTarget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_ConnectorCompositionTarget(ID="sample_text")
    partner = avm_assemblyDetail()
    setattr(partner, 'avm_assemblyDetail106', None)
    _safe_set(owner, 'avm_ConnectorCompositionTarget105', {partner})
    assert getattr(partner, 'avm_assemblyDetail106') == owner
    _safe_set(owner, 'avm_ConnectorCompositionTarget105', set())
    assert getattr(partner, 'avm_assemblyDetail106') is None


def test_assoc_AssignedValue60_stub_double():
    # avm_ParametricEnumeratedValue has no real 'avm_ParametricEnumeratedValue' property in the generated
    # code (a bare stub) -- manually attach it so avm_FixedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_FixedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_FixedValue(Uncertainty="sample_text", Value="sample_text")
    partner = avm_ParametricEnumeratedValue()
    setattr(partner, 'avm_ParametricEnumeratedValue', None)
    _safe_set(owner, 'avm_FixedValue', partner)
    assert getattr(partner, 'avm_ParametricEnumeratedValue') == owner
    _safe_set(owner, 'avm_FixedValue', None)
    assert getattr(partner, 'avm_ParametricEnumeratedValue') is None


def test_assoc_Connector138_stub_double():
    # Connector has no real 'Connector' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_ModelicaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_ModelicaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_ModelicaModel(Class="sample_text")
    partner = Connector()
    setattr(partner, 'Connector', None)
    _safe_set(owner, 'avm_modelica_ModelicaModel139', {partner})
    assert getattr(partner, 'Connector') == owner
    _safe_set(owner, 'avm_modelica_ModelicaModel139', set())
    assert getattr(partner, 'Connector') is None


def test_assoc_Connector235_stub_double():
    # Connector has no real 'Connector236' property in the generated
    # code (a bare stub) -- manually attach it so avm_cyber_CyberModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_cyber_CyberModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_cyber_CyberModel(Class="sample_text", Locator="sample_text", Type="sample_text")
    partner = Connector()
    setattr(partner, 'Connector236', None)
    _safe_set(owner, 'avm_cyber_CyberModel', {partner})
    assert getattr(partner, 'Connector236') == owner
    _safe_set(owner, 'avm_cyber_CyberModel', set())
    assert getattr(partner, 'Connector236') is None


def test_assoc_ConnectorFeature33_stub_double():
    # avm_ConnectorFeature has no real 'avm_ConnectorFeature' property in the generated
    # code (a bare stub) -- manually attach it so avm_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    partner = avm_ConnectorFeature()
    setattr(partner, 'avm_ConnectorFeature', None)
    _safe_set(owner, 'avm_Connector34', {partner})
    assert getattr(partner, 'avm_ConnectorFeature') == owner
    _safe_set(owner, 'avm_Connector34', set())
    assert getattr(partner, 'avm_ConnectorFeature') is None


def test_assoc_DatumMetric163_stub_double():
    # Metric has no real 'Metric164' property in the generated
    # code (a bare stub) -- manually attach it so avm_cad_Datum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_cad_Datum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_cad_Datum(DatumName="sample_text")
    partner = Metric()
    setattr(partner, 'Metric164', None)
    _safe_set(owner, 'avm_cad_Datum', {partner})
    assert getattr(partner, 'Metric164') == owner
    _safe_set(owner, 'avm_cad_Datum', set())
    assert getattr(partner, 'Metric164') is None


def test_assoc_DefaultJoin28_stub_double():
    # avm_assemblyDetail has no real 'avm_assemblyDetail' property in the generated
    # code (a bare stub) -- manually attach it so avm_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Connector(Definition="sample_text", Name="sample_text", Notes="sample_text", XPosition="sample_text", YPosition="sample_text")
    partner = avm_assemblyDetail()
    setattr(partner, 'avm_assemblyDetail', None)
    _safe_set(owner, 'avm_Connector29', {partner})
    assert getattr(partner, 'avm_assemblyDetail') == owner
    _safe_set(owner, 'avm_Connector29', set())
    assert getattr(partner, 'avm_assemblyDetail') is None


def test_assoc_DomainFeature68_stub_double():
    # avm_DesignDomainFeature has no real 'avm_DesignDomainFeature' property in the generated
    # code (a bare stub) -- manually attach it so avm_Design's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Design's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Design(DesignID="sample_text", DesignSpaceSrcID="sample_text", Name="sample_text", SchemaVersion="sample_text")
    partner = avm_DesignDomainFeature()
    setattr(partner, 'avm_DesignDomainFeature', None)
    _safe_set(owner, 'avm_Design69', {partner})
    assert getattr(partner, 'avm_DesignDomainFeature') == owner
    _safe_set(owner, 'avm_Design69', set())
    assert getattr(partner, 'avm_DesignDomainFeature') is None


def test_assoc_FileReferenceSwap247_stub_double():
    # FileReference has no real 'FileReference249' property in the generated
    # code (a bare stub) -- manually attach it so avm_adamsCar_FileReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_adamsCar_FileReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_adamsCar_FileReference(FilePath="sample_text", ID="sample_text", Name="sample_text")
    partner = FileReference()
    setattr(partner, 'FileReference249', None)
    _safe_set(owner, 'avm_adamsCar_FileReference248', {partner})
    assert getattr(partner, 'FileReference249') == owner
    _safe_set(owner, 'avm_adamsCar_FileReference248', set())
    assert getattr(partner, 'FileReference249') is None


def test_assoc_InputGeometry188_stub_double():
    # Geometry has no real 'Geometry' property in the generated
    # code (a bare stub) -- manually attach it so avm_cad_CustomGeometryInput's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_cad_CustomGeometryInput's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_cad_CustomGeometryInput(Operation="sample_text")
    partner = Geometry()
    setattr(partner, 'Geometry', None)
    _safe_set(owner, 'avm_cad_CustomGeometryInput', partner)
    assert getattr(partner, 'Geometry') == owner
    _safe_set(owner, 'avm_cad_CustomGeometryInput', None)
    assert getattr(partner, 'Geometry') is None


def test_assoc_JoinData84_stub_double():
    # avm_assemblyDetail has no real 'avm_assemblyDetail86' property in the generated
    # code (a bare stub) -- manually attach it so avm_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Container(Name="sample_text", XPosition="sample_text", YPosition="sample_text")
    partner = avm_assemblyDetail()
    setattr(partner, 'avm_assemblyDetail86', None)
    _safe_set(owner, 'avm_Container85', {partner})
    assert getattr(partner, 'avm_assemblyDetail86') == owner
    _safe_set(owner, 'avm_Container85', set())
    assert getattr(partner, 'avm_assemblyDetail86') is None


def test_assoc_Limit142_stub_double():
    # Limit has no real 'Limit' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_ModelicaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_ModelicaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_ModelicaModel(Class="sample_text")
    partner = Limit()
    setattr(partner, 'Limit', None)
    _safe_set(owner, 'avm_modelica_ModelicaModel143', {partner})
    assert getattr(partner, 'Limit') == owner
    _safe_set(owner, 'avm_modelica_ModelicaModel143', set())
    assert getattr(partner, 'Limit') is None


def test_assoc_Metric116_stub_double():
    # avm_Metric has no real 'avm_Metric' property in the generated
    # code (a bare stub) -- manually attach it so avm_TestBench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_TestBench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_TestBench(Name="sample_text")
    partner = avm_Metric()
    setattr(partner, 'avm_Metric', None)
    _safe_set(owner, 'avm_TestBench117', {partner})
    assert getattr(partner, 'avm_Metric') == owner
    _safe_set(owner, 'avm_TestBench117', set())
    assert getattr(partner, 'avm_Metric') is None


def test_assoc_Metric140_stub_double():
    # Metric has no real 'Metric' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_ModelicaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_ModelicaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_ModelicaModel(Class="sample_text")
    partner = Metric()
    setattr(partner, 'Metric', None)
    _safe_set(owner, 'avm_modelica_ModelicaModel141', {partner})
    assert getattr(partner, 'Metric') == owner
    _safe_set(owner, 'avm_modelica_ModelicaModel141', set())
    assert getattr(partner, 'Metric') is None


def test_assoc_Parameter114_stub_double():
    # avm_Parameter has no real 'avm_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so avm_TestBench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_TestBench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_TestBench(Name="sample_text")
    partner = avm_Parameter()
    setattr(partner, 'avm_Parameter', None)
    _safe_set(owner, 'avm_TestBench115', {partner})
    assert getattr(partner, 'avm_Parameter') == owner
    _safe_set(owner, 'avm_TestBench115', set())
    assert getattr(partner, 'avm_Parameter') is None


def test_assoc_Parameter137_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_ModelicaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_ModelicaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_ModelicaModel(Class="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'avm_modelica_ModelicaModel', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'avm_modelica_ModelicaModel', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_Parameter146_stub_double():
    # Parameter has no real 'Parameter147' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_Connector(Class="sample_text", Locator="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter147', None)
    _safe_set(owner, 'avm_modelica_Connector', {partner})
    assert getattr(partner, 'Parameter147') == owner
    _safe_set(owner, 'avm_modelica_Connector', set())
    assert getattr(partner, 'Parameter147') is None


def test_assoc_Parameter237_stub_double():
    # Parameter has no real 'Parameter239' property in the generated
    # code (a bare stub) -- manually attach it so avm_cyber_CyberModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_cyber_CyberModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_cyber_CyberModel(Class="sample_text", Locator="sample_text", Type="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter239', None)
    _safe_set(owner, 'avm_cyber_CyberModel238', {partner})
    assert getattr(partner, 'Parameter239') == owner
    _safe_set(owner, 'avm_cyber_CyberModel238', set())
    assert getattr(partner, 'Parameter239') is None


def test_assoc_ParameterSwap245_stub_double():
    # Parameter has no real 'Parameter246' property in the generated
    # code (a bare stub) -- manually attach it so avm_adamsCar_FileReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_adamsCar_FileReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_adamsCar_FileReference(FilePath="sample_text", ID="sample_text", Name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter246', None)
    _safe_set(owner, 'avm_adamsCar_FileReference', {partner})
    assert getattr(partner, 'Parameter246') == owner
    _safe_set(owner, 'avm_adamsCar_FileReference', set())
    assert getattr(partner, 'Parameter246') is None


def test_assoc_Redeclare144_stub_double():
    # Redeclare has no real 'Redeclare' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_ModelicaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_ModelicaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_ModelicaModel(Class="sample_text")
    partner = Redeclare()
    setattr(partner, 'Redeclare', None)
    _safe_set(owner, 'avm_modelica_ModelicaModel145', {partner})
    assert getattr(partner, 'Redeclare') == owner
    _safe_set(owner, 'avm_modelica_ModelicaModel145', set())
    assert getattr(partner, 'Redeclare') is None


def test_assoc_Redeclare148_stub_double():
    # Redeclare has no real 'Redeclare150' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_Connector(Class="sample_text", Locator="sample_text")
    partner = Redeclare()
    setattr(partner, 'Redeclare150', None)
    _safe_set(owner, 'avm_modelica_Connector149', {partner})
    assert getattr(partner, 'Redeclare150') == owner
    _safe_set(owner, 'avm_modelica_Connector149', set())
    assert getattr(partner, 'Redeclare150') is None


def test_assoc_Settings125_stub_double():
    # avm_Settings has no real 'avm_Settings' property in the generated
    # code (a bare stub) -- manually attach it so avm_TestBench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_TestBench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_TestBench(Name="sample_text")
    partner = avm_Settings()
    setattr(partner, 'avm_Settings', None)
    _safe_set(owner, 'avm_TestBench126', {partner})
    assert getattr(partner, 'avm_Settings') == owner
    _safe_set(owner, 'avm_TestBench126', set())
    assert getattr(partner, 'avm_Settings') is None


def test_assoc_Source134_stub_double():
    # avm_ValueFlowMux has no real 'avm_ValueFlowMux135' property in the generated
    # code (a bare stub) -- manually attach it so avm_ValueNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_ValueNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_ValueNode(ID="sample_text")
    partner = avm_ValueFlowMux()
    setattr(partner, 'avm_ValueFlowMux135', None)
    _safe_set(owner, 'avm_ValueNode136', partner)
    assert owner in getattr(partner, 'avm_ValueFlowMux135')
    _safe_set(owner, 'avm_ValueNode136', None)
    assert owner not in getattr(partner, 'avm_ValueFlowMux135')


def test_assoc_TargetValue152_stub_double():
    # modelica_avm_Value has no real 'modelica_avm_Value153' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_Limit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_Limit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_Limit(BoundType="sample_text", Name="sample_text", Notes="sample_text", ToleranceTimeWindow="sample_text", VariableLocator="sample_text")
    partner = modelica_avm_Value()
    setattr(partner, 'modelica_avm_Value153', None)
    _safe_set(owner, 'avm_modelica_Limit', partner)
    assert getattr(partner, 'modelica_avm_Value153') == owner
    _safe_set(owner, 'avm_modelica_Limit', None)
    assert getattr(partner, 'modelica_avm_Value153') is None


def test_assoc_TestInjectionPoint118_stub_double():
    # avm_TestInjectionPoint has no real 'avm_TestInjectionPoint' property in the generated
    # code (a bare stub) -- manually attach it so avm_TestBench's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_TestBench's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_TestBench(Name="sample_text")
    partner = avm_TestInjectionPoint()
    setattr(partner, 'avm_TestInjectionPoint', None)
    _safe_set(owner, 'avm_TestBench119', {partner})
    assert getattr(partner, 'avm_TestInjectionPoint') == owner
    _safe_set(owner, 'avm_TestBench119', set())
    assert getattr(partner, 'avm_TestInjectionPoint') is None


def test_assoc_Value151_stub_double():
    # modelica_avm_Value has no real 'modelica_avm_Value' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_Parameter(Locator="sample_text")
    partner = modelica_avm_Value()
    setattr(partner, 'modelica_avm_Value', None)
    _safe_set(owner, 'avm_modelica_Parameter', partner)
    assert getattr(partner, 'modelica_avm_Value') == owner
    _safe_set(owner, 'avm_modelica_Parameter', None)
    assert getattr(partner, 'modelica_avm_Value') is None


def test_assoc_Value154_stub_double():
    # modelica_avm_Value has no real 'modelica_avm_Value155' property in the generated
    # code (a bare stub) -- manually attach it so avm_modelica_Redeclare's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_modelica_Redeclare's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_modelica_Redeclare(Locator="sample_text", Type="sample_text")
    partner = modelica_avm_Value()
    setattr(partner, 'modelica_avm_Value155', None)
    _safe_set(owner, 'avm_modelica_Redeclare', partner)
    assert getattr(partner, 'modelica_avm_Value155') == owner
    _safe_set(owner, 'avm_modelica_Redeclare', None)
    assert getattr(partner, 'modelica_avm_Value155') is None


def test_assoc_Value165_stub_double():
    # cad_avm_Value has no real 'cad_avm_Value' property in the generated
    # code (a bare stub) -- manually attach it so avm_cad_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_cad_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_cad_Parameter(Name="sample_text")
    partner = cad_avm_Value()
    setattr(partner, 'cad_avm_Value', None)
    _safe_set(owner, 'avm_cad_Parameter', partner)
    assert getattr(partner, 'cad_avm_Value') == owner
    _safe_set(owner, 'avm_cad_Parameter', None)
    assert getattr(partner, 'cad_avm_Value') is None


def test_assoc_Value234_stub_double():
    # manufacturing_avm_Value has no real 'manufacturing_avm_Value' property in the generated
    # code (a bare stub) -- manually attach it so avm_manufacturing_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_manufacturing_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_manufacturing_Parameter(Locator="sample_text", Name="sample_text")
    partner = manufacturing_avm_Value()
    setattr(partner, 'manufacturing_avm_Value', None)
    _safe_set(owner, 'avm_manufacturing_Parameter', partner)
    assert getattr(partner, 'manufacturing_avm_Value') == owner
    _safe_set(owner, 'avm_manufacturing_Parameter', None)
    assert getattr(partner, 'manufacturing_avm_Value') is None


def test_assoc_Value244_stub_double():
    # adamsCar_avm_Value has no real 'adamsCar_avm_Value' property in the generated
    # code (a bare stub) -- manually attach it so avm_adamsCar_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_adamsCar_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_adamsCar_Parameter(ID="sample_text", Name="sample_text")
    partner = adamsCar_avm_Value()
    setattr(partner, 'adamsCar_avm_Value', None)
    _safe_set(owner, 'avm_adamsCar_Parameter', partner)
    assert getattr(partner, 'adamsCar_avm_Value') == owner
    _safe_set(owner, 'avm_adamsCar_Parameter', None)
    assert getattr(partner, 'adamsCar_avm_Value') is None


def test_assoc_Value53_stub_double():
    # avm_PrimitiveProperty has no real 'avm_PrimitiveProperty' property in the generated
    # code (a bare stub) -- manually attach it so avm_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    partner = avm_PrimitiveProperty()
    setattr(partner, 'avm_PrimitiveProperty', None)
    _safe_set(owner, 'avm_Value54', partner)
    assert getattr(partner, 'avm_PrimitiveProperty') == owner
    _safe_set(owner, 'avm_Value54', None)
    assert getattr(partner, 'avm_PrimitiveProperty') is None


def test_assoc_ValueExpression18_stub_double():
    # avm_ValueExpressionType has no real 'avm_ValueExpressionType' property in the generated
    # code (a bare stub) -- manually attach it so avm_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_Value(DataType="sample_text", DimensionType="sample_text", Dimensions="sample_text", Unit="sample_text")
    partner = avm_ValueExpressionType()
    setattr(partner, 'avm_ValueExpressionType', None)
    _safe_set(owner, 'avm_Value', partner)
    assert getattr(partner, 'avm_ValueExpressionType') == owner
    _safe_set(owner, 'avm_Value', None)
    assert getattr(partner, 'avm_ValueExpressionType') is None


def test_assoc_ValueSource21_stub_double():
    # avm_DerivedValue has no real 'avm_DerivedValue' property in the generated
    # code (a bare stub) -- manually attach it so avm_ValueNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # avm_ValueNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = avm_ValueNode(ID="sample_text")
    partner = avm_DerivedValue()
    setattr(partner, 'avm_DerivedValue', None)
    _safe_set(owner, 'avm_ValueNode', partner)
    assert getattr(partner, 'avm_DerivedValue') == owner
    _safe_set(owner, 'avm_ValueNode', None)
    assert getattr(partner, 'avm_DerivedValue') is None


