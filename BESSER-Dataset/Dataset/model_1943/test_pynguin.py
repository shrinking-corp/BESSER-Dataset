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
    Allocations,
    AllocationsContainerA,
    Anatomy,
    AnatomyContainerA,
    Area,
    AreaRestriction,
    AreaSymmetry,
    AttributeA,
    AttributeDefinition,
    AttributeTargetsE,
    AttributeTypesE,
    BoolA,
    BoolNot,
    BoolOperation,
    BoolOperationTypesE,
    Bus,
    BusType,
    Capabilities,
    CapabilitiesContainerA,
    Connection,
    ConnectionAssignment,
    ConnectionAssignmentSegment,
    ConnectionInDuctOrLocationCapability,
    ConnectionRestriction,
    ConnectionType,
    ConnectionTypeRestriction,
    DataTypeA,
    Device,
    DeviceAssignment,
    DeviceInLocationCapability,
    DeviceRestriction,
    DeviceSymmetry,
    DeviceType,
    DeviceTypeDissimilarity,
    DeviceTypeRestriction,
    DeviceTypeSymmetry,
    Duct,
    DuctOpening,
    DuctOpeningDeclaration,
    DuctType,
    EndianessE,
    Enum,
    ExternalOutputLink,
    ExternalTaskLink,
    FailureCondition,
    FaultPropagation,
    Functions,
    FunctionsContainerA,
    Hardware,
    InformationFlow,
    InformationPower,
    Input,
    InputDeclaration,
    InputSegregation,
    IntegretyStateE,
    Io,
    IoDeclaration,
    IoDirectionE,
    IoGroup,
    IoType,
    Library,
    LibraryContainerA,
    Location,
    LocationRestriction,
    LocationSymmetry,
    LocationType,
    Message,
    MessageA,
    MessageOnBusCapability,
    MessageOnConnectionOrDeviceCapability,
    MessageSegment,
    MessageType,
    OaamBaseElementA,
    OperationMode,
    OperationModeReference,
    Output,
    OutputDeclaration,
    OutputIntegrityState,
    Position3D,
    PowerSource,
    PowerSourceRestriction,
    ProvidedInformationA,
    RequiredInformationA,
    Resource,
    ResourceAlternatives,
    ResourceBundle,
    ResourceConsumption,
    ResourceGroup,
    ResourceLink,
    ResourceType,
    ResourceTypeDissimilarity,
    ResourceTypeModifier,
    ResourceTypeModifierLevel,
    ResourceTypeModifierReference,
    Restrictions,
    RestrictionsContainerA,
    Scenario,
    ScenarioContainerA,
    ScenarioParameterA,
    Schedule,
    ScheduledTime,
    SegregationRestriction,
    Signal,
    SignalAssignment,
    SignalAssignmentSegment,
    SignalGroup,
    SignalInMessageCapability,
    SignalOnConnectionOrDeviceCapability,
    SignalToMessageAssignment,
    SignalType,
    Struct,
    Suballocations,
    Subanatomy,
    Subcapabilities,
    SubconnectionAssignment,
    SubconnectionInDeviceCapability,
    SubdeviceAssignment,
    SubdeviceInDeviceCapability,
    Subfunctions,
    Subhardware,
    Sublibrary,
    Submessage,
    SubmessageInMessageCapability,
    Subrestrictions,
    Subscenario,
    Subsystem,
    SymmetryTypesE,
    SynchronicityRestriction,
    System,
    Systems,
    SystemsContainerA,
    Task,
    TaskAssignment,
    TaskAtomicRestriction,
    TaskGroup,
    TaskInputState,
    TaskInputTrigger,
    TaskOnDeviceCapability,
    TaskOutputTrigger,
    TaskParameter,
    TaskParameterDeclaration,
    TaskRedundancy,
    TaskStateDeclaration,
    TaskSymmetry,
    TaskSymmetryRestriction,
    TaskType,
    TaskTypeDissimilarity,
    TimeDelayRestriction,
    Variant,
    WireType,
    abstractmethod,
    allocations_AllocationsContainerA,
    anatomy_AnatomyContainerA,
    capabilities_CapabilitiesContainerA,
    capabilities_CapabilityA,
    common_BoolA,
    common_OaamBaseElementA,
    date,
    datetime,
    hardware_HardwareContainerA,
    library_ResourceConsumerA,
    library_ResourceProviderA,
    library_ResourceProviderInstanceA,
    oaam_Architecture,
    oaam_allocations_Allocations,
    oaam_allocations_AllocationsContainerA,
    oaam_allocations_ConnectionAssignment,
    oaam_allocations_ConnectionAssignmentSegment,
    oaam_allocations_DeviceAssignment,
    oaam_allocations_Message,
    oaam_allocations_MessageA,
    oaam_allocations_MessageSegment,
    oaam_allocations_Schedule,
    oaam_allocations_ScheduledTime,
    oaam_allocations_SignalAssignment,
    oaam_allocations_SignalAssignmentSegment,
    oaam_allocations_SignalToMessageAssignment,
    oaam_allocations_Suballocations,
    oaam_allocations_SubconnectionAssignment,
    oaam_allocations_SubdeviceAssignment,
    oaam_allocations_Submessage,
    oaam_allocations_TaskAssignment,
    oaam_anatomy_Anatomy,
    oaam_anatomy_AnatomyContainerA,
    oaam_anatomy_Area,
    oaam_anatomy_AreaSymmetry,
    oaam_anatomy_Duct,
    oaam_anatomy_DuctOpening,
    oaam_anatomy_Location,
    oaam_anatomy_LocationSymmetry,
    oaam_anatomy_Position3D,
    oaam_anatomy_Subanatomy,
    oaam_capabilities_Capabilities,
    oaam_capabilities_CapabilitiesContainerA,
    oaam_capabilities_CapabilityA,
    oaam_capabilities_ConnectionInDuctOrLocationCapability,
    oaam_capabilities_DeviceInLocationCapability,
    oaam_capabilities_MessageOnBusCapability,
    oaam_capabilities_MessageOnConnectionOrDeviceCapability,
    oaam_capabilities_ResourceConsumption,
    oaam_capabilities_SignalInMessageCapability,
    oaam_capabilities_SignalOnConnectionOrDeviceCapability,
    oaam_capabilities_Subcapabilities,
    oaam_capabilities_SubconnectionInDeviceCapability,
    oaam_capabilities_SubdeviceInDeviceCapability,
    oaam_capabilities_SubmessageInMessageCapability,
    oaam_capabilities_TaskOnDeviceCapability,
    oaam_common_Array,
    oaam_common_AttributeA,
    oaam_common_AttributeContainment,
    oaam_common_AttributeNumeric,
    oaam_common_AttributeReference,
    oaam_common_AttributeString,
    oaam_common_BoolA,
    oaam_common_BoolNot,
    oaam_common_BoolOperation,
    oaam_common_Boolean,
    oaam_common_Byte,
    oaam_common_Character,
    oaam_common_DataTypeA,
    oaam_common_FloatingPoint,
    oaam_common_Integer,
    oaam_common_OaamBaseElementA,
    oaam_common_Struct,
    oaam_functions_ExternalOutputLink,
    oaam_functions_ExternalTaskLink,
    oaam_functions_FailureCondition,
    oaam_functions_Functions,
    oaam_functions_FunctionsContainerA,
    oaam_functions_Input,
    oaam_functions_Output,
    oaam_functions_OutputIntegrityState,
    oaam_functions_Signal,
    oaam_functions_SignalGroup,
    oaam_functions_Subfunctions,
    oaam_functions_Task,
    oaam_functions_TaskGroup,
    oaam_functions_TaskParameter,
    oaam_functions_TaskRedundancy,
    oaam_functions_TaskSymmetry,
    oaam_hardware_Bus,
    oaam_hardware_Connection,
    oaam_hardware_Device,
    oaam_hardware_DeviceSymmetry,
    oaam_hardware_Hardware,
    oaam_hardware_HardwareContainerA,
    oaam_hardware_Io,
    oaam_hardware_Subhardware,
    oaam_library_AttributeDefinition,
    oaam_library_BusType,
    oaam_library_ConnectionType,
    oaam_library_DeviceType,
    oaam_library_DeviceTypeDissimilarity,
    oaam_library_DeviceTypeSymmetry,
    oaam_library_DuctOpeningDeclaration,
    oaam_library_DuctType,
    oaam_library_FaultPropagation,
    oaam_library_InputDeclaration,
    oaam_library_IoDeclaration,
    oaam_library_IoGroup,
    oaam_library_IoType,
    oaam_library_Library,
    oaam_library_LibraryContainerA,
    oaam_library_LocationType,
    oaam_library_MessageType,
    oaam_library_OutputDeclaration,
    oaam_library_PowerSource,
    oaam_library_Resource,
    oaam_library_ResourceAlternatives,
    oaam_library_ResourceBundle,
    oaam_library_ResourceConsumerA,
    oaam_library_ResourceGroup,
    oaam_library_ResourceLink,
    oaam_library_ResourceProviderA,
    oaam_library_ResourceProviderInstanceA,
    oaam_library_ResourceType,
    oaam_library_ResourceTypeDissimilarity,
    oaam_library_ResourceTypeModifier,
    oaam_library_ResourceTypeModifierLevel,
    oaam_library_ResourceTypeModifierReference,
    oaam_library_SignalType,
    oaam_library_Sublibrary,
    oaam_library_TaskInputState,
    oaam_library_TaskInputTrigger,
    oaam_library_TaskOutputTrigger,
    oaam_library_TaskParameterDeclaration,
    oaam_library_TaskStateDeclaration,
    oaam_library_TaskType,
    oaam_library_TaskTypeDissimilarity,
    oaam_library_WireType,
    oaam_restrictions_AreaRestriction,
    oaam_restrictions_ConnectionRestriction,
    oaam_restrictions_ConnectionRestrinctionA,
    oaam_restrictions_ConnectionTypeRestriction,
    oaam_restrictions_DeviceRestriction,
    oaam_restrictions_DeviceRestrictionA,
    oaam_restrictions_DeviceTypeRestriction,
    oaam_restrictions_LocationRestriction,
    oaam_restrictions_PowerSourceRestriction,
    oaam_restrictions_Restrictions,
    oaam_restrictions_RestrictionsContainerA,
    oaam_restrictions_SegregationRestriction,
    oaam_restrictions_SignalGroupRestrictionA,
    oaam_restrictions_SignalRestrictionA,
    oaam_restrictions_SubfunctionRestrictionA,
    oaam_restrictions_Subrestrictions,
    oaam_restrictions_SynchronicityRestriction,
    oaam_restrictions_TaskAtomicRestriction,
    oaam_restrictions_TaskGroupRestrictionA,
    oaam_restrictions_TaskRestrictionA,
    oaam_restrictions_TaskSymmetryRestriction,
    oaam_restrictions_TimeDelayRestriction,
    oaam_scenario_ModeDependentElementA,
    oaam_scenario_OperationMode,
    oaam_scenario_OperationModeReference,
    oaam_scenario_Scenario,
    oaam_scenario_ScenarioContainerA,
    oaam_scenario_ScenarioParameterA,
    oaam_scenario_ScenarioParameterBool,
    oaam_scenario_ScenarioParameterNumeric,
    oaam_scenario_Subscenario,
    oaam_scenario_Variant,
    oaam_scenario_VariantDependentElementA,
    oaam_systems_ElectricPower,
    oaam_systems_HydraulicPower,
    oaam_systems_InformationFlow,
    oaam_systems_InformationMaterial,
    oaam_systems_InformationPower,
    oaam_systems_InformationSignal,
    oaam_systems_InputSegregation,
    oaam_systems_LinearPower,
    oaam_systems_ProvidedInformationA,
    oaam_systems_RequiredInformationA,
    oaam_systems_RotaryPower,
    oaam_systems_Subsystem,
    oaam_systems_System,
    oaam_systems_Systems,
    oaam_systems_SystemsContainerA,
    restrictions_ConnectionRestrinctionA,
    restrictions_DeviceRestrictionA,
    restrictions_RestrictionsContainerA,
    restrictions_SignalGroupRestrictionA,
    restrictions_SignalRestrictionA,
    restrictions_SubfunctionRestrictionA,
    restrictions_TaskGroupRestrictionA,
    restrictions_TaskRestrictionA,
    scenario_ModeDependentElementA,
    scenario_ScenarioParameterA,
    scenario_VariantDependentElementA,
    systems_ProvidedInformationA,
    systems_RequiredInformationA,
    systems_SystemsContainerA,
    time,
)


