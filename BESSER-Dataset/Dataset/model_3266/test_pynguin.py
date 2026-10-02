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
    Abstract,
    AbstractClassifier,
    AbstractFeatureClassifier,
    AbstractNamedValue,
    AbstractSubcomponentType,
    Access,
    AccessCategory,
    AccessConnectionEnd,
    AccessType,
    AnnexLibrary,
    AnnexSubclause,
    ArraySizeProperty,
    ArrayableElement,
    BasicProperty,
    BehavioralFeature,
    BehavioredImplementation,
    Bus,
    BusClassifier,
    BusFeatureClassifier,
    BusSubcomponentType,
    CallContext,
    CalledSubprogram,
    Classifier,
    ClassifierFeature,
    ComponentCategory,
    ComponentClassifier,
    ComponentImplementation,
    ComponentPrototype,
    ComponentType,
    Connection,
    ConnectionEnd,
    ContainedNamedElement,
    Context,
    Data,
    DataClassifier,
    DataSubcomponentType,
    Device,
    DeviceClassifier,
    DeviceSubcomponentType,
    DirectedFeature,
    DirectedRelationship,
    DirectionType,
    Element,
    EndToEndFlowElement,
    Enum,
    EnumerationLiteral,
    EnumerationType,
    Feature,
    FeatureClassifier,
    FeatureConnectionEnd,
    FeatureGroupConnectionEnd,
    FeaturePrototypeActual,
    FeatureType,
    Flow,
    FlowElement,
    FlowFeature,
    FlowKind,
    Generalization_,
    InternalFeature,
    Memory,
    MemoryClassifier,
    MemorySubcomponentType,
    ModalElement,
    ModalPath,
    ModeFeature,
    ModelUnit,
    NamedElement,
    Namespace,
    NonListType,
    NumberType,
    NumberValue,
    OperationKind,
    PackageSection,
    ParameterConnectionEnd,
    Port,
    PortCategory,
    PortConnectionEnd,
    Process,
    ProcessClassifier,
    ProcessSubcomponentType,
    Processor,
    ProcessorClassifier,
    ProcessorFeature,
    ProcessorSubcomponentType,
    PropertyExpression,
    PropertyOwner,
    PropertyType,
    PropertyValue,
    Prototype,
    PrototypeBinding,
    RefinableElement,
    Relationship,
    StructuralFeature,
    Subcomponent,
    SubcomponentType,
    Subprogram,
    SubprogramClassifier,
    SubprogramGroup,
    SubprogramGroupClassifier,
    SubprogramGroupSubcomponentType,
    SubprogramSubcomponentType,
    System,
    SystemClassifier,
    SystemSubcomponentType,
    Thread,
    ThreadClassifier,
    ThreadGroup,
    ThreadGroupClassifier,
    ThreadGroupSubcomponentType,
    ThreadSubcomponentType,
    TriggerPort,
    Type,
    TypedElement,
    VirtualBus,
    VirtualBusClassifier,
    VirtualBusSubcomponentType,
    VirtualProcessor,
    VirtualProcessorClassifier,
    VirtualProcessorSubcomponentType,
    aadl2_AadlBoolean,
    aadl2_AadlInteger,
    aadl2_AadlPackage,
    aadl2_AadlReal,
    aadl2_AadlString,
    aadl2_Abstract,
    aadl2_AbstractClassifier,
    aadl2_AbstractFeature,
    aadl2_AbstractFeatureClassifier,
    aadl2_AbstractImplementation,
    aadl2_AbstractNamedValue,
    aadl2_AbstractPrototype,
    aadl2_AbstractSubcomponent,
    aadl2_AbstractSubcomponentType,
    aadl2_AbstractType,
    aadl2_Access,
    aadl2_AccessConnection,
    aadl2_AccessConnectionEnd,
    aadl2_AccessSpecification,
    aadl2_AnnexLibrary,
    aadl2_AnnexSubclause,
    aadl2_ArrayDimension,
    aadl2_ArrayRange,
    aadl2_ArraySize,
    aadl2_ArraySizeProperty,
    aadl2_ArrayableElement,
    aadl2_BasicProperty,
    aadl2_BasicPropertyAssociation,
    aadl2_BehavioralFeature,
    aadl2_BehavioredImplementation,
    aadl2_BooleanLiteral,
    aadl2_Bus,
    aadl2_BusAccess,
    aadl2_BusClassifier,
    aadl2_BusFeatureClassifier,
    aadl2_BusImplementation,
    aadl2_BusPrototype,
    aadl2_BusSubcomponent,
    aadl2_BusSubcomponentType,
    aadl2_BusType,
    aadl2_CallContext,
    aadl2_CalledSubprogram,
    aadl2_Classifier,
    aadl2_ClassifierFeature,
    aadl2_ClassifierType,
    aadl2_ClassifierValue,
    aadl2_Comment,
    aadl2_ComponentClassifier,
    aadl2_ComponentImplementation,
    aadl2_ComponentImplementationReference,
    aadl2_ComponentPrototype,
    aadl2_ComponentPrototypeActual,
    aadl2_ComponentPrototypeBinding,
    aadl2_ComponentType,
    aadl2_ComponentTypeRename,
    aadl2_ComputedValue,
    aadl2_ConnectedElement,
    aadl2_Connection,
    aadl2_ConnectionEnd,
    aadl2_ContainedNamedElement,
    aadl2_ContainmentPathElement,
    aadl2_Context,
    aadl2_Data,
    aadl2_DataAccess,
    aadl2_DataClassifier,
    aadl2_DataImplementation,
    aadl2_DataPort,
    aadl2_DataPrototype,
    aadl2_DataSubcomponent,
    aadl2_DataSubcomponentType,
    aadl2_DataType,
    aadl2_DefaultAnnexLibrary,
    aadl2_DefaultAnnexSubclause,
    aadl2_Device,
    aadl2_DeviceClassifier,
    aadl2_DeviceImplementation,
    aadl2_DevicePrototype,
    aadl2_DeviceSubcomponent,
    aadl2_DeviceSubcomponentType,
    aadl2_DeviceType,
    aadl2_DirectedFeature,
    aadl2_DirectedRelationship,
    aadl2_Element,
    aadl2_EndToEndFlow,
    aadl2_EndToEndFlowElement,
    aadl2_EndToEndFlowSegment,
    aadl2_EnumerationLiteral,
    aadl2_EnumerationType,
    aadl2_EventDataPort,
    aadl2_EventDataSource,
    aadl2_EventPort,
    aadl2_EventSource,
    aadl2_Feature,
    aadl2_FeatureClassifier,
    aadl2_FeatureConnection,
    aadl2_FeatureConnectionEnd,
    aadl2_FeatureGroup,
    aadl2_FeatureGroupConnection,
    aadl2_FeatureGroupConnectionEnd,
    aadl2_FeatureGroupPrototype,
    aadl2_FeatureGroupPrototypeActual,
    aadl2_FeatureGroupPrototypeBinding,
    aadl2_FeatureGroupType,
    aadl2_FeatureGroupTypeRename,
    aadl2_FeaturePrototype,
    aadl2_FeaturePrototypeActual,
    aadl2_FeaturePrototypeBinding,
    aadl2_FeaturePrototypeReference,
    aadl2_FeatureType,
    aadl2_Flow,
    aadl2_FlowElement,
    aadl2_FlowEnd,
    aadl2_FlowFeature,
    aadl2_FlowImplementation,
    aadl2_FlowSegment,
    aadl2_FlowSpecification,
    aadl2_Generalization_,
    aadl2_GlobalNamespace,
    aadl2_GroupExtension,
    aadl2_ImplementationExtension,
    aadl2_IntegerLiteral,
    aadl2_InternalFeature,
    aadl2_ListType,
    aadl2_ListValue,
    aadl2_Memory,
    aadl2_MemoryClassifier,
    aadl2_MemoryImplementation,
    aadl2_MemoryPrototype,
    aadl2_MemorySubcomponent,
    aadl2_MemorySubcomponentType,
    aadl2_MemoryType,
    aadl2_MetaclassReference,
    aadl2_ModalElement,
    aadl2_ModalPath,
    aadl2_ModalPropertyValue,
    aadl2_Mode,
    aadl2_ModeBinding,
    aadl2_ModeFeature,
    aadl2_ModeTransition,
    aadl2_ModeTransitionTrigger,
    aadl2_ModelUnit,
    aadl2_NamedElement,
    aadl2_NamedValue,
    aadl2_Namespace,
    aadl2_NonListType,
    aadl2_NumberType,
    aadl2_NumberValue,
    aadl2_NumericRange,
    aadl2_Operation,
    aadl2_PackageRename,
    aadl2_PackageSection,
    aadl2_Parameter,
    aadl2_ParameterConnection,
    aadl2_ParameterConnectionEnd,
    aadl2_Port,
    aadl2_PortConnection,
    aadl2_PortConnectionEnd,
    aadl2_PortProxy,
    aadl2_PortSpecification,
    aadl2_PrivatePackageSection,
    aadl2_Process,
    aadl2_ProcessClassifier,
    aadl2_ProcessImplementation,
    aadl2_ProcessPrototype,
    aadl2_ProcessSubcomponent,
    aadl2_ProcessSubcomponentType,
    aadl2_ProcessType,
    aadl2_Processor,
    aadl2_ProcessorClassifier,
    aadl2_ProcessorFeature,
    aadl2_ProcessorImplementation,
    aadl2_ProcessorPrototype,
    aadl2_ProcessorSubcomponent,
    aadl2_ProcessorSubcomponentType,
    aadl2_ProcessorType,
    aadl2_Property,
    aadl2_PropertyAssociation,
    aadl2_PropertyConstant,
    aadl2_PropertyExpression,
    aadl2_PropertyOwner,
    aadl2_PropertySet,
    aadl2_PropertyType,
    aadl2_PropertyValue,
    aadl2_Prototype,
    aadl2_PrototypeBinding,
    aadl2_PublicPackageSection,
    aadl2_RangeType,
    aadl2_RangeValue,
    aadl2_RealLiteral,
    aadl2_Realization,
    aadl2_RecordField,
    aadl2_RecordType,
    aadl2_RecordValue,
    aadl2_ReferenceType,
    aadl2_ReferenceValue,
    aadl2_RefinableElement,
    aadl2_Relationship,
    aadl2_StringLiteral,
    aadl2_StructuralFeature,
    aadl2_Subcomponent,
    aadl2_SubcomponentType,
    aadl2_Subprogram,
    aadl2_SubprogramAccess,
    aadl2_SubprogramCall,
    aadl2_SubprogramCallSequence,
    aadl2_SubprogramClassifier,
    aadl2_SubprogramGroup,
    aadl2_SubprogramGroupAccess,
    aadl2_SubprogramGroupClassifier,
    aadl2_SubprogramGroupImplementation,
    aadl2_SubprogramGroupPrototype,
    aadl2_SubprogramGroupSubcomponent,
    aadl2_SubprogramGroupSubcomponentType,
    aadl2_SubprogramGroupType,
    aadl2_SubprogramImplementation,
    aadl2_SubprogramPrototype,
    aadl2_SubprogramProxy,
    aadl2_SubprogramSubcomponent,
    aadl2_SubprogramSubcomponentType,
    aadl2_SubprogramType,
    aadl2_System,
    aadl2_SystemClassifier,
    aadl2_SystemImplementation,
    aadl2_SystemPrototype,
    aadl2_SystemSubcomponent,
    aadl2_SystemSubcomponentType,
    aadl2_SystemType,
    aadl2_Thread,
    aadl2_ThreadClassifier,
    aadl2_ThreadGroup,
    aadl2_ThreadGroupClassifier,
    aadl2_ThreadGroupImplementation,
    aadl2_ThreadGroupPrototype,
    aadl2_ThreadGroupSubcomponent,
    aadl2_ThreadGroupSubcomponentType,
    aadl2_ThreadGroupType,
    aadl2_ThreadImplementation,
    aadl2_ThreadPrototype,
    aadl2_ThreadSubcomponent,
    aadl2_ThreadSubcomponentType,
    aadl2_ThreadType,
    aadl2_TriggerPort,
    aadl2_Type,
    aadl2_TypeExtension,
    aadl2_TypedElement,
    aadl2_UnitLiteral,
    aadl2_UnitsType,
    aadl2_VirtualBus,
    aadl2_VirtualBusClassifier,
    aadl2_VirtualBusImplementation,
    aadl2_VirtualBusPrototype,
    aadl2_VirtualBusSubcomponent,
    aadl2_VirtualBusSubcomponentType,
    aadl2_VirtualBusType,
    aadl2_VirtualProcessor,
    aadl2_VirtualProcessorClassifier,
    aadl2_VirtualProcessorImplementation,
    aadl2_VirtualProcessorPrototype,
    aadl2_VirtualProcessorSubcomponent,
    aadl2_VirtualProcessorSubcomponentType,
    aadl2_VirtualProcessorType,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = 'Y#hfQQ:\t#p\t"Uq,\\'
    var_1 = python_code_.aadl2_ComponentPrototypeActual(
        category=var_0, aadl2_ComponentPrototypeActual=None
    )
    assert isinstance(var_1, python_code_.aadl2_ComponentPrototypeActual)
    var_6 = python_code_.aadl2_ParameterConnectionEnd()
    python_code_.aadl2_UnitLiteral()
    var_16 = python_code_.VirtualProcessorClassifier()
    var_20 = "aadl2_Property18 aadl2_ConnectedElement"
    var_21 = python_code_.aadl2_ContainmentPathElement(
        annexName=(-2021.58,), aadl2_ContainmentPathElement77=var_6
    )
    assert isinstance(var_21, python_code_.aadl2_ContainmentPathElement)
    var_22 = python_code_.aadl2_ArrayRange(
        lowerBound=var_20, upperBound=var_16, aadl2_ArrayRange=var_21
    )
    assert isinstance(var_22, python_code_.aadl2_ArrayRange)
    var_23 = python_code_.aadl2_Namespace()
    var_24 = python_code_.aadl2_DefaultAnnexLibrary(sourceText=var_20)
    assert isinstance(var_24, python_code_.aadl2_DefaultAnnexLibrary)
    var_28 = "FD]l"
    var_29 = python_code_.aadl2_NamedElement(
        qualifiedName=var_22, name=var_28, aadl2_NamedElement48=var_23
    )
    assert isinstance(var_29, python_code_.aadl2_NamedElement)
    var_29.getPropertyValues(aadl2_propertyName=var_24, aadl2_propertySetName=167)


