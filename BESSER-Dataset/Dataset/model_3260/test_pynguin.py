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
    Access,
    AccessCategory,
    AccessConnectionEnd,
    AccessType,
    AnnexLibrary,
    AnnexSubclause,
    ArraySize,
    ArrayableElement,
    BasicProperty,
    BehavioralFeature,
    BehavioredImplementation,
    Bus,
    BusClassifier,
    CallContext,
    CallSpecification,
    CalledSubprogram,
    Classifier,
    ClassifierFeature,
    ComponentCategory,
    ComponentClassifier,
    ComponentImplementation,
    ComponentPrototypeActual,
    ComponentType,
    Connection,
    ConnectionEnd,
    ConnectionKind,
    ContainedNamedElement,
    Context,
    Data,
    DataClassifier,
    Device,
    DeviceClassifier,
    DirectedFeature,
    DirectedRelationship,
    DirectionType,
    Element,
    EndToEndFlowElement,
    Enum,
    EnumerationLiteral,
    EnumerationType,
    Feature,
    FeatureConnectionEnd,
    FeatureGroupConnectionEnd,
    FeatureGroupPrototypeActual,
    FeaturePrototypeActual,
    Flow,
    FlowElement,
    FlowKind,
    Generalization_,
    Memory,
    MemoryClassifier,
    ModalElement,
    ModalPath,
    ModeFeature,
    ModeTransitionTrigger,
    NamedElement,
    Namespace,
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
    Processor,
    ProcessorClassifier,
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
    Subprogram,
    SubprogramClassifier,
    SubprogramGroup,
    SubprogramGroupClassifier,
    System,
    SystemClassifier,
    Thread,
    ThreadClassifier,
    ThreadGroup,
    ThreadGroupClassifier,
    Type,
    TypedElement,
    VirtualBus,
    VirtualBusClassifier,
    VirtualProcessor,
    VirtualProcessorClassifier,
    aadl2_AadlBoolean,
    aadl2_AadlInteger,
    aadl2_AadlPackage,
    aadl2_AadlReal,
    aadl2_AadlString,
    aadl2_Abstract,
    aadl2_AbstractClassifier,
    aadl2_AbstractFeature,
    aadl2_AbstractImplementation,
    aadl2_AbstractSubcomponent,
    aadl2_AbstractType,
    aadl2_Access,
    aadl2_AccessConnection,
    aadl2_AccessConnectionEnd,
    aadl2_AccessSpecification,
    aadl2_AnnexLibrary,
    aadl2_AnnexSubclause,
    aadl2_ArrayRange,
    aadl2_ArraySize,
    aadl2_ArraySpecification,
    aadl2_ArrayableElement,
    aadl2_BasicProperty,
    aadl2_BasicPropertyAssociation,
    aadl2_BehavioralFeature,
    aadl2_BehavioredImplementation,
    aadl2_BooleanLiteral,
    aadl2_Bus,
    aadl2_BusAccess,
    aadl2_BusClassifier,
    aadl2_BusImplementation,
    aadl2_BusSubcomponent,
    aadl2_BusType,
    aadl2_CallContext,
    aadl2_CallSpecification,
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
    aadl2_ComponentPrototypeReference,
    aadl2_ComponentReference,
    aadl2_ComponentType,
    aadl2_ComponentTypeRename,
    aadl2_ComputedValue,
    aadl2_Connection,
    aadl2_ConnectionEnd,
    aadl2_ConstantValue,
    aadl2_ContainedNamedElement,
    aadl2_ContainmentPathElement,
    aadl2_Context,
    aadl2_Data,
    aadl2_DataAccess,
    aadl2_DataClassifier,
    aadl2_DataImplementation,
    aadl2_DataPort,
    aadl2_DataSubcomponent,
    aadl2_DataType,
    aadl2_DefaultAnnexLibrary,
    aadl2_DefaultAnnexSubclause,
    aadl2_Device,
    aadl2_DeviceClassifier,
    aadl2_DeviceImplementation,
    aadl2_DeviceSubcomponent,
    aadl2_DeviceType,
    aadl2_DirectedFeature,
    aadl2_DirectedRelationship,
    aadl2_Element,
    aadl2_EndToEndFlow,
    aadl2_EndToEndFlowElement,
    aadl2_EnumerationLiteral,
    aadl2_EnumerationType,
    aadl2_EnumerationValue,
    aadl2_EventDataPort,
    aadl2_EventPort,
    aadl2_Feature,
    aadl2_FeatureConnection,
    aadl2_FeatureConnectionEnd,
    aadl2_FeatureGroup,
    aadl2_FeatureGroupConnection,
    aadl2_FeatureGroupConnectionEnd,
    aadl2_FeatureGroupPrototype,
    aadl2_FeatureGroupPrototypeActual,
    aadl2_FeatureGroupPrototypeBinding,
    aadl2_FeatureGroupPrototypeReference,
    aadl2_FeatureGroupReference,
    aadl2_FeatureGroupType,
    aadl2_FeatureGroupTypeRename,
    aadl2_FeaturePrototype,
    aadl2_FeaturePrototypeActual,
    aadl2_FeaturePrototypeBinding,
    aadl2_FeaturePrototypeReference,
    aadl2_Flow,
    aadl2_FlowElement,
    aadl2_FlowImplementation,
    aadl2_FlowSpecification,
    aadl2_Generalization_,
    aadl2_GlobalNamespace,
    aadl2_GroupExtension,
    aadl2_ImplementationExtension,
    aadl2_IntegerLiteral,
    aadl2_InternalEvent,
    aadl2_ListValue,
    aadl2_Memory,
    aadl2_MemoryClassifier,
    aadl2_MemoryImplementation,
    aadl2_MemorySubcomponent,
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
    aadl2_NamedElement,
    aadl2_Namespace,
    aadl2_NumberType,
    aadl2_NumberValue,
    aadl2_Numeral,
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
    aadl2_PortSpecification,
    aadl2_PrivatePackageSection,
    aadl2_Process,
    aadl2_ProcessClassifier,
    aadl2_ProcessImplementation,
    aadl2_ProcessSubcomponent,
    aadl2_ProcessType,
    aadl2_Processor,
    aadl2_ProcessorCall,
    aadl2_ProcessorClassifier,
    aadl2_ProcessorImplementation,
    aadl2_ProcessorPort,
    aadl2_ProcessorSubcomponent,
    aadl2_ProcessorSubprogram,
    aadl2_ProcessorType,
    aadl2_Property,
    aadl2_PropertyAssociation,
    aadl2_PropertyConstant,
    aadl2_PropertyExpression,
    aadl2_PropertyOwner,
    aadl2_PropertyReference,
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
    aadl2_SubcomponentFlow,
    aadl2_Subprogram,
    aadl2_SubprogramAccess,
    aadl2_SubprogramCall,
    aadl2_SubprogramCallSequence,
    aadl2_SubprogramClassifier,
    aadl2_SubprogramGroup,
    aadl2_SubprogramGroupAccess,
    aadl2_SubprogramGroupClassifier,
    aadl2_SubprogramGroupImplementation,
    aadl2_SubprogramGroupSubcomponent,
    aadl2_SubprogramGroupType,
    aadl2_SubprogramImplementation,
    aadl2_SubprogramSubcomponent,
    aadl2_SubprogramType,
    aadl2_System,
    aadl2_SystemClassifier,
    aadl2_SystemImplementation,
    aadl2_SystemSubcomponent,
    aadl2_SystemType,
    aadl2_Thread,
    aadl2_ThreadClassifier,
    aadl2_ThreadGroup,
    aadl2_ThreadGroupClassifier,
    aadl2_ThreadGroupImplementation,
    aadl2_ThreadGroupSubcomponent,
    aadl2_ThreadGroupType,
    aadl2_ThreadImplementation,
    aadl2_ThreadSubcomponent,
    aadl2_ThreadType,
    aadl2_TriggerPort,
    aadl2_Type,
    aadl2_TypeExtension,
    aadl2_TypedElement,
    aadl2_UnitLiteral,
    aadl2_UnitValue,
    aadl2_UnitsType,
    aadl2_VirtualBus,
    aadl2_VirtualBusClassifier,
    aadl2_VirtualBusImplementation,
    aadl2_VirtualBusSubcomponent,
    aadl2_VirtualBusType,
    aadl2_VirtualProcessor,
    aadl2_VirtualProcessorClassifier,
    aadl2_VirtualProcessorImplementation,
    aadl2_VirtualProcessorSubcomponent,
    aadl2_VirtualProcessorType,
    abstractmethod,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = lambda *args, **kwargs: True
    var_1 = python_code_.aadl2_Prototype(
        aadl2_Prototype57=var_0, aadl2_Prototype139=var_0
    )
    assert isinstance(var_1, python_code_.aadl2_Prototype)
    var_1.categoryConstraint(
        aadl2_diagnostics=None, aadl2_context=complex(-1557.0373487, -2878.4)
    )
    var_7 = "@ff^o1py~R7+V"
    var_8 = python_code_.aadl2_FeatureGroup(inverse=var_7)
    assert isinstance(var_8, python_code_.aadl2_FeatureGroup)
    var_12 = python_code_.aadl2_Element()
    python_code_.aadl2_Element(owner=None, ownedElement=var_12, aadl2_Element55=True)