def test_0():
    var_0 = python_code_.oaam_allocations_Schedule
    var_1 = "{3dj@>]VJVv"
    var_2 = "Z%{h2xK?\tbv[\x0cD%H5"
    var_3 = python_code_.oaam_library_InputDeclaration(
        unit="_oaam_common_Struct__oaam_common_Struct",
        precondition=var_1,
        range=var_2,
        lowerBound=var_1,
        upperBound=var_2,
        oaam_library_InputDeclaration=b"j!\xfc\xfb\x9f\xa9\xef\xd10",
    )
    assert isinstance(var_3, python_code_.oaam_library_InputDeclaration)
    var_4 = 1712
    var_5 = python_code_.oaam_allocations_SignalToMessageAssignment(
        position=var_4, oaam_allocations_SignalToMessageAssignment730=var_2
    )
    assert isinstance(var_5, python_code_.oaam_allocations_SignalToMessageAssignment)
    var_6 = python_code_.oaam_common_FloatingPoint(
        nBits=var_0,
        endianess=var_1,
        DataTypeA134=var_3,
        DataTypeA32=var_0,
        DataTypeA734=var_5,
        DataTypeA198=True,
    )
    assert isinstance(var_6, python_code_.oaam_common_FloatingPoint)
    var_12 = python_code_.Input()
    var_13 = 3072.48
    var_14 = python_code_.oaam_systems_LinearPower(force=var_13, velocity=var_4)
    assert isinstance(var_14, python_code_.oaam_systems_LinearPower)
    var_26 = 507
    var_27 = python_code_.oaam_allocations_AllocationsContainerA
    var_28 = python_code_.oaam_common_Struct(
        alignment=var_0, isAbstract=var_12, DataTypeA134=var_3, DataTypeA114=var_27
    )
    assert isinstance(var_28, python_code_.oaam_common_Struct)
    var_34 = "BA0oWK"
    var_35 = python_code_.Subrestrictions
    var_36 = python_code_.oaam_library_OutputDeclaration(
        unit="K2?O*[I#x",
        postcondition=var_34,
        range=var_1,
        lowerBound=var_26,
        upperBound=var_35,
    )
    assert isinstance(var_36, python_code_.oaam_library_OutputDeclaration)
    var_39 = "~EdecL"
    var_40 = python_code_.oaam_restrictions_ConnectionRestriction(
        connectionName=var_39, isForbidden=var_35
    )
    assert isinstance(var_40, python_code_.oaam_restrictions_ConnectionRestriction)


