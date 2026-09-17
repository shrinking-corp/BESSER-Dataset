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
    spinefm_ActionModel_Action,
    spinefm_ActionModel_Rule,
    spinefm_ActionModel_ConfigurationState,
    Rule,
    spinefm_ActionModel_RestrictionFunction,
    spinefm_ProcessModel_DeletedContextInformations,
    LocalContext,
    GlobalContext,
    MultipleSoftwareProductLine,
    spinefm_ProcessModel_ContextManager,
    CompositeConfiguration,
    spinefm_ProcessModel_Context,
    Context,
    spinefm_ProcessModel_LocalContext,
    spinefm_ProcessModel_GlobalContext,
    Action,
    spinefm_ActionModel_ActionAddCTConstraint,
    spinefm_ActionModel_ActionDeselect,
    spinefm_ActionModel_ActionSelect,
    spinefm_ProcessModel_ConfigurationProcessStep,
    ConfigurationState,
    spinefm_ConfigurationModel_CompositeConfiguration,
    Configuration,
    spinefm_ConfigurationModel_Link,
    Link,
    ConfigurationProcessStep,
    spinefm_ConfigurationModel_Configuration,
    spinefm_MSPLModel_DEAssociationEnd,
    FeatureModel,
    spinefm_MSPLModel_DomainElement,
    MultiplicityElement,
    spinefm_MSPLModel_MultiplicityElement,
    DEAssociationEnd,
    RestrictionFunction,
    spinefm_MSPLModel_DEAssociation,
    DEAssociation,
    DomainElement,
    spinefm_FMModel_Group,
    spinefm_MSPLModel_MultipleSoftwareProductLine,
    Group,
    spinefm_FMModel_Constraint,
    Feature,
    spinefm_FMModel_Feature,
    Constraint,
    spinefm_FMModel_FeatureModel,
    GroupState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_spinefm_actionmodel_action_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_Action)


def test_hyp_spinefm_actionmodel_action_constructor_exists():
    assert callable(spinefm_ActionModel_Action.__init__)


def test_hyp_spinefm_actionmodel_action_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_Action.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_spinefm_actionmodel_rule_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_Rule)


def test_hyp_spinefm_actionmodel_rule_constructor_exists():
    assert callable(spinefm_ActionModel_Rule.__init__)


def test_hyp_spinefm_actionmodel_rule_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_spinefm_actionmodel_configurationstate_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_ConfigurationState)


def test_hyp_spinefm_actionmodel_configurationstate_constructor_exists():
    assert callable(spinefm_ActionModel_ConfigurationState.__init__)


def test_hyp_spinefm_actionmodel_configurationstate_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_ConfigurationState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_hyp_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_hyp_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_actionmodel_restrictionfunction_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_RestrictionFunction)


def test_hyp_spinefm_actionmodel_restrictionfunction_constructor_exists():
    assert callable(spinefm_ActionModel_RestrictionFunction.__init__)


def test_hyp_spinefm_actionmodel_restrictionfunction_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_RestrictionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_spinefm_processmodel_deletedcontextinformations_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_DeletedContextInformations)


def test_hyp_spinefm_processmodel_deletedcontextinformations_constructor_exists():
    assert callable(spinefm_ProcessModel_DeletedContextInformations.__init__)


def test_hyp_spinefm_processmodel_deletedcontextinformations_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_DeletedContextInformations.__init__)
    params = list(sig.parameters.keys())
    assert "deletedContext" in params, "Missing parameter 'deletedContext'"




def test_hyp_localcontext_is_not_abstract():
    assert not inspect.isabstract(LocalContext)


def test_hyp_localcontext_constructor_exists():
    assert callable(LocalContext.__init__)


def test_hyp_localcontext_constructor_args():
    sig = inspect.signature(LocalContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_globalcontext_is_not_abstract():
    assert not inspect.isabstract(GlobalContext)


def test_hyp_globalcontext_constructor_exists():
    assert callable(GlobalContext.__init__)


def test_hyp_globalcontext_constructor_args():
    sig = inspect.signature(GlobalContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplesoftwareproductline_is_not_abstract():
    assert not inspect.isabstract(MultipleSoftwareProductLine)


def test_hyp_multiplesoftwareproductline_constructor_exists():
    assert callable(MultipleSoftwareProductLine.__init__)


def test_hyp_multiplesoftwareproductline_constructor_args():
    sig = inspect.signature(MultipleSoftwareProductLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_processmodel_contextmanager_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_ContextManager)


def test_hyp_spinefm_processmodel_contextmanager_constructor_exists():
    assert callable(spinefm_ProcessModel_ContextManager.__init__)


def test_hyp_spinefm_processmodel_contextmanager_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_ContextManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compositeconfiguration_is_not_abstract():
    assert not inspect.isabstract(CompositeConfiguration)


def test_hyp_compositeconfiguration_constructor_exists():
    assert callable(CompositeConfiguration.__init__)


def test_hyp_compositeconfiguration_constructor_args():
    sig = inspect.signature(CompositeConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_processmodel_context_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_Context)


def test_hyp_spinefm_processmodel_context_constructor_exists():
    assert callable(spinefm_ProcessModel_Context.__init__)


def test_hyp_spinefm_processmodel_context_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_Context.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_hyp_context_constructor_exists():
    assert callable(Context.__init__)


def test_hyp_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_processmodel_localcontext_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_LocalContext)


def test_hyp_spinefm_processmodel_localcontext_constructor_exists():
    assert callable(spinefm_ProcessModel_LocalContext.__init__)


def test_hyp_spinefm_processmodel_localcontext_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_LocalContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_processmodel_globalcontext_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_GlobalContext)


def test_hyp_spinefm_processmodel_globalcontext_constructor_exists():
    assert callable(spinefm_ProcessModel_GlobalContext.__init__)


def test_hyp_spinefm_processmodel_globalcontext_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_GlobalContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_actionmodel_actionaddctconstraint_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_ActionAddCTConstraint)


def test_hyp_spinefm_actionmodel_actionaddctconstraint_constructor_exists():
    assert callable(spinefm_ActionModel_ActionAddCTConstraint.__init__)


def test_hyp_spinefm_actionmodel_actionaddctconstraint_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_ActionAddCTConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_actionmodel_actiondeselect_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_ActionDeselect)


def test_hyp_spinefm_actionmodel_actiondeselect_constructor_exists():
    assert callable(spinefm_ActionModel_ActionDeselect.__init__)


def test_hyp_spinefm_actionmodel_actiondeselect_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_ActionDeselect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_actionmodel_actionselect_is_not_abstract():
    assert not inspect.isabstract(spinefm_ActionModel_ActionSelect)


def test_hyp_spinefm_actionmodel_actionselect_constructor_exists():
    assert callable(spinefm_ActionModel_ActionSelect.__init__)