@pytest.mark.xfail(strict=True)
def test_1():
    var_3 = ""
    var_4 = python_code_.aadl2_DefaultAnnexSubclause(sourceText=var_3)
    assert isinstance(var_4, python_code_.aadl2_DefaultAnnexSubclause)
    var_5 = python_code_.aadl2_ThreadGroupImplementation()
    var_9 = "JFy|\t_441nGK:L"
    var_10 = python_code_.aadl2_ProcessorCall(subprogramAccessName=var_9)
    assert isinstance(var_10, python_code_.aadl2_ProcessorCall)
    var_11 = lambda *args, **kwargs: "d:_5CLOjW"
    var_12 = python_code_.aadl2_ClassifierFeature
    python_code_.aadl2_ComponentType(
        features=var_5,
        noFeatures=var_11,
        aadl2_ComponentType153=var_12,
        aadl2_ComponentType177=var_5,
        aadl2_ComponentType399=var_11,
    )


def test_2():
    var_1 = "_aadl2_Connection__aadl2_Connection284"
    var_2 = python_code_.aadl2_NamedElement(name=var_1, qualifiedName=var_1)
    assert isinstance(var_2, python_code_.aadl2_NamedElement)
    var_3 = python_code_.aadl2_ProcessorPort
    var_2.has_no_qualified_name(aadl2_diagnostics=var_3, aadl2_context=var_1)
    var_7 = python_code_.Type()
    var_12 = python_code_.aadl2_Context()
    var_13 = python_code_.aadl2_SubcomponentFlow()
    var_14 = python_code_.aadl2_FlowSpecification(
        kind=True,
        aadl2_FlowSpecification167=var_12,
        aadl2_FlowSpecification170=(),
        aadl2_FlowSpecification173=1,
        aadl2_FlowSpecification277=var_13,
        aadl2_FlowSpecification265=var_7,
    )
    assert isinstance(var_14, python_code_.aadl2_FlowSpecification)


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = "thread.aadl2_SubprogramCallSequence.aadl2_Context288"
    var_1 = python_code_.Subprogram
    var_2 = python_code_.aadl2_RefinableElement()
    python_code_.aadl2_Classifier(
        noPrototypes=var_0,
        noAnnexes="*M\ns4",
        noProperties=[],
        aadl2_Classifier35=var_1,
        aadl2_Classifier61=var_2,
        aadl2_Classifier840=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_4 = lambda *args, **kwargs: True
    var_5 = "aadl2_ThreadType_aadl2_Classifier__aadl2_Classifier25_aadl2_ComponentImplementation__aadl2_ComponentImplementation103"
    var_7 = "J/J+?vYDD\t I\tbt"
    python_code_.aadl2_Classifier(
        noPrototypes=var_7,
        noAnnexes={179.46},
        noProperties=var_5,
        aadl2_Classifier41=var_4,
        aadl2_Classifier35=var_4,
        Classifier48={"C!{b\\ Ht;[": -1096.95},
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.aadl2_AbstractType()
    var_5 = python_code_.SubprogramGroupClassifier()
    var_6 = python_code_.aadl2_VirtualProcessorType()
    var_7 = "aadl2_VirtualBusImplementation"
    var_8 = python_code_.aadl2_BooleanLiteral(value=var_7)
    assert isinstance(var_8, python_code_.aadl2_BooleanLiteral)
    var_10 = lambda *args, **kwargs: [1508]
    var_11 = "aadl2_ConnectionEnd_aadl2_BasicProperty__aadl2_BasicProperty886_aadl2_ComponentImplementation__aadl2_ComponentImplementation297"
    var_12 = 'y;,vn&"'
    var_13 = python_code_.aadl2_NamedElement(
        name=var_6,
        qualifiedName=var_11,
        NamedElement=b"\xb3\xbb\xdc\x8a\xc8\xb3\x19\x89e\xf3\xb5z\x87\x04S\x0f\x06\xb6",
    )
    assert isinstance(var_13, python_code_.aadl2_NamedElement)
    var_14 = var_13.allNamespaces()
    var_15 = python_code_.aadl2_Classifier(
        noPrototypes=var_10,
        noAnnexes=True,
        noProperties=var_7,
        aadl2_Classifier46=var_14,
        aadl2_Classifier840=(True,),
    )
    assert isinstance(var_15, python_code_.aadl2_Classifier)
    var_16 = var_15.inheritedMember()
    var_17 = python_code_.aadl2_Generalization_()
    python_code_.aadl2_Classifier(
        noPrototypes=var_10,
        noAnnexes=var_11,
        noProperties=var_12,
        featuringClassifier=var_14,
        aadl2_Classifier43=var_16,
        aadl2_Classifier32=var_0,
        aadl2_Classifier46=var_0,
        Classifier48=var_17,
        aadl2_Classifier61=var_5,
        aadl2_Classifier840=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_1 = "_aadl2_PackageSection__aadl2_PackageSection347,_aadl2_PropertyAssociation__aadl2_PropertyAssociation,_aadl2_Connection__aadl2_Connection287"
    var_2 = "_aadl2_PackageRename__aadl2_PackageRename384"
    var_3 = "e"
    var_4 = "_aadl2_BasicProperty__aadl2_BasicProperty825"
    var_5 = python_code_.aadl2_FeaturePrototypeReference
    var_6 = python_code_.aadl2_NamedElement(
        name=var_4, qualifiedName=var_3, aadl2_NamedElement33=var_5
    )
    assert isinstance(var_6, python_code_.aadl2_NamedElement)
    var_7 = "aadl2_VirtualProcessorType"
    var_8 = python_code_.aadl2_Classifier(
        noPrototypes=var_4,
        noAnnexes=var_7,
        noProperties={-3869.74},
        aadl2_Classifier37=var_2,
        aadl2_Classifier35=var_1,
        Classifier48=var_5,
    )
    assert isinstance(var_8, python_code_.aadl2_Classifier)
    var_9 = var_8.inherit(aadl2_inhs=b"7JQdR\xe5\xc6\xb0\xee\xb8\xe7\xde")
    python_code_.aadl2_PropertyAssociation(
        append={},
        constant=var_3,
        aadl2_PropertyAssociation=var_6,
        aadl2_PropertyAssociation14=2777,
        aadl2_PropertyAssociation18=var_9,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.aadl2_VirtualProcessorClassifier()
    var_1 = python_code_.aadl2_TriggerPort()
    var_3 = python_code_.ThreadGroup()
    var_5 = python_code_.aadl2_ComponentPrototypeActual(
        category=var_1, aadl2_ComponentPrototypeActual=var_0
    )
    assert isinstance(var_5, python_code_.aadl2_ComponentPrototypeActual)
    var_6 = python_code_.aadl2_TypeExtension()
    var_8 = python_code_.aadl2_ContainmentPathElement
    var_9 = python_code_.aadl2_Element(aadl2_Element55=var_8, aadl2_Element50=var_8)
    assert isinstance(var_9, python_code_.aadl2_Element)
    python_code_.aadl2_Element(Element=var_3, Element4=var_9, aadl2_Element53=var_6)


@pytest.mark.xfail(strict=True)
def test_8():
    var_8 = python_code_.aadl2_CalledSubprogram()
    var_10 = "_aadl2_PackageSection__aadl2_PackageSection339"
    var_11 = python_code_.aadl2_DirectedRelationship()
    var_12 = python_code_.aadl2_Element(aadl2_Element53=var_11)
    assert isinstance(var_12, python_code_.aadl2_Element)
    var_12.not_own_self(aadl2_context=var_8, aadl2_diagnostics=[True])
    var_12.allOwnedElements()
    var_15 = python_code_.aadl2_Namespace()
    python_code_.aadl2_NamedElement(
        name=var_10,
        qualifiedName=(-3111.61, 3, 233.93),
        ownedMember=var_15,
        aadl2_NamedElement10=complex(-1914.946, 2865.1),
    )


def test_9():
    var_1 = python_code_.aadl2_DirectedRelationship()
    var_2 = python_code_.aadl2_Element(aadl2_Element50=var_1)
    assert isinstance(var_2, python_code_.aadl2_Element)
    var_2.not_own_self(aadl2_context=[], aadl2_diagnostics=var_2)