@pytest.mark.xfail(strict=True)
def test_1():
    var_7 = python_code_.aadl2_RealLiteral(value=-2268.57)
    assert isinstance(var_7, python_code_.aadl2_RealLiteral)
    var_13 = python_code_.PropertyType()
    python_code_.aadl2_BehavioredImplementation(
        aadl2_BehavioredImplementation421=var_13
    )


def test_2():
    var_3 = python_code_.aadl2_ModalPath()
    var_4 = var_3.getInModeTransitions()
    var_5 = python_code_.aadl2_BehavioredImplementation(
        aadl2_BehavioredImplementation=var_4
    )
    assert isinstance(var_5, python_code_.aadl2_BehavioredImplementation)
    var_5.subprogramCalls()


def test_3():
    var_4 = python_code_.aadl2_Port(category=1912)
    assert isinstance(var_4, python_code_.aadl2_Port)
    var_5 = python_code_.TriggerPort()
    var_7 = "_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement81:_aadl2_UnitLiteral__aadl2_UnitLiteral:aadl2_PrototypeBinding"
    var_8 = python_code_.aadl2_PackageRename(renameAll=var_7, aadl2_PackageRename=var_5)
    assert isinstance(var_8, python_code_.aadl2_PackageRename)
    var_10 = "aadl2_Classifier:aadl2_ComponentType:_aadl2_ComponentClassifier__aadl2_ComponentClassifier407:_aadl2_FlowSpecification__aadl2_FlowSpecification183"
    var_11 = python_code_.aadl2_IntegerLiteral(base=var_10, value=-343.13)
    assert isinstance(var_11, python_code_.aadl2_IntegerLiteral)
    var_17 = python_code_.aadl2_AnnexLibrary()
    var_18 = python_code_.aadl2_DefaultAnnexLibrary(
        sourceText=var_10, aadl2_DefaultAnnexLibrary=var_17
    )
    assert isinstance(var_18, python_code_.aadl2_DefaultAnnexLibrary)
    python_code_.aadl2_PackageRename(
        renameAll=b"K=W\xfd\xf7\xd6\xcb\xe5\x1dL\xa3\x90m\x91\xceO\xbd"
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.aadl2_ProcessSubcomponentType
    var_1 = "_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement79,aadl2_ComponentPrototype179,aadl2_FeatureGroupType227"
    python_code_.aadl2_ComponentClassifier(
        derivedModes=(), noFlows=var_0, noModes=var_1, aadl2_ComponentClassifier=True
    )


def test_5():
    var_0 = python_code_.aadl2_GroupExtension()
    var_1 = python_code_.aadl2_BusType()
    var_2 = python_code_.aadl2_AadlPackage
    var_3 = "SE7\x0bRw%E6](c;@H"
    var_4 = python_code_.aadl2_ComponentClassifier(
        derivedModes=var_0,
        noFlows=var_2,
        noModes=var_3,
        aadl2_ComponentClassifier180={},
    )
    assert isinstance(var_4, python_code_.aadl2_ComponentClassifier)
    var_7 = python_code_.aadl2_ProcessClassifier()
    var_21 = python_code_.aadl2_ModalPath()
    var_22 = var_21.getAllInModeTransitions()
    var_23 = python_code_.aadl2_Namespace()
    var_24 = python_code_.aadl2_NamedElement(
        qualifiedName=var_7,
        name={2301.75, -694.12, False},
        aadl2_NamedElement=var_22,
        aadl2_NamedElement33=var_21,
        aadl2_NamedElement48=var_23,
        aadl2_NamedElement82=var_1,
    )
    assert isinstance(var_24, python_code_.aadl2_NamedElement)
    var_24.getNamespace()
    var_26 = python_code_.aadl2_StringLiteral(
        value={"'C*Q9uwUnpGT": 494, "aadl2_ComponentPrototype179": True}
    )
    assert isinstance(var_26, python_code_.aadl2_StringLiteral)


def test_6():
    var_3 = ":no\rj,~93ey/uO\x0b$:=R"
    var_4 = "_aadl2_Connection__aadl2_Connection,classifierFeature,_aadl2_Property__aadl2_Property,out"
    var_5 = python_code_.aadl2_ContainedNamedElement()
    var_6 = python_code_.aadl2_ContainmentPathElement(
        annexName=var_4,
        aadl2_ContainmentPathElement=var_5,
        aadl2_ContainmentPathElement83=complex(2127.96, 1595.530866),
    )
    assert isinstance(var_6, python_code_.aadl2_ContainmentPathElement)
    var_7 = python_code_.aadl2_ArrayRange(
        lowerBound=var_3, upperBound=var_3, aadl2_ArrayRange=var_6
    )
    assert isinstance(var_7, python_code_.aadl2_ArrayRange)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = "_aadl2_Mode__aadl2_Mode145-_aadl2_BusAccess__aadl2_BusAccess795-aadl2_ComponentImplementation106"
    var_1 = "aadl2_Element"
    var_2 = python_code_.aadl2_ArrayRange(lowerBound=var_0, upperBound=var_1)
    assert isinstance(var_2, python_code_.aadl2_ArrayRange)
    var_4 = python_code_.aadl2_UnitLiteral()
    var_5 = var_4.getAbsoluteFactor(aadl2_target=var_1)
    python_code_.aadl2_Element(
        aadl2_Element0=var_5, aadl2_Element3=var_2, aadl2_Element60=var_5
    )


def test_8():
    python_code_.aadl2_ProcessSubcomponentType()