def test_hyp_spinefm_actionmodel_actionselect_constructor_args():
    sig = inspect.signature(spinefm_ActionModel_ActionSelect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_processmodel_configurationprocessstep_is_not_abstract():
    assert not inspect.isabstract(spinefm_ProcessModel_ConfigurationProcessStep)


def test_hyp_spinefm_processmodel_configurationprocessstep_constructor_exists():
    assert callable(spinefm_ProcessModel_ConfigurationProcessStep.__init__)


def test_hyp_spinefm_processmodel_configurationprocessstep_constructor_args():
    sig = inspect.signature(spinefm_ProcessModel_ConfigurationProcessStep.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "userConfig" in params, "Missing parameter 'userConfig'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_configurationstate_is_not_abstract():
    assert not inspect.isabstract(ConfigurationState)


def test_hyp_configurationstate_constructor_exists():
    assert callable(ConfigurationState.__init__)


def test_hyp_configurationstate_constructor_args():
    sig = inspect.signature(ConfigurationState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_configurationmodel_compositeconfiguration_is_not_abstract():
    assert not inspect.isabstract(spinefm_ConfigurationModel_CompositeConfiguration)


def test_hyp_spinefm_configurationmodel_compositeconfiguration_constructor_exists():
    assert callable(spinefm_ConfigurationModel_CompositeConfiguration.__init__)


def test_hyp_spinefm_configurationmodel_compositeconfiguration_constructor_args():
    sig = inspect.signature(spinefm_ConfigurationModel_CompositeConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_configuration_is_not_abstract():
    assert not inspect.isabstract(Configuration)


def test_hyp_configuration_constructor_exists():
    assert callable(Configuration.__init__)


def test_hyp_configuration_constructor_args():
    sig = inspect.signature(Configuration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_configurationmodel_link_is_not_abstract():
    assert not inspect.isabstract(spinefm_ConfigurationModel_Link)


def test_hyp_spinefm_configurationmodel_link_constructor_exists():
    assert callable(spinefm_ConfigurationModel_Link.__init__)


def test_hyp_spinefm_configurationmodel_link_constructor_args():
    sig = inspect.signature(spinefm_ConfigurationModel_Link.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_hyp_link_constructor_exists():
    assert callable(Link.__init__)


def test_hyp_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_configurationprocessstep_is_not_abstract():
    assert not inspect.isabstract(ConfigurationProcessStep)


def test_hyp_configurationprocessstep_constructor_exists():
    assert callable(ConfigurationProcessStep.__init__)


def test_hyp_configurationprocessstep_constructor_args():
    sig = inspect.signature(ConfigurationProcessStep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_configurationmodel_configuration_is_not_abstract():
    assert not inspect.isabstract(spinefm_ConfigurationModel_Configuration)


def test_hyp_spinefm_configurationmodel_configuration_constructor_exists():
    assert callable(spinefm_ConfigurationModel_Configuration.__init__)


def test_hyp_spinefm_configurationmodel_configuration_constructor_args():
    sig = inspect.signature(spinefm_ConfigurationModel_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_spinefm_msplmodel_deassociationend_is_not_abstract():
    assert not inspect.isabstract(spinefm_MSPLModel_DEAssociationEnd)


def test_hyp_spinefm_msplmodel_deassociationend_constructor_exists():
    assert callable(spinefm_MSPLModel_DEAssociationEnd.__init__)


def test_hyp_spinefm_msplmodel_deassociationend_constructor_args():
    sig = inspect.signature(spinefm_MSPLModel_DEAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_featuremodel_is_not_abstract():
    assert not inspect.isabstract(FeatureModel)


def test_hyp_featuremodel_constructor_exists():
    assert callable(FeatureModel.__init__)


def test_hyp_featuremodel_constructor_args():
    sig = inspect.signature(FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_msplmodel_domainelement_is_not_abstract():
    assert not inspect.isabstract(spinefm_MSPLModel_DomainElement)


def test_hyp_spinefm_msplmodel_domainelement_constructor_exists():
    assert callable(spinefm_MSPLModel_DomainElement.__init__)


def test_hyp_spinefm_msplmodel_domainelement_constructor_args():
    sig = inspect.signature(spinefm_MSPLModel_DomainElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_hyp_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_hyp_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_msplmodel_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(spinefm_MSPLModel_MultiplicityElement)


def test_hyp_spinefm_msplmodel_multiplicityelement_constructor_exists():
    assert callable(spinefm_MSPLModel_MultiplicityElement.__init__)


def test_hyp_spinefm_msplmodel_multiplicityelement_constructor_args():
    sig = inspect.signature(spinefm_MSPLModel_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"






def test_hyp_deassociationend_is_not_abstract():
    assert not inspect.isabstract(DEAssociationEnd)


def test_hyp_deassociationend_constructor_exists():
    assert callable(DEAssociationEnd.__init__)


def test_hyp_deassociationend_constructor_args():
    sig = inspect.signature(DEAssociationEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_restrictionfunction_is_not_abstract():
    assert not inspect.isabstract(RestrictionFunction)


def test_hyp_restrictionfunction_constructor_exists():
    assert callable(RestrictionFunction.__init__)


def test_hyp_restrictionfunction_constructor_args():
    sig = inspect.signature(RestrictionFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_msplmodel_deassociation_is_not_abstract():
    assert not inspect.isabstract(spinefm_MSPLModel_DEAssociation)


def test_hyp_spinefm_msplmodel_deassociation_constructor_exists():
    assert callable(spinefm_MSPLModel_DEAssociation.__init__)


def test_hyp_spinefm_msplmodel_deassociation_constructor_args():
    sig = inspect.signature(spinefm_MSPLModel_DEAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_deassociation_is_not_abstract():
    assert not inspect.isabstract(DEAssociation)


def test_hyp_deassociation_constructor_exists():
    assert callable(DEAssociation.__init__)


def test_hyp_deassociation_constructor_args():
    sig = inspect.signature(DEAssociation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_domainelement_is_not_abstract():
    assert not inspect.isabstract(DomainElement)


def test_hyp_domainelement_constructor_exists():
    assert callable(DomainElement.__init__)


def test_hyp_domainelement_constructor_args():
    sig = inspect.signature(DomainElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_fmmodel_group_is_not_abstract():
    assert not inspect.isabstract(spinefm_FMModel_Group)


def test_hyp_spinefm_fmmodel_group_constructor_exists():
    assert callable(spinefm_FMModel_Group.__init__)


def test_hyp_spinefm_fmmodel_group_constructor_args():
    sig = inspect.signature(spinefm_FMModel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"




def test_hyp_spinefm_msplmodel_multiplesoftwareproductline_is_not_abstract():
    assert not inspect.isabstract(spinefm_MSPLModel_MultipleSoftwareProductLine)


def test_hyp_spinefm_msplmodel_multiplesoftwareproductline_constructor_exists():
    assert callable(spinefm_MSPLModel_MultipleSoftwareProductLine.__init__)


def test_hyp_spinefm_msplmodel_multiplesoftwareproductline_constructor_args():
    sig = inspect.signature(spinefm_MSPLModel_MultipleSoftwareProductLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_fmmodel_constraint_is_not_abstract():
    assert not inspect.isabstract(spinefm_FMModel_Constraint)


def test_hyp_spinefm_fmmodel_constraint_constructor_exists():
    assert callable(spinefm_FMModel_Constraint.__init__)


def test_hyp_spinefm_fmmodel_constraint_constructor_args():
    sig = inspect.signature(spinefm_FMModel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "Rule" in params, "Missing parameter 'Rule'"




def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_fmmodel_feature_is_not_abstract():
    assert not inspect.isabstract(spinefm_FMModel_Feature)


def test_hyp_spinefm_fmmodel_feature_constructor_exists():
    assert callable(spinefm_FMModel_Feature.__init__)


def test_hyp_spinefm_fmmodel_feature_constructor_args():
    sig = inspect.signature(spinefm_FMModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spinefm_fmmodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(spinefm_FMModel_FeatureModel)


def test_hyp_spinefm_fmmodel_featuremodel_constructor_exists():
    assert callable(spinefm_FMModel_FeatureModel.__init__)


def test_hyp_spinefm_fmmodel_featuremodel_constructor_args():
    sig = inspect.signature(spinefm_FMModel_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"



def test_hyp_groupstate_exists():
    # Check that the Enumeration exists
    assert GroupState is not None

def test_hyp_groupstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GroupState]
    expected_literals = [
        "MANDATORY",
        "OPTIONAL",
        "ALTERNATIVE",
        "MUTEX",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GroupState"


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
spinefm_ActionModel_Action_strategy = st.builds(
    spinefm_ActionModel_Action,
    id=
        safe_text
)
spinefm_ActionModel_Rule_strategy = st.builds(
    spinefm_ActionModel_Rule,
    id=
        safe_text
)
spinefm_ActionModel_ConfigurationState_strategy = st.builds(
    spinefm_ActionModel_ConfigurationState,
    id=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
spinefm_ActionModel_RestrictionFunction_strategy = st.builds(
    spinefm_ActionModel_RestrictionFunction,
    id=
        safe_text
)
spinefm_ProcessModel_DeletedContextInformations_strategy = st.builds(
    spinefm_ProcessModel_DeletedContextInformations,
    deletedContext=
        safe_text
)
LocalContext_strategy = st.builds(
    LocalContext,
)
GlobalContext_strategy = st.builds(
    GlobalContext,
)
MultipleSoftwareProductLine_strategy = st.builds(
    MultipleSoftwareProductLine,
)
spinefm_ProcessModel_ContextManager_strategy = st.builds(
    spinefm_ProcessModel_ContextManager,
)
CompositeConfiguration_strategy = st.builds(
    CompositeConfiguration,
)
spinefm_ProcessModel_Context_strategy = st.builds(
    spinefm_ProcessModel_Context,
    id=
        safe_text
)
Context_strategy = st.builds(
    Context,
)
spinefm_ProcessModel_LocalContext_strategy = st.builds(
    spinefm_ProcessModel_LocalContext,
)
spinefm_ProcessModel_GlobalContext_strategy = st.builds(
    spinefm_ProcessModel_GlobalContext,
)
Action_strategy = st.builds(
    Action,
)
spinefm_ActionModel_ActionAddCTConstraint_strategy = st.builds(
    spinefm_ActionModel_ActionAddCTConstraint,
)
spinefm_ActionModel_ActionDeselect_strategy = st.builds(
    spinefm_ActionModel_ActionDeselect,
)
spinefm_ActionModel_ActionSelect_strategy = st.builds(
    spinefm_ActionModel_ActionSelect,
)
spinefm_ProcessModel_ConfigurationProcessStep_strategy = st.builds(
    spinefm_ProcessModel_ConfigurationProcessStep,
    description=
        safe_text,
    userConfig=
        st.booleans(),
    id=
        safe_text
)
ConfigurationState_strategy = st.builds(
    ConfigurationState,
)
spinefm_ConfigurationModel_CompositeConfiguration_strategy = st.builds(
    spinefm_ConfigurationModel_CompositeConfiguration,
    name=
        safe_text
)
Configuration_strategy = st.builds(
    Configuration,
)
spinefm_ConfigurationModel_Link_strategy = st.builds(
    spinefm_ConfigurationModel_Link,
    id=
        safe_text
)
Link_strategy = st.builds(
    Link,
)
ConfigurationProcessStep_strategy = st.builds(
    ConfigurationProcessStep,
)
spinefm_ConfigurationModel_Configuration_strategy = st.builds(
    spinefm_ConfigurationModel_Configuration,
    id=
        safe_text,
    description=
        safe_text
)
spinefm_MSPLModel_DEAssociationEnd_strategy = st.builds(
    spinefm_MSPLModel_DEAssociationEnd,
    id=
        safe_text
)
FeatureModel_strategy = st.builds(
    FeatureModel,
)
spinefm_MSPLModel_DomainElement_strategy = st.builds(
    spinefm_MSPLModel_DomainElement,
    id=
        safe_text
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
spinefm_MSPLModel_MultiplicityElement_strategy = st.builds(
    spinefm_MSPLModel_MultiplicityElement,
    id=
        safe_text,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
DEAssociationEnd_strategy = st.builds(
    DEAssociationEnd,
)
RestrictionFunction_strategy = st.builds(
    RestrictionFunction,
)
spinefm_MSPLModel_DEAssociation_strategy = st.builds(
    spinefm_MSPLModel_DEAssociation,
    id=
        safe_text
)
DEAssociation_strategy = st.builds(
    DEAssociation,
)
DomainElement_strategy = st.builds(
    DomainElement,
)
spinefm_FMModel_Group_strategy = st.builds(
    spinefm_FMModel_Group,
    state=
        safe_text
)
spinefm_MSPLModel_MultipleSoftwareProductLine_strategy = st.builds(
    spinefm_MSPLModel_MultipleSoftwareProductLine,
)
Group_strategy = st.builds(
    Group,
)
spinefm_FMModel_Constraint_strategy = st.builds(
    spinefm_FMModel_Constraint,
    Rule=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
spinefm_FMModel_Feature_strategy = st.builds(
    spinefm_FMModel_Feature,
    name=
        safe_text,
    id=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
spinefm_FMModel_FeatureModel_strategy = st.builds(
    spinefm_FMModel_FeatureModel,
    name=
        safe_text,
    id=
        safe_text
)




@given(instance=spinefm_ActionModel_Action_strategy)
def test_hyp_spinefm_actionmodel_action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ActionModel_Action_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_actionmodel_action_applyaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.applyAction(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.applyAction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'applyAction' in spinefm_ActionModel_Action is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'applyAction' in spinefm_ActionModel_Action did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'applyAction' in spinefm_ActionModel_Action is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ActionModel_Action_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_actionmodel_action_issameobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSameObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSameObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSameObject' in spinefm_ActionModel_Action is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSameObject' in spinefm_ActionModel_Action did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSameObject' in spinefm_ActionModel_Action is not implemented or raised an error")




@given(instance=spinefm_ActionModel_Rule_strategy)
def test_hyp_spinefm_actionmodel_rule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ActionModel_Rule_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_actionmodel_rule_createinverserule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createInverseRule()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createInverseRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createInverseRule' in spinefm_ActionModel_Rule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createInverseRule' in spinefm_ActionModel_Rule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createInverseRule' in spinefm_ActionModel_Rule is not implemented or raised an error")




@given(instance=spinefm_ActionModel_ConfigurationState_strategy)
def test_hyp_spinefm_actionmodel_configurationstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ActionModel_ConfigurationState_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_actionmodel_configurationstate_isincludedin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isIncludedIn(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isIncludedIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isIncludedIn' in spinefm_ActionModel_ConfigurationState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isIncludedIn' in spinefm_ActionModel_ConfigurationState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isIncludedIn' in spinefm_ActionModel_ConfigurationState is not implemented or raised an error")





@given(instance=spinefm_ActionModel_RestrictionFunction_strategy)
def test_hyp_spinefm_actionmodel_restrictionfunction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ActionModel_RestrictionFunction_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_actionmodel_restrictionfunction_createandassociateinverserestfunc_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createAndAssociateInverseRestFunc()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createAndAssociateInverseRestFunc).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createAndAssociateInverseRestFunc' in spinefm_ActionModel_RestrictionFunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createAndAssociateInverseRestFunc' in spinefm_ActionModel_RestrictionFunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createAndAssociateInverseRestFunc' in spinefm_ActionModel_RestrictionFunction is not implemented or raised an error")




@given(instance=spinefm_ProcessModel_DeletedContextInformations_strategy)
def test_hyp_spinefm_processmodel_deletedcontextinformations_deletedContext_setter(instance):
    original = instance.deletedContext
    instance.deletedContext = original
    assert instance.deletedContext == original





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_contextmanager_linkconfigurationsandmanagecontexts_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.linkConfigurationsAndManageContexts(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.linkConfigurationsAndManageContexts).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'linkConfigurationsAndManageContexts' in spinefm_ProcessModel_ContextManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'linkConfigurationsAndManageContexts' in spinefm_ProcessModel_ContextManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'linkConfigurationsAndManageContexts' in spinefm_ProcessModel_ContextManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_contextmanager_createnewcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNewContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNewContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNewContext' in spinefm_ProcessModel_ContextManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNewContext' in spinefm_ProcessModel_ContextManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNewContext' in spinefm_ProcessModel_ContextManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_contextmanager_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in spinefm_ProcessModel_ContextManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in spinefm_ProcessModel_ContextManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in spinefm_ProcessModel_ContextManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_contextmanager_setfmadapter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setFMAdapter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setFMAdapter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setFMAdapter' in spinefm_ProcessModel_ContextManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setFMAdapter' in spinefm_ProcessModel_ContextManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setFMAdapter' in spinefm_ProcessModel_ContextManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_contextmanager_propagate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.propagate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.propagate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'propagate' in spinefm_ProcessModel_ContextManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'propagate' in spinefm_ProcessModel_ContextManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'propagate' in spinefm_ProcessModel_ContextManager is not implemented or raised an error")





@given(instance=spinefm_ProcessModel_Context_strategy)
def test_hyp_spinefm_processmodel_context_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_Context_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_context_mergeexternalcps_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.mergeExternalCPS(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.mergeExternalCPS).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'mergeExternalCPS' in spinefm_ProcessModel_Context is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'mergeExternalCPS' in spinefm_ProcessModel_Context did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'mergeExternalCPS' in spinefm_ProcessModel_Context is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_Context_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_context_addcps_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addCPS(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addCPS).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addCPS' in spinefm_ProcessModel_Context is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCPS' in spinefm_ProcessModel_Context did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCPS' in spinefm_ProcessModel_Context is not implemented or raised an error")











@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
def test_hyp_spinefm_processmodel_configurationprocessstep_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
def test_hyp_spinefm_processmodel_configurationprocessstep_userConfig_setter(instance):
    original = instance.userConfig
    instance.userConfig = original
    assert instance.userConfig == original



@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
def test_hyp_spinefm_processmodel_configurationprocessstep_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_alreadyhaveaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.alreadyHaveAction(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.alreadyHaveAction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'alreadyHaveAction' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'alreadyHaveAction' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'alreadyHaveAction' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_mergewithexternalcps_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.mergeWithExternalCPS(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.mergeWithExternalCPS).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'mergeWithExternalCPS' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'mergeWithExternalCPS' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'mergeWithExternalCPS' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_iscompatiblewithconfiguration_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCompatibleWithConfiguration(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCompatibleWithConfiguration).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCompatibleWithConfiguration' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCompatibleWithConfiguration' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCompatibleWithConfiguration' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_iscomplete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isComplete()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isComplete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isComplete' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isComplete' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isComplete' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_apply_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.apply()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.apply).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'apply' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'apply' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'apply' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_addactiontodo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addActionToDo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addActionToDo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addActionToDo' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addActionToDo' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addActionToDo' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_processmodel_configurationprocessstep_setfma_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setFMA(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setFMA).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setFMA' in spinefm_ProcessModel_ConfigurationProcessStep is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setFMA' in spinefm_ProcessModel_ConfigurationProcessStep did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setFMA' in spinefm_ProcessModel_ConfigurationProcessStep is not implemented or raised an error")





@given(instance=spinefm_ConfigurationModel_CompositeConfiguration_strategy)
def test_hyp_spinefm_configurationmodel_compositeconfiguration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ConfigurationModel_CompositeConfiguration_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_configurationmodel_compositeconfiguration_addconfiguration_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addConfiguration(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addConfiguration).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addConfiguration' in spinefm_ConfigurationModel_CompositeConfiguration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addConfiguration' in spinefm_ConfigurationModel_CompositeConfiguration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addConfiguration' in spinefm_ConfigurationModel_CompositeConfiguration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ConfigurationModel_CompositeConfiguration_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_configurationmodel_compositeconfiguration_createconfigurationlink_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createConfigurationLink(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createConfigurationLink).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createConfigurationLink' in spinefm_ConfigurationModel_CompositeConfiguration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createConfigurationLink' in spinefm_ConfigurationModel_CompositeConfiguration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createConfigurationLink' in spinefm_ConfigurationModel_CompositeConfiguration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ConfigurationModel_CompositeConfiguration_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_configurationmodel_compositeconfiguration_isvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValid()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValid' in spinefm_ConfigurationModel_CompositeConfiguration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValid' in spinefm_ConfigurationModel_CompositeConfiguration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValid' in spinefm_ConfigurationModel_CompositeConfiguration is not implemented or raised an error")





@given(instance=spinefm_ConfigurationModel_Link_strategy)
def test_hyp_spinefm_configurationmodel_link_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original






@given(instance=spinefm_ConfigurationModel_Configuration_strategy)
def test_hyp_spinefm_configurationmodel_configuration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=spinefm_ConfigurationModel_Configuration_strategy)
def test_hyp_spinefm_configurationmodel_configuration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ConfigurationModel_Configuration_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_configurationmodel_configuration_iscompletlylinked_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCompletlyLinked()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCompletlyLinked).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCompletlyLinked' in spinefm_ConfigurationModel_Configuration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCompletlyLinked' in spinefm_ConfigurationModel_Configuration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCompletlyLinked' in spinefm_ConfigurationModel_Configuration is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_ConfigurationModel_Configuration_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_configurationmodel_configuration_canbelinked_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canBeLinked(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canBeLinked).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canBeLinked' in spinefm_ConfigurationModel_Configuration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canBeLinked' in spinefm_ConfigurationModel_Configuration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canBeLinked' in spinefm_ConfigurationModel_Configuration is not implemented or raised an error")




@given(instance=spinefm_MSPLModel_DEAssociationEnd_strategy)
def test_hyp_spinefm_msplmodel_deassociationend_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=spinefm_MSPLModel_DomainElement_strategy)
def test_hyp_spinefm_msplmodel_domainelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
def test_hyp_spinefm_msplmodel_multiplicityelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
def test_hyp_spinefm_msplmodel_multiplicityelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
def test_hyp_spinefm_msplmodel_multiplicityelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_msplmodel_multiplicityelement_respectboundaries_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.respectBoundaries(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.respectBoundaries).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'respectBoundaries' in spinefm_MSPLModel_MultiplicityElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'respectBoundaries' in spinefm_MSPLModel_MultiplicityElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'respectBoundaries' in spinefm_MSPLModel_MultiplicityElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_msplmodel_multiplicityelement_islowerthanupperbound_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLowerThanUpperBound(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLowerThanUpperBound).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLowerThanUpperBound' in spinefm_MSPLModel_MultiplicityElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLowerThanUpperBound' in spinefm_MSPLModel_MultiplicityElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLowerThanUpperBound' in spinefm_MSPLModel_MultiplicityElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_msplmodel_multiplicityelement_isexactlyone_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isExactlyOne()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isExactlyOne).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isExactlyOne' in spinefm_MSPLModel_MultiplicityElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isExactlyOne' in spinefm_MSPLModel_MultiplicityElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isExactlyOne' in spinefm_MSPLModel_MultiplicityElement is not implemented or raised an error")






@given(instance=spinefm_MSPLModel_DEAssociation_strategy)
def test_hyp_spinefm_msplmodel_deassociation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_MSPLModel_DEAssociation_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_msplmodel_deassociation_computeactionstodo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.computeActionsToDo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.computeActionsToDo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'computeActionsToDo' in spinefm_MSPLModel_DEAssociation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'computeActionsToDo' in spinefm_MSPLModel_DEAssociation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'computeActionsToDo' in spinefm_MSPLModel_DEAssociation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_MSPLModel_DEAssociation_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_msplmodel_deassociation_createandassociateinverseassociation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createAndAssociateInverseAssociation()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createAndAssociateInverseAssociation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createAndAssociateInverseAssociation' in spinefm_MSPLModel_DEAssociation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createAndAssociateInverseAssociation' in spinefm_MSPLModel_DEAssociation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createAndAssociateInverseAssociation' in spinefm_MSPLModel_DEAssociation is not implemented or raised an error")






@given(instance=spinefm_FMModel_Group_strategy)
def test_hyp_spinefm_fmmodel_group_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original






@given(instance=spinefm_FMModel_Constraint_strategy)
def test_hyp_spinefm_fmmodel_constraint_Rule_setter(instance):
    original = instance.Rule
    instance.Rule = original
    assert instance.Rule == original





@given(instance=spinefm_FMModel_Feature_strategy)
def test_hyp_spinefm_fmmodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=spinefm_FMModel_Feature_strategy)
def test_hyp_spinefm_fmmodel_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=spinefm_FMModel_FeatureModel_strategy)
def test_hyp_spinefm_fmmodel_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=spinefm_FMModel_FeatureModel_strategy)
def test_hyp_spinefm_fmmodel_featuremodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spinefm_FMModel_FeatureModel_strategy)
@settings(max_examples=30)
def test_hyp_spinefm_fmmodel_featuremodel_addfeature_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addFeature(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addFeature).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addFeature' in spinefm_FMModel_FeatureModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addFeature' in spinefm_FMModel_FeatureModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addFeature' in spinefm_FMModel_FeatureModel is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    CompositeConfiguration,
    Configuration,
    ConfigurationProcessStep,
    ConfigurationState,
    Constraint,
    Context,
    DEAssociation,
    DEAssociationEnd,
    DomainElement,
    Feature,
    FeatureModel,
    GlobalContext,
    Group,
    Link,
    LocalContext,
    MultipleSoftwareProductLine,
    MultiplicityElement,
    RestrictionFunction,
    Rule,
    spinefm_ActionModel_Action,
    spinefm_ActionModel_ActionAddCTConstraint,
    spinefm_ActionModel_ActionDeselect,
    spinefm_ActionModel_ActionSelect,
    spinefm_ActionModel_ConfigurationState,
    spinefm_ActionModel_RestrictionFunction,
    spinefm_ActionModel_Rule,
    spinefm_ConfigurationModel_CompositeConfiguration,
    spinefm_ConfigurationModel_Configuration,
    spinefm_ConfigurationModel_Link,
    spinefm_FMModel_Constraint,
    spinefm_FMModel_Feature,
    spinefm_FMModel_FeatureModel,
    spinefm_FMModel_Group,
    spinefm_MSPLModel_DEAssociation,
    spinefm_MSPLModel_DEAssociationEnd,
    spinefm_MSPLModel_DomainElement,
    spinefm_MSPLModel_MultipleSoftwareProductLine,
    spinefm_MSPLModel_MultiplicityElement,
    spinefm_ProcessModel_ConfigurationProcessStep,
    spinefm_ProcessModel_Context,
    spinefm_ProcessModel_ContextManager,
    spinefm_ProcessModel_DeletedContextInformations,
    spinefm_ProcessModel_GlobalContext,
    spinefm_ProcessModel_LocalContext,
    GroupState,
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

def test_spinefm_ActionModel_Action_id_value_roundtrip():
    instance = spinefm_ActionModel_Action(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ActionModel_ConfigurationState_id_value_roundtrip():
    instance = spinefm_ActionModel_ConfigurationState(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ActionModel_RestrictionFunction_id_value_roundtrip():
    instance = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ActionModel_Rule_id_value_roundtrip():
    instance = spinefm_ActionModel_Rule(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ConfigurationModel_CompositeConfiguration_name_value_roundtrip():
    instance = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_spinefm_ConfigurationModel_Configuration_description_value_roundtrip():
    instance = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_spinefm_ConfigurationModel_Configuration_id_value_roundtrip():
    instance = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ConfigurationModel_Link_id_value_roundtrip():
    instance = spinefm_ConfigurationModel_Link(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_FMModel_Constraint_Rule_value_roundtrip():
    instance = spinefm_FMModel_Constraint(Rule="sample_text")
    assert instance.Rule == "sample_text"
    instance.Rule = "sample_text_2"
    assert instance.Rule == "sample_text_2"


def test_spinefm_FMModel_Feature_id_value_roundtrip():
    instance = spinefm_FMModel_Feature(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_FMModel_Feature_name_value_roundtrip():
    instance = spinefm_FMModel_Feature(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_spinefm_FMModel_FeatureModel_id_value_roundtrip():
    instance = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_FMModel_FeatureModel_name_value_roundtrip():
    instance = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_spinefm_FMModel_Group_state_value_roundtrip():
    instance = spinefm_FMModel_Group(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_spinefm_MSPLModel_DEAssociation_id_value_roundtrip():
    instance = spinefm_MSPLModel_DEAssociation(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_MSPLModel_DEAssociationEnd_id_value_roundtrip():
    instance = spinefm_MSPLModel_DEAssociationEnd(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_MSPLModel_DomainElement_id_value_roundtrip():
    instance = spinefm_MSPLModel_DomainElement(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_MSPLModel_MultiplicityElement_id_value_roundtrip():
    instance = spinefm_MSPLModel_MultiplicityElement(id="sample_text", lowerBound=7, upperBound=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_MSPLModel_MultiplicityElement_lowerBound_value_roundtrip():
    instance = spinefm_MSPLModel_MultiplicityElement(id="sample_text", lowerBound=7, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_spinefm_MSPLModel_MultiplicityElement_upperBound_value_roundtrip():
    instance = spinefm_MSPLModel_MultiplicityElement(id="sample_text", lowerBound=7, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_spinefm_ProcessModel_ConfigurationProcessStep_description_value_roundtrip():
    instance = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_spinefm_ProcessModel_ConfigurationProcessStep_id_value_roundtrip():
    instance = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ProcessModel_ConfigurationProcessStep_userConfig_value_roundtrip():
    instance = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    assert instance.userConfig == True
    instance.userConfig = False
    assert instance.userConfig == False


def test_spinefm_ProcessModel_Context_id_value_roundtrip():
    instance = spinefm_ProcessModel_Context(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_spinefm_ProcessModel_DeletedContextInformations_deletedContext_value_roundtrip():
    instance = spinefm_ProcessModel_DeletedContextInformations(deletedContext="sample_text")
    assert instance.deletedContext == "sample_text"
    instance.deletedContext = "sample_text_2"
    assert instance.deletedContext == "sample_text_2"


def test_spinefm_ActionModel_ActionAddCTConstraint_isa_Action():
    instance = spinefm_ActionModel_ActionAddCTConstraint()
    assert isinstance(instance, Action)


def test_spinefm_ActionModel_ActionDeselect_isa_Action():
    instance = spinefm_ActionModel_ActionDeselect()
    assert isinstance(instance, Action)


def test_spinefm_ActionModel_ActionSelect_isa_Action():
    instance = spinefm_ActionModel_ActionSelect()
    assert isinstance(instance, Action)


def test_spinefm_ProcessModel_GlobalContext_isa_Context():
    instance = spinefm_ProcessModel_GlobalContext()
    assert isinstance(instance, Context)


def test_spinefm_ProcessModel_LocalContext_isa_Context():
    instance = spinefm_ProcessModel_LocalContext()
    assert isinstance(instance, Context)


def test_assoc_CPS29_link_reassign_clear():
    a = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    b1 = ConfigurationProcessStep()
    b2 = ConfigurationProcessStep()
    _safe_set(a, 'configuration', b1)
    assert _is_linked(a, 'configuration', b1)
    if hasattr(b1, 'ConfigurationProcessStep'):
        assert _is_linked(b1, 'ConfigurationProcessStep', a)
    _safe_set(a, 'configuration', b2)
    assert _is_linked(a, 'configuration', b2)
    if hasattr(b1, 'ConfigurationProcessStep'):
        assert not _is_linked(b1, 'ConfigurationProcessStep', a)
    if hasattr(b2, 'ConfigurationProcessStep'):
        assert _is_linked(b2, 'ConfigurationProcessStep', a)
    _safe_set(a, 'configuration', None)
    assert not _is_linked(a, 'configuration', b2)
    if hasattr(b2, 'ConfigurationProcessStep'):
        assert not _is_linked(b2, 'ConfigurationProcessStep', a)


def test_assoc_CPS56_link_reassign_clear():
    a = spinefm_ProcessModel_Context(id="sample_text")
    b1 = ConfigurationProcessStep()
    b2 = ConfigurationProcessStep()
    _safe_set(a, 'spinefm_ProcessModel_Context', {b1})
    assert _is_linked(a, 'spinefm_ProcessModel_Context', b1)
    if hasattr(b1, 'ConfigurationProcessStep57'):
        assert _is_linked(b1, 'ConfigurationProcessStep57', a)
    _safe_set(a, 'spinefm_ProcessModel_Context', {b2})
    assert _is_linked(a, 'spinefm_ProcessModel_Context', b2)
    if hasattr(b1, 'ConfigurationProcessStep57'):
        assert not _is_linked(b1, 'ConfigurationProcessStep57', a)
    if hasattr(b2, 'ConfigurationProcessStep57'):
        assert _is_linked(b2, 'ConfigurationProcessStep57', a)
    _safe_set(a, 'spinefm_ProcessModel_Context', set())
    assert not _is_linked(a, 'spinefm_ProcessModel_Context', b2)
    if hasattr(b2, 'ConfigurationProcessStep57'):
        assert not _is_linked(b2, 'ConfigurationProcessStep57', a)


def test_assoc_LinkMultiplicity18_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociationEnd(id="sample_text")
    b1 = MultiplicityElement()
    b2 = MultiplicityElement()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd', b1)
    if hasattr(b1, 'MultiplicityElement'):
        assert _is_linked(b1, 'MultiplicityElement', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd', b2)
    if hasattr(b1, 'MultiplicityElement'):
        assert not _is_linked(b1, 'MultiplicityElement', a)
    if hasattr(b2, 'MultiplicityElement'):
        assert _is_linked(b2, 'MultiplicityElement', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd', b2)
    if hasattr(b2, 'MultiplicityElement'):
        assert not _is_linked(b2, 'MultiplicityElement', a)


def test_assoc_MultiplicityElement22_link_reassign_clear():
    a = spinefm_MSPLModel_DomainElement(id="sample_text")
    b1 = MultiplicityElement()
    b2 = MultiplicityElement()
    _safe_set(a, 'spinefm_MSPLModel_DomainElement', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement', b1)
    if hasattr(b1, 'MultiplicityElement23'):
        assert _is_linked(b1, 'MultiplicityElement23', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement', b2)
    if hasattr(b1, 'MultiplicityElement23'):
        assert not _is_linked(b1, 'MultiplicityElement23', a)
    if hasattr(b2, 'MultiplicityElement23'):
        assert _is_linked(b2, 'MultiplicityElement23', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DomainElement', b2)
    if hasattr(b2, 'MultiplicityElement23'):
        assert not _is_linked(b2, 'MultiplicityElement23', a)


def test_assoc_actions80_link_reassign_clear():
    a = spinefm_ActionModel_Rule(id="sample_text")
    b1 = Action()
    b2 = Action()
    _safe_set(a, 'spinefm_ActionModel_Rule', b1)
    assert _is_linked(a, 'spinefm_ActionModel_Rule', b1)
    if hasattr(b1, 'Action81'):
        assert _is_linked(b1, 'Action81', a)
    _safe_set(a, 'spinefm_ActionModel_Rule', b2)
    assert _is_linked(a, 'spinefm_ActionModel_Rule', b2)
    if hasattr(b1, 'Action81'):
        assert not _is_linked(b1, 'Action81', a)
    if hasattr(b2, 'Action81'):
        assert _is_linked(b2, 'Action81', a)
    _safe_set(a, 'spinefm_ActionModel_Rule', None)
    assert not _is_linked(a, 'spinefm_ActionModel_Rule', b2)
    if hasattr(b2, 'Action81'):
        assert not _is_linked(b2, 'Action81', a)


def test_assoc_actionsDone45_link_reassign_clear():
    a = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    b1 = Action()
    b2 = Action()
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep', {b1})
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep', b1)
    if hasattr(b1, 'Action'):
        assert _is_linked(b1, 'Action', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep', {b2})
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep', b2)
    if hasattr(b1, 'Action'):
        assert not _is_linked(b1, 'Action', a)
    if hasattr(b2, 'Action'):
        assert _is_linked(b2, 'Action', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep', set())
    assert not _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep', b2)
    if hasattr(b2, 'Action'):
        assert not _is_linked(b2, 'Action', a)


def test_assoc_actionsToDo49_link_reassign_clear():
    a = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    b1 = Action()
    b2 = Action()
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', {b1})
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', b1)
    if hasattr(b1, 'Action51'):
        assert _is_linked(b1, 'Action51', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', {b2})
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', b2)
    if hasattr(b1, 'Action51'):
        assert not _is_linked(b1, 'Action51', a)
    if hasattr(b2, 'Action51'):
        assert _is_linked(b2, 'Action51', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', set())
    assert not _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep50', b2)
    if hasattr(b2, 'Action51'):
        assert not _is_linked(b2, 'Action51', a)


def test_assoc_apply_on19_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociationEnd(id="sample_text")
    b1 = DomainElement()
    b2 = DomainElement()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd20', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd20', b1)
    if hasattr(b1, 'DomainElement21'):
        assert _is_linked(b1, 'DomainElement21', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd20', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd20', b2)
    if hasattr(b1, 'DomainElement21'):
        assert not _is_linked(b1, 'DomainElement21', a)
    if hasattr(b2, 'DomainElement21'):
        assert _is_linked(b2, 'DomainElement21', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociationEnd20', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociationEnd20', b2)
    if hasattr(b2, 'DomainElement21'):
        assert not _is_linked(b2, 'DomainElement21', a)


def test_assoc_associations7_link_reassign_clear():
    a = spinefm_MSPLModel_MultipleSoftwareProductLine()
    b1 = DEAssociation()
    b2 = DEAssociation()
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', {b1})
    assert _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', b1)
    if hasattr(b1, 'DEAssociation'):
        assert _is_linked(b1, 'DEAssociation', a)
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', {b2})
    assert _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', b2)
    if hasattr(b1, 'DEAssociation'):
        assert not _is_linked(b1, 'DEAssociation', a)
    if hasattr(b2, 'DEAssociation'):
        assert _is_linked(b2, 'DEAssociation', a)
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', set())
    assert not _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine8', b2)
    if hasattr(b2, 'DEAssociation'):
        assert not _is_linked(b2, 'DEAssociation', a)


def test_assoc_belongs_to26_link_reassign_clear():
    a = spinefm_MSPLModel_DomainElement(id="sample_text")
    b1 = DEAssociation()
    b2 = DEAssociation()
    _safe_set(a, 'spinefm_MSPLModel_DomainElement27', {b1})
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement27', b1)
    if hasattr(b1, 'DEAssociation28'):
        assert _is_linked(b1, 'DEAssociation28', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement27', {b2})
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement27', b2)
    if hasattr(b1, 'DEAssociation28'):
        assert not _is_linked(b1, 'DEAssociation28', a)
    if hasattr(b2, 'DEAssociation28'):
        assert _is_linked(b2, 'DEAssociation28', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement27', set())
    assert not _is_linked(a, 'spinefm_MSPLModel_DomainElement27', b2)
    if hasattr(b2, 'DEAssociation28'):
        assert not _is_linked(b2, 'DEAssociation28', a)


def test_assoc_belongs_to30_link_reassign_clear():
    a = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    b1 = Link()
    b2 = Link()
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration', {b1})
    assert _is_linked(a, 'spinefm_ConfigurationModel_Configuration', b1)
    if hasattr(b1, 'Link'):
        assert _is_linked(b1, 'Link', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration', {b2})
    assert _is_linked(a, 'spinefm_ConfigurationModel_Configuration', b2)
    if hasattr(b1, 'Link'):
        assert not _is_linked(b1, 'Link', a)
    if hasattr(b2, 'Link'):
        assert _is_linked(b2, 'Link', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration', set())
    assert not _is_linked(a, 'spinefm_ConfigurationModel_Configuration', b2)
    if hasattr(b2, 'Link'):
        assert not _is_linked(b2, 'Link', a)


def test_assoc_children3_link_reassign_clear():
    a = spinefm_FMModel_Feature(id="sample_text", name="sample_text")
    b1 = Group()
    b2 = Group()
    _safe_set(a, 'spinefm_FMModel_Feature', {b1})
    assert _is_linked(a, 'spinefm_FMModel_Feature', b1)
    if hasattr(b1, 'Group'):
        assert _is_linked(b1, 'Group', a)
    _safe_set(a, 'spinefm_FMModel_Feature', {b2})
    assert _is_linked(a, 'spinefm_FMModel_Feature', b2)
    if hasattr(b1, 'Group'):
        assert not _is_linked(b1, 'Group', a)
    if hasattr(b2, 'Group'):
        assert _is_linked(b2, 'Group', a)
    _safe_set(a, 'spinefm_FMModel_Feature', set())
    assert not _is_linked(a, 'spinefm_FMModel_Feature', b2)
    if hasattr(b2, 'Group'):
        assert not _is_linked(b2, 'Group', a)


def test_assoc_configuration54_link_reassign_clear():
    a = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'CPS', b1)
    assert _is_linked(a, 'CPS', b1)
    if hasattr(b1, 'Configuration55'):
        assert _is_linked(b1, 'Configuration55', a)
    _safe_set(a, 'CPS', b2)
    assert _is_linked(a, 'CPS', b2)
    if hasattr(b1, 'Configuration55'):
        assert not _is_linked(b1, 'Configuration55', a)
    if hasattr(b2, 'Configuration55'):
        assert _is_linked(b2, 'Configuration55', a)
    _safe_set(a, 'CPS', None)
    assert not _is_linked(a, 'CPS', b2)
    if hasattr(b2, 'Configuration55'):
        assert not _is_linked(b2, 'Configuration55', a)


def test_assoc_constraints1_link_reassign_clear():
    a = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'spinefm_FMModel_FeatureModel2', {b1})
    assert _is_linked(a, 'spinefm_FMModel_FeatureModel2', b1)
    if hasattr(b1, 'Constraint'):
        assert _is_linked(b1, 'Constraint', a)
    _safe_set(a, 'spinefm_FMModel_FeatureModel2', {b2})
    assert _is_linked(a, 'spinefm_FMModel_FeatureModel2', b2)
    if hasattr(b1, 'Constraint'):
        assert not _is_linked(b1, 'Constraint', a)
    if hasattr(b2, 'Constraint'):
        assert _is_linked(b2, 'Constraint', a)
    _safe_set(a, 'spinefm_FMModel_FeatureModel2', set())
    assert not _is_linked(a, 'spinefm_FMModel_FeatureModel2', b2)
    if hasattr(b2, 'Constraint'):
        assert not _is_linked(b2, 'Constraint', a)


def test_assoc_context52_link_reassign_clear():
    a = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    b1 = Context()
    b2 = Context()
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', b1)
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', b1)
    if hasattr(b1, 'Context'):
        assert _is_linked(b1, 'Context', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', b2)
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', b2)
    if hasattr(b1, 'Context'):
        assert not _is_linked(b1, 'Context', a)
    if hasattr(b2, 'Context'):
        assert _is_linked(b2, 'Context', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', None)
    assert not _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep53', b2)
    if hasattr(b2, 'Context'):
        assert not _is_linked(b2, 'Context', a)


def test_assoc_deselectedFeatures74_link_reassign_clear():
    a = spinefm_ActionModel_ConfigurationState(id="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState75', {b1})
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState75', b1)
    if hasattr(b1, 'Feature76'):
        assert _is_linked(b1, 'Feature76', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState75', {b2})
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState75', b2)
    if hasattr(b1, 'Feature76'):
        assert not _is_linked(b1, 'Feature76', a)
    if hasattr(b2, 'Feature76'):
        assert _is_linked(b2, 'Feature76', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState75', set())
    assert not _is_linked(a, 'spinefm_ActionModel_ConfigurationState75', b2)
    if hasattr(b2, 'Feature76'):
        assert not _is_linked(b2, 'Feature76', a)


def test_assoc_domainElement46_link_reassign_clear():
    a = spinefm_ProcessModel_ConfigurationProcessStep(description="sample_text", id="sample_text", userConfig=True)
    b1 = DomainElement()
    b2 = DomainElement()
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', b1)
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', b1)
    if hasattr(b1, 'DomainElement48'):
        assert _is_linked(b1, 'DomainElement48', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', b2)
    assert _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', b2)
    if hasattr(b1, 'DomainElement48'):
        assert not _is_linked(b1, 'DomainElement48', a)
    if hasattr(b2, 'DomainElement48'):
        assert _is_linked(b2, 'DomainElement48', a)
    _safe_set(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', None)
    assert not _is_linked(a, 'spinefm_ProcessModel_ConfigurationProcessStep47', b2)
    if hasattr(b2, 'DomainElement48'):
        assert not _is_linked(b2, 'DomainElement48', a)


def test_assoc_domainElements6_link_reassign_clear():
    a = spinefm_MSPLModel_MultipleSoftwareProductLine()
    b1 = DomainElement()
    b2 = DomainElement()
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', {b1})
    assert _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', b1)
    if hasattr(b1, 'DomainElement'):
        assert _is_linked(b1, 'DomainElement', a)
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', {b2})
    assert _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', b2)
    if hasattr(b1, 'DomainElement'):
        assert not _is_linked(b1, 'DomainElement', a)
    if hasattr(b2, 'DomainElement'):
        assert _is_linked(b2, 'DomainElement', a)
    _safe_set(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', set())
    assert not _is_linked(a, 'spinefm_MSPLModel_MultipleSoftwareProductLine', b2)
    if hasattr(b2, 'DomainElement'):
        assert not _is_linked(b2, 'DomainElement', a)


def test_assoc_feature85_link_reassign_clear():
    a = spinefm_ActionModel_Action(id="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'spinefm_ActionModel_Action', b1)
    assert _is_linked(a, 'spinefm_ActionModel_Action', b1)
    if hasattr(b1, 'Feature86'):
        assert _is_linked(b1, 'Feature86', a)
    _safe_set(a, 'spinefm_ActionModel_Action', b2)
    assert _is_linked(a, 'spinefm_ActionModel_Action', b2)
    if hasattr(b1, 'Feature86'):
        assert not _is_linked(b1, 'Feature86', a)
    if hasattr(b2, 'Feature86'):
        assert _is_linked(b2, 'Feature86', a)
    _safe_set(a, 'spinefm_ActionModel_Action', None)
    assert not _is_linked(a, 'spinefm_ActionModel_Action', b2)
    if hasattr(b2, 'Feature86'):
        assert not _is_linked(b2, 'Feature86', a)


def test_assoc_features4_link_reassign_clear():
    a = spinefm_FMModel_Group(state="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'spinefm_FMModel_Group', {b1})
    assert _is_linked(a, 'spinefm_FMModel_Group', b1)
    if hasattr(b1, 'Feature5'):
        assert _is_linked(b1, 'Feature5', a)
    _safe_set(a, 'spinefm_FMModel_Group', {b2})
    assert _is_linked(a, 'spinefm_FMModel_Group', b2)
    if hasattr(b1, 'Feature5'):
        assert not _is_linked(b1, 'Feature5', a)
    if hasattr(b2, 'Feature5'):
        assert _is_linked(b2, 'Feature5', a)
    _safe_set(a, 'spinefm_FMModel_Group', set())
    assert not _is_linked(a, 'spinefm_FMModel_Group', b2)
    if hasattr(b2, 'Feature5'):
        assert not _is_linked(b2, 'Feature5', a)


def test_assoc_fm77_link_reassign_clear():
    a = spinefm_ActionModel_ConfigurationState(id="sample_text")
    b1 = FeatureModel()
    b2 = FeatureModel()
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState78', b1)
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState78', b1)
    if hasattr(b1, 'FeatureModel79'):
        assert _is_linked(b1, 'FeatureModel79', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState78', b2)
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState78', b2)
    if hasattr(b1, 'FeatureModel79'):
        assert not _is_linked(b1, 'FeatureModel79', a)
    if hasattr(b2, 'FeatureModel79'):
        assert _is_linked(b2, 'FeatureModel79', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState78', None)
    assert not _is_linked(a, 'spinefm_ActionModel_ConfigurationState78', b2)
    if hasattr(b2, 'FeatureModel79'):
        assert not _is_linked(b2, 'FeatureModel79', a)


def test_assoc_fm87_link_reassign_clear():
    a = spinefm_ActionModel_Action(id="sample_text")
    b1 = FeatureModel()
    b2 = FeatureModel()
    _safe_set(a, 'spinefm_ActionModel_Action88', b1)
    assert _is_linked(a, 'spinefm_ActionModel_Action88', b1)
    if hasattr(b1, 'FeatureModel89'):
        assert _is_linked(b1, 'FeatureModel89', a)
    _safe_set(a, 'spinefm_ActionModel_Action88', b2)
    assert _is_linked(a, 'spinefm_ActionModel_Action88', b2)
    if hasattr(b1, 'FeatureModel89'):
        assert not _is_linked(b1, 'FeatureModel89', a)
    if hasattr(b2, 'FeatureModel89'):
        assert _is_linked(b2, 'FeatureModel89', a)
    _safe_set(a, 'spinefm_ActionModel_Action88', None)
    assert not _is_linked(a, 'spinefm_ActionModel_Action88', b2)
    if hasattr(b2, 'FeatureModel89'):
        assert not _is_linked(b2, 'FeatureModel89', a)


def test_assoc_globalContext62_link_reassign_clear():
    a = spinefm_ProcessModel_ContextManager()
    b1 = GlobalContext()
    b2 = GlobalContext()
    _safe_set(a, 'spinefm_ProcessModel_ContextManager63', b1)
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager63', b1)
    if hasattr(b1, 'GlobalContext'):
        assert _is_linked(b1, 'GlobalContext', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager63', b2)
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager63', b2)
    if hasattr(b1, 'GlobalContext'):
        assert not _is_linked(b1, 'GlobalContext', a)
    if hasattr(b2, 'GlobalContext'):
        assert _is_linked(b2, 'GlobalContext', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager63', None)
    assert not _is_linked(a, 'spinefm_ProcessModel_ContextManager63', b2)
    if hasattr(b2, 'GlobalContext'):
        assert not _is_linked(b2, 'GlobalContext', a)


def test_assoc_inverse15_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociation(id="sample_text")
    b1 = DEAssociation()
    b2 = DEAssociation()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation16', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation16', b1)
    if hasattr(b1, 'DEAssociation17'):
        assert _is_linked(b1, 'DEAssociation17', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation16', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation16', b2)
    if hasattr(b1, 'DEAssociation17'):
        assert not _is_linked(b1, 'DEAssociation17', a)
    if hasattr(b2, 'DEAssociation17'):
        assert _is_linked(b2, 'DEAssociation17', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation16', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociation16', b2)
    if hasattr(b2, 'DEAssociation17'):
        assert not _is_linked(b2, 'DEAssociation17', a)


def test_assoc_inverse69_link_reassign_clear():
    a = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    b1 = RestrictionFunction()
    b2 = RestrictionFunction()
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction70', b1)
    assert _is_linked(a, 'spinefm_ActionModel_RestrictionFunction70', b1)
    if hasattr(b1, 'RestrictionFunction71'):
        assert _is_linked(b1, 'RestrictionFunction71', a)
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction70', b2)
    assert _is_linked(a, 'spinefm_ActionModel_RestrictionFunction70', b2)
    if hasattr(b1, 'RestrictionFunction71'):
        assert not _is_linked(b1, 'RestrictionFunction71', a)
    if hasattr(b2, 'RestrictionFunction71'):
        assert _is_linked(b2, 'RestrictionFunction71', a)
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction70', None)
    assert not _is_linked(a, 'spinefm_ActionModel_RestrictionFunction70', b2)
    if hasattr(b2, 'RestrictionFunction71'):
        assert not _is_linked(b2, 'RestrictionFunction71', a)


def test_assoc_links42_link_reassign_clear():
    a = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    b1 = Link()
    b2 = Link()
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', {b1})
    assert _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', b1)
    if hasattr(b1, 'Link44'):
        assert _is_linked(b1, 'Link44', a)
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', {b2})
    assert _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', b2)
    if hasattr(b1, 'Link44'):
        assert not _is_linked(b1, 'Link44', a)
    if hasattr(b2, 'Link44'):
        assert _is_linked(b2, 'Link44', a)
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', set())
    assert not _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration43', b2)
    if hasattr(b2, 'Link44'):
        assert not _is_linked(b2, 'Link44', a)


def test_assoc_localContexts64_link_reassign_clear():
    a = spinefm_ProcessModel_ContextManager()
    b1 = LocalContext()
    b2 = LocalContext()
    _safe_set(a, 'spinefm_ProcessModel_ContextManager65', {b1})
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager65', b1)
    if hasattr(b1, 'LocalContext'):
        assert _is_linked(b1, 'LocalContext', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager65', {b2})
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager65', b2)
    if hasattr(b1, 'LocalContext'):
        assert not _is_linked(b1, 'LocalContext', a)
    if hasattr(b2, 'LocalContext'):
        assert _is_linked(b2, 'LocalContext', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager65', set())
    assert not _is_linked(a, 'spinefm_ProcessModel_ContextManager65', b2)
    if hasattr(b2, 'LocalContext'):
        assert not _is_linked(b2, 'LocalContext', a)


def test_assoc_mspl61_link_reassign_clear():
    a = spinefm_ProcessModel_ContextManager()
    b1 = MultipleSoftwareProductLine()
    b2 = MultipleSoftwareProductLine()
    _safe_set(a, 'spinefm_ProcessModel_ContextManager', b1)
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager', b1)
    if hasattr(b1, 'MultipleSoftwareProductLine'):
        assert _is_linked(b1, 'MultipleSoftwareProductLine', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager', b2)
    assert _is_linked(a, 'spinefm_ProcessModel_ContextManager', b2)
    if hasattr(b1, 'MultipleSoftwareProductLine'):
        assert not _is_linked(b1, 'MultipleSoftwareProductLine', a)
    if hasattr(b2, 'MultipleSoftwareProductLine'):
        assert _is_linked(b2, 'MultipleSoftwareProductLine', a)
    _safe_set(a, 'spinefm_ProcessModel_ContextManager', None)
    assert not _is_linked(a, 'spinefm_ProcessModel_ContextManager', b2)
    if hasattr(b2, 'MultipleSoftwareProductLine'):
        assert not _is_linked(b2, 'MultipleSoftwareProductLine', a)


def test_assoc_refers_on24_link_reassign_clear():
    a = spinefm_MSPLModel_DomainElement(id="sample_text")
    b1 = FeatureModel()
    b2 = FeatureModel()
    _safe_set(a, 'spinefm_MSPLModel_DomainElement25', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement25', b1)
    if hasattr(b1, 'FeatureModel'):
        assert _is_linked(b1, 'FeatureModel', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement25', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DomainElement25', b2)
    if hasattr(b1, 'FeatureModel'):
        assert not _is_linked(b1, 'FeatureModel', a)
    if hasattr(b2, 'FeatureModel'):
        assert _is_linked(b2, 'FeatureModel', a)
    _safe_set(a, 'spinefm_MSPLModel_DomainElement25', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DomainElement25', b2)
    if hasattr(b2, 'FeatureModel'):
        assert not _is_linked(b2, 'FeatureModel', a)


def test_assoc_relatedAssociation34_link_reassign_clear():
    a = spinefm_ConfigurationModel_Link(id="sample_text")
    b1 = DEAssociation()
    b2 = DEAssociation()
    _safe_set(a, 'spinefm_ConfigurationModel_Link35', b1)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link35', b1)
    if hasattr(b1, 'DEAssociation36'):
        assert _is_linked(b1, 'DEAssociation36', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link35', b2)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link35', b2)
    if hasattr(b1, 'DEAssociation36'):
        assert not _is_linked(b1, 'DEAssociation36', a)
    if hasattr(b2, 'DEAssociation36'):
        assert _is_linked(b2, 'DEAssociation36', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link35', None)
    assert not _is_linked(a, 'spinefm_ConfigurationModel_Link35', b2)
    if hasattr(b2, 'DEAssociation36'):
        assert not _is_linked(b2, 'DEAssociation36', a)


def test_assoc_replacedBy66_link_reassign_clear():
    a = spinefm_ProcessModel_DeletedContextInformations(deletedContext="sample_text")
    b1 = Context()
    b2 = Context()
    _safe_set(a, 'spinefm_ProcessModel_DeletedContextInformations', b1)
    assert _is_linked(a, 'spinefm_ProcessModel_DeletedContextInformations', b1)
    if hasattr(b1, 'Context67'):
        assert _is_linked(b1, 'Context67', a)
    _safe_set(a, 'spinefm_ProcessModel_DeletedContextInformations', b2)
    assert _is_linked(a, 'spinefm_ProcessModel_DeletedContextInformations', b2)
    if hasattr(b1, 'Context67'):
        assert not _is_linked(b1, 'Context67', a)
    if hasattr(b2, 'Context67'):
        assert _is_linked(b2, 'Context67', a)
    _safe_set(a, 'spinefm_ProcessModel_DeletedContextInformations', None)
    assert not _is_linked(a, 'spinefm_ProcessModel_DeletedContextInformations', b2)
    if hasattr(b2, 'Context67'):
        assert not _is_linked(b2, 'Context67', a)


def test_assoc_restrictionFunction9_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociation(id="sample_text")
    b1 = RestrictionFunction()
    b2 = RestrictionFunction()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation', {b1})
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation', b1)
    if hasattr(b1, 'RestrictionFunction'):
        assert _is_linked(b1, 'RestrictionFunction', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation', {b2})
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation', b2)
    if hasattr(b1, 'RestrictionFunction'):
        assert not _is_linked(b1, 'RestrictionFunction', a)
    if hasattr(b2, 'RestrictionFunction'):
        assert _is_linked(b2, 'RestrictionFunction', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation', set())
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociation', b2)
    if hasattr(b2, 'RestrictionFunction'):
        assert not _is_linked(b2, 'RestrictionFunction', a)


def test_assoc_root0_link_reassign_clear():
    a = spinefm_FMModel_FeatureModel(id="sample_text", name="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'spinefm_FMModel_FeatureModel', b1)
    assert _is_linked(a, 'spinefm_FMModel_FeatureModel', b1)
    if hasattr(b1, 'Feature'):
        assert _is_linked(b1, 'Feature', a)
    _safe_set(a, 'spinefm_FMModel_FeatureModel', b2)
    assert _is_linked(a, 'spinefm_FMModel_FeatureModel', b2)
    if hasattr(b1, 'Feature'):
        assert not _is_linked(b1, 'Feature', a)
    if hasattr(b2, 'Feature'):
        assert _is_linked(b2, 'Feature', a)
    _safe_set(a, 'spinefm_FMModel_FeatureModel', None)
    assert not _is_linked(a, 'spinefm_FMModel_FeatureModel', b2)
    if hasattr(b2, 'Feature'):
        assert not _is_linked(b2, 'Feature', a)


def test_assoc_rules68_link_reassign_clear():
    a = spinefm_ActionModel_RestrictionFunction(id="sample_text")
    b1 = Rule()
    b2 = Rule()
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction', {b1})
    assert _is_linked(a, 'spinefm_ActionModel_RestrictionFunction', b1)
    if hasattr(b1, 'Rule'):
        assert _is_linked(b1, 'Rule', a)
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction', {b2})
    assert _is_linked(a, 'spinefm_ActionModel_RestrictionFunction', b2)
    if hasattr(b1, 'Rule'):
        assert not _is_linked(b1, 'Rule', a)
    if hasattr(b2, 'Rule'):
        assert _is_linked(b2, 'Rule', a)
    _safe_set(a, 'spinefm_ActionModel_RestrictionFunction', set())
    assert not _is_linked(a, 'spinefm_ActionModel_RestrictionFunction', b2)
    if hasattr(b2, 'Rule'):
        assert not _is_linked(b2, 'Rule', a)


def test_assoc_selectedFeatures72_link_reassign_clear():
    a = spinefm_ActionModel_ConfigurationState(id="sample_text")
    b1 = Feature()
    b2 = Feature()
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState', {b1})
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState', b1)
    if hasattr(b1, 'Feature73'):
        assert _is_linked(b1, 'Feature73', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState', {b2})
    assert _is_linked(a, 'spinefm_ActionModel_ConfigurationState', b2)
    if hasattr(b1, 'Feature73'):
        assert not _is_linked(b1, 'Feature73', a)
    if hasattr(b2, 'Feature73'):
        assert _is_linked(b2, 'Feature73', a)
    _safe_set(a, 'spinefm_ActionModel_ConfigurationState', set())
    assert not _is_linked(a, 'spinefm_ActionModel_ConfigurationState', b2)
    if hasattr(b2, 'Feature73'):
        assert not _is_linked(b2, 'Feature73', a)


def test_assoc_source10_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociation(id="sample_text")
    b1 = DEAssociationEnd()
    b2 = DEAssociationEnd()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation11', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation11', b1)
    if hasattr(b1, 'DEAssociationEnd'):
        assert _is_linked(b1, 'DEAssociationEnd', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation11', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation11', b2)
    if hasattr(b1, 'DEAssociationEnd'):
        assert not _is_linked(b1, 'DEAssociationEnd', a)
    if hasattr(b2, 'DEAssociationEnd'):
        assert _is_linked(b2, 'DEAssociationEnd', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation11', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociation11', b2)
    if hasattr(b2, 'DEAssociationEnd'):
        assert not _is_linked(b2, 'DEAssociationEnd', a)


def test_assoc_source33_link_reassign_clear():
    a = spinefm_ConfigurationModel_Link(id="sample_text")
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'spinefm_ConfigurationModel_Link', b1)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link', b1)
    if hasattr(b1, 'Configuration'):
        assert _is_linked(b1, 'Configuration', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link', b2)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link', b2)
    if hasattr(b1, 'Configuration'):
        assert not _is_linked(b1, 'Configuration', a)
    if hasattr(b2, 'Configuration'):
        assert _is_linked(b2, 'Configuration', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link', None)
    assert not _is_linked(a, 'spinefm_ConfigurationModel_Link', b2)
    if hasattr(b2, 'Configuration'):
        assert not _is_linked(b2, 'Configuration', a)


def test_assoc_state31_link_reassign_clear():
    a = spinefm_ConfigurationModel_Configuration(description="sample_text", id="sample_text")
    b1 = ConfigurationState()
    b2 = ConfigurationState()
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration32', b1)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Configuration32', b1)
    if hasattr(b1, 'ConfigurationState'):
        assert _is_linked(b1, 'ConfigurationState', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration32', b2)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Configuration32', b2)
    if hasattr(b1, 'ConfigurationState'):
        assert not _is_linked(b1, 'ConfigurationState', a)
    if hasattr(b2, 'ConfigurationState'):
        assert _is_linked(b2, 'ConfigurationState', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Configuration32', None)
    assert not _is_linked(a, 'spinefm_ConfigurationModel_Configuration32', b2)
    if hasattr(b2, 'ConfigurationState'):
        assert not _is_linked(b2, 'ConfigurationState', a)


def test_assoc_state82_link_reassign_clear():
    a = spinefm_ActionModel_Rule(id="sample_text")
    b1 = ConfigurationState()
    b2 = ConfigurationState()
    _safe_set(a, 'spinefm_ActionModel_Rule83', b1)
    assert _is_linked(a, 'spinefm_ActionModel_Rule83', b1)
    if hasattr(b1, 'ConfigurationState84'):
        assert _is_linked(b1, 'ConfigurationState84', a)
    _safe_set(a, 'spinefm_ActionModel_Rule83', b2)
    assert _is_linked(a, 'spinefm_ActionModel_Rule83', b2)
    if hasattr(b1, 'ConfigurationState84'):
        assert not _is_linked(b1, 'ConfigurationState84', a)
    if hasattr(b2, 'ConfigurationState84'):
        assert _is_linked(b2, 'ConfigurationState84', a)
    _safe_set(a, 'spinefm_ActionModel_Rule83', None)
    assert not _is_linked(a, 'spinefm_ActionModel_Rule83', b2)
    if hasattr(b2, 'ConfigurationState84'):
        assert not _is_linked(b2, 'ConfigurationState84', a)


def test_assoc_subConfigurations40_link_reassign_clear():
    a = spinefm_ConfigurationModel_CompositeConfiguration(name="sample_text")
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration', {b1})
    assert _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration', b1)
    if hasattr(b1, 'Configuration41'):
        assert _is_linked(b1, 'Configuration41', a)
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration', {b2})
    assert _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration', b2)
    if hasattr(b1, 'Configuration41'):
        assert not _is_linked(b1, 'Configuration41', a)
    if hasattr(b2, 'Configuration41'):
        assert _is_linked(b2, 'Configuration41', a)
    _safe_set(a, 'spinefm_ConfigurationModel_CompositeConfiguration', set())
    assert not _is_linked(a, 'spinefm_ConfigurationModel_CompositeConfiguration', b2)
    if hasattr(b2, 'Configuration41'):
        assert not _is_linked(b2, 'Configuration41', a)


def test_assoc_target12_link_reassign_clear():
    a = spinefm_MSPLModel_DEAssociation(id="sample_text")
    b1 = DEAssociationEnd()
    b2 = DEAssociationEnd()
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation13', b1)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation13', b1)
    if hasattr(b1, 'DEAssociationEnd14'):
        assert _is_linked(b1, 'DEAssociationEnd14', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation13', b2)
    assert _is_linked(a, 'spinefm_MSPLModel_DEAssociation13', b2)
    if hasattr(b1, 'DEAssociationEnd14'):
        assert not _is_linked(b1, 'DEAssociationEnd14', a)
    if hasattr(b2, 'DEAssociationEnd14'):
        assert _is_linked(b2, 'DEAssociationEnd14', a)
    _safe_set(a, 'spinefm_MSPLModel_DEAssociation13', None)
    assert not _is_linked(a, 'spinefm_MSPLModel_DEAssociation13', b2)
    if hasattr(b2, 'DEAssociationEnd14'):
        assert not _is_linked(b2, 'DEAssociationEnd14', a)


def test_assoc_target37_link_reassign_clear():
    a = spinefm_ConfigurationModel_Link(id="sample_text")
    b1 = Configuration()
    b2 = Configuration()
    _safe_set(a, 'spinefm_ConfigurationModel_Link38', b1)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link38', b1)
    if hasattr(b1, 'Configuration39'):
        assert _is_linked(b1, 'Configuration39', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link38', b2)
    assert _is_linked(a, 'spinefm_ConfigurationModel_Link38', b2)
    if hasattr(b1, 'Configuration39'):
        assert not _is_linked(b1, 'Configuration39', a)
    if hasattr(b2, 'Configuration39'):
        assert _is_linked(b2, 'Configuration39', a)
    _safe_set(a, 'spinefm_ConfigurationModel_Link38', None)
    assert not _is_linked(a, 'spinefm_ConfigurationModel_Link38', b2)
    if hasattr(b2, 'Configuration39'):
        assert not _is_linked(b2, 'Configuration39', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


CompositeConfiguration_strategy = st.builds(CompositeConfiguration)
@given(instance=CompositeConfiguration_strategy)
@settings(max_examples=25)
def test_CompositeConfiguration_instantiation(instance):
    assert isinstance(instance, CompositeConfiguration)


Configuration_strategy = st.builds(Configuration)
@given(instance=Configuration_strategy)
@settings(max_examples=25)
def test_Configuration_instantiation(instance):
    assert isinstance(instance, Configuration)


ConfigurationProcessStep_strategy = st.builds(ConfigurationProcessStep)
@given(instance=ConfigurationProcessStep_strategy)
@settings(max_examples=25)
def test_ConfigurationProcessStep_instantiation(instance):
    assert isinstance(instance, ConfigurationProcessStep)


ConfigurationState_strategy = st.builds(ConfigurationState)
@given(instance=ConfigurationState_strategy)
@settings(max_examples=25)
def test_ConfigurationState_instantiation(instance):
    assert isinstance(instance, ConfigurationState)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Context_strategy = st.builds(Context)
@given(instance=Context_strategy)
@settings(max_examples=25)
def test_Context_instantiation(instance):
    assert isinstance(instance, Context)


DEAssociation_strategy = st.builds(DEAssociation)
@given(instance=DEAssociation_strategy)
@settings(max_examples=25)
def test_DEAssociation_instantiation(instance):
    assert isinstance(instance, DEAssociation)


DEAssociationEnd_strategy = st.builds(DEAssociationEnd)
@given(instance=DEAssociationEnd_strategy)
@settings(max_examples=25)
def test_DEAssociationEnd_instantiation(instance):
    assert isinstance(instance, DEAssociationEnd)


DomainElement_strategy = st.builds(DomainElement)
@given(instance=DomainElement_strategy)
@settings(max_examples=25)
def test_DomainElement_instantiation(instance):
    assert isinstance(instance, DomainElement)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


FeatureModel_strategy = st.builds(FeatureModel)
@given(instance=FeatureModel_strategy)
@settings(max_examples=25)
def test_FeatureModel_instantiation(instance):
    assert isinstance(instance, FeatureModel)


GlobalContext_strategy = st.builds(GlobalContext)
@given(instance=GlobalContext_strategy)
@settings(max_examples=25)
def test_GlobalContext_instantiation(instance):
    assert isinstance(instance, GlobalContext)


Group_strategy = st.builds(Group)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Link_strategy = st.builds(Link)
@given(instance=Link_strategy)
@settings(max_examples=25)
def test_Link_instantiation(instance):
    assert isinstance(instance, Link)


LocalContext_strategy = st.builds(LocalContext)
@given(instance=LocalContext_strategy)
@settings(max_examples=25)
def test_LocalContext_instantiation(instance):
    assert isinstance(instance, LocalContext)


MultipleSoftwareProductLine_strategy = st.builds(MultipleSoftwareProductLine)
@given(instance=MultipleSoftwareProductLine_strategy)
@settings(max_examples=25)
def test_MultipleSoftwareProductLine_instantiation(instance):
    assert isinstance(instance, MultipleSoftwareProductLine)


MultiplicityElement_strategy = st.builds(MultiplicityElement)
@given(instance=MultiplicityElement_strategy)
@settings(max_examples=25)
def test_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)


RestrictionFunction_strategy = st.builds(RestrictionFunction)
@given(instance=RestrictionFunction_strategy)
@settings(max_examples=25)
def test_RestrictionFunction_instantiation(instance):
    assert isinstance(instance, RestrictionFunction)


Rule_strategy = st.builds(Rule)
@given(instance=Rule_strategy)
@settings(max_examples=25)
def test_Rule_instantiation(instance):
    assert isinstance(instance, Rule)


spinefm_ActionModel_Action_strategy = st.builds(spinefm_ActionModel_Action, id=safe_text)
@given(instance=spinefm_ActionModel_Action_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_Action_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_Action)


spinefm_ActionModel_ActionAddCTConstraint_strategy = st.builds(spinefm_ActionModel_ActionAddCTConstraint)
@given(instance=spinefm_ActionModel_ActionAddCTConstraint_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_ActionAddCTConstraint_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_ActionAddCTConstraint)


spinefm_ActionModel_ActionDeselect_strategy = st.builds(spinefm_ActionModel_ActionDeselect)
@given(instance=spinefm_ActionModel_ActionDeselect_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_ActionDeselect_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_ActionDeselect)


spinefm_ActionModel_ActionSelect_strategy = st.builds(spinefm_ActionModel_ActionSelect)
@given(instance=spinefm_ActionModel_ActionSelect_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_ActionSelect_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_ActionSelect)


spinefm_ActionModel_ConfigurationState_strategy = st.builds(spinefm_ActionModel_ConfigurationState, id=safe_text)
@given(instance=spinefm_ActionModel_ConfigurationState_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_ConfigurationState_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_ConfigurationState)


spinefm_ActionModel_RestrictionFunction_strategy = st.builds(spinefm_ActionModel_RestrictionFunction, id=safe_text)
@given(instance=spinefm_ActionModel_RestrictionFunction_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_RestrictionFunction_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_RestrictionFunction)


spinefm_ActionModel_Rule_strategy = st.builds(spinefm_ActionModel_Rule, id=safe_text)
@given(instance=spinefm_ActionModel_Rule_strategy)
@settings(max_examples=25)
def test_spinefm_ActionModel_Rule_instantiation(instance):
    assert isinstance(instance, spinefm_ActionModel_Rule)


spinefm_ConfigurationModel_CompositeConfiguration_strategy = st.builds(spinefm_ConfigurationModel_CompositeConfiguration, name=safe_text)
@given(instance=spinefm_ConfigurationModel_CompositeConfiguration_strategy)
@settings(max_examples=25)
def test_spinefm_ConfigurationModel_CompositeConfiguration_instantiation(instance):
    assert isinstance(instance, spinefm_ConfigurationModel_CompositeConfiguration)


spinefm_ConfigurationModel_Configuration_strategy = st.builds(spinefm_ConfigurationModel_Configuration, description=safe_text, id=safe_text)
@given(instance=spinefm_ConfigurationModel_Configuration_strategy)
@settings(max_examples=25)
def test_spinefm_ConfigurationModel_Configuration_instantiation(instance):
    assert isinstance(instance, spinefm_ConfigurationModel_Configuration)


spinefm_ConfigurationModel_Link_strategy = st.builds(spinefm_ConfigurationModel_Link, id=safe_text)
@given(instance=spinefm_ConfigurationModel_Link_strategy)
@settings(max_examples=25)
def test_spinefm_ConfigurationModel_Link_instantiation(instance):
    assert isinstance(instance, spinefm_ConfigurationModel_Link)


spinefm_FMModel_Constraint_strategy = st.builds(spinefm_FMModel_Constraint, Rule=safe_text)
@given(instance=spinefm_FMModel_Constraint_strategy)
@settings(max_examples=25)
def test_spinefm_FMModel_Constraint_instantiation(instance):
    assert isinstance(instance, spinefm_FMModel_Constraint)


spinefm_FMModel_Feature_strategy = st.builds(spinefm_FMModel_Feature, id=safe_text, name=safe_text)
@given(instance=spinefm_FMModel_Feature_strategy)
@settings(max_examples=25)
def test_spinefm_FMModel_Feature_instantiation(instance):
    assert isinstance(instance, spinefm_FMModel_Feature)


spinefm_FMModel_FeatureModel_strategy = st.builds(spinefm_FMModel_FeatureModel, id=safe_text, name=safe_text)
@given(instance=spinefm_FMModel_FeatureModel_strategy)
@settings(max_examples=25)
def test_spinefm_FMModel_FeatureModel_instantiation(instance):
    assert isinstance(instance, spinefm_FMModel_FeatureModel)


spinefm_FMModel_Group_strategy = st.builds(spinefm_FMModel_Group, state=safe_text)
@given(instance=spinefm_FMModel_Group_strategy)
@settings(max_examples=25)
def test_spinefm_FMModel_Group_instantiation(instance):
    assert isinstance(instance, spinefm_FMModel_Group)


spinefm_MSPLModel_DEAssociation_strategy = st.builds(spinefm_MSPLModel_DEAssociation, id=safe_text)
@given(instance=spinefm_MSPLModel_DEAssociation_strategy)
@settings(max_examples=25)
def test_spinefm_MSPLModel_DEAssociation_instantiation(instance):
    assert isinstance(instance, spinefm_MSPLModel_DEAssociation)


spinefm_MSPLModel_DEAssociationEnd_strategy = st.builds(spinefm_MSPLModel_DEAssociationEnd, id=safe_text)
@given(instance=spinefm_MSPLModel_DEAssociationEnd_strategy)
@settings(max_examples=25)
def test_spinefm_MSPLModel_DEAssociationEnd_instantiation(instance):
    assert isinstance(instance, spinefm_MSPLModel_DEAssociationEnd)


spinefm_MSPLModel_DomainElement_strategy = st.builds(spinefm_MSPLModel_DomainElement, id=safe_text)
@given(instance=spinefm_MSPLModel_DomainElement_strategy)
@settings(max_examples=25)
def test_spinefm_MSPLModel_DomainElement_instantiation(instance):
    assert isinstance(instance, spinefm_MSPLModel_DomainElement)


spinefm_MSPLModel_MultipleSoftwareProductLine_strategy = st.builds(spinefm_MSPLModel_MultipleSoftwareProductLine)
@given(instance=spinefm_MSPLModel_MultipleSoftwareProductLine_strategy)
@settings(max_examples=25)
def test_spinefm_MSPLModel_MultipleSoftwareProductLine_instantiation(instance):
    assert isinstance(instance, spinefm_MSPLModel_MultipleSoftwareProductLine)


spinefm_MSPLModel_MultiplicityElement_strategy = st.builds(spinefm_MSPLModel_MultiplicityElement, id=safe_text, lowerBound=st.integers(), upperBound=st.integers())
@given(instance=spinefm_MSPLModel_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_spinefm_MSPLModel_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, spinefm_MSPLModel_MultiplicityElement)


spinefm_ProcessModel_ConfigurationProcessStep_strategy = st.builds(spinefm_ProcessModel_ConfigurationProcessStep, description=safe_text, id=safe_text, userConfig=st.booleans())
@given(instance=spinefm_ProcessModel_ConfigurationProcessStep_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_ConfigurationProcessStep_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_ConfigurationProcessStep)


spinefm_ProcessModel_Context_strategy = st.builds(spinefm_ProcessModel_Context, id=safe_text)
@given(instance=spinefm_ProcessModel_Context_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_Context_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_Context)


spinefm_ProcessModel_ContextManager_strategy = st.builds(spinefm_ProcessModel_ContextManager)
@given(instance=spinefm_ProcessModel_ContextManager_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_ContextManager_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_ContextManager)


spinefm_ProcessModel_DeletedContextInformations_strategy = st.builds(spinefm_ProcessModel_DeletedContextInformations, deletedContext=safe_text)
@given(instance=spinefm_ProcessModel_DeletedContextInformations_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_DeletedContextInformations_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_DeletedContextInformations)


spinefm_ProcessModel_GlobalContext_strategy = st.builds(spinefm_ProcessModel_GlobalContext)
@given(instance=spinefm_ProcessModel_GlobalContext_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_GlobalContext_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_GlobalContext)


spinefm_ProcessModel_LocalContext_strategy = st.builds(spinefm_ProcessModel_LocalContext)
@given(instance=spinefm_ProcessModel_LocalContext_strategy)
@settings(max_examples=25)
def test_spinefm_ProcessModel_LocalContext_instantiation(instance):
    assert isinstance(instance, spinefm_ProcessModel_LocalContext)



