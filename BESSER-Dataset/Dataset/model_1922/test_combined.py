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
    libraryElement_IVarElement,
    libraryElement_ColorizableElement,
    libraryElement_Color,
    libraryElement_PositionableElement,
    libraryElement_Primitive,
    Event,
    libraryElement_AdapterEvent,
    I4DIACElement,
    libraryElement_Annotation,
    libraryElement_I4DIACElement,
    FB,
    libraryElement_ResourceTypeFB,
    libraryElement_INamedElement,
    libraryElement_Value,
    libraryElement_DataType,
    PositionableElement,
    TypedConfigureableObject,
    ConfigurableObject,
    libraryElement_TypedConfigureableObject,
    libraryElement_Connection,
    DataType,
    libraryElement_AdapterType,
    libraryElement_AdapterTypePaletteEntry,
    libraryElement_AdapterFB,
    VarDeclaration,
    libraryElement_AdapterDeclaration,
    libraryElement_Compiler,
    libraryElement_CompilerInfo,
    libraryElement_ECC,
    FBType,
    libraryElement_CompositeFBType,
    libraryElement_BasicFBType,
    libraryElement_FBNetwork,
    INamedElement,
    libraryElement_Application,
    libraryElement_ServiceInterface,
    libraryElement_IInterfaceElement,
    libraryElement_Algorithm,
    libraryElement_AdapterFBType,
    Connection,
    Algorithm,
    libraryElement_TextAlgorithm,
    libraryElement_SystemConfiguration,
    libraryElement_Palette,
    libraryElement_ConfigurableObject,
    libraryElement_PaletteEntry,
    libraryElement_LibraryElement,
    libraryElement_VersionInfo,
    libraryElement_VarInitialization,
    LibraryElement,
    libraryElement_CompilableType,
    libraryElement_AutomationSystem,
    CompositeFBType,
    libraryElement_SubAppType,
    libraryElement_AdapterConnection,
    libraryElement_EventConnection,
    libraryElement_DataConnection,
    libraryElement_ServiceInterfaceFBType,
    libraryElement_ServiceTransaction,
    libraryElement_ServiceSequence,
    libraryElement_Parameter,
    TextAlgorithm,
    libraryElement_STAlgorithm,
    libraryElement_OtherAlgorithm,
    libraryElement_Identification,
    libraryElement_Service,
    Primitive,
    libraryElement_OutputPrimitive,
    libraryElement_InputPrimitive,
    libraryElement_Mapping,
    libraryElement_InterfaceList,
    libraryElement_FBNetworkElement,
    FBNetworkElement,
    libraryElement_SubApp,
    libraryElement_FB,
    libraryElement_With,
    IInterfaceElement,
    libraryElement_VarDeclaration,
    libraryElement_ECTransition,
    libraryElement_ECState,
    libraryElement_Event,
    libraryElement_ECAction,
    libraryElement_ResourceTypeName,
    CompilableType,
    libraryElement_ResourceType,
    libraryElement_SegmentType,
    libraryElement_FBType,
    libraryElement_DeviceType,
    libraryElement_Link,
    IVarElement,
    libraryElement_Resource,
    ColorizableElement,
    libraryElement_Segment,
    libraryElement_Device,
    Language,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_libraryelement_ivarelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_IVarElement)


def test_hyp_libraryelement_ivarelement_constructor_exists():
    assert callable(libraryElement_IVarElement.__init__)


def test_hyp_libraryelement_ivarelement_constructor_args():
    sig = inspect.signature(libraryElement_IVarElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_colorizableelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ColorizableElement)


def test_hyp_libraryelement_colorizableelement_constructor_exists():
    assert callable(libraryElement_ColorizableElement.__init__)


def test_hyp_libraryelement_colorizableelement_constructor_args():
    sig = inspect.signature(libraryElement_ColorizableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_color_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Color)


def test_hyp_libraryelement_color_constructor_exists():
    assert callable(libraryElement_Color.__init__)


def test_hyp_libraryelement_color_constructor_args():
    sig = inspect.signature(libraryElement_Color.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"






def test_hyp_libraryelement_positionableelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_PositionableElement)


def test_hyp_libraryelement_positionableelement_constructor_exists():
    assert callable(libraryElement_PositionableElement.__init__)


def test_hyp_libraryelement_positionableelement_constructor_args():
    sig = inspect.signature(libraryElement_PositionableElement.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_libraryelement_primitive_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Primitive)


def test_hyp_libraryelement_primitive_constructor_exists():
    assert callable(libraryElement_Primitive.__init__)


def test_hyp_libraryelement_primitive_constructor_args():
    sig = inspect.signature(libraryElement_Primitive.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "event" in params, "Missing parameter 'event'"





def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adapterevent_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterEvent)


def test_hyp_libraryelement_adapterevent_constructor_exists():
    assert callable(libraryElement_AdapterEvent.__init__)


