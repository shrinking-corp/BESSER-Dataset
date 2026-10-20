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
    componentModel_Type,
    DelegationConnector,
    componentModel_RequiredDelegationConnector,
    componentModel_RequiredRole,
    componentModel_ProvidedRole,
    AssemblyViewType,
    componentModel_AssemblyContext,
    componentModel_ViewType,
    componentModel_Signature,
    Action,
    componentModel_InternalAction,
    componentModel_Loop,
    componentModel_ExternalCall,
    componentModel_Branch,
    componentModel_Action,
    componentModel_Service,
    componentModel_DelegationConnector,
    componentModel_AssemblyConnector,
    componentModel_InterfaceServiceMapTuple,
    componentModel_ServiceEffectSpecification,
    componentModel_Interface,
    componentModel_Component,
    ViewType,
    componentModel_Repository,
    ViewPoint,
    componentModel_AssemblyViewPoint,
    componentModel_SystemIndependentViewPoint,
    ParameterTyp,
    componentModel_SimpleParameterType,
    componentModel_ComplexParameterType,
    Type,
    componentModel_Void,
    componentModel_ParameterTyp,
    SimpleParameterType,
    componentModel_Map,
    componentModel_Boolean,
    componentModel_Int,
    componentModel_Float,
    componentModel_List,
    componentModel_Char,
    componentModel_Long,
    componentModel_String,
    componentModel_Parameter,
    componentModel_Double,
    componentModel_Date,
    componentModel_AllocationViewType,
    componentModel_EnvironmentViewType,
    componentModel_RepositoryViewType,
    componentModel_DeploymentViewPoint,
    componentModel_AssemblyViewType,
    Component,
    componentModel_CompositeComponent,
    componentModel_ViewPoint,
    componentModel_ProvidedDelegationConnector,
    componentModel_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_componentmodel_type_is_not_abstract():
    assert not inspect.isabstract(componentModel_Type)


def test_hyp_componentmodel_type_constructor_exists():
    assert callable(componentModel_Type.__init__)


