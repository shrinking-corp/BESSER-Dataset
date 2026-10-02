#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AnalysisConstruct,
    Axis,
    BoundTypeEnum,
    CADModel,
    CalculationTypeEnum,
    Connector,
    ConnectorCompositionTarget,
    ConnectorFeature,
    Container,
    ContainerFeature,
    ContainerInstanceBase,
    CustomGeometryInput,
    CustomGeometryInputOperationEnum,
    DataTypeEnum,
    Datum,
    DesignDomainFeature,
    DesignSpaceContainer,
    DimensionTypeEnum,
    DirectionalityEnum,
    DistributionRestriction,
    DoDDistributionStatementEnum,
    DomainMapping,
    DomainModelMetric,
    DomainModelParameter,
    DomainModelPort,
    DomainModel_,
    Enum,
    FileFormat,
    FileReference,
    Formula,
    FunctionEnum,
    Geometry,
    Geometry2D,
    Geometry3D,
    GeometryQualifierEnum,
    GlobalConstraintTypeEnum,
    IntervalMethod,
    JobManagerToolSelection,
    KinematicJointSpec,
    LayerEnum,
    LayerRangeEnum,
    Limit,
    Metric,
    ModelType,
    Parameter,
    PartIntersectionEnum,
    PcbLayoutConstraint,
    Pin,
    Plane,
    PlaneReference,
    Point,
    PointReference,
    Port,
    PortDirectionality,
    PortMapTarget,
    ProbabilisticValue,
    Property,
    RFPort,
    RangeConstraintTypeEnum,
    Redeclare,
    RedeclareTypeEnum,
    RelativeLayerEnum,
    RelativeRotationEnum,
    RotationEnum,
    SchematicModel,
    Settings,
    SimpleFormulaOperation,
    SystemCDataTypeEnum,
    SystemCPort,
    TestBenchValueBase,
    ValueExpressionType,
    ValueNode,
    WorkflowTaskBase,
    abstractmethod,
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
    avm_ContainerFeature,
    avm_ContainerInstanceBase,
    avm_DataSource,
    avm_DerivedValue,
    avm_Design,
    avm_DesignDomainFeature,
    avm_DesignSpaceContainer,
    avm_DistributionRestriction,
    avm_DoDDistributionStatement,
    avm_DomainMapping,
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
    avm_domainmapping_CAD2EDATransform,
    avm_eda_CircuitLayout,
    avm_eda_EDAModel,
    avm_eda_ExactLayoutConstraint,
    avm_eda_GlobalLayoutConstraintException,
    avm_eda_Parameter,
    avm_eda_PcbLayoutConstraint,
    avm_eda_RangeLayoutConstraint,
    avm_eda_RelativeLayoutConstraint,
    avm_eda_RelativeRangeLayoutConstraint,
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
    avm_rf_RFModel,
    avm_rf_RFPort,
    avm_schematic_Pin,
    avm_schematic_SchematicModel,
    avm_spice_Parameter,
    avm_spice_SPICEModel,
    avm_systemc_Parameter,
    avm_systemc_SystemCModel,
    avm_systemc_SystemCPort,
    cad_avm_ComponentInstance,
    cad_avm_Value,
    date,
    datetime,
    eda_EDAModel,
    eda_Parameter,
    eda_avm_ComponentInstance,
    eda_avm_Container,
    eda_avm_Value,
    manufacturing_avm_Value,
    modelica_avm_Value,
    spice_Parameter,
    spice_avm_Value,
    systemc_avm_Value,
    time,
)


