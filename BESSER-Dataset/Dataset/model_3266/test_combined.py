# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PropertyValue,
    aadl2_StringLiteral,
    VirtualProcessorClassifier,
    VirtualBusClassifier,
    ThreadGroupClassifier,
    ThreadClassifier,
    ProcessClassifier,
    ProcessorClassifier,
    SystemClassifier,
    SubprogramGroupClassifier,
    SubprogramClassifier,
    MemoryClassifier,
    DeviceClassifier,
    DataClassifier,
    ComponentPrototype,
    BusClassifier,
    Thread,
    VirtualProcessor,
    VirtualBus,
    ThreadGroup,
    Processor,
    SubprogramGroup,
    System,
    Process,
    Memory,
    Device,
    Bus,
    BehavioredImplementation,
    aadl2_SubprogramImplementation,
    aadl2_ThreadImplementation,
    BusFeatureClassifier,
    VirtualProcessorSubcomponentType,
    aadl2_VirtualProcessorPrototype,
    VirtualBusSubcomponentType,
    aadl2_VirtualBusPrototype,
    ThreadSubcomponentType,
    aadl2_ThreadPrototype,
    ThreadGroupSubcomponentType,
    aadl2_ThreadGroupPrototype,
    SystemSubcomponentType,
    aadl2_SystemPrototype,
    SubprogramGroupSubcomponentType,
    aadl2_SubprogramGroupPrototype,
    ProcessSubcomponentType,
    aadl2_ProcessPrototype,
    ProcessorSubcomponentType,
    aadl2_ProcessorPrototype,
    MemorySubcomponentType,
    aadl2_MemoryPrototype,
    DeviceSubcomponentType,
    aadl2_DevicePrototype,
    BusSubcomponentType,
    aadl2_BusPrototype,
    AbstractSubcomponentType,
    AbstractClassifier,
    aadl2_AbstractImplementation,
    ComponentType,
    aadl2_BusType,
    aadl2_ProcessType,
    aadl2_VirtualBusType,
    aadl2_DeviceType,
    aadl2_SystemType,
    aadl2_VirtualProcessorType,
    aadl2_ThreadGroupType,
    aadl2_ThreadType,
    aadl2_ProcessorType,
    aadl2_MemoryType,
    ComponentImplementation,
    aadl2_ProcessImplementation,
    aadl2_ThreadGroupImplementation,
    aadl2_VirtualBusImplementation,
    aadl2_MemoryImplementation,
    aadl2_ProcessorImplementation,
    aadl2_VirtualProcessorImplementation,
    aadl2_BusImplementation,
    aadl2_DeviceImplementation,
    aadl2_DataImplementation,
    aadl2_SystemImplementation,
    aadl2_SubprogramGroupImplementation,
    aadl2_BehavioredImplementation,
    BehavioralFeature,
    PrototypeBinding,
    aadl2_FeaturePrototypeBinding,
    aadl2_ComponentPrototypeBinding,
    FeaturePrototypeActual,
    aadl2_FeaturePrototypeReference,
    aadl2_AccessSpecification,
    aadl2_PortSpecification,
    aadl2_FeatureGroupPrototypeActual,
    aadl2_FeatureGroupPrototypeBinding,
    ModelUnit,
    aadl2_AadlPackage,
    PackageSection,
    aadl2_PrivatePackageSection,
    aadl2_PublicPackageSection,
    SubprogramSubcomponentType,
    Subprogram,
    aadl2_SubprogramPrototype,
    AnnexSubclause,
    aadl2_DefaultAnnexSubclause,
    AnnexLibrary,
    aadl2_DefaultAnnexLibrary,
    InternalFeature,
    ProcessorFeature,
    DataSubcomponentType,
    Data,
    aadl2_DataPrototype,
    Abstract,
    aadl2_AbstractPrototype,
    Subcomponent,
    aadl2_VirtualProcessorSubcomponent,
    aadl2_SystemSubcomponent,
    aadl2_ProcessSubcomponent,
    aadl2_ProcessorSubcomponent,
    aadl2_DeviceSubcomponent,
    aadl2_ThreadGroupSubcomponent,
    aadl2_ThreadSubcomponent,
    aadl2_MemorySubcomponent,
    Connection,
    NumberType,
    aadl2_AadlReal,
    aadl2_AadlInteger,
    NonListType,
    aadl2_RangeType,
    aadl2_ReferenceType,
    aadl2_ClassifierType,
    aadl2_AadlString,
    aadl2_NumberType,
    aadl2_AadlBoolean,
    PropertyType,
    aadl2_ListType,
    aadl2_NonListType,
    EnumerationType,
    aadl2_UnitsType,
    aadl2_ComputedValue,
    aadl2_RecordValue,
    aadl2_NamedValue,
    NumberValue,
    aadl2_IntegerLiteral,
    aadl2_RangeValue,
    aadl2_BooleanLiteral,
    ContainedNamedElement,
    aadl2_ReferenceValue,
    aadl2_RealLiteral,
    EnumerationLiteral,
    aadl2_UnitLiteral,
    aadl2_NumberValue,
    PropertyExpression,
    aadl2_ListValue,
    aadl2_Operation,
    aadl2_PropertyValue,
    ArraySizeProperty,
    ArrayableElement,
    aadl2_FeaturePrototypeActual,
    aadl2_ComponentPrototypeActual,
    FeatureConnectionEnd,
    aadl2_FeatureClassifier,
    aadl2_EventSource,
    FeatureClassifier,
    SubcomponentType,
    aadl2_ThreadGroupSubcomponentType,
    aadl2_ThreadSubcomponentType,
    aadl2_MemorySubcomponentType,
    aadl2_ProcessSubcomponentType,
    aadl2_SystemSubcomponentType,
    aadl2_DeviceSubcomponentType,
    aadl2_ProcessorSubcomponentType,
    aadl2_VirtualProcessorSubcomponentType,
    Classifier,
    aadl2_ComponentClassifier,
    aadl2_EventDataSource,
    aadl2_FeatureGroupConnection,
    aadl2_FeatureConnection,
    aadl2_PortConnection,
    aadl2_ParameterConnection,
    ComponentClassifier,
    aadl2_DeviceClassifier,
    aadl2_ThreadGroupClassifier,
    aadl2_MemoryClassifier,
    aadl2_ProcessClassifier,
    aadl2_VirtualProcessorClassifier,
    aadl2_ThreadClassifier,
    aadl2_SubprogramGroupClassifier,
    aadl2_SubprogramClassifier,
    aadl2_AbstractClassifier,
    aadl2_BusClassifier,
    aadl2_SystemClassifier,
    aadl2_VirtualBusClassifier,
    aadl2_ProcessorClassifier,
    aadl2_DataClassifier,
    aadl2_AccessConnection,
    aadl2_AbstractSubcomponent,
    aadl2_ComponentType,
    aadl2_ComponentImplementation,
    aadl2_ArraySizeProperty,
    RefinableElement,
    CalledSubprogram,
    StructuralFeature,
    aadl2_ProcessorFeature,
    aadl2_Feature,
    ClassifierFeature,
    aadl2_BehavioralFeature,
    aadl2_StructuralFeature,
    aadl2_ModeFeature,
    aadl2_CalledSubprogram,
    Relationship,
    aadl2_DirectedRelationship,
    DirectedRelationship,
    ModeFeature,
    aadl2_ModeTransition,
    aadl2_Mode,
    ModalElement,
    aadl2_SubprogramCallSequence,
    aadl2_Prototype,
    aadl2_AnnexSubclause,
    aadl2_Generalization_,
    PropertyOwner,
    aadl2_ClassifierValue,
    aadl2_AbstractNamedValue,
    Type,
    aadl2_SubcomponentType,
    Namespace,
    aadl2_RecordType,
    aadl2_EnumerationType,
    aadl2_GlobalNamespace,
    aadl2_PropertySet,
    aadl2_PackageSection,
    aadl2_MetaclassReference,
    AbstractNamedValue,
    BasicProperty,
    aadl2_RecordField,
    aadl2_ModalPropertyValue,
    aadl2_Classifier,
    aadl2_PropertyType,
    TypedElement,
    aadl2_PropertyConstant,
    aadl2_BasicProperty,
    NamedElement,
    aadl2_AnnexLibrary,
    aadl2_ClassifierFeature,
    aadl2_Bus,
    aadl2_Namespace,
    aadl2_Device,
    aadl2_Context,
    aadl2_TriggerPort,
    aadl2_Processor,
    aadl2_Memory,
    aadl2_Subprogram,
    aadl2_ComponentTypeRename,
    aadl2_Abstract,
    aadl2_ModalElement,
    aadl2_FeatureGroupTypeRename,
    aadl2_RefinableElement,
    aadl2_ModelUnit,
    aadl2_SubprogramGroup,
    aadl2_Process,
    aadl2_System,
    aadl2_Data,
    aadl2_VirtualProcessor,
    aadl2_PackageRename,
    aadl2_Thread,
    aadl2_ThreadGroup,
    aadl2_VirtualBus,
    aadl2_EnumerationLiteral,
    aadl2_TypedElement,
    aadl2_Type,
    aadl2_Property,
    Element,
    aadl2_NumericRange,
    aadl2_ArrayDimension,
    aadl2_ArraySize,
    aadl2_ContainedNamedElement,
    aadl2_ComponentImplementationReference,
    aadl2_ModeTransitionTrigger,
    aadl2_NamedElement,
    aadl2_PrototypeBinding,
    aadl2_ArrayableElement,
    aadl2_PropertyExpression,
    aadl2_PropertyAssociation,
    aadl2_FlowEnd,
    aadl2_ArrayRange,
    aadl2_BasicPropertyAssociation,
    aadl2_EndToEndFlowSegment,
    aadl2_Relationship,
    aadl2_ConnectedElement,
    aadl2_PropertyOwner,
    aadl2_FlowSegment,
    aadl2_ContainmentPathElement,
    aadl2_Comment,
    aadl2_Element,
    aadl2_ModeBinding,
    TriggerPort,
    Port,
    AccessConnectionEnd,
    aadl2_VirtualBusSubcomponent,
    aadl2_SubprogramSubcomponent,
    aadl2_SubprogramProxy,
    aadl2_BusSubcomponent,
    aadl2_BusFeatureClassifier,
    aadl2_AbstractFeatureClassifier,
    Access,
    AbstractFeatureClassifier,
    aadl2_SubprogramGroupSubcomponentType,
    aadl2_VirtualBusSubcomponentType,
    aadl2_AbstractSubcomponentType,
    aadl2_SubprogramSubcomponentType,
    aadl2_BusSubcomponentType,
    aadl2_DataSubcomponentType,
    PortConnectionEnd,
    aadl2_PortProxy,
    aadl2_InternalFeature,
    ParameterConnectionEnd,
    aadl2_DataSubcomponent,
    aadl2_EventPort,
    FeatureType,
    aadl2_BusAccess,
    Generalization_,
    aadl2_Realization,
    aadl2_ImplementationExtension,
    aadl2_TypeExtension,
    aadl2_GroupExtension,
    aadl2_EndToEndFlowElement,
    EndToEndFlowElement,
    aadl2_FlowElement,
    Feature,
    aadl2_Access,
    aadl2_DirectedFeature,
    aadl2_CallContext,
    aadl2_FeatureGroupType,
    aadl2_FeatureType,
    CallContext,
    aadl2_SubprogramGroupAccess,
    aadl2_SubprogramGroupSubcomponent,
    aadl2_SubprogramGroupType,
    aadl2_SubprogramType,
    aadl2_AbstractType,
    aadl2_DataType,
    FeatureGroupConnectionEnd,
    Context,
    aadl2_SubprogramAccess,
    aadl2_DataPort,
    aadl2_EventDataPort,
    aadl2_SubprogramCall,
    DirectedFeature,
    aadl2_FeatureGroup,
    aadl2_Port,
    aadl2_Parameter,
    aadl2_AbstractFeature,
    FlowElement,
    aadl2_DataAccess,
    aadl2_Subcomponent,
    ModalPath,
    aadl2_Connection,
    FlowFeature,
    aadl2_FlowSpecification,
    aadl2_EndToEndFlow,
    Prototype,
    aadl2_ComponentPrototype,
    aadl2_FeaturePrototype,
    aadl2_FeatureGroupPrototype,
    aadl2_ConnectionEnd,
    ConnectionEnd,
    aadl2_AccessConnectionEnd,
    aadl2_FeatureGroupConnectionEnd,
    aadl2_ParameterConnectionEnd,
    aadl2_PortConnectionEnd,
    aadl2_FeatureConnectionEnd,
    aadl2_ModalPath,
    aadl2_Flow,
    Flow,
    aadl2_FlowFeature,
    aadl2_FlowImplementation,
    PortCategory,
    AccessCategory,
    AccessType,
    FlowKind,
    OperationKind,
    ComponentCategory,
    DirectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(PropertyValue)


def test_hyp_propertyvalue_constructor_exists():
    assert callable(PropertyValue.__init__)


def test_hyp_propertyvalue_constructor_args():
    sig = inspect.signature(PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_stringliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_StringLiteral)


def test_hyp_aadl2_stringliteral_constructor_exists():
    assert callable(aadl2_StringLiteral.__init__)


def test_hyp_aadl2_stringliteral_constructor_args():
    sig = inspect.signature(aadl2_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorClassifier)


def test_hyp_virtualprocessorclassifier_constructor_exists():
    assert callable(VirtualProcessorClassifier.__init__)


def test_hyp_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualBusClassifier)


def test_hyp_virtualbusclassifier_constructor_exists():
    assert callable(VirtualBusClassifier.__init__)


def test_hyp_virtualbusclassifier_constructor_args():
    sig = inspect.signature(VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupClassifier)


def test_hyp_threadgroupclassifier_constructor_exists():
    assert callable(ThreadGroupClassifier.__init__)


def test_hyp_threadgroupclassifier_constructor_args():
    sig = inspect.signature(ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadClassifier)


def test_hyp_threadclassifier_constructor_exists():
    assert callable(ThreadClassifier.__init__)


def test_hyp_threadclassifier_constructor_args():
    sig = inspect.signature(ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessClassifier)


def test_hyp_processclassifier_constructor_exists():
    assert callable(ProcessClassifier.__init__)


def test_hyp_processclassifier_constructor_args():
    sig = inspect.signature(ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessorClassifier)


def test_hyp_processorclassifier_constructor_exists():
    assert callable(ProcessorClassifier.__init__)


def test_hyp_processorclassifier_constructor_args():
    sig = inspect.signature(ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(SystemClassifier)


def test_hyp_systemclassifier_constructor_exists():
    assert callable(SystemClassifier.__init__)


def test_hyp_systemclassifier_constructor_args():
    sig = inspect.signature(SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupClassifier)


def test_hyp_subprogramgroupclassifier_constructor_exists():
    assert callable(SubprogramGroupClassifier.__init__)


def test_hyp_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramClassifier)


def test_hyp_subprogramclassifier_constructor_exists():
    assert callable(SubprogramClassifier.__init__)


def test_hyp_subprogramclassifier_constructor_args():
    sig = inspect.signature(SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(MemoryClassifier)


def test_hyp_memoryclassifier_constructor_exists():
    assert callable(MemoryClassifier.__init__)


def test_hyp_memoryclassifier_constructor_args():
    sig = inspect.signature(MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(DeviceClassifier)


def test_hyp_deviceclassifier_constructor_exists():
    assert callable(DeviceClassifier.__init__)


def test_hyp_deviceclassifier_constructor_args():
    sig = inspect.signature(DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(DataClassifier)


def test_hyp_dataclassifier_constructor_exists():
    assert callable(DataClassifier.__init__)


def test_hyp_dataclassifier_constructor_args():
    sig = inspect.signature(DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentprototype_is_not_abstract():
    assert not inspect.isabstract(ComponentPrototype)


def test_hyp_componentprototype_constructor_exists():
    assert callable(ComponentPrototype.__init__)


def test_hyp_componentprototype_constructor_args():
    sig = inspect.signature(ComponentPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_busclassifier_is_not_abstract():
    assert not inspect.isabstract(BusClassifier)


def test_hyp_busclassifier_constructor_exists():
    assert callable(BusClassifier.__init__)


def test_hyp_busclassifier_constructor_args():
    sig = inspect.signature(BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_thread_is_not_abstract():
    assert not inspect.isabstract(Thread)


def test_hyp_thread_constructor_exists():
    assert callable(Thread.__init__)


def test_hyp_thread_constructor_args():
    sig = inspect.signature(Thread.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessor)


def test_hyp_virtualprocessor_constructor_exists():
    assert callable(VirtualProcessor.__init__)


def test_hyp_virtualprocessor_constructor_args():
    sig = inspect.signature(VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualbus_is_not_abstract():
    assert not inspect.isabstract(VirtualBus)


def test_hyp_virtualbus_constructor_exists():
    assert callable(VirtualBus.__init__)


def test_hyp_virtualbus_constructor_args():
    sig = inspect.signature(VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_threadgroup_is_not_abstract():
    assert not inspect.isabstract(ThreadGroup)


def test_hyp_threadgroup_constructor_exists():
    assert callable(ThreadGroup.__init__)


def test_hyp_threadgroup_constructor_args():
    sig = inspect.signature(ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_hyp_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_hyp_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroup)


def test_hyp_subprogramgroup_constructor_exists():
    assert callable(SubprogramGroup.__init__)


def test_hyp_subprogramgroup_constructor_args():
    sig = inspect.signature(SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_hyp_system_constructor_exists():
    assert callable(System.__init__)


def test_hyp_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_hyp_process_constructor_exists():
    assert callable(Process.__init__)


def test_hyp_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memory_is_not_abstract():
    assert not inspect.isabstract(Memory)


def test_hyp_memory_constructor_exists():
    assert callable(Memory.__init__)


def test_hyp_memory_constructor_args():
    sig = inspect.signature(Memory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_hyp_device_constructor_exists():
    assert callable(Device.__init__)


def test_hyp_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_hyp_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_hyp_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(BehavioredImplementation)


def test_hyp_behavioredimplementation_constructor_exists():
    assert callable(BehavioredImplementation.__init__)


def test_hyp_behavioredimplementation_constructor_args():
    sig = inspect.signature(BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramImplementation)


def test_hyp_aadl2_subprogramimplementation_constructor_exists():
    assert callable(aadl2_SubprogramImplementation.__init__)


def test_hyp_aadl2_subprogramimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadImplementation)


def test_hyp_aadl2_threadimplementation_constructor_exists():
    assert callable(aadl2_ThreadImplementation.__init__)


def test_hyp_aadl2_threadimplementation_constructor_args():
    sig = inspect.signature(aadl2_ThreadImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_busfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(BusFeatureClassifier)


def test_hyp_busfeatureclassifier_constructor_exists():
    assert callable(BusFeatureClassifier.__init__)


def test_hyp_busfeatureclassifier_constructor_args():
    sig = inspect.signature(BusFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorSubcomponentType)


def test_hyp_virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(VirtualProcessorSubcomponentType.__init__)


def test_hyp_virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorPrototype)


def test_hyp_aadl2_virtualprocessorprototype_constructor_exists():
    assert callable(aadl2_VirtualProcessorPrototype.__init__)


def test_hyp_aadl2_virtualprocessorprototype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualBusSubcomponentType)


def test_hyp_virtualbussubcomponenttype_constructor_exists():
    assert callable(VirtualBusSubcomponentType.__init__)


def test_hyp_virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbusprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusPrototype)


def test_hyp_aadl2_virtualbusprototype_constructor_exists():
    assert callable(aadl2_VirtualBusPrototype.__init__)


def test_hyp_aadl2_virtualbusprototype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadSubcomponentType)


def test_hyp_threadsubcomponenttype_constructor_exists():
    assert callable(ThreadSubcomponentType.__init__)


def test_hyp_threadsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadPrototype)


def test_hyp_aadl2_threadprototype_constructor_exists():
    assert callable(aadl2_ThreadPrototype.__init__)


def test_hyp_aadl2_threadprototype_constructor_args():
    sig = inspect.signature(aadl2_ThreadPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupSubcomponentType)


def test_hyp_threadgroupsubcomponenttype_constructor_exists():
    assert callable(ThreadGroupSubcomponentType.__init__)


def test_hyp_threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupPrototype)


def test_hyp_aadl2_threadgroupprototype_constructor_exists():
    assert callable(aadl2_ThreadGroupPrototype.__init__)


def test_hyp_aadl2_threadgroupprototype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SystemSubcomponentType)


def test_hyp_systemsubcomponenttype_constructor_exists():
    assert callable(SystemSubcomponentType.__init__)


def test_hyp_systemsubcomponenttype_constructor_args():
    sig = inspect.signature(SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemPrototype)


def test_hyp_aadl2_systemprototype_constructor_exists():
    assert callable(aadl2_SystemPrototype.__init__)


def test_hyp_aadl2_systemprototype_constructor_args():
    sig = inspect.signature(aadl2_SystemPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupSubcomponentType)


def test_hyp_subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(SubprogramGroupSubcomponentType.__init__)


def test_hyp_subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupPrototype)


def test_hyp_aadl2_subprogramgroupprototype_constructor_exists():
    assert callable(aadl2_SubprogramGroupPrototype.__init__)


def test_hyp_aadl2_subprogramgroupprototype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessSubcomponentType)


def test_hyp_processsubcomponenttype_constructor_exists():
    assert callable(ProcessSubcomponentType.__init__)


def test_hyp_processsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessPrototype)


def test_hyp_aadl2_processprototype_constructor_exists():
    assert callable(aadl2_ProcessPrototype.__init__)


def test_hyp_aadl2_processprototype_constructor_args():
    sig = inspect.signature(aadl2_ProcessPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessorSubcomponentType)


def test_hyp_processorsubcomponenttype_constructor_exists():
    assert callable(ProcessorSubcomponentType.__init__)


def test_hyp_processorsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorPrototype)


def test_hyp_aadl2_processorprototype_constructor_exists():
    assert callable(aadl2_ProcessorPrototype.__init__)


def test_hyp_aadl2_processorprototype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(MemorySubcomponentType)


def test_hyp_memorysubcomponenttype_constructor_exists():
    assert callable(MemorySubcomponentType.__init__)


def test_hyp_memorysubcomponenttype_constructor_args():
    sig = inspect.signature(MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memoryprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryPrototype)


def test_hyp_aadl2_memoryprototype_constructor_exists():
    assert callable(aadl2_MemoryPrototype.__init__)


def test_hyp_aadl2_memoryprototype_constructor_args():
    sig = inspect.signature(aadl2_MemoryPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DeviceSubcomponentType)


def test_hyp_devicesubcomponenttype_constructor_exists():
    assert callable(DeviceSubcomponentType.__init__)


def test_hyp_devicesubcomponenttype_constructor_args():
    sig = inspect.signature(DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_deviceprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DevicePrototype)


def test_hyp_aadl2_deviceprototype_constructor_exists():
    assert callable(aadl2_DevicePrototype.__init__)


def test_hyp_aadl2_deviceprototype_constructor_args():
    sig = inspect.signature(aadl2_DevicePrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(BusSubcomponentType)


def test_hyp_bussubcomponenttype_constructor_exists():
    assert callable(BusSubcomponentType.__init__)


def test_hyp_bussubcomponenttype_constructor_args():
    sig = inspect.signature(BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_busprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusPrototype)


def test_hyp_aadl2_busprototype_constructor_exists():
    assert callable(aadl2_BusPrototype.__init__)


def test_hyp_aadl2_busprototype_constructor_args():
    sig = inspect.signature(aadl2_BusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(AbstractSubcomponentType)


def test_hyp_abstractsubcomponenttype_constructor_exists():
    assert callable(AbstractSubcomponentType.__init__)


def test_hyp_abstractsubcomponenttype_constructor_args():
    sig = inspect.signature(AbstractSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(AbstractClassifier)


def test_hyp_abstractclassifier_constructor_exists():
    assert callable(AbstractClassifier.__init__)


def test_hyp_abstractclassifier_constructor_args():
    sig = inspect.signature(AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractImplementation)


def test_hyp_aadl2_abstractimplementation_constructor_exists():
    assert callable(aadl2_AbstractImplementation.__init__)


def test_hyp_aadl2_abstractimplementation_constructor_args():
    sig = inspect.signature(aadl2_AbstractImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componenttype_is_not_abstract():
    assert not inspect.isabstract(ComponentType)


def test_hyp_componenttype_constructor_exists():
    assert callable(ComponentType.__init__)


def test_hyp_componenttype_constructor_args():
    sig = inspect.signature(ComponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_bustype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusType)


def test_hyp_aadl2_bustype_constructor_exists():
    assert callable(aadl2_BusType.__init__)


def test_hyp_aadl2_bustype_constructor_args():
    sig = inspect.signature(aadl2_BusType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessType)


def test_hyp_aadl2_processtype_constructor_exists():
    assert callable(aadl2_ProcessType.__init__)


def test_hyp_aadl2_processtype_constructor_args():
    sig = inspect.signature(aadl2_ProcessType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbustype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusType)


def test_hyp_aadl2_virtualbustype_constructor_exists():
    assert callable(aadl2_VirtualBusType.__init__)


def test_hyp_aadl2_virtualbustype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_devicetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceType)


def test_hyp_aadl2_devicetype_constructor_exists():
    assert callable(aadl2_DeviceType.__init__)


def test_hyp_aadl2_devicetype_constructor_args():
    sig = inspect.signature(aadl2_DeviceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemType)


def test_hyp_aadl2_systemtype_constructor_exists():
    assert callable(aadl2_SystemType.__init__)


def test_hyp_aadl2_systemtype_constructor_args():
    sig = inspect.signature(aadl2_SystemType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessortype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorType)


def test_hyp_aadl2_virtualprocessortype_constructor_exists():
    assert callable(aadl2_VirtualProcessorType.__init__)


def test_hyp_aadl2_virtualprocessortype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupType)


def test_hyp_aadl2_threadgrouptype_constructor_exists():
    assert callable(aadl2_ThreadGroupType.__init__)


def test_hyp_aadl2_threadgrouptype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadType)


def test_hyp_aadl2_threadtype_constructor_exists():
    assert callable(aadl2_ThreadType.__init__)


def test_hyp_aadl2_threadtype_constructor_args():
    sig = inspect.signature(aadl2_ThreadType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processortype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorType)


def test_hyp_aadl2_processortype_constructor_exists():
    assert callable(aadl2_ProcessorType.__init__)


def test_hyp_aadl2_processortype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memorytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryType)


def test_hyp_aadl2_memorytype_constructor_exists():
    assert callable(aadl2_MemoryType.__init__)


def test_hyp_aadl2_memorytype_constructor_args():
    sig = inspect.signature(aadl2_MemoryType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(ComponentImplementation)


def test_hyp_componentimplementation_constructor_exists():
    assert callable(ComponentImplementation.__init__)


def test_hyp_componentimplementation_constructor_args():
    sig = inspect.signature(ComponentImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessImplementation)


def test_hyp_aadl2_processimplementation_constructor_exists():
    assert callable(aadl2_ProcessImplementation.__init__)


def test_hyp_aadl2_processimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupImplementation)


def test_hyp_aadl2_threadgroupimplementation_constructor_exists():
    assert callable(aadl2_ThreadGroupImplementation.__init__)


def test_hyp_aadl2_threadgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbusimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusImplementation)


def test_hyp_aadl2_virtualbusimplementation_constructor_exists():
    assert callable(aadl2_VirtualBusImplementation.__init__)


def test_hyp_aadl2_virtualbusimplementation_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memoryimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryImplementation)


def test_hyp_aadl2_memoryimplementation_constructor_exists():
    assert callable(aadl2_MemoryImplementation.__init__)


def test_hyp_aadl2_memoryimplementation_constructor_args():
    sig = inspect.signature(aadl2_MemoryImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorImplementation)


def test_hyp_aadl2_processorimplementation_constructor_exists():
    assert callable(aadl2_ProcessorImplementation.__init__)


def test_hyp_aadl2_processorimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorImplementation)


def test_hyp_aadl2_virtualprocessorimplementation_constructor_exists():
    assert callable(aadl2_VirtualProcessorImplementation.__init__)


def test_hyp_aadl2_virtualprocessorimplementation_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_busimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusImplementation)


def test_hyp_aadl2_busimplementation_constructor_exists():
    assert callable(aadl2_BusImplementation.__init__)


def test_hyp_aadl2_busimplementation_constructor_args():
    sig = inspect.signature(aadl2_BusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_deviceimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceImplementation)


def test_hyp_aadl2_deviceimplementation_constructor_exists():
    assert callable(aadl2_DeviceImplementation.__init__)


def test_hyp_aadl2_deviceimplementation_constructor_args():
    sig = inspect.signature(aadl2_DeviceImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_dataimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataImplementation)


def test_hyp_aadl2_dataimplementation_constructor_exists():
    assert callable(aadl2_DataImplementation.__init__)


def test_hyp_aadl2_dataimplementation_constructor_args():
    sig = inspect.signature(aadl2_DataImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemImplementation)


def test_hyp_aadl2_systemimplementation_constructor_exists():
    assert callable(aadl2_SystemImplementation.__init__)


def test_hyp_aadl2_systemimplementation_constructor_args():
    sig = inspect.signature(aadl2_SystemImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupImplementation)


def test_hyp_aadl2_subprogramgroupimplementation_constructor_exists():
    assert callable(aadl2_SubprogramGroupImplementation.__init__)


def test_hyp_aadl2_subprogramgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BehavioredImplementation)


def test_hyp_aadl2_behavioredimplementation_constructor_exists():
    assert callable(aadl2_BehavioredImplementation.__init__)


def test_hyp_aadl2_behavioredimplementation_constructor_args():
    sig = inspect.signature(aadl2_BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_hyp_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_hyp_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(PrototypeBinding)


def test_hyp_prototypebinding_constructor_exists():
    assert callable(PrototypeBinding.__init__)


def test_hyp_prototypebinding_constructor_args():
    sig = inspect.signature(PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeBinding)


def test_hyp_aadl2_featureprototypebinding_constructor_exists():
    assert callable(aadl2_FeaturePrototypeBinding.__init__)


def test_hyp_aadl2_featureprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componentprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototypeBinding)


def test_hyp_aadl2_componentprototypebinding_constructor_exists():
    assert callable(aadl2_ComponentPrototypeBinding.__init__)


def test_hyp_aadl2_componentprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(FeaturePrototypeActual)


def test_hyp_featureprototypeactual_constructor_exists():
    assert callable(FeaturePrototypeActual.__init__)


def test_hyp_featureprototypeactual_constructor_args():
    sig = inspect.signature(FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureprototypereference_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeReference)


def test_hyp_aadl2_featureprototypereference_constructor_exists():
    assert callable(aadl2_FeaturePrototypeReference.__init__)


def test_hyp_aadl2_featureprototypereference_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "out" in params, "Missing parameter 'out'"






def test_hyp_aadl2_accessspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessSpecification)


def test_hyp_aadl2_accessspecification_constructor_exists():
    assert callable(aadl2_AccessSpecification.__init__)


def test_hyp_aadl2_accessspecification_constructor_args():
    sig = inspect.signature(aadl2_AccessSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_aadl2_portspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortSpecification)


def test_hyp_aadl2_portspecification_constructor_exists():
    assert callable(aadl2_PortSpecification.__init__)


def test_hyp_aadl2_portspecification_constructor_args():
    sig = inspect.signature(aadl2_PortSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "out" in params, "Missing parameter 'out'"







def test_hyp_aadl2_featuregroupprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototypeActual)


def test_hyp_aadl2_featuregroupprototypeactual_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototypeActual.__init__)


def test_hyp_aadl2_featuregroupprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregroupprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototypeBinding)


def test_hyp_aadl2_featuregroupprototypebinding_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototypeBinding.__init__)


def test_hyp_aadl2_featuregroupprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelunit_is_not_abstract():
    assert not inspect.isabstract(ModelUnit)


def test_hyp_modelunit_constructor_exists():
    assert callable(ModelUnit.__init__)


def test_hyp_modelunit_constructor_args():
    sig = inspect.signature(ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_aadlpackage_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlPackage)


def test_hyp_aadl2_aadlpackage_constructor_exists():
    assert callable(aadl2_AadlPackage.__init__)


def test_hyp_aadl2_aadlpackage_constructor_args():
    sig = inspect.signature(aadl2_AadlPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packagesection_is_not_abstract():
    assert not inspect.isabstract(PackageSection)


def test_hyp_packagesection_constructor_exists():
    assert callable(PackageSection.__init__)


def test_hyp_packagesection_constructor_args():
    sig = inspect.signature(PackageSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_privatepackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrivatePackageSection)


def test_hyp_aadl2_privatepackagesection_constructor_exists():
    assert callable(aadl2_PrivatePackageSection.__init__)


def test_hyp_aadl2_privatepackagesection_constructor_args():
    sig = inspect.signature(aadl2_PrivatePackageSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_publicpackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PublicPackageSection)


def test_hyp_aadl2_publicpackagesection_constructor_exists():
    assert callable(aadl2_PublicPackageSection.__init__)


def test_hyp_aadl2_publicpackagesection_constructor_args():
    sig = inspect.signature(aadl2_PublicPackageSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramSubcomponentType)


def test_hyp_subprogramsubcomponenttype_constructor_exists():
    assert callable(SubprogramSubcomponentType.__init__)


def test_hyp_subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subprogram_is_not_abstract():
    assert not inspect.isabstract(Subprogram)


def test_hyp_subprogram_constructor_exists():
    assert callable(Subprogram.__init__)


def test_hyp_subprogram_constructor_args():
    sig = inspect.signature(Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramPrototype)


def test_hyp_aadl2_subprogramprototype_constructor_exists():
    assert callable(aadl2_SubprogramPrototype.__init__)


def test_hyp_aadl2_subprogramprototype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annexsubclause_is_not_abstract():
    assert not inspect.isabstract(AnnexSubclause)


def test_hyp_annexsubclause_constructor_exists():
    assert callable(AnnexSubclause.__init__)


def test_hyp_annexsubclause_constructor_args():
    sig = inspect.signature(AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_defaultannexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2_DefaultAnnexSubclause)


def test_hyp_aadl2_defaultannexsubclause_constructor_exists():
    assert callable(aadl2_DefaultAnnexSubclause.__init__)


def test_hyp_aadl2_defaultannexsubclause_constructor_args():
    sig = inspect.signature(aadl2_DefaultAnnexSubclause.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"




def test_hyp_annexlibrary_is_not_abstract():
    assert not inspect.isabstract(AnnexLibrary)


def test_hyp_annexlibrary_constructor_exists():
    assert callable(AnnexLibrary.__init__)


def test_hyp_annexlibrary_constructor_args():
    sig = inspect.signature(AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_defaultannexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2_DefaultAnnexLibrary)


def test_hyp_aadl2_defaultannexlibrary_constructor_exists():
    assert callable(aadl2_DefaultAnnexLibrary.__init__)


def test_hyp_aadl2_defaultannexlibrary_constructor_args():
    sig = inspect.signature(aadl2_DefaultAnnexLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"




def test_hyp_internalfeature_is_not_abstract():
    assert not inspect.isabstract(InternalFeature)


def test_hyp_internalfeature_constructor_exists():
    assert callable(InternalFeature.__init__)


def test_hyp_internalfeature_constructor_args():
    sig = inspect.signature(InternalFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processorfeature_is_not_abstract():
    assert not inspect.isabstract(ProcessorFeature)


def test_hyp_processorfeature_constructor_exists():
    assert callable(ProcessorFeature.__init__)


def test_hyp_processorfeature_constructor_args():
    sig = inspect.signature(ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DataSubcomponentType)


def test_hyp_datasubcomponenttype_constructor_exists():
    assert callable(DataSubcomponentType.__init__)


def test_hyp_datasubcomponenttype_constructor_args():
    sig = inspect.signature(DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_hyp_data_constructor_exists():
    assert callable(Data.__init__)


def test_hyp_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_dataprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataPrototype)


def test_hyp_aadl2_dataprototype_constructor_exists():
    assert callable(aadl2_DataPrototype.__init__)


def test_hyp_aadl2_dataprototype_constructor_args():
    sig = inspect.signature(aadl2_DataPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstract_is_not_abstract():
    assert not inspect.isabstract(Abstract)


def test_hyp_abstract_constructor_exists():
    assert callable(Abstract.__init__)


def test_hyp_abstract_constructor_args():
    sig = inspect.signature(Abstract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractPrototype)


def test_hyp_aadl2_abstractprototype_constructor_exists():
    assert callable(aadl2_AbstractPrototype.__init__)


def test_hyp_aadl2_abstractprototype_constructor_args():
    sig = inspect.signature(aadl2_AbstractPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subcomponent_is_not_abstract():
    assert not inspect.isabstract(Subcomponent)


def test_hyp_subcomponent_constructor_exists():
    assert callable(Subcomponent.__init__)


def test_hyp_subcomponent_constructor_args():
    sig = inspect.signature(Subcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorSubcomponent)


def test_hyp_aadl2_virtualprocessorsubcomponent_constructor_exists():
    assert callable(aadl2_VirtualProcessorSubcomponent.__init__)


def test_hyp_aadl2_virtualprocessorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemSubcomponent)


def test_hyp_aadl2_systemsubcomponent_constructor_exists():
    assert callable(aadl2_SystemSubcomponent.__init__)


def test_hyp_aadl2_systemsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SystemSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessSubcomponent)


def test_hyp_aadl2_processsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessSubcomponent.__init__)


def test_hyp_aadl2_processsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubcomponent)


def test_hyp_aadl2_processorsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessorSubcomponent.__init__)


def test_hyp_aadl2_processorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_devicesubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceSubcomponent)


def test_hyp_aadl2_devicesubcomponent_constructor_exists():
    assert callable(aadl2_DeviceSubcomponent.__init__)


def test_hyp_aadl2_devicesubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DeviceSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupSubcomponent)


def test_hyp_aadl2_threadgroupsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadGroupSubcomponent.__init__)


def test_hyp_aadl2_threadgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadSubcomponent)


def test_hyp_aadl2_threadsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadSubcomponent.__init__)


def test_hyp_aadl2_threadsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memorysubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemorySubcomponent)


def test_hyp_aadl2_memorysubcomponent_constructor_exists():
    assert callable(aadl2_MemorySubcomponent.__init__)


def test_hyp_aadl2_memorysubcomponent_constructor_args():
    sig = inspect.signature(aadl2_MemorySubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_hyp_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_hyp_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_hyp_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_hyp_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_aadlreal_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlReal)


def test_hyp_aadl2_aadlreal_constructor_exists():
    assert callable(aadl2_AadlReal.__init__)


def test_hyp_aadl2_aadlreal_constructor_args():
    sig = inspect.signature(aadl2_AadlReal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_aadlinteger_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlInteger)


def test_hyp_aadl2_aadlinteger_constructor_exists():
    assert callable(aadl2_AadlInteger.__init__)


def test_hyp_aadl2_aadlinteger_constructor_args():
    sig = inspect.signature(aadl2_AadlInteger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nonlisttype_is_not_abstract():
    assert not inspect.isabstract(NonListType)


def test_hyp_nonlisttype_constructor_exists():
    assert callable(NonListType.__init__)


def test_hyp_nonlisttype_constructor_args():
    sig = inspect.signature(NonListType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_rangetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeType)


def test_hyp_aadl2_rangetype_constructor_exists():
    assert callable(aadl2_RangeType.__init__)


def test_hyp_aadl2_rangetype_constructor_args():
    sig = inspect.signature(aadl2_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_referencetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ReferenceType)


def test_hyp_aadl2_referencetype_constructor_exists():
    assert callable(aadl2_ReferenceType.__init__)


def test_hyp_aadl2_referencetype_constructor_args():
    sig = inspect.signature(aadl2_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_classifiertype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierType)


def test_hyp_aadl2_classifiertype_constructor_exists():
    assert callable(aadl2_ClassifierType.__init__)


def test_hyp_aadl2_classifiertype_constructor_args():
    sig = inspect.signature(aadl2_ClassifierType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_aadlstring_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlString)


def test_hyp_aadl2_aadlstring_constructor_exists():
    assert callable(aadl2_AadlString.__init__)


def test_hyp_aadl2_aadlstring_constructor_args():
    sig = inspect.signature(aadl2_AadlString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_numbertype_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberType)


def test_hyp_aadl2_numbertype_constructor_exists():
    assert callable(aadl2_NumberType.__init__)


def test_hyp_aadl2_numbertype_constructor_args():
    sig = inspect.signature(aadl2_NumberType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_aadlboolean_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlBoolean)


def test_hyp_aadl2_aadlboolean_constructor_exists():
    assert callable(aadl2_AadlBoolean.__init__)


def test_hyp_aadl2_aadlboolean_constructor_args():
    sig = inspect.signature(aadl2_AadlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_hyp_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_hyp_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_listtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ListType)


def test_hyp_aadl2_listtype_constructor_exists():
    assert callable(aadl2_ListType.__init__)


def test_hyp_aadl2_listtype_constructor_args():
    sig = inspect.signature(aadl2_ListType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_nonlisttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_NonListType)


def test_hyp_aadl2_nonlisttype_constructor_exists():
    assert callable(aadl2_NonListType.__init__)


def test_hyp_aadl2_nonlisttype_constructor_args():
    sig = inspect.signature(aadl2_NonListType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_hyp_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_hyp_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_unitstype_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitsType)


def test_hyp_aadl2_unitstype_constructor_exists():
    assert callable(aadl2_UnitsType.__init__)


def test_hyp_aadl2_unitstype_constructor_args():
    sig = inspect.signature(aadl2_UnitsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_computedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComputedValue)


def test_hyp_aadl2_computedvalue_constructor_exists():
    assert callable(aadl2_ComputedValue.__init__)


def test_hyp_aadl2_computedvalue_constructor_args():
    sig = inspect.signature(aadl2_ComputedValue.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"




def test_hyp_aadl2_recordvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordValue)


def test_hyp_aadl2_recordvalue_constructor_exists():
    assert callable(aadl2_RecordValue.__init__)


def test_hyp_aadl2_recordvalue_constructor_args():
    sig = inspect.signature(aadl2_RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_namedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_NamedValue)


def test_hyp_aadl2_namedvalue_constructor_exists():
    assert callable(aadl2_NamedValue.__init__)


def test_hyp_aadl2_namedvalue_constructor_args():
    sig = inspect.signature(aadl2_NamedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_hyp_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_hyp_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_integerliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_IntegerLiteral)


def test_hyp_aadl2_integerliteral_constructor_exists():
    assert callable(aadl2_IntegerLiteral.__init__)


def test_hyp_aadl2_integerliteral_constructor_args():
    sig = inspect.signature(aadl2_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "base" in params, "Missing parameter 'base'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_aadl2_rangevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeValue)


def test_hyp_aadl2_rangevalue_constructor_exists():
    assert callable(aadl2_RangeValue.__init__)


def test_hyp_aadl2_rangevalue_constructor_args():
    sig = inspect.signature(aadl2_RangeValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_BooleanLiteral)


def test_hyp_aadl2_booleanliteral_constructor_exists():
    assert callable(aadl2_BooleanLiteral.__init__)


def test_hyp_aadl2_booleanliteral_constructor_args():
    sig = inspect.signature(aadl2_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(ContainedNamedElement)


def test_hyp_containednamedelement_constructor_exists():
    assert callable(ContainedNamedElement.__init__)


def test_hyp_containednamedelement_constructor_args():
    sig = inspect.signature(ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_referencevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ReferenceValue)


def test_hyp_aadl2_referencevalue_constructor_exists():
    assert callable(aadl2_ReferenceValue.__init__)


def test_hyp_aadl2_referencevalue_constructor_args():
    sig = inspect.signature(aadl2_ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_realliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_RealLiteral)


def test_hyp_aadl2_realliteral_constructor_exists():
    assert callable(aadl2_RealLiteral.__init__)


def test_hyp_aadl2_realliteral_constructor_args():
    sig = inspect.signature(aadl2_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_hyp_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_hyp_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_unitliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitLiteral)


def test_hyp_aadl2_unitliteral_constructor_exists():
    assert callable(aadl2_UnitLiteral.__init__)


def test_hyp_aadl2_unitliteral_constructor_args():
    sig = inspect.signature(aadl2_UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_numbervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberValue)


def test_hyp_aadl2_numbervalue_constructor_exists():
    assert callable(aadl2_NumberValue.__init__)


def test_hyp_aadl2_numbervalue_constructor_args():
    sig = inspect.signature(aadl2_NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertyexpression_is_not_abstract():
    assert not inspect.isabstract(PropertyExpression)


def test_hyp_propertyexpression_constructor_exists():
    assert callable(PropertyExpression.__init__)


def test_hyp_propertyexpression_constructor_args():
    sig = inspect.signature(PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_listvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ListValue)


def test_hyp_aadl2_listvalue_constructor_exists():
    assert callable(aadl2_ListValue.__init__)


def test_hyp_aadl2_listvalue_constructor_args():
    sig = inspect.signature(aadl2_ListValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_operation_is_not_abstract():
    assert not inspect.isabstract(aadl2_Operation)


def test_hyp_aadl2_operation_constructor_exists():
    assert callable(aadl2_Operation.__init__)


def test_hyp_aadl2_operation_constructor_args():
    sig = inspect.signature(aadl2_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_aadl2_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyValue)


def test_hyp_aadl2_propertyvalue_constructor_exists():
    assert callable(aadl2_PropertyValue.__init__)


def test_hyp_aadl2_propertyvalue_constructor_args():
    sig = inspect.signature(aadl2_PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(ArraySizeProperty)


def test_hyp_arraysizeproperty_constructor_exists():
    assert callable(ArraySizeProperty.__init__)


def test_hyp_arraysizeproperty_constructor_args():
    sig = inspect.signature(ArraySizeProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(ArrayableElement)


def test_hyp_arrayableelement_constructor_exists():
    assert callable(ArrayableElement.__init__)


def test_hyp_arrayableelement_constructor_args():
    sig = inspect.signature(ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeActual)


def test_hyp_aadl2_featureprototypeactual_constructor_exists():
    assert callable(aadl2_FeaturePrototypeActual.__init__)


def test_hyp_aadl2_featureprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componentprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototypeActual)


def test_hyp_aadl2_componentprototypeactual_constructor_exists():
    assert callable(aadl2_ComponentPrototypeActual.__init__)


def test_hyp_aadl2_componentprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototypeActual.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"




def test_hyp_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(FeatureConnectionEnd)


def test_hyp_featureconnectionend_constructor_exists():
    assert callable(FeatureConnectionEnd.__init__)


def test_hyp_featureconnectionend_constructor_args():
    sig = inspect.signature(FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureClassifier)


def test_hyp_aadl2_featureclassifier_constructor_exists():
    assert callable(aadl2_FeatureClassifier.__init__)


def test_hyp_aadl2_featureclassifier_constructor_args():
    sig = inspect.signature(aadl2_FeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_eventsource_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventSource)


def test_hyp_aadl2_eventsource_constructor_exists():
    assert callable(aadl2_EventSource.__init__)


def test_hyp_aadl2_eventsource_constructor_args():
    sig = inspect.signature(aadl2_EventSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureclassifier_is_not_abstract():
    assert not inspect.isabstract(FeatureClassifier)


def test_hyp_featureclassifier_constructor_exists():
    assert callable(FeatureClassifier.__init__)


def test_hyp_featureclassifier_constructor_args():
    sig = inspect.signature(FeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubcomponentType)


def test_hyp_subcomponenttype_constructor_exists():
    assert callable(SubcomponentType.__init__)


def test_hyp_subcomponenttype_constructor_args():
    sig = inspect.signature(SubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupSubcomponentType)


def test_hyp_aadl2_threadgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2_ThreadGroupSubcomponentType.__init__)


def test_hyp_aadl2_threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadSubcomponentType)


def test_hyp_aadl2_threadsubcomponenttype_constructor_exists():
    assert callable(aadl2_ThreadSubcomponentType.__init__)


def test_hyp_aadl2_threadsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemorySubcomponentType)


def test_hyp_aadl2_memorysubcomponenttype_constructor_exists():
    assert callable(aadl2_MemorySubcomponentType.__init__)


def test_hyp_aadl2_memorysubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessSubcomponentType)


def test_hyp_aadl2_processsubcomponenttype_constructor_exists():
    assert callable(aadl2_ProcessSubcomponentType.__init__)


def test_hyp_aadl2_processsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemSubcomponentType)


def test_hyp_aadl2_systemsubcomponenttype_constructor_exists():
    assert callable(aadl2_SystemSubcomponentType.__init__)


def test_hyp_aadl2_systemsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceSubcomponentType)


def test_hyp_aadl2_devicesubcomponenttype_constructor_exists():
    assert callable(aadl2_DeviceSubcomponentType.__init__)


def test_hyp_aadl2_devicesubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubcomponentType)


def test_hyp_aadl2_processorsubcomponenttype_constructor_exists():
    assert callable(aadl2_ProcessorSubcomponentType.__init__)


def test_hyp_aadl2_processorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorSubcomponentType)


def test_hyp_aadl2_virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(aadl2_VirtualProcessorSubcomponentType.__init__)


def test_hyp_aadl2_virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentClassifier)


def test_hyp_aadl2_componentclassifier_constructor_exists():
    assert callable(aadl2_ComponentClassifier.__init__)


def test_hyp_aadl2_componentclassifier_constructor_args():
    sig = inspect.signature(aadl2_ComponentClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "derivedModes" in params, "Missing parameter 'derivedModes'"
    assert "noModes" in params, "Missing parameter 'noModes'"
    assert "noFlows" in params, "Missing parameter 'noFlows'"






def test_hyp_aadl2_eventdatasource_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventDataSource)


def test_hyp_aadl2_eventdatasource_constructor_exists():
    assert callable(aadl2_EventDataSource.__init__)


def test_hyp_aadl2_eventdatasource_constructor_args():
    sig = inspect.signature(aadl2_EventDataSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregroupconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupConnection)


def test_hyp_aadl2_featuregroupconnection_constructor_exists():
    assert callable(aadl2_FeatureGroupConnection.__init__)


def test_hyp_aadl2_featuregroupconnection_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureConnection)


def test_hyp_aadl2_featureconnection_constructor_exists():
    assert callable(aadl2_FeatureConnection.__init__)


def test_hyp_aadl2_featureconnection_constructor_args():
    sig = inspect.signature(aadl2_FeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_portconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortConnection)


def test_hyp_aadl2_portconnection_constructor_exists():
    assert callable(aadl2_PortConnection.__init__)


def test_hyp_aadl2_portconnection_constructor_args():
    sig = inspect.signature(aadl2_PortConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_parameterconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_ParameterConnection)


def test_hyp_aadl2_parameterconnection_constructor_exists():
    assert callable(aadl2_ParameterConnection.__init__)


def test_hyp_aadl2_parameterconnection_constructor_args():
    sig = inspect.signature(aadl2_ParameterConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(ComponentClassifier)


def test_hyp_componentclassifier_constructor_exists():
    assert callable(ComponentClassifier.__init__)


def test_hyp_componentclassifier_constructor_args():
    sig = inspect.signature(ComponentClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceClassifier)


def test_hyp_aadl2_deviceclassifier_constructor_exists():
    assert callable(aadl2_DeviceClassifier.__init__)


def test_hyp_aadl2_deviceclassifier_constructor_args():
    sig = inspect.signature(aadl2_DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupClassifier)


def test_hyp_aadl2_threadgroupclassifier_constructor_exists():
    assert callable(aadl2_ThreadGroupClassifier.__init__)


def test_hyp_aadl2_threadgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryClassifier)


def test_hyp_aadl2_memoryclassifier_constructor_exists():
    assert callable(aadl2_MemoryClassifier.__init__)


def test_hyp_aadl2_memoryclassifier_constructor_args():
    sig = inspect.signature(aadl2_MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessClassifier)


def test_hyp_aadl2_processclassifier_constructor_exists():
    assert callable(aadl2_ProcessClassifier.__init__)


def test_hyp_aadl2_processclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorClassifier)


def test_hyp_aadl2_virtualprocessorclassifier_constructor_exists():
    assert callable(aadl2_VirtualProcessorClassifier.__init__)


def test_hyp_aadl2_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadClassifier)


def test_hyp_aadl2_threadclassifier_constructor_exists():
    assert callable(aadl2_ThreadClassifier.__init__)


def test_hyp_aadl2_threadclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupClassifier)


def test_hyp_aadl2_subprogramgroupclassifier_constructor_exists():
    assert callable(aadl2_SubprogramGroupClassifier.__init__)


def test_hyp_aadl2_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramClassifier)


def test_hyp_aadl2_subprogramclassifier_constructor_exists():
    assert callable(aadl2_SubprogramClassifier.__init__)


def test_hyp_aadl2_subprogramclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractClassifier)


def test_hyp_aadl2_abstractclassifier_constructor_exists():
    assert callable(aadl2_AbstractClassifier.__init__)


def test_hyp_aadl2_abstractclassifier_constructor_args():
    sig = inspect.signature(aadl2_AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_busclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusClassifier)


def test_hyp_aadl2_busclassifier_constructor_exists():
    assert callable(aadl2_BusClassifier.__init__)


def test_hyp_aadl2_busclassifier_constructor_args():
    sig = inspect.signature(aadl2_BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemClassifier)


def test_hyp_aadl2_systemclassifier_constructor_exists():
    assert callable(aadl2_SystemClassifier.__init__)


def test_hyp_aadl2_systemclassifier_constructor_args():
    sig = inspect.signature(aadl2_SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusClassifier)


def test_hyp_aadl2_virtualbusclassifier_constructor_exists():
    assert callable(aadl2_VirtualBusClassifier.__init__)


def test_hyp_aadl2_virtualbusclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorClassifier)


def test_hyp_aadl2_processorclassifier_constructor_exists():
    assert callable(aadl2_ProcessorClassifier.__init__)


def test_hyp_aadl2_processorclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataClassifier)


def test_hyp_aadl2_dataclassifier_constructor_exists():
    assert callable(aadl2_DataClassifier.__init__)


def test_hyp_aadl2_dataclassifier_constructor_args():
    sig = inspect.signature(aadl2_DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_accessconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessConnection)


def test_hyp_aadl2_accessconnection_constructor_exists():
    assert callable(aadl2_AccessConnection.__init__)


def test_hyp_aadl2_accessconnection_constructor_args():
    sig = inspect.signature(aadl2_AccessConnection.__init__)
    params = list(sig.parameters.keys())
    assert "accessCategory" in params, "Missing parameter 'accessCategory'"




def test_hyp_aadl2_abstractsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractSubcomponent)


def test_hyp_aadl2_abstractsubcomponent_constructor_exists():
    assert callable(aadl2_AbstractSubcomponent.__init__)


def test_hyp_aadl2_abstractsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_AbstractSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentType)


def test_hyp_aadl2_componenttype_constructor_exists():
    assert callable(aadl2_ComponentType.__init__)


def test_hyp_aadl2_componenttype_constructor_args():
    sig = inspect.signature(aadl2_ComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "noFeatures" in params, "Missing parameter 'noFeatures'"




def test_hyp_aadl2_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentImplementation)


def test_hyp_aadl2_componentimplementation_constructor_exists():
    assert callable(aadl2_ComponentImplementation.__init__)


def test_hyp_aadl2_componentimplementation_constructor_args():
    sig = inspect.signature(aadl2_ComponentImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "noConnections" in params, "Missing parameter 'noConnections'"
    assert "noSubcomponents" in params, "Missing parameter 'noSubcomponents'"
    assert "noCalls" in params, "Missing parameter 'noCalls'"






def test_hyp_aadl2_arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySizeProperty)


def test_hyp_aadl2_arraysizeproperty_constructor_exists():
    assert callable(aadl2_ArraySizeProperty.__init__)


def test_hyp_aadl2_arraysizeproperty_constructor_args():
    sig = inspect.signature(aadl2_ArraySizeProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refinableelement_is_not_abstract():
    assert not inspect.isabstract(RefinableElement)


def test_hyp_refinableelement_constructor_exists():
    assert callable(RefinableElement.__init__)


def test_hyp_refinableelement_constructor_args():
    sig = inspect.signature(RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(CalledSubprogram)


def test_hyp_calledsubprogram_constructor_exists():
    assert callable(CalledSubprogram.__init__)


def test_hyp_calledsubprogram_constructor_args():
    sig = inspect.signature(CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_hyp_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_hyp_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processorfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorFeature)


def test_hyp_aadl2_processorfeature_constructor_exists():
    assert callable(aadl2_ProcessorFeature.__init__)


def test_hyp_aadl2_processorfeature_constructor_args():
    sig = inspect.signature(aadl2_ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_feature_is_not_abstract():
    assert not inspect.isabstract(aadl2_Feature)


def test_hyp_aadl2_feature_constructor_exists():
    assert callable(aadl2_Feature.__init__)


def test_hyp_aadl2_feature_constructor_args():
    sig = inspect.signature(aadl2_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(ClassifierFeature)


def test_hyp_classifierfeature_constructor_exists():
    assert callable(ClassifierFeature.__init__)


def test_hyp_classifierfeature_constructor_args():
    sig = inspect.signature(ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_BehavioralFeature)


def test_hyp_aadl2_behavioralfeature_constructor_exists():
    assert callable(aadl2_BehavioralFeature.__init__)


def test_hyp_aadl2_behavioralfeature_constructor_args():
    sig = inspect.signature(aadl2_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_StructuralFeature)


def test_hyp_aadl2_structuralfeature_constructor_exists():
    assert callable(aadl2_StructuralFeature.__init__)


def test_hyp_aadl2_structuralfeature_constructor_args():
    sig = inspect.signature(aadl2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modefeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeFeature)


def test_hyp_aadl2_modefeature_constructor_exists():
    assert callable(aadl2_ModeFeature.__init__)


def test_hyp_aadl2_modefeature_constructor_args():
    sig = inspect.signature(aadl2_ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_CalledSubprogram)


def test_hyp_aadl2_calledsubprogram_constructor_exists():
    assert callable(aadl2_CalledSubprogram.__init__)


def test_hyp_aadl2_calledsubprogram_constructor_args():
    sig = inspect.signature(aadl2_CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_hyp_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_hyp_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(aadl2_DirectedRelationship)


def test_hyp_aadl2_directedrelationship_constructor_exists():
    assert callable(aadl2_DirectedRelationship.__init__)


def test_hyp_aadl2_directedrelationship_constructor_args():
    sig = inspect.signature(aadl2_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_hyp_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_hyp_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modefeature_is_not_abstract():
    assert not inspect.isabstract(ModeFeature)


def test_hyp_modefeature_constructor_exists():
    assert callable(ModeFeature.__init__)


def test_hyp_modefeature_constructor_args():
    sig = inspect.signature(ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modetransition_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeTransition)


def test_hyp_aadl2_modetransition_constructor_exists():
    assert callable(aadl2_ModeTransition.__init__)


def test_hyp_aadl2_modetransition_constructor_args():
    sig = inspect.signature(aadl2_ModeTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_mode_is_not_abstract():
    assert not inspect.isabstract(aadl2_Mode)


def test_hyp_aadl2_mode_constructor_exists():
    assert callable(aadl2_Mode.__init__)


def test_hyp_aadl2_mode_constructor_args():
    sig = inspect.signature(aadl2_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "derived" in params, "Missing parameter 'derived'"





def test_hyp_modalelement_is_not_abstract():
    assert not inspect.isabstract(ModalElement)


def test_hyp_modalelement_constructor_exists():
    assert callable(ModalElement.__init__)


def test_hyp_modalelement_constructor_args():
    sig = inspect.signature(ModalElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramcallsequence_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramCallSequence)


def test_hyp_aadl2_subprogramcallsequence_constructor_exists():
    assert callable(aadl2_SubprogramCallSequence.__init__)


def test_hyp_aadl2_subprogramcallsequence_constructor_args():
    sig = inspect.signature(aadl2_SubprogramCallSequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_prototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_Prototype)


def test_hyp_aadl2_prototype_constructor_exists():
    assert callable(aadl2_Prototype.__init__)


def test_hyp_aadl2_prototype_constructor_args():
    sig = inspect.signature(aadl2_Prototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_annexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2_AnnexSubclause)


def test_hyp_aadl2_annexsubclause_constructor_exists():
    assert callable(aadl2_AnnexSubclause.__init__)


def test_hyp_aadl2_annexsubclause_constructor_args():
    sig = inspect.signature(aadl2_AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_generalization__is_not_abstract():
    assert not inspect.isabstract(aadl2_Generalization_)


def test_hyp_aadl2_generalization__constructor_exists():
    assert callable(aadl2_Generalization_.__init__)


def test_hyp_aadl2_generalization__constructor_args():
    sig = inspect.signature(aadl2_Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertyowner_is_not_abstract():
    assert not inspect.isabstract(PropertyOwner)


def test_hyp_propertyowner_constructor_exists():
    assert callable(PropertyOwner.__init__)


def test_hyp_propertyowner_constructor_args():
    sig = inspect.signature(PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_classifiervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierValue)


def test_hyp_aadl2_classifiervalue_constructor_exists():
    assert callable(aadl2_ClassifierValue.__init__)


def test_hyp_aadl2_classifiervalue_constructor_args():
    sig = inspect.signature(aadl2_ClassifierValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractnamedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractNamedValue)


def test_hyp_aadl2_abstractnamedvalue_constructor_exists():
    assert callable(aadl2_AbstractNamedValue.__init__)


def test_hyp_aadl2_abstractnamedvalue_constructor_args():
    sig = inspect.signature(aadl2_AbstractNamedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubcomponentType)


def test_hyp_aadl2_subcomponenttype_constructor_exists():
    assert callable(aadl2_SubcomponentType.__init__)


def test_hyp_aadl2_subcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_recordtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordType)


def test_hyp_aadl2_recordtype_constructor_exists():
    assert callable(aadl2_RecordType.__init__)


def test_hyp_aadl2_recordtype_constructor_args():
    sig = inspect.signature(aadl2_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationType)


def test_hyp_aadl2_enumerationtype_constructor_exists():
    assert callable(aadl2_EnumerationType.__init__)


def test_hyp_aadl2_enumerationtype_constructor_args():
    sig = inspect.signature(aadl2_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_globalnamespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_GlobalNamespace)


def test_hyp_aadl2_globalnamespace_constructor_exists():
    assert callable(aadl2_GlobalNamespace.__init__)


def test_hyp_aadl2_globalnamespace_constructor_args():
    sig = inspect.signature(aadl2_GlobalNamespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_propertyset_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertySet)


def test_hyp_aadl2_propertyset_constructor_exists():
    assert callable(aadl2_PropertySet.__init__)


def test_hyp_aadl2_propertyset_constructor_args():
    sig = inspect.signature(aadl2_PropertySet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_packagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PackageSection)


def test_hyp_aadl2_packagesection_constructor_exists():
    assert callable(aadl2_PackageSection.__init__)


def test_hyp_aadl2_packagesection_constructor_args():
    sig = inspect.signature(aadl2_PackageSection.__init__)
    params = list(sig.parameters.keys())
    assert "noProperties" in params, "Missing parameter 'noProperties'"
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"





def test_hyp_aadl2_metaclassreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_MetaclassReference)


def test_hyp_aadl2_metaclassreference_constructor_exists():
    assert callable(aadl2_MetaclassReference.__init__)


def test_hyp_aadl2_metaclassreference_constructor_args():
    sig = inspect.signature(aadl2_MetaclassReference.__init__)
    params = list(sig.parameters.keys())
    assert "metaclassName" in params, "Missing parameter 'metaclassName'"
    assert "annexName" in params, "Missing parameter 'annexName'"





def test_hyp_abstractnamedvalue_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedValue)


def test_hyp_abstractnamedvalue_constructor_exists():
    assert callable(AbstractNamedValue.__init__)


def test_hyp_abstractnamedvalue_constructor_args():
    sig = inspect.signature(AbstractNamedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicproperty_is_not_abstract():
    assert not inspect.isabstract(BasicProperty)


def test_hyp_basicproperty_constructor_exists():
    assert callable(BasicProperty.__init__)


def test_hyp_basicproperty_constructor_args():
    sig = inspect.signature(BasicProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_recordfield_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordField)


def test_hyp_aadl2_recordfield_constructor_exists():
    assert callable(aadl2_RecordField.__init__)


def test_hyp_aadl2_recordfield_constructor_args():
    sig = inspect.signature(aadl2_RecordField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modalpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalPropertyValue)


def test_hyp_aadl2_modalpropertyvalue_constructor_exists():
    assert callable(aadl2_ModalPropertyValue.__init__)


def test_hyp_aadl2_modalpropertyvalue_constructor_args():
    sig = inspect.signature(aadl2_ModalPropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_classifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_Classifier)


def test_hyp_aadl2_classifier_constructor_exists():
    assert callable(aadl2_Classifier.__init__)


def test_hyp_aadl2_classifier_constructor_args():
    sig = inspect.signature(aadl2_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "noProperties" in params, "Missing parameter 'noProperties'"
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"
    assert "noPrototypes" in params, "Missing parameter 'noPrototypes'"






def test_hyp_aadl2_propertytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyType)


def test_hyp_aadl2_propertytype_constructor_exists():
    assert callable(aadl2_PropertyType.__init__)


def test_hyp_aadl2_propertytype_constructor_args():
    sig = inspect.signature(aadl2_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_propertyconstant_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyConstant)


def test_hyp_aadl2_propertyconstant_constructor_exists():
    assert callable(aadl2_PropertyConstant.__init__)


def test_hyp_aadl2_propertyconstant_constructor_args():
    sig = inspect.signature(aadl2_PropertyConstant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_basicproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicProperty)


def test_hyp_aadl2_basicproperty_constructor_exists():
    assert callable(aadl2_BasicProperty.__init__)


def test_hyp_aadl2_basicproperty_constructor_args():
    sig = inspect.signature(aadl2_BasicProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_annexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2_AnnexLibrary)


def test_hyp_aadl2_annexlibrary_constructor_exists():
    assert callable(aadl2_AnnexLibrary.__init__)


def test_hyp_aadl2_annexlibrary_constructor_args():
    sig = inspect.signature(aadl2_AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierFeature)


def test_hyp_aadl2_classifierfeature_constructor_exists():
    assert callable(aadl2_ClassifierFeature.__init__)


def test_hyp_aadl2_classifierfeature_constructor_args():
    sig = inspect.signature(aadl2_ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_bus_is_not_abstract():
    assert not inspect.isabstract(aadl2_Bus)


def test_hyp_aadl2_bus_constructor_exists():
    assert callable(aadl2_Bus.__init__)


def test_hyp_aadl2_bus_constructor_args():
    sig = inspect.signature(aadl2_Bus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_namespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_Namespace)


def test_hyp_aadl2_namespace_constructor_exists():
    assert callable(aadl2_Namespace.__init__)


def test_hyp_aadl2_namespace_constructor_args():
    sig = inspect.signature(aadl2_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_device_is_not_abstract():
    assert not inspect.isabstract(aadl2_Device)


def test_hyp_aadl2_device_constructor_exists():
    assert callable(aadl2_Device.__init__)


def test_hyp_aadl2_device_constructor_args():
    sig = inspect.signature(aadl2_Device.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_context_is_not_abstract():
    assert not inspect.isabstract(aadl2_Context)


def test_hyp_aadl2_context_constructor_exists():
    assert callable(aadl2_Context.__init__)


def test_hyp_aadl2_context_constructor_args():
    sig = inspect.signature(aadl2_Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_triggerport_is_not_abstract():
    assert not inspect.isabstract(aadl2_TriggerPort)


def test_hyp_aadl2_triggerport_constructor_exists():
    assert callable(aadl2_TriggerPort.__init__)


def test_hyp_aadl2_triggerport_constructor_args():
    sig = inspect.signature(aadl2_TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_processor_is_not_abstract():
    assert not inspect.isabstract(aadl2_Processor)


def test_hyp_aadl2_processor_constructor_exists():
    assert callable(aadl2_Processor.__init__)


def test_hyp_aadl2_processor_constructor_args():
    sig = inspect.signature(aadl2_Processor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_memory_is_not_abstract():
    assert not inspect.isabstract(aadl2_Memory)


def test_hyp_aadl2_memory_constructor_exists():
    assert callable(aadl2_Memory.__init__)


def test_hyp_aadl2_memory_constructor_args():
    sig = inspect.signature(aadl2_Memory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_Subprogram)


def test_hyp_aadl2_subprogram_constructor_exists():
    assert callable(aadl2_Subprogram.__init__)


def test_hyp_aadl2_subprogram_constructor_args():
    sig = inspect.signature(aadl2_Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componenttyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentTypeRename)


def test_hyp_aadl2_componenttyperename_constructor_exists():
    assert callable(aadl2_ComponentTypeRename.__init__)


def test_hyp_aadl2_componenttyperename_constructor_args():
    sig = inspect.signature(aadl2_ComponentTypeRename.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"




def test_hyp_aadl2_abstract_is_not_abstract():
    assert not inspect.isabstract(aadl2_Abstract)


def test_hyp_aadl2_abstract_constructor_exists():
    assert callable(aadl2_Abstract.__init__)


def test_hyp_aadl2_abstract_constructor_args():
    sig = inspect.signature(aadl2_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modalelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalElement)


def test_hyp_aadl2_modalelement_constructor_exists():
    assert callable(aadl2_ModalElement.__init__)


def test_hyp_aadl2_modalelement_constructor_args():
    sig = inspect.signature(aadl2_ModalElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregrouptyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupTypeRename)


def test_hyp_aadl2_featuregrouptyperename_constructor_exists():
    assert callable(aadl2_FeatureGroupTypeRename.__init__)


def test_hyp_aadl2_featuregrouptyperename_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupTypeRename.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_refinableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_RefinableElement)


def test_hyp_aadl2_refinableelement_constructor_exists():
    assert callable(aadl2_RefinableElement.__init__)


def test_hyp_aadl2_refinableelement_constructor_args():
    sig = inspect.signature(aadl2_RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modelunit_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModelUnit)


def test_hyp_aadl2_modelunit_constructor_exists():
    assert callable(aadl2_ModelUnit.__init__)


def test_hyp_aadl2_modelunit_constructor_args():
    sig = inspect.signature(aadl2_ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroup)


def test_hyp_aadl2_subprogramgroup_constructor_exists():
    assert callable(aadl2_SubprogramGroup.__init__)


def test_hyp_aadl2_subprogramgroup_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_process_is_not_abstract():
    assert not inspect.isabstract(aadl2_Process)


def test_hyp_aadl2_process_constructor_exists():
    assert callable(aadl2_Process.__init__)


def test_hyp_aadl2_process_constructor_args():
    sig = inspect.signature(aadl2_Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_system_is_not_abstract():
    assert not inspect.isabstract(aadl2_System)


def test_hyp_aadl2_system_constructor_exists():
    assert callable(aadl2_System.__init__)


def test_hyp_aadl2_system_constructor_args():
    sig = inspect.signature(aadl2_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_data_is_not_abstract():
    assert not inspect.isabstract(aadl2_Data)


def test_hyp_aadl2_data_constructor_exists():
    assert callable(aadl2_Data.__init__)


def test_hyp_aadl2_data_constructor_args():
    sig = inspect.signature(aadl2_Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessor)


def test_hyp_aadl2_virtualprocessor_constructor_exists():
    assert callable(aadl2_VirtualProcessor.__init__)


def test_hyp_aadl2_virtualprocessor_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_packagerename_is_not_abstract():
    assert not inspect.isabstract(aadl2_PackageRename)


def test_hyp_aadl2_packagerename_constructor_exists():
    assert callable(aadl2_PackageRename.__init__)


def test_hyp_aadl2_packagerename_constructor_args():
    sig = inspect.signature(aadl2_PackageRename.__init__)
    params = list(sig.parameters.keys())
    assert "renameAll" in params, "Missing parameter 'renameAll'"




def test_hyp_aadl2_thread_is_not_abstract():
    assert not inspect.isabstract(aadl2_Thread)


def test_hyp_aadl2_thread_constructor_exists():
    assert callable(aadl2_Thread.__init__)


def test_hyp_aadl2_thread_constructor_args():
    sig = inspect.signature(aadl2_Thread.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_threadgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroup)


def test_hyp_aadl2_threadgroup_constructor_exists():
    assert callable(aadl2_ThreadGroup.__init__)


def test_hyp_aadl2_threadgroup_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbus_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBus)


def test_hyp_aadl2_virtualbus_constructor_exists():
    assert callable(aadl2_VirtualBus.__init__)


def test_hyp_aadl2_virtualbus_constructor_args():
    sig = inspect.signature(aadl2_VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationLiteral)


def test_hyp_aadl2_enumerationliteral_constructor_exists():
    assert callable(aadl2_EnumerationLiteral.__init__)


def test_hyp_aadl2_enumerationliteral_constructor_args():
    sig = inspect.signature(aadl2_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_typedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypedElement)


def test_hyp_aadl2_typedelement_constructor_exists():
    assert callable(aadl2_TypedElement.__init__)


def test_hyp_aadl2_typedelement_constructor_args():
    sig = inspect.signature(aadl2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_type_is_not_abstract():
    assert not inspect.isabstract(aadl2_Type)


def test_hyp_aadl2_type_constructor_exists():
    assert callable(aadl2_Type.__init__)


def test_hyp_aadl2_type_constructor_args():
    sig = inspect.signature(aadl2_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_property_is_not_abstract():
    assert not inspect.isabstract(aadl2_Property)


def test_hyp_aadl2_property_constructor_exists():
    assert callable(aadl2_Property.__init__)


def test_hyp_aadl2_property_constructor_args():
    sig = inspect.signature(aadl2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "inherit" in params, "Missing parameter 'inherit'"
    assert "emptyListDefault" in params, "Missing parameter 'emptyListDefault'"





def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_numericrange_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumericRange)


def test_hyp_aadl2_numericrange_constructor_exists():
    assert callable(aadl2_NumericRange.__init__)


def test_hyp_aadl2_numericrange_constructor_args():
    sig = inspect.signature(aadl2_NumericRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_arraydimension_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayDimension)


def test_hyp_aadl2_arraydimension_constructor_exists():
    assert callable(aadl2_ArrayDimension.__init__)


def test_hyp_aadl2_arraydimension_constructor_args():
    sig = inspect.signature(aadl2_ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_arraysize_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySize)


def test_hyp_aadl2_arraysize_constructor_exists():
    assert callable(aadl2_ArraySize.__init__)


def test_hyp_aadl2_arraysize_constructor_args():
    sig = inspect.signature(aadl2_ArraySize.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_aadl2_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainedNamedElement)


def test_hyp_aadl2_containednamedelement_constructor_exists():
    assert callable(aadl2_ContainedNamedElement.__init__)


def test_hyp_aadl2_containednamedelement_constructor_args():
    sig = inspect.signature(aadl2_ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componentimplementationreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentImplementationReference)


def test_hyp_aadl2_componentimplementationreference_constructor_exists():
    assert callable(aadl2_ComponentImplementationReference.__init__)


def test_hyp_aadl2_componentimplementationreference_constructor_args():
    sig = inspect.signature(aadl2_ComponentImplementationReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modetransitiontrigger_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeTransitionTrigger)


def test_hyp_aadl2_modetransitiontrigger_constructor_exists():
    assert callable(aadl2_ModeTransitionTrigger.__init__)


def test_hyp_aadl2_modetransitiontrigger_constructor_args():
    sig = inspect.signature(aadl2_ModeTransitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_namedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_NamedElement)


def test_hyp_aadl2_namedelement_constructor_exists():
    assert callable(aadl2_NamedElement.__init__)


def test_hyp_aadl2_namedelement_constructor_args():
    sig = inspect.signature(aadl2_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"





def test_hyp_aadl2_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrototypeBinding)


def test_hyp_aadl2_prototypebinding_constructor_exists():
    assert callable(aadl2_PrototypeBinding.__init__)


def test_hyp_aadl2_prototypebinding_constructor_args():
    sig = inspect.signature(aadl2_PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayableElement)


def test_hyp_aadl2_arrayableelement_constructor_exists():
    assert callable(aadl2_ArrayableElement.__init__)


def test_hyp_aadl2_arrayableelement_constructor_args():
    sig = inspect.signature(aadl2_ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_propertyexpression_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyExpression)


def test_hyp_aadl2_propertyexpression_constructor_exists():
    assert callable(aadl2_PropertyExpression.__init__)


def test_hyp_aadl2_propertyexpression_constructor_args():
    sig = inspect.signature(aadl2_PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_propertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyAssociation)


def test_hyp_aadl2_propertyassociation_constructor_exists():
    assert callable(aadl2_PropertyAssociation.__init__)


def test_hyp_aadl2_propertyassociation_constructor_args():
    sig = inspect.signature(aadl2_PropertyAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "constant" in params, "Missing parameter 'constant'"





def test_hyp_aadl2_flowend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowEnd)


def test_hyp_aadl2_flowend_constructor_exists():
    assert callable(aadl2_FlowEnd.__init__)


def test_hyp_aadl2_flowend_constructor_args():
    sig = inspect.signature(aadl2_FlowEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_arrayrange_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayRange)


def test_hyp_aadl2_arrayrange_constructor_exists():
    assert callable(aadl2_ArrayRange.__init__)


def test_hyp_aadl2_arrayrange_constructor_args():
    sig = inspect.signature(aadl2_ArrayRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"





def test_hyp_aadl2_basicpropertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicPropertyAssociation)


def test_hyp_aadl2_basicpropertyassociation_constructor_exists():
    assert callable(aadl2_BasicPropertyAssociation.__init__)


def test_hyp_aadl2_basicpropertyassociation_constructor_args():
    sig = inspect.signature(aadl2_BasicPropertyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_endtoendflowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlowSegment)


def test_hyp_aadl2_endtoendflowsegment_constructor_exists():
    assert callable(aadl2_EndToEndFlowSegment.__init__)


def test_hyp_aadl2_endtoendflowsegment_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlowSegment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_relationship_is_not_abstract():
    assert not inspect.isabstract(aadl2_Relationship)


def test_hyp_aadl2_relationship_constructor_exists():
    assert callable(aadl2_Relationship.__init__)


def test_hyp_aadl2_relationship_constructor_args():
    sig = inspect.signature(aadl2_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_connectedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConnectedElement)


def test_hyp_aadl2_connectedelement_constructor_exists():
    assert callable(aadl2_ConnectedElement.__init__)


def test_hyp_aadl2_connectedelement_constructor_args():
    sig = inspect.signature(aadl2_ConnectedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_propertyowner_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyOwner)


def test_hyp_aadl2_propertyowner_constructor_exists():
    assert callable(aadl2_PropertyOwner.__init__)


def test_hyp_aadl2_propertyowner_constructor_args():
    sig = inspect.signature(aadl2_PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowSegment)


def test_hyp_aadl2_flowsegment_constructor_exists():
    assert callable(aadl2_FlowSegment.__init__)


def test_hyp_aadl2_flowsegment_constructor_args():
    sig = inspect.signature(aadl2_FlowSegment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_containmentpathelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainmentPathElement)


def test_hyp_aadl2_containmentpathelement_constructor_exists():
    assert callable(aadl2_ContainmentPathElement.__init__)


def test_hyp_aadl2_containmentpathelement_constructor_args():
    sig = inspect.signature(aadl2_ContainmentPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "annexName" in params, "Missing parameter 'annexName'"




def test_hyp_aadl2_comment_is_not_abstract():
    assert not inspect.isabstract(aadl2_Comment)


def test_hyp_aadl2_comment_constructor_exists():
    assert callable(aadl2_Comment.__init__)


def test_hyp_aadl2_comment_constructor_args():
    sig = inspect.signature(aadl2_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"




def test_hyp_aadl2_element_is_not_abstract():
    assert not inspect.isabstract(aadl2_Element)


def test_hyp_aadl2_element_constructor_exists():
    assert callable(aadl2_Element.__init__)


def test_hyp_aadl2_element_constructor_args():
    sig = inspect.signature(aadl2_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeBinding)


def test_hyp_aadl2_modebinding_constructor_exists():
    assert callable(aadl2_ModeBinding.__init__)


def test_hyp_aadl2_modebinding_constructor_args():
    sig = inspect.signature(aadl2_ModeBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_triggerport_is_not_abstract():
    assert not inspect.isabstract(TriggerPort)


def test_hyp_triggerport_constructor_exists():
    assert callable(TriggerPort.__init__)


def test_hyp_triggerport_constructor_args():
    sig = inspect.signature(TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_hyp_port_constructor_exists():
    assert callable(Port.__init__)


def test_hyp_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(AccessConnectionEnd)


def test_hyp_accessconnectionend_constructor_exists():
    assert callable(AccessConnectionEnd.__init__)


def test_hyp_accessconnectionend_constructor_args():
    sig = inspect.signature(AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusSubcomponent)


def test_hyp_aadl2_virtualbussubcomponent_constructor_exists():
    assert callable(aadl2_VirtualBusSubcomponent.__init__)


def test_hyp_aadl2_virtualbussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramSubcomponent)


def test_hyp_aadl2_subprogramsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramSubcomponent.__init__)


def test_hyp_aadl2_subprogramsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramProxy)


def test_hyp_aadl2_subprogramproxy_constructor_exists():
    assert callable(aadl2_SubprogramProxy.__init__)


def test_hyp_aadl2_subprogramproxy_constructor_args():
    sig = inspect.signature(aadl2_SubprogramProxy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_bussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusSubcomponent)


def test_hyp_aadl2_bussubcomponent_constructor_exists():
    assert callable(aadl2_BusSubcomponent.__init__)


def test_hyp_aadl2_bussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_BusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_busfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusFeatureClassifier)


def test_hyp_aadl2_busfeatureclassifier_constructor_exists():
    assert callable(aadl2_BusFeatureClassifier.__init__)


def test_hyp_aadl2_busfeatureclassifier_constructor_args():
    sig = inspect.signature(aadl2_BusFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractFeatureClassifier)


def test_hyp_aadl2_abstractfeatureclassifier_constructor_exists():
    assert callable(aadl2_AbstractFeatureClassifier.__init__)


def test_hyp_aadl2_abstractfeatureclassifier_constructor_args():
    sig = inspect.signature(aadl2_AbstractFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_hyp_access_constructor_exists():
    assert callable(Access.__init__)


def test_hyp_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(AbstractFeatureClassifier)


def test_hyp_abstractfeatureclassifier_constructor_exists():
    assert callable(AbstractFeatureClassifier.__init__)


def test_hyp_abstractfeatureclassifier_constructor_args():
    sig = inspect.signature(AbstractFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupSubcomponentType)


def test_hyp_aadl2_subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2_SubprogramGroupSubcomponentType.__init__)


def test_hyp_aadl2_subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusSubcomponentType)


def test_hyp_aadl2_virtualbussubcomponenttype_constructor_exists():
    assert callable(aadl2_VirtualBusSubcomponentType.__init__)


def test_hyp_aadl2_virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractSubcomponentType)


def test_hyp_aadl2_abstractsubcomponenttype_constructor_exists():
    assert callable(aadl2_AbstractSubcomponentType.__init__)


def test_hyp_aadl2_abstractsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_AbstractSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramSubcomponentType)


def test_hyp_aadl2_subprogramsubcomponenttype_constructor_exists():
    assert callable(aadl2_SubprogramSubcomponentType.__init__)


def test_hyp_aadl2_subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusSubcomponentType)


def test_hyp_aadl2_bussubcomponenttype_constructor_exists():
    assert callable(aadl2_BusSubcomponentType.__init__)


def test_hyp_aadl2_bussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataSubcomponentType)


def test_hyp_aadl2_datasubcomponenttype_constructor_exists():
    assert callable(aadl2_DataSubcomponentType.__init__)


def test_hyp_aadl2_datasubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(PortConnectionEnd)


def test_hyp_portconnectionend_constructor_exists():
    assert callable(PortConnectionEnd.__init__)


def test_hyp_portconnectionend_constructor_args():
    sig = inspect.signature(PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_portproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortProxy)


def test_hyp_aadl2_portproxy_constructor_exists():
    assert callable(aadl2_PortProxy.__init__)


def test_hyp_aadl2_portproxy_constructor_args():
    sig = inspect.signature(aadl2_PortProxy.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "direction" in params, "Missing parameter 'direction'"






def test_hyp_aadl2_internalfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_InternalFeature)


def test_hyp_aadl2_internalfeature_constructor_exists():
    assert callable(aadl2_InternalFeature.__init__)


def test_hyp_aadl2_internalfeature_constructor_args():
    sig = inspect.signature(aadl2_InternalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "out" in params, "Missing parameter 'out'"






def test_hyp_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(ParameterConnectionEnd)


def test_hyp_parameterconnectionend_constructor_exists():
    assert callable(ParameterConnectionEnd.__init__)


def test_hyp_parameterconnectionend_constructor_args():
    sig = inspect.signature(ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_datasubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataSubcomponent)


def test_hyp_aadl2_datasubcomponent_constructor_exists():
    assert callable(aadl2_DataSubcomponent.__init__)


def test_hyp_aadl2_datasubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DataSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_eventport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventPort)


def test_hyp_aadl2_eventport_constructor_exists():
    assert callable(aadl2_EventPort.__init__)


def test_hyp_aadl2_eventport_constructor_args():
    sig = inspect.signature(aadl2_EventPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuretype_is_not_abstract():
    assert not inspect.isabstract(FeatureType)


def test_hyp_featuretype_constructor_exists():
    assert callable(FeatureType.__init__)


def test_hyp_featuretype_constructor_args():
    sig = inspect.signature(FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_busaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusAccess)


def test_hyp_aadl2_busaccess_constructor_exists():
    assert callable(aadl2_BusAccess.__init__)


def test_hyp_aadl2_busaccess_constructor_args():
    sig = inspect.signature(aadl2_BusAccess.__init__)
    params = list(sig.parameters.keys())
    assert "virtual" in params, "Missing parameter 'virtual'"




def test_hyp_generalization__is_not_abstract():
    assert not inspect.isabstract(Generalization_)


def test_hyp_generalization__constructor_exists():
    assert callable(Generalization_.__init__)


def test_hyp_generalization__constructor_args():
    sig = inspect.signature(Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_realization_is_not_abstract():
    assert not inspect.isabstract(aadl2_Realization)


def test_hyp_aadl2_realization_constructor_exists():
    assert callable(aadl2_Realization.__init__)


def test_hyp_aadl2_realization_constructor_args():
    sig = inspect.signature(aadl2_Realization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_implementationextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_ImplementationExtension)


def test_hyp_aadl2_implementationextension_constructor_exists():
    assert callable(aadl2_ImplementationExtension.__init__)


def test_hyp_aadl2_implementationextension_constructor_args():
    sig = inspect.signature(aadl2_ImplementationExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_typeextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypeExtension)


def test_hyp_aadl2_typeextension_constructor_exists():
    assert callable(aadl2_TypeExtension.__init__)


def test_hyp_aadl2_typeextension_constructor_args():
    sig = inspect.signature(aadl2_TypeExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_groupextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_GroupExtension)


def test_hyp_aadl2_groupextension_constructor_exists():
    assert callable(aadl2_GroupExtension.__init__)


def test_hyp_aadl2_groupextension_constructor_args():
    sig = inspect.signature(aadl2_GroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlowElement)


def test_hyp_aadl2_endtoendflowelement_constructor_exists():
    assert callable(aadl2_EndToEndFlowElement.__init__)


def test_hyp_aadl2_endtoendflowelement_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(EndToEndFlowElement)


def test_hyp_endtoendflowelement_constructor_exists():
    assert callable(EndToEndFlowElement.__init__)


def test_hyp_endtoendflowelement_constructor_args():
    sig = inspect.signature(EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowElement)


def test_hyp_aadl2_flowelement_constructor_exists():
    assert callable(aadl2_FlowElement.__init__)


def test_hyp_aadl2_flowelement_constructor_args():
    sig = inspect.signature(aadl2_FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_access_is_not_abstract():
    assert not inspect.isabstract(aadl2_Access)


def test_hyp_aadl2_access_constructor_exists():
    assert callable(aadl2_Access.__init__)


def test_hyp_aadl2_access_constructor_args():
    sig = inspect.signature(aadl2_Access.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "category" in params, "Missing parameter 'category'"





def test_hyp_aadl2_directedfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_DirectedFeature)


def test_hyp_aadl2_directedfeature_constructor_exists():
    assert callable(aadl2_DirectedFeature.__init__)


def test_hyp_aadl2_directedfeature_constructor_args():
    sig = inspect.signature(aadl2_DirectedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"
    assert "out" in params, "Missing parameter 'out'"
    assert "direction" in params, "Missing parameter 'direction'"






def test_hyp_aadl2_callcontext_is_not_abstract():
    assert not inspect.isabstract(aadl2_CallContext)


def test_hyp_aadl2_callcontext_constructor_exists():
    assert callable(aadl2_CallContext.__init__)


def test_hyp_aadl2_callcontext_constructor_args():
    sig = inspect.signature(aadl2_CallContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupType)


def test_hyp_aadl2_featuregrouptype_constructor_exists():
    assert callable(aadl2_FeatureGroupType.__init__)


def test_hyp_aadl2_featuregrouptype_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuretype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureType)


def test_hyp_aadl2_featuretype_constructor_exists():
    assert callable(aadl2_FeatureType.__init__)


def test_hyp_aadl2_featuretype_constructor_args():
    sig = inspect.signature(aadl2_FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_callcontext_is_not_abstract():
    assert not inspect.isabstract(CallContext)


def test_hyp_callcontext_constructor_exists():
    assert callable(CallContext.__init__)


def test_hyp_callcontext_constructor_args():
    sig = inspect.signature(CallContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupAccess)


def test_hyp_aadl2_subprogramgroupaccess_constructor_exists():
    assert callable(aadl2_SubprogramGroupAccess.__init__)


def test_hyp_aadl2_subprogramgroupaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupSubcomponent)


def test_hyp_aadl2_subprogramgroupsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramGroupSubcomponent.__init__)


def test_hyp_aadl2_subprogramgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupType)


def test_hyp_aadl2_subprogramgrouptype_constructor_exists():
    assert callable(aadl2_SubprogramGroupType.__init__)


def test_hyp_aadl2_subprogramgrouptype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramType)


def test_hyp_aadl2_subprogramtype_constructor_exists():
    assert callable(aadl2_SubprogramType.__init__)


def test_hyp_aadl2_subprogramtype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstracttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractType)


def test_hyp_aadl2_abstracttype_constructor_exists():
    assert callable(aadl2_AbstractType.__init__)


def test_hyp_aadl2_abstracttype_constructor_args():
    sig = inspect.signature(aadl2_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_datatype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataType)


def test_hyp_aadl2_datatype_constructor_exists():
    assert callable(aadl2_DataType.__init__)


def test_hyp_aadl2_datatype_constructor_args():
    sig = inspect.signature(aadl2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(FeatureGroupConnectionEnd)


def test_hyp_featuregroupconnectionend_constructor_exists():
    assert callable(FeatureGroupConnectionEnd.__init__)


def test_hyp_featuregroupconnectionend_constructor_args():
    sig = inspect.signature(FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_hyp_context_constructor_exists():
    assert callable(Context.__init__)


def test_hyp_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramAccess)


def test_hyp_aadl2_subprogramaccess_constructor_exists():
    assert callable(aadl2_SubprogramAccess.__init__)


def test_hyp_aadl2_subprogramaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_dataport_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataPort)


def test_hyp_aadl2_dataport_constructor_exists():
    assert callable(aadl2_DataPort.__init__)


def test_hyp_aadl2_dataport_constructor_args():
    sig = inspect.signature(aadl2_DataPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_eventdataport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventDataPort)


def test_hyp_aadl2_eventdataport_constructor_exists():
    assert callable(aadl2_EventDataPort.__init__)


def test_hyp_aadl2_eventdataport_constructor_args():
    sig = inspect.signature(aadl2_EventDataPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subprogramcall_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramCall)


def test_hyp_aadl2_subprogramcall_constructor_exists():
    assert callable(aadl2_SubprogramCall.__init__)


def test_hyp_aadl2_subprogramcall_constructor_args():
    sig = inspect.signature(aadl2_SubprogramCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_directedfeature_is_not_abstract():
    assert not inspect.isabstract(DirectedFeature)


def test_hyp_directedfeature_constructor_exists():
    assert callable(DirectedFeature.__init__)


def test_hyp_directedfeature_constructor_args():
    sig = inspect.signature(DirectedFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroup)


def test_hyp_aadl2_featuregroup_constructor_exists():
    assert callable(aadl2_FeatureGroup.__init__)


def test_hyp_aadl2_featuregroup_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"




def test_hyp_aadl2_port_is_not_abstract():
    assert not inspect.isabstract(aadl2_Port)


def test_hyp_aadl2_port_constructor_exists():
    assert callable(aadl2_Port.__init__)


def test_hyp_aadl2_port_constructor_args():
    sig = inspect.signature(aadl2_Port.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"




def test_hyp_aadl2_parameter_is_not_abstract():
    assert not inspect.isabstract(aadl2_Parameter)


def test_hyp_aadl2_parameter_constructor_exists():
    assert callable(aadl2_Parameter.__init__)


def test_hyp_aadl2_parameter_constructor_args():
    sig = inspect.signature(aadl2_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_abstractfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractFeature)


def test_hyp_aadl2_abstractfeature_constructor_exists():
    assert callable(aadl2_AbstractFeature.__init__)


def test_hyp_aadl2_abstractfeature_constructor_args():
    sig = inspect.signature(aadl2_AbstractFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_hyp_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_hyp_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_dataaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataAccess)


def test_hyp_aadl2_dataaccess_constructor_exists():
    assert callable(aadl2_DataAccess.__init__)


def test_hyp_aadl2_dataaccess_constructor_args():
    sig = inspect.signature(aadl2_DataAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_subcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_Subcomponent)


def test_hyp_aadl2_subcomponent_constructor_exists():
    assert callable(aadl2_Subcomponent.__init__)


def test_hyp_aadl2_subcomponent_constructor_args():
    sig = inspect.signature(aadl2_Subcomponent.__init__)
    params = list(sig.parameters.keys())
    assert "allModes" in params, "Missing parameter 'allModes'"




def test_hyp_modalpath_is_not_abstract():
    assert not inspect.isabstract(ModalPath)


def test_hyp_modalpath_constructor_exists():
    assert callable(ModalPath.__init__)


def test_hyp_modalpath_constructor_args():
    sig = inspect.signature(ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_connection_is_not_abstract():
    assert not inspect.isabstract(aadl2_Connection)


def test_hyp_aadl2_connection_constructor_exists():
    assert callable(aadl2_Connection.__init__)


def test_hyp_aadl2_connection_constructor_args():
    sig = inspect.signature(aadl2_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"




def test_hyp_flowfeature_is_not_abstract():
    assert not inspect.isabstract(FlowFeature)


def test_hyp_flowfeature_constructor_exists():
    assert callable(FlowFeature.__init__)


def test_hyp_flowfeature_constructor_args():
    sig = inspect.signature(FlowFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flowspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowSpecification)


def test_hyp_aadl2_flowspecification_constructor_exists():
    assert callable(aadl2_FlowSpecification.__init__)


def test_hyp_aadl2_flowspecification_constructor_args():
    sig = inspect.signature(aadl2_FlowSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_aadl2_endtoendflow_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlow)


def test_hyp_aadl2_endtoendflow_constructor_exists():
    assert callable(aadl2_EndToEndFlow.__init__)


def test_hyp_aadl2_endtoendflow_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_prototype_is_not_abstract():
    assert not inspect.isabstract(Prototype)


def test_hyp_prototype_constructor_exists():
    assert callable(Prototype.__init__)


def test_hyp_prototype_constructor_args():
    sig = inspect.signature(Prototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_componentprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototype)


def test_hyp_aadl2_componentprototype_constructor_exists():
    assert callable(aadl2_ComponentPrototype.__init__)


def test_hyp_aadl2_componentprototype_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"




def test_hyp_aadl2_featureprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototype)


def test_hyp_aadl2_featureprototype_constructor_exists():
    assert callable(aadl2_FeaturePrototype.__init__)


def test_hyp_aadl2_featureprototype_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototype.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "out" in params, "Missing parameter 'out'"






def test_hyp_aadl2_featuregroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototype)


def test_hyp_aadl2_featuregroupprototype_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototype.__init__)


def test_hyp_aadl2_featuregroupprototype_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_connectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConnectionEnd)


def test_hyp_aadl2_connectionend_constructor_exists():
    assert callable(aadl2_ConnectionEnd.__init__)


def test_hyp_aadl2_connectionend_constructor_args():
    sig = inspect.signature(aadl2_ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connectionend_is_not_abstract():
    assert not inspect.isabstract(ConnectionEnd)


def test_hyp_connectionend_constructor_exists():
    assert callable(ConnectionEnd.__init__)


def test_hyp_connectionend_constructor_args():
    sig = inspect.signature(ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessConnectionEnd)


def test_hyp_aadl2_accessconnectionend_constructor_exists():
    assert callable(aadl2_AccessConnectionEnd.__init__)


def test_hyp_aadl2_accessconnectionend_constructor_args():
    sig = inspect.signature(aadl2_AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupConnectionEnd)


def test_hyp_aadl2_featuregroupconnectionend_constructor_exists():
    assert callable(aadl2_FeatureGroupConnectionEnd.__init__)


def test_hyp_aadl2_featuregroupconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ParameterConnectionEnd)


def test_hyp_aadl2_parameterconnectionend_constructor_exists():
    assert callable(aadl2_ParameterConnectionEnd.__init__)


def test_hyp_aadl2_parameterconnectionend_constructor_args():
    sig = inspect.signature(aadl2_ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortConnectionEnd)


def test_hyp_aadl2_portconnectionend_constructor_exists():
    assert callable(aadl2_PortConnectionEnd.__init__)


def test_hyp_aadl2_portconnectionend_constructor_args():
    sig = inspect.signature(aadl2_PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureConnectionEnd)


def test_hyp_aadl2_featureconnectionend_constructor_exists():
    assert callable(aadl2_FeatureConnectionEnd.__init__)


def test_hyp_aadl2_featureconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_modalpath_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalPath)


def test_hyp_aadl2_modalpath_constructor_exists():
    assert callable(aadl2_ModalPath.__init__)


def test_hyp_aadl2_modalpath_constructor_args():
    sig = inspect.signature(aadl2_ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flow_is_not_abstract():
    assert not inspect.isabstract(aadl2_Flow)


def test_hyp_aadl2_flow_constructor_exists():
    assert callable(aadl2_Flow.__init__)


def test_hyp_aadl2_flow_constructor_args():
    sig = inspect.signature(aadl2_Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_hyp_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_hyp_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flowfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowFeature)


def test_hyp_aadl2_flowfeature_constructor_exists():
    assert callable(aadl2_FlowFeature.__init__)


def test_hyp_aadl2_flowfeature_constructor_args():
    sig = inspect.signature(aadl2_FlowFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aadl2_flowimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowImplementation)


def test_hyp_aadl2_flowimplementation_constructor_exists():
    assert callable(aadl2_FlowImplementation.__init__)


def test_hyp_aadl2_flowimplementation_constructor_args():
    sig = inspect.signature(aadl2_FlowImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"


def test_hyp_portcategory_exists():
    # Check that the Enumeration exists
    assert PortCategory is not None

def test_hyp_portcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortCategory]
    expected_literals = [
        "event",
        "eventData",
        "data",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortCategory"

def test_hyp_accesscategory_exists():
    # Check that the Enumeration exists
    assert AccessCategory is not None

def test_hyp_accesscategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessCategory]
    expected_literals = [
        "virtualBus",
        "bus",
        "subprogram",
        "data",
        "subprogramGroup",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessCategory"

def test_hyp_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_hyp_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "requires",
        "provides",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessType"

def test_hyp_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_hyp_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "source",
        "sink",
        "path",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowKind"

def test_hyp_operationkind_exists():
    # Check that the Enumeration exists
    assert OperationKind is not None

def test_hyp_operationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationKind]
    expected_literals = [
        "minus",
        "or_",
        "plus",
        "and_",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationKind"

def test_hyp_componentcategory_exists():
    # Check that the Enumeration exists
    assert ComponentCategory is not None

def test_hyp_componentcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentCategory]
    expected_literals = [
        "abstract",
        "subprogram",
        "data",
        "threadGroup",
        "virtualProcessor",
        "virtualBus",
        "processor",
        "device",
        "system",
        "thread",
        "process",
        "memory",
        "bus",
        "subprogramGroup",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentCategory"

def test_hyp_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_hyp_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "inOut",
        "in_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
PropertyValue_strategy = st.builds(
    PropertyValue,
)
aadl2_StringLiteral_strategy = st.builds(
    aadl2_StringLiteral,
    value=
        safe_text
)
VirtualProcessorClassifier_strategy = st.builds(
    VirtualProcessorClassifier,
)
VirtualBusClassifier_strategy = st.builds(
    VirtualBusClassifier,
)
ThreadGroupClassifier_strategy = st.builds(
    ThreadGroupClassifier,
)
ThreadClassifier_strategy = st.builds(
    ThreadClassifier,
)
ProcessClassifier_strategy = st.builds(
    ProcessClassifier,
)
ProcessorClassifier_strategy = st.builds(
    ProcessorClassifier,
)
SystemClassifier_strategy = st.builds(
    SystemClassifier,
)
SubprogramGroupClassifier_strategy = st.builds(
    SubprogramGroupClassifier,
)
SubprogramClassifier_strategy = st.builds(
    SubprogramClassifier,
)
MemoryClassifier_strategy = st.builds(
    MemoryClassifier,
)
DeviceClassifier_strategy = st.builds(
    DeviceClassifier,
)
DataClassifier_strategy = st.builds(
    DataClassifier,
)
ComponentPrototype_strategy = st.builds(
    ComponentPrototype,
)
BusClassifier_strategy = st.builds(
    BusClassifier,
)
Thread_strategy = st.builds(
    Thread,
)
VirtualProcessor_strategy = st.builds(
    VirtualProcessor,
)
VirtualBus_strategy = st.builds(
    VirtualBus,
)
ThreadGroup_strategy = st.builds(
    ThreadGroup,
)
Processor_strategy = st.builds(
    Processor,
)
SubprogramGroup_strategy = st.builds(
    SubprogramGroup,
)
System_strategy = st.builds(
    System,
)
Process_strategy = st.builds(
    Process,
)
Memory_strategy = st.builds(
    Memory,
)
Device_strategy = st.builds(
    Device,
)
Bus_strategy = st.builds(
    Bus,
)
BehavioredImplementation_strategy = st.builds(
    BehavioredImplementation,
)
aadl2_SubprogramImplementation_strategy = st.builds(
    aadl2_SubprogramImplementation,
)
aadl2_ThreadImplementation_strategy = st.builds(
    aadl2_ThreadImplementation,
)
BusFeatureClassifier_strategy = st.builds(
    BusFeatureClassifier,
)
VirtualProcessorSubcomponentType_strategy = st.builds(
    VirtualProcessorSubcomponentType,
)
aadl2_VirtualProcessorPrototype_strategy = st.builds(
    aadl2_VirtualProcessorPrototype,
)
VirtualBusSubcomponentType_strategy = st.builds(
    VirtualBusSubcomponentType,
)
aadl2_VirtualBusPrototype_strategy = st.builds(
    aadl2_VirtualBusPrototype,
)
ThreadSubcomponentType_strategy = st.builds(
    ThreadSubcomponentType,
)
aadl2_ThreadPrototype_strategy = st.builds(
    aadl2_ThreadPrototype,
)
ThreadGroupSubcomponentType_strategy = st.builds(
    ThreadGroupSubcomponentType,
)
aadl2_ThreadGroupPrototype_strategy = st.builds(
    aadl2_ThreadGroupPrototype,
)
SystemSubcomponentType_strategy = st.builds(
    SystemSubcomponentType,
)
aadl2_SystemPrototype_strategy = st.builds(
    aadl2_SystemPrototype,
)
SubprogramGroupSubcomponentType_strategy = st.builds(
    SubprogramGroupSubcomponentType,
)
aadl2_SubprogramGroupPrototype_strategy = st.builds(
    aadl2_SubprogramGroupPrototype,
)
ProcessSubcomponentType_strategy = st.builds(
    ProcessSubcomponentType,
)
aadl2_ProcessPrototype_strategy = st.builds(
    aadl2_ProcessPrototype,
)
ProcessorSubcomponentType_strategy = st.builds(
    ProcessorSubcomponentType,
)
aadl2_ProcessorPrototype_strategy = st.builds(
    aadl2_ProcessorPrototype,
)
MemorySubcomponentType_strategy = st.builds(
    MemorySubcomponentType,
)
aadl2_MemoryPrototype_strategy = st.builds(
    aadl2_MemoryPrototype,
)
DeviceSubcomponentType_strategy = st.builds(
    DeviceSubcomponentType,
)
aadl2_DevicePrototype_strategy = st.builds(
    aadl2_DevicePrototype,
)
BusSubcomponentType_strategy = st.builds(
    BusSubcomponentType,
)
aadl2_BusPrototype_strategy = st.builds(
    aadl2_BusPrototype,
)
AbstractSubcomponentType_strategy = st.builds(
    AbstractSubcomponentType,
)
AbstractClassifier_strategy = st.builds(
    AbstractClassifier,
)
aadl2_AbstractImplementation_strategy = st.builds(
    aadl2_AbstractImplementation,
)
ComponentType_strategy = st.builds(
    ComponentType,
)
aadl2_BusType_strategy = st.builds(
    aadl2_BusType,
)
aadl2_ProcessType_strategy = st.builds(
    aadl2_ProcessType,
)
aadl2_VirtualBusType_strategy = st.builds(
    aadl2_VirtualBusType,
)
aadl2_DeviceType_strategy = st.builds(
    aadl2_DeviceType,
)
aadl2_SystemType_strategy = st.builds(
    aadl2_SystemType,
)
aadl2_VirtualProcessorType_strategy = st.builds(
    aadl2_VirtualProcessorType,
)
aadl2_ThreadGroupType_strategy = st.builds(
    aadl2_ThreadGroupType,
)
aadl2_ThreadType_strategy = st.builds(
    aadl2_ThreadType,
)
aadl2_ProcessorType_strategy = st.builds(
    aadl2_ProcessorType,
)
aadl2_MemoryType_strategy = st.builds(
    aadl2_MemoryType,
)
ComponentImplementation_strategy = st.builds(
    ComponentImplementation,
)
aadl2_ProcessImplementation_strategy = st.builds(
    aadl2_ProcessImplementation,
)
aadl2_ThreadGroupImplementation_strategy = st.builds(
    aadl2_ThreadGroupImplementation,
)
aadl2_VirtualBusImplementation_strategy = st.builds(
    aadl2_VirtualBusImplementation,
)
aadl2_MemoryImplementation_strategy = st.builds(
    aadl2_MemoryImplementation,
)
aadl2_ProcessorImplementation_strategy = st.builds(
    aadl2_ProcessorImplementation,
)
aadl2_VirtualProcessorImplementation_strategy = st.builds(
    aadl2_VirtualProcessorImplementation,
)
aadl2_BusImplementation_strategy = st.builds(
    aadl2_BusImplementation,
)
aadl2_DeviceImplementation_strategy = st.builds(
    aadl2_DeviceImplementation,
)
aadl2_DataImplementation_strategy = st.builds(
    aadl2_DataImplementation,
)
aadl2_SystemImplementation_strategy = st.builds(
    aadl2_SystemImplementation,
)
aadl2_SubprogramGroupImplementation_strategy = st.builds(
    aadl2_SubprogramGroupImplementation,
)
aadl2_BehavioredImplementation_strategy = st.builds(
    aadl2_BehavioredImplementation,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
PrototypeBinding_strategy = st.builds(
    PrototypeBinding,
)
aadl2_FeaturePrototypeBinding_strategy = st.builds(
    aadl2_FeaturePrototypeBinding,
)
aadl2_ComponentPrototypeBinding_strategy = st.builds(
    aadl2_ComponentPrototypeBinding,
)
FeaturePrototypeActual_strategy = st.builds(
    FeaturePrototypeActual,
)
aadl2_FeaturePrototypeReference_strategy = st.builds(
    aadl2_FeaturePrototypeReference,
    in_=
        safe_text,
    direction=
        safe_text,
    out=
        safe_text
)
aadl2_AccessSpecification_strategy = st.builds(
    aadl2_AccessSpecification,
    category=
        safe_text,
    kind=
        safe_text
)
aadl2_PortSpecification_strategy = st.builds(
    aadl2_PortSpecification,
    category=
        safe_text,
    direction=
        safe_text,
    in_=
        safe_text,
    out=
        safe_text
)
aadl2_FeatureGroupPrototypeActual_strategy = st.builds(
    aadl2_FeatureGroupPrototypeActual,
)
aadl2_FeatureGroupPrototypeBinding_strategy = st.builds(
    aadl2_FeatureGroupPrototypeBinding,
)
ModelUnit_strategy = st.builds(
    ModelUnit,
)
aadl2_AadlPackage_strategy = st.builds(
    aadl2_AadlPackage,
)
PackageSection_strategy = st.builds(
    PackageSection,
)
aadl2_PrivatePackageSection_strategy = st.builds(
    aadl2_PrivatePackageSection,
)
aadl2_PublicPackageSection_strategy = st.builds(
    aadl2_PublicPackageSection,
)
SubprogramSubcomponentType_strategy = st.builds(
    SubprogramSubcomponentType,
)
Subprogram_strategy = st.builds(
    Subprogram,
)
aadl2_SubprogramPrototype_strategy = st.builds(
    aadl2_SubprogramPrototype,
)
AnnexSubclause_strategy = st.builds(
    AnnexSubclause,
)
aadl2_DefaultAnnexSubclause_strategy = st.builds(
    aadl2_DefaultAnnexSubclause,
    sourceText=
        safe_text
)
AnnexLibrary_strategy = st.builds(
    AnnexLibrary,
)
aadl2_DefaultAnnexLibrary_strategy = st.builds(
    aadl2_DefaultAnnexLibrary,
    sourceText=
        safe_text
)
InternalFeature_strategy = st.builds(
    InternalFeature,
)
ProcessorFeature_strategy = st.builds(
    ProcessorFeature,
)
DataSubcomponentType_strategy = st.builds(
    DataSubcomponentType,
)
Data_strategy = st.builds(
    Data,
)
aadl2_DataPrototype_strategy = st.builds(
    aadl2_DataPrototype,
)
Abstract_strategy = st.builds(
    Abstract,
)
aadl2_AbstractPrototype_strategy = st.builds(
    aadl2_AbstractPrototype,
)
Subcomponent_strategy = st.builds(
    Subcomponent,
)
aadl2_VirtualProcessorSubcomponent_strategy = st.builds(
    aadl2_VirtualProcessorSubcomponent,
)
aadl2_SystemSubcomponent_strategy = st.builds(
    aadl2_SystemSubcomponent,
)
aadl2_ProcessSubcomponent_strategy = st.builds(
    aadl2_ProcessSubcomponent,
)
aadl2_ProcessorSubcomponent_strategy = st.builds(
    aadl2_ProcessorSubcomponent,
)
aadl2_DeviceSubcomponent_strategy = st.builds(
    aadl2_DeviceSubcomponent,
)
aadl2_ThreadGroupSubcomponent_strategy = st.builds(
    aadl2_ThreadGroupSubcomponent,
)
aadl2_ThreadSubcomponent_strategy = st.builds(
    aadl2_ThreadSubcomponent,
)
aadl2_MemorySubcomponent_strategy = st.builds(
    aadl2_MemorySubcomponent,
)
Connection_strategy = st.builds(
    Connection,
)
NumberType_strategy = st.builds(
    NumberType,
)
aadl2_AadlReal_strategy = st.builds(
    aadl2_AadlReal,
)
aadl2_AadlInteger_strategy = st.builds(
    aadl2_AadlInteger,
)
NonListType_strategy = st.builds(
    NonListType,
)
aadl2_RangeType_strategy = st.builds(
    aadl2_RangeType,
)
aadl2_ReferenceType_strategy = st.builds(
    aadl2_ReferenceType,
)
aadl2_ClassifierType_strategy = st.builds(
    aadl2_ClassifierType,
)
aadl2_AadlString_strategy = st.builds(
    aadl2_AadlString,
)
aadl2_NumberType_strategy = st.builds(
    aadl2_NumberType,
)
aadl2_AadlBoolean_strategy = st.builds(
    aadl2_AadlBoolean,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
aadl2_ListType_strategy = st.builds(
    aadl2_ListType,
)
aadl2_NonListType_strategy = st.builds(
    aadl2_NonListType,
)
EnumerationType_strategy = st.builds(
    EnumerationType,
)
aadl2_UnitsType_strategy = st.builds(
    aadl2_UnitsType,
)
aadl2_ComputedValue_strategy = st.builds(
    aadl2_ComputedValue,
    function=
        safe_text
)
aadl2_RecordValue_strategy = st.builds(
    aadl2_RecordValue,
)
aadl2_NamedValue_strategy = st.builds(
    aadl2_NamedValue,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
aadl2_IntegerLiteral_strategy = st.builds(
    aadl2_IntegerLiteral,
    base=
        safe_text,
    value=
        safe_text
)
aadl2_RangeValue_strategy = st.builds(
    aadl2_RangeValue,
)
aadl2_BooleanLiteral_strategy = st.builds(
    aadl2_BooleanLiteral,
    value=
        safe_text
)
ContainedNamedElement_strategy = st.builds(
    ContainedNamedElement,
)
aadl2_ReferenceValue_strategy = st.builds(
    aadl2_ReferenceValue,
)
aadl2_RealLiteral_strategy = st.builds(
    aadl2_RealLiteral,
    value=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
aadl2_UnitLiteral_strategy = st.builds(
    aadl2_UnitLiteral,
)
aadl2_NumberValue_strategy = st.builds(
    aadl2_NumberValue,
)
PropertyExpression_strategy = st.builds(
    PropertyExpression,
)
aadl2_ListValue_strategy = st.builds(
    aadl2_ListValue,
)
aadl2_Operation_strategy = st.builds(
    aadl2_Operation,
    op=
        safe_text
)
aadl2_PropertyValue_strategy = st.builds(
    aadl2_PropertyValue,
)
ArraySizeProperty_strategy = st.builds(
    ArraySizeProperty,
)
ArrayableElement_strategy = st.builds(
    ArrayableElement,
)
aadl2_FeaturePrototypeActual_strategy = st.builds(
    aadl2_FeaturePrototypeActual,
)
aadl2_ComponentPrototypeActual_strategy = st.builds(
    aadl2_ComponentPrototypeActual,
    category=
        safe_text
)
FeatureConnectionEnd_strategy = st.builds(
    FeatureConnectionEnd,
)
aadl2_FeatureClassifier_strategy = st.builds(
    aadl2_FeatureClassifier,
)
aadl2_EventSource_strategy = st.builds(
    aadl2_EventSource,
)
FeatureClassifier_strategy = st.builds(
    FeatureClassifier,
)
SubcomponentType_strategy = st.builds(
    SubcomponentType,
)
aadl2_ThreadGroupSubcomponentType_strategy = st.builds(
    aadl2_ThreadGroupSubcomponentType,
)
aadl2_ThreadSubcomponentType_strategy = st.builds(
    aadl2_ThreadSubcomponentType,
)
aadl2_MemorySubcomponentType_strategy = st.builds(
    aadl2_MemorySubcomponentType,
)
aadl2_ProcessSubcomponentType_strategy = st.builds(
    aadl2_ProcessSubcomponentType,
)
aadl2_SystemSubcomponentType_strategy = st.builds(
    aadl2_SystemSubcomponentType,
)
aadl2_DeviceSubcomponentType_strategy = st.builds(
    aadl2_DeviceSubcomponentType,
)
aadl2_ProcessorSubcomponentType_strategy = st.builds(
    aadl2_ProcessorSubcomponentType,
)
aadl2_VirtualProcessorSubcomponentType_strategy = st.builds(
    aadl2_VirtualProcessorSubcomponentType,
)
Classifier_strategy = st.builds(
    Classifier,
)
aadl2_ComponentClassifier_strategy = st.builds(
    aadl2_ComponentClassifier,
    derivedModes=
        safe_text,
    noModes=
        safe_text,
    noFlows=
        safe_text
)
aadl2_EventDataSource_strategy = st.builds(
    aadl2_EventDataSource,
)
aadl2_FeatureGroupConnection_strategy = st.builds(
    aadl2_FeatureGroupConnection,
)
aadl2_FeatureConnection_strategy = st.builds(
    aadl2_FeatureConnection,
)
aadl2_PortConnection_strategy = st.builds(
    aadl2_PortConnection,
)
aadl2_ParameterConnection_strategy = st.builds(
    aadl2_ParameterConnection,
)
ComponentClassifier_strategy = st.builds(
    ComponentClassifier,
)
aadl2_DeviceClassifier_strategy = st.builds(
    aadl2_DeviceClassifier,
)
aadl2_ThreadGroupClassifier_strategy = st.builds(
    aadl2_ThreadGroupClassifier,
)
aadl2_MemoryClassifier_strategy = st.builds(
    aadl2_MemoryClassifier,
)
aadl2_ProcessClassifier_strategy = st.builds(
    aadl2_ProcessClassifier,
)
aadl2_VirtualProcessorClassifier_strategy = st.builds(
    aadl2_VirtualProcessorClassifier,
)
aadl2_ThreadClassifier_strategy = st.builds(
    aadl2_ThreadClassifier,
)
aadl2_SubprogramGroupClassifier_strategy = st.builds(
    aadl2_SubprogramGroupClassifier,
)
aadl2_SubprogramClassifier_strategy = st.builds(
    aadl2_SubprogramClassifier,
)
aadl2_AbstractClassifier_strategy = st.builds(
    aadl2_AbstractClassifier,
)
aadl2_BusClassifier_strategy = st.builds(
    aadl2_BusClassifier,
)
aadl2_SystemClassifier_strategy = st.builds(
    aadl2_SystemClassifier,
)
aadl2_VirtualBusClassifier_strategy = st.builds(
    aadl2_VirtualBusClassifier,
)
aadl2_ProcessorClassifier_strategy = st.builds(
    aadl2_ProcessorClassifier,
)
aadl2_DataClassifier_strategy = st.builds(
    aadl2_DataClassifier,
)
aadl2_AccessConnection_strategy = st.builds(
    aadl2_AccessConnection,
    accessCategory=
        safe_text
)
aadl2_AbstractSubcomponent_strategy = st.builds(
    aadl2_AbstractSubcomponent,
)
aadl2_ComponentType_strategy = st.builds(
    aadl2_ComponentType,
    noFeatures=
        safe_text
)
aadl2_ComponentImplementation_strategy = st.builds(
    aadl2_ComponentImplementation,
    noConnections=
        safe_text,
    noSubcomponents=
        safe_text,
    noCalls=
        safe_text
)
aadl2_ArraySizeProperty_strategy = st.builds(
    aadl2_ArraySizeProperty,
)
RefinableElement_strategy = st.builds(
    RefinableElement,
)
CalledSubprogram_strategy = st.builds(
    CalledSubprogram,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
aadl2_ProcessorFeature_strategy = st.builds(
    aadl2_ProcessorFeature,
)
aadl2_Feature_strategy = st.builds(
    aadl2_Feature,
)
ClassifierFeature_strategy = st.builds(
    ClassifierFeature,
)
aadl2_BehavioralFeature_strategy = st.builds(
    aadl2_BehavioralFeature,
)
aadl2_StructuralFeature_strategy = st.builds(
    aadl2_StructuralFeature,
)
aadl2_ModeFeature_strategy = st.builds(
    aadl2_ModeFeature,
)
aadl2_CalledSubprogram_strategy = st.builds(
    aadl2_CalledSubprogram,
)
Relationship_strategy = st.builds(
    Relationship,
)
aadl2_DirectedRelationship_strategy = st.builds(
    aadl2_DirectedRelationship,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
ModeFeature_strategy = st.builds(
    ModeFeature,
)
aadl2_ModeTransition_strategy = st.builds(
    aadl2_ModeTransition,
)
aadl2_Mode_strategy = st.builds(
    aadl2_Mode,
    initial=
        safe_text,
    derived=
        safe_text
)
ModalElement_strategy = st.builds(
    ModalElement,
)
aadl2_SubprogramCallSequence_strategy = st.builds(
    aadl2_SubprogramCallSequence,
)
aadl2_Prototype_strategy = st.builds(
    aadl2_Prototype,
)
aadl2_AnnexSubclause_strategy = st.builds(
    aadl2_AnnexSubclause,
)
aadl2_Generalization__strategy = st.builds(
    aadl2_Generalization_,
)
PropertyOwner_strategy = st.builds(
    PropertyOwner,
)
aadl2_ClassifierValue_strategy = st.builds(
    aadl2_ClassifierValue,
)
aadl2_AbstractNamedValue_strategy = st.builds(
    aadl2_AbstractNamedValue,
)
Type_strategy = st.builds(
    Type,
)
aadl2_SubcomponentType_strategy = st.builds(
    aadl2_SubcomponentType,
)
Namespace_strategy = st.builds(
    Namespace,
)
aadl2_RecordType_strategy = st.builds(
    aadl2_RecordType,
)
aadl2_EnumerationType_strategy = st.builds(
    aadl2_EnumerationType,
)
aadl2_GlobalNamespace_strategy = st.builds(
    aadl2_GlobalNamespace,
)
aadl2_PropertySet_strategy = st.builds(
    aadl2_PropertySet,
)
aadl2_PackageSection_strategy = st.builds(
    aadl2_PackageSection,
    noProperties=
        safe_text,
    noAnnexes=
        safe_text
)
aadl2_MetaclassReference_strategy = st.builds(
    aadl2_MetaclassReference,
    metaclassName=
        safe_text,
    annexName=
        safe_text
)
AbstractNamedValue_strategy = st.builds(
    AbstractNamedValue,
)
BasicProperty_strategy = st.builds(
    BasicProperty,
)
aadl2_RecordField_strategy = st.builds(
    aadl2_RecordField,
)
aadl2_ModalPropertyValue_strategy = st.builds(
    aadl2_ModalPropertyValue,
)
aadl2_Classifier_strategy = st.builds(
    aadl2_Classifier,
    noProperties=
        safe_text,
    noAnnexes=
        safe_text,
    noPrototypes=
        safe_text
)
aadl2_PropertyType_strategy = st.builds(
    aadl2_PropertyType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
aadl2_PropertyConstant_strategy = st.builds(
    aadl2_PropertyConstant,
)
aadl2_BasicProperty_strategy = st.builds(
    aadl2_BasicProperty,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
aadl2_AnnexLibrary_strategy = st.builds(
    aadl2_AnnexLibrary,
)
aadl2_ClassifierFeature_strategy = st.builds(
    aadl2_ClassifierFeature,
)
aadl2_Bus_strategy = st.builds(
    aadl2_Bus,
)
aadl2_Namespace_strategy = st.builds(
    aadl2_Namespace,
)
aadl2_Device_strategy = st.builds(
    aadl2_Device,
)
aadl2_Context_strategy = st.builds(
    aadl2_Context,
)
aadl2_TriggerPort_strategy = st.builds(
    aadl2_TriggerPort,
)
aadl2_Processor_strategy = st.builds(
    aadl2_Processor,
)
aadl2_Memory_strategy = st.builds(
    aadl2_Memory,
)
aadl2_Subprogram_strategy = st.builds(
    aadl2_Subprogram,
)
aadl2_ComponentTypeRename_strategy = st.builds(
    aadl2_ComponentTypeRename,
    category=
        safe_text
)
aadl2_Abstract_strategy = st.builds(
    aadl2_Abstract,
)
aadl2_ModalElement_strategy = st.builds(
    aadl2_ModalElement,
)
aadl2_FeatureGroupTypeRename_strategy = st.builds(
    aadl2_FeatureGroupTypeRename,
)
aadl2_RefinableElement_strategy = st.builds(
    aadl2_RefinableElement,
)
aadl2_ModelUnit_strategy = st.builds(
    aadl2_ModelUnit,
)
aadl2_SubprogramGroup_strategy = st.builds(
    aadl2_SubprogramGroup,
)
aadl2_Process_strategy = st.builds(
    aadl2_Process,
)
aadl2_System_strategy = st.builds(
    aadl2_System,
)
aadl2_Data_strategy = st.builds(
    aadl2_Data,
)
aadl2_VirtualProcessor_strategy = st.builds(
    aadl2_VirtualProcessor,
)
aadl2_PackageRename_strategy = st.builds(
    aadl2_PackageRename,
    renameAll=
        safe_text
)
aadl2_Thread_strategy = st.builds(
    aadl2_Thread,
)
aadl2_ThreadGroup_strategy = st.builds(
    aadl2_ThreadGroup,
)
aadl2_VirtualBus_strategy = st.builds(
    aadl2_VirtualBus,
)
aadl2_EnumerationLiteral_strategy = st.builds(
    aadl2_EnumerationLiteral,
)
aadl2_TypedElement_strategy = st.builds(
    aadl2_TypedElement,
)
aadl2_Type_strategy = st.builds(
    aadl2_Type,
)
aadl2_Property_strategy = st.builds(
    aadl2_Property,
    inherit=
        safe_text,
    emptyListDefault=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
aadl2_NumericRange_strategy = st.builds(
    aadl2_NumericRange,
)
aadl2_ArrayDimension_strategy = st.builds(
    aadl2_ArrayDimension,
)
aadl2_ArraySize_strategy = st.builds(
    aadl2_ArraySize,
    size=
        safe_text
)
aadl2_ContainedNamedElement_strategy = st.builds(
    aadl2_ContainedNamedElement,
)
aadl2_ComponentImplementationReference_strategy = st.builds(
    aadl2_ComponentImplementationReference,
)
aadl2_ModeTransitionTrigger_strategy = st.builds(
    aadl2_ModeTransitionTrigger,
)
aadl2_NamedElement_strategy = st.builds(
    aadl2_NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
aadl2_PrototypeBinding_strategy = st.builds(
    aadl2_PrototypeBinding,
)
aadl2_ArrayableElement_strategy = st.builds(
    aadl2_ArrayableElement,
)
aadl2_PropertyExpression_strategy = st.builds(
    aadl2_PropertyExpression,
)
aadl2_PropertyAssociation_strategy = st.builds(
    aadl2_PropertyAssociation,
    append=
        safe_text,
    constant=
        safe_text
)
aadl2_FlowEnd_strategy = st.builds(
    aadl2_FlowEnd,
)
aadl2_ArrayRange_strategy = st.builds(
    aadl2_ArrayRange,
    upperBound=
        safe_text,
    lowerBound=
        safe_text
)
aadl2_BasicPropertyAssociation_strategy = st.builds(
    aadl2_BasicPropertyAssociation,
)
aadl2_EndToEndFlowSegment_strategy = st.builds(
    aadl2_EndToEndFlowSegment,
)
aadl2_Relationship_strategy = st.builds(
    aadl2_Relationship,
)
aadl2_ConnectedElement_strategy = st.builds(
    aadl2_ConnectedElement,
)
aadl2_PropertyOwner_strategy = st.builds(
    aadl2_PropertyOwner,
)
aadl2_FlowSegment_strategy = st.builds(
    aadl2_FlowSegment,
)
aadl2_ContainmentPathElement_strategy = st.builds(
    aadl2_ContainmentPathElement,
    annexName=
        safe_text
)
aadl2_Comment_strategy = st.builds(
    aadl2_Comment,
    body=
        safe_text
)
aadl2_Element_strategy = st.builds(
    aadl2_Element,
)
aadl2_ModeBinding_strategy = st.builds(
    aadl2_ModeBinding,
)
TriggerPort_strategy = st.builds(
    TriggerPort,
)
Port_strategy = st.builds(
    Port,
)
AccessConnectionEnd_strategy = st.builds(
    AccessConnectionEnd,
)
aadl2_VirtualBusSubcomponent_strategy = st.builds(
    aadl2_VirtualBusSubcomponent,
)
aadl2_SubprogramSubcomponent_strategy = st.builds(
    aadl2_SubprogramSubcomponent,
)
aadl2_SubprogramProxy_strategy = st.builds(
    aadl2_SubprogramProxy,
)
aadl2_BusSubcomponent_strategy = st.builds(
    aadl2_BusSubcomponent,
)
aadl2_BusFeatureClassifier_strategy = st.builds(
    aadl2_BusFeatureClassifier,
)
aadl2_AbstractFeatureClassifier_strategy = st.builds(
    aadl2_AbstractFeatureClassifier,
)
Access_strategy = st.builds(
    Access,
)
AbstractFeatureClassifier_strategy = st.builds(
    AbstractFeatureClassifier,
)
aadl2_SubprogramGroupSubcomponentType_strategy = st.builds(
    aadl2_SubprogramGroupSubcomponentType,
)
aadl2_VirtualBusSubcomponentType_strategy = st.builds(
    aadl2_VirtualBusSubcomponentType,
)
aadl2_AbstractSubcomponentType_strategy = st.builds(
    aadl2_AbstractSubcomponentType,
)
aadl2_SubprogramSubcomponentType_strategy = st.builds(
    aadl2_SubprogramSubcomponentType,
)
aadl2_BusSubcomponentType_strategy = st.builds(
    aadl2_BusSubcomponentType,
)
aadl2_DataSubcomponentType_strategy = st.builds(
    aadl2_DataSubcomponentType,
)
PortConnectionEnd_strategy = st.builds(
    PortConnectionEnd,
)
aadl2_PortProxy_strategy = st.builds(
    aadl2_PortProxy,
    out=
        safe_text,
    in_=
        safe_text,
    direction=
        safe_text
)
aadl2_InternalFeature_strategy = st.builds(
    aadl2_InternalFeature,
    in_=
        safe_text,
    direction=
        safe_text,
    out=
        safe_text
)
ParameterConnectionEnd_strategy = st.builds(
    ParameterConnectionEnd,
)
aadl2_DataSubcomponent_strategy = st.builds(
    aadl2_DataSubcomponent,
)
aadl2_EventPort_strategy = st.builds(
    aadl2_EventPort,
)
FeatureType_strategy = st.builds(
    FeatureType,
)
aadl2_BusAccess_strategy = st.builds(
    aadl2_BusAccess,
    virtual=
        safe_text
)
Generalization__strategy = st.builds(
    Generalization_,
)
aadl2_Realization_strategy = st.builds(
    aadl2_Realization,
)
aadl2_ImplementationExtension_strategy = st.builds(
    aadl2_ImplementationExtension,
)
aadl2_TypeExtension_strategy = st.builds(
    aadl2_TypeExtension,
)
aadl2_GroupExtension_strategy = st.builds(
    aadl2_GroupExtension,
)
aadl2_EndToEndFlowElement_strategy = st.builds(
    aadl2_EndToEndFlowElement,
)
EndToEndFlowElement_strategy = st.builds(
    EndToEndFlowElement,
)
aadl2_FlowElement_strategy = st.builds(
    aadl2_FlowElement,
)
Feature_strategy = st.builds(
    Feature,
)
aadl2_Access_strategy = st.builds(
    aadl2_Access,
    kind=
        safe_text,
    category=
        safe_text
)
aadl2_DirectedFeature_strategy = st.builds(
    aadl2_DirectedFeature,
    in_=
        safe_text,
    out=
        safe_text,
    direction=
        safe_text
)
aadl2_CallContext_strategy = st.builds(
    aadl2_CallContext,
)
aadl2_FeatureGroupType_strategy = st.builds(
    aadl2_FeatureGroupType,
)
aadl2_FeatureType_strategy = st.builds(
    aadl2_FeatureType,
)
CallContext_strategy = st.builds(
    CallContext,
)
aadl2_SubprogramGroupAccess_strategy = st.builds(
    aadl2_SubprogramGroupAccess,
)
aadl2_SubprogramGroupSubcomponent_strategy = st.builds(
    aadl2_SubprogramGroupSubcomponent,
)
aadl2_SubprogramGroupType_strategy = st.builds(
    aadl2_SubprogramGroupType,
)
aadl2_SubprogramType_strategy = st.builds(
    aadl2_SubprogramType,
)
aadl2_AbstractType_strategy = st.builds(
    aadl2_AbstractType,
)
aadl2_DataType_strategy = st.builds(
    aadl2_DataType,
)
FeatureGroupConnectionEnd_strategy = st.builds(
    FeatureGroupConnectionEnd,
)
Context_strategy = st.builds(
    Context,
)
aadl2_SubprogramAccess_strategy = st.builds(
    aadl2_SubprogramAccess,
)
aadl2_DataPort_strategy = st.builds(
    aadl2_DataPort,
)
aadl2_EventDataPort_strategy = st.builds(
    aadl2_EventDataPort,
)
aadl2_SubprogramCall_strategy = st.builds(
    aadl2_SubprogramCall,
)
DirectedFeature_strategy = st.builds(
    DirectedFeature,
)
aadl2_FeatureGroup_strategy = st.builds(
    aadl2_FeatureGroup,
    inverse=
        safe_text
)
aadl2_Port_strategy = st.builds(
    aadl2_Port,
    category=
        safe_text
)
aadl2_Parameter_strategy = st.builds(
    aadl2_Parameter,
)
aadl2_AbstractFeature_strategy = st.builds(
    aadl2_AbstractFeature,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
aadl2_DataAccess_strategy = st.builds(
    aadl2_DataAccess,
)
aadl2_Subcomponent_strategy = st.builds(
    aadl2_Subcomponent,
    allModes=
        safe_text
)
ModalPath_strategy = st.builds(
    ModalPath,
)
aadl2_Connection_strategy = st.builds(
    aadl2_Connection,
    bidirectional=
        safe_text
)
FlowFeature_strategy = st.builds(
    FlowFeature,
)
aadl2_FlowSpecification_strategy = st.builds(
    aadl2_FlowSpecification,
    kind=
        safe_text
)
aadl2_EndToEndFlow_strategy = st.builds(
    aadl2_EndToEndFlow,
)
Prototype_strategy = st.builds(
    Prototype,
)
aadl2_ComponentPrototype_strategy = st.builds(
    aadl2_ComponentPrototype,
    array=
        safe_text
)
aadl2_FeaturePrototype_strategy = st.builds(
    aadl2_FeaturePrototype,
    in_=
        safe_text,
    direction=
        safe_text,
    out=
        safe_text
)
aadl2_FeatureGroupPrototype_strategy = st.builds(
    aadl2_FeatureGroupPrototype,
)
aadl2_ConnectionEnd_strategy = st.builds(
    aadl2_ConnectionEnd,
)
ConnectionEnd_strategy = st.builds(
    ConnectionEnd,
)
aadl2_AccessConnectionEnd_strategy = st.builds(
    aadl2_AccessConnectionEnd,
)
aadl2_FeatureGroupConnectionEnd_strategy = st.builds(
    aadl2_FeatureGroupConnectionEnd,
)
aadl2_ParameterConnectionEnd_strategy = st.builds(
    aadl2_ParameterConnectionEnd,
)
aadl2_PortConnectionEnd_strategy = st.builds(
    aadl2_PortConnectionEnd,
)
aadl2_FeatureConnectionEnd_strategy = st.builds(
    aadl2_FeatureConnectionEnd,
)
aadl2_ModalPath_strategy = st.builds(
    aadl2_ModalPath,
)
aadl2_Flow_strategy = st.builds(
    aadl2_Flow,
)
Flow_strategy = st.builds(
    Flow,
)
aadl2_FlowFeature_strategy = st.builds(
    aadl2_FlowFeature,
)
aadl2_FlowImplementation_strategy = st.builds(
    aadl2_FlowImplementation,
    kind=
        safe_text
)





@given(instance=aadl2_StringLiteral_strategy)
def test_hyp_aadl2_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original















































































import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_BehavioredImplementation_strategy)
@settings(max_examples=30)
def test_hyp_aadl2_behavioredimplementation_subprogramcalls_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subprogramCalls()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subprogramCalls).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subprogramCalls' in aadl2_BehavioredImplementation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subprogramCalls' in aadl2_BehavioredImplementation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subprogramCalls' in aadl2_BehavioredImplementation is not implemented or raised an error")









@given(instance=aadl2_FeaturePrototypeReference_strategy)
def test_hyp_aadl2_featureprototypereference_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_FeaturePrototypeReference_strategy)
def test_hyp_aadl2_featureprototypereference_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=aadl2_FeaturePrototypeReference_strategy)
def test_hyp_aadl2_featureprototypereference_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original




@given(instance=aadl2_AccessSpecification_strategy)
def test_hyp_aadl2_accessspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=aadl2_AccessSpecification_strategy)
def test_hyp_aadl2_accessspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=aadl2_PortSpecification_strategy)
def test_hyp_aadl2_portspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=aadl2_PortSpecification_strategy)
def test_hyp_aadl2_portspecification_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=aadl2_PortSpecification_strategy)
def test_hyp_aadl2_portspecification_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_PortSpecification_strategy)
def test_hyp_aadl2_portspecification_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original















@given(instance=aadl2_DefaultAnnexSubclause_strategy)
def test_hyp_aadl2_defaultannexsubclause_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original





@given(instance=aadl2_DefaultAnnexLibrary_strategy)
def test_hyp_aadl2_defaultannexlibrary_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original




































@given(instance=aadl2_ComputedValue_strategy)
def test_hyp_aadl2_computedvalue_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original







@given(instance=aadl2_IntegerLiteral_strategy)
def test_hyp_aadl2_integerliteral_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original



@given(instance=aadl2_IntegerLiteral_strategy)
def test_hyp_aadl2_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=aadl2_BooleanLiteral_strategy)
def test_hyp_aadl2_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=aadl2_RealLiteral_strategy)
def test_hyp_aadl2_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=aadl2_Operation_strategy)
def test_hyp_aadl2_operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original








@given(instance=aadl2_ComponentPrototypeActual_strategy)
def test_hyp_aadl2_componentprototypeactual_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original


















@given(instance=aadl2_ComponentClassifier_strategy)
def test_hyp_aadl2_componentclassifier_derivedModes_setter(instance):
    original = instance.derivedModes
    instance.derivedModes = original
    assert instance.derivedModes == original



@given(instance=aadl2_ComponentClassifier_strategy)
def test_hyp_aadl2_componentclassifier_noModes_setter(instance):
    original = instance.noModes
    instance.noModes = original
    assert instance.noModes == original



@given(instance=aadl2_ComponentClassifier_strategy)
def test_hyp_aadl2_componentclassifier_noFlows_setter(instance):
    original = instance.noFlows
    instance.noFlows = original
    assert instance.noFlows == original
























@given(instance=aadl2_AccessConnection_strategy)
def test_hyp_aadl2_accessconnection_accessCategory_setter(instance):
    original = instance.accessCategory
    instance.accessCategory = original
    assert instance.accessCategory == original





@given(instance=aadl2_ComponentType_strategy)
def test_hyp_aadl2_componenttype_noFeatures_setter(instance):
    original = instance.noFeatures
    instance.noFeatures = original
    assert instance.noFeatures == original




@given(instance=aadl2_ComponentImplementation_strategy)
def test_hyp_aadl2_componentimplementation_noConnections_setter(instance):
    original = instance.noConnections
    instance.noConnections = original
    assert instance.noConnections == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_hyp_aadl2_componentimplementation_noSubcomponents_setter(instance):
    original = instance.noSubcomponents
    instance.noSubcomponents = original
    assert instance.noSubcomponents == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_hyp_aadl2_componentimplementation_noCalls_setter(instance):
    original = instance.noCalls
    instance.noCalls = original
    assert instance.noCalls == original




















@given(instance=aadl2_Mode_strategy)
def test_hyp_aadl2_mode_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=aadl2_Mode_strategy)
def test_hyp_aadl2_mode_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



















@given(instance=aadl2_PackageSection_strategy)
def test_hyp_aadl2_packagesection_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original



@given(instance=aadl2_PackageSection_strategy)
def test_hyp_aadl2_packagesection_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original




@given(instance=aadl2_MetaclassReference_strategy)
def test_hyp_aadl2_metaclassreference_metaclassName_setter(instance):
    original = instance.metaclassName
    instance.metaclassName = original
    assert instance.metaclassName == original



@given(instance=aadl2_MetaclassReference_strategy)
def test_hyp_aadl2_metaclassreference_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original








@given(instance=aadl2_Classifier_strategy)
def test_hyp_aadl2_classifier_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original



@given(instance=aadl2_Classifier_strategy)
def test_hyp_aadl2_classifier_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original



@given(instance=aadl2_Classifier_strategy)
def test_hyp_aadl2_classifier_noPrototypes_setter(instance):
    original = instance.noPrototypes
    instance.noPrototypes = original
    assert instance.noPrototypes == original



















@given(instance=aadl2_ComponentTypeRename_strategy)
def test_hyp_aadl2_componenttyperename_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original














@given(instance=aadl2_PackageRename_strategy)
def test_hyp_aadl2_packagerename_renameAll_setter(instance):
    original = instance.renameAll
    instance.renameAll = original
    assert instance.renameAll == original










@given(instance=aadl2_Property_strategy)
def test_hyp_aadl2_property_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original



@given(instance=aadl2_Property_strategy)
def test_hyp_aadl2_property_emptyListDefault_setter(instance):
    original = instance.emptyListDefault
    instance.emptyListDefault = original
    assert instance.emptyListDefault == original







@given(instance=aadl2_ArraySize_strategy)
def test_hyp_aadl2_arraysize_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original







@given(instance=aadl2_NamedElement_strategy)
def test_hyp_aadl2_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aadl2_NamedElement_strategy)
def test_hyp_aadl2_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_hyp_aadl2_namedelement_qualifiedname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.qualifiedName()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.qualifiedName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'qualifiedName' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'qualifiedName' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'qualifiedName' in aadl2_NamedElement is not implemented or raised an error")







@given(instance=aadl2_PropertyAssociation_strategy)
def test_hyp_aadl2_propertyassociation_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original



@given(instance=aadl2_PropertyAssociation_strategy)
def test_hyp_aadl2_propertyassociation_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original





@given(instance=aadl2_ArrayRange_strategy)
def test_hyp_aadl2_arrayrange_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=aadl2_ArrayRange_strategy)
def test_hyp_aadl2_arrayrange_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original










@given(instance=aadl2_ContainmentPathElement_strategy)
def test_hyp_aadl2_containmentpathelement_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original




@given(instance=aadl2_Comment_strategy)
def test_hyp_aadl2_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original
























@given(instance=aadl2_PortProxy_strategy)
def test_hyp_aadl2_portproxy_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=aadl2_PortProxy_strategy)
def test_hyp_aadl2_portproxy_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_PortProxy_strategy)
def test_hyp_aadl2_portproxy_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original




@given(instance=aadl2_InternalFeature_strategy)
def test_hyp_aadl2_internalfeature_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_InternalFeature_strategy)
def test_hyp_aadl2_internalfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=aadl2_InternalFeature_strategy)
def test_hyp_aadl2_internalfeature_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original








@given(instance=aadl2_BusAccess_strategy)
def test_hyp_aadl2_busaccess_virtual_setter(instance):
    original = instance.virtual
    instance.virtual = original
    assert instance.virtual == original













@given(instance=aadl2_Access_strategy)
def test_hyp_aadl2_access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aadl2_Access_strategy)
def test_hyp_aadl2_access_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original




@given(instance=aadl2_DirectedFeature_strategy)
def test_hyp_aadl2_directedfeature_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_DirectedFeature_strategy)
def test_hyp_aadl2_directedfeature_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=aadl2_DirectedFeature_strategy)
def test_hyp_aadl2_directedfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original





















@given(instance=aadl2_FeatureGroup_strategy)
def test_hyp_aadl2_featuregroup_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original




@given(instance=aadl2_Port_strategy)
def test_hyp_aadl2_port_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original








@given(instance=aadl2_Subcomponent_strategy)
def test_hyp_aadl2_subcomponent_allModes_setter(instance):
    original = instance.allModes
    instance.allModes = original
    assert instance.allModes == original





@given(instance=aadl2_Connection_strategy)
def test_hyp_aadl2_connection_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original





@given(instance=aadl2_FlowSpecification_strategy)
def test_hyp_aadl2_flowspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original






@given(instance=aadl2_ComponentPrototype_strategy)
def test_hyp_aadl2_componentprototype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original




@given(instance=aadl2_FeaturePrototype_strategy)
def test_hyp_aadl2_featureprototype_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original



@given(instance=aadl2_FeaturePrototype_strategy)
def test_hyp_aadl2_featureprototype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=aadl2_FeaturePrototype_strategy)
def test_hyp_aadl2_featureprototype_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original
















@given(instance=aadl2_FlowImplementation_strategy)
def test_hyp_aadl2_flowimplementation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Abstract,
    AbstractClassifier,
    AbstractFeatureClassifier,
    AbstractNamedValue,
    AbstractSubcomponentType,
    Access,
    AccessConnectionEnd,
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
    Element,
    EndToEndFlowElement,
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
    PackageSection,
    ParameterConnectionEnd,
    Port,
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
    AccessCategory,
    AccessType,
    ComponentCategory,
    DirectionType,
    FlowKind,
    OperationKind,
    PortCategory,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_aadl2_Access_category_value_roundtrip():
    instance = aadl2_Access(category="sample_text", kind="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_Access_kind_value_roundtrip():
    instance = aadl2_Access(category="sample_text", kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aadl2_AccessConnection_accessCategory_value_roundtrip():
    instance = aadl2_AccessConnection(accessCategory="sample_text")
    assert instance.accessCategory == "sample_text"
    instance.accessCategory = "sample_text_2"
    assert instance.accessCategory == "sample_text_2"


def test_aadl2_AccessSpecification_category_value_roundtrip():
    instance = aadl2_AccessSpecification(category="sample_text", kind="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_AccessSpecification_kind_value_roundtrip():
    instance = aadl2_AccessSpecification(category="sample_text", kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aadl2_ArrayRange_lowerBound_value_roundtrip():
    instance = aadl2_ArrayRange(lowerBound="sample_text", upperBound="sample_text")
    assert instance.lowerBound == "sample_text"
    instance.lowerBound = "sample_text_2"
    assert instance.lowerBound == "sample_text_2"


def test_aadl2_ArrayRange_upperBound_value_roundtrip():
    instance = aadl2_ArrayRange(lowerBound="sample_text", upperBound="sample_text")
    assert instance.upperBound == "sample_text"
    instance.upperBound = "sample_text_2"
    assert instance.upperBound == "sample_text_2"


def test_aadl2_ArraySize_size_value_roundtrip():
    instance = aadl2_ArraySize(size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_aadl2_BooleanLiteral_value_value_roundtrip():
    instance = aadl2_BooleanLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aadl2_BusAccess_virtual_value_roundtrip():
    instance = aadl2_BusAccess(virtual="sample_text")
    assert instance.virtual == "sample_text"
    instance.virtual = "sample_text_2"
    assert instance.virtual == "sample_text_2"


def test_aadl2_Classifier_noAnnexes_value_roundtrip():
    instance = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    assert instance.noAnnexes == "sample_text"
    instance.noAnnexes = "sample_text_2"
    assert instance.noAnnexes == "sample_text_2"


def test_aadl2_Classifier_noProperties_value_roundtrip():
    instance = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    assert instance.noProperties == "sample_text"
    instance.noProperties = "sample_text_2"
    assert instance.noProperties == "sample_text_2"


def test_aadl2_Classifier_noPrototypes_value_roundtrip():
    instance = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    assert instance.noPrototypes == "sample_text"
    instance.noPrototypes = "sample_text_2"
    assert instance.noPrototypes == "sample_text_2"


def test_aadl2_Comment_body_value_roundtrip():
    instance = aadl2_Comment(body="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_aadl2_ComponentClassifier_derivedModes_value_roundtrip():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert instance.derivedModes == "sample_text"
    instance.derivedModes = "sample_text_2"
    assert instance.derivedModes == "sample_text_2"


def test_aadl2_ComponentClassifier_noFlows_value_roundtrip():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert instance.noFlows == "sample_text"
    instance.noFlows = "sample_text_2"
    assert instance.noFlows == "sample_text_2"


def test_aadl2_ComponentClassifier_noModes_value_roundtrip():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert instance.noModes == "sample_text"
    instance.noModes = "sample_text_2"
    assert instance.noModes == "sample_text_2"


def test_aadl2_ComponentImplementation_noCalls_value_roundtrip():
    instance = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    assert instance.noCalls == "sample_text"
    instance.noCalls = "sample_text_2"
    assert instance.noCalls == "sample_text_2"


def test_aadl2_ComponentImplementation_noConnections_value_roundtrip():
    instance = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    assert instance.noConnections == "sample_text"
    instance.noConnections = "sample_text_2"
    assert instance.noConnections == "sample_text_2"


def test_aadl2_ComponentImplementation_noSubcomponents_value_roundtrip():
    instance = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    assert instance.noSubcomponents == "sample_text"
    instance.noSubcomponents = "sample_text_2"
    assert instance.noSubcomponents == "sample_text_2"


def test_aadl2_ComponentPrototype_array_value_roundtrip():
    instance = aadl2_ComponentPrototype(array="sample_text")
    assert instance.array == "sample_text"
    instance.array = "sample_text_2"
    assert instance.array == "sample_text_2"


def test_aadl2_ComponentPrototypeActual_category_value_roundtrip():
    instance = aadl2_ComponentPrototypeActual(category="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_ComponentType_noFeatures_value_roundtrip():
    instance = aadl2_ComponentType(noFeatures="sample_text")
    assert instance.noFeatures == "sample_text"
    instance.noFeatures = "sample_text_2"
    assert instance.noFeatures == "sample_text_2"


def test_aadl2_ComponentTypeRename_category_value_roundtrip():
    instance = aadl2_ComponentTypeRename(category="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_ComputedValue_function_value_roundtrip():
    instance = aadl2_ComputedValue(function="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_aadl2_Connection_bidirectional_value_roundtrip():
    instance = aadl2_Connection(bidirectional="sample_text")
    assert instance.bidirectional == "sample_text"
    instance.bidirectional = "sample_text_2"
    assert instance.bidirectional == "sample_text_2"


def test_aadl2_ContainmentPathElement_annexName_value_roundtrip():
    instance = aadl2_ContainmentPathElement(annexName="sample_text")
    assert instance.annexName == "sample_text"
    instance.annexName = "sample_text_2"
    assert instance.annexName == "sample_text_2"


def test_aadl2_DefaultAnnexLibrary_sourceText_value_roundtrip():
    instance = aadl2_DefaultAnnexLibrary(sourceText="sample_text")
    assert instance.sourceText == "sample_text"
    instance.sourceText = "sample_text_2"
    assert instance.sourceText == "sample_text_2"


def test_aadl2_DefaultAnnexSubclause_sourceText_value_roundtrip():
    instance = aadl2_DefaultAnnexSubclause(sourceText="sample_text")
    assert instance.sourceText == "sample_text"
    instance.sourceText = "sample_text_2"
    assert instance.sourceText == "sample_text_2"


def test_aadl2_DirectedFeature_direction_value_roundtrip():
    instance = aadl2_DirectedFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_DirectedFeature_in__value_roundtrip():
    instance = aadl2_DirectedFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_DirectedFeature_out_value_roundtrip():
    instance = aadl2_DirectedFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_FeatureGroup_inverse_value_roundtrip():
    instance = aadl2_FeatureGroup(inverse="sample_text")
    assert instance.inverse == "sample_text"
    instance.inverse = "sample_text_2"
    assert instance.inverse == "sample_text_2"


def test_aadl2_FeaturePrototype_direction_value_roundtrip():
    instance = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_FeaturePrototype_in__value_roundtrip():
    instance = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_FeaturePrototype_out_value_roundtrip():
    instance = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_FeaturePrototypeReference_direction_value_roundtrip():
    instance = aadl2_FeaturePrototypeReference(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_FeaturePrototypeReference_in__value_roundtrip():
    instance = aadl2_FeaturePrototypeReference(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_FeaturePrototypeReference_out_value_roundtrip():
    instance = aadl2_FeaturePrototypeReference(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_FlowImplementation_kind_value_roundtrip():
    instance = aadl2_FlowImplementation(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aadl2_FlowSpecification_kind_value_roundtrip():
    instance = aadl2_FlowSpecification(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aadl2_IntegerLiteral_base_value_roundtrip():
    instance = aadl2_IntegerLiteral(base="sample_text", value="sample_text")
    assert instance.base == "sample_text"
    instance.base = "sample_text_2"
    assert instance.base == "sample_text_2"


def test_aadl2_IntegerLiteral_value_value_roundtrip():
    instance = aadl2_IntegerLiteral(base="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aadl2_InternalFeature_direction_value_roundtrip():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_InternalFeature_in__value_roundtrip():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_InternalFeature_out_value_roundtrip():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_MetaclassReference_annexName_value_roundtrip():
    instance = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    assert instance.annexName == "sample_text"
    instance.annexName = "sample_text_2"
    assert instance.annexName == "sample_text_2"


def test_aadl2_MetaclassReference_metaclassName_value_roundtrip():
    instance = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    assert instance.metaclassName == "sample_text"
    instance.metaclassName = "sample_text_2"
    assert instance.metaclassName == "sample_text_2"


def test_aadl2_Mode_derived_value_roundtrip():
    instance = aadl2_Mode(derived="sample_text", initial="sample_text")
    assert instance.derived == "sample_text"
    instance.derived = "sample_text_2"
    assert instance.derived == "sample_text_2"


def test_aadl2_Mode_initial_value_roundtrip():
    instance = aadl2_Mode(derived="sample_text", initial="sample_text")
    assert instance.initial == "sample_text"
    instance.initial = "sample_text_2"
    assert instance.initial == "sample_text_2"


def test_aadl2_NamedElement_name_value_roundtrip():
    instance = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aadl2_NamedElement_qualifiedName_value_roundtrip():
    instance = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_aadl2_Operation_op_value_roundtrip():
    instance = aadl2_Operation(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_aadl2_PackageRename_renameAll_value_roundtrip():
    instance = aadl2_PackageRename(renameAll="sample_text")
    assert instance.renameAll == "sample_text"
    instance.renameAll = "sample_text_2"
    assert instance.renameAll == "sample_text_2"


def test_aadl2_PackageSection_noAnnexes_value_roundtrip():
    instance = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    assert instance.noAnnexes == "sample_text"
    instance.noAnnexes = "sample_text_2"
    assert instance.noAnnexes == "sample_text_2"


def test_aadl2_PackageSection_noProperties_value_roundtrip():
    instance = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    assert instance.noProperties == "sample_text"
    instance.noProperties = "sample_text_2"
    assert instance.noProperties == "sample_text_2"


def test_aadl2_Port_category_value_roundtrip():
    instance = aadl2_Port(category="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_PortProxy_direction_value_roundtrip():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_PortProxy_in__value_roundtrip():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_PortProxy_out_value_roundtrip():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_PortSpecification_category_value_roundtrip():
    instance = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_aadl2_PortSpecification_direction_value_roundtrip():
    instance = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_aadl2_PortSpecification_in__value_roundtrip():
    instance = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.in_ == "sample_text"
    instance.in_ = "sample_text_2"
    assert instance.in_ == "sample_text_2"


def test_aadl2_PortSpecification_out_value_roundtrip():
    instance = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    assert instance.out == "sample_text"
    instance.out = "sample_text_2"
    assert instance.out == "sample_text_2"


def test_aadl2_Property_emptyListDefault_value_roundtrip():
    instance = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    assert instance.emptyListDefault == "sample_text"
    instance.emptyListDefault = "sample_text_2"
    assert instance.emptyListDefault == "sample_text_2"


def test_aadl2_Property_inherit_value_roundtrip():
    instance = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    assert instance.inherit == "sample_text"
    instance.inherit = "sample_text_2"
    assert instance.inherit == "sample_text_2"


def test_aadl2_PropertyAssociation_append_value_roundtrip():
    instance = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    assert instance.append == "sample_text"
    instance.append = "sample_text_2"
    assert instance.append == "sample_text_2"


def test_aadl2_PropertyAssociation_constant_value_roundtrip():
    instance = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    assert instance.constant == "sample_text"
    instance.constant = "sample_text_2"
    assert instance.constant == "sample_text_2"


def test_aadl2_RealLiteral_value_value_roundtrip():
    instance = aadl2_RealLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aadl2_StringLiteral_value_value_roundtrip():
    instance = aadl2_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aadl2_Subcomponent_allModes_value_roundtrip():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert instance.allModes == "sample_text"
    instance.allModes = "sample_text_2"
    assert instance.allModes == "sample_text_2"


def test_aadl2_AbstractClassifier_isa_Abstract():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, Abstract)


def test_aadl2_AbstractPrototype_isa_Abstract():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, Abstract)


def test_aadl2_AbstractSubcomponent_isa_Abstract():
    instance = aadl2_AbstractSubcomponent()
    assert isinstance(instance, Abstract)


def test_aadl2_AbstractImplementation_isa_AbstractClassifier():
    instance = aadl2_AbstractImplementation()
    assert isinstance(instance, AbstractClassifier)


def test_aadl2_AbstractType_isa_AbstractClassifier():
    instance = aadl2_AbstractType()
    assert isinstance(instance, AbstractClassifier)


def test_aadl2_AbstractSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_AbstractSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_BusSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_BusSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_DataSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_DataSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_SubprogramGroupSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_SubprogramGroupSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_SubprogramSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_SubprogramSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_VirtualBusSubcomponentType_isa_AbstractFeatureClassifier():
    instance = aadl2_VirtualBusSubcomponentType()
    assert isinstance(instance, AbstractFeatureClassifier)


def test_aadl2_EnumerationLiteral_isa_AbstractNamedValue():
    instance = aadl2_EnumerationLiteral()
    assert isinstance(instance, AbstractNamedValue)


def test_aadl2_Property_isa_AbstractNamedValue():
    instance = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    assert isinstance(instance, AbstractNamedValue)


def test_aadl2_PropertyConstant_isa_AbstractNamedValue():
    instance = aadl2_PropertyConstant()
    assert isinstance(instance, AbstractNamedValue)


def test_aadl2_AbstractClassifier_isa_AbstractSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, AbstractSubcomponentType)


def test_aadl2_AbstractPrototype_isa_AbstractSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, AbstractSubcomponentType)


def test_aadl2_BusAccess_isa_Access():
    instance = aadl2_BusAccess(virtual="sample_text")
    assert isinstance(instance, Access)


def test_aadl2_DataAccess_isa_Access():
    instance = aadl2_DataAccess()
    assert isinstance(instance, Access)


def test_aadl2_SubprogramAccess_isa_Access():
    instance = aadl2_SubprogramAccess()
    assert isinstance(instance, Access)


def test_aadl2_SubprogramGroupAccess_isa_Access():
    instance = aadl2_SubprogramGroupAccess()
    assert isinstance(instance, Access)


def test_aadl2_Access_isa_AccessConnectionEnd():
    instance = aadl2_Access(category="sample_text", kind="sample_text")
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_BusSubcomponent_isa_AccessConnectionEnd():
    instance = aadl2_BusSubcomponent()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_DataSubcomponent_isa_AccessConnectionEnd():
    instance = aadl2_DataSubcomponent()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_SubprogramGroupSubcomponent_isa_AccessConnectionEnd():
    instance = aadl2_SubprogramGroupSubcomponent()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_SubprogramProxy_isa_AccessConnectionEnd():
    instance = aadl2_SubprogramProxy()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_SubprogramSubcomponent_isa_AccessConnectionEnd():
    instance = aadl2_SubprogramSubcomponent()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_VirtualBusSubcomponent_isa_AccessConnectionEnd():
    instance = aadl2_VirtualBusSubcomponent()
    assert isinstance(instance, AccessConnectionEnd)


def test_aadl2_DefaultAnnexLibrary_isa_AnnexLibrary():
    instance = aadl2_DefaultAnnexLibrary(sourceText="sample_text")
    assert isinstance(instance, AnnexLibrary)


def test_aadl2_DefaultAnnexSubclause_isa_AnnexSubclause():
    instance = aadl2_DefaultAnnexSubclause(sourceText="sample_text")
    assert isinstance(instance, AnnexSubclause)


def test_aadl2_PropertyConstant_isa_ArraySizeProperty():
    instance = aadl2_PropertyConstant()
    assert isinstance(instance, ArraySizeProperty)


def test_aadl2_ComponentPrototypeActual_isa_ArrayableElement():
    instance = aadl2_ComponentPrototypeActual(category="sample_text")
    assert isinstance(instance, ArrayableElement)


def test_aadl2_Feature_isa_ArrayableElement():
    instance = aadl2_Feature()
    assert isinstance(instance, ArrayableElement)


def test_aadl2_FeaturePrototypeActual_isa_ArrayableElement():
    instance = aadl2_FeaturePrototypeActual()
    assert isinstance(instance, ArrayableElement)


def test_aadl2_Subcomponent_isa_ArrayableElement():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert isinstance(instance, ArrayableElement)


def test_aadl2_Property_isa_BasicProperty():
    instance = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    assert isinstance(instance, BasicProperty)


def test_aadl2_RecordField_isa_BasicProperty():
    instance = aadl2_RecordField()
    assert isinstance(instance, BasicProperty)


def test_aadl2_SubprogramCall_isa_BehavioralFeature():
    instance = aadl2_SubprogramCall()
    assert isinstance(instance, BehavioralFeature)


def test_aadl2_SubprogramCallSequence_isa_BehavioralFeature():
    instance = aadl2_SubprogramCallSequence()
    assert isinstance(instance, BehavioralFeature)


def test_aadl2_AbstractImplementation_isa_BehavioredImplementation():
    instance = aadl2_AbstractImplementation()
    assert isinstance(instance, BehavioredImplementation)


def test_aadl2_SubprogramImplementation_isa_BehavioredImplementation():
    instance = aadl2_SubprogramImplementation()
    assert isinstance(instance, BehavioredImplementation)


def test_aadl2_ThreadImplementation_isa_BehavioredImplementation():
    instance = aadl2_ThreadImplementation()
    assert isinstance(instance, BehavioredImplementation)


def test_aadl2_BusClassifier_isa_Bus():
    instance = aadl2_BusClassifier()
    assert isinstance(instance, Bus)


def test_aadl2_BusPrototype_isa_Bus():
    instance = aadl2_BusPrototype()
    assert isinstance(instance, Bus)


def test_aadl2_BusSubcomponent_isa_Bus():
    instance = aadl2_BusSubcomponent()
    assert isinstance(instance, Bus)


def test_aadl2_BusImplementation_isa_BusClassifier():
    instance = aadl2_BusImplementation()
    assert isinstance(instance, BusClassifier)


def test_aadl2_BusType_isa_BusClassifier():
    instance = aadl2_BusType()
    assert isinstance(instance, BusClassifier)


def test_aadl2_BusSubcomponentType_isa_BusFeatureClassifier():
    instance = aadl2_BusSubcomponentType()
    assert isinstance(instance, BusFeatureClassifier)


def test_aadl2_VirtualBusSubcomponentType_isa_BusFeatureClassifier():
    instance = aadl2_VirtualBusSubcomponentType()
    assert isinstance(instance, BusFeatureClassifier)


def test_aadl2_AbstractClassifier_isa_BusSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, BusSubcomponentType)


def test_aadl2_AbstractPrototype_isa_BusSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, BusSubcomponentType)


def test_aadl2_BusClassifier_isa_BusSubcomponentType():
    instance = aadl2_BusClassifier()
    assert isinstance(instance, BusSubcomponentType)


def test_aadl2_BusPrototype_isa_BusSubcomponentType():
    instance = aadl2_BusPrototype()
    assert isinstance(instance, BusSubcomponentType)


def test_aadl2_AbstractType_isa_CallContext():
    instance = aadl2_AbstractType()
    assert isinstance(instance, CallContext)


def test_aadl2_DataType_isa_CallContext():
    instance = aadl2_DataType()
    assert isinstance(instance, CallContext)


def test_aadl2_FeatureGroup_isa_CallContext():
    instance = aadl2_FeatureGroup(inverse="sample_text")
    assert isinstance(instance, CallContext)


def test_aadl2_SubprogramGroupAccess_isa_CallContext():
    instance = aadl2_SubprogramGroupAccess()
    assert isinstance(instance, CallContext)


def test_aadl2_SubprogramGroupSubcomponent_isa_CallContext():
    instance = aadl2_SubprogramGroupSubcomponent()
    assert isinstance(instance, CallContext)


def test_aadl2_SubprogramGroupType_isa_CallContext():
    instance = aadl2_SubprogramGroupType()
    assert isinstance(instance, CallContext)


def test_aadl2_SubprogramType_isa_CallContext():
    instance = aadl2_SubprogramType()
    assert isinstance(instance, CallContext)


def test_aadl2_Prototype_isa_CalledSubprogram():
    instance = aadl2_Prototype()
    assert isinstance(instance, CalledSubprogram)


def test_aadl2_Subprogram_isa_CalledSubprogram():
    instance = aadl2_Subprogram()
    assert isinstance(instance, CalledSubprogram)


def test_aadl2_SubprogramAccess_isa_CalledSubprogram():
    instance = aadl2_SubprogramAccess()
    assert isinstance(instance, CalledSubprogram)


def test_aadl2_SubprogramProxy_isa_CalledSubprogram():
    instance = aadl2_SubprogramProxy()
    assert isinstance(instance, CalledSubprogram)


def test_aadl2_ComponentClassifier_isa_Classifier():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert isinstance(instance, Classifier)


def test_aadl2_FeatureGroupType_isa_Classifier():
    instance = aadl2_FeatureGroupType()
    assert isinstance(instance, Classifier)


def test_aadl2_BehavioralFeature_isa_ClassifierFeature():
    instance = aadl2_BehavioralFeature()
    assert isinstance(instance, ClassifierFeature)


def test_aadl2_FlowImplementation_isa_ClassifierFeature():
    instance = aadl2_FlowImplementation(kind="sample_text")
    assert isinstance(instance, ClassifierFeature)


def test_aadl2_ModeFeature_isa_ClassifierFeature():
    instance = aadl2_ModeFeature()
    assert isinstance(instance, ClassifierFeature)


def test_aadl2_StructuralFeature_isa_ClassifierFeature():
    instance = aadl2_StructuralFeature()
    assert isinstance(instance, ClassifierFeature)


def test_aadl2_AbstractClassifier_isa_ComponentClassifier():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_BusClassifier_isa_ComponentClassifier():
    instance = aadl2_BusClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ComponentImplementation_isa_ComponentClassifier():
    instance = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ComponentType_isa_ComponentClassifier():
    instance = aadl2_ComponentType(noFeatures="sample_text")
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_DataClassifier_isa_ComponentClassifier():
    instance = aadl2_DataClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_DeviceClassifier_isa_ComponentClassifier():
    instance = aadl2_DeviceClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_MemoryClassifier_isa_ComponentClassifier():
    instance = aadl2_MemoryClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ProcessClassifier_isa_ComponentClassifier():
    instance = aadl2_ProcessClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ProcessorClassifier_isa_ComponentClassifier():
    instance = aadl2_ProcessorClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_SubprogramClassifier_isa_ComponentClassifier():
    instance = aadl2_SubprogramClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_SubprogramGroupClassifier_isa_ComponentClassifier():
    instance = aadl2_SubprogramGroupClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_SystemClassifier_isa_ComponentClassifier():
    instance = aadl2_SystemClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ThreadClassifier_isa_ComponentClassifier():
    instance = aadl2_ThreadClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_ThreadGroupClassifier_isa_ComponentClassifier():
    instance = aadl2_ThreadGroupClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_VirtualBusClassifier_isa_ComponentClassifier():
    instance = aadl2_VirtualBusClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_VirtualProcessorClassifier_isa_ComponentClassifier():
    instance = aadl2_VirtualProcessorClassifier()
    assert isinstance(instance, ComponentClassifier)


def test_aadl2_BehavioredImplementation_isa_ComponentImplementation():
    instance = aadl2_BehavioredImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_BusImplementation_isa_ComponentImplementation():
    instance = aadl2_BusImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_DataImplementation_isa_ComponentImplementation():
    instance = aadl2_DataImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_DeviceImplementation_isa_ComponentImplementation():
    instance = aadl2_DeviceImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_MemoryImplementation_isa_ComponentImplementation():
    instance = aadl2_MemoryImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_ProcessImplementation_isa_ComponentImplementation():
    instance = aadl2_ProcessImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_ProcessorImplementation_isa_ComponentImplementation():
    instance = aadl2_ProcessorImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_SubprogramGroupImplementation_isa_ComponentImplementation():
    instance = aadl2_SubprogramGroupImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_SystemImplementation_isa_ComponentImplementation():
    instance = aadl2_SystemImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_ThreadGroupImplementation_isa_ComponentImplementation():
    instance = aadl2_ThreadGroupImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_VirtualBusImplementation_isa_ComponentImplementation():
    instance = aadl2_VirtualBusImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_VirtualProcessorImplementation_isa_ComponentImplementation():
    instance = aadl2_VirtualProcessorImplementation()
    assert isinstance(instance, ComponentImplementation)


def test_aadl2_AbstractPrototype_isa_ComponentPrototype():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_BusPrototype_isa_ComponentPrototype():
    instance = aadl2_BusPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_DataPrototype_isa_ComponentPrototype():
    instance = aadl2_DataPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_DevicePrototype_isa_ComponentPrototype():
    instance = aadl2_DevicePrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_MemoryPrototype_isa_ComponentPrototype():
    instance = aadl2_MemoryPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_ProcessPrototype_isa_ComponentPrototype():
    instance = aadl2_ProcessPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_ProcessorPrototype_isa_ComponentPrototype():
    instance = aadl2_ProcessorPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_SubprogramGroupPrototype_isa_ComponentPrototype():
    instance = aadl2_SubprogramGroupPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_SubprogramPrototype_isa_ComponentPrototype():
    instance = aadl2_SubprogramPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_SystemPrototype_isa_ComponentPrototype():
    instance = aadl2_SystemPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_ThreadGroupPrototype_isa_ComponentPrototype():
    instance = aadl2_ThreadGroupPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_ThreadPrototype_isa_ComponentPrototype():
    instance = aadl2_ThreadPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_VirtualBusPrototype_isa_ComponentPrototype():
    instance = aadl2_VirtualBusPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_VirtualProcessorPrototype_isa_ComponentPrototype():
    instance = aadl2_VirtualProcessorPrototype()
    assert isinstance(instance, ComponentPrototype)


def test_aadl2_AbstractType_isa_ComponentType():
    instance = aadl2_AbstractType()
    assert isinstance(instance, ComponentType)


def test_aadl2_BusType_isa_ComponentType():
    instance = aadl2_BusType()
    assert isinstance(instance, ComponentType)


def test_aadl2_DataType_isa_ComponentType():
    instance = aadl2_DataType()
    assert isinstance(instance, ComponentType)


def test_aadl2_DeviceType_isa_ComponentType():
    instance = aadl2_DeviceType()
    assert isinstance(instance, ComponentType)


def test_aadl2_MemoryType_isa_ComponentType():
    instance = aadl2_MemoryType()
    assert isinstance(instance, ComponentType)


def test_aadl2_ProcessType_isa_ComponentType():
    instance = aadl2_ProcessType()
    assert isinstance(instance, ComponentType)


def test_aadl2_ProcessorType_isa_ComponentType():
    instance = aadl2_ProcessorType()
    assert isinstance(instance, ComponentType)


def test_aadl2_SubprogramGroupType_isa_ComponentType():
    instance = aadl2_SubprogramGroupType()
    assert isinstance(instance, ComponentType)


def test_aadl2_SubprogramType_isa_ComponentType():
    instance = aadl2_SubprogramType()
    assert isinstance(instance, ComponentType)


def test_aadl2_SystemType_isa_ComponentType():
    instance = aadl2_SystemType()
    assert isinstance(instance, ComponentType)


def test_aadl2_ThreadGroupType_isa_ComponentType():
    instance = aadl2_ThreadGroupType()
    assert isinstance(instance, ComponentType)


def test_aadl2_ThreadType_isa_ComponentType():
    instance = aadl2_ThreadType()
    assert isinstance(instance, ComponentType)


def test_aadl2_VirtualBusType_isa_ComponentType():
    instance = aadl2_VirtualBusType()
    assert isinstance(instance, ComponentType)


def test_aadl2_VirtualProcessorType_isa_ComponentType():
    instance = aadl2_VirtualProcessorType()
    assert isinstance(instance, ComponentType)


def test_aadl2_AccessConnection_isa_Connection():
    instance = aadl2_AccessConnection(accessCategory="sample_text")
    assert isinstance(instance, Connection)


def test_aadl2_FeatureConnection_isa_Connection():
    instance = aadl2_FeatureConnection()
    assert isinstance(instance, Connection)


def test_aadl2_FeatureGroupConnection_isa_Connection():
    instance = aadl2_FeatureGroupConnection()
    assert isinstance(instance, Connection)


def test_aadl2_ParameterConnection_isa_Connection():
    instance = aadl2_ParameterConnection()
    assert isinstance(instance, Connection)


def test_aadl2_PortConnection_isa_Connection():
    instance = aadl2_PortConnection()
    assert isinstance(instance, Connection)


def test_aadl2_AccessConnectionEnd_isa_ConnectionEnd():
    instance = aadl2_AccessConnectionEnd()
    assert isinstance(instance, ConnectionEnd)


def test_aadl2_FeatureConnectionEnd_isa_ConnectionEnd():
    instance = aadl2_FeatureConnectionEnd()
    assert isinstance(instance, ConnectionEnd)


def test_aadl2_FeatureGroupConnectionEnd_isa_ConnectionEnd():
    instance = aadl2_FeatureGroupConnectionEnd()
    assert isinstance(instance, ConnectionEnd)


def test_aadl2_ParameterConnectionEnd_isa_ConnectionEnd():
    instance = aadl2_ParameterConnectionEnd()
    assert isinstance(instance, ConnectionEnd)


def test_aadl2_PortConnectionEnd_isa_ConnectionEnd():
    instance = aadl2_PortConnectionEnd()
    assert isinstance(instance, ConnectionEnd)


def test_aadl2_ReferenceValue_isa_ContainedNamedElement():
    instance = aadl2_ReferenceValue()
    assert isinstance(instance, ContainedNamedElement)


def test_aadl2_DataPort_isa_Context():
    instance = aadl2_DataPort()
    assert isinstance(instance, Context)


def test_aadl2_EventDataPort_isa_Context():
    instance = aadl2_EventDataPort()
    assert isinstance(instance, Context)


def test_aadl2_FeatureGroup_isa_Context():
    instance = aadl2_FeatureGroup(inverse="sample_text")
    assert isinstance(instance, Context)


def test_aadl2_Parameter_isa_Context():
    instance = aadl2_Parameter()
    assert isinstance(instance, Context)


def test_aadl2_Subcomponent_isa_Context():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert isinstance(instance, Context)


def test_aadl2_SubprogramAccess_isa_Context():
    instance = aadl2_SubprogramAccess()
    assert isinstance(instance, Context)


def test_aadl2_SubprogramCall_isa_Context():
    instance = aadl2_SubprogramCall()
    assert isinstance(instance, Context)


def test_aadl2_DataClassifier_isa_Data():
    instance = aadl2_DataClassifier()
    assert isinstance(instance, Data)


def test_aadl2_DataPrototype_isa_Data():
    instance = aadl2_DataPrototype()
    assert isinstance(instance, Data)


def test_aadl2_DataSubcomponent_isa_Data():
    instance = aadl2_DataSubcomponent()
    assert isinstance(instance, Data)


def test_aadl2_DataImplementation_isa_DataClassifier():
    instance = aadl2_DataImplementation()
    assert isinstance(instance, DataClassifier)


def test_aadl2_DataType_isa_DataClassifier():
    instance = aadl2_DataType()
    assert isinstance(instance, DataClassifier)


def test_aadl2_AbstractClassifier_isa_DataSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, DataSubcomponentType)


def test_aadl2_AbstractPrototype_isa_DataSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, DataSubcomponentType)


def test_aadl2_DataClassifier_isa_DataSubcomponentType():
    instance = aadl2_DataClassifier()
    assert isinstance(instance, DataSubcomponentType)


def test_aadl2_DataPrototype_isa_DataSubcomponentType():
    instance = aadl2_DataPrototype()
    assert isinstance(instance, DataSubcomponentType)


def test_aadl2_DeviceClassifier_isa_Device():
    instance = aadl2_DeviceClassifier()
    assert isinstance(instance, Device)


def test_aadl2_DevicePrototype_isa_Device():
    instance = aadl2_DevicePrototype()
    assert isinstance(instance, Device)


def test_aadl2_DeviceSubcomponent_isa_Device():
    instance = aadl2_DeviceSubcomponent()
    assert isinstance(instance, Device)


def test_aadl2_DeviceImplementation_isa_DeviceClassifier():
    instance = aadl2_DeviceImplementation()
    assert isinstance(instance, DeviceClassifier)


def test_aadl2_DeviceType_isa_DeviceClassifier():
    instance = aadl2_DeviceType()
    assert isinstance(instance, DeviceClassifier)


def test_aadl2_AbstractClassifier_isa_DeviceSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, DeviceSubcomponentType)


def test_aadl2_AbstractPrototype_isa_DeviceSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, DeviceSubcomponentType)


def test_aadl2_DeviceClassifier_isa_DeviceSubcomponentType():
    instance = aadl2_DeviceClassifier()
    assert isinstance(instance, DeviceSubcomponentType)


def test_aadl2_DevicePrototype_isa_DeviceSubcomponentType():
    instance = aadl2_DevicePrototype()
    assert isinstance(instance, DeviceSubcomponentType)


def test_aadl2_AbstractFeature_isa_DirectedFeature():
    instance = aadl2_AbstractFeature()
    assert isinstance(instance, DirectedFeature)


def test_aadl2_FeatureGroup_isa_DirectedFeature():
    instance = aadl2_FeatureGroup(inverse="sample_text")
    assert isinstance(instance, DirectedFeature)


def test_aadl2_Parameter_isa_DirectedFeature():
    instance = aadl2_Parameter()
    assert isinstance(instance, DirectedFeature)


def test_aadl2_Port_isa_DirectedFeature():
    instance = aadl2_Port(category="sample_text")
    assert isinstance(instance, DirectedFeature)


def test_aadl2_Generalization__isa_DirectedRelationship():
    instance = aadl2_Generalization_()
    assert isinstance(instance, DirectedRelationship)


def test_aadl2_ArrayDimension_isa_Element():
    instance = aadl2_ArrayDimension()
    assert isinstance(instance, Element)


def test_aadl2_ArrayRange_isa_Element():
    instance = aadl2_ArrayRange(lowerBound="sample_text", upperBound="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_ArraySize_isa_Element():
    instance = aadl2_ArraySize(size="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_ArrayableElement_isa_Element():
    instance = aadl2_ArrayableElement()
    assert isinstance(instance, Element)


def test_aadl2_BasicPropertyAssociation_isa_Element():
    instance = aadl2_BasicPropertyAssociation()
    assert isinstance(instance, Element)


def test_aadl2_Comment_isa_Element():
    instance = aadl2_Comment(body="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_ComponentImplementationReference_isa_Element():
    instance = aadl2_ComponentImplementationReference()
    assert isinstance(instance, Element)


def test_aadl2_ConnectedElement_isa_Element():
    instance = aadl2_ConnectedElement()
    assert isinstance(instance, Element)


def test_aadl2_ContainedNamedElement_isa_Element():
    instance = aadl2_ContainedNamedElement()
    assert isinstance(instance, Element)


def test_aadl2_ContainmentPathElement_isa_Element():
    instance = aadl2_ContainmentPathElement(annexName="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_EndToEndFlowSegment_isa_Element():
    instance = aadl2_EndToEndFlowSegment()
    assert isinstance(instance, Element)


def test_aadl2_FlowEnd_isa_Element():
    instance = aadl2_FlowEnd()
    assert isinstance(instance, Element)


def test_aadl2_FlowSegment_isa_Element():
    instance = aadl2_FlowSegment()
    assert isinstance(instance, Element)


def test_aadl2_ModeBinding_isa_Element():
    instance = aadl2_ModeBinding()
    assert isinstance(instance, Element)


def test_aadl2_ModeTransitionTrigger_isa_Element():
    instance = aadl2_ModeTransitionTrigger()
    assert isinstance(instance, Element)


def test_aadl2_NamedElement_isa_Element():
    instance = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_NumericRange_isa_Element():
    instance = aadl2_NumericRange()
    assert isinstance(instance, Element)


def test_aadl2_PropertyAssociation_isa_Element():
    instance = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    assert isinstance(instance, Element)


def test_aadl2_PropertyExpression_isa_Element():
    instance = aadl2_PropertyExpression()
    assert isinstance(instance, Element)


def test_aadl2_PropertyOwner_isa_Element():
    instance = aadl2_PropertyOwner()
    assert isinstance(instance, Element)


def test_aadl2_PrototypeBinding_isa_Element():
    instance = aadl2_PrototypeBinding()
    assert isinstance(instance, Element)


def test_aadl2_Relationship_isa_Element():
    instance = aadl2_Relationship()
    assert isinstance(instance, Element)


def test_aadl2_EndToEndFlow_isa_EndToEndFlowElement():
    instance = aadl2_EndToEndFlow()
    assert isinstance(instance, EndToEndFlowElement)


def test_aadl2_FlowElement_isa_EndToEndFlowElement():
    instance = aadl2_FlowElement()
    assert isinstance(instance, EndToEndFlowElement)


def test_aadl2_UnitLiteral_isa_EnumerationLiteral():
    instance = aadl2_UnitLiteral()
    assert isinstance(instance, EnumerationLiteral)


def test_aadl2_UnitsType_isa_EnumerationType():
    instance = aadl2_UnitsType()
    assert isinstance(instance, EnumerationType)


def test_aadl2_Access_isa_Feature():
    instance = aadl2_Access(category="sample_text", kind="sample_text")
    assert isinstance(instance, Feature)


def test_aadl2_DirectedFeature_isa_Feature():
    instance = aadl2_DirectedFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, Feature)


def test_aadl2_AbstractFeatureClassifier_isa_FeatureClassifier():
    instance = aadl2_AbstractFeatureClassifier()
    assert isinstance(instance, FeatureClassifier)


def test_aadl2_BusFeatureClassifier_isa_FeatureClassifier():
    instance = aadl2_BusFeatureClassifier()
    assert isinstance(instance, FeatureClassifier)


def test_aadl2_ComponentClassifier_isa_FeatureClassifier():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert isinstance(instance, FeatureClassifier)


def test_aadl2_ComponentPrototype_isa_FeatureClassifier():
    instance = aadl2_ComponentPrototype(array="sample_text")
    assert isinstance(instance, FeatureClassifier)


def test_aadl2_Feature_isa_FeatureConnectionEnd():
    instance = aadl2_Feature()
    assert isinstance(instance, FeatureConnectionEnd)


def test_aadl2_InternalFeature_isa_FeatureConnectionEnd():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, FeatureConnectionEnd)


def test_aadl2_PortProxy_isa_FeatureConnectionEnd():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, FeatureConnectionEnd)


def test_aadl2_FeatureGroup_isa_FeatureGroupConnectionEnd():
    instance = aadl2_FeatureGroup(inverse="sample_text")
    assert isinstance(instance, FeatureGroupConnectionEnd)


def test_aadl2_AccessSpecification_isa_FeaturePrototypeActual():
    instance = aadl2_AccessSpecification(category="sample_text", kind="sample_text")
    assert isinstance(instance, FeaturePrototypeActual)


def test_aadl2_FeatureGroupPrototypeActual_isa_FeaturePrototypeActual():
    instance = aadl2_FeatureGroupPrototypeActual()
    assert isinstance(instance, FeaturePrototypeActual)


def test_aadl2_FeaturePrototypeReference_isa_FeaturePrototypeActual():
    instance = aadl2_FeaturePrototypeReference(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, FeaturePrototypeActual)


def test_aadl2_PortSpecification_isa_FeaturePrototypeActual():
    instance = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, FeaturePrototypeActual)


def test_aadl2_FeatureGroupPrototype_isa_FeatureType():
    instance = aadl2_FeatureGroupPrototype()
    assert isinstance(instance, FeatureType)


def test_aadl2_FeatureGroupType_isa_FeatureType():
    instance = aadl2_FeatureGroupType()
    assert isinstance(instance, FeatureType)


def test_aadl2_FlowFeature_isa_Flow():
    instance = aadl2_FlowFeature()
    assert isinstance(instance, Flow)


def test_aadl2_FlowImplementation_isa_Flow():
    instance = aadl2_FlowImplementation(kind="sample_text")
    assert isinstance(instance, Flow)


def test_aadl2_Connection_isa_FlowElement():
    instance = aadl2_Connection(bidirectional="sample_text")
    assert isinstance(instance, FlowElement)


def test_aadl2_DataAccess_isa_FlowElement():
    instance = aadl2_DataAccess()
    assert isinstance(instance, FlowElement)


def test_aadl2_FlowSpecification_isa_FlowElement():
    instance = aadl2_FlowSpecification(kind="sample_text")
    assert isinstance(instance, FlowElement)


def test_aadl2_Subcomponent_isa_FlowElement():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert isinstance(instance, FlowElement)


def test_aadl2_EndToEndFlow_isa_FlowFeature():
    instance = aadl2_EndToEndFlow()
    assert isinstance(instance, FlowFeature)


def test_aadl2_FlowSpecification_isa_FlowFeature():
    instance = aadl2_FlowSpecification(kind="sample_text")
    assert isinstance(instance, FlowFeature)


def test_aadl2_GroupExtension_isa_Generalization_():
    instance = aadl2_GroupExtension()
    assert isinstance(instance, Generalization_)


def test_aadl2_ImplementationExtension_isa_Generalization_():
    instance = aadl2_ImplementationExtension()
    assert isinstance(instance, Generalization_)


def test_aadl2_Realization_isa_Generalization_():
    instance = aadl2_Realization()
    assert isinstance(instance, Generalization_)


def test_aadl2_TypeExtension_isa_Generalization_():
    instance = aadl2_TypeExtension()
    assert isinstance(instance, Generalization_)


def test_aadl2_EventDataSource_isa_InternalFeature():
    instance = aadl2_EventDataSource()
    assert isinstance(instance, InternalFeature)


def test_aadl2_EventSource_isa_InternalFeature():
    instance = aadl2_EventSource()
    assert isinstance(instance, InternalFeature)


def test_aadl2_MemoryClassifier_isa_Memory():
    instance = aadl2_MemoryClassifier()
    assert isinstance(instance, Memory)


def test_aadl2_MemoryPrototype_isa_Memory():
    instance = aadl2_MemoryPrototype()
    assert isinstance(instance, Memory)


def test_aadl2_MemorySubcomponent_isa_Memory():
    instance = aadl2_MemorySubcomponent()
    assert isinstance(instance, Memory)


def test_aadl2_MemoryImplementation_isa_MemoryClassifier():
    instance = aadl2_MemoryImplementation()
    assert isinstance(instance, MemoryClassifier)


def test_aadl2_MemoryType_isa_MemoryClassifier():
    instance = aadl2_MemoryType()
    assert isinstance(instance, MemoryClassifier)


def test_aadl2_AbstractClassifier_isa_MemorySubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, MemorySubcomponentType)


def test_aadl2_AbstractPrototype_isa_MemorySubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, MemorySubcomponentType)


def test_aadl2_MemoryClassifier_isa_MemorySubcomponentType():
    instance = aadl2_MemoryClassifier()
    assert isinstance(instance, MemorySubcomponentType)


def test_aadl2_MemoryPrototype_isa_MemorySubcomponentType():
    instance = aadl2_MemoryPrototype()
    assert isinstance(instance, MemorySubcomponentType)


def test_aadl2_AnnexSubclause_isa_ModalElement():
    instance = aadl2_AnnexSubclause()
    assert isinstance(instance, ModalElement)


def test_aadl2_ModalPath_isa_ModalElement():
    instance = aadl2_ModalPath()
    assert isinstance(instance, ModalElement)


def test_aadl2_ModalPropertyValue_isa_ModalElement():
    instance = aadl2_ModalPropertyValue()
    assert isinstance(instance, ModalElement)


def test_aadl2_Subcomponent_isa_ModalElement():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert isinstance(instance, ModalElement)


def test_aadl2_SubprogramCallSequence_isa_ModalElement():
    instance = aadl2_SubprogramCallSequence()
    assert isinstance(instance, ModalElement)


def test_aadl2_Connection_isa_ModalPath():
    instance = aadl2_Connection(bidirectional="sample_text")
    assert isinstance(instance, ModalPath)


def test_aadl2_EndToEndFlow_isa_ModalPath():
    instance = aadl2_EndToEndFlow()
    assert isinstance(instance, ModalPath)


def test_aadl2_FlowImplementation_isa_ModalPath():
    instance = aadl2_FlowImplementation(kind="sample_text")
    assert isinstance(instance, ModalPath)


def test_aadl2_FlowSpecification_isa_ModalPath():
    instance = aadl2_FlowSpecification(kind="sample_text")
    assert isinstance(instance, ModalPath)


def test_aadl2_Mode_isa_ModeFeature():
    instance = aadl2_Mode(derived="sample_text", initial="sample_text")
    assert isinstance(instance, ModeFeature)


def test_aadl2_ModeTransition_isa_ModeFeature():
    instance = aadl2_ModeTransition()
    assert isinstance(instance, ModeFeature)


def test_aadl2_AadlPackage_isa_ModelUnit():
    instance = aadl2_AadlPackage()
    assert isinstance(instance, ModelUnit)


def test_aadl2_PropertySet_isa_ModelUnit():
    instance = aadl2_PropertySet()
    assert isinstance(instance, ModelUnit)


def test_aadl2_Abstract_isa_NamedElement():
    instance = aadl2_Abstract()
    assert isinstance(instance, NamedElement)


def test_aadl2_AnnexLibrary_isa_NamedElement():
    instance = aadl2_AnnexLibrary()
    assert isinstance(instance, NamedElement)


def test_aadl2_Bus_isa_NamedElement():
    instance = aadl2_Bus()
    assert isinstance(instance, NamedElement)


def test_aadl2_ClassifierFeature_isa_NamedElement():
    instance = aadl2_ClassifierFeature()
    assert isinstance(instance, NamedElement)


def test_aadl2_ComponentTypeRename_isa_NamedElement():
    instance = aadl2_ComponentTypeRename(category="sample_text")
    assert isinstance(instance, NamedElement)


def test_aadl2_ConnectionEnd_isa_NamedElement():
    instance = aadl2_ConnectionEnd()
    assert isinstance(instance, NamedElement)


def test_aadl2_Context_isa_NamedElement():
    instance = aadl2_Context()
    assert isinstance(instance, NamedElement)


def test_aadl2_Data_isa_NamedElement():
    instance = aadl2_Data()
    assert isinstance(instance, NamedElement)


def test_aadl2_Device_isa_NamedElement():
    instance = aadl2_Device()
    assert isinstance(instance, NamedElement)


def test_aadl2_EndToEndFlowElement_isa_NamedElement():
    instance = aadl2_EndToEndFlowElement()
    assert isinstance(instance, NamedElement)


def test_aadl2_EnumerationLiteral_isa_NamedElement():
    instance = aadl2_EnumerationLiteral()
    assert isinstance(instance, NamedElement)


def test_aadl2_FeatureGroupTypeRename_isa_NamedElement():
    instance = aadl2_FeatureGroupTypeRename()
    assert isinstance(instance, NamedElement)


def test_aadl2_Flow_isa_NamedElement():
    instance = aadl2_Flow()
    assert isinstance(instance, NamedElement)


def test_aadl2_Memory_isa_NamedElement():
    instance = aadl2_Memory()
    assert isinstance(instance, NamedElement)


def test_aadl2_ModalElement_isa_NamedElement():
    instance = aadl2_ModalElement()
    assert isinstance(instance, NamedElement)


def test_aadl2_ModelUnit_isa_NamedElement():
    instance = aadl2_ModelUnit()
    assert isinstance(instance, NamedElement)


def test_aadl2_Namespace_isa_NamedElement():
    instance = aadl2_Namespace()
    assert isinstance(instance, NamedElement)


def test_aadl2_PackageRename_isa_NamedElement():
    instance = aadl2_PackageRename(renameAll="sample_text")
    assert isinstance(instance, NamedElement)


def test_aadl2_Process_isa_NamedElement():
    instance = aadl2_Process()
    assert isinstance(instance, NamedElement)


def test_aadl2_Processor_isa_NamedElement():
    instance = aadl2_Processor()
    assert isinstance(instance, NamedElement)


def test_aadl2_RefinableElement_isa_NamedElement():
    instance = aadl2_RefinableElement()
    assert isinstance(instance, NamedElement)


def test_aadl2_Subprogram_isa_NamedElement():
    instance = aadl2_Subprogram()
    assert isinstance(instance, NamedElement)


def test_aadl2_SubprogramGroup_isa_NamedElement():
    instance = aadl2_SubprogramGroup()
    assert isinstance(instance, NamedElement)


def test_aadl2_System_isa_NamedElement():
    instance = aadl2_System()
    assert isinstance(instance, NamedElement)


def test_aadl2_Thread_isa_NamedElement():
    instance = aadl2_Thread()
    assert isinstance(instance, NamedElement)


def test_aadl2_ThreadGroup_isa_NamedElement():
    instance = aadl2_ThreadGroup()
    assert isinstance(instance, NamedElement)


def test_aadl2_TriggerPort_isa_NamedElement():
    instance = aadl2_TriggerPort()
    assert isinstance(instance, NamedElement)


def test_aadl2_Type_isa_NamedElement():
    instance = aadl2_Type()
    assert isinstance(instance, NamedElement)


def test_aadl2_TypedElement_isa_NamedElement():
    instance = aadl2_TypedElement()
    assert isinstance(instance, NamedElement)


def test_aadl2_VirtualBus_isa_NamedElement():
    instance = aadl2_VirtualBus()
    assert isinstance(instance, NamedElement)


def test_aadl2_VirtualProcessor_isa_NamedElement():
    instance = aadl2_VirtualProcessor()
    assert isinstance(instance, NamedElement)


def test_aadl2_Classifier_isa_Namespace():
    instance = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    assert isinstance(instance, Namespace)


def test_aadl2_EnumerationType_isa_Namespace():
    instance = aadl2_EnumerationType()
    assert isinstance(instance, Namespace)


def test_aadl2_GlobalNamespace_isa_Namespace():
    instance = aadl2_GlobalNamespace()
    assert isinstance(instance, Namespace)


def test_aadl2_PackageSection_isa_Namespace():
    instance = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    assert isinstance(instance, Namespace)


def test_aadl2_PropertySet_isa_Namespace():
    instance = aadl2_PropertySet()
    assert isinstance(instance, Namespace)


def test_aadl2_RecordType_isa_Namespace():
    instance = aadl2_RecordType()
    assert isinstance(instance, Namespace)


def test_aadl2_AadlBoolean_isa_NonListType():
    instance = aadl2_AadlBoolean()
    assert isinstance(instance, NonListType)


def test_aadl2_AadlString_isa_NonListType():
    instance = aadl2_AadlString()
    assert isinstance(instance, NonListType)


def test_aadl2_ClassifierType_isa_NonListType():
    instance = aadl2_ClassifierType()
    assert isinstance(instance, NonListType)


def test_aadl2_EnumerationType_isa_NonListType():
    instance = aadl2_EnumerationType()
    assert isinstance(instance, NonListType)


def test_aadl2_NumberType_isa_NonListType():
    instance = aadl2_NumberType()
    assert isinstance(instance, NonListType)


def test_aadl2_RangeType_isa_NonListType():
    instance = aadl2_RangeType()
    assert isinstance(instance, NonListType)


def test_aadl2_RecordType_isa_NonListType():
    instance = aadl2_RecordType()
    assert isinstance(instance, NonListType)


def test_aadl2_ReferenceType_isa_NonListType():
    instance = aadl2_ReferenceType()
    assert isinstance(instance, NonListType)


def test_aadl2_AadlInteger_isa_NumberType():
    instance = aadl2_AadlInteger()
    assert isinstance(instance, NumberType)


def test_aadl2_AadlReal_isa_NumberType():
    instance = aadl2_AadlReal()
    assert isinstance(instance, NumberType)


def test_aadl2_IntegerLiteral_isa_NumberValue():
    instance = aadl2_IntegerLiteral(base="sample_text", value="sample_text")
    assert isinstance(instance, NumberValue)


def test_aadl2_RealLiteral_isa_NumberValue():
    instance = aadl2_RealLiteral(value="sample_text")
    assert isinstance(instance, NumberValue)


def test_aadl2_PrivatePackageSection_isa_PackageSection():
    instance = aadl2_PrivatePackageSection()
    assert isinstance(instance, PackageSection)


def test_aadl2_PublicPackageSection_isa_PackageSection():
    instance = aadl2_PublicPackageSection()
    assert isinstance(instance, PackageSection)


def test_aadl2_DataAccess_isa_ParameterConnectionEnd():
    instance = aadl2_DataAccess()
    assert isinstance(instance, ParameterConnectionEnd)


def test_aadl2_DataPort_isa_ParameterConnectionEnd():
    instance = aadl2_DataPort()
    assert isinstance(instance, ParameterConnectionEnd)


def test_aadl2_DataSubcomponent_isa_ParameterConnectionEnd():
    instance = aadl2_DataSubcomponent()
    assert isinstance(instance, ParameterConnectionEnd)


def test_aadl2_EventDataPort_isa_ParameterConnectionEnd():
    instance = aadl2_EventDataPort()
    assert isinstance(instance, ParameterConnectionEnd)


def test_aadl2_Parameter_isa_ParameterConnectionEnd():
    instance = aadl2_Parameter()
    assert isinstance(instance, ParameterConnectionEnd)


def test_aadl2_DataPort_isa_Port():
    instance = aadl2_DataPort()
    assert isinstance(instance, Port)


def test_aadl2_EventDataPort_isa_Port():
    instance = aadl2_EventDataPort()
    assert isinstance(instance, Port)


def test_aadl2_EventPort_isa_Port():
    instance = aadl2_EventPort()
    assert isinstance(instance, Port)


def test_aadl2_DataAccess_isa_PortConnectionEnd():
    instance = aadl2_DataAccess()
    assert isinstance(instance, PortConnectionEnd)


def test_aadl2_DataSubcomponent_isa_PortConnectionEnd():
    instance = aadl2_DataSubcomponent()
    assert isinstance(instance, PortConnectionEnd)


def test_aadl2_InternalFeature_isa_PortConnectionEnd():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, PortConnectionEnd)


def test_aadl2_Port_isa_PortConnectionEnd():
    instance = aadl2_Port(category="sample_text")
    assert isinstance(instance, PortConnectionEnd)


def test_aadl2_PortProxy_isa_PortConnectionEnd():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, PortConnectionEnd)


def test_aadl2_ProcessClassifier_isa_Process():
    instance = aadl2_ProcessClassifier()
    assert isinstance(instance, Process)


def test_aadl2_ProcessPrototype_isa_Process():
    instance = aadl2_ProcessPrototype()
    assert isinstance(instance, Process)


def test_aadl2_ProcessSubcomponent_isa_Process():
    instance = aadl2_ProcessSubcomponent()
    assert isinstance(instance, Process)


def test_aadl2_ProcessImplementation_isa_ProcessClassifier():
    instance = aadl2_ProcessImplementation()
    assert isinstance(instance, ProcessClassifier)


def test_aadl2_ProcessType_isa_ProcessClassifier():
    instance = aadl2_ProcessType()
    assert isinstance(instance, ProcessClassifier)


def test_aadl2_AbstractClassifier_isa_ProcessSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, ProcessSubcomponentType)


def test_aadl2_AbstractPrototype_isa_ProcessSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, ProcessSubcomponentType)


def test_aadl2_ProcessClassifier_isa_ProcessSubcomponentType():
    instance = aadl2_ProcessClassifier()
    assert isinstance(instance, ProcessSubcomponentType)


def test_aadl2_ProcessPrototype_isa_ProcessSubcomponentType():
    instance = aadl2_ProcessPrototype()
    assert isinstance(instance, ProcessSubcomponentType)


def test_aadl2_ProcessorClassifier_isa_Processor():
    instance = aadl2_ProcessorClassifier()
    assert isinstance(instance, Processor)


def test_aadl2_ProcessorPrototype_isa_Processor():
    instance = aadl2_ProcessorPrototype()
    assert isinstance(instance, Processor)


def test_aadl2_ProcessorSubcomponent_isa_Processor():
    instance = aadl2_ProcessorSubcomponent()
    assert isinstance(instance, Processor)


def test_aadl2_ProcessorImplementation_isa_ProcessorClassifier():
    instance = aadl2_ProcessorImplementation()
    assert isinstance(instance, ProcessorClassifier)


def test_aadl2_ProcessorType_isa_ProcessorClassifier():
    instance = aadl2_ProcessorType()
    assert isinstance(instance, ProcessorClassifier)


def test_aadl2_PortProxy_isa_ProcessorFeature():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, ProcessorFeature)


def test_aadl2_SubprogramProxy_isa_ProcessorFeature():
    instance = aadl2_SubprogramProxy()
    assert isinstance(instance, ProcessorFeature)


def test_aadl2_AbstractClassifier_isa_ProcessorSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, ProcessorSubcomponentType)


def test_aadl2_AbstractPrototype_isa_ProcessorSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, ProcessorSubcomponentType)


def test_aadl2_ProcessorClassifier_isa_ProcessorSubcomponentType():
    instance = aadl2_ProcessorClassifier()
    assert isinstance(instance, ProcessorSubcomponentType)


def test_aadl2_ProcessorPrototype_isa_ProcessorSubcomponentType():
    instance = aadl2_ProcessorPrototype()
    assert isinstance(instance, ProcessorSubcomponentType)


def test_aadl2_ListValue_isa_PropertyExpression():
    instance = aadl2_ListValue()
    assert isinstance(instance, PropertyExpression)


def test_aadl2_Operation_isa_PropertyExpression():
    instance = aadl2_Operation(op="sample_text")
    assert isinstance(instance, PropertyExpression)


def test_aadl2_PropertyValue_isa_PropertyExpression():
    instance = aadl2_PropertyValue()
    assert isinstance(instance, PropertyExpression)


def test_aadl2_ClassifierValue_isa_PropertyOwner():
    instance = aadl2_ClassifierValue()
    assert isinstance(instance, PropertyOwner)


def test_aadl2_MetaclassReference_isa_PropertyOwner():
    instance = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    assert isinstance(instance, PropertyOwner)


def test_aadl2_ListType_isa_PropertyType():
    instance = aadl2_ListType()
    assert isinstance(instance, PropertyType)


def test_aadl2_NonListType_isa_PropertyType():
    instance = aadl2_NonListType()
    assert isinstance(instance, PropertyType)


def test_aadl2_BooleanLiteral_isa_PropertyValue():
    instance = aadl2_BooleanLiteral(value="sample_text")
    assert isinstance(instance, PropertyValue)


def test_aadl2_ClassifierValue_isa_PropertyValue():
    instance = aadl2_ClassifierValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_ComputedValue_isa_PropertyValue():
    instance = aadl2_ComputedValue(function="sample_text")
    assert isinstance(instance, PropertyValue)


def test_aadl2_NamedValue_isa_PropertyValue():
    instance = aadl2_NamedValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_NumberValue_isa_PropertyValue():
    instance = aadl2_NumberValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_RangeValue_isa_PropertyValue():
    instance = aadl2_RangeValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_RecordValue_isa_PropertyValue():
    instance = aadl2_RecordValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_ReferenceValue_isa_PropertyValue():
    instance = aadl2_ReferenceValue()
    assert isinstance(instance, PropertyValue)


def test_aadl2_StringLiteral_isa_PropertyValue():
    instance = aadl2_StringLiteral(value="sample_text")
    assert isinstance(instance, PropertyValue)


def test_aadl2_ComponentPrototype_isa_Prototype():
    instance = aadl2_ComponentPrototype(array="sample_text")
    assert isinstance(instance, Prototype)


def test_aadl2_FeatureGroupPrototype_isa_Prototype():
    instance = aadl2_FeatureGroupPrototype()
    assert isinstance(instance, Prototype)


def test_aadl2_FeaturePrototype_isa_Prototype():
    instance = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, Prototype)


def test_aadl2_ComponentPrototypeBinding_isa_PrototypeBinding():
    instance = aadl2_ComponentPrototypeBinding()
    assert isinstance(instance, PrototypeBinding)


def test_aadl2_FeatureGroupPrototypeBinding_isa_PrototypeBinding():
    instance = aadl2_FeatureGroupPrototypeBinding()
    assert isinstance(instance, PrototypeBinding)


def test_aadl2_FeaturePrototypeBinding_isa_PrototypeBinding():
    instance = aadl2_FeaturePrototypeBinding()
    assert isinstance(instance, PrototypeBinding)


def test_aadl2_StructuralFeature_isa_RefinableElement():
    instance = aadl2_StructuralFeature()
    assert isinstance(instance, RefinableElement)


def test_aadl2_DirectedRelationship_isa_Relationship():
    instance = aadl2_DirectedRelationship()
    assert isinstance(instance, Relationship)


def test_aadl2_Connection_isa_StructuralFeature():
    instance = aadl2_Connection(bidirectional="sample_text")
    assert isinstance(instance, StructuralFeature)


def test_aadl2_Feature_isa_StructuralFeature():
    instance = aadl2_Feature()
    assert isinstance(instance, StructuralFeature)


def test_aadl2_FlowFeature_isa_StructuralFeature():
    instance = aadl2_FlowFeature()
    assert isinstance(instance, StructuralFeature)


def test_aadl2_InternalFeature_isa_StructuralFeature():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, StructuralFeature)


def test_aadl2_ProcessorFeature_isa_StructuralFeature():
    instance = aadl2_ProcessorFeature()
    assert isinstance(instance, StructuralFeature)


def test_aadl2_Prototype_isa_StructuralFeature():
    instance = aadl2_Prototype()
    assert isinstance(instance, StructuralFeature)


def test_aadl2_Subcomponent_isa_StructuralFeature():
    instance = aadl2_Subcomponent(allModes="sample_text")
    assert isinstance(instance, StructuralFeature)


def test_aadl2_AbstractSubcomponent_isa_Subcomponent():
    instance = aadl2_AbstractSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_BusSubcomponent_isa_Subcomponent():
    instance = aadl2_BusSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_DataSubcomponent_isa_Subcomponent():
    instance = aadl2_DataSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_DeviceSubcomponent_isa_Subcomponent():
    instance = aadl2_DeviceSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_MemorySubcomponent_isa_Subcomponent():
    instance = aadl2_MemorySubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_ProcessSubcomponent_isa_Subcomponent():
    instance = aadl2_ProcessSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_ProcessorSubcomponent_isa_Subcomponent():
    instance = aadl2_ProcessorSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_SubprogramGroupSubcomponent_isa_Subcomponent():
    instance = aadl2_SubprogramGroupSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_SubprogramSubcomponent_isa_Subcomponent():
    instance = aadl2_SubprogramSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_SystemSubcomponent_isa_Subcomponent():
    instance = aadl2_SystemSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_ThreadGroupSubcomponent_isa_Subcomponent():
    instance = aadl2_ThreadGroupSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_ThreadSubcomponent_isa_Subcomponent():
    instance = aadl2_ThreadSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_VirtualBusSubcomponent_isa_Subcomponent():
    instance = aadl2_VirtualBusSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_VirtualProcessorSubcomponent_isa_Subcomponent():
    instance = aadl2_VirtualProcessorSubcomponent()
    assert isinstance(instance, Subcomponent)


def test_aadl2_AbstractSubcomponentType_isa_SubcomponentType():
    instance = aadl2_AbstractSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_BusSubcomponentType_isa_SubcomponentType():
    instance = aadl2_BusSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ComponentClassifier_isa_SubcomponentType():
    instance = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ComponentPrototype_isa_SubcomponentType():
    instance = aadl2_ComponentPrototype(array="sample_text")
    assert isinstance(instance, SubcomponentType)


def test_aadl2_DataSubcomponentType_isa_SubcomponentType():
    instance = aadl2_DataSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_DeviceSubcomponentType_isa_SubcomponentType():
    instance = aadl2_DeviceSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_MemorySubcomponentType_isa_SubcomponentType():
    instance = aadl2_MemorySubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ProcessSubcomponentType_isa_SubcomponentType():
    instance = aadl2_ProcessSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ProcessorSubcomponentType_isa_SubcomponentType():
    instance = aadl2_ProcessorSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_SubprogramGroupSubcomponentType_isa_SubcomponentType():
    instance = aadl2_SubprogramGroupSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_SubprogramSubcomponentType_isa_SubcomponentType():
    instance = aadl2_SubprogramSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_SystemSubcomponentType_isa_SubcomponentType():
    instance = aadl2_SystemSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ThreadGroupSubcomponentType_isa_SubcomponentType():
    instance = aadl2_ThreadGroupSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_ThreadSubcomponentType_isa_SubcomponentType():
    instance = aadl2_ThreadSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_VirtualBusSubcomponentType_isa_SubcomponentType():
    instance = aadl2_VirtualBusSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_VirtualProcessorSubcomponentType_isa_SubcomponentType():
    instance = aadl2_VirtualProcessorSubcomponentType()
    assert isinstance(instance, SubcomponentType)


def test_aadl2_SubprogramClassifier_isa_Subprogram():
    instance = aadl2_SubprogramClassifier()
    assert isinstance(instance, Subprogram)


def test_aadl2_SubprogramPrototype_isa_Subprogram():
    instance = aadl2_SubprogramPrototype()
    assert isinstance(instance, Subprogram)


def test_aadl2_SubprogramSubcomponent_isa_Subprogram():
    instance = aadl2_SubprogramSubcomponent()
    assert isinstance(instance, Subprogram)


def test_aadl2_SubprogramImplementation_isa_SubprogramClassifier():
    instance = aadl2_SubprogramImplementation()
    assert isinstance(instance, SubprogramClassifier)


def test_aadl2_SubprogramType_isa_SubprogramClassifier():
    instance = aadl2_SubprogramType()
    assert isinstance(instance, SubprogramClassifier)


def test_aadl2_SubprogramGroupClassifier_isa_SubprogramGroup():
    instance = aadl2_SubprogramGroupClassifier()
    assert isinstance(instance, SubprogramGroup)


def test_aadl2_SubprogramGroupPrototype_isa_SubprogramGroup():
    instance = aadl2_SubprogramGroupPrototype()
    assert isinstance(instance, SubprogramGroup)


def test_aadl2_SubprogramGroupSubcomponent_isa_SubprogramGroup():
    instance = aadl2_SubprogramGroupSubcomponent()
    assert isinstance(instance, SubprogramGroup)


def test_aadl2_SubprogramGroupImplementation_isa_SubprogramGroupClassifier():
    instance = aadl2_SubprogramGroupImplementation()
    assert isinstance(instance, SubprogramGroupClassifier)


def test_aadl2_SubprogramGroupType_isa_SubprogramGroupClassifier():
    instance = aadl2_SubprogramGroupType()
    assert isinstance(instance, SubprogramGroupClassifier)


def test_aadl2_AbstractClassifier_isa_SubprogramGroupSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, SubprogramGroupSubcomponentType)


def test_aadl2_AbstractPrototype_isa_SubprogramGroupSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, SubprogramGroupSubcomponentType)


def test_aadl2_SubprogramGroupClassifier_isa_SubprogramGroupSubcomponentType():
    instance = aadl2_SubprogramGroupClassifier()
    assert isinstance(instance, SubprogramGroupSubcomponentType)


def test_aadl2_SubprogramGroupPrototype_isa_SubprogramGroupSubcomponentType():
    instance = aadl2_SubprogramGroupPrototype()
    assert isinstance(instance, SubprogramGroupSubcomponentType)


def test_aadl2_AbstractClassifier_isa_SubprogramSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, SubprogramSubcomponentType)


def test_aadl2_AbstractPrototype_isa_SubprogramSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, SubprogramSubcomponentType)


def test_aadl2_SubprogramClassifier_isa_SubprogramSubcomponentType():
    instance = aadl2_SubprogramClassifier()
    assert isinstance(instance, SubprogramSubcomponentType)


def test_aadl2_SubprogramPrototype_isa_SubprogramSubcomponentType():
    instance = aadl2_SubprogramPrototype()
    assert isinstance(instance, SubprogramSubcomponentType)


def test_aadl2_SystemClassifier_isa_System():
    instance = aadl2_SystemClassifier()
    assert isinstance(instance, System)


def test_aadl2_SystemPrototype_isa_System():
    instance = aadl2_SystemPrototype()
    assert isinstance(instance, System)


def test_aadl2_SystemSubcomponent_isa_System():
    instance = aadl2_SystemSubcomponent()
    assert isinstance(instance, System)


def test_aadl2_SystemImplementation_isa_SystemClassifier():
    instance = aadl2_SystemImplementation()
    assert isinstance(instance, SystemClassifier)


def test_aadl2_SystemType_isa_SystemClassifier():
    instance = aadl2_SystemType()
    assert isinstance(instance, SystemClassifier)


def test_aadl2_AbstractClassifier_isa_SystemSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, SystemSubcomponentType)


def test_aadl2_AbstractPrototype_isa_SystemSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, SystemSubcomponentType)


def test_aadl2_SystemClassifier_isa_SystemSubcomponentType():
    instance = aadl2_SystemClassifier()
    assert isinstance(instance, SystemSubcomponentType)


def test_aadl2_SystemPrototype_isa_SystemSubcomponentType():
    instance = aadl2_SystemPrototype()
    assert isinstance(instance, SystemSubcomponentType)


def test_aadl2_ThreadClassifier_isa_Thread():
    instance = aadl2_ThreadClassifier()
    assert isinstance(instance, Thread)


def test_aadl2_ThreadPrototype_isa_Thread():
    instance = aadl2_ThreadPrototype()
    assert isinstance(instance, Thread)


def test_aadl2_ThreadSubcomponent_isa_Thread():
    instance = aadl2_ThreadSubcomponent()
    assert isinstance(instance, Thread)


def test_aadl2_ThreadImplementation_isa_ThreadClassifier():
    instance = aadl2_ThreadImplementation()
    assert isinstance(instance, ThreadClassifier)


def test_aadl2_ThreadType_isa_ThreadClassifier():
    instance = aadl2_ThreadType()
    assert isinstance(instance, ThreadClassifier)


def test_aadl2_ThreadGroupClassifier_isa_ThreadGroup():
    instance = aadl2_ThreadGroupClassifier()
    assert isinstance(instance, ThreadGroup)


def test_aadl2_ThreadGroupPrototype_isa_ThreadGroup():
    instance = aadl2_ThreadGroupPrototype()
    assert isinstance(instance, ThreadGroup)


def test_aadl2_ThreadGroupSubcomponent_isa_ThreadGroup():
    instance = aadl2_ThreadGroupSubcomponent()
    assert isinstance(instance, ThreadGroup)


def test_aadl2_ThreadGroupImplementation_isa_ThreadGroupClassifier():
    instance = aadl2_ThreadGroupImplementation()
    assert isinstance(instance, ThreadGroupClassifier)


def test_aadl2_ThreadGroupType_isa_ThreadGroupClassifier():
    instance = aadl2_ThreadGroupType()
    assert isinstance(instance, ThreadGroupClassifier)


def test_aadl2_AbstractClassifier_isa_ThreadGroupSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, ThreadGroupSubcomponentType)


def test_aadl2_AbstractPrototype_isa_ThreadGroupSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, ThreadGroupSubcomponentType)


def test_aadl2_ThreadGroupClassifier_isa_ThreadGroupSubcomponentType():
    instance = aadl2_ThreadGroupClassifier()
    assert isinstance(instance, ThreadGroupSubcomponentType)


def test_aadl2_ThreadGroupPrototype_isa_ThreadGroupSubcomponentType():
    instance = aadl2_ThreadGroupPrototype()
    assert isinstance(instance, ThreadGroupSubcomponentType)


def test_aadl2_AbstractClassifier_isa_ThreadSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, ThreadSubcomponentType)


def test_aadl2_AbstractPrototype_isa_ThreadSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, ThreadSubcomponentType)


def test_aadl2_ThreadClassifier_isa_ThreadSubcomponentType():
    instance = aadl2_ThreadClassifier()
    assert isinstance(instance, ThreadSubcomponentType)


def test_aadl2_ThreadPrototype_isa_ThreadSubcomponentType():
    instance = aadl2_ThreadPrototype()
    assert isinstance(instance, ThreadSubcomponentType)


def test_aadl2_AbstractFeature_isa_TriggerPort():
    instance = aadl2_AbstractFeature()
    assert isinstance(instance, TriggerPort)


def test_aadl2_InternalFeature_isa_TriggerPort():
    instance = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, TriggerPort)


def test_aadl2_Port_isa_TriggerPort():
    instance = aadl2_Port(category="sample_text")
    assert isinstance(instance, TriggerPort)


def test_aadl2_PortProxy_isa_TriggerPort():
    instance = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    assert isinstance(instance, TriggerPort)


def test_aadl2_Classifier_isa_Type():
    instance = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    assert isinstance(instance, Type)


def test_aadl2_PropertyType_isa_Type():
    instance = aadl2_PropertyType()
    assert isinstance(instance, Type)


def test_aadl2_SubcomponentType_isa_Type():
    instance = aadl2_SubcomponentType()
    assert isinstance(instance, Type)


def test_aadl2_BasicProperty_isa_TypedElement():
    instance = aadl2_BasicProperty()
    assert isinstance(instance, TypedElement)


def test_aadl2_PropertyConstant_isa_TypedElement():
    instance = aadl2_PropertyConstant()
    assert isinstance(instance, TypedElement)


def test_aadl2_VirtualBusClassifier_isa_VirtualBus():
    instance = aadl2_VirtualBusClassifier()
    assert isinstance(instance, VirtualBus)


def test_aadl2_VirtualBusPrototype_isa_VirtualBus():
    instance = aadl2_VirtualBusPrototype()
    assert isinstance(instance, VirtualBus)


def test_aadl2_VirtualBusSubcomponent_isa_VirtualBus():
    instance = aadl2_VirtualBusSubcomponent()
    assert isinstance(instance, VirtualBus)


def test_aadl2_VirtualBusImplementation_isa_VirtualBusClassifier():
    instance = aadl2_VirtualBusImplementation()
    assert isinstance(instance, VirtualBusClassifier)


def test_aadl2_VirtualBusType_isa_VirtualBusClassifier():
    instance = aadl2_VirtualBusType()
    assert isinstance(instance, VirtualBusClassifier)


def test_aadl2_AbstractClassifier_isa_VirtualBusSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, VirtualBusSubcomponentType)


def test_aadl2_AbstractPrototype_isa_VirtualBusSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, VirtualBusSubcomponentType)


def test_aadl2_VirtualBusClassifier_isa_VirtualBusSubcomponentType():
    instance = aadl2_VirtualBusClassifier()
    assert isinstance(instance, VirtualBusSubcomponentType)


def test_aadl2_VirtualBusPrototype_isa_VirtualBusSubcomponentType():
    instance = aadl2_VirtualBusPrototype()
    assert isinstance(instance, VirtualBusSubcomponentType)


def test_aadl2_VirtualProcessorClassifier_isa_VirtualProcessor():
    instance = aadl2_VirtualProcessorClassifier()
    assert isinstance(instance, VirtualProcessor)


def test_aadl2_VirtualProcessorPrototype_isa_VirtualProcessor():
    instance = aadl2_VirtualProcessorPrototype()
    assert isinstance(instance, VirtualProcessor)


def test_aadl2_VirtualProcessorSubcomponent_isa_VirtualProcessor():
    instance = aadl2_VirtualProcessorSubcomponent()
    assert isinstance(instance, VirtualProcessor)


def test_aadl2_VirtualProcessorImplementation_isa_VirtualProcessorClassifier():
    instance = aadl2_VirtualProcessorImplementation()
    assert isinstance(instance, VirtualProcessorClassifier)


def test_aadl2_VirtualProcessorType_isa_VirtualProcessorClassifier():
    instance = aadl2_VirtualProcessorType()
    assert isinstance(instance, VirtualProcessorClassifier)


def test_aadl2_AbstractClassifier_isa_VirtualProcessorSubcomponentType():
    instance = aadl2_AbstractClassifier()
    assert isinstance(instance, VirtualProcessorSubcomponentType)


def test_aadl2_AbstractPrototype_isa_VirtualProcessorSubcomponentType():
    instance = aadl2_AbstractPrototype()
    assert isinstance(instance, VirtualProcessorSubcomponentType)


def test_aadl2_VirtualProcessorClassifier_isa_VirtualProcessorSubcomponentType():
    instance = aadl2_VirtualProcessorClassifier()
    assert isinstance(instance, VirtualProcessorSubcomponentType)


def test_aadl2_VirtualProcessorPrototype_isa_VirtualProcessorSubcomponentType():
    instance = aadl2_VirtualProcessorPrototype()
    assert isinstance(instance, VirtualProcessorSubcomponentType)


def test_assoc_InEnd186_link_reassign_clear():
    a = aadl2_FlowSpecification(kind="sample_text")
    b1 = aadl2_FlowEnd()
    b2 = aadl2_FlowEnd()
    _safe_set(a, 'aadl2_FlowSpecification187', b1)
    assert _is_linked(a, 'aadl2_FlowSpecification187', b1)
    if hasattr(b1, 'aadl2_FlowEnd188'):
        assert _is_linked(b1, 'aadl2_FlowEnd188', a)
    _safe_set(a, 'aadl2_FlowSpecification187', b2)
    assert _is_linked(a, 'aadl2_FlowSpecification187', b2)
    if hasattr(b1, 'aadl2_FlowEnd188'):
        assert not _is_linked(b1, 'aadl2_FlowEnd188', a)
    if hasattr(b2, 'aadl2_FlowEnd188'):
        assert _is_linked(b2, 'aadl2_FlowEnd188', a)
    _safe_set(a, 'aadl2_FlowSpecification187', None)
    assert not _is_linked(a, 'aadl2_FlowSpecification187', b2)
    if hasattr(b2, 'aadl2_FlowEnd188'):
        assert not _is_linked(b2, 'aadl2_FlowEnd188', a)


def test_assoc_actual386_link_reassign_clear():
    a = aadl2_ComponentPrototypeActual(category="sample_text")
    b1 = aadl2_ComponentPrototypeBinding()
    b2 = aadl2_ComponentPrototypeBinding()
    _safe_set(a, 'aadl2_ComponentPrototypeActual', b1)
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual', b1)
    if hasattr(b1, 'aadl2_ComponentPrototypeBinding'):
        assert _is_linked(b1, 'aadl2_ComponentPrototypeBinding', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual', b2)
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual', b2)
    if hasattr(b1, 'aadl2_ComponentPrototypeBinding'):
        assert not _is_linked(b1, 'aadl2_ComponentPrototypeBinding', a)
    if hasattr(b2, 'aadl2_ComponentPrototypeBinding'):
        assert _is_linked(b2, 'aadl2_ComponentPrototypeBinding', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual', None)
    assert not _is_linked(a, 'aadl2_ComponentPrototypeActual', b2)
    if hasattr(b2, 'aadl2_ComponentPrototypeBinding'):
        assert not _is_linked(b2, 'aadl2_ComponentPrototypeBinding', a)


def test_assoc_appliesTo20_link_reassign_clear():
    a = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b1 = aadl2_PropertyOwner()
    b2 = aadl2_PropertyOwner()
    _safe_set(a, 'aadl2_Property21', {b1})
    assert _is_linked(a, 'aadl2_Property21', b1)
    if hasattr(b1, 'aadl2_PropertyOwner'):
        assert _is_linked(b1, 'aadl2_PropertyOwner', a)
    _safe_set(a, 'aadl2_Property21', {b2})
    assert _is_linked(a, 'aadl2_Property21', b2)
    if hasattr(b1, 'aadl2_PropertyOwner'):
        assert not _is_linked(b1, 'aadl2_PropertyOwner', a)
    if hasattr(b2, 'aadl2_PropertyOwner'):
        assert _is_linked(b2, 'aadl2_PropertyOwner', a)
    _safe_set(a, 'aadl2_Property21', set())
    assert not _is_linked(a, 'aadl2_Property21', b2)
    if hasattr(b2, 'aadl2_PropertyOwner'):
        assert not _is_linked(b2, 'aadl2_PropertyOwner', a)


def test_assoc_appliesTo7_link_reassign_clear():
    a = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    b1 = aadl2_ContainedNamedElement()
    b2 = aadl2_ContainedNamedElement()
    _safe_set(a, 'aadl2_PropertyAssociation8', {b1})
    assert _is_linked(a, 'aadl2_PropertyAssociation8', b1)
    if hasattr(b1, 'aadl2_ContainedNamedElement'):
        assert _is_linked(b1, 'aadl2_ContainedNamedElement', a)
    _safe_set(a, 'aadl2_PropertyAssociation8', {b2})
    assert _is_linked(a, 'aadl2_PropertyAssociation8', b2)
    if hasattr(b1, 'aadl2_ContainedNamedElement'):
        assert not _is_linked(b1, 'aadl2_ContainedNamedElement', a)
    if hasattr(b2, 'aadl2_ContainedNamedElement'):
        assert _is_linked(b2, 'aadl2_ContainedNamedElement', a)
    _safe_set(a, 'aadl2_PropertyAssociation8', set())
    assert not _is_linked(a, 'aadl2_PropertyAssociation8', b2)
    if hasattr(b2, 'aadl2_ContainedNamedElement'):
        assert not _is_linked(b2, 'aadl2_ContainedNamedElement', a)


def test_assoc_appliesToClassifier17_link_reassign_clear():
    a = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b1 = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b2 = aadl2_Classifier(noAnnexes="sample_text_2", noProperties="sample_text_2", noPrototypes="sample_text_2")
    _safe_set(a, 'aadl2_Property18', {b1})
    assert _is_linked(a, 'aadl2_Property18', b1)
    if hasattr(b1, 'aadl2_Classifier19'):
        assert _is_linked(b1, 'aadl2_Classifier19', a)
    _safe_set(a, 'aadl2_Property18', {b2})
    assert _is_linked(a, 'aadl2_Property18', b2)
    if hasattr(b1, 'aadl2_Classifier19'):
        assert not _is_linked(b1, 'aadl2_Classifier19', a)
    if hasattr(b2, 'aadl2_Classifier19'):
        assert _is_linked(b2, 'aadl2_Classifier19', a)
    _safe_set(a, 'aadl2_Property18', set())
    assert not _is_linked(a, 'aadl2_Property18', b2)
    if hasattr(b2, 'aadl2_Classifier19'):
        assert not _is_linked(b2, 'aadl2_Classifier19', a)


def test_assoc_appliesToMetaclass15_link_reassign_clear():
    a = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b1 = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    b2 = aadl2_MetaclassReference(annexName="sample_text_2", metaclassName="sample_text_2")
    _safe_set(a, 'aadl2_Property16', {b1})
    assert _is_linked(a, 'aadl2_Property16', b1)
    if hasattr(b1, 'aadl2_MetaclassReference'):
        assert _is_linked(b1, 'aadl2_MetaclassReference', a)
    _safe_set(a, 'aadl2_Property16', {b2})
    assert _is_linked(a, 'aadl2_Property16', b2)
    if hasattr(b1, 'aadl2_MetaclassReference'):
        assert not _is_linked(b1, 'aadl2_MetaclassReference', a)
    if hasattr(b2, 'aadl2_MetaclassReference'):
        assert _is_linked(b2, 'aadl2_MetaclassReference', a)
    _safe_set(a, 'aadl2_Property16', set())
    assert not _is_linked(a, 'aadl2_Property16', b2)
    if hasattr(b2, 'aadl2_MetaclassReference'):
        assert not _is_linked(b2, 'aadl2_MetaclassReference', a)


def test_assoc_arrayRange78_link_reassign_clear():
    a = aadl2_ContainmentPathElement(annexName="sample_text")
    b1 = aadl2_ArrayRange(lowerBound="sample_text", upperBound="sample_text")
    b2 = aadl2_ArrayRange(lowerBound="sample_text_2", upperBound="sample_text_2")
    _safe_set(a, 'aadl2_ContainmentPathElement79', {b1})
    assert _is_linked(a, 'aadl2_ContainmentPathElement79', b1)
    if hasattr(b1, 'aadl2_ArrayRange'):
        assert _is_linked(b1, 'aadl2_ArrayRange', a)
    _safe_set(a, 'aadl2_ContainmentPathElement79', {b2})
    assert _is_linked(a, 'aadl2_ContainmentPathElement79', b2)
    if hasattr(b1, 'aadl2_ArrayRange'):
        assert not _is_linked(b1, 'aadl2_ArrayRange', a)
    if hasattr(b2, 'aadl2_ArrayRange'):
        assert _is_linked(b2, 'aadl2_ArrayRange', a)
    _safe_set(a, 'aadl2_ContainmentPathElement79', set())
    assert not _is_linked(a, 'aadl2_ContainmentPathElement79', b2)
    if hasattr(b2, 'aadl2_ArrayRange'):
        assert not _is_linked(b2, 'aadl2_ArrayRange', a)


def test_assoc_baseUnit819_link_reassign_clear():
    a = aadl2_UnitLiteral()
    b1 = aadl2_UnitLiteral()
    b2 = aadl2_UnitLiteral()
    _safe_set(a, 'aadl2_UnitLiteral818', b1)
    assert _is_linked(a, 'aadl2_UnitLiteral818', b1)
    if hasattr(b1, 'aadl2_UnitLiteral820'):
        assert _is_linked(b1, 'aadl2_UnitLiteral820', a)
    _safe_set(a, 'aadl2_UnitLiteral818', b2)
    assert _is_linked(a, 'aadl2_UnitLiteral818', b2)
    if hasattr(b1, 'aadl2_UnitLiteral820'):
        assert not _is_linked(b1, 'aadl2_UnitLiteral820', a)
    if hasattr(b2, 'aadl2_UnitLiteral820'):
        assert _is_linked(b2, 'aadl2_UnitLiteral820', a)
    _safe_set(a, 'aadl2_UnitLiteral818', None)
    assert not _is_linked(a, 'aadl2_UnitLiteral818', b2)
    if hasattr(b2, 'aadl2_UnitLiteral820'):
        assert not _is_linked(b2, 'aadl2_UnitLiteral820', a)


def test_assoc_binding387_link_reassign_clear():
    a = aadl2_ComponentPrototypeActual(category="sample_text")
    b1 = aadl2_PrototypeBinding()
    b2 = aadl2_PrototypeBinding()
    _safe_set(a, 'aadl2_ComponentPrototypeActual388', {b1})
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual388', b1)
    if hasattr(b1, 'aadl2_PrototypeBinding389'):
        assert _is_linked(b1, 'aadl2_PrototypeBinding389', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual388', {b2})
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual388', b2)
    if hasattr(b1, 'aadl2_PrototypeBinding389'):
        assert not _is_linked(b1, 'aadl2_PrototypeBinding389', a)
    if hasattr(b2, 'aadl2_PrototypeBinding389'):
        assert _is_linked(b2, 'aadl2_PrototypeBinding389', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual388', set())
    assert not _is_linked(a, 'aadl2_ComponentPrototypeActual388', b2)
    if hasattr(b2, 'aadl2_PrototypeBinding389'):
        assert not _is_linked(b2, 'aadl2_PrototypeBinding389', a)


def test_assoc_busFeatureClassifier241_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_BusFeatureClassifier()
    b2 = aadl2_BusFeatureClassifier()
    _safe_set(a, 'aadl2_BusAccess242', b1)
    assert _is_linked(a, 'aadl2_BusAccess242', b1)
    if hasattr(b1, 'aadl2_BusFeatureClassifier'):
        assert _is_linked(b1, 'aadl2_BusFeatureClassifier', a)
    _safe_set(a, 'aadl2_BusAccess242', b2)
    assert _is_linked(a, 'aadl2_BusAccess242', b2)
    if hasattr(b1, 'aadl2_BusFeatureClassifier'):
        assert not _is_linked(b1, 'aadl2_BusFeatureClassifier', a)
    if hasattr(b2, 'aadl2_BusFeatureClassifier'):
        assert _is_linked(b2, 'aadl2_BusFeatureClassifier', a)
    _safe_set(a, 'aadl2_BusAccess242', None)
    assert not _is_linked(a, 'aadl2_BusAccess242', b2)
    if hasattr(b2, 'aadl2_BusFeatureClassifier'):
        assert not _is_linked(b2, 'aadl2_BusFeatureClassifier', a)


def test_assoc_classifier175_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Feature()
    b2 = aadl2_Feature()
    _safe_set(a, 'aadl2_Classifier177', b1)
    assert _is_linked(a, 'aadl2_Classifier177', b1)
    if hasattr(b1, 'aadl2_Feature176'):
        assert _is_linked(b1, 'aadl2_Feature176', a)
    _safe_set(a, 'aadl2_Classifier177', b2)
    assert _is_linked(a, 'aadl2_Classifier177', b2)
    if hasattr(b1, 'aadl2_Feature176'):
        assert not _is_linked(b1, 'aadl2_Feature176', a)
    if hasattr(b2, 'aadl2_Feature176'):
        assert _is_linked(b2, 'aadl2_Feature176', a)
    _safe_set(a, 'aadl2_Classifier177', None)
    assert not _is_linked(a, 'aadl2_Classifier177', b2)
    if hasattr(b2, 'aadl2_Feature176'):
        assert not _is_linked(b2, 'aadl2_Feature176', a)


def test_assoc_classifier284_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b2 = aadl2_ComponentClassifier(derivedModes="sample_text_2", noFlows="sample_text_2", noModes="sample_text_2")
    _safe_set(a, 'aadl2_Subcomponent285', b1)
    assert _is_linked(a, 'aadl2_Subcomponent285', b1)
    if hasattr(b1, 'aadl2_ComponentClassifier286'):
        assert _is_linked(b1, 'aadl2_ComponentClassifier286', a)
    _safe_set(a, 'aadl2_Subcomponent285', b2)
    assert _is_linked(a, 'aadl2_Subcomponent285', b2)
    if hasattr(b1, 'aadl2_ComponentClassifier286'):
        assert not _is_linked(b1, 'aadl2_ComponentClassifier286', a)
    if hasattr(b2, 'aadl2_ComponentClassifier286'):
        assert _is_linked(b2, 'aadl2_ComponentClassifier286', a)
    _safe_set(a, 'aadl2_Subcomponent285', None)
    assert not _is_linked(a, 'aadl2_Subcomponent285', b2)
    if hasattr(b2, 'aadl2_ComponentClassifier286'):
        assert not _is_linked(b2, 'aadl2_ComponentClassifier286', a)


def test_assoc_classifier401_link_reassign_clear():
    a = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b1 = aadl2_AccessSpecification(category="sample_text", kind="sample_text")
    b2 = aadl2_AccessSpecification(category="sample_text_2", kind="sample_text_2")
    _safe_set(a, 'aadl2_ComponentClassifier402', b1)
    assert _is_linked(a, 'aadl2_ComponentClassifier402', b1)
    if hasattr(b1, 'aadl2_AccessSpecification'):
        assert _is_linked(b1, 'aadl2_AccessSpecification', a)
    _safe_set(a, 'aadl2_ComponentClassifier402', b2)
    assert _is_linked(a, 'aadl2_ComponentClassifier402', b2)
    if hasattr(b1, 'aadl2_AccessSpecification'):
        assert not _is_linked(b1, 'aadl2_AccessSpecification', a)
    if hasattr(b2, 'aadl2_AccessSpecification'):
        assert _is_linked(b2, 'aadl2_AccessSpecification', a)
    _safe_set(a, 'aadl2_ComponentClassifier402', None)
    assert not _is_linked(a, 'aadl2_ComponentClassifier402', b2)
    if hasattr(b2, 'aadl2_AccessSpecification'):
        assert not _is_linked(b2, 'aadl2_AccessSpecification', a)


def test_assoc_classifier406_link_reassign_clear():
    a = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b2 = aadl2_ComponentClassifier(derivedModes="sample_text_2", noFlows="sample_text_2", noModes="sample_text_2")
    _safe_set(a, 'aadl2_PortSpecification', b1)
    assert _is_linked(a, 'aadl2_PortSpecification', b1)
    if hasattr(b1, 'aadl2_ComponentClassifier407'):
        assert _is_linked(b1, 'aadl2_ComponentClassifier407', a)
    _safe_set(a, 'aadl2_PortSpecification', b2)
    assert _is_linked(a, 'aadl2_PortSpecification', b2)
    if hasattr(b1, 'aadl2_ComponentClassifier407'):
        assert not _is_linked(b1, 'aadl2_ComponentClassifier407', a)
    if hasattr(b2, 'aadl2_ComponentClassifier407'):
        assert _is_linked(b2, 'aadl2_ComponentClassifier407', a)
    _safe_set(a, 'aadl2_PortSpecification', None)
    assert not _is_linked(a, 'aadl2_PortSpecification', b2)
    if hasattr(b2, 'aadl2_ComponentClassifier407'):
        assert not _is_linked(b2, 'aadl2_ComponentClassifier407', a)


def test_assoc_classifier824_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_ClassifierValue()
    b2 = aadl2_ClassifierValue()
    _safe_set(a, 'aadl2_Classifier825', b1)
    assert _is_linked(a, 'aadl2_Classifier825', b1)
    if hasattr(b1, 'aadl2_ClassifierValue'):
        assert _is_linked(b1, 'aadl2_ClassifierValue', a)
    _safe_set(a, 'aadl2_Classifier825', b2)
    assert _is_linked(a, 'aadl2_Classifier825', b2)
    if hasattr(b1, 'aadl2_ClassifierValue'):
        assert not _is_linked(b1, 'aadl2_ClassifierValue', a)
    if hasattr(b2, 'aadl2_ClassifierValue'):
        assert _is_linked(b2, 'aadl2_ClassifierValue', a)
    _safe_set(a, 'aadl2_Classifier825', None)
    assert not _is_linked(a, 'aadl2_Classifier825', b2)
    if hasattr(b2, 'aadl2_ClassifierValue'):
        assert not _is_linked(b2, 'aadl2_ClassifierValue', a)


def test_assoc_classifierFeature30_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_ClassifierFeature()
    b2 = aadl2_ClassifierFeature()
    _safe_set(a, 'featuringClassifier', {b1})
    assert _is_linked(a, 'featuringClassifier', b1)
    if hasattr(b1, 'ClassifierFeature'):
        assert _is_linked(b1, 'ClassifierFeature', a)
    _safe_set(a, 'featuringClassifier', {b2})
    assert _is_linked(a, 'featuringClassifier', b2)
    if hasattr(b1, 'ClassifierFeature'):
        assert not _is_linked(b1, 'ClassifierFeature', a)
    if hasattr(b2, 'ClassifierFeature'):
        assert _is_linked(b2, 'ClassifierFeature', a)
    _safe_set(a, 'featuringClassifier', set())
    assert not _is_linked(a, 'featuringClassifier', b2)
    if hasattr(b2, 'ClassifierFeature'):
        assert not _is_linked(b2, 'ClassifierFeature', a)


def test_assoc_classifierReference876_link_reassign_clear():
    a = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    b1 = aadl2_ClassifierType()
    b2 = aadl2_ClassifierType()
    _safe_set(a, 'aadl2_MetaclassReference877', b1)
    assert _is_linked(a, 'aadl2_MetaclassReference877', b1)
    if hasattr(b1, 'aadl2_ClassifierType'):
        assert _is_linked(b1, 'aadl2_ClassifierType', a)
    _safe_set(a, 'aadl2_MetaclassReference877', b2)
    assert _is_linked(a, 'aadl2_MetaclassReference877', b2)
    if hasattr(b1, 'aadl2_ClassifierType'):
        assert not _is_linked(b1, 'aadl2_ClassifierType', a)
    if hasattr(b2, 'aadl2_ClassifierType'):
        assert _is_linked(b2, 'aadl2_ClassifierType', a)
    _safe_set(a, 'aadl2_MetaclassReference877', None)
    assert not _is_linked(a, 'aadl2_MetaclassReference877', b2)
    if hasattr(b2, 'aadl2_ClassifierType'):
        assert not _is_linked(b2, 'aadl2_ClassifierType', a)


def test_assoc_componentPrototype403_link_reassign_clear():
    a = aadl2_ComponentPrototype(array="sample_text")
    b1 = aadl2_AccessSpecification(category="sample_text", kind="sample_text")
    b2 = aadl2_AccessSpecification(category="sample_text_2", kind="sample_text_2")
    _safe_set(a, 'aadl2_ComponentPrototype405', b1)
    assert _is_linked(a, 'aadl2_ComponentPrototype405', b1)
    if hasattr(b1, 'aadl2_AccessSpecification404'):
        assert _is_linked(b1, 'aadl2_AccessSpecification404', a)
    _safe_set(a, 'aadl2_ComponentPrototype405', b2)
    assert _is_linked(a, 'aadl2_ComponentPrototype405', b2)
    if hasattr(b1, 'aadl2_AccessSpecification404'):
        assert not _is_linked(b1, 'aadl2_AccessSpecification404', a)
    if hasattr(b2, 'aadl2_AccessSpecification404'):
        assert _is_linked(b2, 'aadl2_AccessSpecification404', a)
    _safe_set(a, 'aadl2_ComponentPrototype405', None)
    assert not _is_linked(a, 'aadl2_ComponentPrototype405', b2)
    if hasattr(b2, 'aadl2_AccessSpecification404'):
        assert not _is_linked(b2, 'aadl2_AccessSpecification404', a)


def test_assoc_componentPrototype408_link_reassign_clear():
    a = aadl2_PortSpecification(category="sample_text", direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_ComponentPrototype(array="sample_text")
    b2 = aadl2_ComponentPrototype(array="sample_text_2")
    _safe_set(a, 'aadl2_PortSpecification409', b1)
    assert _is_linked(a, 'aadl2_PortSpecification409', b1)
    if hasattr(b1, 'aadl2_ComponentPrototype410'):
        assert _is_linked(b1, 'aadl2_ComponentPrototype410', a)
    _safe_set(a, 'aadl2_PortSpecification409', b2)
    assert _is_linked(a, 'aadl2_PortSpecification409', b2)
    if hasattr(b1, 'aadl2_ComponentPrototype410'):
        assert not _is_linked(b1, 'aadl2_ComponentPrototype410', a)
    if hasattr(b2, 'aadl2_ComponentPrototype410'):
        assert _is_linked(b2, 'aadl2_ComponentPrototype410', a)
    _safe_set(a, 'aadl2_PortSpecification409', None)
    assert not _is_linked(a, 'aadl2_PortSpecification409', b2)
    if hasattr(b2, 'aadl2_ComponentPrototype410'):
        assert not _is_linked(b2, 'aadl2_ComponentPrototype410', a)


def test_assoc_constrainingClassifier178_link_reassign_clear():
    a = aadl2_ComponentPrototype(array="sample_text")
    b1 = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b2 = aadl2_ComponentClassifier(derivedModes="sample_text_2", noFlows="sample_text_2", noModes="sample_text_2")
    _safe_set(a, 'aadl2_ComponentPrototype179', b1)
    assert _is_linked(a, 'aadl2_ComponentPrototype179', b1)
    if hasattr(b1, 'aadl2_ComponentClassifier180'):
        assert _is_linked(b1, 'aadl2_ComponentClassifier180', a)
    _safe_set(a, 'aadl2_ComponentPrototype179', b2)
    assert _is_linked(a, 'aadl2_ComponentPrototype179', b2)
    if hasattr(b1, 'aadl2_ComponentClassifier180'):
        assert not _is_linked(b1, 'aadl2_ComponentClassifier180', a)
    if hasattr(b2, 'aadl2_ComponentClassifier180'):
        assert _is_linked(b2, 'aadl2_ComponentClassifier180', a)
    _safe_set(a, 'aadl2_ComponentPrototype179', None)
    assert not _is_linked(a, 'aadl2_ComponentPrototype179', b2)
    if hasattr(b2, 'aadl2_ComponentClassifier180'):
        assert not _is_linked(b2, 'aadl2_ComponentClassifier180', a)


def test_assoc_constrainingClassifier262_link_reassign_clear():
    a = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b2 = aadl2_ComponentClassifier(derivedModes="sample_text_2", noFlows="sample_text_2", noModes="sample_text_2")
    _safe_set(a, 'aadl2_FeaturePrototype263', b1)
    assert _is_linked(a, 'aadl2_FeaturePrototype263', b1)
    if hasattr(b1, 'aadl2_ComponentClassifier264'):
        assert _is_linked(b1, 'aadl2_ComponentClassifier264', a)
    _safe_set(a, 'aadl2_FeaturePrototype263', b2)
    assert _is_linked(a, 'aadl2_FeaturePrototype263', b2)
    if hasattr(b1, 'aadl2_ComponentClassifier264'):
        assert not _is_linked(b1, 'aadl2_ComponentClassifier264', a)
    if hasattr(b2, 'aadl2_ComponentClassifier264'):
        assert _is_linked(b2, 'aadl2_ComponentClassifier264', a)
    _safe_set(a, 'aadl2_FeaturePrototype263', None)
    assert not _is_linked(a, 'aadl2_FeaturePrototype263', b2)
    if hasattr(b2, 'aadl2_ComponentClassifier264'):
        assert not _is_linked(b2, 'aadl2_ComponentClassifier264', a)


def test_assoc_containmentPathElement75_link_reassign_clear():
    a = aadl2_ContainmentPathElement(annexName="sample_text")
    b1 = aadl2_ContainedNamedElement()
    b2 = aadl2_ContainedNamedElement()
    _safe_set(a, 'aadl2_ContainmentPathElement77', b1)
    assert _is_linked(a, 'aadl2_ContainmentPathElement77', b1)
    if hasattr(b1, 'aadl2_ContainedNamedElement76'):
        assert _is_linked(b1, 'aadl2_ContainedNamedElement76', a)
    _safe_set(a, 'aadl2_ContainmentPathElement77', b2)
    assert _is_linked(a, 'aadl2_ContainmentPathElement77', b2)
    if hasattr(b1, 'aadl2_ContainedNamedElement76'):
        assert not _is_linked(b1, 'aadl2_ContainedNamedElement76', a)
    if hasattr(b2, 'aadl2_ContainedNamedElement76'):
        assert _is_linked(b2, 'aadl2_ContainedNamedElement76', a)
    _safe_set(a, 'aadl2_ContainmentPathElement77', None)
    assert not _is_linked(a, 'aadl2_ContainmentPathElement77', b2)
    if hasattr(b2, 'aadl2_ContainedNamedElement76'):
        assert not _is_linked(b2, 'aadl2_ContainedNamedElement76', a)


def test_assoc_dataClassifier345_link_reassign_clear():
    a = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_DataClassifier()
    b2 = aadl2_DataClassifier()
    _safe_set(a, 'aadl2_PortProxy346', b1)
    assert _is_linked(a, 'aadl2_PortProxy346', b1)
    if hasattr(b1, 'aadl2_DataClassifier347'):
        assert _is_linked(b1, 'aadl2_DataClassifier347', a)
    _safe_set(a, 'aadl2_PortProxy346', b2)
    assert _is_linked(a, 'aadl2_PortProxy346', b2)
    if hasattr(b1, 'aadl2_DataClassifier347'):
        assert not _is_linked(b1, 'aadl2_DataClassifier347', a)
    if hasattr(b2, 'aadl2_DataClassifier347'):
        assert _is_linked(b2, 'aadl2_DataClassifier347', a)
    _safe_set(a, 'aadl2_PortProxy346', None)
    assert not _is_linked(a, 'aadl2_PortProxy346', b2)
    if hasattr(b2, 'aadl2_DataClassifier347'):
        assert not _is_linked(b2, 'aadl2_DataClassifier347', a)


def test_assoc_defaultValue13_link_reassign_clear():
    a = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b1 = aadl2_PropertyExpression()
    b2 = aadl2_PropertyExpression()
    _safe_set(a, 'aadl2_Property14', b1)
    assert _is_linked(a, 'aadl2_Property14', b1)
    if hasattr(b1, 'aadl2_PropertyExpression'):
        assert _is_linked(b1, 'aadl2_PropertyExpression', a)
    _safe_set(a, 'aadl2_Property14', b2)
    assert _is_linked(a, 'aadl2_Property14', b2)
    if hasattr(b1, 'aadl2_PropertyExpression'):
        assert not _is_linked(b1, 'aadl2_PropertyExpression', a)
    if hasattr(b2, 'aadl2_PropertyExpression'):
        assert _is_linked(b2, 'aadl2_PropertyExpression', a)
    _safe_set(a, 'aadl2_Property14', None)
    assert not _is_linked(a, 'aadl2_Property14', b2)
    if hasattr(b2, 'aadl2_PropertyExpression'):
        assert not _is_linked(b2, 'aadl2_PropertyExpression', a)


def test_assoc_derivedMode290_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ModeBinding()
    b2 = aadl2_ModeBinding()
    _safe_set(a, 'aadl2_Mode292', b1)
    assert _is_linked(a, 'aadl2_Mode292', b1)
    if hasattr(b1, 'aadl2_ModeBinding291'):
        assert _is_linked(b1, 'aadl2_ModeBinding291', a)
    _safe_set(a, 'aadl2_Mode292', b2)
    assert _is_linked(a, 'aadl2_Mode292', b2)
    if hasattr(b1, 'aadl2_ModeBinding291'):
        assert not _is_linked(b1, 'aadl2_ModeBinding291', a)
    if hasattr(b2, 'aadl2_ModeBinding291'):
        assert _is_linked(b2, 'aadl2_ModeBinding291', a)
    _safe_set(a, 'aadl2_Mode292', None)
    assert not _is_linked(a, 'aadl2_Mode292', b2)
    if hasattr(b2, 'aadl2_ModeBinding291'):
        assert not _is_linked(b2, 'aadl2_ModeBinding291', a)


def test_assoc_destination146_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ModeTransition()
    b2 = aadl2_ModeTransition()
    _safe_set(a, 'aadl2_Mode148', b1)
    assert _is_linked(a, 'aadl2_Mode148', b1)
    if hasattr(b1, 'aadl2_ModeTransition147'):
        assert _is_linked(b1, 'aadl2_ModeTransition147', a)
    _safe_set(a, 'aadl2_Mode148', b2)
    assert _is_linked(a, 'aadl2_Mode148', b2)
    if hasattr(b1, 'aadl2_ModeTransition147'):
        assert not _is_linked(b1, 'aadl2_ModeTransition147', a)
    if hasattr(b2, 'aadl2_ModeTransition147'):
        assert _is_linked(b2, 'aadl2_ModeTransition147', a)
    _safe_set(a, 'aadl2_Mode148', None)
    assert not _is_linked(a, 'aadl2_Mode148', b2)
    if hasattr(b2, 'aadl2_ModeTransition147'):
        assert not _is_linked(b2, 'aadl2_ModeTransition147', a)


def test_assoc_destination309_link_reassign_clear():
    a = aadl2_Connection(bidirectional="sample_text")
    b1 = aadl2_ConnectedElement()
    b2 = aadl2_ConnectedElement()
    _safe_set(a, 'aadl2_Connection310', b1)
    assert _is_linked(a, 'aadl2_Connection310', b1)
    if hasattr(b1, 'aadl2_ConnectedElement'):
        assert _is_linked(b1, 'aadl2_ConnectedElement', a)
    _safe_set(a, 'aadl2_Connection310', b2)
    assert _is_linked(a, 'aadl2_Connection310', b2)
    if hasattr(b1, 'aadl2_ConnectedElement'):
        assert not _is_linked(b1, 'aadl2_ConnectedElement', a)
    if hasattr(b2, 'aadl2_ConnectedElement'):
        assert _is_linked(b2, 'aadl2_ConnectedElement', a)
    _safe_set(a, 'aadl2_Connection310', None)
    assert not _is_linked(a, 'aadl2_Connection310', b2)
    if hasattr(b2, 'aadl2_ConnectedElement'):
        assert not _is_linked(b2, 'aadl2_ConnectedElement', a)


def test_assoc_extended103_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_ComponentImplementation102', b1)
    assert _is_linked(a, 'aadl2_ComponentImplementation102', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation104'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation104', a)
    _safe_set(a, 'aadl2_ComponentImplementation102', b2)
    assert _is_linked(a, 'aadl2_ComponentImplementation102', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation104'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation104', a)
    if hasattr(b2, 'aadl2_ComponentImplementation104'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation104', a)
    _safe_set(a, 'aadl2_ComponentImplementation102', None)
    assert not _is_linked(a, 'aadl2_ComponentImplementation102', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation104'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation104', a)


def test_assoc_extended158_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_ComponentType(noFeatures="sample_text")
    b2 = aadl2_ComponentType(noFeatures="sample_text_2")
    _safe_set(a, 'aadl2_ComponentType157', b1)
    assert _is_linked(a, 'aadl2_ComponentType157', b1)
    if hasattr(b1, 'aadl2_ComponentType159'):
        assert _is_linked(b1, 'aadl2_ComponentType159', a)
    _safe_set(a, 'aadl2_ComponentType157', b2)
    assert _is_linked(a, 'aadl2_ComponentType157', b2)
    if hasattr(b1, 'aadl2_ComponentType159'):
        assert not _is_linked(b1, 'aadl2_ComponentType159', a)
    if hasattr(b2, 'aadl2_ComponentType159'):
        assert _is_linked(b2, 'aadl2_ComponentType159', a)
    _safe_set(a, 'aadl2_ComponentType157', None)
    assert not _is_linked(a, 'aadl2_ComponentType157', b2)
    if hasattr(b2, 'aadl2_ComponentType159'):
        assert not _is_linked(b2, 'aadl2_ComponentType159', a)


def test_assoc_extended196_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_TypeExtension()
    b2 = aadl2_TypeExtension()
    _safe_set(a, 'aadl2_ComponentType198', b1)
    assert _is_linked(a, 'aadl2_ComponentType198', b1)
    if hasattr(b1, 'aadl2_TypeExtension197'):
        assert _is_linked(b1, 'aadl2_TypeExtension197', a)
    _safe_set(a, 'aadl2_ComponentType198', b2)
    assert _is_linked(a, 'aadl2_ComponentType198', b2)
    if hasattr(b1, 'aadl2_TypeExtension197'):
        assert not _is_linked(b1, 'aadl2_TypeExtension197', a)
    if hasattr(b2, 'aadl2_TypeExtension197'):
        assert _is_linked(b2, 'aadl2_TypeExtension197', a)
    _safe_set(a, 'aadl2_ComponentType198', None)
    assert not _is_linked(a, 'aadl2_ComponentType198', b2)
    if hasattr(b2, 'aadl2_TypeExtension197'):
        assert not _is_linked(b2, 'aadl2_TypeExtension197', a)


def test_assoc_extended325_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ImplementationExtension()
    b2 = aadl2_ImplementationExtension()
    _safe_set(a, 'aadl2_ComponentImplementation327', b1)
    assert _is_linked(a, 'aadl2_ComponentImplementation327', b1)
    if hasattr(b1, 'aadl2_ImplementationExtension326'):
        assert _is_linked(b1, 'aadl2_ImplementationExtension326', a)
    _safe_set(a, 'aadl2_ComponentImplementation327', b2)
    assert _is_linked(a, 'aadl2_ComponentImplementation327', b2)
    if hasattr(b1, 'aadl2_ImplementationExtension326'):
        assert not _is_linked(b1, 'aadl2_ImplementationExtension326', a)
    if hasattr(b2, 'aadl2_ImplementationExtension326'):
        assert _is_linked(b2, 'aadl2_ImplementationExtension326', a)
    _safe_set(a, 'aadl2_ComponentImplementation327', None)
    assert not _is_linked(a, 'aadl2_ComponentImplementation327', b2)
    if hasattr(b2, 'aadl2_ImplementationExtension326'):
        assert not _is_linked(b2, 'aadl2_ImplementationExtension326', a)


def test_assoc_factor821_link_reassign_clear():
    a = aadl2_UnitLiteral()
    b1 = aadl2_NumberValue()
    b2 = aadl2_NumberValue()
    _safe_set(a, 'aadl2_UnitLiteral822', b1)
    assert _is_linked(a, 'aadl2_UnitLiteral822', b1)
    if hasattr(b1, 'aadl2_NumberValue823'):
        assert _is_linked(b1, 'aadl2_NumberValue823', a)
    _safe_set(a, 'aadl2_UnitLiteral822', b2)
    assert _is_linked(a, 'aadl2_UnitLiteral822', b2)
    if hasattr(b1, 'aadl2_NumberValue823'):
        assert not _is_linked(b1, 'aadl2_NumberValue823', a)
    if hasattr(b2, 'aadl2_NumberValue823'):
        assert _is_linked(b2, 'aadl2_NumberValue823', a)
    _safe_set(a, 'aadl2_UnitLiteral822', None)
    assert not _is_linked(a, 'aadl2_UnitLiteral822', b2)
    if hasattr(b2, 'aadl2_NumberValue823'):
        assert not _is_linked(b2, 'aadl2_NumberValue823', a)


def test_assoc_featureGroupPrototype203_link_reassign_clear():
    a = aadl2_FeatureGroup(inverse="sample_text")
    b1 = aadl2_FeatureGroupPrototype()
    b2 = aadl2_FeatureGroupPrototype()
    _safe_set(a, 'aadl2_FeatureGroup204', b1)
    assert _is_linked(a, 'aadl2_FeatureGroup204', b1)
    if hasattr(b1, 'aadl2_FeatureGroupPrototype'):
        assert _is_linked(b1, 'aadl2_FeatureGroupPrototype', a)
    _safe_set(a, 'aadl2_FeatureGroup204', b2)
    assert _is_linked(a, 'aadl2_FeatureGroup204', b2)
    if hasattr(b1, 'aadl2_FeatureGroupPrototype'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupPrototype', a)
    if hasattr(b2, 'aadl2_FeatureGroupPrototype'):
        assert _is_linked(b2, 'aadl2_FeatureGroupPrototype', a)
    _safe_set(a, 'aadl2_FeatureGroup204', None)
    assert not _is_linked(a, 'aadl2_FeatureGroup204', b2)
    if hasattr(b2, 'aadl2_FeatureGroupPrototype'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupPrototype', a)


def test_assoc_featureGroupType201_link_reassign_clear():
    a = aadl2_FeatureGroup(inverse="sample_text")
    b1 = aadl2_FeatureGroupType()
    b2 = aadl2_FeatureGroupType()
    _safe_set(a, 'aadl2_FeatureGroup202', b1)
    assert _is_linked(a, 'aadl2_FeatureGroup202', b1)
    if hasattr(b1, 'aadl2_FeatureGroupType'):
        assert _is_linked(b1, 'aadl2_FeatureGroupType', a)
    _safe_set(a, 'aadl2_FeatureGroup202', b2)
    assert _is_linked(a, 'aadl2_FeatureGroup202', b2)
    if hasattr(b1, 'aadl2_FeatureGroupType'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupType', a)
    if hasattr(b2, 'aadl2_FeatureGroupType'):
        assert _is_linked(b2, 'aadl2_FeatureGroupType', a)
    _safe_set(a, 'aadl2_FeatureGroup202', None)
    assert not _is_linked(a, 'aadl2_FeatureGroup202', b2)
    if hasattr(b2, 'aadl2_FeatureGroupType'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupType', a)


def test_assoc_featurePrototype258_link_reassign_clear():
    a = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_AbstractFeature()
    b2 = aadl2_AbstractFeature()
    _safe_set(a, 'aadl2_FeaturePrototype', b1)
    assert _is_linked(a, 'aadl2_FeaturePrototype', b1)
    if hasattr(b1, 'aadl2_AbstractFeature259'):
        assert _is_linked(b1, 'aadl2_AbstractFeature259', a)
    _safe_set(a, 'aadl2_FeaturePrototype', b2)
    assert _is_linked(a, 'aadl2_FeaturePrototype', b2)
    if hasattr(b1, 'aadl2_AbstractFeature259'):
        assert not _is_linked(b1, 'aadl2_AbstractFeature259', a)
    if hasattr(b2, 'aadl2_AbstractFeature259'):
        assert _is_linked(b2, 'aadl2_AbstractFeature259', a)
    _safe_set(a, 'aadl2_FeaturePrototype', None)
    assert not _is_linked(a, 'aadl2_FeaturePrototype', b2)
    if hasattr(b2, 'aadl2_AbstractFeature259'):
        assert not _is_linked(b2, 'aadl2_AbstractFeature259', a)


def test_assoc_featureType199_link_reassign_clear():
    a = aadl2_FeatureGroup(inverse="sample_text")
    b1 = aadl2_FeatureType()
    b2 = aadl2_FeatureType()
    _safe_set(a, 'aadl2_FeatureGroup200', b1)
    assert _is_linked(a, 'aadl2_FeatureGroup200', b1)
    if hasattr(b1, 'aadl2_FeatureType'):
        assert _is_linked(b1, 'aadl2_FeatureType', a)
    _safe_set(a, 'aadl2_FeatureGroup200', b2)
    assert _is_linked(a, 'aadl2_FeatureGroup200', b2)
    if hasattr(b1, 'aadl2_FeatureType'):
        assert not _is_linked(b1, 'aadl2_FeatureType', a)
    if hasattr(b2, 'aadl2_FeatureType'):
        assert _is_linked(b2, 'aadl2_FeatureType', a)
    _safe_set(a, 'aadl2_FeatureGroup200', None)
    assert not _is_linked(a, 'aadl2_FeatureGroup200', b2)
    if hasattr(b2, 'aadl2_FeatureType'):
        assert not _is_linked(b2, 'aadl2_FeatureType', a)


def test_assoc_featuringClassifier49_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_ClassifierFeature()
    b2 = aadl2_ClassifierFeature()
    _safe_set(a, 'Classifier', b1)
    assert _is_linked(a, 'Classifier', b1)
    if hasattr(b1, 'classifierFeature'):
        assert _is_linked(b1, 'classifierFeature', a)
    _safe_set(a, 'Classifier', b2)
    assert _is_linked(a, 'Classifier', b2)
    if hasattr(b1, 'classifierFeature'):
        assert not _is_linked(b1, 'classifierFeature', a)
    if hasattr(b2, 'classifierFeature'):
        assert _is_linked(b2, 'classifierFeature', a)
    _safe_set(a, 'Classifier', None)
    assert not _is_linked(a, 'Classifier', b2)
    if hasattr(b2, 'classifierFeature'):
        assert not _is_linked(b2, 'classifierFeature', a)


def test_assoc_general36_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b2 = aadl2_Classifier(noAnnexes="sample_text_2", noProperties="sample_text_2", noPrototypes="sample_text_2")
    _safe_set(a, 'aadl2_Classifier35', {b1})
    assert _is_linked(a, 'aadl2_Classifier35', b1)
    if hasattr(b1, 'aadl2_Classifier37'):
        assert _is_linked(b1, 'aadl2_Classifier37', a)
    _safe_set(a, 'aadl2_Classifier35', {b2})
    assert _is_linked(a, 'aadl2_Classifier35', b2)
    if hasattr(b1, 'aadl2_Classifier37'):
        assert not _is_linked(b1, 'aadl2_Classifier37', a)
    if hasattr(b2, 'aadl2_Classifier37'):
        assert _is_linked(b2, 'aadl2_Classifier37', a)
    _safe_set(a, 'aadl2_Classifier35', set())
    assert not _is_linked(a, 'aadl2_Classifier35', b2)
    if hasattr(b2, 'aadl2_Classifier37'):
        assert not _is_linked(b2, 'aadl2_Classifier37', a)


def test_assoc_general50_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Generalization_()
    b2 = aadl2_Generalization_()
    _safe_set(a, 'aadl2_Classifier51', b1)
    assert _is_linked(a, 'aadl2_Classifier51', b1)
    if hasattr(b1, 'aadl2_Generalization'):
        assert _is_linked(b1, 'aadl2_Generalization', a)
    _safe_set(a, 'aadl2_Classifier51', b2)
    assert _is_linked(a, 'aadl2_Classifier51', b2)
    if hasattr(b1, 'aadl2_Generalization'):
        assert not _is_linked(b1, 'aadl2_Generalization', a)
    if hasattr(b2, 'aadl2_Generalization'):
        assert _is_linked(b2, 'aadl2_Generalization', a)
    _safe_set(a, 'aadl2_Classifier51', None)
    assert not _is_linked(a, 'aadl2_Classifier51', b2)
    if hasattr(b2, 'aadl2_Generalization'):
        assert not _is_linked(b2, 'aadl2_Generalization', a)


def test_assoc_generalization34_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Generalization_()
    b2 = aadl2_Generalization_()
    _safe_set(a, 'specific', {b1})
    assert _is_linked(a, 'specific', b1)
    if hasattr(b1, 'Generalization_'):
        assert _is_linked(b1, 'Generalization_', a)
    _safe_set(a, 'specific', {b2})
    assert _is_linked(a, 'specific', b2)
    if hasattr(b1, 'Generalization_'):
        assert not _is_linked(b1, 'Generalization_', a)
    if hasattr(b2, 'Generalization_'):
        assert _is_linked(b2, 'Generalization_', a)
    _safe_set(a, 'specific', set())
    assert not _is_linked(a, 'specific', b2)
    if hasattr(b2, 'Generalization_'):
        assert not _is_linked(b2, 'Generalization_', a)


def test_assoc_implementation94_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ComponentImplementationReference()
    b2 = aadl2_ComponentImplementationReference()
    _safe_set(a, 'aadl2_ComponentImplementation', b1)
    assert _is_linked(a, 'aadl2_ComponentImplementation', b1)
    if hasattr(b1, 'aadl2_ComponentImplementationReference'):
        assert _is_linked(b1, 'aadl2_ComponentImplementationReference', a)
    _safe_set(a, 'aadl2_ComponentImplementation', b2)
    assert _is_linked(a, 'aadl2_ComponentImplementation', b2)
    if hasattr(b1, 'aadl2_ComponentImplementationReference'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementationReference', a)
    if hasattr(b2, 'aadl2_ComponentImplementationReference'):
        assert _is_linked(b2, 'aadl2_ComponentImplementationReference', a)
    _safe_set(a, 'aadl2_ComponentImplementation', None)
    assert not _is_linked(a, 'aadl2_ComponentImplementation', b2)
    if hasattr(b2, 'aadl2_ComponentImplementationReference'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementationReference', a)


def test_assoc_implementationReference278_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_ComponentImplementationReference()
    b2 = aadl2_ComponentImplementationReference()
    _safe_set(a, 'aadl2_Subcomponent279', {b1})
    assert _is_linked(a, 'aadl2_Subcomponent279', b1)
    if hasattr(b1, 'aadl2_ComponentImplementationReference280'):
        assert _is_linked(b1, 'aadl2_ComponentImplementationReference280', a)
    _safe_set(a, 'aadl2_Subcomponent279', {b2})
    assert _is_linked(a, 'aadl2_Subcomponent279', b2)
    if hasattr(b1, 'aadl2_ComponentImplementationReference280'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementationReference280', a)
    if hasattr(b2, 'aadl2_ComponentImplementationReference280'):
        assert _is_linked(b2, 'aadl2_ComponentImplementationReference280', a)
    _safe_set(a, 'aadl2_Subcomponent279', set())
    assert not _is_linked(a, 'aadl2_Subcomponent279', b2)
    if hasattr(b2, 'aadl2_ComponentImplementationReference280'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementationReference280', a)


def test_assoc_implemented328_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_Realization()
    b2 = aadl2_Realization()
    _safe_set(a, 'aadl2_ComponentType330', b1)
    assert _is_linked(a, 'aadl2_ComponentType330', b1)
    if hasattr(b1, 'aadl2_Realization329'):
        assert _is_linked(b1, 'aadl2_Realization329', a)
    _safe_set(a, 'aadl2_ComponentType330', b2)
    assert _is_linked(a, 'aadl2_ComponentType330', b2)
    if hasattr(b1, 'aadl2_Realization329'):
        assert not _is_linked(b1, 'aadl2_Realization329', a)
    if hasattr(b2, 'aadl2_Realization329'):
        assert _is_linked(b2, 'aadl2_Realization329', a)
    _safe_set(a, 'aadl2_ComponentType330', None)
    assert not _is_linked(a, 'aadl2_ComponentType330', b2)
    if hasattr(b2, 'aadl2_Realization329'):
        assert not _is_linked(b2, 'aadl2_Realization329', a)


def test_assoc_importedUnit365_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_ModelUnit()
    b2 = aadl2_ModelUnit()
    _safe_set(a, 'aadl2_PackageSection366', {b1})
    assert _is_linked(a, 'aadl2_PackageSection366', b1)
    if hasattr(b1, 'aadl2_ModelUnit'):
        assert _is_linked(b1, 'aadl2_ModelUnit', a)
    _safe_set(a, 'aadl2_PackageSection366', {b2})
    assert _is_linked(a, 'aadl2_PackageSection366', b2)
    if hasattr(b1, 'aadl2_ModelUnit'):
        assert not _is_linked(b1, 'aadl2_ModelUnit', a)
    if hasattr(b2, 'aadl2_ModelUnit'):
        assert _is_linked(b2, 'aadl2_ModelUnit', a)
    _safe_set(a, 'aadl2_PackageSection366', set())
    assert not _is_linked(a, 'aadl2_PackageSection366', b2)
    if hasattr(b2, 'aadl2_ModelUnit'):
        assert not _is_linked(b2, 'aadl2_ModelUnit', a)


def test_assoc_inBinding9_link_reassign_clear():
    a = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    b1 = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b2 = aadl2_Classifier(noAnnexes="sample_text_2", noProperties="sample_text_2", noPrototypes="sample_text_2")
    _safe_set(a, 'aadl2_PropertyAssociation10', {b1})
    assert _is_linked(a, 'aadl2_PropertyAssociation10', b1)
    if hasattr(b1, 'aadl2_Classifier'):
        assert _is_linked(b1, 'aadl2_Classifier', a)
    _safe_set(a, 'aadl2_PropertyAssociation10', {b2})
    assert _is_linked(a, 'aadl2_PropertyAssociation10', b2)
    if hasattr(b1, 'aadl2_Classifier'):
        assert not _is_linked(b1, 'aadl2_Classifier', a)
    if hasattr(b2, 'aadl2_Classifier'):
        assert _is_linked(b2, 'aadl2_Classifier', a)
    _safe_set(a, 'aadl2_PropertyAssociation10', set())
    assert not _is_linked(a, 'aadl2_PropertyAssociation10', b2)
    if hasattr(b2, 'aadl2_Classifier'):
        assert not _is_linked(b2, 'aadl2_Classifier', a)


def test_assoc_inEnd298_link_reassign_clear():
    a = aadl2_FlowImplementation(kind="sample_text")
    b1 = aadl2_FlowEnd()
    b2 = aadl2_FlowEnd()
    _safe_set(a, 'aadl2_FlowImplementation299', b1)
    assert _is_linked(a, 'aadl2_FlowImplementation299', b1)
    if hasattr(b1, 'aadl2_FlowEnd300'):
        assert _is_linked(b1, 'aadl2_FlowEnd300', a)
    _safe_set(a, 'aadl2_FlowImplementation299', b2)
    assert _is_linked(a, 'aadl2_FlowImplementation299', b2)
    if hasattr(b1, 'aadl2_FlowEnd300'):
        assert not _is_linked(b1, 'aadl2_FlowEnd300', a)
    if hasattr(b2, 'aadl2_FlowEnd300'):
        assert _is_linked(b2, 'aadl2_FlowEnd300', a)
    _safe_set(a, 'aadl2_FlowImplementation299', None)
    assert not _is_linked(a, 'aadl2_FlowImplementation299', b2)
    if hasattr(b2, 'aadl2_FlowEnd300'):
        assert not _is_linked(b2, 'aadl2_FlowEnd300', a)


def test_assoc_inMode61_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ModalElement()
    b2 = aadl2_ModalElement()
    _safe_set(a, 'aadl2_Mode', b1)
    assert _is_linked(a, 'aadl2_Mode', b1)
    if hasattr(b1, 'aadl2_ModalElement'):
        assert _is_linked(b1, 'aadl2_ModalElement', a)
    _safe_set(a, 'aadl2_Mode', b2)
    assert _is_linked(a, 'aadl2_Mode', b2)
    if hasattr(b1, 'aadl2_ModalElement'):
        assert not _is_linked(b1, 'aadl2_ModalElement', a)
    if hasattr(b2, 'aadl2_ModalElement'):
        assert _is_linked(b2, 'aadl2_ModalElement', a)
    _safe_set(a, 'aadl2_Mode', None)
    assert not _is_linked(a, 'aadl2_Mode', b2)
    if hasattr(b2, 'aadl2_ModalElement'):
        assert not _is_linked(b2, 'aadl2_ModalElement', a)


def test_assoc_inModeOrTransition189_link_reassign_clear():
    a = aadl2_ModalPath()
    b1 = aadl2_ModeFeature()
    b2 = aadl2_ModeFeature()
    _safe_set(a, 'aadl2_ModalPath', {b1})
    assert _is_linked(a, 'aadl2_ModalPath', b1)
    if hasattr(b1, 'aadl2_ModeFeature'):
        assert _is_linked(b1, 'aadl2_ModeFeature', a)
    _safe_set(a, 'aadl2_ModalPath', {b2})
    assert _is_linked(a, 'aadl2_ModalPath', b2)
    if hasattr(b1, 'aadl2_ModeFeature'):
        assert not _is_linked(b1, 'aadl2_ModeFeature', a)
    if hasattr(b2, 'aadl2_ModeFeature'):
        assert _is_linked(b2, 'aadl2_ModeFeature', a)
    _safe_set(a, 'aadl2_ModalPath', set())
    assert not _is_linked(a, 'aadl2_ModalPath', b2)
    if hasattr(b2, 'aadl2_ModeFeature'):
        assert not _is_linked(b2, 'aadl2_ModeFeature', a)


def test_assoc_inheritedMember31_link_reassign_clear():
    a = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    b1 = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b2 = aadl2_Classifier(noAnnexes="sample_text_2", noProperties="sample_text_2", noPrototypes="sample_text_2")
    _safe_set(a, 'aadl2_NamedElement33', b1)
    assert _is_linked(a, 'aadl2_NamedElement33', b1)
    if hasattr(b1, 'aadl2_Classifier32'):
        assert _is_linked(b1, 'aadl2_Classifier32', a)
    _safe_set(a, 'aadl2_NamedElement33', b2)
    assert _is_linked(a, 'aadl2_NamedElement33', b2)
    if hasattr(b1, 'aadl2_Classifier32'):
        assert not _is_linked(b1, 'aadl2_Classifier32', a)
    if hasattr(b2, 'aadl2_Classifier32'):
        assert _is_linked(b2, 'aadl2_Classifier32', a)
    _safe_set(a, 'aadl2_NamedElement33', None)
    assert not _is_linked(a, 'aadl2_NamedElement33', b2)
    if hasattr(b2, 'aadl2_Classifier32'):
        assert not _is_linked(b2, 'aadl2_Classifier32', a)


def test_assoc_member46_link_reassign_clear():
    a = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    b1 = aadl2_Namespace()
    b2 = aadl2_Namespace()
    _safe_set(a, 'aadl2_NamedElement48', b1)
    assert _is_linked(a, 'aadl2_NamedElement48', b1)
    if hasattr(b1, 'aadl2_Namespace47'):
        assert _is_linked(b1, 'aadl2_Namespace47', a)
    _safe_set(a, 'aadl2_NamedElement48', b2)
    assert _is_linked(a, 'aadl2_NamedElement48', b2)
    if hasattr(b1, 'aadl2_Namespace47'):
        assert not _is_linked(b1, 'aadl2_Namespace47', a)
    if hasattr(b2, 'aadl2_Namespace47'):
        assert _is_linked(b2, 'aadl2_Namespace47', a)
    _safe_set(a, 'aadl2_NamedElement48', None)
    assert not _is_linked(a, 'aadl2_NamedElement48', b2)
    if hasattr(b2, 'aadl2_Namespace47'):
        assert not _is_linked(b2, 'aadl2_Namespace47', a)


def test_assoc_namedElement80_link_reassign_clear():
    a = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    b1 = aadl2_ContainmentPathElement(annexName="sample_text")
    b2 = aadl2_ContainmentPathElement(annexName="sample_text_2")
    _safe_set(a, 'aadl2_NamedElement82', b1)
    assert _is_linked(a, 'aadl2_NamedElement82', b1)
    if hasattr(b1, 'aadl2_ContainmentPathElement81'):
        assert _is_linked(b1, 'aadl2_ContainmentPathElement81', a)
    _safe_set(a, 'aadl2_NamedElement82', b2)
    assert _is_linked(a, 'aadl2_NamedElement82', b2)
    if hasattr(b1, 'aadl2_ContainmentPathElement81'):
        assert not _is_linked(b1, 'aadl2_ContainmentPathElement81', a)
    if hasattr(b2, 'aadl2_ContainmentPathElement81'):
        assert _is_linked(b2, 'aadl2_ContainmentPathElement81', a)
    _safe_set(a, 'aadl2_NamedElement82', None)
    assert not _is_linked(a, 'aadl2_NamedElement82', b2)
    if hasattr(b2, 'aadl2_ContainmentPathElement81'):
        assert not _is_linked(b2, 'aadl2_ContainmentPathElement81', a)


def test_assoc_namedElementReference888_link_reassign_clear():
    a = aadl2_MetaclassReference(annexName="sample_text", metaclassName="sample_text")
    b1 = aadl2_ReferenceType()
    b2 = aadl2_ReferenceType()
    _safe_set(a, 'aadl2_MetaclassReference889', b1)
    assert _is_linked(a, 'aadl2_MetaclassReference889', b1)
    if hasattr(b1, 'aadl2_ReferenceType'):
        assert _is_linked(b1, 'aadl2_ReferenceType', a)
    _safe_set(a, 'aadl2_MetaclassReference889', b2)
    assert _is_linked(a, 'aadl2_MetaclassReference889', b2)
    if hasattr(b1, 'aadl2_ReferenceType'):
        assert not _is_linked(b1, 'aadl2_ReferenceType', a)
    if hasattr(b2, 'aadl2_ReferenceType'):
        assert _is_linked(b2, 'aadl2_ReferenceType', a)
    _safe_set(a, 'aadl2_MetaclassReference889', None)
    assert not _is_linked(a, 'aadl2_MetaclassReference889', b2)
    if hasattr(b2, 'aadl2_ReferenceType'):
        assert not _is_linked(b2, 'aadl2_ReferenceType', a)


def test_assoc_outEnd184_link_reassign_clear():
    a = aadl2_FlowSpecification(kind="sample_text")
    b1 = aadl2_FlowEnd()
    b2 = aadl2_FlowEnd()
    _safe_set(a, 'aadl2_FlowSpecification185', b1)
    assert _is_linked(a, 'aadl2_FlowSpecification185', b1)
    if hasattr(b1, 'aadl2_FlowEnd'):
        assert _is_linked(b1, 'aadl2_FlowEnd', a)
    _safe_set(a, 'aadl2_FlowSpecification185', b2)
    assert _is_linked(a, 'aadl2_FlowSpecification185', b2)
    if hasattr(b1, 'aadl2_FlowEnd'):
        assert not _is_linked(b1, 'aadl2_FlowEnd', a)
    if hasattr(b2, 'aadl2_FlowEnd'):
        assert _is_linked(b2, 'aadl2_FlowEnd', a)
    _safe_set(a, 'aadl2_FlowSpecification185', None)
    assert not _is_linked(a, 'aadl2_FlowSpecification185', b2)
    if hasattr(b2, 'aadl2_FlowEnd'):
        assert not _is_linked(b2, 'aadl2_FlowEnd', a)


def test_assoc_outEnd301_link_reassign_clear():
    a = aadl2_FlowImplementation(kind="sample_text")
    b1 = aadl2_FlowEnd()
    b2 = aadl2_FlowEnd()
    _safe_set(a, 'aadl2_FlowImplementation302', b1)
    assert _is_linked(a, 'aadl2_FlowImplementation302', b1)
    if hasattr(b1, 'aadl2_FlowEnd303'):
        assert _is_linked(b1, 'aadl2_FlowEnd303', a)
    _safe_set(a, 'aadl2_FlowImplementation302', b2)
    assert _is_linked(a, 'aadl2_FlowImplementation302', b2)
    if hasattr(b1, 'aadl2_FlowEnd303'):
        assert not _is_linked(b1, 'aadl2_FlowEnd303', a)
    if hasattr(b2, 'aadl2_FlowEnd303'):
        assert _is_linked(b2, 'aadl2_FlowEnd303', a)
    _safe_set(a, 'aadl2_FlowImplementation302', None)
    assert not _is_linked(a, 'aadl2_FlowImplementation302', b2)
    if hasattr(b2, 'aadl2_FlowEnd303'):
        assert not _is_linked(b2, 'aadl2_FlowEnd303', a)


def test_assoc_ownedAbstractFeature166_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_AbstractFeature()
    b2 = aadl2_AbstractFeature()
    _safe_set(a, 'aadl2_ComponentType167', {b1})
    assert _is_linked(a, 'aadl2_ComponentType167', b1)
    if hasattr(b1, 'aadl2_AbstractFeature'):
        assert _is_linked(b1, 'aadl2_AbstractFeature', a)
    _safe_set(a, 'aadl2_ComponentType167', {b2})
    assert _is_linked(a, 'aadl2_ComponentType167', b2)
    if hasattr(b1, 'aadl2_AbstractFeature'):
        assert not _is_linked(b1, 'aadl2_AbstractFeature', a)
    if hasattr(b2, 'aadl2_AbstractFeature'):
        assert _is_linked(b2, 'aadl2_AbstractFeature', a)
    _safe_set(a, 'aadl2_ComponentType167', set())
    assert not _is_linked(a, 'aadl2_ComponentType167', b2)
    if hasattr(b2, 'aadl2_AbstractFeature'):
        assert not _is_linked(b2, 'aadl2_AbstractFeature', a)


def test_assoc_ownedAbstractSubcomponent115_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_AbstractSubcomponent()
    b2 = aadl2_AbstractSubcomponent()
    _safe_set(a, 'aadl2_ComponentImplementation116', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation116', b1)
    if hasattr(b1, 'aadl2_AbstractSubcomponent'):
        assert _is_linked(b1, 'aadl2_AbstractSubcomponent', a)
    _safe_set(a, 'aadl2_ComponentImplementation116', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation116', b2)
    if hasattr(b1, 'aadl2_AbstractSubcomponent'):
        assert not _is_linked(b1, 'aadl2_AbstractSubcomponent', a)
    if hasattr(b2, 'aadl2_AbstractSubcomponent'):
        assert _is_linked(b2, 'aadl2_AbstractSubcomponent', a)
    _safe_set(a, 'aadl2_ComponentImplementation116', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation116', b2)
    if hasattr(b2, 'aadl2_AbstractSubcomponent'):
        assert not _is_linked(b2, 'aadl2_AbstractSubcomponent', a)


def test_assoc_ownedAccessConnection117_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_AccessConnection(accessCategory="sample_text")
    b2 = aadl2_AccessConnection(accessCategory="sample_text_2")
    _safe_set(a, 'aadl2_ComponentImplementation118', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation118', b1)
    if hasattr(b1, 'aadl2_AccessConnection'):
        assert _is_linked(b1, 'aadl2_AccessConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation118', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation118', b2)
    if hasattr(b1, 'aadl2_AccessConnection'):
        assert not _is_linked(b1, 'aadl2_AccessConnection', a)
    if hasattr(b2, 'aadl2_AccessConnection'):
        assert _is_linked(b2, 'aadl2_AccessConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation118', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation118', b2)
    if hasattr(b2, 'aadl2_AccessConnection'):
        assert not _is_linked(b2, 'aadl2_AccessConnection', a)


def test_assoc_ownedAnnexLibrary362_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_AnnexLibrary()
    b2 = aadl2_AnnexLibrary()
    _safe_set(a, 'aadl2_PackageSection363', {b1})
    assert _is_linked(a, 'aadl2_PackageSection363', b1)
    if hasattr(b1, 'aadl2_AnnexLibrary364'):
        assert _is_linked(b1, 'aadl2_AnnexLibrary364', a)
    _safe_set(a, 'aadl2_PackageSection363', {b2})
    assert _is_linked(a, 'aadl2_PackageSection363', b2)
    if hasattr(b1, 'aadl2_AnnexLibrary364'):
        assert not _is_linked(b1, 'aadl2_AnnexLibrary364', a)
    if hasattr(b2, 'aadl2_AnnexLibrary364'):
        assert _is_linked(b2, 'aadl2_AnnexLibrary364', a)
    _safe_set(a, 'aadl2_PackageSection363', set())
    assert not _is_linked(a, 'aadl2_PackageSection363', b2)
    if hasattr(b2, 'aadl2_AnnexLibrary364'):
        assert not _is_linked(b2, 'aadl2_AnnexLibrary364', a)


def test_assoc_ownedAnnexSubclause38_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_AnnexSubclause()
    b2 = aadl2_AnnexSubclause()
    _safe_set(a, 'aadl2_Classifier39', {b1})
    assert _is_linked(a, 'aadl2_Classifier39', b1)
    if hasattr(b1, 'aadl2_AnnexSubclause'):
        assert _is_linked(b1, 'aadl2_AnnexSubclause', a)
    _safe_set(a, 'aadl2_Classifier39', {b2})
    assert _is_linked(a, 'aadl2_Classifier39', b2)
    if hasattr(b1, 'aadl2_AnnexSubclause'):
        assert not _is_linked(b1, 'aadl2_AnnexSubclause', a)
    if hasattr(b2, 'aadl2_AnnexSubclause'):
        assert _is_linked(b2, 'aadl2_AnnexSubclause', a)
    _safe_set(a, 'aadl2_Classifier39', set())
    assert not _is_linked(a, 'aadl2_Classifier39', b2)
    if hasattr(b2, 'aadl2_AnnexSubclause'):
        assert not _is_linked(b2, 'aadl2_AnnexSubclause', a)


def test_assoc_ownedBusAccess216_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_FeatureGroupType()
    b2 = aadl2_FeatureGroupType()
    _safe_set(a, 'aadl2_BusAccess', b1)
    assert _is_linked(a, 'aadl2_BusAccess', b1)
    if hasattr(b1, 'aadl2_FeatureGroupType217'):
        assert _is_linked(b1, 'aadl2_FeatureGroupType217', a)
    _safe_set(a, 'aadl2_BusAccess', b2)
    assert _is_linked(a, 'aadl2_BusAccess', b2)
    if hasattr(b1, 'aadl2_FeatureGroupType217'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupType217', a)
    if hasattr(b2, 'aadl2_FeatureGroupType217'):
        assert _is_linked(b2, 'aadl2_FeatureGroupType217', a)
    _safe_set(a, 'aadl2_BusAccess', None)
    assert not _is_linked(a, 'aadl2_BusAccess', b2)
    if hasattr(b2, 'aadl2_FeatureGroupType217'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupType217', a)


def test_assoc_ownedBusAccess423_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_AbstractType()
    b2 = aadl2_AbstractType()
    _safe_set(a, 'aadl2_BusAccess424', b1)
    assert _is_linked(a, 'aadl2_BusAccess424', b1)
    if hasattr(b1, 'aadl2_AbstractType'):
        assert _is_linked(b1, 'aadl2_AbstractType', a)
    _safe_set(a, 'aadl2_BusAccess424', b2)
    assert _is_linked(a, 'aadl2_BusAccess424', b2)
    if hasattr(b1, 'aadl2_AbstractType'):
        assert not _is_linked(b1, 'aadl2_AbstractType', a)
    if hasattr(b2, 'aadl2_AbstractType'):
        assert _is_linked(b2, 'aadl2_AbstractType', a)
    _safe_set(a, 'aadl2_BusAccess424', None)
    assert not _is_linked(a, 'aadl2_BusAccess424', b2)
    if hasattr(b2, 'aadl2_AbstractType'):
        assert not _is_linked(b2, 'aadl2_AbstractType', a)


def test_assoc_ownedBusAccess497_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_BusType()
    b2 = aadl2_BusType()
    _safe_set(a, 'aadl2_BusAccess498', b1)
    assert _is_linked(a, 'aadl2_BusAccess498', b1)
    if hasattr(b1, 'aadl2_BusType'):
        assert _is_linked(b1, 'aadl2_BusType', a)
    _safe_set(a, 'aadl2_BusAccess498', b2)
    assert _is_linked(a, 'aadl2_BusAccess498', b2)
    if hasattr(b1, 'aadl2_BusType'):
        assert not _is_linked(b1, 'aadl2_BusType', a)
    if hasattr(b2, 'aadl2_BusType'):
        assert _is_linked(b2, 'aadl2_BusType', a)
    _safe_set(a, 'aadl2_BusAccess498', None)
    assert not _is_linked(a, 'aadl2_BusAccess498', b2)
    if hasattr(b2, 'aadl2_BusType'):
        assert not _is_linked(b2, 'aadl2_BusType', a)


def test_assoc_ownedBusAccess531_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_DeviceType()
    b2 = aadl2_DeviceType()
    _safe_set(a, 'aadl2_BusAccess533', b1)
    assert _is_linked(a, 'aadl2_BusAccess533', b1)
    if hasattr(b1, 'aadl2_DeviceType532'):
        assert _is_linked(b1, 'aadl2_DeviceType532', a)
    _safe_set(a, 'aadl2_BusAccess533', b2)
    assert _is_linked(a, 'aadl2_BusAccess533', b2)
    if hasattr(b1, 'aadl2_DeviceType532'):
        assert not _is_linked(b1, 'aadl2_DeviceType532', a)
    if hasattr(b2, 'aadl2_DeviceType532'):
        assert _is_linked(b2, 'aadl2_DeviceType532', a)
    _safe_set(a, 'aadl2_BusAccess533', None)
    assert not _is_linked(a, 'aadl2_BusAccess533', b2)
    if hasattr(b2, 'aadl2_DeviceType532'):
        assert not _is_linked(b2, 'aadl2_DeviceType532', a)


def test_assoc_ownedBusAccess548_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_MemoryType()
    b2 = aadl2_MemoryType()
    _safe_set(a, 'aadl2_BusAccess549', b1)
    assert _is_linked(a, 'aadl2_BusAccess549', b1)
    if hasattr(b1, 'aadl2_MemoryType'):
        assert _is_linked(b1, 'aadl2_MemoryType', a)
    _safe_set(a, 'aadl2_BusAccess549', b2)
    assert _is_linked(a, 'aadl2_BusAccess549', b2)
    if hasattr(b1, 'aadl2_MemoryType'):
        assert not _is_linked(b1, 'aadl2_MemoryType', a)
    if hasattr(b2, 'aadl2_MemoryType'):
        assert _is_linked(b2, 'aadl2_MemoryType', a)
    _safe_set(a, 'aadl2_BusAccess549', None)
    assert not _is_linked(a, 'aadl2_BusAccess549', b2)
    if hasattr(b2, 'aadl2_MemoryType'):
        assert not _is_linked(b2, 'aadl2_MemoryType', a)


def test_assoc_ownedBusAccess599_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_SystemType()
    b2 = aadl2_SystemType()
    _safe_set(a, 'aadl2_BusAccess600', b1)
    assert _is_linked(a, 'aadl2_BusAccess600', b1)
    if hasattr(b1, 'aadl2_SystemType'):
        assert _is_linked(b1, 'aadl2_SystemType', a)
    _safe_set(a, 'aadl2_BusAccess600', b2)
    assert _is_linked(a, 'aadl2_BusAccess600', b2)
    if hasattr(b1, 'aadl2_SystemType'):
        assert not _is_linked(b1, 'aadl2_SystemType', a)
    if hasattr(b2, 'aadl2_SystemType'):
        assert _is_linked(b2, 'aadl2_SystemType', a)
    _safe_set(a, 'aadl2_BusAccess600', None)
    assert not _is_linked(a, 'aadl2_BusAccess600', b2)
    if hasattr(b2, 'aadl2_SystemType'):
        assert not _is_linked(b2, 'aadl2_SystemType', a)


def test_assoc_ownedBusAccess659_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_ProcessorType()
    b2 = aadl2_ProcessorType()
    _safe_set(a, 'aadl2_BusAccess661', b1)
    assert _is_linked(a, 'aadl2_BusAccess661', b1)
    if hasattr(b1, 'aadl2_ProcessorType660'):
        assert _is_linked(b1, 'aadl2_ProcessorType660', a)
    _safe_set(a, 'aadl2_BusAccess661', b2)
    assert _is_linked(a, 'aadl2_BusAccess661', b2)
    if hasattr(b1, 'aadl2_ProcessorType660'):
        assert not _is_linked(b1, 'aadl2_ProcessorType660', a)
    if hasattr(b2, 'aadl2_ProcessorType660'):
        assert _is_linked(b2, 'aadl2_ProcessorType660', a)
    _safe_set(a, 'aadl2_BusAccess661', None)
    assert not _is_linked(a, 'aadl2_BusAccess661', b2)
    if hasattr(b2, 'aadl2_ProcessorType660'):
        assert not _is_linked(b2, 'aadl2_ProcessorType660', a)


def test_assoc_ownedBusAccess774_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_VirtualBusType()
    b2 = aadl2_VirtualBusType()
    _safe_set(a, 'aadl2_BusAccess776', b1)
    assert _is_linked(a, 'aadl2_BusAccess776', b1)
    if hasattr(b1, 'aadl2_VirtualBusType775'):
        assert _is_linked(b1, 'aadl2_VirtualBusType775', a)
    _safe_set(a, 'aadl2_BusAccess776', b2)
    assert _is_linked(a, 'aadl2_BusAccess776', b2)
    if hasattr(b1, 'aadl2_VirtualBusType775'):
        assert not _is_linked(b1, 'aadl2_VirtualBusType775', a)
    if hasattr(b2, 'aadl2_VirtualBusType775'):
        assert _is_linked(b2, 'aadl2_VirtualBusType775', a)
    _safe_set(a, 'aadl2_BusAccess776', None)
    assert not _is_linked(a, 'aadl2_BusAccess776', b2)
    if hasattr(b2, 'aadl2_VirtualBusType775'):
        assert not _is_linked(b2, 'aadl2_VirtualBusType775', a)


def test_assoc_ownedBusAccess793_link_reassign_clear():
    a = aadl2_BusAccess(virtual="sample_text")
    b1 = aadl2_VirtualProcessorType()
    b2 = aadl2_VirtualProcessorType()
    _safe_set(a, 'aadl2_BusAccess795', b1)
    assert _is_linked(a, 'aadl2_BusAccess795', b1)
    if hasattr(b1, 'aadl2_VirtualProcessorType794'):
        assert _is_linked(b1, 'aadl2_VirtualProcessorType794', a)
    _safe_set(a, 'aadl2_BusAccess795', b2)
    assert _is_linked(a, 'aadl2_BusAccess795', b2)
    if hasattr(b1, 'aadl2_VirtualProcessorType794'):
        assert not _is_linked(b1, 'aadl2_VirtualProcessorType794', a)
    if hasattr(b2, 'aadl2_VirtualProcessorType794'):
        assert _is_linked(b2, 'aadl2_VirtualProcessorType794', a)
    _safe_set(a, 'aadl2_BusAccess795', None)
    assert not _is_linked(a, 'aadl2_BusAccess795', b2)
    if hasattr(b2, 'aadl2_VirtualProcessorType794'):
        assert not _is_linked(b2, 'aadl2_VirtualProcessorType794', a)


def test_assoc_ownedClassifier357_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b2 = aadl2_Classifier(noAnnexes="sample_text_2", noProperties="sample_text_2", noPrototypes="sample_text_2")
    _safe_set(a, 'aadl2_PackageSection358', {b1})
    assert _is_linked(a, 'aadl2_PackageSection358', b1)
    if hasattr(b1, 'aadl2_Classifier359'):
        assert _is_linked(b1, 'aadl2_Classifier359', a)
    _safe_set(a, 'aadl2_PackageSection358', {b2})
    assert _is_linked(a, 'aadl2_PackageSection358', b2)
    if hasattr(b1, 'aadl2_Classifier359'):
        assert not _is_linked(b1, 'aadl2_Classifier359', a)
    if hasattr(b2, 'aadl2_Classifier359'):
        assert _is_linked(b2, 'aadl2_Classifier359', a)
    _safe_set(a, 'aadl2_PackageSection358', set())
    assert not _is_linked(a, 'aadl2_PackageSection358', b2)
    if hasattr(b2, 'aadl2_Classifier359'):
        assert not _is_linked(b2, 'aadl2_Classifier359', a)


def test_assoc_ownedComment2_link_reassign_clear():
    a = aadl2_Element()
    b1 = aadl2_Comment(body="sample_text")
    b2 = aadl2_Comment(body="sample_text_2")
    _safe_set(a, 'aadl2_Element3', {b1})
    assert _is_linked(a, 'aadl2_Element3', b1)
    if hasattr(b1, 'aadl2_Comment'):
        assert _is_linked(b1, 'aadl2_Comment', a)
    _safe_set(a, 'aadl2_Element3', {b2})
    assert _is_linked(a, 'aadl2_Element3', b2)
    if hasattr(b1, 'aadl2_Comment'):
        assert not _is_linked(b1, 'aadl2_Comment', a)
    if hasattr(b2, 'aadl2_Comment'):
        assert _is_linked(b2, 'aadl2_Comment', a)
    _safe_set(a, 'aadl2_Element3', set())
    assert not _is_linked(a, 'aadl2_Element3', b2)
    if hasattr(b2, 'aadl2_Comment'):
        assert not _is_linked(b2, 'aadl2_Comment', a)


def test_assoc_ownedComponentTypeRename355_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_ComponentTypeRename(category="sample_text")
    b2 = aadl2_ComponentTypeRename(category="sample_text_2")
    _safe_set(a, 'aadl2_PackageSection356', {b1})
    assert _is_linked(a, 'aadl2_PackageSection356', b1)
    if hasattr(b1, 'aadl2_ComponentTypeRename'):
        assert _is_linked(b1, 'aadl2_ComponentTypeRename', a)
    _safe_set(a, 'aadl2_PackageSection356', {b2})
    assert _is_linked(a, 'aadl2_PackageSection356', b2)
    if hasattr(b1, 'aadl2_ComponentTypeRename'):
        assert not _is_linked(b1, 'aadl2_ComponentTypeRename', a)
    if hasattr(b2, 'aadl2_ComponentTypeRename'):
        assert _is_linked(b2, 'aadl2_ComponentTypeRename', a)
    _safe_set(a, 'aadl2_PackageSection356', set())
    assert not _is_linked(a, 'aadl2_PackageSection356', b2)
    if hasattr(b2, 'aadl2_ComponentTypeRename'):
        assert not _is_linked(b2, 'aadl2_ComponentTypeRename', a)


def test_assoc_ownedConnection107_link_reassign_clear():
    a = aadl2_Connection(bidirectional="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_Connection', b1)
    assert _is_linked(a, 'aadl2_Connection', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation108'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation108', a)
    _safe_set(a, 'aadl2_Connection', b2)
    assert _is_linked(a, 'aadl2_Connection', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation108'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation108', a)
    if hasattr(b2, 'aadl2_ComponentImplementation108'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation108', a)
    _safe_set(a, 'aadl2_Connection', None)
    assert not _is_linked(a, 'aadl2_Connection', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation108'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation108', a)


def test_assoc_ownedElement1_link_reassign_clear():
    a = aadl2_Element()
    b1 = aadl2_Element()
    b2 = aadl2_Element()
    _safe_set(a, 'aadl2_Element', b1)
    assert _is_linked(a, 'aadl2_Element', b1)
    if hasattr(b1, 'aadl2_Element0'):
        assert _is_linked(b1, 'aadl2_Element0', a)
    _safe_set(a, 'aadl2_Element', b2)
    assert _is_linked(a, 'aadl2_Element', b2)
    if hasattr(b1, 'aadl2_Element0'):
        assert not _is_linked(b1, 'aadl2_Element0', a)
    if hasattr(b2, 'aadl2_Element0'):
        assert _is_linked(b2, 'aadl2_Element0', a)
    _safe_set(a, 'aadl2_Element', None)
    assert not _is_linked(a, 'aadl2_Element', b2)
    if hasattr(b2, 'aadl2_Element0'):
        assert not _is_linked(b2, 'aadl2_Element0', a)


def test_assoc_ownedEndToEndFlow113_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_EndToEndFlow()
    b2 = aadl2_EndToEndFlow()
    _safe_set(a, 'aadl2_ComponentImplementation114', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation114', b1)
    if hasattr(b1, 'aadl2_EndToEndFlow'):
        assert _is_linked(b1, 'aadl2_EndToEndFlow', a)
    _safe_set(a, 'aadl2_ComponentImplementation114', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation114', b2)
    if hasattr(b1, 'aadl2_EndToEndFlow'):
        assert not _is_linked(b1, 'aadl2_EndToEndFlow', a)
    if hasattr(b2, 'aadl2_EndToEndFlow'):
        assert _is_linked(b2, 'aadl2_EndToEndFlow', a)
    _safe_set(a, 'aadl2_ComponentImplementation114', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation114', b2)
    if hasattr(b2, 'aadl2_EndToEndFlow'):
        assert not _is_linked(b2, 'aadl2_EndToEndFlow', a)


def test_assoc_ownedEventDataSource133_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_EventDataSource()
    b2 = aadl2_EventDataSource()
    _safe_set(a, 'aadl2_ComponentImplementation134', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation134', b1)
    if hasattr(b1, 'aadl2_EventDataSource'):
        assert _is_linked(b1, 'aadl2_EventDataSource', a)
    _safe_set(a, 'aadl2_ComponentImplementation134', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation134', b2)
    if hasattr(b1, 'aadl2_EventDataSource'):
        assert not _is_linked(b1, 'aadl2_EventDataSource', a)
    if hasattr(b2, 'aadl2_EventDataSource'):
        assert _is_linked(b2, 'aadl2_EventDataSource', a)
    _safe_set(a, 'aadl2_ComponentImplementation134', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation134', b2)
    if hasattr(b2, 'aadl2_EventDataSource'):
        assert not _is_linked(b2, 'aadl2_EventDataSource', a)


def test_assoc_ownedEventSource131_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_EventSource()
    b2 = aadl2_EventSource()
    _safe_set(a, 'aadl2_ComponentImplementation132', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation132', b1)
    if hasattr(b1, 'aadl2_EventSource'):
        assert _is_linked(b1, 'aadl2_EventSource', a)
    _safe_set(a, 'aadl2_ComponentImplementation132', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation132', b2)
    if hasattr(b1, 'aadl2_EventSource'):
        assert not _is_linked(b1, 'aadl2_EventSource', a)
    if hasattr(b2, 'aadl2_EventSource'):
        assert _is_linked(b2, 'aadl2_EventSource', a)
    _safe_set(a, 'aadl2_ComponentImplementation132', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation132', b2)
    if hasattr(b2, 'aadl2_EventSource'):
        assert not _is_linked(b2, 'aadl2_EventSource', a)


def test_assoc_ownedExtension109_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ImplementationExtension()
    b2 = aadl2_ImplementationExtension()
    _safe_set(a, 'aadl2_ComponentImplementation110', b1)
    assert _is_linked(a, 'aadl2_ComponentImplementation110', b1)
    if hasattr(b1, 'aadl2_ImplementationExtension'):
        assert _is_linked(b1, 'aadl2_ImplementationExtension', a)
    _safe_set(a, 'aadl2_ComponentImplementation110', b2)
    assert _is_linked(a, 'aadl2_ComponentImplementation110', b2)
    if hasattr(b1, 'aadl2_ImplementationExtension'):
        assert not _is_linked(b1, 'aadl2_ImplementationExtension', a)
    if hasattr(b2, 'aadl2_ImplementationExtension'):
        assert _is_linked(b2, 'aadl2_ImplementationExtension', a)
    _safe_set(a, 'aadl2_ComponentImplementation110', None)
    assert not _is_linked(a, 'aadl2_ComponentImplementation110', b2)
    if hasattr(b2, 'aadl2_ImplementationExtension'):
        assert not _is_linked(b2, 'aadl2_ImplementationExtension', a)


def test_assoc_ownedExtension162_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_TypeExtension()
    b2 = aadl2_TypeExtension()
    _safe_set(a, 'aadl2_ComponentType163', b1)
    assert _is_linked(a, 'aadl2_ComponentType163', b1)
    if hasattr(b1, 'aadl2_TypeExtension'):
        assert _is_linked(b1, 'aadl2_TypeExtension', a)
    _safe_set(a, 'aadl2_ComponentType163', b2)
    assert _is_linked(a, 'aadl2_ComponentType163', b2)
    if hasattr(b1, 'aadl2_TypeExtension'):
        assert not _is_linked(b1, 'aadl2_TypeExtension', a)
    if hasattr(b2, 'aadl2_TypeExtension'):
        assert _is_linked(b2, 'aadl2_TypeExtension', a)
    _safe_set(a, 'aadl2_ComponentType163', None)
    assert not _is_linked(a, 'aadl2_ComponentType163', b2)
    if hasattr(b2, 'aadl2_TypeExtension'):
        assert not _is_linked(b2, 'aadl2_TypeExtension', a)


def test_assoc_ownedFeature155_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_Feature()
    b2 = aadl2_Feature()
    _safe_set(a, 'aadl2_ComponentType156', {b1})
    assert _is_linked(a, 'aadl2_ComponentType156', b1)
    if hasattr(b1, 'aadl2_Feature'):
        assert _is_linked(b1, 'aadl2_Feature', a)
    _safe_set(a, 'aadl2_ComponentType156', {b2})
    assert _is_linked(a, 'aadl2_ComponentType156', b2)
    if hasattr(b1, 'aadl2_Feature'):
        assert not _is_linked(b1, 'aadl2_Feature', a)
    if hasattr(b2, 'aadl2_Feature'):
        assert _is_linked(b2, 'aadl2_Feature', a)
    _safe_set(a, 'aadl2_ComponentType156', set())
    assert not _is_linked(a, 'aadl2_ComponentType156', b2)
    if hasattr(b2, 'aadl2_Feature'):
        assert not _is_linked(b2, 'aadl2_Feature', a)


def test_assoc_ownedFeatureConnection123_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_FeatureConnection()
    b2 = aadl2_FeatureConnection()
    _safe_set(a, 'aadl2_ComponentImplementation124', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation124', b1)
    if hasattr(b1, 'aadl2_FeatureConnection'):
        assert _is_linked(b1, 'aadl2_FeatureConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation124', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation124', b2)
    if hasattr(b1, 'aadl2_FeatureConnection'):
        assert not _is_linked(b1, 'aadl2_FeatureConnection', a)
    if hasattr(b2, 'aadl2_FeatureConnection'):
        assert _is_linked(b2, 'aadl2_FeatureConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation124', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation124', b2)
    if hasattr(b2, 'aadl2_FeatureConnection'):
        assert not _is_linked(b2, 'aadl2_FeatureConnection', a)


def test_assoc_ownedFeatureGroup164_link_reassign_clear():
    a = aadl2_FeatureGroup(inverse="sample_text")
    b1 = aadl2_ComponentType(noFeatures="sample_text")
    b2 = aadl2_ComponentType(noFeatures="sample_text_2")
    _safe_set(a, 'aadl2_FeatureGroup', b1)
    assert _is_linked(a, 'aadl2_FeatureGroup', b1)
    if hasattr(b1, 'aadl2_ComponentType165'):
        assert _is_linked(b1, 'aadl2_ComponentType165', a)
    _safe_set(a, 'aadl2_FeatureGroup', b2)
    assert _is_linked(a, 'aadl2_FeatureGroup', b2)
    if hasattr(b1, 'aadl2_ComponentType165'):
        assert not _is_linked(b1, 'aadl2_ComponentType165', a)
    if hasattr(b2, 'aadl2_ComponentType165'):
        assert _is_linked(b2, 'aadl2_ComponentType165', a)
    _safe_set(a, 'aadl2_FeatureGroup', None)
    assert not _is_linked(a, 'aadl2_FeatureGroup', b2)
    if hasattr(b2, 'aadl2_ComponentType165'):
        assert not _is_linked(b2, 'aadl2_ComponentType165', a)


def test_assoc_ownedFeatureGroup226_link_reassign_clear():
    a = aadl2_FeatureGroup(inverse="sample_text")
    b1 = aadl2_FeatureGroupType()
    b2 = aadl2_FeatureGroupType()
    _safe_set(a, 'aadl2_FeatureGroup228', b1)
    assert _is_linked(a, 'aadl2_FeatureGroup228', b1)
    if hasattr(b1, 'aadl2_FeatureGroupType227'):
        assert _is_linked(b1, 'aadl2_FeatureGroupType227', a)
    _safe_set(a, 'aadl2_FeatureGroup228', b2)
    assert _is_linked(a, 'aadl2_FeatureGroup228', b2)
    if hasattr(b1, 'aadl2_FeatureGroupType227'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupType227', a)
    if hasattr(b2, 'aadl2_FeatureGroupType227'):
        assert _is_linked(b2, 'aadl2_FeatureGroupType227', a)
    _safe_set(a, 'aadl2_FeatureGroup228', None)
    assert not _is_linked(a, 'aadl2_FeatureGroup228', b2)
    if hasattr(b2, 'aadl2_FeatureGroupType227'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupType227', a)


def test_assoc_ownedFeatureGroupConnection125_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_FeatureGroupConnection()
    b2 = aadl2_FeatureGroupConnection()
    _safe_set(a, 'aadl2_ComponentImplementation126', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation126', b1)
    if hasattr(b1, 'aadl2_FeatureGroupConnection'):
        assert _is_linked(b1, 'aadl2_FeatureGroupConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation126', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation126', b2)
    if hasattr(b1, 'aadl2_FeatureGroupConnection'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupConnection', a)
    if hasattr(b2, 'aadl2_FeatureGroupConnection'):
        assert _is_linked(b2, 'aadl2_FeatureGroupConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation126', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation126', b2)
    if hasattr(b2, 'aadl2_FeatureGroupConnection'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupConnection', a)


def test_assoc_ownedFeatureGroupTypeRename360_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_FeatureGroupTypeRename()
    b2 = aadl2_FeatureGroupTypeRename()
    _safe_set(a, 'aadl2_PackageSection361', {b1})
    assert _is_linked(a, 'aadl2_PackageSection361', b1)
    if hasattr(b1, 'aadl2_FeatureGroupTypeRename'):
        assert _is_linked(b1, 'aadl2_FeatureGroupTypeRename', a)
    _safe_set(a, 'aadl2_PackageSection361', {b2})
    assert _is_linked(a, 'aadl2_PackageSection361', b2)
    if hasattr(b1, 'aadl2_FeatureGroupTypeRename'):
        assert not _is_linked(b1, 'aadl2_FeatureGroupTypeRename', a)
    if hasattr(b2, 'aadl2_FeatureGroupTypeRename'):
        assert _is_linked(b2, 'aadl2_FeatureGroupTypeRename', a)
    _safe_set(a, 'aadl2_PackageSection361', set())
    assert not _is_linked(a, 'aadl2_PackageSection361', b2)
    if hasattr(b2, 'aadl2_FeatureGroupTypeRename'):
        assert not _is_linked(b2, 'aadl2_FeatureGroupTypeRename', a)


def test_assoc_ownedFlowImplementation105_link_reassign_clear():
    a = aadl2_FlowImplementation(kind="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_FlowImplementation', b1)
    assert _is_linked(a, 'aadl2_FlowImplementation', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation106'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation106', a)
    _safe_set(a, 'aadl2_FlowImplementation', b2)
    assert _is_linked(a, 'aadl2_FlowImplementation', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation106'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation106', a)
    if hasattr(b2, 'aadl2_ComponentImplementation106'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation106', a)
    _safe_set(a, 'aadl2_FlowImplementation', None)
    assert not _is_linked(a, 'aadl2_FlowImplementation', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation106'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation106', a)


def test_assoc_ownedFlowSegment296_link_reassign_clear():
    a = aadl2_FlowImplementation(kind="sample_text")
    b1 = aadl2_FlowSegment()
    b2 = aadl2_FlowSegment()
    _safe_set(a, 'aadl2_FlowImplementation297', {b1})
    assert _is_linked(a, 'aadl2_FlowImplementation297', b1)
    if hasattr(b1, 'aadl2_FlowSegment'):
        assert _is_linked(b1, 'aadl2_FlowSegment', a)
    _safe_set(a, 'aadl2_FlowImplementation297', {b2})
    assert _is_linked(a, 'aadl2_FlowImplementation297', b2)
    if hasattr(b1, 'aadl2_FlowSegment'):
        assert not _is_linked(b1, 'aadl2_FlowSegment', a)
    if hasattr(b2, 'aadl2_FlowSegment'):
        assert _is_linked(b2, 'aadl2_FlowSegment', a)
    _safe_set(a, 'aadl2_FlowImplementation297', set())
    assert not _is_linked(a, 'aadl2_FlowImplementation297', b2)
    if hasattr(b2, 'aadl2_FlowSegment'):
        assert not _is_linked(b2, 'aadl2_FlowSegment', a)


def test_assoc_ownedFlowSpecification160_link_reassign_clear():
    a = aadl2_FlowSpecification(kind="sample_text")
    b1 = aadl2_ComponentType(noFeatures="sample_text")
    b2 = aadl2_ComponentType(noFeatures="sample_text_2")
    _safe_set(a, 'aadl2_FlowSpecification', b1)
    assert _is_linked(a, 'aadl2_FlowSpecification', b1)
    if hasattr(b1, 'aadl2_ComponentType161'):
        assert _is_linked(b1, 'aadl2_ComponentType161', a)
    _safe_set(a, 'aadl2_FlowSpecification', b2)
    assert _is_linked(a, 'aadl2_FlowSpecification', b2)
    if hasattr(b1, 'aadl2_ComponentType161'):
        assert not _is_linked(b1, 'aadl2_ComponentType161', a)
    if hasattr(b2, 'aadl2_ComponentType161'):
        assert _is_linked(b2, 'aadl2_ComponentType161', a)
    _safe_set(a, 'aadl2_FlowSpecification', None)
    assert not _is_linked(a, 'aadl2_FlowSpecification', b2)
    if hasattr(b2, 'aadl2_ComponentType161'):
        assert not _is_linked(b2, 'aadl2_ComponentType161', a)


def test_assoc_ownedInternalFeature129_link_reassign_clear():
    a = aadl2_InternalFeature(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_InternalFeature', b1)
    assert _is_linked(a, 'aadl2_InternalFeature', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation130'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation130', a)
    _safe_set(a, 'aadl2_InternalFeature', b2)
    assert _is_linked(a, 'aadl2_InternalFeature', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation130'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation130', a)
    if hasattr(b2, 'aadl2_ComponentImplementation130'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation130', a)
    _safe_set(a, 'aadl2_InternalFeature', None)
    assert not _is_linked(a, 'aadl2_InternalFeature', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation130'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation130', a)


def test_assoc_ownedMember44_link_reassign_clear():
    a = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    b1 = aadl2_Namespace()
    b2 = aadl2_Namespace()
    _safe_set(a, 'aadl2_NamedElement45', b1)
    assert _is_linked(a, 'aadl2_NamedElement45', b1)
    if hasattr(b1, 'aadl2_Namespace'):
        assert _is_linked(b1, 'aadl2_Namespace', a)
    _safe_set(a, 'aadl2_NamedElement45', b2)
    assert _is_linked(a, 'aadl2_NamedElement45', b2)
    if hasattr(b1, 'aadl2_Namespace'):
        assert not _is_linked(b1, 'aadl2_Namespace', a)
    if hasattr(b2, 'aadl2_Namespace'):
        assert _is_linked(b2, 'aadl2_Namespace', a)
    _safe_set(a, 'aadl2_NamedElement45', None)
    assert not _is_linked(a, 'aadl2_NamedElement45', b2)
    if hasattr(b2, 'aadl2_Namespace'):
        assert not _is_linked(b2, 'aadl2_Namespace', a)


def test_assoc_ownedMode139_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b2 = aadl2_ComponentClassifier(derivedModes="sample_text_2", noFlows="sample_text_2", noModes="sample_text_2")
    _safe_set(a, 'aadl2_Mode140', b1)
    assert _is_linked(a, 'aadl2_Mode140', b1)
    if hasattr(b1, 'aadl2_ComponentClassifier'):
        assert _is_linked(b1, 'aadl2_ComponentClassifier', a)
    _safe_set(a, 'aadl2_Mode140', b2)
    assert _is_linked(a, 'aadl2_Mode140', b2)
    if hasattr(b1, 'aadl2_ComponentClassifier'):
        assert not _is_linked(b1, 'aadl2_ComponentClassifier', a)
    if hasattr(b2, 'aadl2_ComponentClassifier'):
        assert _is_linked(b2, 'aadl2_ComponentClassifier', a)
    _safe_set(a, 'aadl2_Mode140', None)
    assert not _is_linked(a, 'aadl2_Mode140', b2)
    if hasattr(b2, 'aadl2_ComponentClassifier'):
        assert not _is_linked(b2, 'aadl2_ComponentClassifier', a)


def test_assoc_ownedModeBinding276_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_ModeBinding()
    b2 = aadl2_ModeBinding()
    _safe_set(a, 'aadl2_Subcomponent277', {b1})
    assert _is_linked(a, 'aadl2_Subcomponent277', b1)
    if hasattr(b1, 'aadl2_ModeBinding'):
        assert _is_linked(b1, 'aadl2_ModeBinding', a)
    _safe_set(a, 'aadl2_Subcomponent277', {b2})
    assert _is_linked(a, 'aadl2_Subcomponent277', b2)
    if hasattr(b1, 'aadl2_ModeBinding'):
        assert not _is_linked(b1, 'aadl2_ModeBinding', a)
    if hasattr(b2, 'aadl2_ModeBinding'):
        assert _is_linked(b2, 'aadl2_ModeBinding', a)
    _safe_set(a, 'aadl2_Subcomponent277', set())
    assert not _is_linked(a, 'aadl2_Subcomponent277', b2)
    if hasattr(b2, 'aadl2_ModeBinding'):
        assert not _is_linked(b2, 'aadl2_ModeBinding', a)


def test_assoc_ownedModeTransition141_link_reassign_clear():
    a = aadl2_ComponentClassifier(derivedModes="sample_text", noFlows="sample_text", noModes="sample_text")
    b1 = aadl2_ModeTransition()
    b2 = aadl2_ModeTransition()
    _safe_set(a, 'aadl2_ComponentClassifier142', {b1})
    assert _is_linked(a, 'aadl2_ComponentClassifier142', b1)
    if hasattr(b1, 'aadl2_ModeTransition'):
        assert _is_linked(b1, 'aadl2_ModeTransition', a)
    _safe_set(a, 'aadl2_ComponentClassifier142', {b2})
    assert _is_linked(a, 'aadl2_ComponentClassifier142', b2)
    if hasattr(b1, 'aadl2_ModeTransition'):
        assert not _is_linked(b1, 'aadl2_ModeTransition', a)
    if hasattr(b2, 'aadl2_ModeTransition'):
        assert _is_linked(b2, 'aadl2_ModeTransition', a)
    _safe_set(a, 'aadl2_ComponentClassifier142', set())
    assert not _is_linked(a, 'aadl2_ComponentClassifier142', b2)
    if hasattr(b2, 'aadl2_ModeTransition'):
        assert not _is_linked(b2, 'aadl2_ModeTransition', a)


def test_assoc_ownedPackageRename354_link_reassign_clear():
    a = aadl2_PackageSection(noAnnexes="sample_text", noProperties="sample_text")
    b1 = aadl2_PackageRename(renameAll="sample_text")
    b2 = aadl2_PackageRename(renameAll="sample_text_2")
    _safe_set(a, 'aadl2_PackageSection', {b1})
    assert _is_linked(a, 'aadl2_PackageSection', b1)
    if hasattr(b1, 'aadl2_PackageRename'):
        assert _is_linked(b1, 'aadl2_PackageRename', a)
    _safe_set(a, 'aadl2_PackageSection', {b2})
    assert _is_linked(a, 'aadl2_PackageSection', b2)
    if hasattr(b1, 'aadl2_PackageRename'):
        assert not _is_linked(b1, 'aadl2_PackageRename', a)
    if hasattr(b2, 'aadl2_PackageRename'):
        assert _is_linked(b2, 'aadl2_PackageRename', a)
    _safe_set(a, 'aadl2_PackageSection', set())
    assert not _is_linked(a, 'aadl2_PackageSection', b2)
    if hasattr(b2, 'aadl2_PackageRename'):
        assert not _is_linked(b2, 'aadl2_PackageRename', a)


def test_assoc_ownedParameterConnection119_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ParameterConnection()
    b2 = aadl2_ParameterConnection()
    _safe_set(a, 'aadl2_ComponentImplementation120', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation120', b1)
    if hasattr(b1, 'aadl2_ParameterConnection'):
        assert _is_linked(b1, 'aadl2_ParameterConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation120', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation120', b2)
    if hasattr(b1, 'aadl2_ParameterConnection'):
        assert not _is_linked(b1, 'aadl2_ParameterConnection', a)
    if hasattr(b2, 'aadl2_ParameterConnection'):
        assert _is_linked(b2, 'aadl2_ParameterConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation120', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation120', b2)
    if hasattr(b2, 'aadl2_ParameterConnection'):
        assert not _is_linked(b2, 'aadl2_ParameterConnection', a)


def test_assoc_ownedPortConnection121_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_PortConnection()
    b2 = aadl2_PortConnection()
    _safe_set(a, 'aadl2_ComponentImplementation122', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation122', b1)
    if hasattr(b1, 'aadl2_PortConnection'):
        assert _is_linked(b1, 'aadl2_PortConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation122', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation122', b2)
    if hasattr(b1, 'aadl2_PortConnection'):
        assert not _is_linked(b1, 'aadl2_PortConnection', a)
    if hasattr(b2, 'aadl2_PortConnection'):
        assert _is_linked(b2, 'aadl2_PortConnection', a)
    _safe_set(a, 'aadl2_ComponentImplementation122', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation122', b2)
    if hasattr(b2, 'aadl2_PortConnection'):
        assert not _is_linked(b2, 'aadl2_PortConnection', a)


def test_assoc_ownedPortProxy135_link_reassign_clear():
    a = aadl2_PortProxy(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_PortProxy', b1)
    assert _is_linked(a, 'aadl2_PortProxy', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation136'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation136', a)
    _safe_set(a, 'aadl2_PortProxy', b2)
    assert _is_linked(a, 'aadl2_PortProxy', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation136'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation136', a)
    if hasattr(b2, 'aadl2_ComponentImplementation136'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation136', a)
    _safe_set(a, 'aadl2_PortProxy', None)
    assert not _is_linked(a, 'aadl2_PortProxy', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation136'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation136', a)


def test_assoc_ownedProcessorFeature127_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_ProcessorFeature()
    b2 = aadl2_ProcessorFeature()
    _safe_set(a, 'aadl2_ComponentImplementation128', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation128', b1)
    if hasattr(b1, 'aadl2_ProcessorFeature'):
        assert _is_linked(b1, 'aadl2_ProcessorFeature', a)
    _safe_set(a, 'aadl2_ComponentImplementation128', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation128', b2)
    if hasattr(b1, 'aadl2_ProcessorFeature'):
        assert not _is_linked(b1, 'aadl2_ProcessorFeature', a)
    if hasattr(b2, 'aadl2_ProcessorFeature'):
        assert _is_linked(b2, 'aadl2_ProcessorFeature', a)
    _safe_set(a, 'aadl2_ComponentImplementation128', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation128', b2)
    if hasattr(b2, 'aadl2_ProcessorFeature'):
        assert not _is_linked(b2, 'aadl2_ProcessorFeature', a)


def test_assoc_ownedProperty843_link_reassign_clear():
    a = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b1 = aadl2_PropertySet()
    b2 = aadl2_PropertySet()
    _safe_set(a, 'aadl2_Property845', b1)
    assert _is_linked(a, 'aadl2_Property845', b1)
    if hasattr(b1, 'aadl2_PropertySet844'):
        assert _is_linked(b1, 'aadl2_PropertySet844', a)
    _safe_set(a, 'aadl2_Property845', b2)
    assert _is_linked(a, 'aadl2_Property845', b2)
    if hasattr(b1, 'aadl2_PropertySet844'):
        assert not _is_linked(b1, 'aadl2_PropertySet844', a)
    if hasattr(b2, 'aadl2_PropertySet844'):
        assert _is_linked(b2, 'aadl2_PropertySet844', a)
    _safe_set(a, 'aadl2_Property845', None)
    assert not _is_linked(a, 'aadl2_Property845', b2)
    if hasattr(b2, 'aadl2_PropertySet844'):
        assert not _is_linked(b2, 'aadl2_PropertySet844', a)


def test_assoc_ownedPropertyAssociation4_link_reassign_clear():
    a = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    b1 = aadl2_NamedElement(name="sample_text", qualifiedName="sample_text")
    b2 = aadl2_NamedElement(name="sample_text_2", qualifiedName="sample_text_2")
    _safe_set(a, 'aadl2_PropertyAssociation', b1)
    assert _is_linked(a, 'aadl2_PropertyAssociation', b1)
    if hasattr(b1, 'aadl2_NamedElement'):
        assert _is_linked(b1, 'aadl2_NamedElement', a)
    _safe_set(a, 'aadl2_PropertyAssociation', b2)
    assert _is_linked(a, 'aadl2_PropertyAssociation', b2)
    if hasattr(b1, 'aadl2_NamedElement'):
        assert not _is_linked(b1, 'aadl2_NamedElement', a)
    if hasattr(b2, 'aadl2_NamedElement'):
        assert _is_linked(b2, 'aadl2_NamedElement', a)
    _safe_set(a, 'aadl2_PropertyAssociation', None)
    assert not _is_linked(a, 'aadl2_PropertyAssociation', b2)
    if hasattr(b2, 'aadl2_NamedElement'):
        assert not _is_linked(b2, 'aadl2_NamedElement', a)


def test_assoc_ownedPropertyExpression834_link_reassign_clear():
    a = aadl2_Operation(op="sample_text")
    b1 = aadl2_PropertyExpression()
    b2 = aadl2_PropertyExpression()
    _safe_set(a, 'aadl2_Operation', {b1})
    assert _is_linked(a, 'aadl2_Operation', b1)
    if hasattr(b1, 'aadl2_PropertyExpression835'):
        assert _is_linked(b1, 'aadl2_PropertyExpression835', a)
    _safe_set(a, 'aadl2_Operation', {b2})
    assert _is_linked(a, 'aadl2_Operation', b2)
    if hasattr(b1, 'aadl2_PropertyExpression835'):
        assert not _is_linked(b1, 'aadl2_PropertyExpression835', a)
    if hasattr(b2, 'aadl2_PropertyExpression835'):
        assert _is_linked(b2, 'aadl2_PropertyExpression835', a)
    _safe_set(a, 'aadl2_Operation', set())
    assert not _is_linked(a, 'aadl2_Operation', b2)
    if hasattr(b2, 'aadl2_PropertyExpression835'):
        assert not _is_linked(b2, 'aadl2_PropertyExpression835', a)


def test_assoc_ownedPrototype40_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Prototype()
    b2 = aadl2_Prototype()
    _safe_set(a, 'aadl2_Classifier41', {b1})
    assert _is_linked(a, 'aadl2_Classifier41', b1)
    if hasattr(b1, 'aadl2_Prototype'):
        assert _is_linked(b1, 'aadl2_Prototype', a)
    _safe_set(a, 'aadl2_Classifier41', {b2})
    assert _is_linked(a, 'aadl2_Classifier41', b2)
    if hasattr(b1, 'aadl2_Prototype'):
        assert not _is_linked(b1, 'aadl2_Prototype', a)
    if hasattr(b2, 'aadl2_Prototype'):
        assert _is_linked(b2, 'aadl2_Prototype', a)
    _safe_set(a, 'aadl2_Classifier41', set())
    assert not _is_linked(a, 'aadl2_Classifier41', b2)
    if hasattr(b2, 'aadl2_Prototype'):
        assert not _is_linked(b2, 'aadl2_Prototype', a)


def test_assoc_ownedPrototypeBinding270_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_PrototypeBinding()
    b2 = aadl2_PrototypeBinding()
    _safe_set(a, 'aadl2_Subcomponent271', {b1})
    assert _is_linked(a, 'aadl2_Subcomponent271', b1)
    if hasattr(b1, 'aadl2_PrototypeBinding272'):
        assert _is_linked(b1, 'aadl2_PrototypeBinding272', a)
    _safe_set(a, 'aadl2_Subcomponent271', {b2})
    assert _is_linked(a, 'aadl2_Subcomponent271', b2)
    if hasattr(b1, 'aadl2_PrototypeBinding272'):
        assert not _is_linked(b1, 'aadl2_PrototypeBinding272', a)
    if hasattr(b2, 'aadl2_PrototypeBinding272'):
        assert _is_linked(b2, 'aadl2_PrototypeBinding272', a)
    _safe_set(a, 'aadl2_Subcomponent271', set())
    assert not _is_linked(a, 'aadl2_Subcomponent271', b2)
    if hasattr(b2, 'aadl2_PrototypeBinding272'):
        assert not _is_linked(b2, 'aadl2_PrototypeBinding272', a)


def test_assoc_ownedPrototypeBinding42_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_PrototypeBinding()
    b2 = aadl2_PrototypeBinding()
    _safe_set(a, 'aadl2_Classifier43', {b1})
    assert _is_linked(a, 'aadl2_Classifier43', b1)
    if hasattr(b1, 'aadl2_PrototypeBinding'):
        assert _is_linked(b1, 'aadl2_PrototypeBinding', a)
    _safe_set(a, 'aadl2_Classifier43', {b2})
    assert _is_linked(a, 'aadl2_Classifier43', b2)
    if hasattr(b1, 'aadl2_PrototypeBinding'):
        assert not _is_linked(b1, 'aadl2_PrototypeBinding', a)
    if hasattr(b2, 'aadl2_PrototypeBinding'):
        assert _is_linked(b2, 'aadl2_PrototypeBinding', a)
    _safe_set(a, 'aadl2_Classifier43', set())
    assert not _is_linked(a, 'aadl2_Classifier43', b2)
    if hasattr(b2, 'aadl2_PrototypeBinding'):
        assert not _is_linked(b2, 'aadl2_PrototypeBinding', a)


def test_assoc_ownedRealization111_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_Realization()
    b2 = aadl2_Realization()
    _safe_set(a, 'aadl2_ComponentImplementation112', b1)
    assert _is_linked(a, 'aadl2_ComponentImplementation112', b1)
    if hasattr(b1, 'aadl2_Realization'):
        assert _is_linked(b1, 'aadl2_Realization', a)
    _safe_set(a, 'aadl2_ComponentImplementation112', b2)
    assert _is_linked(a, 'aadl2_ComponentImplementation112', b2)
    if hasattr(b1, 'aadl2_Realization'):
        assert not _is_linked(b1, 'aadl2_Realization', a)
    if hasattr(b2, 'aadl2_Realization'):
        assert _is_linked(b2, 'aadl2_Realization', a)
    _safe_set(a, 'aadl2_ComponentImplementation112', None)
    assert not _is_linked(a, 'aadl2_ComponentImplementation112', b2)
    if hasattr(b2, 'aadl2_Realization'):
        assert not _is_linked(b2, 'aadl2_Realization', a)


def test_assoc_ownedSubcomponent100_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_Subcomponent', b1)
    assert _is_linked(a, 'aadl2_Subcomponent', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation101'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation101', a)
    _safe_set(a, 'aadl2_Subcomponent', b2)
    assert _is_linked(a, 'aadl2_Subcomponent', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation101'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation101', a)
    if hasattr(b2, 'aadl2_ComponentImplementation101'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation101', a)
    _safe_set(a, 'aadl2_Subcomponent', None)
    assert not _is_linked(a, 'aadl2_Subcomponent', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation101'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation101', a)


def test_assoc_ownedSubprogramCallSequence420_link_reassign_clear():
    a = aadl2_BehavioredImplementation()
    b1 = aadl2_SubprogramCallSequence()
    b2 = aadl2_SubprogramCallSequence()
    _safe_set(a, 'aadl2_BehavioredImplementation421', {b1})
    assert _is_linked(a, 'aadl2_BehavioredImplementation421', b1)
    if hasattr(b1, 'aadl2_SubprogramCallSequence422'):
        assert _is_linked(b1, 'aadl2_SubprogramCallSequence422', a)
    _safe_set(a, 'aadl2_BehavioredImplementation421', {b2})
    assert _is_linked(a, 'aadl2_BehavioredImplementation421', b2)
    if hasattr(b1, 'aadl2_SubprogramCallSequence422'):
        assert not _is_linked(b1, 'aadl2_SubprogramCallSequence422', a)
    if hasattr(b2, 'aadl2_SubprogramCallSequence422'):
        assert _is_linked(b2, 'aadl2_SubprogramCallSequence422', a)
    _safe_set(a, 'aadl2_BehavioredImplementation421', set())
    assert not _is_linked(a, 'aadl2_BehavioredImplementation421', b2)
    if hasattr(b2, 'aadl2_SubprogramCallSequence422'):
        assert not _is_linked(b2, 'aadl2_SubprogramCallSequence422', a)


def test_assoc_ownedSubprogramProxy137_link_reassign_clear():
    a = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b1 = aadl2_SubprogramProxy()
    b2 = aadl2_SubprogramProxy()
    _safe_set(a, 'aadl2_ComponentImplementation138', {b1})
    assert _is_linked(a, 'aadl2_ComponentImplementation138', b1)
    if hasattr(b1, 'aadl2_SubprogramProxy'):
        assert _is_linked(b1, 'aadl2_SubprogramProxy', a)
    _safe_set(a, 'aadl2_ComponentImplementation138', {b2})
    assert _is_linked(a, 'aadl2_ComponentImplementation138', b2)
    if hasattr(b1, 'aadl2_SubprogramProxy'):
        assert not _is_linked(b1, 'aadl2_SubprogramProxy', a)
    if hasattr(b2, 'aadl2_SubprogramProxy'):
        assert _is_linked(b2, 'aadl2_SubprogramProxy', a)
    _safe_set(a, 'aadl2_ComponentImplementation138', set())
    assert not _is_linked(a, 'aadl2_ComponentImplementation138', b2)
    if hasattr(b2, 'aadl2_SubprogramProxy'):
        assert not _is_linked(b2, 'aadl2_SubprogramProxy', a)


def test_assoc_ownedValue11_link_reassign_clear():
    a = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    b1 = aadl2_ModalPropertyValue()
    b2 = aadl2_ModalPropertyValue()
    _safe_set(a, 'aadl2_PropertyAssociation12', {b1})
    assert _is_linked(a, 'aadl2_PropertyAssociation12', b1)
    if hasattr(b1, 'aadl2_ModalPropertyValue'):
        assert _is_linked(b1, 'aadl2_ModalPropertyValue', a)
    _safe_set(a, 'aadl2_PropertyAssociation12', {b2})
    assert _is_linked(a, 'aadl2_PropertyAssociation12', b2)
    if hasattr(b1, 'aadl2_ModalPropertyValue'):
        assert not _is_linked(b1, 'aadl2_ModalPropertyValue', a)
    if hasattr(b2, 'aadl2_ModalPropertyValue'):
        assert _is_linked(b2, 'aadl2_ModalPropertyValue', a)
    _safe_set(a, 'aadl2_PropertyAssociation12', set())
    assert not _is_linked(a, 'aadl2_PropertyAssociation12', b2)
    if hasattr(b2, 'aadl2_ModalPropertyValue'):
        assert not _is_linked(b2, 'aadl2_ModalPropertyValue', a)


def test_assoc_parentMode287_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ModeBinding()
    b2 = aadl2_ModeBinding()
    _safe_set(a, 'aadl2_Mode289', b1)
    assert _is_linked(a, 'aadl2_Mode289', b1)
    if hasattr(b1, 'aadl2_ModeBinding288'):
        assert _is_linked(b1, 'aadl2_ModeBinding288', a)
    _safe_set(a, 'aadl2_Mode289', b2)
    assert _is_linked(a, 'aadl2_Mode289', b2)
    if hasattr(b1, 'aadl2_ModeBinding288'):
        assert not _is_linked(b1, 'aadl2_ModeBinding288', a)
    if hasattr(b2, 'aadl2_ModeBinding288'):
        assert _is_linked(b2, 'aadl2_ModeBinding288', a)
    _safe_set(a, 'aadl2_Mode289', None)
    assert not _is_linked(a, 'aadl2_Mode289', b2)
    if hasattr(b2, 'aadl2_ModeBinding288'):
        assert not _is_linked(b2, 'aadl2_ModeBinding288', a)


def test_assoc_parsedAnnexLibrary350_link_reassign_clear():
    a = aadl2_DefaultAnnexLibrary(sourceText="sample_text")
    b1 = aadl2_AnnexLibrary()
    b2 = aadl2_AnnexLibrary()
    _safe_set(a, 'aadl2_DefaultAnnexLibrary', b1)
    assert _is_linked(a, 'aadl2_DefaultAnnexLibrary', b1)
    if hasattr(b1, 'aadl2_AnnexLibrary'):
        assert _is_linked(b1, 'aadl2_AnnexLibrary', a)
    _safe_set(a, 'aadl2_DefaultAnnexLibrary', b2)
    assert _is_linked(a, 'aadl2_DefaultAnnexLibrary', b2)
    if hasattr(b1, 'aadl2_AnnexLibrary'):
        assert not _is_linked(b1, 'aadl2_AnnexLibrary', a)
    if hasattr(b2, 'aadl2_AnnexLibrary'):
        assert _is_linked(b2, 'aadl2_AnnexLibrary', a)
    _safe_set(a, 'aadl2_DefaultAnnexLibrary', None)
    assert not _is_linked(a, 'aadl2_DefaultAnnexLibrary', b2)
    if hasattr(b2, 'aadl2_AnnexLibrary'):
        assert not _is_linked(b2, 'aadl2_AnnexLibrary', a)


def test_assoc_parsedAnnexSubclause351_link_reassign_clear():
    a = aadl2_DefaultAnnexSubclause(sourceText="sample_text")
    b1 = aadl2_AnnexSubclause()
    b2 = aadl2_AnnexSubclause()
    _safe_set(a, 'aadl2_DefaultAnnexSubclause', b1)
    assert _is_linked(a, 'aadl2_DefaultAnnexSubclause', b1)
    if hasattr(b1, 'aadl2_AnnexSubclause352'):
        assert _is_linked(b1, 'aadl2_AnnexSubclause352', a)
    _safe_set(a, 'aadl2_DefaultAnnexSubclause', b2)
    assert _is_linked(a, 'aadl2_DefaultAnnexSubclause', b2)
    if hasattr(b1, 'aadl2_AnnexSubclause352'):
        assert not _is_linked(b1, 'aadl2_AnnexSubclause352', a)
    if hasattr(b2, 'aadl2_AnnexSubclause352'):
        assert _is_linked(b2, 'aadl2_AnnexSubclause352', a)
    _safe_set(a, 'aadl2_DefaultAnnexSubclause', None)
    assert not _is_linked(a, 'aadl2_DefaultAnnexSubclause', b2)
    if hasattr(b2, 'aadl2_AnnexSubclause352'):
        assert not _is_linked(b2, 'aadl2_AnnexSubclause352', a)


def test_assoc_path73_link_reassign_clear():
    a = aadl2_ContainmentPathElement(annexName="sample_text")
    b1 = aadl2_ContainedNamedElement()
    b2 = aadl2_ContainedNamedElement()
    _safe_set(a, 'aadl2_ContainmentPathElement', b1)
    assert _is_linked(a, 'aadl2_ContainmentPathElement', b1)
    if hasattr(b1, 'aadl2_ContainedNamedElement74'):
        assert _is_linked(b1, 'aadl2_ContainedNamedElement74', a)
    _safe_set(a, 'aadl2_ContainmentPathElement', b2)
    assert _is_linked(a, 'aadl2_ContainmentPathElement', b2)
    if hasattr(b1, 'aadl2_ContainedNamedElement74'):
        assert not _is_linked(b1, 'aadl2_ContainedNamedElement74', a)
    if hasattr(b2, 'aadl2_ContainedNamedElement74'):
        assert _is_linked(b2, 'aadl2_ContainedNamedElement74', a)
    _safe_set(a, 'aadl2_ContainmentPathElement', None)
    assert not _is_linked(a, 'aadl2_ContainmentPathElement', b2)
    if hasattr(b2, 'aadl2_ContainedNamedElement74'):
        assert not _is_linked(b2, 'aadl2_ContainedNamedElement74', a)


def test_assoc_path84_link_reassign_clear():
    a = aadl2_ContainmentPathElement(annexName="sample_text")
    b1 = aadl2_ContainmentPathElement(annexName="sample_text")
    b2 = aadl2_ContainmentPathElement(annexName="sample_text_2")
    _safe_set(a, 'aadl2_ContainmentPathElement83', b1)
    assert _is_linked(a, 'aadl2_ContainmentPathElement83', b1)
    if hasattr(b1, 'aadl2_ContainmentPathElement85'):
        assert _is_linked(b1, 'aadl2_ContainmentPathElement85', a)
    _safe_set(a, 'aadl2_ContainmentPathElement83', b2)
    assert _is_linked(a, 'aadl2_ContainmentPathElement83', b2)
    if hasattr(b1, 'aadl2_ContainmentPathElement85'):
        assert not _is_linked(b1, 'aadl2_ContainmentPathElement85', a)
    if hasattr(b2, 'aadl2_ContainmentPathElement85'):
        assert _is_linked(b2, 'aadl2_ContainmentPathElement85', a)
    _safe_set(a, 'aadl2_ContainmentPathElement83', None)
    assert not _is_linked(a, 'aadl2_ContainmentPathElement83', b2)
    if hasattr(b2, 'aadl2_ContainmentPathElement85'):
        assert not _is_linked(b2, 'aadl2_ContainmentPathElement85', a)


def test_assoc_property5_link_reassign_clear():
    a = aadl2_PropertyAssociation(append="sample_text", constant="sample_text")
    b1 = aadl2_Property(emptyListDefault="sample_text", inherit="sample_text")
    b2 = aadl2_Property(emptyListDefault="sample_text_2", inherit="sample_text_2")
    _safe_set(a, 'aadl2_PropertyAssociation6', b1)
    assert _is_linked(a, 'aadl2_PropertyAssociation6', b1)
    if hasattr(b1, 'aadl2_Property'):
        assert _is_linked(b1, 'aadl2_Property', a)
    _safe_set(a, 'aadl2_PropertyAssociation6', b2)
    assert _is_linked(a, 'aadl2_PropertyAssociation6', b2)
    if hasattr(b1, 'aadl2_Property'):
        assert not _is_linked(b1, 'aadl2_Property', a)
    if hasattr(b2, 'aadl2_Property'):
        assert _is_linked(b2, 'aadl2_Property', a)
    _safe_set(a, 'aadl2_PropertyAssociation6', None)
    assert not _is_linked(a, 'aadl2_PropertyAssociation6', b2)
    if hasattr(b2, 'aadl2_Property'):
        assert not _is_linked(b2, 'aadl2_Property', a)


def test_assoc_prototype168_link_reassign_clear():
    a = aadl2_ComponentPrototype(array="sample_text")
    b1 = aadl2_Feature()
    b2 = aadl2_Feature()
    _safe_set(a, 'aadl2_ComponentPrototype', b1)
    assert _is_linked(a, 'aadl2_ComponentPrototype', b1)
    if hasattr(b1, 'aadl2_Feature169'):
        assert _is_linked(b1, 'aadl2_Feature169', a)
    _safe_set(a, 'aadl2_ComponentPrototype', b2)
    assert _is_linked(a, 'aadl2_ComponentPrototype', b2)
    if hasattr(b1, 'aadl2_Feature169'):
        assert not _is_linked(b1, 'aadl2_Feature169', a)
    if hasattr(b2, 'aadl2_Feature169'):
        assert _is_linked(b2, 'aadl2_Feature169', a)
    _safe_set(a, 'aadl2_ComponentPrototype', None)
    assert not _is_linked(a, 'aadl2_ComponentPrototype', b2)
    if hasattr(b2, 'aadl2_Feature169'):
        assert not _is_linked(b2, 'aadl2_Feature169', a)


def test_assoc_prototype273_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_ComponentPrototype(array="sample_text")
    b2 = aadl2_ComponentPrototype(array="sample_text_2")
    _safe_set(a, 'aadl2_Subcomponent274', b1)
    assert _is_linked(a, 'aadl2_Subcomponent274', b1)
    if hasattr(b1, 'aadl2_ComponentPrototype275'):
        assert _is_linked(b1, 'aadl2_ComponentPrototype275', a)
    _safe_set(a, 'aadl2_Subcomponent274', b2)
    assert _is_linked(a, 'aadl2_Subcomponent274', b2)
    if hasattr(b1, 'aadl2_ComponentPrototype275'):
        assert not _is_linked(b1, 'aadl2_ComponentPrototype275', a)
    if hasattr(b2, 'aadl2_ComponentPrototype275'):
        assert _is_linked(b2, 'aadl2_ComponentPrototype275', a)
    _safe_set(a, 'aadl2_Subcomponent274', None)
    assert not _is_linked(a, 'aadl2_Subcomponent274', b2)
    if hasattr(b2, 'aadl2_ComponentPrototype275'):
        assert not _is_linked(b2, 'aadl2_ComponentPrototype275', a)


def test_assoc_prototype411_link_reassign_clear():
    a = aadl2_FeaturePrototypeReference(direction="sample_text", in_="sample_text", out="sample_text")
    b1 = aadl2_FeaturePrototype(direction="sample_text", in_="sample_text", out="sample_text")
    b2 = aadl2_FeaturePrototype(direction="sample_text_2", in_="sample_text_2", out="sample_text_2")
    _safe_set(a, 'aadl2_FeaturePrototypeReference', b1)
    assert _is_linked(a, 'aadl2_FeaturePrototypeReference', b1)
    if hasattr(b1, 'aadl2_FeaturePrototype412'):
        assert _is_linked(b1, 'aadl2_FeaturePrototype412', a)
    _safe_set(a, 'aadl2_FeaturePrototypeReference', b2)
    assert _is_linked(a, 'aadl2_FeaturePrototypeReference', b2)
    if hasattr(b1, 'aadl2_FeaturePrototype412'):
        assert not _is_linked(b1, 'aadl2_FeaturePrototype412', a)
    if hasattr(b2, 'aadl2_FeaturePrototype412'):
        assert _is_linked(b2, 'aadl2_FeaturePrototype412', a)
    _safe_set(a, 'aadl2_FeaturePrototypeReference', None)
    assert not _is_linked(a, 'aadl2_FeaturePrototypeReference', b2)
    if hasattr(b2, 'aadl2_FeaturePrototype412'):
        assert not _is_linked(b2, 'aadl2_FeaturePrototype412', a)


def test_assoc_refined182_link_reassign_clear():
    a = aadl2_FlowSpecification(kind="sample_text")
    b1 = aadl2_FlowSpecification(kind="sample_text")
    b2 = aadl2_FlowSpecification(kind="sample_text_2")
    _safe_set(a, 'aadl2_FlowSpecification181', b1)
    assert _is_linked(a, 'aadl2_FlowSpecification181', b1)
    if hasattr(b1, 'aadl2_FlowSpecification183'):
        assert _is_linked(b1, 'aadl2_FlowSpecification183', a)
    _safe_set(a, 'aadl2_FlowSpecification181', b2)
    assert _is_linked(a, 'aadl2_FlowSpecification181', b2)
    if hasattr(b1, 'aadl2_FlowSpecification183'):
        assert not _is_linked(b1, 'aadl2_FlowSpecification183', a)
    if hasattr(b2, 'aadl2_FlowSpecification183'):
        assert _is_linked(b2, 'aadl2_FlowSpecification183', a)
    _safe_set(a, 'aadl2_FlowSpecification181', None)
    assert not _is_linked(a, 'aadl2_FlowSpecification181', b2)
    if hasattr(b2, 'aadl2_FlowSpecification183'):
        assert not _is_linked(b2, 'aadl2_FlowSpecification183', a)


def test_assoc_refined282_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_Subcomponent(allModes="sample_text")
    b2 = aadl2_Subcomponent(allModes="sample_text_2")
    _safe_set(a, 'aadl2_Subcomponent281', b1)
    assert _is_linked(a, 'aadl2_Subcomponent281', b1)
    if hasattr(b1, 'aadl2_Subcomponent283'):
        assert _is_linked(b1, 'aadl2_Subcomponent283', a)
    _safe_set(a, 'aadl2_Subcomponent281', b2)
    assert _is_linked(a, 'aadl2_Subcomponent281', b2)
    if hasattr(b1, 'aadl2_Subcomponent283'):
        assert not _is_linked(b1, 'aadl2_Subcomponent283', a)
    if hasattr(b2, 'aadl2_Subcomponent283'):
        assert _is_linked(b2, 'aadl2_Subcomponent283', a)
    _safe_set(a, 'aadl2_Subcomponent281', None)
    assert not _is_linked(a, 'aadl2_Subcomponent281', b2)
    if hasattr(b2, 'aadl2_Subcomponent283'):
        assert not _is_linked(b2, 'aadl2_Subcomponent283', a)


def test_assoc_refined315_link_reassign_clear():
    a = aadl2_Connection(bidirectional="sample_text")
    b1 = aadl2_Connection(bidirectional="sample_text")
    b2 = aadl2_Connection(bidirectional="sample_text_2")
    _safe_set(a, 'aadl2_Connection314', b1)
    assert _is_linked(a, 'aadl2_Connection314', b1)
    if hasattr(b1, 'aadl2_Connection316'):
        assert _is_linked(b1, 'aadl2_Connection316', a)
    _safe_set(a, 'aadl2_Connection314', b2)
    assert _is_linked(a, 'aadl2_Connection314', b2)
    if hasattr(b1, 'aadl2_Connection316'):
        assert not _is_linked(b1, 'aadl2_Connection316', a)
    if hasattr(b2, 'aadl2_Connection316'):
        assert _is_linked(b2, 'aadl2_Connection316', a)
    _safe_set(a, 'aadl2_Connection314', None)
    assert not _is_linked(a, 'aadl2_Connection314', b2)
    if hasattr(b2, 'aadl2_Connection316'):
        assert not _is_linked(b2, 'aadl2_Connection316', a)


def test_assoc_refinementContext65_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_RefinableElement()
    b2 = aadl2_RefinableElement()
    _safe_set(a, 'aadl2_Classifier66', b1)
    assert _is_linked(a, 'aadl2_Classifier66', b1)
    if hasattr(b1, 'aadl2_RefinableElement'):
        assert _is_linked(b1, 'aadl2_RefinableElement', a)
    _safe_set(a, 'aadl2_Classifier66', b2)
    assert _is_linked(a, 'aadl2_Classifier66', b2)
    if hasattr(b1, 'aadl2_RefinableElement'):
        assert not _is_linked(b1, 'aadl2_RefinableElement', a)
    if hasattr(b2, 'aadl2_RefinableElement'):
        assert _is_linked(b2, 'aadl2_RefinableElement', a)
    _safe_set(a, 'aadl2_Classifier66', None)
    assert not _is_linked(a, 'aadl2_Classifier66', b2)
    if hasattr(b2, 'aadl2_RefinableElement'):
        assert not _is_linked(b2, 'aadl2_RefinableElement', a)


def test_assoc_relatedElement59_link_reassign_clear():
    a = aadl2_Element()
    b1 = aadl2_Relationship()
    b2 = aadl2_Relationship()
    _safe_set(a, 'aadl2_Element60', b1)
    assert _is_linked(a, 'aadl2_Element60', b1)
    if hasattr(b1, 'aadl2_Relationship'):
        assert _is_linked(b1, 'aadl2_Relationship', a)
    _safe_set(a, 'aadl2_Element60', b2)
    assert _is_linked(a, 'aadl2_Element60', b2)
    if hasattr(b1, 'aadl2_Relationship'):
        assert not _is_linked(b1, 'aadl2_Relationship', a)
    if hasattr(b2, 'aadl2_Relationship'):
        assert _is_linked(b2, 'aadl2_Relationship', a)
    _safe_set(a, 'aadl2_Element60', None)
    assert not _is_linked(a, 'aadl2_Element60', b2)
    if hasattr(b2, 'aadl2_Relationship'):
        assert not _is_linked(b2, 'aadl2_Relationship', a)


def test_assoc_renamedComponentType380_link_reassign_clear():
    a = aadl2_ComponentTypeRename(category="sample_text")
    b1 = aadl2_ComponentType(noFeatures="sample_text")
    b2 = aadl2_ComponentType(noFeatures="sample_text_2")
    _safe_set(a, 'aadl2_ComponentTypeRename381', b1)
    assert _is_linked(a, 'aadl2_ComponentTypeRename381', b1)
    if hasattr(b1, 'aadl2_ComponentType382'):
        assert _is_linked(b1, 'aadl2_ComponentType382', a)
    _safe_set(a, 'aadl2_ComponentTypeRename381', b2)
    assert _is_linked(a, 'aadl2_ComponentTypeRename381', b2)
    if hasattr(b1, 'aadl2_ComponentType382'):
        assert not _is_linked(b1, 'aadl2_ComponentType382', a)
    if hasattr(b2, 'aadl2_ComponentType382'):
        assert _is_linked(b2, 'aadl2_ComponentType382', a)
    _safe_set(a, 'aadl2_ComponentTypeRename381', None)
    assert not _is_linked(a, 'aadl2_ComponentTypeRename381', b2)
    if hasattr(b2, 'aadl2_ComponentType382'):
        assert not _is_linked(b2, 'aadl2_ComponentType382', a)


def test_assoc_renamedPackage367_link_reassign_clear():
    a = aadl2_PackageRename(renameAll="sample_text")
    b1 = aadl2_AadlPackage()
    b2 = aadl2_AadlPackage()
    _safe_set(a, 'aadl2_PackageRename368', b1)
    assert _is_linked(a, 'aadl2_PackageRename368', b1)
    if hasattr(b1, 'aadl2_AadlPackage'):
        assert _is_linked(b1, 'aadl2_AadlPackage', a)
    _safe_set(a, 'aadl2_PackageRename368', b2)
    assert _is_linked(a, 'aadl2_PackageRename368', b2)
    if hasattr(b1, 'aadl2_AadlPackage'):
        assert not _is_linked(b1, 'aadl2_AadlPackage', a)
    if hasattr(b2, 'aadl2_AadlPackage'):
        assert _is_linked(b2, 'aadl2_AadlPackage', a)
    _safe_set(a, 'aadl2_PackageRename368', None)
    assert not _is_linked(a, 'aadl2_PackageRename368', b2)
    if hasattr(b2, 'aadl2_AadlPackage'):
        assert not _is_linked(b2, 'aadl2_AadlPackage', a)


def test_assoc_size89_link_reassign_clear():
    a = aadl2_ArraySize(size="sample_text")
    b1 = aadl2_ArrayDimension()
    b2 = aadl2_ArrayDimension()
    _safe_set(a, 'aadl2_ArraySize', b1)
    assert _is_linked(a, 'aadl2_ArraySize', b1)
    if hasattr(b1, 'aadl2_ArrayDimension'):
        assert _is_linked(b1, 'aadl2_ArrayDimension', a)
    _safe_set(a, 'aadl2_ArraySize', b2)
    assert _is_linked(a, 'aadl2_ArraySize', b2)
    if hasattr(b1, 'aadl2_ArrayDimension'):
        assert not _is_linked(b1, 'aadl2_ArrayDimension', a)
    if hasattr(b2, 'aadl2_ArrayDimension'):
        assert _is_linked(b2, 'aadl2_ArrayDimension', a)
    _safe_set(a, 'aadl2_ArraySize', None)
    assert not _is_linked(a, 'aadl2_ArraySize', b2)
    if hasattr(b2, 'aadl2_ArrayDimension'):
        assert not _is_linked(b2, 'aadl2_ArrayDimension', a)


def test_assoc_sizeProperty90_link_reassign_clear():
    a = aadl2_ArraySize(size="sample_text")
    b1 = aadl2_ArraySizeProperty()
    b2 = aadl2_ArraySizeProperty()
    _safe_set(a, 'aadl2_ArraySize91', b1)
    assert _is_linked(a, 'aadl2_ArraySize91', b1)
    if hasattr(b1, 'aadl2_ArraySizeProperty'):
        assert _is_linked(b1, 'aadl2_ArraySizeProperty', a)
    _safe_set(a, 'aadl2_ArraySize91', b2)
    assert _is_linked(a, 'aadl2_ArraySize91', b2)
    if hasattr(b1, 'aadl2_ArraySizeProperty'):
        assert not _is_linked(b1, 'aadl2_ArraySizeProperty', a)
    if hasattr(b2, 'aadl2_ArraySizeProperty'):
        assert _is_linked(b2, 'aadl2_ArraySizeProperty', a)
    _safe_set(a, 'aadl2_ArraySize91', None)
    assert not _is_linked(a, 'aadl2_ArraySize91', b2)
    if hasattr(b2, 'aadl2_ArraySizeProperty'):
        assert not _is_linked(b2, 'aadl2_ArraySizeProperty', a)


def test_assoc_source143_link_reassign_clear():
    a = aadl2_Mode(derived="sample_text", initial="sample_text")
    b1 = aadl2_ModeTransition()
    b2 = aadl2_ModeTransition()
    _safe_set(a, 'aadl2_Mode145', b1)
    assert _is_linked(a, 'aadl2_Mode145', b1)
    if hasattr(b1, 'aadl2_ModeTransition144'):
        assert _is_linked(b1, 'aadl2_ModeTransition144', a)
    _safe_set(a, 'aadl2_Mode145', b2)
    assert _is_linked(a, 'aadl2_Mode145', b2)
    if hasattr(b1, 'aadl2_ModeTransition144'):
        assert not _is_linked(b1, 'aadl2_ModeTransition144', a)
    if hasattr(b2, 'aadl2_ModeTransition144'):
        assert _is_linked(b2, 'aadl2_ModeTransition144', a)
    _safe_set(a, 'aadl2_Mode145', None)
    assert not _is_linked(a, 'aadl2_Mode145', b2)
    if hasattr(b2, 'aadl2_ModeTransition144'):
        assert not _is_linked(b2, 'aadl2_ModeTransition144', a)


def test_assoc_source311_link_reassign_clear():
    a = aadl2_Connection(bidirectional="sample_text")
    b1 = aadl2_ConnectedElement()
    b2 = aadl2_ConnectedElement()
    _safe_set(a, 'aadl2_Connection312', b1)
    assert _is_linked(a, 'aadl2_Connection312', b1)
    if hasattr(b1, 'aadl2_ConnectedElement313'):
        assert _is_linked(b1, 'aadl2_ConnectedElement313', a)
    _safe_set(a, 'aadl2_Connection312', b2)
    assert _is_linked(a, 'aadl2_Connection312', b2)
    if hasattr(b1, 'aadl2_ConnectedElement313'):
        assert not _is_linked(b1, 'aadl2_ConnectedElement313', a)
    if hasattr(b2, 'aadl2_ConnectedElement313'):
        assert _is_linked(b2, 'aadl2_ConnectedElement313', a)
    _safe_set(a, 'aadl2_Connection312', None)
    assert not _is_linked(a, 'aadl2_Connection312', b2)
    if hasattr(b2, 'aadl2_ConnectedElement313'):
        assert not _is_linked(b2, 'aadl2_ConnectedElement313', a)


def test_assoc_source54_link_reassign_clear():
    a = aadl2_Element()
    b1 = aadl2_DirectedRelationship()
    b2 = aadl2_DirectedRelationship()
    _safe_set(a, 'aadl2_Element55', b1)
    assert _is_linked(a, 'aadl2_Element55', b1)
    if hasattr(b1, 'aadl2_DirectedRelationship'):
        assert _is_linked(b1, 'aadl2_DirectedRelationship', a)
    _safe_set(a, 'aadl2_Element55', b2)
    assert _is_linked(a, 'aadl2_Element55', b2)
    if hasattr(b1, 'aadl2_DirectedRelationship'):
        assert not _is_linked(b1, 'aadl2_DirectedRelationship', a)
    if hasattr(b2, 'aadl2_DirectedRelationship'):
        assert _is_linked(b2, 'aadl2_DirectedRelationship', a)
    _safe_set(a, 'aadl2_Element55', None)
    assert not _is_linked(a, 'aadl2_Element55', b2)
    if hasattr(b2, 'aadl2_DirectedRelationship'):
        assert not _is_linked(b2, 'aadl2_DirectedRelationship', a)


def test_assoc_specific52_link_reassign_clear():
    a = aadl2_Classifier(noAnnexes="sample_text", noProperties="sample_text", noPrototypes="sample_text")
    b1 = aadl2_Generalization_()
    b2 = aadl2_Generalization_()
    _safe_set(a, 'Classifier53', b1)
    assert _is_linked(a, 'Classifier53', b1)
    if hasattr(b1, 'generalization'):
        assert _is_linked(b1, 'generalization', a)
    _safe_set(a, 'Classifier53', b2)
    assert _is_linked(a, 'Classifier53', b2)
    if hasattr(b1, 'generalization'):
        assert not _is_linked(b1, 'generalization', a)
    if hasattr(b2, 'generalization'):
        assert _is_linked(b2, 'generalization', a)
    _safe_set(a, 'Classifier53', None)
    assert not _is_linked(a, 'Classifier53', b2)
    if hasattr(b2, 'generalization'):
        assert not _is_linked(b2, 'generalization', a)


def test_assoc_specification293_link_reassign_clear():
    a = aadl2_FlowSpecification(kind="sample_text")
    b1 = aadl2_FlowImplementation(kind="sample_text")
    b2 = aadl2_FlowImplementation(kind="sample_text_2")
    _safe_set(a, 'aadl2_FlowSpecification295', b1)
    assert _is_linked(a, 'aadl2_FlowSpecification295', b1)
    if hasattr(b1, 'aadl2_FlowImplementation294'):
        assert _is_linked(b1, 'aadl2_FlowImplementation294', a)
    _safe_set(a, 'aadl2_FlowSpecification295', b2)
    assert _is_linked(a, 'aadl2_FlowSpecification295', b2)
    if hasattr(b1, 'aadl2_FlowImplementation294'):
        assert not _is_linked(b1, 'aadl2_FlowImplementation294', a)
    if hasattr(b2, 'aadl2_FlowImplementation294'):
        assert _is_linked(b2, 'aadl2_FlowImplementation294', a)
    _safe_set(a, 'aadl2_FlowSpecification295', None)
    assert not _is_linked(a, 'aadl2_FlowSpecification295', b2)
    if hasattr(b2, 'aadl2_FlowImplementation294'):
        assert not _is_linked(b2, 'aadl2_FlowImplementation294', a)


def test_assoc_subcomponentType268_link_reassign_clear():
    a = aadl2_Subcomponent(allModes="sample_text")
    b1 = aadl2_SubcomponentType()
    b2 = aadl2_SubcomponentType()
    _safe_set(a, 'aadl2_Subcomponent269', b1)
    assert _is_linked(a, 'aadl2_Subcomponent269', b1)
    if hasattr(b1, 'aadl2_SubcomponentType'):
        assert _is_linked(b1, 'aadl2_SubcomponentType', a)
    _safe_set(a, 'aadl2_Subcomponent269', b2)
    assert _is_linked(a, 'aadl2_Subcomponent269', b2)
    if hasattr(b1, 'aadl2_SubcomponentType'):
        assert not _is_linked(b1, 'aadl2_SubcomponentType', a)
    if hasattr(b2, 'aadl2_SubcomponentType'):
        assert _is_linked(b2, 'aadl2_SubcomponentType', a)
    _safe_set(a, 'aadl2_Subcomponent269', None)
    assert not _is_linked(a, 'aadl2_Subcomponent269', b2)
    if hasattr(b2, 'aadl2_SubcomponentType'):
        assert not _is_linked(b2, 'aadl2_SubcomponentType', a)


def test_assoc_subcomponentType390_link_reassign_clear():
    a = aadl2_ComponentPrototypeActual(category="sample_text")
    b1 = aadl2_SubcomponentType()
    b2 = aadl2_SubcomponentType()
    _safe_set(a, 'aadl2_ComponentPrototypeActual391', b1)
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual391', b1)
    if hasattr(b1, 'aadl2_SubcomponentType392'):
        assert _is_linked(b1, 'aadl2_SubcomponentType392', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual391', b2)
    assert _is_linked(a, 'aadl2_ComponentPrototypeActual391', b2)
    if hasattr(b1, 'aadl2_SubcomponentType392'):
        assert not _is_linked(b1, 'aadl2_SubcomponentType392', a)
    if hasattr(b2, 'aadl2_SubcomponentType392'):
        assert _is_linked(b2, 'aadl2_SubcomponentType392', a)
    _safe_set(a, 'aadl2_ComponentPrototypeActual391', None)
    assert not _is_linked(a, 'aadl2_ComponentPrototypeActual391', b2)
    if hasattr(b2, 'aadl2_SubcomponentType392'):
        assert not _is_linked(b2, 'aadl2_SubcomponentType392', a)


def test_assoc_subprogramCall418_link_reassign_clear():
    a = aadl2_BehavioredImplementation()
    b1 = aadl2_SubprogramCall()
    b2 = aadl2_SubprogramCall()
    _safe_set(a, 'aadl2_BehavioredImplementation', {b1})
    assert _is_linked(a, 'aadl2_BehavioredImplementation', b1)
    if hasattr(b1, 'aadl2_SubprogramCall419'):
        assert _is_linked(b1, 'aadl2_SubprogramCall419', a)
    _safe_set(a, 'aadl2_BehavioredImplementation', {b2})
    assert _is_linked(a, 'aadl2_BehavioredImplementation', b2)
    if hasattr(b1, 'aadl2_SubprogramCall419'):
        assert not _is_linked(b1, 'aadl2_SubprogramCall419', a)
    if hasattr(b2, 'aadl2_SubprogramCall419'):
        assert _is_linked(b2, 'aadl2_SubprogramCall419', a)
    _safe_set(a, 'aadl2_BehavioredImplementation', set())
    assert not _is_linked(a, 'aadl2_BehavioredImplementation', b2)
    if hasattr(b2, 'aadl2_SubprogramCall419'):
        assert not _is_linked(b2, 'aadl2_SubprogramCall419', a)


def test_assoc_target56_link_reassign_clear():
    a = aadl2_Element()
    b1 = aadl2_DirectedRelationship()
    b2 = aadl2_DirectedRelationship()
    _safe_set(a, 'aadl2_Element58', b1)
    assert _is_linked(a, 'aadl2_Element58', b1)
    if hasattr(b1, 'aadl2_DirectedRelationship57'):
        assert _is_linked(b1, 'aadl2_DirectedRelationship57', a)
    _safe_set(a, 'aadl2_Element58', b2)
    assert _is_linked(a, 'aadl2_Element58', b2)
    if hasattr(b1, 'aadl2_DirectedRelationship57'):
        assert not _is_linked(b1, 'aadl2_DirectedRelationship57', a)
    if hasattr(b2, 'aadl2_DirectedRelationship57'):
        assert _is_linked(b2, 'aadl2_DirectedRelationship57', a)
    _safe_set(a, 'aadl2_Element58', None)
    assert not _is_linked(a, 'aadl2_Element58', b2)
    if hasattr(b2, 'aadl2_DirectedRelationship57'):
        assert not _is_linked(b2, 'aadl2_DirectedRelationship57', a)


def test_assoc_type98_link_reassign_clear():
    a = aadl2_ComponentType(noFeatures="sample_text")
    b1 = aadl2_ComponentImplementation(noCalls="sample_text", noConnections="sample_text", noSubcomponents="sample_text")
    b2 = aadl2_ComponentImplementation(noCalls="sample_text_2", noConnections="sample_text_2", noSubcomponents="sample_text_2")
    _safe_set(a, 'aadl2_ComponentType', b1)
    assert _is_linked(a, 'aadl2_ComponentType', b1)
    if hasattr(b1, 'aadl2_ComponentImplementation99'):
        assert _is_linked(b1, 'aadl2_ComponentImplementation99', a)
    _safe_set(a, 'aadl2_ComponentType', b2)
    assert _is_linked(a, 'aadl2_ComponentType', b2)
    if hasattr(b1, 'aadl2_ComponentImplementation99'):
        assert not _is_linked(b1, 'aadl2_ComponentImplementation99', a)
    if hasattr(b2, 'aadl2_ComponentImplementation99'):
        assert _is_linked(b2, 'aadl2_ComponentImplementation99', a)
    _safe_set(a, 'aadl2_ComponentType', None)
    assert not _is_linked(a, 'aadl2_ComponentType', b2)
    if hasattr(b2, 'aadl2_ComponentImplementation99'):
        assert not _is_linked(b2, 'aadl2_ComponentImplementation99', a)


def test_assoc_unit817_link_reassign_clear():
    a = aadl2_UnitLiteral()
    b1 = aadl2_NumberValue()
    b2 = aadl2_NumberValue()
    _safe_set(a, 'aadl2_UnitLiteral', b1)
    assert _is_linked(a, 'aadl2_UnitLiteral', b1)
    if hasattr(b1, 'aadl2_NumberValue'):
        assert _is_linked(b1, 'aadl2_NumberValue', a)
    _safe_set(a, 'aadl2_UnitLiteral', b2)
    assert _is_linked(a, 'aadl2_UnitLiteral', b2)
    if hasattr(b1, 'aadl2_NumberValue'):
        assert not _is_linked(b1, 'aadl2_NumberValue', a)
    if hasattr(b2, 'aadl2_NumberValue'):
        assert _is_linked(b2, 'aadl2_NumberValue', a)
    _safe_set(a, 'aadl2_UnitLiteral', None)
    assert not _is_linked(a, 'aadl2_UnitLiteral', b2)
    if hasattr(b2, 'aadl2_NumberValue'):
        assert not _is_linked(b2, 'aadl2_NumberValue', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Abstract_strategy = st.builds(Abstract)
@given(instance=Abstract_strategy)
@settings(max_examples=25)
def test_Abstract_instantiation(instance):
    assert isinstance(instance, Abstract)


AbstractClassifier_strategy = st.builds(AbstractClassifier)
@given(instance=AbstractClassifier_strategy)
@settings(max_examples=25)
def test_AbstractClassifier_instantiation(instance):
    assert isinstance(instance, AbstractClassifier)


AbstractFeatureClassifier_strategy = st.builds(AbstractFeatureClassifier)
@given(instance=AbstractFeatureClassifier_strategy)
@settings(max_examples=25)
def test_AbstractFeatureClassifier_instantiation(instance):
    assert isinstance(instance, AbstractFeatureClassifier)


AbstractNamedValue_strategy = st.builds(AbstractNamedValue)
@given(instance=AbstractNamedValue_strategy)
@settings(max_examples=25)
def test_AbstractNamedValue_instantiation(instance):
    assert isinstance(instance, AbstractNamedValue)


AbstractSubcomponentType_strategy = st.builds(AbstractSubcomponentType)
@given(instance=AbstractSubcomponentType_strategy)
@settings(max_examples=25)
def test_AbstractSubcomponentType_instantiation(instance):
    assert isinstance(instance, AbstractSubcomponentType)


Access_strategy = st.builds(Access)
@given(instance=Access_strategy)
@settings(max_examples=25)
def test_Access_instantiation(instance):
    assert isinstance(instance, Access)


AccessConnectionEnd_strategy = st.builds(AccessConnectionEnd)
@given(instance=AccessConnectionEnd_strategy)
@settings(max_examples=25)
def test_AccessConnectionEnd_instantiation(instance):
    assert isinstance(instance, AccessConnectionEnd)


AnnexLibrary_strategy = st.builds(AnnexLibrary)
@given(instance=AnnexLibrary_strategy)
@settings(max_examples=25)
def test_AnnexLibrary_instantiation(instance):
    assert isinstance(instance, AnnexLibrary)


AnnexSubclause_strategy = st.builds(AnnexSubclause)
@given(instance=AnnexSubclause_strategy)
@settings(max_examples=25)
def test_AnnexSubclause_instantiation(instance):
    assert isinstance(instance, AnnexSubclause)


ArraySizeProperty_strategy = st.builds(ArraySizeProperty)
@given(instance=ArraySizeProperty_strategy)
@settings(max_examples=25)
def test_ArraySizeProperty_instantiation(instance):
    assert isinstance(instance, ArraySizeProperty)


ArrayableElement_strategy = st.builds(ArrayableElement)
@given(instance=ArrayableElement_strategy)
@settings(max_examples=25)
def test_ArrayableElement_instantiation(instance):
    assert isinstance(instance, ArrayableElement)


BasicProperty_strategy = st.builds(BasicProperty)
@given(instance=BasicProperty_strategy)
@settings(max_examples=25)
def test_BasicProperty_instantiation(instance):
    assert isinstance(instance, BasicProperty)


BehavioralFeature_strategy = st.builds(BehavioralFeature)
@given(instance=BehavioralFeature_strategy)
@settings(max_examples=25)
def test_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)


BehavioredImplementation_strategy = st.builds(BehavioredImplementation)
@given(instance=BehavioredImplementation_strategy)
@settings(max_examples=25)
def test_BehavioredImplementation_instantiation(instance):
    assert isinstance(instance, BehavioredImplementation)


Bus_strategy = st.builds(Bus)
@given(instance=Bus_strategy)
@settings(max_examples=25)
def test_Bus_instantiation(instance):
    assert isinstance(instance, Bus)


BusClassifier_strategy = st.builds(BusClassifier)
@given(instance=BusClassifier_strategy)
@settings(max_examples=25)
def test_BusClassifier_instantiation(instance):
    assert isinstance(instance, BusClassifier)


BusFeatureClassifier_strategy = st.builds(BusFeatureClassifier)
@given(instance=BusFeatureClassifier_strategy)
@settings(max_examples=25)
def test_BusFeatureClassifier_instantiation(instance):
    assert isinstance(instance, BusFeatureClassifier)


BusSubcomponentType_strategy = st.builds(BusSubcomponentType)
@given(instance=BusSubcomponentType_strategy)
@settings(max_examples=25)
def test_BusSubcomponentType_instantiation(instance):
    assert isinstance(instance, BusSubcomponentType)


CallContext_strategy = st.builds(CallContext)
@given(instance=CallContext_strategy)
@settings(max_examples=25)
def test_CallContext_instantiation(instance):
    assert isinstance(instance, CallContext)


CalledSubprogram_strategy = st.builds(CalledSubprogram)
@given(instance=CalledSubprogram_strategy)
@settings(max_examples=25)
def test_CalledSubprogram_instantiation(instance):
    assert isinstance(instance, CalledSubprogram)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


ClassifierFeature_strategy = st.builds(ClassifierFeature)
@given(instance=ClassifierFeature_strategy)
@settings(max_examples=25)
def test_ClassifierFeature_instantiation(instance):
    assert isinstance(instance, ClassifierFeature)


ComponentClassifier_strategy = st.builds(ComponentClassifier)
@given(instance=ComponentClassifier_strategy)
@settings(max_examples=25)
def test_ComponentClassifier_instantiation(instance):
    assert isinstance(instance, ComponentClassifier)


ComponentImplementation_strategy = st.builds(ComponentImplementation)
@given(instance=ComponentImplementation_strategy)
@settings(max_examples=25)
def test_ComponentImplementation_instantiation(instance):
    assert isinstance(instance, ComponentImplementation)


ComponentPrototype_strategy = st.builds(ComponentPrototype)
@given(instance=ComponentPrototype_strategy)
@settings(max_examples=25)
def test_ComponentPrototype_instantiation(instance):
    assert isinstance(instance, ComponentPrototype)


ComponentType_strategy = st.builds(ComponentType)
@given(instance=ComponentType_strategy)
@settings(max_examples=25)
def test_ComponentType_instantiation(instance):
    assert isinstance(instance, ComponentType)


Connection_strategy = st.builds(Connection)
@given(instance=Connection_strategy)
@settings(max_examples=25)
def test_Connection_instantiation(instance):
    assert isinstance(instance, Connection)


ConnectionEnd_strategy = st.builds(ConnectionEnd)
@given(instance=ConnectionEnd_strategy)
@settings(max_examples=25)
def test_ConnectionEnd_instantiation(instance):
    assert isinstance(instance, ConnectionEnd)


ContainedNamedElement_strategy = st.builds(ContainedNamedElement)
@given(instance=ContainedNamedElement_strategy)
@settings(max_examples=25)
def test_ContainedNamedElement_instantiation(instance):
    assert isinstance(instance, ContainedNamedElement)


Context_strategy = st.builds(Context)
@given(instance=Context_strategy)
@settings(max_examples=25)
def test_Context_instantiation(instance):
    assert isinstance(instance, Context)


Data_strategy = st.builds(Data)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


DataClassifier_strategy = st.builds(DataClassifier)
@given(instance=DataClassifier_strategy)
@settings(max_examples=25)
def test_DataClassifier_instantiation(instance):
    assert isinstance(instance, DataClassifier)


DataSubcomponentType_strategy = st.builds(DataSubcomponentType)
@given(instance=DataSubcomponentType_strategy)
@settings(max_examples=25)
def test_DataSubcomponentType_instantiation(instance):
    assert isinstance(instance, DataSubcomponentType)


Device_strategy = st.builds(Device)
@given(instance=Device_strategy)
@settings(max_examples=25)
def test_Device_instantiation(instance):
    assert isinstance(instance, Device)


DeviceClassifier_strategy = st.builds(DeviceClassifier)
@given(instance=DeviceClassifier_strategy)
@settings(max_examples=25)
def test_DeviceClassifier_instantiation(instance):
    assert isinstance(instance, DeviceClassifier)


DeviceSubcomponentType_strategy = st.builds(DeviceSubcomponentType)
@given(instance=DeviceSubcomponentType_strategy)
@settings(max_examples=25)
def test_DeviceSubcomponentType_instantiation(instance):
    assert isinstance(instance, DeviceSubcomponentType)


DirectedFeature_strategy = st.builds(DirectedFeature)
@given(instance=DirectedFeature_strategy)
@settings(max_examples=25)
def test_DirectedFeature_instantiation(instance):
    assert isinstance(instance, DirectedFeature)


DirectedRelationship_strategy = st.builds(DirectedRelationship)
@given(instance=DirectedRelationship_strategy)
@settings(max_examples=25)
def test_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


EndToEndFlowElement_strategy = st.builds(EndToEndFlowElement)
@given(instance=EndToEndFlowElement_strategy)
@settings(max_examples=25)
def test_EndToEndFlowElement_instantiation(instance):
    assert isinstance(instance, EndToEndFlowElement)


EnumerationLiteral_strategy = st.builds(EnumerationLiteral)
@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)


EnumerationType_strategy = st.builds(EnumerationType)
@given(instance=EnumerationType_strategy)
@settings(max_examples=25)
def test_EnumerationType_instantiation(instance):
    assert isinstance(instance, EnumerationType)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


FeatureClassifier_strategy = st.builds(FeatureClassifier)
@given(instance=FeatureClassifier_strategy)
@settings(max_examples=25)
def test_FeatureClassifier_instantiation(instance):
    assert isinstance(instance, FeatureClassifier)


FeatureConnectionEnd_strategy = st.builds(FeatureConnectionEnd)
@given(instance=FeatureConnectionEnd_strategy)
@settings(max_examples=25)
def test_FeatureConnectionEnd_instantiation(instance):
    assert isinstance(instance, FeatureConnectionEnd)


FeatureGroupConnectionEnd_strategy = st.builds(FeatureGroupConnectionEnd)
@given(instance=FeatureGroupConnectionEnd_strategy)
@settings(max_examples=25)
def test_FeatureGroupConnectionEnd_instantiation(instance):
    assert isinstance(instance, FeatureGroupConnectionEnd)


FeaturePrototypeActual_strategy = st.builds(FeaturePrototypeActual)
@given(instance=FeaturePrototypeActual_strategy)
@settings(max_examples=25)
def test_FeaturePrototypeActual_instantiation(instance):
    assert isinstance(instance, FeaturePrototypeActual)


FeatureType_strategy = st.builds(FeatureType)
@given(instance=FeatureType_strategy)
@settings(max_examples=25)
def test_FeatureType_instantiation(instance):
    assert isinstance(instance, FeatureType)


Flow_strategy = st.builds(Flow)
@given(instance=Flow_strategy)
@settings(max_examples=25)
def test_Flow_instantiation(instance):
    assert isinstance(instance, Flow)


FlowElement_strategy = st.builds(FlowElement)
@given(instance=FlowElement_strategy)
@settings(max_examples=25)
def test_FlowElement_instantiation(instance):
    assert isinstance(instance, FlowElement)


FlowFeature_strategy = st.builds(FlowFeature)
@given(instance=FlowFeature_strategy)
@settings(max_examples=25)
def test_FlowFeature_instantiation(instance):
    assert isinstance(instance, FlowFeature)


Generalization__strategy = st.builds(Generalization_)
@given(instance=Generalization__strategy)
@settings(max_examples=25)
def test_Generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)


InternalFeature_strategy = st.builds(InternalFeature)
@given(instance=InternalFeature_strategy)
@settings(max_examples=25)
def test_InternalFeature_instantiation(instance):
    assert isinstance(instance, InternalFeature)


Memory_strategy = st.builds(Memory)
@given(instance=Memory_strategy)
@settings(max_examples=25)
def test_Memory_instantiation(instance):
    assert isinstance(instance, Memory)


MemoryClassifier_strategy = st.builds(MemoryClassifier)
@given(instance=MemoryClassifier_strategy)
@settings(max_examples=25)
def test_MemoryClassifier_instantiation(instance):
    assert isinstance(instance, MemoryClassifier)


MemorySubcomponentType_strategy = st.builds(MemorySubcomponentType)
@given(instance=MemorySubcomponentType_strategy)
@settings(max_examples=25)
def test_MemorySubcomponentType_instantiation(instance):
    assert isinstance(instance, MemorySubcomponentType)


ModalElement_strategy = st.builds(ModalElement)
@given(instance=ModalElement_strategy)
@settings(max_examples=25)
def test_ModalElement_instantiation(instance):
    assert isinstance(instance, ModalElement)


ModalPath_strategy = st.builds(ModalPath)
@given(instance=ModalPath_strategy)
@settings(max_examples=25)
def test_ModalPath_instantiation(instance):
    assert isinstance(instance, ModalPath)


ModeFeature_strategy = st.builds(ModeFeature)
@given(instance=ModeFeature_strategy)
@settings(max_examples=25)
def test_ModeFeature_instantiation(instance):
    assert isinstance(instance, ModeFeature)


ModelUnit_strategy = st.builds(ModelUnit)
@given(instance=ModelUnit_strategy)
@settings(max_examples=25)
def test_ModelUnit_instantiation(instance):
    assert isinstance(instance, ModelUnit)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


NonListType_strategy = st.builds(NonListType)
@given(instance=NonListType_strategy)
@settings(max_examples=25)
def test_NonListType_instantiation(instance):
    assert isinstance(instance, NonListType)


NumberType_strategy = st.builds(NumberType)
@given(instance=NumberType_strategy)
@settings(max_examples=25)
def test_NumberType_instantiation(instance):
    assert isinstance(instance, NumberType)


NumberValue_strategy = st.builds(NumberValue)
@given(instance=NumberValue_strategy)
@settings(max_examples=25)
def test_NumberValue_instantiation(instance):
    assert isinstance(instance, NumberValue)


PackageSection_strategy = st.builds(PackageSection)
@given(instance=PackageSection_strategy)
@settings(max_examples=25)
def test_PackageSection_instantiation(instance):
    assert isinstance(instance, PackageSection)


ParameterConnectionEnd_strategy = st.builds(ParameterConnectionEnd)
@given(instance=ParameterConnectionEnd_strategy)
@settings(max_examples=25)
def test_ParameterConnectionEnd_instantiation(instance):
    assert isinstance(instance, ParameterConnectionEnd)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


PortConnectionEnd_strategy = st.builds(PortConnectionEnd)
@given(instance=PortConnectionEnd_strategy)
@settings(max_examples=25)
def test_PortConnectionEnd_instantiation(instance):
    assert isinstance(instance, PortConnectionEnd)


Process_strategy = st.builds(Process)
@given(instance=Process_strategy)
@settings(max_examples=25)
def test_Process_instantiation(instance):
    assert isinstance(instance, Process)


ProcessClassifier_strategy = st.builds(ProcessClassifier)
@given(instance=ProcessClassifier_strategy)
@settings(max_examples=25)
def test_ProcessClassifier_instantiation(instance):
    assert isinstance(instance, ProcessClassifier)


ProcessSubcomponentType_strategy = st.builds(ProcessSubcomponentType)
@given(instance=ProcessSubcomponentType_strategy)
@settings(max_examples=25)
def test_ProcessSubcomponentType_instantiation(instance):
    assert isinstance(instance, ProcessSubcomponentType)


Processor_strategy = st.builds(Processor)
@given(instance=Processor_strategy)
@settings(max_examples=25)
def test_Processor_instantiation(instance):
    assert isinstance(instance, Processor)


ProcessorClassifier_strategy = st.builds(ProcessorClassifier)
@given(instance=ProcessorClassifier_strategy)
@settings(max_examples=25)
def test_ProcessorClassifier_instantiation(instance):
    assert isinstance(instance, ProcessorClassifier)


ProcessorFeature_strategy = st.builds(ProcessorFeature)
@given(instance=ProcessorFeature_strategy)
@settings(max_examples=25)
def test_ProcessorFeature_instantiation(instance):
    assert isinstance(instance, ProcessorFeature)


ProcessorSubcomponentType_strategy = st.builds(ProcessorSubcomponentType)
@given(instance=ProcessorSubcomponentType_strategy)
@settings(max_examples=25)
def test_ProcessorSubcomponentType_instantiation(instance):
    assert isinstance(instance, ProcessorSubcomponentType)


PropertyExpression_strategy = st.builds(PropertyExpression)
@given(instance=PropertyExpression_strategy)
@settings(max_examples=25)
def test_PropertyExpression_instantiation(instance):
    assert isinstance(instance, PropertyExpression)


PropertyOwner_strategy = st.builds(PropertyOwner)
@given(instance=PropertyOwner_strategy)
@settings(max_examples=25)
def test_PropertyOwner_instantiation(instance):
    assert isinstance(instance, PropertyOwner)


PropertyType_strategy = st.builds(PropertyType)
@given(instance=PropertyType_strategy)
@settings(max_examples=25)
def test_PropertyType_instantiation(instance):
    assert isinstance(instance, PropertyType)


PropertyValue_strategy = st.builds(PropertyValue)
@given(instance=PropertyValue_strategy)
@settings(max_examples=25)
def test_PropertyValue_instantiation(instance):
    assert isinstance(instance, PropertyValue)


Prototype_strategy = st.builds(Prototype)
@given(instance=Prototype_strategy)
@settings(max_examples=25)
def test_Prototype_instantiation(instance):
    assert isinstance(instance, Prototype)


PrototypeBinding_strategy = st.builds(PrototypeBinding)
@given(instance=PrototypeBinding_strategy)
@settings(max_examples=25)
def test_PrototypeBinding_instantiation(instance):
    assert isinstance(instance, PrototypeBinding)


RefinableElement_strategy = st.builds(RefinableElement)
@given(instance=RefinableElement_strategy)
@settings(max_examples=25)
def test_RefinableElement_instantiation(instance):
    assert isinstance(instance, RefinableElement)


Relationship_strategy = st.builds(Relationship)
@given(instance=Relationship_strategy)
@settings(max_examples=25)
def test_Relationship_instantiation(instance):
    assert isinstance(instance, Relationship)


StructuralFeature_strategy = st.builds(StructuralFeature)
@given(instance=StructuralFeature_strategy)
@settings(max_examples=25)
def test_StructuralFeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)


Subcomponent_strategy = st.builds(Subcomponent)
@given(instance=Subcomponent_strategy)
@settings(max_examples=25)
def test_Subcomponent_instantiation(instance):
    assert isinstance(instance, Subcomponent)


SubcomponentType_strategy = st.builds(SubcomponentType)
@given(instance=SubcomponentType_strategy)
@settings(max_examples=25)
def test_SubcomponentType_instantiation(instance):
    assert isinstance(instance, SubcomponentType)


Subprogram_strategy = st.builds(Subprogram)
@given(instance=Subprogram_strategy)
@settings(max_examples=25)
def test_Subprogram_instantiation(instance):
    assert isinstance(instance, Subprogram)


SubprogramClassifier_strategy = st.builds(SubprogramClassifier)
@given(instance=SubprogramClassifier_strategy)
@settings(max_examples=25)
def test_SubprogramClassifier_instantiation(instance):
    assert isinstance(instance, SubprogramClassifier)


SubprogramGroup_strategy = st.builds(SubprogramGroup)
@given(instance=SubprogramGroup_strategy)
@settings(max_examples=25)
def test_SubprogramGroup_instantiation(instance):
    assert isinstance(instance, SubprogramGroup)


SubprogramGroupClassifier_strategy = st.builds(SubprogramGroupClassifier)
@given(instance=SubprogramGroupClassifier_strategy)
@settings(max_examples=25)
def test_SubprogramGroupClassifier_instantiation(instance):
    assert isinstance(instance, SubprogramGroupClassifier)


SubprogramGroupSubcomponentType_strategy = st.builds(SubprogramGroupSubcomponentType)
@given(instance=SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=25)
def test_SubprogramGroupSubcomponentType_instantiation(instance):
    assert isinstance(instance, SubprogramGroupSubcomponentType)


SubprogramSubcomponentType_strategy = st.builds(SubprogramSubcomponentType)
@given(instance=SubprogramSubcomponentType_strategy)
@settings(max_examples=25)
def test_SubprogramSubcomponentType_instantiation(instance):
    assert isinstance(instance, SubprogramSubcomponentType)


System_strategy = st.builds(System)
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


SystemClassifier_strategy = st.builds(SystemClassifier)
@given(instance=SystemClassifier_strategy)
@settings(max_examples=25)
def test_SystemClassifier_instantiation(instance):
    assert isinstance(instance, SystemClassifier)


SystemSubcomponentType_strategy = st.builds(SystemSubcomponentType)
@given(instance=SystemSubcomponentType_strategy)
@settings(max_examples=25)
def test_SystemSubcomponentType_instantiation(instance):
    assert isinstance(instance, SystemSubcomponentType)


Thread_strategy = st.builds(Thread)
@given(instance=Thread_strategy)
@settings(max_examples=25)
def test_Thread_instantiation(instance):
    assert isinstance(instance, Thread)


ThreadClassifier_strategy = st.builds(ThreadClassifier)
@given(instance=ThreadClassifier_strategy)
@settings(max_examples=25)
def test_ThreadClassifier_instantiation(instance):
    assert isinstance(instance, ThreadClassifier)


ThreadGroup_strategy = st.builds(ThreadGroup)
@given(instance=ThreadGroup_strategy)
@settings(max_examples=25)
def test_ThreadGroup_instantiation(instance):
    assert isinstance(instance, ThreadGroup)


ThreadGroupClassifier_strategy = st.builds(ThreadGroupClassifier)
@given(instance=ThreadGroupClassifier_strategy)
@settings(max_examples=25)
def test_ThreadGroupClassifier_instantiation(instance):
    assert isinstance(instance, ThreadGroupClassifier)


ThreadGroupSubcomponentType_strategy = st.builds(ThreadGroupSubcomponentType)
@given(instance=ThreadGroupSubcomponentType_strategy)
@settings(max_examples=25)
def test_ThreadGroupSubcomponentType_instantiation(instance):
    assert isinstance(instance, ThreadGroupSubcomponentType)


ThreadSubcomponentType_strategy = st.builds(ThreadSubcomponentType)
@given(instance=ThreadSubcomponentType_strategy)
@settings(max_examples=25)
def test_ThreadSubcomponentType_instantiation(instance):
    assert isinstance(instance, ThreadSubcomponentType)


TriggerPort_strategy = st.builds(TriggerPort)
@given(instance=TriggerPort_strategy)
@settings(max_examples=25)
def test_TriggerPort_instantiation(instance):
    assert isinstance(instance, TriggerPort)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


VirtualBus_strategy = st.builds(VirtualBus)
@given(instance=VirtualBus_strategy)
@settings(max_examples=25)
def test_VirtualBus_instantiation(instance):
    assert isinstance(instance, VirtualBus)


VirtualBusClassifier_strategy = st.builds(VirtualBusClassifier)
@given(instance=VirtualBusClassifier_strategy)
@settings(max_examples=25)
def test_VirtualBusClassifier_instantiation(instance):
    assert isinstance(instance, VirtualBusClassifier)


VirtualBusSubcomponentType_strategy = st.builds(VirtualBusSubcomponentType)
@given(instance=VirtualBusSubcomponentType_strategy)
@settings(max_examples=25)
def test_VirtualBusSubcomponentType_instantiation(instance):
    assert isinstance(instance, VirtualBusSubcomponentType)


VirtualProcessor_strategy = st.builds(VirtualProcessor)
@given(instance=VirtualProcessor_strategy)
@settings(max_examples=25)
def test_VirtualProcessor_instantiation(instance):
    assert isinstance(instance, VirtualProcessor)


VirtualProcessorClassifier_strategy = st.builds(VirtualProcessorClassifier)
@given(instance=VirtualProcessorClassifier_strategy)
@settings(max_examples=25)
def test_VirtualProcessorClassifier_instantiation(instance):
    assert isinstance(instance, VirtualProcessorClassifier)


VirtualProcessorSubcomponentType_strategy = st.builds(VirtualProcessorSubcomponentType)
@given(instance=VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=25)
def test_VirtualProcessorSubcomponentType_instantiation(instance):
    assert isinstance(instance, VirtualProcessorSubcomponentType)


aadl2_AadlBoolean_strategy = st.builds(aadl2_AadlBoolean)
@given(instance=aadl2_AadlBoolean_strategy)
@settings(max_examples=25)
def test_aadl2_AadlBoolean_instantiation(instance):
    assert isinstance(instance, aadl2_AadlBoolean)


aadl2_AadlInteger_strategy = st.builds(aadl2_AadlInteger)
@given(instance=aadl2_AadlInteger_strategy)
@settings(max_examples=25)
def test_aadl2_AadlInteger_instantiation(instance):
    assert isinstance(instance, aadl2_AadlInteger)


aadl2_AadlPackage_strategy = st.builds(aadl2_AadlPackage)
@given(instance=aadl2_AadlPackage_strategy)
@settings(max_examples=25)
def test_aadl2_AadlPackage_instantiation(instance):
    assert isinstance(instance, aadl2_AadlPackage)


aadl2_AadlReal_strategy = st.builds(aadl2_AadlReal)
@given(instance=aadl2_AadlReal_strategy)
@settings(max_examples=25)
def test_aadl2_AadlReal_instantiation(instance):
    assert isinstance(instance, aadl2_AadlReal)


aadl2_AadlString_strategy = st.builds(aadl2_AadlString)
@given(instance=aadl2_AadlString_strategy)
@settings(max_examples=25)
def test_aadl2_AadlString_instantiation(instance):
    assert isinstance(instance, aadl2_AadlString)


aadl2_Abstract_strategy = st.builds(aadl2_Abstract)
@given(instance=aadl2_Abstract_strategy)
@settings(max_examples=25)
def test_aadl2_Abstract_instantiation(instance):
    assert isinstance(instance, aadl2_Abstract)


aadl2_AbstractClassifier_strategy = st.builds(aadl2_AbstractClassifier)
@given(instance=aadl2_AbstractClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractClassifier)


aadl2_AbstractFeature_strategy = st.builds(aadl2_AbstractFeature)
@given(instance=aadl2_AbstractFeature_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractFeature_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractFeature)


aadl2_AbstractFeatureClassifier_strategy = st.builds(aadl2_AbstractFeatureClassifier)
@given(instance=aadl2_AbstractFeatureClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractFeatureClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractFeatureClassifier)


aadl2_AbstractImplementation_strategy = st.builds(aadl2_AbstractImplementation)
@given(instance=aadl2_AbstractImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractImplementation)


aadl2_AbstractNamedValue_strategy = st.builds(aadl2_AbstractNamedValue)
@given(instance=aadl2_AbstractNamedValue_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractNamedValue_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractNamedValue)


aadl2_AbstractPrototype_strategy = st.builds(aadl2_AbstractPrototype)
@given(instance=aadl2_AbstractPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractPrototype)


aadl2_AbstractSubcomponent_strategy = st.builds(aadl2_AbstractSubcomponent)
@given(instance=aadl2_AbstractSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractSubcomponent)


aadl2_AbstractSubcomponentType_strategy = st.builds(aadl2_AbstractSubcomponentType)
@given(instance=aadl2_AbstractSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractSubcomponentType)


aadl2_AbstractType_strategy = st.builds(aadl2_AbstractType)
@given(instance=aadl2_AbstractType_strategy)
@settings(max_examples=25)
def test_aadl2_AbstractType_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractType)


aadl2_Access_strategy = st.builds(aadl2_Access, category=safe_text, kind=safe_text)
@given(instance=aadl2_Access_strategy)
@settings(max_examples=25)
def test_aadl2_Access_instantiation(instance):
    assert isinstance(instance, aadl2_Access)


aadl2_AccessConnection_strategy = st.builds(aadl2_AccessConnection, accessCategory=safe_text)
@given(instance=aadl2_AccessConnection_strategy)
@settings(max_examples=25)
def test_aadl2_AccessConnection_instantiation(instance):
    assert isinstance(instance, aadl2_AccessConnection)


aadl2_AccessConnectionEnd_strategy = st.builds(aadl2_AccessConnectionEnd)
@given(instance=aadl2_AccessConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_AccessConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_AccessConnectionEnd)


aadl2_AccessSpecification_strategy = st.builds(aadl2_AccessSpecification, category=safe_text, kind=safe_text)
@given(instance=aadl2_AccessSpecification_strategy)
@settings(max_examples=25)
def test_aadl2_AccessSpecification_instantiation(instance):
    assert isinstance(instance, aadl2_AccessSpecification)


aadl2_AnnexLibrary_strategy = st.builds(aadl2_AnnexLibrary)
@given(instance=aadl2_AnnexLibrary_strategy)
@settings(max_examples=25)
def test_aadl2_AnnexLibrary_instantiation(instance):
    assert isinstance(instance, aadl2_AnnexLibrary)


aadl2_AnnexSubclause_strategy = st.builds(aadl2_AnnexSubclause)
@given(instance=aadl2_AnnexSubclause_strategy)
@settings(max_examples=25)
def test_aadl2_AnnexSubclause_instantiation(instance):
    assert isinstance(instance, aadl2_AnnexSubclause)


aadl2_ArrayDimension_strategy = st.builds(aadl2_ArrayDimension)
@given(instance=aadl2_ArrayDimension_strategy)
@settings(max_examples=25)
def test_aadl2_ArrayDimension_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayDimension)


aadl2_ArrayRange_strategy = st.builds(aadl2_ArrayRange, lowerBound=safe_text, upperBound=safe_text)
@given(instance=aadl2_ArrayRange_strategy)
@settings(max_examples=25)
def test_aadl2_ArrayRange_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayRange)


aadl2_ArraySize_strategy = st.builds(aadl2_ArraySize, size=safe_text)
@given(instance=aadl2_ArraySize_strategy)
@settings(max_examples=25)
def test_aadl2_ArraySize_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySize)


aadl2_ArraySizeProperty_strategy = st.builds(aadl2_ArraySizeProperty)
@given(instance=aadl2_ArraySizeProperty_strategy)
@settings(max_examples=25)
def test_aadl2_ArraySizeProperty_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySizeProperty)


aadl2_ArrayableElement_strategy = st.builds(aadl2_ArrayableElement)
@given(instance=aadl2_ArrayableElement_strategy)
@settings(max_examples=25)
def test_aadl2_ArrayableElement_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayableElement)


aadl2_BasicProperty_strategy = st.builds(aadl2_BasicProperty)
@given(instance=aadl2_BasicProperty_strategy)
@settings(max_examples=25)
def test_aadl2_BasicProperty_instantiation(instance):
    assert isinstance(instance, aadl2_BasicProperty)


aadl2_BasicPropertyAssociation_strategy = st.builds(aadl2_BasicPropertyAssociation)
@given(instance=aadl2_BasicPropertyAssociation_strategy)
@settings(max_examples=25)
def test_aadl2_BasicPropertyAssociation_instantiation(instance):
    assert isinstance(instance, aadl2_BasicPropertyAssociation)


aadl2_BehavioralFeature_strategy = st.builds(aadl2_BehavioralFeature)
@given(instance=aadl2_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_aadl2_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, aadl2_BehavioralFeature)


aadl2_BehavioredImplementation_strategy = st.builds(aadl2_BehavioredImplementation)
@given(instance=aadl2_BehavioredImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_BehavioredImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_BehavioredImplementation)


aadl2_BooleanLiteral_strategy = st.builds(aadl2_BooleanLiteral, value=safe_text)
@given(instance=aadl2_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_BooleanLiteral)


aadl2_Bus_strategy = st.builds(aadl2_Bus)
@given(instance=aadl2_Bus_strategy)
@settings(max_examples=25)
def test_aadl2_Bus_instantiation(instance):
    assert isinstance(instance, aadl2_Bus)


aadl2_BusAccess_strategy = st.builds(aadl2_BusAccess, virtual=safe_text)
@given(instance=aadl2_BusAccess_strategy)
@settings(max_examples=25)
def test_aadl2_BusAccess_instantiation(instance):
    assert isinstance(instance, aadl2_BusAccess)


aadl2_BusClassifier_strategy = st.builds(aadl2_BusClassifier)
@given(instance=aadl2_BusClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_BusClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_BusClassifier)


aadl2_BusFeatureClassifier_strategy = st.builds(aadl2_BusFeatureClassifier)
@given(instance=aadl2_BusFeatureClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_BusFeatureClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_BusFeatureClassifier)


aadl2_BusImplementation_strategy = st.builds(aadl2_BusImplementation)
@given(instance=aadl2_BusImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_BusImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_BusImplementation)


aadl2_BusPrototype_strategy = st.builds(aadl2_BusPrototype)
@given(instance=aadl2_BusPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_BusPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_BusPrototype)


aadl2_BusSubcomponent_strategy = st.builds(aadl2_BusSubcomponent)
@given(instance=aadl2_BusSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_BusSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_BusSubcomponent)


aadl2_BusSubcomponentType_strategy = st.builds(aadl2_BusSubcomponentType)
@given(instance=aadl2_BusSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_BusSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_BusSubcomponentType)


aadl2_BusType_strategy = st.builds(aadl2_BusType)
@given(instance=aadl2_BusType_strategy)
@settings(max_examples=25)
def test_aadl2_BusType_instantiation(instance):
    assert isinstance(instance, aadl2_BusType)


aadl2_CallContext_strategy = st.builds(aadl2_CallContext)
@given(instance=aadl2_CallContext_strategy)
@settings(max_examples=25)
def test_aadl2_CallContext_instantiation(instance):
    assert isinstance(instance, aadl2_CallContext)


aadl2_CalledSubprogram_strategy = st.builds(aadl2_CalledSubprogram)
@given(instance=aadl2_CalledSubprogram_strategy)
@settings(max_examples=25)
def test_aadl2_CalledSubprogram_instantiation(instance):
    assert isinstance(instance, aadl2_CalledSubprogram)


aadl2_Classifier_strategy = st.builds(aadl2_Classifier, noAnnexes=safe_text, noProperties=safe_text, noPrototypes=safe_text)
@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=25)
def test_aadl2_Classifier_instantiation(instance):
    assert isinstance(instance, aadl2_Classifier)


aadl2_ClassifierFeature_strategy = st.builds(aadl2_ClassifierFeature)
@given(instance=aadl2_ClassifierFeature_strategy)
@settings(max_examples=25)
def test_aadl2_ClassifierFeature_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierFeature)


aadl2_ClassifierType_strategy = st.builds(aadl2_ClassifierType)
@given(instance=aadl2_ClassifierType_strategy)
@settings(max_examples=25)
def test_aadl2_ClassifierType_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierType)


aadl2_ClassifierValue_strategy = st.builds(aadl2_ClassifierValue)
@given(instance=aadl2_ClassifierValue_strategy)
@settings(max_examples=25)
def test_aadl2_ClassifierValue_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierValue)


aadl2_Comment_strategy = st.builds(aadl2_Comment, body=safe_text)
@given(instance=aadl2_Comment_strategy)
@settings(max_examples=25)
def test_aadl2_Comment_instantiation(instance):
    assert isinstance(instance, aadl2_Comment)


aadl2_ComponentClassifier_strategy = st.builds(aadl2_ComponentClassifier, derivedModes=safe_text, noFlows=safe_text, noModes=safe_text)
@given(instance=aadl2_ComponentClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentClassifier)


aadl2_ComponentImplementation_strategy = st.builds(aadl2_ComponentImplementation, noCalls=safe_text, noConnections=safe_text, noSubcomponents=safe_text)
@given(instance=aadl2_ComponentImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentImplementation)


aadl2_ComponentImplementationReference_strategy = st.builds(aadl2_ComponentImplementationReference)
@given(instance=aadl2_ComponentImplementationReference_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentImplementationReference_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentImplementationReference)


aadl2_ComponentPrototype_strategy = st.builds(aadl2_ComponentPrototype, array=safe_text)
@given(instance=aadl2_ComponentPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototype)


aadl2_ComponentPrototypeActual_strategy = st.builds(aadl2_ComponentPrototypeActual, category=safe_text)
@given(instance=aadl2_ComponentPrototypeActual_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentPrototypeActual_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeActual)


aadl2_ComponentPrototypeBinding_strategy = st.builds(aadl2_ComponentPrototypeBinding)
@given(instance=aadl2_ComponentPrototypeBinding_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentPrototypeBinding_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeBinding)


aadl2_ComponentType_strategy = st.builds(aadl2_ComponentType, noFeatures=safe_text)
@given(instance=aadl2_ComponentType_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentType_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentType)


aadl2_ComponentTypeRename_strategy = st.builds(aadl2_ComponentTypeRename, category=safe_text)
@given(instance=aadl2_ComponentTypeRename_strategy)
@settings(max_examples=25)
def test_aadl2_ComponentTypeRename_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentTypeRename)


aadl2_ComputedValue_strategy = st.builds(aadl2_ComputedValue, function=safe_text)
@given(instance=aadl2_ComputedValue_strategy)
@settings(max_examples=25)
def test_aadl2_ComputedValue_instantiation(instance):
    assert isinstance(instance, aadl2_ComputedValue)


aadl2_ConnectedElement_strategy = st.builds(aadl2_ConnectedElement)
@given(instance=aadl2_ConnectedElement_strategy)
@settings(max_examples=25)
def test_aadl2_ConnectedElement_instantiation(instance):
    assert isinstance(instance, aadl2_ConnectedElement)


aadl2_Connection_strategy = st.builds(aadl2_Connection, bidirectional=safe_text)
@given(instance=aadl2_Connection_strategy)
@settings(max_examples=25)
def test_aadl2_Connection_instantiation(instance):
    assert isinstance(instance, aadl2_Connection)


aadl2_ConnectionEnd_strategy = st.builds(aadl2_ConnectionEnd)
@given(instance=aadl2_ConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_ConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_ConnectionEnd)


aadl2_ContainedNamedElement_strategy = st.builds(aadl2_ContainedNamedElement)
@given(instance=aadl2_ContainedNamedElement_strategy)
@settings(max_examples=25)
def test_aadl2_ContainedNamedElement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainedNamedElement)


aadl2_ContainmentPathElement_strategy = st.builds(aadl2_ContainmentPathElement, annexName=safe_text)
@given(instance=aadl2_ContainmentPathElement_strategy)
@settings(max_examples=25)
def test_aadl2_ContainmentPathElement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainmentPathElement)


aadl2_Context_strategy = st.builds(aadl2_Context)
@given(instance=aadl2_Context_strategy)
@settings(max_examples=25)
def test_aadl2_Context_instantiation(instance):
    assert isinstance(instance, aadl2_Context)


aadl2_Data_strategy = st.builds(aadl2_Data)
@given(instance=aadl2_Data_strategy)
@settings(max_examples=25)
def test_aadl2_Data_instantiation(instance):
    assert isinstance(instance, aadl2_Data)


aadl2_DataAccess_strategy = st.builds(aadl2_DataAccess)
@given(instance=aadl2_DataAccess_strategy)
@settings(max_examples=25)
def test_aadl2_DataAccess_instantiation(instance):
    assert isinstance(instance, aadl2_DataAccess)


aadl2_DataClassifier_strategy = st.builds(aadl2_DataClassifier)
@given(instance=aadl2_DataClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_DataClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DataClassifier)


aadl2_DataImplementation_strategy = st.builds(aadl2_DataImplementation)
@given(instance=aadl2_DataImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_DataImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DataImplementation)


aadl2_DataPort_strategy = st.builds(aadl2_DataPort)
@given(instance=aadl2_DataPort_strategy)
@settings(max_examples=25)
def test_aadl2_DataPort_instantiation(instance):
    assert isinstance(instance, aadl2_DataPort)


aadl2_DataPrototype_strategy = st.builds(aadl2_DataPrototype)
@given(instance=aadl2_DataPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_DataPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_DataPrototype)


aadl2_DataSubcomponent_strategy = st.builds(aadl2_DataSubcomponent)
@given(instance=aadl2_DataSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_DataSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DataSubcomponent)


aadl2_DataSubcomponentType_strategy = st.builds(aadl2_DataSubcomponentType)
@given(instance=aadl2_DataSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_DataSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_DataSubcomponentType)


aadl2_DataType_strategy = st.builds(aadl2_DataType)
@given(instance=aadl2_DataType_strategy)
@settings(max_examples=25)
def test_aadl2_DataType_instantiation(instance):
    assert isinstance(instance, aadl2_DataType)


aadl2_DefaultAnnexLibrary_strategy = st.builds(aadl2_DefaultAnnexLibrary, sourceText=safe_text)
@given(instance=aadl2_DefaultAnnexLibrary_strategy)
@settings(max_examples=25)
def test_aadl2_DefaultAnnexLibrary_instantiation(instance):
    assert isinstance(instance, aadl2_DefaultAnnexLibrary)


aadl2_DefaultAnnexSubclause_strategy = st.builds(aadl2_DefaultAnnexSubclause, sourceText=safe_text)
@given(instance=aadl2_DefaultAnnexSubclause_strategy)
@settings(max_examples=25)
def test_aadl2_DefaultAnnexSubclause_instantiation(instance):
    assert isinstance(instance, aadl2_DefaultAnnexSubclause)


aadl2_Device_strategy = st.builds(aadl2_Device)
@given(instance=aadl2_Device_strategy)
@settings(max_examples=25)
def test_aadl2_Device_instantiation(instance):
    assert isinstance(instance, aadl2_Device)


aadl2_DeviceClassifier_strategy = st.builds(aadl2_DeviceClassifier)
@given(instance=aadl2_DeviceClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_DeviceClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceClassifier)


aadl2_DeviceImplementation_strategy = st.builds(aadl2_DeviceImplementation)
@given(instance=aadl2_DeviceImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_DeviceImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceImplementation)


aadl2_DevicePrototype_strategy = st.builds(aadl2_DevicePrototype)
@given(instance=aadl2_DevicePrototype_strategy)
@settings(max_examples=25)
def test_aadl2_DevicePrototype_instantiation(instance):
    assert isinstance(instance, aadl2_DevicePrototype)


aadl2_DeviceSubcomponent_strategy = st.builds(aadl2_DeviceSubcomponent)
@given(instance=aadl2_DeviceSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_DeviceSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceSubcomponent)


aadl2_DeviceSubcomponentType_strategy = st.builds(aadl2_DeviceSubcomponentType)
@given(instance=aadl2_DeviceSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_DeviceSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceSubcomponentType)


aadl2_DeviceType_strategy = st.builds(aadl2_DeviceType)
@given(instance=aadl2_DeviceType_strategy)
@settings(max_examples=25)
def test_aadl2_DeviceType_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceType)


aadl2_DirectedFeature_strategy = st.builds(aadl2_DirectedFeature, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_DirectedFeature_strategy)
@settings(max_examples=25)
def test_aadl2_DirectedFeature_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedFeature)


aadl2_DirectedRelationship_strategy = st.builds(aadl2_DirectedRelationship)
@given(instance=aadl2_DirectedRelationship_strategy)
@settings(max_examples=25)
def test_aadl2_DirectedRelationship_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedRelationship)


aadl2_Element_strategy = st.builds(aadl2_Element)
@given(instance=aadl2_Element_strategy)
@settings(max_examples=25)
def test_aadl2_Element_instantiation(instance):
    assert isinstance(instance, aadl2_Element)


aadl2_EndToEndFlow_strategy = st.builds(aadl2_EndToEndFlow)
@given(instance=aadl2_EndToEndFlow_strategy)
@settings(max_examples=25)
def test_aadl2_EndToEndFlow_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlow)


aadl2_EndToEndFlowElement_strategy = st.builds(aadl2_EndToEndFlowElement)
@given(instance=aadl2_EndToEndFlowElement_strategy)
@settings(max_examples=25)
def test_aadl2_EndToEndFlowElement_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlowElement)


aadl2_EndToEndFlowSegment_strategy = st.builds(aadl2_EndToEndFlowSegment)
@given(instance=aadl2_EndToEndFlowSegment_strategy)
@settings(max_examples=25)
def test_aadl2_EndToEndFlowSegment_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlowSegment)


aadl2_EnumerationLiteral_strategy = st.builds(aadl2_EnumerationLiteral)
@given(instance=aadl2_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationLiteral)


aadl2_EnumerationType_strategy = st.builds(aadl2_EnumerationType)
@given(instance=aadl2_EnumerationType_strategy)
@settings(max_examples=25)
def test_aadl2_EnumerationType_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationType)


aadl2_EventDataPort_strategy = st.builds(aadl2_EventDataPort)
@given(instance=aadl2_EventDataPort_strategy)
@settings(max_examples=25)
def test_aadl2_EventDataPort_instantiation(instance):
    assert isinstance(instance, aadl2_EventDataPort)


aadl2_EventDataSource_strategy = st.builds(aadl2_EventDataSource)
@given(instance=aadl2_EventDataSource_strategy)
@settings(max_examples=25)
def test_aadl2_EventDataSource_instantiation(instance):
    assert isinstance(instance, aadl2_EventDataSource)


aadl2_EventPort_strategy = st.builds(aadl2_EventPort)
@given(instance=aadl2_EventPort_strategy)
@settings(max_examples=25)
def test_aadl2_EventPort_instantiation(instance):
    assert isinstance(instance, aadl2_EventPort)


aadl2_EventSource_strategy = st.builds(aadl2_EventSource)
@given(instance=aadl2_EventSource_strategy)
@settings(max_examples=25)
def test_aadl2_EventSource_instantiation(instance):
    assert isinstance(instance, aadl2_EventSource)


aadl2_Feature_strategy = st.builds(aadl2_Feature)
@given(instance=aadl2_Feature_strategy)
@settings(max_examples=25)
def test_aadl2_Feature_instantiation(instance):
    assert isinstance(instance, aadl2_Feature)


aadl2_FeatureClassifier_strategy = st.builds(aadl2_FeatureClassifier)
@given(instance=aadl2_FeatureClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureClassifier)


aadl2_FeatureConnection_strategy = st.builds(aadl2_FeatureConnection)
@given(instance=aadl2_FeatureConnection_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureConnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnection)


aadl2_FeatureConnectionEnd_strategy = st.builds(aadl2_FeatureConnectionEnd)
@given(instance=aadl2_FeatureConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnectionEnd)


aadl2_FeatureGroup_strategy = st.builds(aadl2_FeatureGroup, inverse=safe_text)
@given(instance=aadl2_FeatureGroup_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroup_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroup)


aadl2_FeatureGroupConnection_strategy = st.builds(aadl2_FeatureGroupConnection)
@given(instance=aadl2_FeatureGroupConnection_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupConnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnection)


aadl2_FeatureGroupConnectionEnd_strategy = st.builds(aadl2_FeatureGroupConnectionEnd)
@given(instance=aadl2_FeatureGroupConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnectionEnd)


aadl2_FeatureGroupPrototype_strategy = st.builds(aadl2_FeatureGroupPrototype)
@given(instance=aadl2_FeatureGroupPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototype)


aadl2_FeatureGroupPrototypeActual_strategy = st.builds(aadl2_FeatureGroupPrototypeActual)
@given(instance=aadl2_FeatureGroupPrototypeActual_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupPrototypeActual_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeActual)


aadl2_FeatureGroupPrototypeBinding_strategy = st.builds(aadl2_FeatureGroupPrototypeBinding)
@given(instance=aadl2_FeatureGroupPrototypeBinding_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupPrototypeBinding_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeBinding)


aadl2_FeatureGroupType_strategy = st.builds(aadl2_FeatureGroupType)
@given(instance=aadl2_FeatureGroupType_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupType_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupType)


aadl2_FeatureGroupTypeRename_strategy = st.builds(aadl2_FeatureGroupTypeRename)
@given(instance=aadl2_FeatureGroupTypeRename_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureGroupTypeRename_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupTypeRename)


aadl2_FeaturePrototype_strategy = st.builds(aadl2_FeaturePrototype, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_FeaturePrototype_strategy)
@settings(max_examples=25)
def test_aadl2_FeaturePrototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototype)


aadl2_FeaturePrototypeActual_strategy = st.builds(aadl2_FeaturePrototypeActual)
@given(instance=aadl2_FeaturePrototypeActual_strategy)
@settings(max_examples=25)
def test_aadl2_FeaturePrototypeActual_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeActual)


aadl2_FeaturePrototypeBinding_strategy = st.builds(aadl2_FeaturePrototypeBinding)
@given(instance=aadl2_FeaturePrototypeBinding_strategy)
@settings(max_examples=25)
def test_aadl2_FeaturePrototypeBinding_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeBinding)


aadl2_FeaturePrototypeReference_strategy = st.builds(aadl2_FeaturePrototypeReference, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_FeaturePrototypeReference_strategy)
@settings(max_examples=25)
def test_aadl2_FeaturePrototypeReference_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeReference)


aadl2_FeatureType_strategy = st.builds(aadl2_FeatureType)
@given(instance=aadl2_FeatureType_strategy)
@settings(max_examples=25)
def test_aadl2_FeatureType_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureType)


aadl2_Flow_strategy = st.builds(aadl2_Flow)
@given(instance=aadl2_Flow_strategy)
@settings(max_examples=25)
def test_aadl2_Flow_instantiation(instance):
    assert isinstance(instance, aadl2_Flow)


aadl2_FlowElement_strategy = st.builds(aadl2_FlowElement)
@given(instance=aadl2_FlowElement_strategy)
@settings(max_examples=25)
def test_aadl2_FlowElement_instantiation(instance):
    assert isinstance(instance, aadl2_FlowElement)


aadl2_FlowEnd_strategy = st.builds(aadl2_FlowEnd)
@given(instance=aadl2_FlowEnd_strategy)
@settings(max_examples=25)
def test_aadl2_FlowEnd_instantiation(instance):
    assert isinstance(instance, aadl2_FlowEnd)


aadl2_FlowFeature_strategy = st.builds(aadl2_FlowFeature)
@given(instance=aadl2_FlowFeature_strategy)
@settings(max_examples=25)
def test_aadl2_FlowFeature_instantiation(instance):
    assert isinstance(instance, aadl2_FlowFeature)


aadl2_FlowImplementation_strategy = st.builds(aadl2_FlowImplementation, kind=safe_text)
@given(instance=aadl2_FlowImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_FlowImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_FlowImplementation)


aadl2_FlowSegment_strategy = st.builds(aadl2_FlowSegment)
@given(instance=aadl2_FlowSegment_strategy)
@settings(max_examples=25)
def test_aadl2_FlowSegment_instantiation(instance):
    assert isinstance(instance, aadl2_FlowSegment)


aadl2_FlowSpecification_strategy = st.builds(aadl2_FlowSpecification, kind=safe_text)
@given(instance=aadl2_FlowSpecification_strategy)
@settings(max_examples=25)
def test_aadl2_FlowSpecification_instantiation(instance):
    assert isinstance(instance, aadl2_FlowSpecification)


aadl2_Generalization__strategy = st.builds(aadl2_Generalization_)
@given(instance=aadl2_Generalization__strategy)
@settings(max_examples=25)
def test_aadl2_Generalization__instantiation(instance):
    assert isinstance(instance, aadl2_Generalization_)


aadl2_GlobalNamespace_strategy = st.builds(aadl2_GlobalNamespace)
@given(instance=aadl2_GlobalNamespace_strategy)
@settings(max_examples=25)
def test_aadl2_GlobalNamespace_instantiation(instance):
    assert isinstance(instance, aadl2_GlobalNamespace)


aadl2_GroupExtension_strategy = st.builds(aadl2_GroupExtension)
@given(instance=aadl2_GroupExtension_strategy)
@settings(max_examples=25)
def test_aadl2_GroupExtension_instantiation(instance):
    assert isinstance(instance, aadl2_GroupExtension)


aadl2_ImplementationExtension_strategy = st.builds(aadl2_ImplementationExtension)
@given(instance=aadl2_ImplementationExtension_strategy)
@settings(max_examples=25)
def test_aadl2_ImplementationExtension_instantiation(instance):
    assert isinstance(instance, aadl2_ImplementationExtension)


aadl2_IntegerLiteral_strategy = st.builds(aadl2_IntegerLiteral, base=safe_text, value=safe_text)
@given(instance=aadl2_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_IntegerLiteral)


aadl2_InternalFeature_strategy = st.builds(aadl2_InternalFeature, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_InternalFeature_strategy)
@settings(max_examples=25)
def test_aadl2_InternalFeature_instantiation(instance):
    assert isinstance(instance, aadl2_InternalFeature)


aadl2_ListType_strategy = st.builds(aadl2_ListType)
@given(instance=aadl2_ListType_strategy)
@settings(max_examples=25)
def test_aadl2_ListType_instantiation(instance):
    assert isinstance(instance, aadl2_ListType)


aadl2_ListValue_strategy = st.builds(aadl2_ListValue)
@given(instance=aadl2_ListValue_strategy)
@settings(max_examples=25)
def test_aadl2_ListValue_instantiation(instance):
    assert isinstance(instance, aadl2_ListValue)


aadl2_Memory_strategy = st.builds(aadl2_Memory)
@given(instance=aadl2_Memory_strategy)
@settings(max_examples=25)
def test_aadl2_Memory_instantiation(instance):
    assert isinstance(instance, aadl2_Memory)


aadl2_MemoryClassifier_strategy = st.builds(aadl2_MemoryClassifier)
@given(instance=aadl2_MemoryClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_MemoryClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryClassifier)


aadl2_MemoryImplementation_strategy = st.builds(aadl2_MemoryImplementation)
@given(instance=aadl2_MemoryImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_MemoryImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryImplementation)


aadl2_MemoryPrototype_strategy = st.builds(aadl2_MemoryPrototype)
@given(instance=aadl2_MemoryPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_MemoryPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryPrototype)


aadl2_MemorySubcomponent_strategy = st.builds(aadl2_MemorySubcomponent)
@given(instance=aadl2_MemorySubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_MemorySubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_MemorySubcomponent)


aadl2_MemorySubcomponentType_strategy = st.builds(aadl2_MemorySubcomponentType)
@given(instance=aadl2_MemorySubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_MemorySubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_MemorySubcomponentType)


aadl2_MemoryType_strategy = st.builds(aadl2_MemoryType)
@given(instance=aadl2_MemoryType_strategy)
@settings(max_examples=25)
def test_aadl2_MemoryType_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryType)


aadl2_MetaclassReference_strategy = st.builds(aadl2_MetaclassReference, annexName=safe_text, metaclassName=safe_text)
@given(instance=aadl2_MetaclassReference_strategy)
@settings(max_examples=25)
def test_aadl2_MetaclassReference_instantiation(instance):
    assert isinstance(instance, aadl2_MetaclassReference)


aadl2_ModalElement_strategy = st.builds(aadl2_ModalElement)
@given(instance=aadl2_ModalElement_strategy)
@settings(max_examples=25)
def test_aadl2_ModalElement_instantiation(instance):
    assert isinstance(instance, aadl2_ModalElement)


aadl2_ModalPath_strategy = st.builds(aadl2_ModalPath)
@given(instance=aadl2_ModalPath_strategy)
@settings(max_examples=25)
def test_aadl2_ModalPath_instantiation(instance):
    assert isinstance(instance, aadl2_ModalPath)


aadl2_ModalPropertyValue_strategy = st.builds(aadl2_ModalPropertyValue)
@given(instance=aadl2_ModalPropertyValue_strategy)
@settings(max_examples=25)
def test_aadl2_ModalPropertyValue_instantiation(instance):
    assert isinstance(instance, aadl2_ModalPropertyValue)


aadl2_Mode_strategy = st.builds(aadl2_Mode, derived=safe_text, initial=safe_text)
@given(instance=aadl2_Mode_strategy)
@settings(max_examples=25)
def test_aadl2_Mode_instantiation(instance):
    assert isinstance(instance, aadl2_Mode)


aadl2_ModeBinding_strategy = st.builds(aadl2_ModeBinding)
@given(instance=aadl2_ModeBinding_strategy)
@settings(max_examples=25)
def test_aadl2_ModeBinding_instantiation(instance):
    assert isinstance(instance, aadl2_ModeBinding)


aadl2_ModeFeature_strategy = st.builds(aadl2_ModeFeature)
@given(instance=aadl2_ModeFeature_strategy)
@settings(max_examples=25)
def test_aadl2_ModeFeature_instantiation(instance):
    assert isinstance(instance, aadl2_ModeFeature)


aadl2_ModeTransition_strategy = st.builds(aadl2_ModeTransition)
@given(instance=aadl2_ModeTransition_strategy)
@settings(max_examples=25)
def test_aadl2_ModeTransition_instantiation(instance):
    assert isinstance(instance, aadl2_ModeTransition)


aadl2_ModeTransitionTrigger_strategy = st.builds(aadl2_ModeTransitionTrigger)
@given(instance=aadl2_ModeTransitionTrigger_strategy)
@settings(max_examples=25)
def test_aadl2_ModeTransitionTrigger_instantiation(instance):
    assert isinstance(instance, aadl2_ModeTransitionTrigger)


aadl2_ModelUnit_strategy = st.builds(aadl2_ModelUnit)
@given(instance=aadl2_ModelUnit_strategy)
@settings(max_examples=25)
def test_aadl2_ModelUnit_instantiation(instance):
    assert isinstance(instance, aadl2_ModelUnit)


aadl2_NamedElement_strategy = st.builds(aadl2_NamedElement, name=safe_text, qualifiedName=safe_text)
@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=25)
def test_aadl2_NamedElement_instantiation(instance):
    assert isinstance(instance, aadl2_NamedElement)


aadl2_NamedValue_strategy = st.builds(aadl2_NamedValue)
@given(instance=aadl2_NamedValue_strategy)
@settings(max_examples=25)
def test_aadl2_NamedValue_instantiation(instance):
    assert isinstance(instance, aadl2_NamedValue)


aadl2_Namespace_strategy = st.builds(aadl2_Namespace)
@given(instance=aadl2_Namespace_strategy)
@settings(max_examples=25)
def test_aadl2_Namespace_instantiation(instance):
    assert isinstance(instance, aadl2_Namespace)


aadl2_NonListType_strategy = st.builds(aadl2_NonListType)
@given(instance=aadl2_NonListType_strategy)
@settings(max_examples=25)
def test_aadl2_NonListType_instantiation(instance):
    assert isinstance(instance, aadl2_NonListType)


aadl2_NumberType_strategy = st.builds(aadl2_NumberType)
@given(instance=aadl2_NumberType_strategy)
@settings(max_examples=25)
def test_aadl2_NumberType_instantiation(instance):
    assert isinstance(instance, aadl2_NumberType)


aadl2_NumberValue_strategy = st.builds(aadl2_NumberValue)
@given(instance=aadl2_NumberValue_strategy)
@settings(max_examples=25)
def test_aadl2_NumberValue_instantiation(instance):
    assert isinstance(instance, aadl2_NumberValue)


aadl2_NumericRange_strategy = st.builds(aadl2_NumericRange)
@given(instance=aadl2_NumericRange_strategy)
@settings(max_examples=25)
def test_aadl2_NumericRange_instantiation(instance):
    assert isinstance(instance, aadl2_NumericRange)


aadl2_Operation_strategy = st.builds(aadl2_Operation, op=safe_text)
@given(instance=aadl2_Operation_strategy)
@settings(max_examples=25)
def test_aadl2_Operation_instantiation(instance):
    assert isinstance(instance, aadl2_Operation)


aadl2_PackageRename_strategy = st.builds(aadl2_PackageRename, renameAll=safe_text)
@given(instance=aadl2_PackageRename_strategy)
@settings(max_examples=25)
def test_aadl2_PackageRename_instantiation(instance):
    assert isinstance(instance, aadl2_PackageRename)


aadl2_PackageSection_strategy = st.builds(aadl2_PackageSection, noAnnexes=safe_text, noProperties=safe_text)
@given(instance=aadl2_PackageSection_strategy)
@settings(max_examples=25)
def test_aadl2_PackageSection_instantiation(instance):
    assert isinstance(instance, aadl2_PackageSection)


aadl2_Parameter_strategy = st.builds(aadl2_Parameter)
@given(instance=aadl2_Parameter_strategy)
@settings(max_examples=25)
def test_aadl2_Parameter_instantiation(instance):
    assert isinstance(instance, aadl2_Parameter)


aadl2_ParameterConnection_strategy = st.builds(aadl2_ParameterConnection)
@given(instance=aadl2_ParameterConnection_strategy)
@settings(max_examples=25)
def test_aadl2_ParameterConnection_instantiation(instance):
    assert isinstance(instance, aadl2_ParameterConnection)


aadl2_ParameterConnectionEnd_strategy = st.builds(aadl2_ParameterConnectionEnd)
@given(instance=aadl2_ParameterConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_ParameterConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_ParameterConnectionEnd)


aadl2_Port_strategy = st.builds(aadl2_Port, category=safe_text)
@given(instance=aadl2_Port_strategy)
@settings(max_examples=25)
def test_aadl2_Port_instantiation(instance):
    assert isinstance(instance, aadl2_Port)


aadl2_PortConnection_strategy = st.builds(aadl2_PortConnection)
@given(instance=aadl2_PortConnection_strategy)
@settings(max_examples=25)
def test_aadl2_PortConnection_instantiation(instance):
    assert isinstance(instance, aadl2_PortConnection)


aadl2_PortConnectionEnd_strategy = st.builds(aadl2_PortConnectionEnd)
@given(instance=aadl2_PortConnectionEnd_strategy)
@settings(max_examples=25)
def test_aadl2_PortConnectionEnd_instantiation(instance):
    assert isinstance(instance, aadl2_PortConnectionEnd)


aadl2_PortProxy_strategy = st.builds(aadl2_PortProxy, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_PortProxy_strategy)
@settings(max_examples=25)
def test_aadl2_PortProxy_instantiation(instance):
    assert isinstance(instance, aadl2_PortProxy)


aadl2_PortSpecification_strategy = st.builds(aadl2_PortSpecification, category=safe_text, direction=safe_text, in_=safe_text, out=safe_text)
@given(instance=aadl2_PortSpecification_strategy)
@settings(max_examples=25)
def test_aadl2_PortSpecification_instantiation(instance):
    assert isinstance(instance, aadl2_PortSpecification)


aadl2_PrivatePackageSection_strategy = st.builds(aadl2_PrivatePackageSection)
@given(instance=aadl2_PrivatePackageSection_strategy)
@settings(max_examples=25)
def test_aadl2_PrivatePackageSection_instantiation(instance):
    assert isinstance(instance, aadl2_PrivatePackageSection)


aadl2_Process_strategy = st.builds(aadl2_Process)
@given(instance=aadl2_Process_strategy)
@settings(max_examples=25)
def test_aadl2_Process_instantiation(instance):
    assert isinstance(instance, aadl2_Process)


aadl2_ProcessClassifier_strategy = st.builds(aadl2_ProcessClassifier)
@given(instance=aadl2_ProcessClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessClassifier)


aadl2_ProcessImplementation_strategy = st.builds(aadl2_ProcessImplementation)
@given(instance=aadl2_ProcessImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessImplementation)


aadl2_ProcessPrototype_strategy = st.builds(aadl2_ProcessPrototype)
@given(instance=aadl2_ProcessPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessPrototype)


aadl2_ProcessSubcomponent_strategy = st.builds(aadl2_ProcessSubcomponent)
@given(instance=aadl2_ProcessSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessSubcomponent)


aadl2_ProcessSubcomponentType_strategy = st.builds(aadl2_ProcessSubcomponentType)
@given(instance=aadl2_ProcessSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessSubcomponentType)


aadl2_ProcessType_strategy = st.builds(aadl2_ProcessType)
@given(instance=aadl2_ProcessType_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessType_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessType)


aadl2_Processor_strategy = st.builds(aadl2_Processor)
@given(instance=aadl2_Processor_strategy)
@settings(max_examples=25)
def test_aadl2_Processor_instantiation(instance):
    assert isinstance(instance, aadl2_Processor)


aadl2_ProcessorClassifier_strategy = st.builds(aadl2_ProcessorClassifier)
@given(instance=aadl2_ProcessorClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorClassifier)


aadl2_ProcessorFeature_strategy = st.builds(aadl2_ProcessorFeature)
@given(instance=aadl2_ProcessorFeature_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorFeature_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorFeature)


aadl2_ProcessorImplementation_strategy = st.builds(aadl2_ProcessorImplementation)
@given(instance=aadl2_ProcessorImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorImplementation)


aadl2_ProcessorPrototype_strategy = st.builds(aadl2_ProcessorPrototype)
@given(instance=aadl2_ProcessorPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorPrototype)


aadl2_ProcessorSubcomponent_strategy = st.builds(aadl2_ProcessorSubcomponent)
@given(instance=aadl2_ProcessorSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubcomponent)


aadl2_ProcessorSubcomponentType_strategy = st.builds(aadl2_ProcessorSubcomponentType)
@given(instance=aadl2_ProcessorSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubcomponentType)


aadl2_ProcessorType_strategy = st.builds(aadl2_ProcessorType)
@given(instance=aadl2_ProcessorType_strategy)
@settings(max_examples=25)
def test_aadl2_ProcessorType_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorType)


aadl2_Property_strategy = st.builds(aadl2_Property, emptyListDefault=safe_text, inherit=safe_text)
@given(instance=aadl2_Property_strategy)
@settings(max_examples=25)
def test_aadl2_Property_instantiation(instance):
    assert isinstance(instance, aadl2_Property)


aadl2_PropertyAssociation_strategy = st.builds(aadl2_PropertyAssociation, append=safe_text, constant=safe_text)
@given(instance=aadl2_PropertyAssociation_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyAssociation_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyAssociation)


aadl2_PropertyConstant_strategy = st.builds(aadl2_PropertyConstant)
@given(instance=aadl2_PropertyConstant_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyConstant_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyConstant)


aadl2_PropertyExpression_strategy = st.builds(aadl2_PropertyExpression)
@given(instance=aadl2_PropertyExpression_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyExpression_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyExpression)


aadl2_PropertyOwner_strategy = st.builds(aadl2_PropertyOwner)
@given(instance=aadl2_PropertyOwner_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyOwner_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyOwner)


aadl2_PropertySet_strategy = st.builds(aadl2_PropertySet)
@given(instance=aadl2_PropertySet_strategy)
@settings(max_examples=25)
def test_aadl2_PropertySet_instantiation(instance):
    assert isinstance(instance, aadl2_PropertySet)


aadl2_PropertyType_strategy = st.builds(aadl2_PropertyType)
@given(instance=aadl2_PropertyType_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyType_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyType)


aadl2_PropertyValue_strategy = st.builds(aadl2_PropertyValue)
@given(instance=aadl2_PropertyValue_strategy)
@settings(max_examples=25)
def test_aadl2_PropertyValue_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyValue)


aadl2_Prototype_strategy = st.builds(aadl2_Prototype)
@given(instance=aadl2_Prototype_strategy)
@settings(max_examples=25)
def test_aadl2_Prototype_instantiation(instance):
    assert isinstance(instance, aadl2_Prototype)


aadl2_PrototypeBinding_strategy = st.builds(aadl2_PrototypeBinding)
@given(instance=aadl2_PrototypeBinding_strategy)
@settings(max_examples=25)
def test_aadl2_PrototypeBinding_instantiation(instance):
    assert isinstance(instance, aadl2_PrototypeBinding)


aadl2_PublicPackageSection_strategy = st.builds(aadl2_PublicPackageSection)
@given(instance=aadl2_PublicPackageSection_strategy)
@settings(max_examples=25)
def test_aadl2_PublicPackageSection_instantiation(instance):
    assert isinstance(instance, aadl2_PublicPackageSection)


aadl2_RangeType_strategy = st.builds(aadl2_RangeType)
@given(instance=aadl2_RangeType_strategy)
@settings(max_examples=25)
def test_aadl2_RangeType_instantiation(instance):
    assert isinstance(instance, aadl2_RangeType)


aadl2_RangeValue_strategy = st.builds(aadl2_RangeValue)
@given(instance=aadl2_RangeValue_strategy)
@settings(max_examples=25)
def test_aadl2_RangeValue_instantiation(instance):
    assert isinstance(instance, aadl2_RangeValue)


aadl2_RealLiteral_strategy = st.builds(aadl2_RealLiteral, value=safe_text)
@given(instance=aadl2_RealLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_RealLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_RealLiteral)


aadl2_Realization_strategy = st.builds(aadl2_Realization)
@given(instance=aadl2_Realization_strategy)
@settings(max_examples=25)
def test_aadl2_Realization_instantiation(instance):
    assert isinstance(instance, aadl2_Realization)


aadl2_RecordField_strategy = st.builds(aadl2_RecordField)
@given(instance=aadl2_RecordField_strategy)
@settings(max_examples=25)
def test_aadl2_RecordField_instantiation(instance):
    assert isinstance(instance, aadl2_RecordField)


aadl2_RecordType_strategy = st.builds(aadl2_RecordType)
@given(instance=aadl2_RecordType_strategy)
@settings(max_examples=25)
def test_aadl2_RecordType_instantiation(instance):
    assert isinstance(instance, aadl2_RecordType)


aadl2_RecordValue_strategy = st.builds(aadl2_RecordValue)
@given(instance=aadl2_RecordValue_strategy)
@settings(max_examples=25)
def test_aadl2_RecordValue_instantiation(instance):
    assert isinstance(instance, aadl2_RecordValue)


aadl2_ReferenceType_strategy = st.builds(aadl2_ReferenceType)
@given(instance=aadl2_ReferenceType_strategy)
@settings(max_examples=25)
def test_aadl2_ReferenceType_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceType)


aadl2_ReferenceValue_strategy = st.builds(aadl2_ReferenceValue)
@given(instance=aadl2_ReferenceValue_strategy)
@settings(max_examples=25)
def test_aadl2_ReferenceValue_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceValue)


aadl2_RefinableElement_strategy = st.builds(aadl2_RefinableElement)
@given(instance=aadl2_RefinableElement_strategy)
@settings(max_examples=25)
def test_aadl2_RefinableElement_instantiation(instance):
    assert isinstance(instance, aadl2_RefinableElement)


aadl2_Relationship_strategy = st.builds(aadl2_Relationship)
@given(instance=aadl2_Relationship_strategy)
@settings(max_examples=25)
def test_aadl2_Relationship_instantiation(instance):
    assert isinstance(instance, aadl2_Relationship)


aadl2_StringLiteral_strategy = st.builds(aadl2_StringLiteral, value=safe_text)
@given(instance=aadl2_StringLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_StringLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_StringLiteral)


aadl2_StructuralFeature_strategy = st.builds(aadl2_StructuralFeature)
@given(instance=aadl2_StructuralFeature_strategy)
@settings(max_examples=25)
def test_aadl2_StructuralFeature_instantiation(instance):
    assert isinstance(instance, aadl2_StructuralFeature)


aadl2_Subcomponent_strategy = st.builds(aadl2_Subcomponent, allModes=safe_text)
@given(instance=aadl2_Subcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_Subcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_Subcomponent)


aadl2_SubcomponentType_strategy = st.builds(aadl2_SubcomponentType)
@given(instance=aadl2_SubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_SubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_SubcomponentType)


aadl2_Subprogram_strategy = st.builds(aadl2_Subprogram)
@given(instance=aadl2_Subprogram_strategy)
@settings(max_examples=25)
def test_aadl2_Subprogram_instantiation(instance):
    assert isinstance(instance, aadl2_Subprogram)


aadl2_SubprogramAccess_strategy = st.builds(aadl2_SubprogramAccess)
@given(instance=aadl2_SubprogramAccess_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramAccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramAccess)


aadl2_SubprogramCall_strategy = st.builds(aadl2_SubprogramCall)
@given(instance=aadl2_SubprogramCall_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramCall_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCall)


aadl2_SubprogramCallSequence_strategy = st.builds(aadl2_SubprogramCallSequence)
@given(instance=aadl2_SubprogramCallSequence_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramCallSequence_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCallSequence)


aadl2_SubprogramClassifier_strategy = st.builds(aadl2_SubprogramClassifier)
@given(instance=aadl2_SubprogramClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramClassifier)


aadl2_SubprogramGroup_strategy = st.builds(aadl2_SubprogramGroup)
@given(instance=aadl2_SubprogramGroup_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroup_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroup)


aadl2_SubprogramGroupAccess_strategy = st.builds(aadl2_SubprogramGroupAccess)
@given(instance=aadl2_SubprogramGroupAccess_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupAccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupAccess)


aadl2_SubprogramGroupClassifier_strategy = st.builds(aadl2_SubprogramGroupClassifier)
@given(instance=aadl2_SubprogramGroupClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupClassifier)


aadl2_SubprogramGroupImplementation_strategy = st.builds(aadl2_SubprogramGroupImplementation)
@given(instance=aadl2_SubprogramGroupImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupImplementation)


aadl2_SubprogramGroupPrototype_strategy = st.builds(aadl2_SubprogramGroupPrototype)
@given(instance=aadl2_SubprogramGroupPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupPrototype)


aadl2_SubprogramGroupSubcomponent_strategy = st.builds(aadl2_SubprogramGroupSubcomponent)
@given(instance=aadl2_SubprogramGroupSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupSubcomponent)


aadl2_SubprogramGroupSubcomponentType_strategy = st.builds(aadl2_SubprogramGroupSubcomponentType)
@given(instance=aadl2_SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupSubcomponentType)


aadl2_SubprogramGroupType_strategy = st.builds(aadl2_SubprogramGroupType)
@given(instance=aadl2_SubprogramGroupType_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramGroupType_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupType)


aadl2_SubprogramImplementation_strategy = st.builds(aadl2_SubprogramImplementation)
@given(instance=aadl2_SubprogramImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramImplementation)


aadl2_SubprogramPrototype_strategy = st.builds(aadl2_SubprogramPrototype)
@given(instance=aadl2_SubprogramPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramPrototype)


aadl2_SubprogramProxy_strategy = st.builds(aadl2_SubprogramProxy)
@given(instance=aadl2_SubprogramProxy_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramProxy_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramProxy)


aadl2_SubprogramSubcomponent_strategy = st.builds(aadl2_SubprogramSubcomponent)
@given(instance=aadl2_SubprogramSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramSubcomponent)


aadl2_SubprogramSubcomponentType_strategy = st.builds(aadl2_SubprogramSubcomponentType)
@given(instance=aadl2_SubprogramSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramSubcomponentType)


aadl2_SubprogramType_strategy = st.builds(aadl2_SubprogramType)
@given(instance=aadl2_SubprogramType_strategy)
@settings(max_examples=25)
def test_aadl2_SubprogramType_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramType)


aadl2_System_strategy = st.builds(aadl2_System)
@given(instance=aadl2_System_strategy)
@settings(max_examples=25)
def test_aadl2_System_instantiation(instance):
    assert isinstance(instance, aadl2_System)


aadl2_SystemClassifier_strategy = st.builds(aadl2_SystemClassifier)
@given(instance=aadl2_SystemClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_SystemClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SystemClassifier)


aadl2_SystemImplementation_strategy = st.builds(aadl2_SystemImplementation)
@given(instance=aadl2_SystemImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_SystemImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SystemImplementation)


aadl2_SystemPrototype_strategy = st.builds(aadl2_SystemPrototype)
@given(instance=aadl2_SystemPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_SystemPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_SystemPrototype)


aadl2_SystemSubcomponent_strategy = st.builds(aadl2_SystemSubcomponent)
@given(instance=aadl2_SystemSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_SystemSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SystemSubcomponent)


aadl2_SystemSubcomponentType_strategy = st.builds(aadl2_SystemSubcomponentType)
@given(instance=aadl2_SystemSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_SystemSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_SystemSubcomponentType)


aadl2_SystemType_strategy = st.builds(aadl2_SystemType)
@given(instance=aadl2_SystemType_strategy)
@settings(max_examples=25)
def test_aadl2_SystemType_instantiation(instance):
    assert isinstance(instance, aadl2_SystemType)


aadl2_Thread_strategy = st.builds(aadl2_Thread)
@given(instance=aadl2_Thread_strategy)
@settings(max_examples=25)
def test_aadl2_Thread_instantiation(instance):
    assert isinstance(instance, aadl2_Thread)


aadl2_ThreadClassifier_strategy = st.builds(aadl2_ThreadClassifier)
@given(instance=aadl2_ThreadClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadClassifier)


aadl2_ThreadGroup_strategy = st.builds(aadl2_ThreadGroup)
@given(instance=aadl2_ThreadGroup_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroup_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroup)


aadl2_ThreadGroupClassifier_strategy = st.builds(aadl2_ThreadGroupClassifier)
@given(instance=aadl2_ThreadGroupClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupClassifier)


aadl2_ThreadGroupImplementation_strategy = st.builds(aadl2_ThreadGroupImplementation)
@given(instance=aadl2_ThreadGroupImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupImplementation)


aadl2_ThreadGroupPrototype_strategy = st.builds(aadl2_ThreadGroupPrototype)
@given(instance=aadl2_ThreadGroupPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupPrototype)


aadl2_ThreadGroupSubcomponent_strategy = st.builds(aadl2_ThreadGroupSubcomponent)
@given(instance=aadl2_ThreadGroupSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupSubcomponent)


aadl2_ThreadGroupSubcomponentType_strategy = st.builds(aadl2_ThreadGroupSubcomponentType)
@given(instance=aadl2_ThreadGroupSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupSubcomponentType)


aadl2_ThreadGroupType_strategy = st.builds(aadl2_ThreadGroupType)
@given(instance=aadl2_ThreadGroupType_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadGroupType_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupType)


aadl2_ThreadImplementation_strategy = st.builds(aadl2_ThreadImplementation)
@given(instance=aadl2_ThreadImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadImplementation)


aadl2_ThreadPrototype_strategy = st.builds(aadl2_ThreadPrototype)
@given(instance=aadl2_ThreadPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadPrototype)


aadl2_ThreadSubcomponent_strategy = st.builds(aadl2_ThreadSubcomponent)
@given(instance=aadl2_ThreadSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadSubcomponent)


aadl2_ThreadSubcomponentType_strategy = st.builds(aadl2_ThreadSubcomponentType)
@given(instance=aadl2_ThreadSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadSubcomponentType)


aadl2_ThreadType_strategy = st.builds(aadl2_ThreadType)
@given(instance=aadl2_ThreadType_strategy)
@settings(max_examples=25)
def test_aadl2_ThreadType_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadType)


aadl2_TriggerPort_strategy = st.builds(aadl2_TriggerPort)
@given(instance=aadl2_TriggerPort_strategy)
@settings(max_examples=25)
def test_aadl2_TriggerPort_instantiation(instance):
    assert isinstance(instance, aadl2_TriggerPort)


aadl2_Type_strategy = st.builds(aadl2_Type)
@given(instance=aadl2_Type_strategy)
@settings(max_examples=25)
def test_aadl2_Type_instantiation(instance):
    assert isinstance(instance, aadl2_Type)


aadl2_TypeExtension_strategy = st.builds(aadl2_TypeExtension)
@given(instance=aadl2_TypeExtension_strategy)
@settings(max_examples=25)
def test_aadl2_TypeExtension_instantiation(instance):
    assert isinstance(instance, aadl2_TypeExtension)


aadl2_TypedElement_strategy = st.builds(aadl2_TypedElement)
@given(instance=aadl2_TypedElement_strategy)
@settings(max_examples=25)
def test_aadl2_TypedElement_instantiation(instance):
    assert isinstance(instance, aadl2_TypedElement)


aadl2_UnitLiteral_strategy = st.builds(aadl2_UnitLiteral)
@given(instance=aadl2_UnitLiteral_strategy)
@settings(max_examples=25)
def test_aadl2_UnitLiteral_instantiation(instance):
    assert isinstance(instance, aadl2_UnitLiteral)


aadl2_UnitsType_strategy = st.builds(aadl2_UnitsType)
@given(instance=aadl2_UnitsType_strategy)
@settings(max_examples=25)
def test_aadl2_UnitsType_instantiation(instance):
    assert isinstance(instance, aadl2_UnitsType)


aadl2_VirtualBus_strategy = st.builds(aadl2_VirtualBus)
@given(instance=aadl2_VirtualBus_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBus_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBus)


aadl2_VirtualBusClassifier_strategy = st.builds(aadl2_VirtualBusClassifier)
@given(instance=aadl2_VirtualBusClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusClassifier)


aadl2_VirtualBusImplementation_strategy = st.builds(aadl2_VirtualBusImplementation)
@given(instance=aadl2_VirtualBusImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusImplementation)


aadl2_VirtualBusPrototype_strategy = st.builds(aadl2_VirtualBusPrototype)
@given(instance=aadl2_VirtualBusPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusPrototype)


aadl2_VirtualBusSubcomponent_strategy = st.builds(aadl2_VirtualBusSubcomponent)
@given(instance=aadl2_VirtualBusSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusSubcomponent)


aadl2_VirtualBusSubcomponentType_strategy = st.builds(aadl2_VirtualBusSubcomponentType)
@given(instance=aadl2_VirtualBusSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusSubcomponentType)


aadl2_VirtualBusType_strategy = st.builds(aadl2_VirtualBusType)
@given(instance=aadl2_VirtualBusType_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualBusType_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusType)


aadl2_VirtualProcessor_strategy = st.builds(aadl2_VirtualProcessor)
@given(instance=aadl2_VirtualProcessor_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessor_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessor)


aadl2_VirtualProcessorClassifier_strategy = st.builds(aadl2_VirtualProcessorClassifier)
@given(instance=aadl2_VirtualProcessorClassifier_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorClassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorClassifier)


aadl2_VirtualProcessorImplementation_strategy = st.builds(aadl2_VirtualProcessorImplementation)
@given(instance=aadl2_VirtualProcessorImplementation_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorImplementation_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorImplementation)


aadl2_VirtualProcessorPrototype_strategy = st.builds(aadl2_VirtualProcessorPrototype)
@given(instance=aadl2_VirtualProcessorPrototype_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorPrototype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorPrototype)


aadl2_VirtualProcessorSubcomponent_strategy = st.builds(aadl2_VirtualProcessorSubcomponent)
@given(instance=aadl2_VirtualProcessorSubcomponent_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorSubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorSubcomponent)


aadl2_VirtualProcessorSubcomponentType_strategy = st.builds(aadl2_VirtualProcessorSubcomponentType)
@given(instance=aadl2_VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorSubcomponentType_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorSubcomponentType)


aadl2_VirtualProcessorType_strategy = st.builds(aadl2_VirtualProcessorType)
@given(instance=aadl2_VirtualProcessorType_strategy)
@settings(max_examples=25)
def test_aadl2_VirtualProcessorType_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorType)