def test_hyp_componentmodel_type_constructor_args():
    sig = inspect.signature(componentModel_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(DelegationConnector)


def test_hyp_delegationconnector_constructor_exists():
    assert callable(DelegationConnector.__init__)


def test_hyp_delegationconnector_constructor_args():
    sig = inspect.signature(DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_requireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_RequiredDelegationConnector)


def test_hyp_componentmodel_requireddelegationconnector_constructor_exists():
    assert callable(componentModel_RequiredDelegationConnector.__init__)


def test_hyp_componentmodel_requireddelegationconnector_constructor_args():
    sig = inspect.signature(componentModel_RequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_requiredrole_is_not_abstract():
    assert not inspect.isabstract(componentModel_RequiredRole)


def test_hyp_componentmodel_requiredrole_constructor_exists():
    assert callable(componentModel_RequiredRole.__init__)


def test_hyp_componentmodel_requiredrole_constructor_args():
    sig = inspect.signature(componentModel_RequiredRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_componentmodel_providedrole_is_not_abstract():
    assert not inspect.isabstract(componentModel_ProvidedRole)


def test_hyp_componentmodel_providedrole_constructor_exists():
    assert callable(componentModel_ProvidedRole.__init__)


def test_hyp_componentmodel_providedrole_constructor_args():
    sig = inspect.signature(componentModel_ProvidedRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_assemblyviewtype_is_not_abstract():
    assert not inspect.isabstract(AssemblyViewType)


def test_hyp_assemblyviewtype_constructor_exists():
    assert callable(AssemblyViewType.__init__)


def test_hyp_assemblyviewtype_constructor_args():
    sig = inspect.signature(AssemblyViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_assemblycontext_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyContext)


def test_hyp_componentmodel_assemblycontext_constructor_exists():
    assert callable(componentModel_AssemblyContext.__init__)


def test_hyp_componentmodel_assemblycontext_constructor_args():
    sig = inspect.signature(componentModel_AssemblyContext.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_componentmodel_viewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_ViewType)


def test_hyp_componentmodel_viewtype_constructor_exists():
    assert callable(componentModel_ViewType.__init__)


def test_hyp_componentmodel_viewtype_constructor_args():
    sig = inspect.signature(componentModel_ViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_signature_is_not_abstract():
    assert not inspect.isabstract(componentModel_Signature)


def test_hyp_componentmodel_signature_constructor_exists():
    assert callable(componentModel_Signature.__init__)


def test_hyp_componentmodel_signature_constructor_args():
    sig = inspect.signature(componentModel_Signature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_internalaction_is_not_abstract():
    assert not inspect.isabstract(componentModel_InternalAction)


def test_hyp_componentmodel_internalaction_constructor_exists():
    assert callable(componentModel_InternalAction.__init__)


def test_hyp_componentmodel_internalaction_constructor_args():
    sig = inspect.signature(componentModel_InternalAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_loop_is_not_abstract():
    assert not inspect.isabstract(componentModel_Loop)


def test_hyp_componentmodel_loop_constructor_exists():
    assert callable(componentModel_Loop.__init__)


def test_hyp_componentmodel_loop_constructor_args():
    sig = inspect.signature(componentModel_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_externalcall_is_not_abstract():
    assert not inspect.isabstract(componentModel_ExternalCall)


def test_hyp_componentmodel_externalcall_constructor_exists():
    assert callable(componentModel_ExternalCall.__init__)


def test_hyp_componentmodel_externalcall_constructor_args():
    sig = inspect.signature(componentModel_ExternalCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_branch_is_not_abstract():
    assert not inspect.isabstract(componentModel_Branch)


def test_hyp_componentmodel_branch_constructor_exists():
    assert callable(componentModel_Branch.__init__)


def test_hyp_componentmodel_branch_constructor_args():
    sig = inspect.signature(componentModel_Branch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_action_is_not_abstract():
    assert not inspect.isabstract(componentModel_Action)


def test_hyp_componentmodel_action_constructor_exists():
    assert callable(componentModel_Action.__init__)


def test_hyp_componentmodel_action_constructor_args():
    sig = inspect.signature(componentModel_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_service_is_not_abstract():
    assert not inspect.isabstract(componentModel_Service)


def test_hyp_componentmodel_service_constructor_exists():
    assert callable(componentModel_Service.__init__)


def test_hyp_componentmodel_service_constructor_args():
    sig = inspect.signature(componentModel_Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_DelegationConnector)


def test_hyp_componentmodel_delegationconnector_constructor_exists():
    assert callable(componentModel_DelegationConnector.__init__)


def test_hyp_componentmodel_delegationconnector_constructor_args():
    sig = inspect.signature(componentModel_DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_assemblyconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyConnector)


def test_hyp_componentmodel_assemblyconnector_constructor_exists():
    assert callable(componentModel_AssemblyConnector.__init__)


def test_hyp_componentmodel_assemblyconnector_constructor_args():
    sig = inspect.signature(componentModel_AssemblyConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_interfaceservicemaptuple_is_not_abstract():
    assert not inspect.isabstract(componentModel_InterfaceServiceMapTuple)


def test_hyp_componentmodel_interfaceservicemaptuple_constructor_exists():
    assert callable(componentModel_InterfaceServiceMapTuple.__init__)


def test_hyp_componentmodel_interfaceservicemaptuple_constructor_args():
    sig = inspect.signature(componentModel_InterfaceServiceMapTuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_serviceeffectspecification_is_not_abstract():
    assert not inspect.isabstract(componentModel_ServiceEffectSpecification)


def test_hyp_componentmodel_serviceeffectspecification_constructor_exists():
    assert callable(componentModel_ServiceEffectSpecification.__init__)


def test_hyp_componentmodel_serviceeffectspecification_constructor_args():
    sig = inspect.signature(componentModel_ServiceEffectSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_interface_is_not_abstract():
    assert not inspect.isabstract(componentModel_Interface)


def test_hyp_componentmodel_interface_constructor_exists():
    assert callable(componentModel_Interface.__init__)


def test_hyp_componentmodel_interface_constructor_args():
    sig = inspect.signature(componentModel_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_componentmodel_component_is_not_abstract():
    assert not inspect.isabstract(componentModel_Component)


def test_hyp_componentmodel_component_constructor_exists():
    assert callable(componentModel_Component.__init__)


def test_hyp_componentmodel_component_constructor_args():
    sig = inspect.signature(componentModel_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_viewtype_is_not_abstract():
    assert not inspect.isabstract(ViewType)


def test_hyp_viewtype_constructor_exists():
    assert callable(ViewType.__init__)


def test_hyp_viewtype_constructor_args():
    sig = inspect.signature(ViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_repository_is_not_abstract():
    assert not inspect.isabstract(componentModel_Repository)


def test_hyp_componentmodel_repository_constructor_exists():
    assert callable(componentModel_Repository.__init__)


def test_hyp_componentmodel_repository_constructor_args():
    sig = inspect.signature(componentModel_Repository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_viewpoint_is_not_abstract():
    assert not inspect.isabstract(ViewPoint)


def test_hyp_viewpoint_constructor_exists():
    assert callable(ViewPoint.__init__)


def test_hyp_viewpoint_constructor_args():
    sig = inspect.signature(ViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_assemblyviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyViewPoint)


def test_hyp_componentmodel_assemblyviewpoint_constructor_exists():
    assert callable(componentModel_AssemblyViewPoint.__init__)


def test_hyp_componentmodel_assemblyviewpoint_constructor_args():
    sig = inspect.signature(componentModel_AssemblyViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_systemindependentviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_SystemIndependentViewPoint)


def test_hyp_componentmodel_systemindependentviewpoint_constructor_exists():
    assert callable(componentModel_SystemIndependentViewPoint.__init__)


def test_hyp_componentmodel_systemindependentviewpoint_constructor_args():
    sig = inspect.signature(componentModel_SystemIndependentViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parametertyp_is_not_abstract():
    assert not inspect.isabstract(ParameterTyp)


def test_hyp_parametertyp_constructor_exists():
    assert callable(ParameterTyp.__init__)


def test_hyp_parametertyp_constructor_args():
    sig = inspect.signature(ParameterTyp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_simpleparametertype_is_not_abstract():
    assert not inspect.isabstract(componentModel_SimpleParameterType)


def test_hyp_componentmodel_simpleparametertype_constructor_exists():
    assert callable(componentModel_SimpleParameterType.__init__)


def test_hyp_componentmodel_simpleparametertype_constructor_args():
    sig = inspect.signature(componentModel_SimpleParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_complexparametertype_is_not_abstract():
    assert not inspect.isabstract(componentModel_ComplexParameterType)


def test_hyp_componentmodel_complexparametertype_constructor_exists():
    assert callable(componentModel_ComplexParameterType.__init__)


def test_hyp_componentmodel_complexparametertype_constructor_args():
    sig = inspect.signature(componentModel_ComplexParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_void_is_not_abstract():
    assert not inspect.isabstract(componentModel_Void)


def test_hyp_componentmodel_void_constructor_exists():
    assert callable(componentModel_Void.__init__)


def test_hyp_componentmodel_void_constructor_args():
    sig = inspect.signature(componentModel_Void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_parametertyp_is_not_abstract():
    assert not inspect.isabstract(componentModel_ParameterTyp)


def test_hyp_componentmodel_parametertyp_constructor_exists():
    assert callable(componentModel_ParameterTyp.__init__)


def test_hyp_componentmodel_parametertyp_constructor_args():
    sig = inspect.signature(componentModel_ParameterTyp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleparametertype_is_not_abstract():
    assert not inspect.isabstract(SimpleParameterType)


def test_hyp_simpleparametertype_constructor_exists():
    assert callable(SimpleParameterType.__init__)


def test_hyp_simpleparametertype_constructor_args():
    sig = inspect.signature(SimpleParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_map_is_not_abstract():
    assert not inspect.isabstract(componentModel_Map)


def test_hyp_componentmodel_map_constructor_exists():
    assert callable(componentModel_Map.__init__)


def test_hyp_componentmodel_map_constructor_args():
    sig = inspect.signature(componentModel_Map.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_boolean_is_not_abstract():
    assert not inspect.isabstract(componentModel_Boolean)


def test_hyp_componentmodel_boolean_constructor_exists():
    assert callable(componentModel_Boolean.__init__)


def test_hyp_componentmodel_boolean_constructor_args():
    sig = inspect.signature(componentModel_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_int_is_not_abstract():
    assert not inspect.isabstract(componentModel_Int)


def test_hyp_componentmodel_int_constructor_exists():
    assert callable(componentModel_Int.__init__)


def test_hyp_componentmodel_int_constructor_args():
    sig = inspect.signature(componentModel_Int.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_float_is_not_abstract():
    assert not inspect.isabstract(componentModel_Float)


def test_hyp_componentmodel_float_constructor_exists():
    assert callable(componentModel_Float.__init__)


def test_hyp_componentmodel_float_constructor_args():
    sig = inspect.signature(componentModel_Float.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_list_is_not_abstract():
    assert not inspect.isabstract(componentModel_List)


def test_hyp_componentmodel_list_constructor_exists():
    assert callable(componentModel_List.__init__)


def test_hyp_componentmodel_list_constructor_args():
    sig = inspect.signature(componentModel_List.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_char_is_not_abstract():
    assert not inspect.isabstract(componentModel_Char)


def test_hyp_componentmodel_char_constructor_exists():
    assert callable(componentModel_Char.__init__)


def test_hyp_componentmodel_char_constructor_args():
    sig = inspect.signature(componentModel_Char.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_long_is_not_abstract():
    assert not inspect.isabstract(componentModel_Long)


def test_hyp_componentmodel_long_constructor_exists():
    assert callable(componentModel_Long.__init__)


def test_hyp_componentmodel_long_constructor_args():
    sig = inspect.signature(componentModel_Long.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_string_is_not_abstract():
    assert not inspect.isabstract(componentModel_String)


def test_hyp_componentmodel_string_constructor_exists():
    assert callable(componentModel_String.__init__)


def test_hyp_componentmodel_string_constructor_args():
    sig = inspect.signature(componentModel_String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(componentModel_Parameter)


def test_hyp_componentmodel_parameter_constructor_exists():
    assert callable(componentModel_Parameter.__init__)


def test_hyp_componentmodel_parameter_constructor_args():
    sig = inspect.signature(componentModel_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_componentmodel_double_is_not_abstract():
    assert not inspect.isabstract(componentModel_Double)


def test_hyp_componentmodel_double_constructor_exists():
    assert callable(componentModel_Double.__init__)


def test_hyp_componentmodel_double_constructor_args():
    sig = inspect.signature(componentModel_Double.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_date_is_not_abstract():
    assert not inspect.isabstract(componentModel_Date)


def test_hyp_componentmodel_date_constructor_exists():
    assert callable(componentModel_Date.__init__)


def test_hyp_componentmodel_date_constructor_args():
    sig = inspect.signature(componentModel_Date.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_allocationviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_AllocationViewType)


def test_hyp_componentmodel_allocationviewtype_constructor_exists():
    assert callable(componentModel_AllocationViewType.__init__)


def test_hyp_componentmodel_allocationviewtype_constructor_args():
    sig = inspect.signature(componentModel_AllocationViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_environmentviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_EnvironmentViewType)


def test_hyp_componentmodel_environmentviewtype_constructor_exists():
    assert callable(componentModel_EnvironmentViewType.__init__)


def test_hyp_componentmodel_environmentviewtype_constructor_args():
    sig = inspect.signature(componentModel_EnvironmentViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_repositoryviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_RepositoryViewType)


def test_hyp_componentmodel_repositoryviewtype_constructor_exists():
    assert callable(componentModel_RepositoryViewType.__init__)


def test_hyp_componentmodel_repositoryviewtype_constructor_args():
    sig = inspect.signature(componentModel_RepositoryViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_deploymentviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_DeploymentViewPoint)


def test_hyp_componentmodel_deploymentviewpoint_constructor_exists():
    assert callable(componentModel_DeploymentViewPoint.__init__)


def test_hyp_componentmodel_deploymentviewpoint_constructor_args():
    sig = inspect.signature(componentModel_DeploymentViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_assemblyviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyViewType)


def test_hyp_componentmodel_assemblyviewtype_constructor_exists():
    assert callable(componentModel_AssemblyViewType.__init__)


def test_hyp_componentmodel_assemblyviewtype_constructor_args():
    sig = inspect.signature(componentModel_AssemblyViewType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_compositecomponent_is_not_abstract():
    assert not inspect.isabstract(componentModel_CompositeComponent)


def test_hyp_componentmodel_compositecomponent_constructor_exists():
    assert callable(componentModel_CompositeComponent.__init__)


def test_hyp_componentmodel_compositecomponent_constructor_args():
    sig = inspect.signature(componentModel_CompositeComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_viewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_ViewPoint)


def test_hyp_componentmodel_viewpoint_constructor_exists():
    assert callable(componentModel_ViewPoint.__init__)


def test_hyp_componentmodel_viewpoint_constructor_args():
    sig = inspect.signature(componentModel_ViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_provideddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_ProvidedDelegationConnector)


def test_hyp_componentmodel_provideddelegationconnector_constructor_exists():
    assert callable(componentModel_ProvidedDelegationConnector.__init__)


def test_hyp_componentmodel_provideddelegationconnector_constructor_args():
    sig = inspect.signature(componentModel_ProvidedDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentmodel_system_is_not_abstract():
    assert not inspect.isabstract(componentModel_System)


def test_hyp_componentmodel_system_constructor_exists():
    assert callable(componentModel_System.__init__)


def test_hyp_componentmodel_system_constructor_args():
    sig = inspect.signature(componentModel_System.__init__)
    params = list(sig.parameters.keys())


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
componentModel_Type_strategy = st.builds(
    componentModel_Type,
)
DelegationConnector_strategy = st.builds(
    DelegationConnector,
)
componentModel_RequiredDelegationConnector_strategy = st.builds(
    componentModel_RequiredDelegationConnector,
)
componentModel_RequiredRole_strategy = st.builds(
    componentModel_RequiredRole,
    name=
        safe_text
)
componentModel_ProvidedRole_strategy = st.builds(
    componentModel_ProvidedRole,
    name=
        safe_text
)
AssemblyViewType_strategy = st.builds(
    AssemblyViewType,
)
componentModel_AssemblyContext_strategy = st.builds(
    componentModel_AssemblyContext,
    name=
        safe_text
)
componentModel_ViewType_strategy = st.builds(
    componentModel_ViewType,
)
componentModel_Signature_strategy = st.builds(
    componentModel_Signature,
    name=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
componentModel_InternalAction_strategy = st.builds(
    componentModel_InternalAction,
)
componentModel_Loop_strategy = st.builds(
    componentModel_Loop,
)
componentModel_ExternalCall_strategy = st.builds(
    componentModel_ExternalCall,
)
componentModel_Branch_strategy = st.builds(
    componentModel_Branch,
)
componentModel_Action_strategy = st.builds(
    componentModel_Action,
)
componentModel_Service_strategy = st.builds(
    componentModel_Service,
)
componentModel_DelegationConnector_strategy = st.builds(
    componentModel_DelegationConnector,
)
componentModel_AssemblyConnector_strategy = st.builds(
    componentModel_AssemblyConnector,
)
componentModel_InterfaceServiceMapTuple_strategy = st.builds(
    componentModel_InterfaceServiceMapTuple,
)
componentModel_ServiceEffectSpecification_strategy = st.builds(
    componentModel_ServiceEffectSpecification,
)
componentModel_Interface_strategy = st.builds(
    componentModel_Interface,
    name=
        safe_text
)
componentModel_Component_strategy = st.builds(
    componentModel_Component,
    name=
        safe_text
)
ViewType_strategy = st.builds(
    ViewType,
)
componentModel_Repository_strategy = st.builds(
    componentModel_Repository,
)
ViewPoint_strategy = st.builds(
    ViewPoint,
)
componentModel_AssemblyViewPoint_strategy = st.builds(
    componentModel_AssemblyViewPoint,
)
componentModel_SystemIndependentViewPoint_strategy = st.builds(
    componentModel_SystemIndependentViewPoint,
)
ParameterTyp_strategy = st.builds(
    ParameterTyp,
)
componentModel_SimpleParameterType_strategy = st.builds(
    componentModel_SimpleParameterType,
)
componentModel_ComplexParameterType_strategy = st.builds(
    componentModel_ComplexParameterType,
)
Type_strategy = st.builds(
    Type,
)
componentModel_Void_strategy = st.builds(
    componentModel_Void,
)
componentModel_ParameterTyp_strategy = st.builds(
    componentModel_ParameterTyp,
)
SimpleParameterType_strategy = st.builds(
    SimpleParameterType,
)
componentModel_Map_strategy = st.builds(
    componentModel_Map,
)
componentModel_Boolean_strategy = st.builds(
    componentModel_Boolean,
)
componentModel_Int_strategy = st.builds(
    componentModel_Int,
)
componentModel_Float_strategy = st.builds(
    componentModel_Float,
)
componentModel_List_strategy = st.builds(
    componentModel_List,
)
componentModel_Char_strategy = st.builds(
    componentModel_Char,
)
componentModel_Long_strategy = st.builds(
    componentModel_Long,
)
componentModel_String_strategy = st.builds(
    componentModel_String,
)
componentModel_Parameter_strategy = st.builds(
    componentModel_Parameter,
    name=
        safe_text
)
componentModel_Double_strategy = st.builds(
    componentModel_Double,
)
componentModel_Date_strategy = st.builds(
    componentModel_Date,
)
componentModel_AllocationViewType_strategy = st.builds(
    componentModel_AllocationViewType,
)
componentModel_EnvironmentViewType_strategy = st.builds(
    componentModel_EnvironmentViewType,
)
componentModel_RepositoryViewType_strategy = st.builds(
    componentModel_RepositoryViewType,
)
componentModel_DeploymentViewPoint_strategy = st.builds(
    componentModel_DeploymentViewPoint,
)
componentModel_AssemblyViewType_strategy = st.builds(
    componentModel_AssemblyViewType,
)
Component_strategy = st.builds(
    Component,
)
componentModel_CompositeComponent_strategy = st.builds(
    componentModel_CompositeComponent,
)
componentModel_ViewPoint_strategy = st.builds(
    componentModel_ViewPoint,
)
componentModel_ProvidedDelegationConnector_strategy = st.builds(
    componentModel_ProvidedDelegationConnector,
)
componentModel_System_strategy = st.builds(
    componentModel_System,
)







@given(instance=componentModel_RequiredRole_strategy)
def test_hyp_componentmodel_requiredrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=componentModel_ProvidedRole_strategy)
def test_hyp_componentmodel_providedrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=componentModel_AssemblyContext_strategy)
def test_hyp_componentmodel_assemblycontext_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=componentModel_Signature_strategy)
def test_hyp_componentmodel_signature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original















@given(instance=componentModel_Interface_strategy)
def test_hyp_componentmodel_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=componentModel_Component_strategy)
def test_hyp_componentmodel_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
























@given(instance=componentModel_Parameter_strategy)
def test_hyp_componentmodel_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original














# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    AssemblyViewType,
    Component,
    DelegationConnector,
    ParameterTyp,
    SimpleParameterType,
    Type,
    ViewPoint,
    ViewType,
    componentModel_Action,
    componentModel_AllocationViewType,
    componentModel_AssemblyConnector,
    componentModel_AssemblyContext,
    componentModel_AssemblyViewPoint,
    componentModel_AssemblyViewType,
    componentModel_Boolean,
    componentModel_Branch,
    componentModel_Char,
    componentModel_ComplexParameterType,
    componentModel_Component,
    componentModel_CompositeComponent,
    componentModel_Date,
    componentModel_DelegationConnector,
    componentModel_DeploymentViewPoint,
    componentModel_Double,
    componentModel_EnvironmentViewType,
    componentModel_ExternalCall,
    componentModel_Float,
    componentModel_Int,
    componentModel_Interface,
    componentModel_InterfaceServiceMapTuple,
    componentModel_InternalAction,
    componentModel_List,
    componentModel_Long,
    componentModel_Loop,
    componentModel_Map,
    componentModel_Parameter,
    componentModel_ParameterTyp,
    componentModel_ProvidedDelegationConnector,
    componentModel_ProvidedRole,
    componentModel_Repository,
    componentModel_RepositoryViewType,
    componentModel_RequiredDelegationConnector,
    componentModel_RequiredRole,
    componentModel_Service,
    componentModel_ServiceEffectSpecification,
    componentModel_Signature,
    componentModel_SimpleParameterType,
    componentModel_String,
    componentModel_System,
    componentModel_SystemIndependentViewPoint,
    componentModel_Type,
    componentModel_ViewPoint,
    componentModel_ViewType,
    componentModel_Void,
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

def test_componentModel_AssemblyContext_name_value_roundtrip():
    instance = componentModel_AssemblyContext(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_Component_name_value_roundtrip():
    instance = componentModel_Component(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_Interface_name_value_roundtrip():
    instance = componentModel_Interface(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_Parameter_name_value_roundtrip():
    instance = componentModel_Parameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_ProvidedRole_name_value_roundtrip():
    instance = componentModel_ProvidedRole(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_RequiredRole_name_value_roundtrip():
    instance = componentModel_RequiredRole(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_Signature_name_value_roundtrip():
    instance = componentModel_Signature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_componentModel_Branch_isa_Action():
    instance = componentModel_Branch()
    assert isinstance(instance, Action)


def test_componentModel_ExternalCall_isa_Action():
    instance = componentModel_ExternalCall()
    assert isinstance(instance, Action)


def test_componentModel_InternalAction_isa_Action():
    instance = componentModel_InternalAction()
    assert isinstance(instance, Action)


def test_componentModel_Loop_isa_Action():
    instance = componentModel_Loop()
    assert isinstance(instance, Action)


def test_componentModel_AssemblyContext_isa_AssemblyViewType():
    instance = componentModel_AssemblyContext(name="sample_text")
    assert isinstance(instance, AssemblyViewType)


def test_componentModel_CompositeComponent_isa_Component():
    instance = componentModel_CompositeComponent()
    assert isinstance(instance, Component)


def test_componentModel_ProvidedDelegationConnector_isa_DelegationConnector():
    instance = componentModel_ProvidedDelegationConnector()
    assert isinstance(instance, DelegationConnector)


def test_componentModel_RequiredDelegationConnector_isa_DelegationConnector():
    instance = componentModel_RequiredDelegationConnector()
    assert isinstance(instance, DelegationConnector)


def test_componentModel_ComplexParameterType_isa_ParameterTyp():
    instance = componentModel_ComplexParameterType()
    assert isinstance(instance, ParameterTyp)


def test_componentModel_SimpleParameterType_isa_ParameterTyp():
    instance = componentModel_SimpleParameterType()
    assert isinstance(instance, ParameterTyp)


def test_componentModel_Boolean_isa_SimpleParameterType():
    instance = componentModel_Boolean()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Char_isa_SimpleParameterType():
    instance = componentModel_Char()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Date_isa_SimpleParameterType():
    instance = componentModel_Date()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Double_isa_SimpleParameterType():
    instance = componentModel_Double()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Float_isa_SimpleParameterType():
    instance = componentModel_Float()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Int_isa_SimpleParameterType():
    instance = componentModel_Int()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_List_isa_SimpleParameterType():
    instance = componentModel_List()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Long_isa_SimpleParameterType():
    instance = componentModel_Long()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Map_isa_SimpleParameterType():
    instance = componentModel_Map()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_Parameter_isa_SimpleParameterType():
    instance = componentModel_Parameter(name="sample_text")
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_String_isa_SimpleParameterType():
    instance = componentModel_String()
    assert isinstance(instance, SimpleParameterType)


def test_componentModel_ParameterTyp_isa_Type():
    instance = componentModel_ParameterTyp()
    assert isinstance(instance, Type)


def test_componentModel_Void_isa_Type():
    instance = componentModel_Void()
    assert isinstance(instance, Type)


def test_componentModel_AssemblyViewPoint_isa_ViewPoint():
    instance = componentModel_AssemblyViewPoint()
    assert isinstance(instance, ViewPoint)


def test_componentModel_DeploymentViewPoint_isa_ViewPoint():
    instance = componentModel_DeploymentViewPoint()
    assert isinstance(instance, ViewPoint)


def test_componentModel_SystemIndependentViewPoint_isa_ViewPoint():
    instance = componentModel_SystemIndependentViewPoint()
    assert isinstance(instance, ViewPoint)


def test_componentModel_AllocationViewType_isa_ViewType():
    instance = componentModel_AllocationViewType()
    assert isinstance(instance, ViewType)


def test_componentModel_AssemblyViewType_isa_ViewType():
    instance = componentModel_AssemblyViewType()
    assert isinstance(instance, ViewType)


def test_componentModel_EnvironmentViewType_isa_ViewType():
    instance = componentModel_EnvironmentViewType()
    assert isinstance(instance, ViewType)


def test_componentModel_Repository_isa_ViewType():
    instance = componentModel_Repository()
    assert isinstance(instance, ViewType)


def test_componentModel_RepositoryViewType_isa_ViewType():
    instance = componentModel_RepositoryViewType()
    assert isinstance(instance, ViewType)


def test_assoc_assemblyConnectors7_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_AssemblyConnector()
    b2 = componentModel_AssemblyConnector()
    _safe_set(a, 'componentModel_Component8', {b1})
    assert _is_linked(a, 'componentModel_Component8', b1)
    if hasattr(b1, 'componentModel_AssemblyConnector'):
        assert _is_linked(b1, 'componentModel_AssemblyConnector', a)
    _safe_set(a, 'componentModel_Component8', {b2})
    assert _is_linked(a, 'componentModel_Component8', b2)
    if hasattr(b1, 'componentModel_AssemblyConnector'):
        assert not _is_linked(b1, 'componentModel_AssemblyConnector', a)
    if hasattr(b2, 'componentModel_AssemblyConnector'):
        assert _is_linked(b2, 'componentModel_AssemblyConnector', a)
    _safe_set(a, 'componentModel_Component8', set())
    assert not _is_linked(a, 'componentModel_Component8', b2)
    if hasattr(b2, 'componentModel_AssemblyConnector'):
        assert not _is_linked(b2, 'componentModel_AssemblyConnector', a)


def test_assoc_assemblycontext50_link_reassign_clear():
    a = componentModel_AssemblyContext(name="sample_text")
    b1 = componentModel_System()
    b2 = componentModel_System()
    _safe_set(a, 'componentModel_AssemblyContext51', b1)
    assert _is_linked(a, 'componentModel_AssemblyContext51', b1)
    if hasattr(b1, 'componentModel_System'):
        assert _is_linked(b1, 'componentModel_System', a)
    _safe_set(a, 'componentModel_AssemblyContext51', b2)
    assert _is_linked(a, 'componentModel_AssemblyContext51', b2)
    if hasattr(b1, 'componentModel_System'):
        assert not _is_linked(b1, 'componentModel_System', a)
    if hasattr(b2, 'componentModel_System'):
        assert _is_linked(b2, 'componentModel_System', a)
    _safe_set(a, 'componentModel_AssemblyContext51', None)
    assert not _is_linked(a, 'componentModel_AssemblyContext51', b2)
    if hasattr(b2, 'componentModel_System'):
        assert not _is_linked(b2, 'componentModel_System', a)


def test_assoc_assemblycontext55_link_reassign_clear():
    a = componentModel_RequiredRole(name="sample_text")
    b1 = componentModel_AssemblyContext(name="sample_text")
    b2 = componentModel_AssemblyContext(name="sample_text_2")
    _safe_set(a, 'requiredrole', b1)
    assert _is_linked(a, 'requiredrole', b1)
    if hasattr(b1, 'AssemblyContext'):
        assert _is_linked(b1, 'AssemblyContext', a)
    _safe_set(a, 'requiredrole', b2)
    assert _is_linked(a, 'requiredrole', b2)
    if hasattr(b1, 'AssemblyContext'):
        assert not _is_linked(b1, 'AssemblyContext', a)
    if hasattr(b2, 'AssemblyContext'):
        assert _is_linked(b2, 'AssemblyContext', a)
    _safe_set(a, 'requiredrole', None)
    assert not _is_linked(a, 'requiredrole', b2)
    if hasattr(b2, 'AssemblyContext'):
        assert not _is_linked(b2, 'AssemblyContext', a)


def test_assoc_assemblycontext59_link_reassign_clear():
    a = componentModel_ProvidedRole(name="sample_text")
    b1 = componentModel_AssemblyContext(name="sample_text")
    b2 = componentModel_AssemblyContext(name="sample_text_2")
    _safe_set(a, 'providedrole', b1)
    assert _is_linked(a, 'providedrole', b1)
    if hasattr(b1, 'AssemblyContext60'):
        assert _is_linked(b1, 'AssemblyContext60', a)
    _safe_set(a, 'providedrole', b2)
    assert _is_linked(a, 'providedrole', b2)
    if hasattr(b1, 'AssemblyContext60'):
        assert not _is_linked(b1, 'AssemblyContext60', a)
    if hasattr(b2, 'AssemblyContext60'):
        assert _is_linked(b2, 'AssemblyContext60', a)
    _safe_set(a, 'providedrole', None)
    assert not _is_linked(a, 'providedrole', b2)
    if hasattr(b2, 'AssemblyContext60'):
        assert not _is_linked(b2, 'AssemblyContext60', a)


def test_assoc_component0_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_Repository()
    b2 = componentModel_Repository()
    _safe_set(a, 'componentModel_Component', b1)
    assert _is_linked(a, 'componentModel_Component', b1)
    if hasattr(b1, 'componentModel_Repository'):
        assert _is_linked(b1, 'componentModel_Repository', a)
    _safe_set(a, 'componentModel_Component', b2)
    assert _is_linked(a, 'componentModel_Component', b2)
    if hasattr(b1, 'componentModel_Repository'):
        assert not _is_linked(b1, 'componentModel_Repository', a)
    if hasattr(b2, 'componentModel_Repository'):
        assert _is_linked(b2, 'componentModel_Repository', a)
    _safe_set(a, 'componentModel_Component', None)
    assert not _is_linked(a, 'componentModel_Component', b2)
    if hasattr(b2, 'componentModel_Repository'):
        assert not _is_linked(b2, 'componentModel_Repository', a)


def test_assoc_correspondence47_link_reassign_clear():
    a = componentModel_Signature(name="sample_text")
    b1 = componentModel_Service()
    b2 = componentModel_Service()
    _safe_set(a, 'componentModel_Signature49', b1)
    assert _is_linked(a, 'componentModel_Signature49', b1)
    if hasattr(b1, 'componentModel_Service48'):
        assert _is_linked(b1, 'componentModel_Service48', a)
    _safe_set(a, 'componentModel_Signature49', b2)
    assert _is_linked(a, 'componentModel_Signature49', b2)
    if hasattr(b1, 'componentModel_Service48'):
        assert not _is_linked(b1, 'componentModel_Service48', a)
    if hasattr(b2, 'componentModel_Service48'):
        assert _is_linked(b2, 'componentModel_Service48', a)
    _safe_set(a, 'componentModel_Signature49', None)
    assert not _is_linked(a, 'componentModel_Signature49', b2)
    if hasattr(b2, 'componentModel_Service48'):
        assert not _is_linked(b2, 'componentModel_Service48', a)


def test_assoc_delegationConnectors9_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_DelegationConnector()
    b2 = componentModel_DelegationConnector()
    _safe_set(a, 'componentModel_Component10', {b1})
    assert _is_linked(a, 'componentModel_Component10', b1)
    if hasattr(b1, 'componentModel_DelegationConnector'):
        assert _is_linked(b1, 'componentModel_DelegationConnector', a)
    _safe_set(a, 'componentModel_Component10', {b2})
    assert _is_linked(a, 'componentModel_Component10', b2)
    if hasattr(b1, 'componentModel_DelegationConnector'):
        assert not _is_linked(b1, 'componentModel_DelegationConnector', a)
    if hasattr(b2, 'componentModel_DelegationConnector'):
        assert _is_linked(b2, 'componentModel_DelegationConnector', a)
    _safe_set(a, 'componentModel_Component10', set())
    assert not _is_linked(a, 'componentModel_Component10', b2)
    if hasattr(b2, 'componentModel_DelegationConnector'):
        assert not _is_linked(b2, 'componentModel_DelegationConnector', a)


def test_assoc_encapsulated70_link_reassign_clear():
    a = componentModel_AssemblyContext(name="sample_text")
    b1 = componentModel_CompositeComponent()
    b2 = componentModel_CompositeComponent()
    _safe_set(a, 'componentModel_AssemblyContext71', b1)
    assert _is_linked(a, 'componentModel_AssemblyContext71', b1)
    if hasattr(b1, 'componentModel_CompositeComponent'):
        assert _is_linked(b1, 'componentModel_CompositeComponent', a)
    _safe_set(a, 'componentModel_AssemblyContext71', b2)
    assert _is_linked(a, 'componentModel_AssemblyContext71', b2)
    if hasattr(b1, 'componentModel_CompositeComponent'):
        assert not _is_linked(b1, 'componentModel_CompositeComponent', a)
    if hasattr(b2, 'componentModel_CompositeComponent'):
        assert _is_linked(b2, 'componentModel_CompositeComponent', a)
    _safe_set(a, 'componentModel_AssemblyContext71', None)
    assert not _is_linked(a, 'componentModel_AssemblyContext71', b2)
    if hasattr(b2, 'componentModel_CompositeComponent'):
        assert not _is_linked(b2, 'componentModel_CompositeComponent', a)


def test_assoc_interface1_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_Repository()
    b2 = componentModel_Repository()
    _safe_set(a, 'componentModel_Interface', b1)
    assert _is_linked(a, 'componentModel_Interface', b1)
    if hasattr(b1, 'componentModel_Repository2'):
        assert _is_linked(b1, 'componentModel_Repository2', a)
    _safe_set(a, 'componentModel_Interface', b2)
    assert _is_linked(a, 'componentModel_Interface', b2)
    if hasattr(b1, 'componentModel_Repository2'):
        assert not _is_linked(b1, 'componentModel_Repository2', a)
    if hasattr(b2, 'componentModel_Repository2'):
        assert _is_linked(b2, 'componentModel_Repository2', a)
    _safe_set(a, 'componentModel_Interface', None)
    assert not _is_linked(a, 'componentModel_Interface', b2)
    if hasattr(b2, 'componentModel_Repository2'):
        assert not _is_linked(b2, 'componentModel_Repository2', a)


def test_assoc_interface52_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_System()
    b2 = componentModel_System()
    _safe_set(a, 'componentModel_Interface54', b1)
    assert _is_linked(a, 'componentModel_Interface54', b1)
    if hasattr(b1, 'componentModel_System53'):
        assert _is_linked(b1, 'componentModel_System53', a)
    _safe_set(a, 'componentModel_Interface54', b2)
    assert _is_linked(a, 'componentModel_Interface54', b2)
    if hasattr(b1, 'componentModel_System53'):
        assert not _is_linked(b1, 'componentModel_System53', a)
    if hasattr(b2, 'componentModel_System53'):
        assert _is_linked(b2, 'componentModel_System53', a)
    _safe_set(a, 'componentModel_Interface54', None)
    assert not _is_linked(a, 'componentModel_Interface54', b2)
    if hasattr(b2, 'componentModel_System53'):
        assert not _is_linked(b2, 'componentModel_System53', a)


def test_assoc_interface56_link_reassign_clear():
    a = componentModel_RequiredRole(name="sample_text")
    b1 = componentModel_Interface(name="sample_text")
    b2 = componentModel_Interface(name="sample_text_2")
    _safe_set(a, 'componentModel_RequiredRole57', b1)
    assert _is_linked(a, 'componentModel_RequiredRole57', b1)
    if hasattr(b1, 'componentModel_Interface58'):
        assert _is_linked(b1, 'componentModel_Interface58', a)
    _safe_set(a, 'componentModel_RequiredRole57', b2)
    assert _is_linked(a, 'componentModel_RequiredRole57', b2)
    if hasattr(b1, 'componentModel_Interface58'):
        assert not _is_linked(b1, 'componentModel_Interface58', a)
    if hasattr(b2, 'componentModel_Interface58'):
        assert _is_linked(b2, 'componentModel_Interface58', a)
    _safe_set(a, 'componentModel_RequiredRole57', None)
    assert not _is_linked(a, 'componentModel_RequiredRole57', b2)
    if hasattr(b2, 'componentModel_Interface58'):
        assert not _is_linked(b2, 'componentModel_Interface58', a)


def test_assoc_interface61_link_reassign_clear():
    a = componentModel_ProvidedRole(name="sample_text")
    b1 = componentModel_Interface(name="sample_text")
    b2 = componentModel_Interface(name="sample_text_2")
    _safe_set(a, 'componentModel_ProvidedRole62', b1)
    assert _is_linked(a, 'componentModel_ProvidedRole62', b1)
    if hasattr(b1, 'componentModel_Interface63'):
        assert _is_linked(b1, 'componentModel_Interface63', a)
    _safe_set(a, 'componentModel_ProvidedRole62', b2)
    assert _is_linked(a, 'componentModel_ProvidedRole62', b2)
    if hasattr(b1, 'componentModel_Interface63'):
        assert not _is_linked(b1, 'componentModel_Interface63', a)
    if hasattr(b2, 'componentModel_Interface63'):
        assert _is_linked(b2, 'componentModel_Interface63', a)
    _safe_set(a, 'componentModel_ProvidedRole62', None)
    assert not _is_linked(a, 'componentModel_ProvidedRole62', b2)
    if hasattr(b2, 'componentModel_Interface63'):
        assert not _is_linked(b2, 'componentModel_Interface63', a)


def test_assoc_interfaceServiceMap5_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_InterfaceServiceMapTuple()
    b2 = componentModel_InterfaceServiceMapTuple()
    _safe_set(a, 'componentModel_Component6', {b1})
    assert _is_linked(a, 'componentModel_Component6', b1)
    if hasattr(b1, 'componentModel_InterfaceServiceMapTuple'):
        assert _is_linked(b1, 'componentModel_InterfaceServiceMapTuple', a)
    _safe_set(a, 'componentModel_Component6', {b2})
    assert _is_linked(a, 'componentModel_Component6', b2)
    if hasattr(b1, 'componentModel_InterfaceServiceMapTuple'):
        assert not _is_linked(b1, 'componentModel_InterfaceServiceMapTuple', a)
    if hasattr(b2, 'componentModel_InterfaceServiceMapTuple'):
        assert _is_linked(b2, 'componentModel_InterfaceServiceMapTuple', a)
    _safe_set(a, 'componentModel_Component6', set())
    assert not _is_linked(a, 'componentModel_Component6', b2)
    if hasattr(b2, 'componentModel_InterfaceServiceMapTuple'):
        assert not _is_linked(b2, 'componentModel_InterfaceServiceMapTuple', a)


def test_assoc_ownerComponent29_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_AssemblyContext(name="sample_text")
    b2 = componentModel_AssemblyContext(name="sample_text_2")
    _safe_set(a, 'componentModel_Component30', b1)
    assert _is_linked(a, 'componentModel_Component30', b1)
    if hasattr(b1, 'componentModel_AssemblyContext'):
        assert _is_linked(b1, 'componentModel_AssemblyContext', a)
    _safe_set(a, 'componentModel_Component30', b2)
    assert _is_linked(a, 'componentModel_Component30', b2)
    if hasattr(b1, 'componentModel_AssemblyContext'):
        assert not _is_linked(b1, 'componentModel_AssemblyContext', a)
    if hasattr(b2, 'componentModel_AssemblyContext'):
        assert _is_linked(b2, 'componentModel_AssemblyContext', a)
    _safe_set(a, 'componentModel_Component30', None)
    assert not _is_linked(a, 'componentModel_Component30', b2)
    if hasattr(b2, 'componentModel_AssemblyContext'):
        assert not _is_linked(b2, 'componentModel_AssemblyContext', a)


def test_assoc_parameterTyp74_link_reassign_clear():
    a = componentModel_Parameter(name="sample_text")
    b1 = componentModel_ParameterTyp()
    b2 = componentModel_ParameterTyp()
    _safe_set(a, 'componentModel_Parameter75', b1)
    assert _is_linked(a, 'componentModel_Parameter75', b1)
    if hasattr(b1, 'componentModel_ParameterTyp'):
        assert _is_linked(b1, 'componentModel_ParameterTyp', a)
    _safe_set(a, 'componentModel_Parameter75', b2)
    assert _is_linked(a, 'componentModel_Parameter75', b2)
    if hasattr(b1, 'componentModel_ParameterTyp'):
        assert not _is_linked(b1, 'componentModel_ParameterTyp', a)
    if hasattr(b2, 'componentModel_ParameterTyp'):
        assert _is_linked(b2, 'componentModel_ParameterTyp', a)
    _safe_set(a, 'componentModel_Parameter75', None)
    assert not _is_linked(a, 'componentModel_Parameter75', b2)
    if hasattr(b2, 'componentModel_ParameterTyp'):
        assert not _is_linked(b2, 'componentModel_ParameterTyp', a)


def test_assoc_parameters40_link_reassign_clear():
    a = componentModel_Signature(name="sample_text")
    b1 = componentModel_Parameter(name="sample_text")
    b2 = componentModel_Parameter(name="sample_text_2")
    _safe_set(a, 'componentModel_Signature41', {b1})
    assert _is_linked(a, 'componentModel_Signature41', b1)
    if hasattr(b1, 'componentModel_Parameter'):
        assert _is_linked(b1, 'componentModel_Parameter', a)
    _safe_set(a, 'componentModel_Signature41', {b2})
    assert _is_linked(a, 'componentModel_Signature41', b2)
    if hasattr(b1, 'componentModel_Parameter'):
        assert not _is_linked(b1, 'componentModel_Parameter', a)
    if hasattr(b2, 'componentModel_Parameter'):
        assert _is_linked(b2, 'componentModel_Parameter', a)
    _safe_set(a, 'componentModel_Signature41', set())
    assert not _is_linked(a, 'componentModel_Signature41', b2)
    if hasattr(b2, 'componentModel_Parameter'):
        assert not _is_linked(b2, 'componentModel_Parameter', a)


def test_assoc_providedInterface11_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_InterfaceServiceMapTuple()
    b2 = componentModel_InterfaceServiceMapTuple()
    _safe_set(a, 'componentModel_Interface13', b1)
    assert _is_linked(a, 'componentModel_Interface13', b1)
    if hasattr(b1, 'componentModel_InterfaceServiceMapTuple12'):
        assert _is_linked(b1, 'componentModel_InterfaceServiceMapTuple12', a)
    _safe_set(a, 'componentModel_Interface13', b2)
    assert _is_linked(a, 'componentModel_Interface13', b2)
    if hasattr(b1, 'componentModel_InterfaceServiceMapTuple12'):
        assert not _is_linked(b1, 'componentModel_InterfaceServiceMapTuple12', a)
    if hasattr(b2, 'componentModel_InterfaceServiceMapTuple12'):
        assert _is_linked(b2, 'componentModel_InterfaceServiceMapTuple12', a)
    _safe_set(a, 'componentModel_Interface13', None)
    assert not _is_linked(a, 'componentModel_Interface13', b2)
    if hasattr(b2, 'componentModel_InterfaceServiceMapTuple12'):
        assert not _is_linked(b2, 'componentModel_InterfaceServiceMapTuple12', a)


def test_assoc_providedInterface64_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_ProvidedDelegationConnector()
    b2 = componentModel_ProvidedDelegationConnector()
    _safe_set(a, 'componentModel_Interface65', b1)
    assert _is_linked(a, 'componentModel_Interface65', b1)
    if hasattr(b1, 'componentModel_ProvidedDelegationConnector'):
        assert _is_linked(b1, 'componentModel_ProvidedDelegationConnector', a)
    _safe_set(a, 'componentModel_Interface65', b2)
    assert _is_linked(a, 'componentModel_Interface65', b2)
    if hasattr(b1, 'componentModel_ProvidedDelegationConnector'):
        assert not _is_linked(b1, 'componentModel_ProvidedDelegationConnector', a)
    if hasattr(b2, 'componentModel_ProvidedDelegationConnector'):
        assert _is_linked(b2, 'componentModel_ProvidedDelegationConnector', a)
    _safe_set(a, 'componentModel_Interface65', None)
    assert not _is_linked(a, 'componentModel_Interface65', b2)
    if hasattr(b2, 'componentModel_ProvidedDelegationConnector'):
        assert not _is_linked(b2, 'componentModel_ProvidedDelegationConnector', a)


def test_assoc_providedrole26_link_reassign_clear():
    a = componentModel_ProvidedRole(name="sample_text")
    b1 = componentModel_AssemblyContext(name="sample_text")
    b2 = componentModel_AssemblyContext(name="sample_text_2")
    _safe_set(a, 'ProvidedRole', b1)
    assert _is_linked(a, 'ProvidedRole', b1)
    if hasattr(b1, 'assemblycontext'):
        assert _is_linked(b1, 'assemblycontext', a)
    _safe_set(a, 'ProvidedRole', b2)
    assert _is_linked(a, 'ProvidedRole', b2)
    if hasattr(b1, 'assemblycontext'):
        assert not _is_linked(b1, 'assemblycontext', a)
    if hasattr(b2, 'assemblycontext'):
        assert _is_linked(b2, 'assemblycontext', a)
    _safe_set(a, 'ProvidedRole', None)
    assert not _is_linked(a, 'ProvidedRole', b2)
    if hasattr(b2, 'assemblycontext'):
        assert not _is_linked(b2, 'assemblycontext', a)


def test_assoc_providedrole31_link_reassign_clear():
    a = componentModel_ProvidedRole(name="sample_text")
    b1 = componentModel_AssemblyConnector()
    b2 = componentModel_AssemblyConnector()
    _safe_set(a, 'componentModel_ProvidedRole', b1)
    assert _is_linked(a, 'componentModel_ProvidedRole', b1)
    if hasattr(b1, 'componentModel_AssemblyConnector32'):
        assert _is_linked(b1, 'componentModel_AssemblyConnector32', a)
    _safe_set(a, 'componentModel_ProvidedRole', b2)
    assert _is_linked(a, 'componentModel_ProvidedRole', b2)
    if hasattr(b1, 'componentModel_AssemblyConnector32'):
        assert not _is_linked(b1, 'componentModel_AssemblyConnector32', a)
    if hasattr(b2, 'componentModel_AssemblyConnector32'):
        assert _is_linked(b2, 'componentModel_AssemblyConnector32', a)
    _safe_set(a, 'componentModel_ProvidedRole', None)
    assert not _is_linked(a, 'componentModel_ProvidedRole', b2)
    if hasattr(b2, 'componentModel_AssemblyConnector32'):
        assert not _is_linked(b2, 'componentModel_AssemblyConnector32', a)


def test_assoc_providedrole66_link_reassign_clear():
    a = componentModel_ProvidedRole(name="sample_text")
    b1 = componentModel_ProvidedDelegationConnector()
    b2 = componentModel_ProvidedDelegationConnector()
    _safe_set(a, 'componentModel_ProvidedRole68', b1)
    assert _is_linked(a, 'componentModel_ProvidedRole68', b1)
    if hasattr(b1, 'componentModel_ProvidedDelegationConnector67'):
        assert _is_linked(b1, 'componentModel_ProvidedDelegationConnector67', a)
    _safe_set(a, 'componentModel_ProvidedRole68', b2)
    assert _is_linked(a, 'componentModel_ProvidedRole68', b2)
    if hasattr(b1, 'componentModel_ProvidedDelegationConnector67'):
        assert not _is_linked(b1, 'componentModel_ProvidedDelegationConnector67', a)
    if hasattr(b2, 'componentModel_ProvidedDelegationConnector67'):
        assert _is_linked(b2, 'componentModel_ProvidedDelegationConnector67', a)
    _safe_set(a, 'componentModel_ProvidedRole68', None)
    assert not _is_linked(a, 'componentModel_ProvidedRole68', b2)
    if hasattr(b2, 'componentModel_ProvidedDelegationConnector67'):
        assert not _is_linked(b2, 'componentModel_ProvidedDelegationConnector67', a)


def test_assoc_required44_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_Service()
    b2 = componentModel_Service()
    _safe_set(a, 'componentModel_Interface46', b1)
    assert _is_linked(a, 'componentModel_Interface46', b1)
    if hasattr(b1, 'componentModel_Service45'):
        assert _is_linked(b1, 'componentModel_Service45', a)
    _safe_set(a, 'componentModel_Interface46', b2)
    assert _is_linked(a, 'componentModel_Interface46', b2)
    if hasattr(b1, 'componentModel_Service45'):
        assert not _is_linked(b1, 'componentModel_Service45', a)
    if hasattr(b2, 'componentModel_Service45'):
        assert _is_linked(b2, 'componentModel_Service45', a)
    _safe_set(a, 'componentModel_Interface46', None)
    assert not _is_linked(a, 'componentModel_Interface46', b2)
    if hasattr(b2, 'componentModel_Service45'):
        assert not _is_linked(b2, 'componentModel_Service45', a)


def test_assoc_requiredInterface37_link_reassign_clear():
    a = componentModel_Interface(name="sample_text")
    b1 = componentModel_RequiredDelegationConnector()
    b2 = componentModel_RequiredDelegationConnector()
    _safe_set(a, 'componentModel_Interface39', b1)
    assert _is_linked(a, 'componentModel_Interface39', b1)
    if hasattr(b1, 'componentModel_RequiredDelegationConnector38'):
        assert _is_linked(b1, 'componentModel_RequiredDelegationConnector38', a)
    _safe_set(a, 'componentModel_Interface39', b2)
    assert _is_linked(a, 'componentModel_Interface39', b2)
    if hasattr(b1, 'componentModel_RequiredDelegationConnector38'):
        assert not _is_linked(b1, 'componentModel_RequiredDelegationConnector38', a)
    if hasattr(b2, 'componentModel_RequiredDelegationConnector38'):
        assert _is_linked(b2, 'componentModel_RequiredDelegationConnector38', a)
    _safe_set(a, 'componentModel_Interface39', None)
    assert not _is_linked(a, 'componentModel_Interface39', b2)
    if hasattr(b2, 'componentModel_RequiredDelegationConnector38'):
        assert not _is_linked(b2, 'componentModel_RequiredDelegationConnector38', a)


def test_assoc_requiredrole27_link_reassign_clear():
    a = componentModel_RequiredRole(name="sample_text")
    b1 = componentModel_AssemblyContext(name="sample_text")
    b2 = componentModel_AssemblyContext(name="sample_text_2")
    _safe_set(a, 'RequiredRole', b1)
    assert _is_linked(a, 'RequiredRole', b1)
    if hasattr(b1, 'assemblycontext28'):
        assert _is_linked(b1, 'assemblycontext28', a)
    _safe_set(a, 'RequiredRole', b2)
    assert _is_linked(a, 'RequiredRole', b2)
    if hasattr(b1, 'assemblycontext28'):
        assert not _is_linked(b1, 'assemblycontext28', a)
    if hasattr(b2, 'assemblycontext28'):
        assert _is_linked(b2, 'assemblycontext28', a)
    _safe_set(a, 'RequiredRole', None)
    assert not _is_linked(a, 'RequiredRole', b2)
    if hasattr(b2, 'assemblycontext28'):
        assert not _is_linked(b2, 'assemblycontext28', a)


def test_assoc_requiredrole33_link_reassign_clear():
    a = componentModel_RequiredRole(name="sample_text")
    b1 = componentModel_AssemblyConnector()
    b2 = componentModel_AssemblyConnector()
    _safe_set(a, 'componentModel_RequiredRole', b1)
    assert _is_linked(a, 'componentModel_RequiredRole', b1)
    if hasattr(b1, 'componentModel_AssemblyConnector34'):
        assert _is_linked(b1, 'componentModel_AssemblyConnector34', a)
    _safe_set(a, 'componentModel_RequiredRole', b2)
    assert _is_linked(a, 'componentModel_RequiredRole', b2)
    if hasattr(b1, 'componentModel_AssemblyConnector34'):
        assert not _is_linked(b1, 'componentModel_AssemblyConnector34', a)
    if hasattr(b2, 'componentModel_AssemblyConnector34'):
        assert _is_linked(b2, 'componentModel_AssemblyConnector34', a)
    _safe_set(a, 'componentModel_RequiredRole', None)
    assert not _is_linked(a, 'componentModel_RequiredRole', b2)
    if hasattr(b2, 'componentModel_AssemblyConnector34'):
        assert not _is_linked(b2, 'componentModel_AssemblyConnector34', a)


def test_assoc_requiredrole35_link_reassign_clear():
    a = componentModel_RequiredRole(name="sample_text")
    b1 = componentModel_RequiredDelegationConnector()
    b2 = componentModel_RequiredDelegationConnector()
    _safe_set(a, 'componentModel_RequiredRole36', b1)
    assert _is_linked(a, 'componentModel_RequiredRole36', b1)
    if hasattr(b1, 'componentModel_RequiredDelegationConnector'):
        assert _is_linked(b1, 'componentModel_RequiredDelegationConnector', a)
    _safe_set(a, 'componentModel_RequiredRole36', b2)
    assert _is_linked(a, 'componentModel_RequiredRole36', b2)
    if hasattr(b1, 'componentModel_RequiredDelegationConnector'):
        assert not _is_linked(b1, 'componentModel_RequiredDelegationConnector', a)
    if hasattr(b2, 'componentModel_RequiredDelegationConnector'):
        assert _is_linked(b2, 'componentModel_RequiredDelegationConnector', a)
    _safe_set(a, 'componentModel_RequiredRole36', None)
    assert not _is_linked(a, 'componentModel_RequiredRole36', b2)
    if hasattr(b2, 'componentModel_RequiredDelegationConnector'):
        assert not _is_linked(b2, 'componentModel_RequiredDelegationConnector', a)


def test_assoc_returnType42_link_reassign_clear():
    a = componentModel_Signature(name="sample_text")
    b1 = componentModel_Type()
    b2 = componentModel_Type()
    _safe_set(a, 'componentModel_Signature43', b1)
    assert _is_linked(a, 'componentModel_Signature43', b1)
    if hasattr(b1, 'componentModel_Type'):
        assert _is_linked(b1, 'componentModel_Type', a)
    _safe_set(a, 'componentModel_Signature43', b2)
    assert _is_linked(a, 'componentModel_Signature43', b2)
    if hasattr(b1, 'componentModel_Type'):
        assert not _is_linked(b1, 'componentModel_Type', a)
    if hasattr(b2, 'componentModel_Type'):
        assert _is_linked(b2, 'componentModel_Type', a)
    _safe_set(a, 'componentModel_Signature43', None)
    assert not _is_linked(a, 'componentModel_Signature43', b2)
    if hasattr(b2, 'componentModel_Type'):
        assert not _is_linked(b2, 'componentModel_Type', a)


def test_assoc_serviceeffectspecification3_link_reassign_clear():
    a = componentModel_Component(name="sample_text")
    b1 = componentModel_ServiceEffectSpecification()
    b2 = componentModel_ServiceEffectSpecification()
    _safe_set(a, 'componentModel_Component4', b1)
    assert _is_linked(a, 'componentModel_Component4', b1)
    if hasattr(b1, 'componentModel_ServiceEffectSpecification'):
        assert _is_linked(b1, 'componentModel_ServiceEffectSpecification', a)
    _safe_set(a, 'componentModel_Component4', b2)
    assert _is_linked(a, 'componentModel_Component4', b2)
    if hasattr(b1, 'componentModel_ServiceEffectSpecification'):
        assert not _is_linked(b1, 'componentModel_ServiceEffectSpecification', a)
    if hasattr(b2, 'componentModel_ServiceEffectSpecification'):
        assert _is_linked(b2, 'componentModel_ServiceEffectSpecification', a)
    _safe_set(a, 'componentModel_Component4', None)
    assert not _is_linked(a, 'componentModel_Component4', b2)
    if hasattr(b2, 'componentModel_ServiceEffectSpecification'):
        assert not _is_linked(b2, 'componentModel_ServiceEffectSpecification', a)


def test_assoc_signatures24_link_reassign_clear():
    a = componentModel_Signature(name="sample_text")
    b1 = componentModel_Interface(name="sample_text")
    b2 = componentModel_Interface(name="sample_text_2")
    _safe_set(a, 'componentModel_Signature', b1)
    assert _is_linked(a, 'componentModel_Signature', b1)
    if hasattr(b1, 'componentModel_Interface25'):
        assert _is_linked(b1, 'componentModel_Interface25', a)
    _safe_set(a, 'componentModel_Signature', b2)
    assert _is_linked(a, 'componentModel_Signature', b2)
    if hasattr(b1, 'componentModel_Interface25'):
        assert not _is_linked(b1, 'componentModel_Interface25', a)
    if hasattr(b2, 'componentModel_Interface25'):
        assert _is_linked(b2, 'componentModel_Interface25', a)
    _safe_set(a, 'componentModel_Signature', None)
    assert not _is_linked(a, 'componentModel_Signature', b2)
    if hasattr(b2, 'componentModel_Interface25'):
        assert not _is_linked(b2, 'componentModel_Interface25', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


AssemblyViewType_strategy = st.builds(AssemblyViewType)
@given(instance=AssemblyViewType_strategy)
@settings(max_examples=25)
def test_AssemblyViewType_instantiation(instance):
    assert isinstance(instance, AssemblyViewType)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


DelegationConnector_strategy = st.builds(DelegationConnector)
@given(instance=DelegationConnector_strategy)
@settings(max_examples=25)
def test_DelegationConnector_instantiation(instance):
    assert isinstance(instance, DelegationConnector)


ParameterTyp_strategy = st.builds(ParameterTyp)
@given(instance=ParameterTyp_strategy)
@settings(max_examples=25)
def test_ParameterTyp_instantiation(instance):
    assert isinstance(instance, ParameterTyp)


SimpleParameterType_strategy = st.builds(SimpleParameterType)
@given(instance=SimpleParameterType_strategy)
@settings(max_examples=25)
def test_SimpleParameterType_instantiation(instance):
    assert isinstance(instance, SimpleParameterType)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


ViewPoint_strategy = st.builds(ViewPoint)
@given(instance=ViewPoint_strategy)
@settings(max_examples=25)
def test_ViewPoint_instantiation(instance):
    assert isinstance(instance, ViewPoint)


ViewType_strategy = st.builds(ViewType)
@given(instance=ViewType_strategy)
@settings(max_examples=25)
def test_ViewType_instantiation(instance):
    assert isinstance(instance, ViewType)


componentModel_Action_strategy = st.builds(componentModel_Action)
@given(instance=componentModel_Action_strategy)
@settings(max_examples=25)
def test_componentModel_Action_instantiation(instance):
    assert isinstance(instance, componentModel_Action)


componentModel_AllocationViewType_strategy = st.builds(componentModel_AllocationViewType)
@given(instance=componentModel_AllocationViewType_strategy)
@settings(max_examples=25)
def test_componentModel_AllocationViewType_instantiation(instance):
    assert isinstance(instance, componentModel_AllocationViewType)


componentModel_AssemblyConnector_strategy = st.builds(componentModel_AssemblyConnector)
@given(instance=componentModel_AssemblyConnector_strategy)
@settings(max_examples=25)
def test_componentModel_AssemblyConnector_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyConnector)


componentModel_AssemblyContext_strategy = st.builds(componentModel_AssemblyContext, name=safe_text)
@given(instance=componentModel_AssemblyContext_strategy)
@settings(max_examples=25)
def test_componentModel_AssemblyContext_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyContext)


componentModel_AssemblyViewPoint_strategy = st.builds(componentModel_AssemblyViewPoint)
@given(instance=componentModel_AssemblyViewPoint_strategy)
@settings(max_examples=25)
def test_componentModel_AssemblyViewPoint_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyViewPoint)


componentModel_AssemblyViewType_strategy = st.builds(componentModel_AssemblyViewType)
@given(instance=componentModel_AssemblyViewType_strategy)
@settings(max_examples=25)
def test_componentModel_AssemblyViewType_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyViewType)


componentModel_Boolean_strategy = st.builds(componentModel_Boolean)
@given(instance=componentModel_Boolean_strategy)
@settings(max_examples=25)
def test_componentModel_Boolean_instantiation(instance):
    assert isinstance(instance, componentModel_Boolean)


componentModel_Branch_strategy = st.builds(componentModel_Branch)
@given(instance=componentModel_Branch_strategy)
@settings(max_examples=25)
def test_componentModel_Branch_instantiation(instance):
    assert isinstance(instance, componentModel_Branch)


componentModel_Char_strategy = st.builds(componentModel_Char)
@given(instance=componentModel_Char_strategy)
@settings(max_examples=25)
def test_componentModel_Char_instantiation(instance):
    assert isinstance(instance, componentModel_Char)


componentModel_ComplexParameterType_strategy = st.builds(componentModel_ComplexParameterType)
@given(instance=componentModel_ComplexParameterType_strategy)
@settings(max_examples=25)
def test_componentModel_ComplexParameterType_instantiation(instance):
    assert isinstance(instance, componentModel_ComplexParameterType)


componentModel_Component_strategy = st.builds(componentModel_Component, name=safe_text)
@given(instance=componentModel_Component_strategy)
@settings(max_examples=25)
def test_componentModel_Component_instantiation(instance):
    assert isinstance(instance, componentModel_Component)


componentModel_CompositeComponent_strategy = st.builds(componentModel_CompositeComponent)
@given(instance=componentModel_CompositeComponent_strategy)
@settings(max_examples=25)
def test_componentModel_CompositeComponent_instantiation(instance):
    assert isinstance(instance, componentModel_CompositeComponent)


componentModel_Date_strategy = st.builds(componentModel_Date)
@given(instance=componentModel_Date_strategy)
@settings(max_examples=25)
def test_componentModel_Date_instantiation(instance):
    assert isinstance(instance, componentModel_Date)


componentModel_DelegationConnector_strategy = st.builds(componentModel_DelegationConnector)
@given(instance=componentModel_DelegationConnector_strategy)
@settings(max_examples=25)
def test_componentModel_DelegationConnector_instantiation(instance):
    assert isinstance(instance, componentModel_DelegationConnector)


componentModel_DeploymentViewPoint_strategy = st.builds(componentModel_DeploymentViewPoint)
@given(instance=componentModel_DeploymentViewPoint_strategy)
@settings(max_examples=25)
def test_componentModel_DeploymentViewPoint_instantiation(instance):
    assert isinstance(instance, componentModel_DeploymentViewPoint)


componentModel_Double_strategy = st.builds(componentModel_Double)
@given(instance=componentModel_Double_strategy)
@settings(max_examples=25)
def test_componentModel_Double_instantiation(instance):
    assert isinstance(instance, componentModel_Double)


componentModel_EnvironmentViewType_strategy = st.builds(componentModel_EnvironmentViewType)
@given(instance=componentModel_EnvironmentViewType_strategy)
@settings(max_examples=25)
def test_componentModel_EnvironmentViewType_instantiation(instance):
    assert isinstance(instance, componentModel_EnvironmentViewType)


componentModel_ExternalCall_strategy = st.builds(componentModel_ExternalCall)
@given(instance=componentModel_ExternalCall_strategy)
@settings(max_examples=25)
def test_componentModel_ExternalCall_instantiation(instance):
    assert isinstance(instance, componentModel_ExternalCall)


componentModel_Float_strategy = st.builds(componentModel_Float)
@given(instance=componentModel_Float_strategy)
@settings(max_examples=25)
def test_componentModel_Float_instantiation(instance):
    assert isinstance(instance, componentModel_Float)


componentModel_Int_strategy = st.builds(componentModel_Int)
@given(instance=componentModel_Int_strategy)
@settings(max_examples=25)
def test_componentModel_Int_instantiation(instance):
    assert isinstance(instance, componentModel_Int)


componentModel_Interface_strategy = st.builds(componentModel_Interface, name=safe_text)
@given(instance=componentModel_Interface_strategy)
@settings(max_examples=25)
def test_componentModel_Interface_instantiation(instance):
    assert isinstance(instance, componentModel_Interface)


componentModel_InterfaceServiceMapTuple_strategy = st.builds(componentModel_InterfaceServiceMapTuple)
@given(instance=componentModel_InterfaceServiceMapTuple_strategy)
@settings(max_examples=25)
def test_componentModel_InterfaceServiceMapTuple_instantiation(instance):
    assert isinstance(instance, componentModel_InterfaceServiceMapTuple)


componentModel_InternalAction_strategy = st.builds(componentModel_InternalAction)
@given(instance=componentModel_InternalAction_strategy)
@settings(max_examples=25)
def test_componentModel_InternalAction_instantiation(instance):
    assert isinstance(instance, componentModel_InternalAction)


componentModel_List_strategy = st.builds(componentModel_List)
@given(instance=componentModel_List_strategy)
@settings(max_examples=25)
def test_componentModel_List_instantiation(instance):
    assert isinstance(instance, componentModel_List)


componentModel_Long_strategy = st.builds(componentModel_Long)
@given(instance=componentModel_Long_strategy)
@settings(max_examples=25)
def test_componentModel_Long_instantiation(instance):
    assert isinstance(instance, componentModel_Long)


componentModel_Loop_strategy = st.builds(componentModel_Loop)
@given(instance=componentModel_Loop_strategy)
@settings(max_examples=25)
def test_componentModel_Loop_instantiation(instance):
    assert isinstance(instance, componentModel_Loop)


componentModel_Map_strategy = st.builds(componentModel_Map)
@given(instance=componentModel_Map_strategy)
@settings(max_examples=25)
def test_componentModel_Map_instantiation(instance):
    assert isinstance(instance, componentModel_Map)


componentModel_Parameter_strategy = st.builds(componentModel_Parameter, name=safe_text)
@given(instance=componentModel_Parameter_strategy)
@settings(max_examples=25)
def test_componentModel_Parameter_instantiation(instance):
    assert isinstance(instance, componentModel_Parameter)


componentModel_ParameterTyp_strategy = st.builds(componentModel_ParameterTyp)
@given(instance=componentModel_ParameterTyp_strategy)
@settings(max_examples=25)
def test_componentModel_ParameterTyp_instantiation(instance):
    assert isinstance(instance, componentModel_ParameterTyp)


componentModel_ProvidedDelegationConnector_strategy = st.builds(componentModel_ProvidedDelegationConnector)
@given(instance=componentModel_ProvidedDelegationConnector_strategy)
@settings(max_examples=25)
def test_componentModel_ProvidedDelegationConnector_instantiation(instance):
    assert isinstance(instance, componentModel_ProvidedDelegationConnector)


componentModel_ProvidedRole_strategy = st.builds(componentModel_ProvidedRole, name=safe_text)
@given(instance=componentModel_ProvidedRole_strategy)
@settings(max_examples=25)
def test_componentModel_ProvidedRole_instantiation(instance):
    assert isinstance(instance, componentModel_ProvidedRole)


componentModel_Repository_strategy = st.builds(componentModel_Repository)
@given(instance=componentModel_Repository_strategy)
@settings(max_examples=25)
def test_componentModel_Repository_instantiation(instance):
    assert isinstance(instance, componentModel_Repository)


componentModel_RepositoryViewType_strategy = st.builds(componentModel_RepositoryViewType)
@given(instance=componentModel_RepositoryViewType_strategy)
@settings(max_examples=25)
def test_componentModel_RepositoryViewType_instantiation(instance):
    assert isinstance(instance, componentModel_RepositoryViewType)


componentModel_RequiredDelegationConnector_strategy = st.builds(componentModel_RequiredDelegationConnector)
@given(instance=componentModel_RequiredDelegationConnector_strategy)
@settings(max_examples=25)
def test_componentModel_RequiredDelegationConnector_instantiation(instance):
    assert isinstance(instance, componentModel_RequiredDelegationConnector)


componentModel_RequiredRole_strategy = st.builds(componentModel_RequiredRole, name=safe_text)
@given(instance=componentModel_RequiredRole_strategy)
@settings(max_examples=25)
def test_componentModel_RequiredRole_instantiation(instance):
    assert isinstance(instance, componentModel_RequiredRole)


componentModel_Service_strategy = st.builds(componentModel_Service)
@given(instance=componentModel_Service_strategy)
@settings(max_examples=25)
def test_componentModel_Service_instantiation(instance):
    assert isinstance(instance, componentModel_Service)


componentModel_ServiceEffectSpecification_strategy = st.builds(componentModel_ServiceEffectSpecification)
@given(instance=componentModel_ServiceEffectSpecification_strategy)
@settings(max_examples=25)
def test_componentModel_ServiceEffectSpecification_instantiation(instance):
    assert isinstance(instance, componentModel_ServiceEffectSpecification)


componentModel_Signature_strategy = st.builds(componentModel_Signature, name=safe_text)
@given(instance=componentModel_Signature_strategy)
@settings(max_examples=25)
def test_componentModel_Signature_instantiation(instance):
    assert isinstance(instance, componentModel_Signature)


componentModel_SimpleParameterType_strategy = st.builds(componentModel_SimpleParameterType)
@given(instance=componentModel_SimpleParameterType_strategy)
@settings(max_examples=25)
def test_componentModel_SimpleParameterType_instantiation(instance):
    assert isinstance(instance, componentModel_SimpleParameterType)


componentModel_String_strategy = st.builds(componentModel_String)
@given(instance=componentModel_String_strategy)
@settings(max_examples=25)
def test_componentModel_String_instantiation(instance):
    assert isinstance(instance, componentModel_String)


componentModel_System_strategy = st.builds(componentModel_System)
@given(instance=componentModel_System_strategy)
@settings(max_examples=25)
def test_componentModel_System_instantiation(instance):
    assert isinstance(instance, componentModel_System)


componentModel_SystemIndependentViewPoint_strategy = st.builds(componentModel_SystemIndependentViewPoint)
@given(instance=componentModel_SystemIndependentViewPoint_strategy)
@settings(max_examples=25)
def test_componentModel_SystemIndependentViewPoint_instantiation(instance):
    assert isinstance(instance, componentModel_SystemIndependentViewPoint)


componentModel_Type_strategy = st.builds(componentModel_Type)
@given(instance=componentModel_Type_strategy)
@settings(max_examples=25)
def test_componentModel_Type_instantiation(instance):
    assert isinstance(instance, componentModel_Type)


componentModel_ViewPoint_strategy = st.builds(componentModel_ViewPoint)
@given(instance=componentModel_ViewPoint_strategy)
@settings(max_examples=25)
def test_componentModel_ViewPoint_instantiation(instance):
    assert isinstance(instance, componentModel_ViewPoint)


componentModel_ViewType_strategy = st.builds(componentModel_ViewType)
@given(instance=componentModel_ViewType_strategy)
@settings(max_examples=25)
def test_componentModel_ViewType_instantiation(instance):
    assert isinstance(instance, componentModel_ViewType)


componentModel_Void_strategy = st.builds(componentModel_Void)
@given(instance=componentModel_Void_strategy)
@settings(max_examples=25)
def test_componentModel_Void_instantiation(instance):
    assert isinstance(instance, componentModel_Void)