def test_1():
    var_0 = -63
    var_1 = python_code_.oaam_allocations_SignalToMessageAssignment(
        position=var_0, oaam_allocations_SignalToMessageAssignment=var_0
    )
    assert isinstance(var_1, python_code_.oaam_allocations_SignalToMessageAssignment)
    var_9 = True
    var_10 = 438
    var_11 = "fN']qPf$\x0cv)"
    var_12 = python_code_.oaam_library_Resource
    var_13 = "Output306"
    var_14 = "BoolNot192._oaam_allocations_Submessage__oaam_allocations_Submessage._oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction593.DUCT_TYPE"
    var_15 = -3231
    var_16 = python_code_.oaam_library_OutputDeclaration(
        unit=var_13,
        postcondition={},
        range=var_14,
        lowerBound=var_10,
        upperBound=var_15,
    )
    assert isinstance(var_16, python_code_.oaam_library_OutputDeclaration)
    var_17 = python_code_.oaam_library_LibraryContainerA()
    var_18 = python_code_.oaam_library_TaskStateDeclaration()
    var_19 = python_code_.oaam_common_Integer(
        signed=var_9,
        nBits=var_10,
        endianess=var_11,
        DataTypeA213=var_12,
        DataTypeA138=var_16,
        DataTypeA48=var_17,
        DataTypeA198=var_18,
    )
    assert isinstance(var_19, python_code_.oaam_common_Integer)
    var_21 = python_code_.oaam_library_ResourceAlternatives()
    var_29 = python_code_.oaam_capabilities_SignalOnConnectionOrDeviceCapability(
        worstCaseTransmissionTime=var_21
    )
    assert isinstance(
        var_29, python_code_.oaam_capabilities_SignalOnConnectionOrDeviceCapability
    )
    var_31 = 1439.79
    var_32 = python_code_.oaam_allocations_ScheduledTime(
        cycle=var_17, startTime=var_21, duration=var_31, restart=4021
    )
    assert isinstance(var_32, python_code_.oaam_allocations_ScheduledTime)