def test_0():
    var_0 = python_code_.Parameter()
    var_6 = python_code_.ValueExpressionType()
    var_7 = python_code_.Redeclare
    var_8 = "y\x0ci!\\C3se#Y[\t;J"
    var_9 = python_code_.avm_Port(
        Notes=var_7,
        XPosition=var_8,
        Definition=-3184.95,
        YPosition=var_8,
        Name=var_8,
        avm_Port85=var_0,
    )
    assert isinstance(var_9, python_code_.avm_Port)
    var_11 = python_code_.DomainModelPort()
    var_12 = "_avm_cad_CADModel__avm_cad_CADModel"
    var_13 = "a\x0cCYJ<"
    var_14 = "o2>"
    var_15 = python_code_.avm_schematic_Pin(
        EDASymbolLocationY=var_12,
        EDASymbolRotation=var_12,
        SPICEPortNumber=var_13,
        EDAGate=var_8,
        EDASymbolLocationX=var_14,
    )
    assert isinstance(var_15, python_code_.avm_schematic_Pin)
    var_20 = "avm_Resource19-avm_ValueNode124-reset_sync"
    var_21 = python_code_.avm_eda_PcbLayoutConstraint(
        XPosition=var_20, YPosition=var_8, Notes={True, True}
    )
    assert isinstance(var_21, python_code_.avm_eda_PcbLayoutConstraint)
    var_22 = "0.!QjFKV"
    var_23 = python_code_.avm_DistributionRestriction(Notes=var_22)
    assert isinstance(var_23, python_code_.avm_DistributionRestriction)
    var_24 = "|0@iI)l'7\n83"
    var_25 = python_code_.avm_eda_RelativeRangeLayoutConstraint(
        XRelativeRangeMin=var_24,
        XRelativeRangeMax=var_11,
        YRelativeRangeMin=var_6,
        YRelativeRangeMax=var_8,
        RelativeLayer=[],
        avm_eda_RelativeRangeLayoutConstraint278=var_6,
    )
    assert isinstance(var_25, python_code_.avm_eda_RelativeRangeLayoutConstraint)
    python_code_.avm_ConnectorCompositionTarget(ID=var_12)
    var_30 = set()
    python_code_.avm_DataSource(
        Notes=b"\xa5\x98\x8c\x96\xf6\x01\xeb",
        avm_DataSource=var_7,
        avm_DataSource67=var_30,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_2 = python_code_.KinematicJointSpec()
    var_3 = "<`"
    var_4 = python_code_.avm_InterpreterTask(Parameters=var_2, COMName=var_3)
    assert isinstance(var_4, python_code_.avm_InterpreterTask)
    var_7 = python_code_.avm_ValueExpressionType()
    python_code_.avm_Value(
        DimensionType=True,
        DataType=1423,
        Dimensions={True, 1746},
        Unit=1008,
        avm_Value=var_7,
        avm_Value22=var_7,
    )


def test_2():
    var_0 = python_code_.avm_NormalDistribution()
    python_code_.avm_cad_CustomGeometryInput(Operation=var_0)
    var_4 = python_code_.RangeConstraintTypeEnum.Inclusion
    var_8 = python_code_.avm_spice_SPICEModel(Class=var_4)
    assert isinstance(var_8, python_code_.avm_spice_SPICEModel)
    var_11 = "?&$Z1@0(h/Y,Ic+"
    var_12 = python_code_.avm_modelica_Parameter(Locator=var_11)
    assert isinstance(var_12, python_code_.avm_modelica_Parameter)
    var_16 = "C&XvUS"
    var_17 = "|ng1\n2Xu[^LtcFyn\\"
    var_18 = "Eg.>"
    var_19 = "IntersectionWithReferencedParts _avm_eda_RangeLayoutConstraint__avm_eda_RangeLayoutConstraint265 r0"
    var_20 = python_code_.avm_cad_Plane
    var_21 = "_r)e+pF-R^"
    var_22 = python_code_.avm_modelica_SolverSettings(
        Tolerance=var_16,
        Solver=var_17,
        JobManagerToolSelection=var_18,
        StartTime=None,
        StopTime=var_19,
        IntervalMethod=var_4,
        NumberOfIntervals=var_20,
        IntervalLength=var_21,
        ToolSpecificAnnotations=var_17,
    )
    assert isinstance(var_22, python_code_.avm_modelica_SolverSettings)
    var_23 = python_code_.avm_cad_CADModel(Format="`>wcvsU'SV^3F\r")
    assert isinstance(var_23, python_code_.avm_cad_CADModel)
    var_24 = '*vl"qW+r%E>\x0c:6$\nR'
    var_25 = python_code_.avm_domainmapping_CAD2EDATransform(
        RotationX=-1968.02,
        RotationY=var_19,
        RotationZ=var_20,
        TranslationX=var_17,
        TranslationY=var_24,
        TranslationZ=-763.93,
        ScaleX=var_19,
        ScaleY=set(),
        ScaleZ=var_17,
    )
    assert isinstance(var_25, python_code_.avm_domainmapping_CAD2EDATransform)
    var_26 = python_code_.DomainModelPort()
    var_30 = python_code_.avm_Proprietary(Organization=var_26)
    assert isinstance(var_30, python_code_.avm_Proprietary)


@pytest.mark.xfail(strict=True)
def test_3():
    var_1 = "_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget121:_avm_TestBench__avm_TestBench140"
    var_2 = 'aH!L",=;"Y'
    var_3 = "G[\x0cj_qh\x0b# -O,Fpo),"
    var_4 = python_code_.avm_Component
    var_5 = python_code_.eda_avm_ComponentInstance()
    python_code_.avm_eda_RelativeLayoutConstraint(
        XOffset=var_1,
        YOffset=var_1,
        RelativeLayer=var_2,
        RelativeRotation=var_3,
        avm_eda_RelativeLayoutConstraint=var_4,
        avm_eda_RelativeLayoutConstraint270=var_5,
    )


def test_4():
    var_0 = "O"
    var_1 = python_code_.avm_InterpreterTask(Parameters=var_0, COMName=var_0)
    assert isinstance(var_1, python_code_.avm_InterpreterTask)
    var_2 = "%"
    var_3 = "JXEoMGh\rm|[-FIw"
    var_4 = python_code_.avm_TestBenchValueBase
    var_5 = python_code_.modelica_avm_Value()
    python_code_.avm_modelica_Limit(
        VariableLocator=var_0,
        BoundType=None,
        Name=var_2,
        ToleranceTimeWindow=var_3,
        Notes=var_4,
        avm_modelica_Limit=var_5,
    )


def test_5():
    var_0 = python_code_.PortDirectionality.in_
    var_3 = "zHV7P4"
    var_4 = python_code_.avm_ComponentConnectorInstance(
        IDinComponentModel=var_3, avm_ComponentConnectorInstance=2
    )
    assert isinstance(var_4, python_code_.avm_ComponentConnectorInstance)
    var_5 = lambda *args, **kwargs: []
    python_code_.avm_modelica_Limit(
        VariableLocator=var_5,
        BoundType=False,
        Name=var_3,
        ToleranceTimeWindow=False,
        Notes=var_5,
    )
    var_9 = python_code_.avm_SecurityClassification(Level=var_0)
    assert isinstance(var_9, python_code_.avm_SecurityClassification)


def test_6():
    var_3 = python_code_.TestBenchValueBase
    var_4 = python_code_.avm_Workflow(Name=var_3, avm_Workflow=True)
    var_5 = python_code_.avm_WorkflowTaskBase(Name=var_3, avm_WorkflowTaskBase=var_4)
    assert isinstance(var_5, python_code_.avm_WorkflowTaskBase)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.DomainModel_
    var_1 = "manufacturing_avm_Value"
    var_2 = python_code_.avm_rf_RFPort(Directionality=var_0, NominalImpedance=var_1)
    assert isinstance(var_2, python_code_.avm_rf_RFPort)
    var_3 = python_code_.avm_cad_Metric(Name=False)
    assert isinstance(var_3, python_code_.avm_cad_Metric)
    var_4 = python_code_.avm_InterpreterTask(Parameters=var_0, COMName=var_1)
    assert isinstance(var_4, python_code_.avm_InterpreterTask)
    var_6 = python_code_.avm_CompoundProperty()
    var_7 = "1slPM^O`3vk2T"
    var_8 = python_code_.avm_FixedValue(Value=var_7, Uncertainty=var_2)
    assert isinstance(var_8, python_code_.avm_FixedValue)
    var_9 = python_code_.avm_DistributionRestriction(Notes=var_6)
    assert isinstance(var_9, python_code_.avm_DistributionRestriction)
    var_10 = python_code_.avm_cad_Polygon()
    var_12 = "eda_Parameter-avm_Component4-Either-MustExceedOrEqual"
    var_13 = "T"
    var_14 = python_code_.avm_modelica_SolverSettings(
        Tolerance=var_12,
        Solver=None,
        JobManagerToolSelection=var_1,
        StartTime=var_9,
        StopTime=var_13,
        IntervalMethod=var_1,
        NumberOfIntervals=var_12,
        IntervalLength=var_3,
        ToolSpecificAnnotations=var_10,
    )
    assert isinstance(var_14, python_code_.avm_modelica_SolverSettings)
    var_15 = "Dymola_2014"
    var_16 = "_avm_ValueNode__avm_ValueNode124"
    var_17 = python_code_.avm_Operand(Symbol=var_16)
    python_code_.avm_ValueNode(ID=var_15, avm_ValueNode128=var_17)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.avm_cad_Plane()
    var_2 = "_avm_TestBench__avm_TestBench140 avm_ValueFlowMux _avm_DomainModelMetric__avm_DomainModelMetric"
    python_code_.avm_TestBench(
        Name=var_2, avm_TestBench131=var_2, avm_TestBench133=var_0
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = lambda *args, **kwargs: "e7IMn-^&C3,EXiE@(c"
    python_code_.avm_SimpleFormula(Operation=var_0, avm_SimpleFormula=var_0)