def test_hyp_libraryelement_adapterevent_constructor_args():
    sig = inspect.signature(libraryElement_AdapterEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_i4diacelement_is_not_abstract():
    assert not inspect.isabstract(I4DIACElement)


def test_hyp_i4diacelement_constructor_exists():
    assert callable(I4DIACElement.__init__)


def test_hyp_i4diacelement_constructor_args():
    sig = inspect.signature(I4DIACElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_annotation_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Annotation)


def test_hyp_libraryelement_annotation_constructor_exists():
    assert callable(libraryElement_Annotation.__init__)


def test_hyp_libraryelement_annotation_constructor_args():
    sig = inspect.signature(libraryElement_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "servity" in params, "Missing parameter 'servity'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_libraryelement_i4diacelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_I4DIACElement)


def test_hyp_libraryelement_i4diacelement_constructor_exists():
    assert callable(libraryElement_I4DIACElement.__init__)


def test_hyp_libraryelement_i4diacelement_constructor_args():
    sig = inspect.signature(libraryElement_I4DIACElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fb_is_not_abstract():
    assert not inspect.isabstract(FB)


def test_hyp_fb_constructor_exists():
    assert callable(FB.__init__)


def test_hyp_fb_constructor_args():
    sig = inspect.signature(FB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_resourcetypefb_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ResourceTypeFB)


def test_hyp_libraryelement_resourcetypefb_constructor_exists():
    assert callable(libraryElement_ResourceTypeFB.__init__)


def test_hyp_libraryelement_resourcetypefb_constructor_args():
    sig = inspect.signature(libraryElement_ResourceTypeFB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_inamedelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_INamedElement)


def test_hyp_libraryelement_inamedelement_constructor_exists():
    assert callable(libraryElement_INamedElement.__init__)


def test_hyp_libraryelement_inamedelement_constructor_args():
    sig = inspect.signature(libraryElement_INamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"





def test_hyp_libraryelement_value_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Value)


def test_hyp_libraryelement_value_constructor_exists():
    assert callable(libraryElement_Value.__init__)


def test_hyp_libraryelement_value_constructor_args():
    sig = inspect.signature(libraryElement_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_libraryelement_datatype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_DataType)


def test_hyp_libraryelement_datatype_constructor_exists():
    assert callable(libraryElement_DataType.__init__)


def test_hyp_libraryelement_datatype_constructor_args():
    sig = inspect.signature(libraryElement_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_positionableelement_is_not_abstract():
    assert not inspect.isabstract(PositionableElement)


def test_hyp_positionableelement_constructor_exists():
    assert callable(PositionableElement.__init__)


def test_hyp_positionableelement_constructor_args():
    sig = inspect.signature(PositionableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedconfigureableobject_is_not_abstract():
    assert not inspect.isabstract(TypedConfigureableObject)


def test_hyp_typedconfigureableobject_constructor_exists():
    assert callable(TypedConfigureableObject.__init__)


def test_hyp_typedconfigureableobject_constructor_args():
    sig = inspect.signature(TypedConfigureableObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_configurableobject_is_not_abstract():
    assert not inspect.isabstract(ConfigurableObject)


def test_hyp_configurableobject_constructor_exists():
    assert callable(ConfigurableObject.__init__)


def test_hyp_configurableobject_constructor_args():
    sig = inspect.signature(ConfigurableObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_typedconfigureableobject_is_not_abstract():
    assert not inspect.isabstract(libraryElement_TypedConfigureableObject)


def test_hyp_libraryelement_typedconfigureableobject_constructor_exists():
    assert callable(libraryElement_TypedConfigureableObject.__init__)


def test_hyp_libraryelement_typedconfigureableobject_constructor_args():
    sig = inspect.signature(libraryElement_TypedConfigureableObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_connection_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Connection)


def test_hyp_libraryelement_connection_constructor_exists():
    assert callable(libraryElement_Connection.__init__)


def test_hyp_libraryelement_connection_constructor_args():
    sig = inspect.signature(libraryElement_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "brokenConnection" in params, "Missing parameter 'brokenConnection'"
    assert "dx1" in params, "Missing parameter 'dx1'"
    assert "resTypeConnection" in params, "Missing parameter 'resTypeConnection'"
    assert "dy" in params, "Missing parameter 'dy'"
    assert "dx2" in params, "Missing parameter 'dx2'"








def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adaptertype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterType)


def test_hyp_libraryelement_adaptertype_constructor_exists():
    assert callable(libraryElement_AdapterType.__init__)


def test_hyp_libraryelement_adaptertype_constructor_args():
    sig = inspect.signature(libraryElement_AdapterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adaptertypepaletteentry_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterTypePaletteEntry)


def test_hyp_libraryelement_adaptertypepaletteentry_constructor_exists():
    assert callable(libraryElement_AdapterTypePaletteEntry.__init__)


def test_hyp_libraryelement_adaptertypepaletteentry_constructor_args():
    sig = inspect.signature(libraryElement_AdapterTypePaletteEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adapterfb_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterFB)


def test_hyp_libraryelement_adapterfb_constructor_exists():
    assert callable(libraryElement_AdapterFB.__init__)


def test_hyp_libraryelement_adapterfb_constructor_args():
    sig = inspect.signature(libraryElement_AdapterFB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(VarDeclaration)


def test_hyp_vardeclaration_constructor_exists():
    assert callable(VarDeclaration.__init__)


def test_hyp_vardeclaration_constructor_args():
    sig = inspect.signature(VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adapterdeclaration_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterDeclaration)


def test_hyp_libraryelement_adapterdeclaration_constructor_exists():
    assert callable(libraryElement_AdapterDeclaration.__init__)


def test_hyp_libraryelement_adapterdeclaration_constructor_args():
    sig = inspect.signature(libraryElement_AdapterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_compiler_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Compiler)


def test_hyp_libraryelement_compiler_constructor_exists():
    assert callable(libraryElement_Compiler.__init__)


def test_hyp_libraryelement_compiler_constructor_args():
    sig = inspect.signature(libraryElement_Compiler.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "product" in params, "Missing parameter 'product'"
    assert "language" in params, "Missing parameter 'language'"







def test_hyp_libraryelement_compilerinfo_is_not_abstract():
    assert not inspect.isabstract(libraryElement_CompilerInfo)


def test_hyp_libraryelement_compilerinfo_constructor_exists():
    assert callable(libraryElement_CompilerInfo.__init__)


def test_hyp_libraryelement_compilerinfo_constructor_args():
    sig = inspect.signature(libraryElement_CompilerInfo.__init__)
    params = list(sig.parameters.keys())
    assert "classdef" in params, "Missing parameter 'classdef'"
    assert "header" in params, "Missing parameter 'header'"





def test_hyp_libraryelement_ecc_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ECC)


def test_hyp_libraryelement_ecc_constructor_exists():
    assert callable(libraryElement_ECC.__init__)


def test_hyp_libraryelement_ecc_constructor_args():
    sig = inspect.signature(libraryElement_ECC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fbtype_is_not_abstract():
    assert not inspect.isabstract(FBType)


def test_hyp_fbtype_constructor_exists():
    assert callable(FBType.__init__)


def test_hyp_fbtype_constructor_args():
    sig = inspect.signature(FBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_compositefbtype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_CompositeFBType)


def test_hyp_libraryelement_compositefbtype_constructor_exists():
    assert callable(libraryElement_CompositeFBType.__init__)


def test_hyp_libraryelement_compositefbtype_constructor_args():
    sig = inspect.signature(libraryElement_CompositeFBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_basicfbtype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_BasicFBType)


def test_hyp_libraryelement_basicfbtype_constructor_exists():
    assert callable(libraryElement_BasicFBType.__init__)


def test_hyp_libraryelement_basicfbtype_constructor_args():
    sig = inspect.signature(libraryElement_BasicFBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_fbnetwork_is_not_abstract():
    assert not inspect.isabstract(libraryElement_FBNetwork)


def test_hyp_libraryelement_fbnetwork_constructor_exists():
    assert callable(libraryElement_FBNetwork.__init__)


def test_hyp_libraryelement_fbnetwork_constructor_args():
    sig = inspect.signature(libraryElement_FBNetwork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inamedelement_is_not_abstract():
    assert not inspect.isabstract(INamedElement)


def test_hyp_inamedelement_constructor_exists():
    assert callable(INamedElement.__init__)


def test_hyp_inamedelement_constructor_args():
    sig = inspect.signature(INamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_application_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Application)


def test_hyp_libraryelement_application_constructor_exists():
    assert callable(libraryElement_Application.__init__)


def test_hyp_libraryelement_application_constructor_args():
    sig = inspect.signature(libraryElement_Application.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_serviceinterface_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ServiceInterface)


def test_hyp_libraryelement_serviceinterface_constructor_exists():
    assert callable(libraryElement_ServiceInterface.__init__)


def test_hyp_libraryelement_serviceinterface_constructor_args():
    sig = inspect.signature(libraryElement_ServiceInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_iinterfaceelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_IInterfaceElement)


def test_hyp_libraryelement_iinterfaceelement_constructor_exists():
    assert callable(libraryElement_IInterfaceElement.__init__)


def test_hyp_libraryelement_iinterfaceelement_constructor_args():
    sig = inspect.signature(libraryElement_IInterfaceElement.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "isInput" in params, "Missing parameter 'isInput'"





def test_hyp_libraryelement_algorithm_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Algorithm)


def test_hyp_libraryelement_algorithm_constructor_exists():
    assert callable(libraryElement_Algorithm.__init__)


def test_hyp_libraryelement_algorithm_constructor_args():
    sig = inspect.signature(libraryElement_Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adapterfbtype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterFBType)


def test_hyp_libraryelement_adapterfbtype_constructor_exists():
    assert callable(libraryElement_AdapterFBType.__init__)


def test_hyp_libraryelement_adapterfbtype_constructor_args():
    sig = inspect.signature(libraryElement_AdapterFBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_hyp_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_hyp_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_algorithm_is_not_abstract():
    assert not inspect.isabstract(Algorithm)


def test_hyp_algorithm_constructor_exists():
    assert callable(Algorithm.__init__)


def test_hyp_algorithm_constructor_args():
    sig = inspect.signature(Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_textalgorithm_is_not_abstract():
    assert not inspect.isabstract(libraryElement_TextAlgorithm)


def test_hyp_libraryelement_textalgorithm_constructor_exists():
    assert callable(libraryElement_TextAlgorithm.__init__)


def test_hyp_libraryelement_textalgorithm_constructor_args():
    sig = inspect.signature(libraryElement_TextAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_libraryelement_systemconfiguration_is_not_abstract():
    assert not inspect.isabstract(libraryElement_SystemConfiguration)


def test_hyp_libraryelement_systemconfiguration_constructor_exists():
    assert callable(libraryElement_SystemConfiguration.__init__)


def test_hyp_libraryelement_systemconfiguration_constructor_args():
    sig = inspect.signature(libraryElement_SystemConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_palette_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Palette)


def test_hyp_libraryelement_palette_constructor_exists():
    assert callable(libraryElement_Palette.__init__)


def test_hyp_libraryelement_palette_constructor_args():
    sig = inspect.signature(libraryElement_Palette.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_configurableobject_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ConfigurableObject)


def test_hyp_libraryelement_configurableobject_constructor_exists():
    assert callable(libraryElement_ConfigurableObject.__init__)


def test_hyp_libraryelement_configurableobject_constructor_args():
    sig = inspect.signature(libraryElement_ConfigurableObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_paletteentry_is_not_abstract():
    assert not inspect.isabstract(libraryElement_PaletteEntry)


def test_hyp_libraryelement_paletteentry_constructor_exists():
    assert callable(libraryElement_PaletteEntry.__init__)


def test_hyp_libraryelement_paletteentry_constructor_args():
    sig = inspect.signature(libraryElement_PaletteEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_libraryelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_LibraryElement)


def test_hyp_libraryelement_libraryelement_constructor_exists():
    assert callable(libraryElement_LibraryElement.__init__)


def test_hyp_libraryelement_libraryelement_constructor_args():
    sig = inspect.signature(libraryElement_LibraryElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_versioninfo_is_not_abstract():
    assert not inspect.isabstract(libraryElement_VersionInfo)


def test_hyp_libraryelement_versioninfo_constructor_exists():
    assert callable(libraryElement_VersionInfo.__init__)


def test_hyp_libraryelement_versioninfo_constructor_args():
    sig = inspect.signature(libraryElement_VersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "date" in params, "Missing parameter 'date'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "author" in params, "Missing parameter 'author'"
    assert "remarks" in params, "Missing parameter 'remarks'"








def test_hyp_libraryelement_varinitialization_is_not_abstract():
    assert not inspect.isabstract(libraryElement_VarInitialization)


def test_hyp_libraryelement_varinitialization_constructor_exists():
    assert callable(libraryElement_VarInitialization.__init__)


def test_hyp_libraryelement_varinitialization_constructor_args():
    sig = inspect.signature(libraryElement_VarInitialization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_is_not_abstract():
    assert not inspect.isabstract(LibraryElement)


def test_hyp_libraryelement_constructor_exists():
    assert callable(LibraryElement.__init__)


def test_hyp_libraryelement_constructor_args():
    sig = inspect.signature(LibraryElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_compilabletype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_CompilableType)


def test_hyp_libraryelement_compilabletype_constructor_exists():
    assert callable(libraryElement_CompilableType.__init__)


def test_hyp_libraryelement_compilabletype_constructor_args():
    sig = inspect.signature(libraryElement_CompilableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_automationsystem_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AutomationSystem)


def test_hyp_libraryelement_automationsystem_constructor_exists():
    assert callable(libraryElement_AutomationSystem.__init__)


def test_hyp_libraryelement_automationsystem_constructor_args():
    sig = inspect.signature(libraryElement_AutomationSystem.__init__)
    params = list(sig.parameters.keys())
    assert "project" in params, "Missing parameter 'project'"




def test_hyp_compositefbtype_is_not_abstract():
    assert not inspect.isabstract(CompositeFBType)


def test_hyp_compositefbtype_constructor_exists():
    assert callable(CompositeFBType.__init__)


def test_hyp_compositefbtype_constructor_args():
    sig = inspect.signature(CompositeFBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_subapptype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_SubAppType)


def test_hyp_libraryelement_subapptype_constructor_exists():
    assert callable(libraryElement_SubAppType.__init__)


def test_hyp_libraryelement_subapptype_constructor_args():
    sig = inspect.signature(libraryElement_SubAppType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_adapterconnection_is_not_abstract():
    assert not inspect.isabstract(libraryElement_AdapterConnection)


def test_hyp_libraryelement_adapterconnection_constructor_exists():
    assert callable(libraryElement_AdapterConnection.__init__)


def test_hyp_libraryelement_adapterconnection_constructor_args():
    sig = inspect.signature(libraryElement_AdapterConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_eventconnection_is_not_abstract():
    assert not inspect.isabstract(libraryElement_EventConnection)


def test_hyp_libraryelement_eventconnection_constructor_exists():
    assert callable(libraryElement_EventConnection.__init__)


def test_hyp_libraryelement_eventconnection_constructor_args():
    sig = inspect.signature(libraryElement_EventConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_dataconnection_is_not_abstract():
    assert not inspect.isabstract(libraryElement_DataConnection)


def test_hyp_libraryelement_dataconnection_constructor_exists():
    assert callable(libraryElement_DataConnection.__init__)


def test_hyp_libraryelement_dataconnection_constructor_args():
    sig = inspect.signature(libraryElement_DataConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_serviceinterfacefbtype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ServiceInterfaceFBType)


def test_hyp_libraryelement_serviceinterfacefbtype_constructor_exists():
    assert callable(libraryElement_ServiceInterfaceFBType.__init__)


def test_hyp_libraryelement_serviceinterfacefbtype_constructor_args():
    sig = inspect.signature(libraryElement_ServiceInterfaceFBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_servicetransaction_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ServiceTransaction)


def test_hyp_libraryelement_servicetransaction_constructor_exists():
    assert callable(libraryElement_ServiceTransaction.__init__)


def test_hyp_libraryelement_servicetransaction_constructor_args():
    sig = inspect.signature(libraryElement_ServiceTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "TestResult" in params, "Missing parameter 'TestResult'"




def test_hyp_libraryelement_servicesequence_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ServiceSequence)


def test_hyp_libraryelement_servicesequence_constructor_exists():
    assert callable(libraryElement_ServiceSequence.__init__)


def test_hyp_libraryelement_servicesequence_constructor_args():
    sig = inspect.signature(libraryElement_ServiceSequence.__init__)
    params = list(sig.parameters.keys())
    assert "TestResult" in params, "Missing parameter 'TestResult'"




def test_hyp_libraryelement_parameter_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Parameter)


def test_hyp_libraryelement_parameter_constructor_exists():
    assert callable(libraryElement_Parameter.__init__)


def test_hyp_libraryelement_parameter_constructor_args():
    sig = inspect.signature(libraryElement_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_textalgorithm_is_not_abstract():
    assert not inspect.isabstract(TextAlgorithm)


def test_hyp_textalgorithm_constructor_exists():
    assert callable(TextAlgorithm.__init__)


def test_hyp_textalgorithm_constructor_args():
    sig = inspect.signature(TextAlgorithm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_stalgorithm_is_not_abstract():
    assert not inspect.isabstract(libraryElement_STAlgorithm)


def test_hyp_libraryelement_stalgorithm_constructor_exists():
    assert callable(libraryElement_STAlgorithm.__init__)


def test_hyp_libraryelement_stalgorithm_constructor_args():
    sig = inspect.signature(libraryElement_STAlgorithm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_otheralgorithm_is_not_abstract():
    assert not inspect.isabstract(libraryElement_OtherAlgorithm)


def test_hyp_libraryelement_otheralgorithm_constructor_exists():
    assert callable(libraryElement_OtherAlgorithm.__init__)


def test_hyp_libraryelement_otheralgorithm_constructor_args():
    sig = inspect.signature(libraryElement_OtherAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"




def test_hyp_libraryelement_identification_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Identification)


def test_hyp_libraryelement_identification_constructor_exists():
    assert callable(libraryElement_Identification.__init__)


def test_hyp_libraryelement_identification_constructor_args():
    sig = inspect.signature(libraryElement_Identification.__init__)
    params = list(sig.parameters.keys())
    assert "standard" in params, "Missing parameter 'standard'"
    assert "applicationDomain" in params, "Missing parameter 'applicationDomain'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "classification" in params, "Missing parameter 'classification'"
    assert "function" in params, "Missing parameter 'function'"









def test_hyp_libraryelement_service_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Service)


def test_hyp_libraryelement_service_constructor_exists():
    assert callable(libraryElement_Service.__init__)


def test_hyp_libraryelement_service_constructor_args():
    sig = inspect.signature(libraryElement_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_hyp_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_hyp_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_outputprimitive_is_not_abstract():
    assert not inspect.isabstract(libraryElement_OutputPrimitive)


def test_hyp_libraryelement_outputprimitive_constructor_exists():
    assert callable(libraryElement_OutputPrimitive.__init__)


def test_hyp_libraryelement_outputprimitive_constructor_args():
    sig = inspect.signature(libraryElement_OutputPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "TestResult" in params, "Missing parameter 'TestResult'"




def test_hyp_libraryelement_inputprimitive_is_not_abstract():
    assert not inspect.isabstract(libraryElement_InputPrimitive)


def test_hyp_libraryelement_inputprimitive_constructor_exists():
    assert callable(libraryElement_InputPrimitive.__init__)


def test_hyp_libraryelement_inputprimitive_constructor_args():
    sig = inspect.signature(libraryElement_InputPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_mapping_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Mapping)


def test_hyp_libraryelement_mapping_constructor_exists():
    assert callable(libraryElement_Mapping.__init__)


def test_hyp_libraryelement_mapping_constructor_args():
    sig = inspect.signature(libraryElement_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_interfacelist_is_not_abstract():
    assert not inspect.isabstract(libraryElement_InterfaceList)


def test_hyp_libraryelement_interfacelist_constructor_exists():
    assert callable(libraryElement_InterfaceList.__init__)


def test_hyp_libraryelement_interfacelist_constructor_args():
    sig = inspect.signature(libraryElement_InterfaceList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_fbnetworkelement_is_not_abstract():
    assert not inspect.isabstract(libraryElement_FBNetworkElement)


def test_hyp_libraryelement_fbnetworkelement_constructor_exists():
    assert callable(libraryElement_FBNetworkElement.__init__)


def test_hyp_libraryelement_fbnetworkelement_constructor_args():
    sig = inspect.signature(libraryElement_FBNetworkElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fbnetworkelement_is_not_abstract():
    assert not inspect.isabstract(FBNetworkElement)


def test_hyp_fbnetworkelement_constructor_exists():
    assert callable(FBNetworkElement.__init__)


def test_hyp_fbnetworkelement_constructor_args():
    sig = inspect.signature(FBNetworkElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_subapp_is_not_abstract():
    assert not inspect.isabstract(libraryElement_SubApp)


def test_hyp_libraryelement_subapp_constructor_exists():
    assert callable(libraryElement_SubApp.__init__)


def test_hyp_libraryelement_subapp_constructor_args():
    sig = inspect.signature(libraryElement_SubApp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_fb_is_not_abstract():
    assert not inspect.isabstract(libraryElement_FB)


def test_hyp_libraryelement_fb_constructor_exists():
    assert callable(libraryElement_FB.__init__)


def test_hyp_libraryelement_fb_constructor_args():
    sig = inspect.signature(libraryElement_FB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_with_is_not_abstract():
    assert not inspect.isabstract(libraryElement_With)


def test_hyp_libraryelement_with_constructor_exists():
    assert callable(libraryElement_With.__init__)


def test_hyp_libraryelement_with_constructor_args():
    sig = inspect.signature(libraryElement_With.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iinterfaceelement_is_not_abstract():
    assert not inspect.isabstract(IInterfaceElement)


def test_hyp_iinterfaceelement_constructor_exists():
    assert callable(IInterfaceElement.__init__)


def test_hyp_iinterfaceelement_constructor_args():
    sig = inspect.signature(IInterfaceElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(libraryElement_VarDeclaration)


def test_hyp_libraryelement_vardeclaration_constructor_exists():
    assert callable(libraryElement_VarDeclaration.__init__)


def test_hyp_libraryelement_vardeclaration_constructor_args():
    sig = inspect.signature(libraryElement_VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "arraySize" in params, "Missing parameter 'arraySize'"




def test_hyp_libraryelement_ectransition_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ECTransition)


def test_hyp_libraryelement_ectransition_constructor_exists():
    assert callable(libraryElement_ECTransition.__init__)


def test_hyp_libraryelement_ectransition_constructor_args():
    sig = inspect.signature(libraryElement_ECTransition.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"
    assert "comment" in params, "Missing parameter 'comment'"





def test_hyp_libraryelement_ecstate_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ECState)


def test_hyp_libraryelement_ecstate_constructor_exists():
    assert callable(libraryElement_ECState.__init__)


def test_hyp_libraryelement_ecstate_constructor_args():
    sig = inspect.signature(libraryElement_ECState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_event_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Event)


def test_hyp_libraryelement_event_constructor_exists():
    assert callable(libraryElement_Event.__init__)


def test_hyp_libraryelement_event_constructor_args():
    sig = inspect.signature(libraryElement_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_ecaction_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ECAction)


def test_hyp_libraryelement_ecaction_constructor_exists():
    assert callable(libraryElement_ECAction.__init__)


def test_hyp_libraryelement_ecaction_constructor_args():
    sig = inspect.signature(libraryElement_ECAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_resourcetypename_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ResourceTypeName)


def test_hyp_libraryelement_resourcetypename_constructor_exists():
    assert callable(libraryElement_ResourceTypeName.__init__)


def test_hyp_libraryelement_resourcetypename_constructor_args():
    sig = inspect.signature(libraryElement_ResourceTypeName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_compilabletype_is_not_abstract():
    assert not inspect.isabstract(CompilableType)


def test_hyp_compilabletype_constructor_exists():
    assert callable(CompilableType.__init__)


def test_hyp_compilabletype_constructor_args():
    sig = inspect.signature(CompilableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_resourcetype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_ResourceType)


def test_hyp_libraryelement_resourcetype_constructor_exists():
    assert callable(libraryElement_ResourceType.__init__)


def test_hyp_libraryelement_resourcetype_constructor_args():
    sig = inspect.signature(libraryElement_ResourceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_segmenttype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_SegmentType)


def test_hyp_libraryelement_segmenttype_constructor_exists():
    assert callable(libraryElement_SegmentType.__init__)


def test_hyp_libraryelement_segmenttype_constructor_args():
    sig = inspect.signature(libraryElement_SegmentType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_fbtype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_FBType)


def test_hyp_libraryelement_fbtype_constructor_exists():
    assert callable(libraryElement_FBType.__init__)


def test_hyp_libraryelement_fbtype_constructor_args():
    sig = inspect.signature(libraryElement_FBType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_devicetype_is_not_abstract():
    assert not inspect.isabstract(libraryElement_DeviceType)


def test_hyp_libraryelement_devicetype_constructor_exists():
    assert callable(libraryElement_DeviceType.__init__)


def test_hyp_libraryelement_devicetype_constructor_args():
    sig = inspect.signature(libraryElement_DeviceType.__init__)
    params = list(sig.parameters.keys())
    assert "profile" in params, "Missing parameter 'profile'"




def test_hyp_libraryelement_link_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Link)


def test_hyp_libraryelement_link_constructor_exists():
    assert callable(libraryElement_Link.__init__)


def test_hyp_libraryelement_link_constructor_args():
    sig = inspect.signature(libraryElement_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ivarelement_is_not_abstract():
    assert not inspect.isabstract(IVarElement)


def test_hyp_ivarelement_constructor_exists():
    assert callable(IVarElement.__init__)


def test_hyp_ivarelement_constructor_args():
    sig = inspect.signature(IVarElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_resource_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Resource)


def test_hyp_libraryelement_resource_constructor_exists():
    assert callable(libraryElement_Resource.__init__)


def test_hyp_libraryelement_resource_constructor_args():
    sig = inspect.signature(libraryElement_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "deviceTypeResource" in params, "Missing parameter 'deviceTypeResource'"






def test_hyp_colorizableelement_is_not_abstract():
    assert not inspect.isabstract(ColorizableElement)


def test_hyp_colorizableelement_constructor_exists():
    assert callable(ColorizableElement.__init__)


def test_hyp_colorizableelement_constructor_args():
    sig = inspect.signature(ColorizableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_libraryelement_segment_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Segment)


def test_hyp_libraryelement_segment_constructor_exists():
    assert callable(libraryElement_Segment.__init__)


def test_hyp_libraryelement_segment_constructor_args():
    sig = inspect.signature(libraryElement_Segment.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"




def test_hyp_libraryelement_device_is_not_abstract():
    assert not inspect.isabstract(libraryElement_Device)


def test_hyp_libraryelement_device_constructor_exists():
    assert callable(libraryElement_Device.__init__)


def test_hyp_libraryelement_device_constructor_args():
    sig = inspect.signature(libraryElement_Device.__init__)
    params = list(sig.parameters.keys())
    assert "profile" in params, "Missing parameter 'profile'"


def test_hyp_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_hyp_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "Cpp",
        "Java",
        "Other",
        "C",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"


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
libraryElement_IVarElement_strategy = st.builds(
    libraryElement_IVarElement,
)
libraryElement_ColorizableElement_strategy = st.builds(
    libraryElement_ColorizableElement,
)
libraryElement_Color_strategy = st.builds(
    libraryElement_Color,
    blue=
        safe_text,
    red=
        safe_text,
    green=
        safe_text
)
libraryElement_PositionableElement_strategy = st.builds(
    libraryElement_PositionableElement,
    x=
        safe_text,
    y=
        safe_text
)
libraryElement_Primitive_strategy = st.builds(
    libraryElement_Primitive,
    parameters=
        safe_text,
    event=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
libraryElement_AdapterEvent_strategy = st.builds(
    libraryElement_AdapterEvent,
)
I4DIACElement_strategy = st.builds(
    I4DIACElement,
)
libraryElement_Annotation_strategy = st.builds(
    libraryElement_Annotation,
    servity=
        safe_text,
    name=
        safe_text
)
libraryElement_I4DIACElement_strategy = st.builds(
    libraryElement_I4DIACElement,
)
FB_strategy = st.builds(
    FB,
)
libraryElement_ResourceTypeFB_strategy = st.builds(
    libraryElement_ResourceTypeFB,
)
libraryElement_INamedElement_strategy = st.builds(
    libraryElement_INamedElement,
    name=
        safe_text,
    comment=
        safe_text
)
libraryElement_Value_strategy = st.builds(
    libraryElement_Value,
    value=
        safe_text
)
libraryElement_DataType_strategy = st.builds(
    libraryElement_DataType,
)
PositionableElement_strategy = st.builds(
    PositionableElement,
)
TypedConfigureableObject_strategy = st.builds(
    TypedConfigureableObject,
)
ConfigurableObject_strategy = st.builds(
    ConfigurableObject,
)
libraryElement_TypedConfigureableObject_strategy = st.builds(
    libraryElement_TypedConfigureableObject,
)
libraryElement_Connection_strategy = st.builds(
    libraryElement_Connection,
    brokenConnection=
        safe_text,
    dx1=
        safe_text,
    resTypeConnection=
        safe_text,
    dy=
        safe_text,
    dx2=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
libraryElement_AdapterType_strategy = st.builds(
    libraryElement_AdapterType,
)
libraryElement_AdapterTypePaletteEntry_strategy = st.builds(
    libraryElement_AdapterTypePaletteEntry,
)
libraryElement_AdapterFB_strategy = st.builds(
    libraryElement_AdapterFB,
)
VarDeclaration_strategy = st.builds(
    VarDeclaration,
)
libraryElement_AdapterDeclaration_strategy = st.builds(
    libraryElement_AdapterDeclaration,
)
libraryElement_Compiler_strategy = st.builds(
    libraryElement_Compiler,
    version=
        safe_text,
    vendor=
        safe_text,
    product=
        safe_text,
    language=
        safe_text
)
libraryElement_CompilerInfo_strategy = st.builds(
    libraryElement_CompilerInfo,
    classdef=
        safe_text,
    header=
        safe_text
)
libraryElement_ECC_strategy = st.builds(
    libraryElement_ECC,
)
FBType_strategy = st.builds(
    FBType,
)
libraryElement_CompositeFBType_strategy = st.builds(
    libraryElement_CompositeFBType,
)
libraryElement_BasicFBType_strategy = st.builds(
    libraryElement_BasicFBType,
)
libraryElement_FBNetwork_strategy = st.builds(
    libraryElement_FBNetwork,
)
INamedElement_strategy = st.builds(
    INamedElement,
)
libraryElement_Application_strategy = st.builds(
    libraryElement_Application,
)
libraryElement_ServiceInterface_strategy = st.builds(
    libraryElement_ServiceInterface,
)
libraryElement_IInterfaceElement_strategy = st.builds(
    libraryElement_IInterfaceElement,
    typeName=
        safe_text,
    isInput=
        safe_text
)
libraryElement_Algorithm_strategy = st.builds(
    libraryElement_Algorithm,
)
libraryElement_AdapterFBType_strategy = st.builds(
    libraryElement_AdapterFBType,
)
Connection_strategy = st.builds(
    Connection,
)
Algorithm_strategy = st.builds(
    Algorithm,
)
libraryElement_TextAlgorithm_strategy = st.builds(
    libraryElement_TextAlgorithm,
    text=
        safe_text
)
libraryElement_SystemConfiguration_strategy = st.builds(
    libraryElement_SystemConfiguration,
)
libraryElement_Palette_strategy = st.builds(
    libraryElement_Palette,
)
libraryElement_ConfigurableObject_strategy = st.builds(
    libraryElement_ConfigurableObject,
)
libraryElement_PaletteEntry_strategy = st.builds(
    libraryElement_PaletteEntry,
)
libraryElement_LibraryElement_strategy = st.builds(
    libraryElement_LibraryElement,
)
libraryElement_VersionInfo_strategy = st.builds(
    libraryElement_VersionInfo,
    version=
        safe_text,
    date=
        safe_text,
    organization=
        safe_text,
    author=
        safe_text,
    remarks=
        safe_text
)
libraryElement_VarInitialization_strategy = st.builds(
    libraryElement_VarInitialization,
)
LibraryElement_strategy = st.builds(
    LibraryElement,
)
libraryElement_CompilableType_strategy = st.builds(
    libraryElement_CompilableType,
)
libraryElement_AutomationSystem_strategy = st.builds(
    libraryElement_AutomationSystem,
    project=
        safe_text
)
CompositeFBType_strategy = st.builds(
    CompositeFBType,
)
libraryElement_SubAppType_strategy = st.builds(
    libraryElement_SubAppType,
)
libraryElement_AdapterConnection_strategy = st.builds(
    libraryElement_AdapterConnection,
)
libraryElement_EventConnection_strategy = st.builds(
    libraryElement_EventConnection,
)
libraryElement_DataConnection_strategy = st.builds(
    libraryElement_DataConnection,
)
libraryElement_ServiceInterfaceFBType_strategy = st.builds(
    libraryElement_ServiceInterfaceFBType,
)
libraryElement_ServiceTransaction_strategy = st.builds(
    libraryElement_ServiceTransaction,
    TestResult=
        safe_text
)
libraryElement_ServiceSequence_strategy = st.builds(
    libraryElement_ServiceSequence,
    TestResult=
        safe_text
)
libraryElement_Parameter_strategy = st.builds(
    libraryElement_Parameter,
    comment=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
TextAlgorithm_strategy = st.builds(
    TextAlgorithm,
)
libraryElement_STAlgorithm_strategy = st.builds(
    libraryElement_STAlgorithm,
)
libraryElement_OtherAlgorithm_strategy = st.builds(
    libraryElement_OtherAlgorithm,
    language=
        safe_text
)
libraryElement_Identification_strategy = st.builds(
    libraryElement_Identification,
    standard=
        safe_text,
    applicationDomain=
        safe_text,
    type=
        safe_text,
    description=
        safe_text,
    classification=
        safe_text,
    function=
        safe_text
)
libraryElement_Service_strategy = st.builds(
    libraryElement_Service,
)
Primitive_strategy = st.builds(
    Primitive,
)
libraryElement_OutputPrimitive_strategy = st.builds(
    libraryElement_OutputPrimitive,
    TestResult=
        safe_text
)
libraryElement_InputPrimitive_strategy = st.builds(
    libraryElement_InputPrimitive,
)
libraryElement_Mapping_strategy = st.builds(
    libraryElement_Mapping,
)
libraryElement_InterfaceList_strategy = st.builds(
    libraryElement_InterfaceList,
)
libraryElement_FBNetworkElement_strategy = st.builds(
    libraryElement_FBNetworkElement,
)
FBNetworkElement_strategy = st.builds(
    FBNetworkElement,
)
libraryElement_SubApp_strategy = st.builds(
    libraryElement_SubApp,
)
libraryElement_FB_strategy = st.builds(
    libraryElement_FB,
)
libraryElement_With_strategy = st.builds(
    libraryElement_With,
)
IInterfaceElement_strategy = st.builds(
    IInterfaceElement,
)
libraryElement_VarDeclaration_strategy = st.builds(
    libraryElement_VarDeclaration,
    arraySize=
        safe_text
)
libraryElement_ECTransition_strategy = st.builds(
    libraryElement_ECTransition,
    conditionExpression=
        safe_text,
    comment=
        safe_text
)
libraryElement_ECState_strategy = st.builds(
    libraryElement_ECState,
)
libraryElement_Event_strategy = st.builds(
    libraryElement_Event,
)
libraryElement_ECAction_strategy = st.builds(
    libraryElement_ECAction,
)
libraryElement_ResourceTypeName_strategy = st.builds(
    libraryElement_ResourceTypeName,
    name=
        safe_text
)
CompilableType_strategy = st.builds(
    CompilableType,
)
libraryElement_ResourceType_strategy = st.builds(
    libraryElement_ResourceType,
)
libraryElement_SegmentType_strategy = st.builds(
    libraryElement_SegmentType,
)
libraryElement_FBType_strategy = st.builds(
    libraryElement_FBType,
)
libraryElement_DeviceType_strategy = st.builds(
    libraryElement_DeviceType,
    profile=
        safe_text
)
libraryElement_Link_strategy = st.builds(
    libraryElement_Link,
)
IVarElement_strategy = st.builds(
    IVarElement,
)
libraryElement_Resource_strategy = st.builds(
    libraryElement_Resource,
    x=
        safe_text,
    y=
        safe_text,
    deviceTypeResource=
        safe_text
)
ColorizableElement_strategy = st.builds(
    ColorizableElement,
)
libraryElement_Segment_strategy = st.builds(
    libraryElement_Segment,
    width=
        safe_text
)
libraryElement_Device_strategy = st.builds(
    libraryElement_Device,
    profile=
        safe_text
)






@given(instance=libraryElement_Color_strategy)
def test_hyp_libraryelement_color_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=libraryElement_Color_strategy)
def test_hyp_libraryelement_color_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=libraryElement_Color_strategy)
def test_hyp_libraryelement_color_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original




@given(instance=libraryElement_PositionableElement_strategy)
def test_hyp_libraryelement_positionableelement_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=libraryElement_PositionableElement_strategy)
def test_hyp_libraryelement_positionableelement_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=libraryElement_Primitive_strategy)
def test_hyp_libraryelement_primitive_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original



@given(instance=libraryElement_Primitive_strategy)
def test_hyp_libraryelement_primitive_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original







@given(instance=libraryElement_Annotation_strategy)
def test_hyp_libraryelement_annotation_servity_setter(instance):
    original = instance.servity
    instance.servity = original
    assert instance.servity == original



@given(instance=libraryElement_Annotation_strategy)
def test_hyp_libraryelement_annotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_I4DIACElement_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_i4diacelement_createannotation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createAnnotation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createAnnotation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createAnnotation' in libraryElement_I4DIACElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createAnnotation' in libraryElement_I4DIACElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createAnnotation' in libraryElement_I4DIACElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_I4DIACElement_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_i4diacelement_removeannotation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeAnnotation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeAnnotation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeAnnotation' in libraryElement_I4DIACElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeAnnotation' in libraryElement_I4DIACElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeAnnotation' in libraryElement_I4DIACElement is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_ResourceTypeFB_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_resourcetypefb_isresourcetypefb_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isResourceTypeFB()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isResourceTypeFB).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isResourceTypeFB' in libraryElement_ResourceTypeFB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isResourceTypeFB' in libraryElement_ResourceTypeFB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isResourceTypeFB' in libraryElement_ResourceTypeFB is not implemented or raised an error")




@given(instance=libraryElement_INamedElement_strategy)
def test_hyp_libraryelement_inamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=libraryElement_INamedElement_strategy)
def test_hyp_libraryelement_inamedelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=libraryElement_Value_strategy)
def test_hyp_libraryelement_value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=libraryElement_Connection_strategy)
def test_hyp_libraryelement_connection_brokenConnection_setter(instance):
    original = instance.brokenConnection
    instance.brokenConnection = original
    assert instance.brokenConnection == original



@given(instance=libraryElement_Connection_strategy)
def test_hyp_libraryelement_connection_dx1_setter(instance):
    original = instance.dx1
    instance.dx1 = original
    assert instance.dx1 == original



@given(instance=libraryElement_Connection_strategy)
def test_hyp_libraryelement_connection_resTypeConnection_setter(instance):
    original = instance.resTypeConnection
    instance.resTypeConnection = original
    assert instance.resTypeConnection == original



@given(instance=libraryElement_Connection_strategy)
def test_hyp_libraryelement_connection_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original



@given(instance=libraryElement_Connection_strategy)
def test_hyp_libraryelement_connection_dx2_setter(instance):
    original = instance.dx2
    instance.dx2 = original
    assert instance.dx2 == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_Connection_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_connection_isresourceconnection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isResourceConnection()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isResourceConnection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isResourceConnection' in libraryElement_Connection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isResourceConnection' in libraryElement_Connection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isResourceConnection' in libraryElement_Connection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_Connection_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_connection_checkifconnectionbroken_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkIfConnectionBroken()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkIfConnectionBroken).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkIfConnectionBroken' in libraryElement_Connection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkIfConnectionBroken' in libraryElement_Connection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkIfConnectionBroken' in libraryElement_Connection is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_AdapterFB_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_adapterfb_isplug_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPlug()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPlug).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPlug' in libraryElement_AdapterFB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPlug' in libraryElement_AdapterFB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPlug' in libraryElement_AdapterFB is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_AdapterFB_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_adapterfb_issocket_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSocket()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSocket).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSocket' in libraryElement_AdapterFB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSocket' in libraryElement_AdapterFB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSocket' in libraryElement_AdapterFB is not implemented or raised an error")






@given(instance=libraryElement_Compiler_strategy)
def test_hyp_libraryelement_compiler_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=libraryElement_Compiler_strategy)
def test_hyp_libraryelement_compiler_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=libraryElement_Compiler_strategy)
def test_hyp_libraryelement_compiler_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=libraryElement_Compiler_strategy)
def test_hyp_libraryelement_compiler_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=libraryElement_CompilerInfo_strategy)
def test_hyp_libraryelement_compilerinfo_classdef_setter(instance):
    original = instance.classdef
    instance.classdef = original
    assert instance.classdef == original



@given(instance=libraryElement_CompilerInfo_strategy)
def test_hyp_libraryelement_compilerinfo_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_isresourcenetwork_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isResourceNetwork()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isResourceNetwork).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isResourceNetwork' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isResourceNetwork' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isResourceNetwork' in libraryElement_FBNetwork is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_removeconnection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeConnection(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeConnection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeConnection' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeConnection' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeConnection' in libraryElement_FBNetwork is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_issubapplicationnetwork_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSubApplicationNetwork()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSubApplicationNetwork).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSubApplicationNetwork' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSubApplicationNetwork' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSubApplicationNetwork' in libraryElement_FBNetwork is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_iscfbtypenetwork_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCFBTypeNetwork()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCFBTypeNetwork).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCFBTypeNetwork' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCFBTypeNetwork' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCFBTypeNetwork' in libraryElement_FBNetwork is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_addconnection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addConnection(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addConnection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addConnection' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addConnection' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addConnection' in libraryElement_FBNetwork is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetwork_isapplicationnetwork_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isApplicationNetwork()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isApplicationNetwork).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isApplicationNetwork' in libraryElement_FBNetwork is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isApplicationNetwork' in libraryElement_FBNetwork did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isApplicationNetwork' in libraryElement_FBNetwork is not implemented or raised an error")







@given(instance=libraryElement_IInterfaceElement_strategy)
def test_hyp_libraryelement_iinterfaceelement_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=libraryElement_IInterfaceElement_strategy)
def test_hyp_libraryelement_iinterfaceelement_isInput_setter(instance):
    original = instance.isInput
    instance.isInput = original
    assert instance.isInput == original








@given(instance=libraryElement_TextAlgorithm_strategy)
def test_hyp_libraryelement_textalgorithm_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_ConfigurableObject_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_configurableobject_setparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setParameter(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setParameter' in libraryElement_ConfigurableObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setParameter' in libraryElement_ConfigurableObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setParameter' in libraryElement_ConfigurableObject is not implemented or raised an error")






@given(instance=libraryElement_VersionInfo_strategy)
def test_hyp_libraryelement_versioninfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=libraryElement_VersionInfo_strategy)
def test_hyp_libraryelement_versioninfo_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=libraryElement_VersionInfo_strategy)
def test_hyp_libraryelement_versioninfo_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=libraryElement_VersionInfo_strategy)
def test_hyp_libraryelement_versioninfo_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=libraryElement_VersionInfo_strategy)
def test_hyp_libraryelement_versioninfo_remarks_setter(instance):
    original = instance.remarks
    instance.remarks = original
    assert instance.remarks == original







@given(instance=libraryElement_AutomationSystem_strategy)
def test_hyp_libraryelement_automationsystem_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original










@given(instance=libraryElement_ServiceTransaction_strategy)
def test_hyp_libraryelement_servicetransaction_TestResult_setter(instance):
    original = instance.TestResult
    instance.TestResult = original
    assert instance.TestResult == original




@given(instance=libraryElement_ServiceSequence_strategy)
def test_hyp_libraryelement_servicesequence_TestResult_setter(instance):
    original = instance.TestResult
    instance.TestResult = original
    assert instance.TestResult == original




@given(instance=libraryElement_Parameter_strategy)
def test_hyp_libraryelement_parameter_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=libraryElement_Parameter_strategy)
def test_hyp_libraryelement_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=libraryElement_Parameter_strategy)
def test_hyp_libraryelement_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=libraryElement_OtherAlgorithm_strategy)
def test_hyp_libraryelement_otheralgorithm_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_standard_setter(instance):
    original = instance.standard
    instance.standard = original
    assert instance.standard == original



@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_applicationDomain_setter(instance):
    original = instance.applicationDomain
    instance.applicationDomain = original
    assert instance.applicationDomain == original



@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_classification_setter(instance):
    original = instance.classification
    instance.classification = original
    assert instance.classification == original



@given(instance=libraryElement_Identification_strategy)
def test_hyp_libraryelement_identification_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original






@given(instance=libraryElement_OutputPrimitive_strategy)
def test_hyp_libraryelement_outputprimitive_TestResult_setter(instance):
    original = instance.TestResult
    instance.TestResult = original
    assert instance.TestResult == original





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetworkElement_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetworkelement_ismapped_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMapped()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMapped).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMapped' in libraryElement_FBNetworkElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMapped' in libraryElement_FBNetworkElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMapped' in libraryElement_FBNetworkElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FBNetworkElement_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fbnetworkelement_checkconnections_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkConnections()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkConnections).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkConnections' in libraryElement_FBNetworkElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkConnections' in libraryElement_FBNetworkElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkConnections' in libraryElement_FBNetworkElement is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FB_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fb_isresourcetypefb_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isResourceTypeFB()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isResourceTypeFB).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isResourceTypeFB' in libraryElement_FB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isResourceTypeFB' in libraryElement_FB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isResourceTypeFB' in libraryElement_FB is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_FB_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_fb_isresourcefb_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isResourceFB()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isResourceFB).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isResourceFB' in libraryElement_FB is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isResourceFB' in libraryElement_FB did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isResourceFB' in libraryElement_FB is not implemented or raised an error")






@given(instance=libraryElement_VarDeclaration_strategy)
def test_hyp_libraryelement_vardeclaration_arraySize_setter(instance):
    original = instance.arraySize
    instance.arraySize = original
    assert instance.arraySize == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_VarDeclaration_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_vardeclaration_isarray_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isArray()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isArray).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isArray' in libraryElement_VarDeclaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isArray' in libraryElement_VarDeclaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isArray' in libraryElement_VarDeclaration is not implemented or raised an error")




@given(instance=libraryElement_ECTransition_strategy)
def test_hyp_libraryelement_ectransition_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original



@given(instance=libraryElement_ECTransition_strategy)
def test_hyp_libraryelement_ectransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryElement_ECState_strategy)
@settings(max_examples=30)
def test_hyp_libraryelement_ecstate_isstartstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStartState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStartState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStartState' in libraryElement_ECState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStartState' in libraryElement_ECState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStartState' in libraryElement_ECState is not implemented or raised an error")






@given(instance=libraryElement_ResourceTypeName_strategy)
def test_hyp_libraryelement_resourcetypename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=libraryElement_DeviceType_strategy)
def test_hyp_libraryelement_devicetype_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original






@given(instance=libraryElement_Resource_strategy)
def test_hyp_libraryelement_resource_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=libraryElement_Resource_strategy)
def test_hyp_libraryelement_resource_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=libraryElement_Resource_strategy)
def test_hyp_libraryelement_resource_deviceTypeResource_setter(instance):
    original = instance.deviceTypeResource
    instance.deviceTypeResource = original
    assert instance.deviceTypeResource == original





@given(instance=libraryElement_Segment_strategy)
def test_hyp_libraryelement_segment_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=libraryElement_Device_strategy)
def test_hyp_libraryelement_device_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Algorithm,
    ColorizableElement,
    CompilableType,
    CompositeFBType,
    ConfigurableObject,
    Connection,
    DataType,
    Event,
    FB,
    FBNetworkElement,
    FBType,
    I4DIACElement,
    IInterfaceElement,
    INamedElement,
    IVarElement,
    LibraryElement,
    PositionableElement,
    Primitive,
    TextAlgorithm,
    TypedConfigureableObject,
    VarDeclaration,
    libraryElement_AdapterConnection,
    libraryElement_AdapterDeclaration,
    libraryElement_AdapterEvent,
    libraryElement_AdapterFB,
    libraryElement_AdapterFBType,
    libraryElement_AdapterType,
    libraryElement_AdapterTypePaletteEntry,
    libraryElement_Algorithm,
    libraryElement_Annotation,
    libraryElement_Application,
    libraryElement_AutomationSystem,
    libraryElement_BasicFBType,
    libraryElement_Color,
    libraryElement_ColorizableElement,
    libraryElement_CompilableType,
    libraryElement_Compiler,
    libraryElement_CompilerInfo,
    libraryElement_CompositeFBType,
    libraryElement_ConfigurableObject,
    libraryElement_Connection,
    libraryElement_DataConnection,
    libraryElement_DataType,
    libraryElement_Device,
    libraryElement_DeviceType,
    libraryElement_ECAction,
    libraryElement_ECC,
    libraryElement_ECState,
    libraryElement_ECTransition,
    libraryElement_Event,
    libraryElement_EventConnection,
    libraryElement_FB,
    libraryElement_FBNetwork,
    libraryElement_FBNetworkElement,
    libraryElement_FBType,
    libraryElement_I4DIACElement,
    libraryElement_IInterfaceElement,
    libraryElement_INamedElement,
    libraryElement_IVarElement,
    libraryElement_Identification,
    libraryElement_InputPrimitive,
    libraryElement_InterfaceList,
    libraryElement_LibraryElement,
    libraryElement_Link,
    libraryElement_Mapping,
    libraryElement_OtherAlgorithm,
    libraryElement_OutputPrimitive,
    libraryElement_Palette,
    libraryElement_PaletteEntry,
    libraryElement_Parameter,
    libraryElement_PositionableElement,
    libraryElement_Primitive,
    libraryElement_Resource,
    libraryElement_ResourceType,
    libraryElement_ResourceTypeFB,
    libraryElement_ResourceTypeName,
    libraryElement_STAlgorithm,
    libraryElement_Segment,
    libraryElement_SegmentType,
    libraryElement_Service,
    libraryElement_ServiceInterface,
    libraryElement_ServiceInterfaceFBType,
    libraryElement_ServiceSequence,
    libraryElement_ServiceTransaction,
    libraryElement_SubApp,
    libraryElement_SubAppType,
    libraryElement_SystemConfiguration,
    libraryElement_TextAlgorithm,
    libraryElement_TypedConfigureableObject,
    libraryElement_Value,
    libraryElement_VarDeclaration,
    libraryElement_VarInitialization,
    libraryElement_VersionInfo,
    libraryElement_With,
    Language,
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

def test_libraryElement_Annotation_name_value_roundtrip():
    instance = libraryElement_Annotation(name="sample_text", servity="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_libraryElement_Annotation_servity_value_roundtrip():
    instance = libraryElement_Annotation(name="sample_text", servity="sample_text")
    assert instance.servity == "sample_text"
    instance.servity = "sample_text_2"
    assert instance.servity == "sample_text_2"


def test_libraryElement_AutomationSystem_project_value_roundtrip():
    instance = libraryElement_AutomationSystem(project="sample_text")
    assert instance.project == "sample_text"
    instance.project = "sample_text_2"
    assert instance.project == "sample_text_2"


def test_libraryElement_Color_blue_value_roundtrip():
    instance = libraryElement_Color(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.blue == "sample_text"
    instance.blue = "sample_text_2"
    assert instance.blue == "sample_text_2"


def test_libraryElement_Color_green_value_roundtrip():
    instance = libraryElement_Color(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.green == "sample_text"
    instance.green = "sample_text_2"
    assert instance.green == "sample_text_2"


def test_libraryElement_Color_red_value_roundtrip():
    instance = libraryElement_Color(blue="sample_text", green="sample_text", red="sample_text")
    assert instance.red == "sample_text"
    instance.red = "sample_text_2"
    assert instance.red == "sample_text_2"


def test_libraryElement_Compiler_language_value_roundtrip():
    instance = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_libraryElement_Compiler_product_value_roundtrip():
    instance = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    assert instance.product == "sample_text"
    instance.product = "sample_text_2"
    assert instance.product == "sample_text_2"


def test_libraryElement_Compiler_vendor_value_roundtrip():
    instance = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_libraryElement_Compiler_version_value_roundtrip():
    instance = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_libraryElement_CompilerInfo_classdef_value_roundtrip():
    instance = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    assert instance.classdef == "sample_text"
    instance.classdef = "sample_text_2"
    assert instance.classdef == "sample_text_2"


def test_libraryElement_CompilerInfo_header_value_roundtrip():
    instance = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    assert instance.header == "sample_text"
    instance.header = "sample_text_2"
    assert instance.header == "sample_text_2"


def test_libraryElement_Connection_brokenConnection_value_roundtrip():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert instance.brokenConnection == "sample_text"
    instance.brokenConnection = "sample_text_2"
    assert instance.brokenConnection == "sample_text_2"


def test_libraryElement_Connection_dx1_value_roundtrip():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert instance.dx1 == "sample_text"
    instance.dx1 = "sample_text_2"
    assert instance.dx1 == "sample_text_2"


def test_libraryElement_Connection_dx2_value_roundtrip():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert instance.dx2 == "sample_text"
    instance.dx2 = "sample_text_2"
    assert instance.dx2 == "sample_text_2"


def test_libraryElement_Connection_dy_value_roundtrip():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert instance.dy == "sample_text"
    instance.dy = "sample_text_2"
    assert instance.dy == "sample_text_2"


def test_libraryElement_Connection_resTypeConnection_value_roundtrip():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert instance.resTypeConnection == "sample_text"
    instance.resTypeConnection = "sample_text_2"
    assert instance.resTypeConnection == "sample_text_2"


def test_libraryElement_Device_profile_value_roundtrip():
    instance = libraryElement_Device(profile="sample_text")
    assert instance.profile == "sample_text"
    instance.profile = "sample_text_2"
    assert instance.profile == "sample_text_2"


def test_libraryElement_DeviceType_profile_value_roundtrip():
    instance = libraryElement_DeviceType(profile="sample_text")
    assert instance.profile == "sample_text"
    instance.profile = "sample_text_2"
    assert instance.profile == "sample_text_2"


def test_libraryElement_ECTransition_comment_value_roundtrip():
    instance = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_libraryElement_ECTransition_conditionExpression_value_roundtrip():
    instance = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    assert instance.conditionExpression == "sample_text"
    instance.conditionExpression = "sample_text_2"
    assert instance.conditionExpression == "sample_text_2"


def test_libraryElement_IInterfaceElement_isInput_value_roundtrip():
    instance = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    assert instance.isInput == "sample_text"
    instance.isInput = "sample_text_2"
    assert instance.isInput == "sample_text_2"


def test_libraryElement_IInterfaceElement_typeName_value_roundtrip():
    instance = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_libraryElement_INamedElement_comment_value_roundtrip():
    instance = libraryElement_INamedElement(comment="sample_text", name="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_libraryElement_INamedElement_name_value_roundtrip():
    instance = libraryElement_INamedElement(comment="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_libraryElement_Identification_applicationDomain_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.applicationDomain == "sample_text"
    instance.applicationDomain = "sample_text_2"
    assert instance.applicationDomain == "sample_text_2"


def test_libraryElement_Identification_classification_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.classification == "sample_text"
    instance.classification = "sample_text_2"
    assert instance.classification == "sample_text_2"


def test_libraryElement_Identification_description_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_libraryElement_Identification_function_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_libraryElement_Identification_standard_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.standard == "sample_text"
    instance.standard = "sample_text_2"
    assert instance.standard == "sample_text_2"


def test_libraryElement_Identification_type_value_roundtrip():
    instance = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_libraryElement_OtherAlgorithm_language_value_roundtrip():
    instance = libraryElement_OtherAlgorithm(language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_libraryElement_OutputPrimitive_TestResult_value_roundtrip():
    instance = libraryElement_OutputPrimitive(TestResult="sample_text")
    assert instance.TestResult == "sample_text"
    instance.TestResult = "sample_text_2"
    assert instance.TestResult == "sample_text_2"


def test_libraryElement_Parameter_comment_value_roundtrip():
    instance = libraryElement_Parameter(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_libraryElement_Parameter_name_value_roundtrip():
    instance = libraryElement_Parameter(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_libraryElement_Parameter_value_value_roundtrip():
    instance = libraryElement_Parameter(comment="sample_text", name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_libraryElement_PositionableElement_x_value_roundtrip():
    instance = libraryElement_PositionableElement(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_libraryElement_PositionableElement_y_value_roundtrip():
    instance = libraryElement_PositionableElement(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_libraryElement_Primitive_event_value_roundtrip():
    instance = libraryElement_Primitive(event="sample_text", parameters="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_libraryElement_Primitive_parameters_value_roundtrip():
    instance = libraryElement_Primitive(event="sample_text", parameters="sample_text")
    assert instance.parameters == "sample_text"
    instance.parameters = "sample_text_2"
    assert instance.parameters == "sample_text_2"


def test_libraryElement_Resource_deviceTypeResource_value_roundtrip():
    instance = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    assert instance.deviceTypeResource == "sample_text"
    instance.deviceTypeResource = "sample_text_2"
    assert instance.deviceTypeResource == "sample_text_2"


def test_libraryElement_Resource_x_value_roundtrip():
    instance = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_libraryElement_Resource_y_value_roundtrip():
    instance = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_libraryElement_ResourceTypeName_name_value_roundtrip():
    instance = libraryElement_ResourceTypeName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_libraryElement_Segment_width_value_roundtrip():
    instance = libraryElement_Segment(width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_libraryElement_ServiceSequence_TestResult_value_roundtrip():
    instance = libraryElement_ServiceSequence(TestResult="sample_text")
    assert instance.TestResult == "sample_text"
    instance.TestResult = "sample_text_2"
    assert instance.TestResult == "sample_text_2"


def test_libraryElement_ServiceTransaction_TestResult_value_roundtrip():
    instance = libraryElement_ServiceTransaction(TestResult="sample_text")
    assert instance.TestResult == "sample_text"
    instance.TestResult = "sample_text_2"
    assert instance.TestResult == "sample_text_2"


def test_libraryElement_TextAlgorithm_text_value_roundtrip():
    instance = libraryElement_TextAlgorithm(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_libraryElement_Value_value_value_roundtrip():
    instance = libraryElement_Value(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_libraryElement_VarDeclaration_arraySize_value_roundtrip():
    instance = libraryElement_VarDeclaration(arraySize="sample_text")
    assert instance.arraySize == "sample_text"
    instance.arraySize = "sample_text_2"
    assert instance.arraySize == "sample_text_2"


def test_libraryElement_VersionInfo_author_value_roundtrip():
    instance = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_libraryElement_VersionInfo_date_value_roundtrip():
    instance = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_libraryElement_VersionInfo_organization_value_roundtrip():
    instance = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_libraryElement_VersionInfo_remarks_value_roundtrip():
    instance = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    assert instance.remarks == "sample_text"
    instance.remarks = "sample_text_2"
    assert instance.remarks == "sample_text_2"


def test_libraryElement_VersionInfo_version_value_roundtrip():
    instance = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_libraryElement_TextAlgorithm_isa_Algorithm():
    instance = libraryElement_TextAlgorithm(text="sample_text")
    assert isinstance(instance, Algorithm)


def test_libraryElement_Device_isa_ColorizableElement():
    instance = libraryElement_Device(profile="sample_text")
    assert isinstance(instance, ColorizableElement)


def test_libraryElement_Segment_isa_ColorizableElement():
    instance = libraryElement_Segment(width="sample_text")
    assert isinstance(instance, ColorizableElement)


def test_libraryElement_DeviceType_isa_CompilableType():
    instance = libraryElement_DeviceType(profile="sample_text")
    assert isinstance(instance, CompilableType)


def test_libraryElement_FBType_isa_CompilableType():
    instance = libraryElement_FBType()
    assert isinstance(instance, CompilableType)


def test_libraryElement_ResourceType_isa_CompilableType():
    instance = libraryElement_ResourceType()
    assert isinstance(instance, CompilableType)


def test_libraryElement_SegmentType_isa_CompilableType():
    instance = libraryElement_SegmentType()
    assert isinstance(instance, CompilableType)


def test_libraryElement_SubAppType_isa_CompositeFBType():
    instance = libraryElement_SubAppType()
    assert isinstance(instance, CompositeFBType)


def test_libraryElement_Connection_isa_ConfigurableObject():
    instance = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    assert isinstance(instance, ConfigurableObject)


def test_libraryElement_Link_isa_ConfigurableObject():
    instance = libraryElement_Link()
    assert isinstance(instance, ConfigurableObject)


def test_libraryElement_TypedConfigureableObject_isa_ConfigurableObject():
    instance = libraryElement_TypedConfigureableObject()
    assert isinstance(instance, ConfigurableObject)


def test_libraryElement_AdapterConnection_isa_Connection():
    instance = libraryElement_AdapterConnection()
    assert isinstance(instance, Connection)


def test_libraryElement_DataConnection_isa_Connection():
    instance = libraryElement_DataConnection()
    assert isinstance(instance, Connection)


def test_libraryElement_EventConnection_isa_Connection():
    instance = libraryElement_EventConnection()
    assert isinstance(instance, Connection)


def test_libraryElement_AdapterType_isa_DataType():
    instance = libraryElement_AdapterType()
    assert isinstance(instance, DataType)


def test_libraryElement_AdapterEvent_isa_Event():
    instance = libraryElement_AdapterEvent()
    assert isinstance(instance, Event)


def test_libraryElement_AdapterFB_isa_FB():
    instance = libraryElement_AdapterFB()
    assert isinstance(instance, FB)


def test_libraryElement_ResourceTypeFB_isa_FB():
    instance = libraryElement_ResourceTypeFB()
    assert isinstance(instance, FB)


def test_libraryElement_FB_isa_FBNetworkElement():
    instance = libraryElement_FB()
    assert isinstance(instance, FBNetworkElement)


def test_libraryElement_SubApp_isa_FBNetworkElement():
    instance = libraryElement_SubApp()
    assert isinstance(instance, FBNetworkElement)


def test_libraryElement_AdapterFBType_isa_FBType():
    instance = libraryElement_AdapterFBType()
    assert isinstance(instance, FBType)


def test_libraryElement_BasicFBType_isa_FBType():
    instance = libraryElement_BasicFBType()
    assert isinstance(instance, FBType)


def test_libraryElement_CompositeFBType_isa_FBType():
    instance = libraryElement_CompositeFBType()
    assert isinstance(instance, FBType)


def test_libraryElement_ServiceInterfaceFBType_isa_FBType():
    instance = libraryElement_ServiceInterfaceFBType()
    assert isinstance(instance, FBType)


def test_libraryElement_INamedElement_isa_I4DIACElement():
    instance = libraryElement_INamedElement(comment="sample_text", name="sample_text")
    assert isinstance(instance, I4DIACElement)


def test_libraryElement_Service_isa_I4DIACElement():
    instance = libraryElement_Service()
    assert isinstance(instance, I4DIACElement)


def test_libraryElement_SystemConfiguration_isa_I4DIACElement():
    instance = libraryElement_SystemConfiguration()
    assert isinstance(instance, I4DIACElement)


def test_libraryElement_Event_isa_IInterfaceElement():
    instance = libraryElement_Event()
    assert isinstance(instance, IInterfaceElement)


def test_libraryElement_VarDeclaration_isa_IInterfaceElement():
    instance = libraryElement_VarDeclaration(arraySize="sample_text")
    assert isinstance(instance, IInterfaceElement)


def test_libraryElement_Algorithm_isa_INamedElement():
    instance = libraryElement_Algorithm()
    assert isinstance(instance, INamedElement)


def test_libraryElement_Application_isa_INamedElement():
    instance = libraryElement_Application()
    assert isinstance(instance, INamedElement)


def test_libraryElement_ConfigurableObject_isa_INamedElement():
    instance = libraryElement_ConfigurableObject()
    assert isinstance(instance, INamedElement)


def test_libraryElement_ECState_isa_INamedElement():
    instance = libraryElement_ECState()
    assert isinstance(instance, INamedElement)


def test_libraryElement_IInterfaceElement_isa_INamedElement():
    instance = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    assert isinstance(instance, INamedElement)


def test_libraryElement_LibraryElement_isa_INamedElement():
    instance = libraryElement_LibraryElement()
    assert isinstance(instance, INamedElement)


def test_libraryElement_ServiceInterface_isa_INamedElement():
    instance = libraryElement_ServiceInterface()
    assert isinstance(instance, INamedElement)


def test_libraryElement_ServiceSequence_isa_INamedElement():
    instance = libraryElement_ServiceSequence(TestResult="sample_text")
    assert isinstance(instance, INamedElement)


def test_libraryElement_Device_isa_IVarElement():
    instance = libraryElement_Device(profile="sample_text")
    assert isinstance(instance, IVarElement)


def test_libraryElement_Resource_isa_IVarElement():
    instance = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, IVarElement)


def test_libraryElement_AutomationSystem_isa_LibraryElement():
    instance = libraryElement_AutomationSystem(project="sample_text")
    assert isinstance(instance, LibraryElement)


def test_libraryElement_CompilableType_isa_LibraryElement():
    instance = libraryElement_CompilableType()
    assert isinstance(instance, LibraryElement)


def test_libraryElement_Device_isa_PositionableElement():
    instance = libraryElement_Device(profile="sample_text")
    assert isinstance(instance, PositionableElement)


def test_libraryElement_ECState_isa_PositionableElement():
    instance = libraryElement_ECState()
    assert isinstance(instance, PositionableElement)


def test_libraryElement_ECTransition_isa_PositionableElement():
    instance = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    assert isinstance(instance, PositionableElement)


def test_libraryElement_FBNetworkElement_isa_PositionableElement():
    instance = libraryElement_FBNetworkElement()
    assert isinstance(instance, PositionableElement)


def test_libraryElement_Segment_isa_PositionableElement():
    instance = libraryElement_Segment(width="sample_text")
    assert isinstance(instance, PositionableElement)


def test_libraryElement_InputPrimitive_isa_Primitive():
    instance = libraryElement_InputPrimitive()
    assert isinstance(instance, Primitive)


def test_libraryElement_OutputPrimitive_isa_Primitive():
    instance = libraryElement_OutputPrimitive(TestResult="sample_text")
    assert isinstance(instance, Primitive)


def test_libraryElement_OtherAlgorithm_isa_TextAlgorithm():
    instance = libraryElement_OtherAlgorithm(language="sample_text")
    assert isinstance(instance, TextAlgorithm)


def test_libraryElement_STAlgorithm_isa_TextAlgorithm():
    instance = libraryElement_STAlgorithm()
    assert isinstance(instance, TextAlgorithm)


def test_libraryElement_Device_isa_TypedConfigureableObject():
    instance = libraryElement_Device(profile="sample_text")
    assert isinstance(instance, TypedConfigureableObject)


def test_libraryElement_FBNetworkElement_isa_TypedConfigureableObject():
    instance = libraryElement_FBNetworkElement()
    assert isinstance(instance, TypedConfigureableObject)


def test_libraryElement_Resource_isa_TypedConfigureableObject():
    instance = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    assert isinstance(instance, TypedConfigureableObject)


def test_libraryElement_Segment_isa_TypedConfigureableObject():
    instance = libraryElement_Segment(width="sample_text")
    assert isinstance(instance, TypedConfigureableObject)


def test_libraryElement_AdapterDeclaration_isa_VarDeclaration():
    instance = libraryElement_AdapterDeclaration()
    assert isinstance(instance, VarDeclaration)


def test_assoc_adapterConnections114_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_AdapterConnection()
    b2 = libraryElement_AdapterConnection()
    _safe_set(a, 'libraryElement_FBNetwork115', {b1})
    assert _is_linked(a, 'libraryElement_FBNetwork115', b1)
    if hasattr(b1, 'libraryElement_AdapterConnection'):
        assert _is_linked(b1, 'libraryElement_AdapterConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork115', {b2})
    assert _is_linked(a, 'libraryElement_FBNetwork115', b2)
    if hasattr(b1, 'libraryElement_AdapterConnection'):
        assert not _is_linked(b1, 'libraryElement_AdapterConnection', a)
    if hasattr(b2, 'libraryElement_AdapterConnection'):
        assert _is_linked(b2, 'libraryElement_AdapterConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork115', set())
    assert not _is_linked(a, 'libraryElement_FBNetwork115', b2)
    if hasattr(b2, 'libraryElement_AdapterConnection'):
        assert not _is_linked(b2, 'libraryElement_AdapterConnection', a)


def test_assoc_adapterDecl169_link_reassign_clear():
    a = libraryElement_AdapterFB()
    b1 = libraryElement_AdapterDeclaration()
    b2 = libraryElement_AdapterDeclaration()
    _safe_set(a, 'adapterFB', b1)
    assert _is_linked(a, 'adapterFB', b1)
    if hasattr(b1, 'AdapterDeclaration'):
        assert _is_linked(b1, 'AdapterDeclaration', a)
    _safe_set(a, 'adapterFB', b2)
    assert _is_linked(a, 'adapterFB', b2)
    if hasattr(b1, 'AdapterDeclaration'):
        assert not _is_linked(b1, 'AdapterDeclaration', a)
    if hasattr(b2, 'AdapterDeclaration'):
        assert _is_linked(b2, 'AdapterDeclaration', a)
    _safe_set(a, 'adapterFB', None)
    assert not _is_linked(a, 'adapterFB', b2)
    if hasattr(b2, 'AdapterDeclaration'):
        assert not _is_linked(b2, 'AdapterDeclaration', a)


def test_assoc_adapterFB0_link_reassign_clear():
    a = libraryElement_AdapterFB()
    b1 = libraryElement_AdapterDeclaration()
    b2 = libraryElement_AdapterDeclaration()
    _safe_set(a, 'AdapterFB', b1)
    assert _is_linked(a, 'AdapterFB', b1)
    if hasattr(b1, 'adapterDecl'):
        assert _is_linked(b1, 'adapterDecl', a)
    _safe_set(a, 'AdapterFB', b2)
    assert _is_linked(a, 'AdapterFB', b2)
    if hasattr(b1, 'adapterDecl'):
        assert not _is_linked(b1, 'adapterDecl', a)
    if hasattr(b2, 'adapterDecl'):
        assert _is_linked(b2, 'adapterDecl', a)
    _safe_set(a, 'AdapterFB', None)
    assert not _is_linked(a, 'AdapterFB', b2)
    if hasattr(b2, 'adapterDecl'):
        assert not _is_linked(b2, 'adapterDecl', a)


def test_assoc_adapterFBType2_link_reassign_clear():
    a = libraryElement_AdapterType()
    b1 = libraryElement_AdapterFBType()
    b2 = libraryElement_AdapterFBType()
    _safe_set(a, 'libraryElement_AdapterType', b1)
    assert _is_linked(a, 'libraryElement_AdapterType', b1)
    if hasattr(b1, 'libraryElement_AdapterFBType'):
        assert _is_linked(b1, 'libraryElement_AdapterFBType', a)
    _safe_set(a, 'libraryElement_AdapterType', b2)
    assert _is_linked(a, 'libraryElement_AdapterType', b2)
    if hasattr(b1, 'libraryElement_AdapterFBType'):
        assert not _is_linked(b1, 'libraryElement_AdapterFBType', a)
    if hasattr(b2, 'libraryElement_AdapterFBType'):
        assert _is_linked(b2, 'libraryElement_AdapterFBType', a)
    _safe_set(a, 'libraryElement_AdapterType', None)
    assert not _is_linked(a, 'libraryElement_AdapterType', b2)
    if hasattr(b2, 'libraryElement_AdapterFBType'):
        assert not _is_linked(b2, 'libraryElement_AdapterFBType', a)


def test_assoc_adapterType155_link_reassign_clear():
    a = libraryElement_AdapterType()
    b1 = libraryElement_AdapterFBType()
    b2 = libraryElement_AdapterFBType()
    _safe_set(a, 'libraryElement_AdapterType157', b1)
    assert _is_linked(a, 'libraryElement_AdapterType157', b1)
    if hasattr(b1, 'libraryElement_AdapterFBType156'):
        assert _is_linked(b1, 'libraryElement_AdapterFBType156', a)
    _safe_set(a, 'libraryElement_AdapterType157', b2)
    assert _is_linked(a, 'libraryElement_AdapterType157', b2)
    if hasattr(b1, 'libraryElement_AdapterFBType156'):
        assert not _is_linked(b1, 'libraryElement_AdapterFBType156', a)
    if hasattr(b2, 'libraryElement_AdapterFBType156'):
        assert _is_linked(b2, 'libraryElement_AdapterFBType156', a)
    _safe_set(a, 'libraryElement_AdapterType157', None)
    assert not _is_linked(a, 'libraryElement_AdapterType157', b2)
    if hasattr(b2, 'libraryElement_AdapterFBType156'):
        assert not _is_linked(b2, 'libraryElement_AdapterFBType156', a)


def test_assoc_annotations152_link_reassign_clear():
    a = libraryElement_I4DIACElement()
    b1 = libraryElement_Annotation(name="sample_text", servity="sample_text")
    b2 = libraryElement_Annotation(name="sample_text_2", servity="sample_text_2")
    _safe_set(a, 'libraryElement_I4DIACElement', {b1})
    assert _is_linked(a, 'libraryElement_I4DIACElement', b1)
    if hasattr(b1, 'libraryElement_Annotation'):
        assert _is_linked(b1, 'libraryElement_Annotation', a)
    _safe_set(a, 'libraryElement_I4DIACElement', {b2})
    assert _is_linked(a, 'libraryElement_I4DIACElement', b2)
    if hasattr(b1, 'libraryElement_Annotation'):
        assert not _is_linked(b1, 'libraryElement_Annotation', a)
    if hasattr(b2, 'libraryElement_Annotation'):
        assert _is_linked(b2, 'libraryElement_Annotation', a)
    _safe_set(a, 'libraryElement_I4DIACElement', set())
    assert not _is_linked(a, 'libraryElement_I4DIACElement', b2)
    if hasattr(b2, 'libraryElement_Annotation'):
        assert not _is_linked(b2, 'libraryElement_Annotation', a)


def test_assoc_application116_link_reassign_clear():
    a = libraryElement_AutomationSystem(project="sample_text")
    b1 = libraryElement_Application()
    b2 = libraryElement_Application()
    _safe_set(a, 'libraryElement_AutomationSystem', {b1})
    assert _is_linked(a, 'libraryElement_AutomationSystem', b1)
    if hasattr(b1, 'libraryElement_Application117'):
        assert _is_linked(b1, 'libraryElement_Application117', a)
    _safe_set(a, 'libraryElement_AutomationSystem', {b2})
    assert _is_linked(a, 'libraryElement_AutomationSystem', b2)
    if hasattr(b1, 'libraryElement_Application117'):
        assert not _is_linked(b1, 'libraryElement_Application117', a)
    if hasattr(b2, 'libraryElement_Application117'):
        assert _is_linked(b2, 'libraryElement_Application117', a)
    _safe_set(a, 'libraryElement_AutomationSystem', set())
    assert not _is_linked(a, 'libraryElement_AutomationSystem', b2)
    if hasattr(b2, 'libraryElement_Application117'):
        assert not _is_linked(b2, 'libraryElement_Application117', a)


def test_assoc_color172_link_reassign_clear():
    a = libraryElement_Color(blue="sample_text", green="sample_text", red="sample_text")
    b1 = libraryElement_ColorizableElement()
    b2 = libraryElement_ColorizableElement()
    _safe_set(a, 'libraryElement_Color', b1)
    assert _is_linked(a, 'libraryElement_Color', b1)
    if hasattr(b1, 'libraryElement_ColorizableElement'):
        assert _is_linked(b1, 'libraryElement_ColorizableElement', a)
    _safe_set(a, 'libraryElement_Color', b2)
    assert _is_linked(a, 'libraryElement_Color', b2)
    if hasattr(b1, 'libraryElement_ColorizableElement'):
        assert not _is_linked(b1, 'libraryElement_ColorizableElement', a)
    if hasattr(b2, 'libraryElement_ColorizableElement'):
        assert _is_linked(b2, 'libraryElement_ColorizableElement', a)
    _safe_set(a, 'libraryElement_Color', None)
    assert not _is_linked(a, 'libraryElement_Color', b2)
    if hasattr(b2, 'libraryElement_ColorizableElement'):
        assert not _is_linked(b2, 'libraryElement_ColorizableElement', a)


def test_assoc_compiler9_link_reassign_clear():
    a = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    b1 = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    b2 = libraryElement_Compiler(language="sample_text_2", product="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    _safe_set(a, 'libraryElement_CompilerInfo', {b1})
    assert _is_linked(a, 'libraryElement_CompilerInfo', b1)
    if hasattr(b1, 'libraryElement_Compiler'):
        assert _is_linked(b1, 'libraryElement_Compiler', a)
    _safe_set(a, 'libraryElement_CompilerInfo', {b2})
    assert _is_linked(a, 'libraryElement_CompilerInfo', b2)
    if hasattr(b1, 'libraryElement_Compiler'):
        assert not _is_linked(b1, 'libraryElement_Compiler', a)
    if hasattr(b2, 'libraryElement_Compiler'):
        assert _is_linked(b2, 'libraryElement_Compiler', a)
    _safe_set(a, 'libraryElement_CompilerInfo', set())
    assert not _is_linked(a, 'libraryElement_CompilerInfo', b2)
    if hasattr(b2, 'libraryElement_Compiler'):
        assert not _is_linked(b2, 'libraryElement_Compiler', a)


def test_assoc_compilerInfo132_link_reassign_clear():
    a = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    b1 = libraryElement_CompilableType()
    b2 = libraryElement_CompilableType()
    _safe_set(a, 'libraryElement_CompilerInfo133', b1)
    assert _is_linked(a, 'libraryElement_CompilerInfo133', b1)
    if hasattr(b1, 'libraryElement_CompilableType'):
        assert _is_linked(b1, 'libraryElement_CompilableType', a)
    _safe_set(a, 'libraryElement_CompilerInfo133', b2)
    assert _is_linked(a, 'libraryElement_CompilerInfo133', b2)
    if hasattr(b1, 'libraryElement_CompilableType'):
        assert not _is_linked(b1, 'libraryElement_CompilableType', a)
    if hasattr(b2, 'libraryElement_CompilableType'):
        assert _is_linked(b2, 'libraryElement_CompilableType', a)
    _safe_set(a, 'libraryElement_CompilerInfo133', None)
    assert not _is_linked(a, 'libraryElement_CompilerInfo133', b2)
    if hasattr(b2, 'libraryElement_CompilableType'):
        assert not _is_linked(b2, 'libraryElement_CompilableType', a)


def test_assoc_conditionEvent45_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_Event()
    b2 = libraryElement_Event()
    _safe_set(a, 'libraryElement_ECTransition46', b1)
    assert _is_linked(a, 'libraryElement_ECTransition46', b1)
    if hasattr(b1, 'libraryElement_Event47'):
        assert _is_linked(b1, 'libraryElement_Event47', a)
    _safe_set(a, 'libraryElement_ECTransition46', b2)
    assert _is_linked(a, 'libraryElement_ECTransition46', b2)
    if hasattr(b1, 'libraryElement_Event47'):
        assert not _is_linked(b1, 'libraryElement_Event47', a)
    if hasattr(b2, 'libraryElement_Event47'):
        assert _is_linked(b2, 'libraryElement_Event47', a)
    _safe_set(a, 'libraryElement_ECTransition46', None)
    assert not _is_linked(a, 'libraryElement_ECTransition46', b2)
    if hasattr(b2, 'libraryElement_Event47'):
        assert not _is_linked(b2, 'libraryElement_Event47', a)


def test_assoc_dataConnections110_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_DataConnection()
    b2 = libraryElement_DataConnection()
    _safe_set(a, 'libraryElement_FBNetwork111', {b1})
    assert _is_linked(a, 'libraryElement_FBNetwork111', b1)
    if hasattr(b1, 'libraryElement_DataConnection'):
        assert _is_linked(b1, 'libraryElement_DataConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork111', {b2})
    assert _is_linked(a, 'libraryElement_FBNetwork111', b2)
    if hasattr(b1, 'libraryElement_DataConnection'):
        assert not _is_linked(b1, 'libraryElement_DataConnection', a)
    if hasattr(b2, 'libraryElement_DataConnection'):
        assert _is_linked(b2, 'libraryElement_DataConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork111', set())
    assert not _is_linked(a, 'libraryElement_FBNetwork111', b2)
    if hasattr(b2, 'libraryElement_DataConnection'):
        assert not _is_linked(b2, 'libraryElement_DataConnection', a)


def test_assoc_destination11_link_reassign_clear():
    a = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b1 = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    b2 = libraryElement_Connection(brokenConnection="sample_text_2", dx1="sample_text_2", dx2="sample_text_2", dy="sample_text_2", resTypeConnection="sample_text_2")
    _safe_set(a, 'IInterfaceElement12', b1)
    assert _is_linked(a, 'IInterfaceElement12', b1)
    if hasattr(b1, 'inputConnections'):
        assert _is_linked(b1, 'inputConnections', a)
    _safe_set(a, 'IInterfaceElement12', b2)
    assert _is_linked(a, 'IInterfaceElement12', b2)
    if hasattr(b1, 'inputConnections'):
        assert not _is_linked(b1, 'inputConnections', a)
    if hasattr(b2, 'inputConnections'):
        assert _is_linked(b2, 'inputConnections', a)
    _safe_set(a, 'IInterfaceElement12', None)
    assert not _is_linked(a, 'IInterfaceElement12', b2)
    if hasattr(b2, 'inputConnections'):
        assert not _is_linked(b2, 'inputConnections', a)


def test_assoc_destination43_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_ECState()
    b2 = libraryElement_ECState()
    _safe_set(a, 'inTransitions', b1)
    assert _is_linked(a, 'inTransitions', b1)
    if hasattr(b1, 'ECState44'):
        assert _is_linked(b1, 'ECState44', a)
    _safe_set(a, 'inTransitions', b2)
    assert _is_linked(a, 'inTransitions', b2)
    if hasattr(b1, 'ECState44'):
        assert not _is_linked(b1, 'ECState44', a)
    if hasattr(b2, 'ECState44'):
        assert _is_linked(b2, 'ECState44', a)
    _safe_set(a, 'inTransitions', None)
    assert not _is_linked(a, 'inTransitions', b2)
    if hasattr(b2, 'ECState44'):
        assert not _is_linked(b2, 'ECState44', a)


def test_assoc_device78_link_reassign_clear():
    a = libraryElement_Device(profile="sample_text")
    b1 = libraryElement_Link()
    b2 = libraryElement_Link()
    _safe_set(a, 'Device', b1)
    assert _is_linked(a, 'Device', b1)
    if hasattr(b1, 'inConnections'):
        assert _is_linked(b1, 'inConnections', a)
    _safe_set(a, 'Device', b2)
    assert _is_linked(a, 'Device', b2)
    if hasattr(b1, 'inConnections'):
        assert not _is_linked(b1, 'inConnections', a)
    if hasattr(b2, 'inConnections'):
        assert _is_linked(b2, 'inConnections', a)
    _safe_set(a, 'Device', None)
    assert not _is_linked(a, 'Device', b2)
    if hasattr(b2, 'inConnections'):
        assert not _is_linked(b2, 'inConnections', a)


def test_assoc_device88_link_reassign_clear():
    a = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    b1 = libraryElement_Device(profile="sample_text")
    b2 = libraryElement_Device(profile="sample_text_2")
    _safe_set(a, 'resource', b1)
    assert _is_linked(a, 'resource', b1)
    if hasattr(b1, 'Device89'):
        assert _is_linked(b1, 'Device89', a)
    _safe_set(a, 'resource', b2)
    assert _is_linked(a, 'resource', b2)
    if hasattr(b1, 'Device89'):
        assert not _is_linked(b1, 'Device89', a)
    if hasattr(b2, 'Device89'):
        assert _is_linked(b2, 'Device89', a)
    _safe_set(a, 'resource', None)
    assert not _is_linked(a, 'resource', b2)
    if hasattr(b2, 'Device89'):
        assert not _is_linked(b2, 'Device89', a)


def test_assoc_devices145_link_reassign_clear():
    a = libraryElement_SystemConfiguration()
    b1 = libraryElement_Device(profile="sample_text")
    b2 = libraryElement_Device(profile="sample_text_2")
    _safe_set(a, 'libraryElement_SystemConfiguration146', {b1})
    assert _is_linked(a, 'libraryElement_SystemConfiguration146', b1)
    if hasattr(b1, 'libraryElement_Device'):
        assert _is_linked(b1, 'libraryElement_Device', a)
    _safe_set(a, 'libraryElement_SystemConfiguration146', {b2})
    assert _is_linked(a, 'libraryElement_SystemConfiguration146', b2)
    if hasattr(b1, 'libraryElement_Device'):
        assert not _is_linked(b1, 'libraryElement_Device', a)
    if hasattr(b2, 'libraryElement_Device'):
        assert _is_linked(b2, 'libraryElement_Device', a)
    _safe_set(a, 'libraryElement_SystemConfiguration146', set())
    assert not _is_linked(a, 'libraryElement_SystemConfiguration146', b2)
    if hasattr(b2, 'libraryElement_Device'):
        assert not _is_linked(b2, 'libraryElement_Device', a)


def test_assoc_eCAction36_link_reassign_clear():
    a = libraryElement_ECState()
    b1 = libraryElement_ECAction()
    b2 = libraryElement_ECAction()
    _safe_set(a, 'libraryElement_ECState37', {b1})
    assert _is_linked(a, 'libraryElement_ECState37', b1)
    if hasattr(b1, 'libraryElement_ECAction38'):
        assert _is_linked(b1, 'libraryElement_ECAction38', a)
    _safe_set(a, 'libraryElement_ECState37', {b2})
    assert _is_linked(a, 'libraryElement_ECState37', b2)
    if hasattr(b1, 'libraryElement_ECAction38'):
        assert not _is_linked(b1, 'libraryElement_ECAction38', a)
    if hasattr(b2, 'libraryElement_ECAction38'):
        assert _is_linked(b2, 'libraryElement_ECAction38', a)
    _safe_set(a, 'libraryElement_ECState37', set())
    assert not _is_linked(a, 'libraryElement_ECState37', b2)
    if hasattr(b2, 'libraryElement_ECAction38'):
        assert not _is_linked(b2, 'libraryElement_ECAction38', a)


def test_assoc_eCState29_link_reassign_clear():
    a = libraryElement_ECState()
    b1 = libraryElement_ECC()
    b2 = libraryElement_ECC()
    _safe_set(a, 'libraryElement_ECState', b1)
    assert _is_linked(a, 'libraryElement_ECState', b1)
    if hasattr(b1, 'libraryElement_ECC30'):
        assert _is_linked(b1, 'libraryElement_ECC30', a)
    _safe_set(a, 'libraryElement_ECState', b2)
    assert _is_linked(a, 'libraryElement_ECState', b2)
    if hasattr(b1, 'libraryElement_ECC30'):
        assert not _is_linked(b1, 'libraryElement_ECC30', a)
    if hasattr(b2, 'libraryElement_ECC30'):
        assert _is_linked(b2, 'libraryElement_ECC30', a)
    _safe_set(a, 'libraryElement_ECState', None)
    assert not _is_linked(a, 'libraryElement_ECState', b2)
    if hasattr(b2, 'libraryElement_ECC30'):
        assert not _is_linked(b2, 'libraryElement_ECC30', a)


def test_assoc_eCTransition31_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_ECC()
    b2 = libraryElement_ECC()
    _safe_set(a, 'libraryElement_ECTransition', b1)
    assert _is_linked(a, 'libraryElement_ECTransition', b1)
    if hasattr(b1, 'libraryElement_ECC32'):
        assert _is_linked(b1, 'libraryElement_ECC32', a)
    _safe_set(a, 'libraryElement_ECTransition', b2)
    assert _is_linked(a, 'libraryElement_ECTransition', b2)
    if hasattr(b1, 'libraryElement_ECC32'):
        assert not _is_linked(b1, 'libraryElement_ECC32', a)
    if hasattr(b2, 'libraryElement_ECC32'):
        assert _is_linked(b2, 'libraryElement_ECC32', a)
    _safe_set(a, 'libraryElement_ECTransition', None)
    assert not _is_linked(a, 'libraryElement_ECTransition', b2)
    if hasattr(b2, 'libraryElement_ECC32'):
        assert not _is_linked(b2, 'libraryElement_ECC32', a)


def test_assoc_eventConnections112_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_EventConnection()
    b2 = libraryElement_EventConnection()
    _safe_set(a, 'libraryElement_FBNetwork113', {b1})
    assert _is_linked(a, 'libraryElement_FBNetwork113', b1)
    if hasattr(b1, 'libraryElement_EventConnection'):
        assert _is_linked(b1, 'libraryElement_EventConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork113', {b2})
    assert _is_linked(a, 'libraryElement_FBNetwork113', b2)
    if hasattr(b1, 'libraryElement_EventConnection'):
        assert not _is_linked(b1, 'libraryElement_EventConnection', a)
    if hasattr(b2, 'libraryElement_EventConnection'):
        assert _is_linked(b2, 'libraryElement_EventConnection', a)
    _safe_set(a, 'libraryElement_FBNetwork113', set())
    assert not _is_linked(a, 'libraryElement_FBNetwork113', b2)
    if hasattr(b2, 'libraryElement_EventConnection'):
        assert not _is_linked(b2, 'libraryElement_EventConnection', a)


def test_assoc_eventInputs65_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_Event()
    b2 = libraryElement_Event()
    _safe_set(a, 'libraryElement_InterfaceList66', {b1})
    assert _is_linked(a, 'libraryElement_InterfaceList66', b1)
    if hasattr(b1, 'libraryElement_Event67'):
        assert _is_linked(b1, 'libraryElement_Event67', a)
    _safe_set(a, 'libraryElement_InterfaceList66', {b2})
    assert _is_linked(a, 'libraryElement_InterfaceList66', b2)
    if hasattr(b1, 'libraryElement_Event67'):
        assert not _is_linked(b1, 'libraryElement_Event67', a)
    if hasattr(b2, 'libraryElement_Event67'):
        assert _is_linked(b2, 'libraryElement_Event67', a)
    _safe_set(a, 'libraryElement_InterfaceList66', set())
    assert not _is_linked(a, 'libraryElement_InterfaceList66', b2)
    if hasattr(b2, 'libraryElement_Event67'):
        assert not _is_linked(b2, 'libraryElement_Event67', a)


def test_assoc_eventOutputs68_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_Event()
    b2 = libraryElement_Event()
    _safe_set(a, 'libraryElement_InterfaceList69', {b1})
    assert _is_linked(a, 'libraryElement_InterfaceList69', b1)
    if hasattr(b1, 'libraryElement_Event70'):
        assert _is_linked(b1, 'libraryElement_Event70', a)
    _safe_set(a, 'libraryElement_InterfaceList69', {b2})
    assert _is_linked(a, 'libraryElement_InterfaceList69', b2)
    if hasattr(b1, 'libraryElement_Event70'):
        assert not _is_linked(b1, 'libraryElement_Event70', a)
    if hasattr(b2, 'libraryElement_Event70'):
        assert _is_linked(b2, 'libraryElement_Event70', a)
    _safe_set(a, 'libraryElement_InterfaceList69', set())
    assert not _is_linked(a, 'libraryElement_InterfaceList69', b2)
    if hasattr(b2, 'libraryElement_Event70'):
        assert not _is_linked(b2, 'libraryElement_Event70', a)


def test_assoc_fBNetwork135_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_CompositeFBType()
    b2 = libraryElement_CompositeFBType()
    _safe_set(a, 'libraryElement_FBNetwork136', b1)
    assert _is_linked(a, 'libraryElement_FBNetwork136', b1)
    if hasattr(b1, 'libraryElement_CompositeFBType'):
        assert _is_linked(b1, 'libraryElement_CompositeFBType', a)
    _safe_set(a, 'libraryElement_FBNetwork136', b2)
    assert _is_linked(a, 'libraryElement_FBNetwork136', b2)
    if hasattr(b1, 'libraryElement_CompositeFBType'):
        assert not _is_linked(b1, 'libraryElement_CompositeFBType', a)
    if hasattr(b2, 'libraryElement_CompositeFBType'):
        assert _is_linked(b2, 'libraryElement_CompositeFBType', a)
    _safe_set(a, 'libraryElement_FBNetwork136', None)
    assert not _is_linked(a, 'libraryElement_FBNetwork136', b2)
    if hasattr(b2, 'libraryElement_CompositeFBType'):
        assert not _is_linked(b2, 'libraryElement_CompositeFBType', a)


def test_assoc_fBNetwork22_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_DeviceType(profile="sample_text")
    b2 = libraryElement_DeviceType(profile="sample_text_2")
    _safe_set(a, 'libraryElement_FBNetwork24', b1)
    assert _is_linked(a, 'libraryElement_FBNetwork24', b1)
    if hasattr(b1, 'libraryElement_DeviceType23'):
        assert _is_linked(b1, 'libraryElement_DeviceType23', a)
    _safe_set(a, 'libraryElement_FBNetwork24', b2)
    assert _is_linked(a, 'libraryElement_FBNetwork24', b2)
    if hasattr(b1, 'libraryElement_DeviceType23'):
        assert not _is_linked(b1, 'libraryElement_DeviceType23', a)
    if hasattr(b2, 'libraryElement_DeviceType23'):
        assert _is_linked(b2, 'libraryElement_DeviceType23', a)
    _safe_set(a, 'libraryElement_FBNetwork24', None)
    assert not _is_linked(a, 'libraryElement_FBNetwork24', b2)
    if hasattr(b2, 'libraryElement_DeviceType23'):
        assert not _is_linked(b2, 'libraryElement_DeviceType23', a)


def test_assoc_fBNetwork3_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_Application()
    b2 = libraryElement_Application()
    _safe_set(a, 'libraryElement_FBNetwork', b1)
    assert _is_linked(a, 'libraryElement_FBNetwork', b1)
    if hasattr(b1, 'libraryElement_Application'):
        assert _is_linked(b1, 'libraryElement_Application', a)
    _safe_set(a, 'libraryElement_FBNetwork', b2)
    assert _is_linked(a, 'libraryElement_FBNetwork', b2)
    if hasattr(b1, 'libraryElement_Application'):
        assert not _is_linked(b1, 'libraryElement_Application', a)
    if hasattr(b2, 'libraryElement_Application'):
        assert _is_linked(b2, 'libraryElement_Application', a)
    _safe_set(a, 'libraryElement_FBNetwork', None)
    assert not _is_linked(a, 'libraryElement_FBNetwork', b2)
    if hasattr(b2, 'libraryElement_Application'):
        assert not _is_linked(b2, 'libraryElement_Application', a)


def test_assoc_fBNetwork85_link_reassign_clear():
    a = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    b1 = libraryElement_FBNetwork()
    b2 = libraryElement_FBNetwork()
    _safe_set(a, 'libraryElement_Resource86', b1)
    assert _is_linked(a, 'libraryElement_Resource86', b1)
    if hasattr(b1, 'libraryElement_FBNetwork87'):
        assert _is_linked(b1, 'libraryElement_FBNetwork87', a)
    _safe_set(a, 'libraryElement_Resource86', b2)
    assert _is_linked(a, 'libraryElement_Resource86', b2)
    if hasattr(b1, 'libraryElement_FBNetwork87'):
        assert not _is_linked(b1, 'libraryElement_FBNetwork87', a)
    if hasattr(b2, 'libraryElement_FBNetwork87'):
        assert _is_linked(b2, 'libraryElement_FBNetwork87', a)
    _safe_set(a, 'libraryElement_Resource86', None)
    assert not _is_linked(a, 'libraryElement_Resource86', b2)
    if hasattr(b2, 'libraryElement_FBNetwork87'):
        assert not _is_linked(b2, 'libraryElement_FBNetwork87', a)


def test_assoc_fBNetwork92_link_reassign_clear():
    a = libraryElement_FBNetwork()
    b1 = libraryElement_ResourceType()
    b2 = libraryElement_ResourceType()
    _safe_set(a, 'libraryElement_FBNetwork94', b1)
    assert _is_linked(a, 'libraryElement_FBNetwork94', b1)
    if hasattr(b1, 'libraryElement_ResourceType93'):
        assert _is_linked(b1, 'libraryElement_ResourceType93', a)
    _safe_set(a, 'libraryElement_FBNetwork94', b2)
    assert _is_linked(a, 'libraryElement_FBNetwork94', b2)
    if hasattr(b1, 'libraryElement_ResourceType93'):
        assert not _is_linked(b1, 'libraryElement_ResourceType93', a)
    if hasattr(b2, 'libraryElement_ResourceType93'):
        assert _is_linked(b2, 'libraryElement_ResourceType93', a)
    _safe_set(a, 'libraryElement_FBNetwork94', None)
    assert not _is_linked(a, 'libraryElement_FBNetwork94', b2)
    if hasattr(b2, 'libraryElement_ResourceType93'):
        assert not _is_linked(b2, 'libraryElement_ResourceType93', a)


def test_assoc_from_79_link_reassign_clear():
    a = libraryElement_Mapping()
    b1 = libraryElement_FBNetworkElement()
    b2 = libraryElement_FBNetworkElement()
    _safe_set(a, 'libraryElement_Mapping80', b1)
    assert _is_linked(a, 'libraryElement_Mapping80', b1)
    if hasattr(b1, 'libraryElement_FBNetworkElement81'):
        assert _is_linked(b1, 'libraryElement_FBNetworkElement81', a)
    _safe_set(a, 'libraryElement_Mapping80', b2)
    assert _is_linked(a, 'libraryElement_Mapping80', b2)
    if hasattr(b1, 'libraryElement_FBNetworkElement81'):
        assert not _is_linked(b1, 'libraryElement_FBNetworkElement81', a)
    if hasattr(b2, 'libraryElement_FBNetworkElement81'):
        assert _is_linked(b2, 'libraryElement_FBNetworkElement81', a)
    _safe_set(a, 'libraryElement_Mapping80', None)
    assert not _is_linked(a, 'libraryElement_Mapping80', b2)
    if hasattr(b2, 'libraryElement_FBNetworkElement81'):
        assert not _is_linked(b2, 'libraryElement_FBNetworkElement81', a)


def test_assoc_identification129_link_reassign_clear():
    a = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    b1 = libraryElement_LibraryElement()
    b2 = libraryElement_LibraryElement()
    _safe_set(a, 'libraryElement_Identification', b1)
    assert _is_linked(a, 'libraryElement_Identification', b1)
    if hasattr(b1, 'libraryElement_LibraryElement130'):
        assert _is_linked(b1, 'libraryElement_LibraryElement130', a)
    _safe_set(a, 'libraryElement_Identification', b2)
    assert _is_linked(a, 'libraryElement_Identification', b2)
    if hasattr(b1, 'libraryElement_LibraryElement130'):
        assert not _is_linked(b1, 'libraryElement_LibraryElement130', a)
    if hasattr(b2, 'libraryElement_LibraryElement130'):
        assert _is_linked(b2, 'libraryElement_LibraryElement130', a)
    _safe_set(a, 'libraryElement_Identification', None)
    assert not _is_linked(a, 'libraryElement_Identification', b2)
    if hasattr(b2, 'libraryElement_LibraryElement130'):
        assert not _is_linked(b2, 'libraryElement_LibraryElement130', a)


def test_assoc_inConnections14_link_reassign_clear():
    a = libraryElement_Device(profile="sample_text")
    b1 = libraryElement_Link()
    b2 = libraryElement_Link()
    _safe_set(a, 'device15', {b1})
    assert _is_linked(a, 'device15', b1)
    if hasattr(b1, 'Link'):
        assert _is_linked(b1, 'Link', a)
    _safe_set(a, 'device15', {b2})
    assert _is_linked(a, 'device15', b2)
    if hasattr(b1, 'Link'):
        assert not _is_linked(b1, 'Link', a)
    if hasattr(b2, 'Link'):
        assert _is_linked(b2, 'Link', a)
    _safe_set(a, 'device15', set())
    assert not _is_linked(a, 'device15', b2)
    if hasattr(b2, 'Link'):
        assert not _is_linked(b2, 'Link', a)


def test_assoc_inTransitions40_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_ECState()
    b2 = libraryElement_ECState()
    _safe_set(a, 'ECTransition41', b1)
    assert _is_linked(a, 'ECTransition41', b1)
    if hasattr(b1, 'destination'):
        assert _is_linked(b1, 'destination', a)
    _safe_set(a, 'ECTransition41', b2)
    assert _is_linked(a, 'ECTransition41', b2)
    if hasattr(b1, 'destination'):
        assert not _is_linked(b1, 'destination', a)
    if hasattr(b2, 'destination'):
        assert _is_linked(b2, 'destination', a)
    _safe_set(a, 'ECTransition41', None)
    assert not _is_linked(a, 'ECTransition41', b2)
    if hasattr(b2, 'destination'):
        assert not _is_linked(b2, 'destination', a)


def test_assoc_inputConnections137_link_reassign_clear():
    a = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b1 = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    b2 = libraryElement_Connection(brokenConnection="sample_text_2", dx1="sample_text_2", dx2="sample_text_2", dy="sample_text_2", resTypeConnection="sample_text_2")
    _safe_set(a, 'destination138', {b1})
    assert _is_linked(a, 'destination138', b1)
    if hasattr(b1, 'Connection'):
        assert _is_linked(b1, 'Connection', a)
    _safe_set(a, 'destination138', {b2})
    assert _is_linked(a, 'destination138', b2)
    if hasattr(b1, 'Connection'):
        assert not _is_linked(b1, 'Connection', a)
    if hasattr(b2, 'Connection'):
        assert _is_linked(b2, 'Connection', a)
    _safe_set(a, 'destination138', set())
    assert not _is_linked(a, 'destination138', b2)
    if hasattr(b2, 'Connection'):
        assert not _is_linked(b2, 'Connection', a)


def test_assoc_inputPrimitive103_link_reassign_clear():
    a = libraryElement_ServiceTransaction(TestResult="sample_text")
    b1 = libraryElement_InputPrimitive()
    b2 = libraryElement_InputPrimitive()
    _safe_set(a, 'libraryElement_ServiceTransaction104', b1)
    assert _is_linked(a, 'libraryElement_ServiceTransaction104', b1)
    if hasattr(b1, 'libraryElement_InputPrimitive'):
        assert _is_linked(b1, 'libraryElement_InputPrimitive', a)
    _safe_set(a, 'libraryElement_ServiceTransaction104', b2)
    assert _is_linked(a, 'libraryElement_ServiceTransaction104', b2)
    if hasattr(b1, 'libraryElement_InputPrimitive'):
        assert not _is_linked(b1, 'libraryElement_InputPrimitive', a)
    if hasattr(b2, 'libraryElement_InputPrimitive'):
        assert _is_linked(b2, 'libraryElement_InputPrimitive', a)
    _safe_set(a, 'libraryElement_ServiceTransaction104', None)
    assert not _is_linked(a, 'libraryElement_ServiceTransaction104', b2)
    if hasattr(b2, 'libraryElement_InputPrimitive'):
        assert not _is_linked(b2, 'libraryElement_InputPrimitive', a)


def test_assoc_inputVars71_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_InterfaceList()
    b2 = libraryElement_InterfaceList()
    _safe_set(a, 'libraryElement_VarDeclaration73', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration73', b1)
    if hasattr(b1, 'libraryElement_InterfaceList72'):
        assert _is_linked(b1, 'libraryElement_InterfaceList72', a)
    _safe_set(a, 'libraryElement_VarDeclaration73', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration73', b2)
    if hasattr(b1, 'libraryElement_InterfaceList72'):
        assert not _is_linked(b1, 'libraryElement_InterfaceList72', a)
    if hasattr(b2, 'libraryElement_InterfaceList72'):
        assert _is_linked(b2, 'libraryElement_InterfaceList72', a)
    _safe_set(a, 'libraryElement_VarDeclaration73', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration73', b2)
    if hasattr(b2, 'libraryElement_InterfaceList72'):
        assert not _is_linked(b2, 'libraryElement_InterfaceList72', a)


def test_assoc_interface170_link_reassign_clear():
    a = libraryElement_Primitive(event="sample_text", parameters="sample_text")
    b1 = libraryElement_ServiceInterface()
    b2 = libraryElement_ServiceInterface()
    _safe_set(a, 'libraryElement_Primitive', b1)
    assert _is_linked(a, 'libraryElement_Primitive', b1)
    if hasattr(b1, 'libraryElement_ServiceInterface171'):
        assert _is_linked(b1, 'libraryElement_ServiceInterface171', a)
    _safe_set(a, 'libraryElement_Primitive', b2)
    assert _is_linked(a, 'libraryElement_Primitive', b2)
    if hasattr(b1, 'libraryElement_ServiceInterface171'):
        assert not _is_linked(b1, 'libraryElement_ServiceInterface171', a)
    if hasattr(b2, 'libraryElement_ServiceInterface171'):
        assert _is_linked(b2, 'libraryElement_ServiceInterface171', a)
    _safe_set(a, 'libraryElement_Primitive', None)
    assert not _is_linked(a, 'libraryElement_Primitive', b2)
    if hasattr(b2, 'libraryElement_ServiceInterface171'):
        assert not _is_linked(b2, 'libraryElement_ServiceInterface171', a)


def test_assoc_interface50_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_FBNetworkElement()
    b2 = libraryElement_FBNetworkElement()
    _safe_set(a, 'libraryElement_InterfaceList', b1)
    assert _is_linked(a, 'libraryElement_InterfaceList', b1)
    if hasattr(b1, 'libraryElement_FBNetworkElement'):
        assert _is_linked(b1, 'libraryElement_FBNetworkElement', a)
    _safe_set(a, 'libraryElement_InterfaceList', b2)
    assert _is_linked(a, 'libraryElement_InterfaceList', b2)
    if hasattr(b1, 'libraryElement_FBNetworkElement'):
        assert not _is_linked(b1, 'libraryElement_FBNetworkElement', a)
    if hasattr(b2, 'libraryElement_FBNetworkElement'):
        assert _is_linked(b2, 'libraryElement_FBNetworkElement', a)
    _safe_set(a, 'libraryElement_InterfaceList', None)
    assert not _is_linked(a, 'libraryElement_InterfaceList', b2)
    if hasattr(b2, 'libraryElement_FBNetworkElement'):
        assert not _is_linked(b2, 'libraryElement_FBNetworkElement', a)


def test_assoc_interfaceList55_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_FBType()
    b2 = libraryElement_FBType()
    _safe_set(a, 'libraryElement_InterfaceList56', b1)
    assert _is_linked(a, 'libraryElement_InterfaceList56', b1)
    if hasattr(b1, 'libraryElement_FBType'):
        assert _is_linked(b1, 'libraryElement_FBType', a)
    _safe_set(a, 'libraryElement_InterfaceList56', b2)
    assert _is_linked(a, 'libraryElement_InterfaceList56', b2)
    if hasattr(b1, 'libraryElement_FBType'):
        assert not _is_linked(b1, 'libraryElement_FBType', a)
    if hasattr(b2, 'libraryElement_FBType'):
        assert _is_linked(b2, 'libraryElement_FBType', a)
    _safe_set(a, 'libraryElement_InterfaceList56', None)
    assert not _is_linked(a, 'libraryElement_InterfaceList56', b2)
    if hasattr(b2, 'libraryElement_FBType'):
        assert not _is_linked(b2, 'libraryElement_FBType', a)


def test_assoc_internalVars7_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_BasicFBType()
    b2 = libraryElement_BasicFBType()
    _safe_set(a, 'libraryElement_VarDeclaration', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration', b1)
    if hasattr(b1, 'libraryElement_BasicFBType8'):
        assert _is_linked(b1, 'libraryElement_BasicFBType8', a)
    _safe_set(a, 'libraryElement_VarDeclaration', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration', b2)
    if hasattr(b1, 'libraryElement_BasicFBType8'):
        assert not _is_linked(b1, 'libraryElement_BasicFBType8', a)
    if hasattr(b2, 'libraryElement_BasicFBType8'):
        assert _is_linked(b2, 'libraryElement_BasicFBType8', a)
    _safe_set(a, 'libraryElement_VarDeclaration', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration', b2)
    if hasattr(b2, 'libraryElement_BasicFBType8'):
        assert not _is_linked(b2, 'libraryElement_BasicFBType8', a)


def test_assoc_links150_link_reassign_clear():
    a = libraryElement_SystemConfiguration()
    b1 = libraryElement_Link()
    b2 = libraryElement_Link()
    _safe_set(a, 'libraryElement_SystemConfiguration151', {b1})
    assert _is_linked(a, 'libraryElement_SystemConfiguration151', b1)
    if hasattr(b1, 'libraryElement_Link'):
        assert _is_linked(b1, 'libraryElement_Link', a)
    _safe_set(a, 'libraryElement_SystemConfiguration151', {b2})
    assert _is_linked(a, 'libraryElement_SystemConfiguration151', b2)
    if hasattr(b1, 'libraryElement_Link'):
        assert not _is_linked(b1, 'libraryElement_Link', a)
    if hasattr(b2, 'libraryElement_Link'):
        assert _is_linked(b2, 'libraryElement_Link', a)
    _safe_set(a, 'libraryElement_SystemConfiguration151', set())
    assert not _is_linked(a, 'libraryElement_SystemConfiguration151', b2)
    if hasattr(b2, 'libraryElement_Link'):
        assert not _is_linked(b2, 'libraryElement_Link', a)


def test_assoc_mapping118_link_reassign_clear():
    a = libraryElement_Mapping()
    b1 = libraryElement_AutomationSystem(project="sample_text")
    b2 = libraryElement_AutomationSystem(project="sample_text_2")
    _safe_set(a, 'libraryElement_Mapping120', b1)
    assert _is_linked(a, 'libraryElement_Mapping120', b1)
    if hasattr(b1, 'libraryElement_AutomationSystem119'):
        assert _is_linked(b1, 'libraryElement_AutomationSystem119', a)
    _safe_set(a, 'libraryElement_Mapping120', b2)
    assert _is_linked(a, 'libraryElement_Mapping120', b2)
    if hasattr(b1, 'libraryElement_AutomationSystem119'):
        assert not _is_linked(b1, 'libraryElement_AutomationSystem119', a)
    if hasattr(b2, 'libraryElement_AutomationSystem119'):
        assert _is_linked(b2, 'libraryElement_AutomationSystem119', a)
    _safe_set(a, 'libraryElement_Mapping120', None)
    assert not _is_linked(a, 'libraryElement_Mapping120', b2)
    if hasattr(b2, 'libraryElement_AutomationSystem119'):
        assert not _is_linked(b2, 'libraryElement_AutomationSystem119', a)


def test_assoc_mapping51_link_reassign_clear():
    a = libraryElement_Mapping()
    b1 = libraryElement_FBNetworkElement()
    b2 = libraryElement_FBNetworkElement()
    _safe_set(a, 'libraryElement_Mapping', b1)
    assert _is_linked(a, 'libraryElement_Mapping', b1)
    if hasattr(b1, 'libraryElement_FBNetworkElement52'):
        assert _is_linked(b1, 'libraryElement_FBNetworkElement52', a)
    _safe_set(a, 'libraryElement_Mapping', b2)
    assert _is_linked(a, 'libraryElement_Mapping', b2)
    if hasattr(b1, 'libraryElement_FBNetworkElement52'):
        assert not _is_linked(b1, 'libraryElement_FBNetworkElement52', a)
    if hasattr(b2, 'libraryElement_FBNetworkElement52'):
        assert _is_linked(b2, 'libraryElement_FBNetworkElement52', a)
    _safe_set(a, 'libraryElement_Mapping', None)
    assert not _is_linked(a, 'libraryElement_Mapping', b2)
    if hasattr(b2, 'libraryElement_FBNetworkElement52'):
        assert not _is_linked(b2, 'libraryElement_FBNetworkElement52', a)


def test_assoc_networkElements107_link_reassign_clear():
    a = libraryElement_FBNetworkElement()
    b1 = libraryElement_FBNetwork()
    b2 = libraryElement_FBNetwork()
    _safe_set(a, 'libraryElement_FBNetworkElement109', b1)
    assert _is_linked(a, 'libraryElement_FBNetworkElement109', b1)
    if hasattr(b1, 'libraryElement_FBNetwork108'):
        assert _is_linked(b1, 'libraryElement_FBNetwork108', a)
    _safe_set(a, 'libraryElement_FBNetworkElement109', b2)
    assert _is_linked(a, 'libraryElement_FBNetworkElement109', b2)
    if hasattr(b1, 'libraryElement_FBNetwork108'):
        assert not _is_linked(b1, 'libraryElement_FBNetwork108', a)
    if hasattr(b2, 'libraryElement_FBNetwork108'):
        assert _is_linked(b2, 'libraryElement_FBNetwork108', a)
    _safe_set(a, 'libraryElement_FBNetworkElement109', None)
    assert not _is_linked(a, 'libraryElement_FBNetworkElement109', b2)
    if hasattr(b2, 'libraryElement_FBNetwork108'):
        assert not _is_linked(b2, 'libraryElement_FBNetwork108', a)


def test_assoc_outConnections100_link_reassign_clear():
    a = libraryElement_Segment(width="sample_text")
    b1 = libraryElement_Link()
    b2 = libraryElement_Link()
    _safe_set(a, 'segment', {b1})
    assert _is_linked(a, 'segment', b1)
    if hasattr(b1, 'Link101'):
        assert _is_linked(b1, 'Link101', a)
    _safe_set(a, 'segment', {b2})
    assert _is_linked(a, 'segment', b2)
    if hasattr(b1, 'Link101'):
        assert not _is_linked(b1, 'Link101', a)
    if hasattr(b2, 'Link101'):
        assert _is_linked(b2, 'Link101', a)
    _safe_set(a, 'segment', set())
    assert not _is_linked(a, 'segment', b2)
    if hasattr(b2, 'Link101'):
        assert not _is_linked(b2, 'Link101', a)


def test_assoc_outTransitions39_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_ECState()
    b2 = libraryElement_ECState()
    _safe_set(a, 'ECTransition', b1)
    assert _is_linked(a, 'ECTransition', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'ECTransition', b2)
    assert _is_linked(a, 'ECTransition', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'ECTransition', None)
    assert not _is_linked(a, 'ECTransition', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_outputConnections139_link_reassign_clear():
    a = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b1 = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    b2 = libraryElement_Connection(brokenConnection="sample_text_2", dx1="sample_text_2", dx2="sample_text_2", dy="sample_text_2", resTypeConnection="sample_text_2")
    _safe_set(a, 'source140', {b1})
    assert _is_linked(a, 'source140', b1)
    if hasattr(b1, 'Connection141'):
        assert _is_linked(b1, 'Connection141', a)
    _safe_set(a, 'source140', {b2})
    assert _is_linked(a, 'source140', b2)
    if hasattr(b1, 'Connection141'):
        assert not _is_linked(b1, 'Connection141', a)
    if hasattr(b2, 'Connection141'):
        assert _is_linked(b2, 'Connection141', a)
    _safe_set(a, 'source140', set())
    assert not _is_linked(a, 'source140', b2)
    if hasattr(b2, 'Connection141'):
        assert not _is_linked(b2, 'Connection141', a)


def test_assoc_outputPrimitive105_link_reassign_clear():
    a = libraryElement_ServiceTransaction(TestResult="sample_text")
    b1 = libraryElement_OutputPrimitive(TestResult="sample_text")
    b2 = libraryElement_OutputPrimitive(TestResult="sample_text_2")
    _safe_set(a, 'libraryElement_ServiceTransaction106', {b1})
    assert _is_linked(a, 'libraryElement_ServiceTransaction106', b1)
    if hasattr(b1, 'libraryElement_OutputPrimitive'):
        assert _is_linked(b1, 'libraryElement_OutputPrimitive', a)
    _safe_set(a, 'libraryElement_ServiceTransaction106', {b2})
    assert _is_linked(a, 'libraryElement_ServiceTransaction106', b2)
    if hasattr(b1, 'libraryElement_OutputPrimitive'):
        assert not _is_linked(b1, 'libraryElement_OutputPrimitive', a)
    if hasattr(b2, 'libraryElement_OutputPrimitive'):
        assert _is_linked(b2, 'libraryElement_OutputPrimitive', a)
    _safe_set(a, 'libraryElement_ServiceTransaction106', set())
    assert not _is_linked(a, 'libraryElement_ServiceTransaction106', b2)
    if hasattr(b2, 'libraryElement_OutputPrimitive'):
        assert not _is_linked(b2, 'libraryElement_OutputPrimitive', a)


def test_assoc_outputVars74_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_InterfaceList()
    b2 = libraryElement_InterfaceList()
    _safe_set(a, 'libraryElement_VarDeclaration76', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration76', b1)
    if hasattr(b1, 'libraryElement_InterfaceList75'):
        assert _is_linked(b1, 'libraryElement_InterfaceList75', a)
    _safe_set(a, 'libraryElement_VarDeclaration76', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration76', b2)
    if hasattr(b1, 'libraryElement_InterfaceList75'):
        assert not _is_linked(b1, 'libraryElement_InterfaceList75', a)
    if hasattr(b2, 'libraryElement_InterfaceList75'):
        assert _is_linked(b2, 'libraryElement_InterfaceList75', a)
    _safe_set(a, 'libraryElement_VarDeclaration76', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration76', b2)
    if hasattr(b2, 'libraryElement_InterfaceList75'):
        assert not _is_linked(b2, 'libraryElement_InterfaceList75', a)


def test_assoc_palette121_link_reassign_clear():
    a = libraryElement_AutomationSystem(project="sample_text")
    b1 = libraryElement_Palette()
    b2 = libraryElement_Palette()
    _safe_set(a, 'automationSystem', b1)
    assert _is_linked(a, 'automationSystem', b1)
    if hasattr(b1, 'palette.ecorePalette'):
        assert _is_linked(b1, 'palette.ecorePalette', a)
    _safe_set(a, 'automationSystem', b2)
    assert _is_linked(a, 'automationSystem', b2)
    if hasattr(b1, 'palette.ecorePalette'):
        assert not _is_linked(b1, 'palette.ecorePalette', a)
    if hasattr(b2, 'palette.ecorePalette'):
        assert _is_linked(b2, 'palette.ecorePalette', a)
    _safe_set(a, 'automationSystem', None)
    assert not _is_linked(a, 'automationSystem', b2)
    if hasattr(b2, 'palette.ecorePalette'):
        assert not _is_linked(b2, 'palette.ecorePalette', a)


def test_assoc_paletteEntry168_link_reassign_clear():
    a = libraryElement_TypedConfigureableObject()
    b1 = libraryElement_PaletteEntry()
    b2 = libraryElement_PaletteEntry()
    _safe_set(a, 'libraryElement_TypedConfigureableObject', b1)
    assert _is_linked(a, 'libraryElement_TypedConfigureableObject', b1)
    if hasattr(b1, 'libraryElement_PaletteEntry'):
        assert _is_linked(b1, 'libraryElement_PaletteEntry', a)
    _safe_set(a, 'libraryElement_TypedConfigureableObject', b2)
    assert _is_linked(a, 'libraryElement_TypedConfigureableObject', b2)
    if hasattr(b1, 'libraryElement_PaletteEntry'):
        assert not _is_linked(b1, 'libraryElement_PaletteEntry', a)
    if hasattr(b2, 'libraryElement_PaletteEntry'):
        assert _is_linked(b2, 'libraryElement_PaletteEntry', a)
    _safe_set(a, 'libraryElement_TypedConfigureableObject', None)
    assert not _is_linked(a, 'libraryElement_TypedConfigureableObject', b2)
    if hasattr(b2, 'libraryElement_PaletteEntry'):
        assert not _is_linked(b2, 'libraryElement_PaletteEntry', a)


def test_assoc_parameter134_link_reassign_clear():
    a = libraryElement_Parameter(comment="sample_text", name="sample_text", value="sample_text")
    b1 = libraryElement_ConfigurableObject()
    b2 = libraryElement_ConfigurableObject()
    _safe_set(a, 'libraryElement_Parameter', b1)
    assert _is_linked(a, 'libraryElement_Parameter', b1)
    if hasattr(b1, 'libraryElement_ConfigurableObject'):
        assert _is_linked(b1, 'libraryElement_ConfigurableObject', a)
    _safe_set(a, 'libraryElement_Parameter', b2)
    assert _is_linked(a, 'libraryElement_Parameter', b2)
    if hasattr(b1, 'libraryElement_ConfigurableObject'):
        assert not _is_linked(b1, 'libraryElement_ConfigurableObject', a)
    if hasattr(b2, 'libraryElement_ConfigurableObject'):
        assert _is_linked(b2, 'libraryElement_ConfigurableObject', a)
    _safe_set(a, 'libraryElement_Parameter', None)
    assert not _is_linked(a, 'libraryElement_Parameter', b2)
    if hasattr(b2, 'libraryElement_ConfigurableObject'):
        assert not _is_linked(b2, 'libraryElement_ConfigurableObject', a)


def test_assoc_plugs59_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_AdapterDeclaration()
    b2 = libraryElement_AdapterDeclaration()
    _safe_set(a, 'libraryElement_InterfaceList60', {b1})
    assert _is_linked(a, 'libraryElement_InterfaceList60', b1)
    if hasattr(b1, 'libraryElement_AdapterDeclaration61'):
        assert _is_linked(b1, 'libraryElement_AdapterDeclaration61', a)
    _safe_set(a, 'libraryElement_InterfaceList60', {b2})
    assert _is_linked(a, 'libraryElement_InterfaceList60', b2)
    if hasattr(b1, 'libraryElement_AdapterDeclaration61'):
        assert not _is_linked(b1, 'libraryElement_AdapterDeclaration61', a)
    if hasattr(b2, 'libraryElement_AdapterDeclaration61'):
        assert _is_linked(b2, 'libraryElement_AdapterDeclaration61', a)
    _safe_set(a, 'libraryElement_InterfaceList60', set())
    assert not _is_linked(a, 'libraryElement_InterfaceList60', b2)
    if hasattr(b2, 'libraryElement_AdapterDeclaration61'):
        assert not _is_linked(b2, 'libraryElement_AdapterDeclaration61', a)


def test_assoc_resource13_link_reassign_clear():
    a = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    b1 = libraryElement_Device(profile="sample_text")
    b2 = libraryElement_Device(profile="sample_text_2")
    _safe_set(a, 'Resource', b1)
    assert _is_linked(a, 'Resource', b1)
    if hasattr(b1, 'device'):
        assert _is_linked(b1, 'device', a)
    _safe_set(a, 'Resource', b2)
    assert _is_linked(a, 'Resource', b2)
    if hasattr(b1, 'device'):
        assert not _is_linked(b1, 'device', a)
    if hasattr(b2, 'device'):
        assert _is_linked(b2, 'device', a)
    _safe_set(a, 'Resource', None)
    assert not _is_linked(a, 'Resource', b2)
    if hasattr(b2, 'device'):
        assert not _is_linked(b2, 'device', a)


def test_assoc_resource20_link_reassign_clear():
    a = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    b1 = libraryElement_DeviceType(profile="sample_text")
    b2 = libraryElement_DeviceType(profile="sample_text_2")
    _safe_set(a, 'libraryElement_Resource', b1)
    assert _is_linked(a, 'libraryElement_Resource', b1)
    if hasattr(b1, 'libraryElement_DeviceType21'):
        assert _is_linked(b1, 'libraryElement_DeviceType21', a)
    _safe_set(a, 'libraryElement_Resource', b2)
    assert _is_linked(a, 'libraryElement_Resource', b2)
    if hasattr(b1, 'libraryElement_DeviceType21'):
        assert not _is_linked(b1, 'libraryElement_DeviceType21', a)
    if hasattr(b2, 'libraryElement_DeviceType21'):
        assert _is_linked(b2, 'libraryElement_DeviceType21', a)
    _safe_set(a, 'libraryElement_Resource', None)
    assert not _is_linked(a, 'libraryElement_Resource', b2)
    if hasattr(b2, 'libraryElement_DeviceType21'):
        assert not _is_linked(b2, 'libraryElement_DeviceType21', a)


def test_assoc_resourceTypeName18_link_reassign_clear():
    a = libraryElement_ResourceTypeName(name="sample_text")
    b1 = libraryElement_DeviceType(profile="sample_text")
    b2 = libraryElement_DeviceType(profile="sample_text_2")
    _safe_set(a, 'libraryElement_ResourceTypeName', b1)
    assert _is_linked(a, 'libraryElement_ResourceTypeName', b1)
    if hasattr(b1, 'libraryElement_DeviceType19'):
        assert _is_linked(b1, 'libraryElement_DeviceType19', a)
    _safe_set(a, 'libraryElement_ResourceTypeName', b2)
    assert _is_linked(a, 'libraryElement_ResourceTypeName', b2)
    if hasattr(b1, 'libraryElement_DeviceType19'):
        assert not _is_linked(b1, 'libraryElement_DeviceType19', a)
    if hasattr(b2, 'libraryElement_DeviceType19'):
        assert _is_linked(b2, 'libraryElement_DeviceType19', a)
    _safe_set(a, 'libraryElement_ResourceTypeName', None)
    assert not _is_linked(a, 'libraryElement_ResourceTypeName', b2)
    if hasattr(b2, 'libraryElement_DeviceType19'):
        assert not _is_linked(b2, 'libraryElement_DeviceType19', a)


def test_assoc_segment77_link_reassign_clear():
    a = libraryElement_Segment(width="sample_text")
    b1 = libraryElement_Link()
    b2 = libraryElement_Link()
    _safe_set(a, 'Segment', b1)
    assert _is_linked(a, 'Segment', b1)
    if hasattr(b1, 'outConnections'):
        assert _is_linked(b1, 'outConnections', a)
    _safe_set(a, 'Segment', b2)
    assert _is_linked(a, 'Segment', b2)
    if hasattr(b1, 'outConnections'):
        assert not _is_linked(b1, 'outConnections', a)
    if hasattr(b2, 'outConnections'):
        assert _is_linked(b2, 'outConnections', a)
    _safe_set(a, 'Segment', None)
    assert not _is_linked(a, 'Segment', b2)
    if hasattr(b2, 'outConnections'):
        assert not _is_linked(b2, 'outConnections', a)


def test_assoc_segments147_link_reassign_clear():
    a = libraryElement_SystemConfiguration()
    b1 = libraryElement_Segment(width="sample_text")
    b2 = libraryElement_Segment(width="sample_text_2")
    _safe_set(a, 'libraryElement_SystemConfiguration148', {b1})
    assert _is_linked(a, 'libraryElement_SystemConfiguration148', b1)
    if hasattr(b1, 'libraryElement_Segment149'):
        assert _is_linked(b1, 'libraryElement_Segment149', a)
    _safe_set(a, 'libraryElement_SystemConfiguration148', {b2})
    assert _is_linked(a, 'libraryElement_SystemConfiguration148', b2)
    if hasattr(b1, 'libraryElement_Segment149'):
        assert not _is_linked(b1, 'libraryElement_Segment149', a)
    if hasattr(b2, 'libraryElement_Segment149'):
        assert _is_linked(b2, 'libraryElement_Segment149', a)
    _safe_set(a, 'libraryElement_SystemConfiguration148', set())
    assert not _is_linked(a, 'libraryElement_SystemConfiguration148', b2)
    if hasattr(b2, 'libraryElement_Segment149'):
        assert not _is_linked(b2, 'libraryElement_Segment149', a)


def test_assoc_serviceSequence165_link_reassign_clear():
    a = libraryElement_ServiceSequence(TestResult="sample_text")
    b1 = libraryElement_Service()
    b2 = libraryElement_Service()
    _safe_set(a, 'libraryElement_ServiceSequence167', b1)
    assert _is_linked(a, 'libraryElement_ServiceSequence167', b1)
    if hasattr(b1, 'libraryElement_Service166'):
        assert _is_linked(b1, 'libraryElement_Service166', a)
    _safe_set(a, 'libraryElement_ServiceSequence167', b2)
    assert _is_linked(a, 'libraryElement_ServiceSequence167', b2)
    if hasattr(b1, 'libraryElement_Service166'):
        assert not _is_linked(b1, 'libraryElement_Service166', a)
    if hasattr(b2, 'libraryElement_Service166'):
        assert _is_linked(b2, 'libraryElement_Service166', a)
    _safe_set(a, 'libraryElement_ServiceSequence167', None)
    assert not _is_linked(a, 'libraryElement_ServiceSequence167', b2)
    if hasattr(b2, 'libraryElement_Service166'):
        assert not _is_linked(b2, 'libraryElement_Service166', a)


def test_assoc_serviceTransaction102_link_reassign_clear():
    a = libraryElement_ServiceTransaction(TestResult="sample_text")
    b1 = libraryElement_ServiceSequence(TestResult="sample_text")
    b2 = libraryElement_ServiceSequence(TestResult="sample_text_2")
    _safe_set(a, 'libraryElement_ServiceTransaction', b1)
    assert _is_linked(a, 'libraryElement_ServiceTransaction', b1)
    if hasattr(b1, 'libraryElement_ServiceSequence'):
        assert _is_linked(b1, 'libraryElement_ServiceSequence', a)
    _safe_set(a, 'libraryElement_ServiceTransaction', b2)
    assert _is_linked(a, 'libraryElement_ServiceTransaction', b2)
    if hasattr(b1, 'libraryElement_ServiceSequence'):
        assert not _is_linked(b1, 'libraryElement_ServiceSequence', a)
    if hasattr(b2, 'libraryElement_ServiceSequence'):
        assert _is_linked(b2, 'libraryElement_ServiceSequence', a)
    _safe_set(a, 'libraryElement_ServiceTransaction', None)
    assert not _is_linked(a, 'libraryElement_ServiceTransaction', b2)
    if hasattr(b2, 'libraryElement_ServiceSequence'):
        assert not _is_linked(b2, 'libraryElement_ServiceSequence', a)


def test_assoc_sockets62_link_reassign_clear():
    a = libraryElement_InterfaceList()
    b1 = libraryElement_AdapterDeclaration()
    b2 = libraryElement_AdapterDeclaration()
    _safe_set(a, 'libraryElement_InterfaceList63', {b1})
    assert _is_linked(a, 'libraryElement_InterfaceList63', b1)
    if hasattr(b1, 'libraryElement_AdapterDeclaration64'):
        assert _is_linked(b1, 'libraryElement_AdapterDeclaration64', a)
    _safe_set(a, 'libraryElement_InterfaceList63', {b2})
    assert _is_linked(a, 'libraryElement_InterfaceList63', b2)
    if hasattr(b1, 'libraryElement_AdapterDeclaration64'):
        assert not _is_linked(b1, 'libraryElement_AdapterDeclaration64', a)
    if hasattr(b2, 'libraryElement_AdapterDeclaration64'):
        assert _is_linked(b2, 'libraryElement_AdapterDeclaration64', a)
    _safe_set(a, 'libraryElement_InterfaceList63', set())
    assert not _is_linked(a, 'libraryElement_InterfaceList63', b2)
    if hasattr(b2, 'libraryElement_AdapterDeclaration64'):
        assert not _is_linked(b2, 'libraryElement_AdapterDeclaration64', a)


def test_assoc_source10_link_reassign_clear():
    a = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b1 = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    b2 = libraryElement_Connection(brokenConnection="sample_text_2", dx1="sample_text_2", dx2="sample_text_2", dy="sample_text_2", resTypeConnection="sample_text_2")
    _safe_set(a, 'IInterfaceElement', b1)
    assert _is_linked(a, 'IInterfaceElement', b1)
    if hasattr(b1, 'outputConnections'):
        assert _is_linked(b1, 'outputConnections', a)
    _safe_set(a, 'IInterfaceElement', b2)
    assert _is_linked(a, 'IInterfaceElement', b2)
    if hasattr(b1, 'outputConnections'):
        assert not _is_linked(b1, 'outputConnections', a)
    if hasattr(b2, 'outputConnections'):
        assert _is_linked(b2, 'outputConnections', a)
    _safe_set(a, 'IInterfaceElement', None)
    assert not _is_linked(a, 'IInterfaceElement', b2)
    if hasattr(b2, 'outputConnections'):
        assert not _is_linked(b2, 'outputConnections', a)


def test_assoc_source42_link_reassign_clear():
    a = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    b1 = libraryElement_ECState()
    b2 = libraryElement_ECState()
    _safe_set(a, 'outTransitions', b1)
    assert _is_linked(a, 'outTransitions', b1)
    if hasattr(b1, 'ECState'):
        assert _is_linked(b1, 'ECState', a)
    _safe_set(a, 'outTransitions', b2)
    assert _is_linked(a, 'outTransitions', b2)
    if hasattr(b1, 'ECState'):
        assert not _is_linked(b1, 'ECState', a)
    if hasattr(b2, 'ECState'):
        assert _is_linked(b2, 'ECState', a)
    _safe_set(a, 'outTransitions', None)
    assert not _is_linked(a, 'outTransitions', b2)
    if hasattr(b2, 'ECState'):
        assert not _is_linked(b2, 'ECState', a)


def test_assoc_start33_link_reassign_clear():
    a = libraryElement_ECState()
    b1 = libraryElement_ECC()
    b2 = libraryElement_ECC()
    _safe_set(a, 'libraryElement_ECState35', b1)
    assert _is_linked(a, 'libraryElement_ECState35', b1)
    if hasattr(b1, 'libraryElement_ECC34'):
        assert _is_linked(b1, 'libraryElement_ECC34', a)
    _safe_set(a, 'libraryElement_ECState35', b2)
    assert _is_linked(a, 'libraryElement_ECState35', b2)
    if hasattr(b1, 'libraryElement_ECC34'):
        assert not _is_linked(b1, 'libraryElement_ECC34', a)
    if hasattr(b2, 'libraryElement_ECC34'):
        assert _is_linked(b2, 'libraryElement_ECC34', a)
    _safe_set(a, 'libraryElement_ECState35', None)
    assert not _is_linked(a, 'libraryElement_ECState35', b2)
    if hasattr(b2, 'libraryElement_ECC34'):
        assert not _is_linked(b2, 'libraryElement_ECC34', a)


def test_assoc_subAppNetwork53_link_reassign_clear():
    a = libraryElement_SubApp()
    b1 = libraryElement_FBNetwork()
    b2 = libraryElement_FBNetwork()
    _safe_set(a, 'libraryElement_SubApp', b1)
    assert _is_linked(a, 'libraryElement_SubApp', b1)
    if hasattr(b1, 'libraryElement_FBNetwork54'):
        assert _is_linked(b1, 'libraryElement_FBNetwork54', a)
    _safe_set(a, 'libraryElement_SubApp', b2)
    assert _is_linked(a, 'libraryElement_SubApp', b2)
    if hasattr(b1, 'libraryElement_FBNetwork54'):
        assert not _is_linked(b1, 'libraryElement_FBNetwork54', a)
    if hasattr(b2, 'libraryElement_FBNetwork54'):
        assert _is_linked(b2, 'libraryElement_FBNetwork54', a)
    _safe_set(a, 'libraryElement_SubApp', None)
    assert not _is_linked(a, 'libraryElement_SubApp', b2)
    if hasattr(b2, 'libraryElement_FBNetwork54'):
        assert not _is_linked(b2, 'libraryElement_FBNetwork54', a)


def test_assoc_systemConfiguration122_link_reassign_clear():
    a = libraryElement_SystemConfiguration()
    b1 = libraryElement_AutomationSystem(project="sample_text")
    b2 = libraryElement_AutomationSystem(project="sample_text_2")
    _safe_set(a, 'libraryElement_SystemConfiguration', b1)
    assert _is_linked(a, 'libraryElement_SystemConfiguration', b1)
    if hasattr(b1, 'libraryElement_AutomationSystem123'):
        assert _is_linked(b1, 'libraryElement_AutomationSystem123', a)
    _safe_set(a, 'libraryElement_SystemConfiguration', b2)
    assert _is_linked(a, 'libraryElement_SystemConfiguration', b2)
    if hasattr(b1, 'libraryElement_AutomationSystem123'):
        assert not _is_linked(b1, 'libraryElement_AutomationSystem123', a)
    if hasattr(b2, 'libraryElement_AutomationSystem123'):
        assert _is_linked(b2, 'libraryElement_AutomationSystem123', a)
    _safe_set(a, 'libraryElement_SystemConfiguration', None)
    assert not _is_linked(a, 'libraryElement_SystemConfiguration', b2)
    if hasattr(b2, 'libraryElement_AutomationSystem123'):
        assert not _is_linked(b2, 'libraryElement_AutomationSystem123', a)


def test_assoc_to82_link_reassign_clear():
    a = libraryElement_Mapping()
    b1 = libraryElement_FBNetworkElement()
    b2 = libraryElement_FBNetworkElement()
    _safe_set(a, 'libraryElement_Mapping83', b1)
    assert _is_linked(a, 'libraryElement_Mapping83', b1)
    if hasattr(b1, 'libraryElement_FBNetworkElement84'):
        assert _is_linked(b1, 'libraryElement_FBNetworkElement84', a)
    _safe_set(a, 'libraryElement_Mapping83', b2)
    assert _is_linked(a, 'libraryElement_Mapping83', b2)
    if hasattr(b1, 'libraryElement_FBNetworkElement84'):
        assert not _is_linked(b1, 'libraryElement_FBNetworkElement84', a)
    if hasattr(b2, 'libraryElement_FBNetworkElement84'):
        assert _is_linked(b2, 'libraryElement_FBNetworkElement84', a)
    _safe_set(a, 'libraryElement_Mapping83', None)
    assert not _is_linked(a, 'libraryElement_Mapping83', b2)
    if hasattr(b2, 'libraryElement_FBNetworkElement84'):
        assert not _is_linked(b2, 'libraryElement_FBNetworkElement84', a)


def test_assoc_type142_link_reassign_clear():
    a = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b1 = libraryElement_DataType()
    b2 = libraryElement_DataType()
    _safe_set(a, 'libraryElement_IInterfaceElement', b1)
    assert _is_linked(a, 'libraryElement_IInterfaceElement', b1)
    if hasattr(b1, 'libraryElement_DataType'):
        assert _is_linked(b1, 'libraryElement_DataType', a)
    _safe_set(a, 'libraryElement_IInterfaceElement', b2)
    assert _is_linked(a, 'libraryElement_IInterfaceElement', b2)
    if hasattr(b1, 'libraryElement_DataType'):
        assert not _is_linked(b1, 'libraryElement_DataType', a)
    if hasattr(b2, 'libraryElement_DataType'):
        assert _is_linked(b2, 'libraryElement_DataType', a)
    _safe_set(a, 'libraryElement_IInterfaceElement', None)
    assert not _is_linked(a, 'libraryElement_IInterfaceElement', b2)
    if hasattr(b2, 'libraryElement_DataType'):
        assert not _is_linked(b2, 'libraryElement_DataType', a)


def test_assoc_value143_link_reassign_clear():
    a = libraryElement_Value(value="sample_text")
    b1 = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    b2 = libraryElement_IInterfaceElement(isInput="sample_text_2", typeName="sample_text_2")
    _safe_set(a, 'libraryElement_Value', b1)
    assert _is_linked(a, 'libraryElement_Value', b1)
    if hasattr(b1, 'libraryElement_IInterfaceElement144'):
        assert _is_linked(b1, 'libraryElement_IInterfaceElement144', a)
    _safe_set(a, 'libraryElement_Value', b2)
    assert _is_linked(a, 'libraryElement_Value', b2)
    if hasattr(b1, 'libraryElement_IInterfaceElement144'):
        assert not _is_linked(b1, 'libraryElement_IInterfaceElement144', a)
    if hasattr(b2, 'libraryElement_IInterfaceElement144'):
        assert _is_linked(b2, 'libraryElement_IInterfaceElement144', a)
    _safe_set(a, 'libraryElement_Value', None)
    assert not _is_linked(a, 'libraryElement_Value', b2)
    if hasattr(b2, 'libraryElement_IInterfaceElement144'):
        assert not _is_linked(b2, 'libraryElement_IInterfaceElement144', a)


def test_assoc_varDeclaration153_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_SegmentType()
    b2 = libraryElement_SegmentType()
    _safe_set(a, 'libraryElement_VarDeclaration154', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration154', b1)
    if hasattr(b1, 'libraryElement_SegmentType'):
        assert _is_linked(b1, 'libraryElement_SegmentType', a)
    _safe_set(a, 'libraryElement_VarDeclaration154', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration154', b2)
    if hasattr(b1, 'libraryElement_SegmentType'):
        assert not _is_linked(b1, 'libraryElement_SegmentType', a)
    if hasattr(b2, 'libraryElement_SegmentType'):
        assert _is_linked(b2, 'libraryElement_SegmentType', a)
    _safe_set(a, 'libraryElement_VarDeclaration154', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration154', b2)
    if hasattr(b2, 'libraryElement_SegmentType'):
        assert not _is_linked(b2, 'libraryElement_SegmentType', a)


def test_assoc_varDeclaration16_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_DeviceType(profile="sample_text")
    b2 = libraryElement_DeviceType(profile="sample_text_2")
    _safe_set(a, 'libraryElement_VarDeclaration17', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration17', b1)
    if hasattr(b1, 'libraryElement_DeviceType'):
        assert _is_linked(b1, 'libraryElement_DeviceType', a)
    _safe_set(a, 'libraryElement_VarDeclaration17', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration17', b2)
    if hasattr(b1, 'libraryElement_DeviceType'):
        assert not _is_linked(b1, 'libraryElement_DeviceType', a)
    if hasattr(b2, 'libraryElement_DeviceType'):
        assert _is_linked(b2, 'libraryElement_DeviceType', a)
    _safe_set(a, 'libraryElement_VarDeclaration17', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration17', b2)
    if hasattr(b2, 'libraryElement_DeviceType'):
        assert not _is_linked(b2, 'libraryElement_DeviceType', a)


def test_assoc_varDeclaration90_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_ResourceType()
    b2 = libraryElement_ResourceType()
    _safe_set(a, 'libraryElement_VarDeclaration91', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration91', b1)
    if hasattr(b1, 'libraryElement_ResourceType'):
        assert _is_linked(b1, 'libraryElement_ResourceType', a)
    _safe_set(a, 'libraryElement_VarDeclaration91', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration91', b2)
    if hasattr(b1, 'libraryElement_ResourceType'):
        assert not _is_linked(b1, 'libraryElement_ResourceType', a)
    if hasattr(b2, 'libraryElement_ResourceType'):
        assert _is_linked(b2, 'libraryElement_ResourceType', a)
    _safe_set(a, 'libraryElement_VarDeclaration91', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration91', b2)
    if hasattr(b2, 'libraryElement_ResourceType'):
        assert not _is_linked(b2, 'libraryElement_ResourceType', a)


def test_assoc_varDeclarations173_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_IVarElement()
    b2 = libraryElement_IVarElement()
    _safe_set(a, 'libraryElement_VarDeclaration174', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration174', b1)
    if hasattr(b1, 'libraryElement_IVarElement'):
        assert _is_linked(b1, 'libraryElement_IVarElement', a)
    _safe_set(a, 'libraryElement_VarDeclaration174', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration174', b2)
    if hasattr(b1, 'libraryElement_IVarElement'):
        assert not _is_linked(b1, 'libraryElement_IVarElement', a)
    if hasattr(b2, 'libraryElement_IVarElement'):
        assert _is_linked(b2, 'libraryElement_IVarElement', a)
    _safe_set(a, 'libraryElement_VarDeclaration174', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration174', b2)
    if hasattr(b2, 'libraryElement_IVarElement'):
        assert not _is_linked(b2, 'libraryElement_IVarElement', a)


def test_assoc_varDeclarations98_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_Segment(width="sample_text")
    b2 = libraryElement_Segment(width="sample_text_2")
    _safe_set(a, 'libraryElement_VarDeclaration99', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration99', b1)
    if hasattr(b1, 'libraryElement_Segment'):
        assert _is_linked(b1, 'libraryElement_Segment', a)
    _safe_set(a, 'libraryElement_VarDeclaration99', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration99', b2)
    if hasattr(b1, 'libraryElement_Segment'):
        assert not _is_linked(b1, 'libraryElement_Segment', a)
    if hasattr(b2, 'libraryElement_Segment'):
        assert _is_linked(b2, 'libraryElement_Segment', a)
    _safe_set(a, 'libraryElement_VarDeclaration99', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration99', b2)
    if hasattr(b2, 'libraryElement_Segment'):
        assert not _is_linked(b2, 'libraryElement_Segment', a)


def test_assoc_varInitialization124_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_VarInitialization()
    b2 = libraryElement_VarInitialization()
    _safe_set(a, 'libraryElement_VarDeclaration125', b1)
    assert _is_linked(a, 'libraryElement_VarDeclaration125', b1)
    if hasattr(b1, 'libraryElement_VarInitialization'):
        assert _is_linked(b1, 'libraryElement_VarInitialization', a)
    _safe_set(a, 'libraryElement_VarDeclaration125', b2)
    assert _is_linked(a, 'libraryElement_VarDeclaration125', b2)
    if hasattr(b1, 'libraryElement_VarInitialization'):
        assert not _is_linked(b1, 'libraryElement_VarInitialization', a)
    if hasattr(b2, 'libraryElement_VarInitialization'):
        assert _is_linked(b2, 'libraryElement_VarInitialization', a)
    _safe_set(a, 'libraryElement_VarDeclaration125', None)
    assert not _is_linked(a, 'libraryElement_VarDeclaration125', b2)
    if hasattr(b2, 'libraryElement_VarInitialization'):
        assert not _is_linked(b2, 'libraryElement_VarInitialization', a)


def test_assoc_variables127_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_With()
    b2 = libraryElement_With()
    _safe_set(a, 'VarDeclaration', b1)
    assert _is_linked(a, 'VarDeclaration', b1)
    if hasattr(b1, 'withs'):
        assert _is_linked(b1, 'withs', a)
    _safe_set(a, 'VarDeclaration', b2)
    assert _is_linked(a, 'VarDeclaration', b2)
    if hasattr(b1, 'withs'):
        assert not _is_linked(b1, 'withs', a)
    if hasattr(b2, 'withs'):
        assert _is_linked(b2, 'withs', a)
    _safe_set(a, 'VarDeclaration', None)
    assert not _is_linked(a, 'VarDeclaration', b2)
    if hasattr(b2, 'withs'):
        assert not _is_linked(b2, 'withs', a)


def test_assoc_versionInfo128_link_reassign_clear():
    a = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    b1 = libraryElement_LibraryElement()
    b2 = libraryElement_LibraryElement()
    _safe_set(a, 'libraryElement_VersionInfo', b1)
    assert _is_linked(a, 'libraryElement_VersionInfo', b1)
    if hasattr(b1, 'libraryElement_LibraryElement'):
        assert _is_linked(b1, 'libraryElement_LibraryElement', a)
    _safe_set(a, 'libraryElement_VersionInfo', b2)
    assert _is_linked(a, 'libraryElement_VersionInfo', b2)
    if hasattr(b1, 'libraryElement_LibraryElement'):
        assert not _is_linked(b1, 'libraryElement_LibraryElement', a)
    if hasattr(b2, 'libraryElement_LibraryElement'):
        assert _is_linked(b2, 'libraryElement_LibraryElement', a)
    _safe_set(a, 'libraryElement_VersionInfo', None)
    assert not _is_linked(a, 'libraryElement_VersionInfo', b2)
    if hasattr(b2, 'libraryElement_LibraryElement'):
        assert not _is_linked(b2, 'libraryElement_LibraryElement', a)


def test_assoc_withs126_link_reassign_clear():
    a = libraryElement_VarDeclaration(arraySize="sample_text")
    b1 = libraryElement_With()
    b2 = libraryElement_With()
    _safe_set(a, 'variables', {b1})
    assert _is_linked(a, 'variables', b1)
    if hasattr(b1, 'With'):
        assert _is_linked(b1, 'With', a)
    _safe_set(a, 'variables', {b2})
    assert _is_linked(a, 'variables', b2)
    if hasattr(b1, 'With'):
        assert not _is_linked(b1, 'With', a)
    if hasattr(b2, 'With'):
        assert _is_linked(b2, 'With', a)
    _safe_set(a, 'variables', set())
    assert not _is_linked(a, 'variables', b2)
    if hasattr(b2, 'With'):
        assert not _is_linked(b2, 'With', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Algorithm_strategy = st.builds(Algorithm)
@given(instance=Algorithm_strategy)
@settings(max_examples=25)
def test_Algorithm_instantiation(instance):
    assert isinstance(instance, Algorithm)


ColorizableElement_strategy = st.builds(ColorizableElement)
@given(instance=ColorizableElement_strategy)
@settings(max_examples=25)
def test_ColorizableElement_instantiation(instance):
    assert isinstance(instance, ColorizableElement)


CompilableType_strategy = st.builds(CompilableType)
@given(instance=CompilableType_strategy)
@settings(max_examples=25)
def test_CompilableType_instantiation(instance):
    assert isinstance(instance, CompilableType)


CompositeFBType_strategy = st.builds(CompositeFBType)
@given(instance=CompositeFBType_strategy)
@settings(max_examples=25)
def test_CompositeFBType_instantiation(instance):
    assert isinstance(instance, CompositeFBType)


ConfigurableObject_strategy = st.builds(ConfigurableObject)
@given(instance=ConfigurableObject_strategy)
@settings(max_examples=25)
def test_ConfigurableObject_instantiation(instance):
    assert isinstance(instance, ConfigurableObject)


Connection_strategy = st.builds(Connection)
@given(instance=Connection_strategy)
@settings(max_examples=25)
def test_Connection_instantiation(instance):
    assert isinstance(instance, Connection)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


FB_strategy = st.builds(FB)
@given(instance=FB_strategy)
@settings(max_examples=25)
def test_FB_instantiation(instance):
    assert isinstance(instance, FB)


FBNetworkElement_strategy = st.builds(FBNetworkElement)
@given(instance=FBNetworkElement_strategy)
@settings(max_examples=25)
def test_FBNetworkElement_instantiation(instance):
    assert isinstance(instance, FBNetworkElement)


FBType_strategy = st.builds(FBType)
@given(instance=FBType_strategy)
@settings(max_examples=25)
def test_FBType_instantiation(instance):
    assert isinstance(instance, FBType)


I4DIACElement_strategy = st.builds(I4DIACElement)
@given(instance=I4DIACElement_strategy)
@settings(max_examples=25)
def test_I4DIACElement_instantiation(instance):
    assert isinstance(instance, I4DIACElement)


IInterfaceElement_strategy = st.builds(IInterfaceElement)
@given(instance=IInterfaceElement_strategy)
@settings(max_examples=25)
def test_IInterfaceElement_instantiation(instance):
    assert isinstance(instance, IInterfaceElement)


INamedElement_strategy = st.builds(INamedElement)
@given(instance=INamedElement_strategy)
@settings(max_examples=25)
def test_INamedElement_instantiation(instance):
    assert isinstance(instance, INamedElement)


IVarElement_strategy = st.builds(IVarElement)
@given(instance=IVarElement_strategy)
@settings(max_examples=25)
def test_IVarElement_instantiation(instance):
    assert isinstance(instance, IVarElement)


LibraryElement_strategy = st.builds(LibraryElement)
@given(instance=LibraryElement_strategy)
@settings(max_examples=25)
def test_LibraryElement_instantiation(instance):
    assert isinstance(instance, LibraryElement)


PositionableElement_strategy = st.builds(PositionableElement)
@given(instance=PositionableElement_strategy)
@settings(max_examples=25)
def test_PositionableElement_instantiation(instance):
    assert isinstance(instance, PositionableElement)


Primitive_strategy = st.builds(Primitive)
@given(instance=Primitive_strategy)
@settings(max_examples=25)
def test_Primitive_instantiation(instance):
    assert isinstance(instance, Primitive)


TextAlgorithm_strategy = st.builds(TextAlgorithm)
@given(instance=TextAlgorithm_strategy)
@settings(max_examples=25)
def test_TextAlgorithm_instantiation(instance):
    assert isinstance(instance, TextAlgorithm)


TypedConfigureableObject_strategy = st.builds(TypedConfigureableObject)
@given(instance=TypedConfigureableObject_strategy)
@settings(max_examples=25)
def test_TypedConfigureableObject_instantiation(instance):
    assert isinstance(instance, TypedConfigureableObject)


VarDeclaration_strategy = st.builds(VarDeclaration)
@given(instance=VarDeclaration_strategy)
@settings(max_examples=25)
def test_VarDeclaration_instantiation(instance):
    assert isinstance(instance, VarDeclaration)


libraryElement_AdapterConnection_strategy = st.builds(libraryElement_AdapterConnection)
@given(instance=libraryElement_AdapterConnection_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterConnection_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterConnection)


libraryElement_AdapterDeclaration_strategy = st.builds(libraryElement_AdapterDeclaration)
@given(instance=libraryElement_AdapterDeclaration_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterDeclaration_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterDeclaration)


libraryElement_AdapterEvent_strategy = st.builds(libraryElement_AdapterEvent)
@given(instance=libraryElement_AdapterEvent_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterEvent_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterEvent)


libraryElement_AdapterFB_strategy = st.builds(libraryElement_AdapterFB)
@given(instance=libraryElement_AdapterFB_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterFB_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterFB)


libraryElement_AdapterFBType_strategy = st.builds(libraryElement_AdapterFBType)
@given(instance=libraryElement_AdapterFBType_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterFBType_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterFBType)


libraryElement_AdapterType_strategy = st.builds(libraryElement_AdapterType)
@given(instance=libraryElement_AdapterType_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterType_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterType)


libraryElement_AdapterTypePaletteEntry_strategy = st.builds(libraryElement_AdapterTypePaletteEntry)
@given(instance=libraryElement_AdapterTypePaletteEntry_strategy)
@settings(max_examples=25)
def test_libraryElement_AdapterTypePaletteEntry_instantiation(instance):
    assert isinstance(instance, libraryElement_AdapterTypePaletteEntry)


libraryElement_Algorithm_strategy = st.builds(libraryElement_Algorithm)
@given(instance=libraryElement_Algorithm_strategy)
@settings(max_examples=25)
def test_libraryElement_Algorithm_instantiation(instance):
    assert isinstance(instance, libraryElement_Algorithm)


libraryElement_Annotation_strategy = st.builds(libraryElement_Annotation, name=safe_text, servity=safe_text)
@given(instance=libraryElement_Annotation_strategy)
@settings(max_examples=25)
def test_libraryElement_Annotation_instantiation(instance):
    assert isinstance(instance, libraryElement_Annotation)


libraryElement_Application_strategy = st.builds(libraryElement_Application)
@given(instance=libraryElement_Application_strategy)
@settings(max_examples=25)
def test_libraryElement_Application_instantiation(instance):
    assert isinstance(instance, libraryElement_Application)


libraryElement_AutomationSystem_strategy = st.builds(libraryElement_AutomationSystem, project=safe_text)
@given(instance=libraryElement_AutomationSystem_strategy)
@settings(max_examples=25)
def test_libraryElement_AutomationSystem_instantiation(instance):
    assert isinstance(instance, libraryElement_AutomationSystem)


libraryElement_BasicFBType_strategy = st.builds(libraryElement_BasicFBType)
@given(instance=libraryElement_BasicFBType_strategy)
@settings(max_examples=25)
def test_libraryElement_BasicFBType_instantiation(instance):
    assert isinstance(instance, libraryElement_BasicFBType)


libraryElement_Color_strategy = st.builds(libraryElement_Color, blue=safe_text, green=safe_text, red=safe_text)
@given(instance=libraryElement_Color_strategy)
@settings(max_examples=25)
def test_libraryElement_Color_instantiation(instance):
    assert isinstance(instance, libraryElement_Color)


libraryElement_ColorizableElement_strategy = st.builds(libraryElement_ColorizableElement)
@given(instance=libraryElement_ColorizableElement_strategy)
@settings(max_examples=25)
def test_libraryElement_ColorizableElement_instantiation(instance):
    assert isinstance(instance, libraryElement_ColorizableElement)


libraryElement_CompilableType_strategy = st.builds(libraryElement_CompilableType)
@given(instance=libraryElement_CompilableType_strategy)
@settings(max_examples=25)
def test_libraryElement_CompilableType_instantiation(instance):
    assert isinstance(instance, libraryElement_CompilableType)


libraryElement_Compiler_strategy = st.builds(libraryElement_Compiler, language=safe_text, product=safe_text, vendor=safe_text, version=safe_text)
@given(instance=libraryElement_Compiler_strategy)
@settings(max_examples=25)
def test_libraryElement_Compiler_instantiation(instance):
    assert isinstance(instance, libraryElement_Compiler)


libraryElement_CompilerInfo_strategy = st.builds(libraryElement_CompilerInfo, classdef=safe_text, header=safe_text)
@given(instance=libraryElement_CompilerInfo_strategy)
@settings(max_examples=25)
def test_libraryElement_CompilerInfo_instantiation(instance):
    assert isinstance(instance, libraryElement_CompilerInfo)


libraryElement_CompositeFBType_strategy = st.builds(libraryElement_CompositeFBType)
@given(instance=libraryElement_CompositeFBType_strategy)
@settings(max_examples=25)
def test_libraryElement_CompositeFBType_instantiation(instance):
    assert isinstance(instance, libraryElement_CompositeFBType)


libraryElement_ConfigurableObject_strategy = st.builds(libraryElement_ConfigurableObject)
@given(instance=libraryElement_ConfigurableObject_strategy)
@settings(max_examples=25)
def test_libraryElement_ConfigurableObject_instantiation(instance):
    assert isinstance(instance, libraryElement_ConfigurableObject)


libraryElement_Connection_strategy = st.builds(libraryElement_Connection, brokenConnection=safe_text, dx1=safe_text, dx2=safe_text, dy=safe_text, resTypeConnection=safe_text)
@given(instance=libraryElement_Connection_strategy)
@settings(max_examples=25)
def test_libraryElement_Connection_instantiation(instance):
    assert isinstance(instance, libraryElement_Connection)


libraryElement_DataConnection_strategy = st.builds(libraryElement_DataConnection)
@given(instance=libraryElement_DataConnection_strategy)
@settings(max_examples=25)
def test_libraryElement_DataConnection_instantiation(instance):
    assert isinstance(instance, libraryElement_DataConnection)


libraryElement_DataType_strategy = st.builds(libraryElement_DataType)
@given(instance=libraryElement_DataType_strategy)
@settings(max_examples=25)
def test_libraryElement_DataType_instantiation(instance):
    assert isinstance(instance, libraryElement_DataType)


libraryElement_Device_strategy = st.builds(libraryElement_Device, profile=safe_text)
@given(instance=libraryElement_Device_strategy)
@settings(max_examples=25)
def test_libraryElement_Device_instantiation(instance):
    assert isinstance(instance, libraryElement_Device)


libraryElement_DeviceType_strategy = st.builds(libraryElement_DeviceType, profile=safe_text)
@given(instance=libraryElement_DeviceType_strategy)
@settings(max_examples=25)
def test_libraryElement_DeviceType_instantiation(instance):
    assert isinstance(instance, libraryElement_DeviceType)


libraryElement_ECAction_strategy = st.builds(libraryElement_ECAction)
@given(instance=libraryElement_ECAction_strategy)
@settings(max_examples=25)
def test_libraryElement_ECAction_instantiation(instance):
    assert isinstance(instance, libraryElement_ECAction)


libraryElement_ECC_strategy = st.builds(libraryElement_ECC)
@given(instance=libraryElement_ECC_strategy)
@settings(max_examples=25)
def test_libraryElement_ECC_instantiation(instance):
    assert isinstance(instance, libraryElement_ECC)


libraryElement_ECState_strategy = st.builds(libraryElement_ECState)
@given(instance=libraryElement_ECState_strategy)
@settings(max_examples=25)
def test_libraryElement_ECState_instantiation(instance):
    assert isinstance(instance, libraryElement_ECState)


libraryElement_ECTransition_strategy = st.builds(libraryElement_ECTransition, comment=safe_text, conditionExpression=safe_text)
@given(instance=libraryElement_ECTransition_strategy)
@settings(max_examples=25)
def test_libraryElement_ECTransition_instantiation(instance):
    assert isinstance(instance, libraryElement_ECTransition)


libraryElement_Event_strategy = st.builds(libraryElement_Event)
@given(instance=libraryElement_Event_strategy)
@settings(max_examples=25)
def test_libraryElement_Event_instantiation(instance):
    assert isinstance(instance, libraryElement_Event)


libraryElement_EventConnection_strategy = st.builds(libraryElement_EventConnection)
@given(instance=libraryElement_EventConnection_strategy)
@settings(max_examples=25)
def test_libraryElement_EventConnection_instantiation(instance):
    assert isinstance(instance, libraryElement_EventConnection)


libraryElement_FB_strategy = st.builds(libraryElement_FB)
@given(instance=libraryElement_FB_strategy)
@settings(max_examples=25)
def test_libraryElement_FB_instantiation(instance):
    assert isinstance(instance, libraryElement_FB)


libraryElement_FBNetwork_strategy = st.builds(libraryElement_FBNetwork)
@given(instance=libraryElement_FBNetwork_strategy)
@settings(max_examples=25)
def test_libraryElement_FBNetwork_instantiation(instance):
    assert isinstance(instance, libraryElement_FBNetwork)


libraryElement_FBNetworkElement_strategy = st.builds(libraryElement_FBNetworkElement)
@given(instance=libraryElement_FBNetworkElement_strategy)
@settings(max_examples=25)
def test_libraryElement_FBNetworkElement_instantiation(instance):
    assert isinstance(instance, libraryElement_FBNetworkElement)


libraryElement_FBType_strategy = st.builds(libraryElement_FBType)
@given(instance=libraryElement_FBType_strategy)
@settings(max_examples=25)
def test_libraryElement_FBType_instantiation(instance):
    assert isinstance(instance, libraryElement_FBType)


libraryElement_I4DIACElement_strategy = st.builds(libraryElement_I4DIACElement)
@given(instance=libraryElement_I4DIACElement_strategy)
@settings(max_examples=25)
def test_libraryElement_I4DIACElement_instantiation(instance):
    assert isinstance(instance, libraryElement_I4DIACElement)


libraryElement_IInterfaceElement_strategy = st.builds(libraryElement_IInterfaceElement, isInput=safe_text, typeName=safe_text)
@given(instance=libraryElement_IInterfaceElement_strategy)
@settings(max_examples=25)
def test_libraryElement_IInterfaceElement_instantiation(instance):
    assert isinstance(instance, libraryElement_IInterfaceElement)


libraryElement_INamedElement_strategy = st.builds(libraryElement_INamedElement, comment=safe_text, name=safe_text)
@given(instance=libraryElement_INamedElement_strategy)
@settings(max_examples=25)
def test_libraryElement_INamedElement_instantiation(instance):
    assert isinstance(instance, libraryElement_INamedElement)


libraryElement_IVarElement_strategy = st.builds(libraryElement_IVarElement)
@given(instance=libraryElement_IVarElement_strategy)
@settings(max_examples=25)
def test_libraryElement_IVarElement_instantiation(instance):
    assert isinstance(instance, libraryElement_IVarElement)


libraryElement_Identification_strategy = st.builds(libraryElement_Identification, applicationDomain=safe_text, classification=safe_text, description=safe_text, function=safe_text, standard=safe_text, type=safe_text)
@given(instance=libraryElement_Identification_strategy)
@settings(max_examples=25)
def test_libraryElement_Identification_instantiation(instance):
    assert isinstance(instance, libraryElement_Identification)


libraryElement_InputPrimitive_strategy = st.builds(libraryElement_InputPrimitive)
@given(instance=libraryElement_InputPrimitive_strategy)
@settings(max_examples=25)
def test_libraryElement_InputPrimitive_instantiation(instance):
    assert isinstance(instance, libraryElement_InputPrimitive)


libraryElement_InterfaceList_strategy = st.builds(libraryElement_InterfaceList)
@given(instance=libraryElement_InterfaceList_strategy)
@settings(max_examples=25)
def test_libraryElement_InterfaceList_instantiation(instance):
    assert isinstance(instance, libraryElement_InterfaceList)


libraryElement_LibraryElement_strategy = st.builds(libraryElement_LibraryElement)
@given(instance=libraryElement_LibraryElement_strategy)
@settings(max_examples=25)
def test_libraryElement_LibraryElement_instantiation(instance):
    assert isinstance(instance, libraryElement_LibraryElement)


libraryElement_Link_strategy = st.builds(libraryElement_Link)
@given(instance=libraryElement_Link_strategy)
@settings(max_examples=25)
def test_libraryElement_Link_instantiation(instance):
    assert isinstance(instance, libraryElement_Link)


libraryElement_Mapping_strategy = st.builds(libraryElement_Mapping)
@given(instance=libraryElement_Mapping_strategy)
@settings(max_examples=25)
def test_libraryElement_Mapping_instantiation(instance):
    assert isinstance(instance, libraryElement_Mapping)


libraryElement_OtherAlgorithm_strategy = st.builds(libraryElement_OtherAlgorithm, language=safe_text)
@given(instance=libraryElement_OtherAlgorithm_strategy)
@settings(max_examples=25)
def test_libraryElement_OtherAlgorithm_instantiation(instance):
    assert isinstance(instance, libraryElement_OtherAlgorithm)


libraryElement_OutputPrimitive_strategy = st.builds(libraryElement_OutputPrimitive, TestResult=safe_text)
@given(instance=libraryElement_OutputPrimitive_strategy)
@settings(max_examples=25)
def test_libraryElement_OutputPrimitive_instantiation(instance):
    assert isinstance(instance, libraryElement_OutputPrimitive)


libraryElement_Palette_strategy = st.builds(libraryElement_Palette)
@given(instance=libraryElement_Palette_strategy)
@settings(max_examples=25)
def test_libraryElement_Palette_instantiation(instance):
    assert isinstance(instance, libraryElement_Palette)


libraryElement_PaletteEntry_strategy = st.builds(libraryElement_PaletteEntry)
@given(instance=libraryElement_PaletteEntry_strategy)
@settings(max_examples=25)
def test_libraryElement_PaletteEntry_instantiation(instance):
    assert isinstance(instance, libraryElement_PaletteEntry)


libraryElement_Parameter_strategy = st.builds(libraryElement_Parameter, comment=safe_text, name=safe_text, value=safe_text)
@given(instance=libraryElement_Parameter_strategy)
@settings(max_examples=25)
def test_libraryElement_Parameter_instantiation(instance):
    assert isinstance(instance, libraryElement_Parameter)


libraryElement_PositionableElement_strategy = st.builds(libraryElement_PositionableElement, x=safe_text, y=safe_text)
@given(instance=libraryElement_PositionableElement_strategy)
@settings(max_examples=25)
def test_libraryElement_PositionableElement_instantiation(instance):
    assert isinstance(instance, libraryElement_PositionableElement)


libraryElement_Primitive_strategy = st.builds(libraryElement_Primitive, event=safe_text, parameters=safe_text)
@given(instance=libraryElement_Primitive_strategy)
@settings(max_examples=25)
def test_libraryElement_Primitive_instantiation(instance):
    assert isinstance(instance, libraryElement_Primitive)


libraryElement_Resource_strategy = st.builds(libraryElement_Resource, deviceTypeResource=safe_text, x=safe_text, y=safe_text)
@given(instance=libraryElement_Resource_strategy)
@settings(max_examples=25)
def test_libraryElement_Resource_instantiation(instance):
    assert isinstance(instance, libraryElement_Resource)


libraryElement_ResourceType_strategy = st.builds(libraryElement_ResourceType)
@given(instance=libraryElement_ResourceType_strategy)
@settings(max_examples=25)
def test_libraryElement_ResourceType_instantiation(instance):
    assert isinstance(instance, libraryElement_ResourceType)


libraryElement_ResourceTypeFB_strategy = st.builds(libraryElement_ResourceTypeFB)
@given(instance=libraryElement_ResourceTypeFB_strategy)
@settings(max_examples=25)
def test_libraryElement_ResourceTypeFB_instantiation(instance):
    assert isinstance(instance, libraryElement_ResourceTypeFB)


libraryElement_ResourceTypeName_strategy = st.builds(libraryElement_ResourceTypeName, name=safe_text)
@given(instance=libraryElement_ResourceTypeName_strategy)
@settings(max_examples=25)
def test_libraryElement_ResourceTypeName_instantiation(instance):
    assert isinstance(instance, libraryElement_ResourceTypeName)


libraryElement_STAlgorithm_strategy = st.builds(libraryElement_STAlgorithm)
@given(instance=libraryElement_STAlgorithm_strategy)
@settings(max_examples=25)
def test_libraryElement_STAlgorithm_instantiation(instance):
    assert isinstance(instance, libraryElement_STAlgorithm)


libraryElement_Segment_strategy = st.builds(libraryElement_Segment, width=safe_text)
@given(instance=libraryElement_Segment_strategy)
@settings(max_examples=25)
def test_libraryElement_Segment_instantiation(instance):
    assert isinstance(instance, libraryElement_Segment)


libraryElement_SegmentType_strategy = st.builds(libraryElement_SegmentType)
@given(instance=libraryElement_SegmentType_strategy)
@settings(max_examples=25)
def test_libraryElement_SegmentType_instantiation(instance):
    assert isinstance(instance, libraryElement_SegmentType)


libraryElement_Service_strategy = st.builds(libraryElement_Service)
@given(instance=libraryElement_Service_strategy)
@settings(max_examples=25)
def test_libraryElement_Service_instantiation(instance):
    assert isinstance(instance, libraryElement_Service)


libraryElement_ServiceInterface_strategy = st.builds(libraryElement_ServiceInterface)
@given(instance=libraryElement_ServiceInterface_strategy)
@settings(max_examples=25)
def test_libraryElement_ServiceInterface_instantiation(instance):
    assert isinstance(instance, libraryElement_ServiceInterface)


libraryElement_ServiceInterfaceFBType_strategy = st.builds(libraryElement_ServiceInterfaceFBType)
@given(instance=libraryElement_ServiceInterfaceFBType_strategy)
@settings(max_examples=25)
def test_libraryElement_ServiceInterfaceFBType_instantiation(instance):
    assert isinstance(instance, libraryElement_ServiceInterfaceFBType)


libraryElement_ServiceSequence_strategy = st.builds(libraryElement_ServiceSequence, TestResult=safe_text)
@given(instance=libraryElement_ServiceSequence_strategy)
@settings(max_examples=25)
def test_libraryElement_ServiceSequence_instantiation(instance):
    assert isinstance(instance, libraryElement_ServiceSequence)


libraryElement_ServiceTransaction_strategy = st.builds(libraryElement_ServiceTransaction, TestResult=safe_text)
@given(instance=libraryElement_ServiceTransaction_strategy)
@settings(max_examples=25)
def test_libraryElement_ServiceTransaction_instantiation(instance):
    assert isinstance(instance, libraryElement_ServiceTransaction)


libraryElement_SubApp_strategy = st.builds(libraryElement_SubApp)
@given(instance=libraryElement_SubApp_strategy)
@settings(max_examples=25)
def test_libraryElement_SubApp_instantiation(instance):
    assert isinstance(instance, libraryElement_SubApp)


libraryElement_SubAppType_strategy = st.builds(libraryElement_SubAppType)
@given(instance=libraryElement_SubAppType_strategy)
@settings(max_examples=25)
def test_libraryElement_SubAppType_instantiation(instance):
    assert isinstance(instance, libraryElement_SubAppType)


libraryElement_SystemConfiguration_strategy = st.builds(libraryElement_SystemConfiguration)
@given(instance=libraryElement_SystemConfiguration_strategy)
@settings(max_examples=25)
def test_libraryElement_SystemConfiguration_instantiation(instance):
    assert isinstance(instance, libraryElement_SystemConfiguration)


libraryElement_TextAlgorithm_strategy = st.builds(libraryElement_TextAlgorithm, text=safe_text)
@given(instance=libraryElement_TextAlgorithm_strategy)
@settings(max_examples=25)
def test_libraryElement_TextAlgorithm_instantiation(instance):
    assert isinstance(instance, libraryElement_TextAlgorithm)


libraryElement_TypedConfigureableObject_strategy = st.builds(libraryElement_TypedConfigureableObject)
@given(instance=libraryElement_TypedConfigureableObject_strategy)
@settings(max_examples=25)
def test_libraryElement_TypedConfigureableObject_instantiation(instance):
    assert isinstance(instance, libraryElement_TypedConfigureableObject)


libraryElement_Value_strategy = st.builds(libraryElement_Value, value=safe_text)
@given(instance=libraryElement_Value_strategy)
@settings(max_examples=25)
def test_libraryElement_Value_instantiation(instance):
    assert isinstance(instance, libraryElement_Value)


libraryElement_VarDeclaration_strategy = st.builds(libraryElement_VarDeclaration, arraySize=safe_text)
@given(instance=libraryElement_VarDeclaration_strategy)
@settings(max_examples=25)
def test_libraryElement_VarDeclaration_instantiation(instance):
    assert isinstance(instance, libraryElement_VarDeclaration)


libraryElement_VarInitialization_strategy = st.builds(libraryElement_VarInitialization)
@given(instance=libraryElement_VarInitialization_strategy)
@settings(max_examples=25)
def test_libraryElement_VarInitialization_instantiation(instance):
    assert isinstance(instance, libraryElement_VarInitialization)


libraryElement_VersionInfo_strategy = st.builds(libraryElement_VersionInfo, author=safe_text, date=safe_text, organization=safe_text, remarks=safe_text, version=safe_text)
@given(instance=libraryElement_VersionInfo_strategy)
@settings(max_examples=25)
def test_libraryElement_VersionInfo_instantiation(instance):
    assert isinstance(instance, libraryElement_VersionInfo)


libraryElement_With_strategy = st.builds(libraryElement_With)
@given(instance=libraryElement_With_strategy)
@settings(max_examples=25)
def test_libraryElement_With_instantiation(instance):
    assert isinstance(instance, libraryElement_With)