def test_2():
    var_1 = python_code_.oaam_systems_InformationFlow()
    var_2 = python_code_.oaam_scenario_ScenarioParameterNumeric(value=var_1)
    assert isinstance(var_2, python_code_.oaam_scenario_ScenarioParameterNumeric)
    var_6 = 414.17
    var_7 = python_code_.oaam_restrictions_TimeDelayRestriction(delay=var_6)
    assert isinstance(var_7, python_code_.oaam_restrictions_TimeDelayRestriction)
    var_15 = python_code_.oaam_restrictions_DeviceRestriction(
        deviceName=False, isForbidden=-744.09
    )
    assert isinstance(var_15, python_code_.oaam_restrictions_DeviceRestriction)
    var_22 = 2801
    var_23 = python_code_.oaam_common_Array(
        nElements=-4557, alignment=var_22, DataTypeA734=-1309
    )
    assert isinstance(var_23, python_code_.oaam_common_Array)


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = True
    var_1 = "_oaam_anatomy_Duct__oaam_anatomy_Duct414:Resource487"
    var_2 = python_code_.oaam_library_ResourceType(
        isDistinguishable=(),
        isPropagated=var_0,
        direction=var_1,
        isIo=(-1589.14, 1169.03),
        isConfigurable=var_0,
        unit=var_0,
        isConsumed=var_0,
    )
    assert isinstance(var_2, python_code_.oaam_library_ResourceType)
    var_10 = python_code_.capabilities_CapabilitiesContainerA()
    var_12 = python_code_.oaam_common_AttributeContainment()
    var_13 = python_code_.oaam_common_AttributeReference()
    var_14 = python_code_.oaam_library_IoType(
        direction=var_0, OaamBaseElementA=var_12, OaamBaseElementA23=var_13
    )
    assert isinstance(var_14, python_code_.oaam_library_IoType)
    var_15 = float
    var_16 = python_code_.MessageType()
    var_17 = {var_16, var_16, var_16, var_16}
    python_code_.oaam_library_BusType(
        mtbf=var_10,
        isSelfManaging=var_15,
        requiresMaster=var_0,
        oaam_library_BusType=1959.69,
        oaam_library_BusType207=var_17,
    )


def test_4():
    var_0 = -2260
    var_1 = python_code_.oaam_allocations_Schedule(
        rate={},
        isPeriodic=b"\x90|}+\xac`@q\x97)\xc9\x05_\x9f;\xefB\x94\xa1",
        priority=var_0,
    )
    assert isinstance(var_1, python_code_.oaam_allocations_Schedule)
    var_2 = "u"
    var_3 = python_code_.AttributeA()
    var_4 = {var_3, var_3}
    var_5 = python_code_.oaam_common_OaamBaseElementA(
        id=var_2,
        name=var_2,
        style=var_2,
        documentation=complex(2913.1065412, 4053.74),
        modified=b"\\\xd6V\x18\r3\x0e\x02\x92\x8a0\xe8U'",
        modifier=-193,
        traceLink=b'!\xec\xa7\xe4@\xee\x1eJh"\xef/\xeb\x14\xe4\x03F',
        oaam_common_OaamBaseElementA=var_4,
    )
    assert isinstance(var_5, python_code_.oaam_common_OaamBaseElementA)
    var_6 = python_code_.oaam_common_AttributeReference()
    var_7 = python_code_.oaam_scenario_ScenarioContainerA()
    var_9 = python_code_.oaam_functions_ExternalOutputLink(filter=var_2)
    assert isinstance(var_9, python_code_.oaam_functions_ExternalOutputLink)
    var_14 = 926.01
    var_15 = python_code_.oaam_scenario_OperationModeReference(
        activeProbability=var_14,
        OaamBaseElementA=(
            1,
            -947.73,
            "_oaam_common_BoolOperation__oaam_common_BoolOperation",
        ),
    )
    assert isinstance(var_15, python_code_.oaam_scenario_OperationModeReference)
    var_28 = python_code_.OaamBaseElementA()
    var_31 = python_code_.oaam_capabilities_Subcapabilities
    var_32 = python_code_.oaam_library_InputDeclaration(
        unit=var_31,
        precondition=var_6,
        range=var_2,
        lowerBound=var_0,
        upperBound=complex(-1603.9, 2421.252),
        OaamBaseElementA23=var_6,
    )
    assert isinstance(var_32, python_code_.oaam_library_InputDeclaration)
    var_33 = python_code_.oaam_library_LibraryContainerA()
    var_34 = python_code_.oaam_common_Struct(
        alignment=var_0,
        isAbstract=None,
        DataTypeA134=var_32,
        DataTypeA138={True},
        DataTypeA32=var_28,
        DataTypeA48=var_33,
        DataTypeA198=(),
    )
    assert isinstance(var_34, python_code_.oaam_common_Struct)
    var_35 = python_code_.oaam_library_MessageType(
        minLength=(True,),
        maxLength={
            "_oaam_restrictions_TimeDelayRestriction__oaam_restrictions_TimeDelayRestriction": 1171.46,
            "V": 1,
        },
        alignment=var_31,
        oaam_library_MessageType212=var_34,
    )
    assert isinstance(var_35, python_code_.oaam_library_MessageType)
    var_43 = python_code_.oaam_capabilities_MessageOnConnectionOrDeviceCapability(
        worstCaseTransmissionTime=var_14,
        oaam_capabilities_MessageOnConnectionOrDeviceCapability=var_7,
        oaam_capabilities_MessageOnConnectionOrDeviceCapability502=var_3,
    )
    assert isinstance(
        var_43, python_code_.oaam_capabilities_MessageOnConnectionOrDeviceCapability
    )
    var_45 = "ResourceType122"
    var_46 = python_code_.oaam_restrictions_DeviceRestriction(
        deviceName=var_45, isForbidden={}
    )
    assert isinstance(var_46, python_code_.oaam_restrictions_DeviceRestriction)


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = python_code_.oaam_library_ResourceProviderA()
    var_3 = python_code_.oaam_capabilities_SubconnectionInDeviceCapability()
    var_6 = python_code_.oaam_allocations_DeviceAssignment()
    var_8 = python_code_.oaam_systems_HydraulicPower(pressure=var_3, massFlowRate=var_6)
    assert isinstance(var_8, python_code_.oaam_systems_HydraulicPower)
    var_10 = python_code_.oaam_anatomy_Location(
        length=var_1, oaam_anatomy_Location403=False
    )
    assert isinstance(var_10, python_code_.oaam_anatomy_Location)
    var_12 = "jQSR"
    var_13 = python_code_.oaam_library_IoType(direction=var_12, OaamBaseElementA=False)
    assert isinstance(var_13, python_code_.oaam_library_IoType)
    var_15 = True
    var_16 = -1690.68
    var_17 = python_code_.TaskStateDeclaration()
    var_18 = {var_17}
    var_19 = tuple
    python_code_.oaam_library_TaskType(
        isDeterministic=var_15,
        preferredExecutionRate=var_16,
        oaam_library_TaskType108=b"\xf3\xac\xb6",
        oaam_library_TaskType110=var_18,
        oaam_library_TaskType112=var_19,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_1 = python_code_.oaam_allocations_MessageSegment()
    var_2 = 3024.63
    var_3 = "~8e\x0cjv:'o%U"
    var_4 = lambda *args, **kwargs: []
    var_5 = python_code_.oaam_systems_InformationSignal(
        accuracy=var_1, resolution=var_2, unit=var_3, rate=var_4, latency=var_2
    )
    assert isinstance(var_5, python_code_.oaam_systems_InformationSignal)
    var_6 = python_code_.IoDeclaration()
    var_7 = python_code_.TaskStateDeclaration()
    var_14 = 4318.95
    var_15 = False
    python_code_.oaam_library_BusType(
        mtbf=var_14,
        isSelfManaging=var_7,
        requiresMaster=var_15,
        oaam_library_BusType207=var_6,
    )


def test_7():
    var_1 = 1828
    var_2 = python_code_.oaam_functions_Subfunctions(
        multiplicityMin=(378,), multiplicityMax=var_1
    )
    assert isinstance(var_2, python_code_.oaam_functions_Subfunctions)
    var_5 = python_code_.oaam_allocations_SignalAssignment()
    var_6 = python_code_.oaam_anatomy_Subanatomy()
    var_8 = python_code_.oaam_common_FloatingPoint
    var_9 = python_code_.oaam_restrictions_DeviceRestriction(
        deviceName=var_8, isForbidden=var_5
    )
    assert isinstance(var_9, python_code_.oaam_restrictions_DeviceRestriction)
    var_10 = 3248.33
    var_11 = python_code_.oaam_anatomy_Position3D(x=var_10, y=None, z=var_6)
    assert isinstance(var_11, python_code_.oaam_anatomy_Position3D)
    var_12 = python_code_.library_ResourceConsumerA()
    var_15 = python_code_.oaam_scenario_ScenarioParameterNumeric(value=var_12)
    assert isinstance(var_15, python_code_.oaam_scenario_ScenarioParameterNumeric)
    var_16 = python_code_.oaam_common_BoolOperation(type=var_10)
    assert isinstance(var_16, python_code_.oaam_common_BoolOperation)


def test_8():
    var_0 = python_code_.oaam_common_AttributeA()
    var_3 = python_code_.oaam_restrictions_DeviceRestriction(
        deviceName=var_0, isForbidden=-873
    )
    assert isinstance(var_3, python_code_.oaam_restrictions_DeviceRestriction)
    var_7 = python_code_.oaam_library_TaskInputTrigger()
    var_10 = python_code_.oaam_restrictions_TaskSymmetryRestriction(type=var_7)
    assert isinstance(var_10, python_code_.oaam_restrictions_TaskSymmetryRestriction)
    var_13 = python_code_.oaam_common_AttributeContainment()
    var_17 = "l,14755PwV'oL79]:Z"
    var_18 = python_code_.oaam_restrictions_ConnectionRestriction(
        connectionName=var_17, isForbidden={}
    )
    assert isinstance(var_18, python_code_.oaam_restrictions_ConnectionRestriction)
    var_21 = -1023.05
    var_22 = python_code_.oaam_common_AttributeReference()
    var_23 = python_code_.oaam_library_TaskTypeDissimilarity(
        percentageOfCommonCode=var_21, OaamBaseElementA23=var_22
    )
    assert isinstance(var_23, python_code_.oaam_library_TaskTypeDissimilarity)
    var_36 = "Ukc*ey!,"
    var_37 = -1909
    var_38 = python_code_.oaam_library_OutputDeclaration(
        unit=var_36,
        postcondition={"hv0s1j6'&#{k!>$x_l)"},
        range=33,
        lowerBound=var_37,
        upperBound=(),
        OaamBaseElementA=var_13,
    )
    assert isinstance(var_38, python_code_.oaam_library_OutputDeclaration)


def test_9():
    var_5 = 0
    var_6 = "WireType119"
    var_7 = python_code_.oaam_common_FloatingPoint(
        nBits=var_5, endianess=var_6, DataTypeA213=var_6, DataTypeA48=var_5
    )
    assert isinstance(var_7, python_code_.oaam_common_FloatingPoint)
