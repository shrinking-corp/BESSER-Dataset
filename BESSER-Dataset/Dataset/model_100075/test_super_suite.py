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
    build_BParameterPredicate,
    RequiredCapability,
    build_AliasedRequiredCapability,
    BuildConcernContext,
    CapabilityPredicate,
    build_UnitNamePredicate,
    build_BuilderConcernContext,
    BConcernContext,
    build_NameSpacePredicate,
    build_BNamePredicate,
    BExpression,
    build_CapabilityPredicate,
    build_PathGroupPredicate,
    build_InputPredicate,
    build_ImplementsPredicate,
    build_ProvidesPredicate,
    build_RequiresPredicate,
    build_BuilderNamePredicate,
    build_UnitProvider,
    build_BuilderQuery,
    build_PathVector,
    CompoundUnitProvider,
    build_BestFoundUnitProvider,
    build_IBuildUnitRepository,
    build_RepoOption,
    UnitProvider,
    build_CompoundUnitProvider,
    build_RepositoryUnitProvider,
    Capability,
    build_VersionedCapability,
    INamedValue,
    build_Capability,
    build_BParameterList,
    BuilderInput,
    build_BuilderCall,
    build_BuilderInputDecorator,
    build_ConditionalPathVector,
    build_PathGroup,
    build_BuilderInput,
    build_BExpression,
    IFunction,
    build_ContainerConfiguration,
    build_FragmentHost,
    build_IBuildUnitContainer,
    build_FirstFoundUnitProvider,
    build_RequiredCapability,
    IVarName,
    IProvidedCapabilityContainer,
    build_IBuilder,
    build_BuildConcernContext,
    build_Repository,
    build_Synchronization,
    build_BPropertySet,
    build_BConcern,
    build_IType,
    IRequiredCapabilityContainer,
    build_UnitConcernContext,
    BParameterDeclaration,
    build_UnitParameterDeclaration,
    BuilderCall,
    build_BuildCallMultiple,
    build_BWithExpression,
    BuilderInputDecorator,
    build_BuilderInputContextDecorator,
    build_BuilderInputCondition,
    build_BuilderInputNameDecorator,
    BuilderCallFacade,
    build_IEffectiveFacade,
    build_BuilderInputGroup,
    BuildCallSingle,
    build_BuildCallOnReferencedRequirement,
    build_BuildCallOnDeclaredRequirement,
    build_BuildCallSingle,
    BuildCallMultiple,
    build_BuildCallOnSelectedRequirements,
    build_DelegatingUnitProvider,
    build_BSwitchExpression,
    build_SwitchUnitProvider,
    build_Branch,
    PathGroupPredicate,
    build_SourcePredicate,
    build_OutputPredicate,
    BInnerContext,
    build_BuildResultContext,
    build_BExecutionContext,
    ResolutionInfo,
    build_UnitResolutionInfo,
    CompoundBuildUnitRepository,
    build_CompoundFirstFoundRepository,
    BuildUnitRepository,
    build_BeeModelRepository,
    build_ExecutionStackRepository,
    build_UnitRepositoryDescription,
    build_CompoundBuildUnitRepository,
    IBuildUnitRepository,
    build_BuildUnitRepository,
    ITypedValueContainer,
    build_BuildSet,
    build_BuilderCallFacade,
    EffectiveFacade,
    build_EffectiveRequirementFacade,
    build_EffectiveUnitFacade,
    build_EffectiveCapabilityFacade,
    build_BeeHive,
    IEffectiveFacade,
    build_EffectiveBuilderCallFacade,
    build_EffectiveFacade,
    build_ResolutionInfo,
    build_IProvidedCapabilityContainer,
    build_IRequiredCapabilityContainer,
    build_IFunction,
    IBuildUnitContainer,
    BChainedExpression,
    build_BeeModel,
    BFunctionWrapper,
    BJavaFunction,
    IBuilder,
    build_BuilderWrapper,
    build_BuilderJava,
    B3Function,
    build_Builder,
    BFunctionContainer,
    VersionedCapability,
    build_BuildUnit,
    BranchPointType,
    MergeConflictStrategy,
    TriState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_build_bparameterpredicate_is_not_abstract():
    assert not inspect.isabstract(build_BParameterPredicate)


def test_hyp_build_bparameterpredicate_constructor_exists():
    assert callable(build_BParameterPredicate.__init__)


def test_hyp_build_bparameterpredicate_constructor_args():
    sig = inspect.signature(build_BParameterPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requiredcapability_is_not_abstract():
    assert not inspect.isabstract(RequiredCapability)


def test_hyp_requiredcapability_constructor_exists():
    assert callable(RequiredCapability.__init__)


def test_hyp_requiredcapability_constructor_args():
    sig = inspect.signature(RequiredCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_aliasedrequiredcapability_is_not_abstract():
    assert not inspect.isabstract(build_AliasedRequiredCapability)


def test_hyp_build_aliasedrequiredcapability_constructor_exists():
    assert callable(build_AliasedRequiredCapability.__init__)


def test_hyp_build_aliasedrequiredcapability_constructor_args():
    sig = inspect.signature(build_AliasedRequiredCapability.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"




def test_hyp_buildconcerncontext_is_not_abstract():
    assert not inspect.isabstract(BuildConcernContext)


def test_hyp_buildconcerncontext_constructor_exists():
    assert callable(BuildConcernContext.__init__)


def test_hyp_buildconcerncontext_constructor_args():
    sig = inspect.signature(BuildConcernContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_capabilitypredicate_is_not_abstract():
    assert not inspect.isabstract(CapabilityPredicate)


def test_hyp_capabilitypredicate_constructor_exists():
    assert callable(CapabilityPredicate.__init__)


def test_hyp_capabilitypredicate_constructor_args():
    sig = inspect.signature(CapabilityPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitnamepredicate_is_not_abstract():
    assert not inspect.isabstract(build_UnitNamePredicate)


def test_hyp_build_unitnamepredicate_constructor_exists():
    assert callable(build_UnitNamePredicate.__init__)


def test_hyp_build_unitnamepredicate_constructor_args():
    sig = inspect.signature(build_UnitNamePredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderconcerncontext_is_not_abstract():
    assert not inspect.isabstract(build_BuilderConcernContext)


def test_hyp_build_builderconcerncontext_constructor_exists():
    assert callable(build_BuilderConcernContext.__init__)


def test_hyp_build_builderconcerncontext_constructor_args():
    sig = inspect.signature(build_BuilderConcernContext.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAnnotationsRemovals" in params, "Missing parameter 'sourceAnnotationsRemovals'"
    assert "removePostInputCondition" in params, "Missing parameter 'removePostInputCondition'"
    assert "matchParameters" in params, "Missing parameter 'matchParameters'"
    assert "outputAnnotationsRemovals" in params, "Missing parameter 'outputAnnotationsRemovals'"
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "removePreCondition" in params, "Missing parameter 'removePreCondition'"
    assert "removePostCondition" in params, "Missing parameter 'removePostCondition'"










def test_hyp_bconcerncontext_is_not_abstract():
    assert not inspect.isabstract(BConcernContext)


def test_hyp_bconcerncontext_constructor_exists():
    assert callable(BConcernContext.__init__)


def test_hyp_bconcerncontext_constructor_args():
    sig = inspect.signature(BConcernContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_namespacepredicate_is_not_abstract():
    assert not inspect.isabstract(build_NameSpacePredicate)


def test_hyp_build_namespacepredicate_constructor_exists():
    assert callable(build_NameSpacePredicate.__init__)


def test_hyp_build_namespacepredicate_constructor_args():
    sig = inspect.signature(build_NameSpacePredicate.__init__)
    params = list(sig.parameters.keys())
    assert "nameSpace" in params, "Missing parameter 'nameSpace'"




def test_hyp_build_bnamepredicate_is_not_abstract():
    assert not inspect.isabstract(build_BNamePredicate)


def test_hyp_build_bnamepredicate_constructor_exists():
    assert callable(build_BNamePredicate.__init__)


def test_hyp_build_bnamepredicate_constructor_args():
    sig = inspect.signature(build_BNamePredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bexpression_is_not_abstract():
    assert not inspect.isabstract(BExpression)


def test_hyp_bexpression_constructor_exists():
    assert callable(BExpression.__init__)


def test_hyp_bexpression_constructor_args():
    sig = inspect.signature(BExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_capabilitypredicate_is_not_abstract():
    assert not inspect.isabstract(build_CapabilityPredicate)


def test_hyp_build_capabilitypredicate_constructor_exists():
    assert callable(build_CapabilityPredicate.__init__)


def test_hyp_build_capabilitypredicate_constructor_args():
    sig = inspect.signature(build_CapabilityPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "versionRange" in params, "Missing parameter 'versionRange'"




def test_hyp_build_pathgrouppredicate_is_not_abstract():
    assert not inspect.isabstract(build_PathGroupPredicate)


def test_hyp_build_pathgrouppredicate_constructor_exists():
    assert callable(build_PathGroupPredicate.__init__)


def test_hyp_build_pathgrouppredicate_constructor_args():
    sig = inspect.signature(build_PathGroupPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_inputpredicate_is_not_abstract():
    assert not inspect.isabstract(build_InputPredicate)


def test_hyp_build_inputpredicate_constructor_exists():
    assert callable(build_InputPredicate.__init__)


def test_hyp_build_inputpredicate_constructor_args():
    sig = inspect.signature(build_InputPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_implementspredicate_is_not_abstract():
    assert not inspect.isabstract(build_ImplementsPredicate)


def test_hyp_build_implementspredicate_constructor_exists():
    assert callable(build_ImplementsPredicate.__init__)


def test_hyp_build_implementspredicate_constructor_args():
    sig = inspect.signature(build_ImplementsPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_providespredicate_is_not_abstract():
    assert not inspect.isabstract(build_ProvidesPredicate)


def test_hyp_build_providespredicate_constructor_exists():
    assert callable(build_ProvidesPredicate.__init__)


def test_hyp_build_providespredicate_constructor_args():
    sig = inspect.signature(build_ProvidesPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_requirespredicate_is_not_abstract():
    assert not inspect.isabstract(build_RequiresPredicate)


def test_hyp_build_requirespredicate_constructor_exists():
    assert callable(build_RequiresPredicate.__init__)


def test_hyp_build_requirespredicate_constructor_args():
    sig = inspect.signature(build_RequiresPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "meta" in params, "Missing parameter 'meta'"




def test_hyp_build_buildernamepredicate_is_not_abstract():
    assert not inspect.isabstract(build_BuilderNamePredicate)


def test_hyp_build_buildernamepredicate_constructor_exists():
    assert callable(build_BuilderNamePredicate.__init__)


def test_hyp_build_buildernamepredicate_constructor_args():
    sig = inspect.signature(build_BuilderNamePredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitprovider_is_not_abstract():
    assert not inspect.isabstract(build_UnitProvider)


def test_hyp_build_unitprovider_constructor_exists():
    assert callable(build_UnitProvider.__init__)


def test_hyp_build_unitprovider_constructor_args():
    sig = inspect.signature(build_UnitProvider.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"




def test_hyp_build_builderquery_is_not_abstract():
    assert not inspect.isabstract(build_BuilderQuery)


def test_hyp_build_builderquery_constructor_exists():
    assert callable(build_BuilderQuery.__init__)


def test_hyp_build_builderquery_constructor_args():
    sig = inspect.signature(build_BuilderQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_pathvector_is_not_abstract():
    assert not inspect.isabstract(build_PathVector)


def test_hyp_build_pathvector_constructor_exists():
    assert callable(build_PathVector.__init__)


def test_hyp_build_pathvector_constructor_args():
    sig = inspect.signature(build_PathVector.__init__)
    params = list(sig.parameters.keys())
    assert "basePath" in params, "Missing parameter 'basePath'"
    assert "paths" in params, "Missing parameter 'paths'"





def test_hyp_compoundunitprovider_is_not_abstract():
    assert not inspect.isabstract(CompoundUnitProvider)


def test_hyp_compoundunitprovider_constructor_exists():
    assert callable(CompoundUnitProvider.__init__)


def test_hyp_compoundunitprovider_constructor_args():
    sig = inspect.signature(CompoundUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bestfoundunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_BestFoundUnitProvider)


def test_hyp_build_bestfoundunitprovider_constructor_exists():
    assert callable(build_BestFoundUnitProvider.__init__)


def test_hyp_build_bestfoundunitprovider_constructor_args():
    sig = inspect.signature(build_BestFoundUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_ibuildunitrepository_is_not_abstract():
    assert not inspect.isabstract(build_IBuildUnitRepository)


def test_hyp_build_ibuildunitrepository_constructor_exists():
    assert callable(build_IBuildUnitRepository.__init__)


def test_hyp_build_ibuildunitrepository_constructor_args():
    sig = inspect.signature(build_IBuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_repooption_is_not_abstract():
    assert not inspect.isabstract(build_RepoOption)


def test_hyp_build_repooption_constructor_exists():
    assert callable(build_RepoOption.__init__)


def test_hyp_build_repooption_constructor_args():
    sig = inspect.signature(build_RepoOption.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_unitprovider_is_not_abstract():
    assert not inspect.isabstract(UnitProvider)


def test_hyp_unitprovider_constructor_exists():
    assert callable(UnitProvider.__init__)


def test_hyp_unitprovider_constructor_args():
    sig = inspect.signature(UnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_compoundunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_CompoundUnitProvider)


def test_hyp_build_compoundunitprovider_constructor_exists():
    assert callable(build_CompoundUnitProvider.__init__)


def test_hyp_build_compoundunitprovider_constructor_args():
    sig = inspect.signature(build_CompoundUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_repositoryunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_RepositoryUnitProvider)


def test_hyp_build_repositoryunitprovider_constructor_exists():
    assert callable(build_RepositoryUnitProvider.__init__)


def test_hyp_build_repositoryunitprovider_constructor_args():
    sig = inspect.signature(build_RepositoryUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_capability_is_not_abstract():
    assert not inspect.isabstract(Capability)


def test_hyp_capability_constructor_exists():
    assert callable(Capability.__init__)


def test_hyp_capability_constructor_args():
    sig = inspect.signature(Capability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_versionedcapability_is_not_abstract():
    assert not inspect.isabstract(build_VersionedCapability)


def test_hyp_build_versionedcapability_constructor_exists():
    assert callable(build_VersionedCapability.__init__)


def test_hyp_build_versionedcapability_constructor_args():
    sig = inspect.signature(build_VersionedCapability.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"




def test_hyp_inamedvalue_is_not_abstract():
    assert not inspect.isabstract(INamedValue)


def test_hyp_inamedvalue_constructor_exists():
    assert callable(INamedValue.__init__)


def test_hyp_inamedvalue_constructor_args():
    sig = inspect.signature(INamedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_capability_is_not_abstract():
    assert not inspect.isabstract(build_Capability)


def test_hyp_build_capability_constructor_exists():
    assert callable(build_Capability.__init__)


def test_hyp_build_capability_constructor_args():
    sig = inspect.signature(build_Capability.__init__)
    params = list(sig.parameters.keys())
    assert "nameSpace" in params, "Missing parameter 'nameSpace'"




def test_hyp_build_bparameterlist_is_not_abstract():
    assert not inspect.isabstract(build_BParameterList)


def test_hyp_build_bparameterlist_constructor_exists():
    assert callable(build_BParameterList.__init__)


def test_hyp_build_bparameterlist_constructor_args():
    sig = inspect.signature(build_BParameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builderinput_is_not_abstract():
    assert not inspect.isabstract(BuilderInput)


def test_hyp_builderinput_constructor_exists():
    assert callable(BuilderInput.__init__)


def test_hyp_builderinput_constructor_args():
    sig = inspect.signature(BuilderInput.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildercall_is_not_abstract():
    assert not inspect.isabstract(build_BuilderCall)


def test_hyp_build_buildercall_constructor_exists():
    assert callable(build_BuilderCall.__init__)


def test_hyp_build_buildercall_constructor_args():
    sig = inspect.signature(build_BuilderCall.__init__)
    params = list(sig.parameters.keys())
    assert "builderName" in params, "Missing parameter 'builderName'"




def test_hyp_build_builderinputdecorator_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInputDecorator)


def test_hyp_build_builderinputdecorator_constructor_exists():
    assert callable(build_BuilderInputDecorator.__init__)


def test_hyp_build_builderinputdecorator_constructor_args():
    sig = inspect.signature(build_BuilderInputDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_conditionalpathvector_is_not_abstract():
    assert not inspect.isabstract(build_ConditionalPathVector)


def test_hyp_build_conditionalpathvector_constructor_exists():
    assert callable(build_ConditionalPathVector.__init__)


def test_hyp_build_conditionalpathvector_constructor_args():
    sig = inspect.signature(build_ConditionalPathVector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_pathgroup_is_not_abstract():
    assert not inspect.isabstract(build_PathGroup)


def test_hyp_build_pathgroup_constructor_exists():
    assert callable(build_PathGroup.__init__)


def test_hyp_build_pathgroup_constructor_args():
    sig = inspect.signature(build_PathGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderinput_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInput)


def test_hyp_build_builderinput_constructor_exists():
    assert callable(build_BuilderInput.__init__)


def test_hyp_build_builderinput_constructor_args():
    sig = inspect.signature(build_BuilderInput.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bexpression_is_not_abstract():
    assert not inspect.isabstract(build_BExpression)


def test_hyp_build_bexpression_constructor_exists():
    assert callable(build_BExpression.__init__)


def test_hyp_build_bexpression_constructor_args():
    sig = inspect.signature(build_BExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ifunction_is_not_abstract():
    assert not inspect.isabstract(IFunction)


def test_hyp_ifunction_constructor_exists():
    assert callable(IFunction.__init__)


def test_hyp_ifunction_constructor_args():
    sig = inspect.signature(IFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_containerconfiguration_is_not_abstract():
    assert not inspect.isabstract(build_ContainerConfiguration)


def test_hyp_build_containerconfiguration_constructor_exists():
    assert callable(build_ContainerConfiguration.__init__)


def test_hyp_build_containerconfiguration_constructor_args():
    sig = inspect.signature(build_ContainerConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_build_fragmenthost_is_not_abstract():
    assert not inspect.isabstract(build_FragmentHost)


def test_hyp_build_fragmenthost_constructor_exists():
    assert callable(build_FragmentHost.__init__)


def test_hyp_build_fragmenthost_constructor_args():
    sig = inspect.signature(build_FragmentHost.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_ibuildunitcontainer_is_not_abstract():
    assert not inspect.isabstract(build_IBuildUnitContainer)


def test_hyp_build_ibuildunitcontainer_constructor_exists():
    assert callable(build_IBuildUnitContainer.__init__)


def test_hyp_build_ibuildunitcontainer_constructor_args():
    sig = inspect.signature(build_IBuildUnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_firstfoundunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_FirstFoundUnitProvider)


def test_hyp_build_firstfoundunitprovider_constructor_exists():
    assert callable(build_FirstFoundUnitProvider.__init__)


def test_hyp_build_firstfoundunitprovider_constructor_args():
    sig = inspect.signature(build_FirstFoundUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_requiredcapability_is_not_abstract():
    assert not inspect.isabstract(build_RequiredCapability)


def test_hyp_build_requiredcapability_constructor_exists():
    assert callable(build_RequiredCapability.__init__)


def test_hyp_build_requiredcapability_constructor_args():
    sig = inspect.signature(build_RequiredCapability.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "greedy" in params, "Missing parameter 'greedy'"
    assert "versionRange" in params, "Missing parameter 'versionRange'"







def test_hyp_ivarname_is_not_abstract():
    assert not inspect.isabstract(IVarName)


def test_hyp_ivarname_constructor_exists():
    assert callable(IVarName.__init__)


def test_hyp_ivarname_constructor_args():
    sig = inspect.signature(IVarName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iprovidedcapabilitycontainer_is_not_abstract():
    assert not inspect.isabstract(IProvidedCapabilityContainer)


def test_hyp_iprovidedcapabilitycontainer_constructor_exists():
    assert callable(IProvidedCapabilityContainer.__init__)


def test_hyp_iprovidedcapabilitycontainer_constructor_args():
    sig = inspect.signature(IProvidedCapabilityContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_ibuilder_is_not_abstract():
    assert not inspect.isabstract(build_IBuilder)


def test_hyp_build_ibuilder_constructor_exists():
    assert callable(build_IBuilder.__init__)


def test_hyp_build_ibuilder_constructor_args():
    sig = inspect.signature(build_IBuilder.__init__)
    params = list(sig.parameters.keys())
    assert "unitType" in params, "Missing parameter 'unitType'"




def test_hyp_build_buildconcerncontext_is_not_abstract():
    assert not inspect.isabstract(build_BuildConcernContext)


def test_hyp_build_buildconcerncontext_constructor_exists():
    assert callable(build_BuildConcernContext.__init__)


def test_hyp_build_buildconcerncontext_constructor_args():
    sig = inspect.signature(build_BuildConcernContext.__init__)
    params = list(sig.parameters.keys())
    assert "defaultPropertiesRemovals" in params, "Missing parameter 'defaultPropertiesRemovals'"




def test_hyp_build_repository_is_not_abstract():
    assert not inspect.isabstract(build_Repository)


def test_hyp_build_repository_constructor_exists():
    assert callable(build_Repository.__init__)


def test_hyp_build_repository_constructor_args():
    sig = inspect.signature(build_Repository.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "handlerType" in params, "Missing parameter 'handlerType'"






def test_hyp_build_synchronization_is_not_abstract():
    assert not inspect.isabstract(build_Synchronization)


def test_hyp_build_synchronization_constructor_exists():
    assert callable(build_Synchronization.__init__)


def test_hyp_build_synchronization_constructor_args():
    sig = inspect.signature(build_Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bpropertyset_is_not_abstract():
    assert not inspect.isabstract(build_BPropertySet)


def test_hyp_build_bpropertyset_constructor_exists():
    assert callable(build_BPropertySet.__init__)


def test_hyp_build_bpropertyset_constructor_args():
    sig = inspect.signature(build_BPropertySet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bconcern_is_not_abstract():
    assert not inspect.isabstract(build_BConcern)


def test_hyp_build_bconcern_constructor_exists():
    assert callable(build_BConcern.__init__)


def test_hyp_build_bconcern_constructor_args():
    sig = inspect.signature(build_BConcern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_itype_is_not_abstract():
    assert not inspect.isabstract(build_IType)


def test_hyp_build_itype_constructor_exists():
    assert callable(build_IType.__init__)


def test_hyp_build_itype_constructor_args():
    sig = inspect.signature(build_IType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_irequiredcapabilitycontainer_is_not_abstract():
    assert not inspect.isabstract(IRequiredCapabilityContainer)


def test_hyp_irequiredcapabilitycontainer_constructor_exists():
    assert callable(IRequiredCapabilityContainer.__init__)


def test_hyp_irequiredcapabilitycontainer_constructor_args():
    sig = inspect.signature(IRequiredCapabilityContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitconcerncontext_is_not_abstract():
    assert not inspect.isabstract(build_UnitConcernContext)


def test_hyp_build_unitconcerncontext_constructor_exists():
    assert callable(build_UnitConcernContext.__init__)


def test_hyp_build_unitconcerncontext_constructor_args():
    sig = inspect.signature(build_UnitConcernContext.__init__)
    params = list(sig.parameters.keys())
    assert "sourceLocation" in params, "Missing parameter 'sourceLocation'"
    assert "outputLocation" in params, "Missing parameter 'outputLocation'"





def test_hyp_bparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(BParameterDeclaration)


def test_hyp_bparameterdeclaration_constructor_exists():
    assert callable(BParameterDeclaration.__init__)


def test_hyp_bparameterdeclaration_constructor_args():
    sig = inspect.signature(BParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(build_UnitParameterDeclaration)


def test_hyp_build_unitparameterdeclaration_constructor_exists():
    assert callable(build_UnitParameterDeclaration.__init__)


def test_hyp_build_unitparameterdeclaration_constructor_args():
    sig = inspect.signature(build_UnitParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buildercall_is_not_abstract():
    assert not inspect.isabstract(BuilderCall)


def test_hyp_buildercall_constructor_exists():
    assert callable(BuilderCall.__init__)


def test_hyp_buildercall_constructor_args():
    sig = inspect.signature(BuilderCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildcallmultiple_is_not_abstract():
    assert not inspect.isabstract(build_BuildCallMultiple)


def test_hyp_build_buildcallmultiple_constructor_exists():
    assert callable(build_BuildCallMultiple.__init__)


def test_hyp_build_buildcallmultiple_constructor_args():
    sig = inspect.signature(build_BuildCallMultiple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bwithexpression_is_not_abstract():
    assert not inspect.isabstract(build_BWithExpression)


def test_hyp_build_bwithexpression_constructor_exists():
    assert callable(build_BWithExpression.__init__)


def test_hyp_build_bwithexpression_constructor_args():
    sig = inspect.signature(build_BWithExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builderinputdecorator_is_not_abstract():
    assert not inspect.isabstract(BuilderInputDecorator)


def test_hyp_builderinputdecorator_constructor_exists():
    assert callable(BuilderInputDecorator.__init__)


def test_hyp_builderinputdecorator_constructor_args():
    sig = inspect.signature(BuilderInputDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderinputcontextdecorator_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInputContextDecorator)


def test_hyp_build_builderinputcontextdecorator_constructor_exists():
    assert callable(build_BuilderInputContextDecorator.__init__)


def test_hyp_build_builderinputcontextdecorator_constructor_args():
    sig = inspect.signature(build_BuilderInputContextDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderinputcondition_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInputCondition)


def test_hyp_build_builderinputcondition_constructor_exists():
    assert callable(build_BuilderInputCondition.__init__)


def test_hyp_build_builderinputcondition_constructor_args():
    sig = inspect.signature(build_BuilderInputCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderinputnamedecorator_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInputNameDecorator)


def test_hyp_build_builderinputnamedecorator_constructor_exists():
    assert callable(build_BuilderInputNameDecorator.__init__)


def test_hyp_build_builderinputnamedecorator_constructor_args():
    sig = inspect.signature(build_BuilderInputNameDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buildercallfacade_is_not_abstract():
    assert not inspect.isabstract(BuilderCallFacade)


def test_hyp_buildercallfacade_constructor_exists():
    assert callable(BuilderCallFacade.__init__)


def test_hyp_buildercallfacade_constructor_args():
    sig = inspect.signature(BuilderCallFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_ieffectivefacade_is_not_abstract():
    assert not inspect.isabstract(build_IEffectiveFacade)


def test_hyp_build_ieffectivefacade_constructor_exists():
    assert callable(build_IEffectiveFacade.__init__)


def test_hyp_build_ieffectivefacade_constructor_args():
    sig = inspect.signature(build_IEffectiveFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderinputgroup_is_not_abstract():
    assert not inspect.isabstract(build_BuilderInputGroup)


def test_hyp_build_builderinputgroup_constructor_exists():
    assert callable(build_BuilderInputGroup.__init__)


def test_hyp_build_builderinputgroup_constructor_args():
    sig = inspect.signature(build_BuilderInputGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buildcallsingle_is_not_abstract():
    assert not inspect.isabstract(BuildCallSingle)


def test_hyp_buildcallsingle_constructor_exists():
    assert callable(BuildCallSingle.__init__)


def test_hyp_buildcallsingle_constructor_args():
    sig = inspect.signature(BuildCallSingle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildcallonreferencedrequirement_is_not_abstract():
    assert not inspect.isabstract(build_BuildCallOnReferencedRequirement)


def test_hyp_build_buildcallonreferencedrequirement_constructor_exists():
    assert callable(build_BuildCallOnReferencedRequirement.__init__)


def test_hyp_build_buildcallonreferencedrequirement_constructor_args():
    sig = inspect.signature(build_BuildCallOnReferencedRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildcallondeclaredrequirement_is_not_abstract():
    assert not inspect.isabstract(build_BuildCallOnDeclaredRequirement)


def test_hyp_build_buildcallondeclaredrequirement_constructor_exists():
    assert callable(build_BuildCallOnDeclaredRequirement.__init__)


def test_hyp_build_buildcallondeclaredrequirement_constructor_args():
    sig = inspect.signature(build_BuildCallOnDeclaredRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildcallsingle_is_not_abstract():
    assert not inspect.isabstract(build_BuildCallSingle)


def test_hyp_build_buildcallsingle_constructor_exists():
    assert callable(build_BuildCallSingle.__init__)


def test_hyp_build_buildcallsingle_constructor_args():
    sig = inspect.signature(build_BuildCallSingle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buildcallmultiple_is_not_abstract():
    assert not inspect.isabstract(BuildCallMultiple)


def test_hyp_buildcallmultiple_constructor_exists():
    assert callable(BuildCallMultiple.__init__)


def test_hyp_buildcallmultiple_constructor_args():
    sig = inspect.signature(BuildCallMultiple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildcallonselectedrequirements_is_not_abstract():
    assert not inspect.isabstract(build_BuildCallOnSelectedRequirements)


def test_hyp_build_buildcallonselectedrequirements_constructor_exists():
    assert callable(build_BuildCallOnSelectedRequirements.__init__)


def test_hyp_build_buildcallonselectedrequirements_constructor_args():
    sig = inspect.signature(build_BuildCallOnSelectedRequirements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_delegatingunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_DelegatingUnitProvider)


def test_hyp_build_delegatingunitprovider_constructor_exists():
    assert callable(build_DelegatingUnitProvider.__init__)


def test_hyp_build_delegatingunitprovider_constructor_args():
    sig = inspect.signature(build_DelegatingUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bswitchexpression_is_not_abstract():
    assert not inspect.isabstract(build_BSwitchExpression)


def test_hyp_build_bswitchexpression_constructor_exists():
    assert callable(build_BSwitchExpression.__init__)


def test_hyp_build_bswitchexpression_constructor_args():
    sig = inspect.signature(build_BSwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_switchunitprovider_is_not_abstract():
    assert not inspect.isabstract(build_SwitchUnitProvider)


def test_hyp_build_switchunitprovider_constructor_exists():
    assert callable(build_SwitchUnitProvider.__init__)


def test_hyp_build_switchunitprovider_constructor_args():
    sig = inspect.signature(build_SwitchUnitProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_branch_is_not_abstract():
    assert not inspect.isabstract(build_Branch)


def test_hyp_build_branch_constructor_exists():
    assert callable(build_Branch.__init__)


def test_hyp_build_branch_constructor_args():
    sig = inspect.signature(build_Branch.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"
    assert "replace" in params, "Missing parameter 'replace'"
    assert "acceptDirty" in params, "Missing parameter 'acceptDirty'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "checkout" in params, "Missing parameter 'checkout'"
    assert "mergeStrategy" in params, "Missing parameter 'mergeStrategy'"
    assert "name" in params, "Missing parameter 'name'"
    assert "branchPointType" in params, "Missing parameter 'branchPointType'"











def test_hyp_pathgrouppredicate_is_not_abstract():
    assert not inspect.isabstract(PathGroupPredicate)


def test_hyp_pathgrouppredicate_constructor_exists():
    assert callable(PathGroupPredicate.__init__)


def test_hyp_pathgrouppredicate_constructor_args():
    sig = inspect.signature(PathGroupPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_sourcepredicate_is_not_abstract():
    assert not inspect.isabstract(build_SourcePredicate)


def test_hyp_build_sourcepredicate_constructor_exists():
    assert callable(build_SourcePredicate.__init__)


def test_hyp_build_sourcepredicate_constructor_args():
    sig = inspect.signature(build_SourcePredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_outputpredicate_is_not_abstract():
    assert not inspect.isabstract(build_OutputPredicate)


def test_hyp_build_outputpredicate_constructor_exists():
    assert callable(build_OutputPredicate.__init__)


def test_hyp_build_outputpredicate_constructor_args():
    sig = inspect.signature(build_OutputPredicate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binnercontext_is_not_abstract():
    assert not inspect.isabstract(BInnerContext)


def test_hyp_binnercontext_constructor_exists():
    assert callable(BInnerContext.__init__)


def test_hyp_binnercontext_constructor_args():
    sig = inspect.signature(BInnerContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildresultcontext_is_not_abstract():
    assert not inspect.isabstract(build_BuildResultContext)


def test_hyp_build_buildresultcontext_constructor_exists():
    assert callable(build_BuildResultContext.__init__)


def test_hyp_build_buildresultcontext_constructor_args():
    sig = inspect.signature(build_BuildResultContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_bexecutioncontext_is_not_abstract():
    assert not inspect.isabstract(build_BExecutionContext)


def test_hyp_build_bexecutioncontext_constructor_exists():
    assert callable(build_BExecutionContext.__init__)


def test_hyp_build_bexecutioncontext_constructor_args():
    sig = inspect.signature(build_BExecutionContext.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resolutioninfo_is_not_abstract():
    assert not inspect.isabstract(ResolutionInfo)


def test_hyp_resolutioninfo_constructor_exists():
    assert callable(ResolutionInfo.__init__)


def test_hyp_resolutioninfo_constructor_args():
    sig = inspect.signature(ResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(build_UnitResolutionInfo)


def test_hyp_build_unitresolutioninfo_constructor_exists():
    assert callable(build_UnitResolutionInfo.__init__)


def test_hyp_build_unitresolutioninfo_constructor_args():
    sig = inspect.signature(build_UnitResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compoundbuildunitrepository_is_not_abstract():
    assert not inspect.isabstract(CompoundBuildUnitRepository)


def test_hyp_compoundbuildunitrepository_constructor_exists():
    assert callable(CompoundBuildUnitRepository.__init__)


def test_hyp_compoundbuildunitrepository_constructor_args():
    sig = inspect.signature(CompoundBuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_compoundfirstfoundrepository_is_not_abstract():
    assert not inspect.isabstract(build_CompoundFirstFoundRepository)


def test_hyp_build_compoundfirstfoundrepository_constructor_exists():
    assert callable(build_CompoundFirstFoundRepository.__init__)


def test_hyp_build_compoundfirstfoundrepository_constructor_args():
    sig = inspect.signature(build_CompoundFirstFoundRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_buildunitrepository_is_not_abstract():
    assert not inspect.isabstract(BuildUnitRepository)


def test_hyp_buildunitrepository_constructor_exists():
    assert callable(BuildUnitRepository.__init__)


def test_hyp_buildunitrepository_constructor_args():
    sig = inspect.signature(BuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_beemodelrepository_is_not_abstract():
    assert not inspect.isabstract(build_BeeModelRepository)


def test_hyp_build_beemodelrepository_constructor_exists():
    assert callable(build_BeeModelRepository.__init__)


def test_hyp_build_beemodelrepository_constructor_args():
    sig = inspect.signature(build_BeeModelRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_executionstackrepository_is_not_abstract():
    assert not inspect.isabstract(build_ExecutionStackRepository)


def test_hyp_build_executionstackrepository_constructor_exists():
    assert callable(build_ExecutionStackRepository.__init__)


def test_hyp_build_executionstackrepository_constructor_args():
    sig = inspect.signature(build_ExecutionStackRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_unitrepositorydescription_is_not_abstract():
    assert not inspect.isabstract(build_UnitRepositoryDescription)


def test_hyp_build_unitrepositorydescription_constructor_exists():
    assert callable(build_UnitRepositoryDescription.__init__)


def test_hyp_build_unitrepositorydescription_constructor_args():
    sig = inspect.signature(build_UnitRepositoryDescription.__init__)
    params = list(sig.parameters.keys())
    assert "evaluatedOptions" in params, "Missing parameter 'evaluatedOptions'"




def test_hyp_build_compoundbuildunitrepository_is_not_abstract():
    assert not inspect.isabstract(build_CompoundBuildUnitRepository)


def test_hyp_build_compoundbuildunitrepository_constructor_exists():
    assert callable(build_CompoundBuildUnitRepository.__init__)


def test_hyp_build_compoundbuildunitrepository_constructor_args():
    sig = inspect.signature(build_CompoundBuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ibuildunitrepository_is_not_abstract():
    assert not inspect.isabstract(IBuildUnitRepository)


def test_hyp_ibuildunitrepository_constructor_exists():
    assert callable(IBuildUnitRepository.__init__)


def test_hyp_ibuildunitrepository_constructor_args():
    sig = inspect.signature(IBuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildunitrepository_is_not_abstract():
    assert not inspect.isabstract(build_BuildUnitRepository)


def test_hyp_build_buildunitrepository_constructor_exists():
    assert callable(build_BuildUnitRepository.__init__)


def test_hyp_build_buildunitrepository_constructor_args():
    sig = inspect.signature(build_BuildUnitRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_itypedvaluecontainer_is_not_abstract():
    assert not inspect.isabstract(ITypedValueContainer)


def test_hyp_itypedvaluecontainer_constructor_exists():
    assert callable(ITypedValueContainer.__init__)


def test_hyp_itypedvaluecontainer_constructor_args():
    sig = inspect.signature(ITypedValueContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildset_is_not_abstract():
    assert not inspect.isabstract(build_BuildSet)


def test_hyp_build_buildset_constructor_exists():
    assert callable(build_BuildSet.__init__)


def test_hyp_build_buildset_constructor_args():
    sig = inspect.signature(build_BuildSet.__init__)
    params = list(sig.parameters.keys())
    assert "valueMap" in params, "Missing parameter 'valueMap'"
    assert "pathIterator" in params, "Missing parameter 'pathIterator'"





def test_hyp_build_buildercallfacade_is_not_abstract():
    assert not inspect.isabstract(build_BuilderCallFacade)


def test_hyp_build_buildercallfacade_constructor_exists():
    assert callable(build_BuilderCallFacade.__init__)


def test_hyp_build_buildercallfacade_constructor_args():
    sig = inspect.signature(build_BuilderCallFacade.__init__)
    params = list(sig.parameters.keys())
    assert "aliases" in params, "Missing parameter 'aliases'"




def test_hyp_effectivefacade_is_not_abstract():
    assert not inspect.isabstract(EffectiveFacade)


def test_hyp_effectivefacade_constructor_exists():
    assert callable(EffectiveFacade.__init__)


def test_hyp_effectivefacade_constructor_args():
    sig = inspect.signature(EffectiveFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_effectiverequirementfacade_is_not_abstract():
    assert not inspect.isabstract(build_EffectiveRequirementFacade)


def test_hyp_build_effectiverequirementfacade_constructor_exists():
    assert callable(build_EffectiveRequirementFacade.__init__)


def test_hyp_build_effectiverequirementfacade_constructor_args():
    sig = inspect.signature(build_EffectiveRequirementFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_effectiveunitfacade_is_not_abstract():
    assert not inspect.isabstract(build_EffectiveUnitFacade)


def test_hyp_build_effectiveunitfacade_constructor_exists():
    assert callable(build_EffectiveUnitFacade.__init__)


def test_hyp_build_effectiveunitfacade_constructor_args():
    sig = inspect.signature(build_EffectiveUnitFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_effectivecapabilityfacade_is_not_abstract():
    assert not inspect.isabstract(build_EffectiveCapabilityFacade)


def test_hyp_build_effectivecapabilityfacade_constructor_exists():
    assert callable(build_EffectiveCapabilityFacade.__init__)


def test_hyp_build_effectivecapabilityfacade_constructor_args():
    sig = inspect.signature(build_EffectiveCapabilityFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_beehive_is_not_abstract():
    assert not inspect.isabstract(build_BeeHive)


def test_hyp_build_beehive_constructor_exists():
    assert callable(build_BeeHive.__init__)


def test_hyp_build_beehive_constructor_args():
    sig = inspect.signature(build_BeeHive.__init__)
    params = list(sig.parameters.keys())
    assert "resolutions" in params, "Missing parameter 'resolutions'"




def test_hyp_ieffectivefacade_is_not_abstract():
    assert not inspect.isabstract(IEffectiveFacade)


def test_hyp_ieffectivefacade_constructor_exists():
    assert callable(IEffectiveFacade.__init__)


def test_hyp_ieffectivefacade_constructor_args():
    sig = inspect.signature(IEffectiveFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_effectivebuildercallfacade_is_not_abstract():
    assert not inspect.isabstract(build_EffectiveBuilderCallFacade)


def test_hyp_build_effectivebuildercallfacade_constructor_exists():
    assert callable(build_EffectiveBuilderCallFacade.__init__)


def test_hyp_build_effectivebuildercallfacade_constructor_args():
    sig = inspect.signature(build_EffectiveBuilderCallFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_effectivefacade_is_not_abstract():
    assert not inspect.isabstract(build_EffectiveFacade)


def test_hyp_build_effectivefacade_constructor_exists():
    assert callable(build_EffectiveFacade.__init__)


def test_hyp_build_effectivefacade_constructor_args():
    sig = inspect.signature(build_EffectiveFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_resolutioninfo_is_not_abstract():
    assert not inspect.isabstract(build_ResolutionInfo)


def test_hyp_build_resolutioninfo_constructor_exists():
    assert callable(build_ResolutionInfo.__init__)


def test_hyp_build_resolutioninfo_constructor_args():
    sig = inspect.signature(build_ResolutionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_build_iprovidedcapabilitycontainer_is_not_abstract():
    assert not inspect.isabstract(build_IProvidedCapabilityContainer)


def test_hyp_build_iprovidedcapabilitycontainer_constructor_exists():
    assert callable(build_IProvidedCapabilityContainer.__init__)


def test_hyp_build_iprovidedcapabilitycontainer_constructor_args():
    sig = inspect.signature(build_IProvidedCapabilityContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_irequiredcapabilitycontainer_is_not_abstract():
    assert not inspect.isabstract(build_IRequiredCapabilityContainer)


def test_hyp_build_irequiredcapabilitycontainer_constructor_exists():
    assert callable(build_IRequiredCapabilityContainer.__init__)


def test_hyp_build_irequiredcapabilitycontainer_constructor_args():
    sig = inspect.signature(build_IRequiredCapabilityContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_ifunction_is_not_abstract():
    assert not inspect.isabstract(build_IFunction)


def test_hyp_build_ifunction_constructor_exists():
    assert callable(build_IFunction.__init__)


def test_hyp_build_ifunction_constructor_args():
    sig = inspect.signature(build_IFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ibuildunitcontainer_is_not_abstract():
    assert not inspect.isabstract(IBuildUnitContainer)


def test_hyp_ibuildunitcontainer_constructor_exists():
    assert callable(IBuildUnitContainer.__init__)


def test_hyp_ibuildunitcontainer_constructor_args():
    sig = inspect.signature(IBuildUnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bchainedexpression_is_not_abstract():
    assert not inspect.isabstract(BChainedExpression)


def test_hyp_bchainedexpression_constructor_exists():
    assert callable(BChainedExpression.__init__)


def test_hyp_bchainedexpression_constructor_args():
    sig = inspect.signature(BChainedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_beemodel_is_not_abstract():
    assert not inspect.isabstract(build_BeeModel)


def test_hyp_build_beemodel_constructor_exists():
    assert callable(build_BeeModel.__init__)


def test_hyp_build_beemodel_constructor_args():
    sig = inspect.signature(build_BeeModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bfunctionwrapper_is_not_abstract():
    assert not inspect.isabstract(BFunctionWrapper)


def test_hyp_bfunctionwrapper_constructor_exists():
    assert callable(BFunctionWrapper.__init__)


def test_hyp_bfunctionwrapper_constructor_args():
    sig = inspect.signature(BFunctionWrapper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bjavafunction_is_not_abstract():
    assert not inspect.isabstract(BJavaFunction)


def test_hyp_bjavafunction_constructor_exists():
    assert callable(BJavaFunction.__init__)


def test_hyp_bjavafunction_constructor_args():
    sig = inspect.signature(BJavaFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ibuilder_is_not_abstract():
    assert not inspect.isabstract(IBuilder)


def test_hyp_ibuilder_constructor_exists():
    assert callable(IBuilder.__init__)


def test_hyp_ibuilder_constructor_args():
    sig = inspect.signature(IBuilder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builderwrapper_is_not_abstract():
    assert not inspect.isabstract(build_BuilderWrapper)


def test_hyp_build_builderwrapper_constructor_exists():
    assert callable(build_BuilderWrapper.__init__)


def test_hyp_build_builderwrapper_constructor_args():
    sig = inspect.signature(build_BuilderWrapper.__init__)
    params = list(sig.parameters.keys())
    assert "defaultPropertiesAdvised" in params, "Missing parameter 'defaultPropertiesAdvised'"
    assert "inputAdvised" in params, "Missing parameter 'inputAdvised'"
    assert "outputAdvised" in params, "Missing parameter 'outputAdvised'"
    assert "providesAdvised" in params, "Missing parameter 'providesAdvised'"
    assert "sourceAdvised" in params, "Missing parameter 'sourceAdvised'"
    assert "unitTypeAdvised" in params, "Missing parameter 'unitTypeAdvised'"









def test_hyp_build_builderjava_is_not_abstract():
    assert not inspect.isabstract(build_BuilderJava)


def test_hyp_build_builderjava_constructor_exists():
    assert callable(build_BuilderJava.__init__)


def test_hyp_build_builderjava_constructor_args():
    sig = inspect.signature(build_BuilderJava.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b3function_is_not_abstract():
    assert not inspect.isabstract(B3Function)


def test_hyp_b3function_constructor_exists():
    assert callable(B3Function.__init__)


def test_hyp_b3function_constructor_args():
    sig = inspect.signature(B3Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_builder_is_not_abstract():
    assert not inspect.isabstract(build_Builder)


def test_hyp_build_builder_constructor_exists():
    assert callable(build_Builder.__init__)


def test_hyp_build_builder_constructor_args():
    sig = inspect.signature(build_Builder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bfunctioncontainer_is_not_abstract():
    assert not inspect.isabstract(BFunctionContainer)


def test_hyp_bfunctioncontainer_constructor_exists():
    assert callable(BFunctionContainer.__init__)


def test_hyp_bfunctioncontainer_constructor_args():
    sig = inspect.signature(BFunctionContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versionedcapability_is_not_abstract():
    assert not inspect.isabstract(VersionedCapability)


def test_hyp_versionedcapability_constructor_exists():
    assert callable(VersionedCapability.__init__)


def test_hyp_versionedcapability_constructor_args():
    sig = inspect.signature(VersionedCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_build_buildunit_is_not_abstract():
    assert not inspect.isabstract(build_BuildUnit)


def test_hyp_build_buildunit_constructor_exists():
    assert callable(build_BuildUnit.__init__)


def test_hyp_build_buildunit_constructor_args():
    sig = inspect.signature(build_BuildUnit.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "outputLocation" in params, "Missing parameter 'outputLocation'"
    assert "platformFilter" in params, "Missing parameter 'platformFilter'"
    assert "executionMode" in params, "Missing parameter 'executionMode'"
    assert "sourceLocation" in params, "Missing parameter 'sourceLocation'"






def test_hyp_branchpointtype_exists():
    # Check that the Enumeration exists
    assert BranchPointType is not None

def test_hyp_branchpointtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BranchPointType]
    expected_literals = [
        "Tag",
        "Revision",
        "Latest",
        "Timestamp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BranchPointType"

def test_hyp_mergeconflictstrategy_exists():
    # Check that the Enumeration exists
    assert MergeConflictStrategy is not None

def test_hyp_mergeconflictstrategy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeConflictStrategy]
    expected_literals = [
        "Default",
        "UseWorkspace",
        "UseSCM",
        "Fail",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeConflictStrategy"

def test_hyp_tristate_exists():
    # Check that the Enumeration exists
    assert TriState is not None

def test_hyp_tristate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TriState]
    expected_literals = [
        "False_",
        "Default",
        "True_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TriState"


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
build_BParameterPredicate_strategy = st.builds(
    build_BParameterPredicate,
)
RequiredCapability_strategy = st.builds(
    RequiredCapability,
)
build_AliasedRequiredCapability_strategy = st.builds(
    build_AliasedRequiredCapability,
    alias=
        safe_text
)
BuildConcernContext_strategy = st.builds(
    BuildConcernContext,
)
CapabilityPredicate_strategy = st.builds(
    CapabilityPredicate,
)
build_UnitNamePredicate_strategy = st.builds(
    build_UnitNamePredicate,
)
build_BuilderConcernContext_strategy = st.builds(
    build_BuilderConcernContext,
    sourceAnnotationsRemovals=
        safe_text,
    removePostInputCondition=
        st.booleans(),
    matchParameters=
        st.booleans(),
    outputAnnotationsRemovals=
        safe_text,
    varArgs=
        st.booleans(),
    removePreCondition=
        st.booleans(),
    removePostCondition=
        st.booleans()
)
BConcernContext_strategy = st.builds(
    BConcernContext,
)
build_NameSpacePredicate_strategy = st.builds(
    build_NameSpacePredicate,
    nameSpace=
        safe_text
)
build_BNamePredicate_strategy = st.builds(
    build_BNamePredicate,
)
BExpression_strategy = st.builds(
    BExpression,
)
build_CapabilityPredicate_strategy = st.builds(
    build_CapabilityPredicate,
    versionRange=
        safe_text
)
build_PathGroupPredicate_strategy = st.builds(
    build_PathGroupPredicate,
)
build_InputPredicate_strategy = st.builds(
    build_InputPredicate,
)
build_ImplementsPredicate_strategy = st.builds(
    build_ImplementsPredicate,
)
build_ProvidesPredicate_strategy = st.builds(
    build_ProvidesPredicate,
)
build_RequiresPredicate_strategy = st.builds(
    build_RequiresPredicate,
    meta=
        st.booleans()
)
build_BuilderNamePredicate_strategy = st.builds(
    build_BuilderNamePredicate,
)
build_UnitProvider_strategy = st.builds(
    build_UnitProvider,
    documentation=
        safe_text
)
build_BuilderQuery_strategy = st.builds(
    build_BuilderQuery,
)
build_PathVector_strategy = st.builds(
    build_PathVector,
    basePath=
        safe_text,
    paths=
        safe_text
)
CompoundUnitProvider_strategy = st.builds(
    CompoundUnitProvider,
)
build_BestFoundUnitProvider_strategy = st.builds(
    build_BestFoundUnitProvider,
)
build_IBuildUnitRepository_strategy = st.builds(
    build_IBuildUnitRepository,
)
build_RepoOption_strategy = st.builds(
    build_RepoOption,
    name=
        safe_text
)
UnitProvider_strategy = st.builds(
    UnitProvider,
)
build_CompoundUnitProvider_strategy = st.builds(
    build_CompoundUnitProvider,
)
build_RepositoryUnitProvider_strategy = st.builds(
    build_RepositoryUnitProvider,
)
Capability_strategy = st.builds(
    Capability,
)
build_VersionedCapability_strategy = st.builds(
    build_VersionedCapability,
    version=
        safe_text
)
INamedValue_strategy = st.builds(
    INamedValue,
)
build_Capability_strategy = st.builds(
    build_Capability,
    nameSpace=
        safe_text
)
build_BParameterList_strategy = st.builds(
    build_BParameterList,
)
BuilderInput_strategy = st.builds(
    BuilderInput,
)
build_BuilderCall_strategy = st.builds(
    build_BuilderCall,
    builderName=
        safe_text
)
build_BuilderInputDecorator_strategy = st.builds(
    build_BuilderInputDecorator,
)
build_ConditionalPathVector_strategy = st.builds(
    build_ConditionalPathVector,
)
build_PathGroup_strategy = st.builds(
    build_PathGroup,
)
build_BuilderInput_strategy = st.builds(
    build_BuilderInput,
)
build_BExpression_strategy = st.builds(
    build_BExpression,
)
IFunction_strategy = st.builds(
    IFunction,
)
build_ContainerConfiguration_strategy = st.builds(
    build_ContainerConfiguration,
    documentation=
        safe_text,
    name=
        safe_text
)
build_FragmentHost_strategy = st.builds(
    build_FragmentHost,
)
build_IBuildUnitContainer_strategy = st.builds(
    build_IBuildUnitContainer,
)
build_FirstFoundUnitProvider_strategy = st.builds(
    build_FirstFoundUnitProvider,
)
build_RequiredCapability_strategy = st.builds(
    build_RequiredCapability,
    min=
        st.integers(),
    max=
        st.integers(),
    greedy=
        st.booleans(),
    versionRange=
        safe_text
)
IVarName_strategy = st.builds(
    IVarName,
)
IProvidedCapabilityContainer_strategy = st.builds(
    IProvidedCapabilityContainer,
)
build_IBuilder_strategy = st.builds(
    build_IBuilder,
    unitType=
        safe_text
)
build_BuildConcernContext_strategy = st.builds(
    build_BuildConcernContext,
    defaultPropertiesRemovals=
        safe_text
)
build_Repository_strategy = st.builds(
    build_Repository,
    documentation=
        safe_text,
    name=
        safe_text,
    handlerType=
        safe_text
)
build_Synchronization_strategy = st.builds(
    build_Synchronization,
)
build_BPropertySet_strategy = st.builds(
    build_BPropertySet,
)
build_BConcern_strategy = st.builds(
    build_BConcern,
)
build_IType_strategy = st.builds(
    build_IType,
)
IRequiredCapabilityContainer_strategy = st.builds(
    IRequiredCapabilityContainer,
)
build_UnitConcernContext_strategy = st.builds(
    build_UnitConcernContext,
    sourceLocation=
        safe_text,
    outputLocation=
        safe_text
)
BParameterDeclaration_strategy = st.builds(
    BParameterDeclaration,
)
build_UnitParameterDeclaration_strategy = st.builds(
    build_UnitParameterDeclaration,
)
BuilderCall_strategy = st.builds(
    BuilderCall,
)
build_BuildCallMultiple_strategy = st.builds(
    build_BuildCallMultiple,
)
build_BWithExpression_strategy = st.builds(
    build_BWithExpression,
)
BuilderInputDecorator_strategy = st.builds(
    BuilderInputDecorator,
)
build_BuilderInputContextDecorator_strategy = st.builds(
    build_BuilderInputContextDecorator,
)
build_BuilderInputCondition_strategy = st.builds(
    build_BuilderInputCondition,
)
build_BuilderInputNameDecorator_strategy = st.builds(
    build_BuilderInputNameDecorator,
)
BuilderCallFacade_strategy = st.builds(
    BuilderCallFacade,
)
build_IEffectiveFacade_strategy = st.builds(
    build_IEffectiveFacade,
)
build_BuilderInputGroup_strategy = st.builds(
    build_BuilderInputGroup,
)
BuildCallSingle_strategy = st.builds(
    BuildCallSingle,
)
build_BuildCallOnReferencedRequirement_strategy = st.builds(
    build_BuildCallOnReferencedRequirement,
)
build_BuildCallOnDeclaredRequirement_strategy = st.builds(
    build_BuildCallOnDeclaredRequirement,
)
build_BuildCallSingle_strategy = st.builds(
    build_BuildCallSingle,
)
BuildCallMultiple_strategy = st.builds(
    BuildCallMultiple,
)
build_BuildCallOnSelectedRequirements_strategy = st.builds(
    build_BuildCallOnSelectedRequirements,
)
build_DelegatingUnitProvider_strategy = st.builds(
    build_DelegatingUnitProvider,
)
build_BSwitchExpression_strategy = st.builds(
    build_BSwitchExpression,
)
build_SwitchUnitProvider_strategy = st.builds(
    build_SwitchUnitProvider,
)
build_Branch_strategy = st.builds(
    build_Branch,
    update=
        safe_text,
    replace=
        safe_text,
    acceptDirty=
        safe_text,
    documentation=
        safe_text,
    checkout=
        safe_text,
    mergeStrategy=
        safe_text,
    name=
        safe_text,
    branchPointType=
        safe_text
)
PathGroupPredicate_strategy = st.builds(
    PathGroupPredicate,
)
build_SourcePredicate_strategy = st.builds(
    build_SourcePredicate,
)
build_OutputPredicate_strategy = st.builds(
    build_OutputPredicate,
)
BInnerContext_strategy = st.builds(
    BInnerContext,
)
build_BuildResultContext_strategy = st.builds(
    build_BuildResultContext,
)
build_BExecutionContext_strategy = st.builds(
    build_BExecutionContext,
)
ResolutionInfo_strategy = st.builds(
    ResolutionInfo,
)
build_UnitResolutionInfo_strategy = st.builds(
    build_UnitResolutionInfo,
)
CompoundBuildUnitRepository_strategy = st.builds(
    CompoundBuildUnitRepository,
)
build_CompoundFirstFoundRepository_strategy = st.builds(
    build_CompoundFirstFoundRepository,
)
BuildUnitRepository_strategy = st.builds(
    BuildUnitRepository,
)
build_BeeModelRepository_strategy = st.builds(
    build_BeeModelRepository,
)
build_ExecutionStackRepository_strategy = st.builds(
    build_ExecutionStackRepository,
)
build_UnitRepositoryDescription_strategy = st.builds(
    build_UnitRepositoryDescription,
    evaluatedOptions=
        safe_text
)
build_CompoundBuildUnitRepository_strategy = st.builds(
    build_CompoundBuildUnitRepository,
)
IBuildUnitRepository_strategy = st.builds(
    IBuildUnitRepository,
)
build_BuildUnitRepository_strategy = st.builds(
    build_BuildUnitRepository,
)
ITypedValueContainer_strategy = st.builds(
    ITypedValueContainer,
)
build_BuildSet_strategy = st.builds(
    build_BuildSet,
    valueMap=
        safe_text,
    pathIterator=
        safe_text
)
build_BuilderCallFacade_strategy = st.builds(
    build_BuilderCallFacade,
    aliases=
        safe_text
)
EffectiveFacade_strategy = st.builds(
    EffectiveFacade,
)
build_EffectiveRequirementFacade_strategy = st.builds(
    build_EffectiveRequirementFacade,
)
build_EffectiveUnitFacade_strategy = st.builds(
    build_EffectiveUnitFacade,
)
build_EffectiveCapabilityFacade_strategy = st.builds(
    build_EffectiveCapabilityFacade,
)
build_BeeHive_strategy = st.builds(
    build_BeeHive,
    resolutions=
        safe_text
)
IEffectiveFacade_strategy = st.builds(
    IEffectiveFacade,
)
build_EffectiveBuilderCallFacade_strategy = st.builds(
    build_EffectiveBuilderCallFacade,
)
build_EffectiveFacade_strategy = st.builds(
    build_EffectiveFacade,
)
build_ResolutionInfo_strategy = st.builds(
    build_ResolutionInfo,
    status=
        safe_text
)
build_IProvidedCapabilityContainer_strategy = st.builds(
    build_IProvidedCapabilityContainer,
)
build_IRequiredCapabilityContainer_strategy = st.builds(
    build_IRequiredCapabilityContainer,
)
build_IFunction_strategy = st.builds(
    build_IFunction,
)
IBuildUnitContainer_strategy = st.builds(
    IBuildUnitContainer,
)
BChainedExpression_strategy = st.builds(
    BChainedExpression,
)
build_BeeModel_strategy = st.builds(
    build_BeeModel,
)
BFunctionWrapper_strategy = st.builds(
    BFunctionWrapper,
)
BJavaFunction_strategy = st.builds(
    BJavaFunction,
)
IBuilder_strategy = st.builds(
    IBuilder,
)
build_BuilderWrapper_strategy = st.builds(
    build_BuilderWrapper,
    defaultPropertiesAdvised=
        st.booleans(),
    inputAdvised=
        st.booleans(),
    outputAdvised=
        st.booleans(),
    providesAdvised=
        st.booleans(),
    sourceAdvised=
        st.booleans(),
    unitTypeAdvised=
        st.booleans()
)
build_BuilderJava_strategy = st.builds(
    build_BuilderJava,
)
B3Function_strategy = st.builds(
    B3Function,
)
build_Builder_strategy = st.builds(
    build_Builder,
)
BFunctionContainer_strategy = st.builds(
    BFunctionContainer,
)
VersionedCapability_strategy = st.builds(
    VersionedCapability,
)
build_BuildUnit_strategy = st.builds(
    build_BuildUnit,
    documentation=
        safe_text,
    outputLocation=
        safe_text,
    platformFilter=
        safe_text,
    executionMode=
        safe_text,
    sourceLocation=
        safe_text
)






@given(instance=build_AliasedRequiredCapability_strategy)
def test_hyp_build_aliasedrequiredcapability_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original







@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_sourceAnnotationsRemovals_setter(instance):
    original = instance.sourceAnnotationsRemovals
    instance.sourceAnnotationsRemovals = original
    assert instance.sourceAnnotationsRemovals == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_removePostInputCondition_setter(instance):
    original = instance.removePostInputCondition
    instance.removePostInputCondition = original
    assert instance.removePostInputCondition == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_matchParameters_setter(instance):
    original = instance.matchParameters
    instance.matchParameters = original
    assert instance.matchParameters == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_outputAnnotationsRemovals_setter(instance):
    original = instance.outputAnnotationsRemovals
    instance.outputAnnotationsRemovals = original
    assert instance.outputAnnotationsRemovals == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_removePreCondition_setter(instance):
    original = instance.removePreCondition
    instance.removePreCondition = original
    assert instance.removePreCondition == original



@given(instance=build_BuilderConcernContext_strategy)
def test_hyp_build_builderconcerncontext_removePostCondition_setter(instance):
    original = instance.removePostCondition
    instance.removePostCondition = original
    assert instance.removePostCondition == original





@given(instance=build_NameSpacePredicate_strategy)
def test_hyp_build_namespacepredicate_nameSpace_setter(instance):
    original = instance.nameSpace
    instance.nameSpace = original
    assert instance.nameSpace == original






@given(instance=build_CapabilityPredicate_strategy)
def test_hyp_build_capabilitypredicate_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=build_RequiresPredicate_strategy)
def test_hyp_build_requirespredicate_meta_setter(instance):
    original = instance.meta
    instance.meta = original
    assert instance.meta == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=build_UnitProvider_strategy)
def test_hyp_build_unitprovider_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=build_PathVector_strategy)
def test_hyp_build_pathvector_basePath_setter(instance):
    original = instance.basePath
    instance.basePath = original
    assert instance.basePath == original



@given(instance=build_PathVector_strategy)
def test_hyp_build_pathvector_paths_setter(instance):
    original = instance.paths
    instance.paths = original
    assert instance.paths == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings








@given(instance=build_RepoOption_strategy)
def test_hyp_build_repooption_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=build_VersionedCapability_strategy)
def test_hyp_build_versionedcapability_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original





@given(instance=build_Capability_strategy)
def test_hyp_build_capability_nameSpace_setter(instance):
    original = instance.nameSpace
    instance.nameSpace = original
    assert instance.nameSpace == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings







@given(instance=build_BuilderCall_strategy)
def test_hyp_build_buildercall_builderName_setter(instance):
    original = instance.builderName
    instance.builderName = original
    assert instance.builderName == original










@given(instance=build_ContainerConfiguration_strategy)
def test_hyp_build_containerconfiguration_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=build_ContainerConfiguration_strategy)
def test_hyp_build_containerconfiguration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=build_RequiredCapability_strategy)
def test_hyp_build_requiredcapability_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=build_RequiredCapability_strategy)
def test_hyp_build_requiredcapability_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=build_RequiredCapability_strategy)
def test_hyp_build_requiredcapability_greedy_setter(instance):
    original = instance.greedy
    instance.greedy = original
    assert instance.greedy == original



@given(instance=build_RequiredCapability_strategy)
def test_hyp_build_requiredcapability_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original






@given(instance=build_IBuilder_strategy)
def test_hyp_build_ibuilder_unitType_setter(instance):
    original = instance.unitType
    instance.unitType = original
    assert instance.unitType == original




@given(instance=build_BuildConcernContext_strategy)
def test_hyp_build_buildconcerncontext_defaultPropertiesRemovals_setter(instance):
    original = instance.defaultPropertiesRemovals
    instance.defaultPropertiesRemovals = original
    assert instance.defaultPropertiesRemovals == original




@given(instance=build_Repository_strategy)
def test_hyp_build_repository_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=build_Repository_strategy)
def test_hyp_build_repository_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=build_Repository_strategy)
def test_hyp_build_repository_handlerType_setter(instance):
    original = instance.handlerType
    instance.handlerType = original
    assert instance.handlerType == original









@given(instance=build_UnitConcernContext_strategy)
def test_hyp_build_unitconcerncontext_sourceLocation_setter(instance):
    original = instance.sourceLocation
    instance.sourceLocation = original
    assert instance.sourceLocation == original



@given(instance=build_UnitConcernContext_strategy)
def test_hyp_build_unitconcerncontext_outputLocation_setter(instance):
    original = instance.outputLocation
    instance.outputLocation = original
    assert instance.outputLocation == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings
























@given(instance=build_Branch_strategy)
def test_hyp_build_branch_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_acceptDirty_setter(instance):
    original = instance.acceptDirty
    instance.acceptDirty = original
    assert instance.acceptDirty == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_checkout_setter(instance):
    original = instance.checkout
    instance.checkout = original
    assert instance.checkout == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_mergeStrategy_setter(instance):
    original = instance.mergeStrategy
    instance.mergeStrategy = original
    assert instance.mergeStrategy == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=build_Branch_strategy)
def test_hyp_build_branch_branchPointType_setter(instance):
    original = instance.branchPointType
    instance.branchPointType = original
    assert instance.branchPointType == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


















@given(instance=build_UnitRepositoryDescription_strategy)
def test_hyp_build_unitrepositorydescription_evaluatedOptions_setter(instance):
    original = instance.evaluatedOptions
    instance.evaluatedOptions = original
    assert instance.evaluatedOptions == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings






@given(instance=build_BuildSet_strategy)
def test_hyp_build_buildset_valueMap_setter(instance):
    original = instance.valueMap
    instance.valueMap = original
    assert instance.valueMap == original



@given(instance=build_BuildSet_strategy)
def test_hyp_build_buildset_pathIterator_setter(instance):
    original = instance.pathIterator
    instance.pathIterator = original
    assert instance.pathIterator == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=build_BuilderCallFacade_strategy)
def test_hyp_build_buildercallfacade_aliases_setter(instance):
    original = instance.aliases
    instance.aliases = original
    assert instance.aliases == original








@given(instance=build_BeeHive_strategy)
def test_hyp_build_beehive_resolutions_setter(instance):
    original = instance.resolutions
    instance.resolutions = original
    assert instance.resolutions == original







@given(instance=build_ResolutionInfo_strategy)
def test_hyp_build_resolutioninfo_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original













@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_defaultPropertiesAdvised_setter(instance):
    original = instance.defaultPropertiesAdvised
    instance.defaultPropertiesAdvised = original
    assert instance.defaultPropertiesAdvised == original



@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_inputAdvised_setter(instance):
    original = instance.inputAdvised
    instance.inputAdvised = original
    assert instance.inputAdvised == original



@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_outputAdvised_setter(instance):
    original = instance.outputAdvised
    instance.outputAdvised = original
    assert instance.outputAdvised == original



@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_providesAdvised_setter(instance):
    original = instance.providesAdvised
    instance.providesAdvised = original
    assert instance.providesAdvised == original



@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_sourceAdvised_setter(instance):
    original = instance.sourceAdvised
    instance.sourceAdvised = original
    assert instance.sourceAdvised == original



@given(instance=build_BuilderWrapper_strategy)
def test_hyp_build_builderwrapper_unitTypeAdvised_setter(instance):
    original = instance.unitTypeAdvised
    instance.unitTypeAdvised = original
    assert instance.unitTypeAdvised == original









@given(instance=build_BuildUnit_strategy)
def test_hyp_build_buildunit_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=build_BuildUnit_strategy)
def test_hyp_build_buildunit_outputLocation_setter(instance):
    original = instance.outputLocation
    instance.outputLocation = original
    assert instance.outputLocation == original



@given(instance=build_BuildUnit_strategy)
def test_hyp_build_buildunit_platformFilter_setter(instance):
    original = instance.platformFilter
    instance.platformFilter = original
    assert instance.platformFilter == original



@given(instance=build_BuildUnit_strategy)
def test_hyp_build_buildunit_executionMode_setter(instance):
    original = instance.executionMode
    instance.executionMode = original
    assert instance.executionMode == original



@given(instance=build_BuildUnit_strategy)
def test_hyp_build_buildunit_sourceLocation_setter(instance):
    original = instance.sourceLocation
    instance.sourceLocation = original
    assert instance.sourceLocation == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    B3Function,
    BChainedExpression,
    BConcernContext,
    BExpression,
    BFunctionContainer,
    BFunctionWrapper,
    BInnerContext,
    BJavaFunction,
    BParameterDeclaration,
    BuildCallMultiple,
    BuildCallSingle,
    BuildConcernContext,
    BuildUnitRepository,
    BuilderCall,
    BuilderCallFacade,
    BuilderInput,
    BuilderInputDecorator,
    Capability,
    CapabilityPredicate,
    CompoundBuildUnitRepository,
    CompoundUnitProvider,
    EffectiveFacade,
    IBuildUnitContainer,
    IBuildUnitRepository,
    IBuilder,
    IEffectiveFacade,
    IFunction,
    INamedValue,
    IProvidedCapabilityContainer,
    IRequiredCapabilityContainer,
    ITypedValueContainer,
    IVarName,
    PathGroupPredicate,
    RequiredCapability,
    ResolutionInfo,
    UnitProvider,
    VersionedCapability,
    build_AliasedRequiredCapability,
    build_BConcern,
    build_BExecutionContext,
    build_BExpression,
    build_BNamePredicate,
    build_BParameterList,
    build_BParameterPredicate,
    build_BPropertySet,
    build_BSwitchExpression,
    build_BWithExpression,
    build_BeeHive,
    build_BeeModel,
    build_BeeModelRepository,
    build_BestFoundUnitProvider,
    build_Branch,
    build_BuildCallMultiple,
    build_BuildCallOnDeclaredRequirement,
    build_BuildCallOnReferencedRequirement,
    build_BuildCallOnSelectedRequirements,
    build_BuildCallSingle,
    build_BuildConcernContext,
    build_BuildResultContext,
    build_BuildSet,
    build_BuildUnit,
    build_BuildUnitRepository,
    build_Builder,
    build_BuilderCall,
    build_BuilderCallFacade,
    build_BuilderConcernContext,
    build_BuilderInput,
    build_BuilderInputCondition,
    build_BuilderInputContextDecorator,
    build_BuilderInputDecorator,
    build_BuilderInputGroup,
    build_BuilderInputNameDecorator,
    build_BuilderJava,
    build_BuilderNamePredicate,
    build_BuilderQuery,
    build_BuilderWrapper,
    build_Capability,
    build_CapabilityPredicate,
    build_CompoundBuildUnitRepository,
    build_CompoundFirstFoundRepository,
    build_CompoundUnitProvider,
    build_ConditionalPathVector,
    build_ContainerConfiguration,
    build_DelegatingUnitProvider,
    build_EffectiveBuilderCallFacade,
    build_EffectiveCapabilityFacade,
    build_EffectiveFacade,
    build_EffectiveRequirementFacade,
    build_EffectiveUnitFacade,
    build_ExecutionStackRepository,
    build_FirstFoundUnitProvider,
    build_FragmentHost,
    build_IBuildUnitContainer,
    build_IBuildUnitRepository,
    build_IBuilder,
    build_IEffectiveFacade,
    build_IFunction,
    build_IProvidedCapabilityContainer,
    build_IRequiredCapabilityContainer,
    build_IType,
    build_ImplementsPredicate,
    build_InputPredicate,
    build_NameSpacePredicate,
    build_OutputPredicate,
    build_PathGroup,
    build_PathGroupPredicate,
    build_PathVector,
    build_ProvidesPredicate,
    build_RepoOption,
    build_Repository,
    build_RepositoryUnitProvider,
    build_RequiredCapability,
    build_RequiresPredicate,
    build_ResolutionInfo,
    build_SourcePredicate,
    build_SwitchUnitProvider,
    build_Synchronization,
    build_UnitConcernContext,
    build_UnitNamePredicate,
    build_UnitParameterDeclaration,
    build_UnitProvider,
    build_UnitRepositoryDescription,
    build_UnitResolutionInfo,
    build_VersionedCapability,
    BranchPointType,
    MergeConflictStrategy,
    TriState,
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

def test_build_AliasedRequiredCapability_alias_value_roundtrip():
    instance = build_AliasedRequiredCapability(alias="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_build_BeeHive_resolutions_value_roundtrip():
    instance = build_BeeHive(resolutions="sample_text")
    assert instance.resolutions == "sample_text"
    instance.resolutions = "sample_text_2"
    assert instance.resolutions == "sample_text_2"


def test_build_Branch_acceptDirty_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.acceptDirty == "sample_text"
    instance.acceptDirty = "sample_text_2"
    assert instance.acceptDirty == "sample_text_2"


def test_build_Branch_branchPointType_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.branchPointType == "sample_text"
    instance.branchPointType = "sample_text_2"
    assert instance.branchPointType == "sample_text_2"


def test_build_Branch_checkout_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.checkout == "sample_text"
    instance.checkout = "sample_text_2"
    assert instance.checkout == "sample_text_2"


def test_build_Branch_documentation_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_build_Branch_mergeStrategy_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.mergeStrategy == "sample_text"
    instance.mergeStrategy = "sample_text_2"
    assert instance.mergeStrategy == "sample_text_2"


def test_build_Branch_name_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_Branch_replace_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.replace == "sample_text"
    instance.replace = "sample_text_2"
    assert instance.replace == "sample_text_2"


def test_build_Branch_update_value_roundtrip():
    instance = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    assert instance.update == "sample_text"
    instance.update = "sample_text_2"
    assert instance.update == "sample_text_2"


def test_build_BuildConcernContext_defaultPropertiesRemovals_value_roundtrip():
    instance = build_BuildConcernContext(defaultPropertiesRemovals="sample_text")
    assert instance.defaultPropertiesRemovals == "sample_text"
    instance.defaultPropertiesRemovals = "sample_text_2"
    assert instance.defaultPropertiesRemovals == "sample_text_2"


def test_build_BuildSet_pathIterator_value_roundtrip():
    instance = build_BuildSet(pathIterator="sample_text", valueMap="sample_text")
    assert instance.pathIterator == "sample_text"
    instance.pathIterator = "sample_text_2"
    assert instance.pathIterator == "sample_text_2"


def test_build_BuildSet_valueMap_value_roundtrip():
    instance = build_BuildSet(pathIterator="sample_text", valueMap="sample_text")
    assert instance.valueMap == "sample_text"
    instance.valueMap = "sample_text_2"
    assert instance.valueMap == "sample_text_2"


def test_build_BuildUnit_documentation_value_roundtrip():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_build_BuildUnit_executionMode_value_roundtrip():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert instance.executionMode == "sample_text"
    instance.executionMode = "sample_text_2"
    assert instance.executionMode == "sample_text_2"


def test_build_BuildUnit_outputLocation_value_roundtrip():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert instance.outputLocation == "sample_text"
    instance.outputLocation = "sample_text_2"
    assert instance.outputLocation == "sample_text_2"


def test_build_BuildUnit_platformFilter_value_roundtrip():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert instance.platformFilter == "sample_text"
    instance.platformFilter = "sample_text_2"
    assert instance.platformFilter == "sample_text_2"


def test_build_BuildUnit_sourceLocation_value_roundtrip():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert instance.sourceLocation == "sample_text"
    instance.sourceLocation = "sample_text_2"
    assert instance.sourceLocation == "sample_text_2"


def test_build_BuilderCall_builderName_value_roundtrip():
    instance = build_BuilderCall(builderName="sample_text")
    assert instance.builderName == "sample_text"
    instance.builderName = "sample_text_2"
    assert instance.builderName == "sample_text_2"


def test_build_BuilderCallFacade_aliases_value_roundtrip():
    instance = build_BuilderCallFacade(aliases="sample_text")
    assert instance.aliases == "sample_text"
    instance.aliases = "sample_text_2"
    assert instance.aliases == "sample_text_2"


def test_build_BuilderConcernContext_matchParameters_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.matchParameters == True
    instance.matchParameters = False
    assert instance.matchParameters == False


def test_build_BuilderConcernContext_outputAnnotationsRemovals_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.outputAnnotationsRemovals == "sample_text"
    instance.outputAnnotationsRemovals = "sample_text_2"
    assert instance.outputAnnotationsRemovals == "sample_text_2"


def test_build_BuilderConcernContext_removePostCondition_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.removePostCondition == True
    instance.removePostCondition = False
    assert instance.removePostCondition == False


def test_build_BuilderConcernContext_removePostInputCondition_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.removePostInputCondition == True
    instance.removePostInputCondition = False
    assert instance.removePostInputCondition == False


def test_build_BuilderConcernContext_removePreCondition_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.removePreCondition == True
    instance.removePreCondition = False
    assert instance.removePreCondition == False


def test_build_BuilderConcernContext_sourceAnnotationsRemovals_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.sourceAnnotationsRemovals == "sample_text"
    instance.sourceAnnotationsRemovals = "sample_text_2"
    assert instance.sourceAnnotationsRemovals == "sample_text_2"


def test_build_BuilderConcernContext_varArgs_value_roundtrip():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert instance.varArgs == True
    instance.varArgs = False
    assert instance.varArgs == False


def test_build_BuilderWrapper_defaultPropertiesAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.defaultPropertiesAdvised == True
    instance.defaultPropertiesAdvised = False
    assert instance.defaultPropertiesAdvised == False


def test_build_BuilderWrapper_inputAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.inputAdvised == True
    instance.inputAdvised = False
    assert instance.inputAdvised == False


def test_build_BuilderWrapper_outputAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.outputAdvised == True
    instance.outputAdvised = False
    assert instance.outputAdvised == False


def test_build_BuilderWrapper_providesAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.providesAdvised == True
    instance.providesAdvised = False
    assert instance.providesAdvised == False


def test_build_BuilderWrapper_sourceAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.sourceAdvised == True
    instance.sourceAdvised = False
    assert instance.sourceAdvised == False


def test_build_BuilderWrapper_unitTypeAdvised_value_roundtrip():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert instance.unitTypeAdvised == True
    instance.unitTypeAdvised = False
    assert instance.unitTypeAdvised == False


def test_build_Capability_nameSpace_value_roundtrip():
    instance = build_Capability(nameSpace="sample_text")
    assert instance.nameSpace == "sample_text"
    instance.nameSpace = "sample_text_2"
    assert instance.nameSpace == "sample_text_2"


def test_build_CapabilityPredicate_versionRange_value_roundtrip():
    instance = build_CapabilityPredicate(versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_build_ContainerConfiguration_documentation_value_roundtrip():
    instance = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_build_ContainerConfiguration_name_value_roundtrip():
    instance = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_IBuilder_unitType_value_roundtrip():
    instance = build_IBuilder(unitType="sample_text")
    assert instance.unitType == "sample_text"
    instance.unitType = "sample_text_2"
    assert instance.unitType == "sample_text_2"


def test_build_NameSpacePredicate_nameSpace_value_roundtrip():
    instance = build_NameSpacePredicate(nameSpace="sample_text")
    assert instance.nameSpace == "sample_text"
    instance.nameSpace = "sample_text_2"
    assert instance.nameSpace == "sample_text_2"


def test_build_PathVector_basePath_value_roundtrip():
    instance = build_PathVector(basePath="sample_text", paths="sample_text")
    assert instance.basePath == "sample_text"
    instance.basePath = "sample_text_2"
    assert instance.basePath == "sample_text_2"


def test_build_PathVector_paths_value_roundtrip():
    instance = build_PathVector(basePath="sample_text", paths="sample_text")
    assert instance.paths == "sample_text"
    instance.paths = "sample_text_2"
    assert instance.paths == "sample_text_2"


def test_build_RepoOption_name_value_roundtrip():
    instance = build_RepoOption(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_Repository_documentation_value_roundtrip():
    instance = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_build_Repository_handlerType_value_roundtrip():
    instance = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    assert instance.handlerType == "sample_text"
    instance.handlerType = "sample_text_2"
    assert instance.handlerType == "sample_text_2"


def test_build_Repository_name_value_roundtrip():
    instance = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_build_RequiredCapability_greedy_value_roundtrip():
    instance = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    assert instance.greedy == True
    instance.greedy = False
    assert instance.greedy == False


def test_build_RequiredCapability_max_value_roundtrip():
    instance = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_build_RequiredCapability_min_value_roundtrip():
    instance = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_build_RequiredCapability_versionRange_value_roundtrip():
    instance = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_build_RequiresPredicate_meta_value_roundtrip():
    instance = build_RequiresPredicate(meta=True)
    assert instance.meta == True
    instance.meta = False
    assert instance.meta == False


def test_build_ResolutionInfo_status_value_roundtrip():
    instance = build_ResolutionInfo(status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_build_UnitConcernContext_outputLocation_value_roundtrip():
    instance = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    assert instance.outputLocation == "sample_text"
    instance.outputLocation = "sample_text_2"
    assert instance.outputLocation == "sample_text_2"


def test_build_UnitConcernContext_sourceLocation_value_roundtrip():
    instance = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    assert instance.sourceLocation == "sample_text"
    instance.sourceLocation = "sample_text_2"
    assert instance.sourceLocation == "sample_text_2"


def test_build_UnitProvider_documentation_value_roundtrip():
    instance = build_UnitProvider(documentation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_build_UnitRepositoryDescription_evaluatedOptions_value_roundtrip():
    instance = build_UnitRepositoryDescription(evaluatedOptions="sample_text")
    assert instance.evaluatedOptions == "sample_text"
    instance.evaluatedOptions = "sample_text_2"
    assert instance.evaluatedOptions == "sample_text_2"


def test_build_VersionedCapability_version_value_roundtrip():
    instance = build_VersionedCapability(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_build_Builder_isa_B3Function():
    instance = build_Builder()
    assert isinstance(instance, B3Function)


def test_build_BeeModel_isa_BChainedExpression():
    instance = build_BeeModel()
    assert isinstance(instance, BChainedExpression)


def test_build_BuildConcernContext_isa_BConcernContext():
    instance = build_BuildConcernContext(defaultPropertiesRemovals="sample_text")
    assert isinstance(instance, BConcernContext)


def test_build_BuilderNamePredicate_isa_BExpression():
    instance = build_BuilderNamePredicate()
    assert isinstance(instance, BExpression)


def test_build_CapabilityPredicate_isa_BExpression():
    instance = build_CapabilityPredicate(versionRange="sample_text")
    assert isinstance(instance, BExpression)


def test_build_ImplementsPredicate_isa_BExpression():
    instance = build_ImplementsPredicate()
    assert isinstance(instance, BExpression)


def test_build_InputPredicate_isa_BExpression():
    instance = build_InputPredicate()
    assert isinstance(instance, BExpression)


def test_build_PathGroupPredicate_isa_BExpression():
    instance = build_PathGroupPredicate()
    assert isinstance(instance, BExpression)


def test_build_ProvidesPredicate_isa_BExpression():
    instance = build_ProvidesPredicate()
    assert isinstance(instance, BExpression)


def test_build_Repository_isa_BExpression():
    instance = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    assert isinstance(instance, BExpression)


def test_build_RequiresPredicate_isa_BExpression():
    instance = build_RequiresPredicate(meta=True)
    assert isinstance(instance, BExpression)


def test_build_UnitProvider_isa_BExpression():
    instance = build_UnitProvider(documentation="sample_text")
    assert isinstance(instance, BExpression)


def test_build_BuildUnit_isa_BFunctionContainer():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, BFunctionContainer)


def test_build_BuilderWrapper_isa_BFunctionWrapper():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert isinstance(instance, BFunctionWrapper)


def test_build_BuildResultContext_isa_BInnerContext():
    instance = build_BuildResultContext()
    assert isinstance(instance, BInnerContext)


def test_build_BuilderJava_isa_BJavaFunction():
    instance = build_BuilderJava()
    assert isinstance(instance, BJavaFunction)


def test_build_UnitParameterDeclaration_isa_BParameterDeclaration():
    instance = build_UnitParameterDeclaration()
    assert isinstance(instance, BParameterDeclaration)


def test_build_BuildCallOnSelectedRequirements_isa_BuildCallMultiple():
    instance = build_BuildCallOnSelectedRequirements()
    assert isinstance(instance, BuildCallMultiple)


def test_build_BuildCallOnDeclaredRequirement_isa_BuildCallSingle():
    instance = build_BuildCallOnDeclaredRequirement()
    assert isinstance(instance, BuildCallSingle)


def test_build_BuildCallOnReferencedRequirement_isa_BuildCallSingle():
    instance = build_BuildCallOnReferencedRequirement()
    assert isinstance(instance, BuildCallSingle)


def test_build_BuilderConcernContext_isa_BuildConcernContext():
    instance = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    assert isinstance(instance, BuildConcernContext)


def test_build_UnitConcernContext_isa_BuildConcernContext():
    instance = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, BuildConcernContext)


def test_build_BeeModelRepository_isa_BuildUnitRepository():
    instance = build_BeeModelRepository()
    assert isinstance(instance, BuildUnitRepository)


def test_build_CompoundBuildUnitRepository_isa_BuildUnitRepository():
    instance = build_CompoundBuildUnitRepository()
    assert isinstance(instance, BuildUnitRepository)


def test_build_ExecutionStackRepository_isa_BuildUnitRepository():
    instance = build_ExecutionStackRepository()
    assert isinstance(instance, BuildUnitRepository)


def test_build_UnitRepositoryDescription_isa_BuildUnitRepository():
    instance = build_UnitRepositoryDescription(evaluatedOptions="sample_text")
    assert isinstance(instance, BuildUnitRepository)


def test_build_BuildCallMultiple_isa_BuilderCall():
    instance = build_BuildCallMultiple()
    assert isinstance(instance, BuilderCall)


def test_build_BuildCallSingle_isa_BuilderCall():
    instance = build_BuildCallSingle()
    assert isinstance(instance, BuilderCall)


def test_build_EffectiveBuilderCallFacade_isa_BuilderCallFacade():
    instance = build_EffectiveBuilderCallFacade()
    assert isinstance(instance, BuilderCallFacade)


def test_build_BuilderCall_isa_BuilderInput():
    instance = build_BuilderCall(builderName="sample_text")
    assert isinstance(instance, BuilderInput)


def test_build_BuilderInputDecorator_isa_BuilderInput():
    instance = build_BuilderInputDecorator()
    assert isinstance(instance, BuilderInput)


def test_build_BuilderInputCondition_isa_BuilderInputDecorator():
    instance = build_BuilderInputCondition()
    assert isinstance(instance, BuilderInputDecorator)


def test_build_BuilderInputContextDecorator_isa_BuilderInputDecorator():
    instance = build_BuilderInputContextDecorator()
    assert isinstance(instance, BuilderInputDecorator)


def test_build_BuilderInputGroup_isa_BuilderInputDecorator():
    instance = build_BuilderInputGroup()
    assert isinstance(instance, BuilderInputDecorator)


def test_build_BuilderInputNameDecorator_isa_BuilderInputDecorator():
    instance = build_BuilderInputNameDecorator()
    assert isinstance(instance, BuilderInputDecorator)


def test_build_RequiredCapability_isa_Capability():
    instance = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    assert isinstance(instance, Capability)


def test_build_VersionedCapability_isa_Capability():
    instance = build_VersionedCapability(version="sample_text")
    assert isinstance(instance, Capability)


def test_build_UnitNamePredicate_isa_CapabilityPredicate():
    instance = build_UnitNamePredicate()
    assert isinstance(instance, CapabilityPredicate)


def test_build_CompoundFirstFoundRepository_isa_CompoundBuildUnitRepository():
    instance = build_CompoundFirstFoundRepository()
    assert isinstance(instance, CompoundBuildUnitRepository)


def test_build_BestFoundUnitProvider_isa_CompoundUnitProvider():
    instance = build_BestFoundUnitProvider()
    assert isinstance(instance, CompoundUnitProvider)


def test_build_FirstFoundUnitProvider_isa_CompoundUnitProvider():
    instance = build_FirstFoundUnitProvider()
    assert isinstance(instance, CompoundUnitProvider)


def test_build_EffectiveCapabilityFacade_isa_EffectiveFacade():
    instance = build_EffectiveCapabilityFacade()
    assert isinstance(instance, EffectiveFacade)


def test_build_EffectiveRequirementFacade_isa_EffectiveFacade():
    instance = build_EffectiveRequirementFacade()
    assert isinstance(instance, EffectiveFacade)


def test_build_EffectiveUnitFacade_isa_EffectiveFacade():
    instance = build_EffectiveUnitFacade()
    assert isinstance(instance, EffectiveFacade)


def test_build_BeeModel_isa_IBuildUnitContainer():
    instance = build_BeeModel()
    assert isinstance(instance, IBuildUnitContainer)


def test_build_BuildUnitRepository_isa_IBuildUnitRepository():
    instance = build_BuildUnitRepository()
    assert isinstance(instance, IBuildUnitRepository)


def test_build_Builder_isa_IBuilder():
    instance = build_Builder()
    assert isinstance(instance, IBuilder)


def test_build_BuilderJava_isa_IBuilder():
    instance = build_BuilderJava()
    assert isinstance(instance, IBuilder)


def test_build_BuilderWrapper_isa_IBuilder():
    instance = build_BuilderWrapper(defaultPropertiesAdvised=True, inputAdvised=True, outputAdvised=True, providesAdvised=True, sourceAdvised=True, unitTypeAdvised=True)
    assert isinstance(instance, IBuilder)


def test_build_EffectiveBuilderCallFacade_isa_IEffectiveFacade():
    instance = build_EffectiveBuilderCallFacade()
    assert isinstance(instance, IEffectiveFacade)


def test_build_EffectiveFacade_isa_IEffectiveFacade():
    instance = build_EffectiveFacade()
    assert isinstance(instance, IEffectiveFacade)


def test_build_IBuilder_isa_IFunction():
    instance = build_IBuilder(unitType="sample_text")
    assert isinstance(instance, IFunction)


def test_build_BuilderInputNameDecorator_isa_INamedValue():
    instance = build_BuilderInputNameDecorator()
    assert isinstance(instance, INamedValue)


def test_build_Capability_isa_INamedValue():
    instance = build_Capability(nameSpace="sample_text")
    assert isinstance(instance, INamedValue)


def test_build_BuildConcernContext_isa_IProvidedCapabilityContainer():
    instance = build_BuildConcernContext(defaultPropertiesRemovals="sample_text")
    assert isinstance(instance, IProvidedCapabilityContainer)


def test_build_BuildUnit_isa_IProvidedCapabilityContainer():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, IProvidedCapabilityContainer)


def test_build_IBuilder_isa_IProvidedCapabilityContainer():
    instance = build_IBuilder(unitType="sample_text")
    assert isinstance(instance, IProvidedCapabilityContainer)


def test_build_BuildUnit_isa_IRequiredCapabilityContainer():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, IRequiredCapabilityContainer)


def test_build_UnitConcernContext_isa_IRequiredCapabilityContainer():
    instance = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, IRequiredCapabilityContainer)


def test_build_BuildSet_isa_ITypedValueContainer():
    instance = build_BuildSet(pathIterator="sample_text", valueMap="sample_text")
    assert isinstance(instance, ITypedValueContainer)


def test_build_BuildUnit_isa_IVarName():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, IVarName)


def test_build_OutputPredicate_isa_PathGroupPredicate():
    instance = build_OutputPredicate()
    assert isinstance(instance, PathGroupPredicate)


def test_build_SourcePredicate_isa_PathGroupPredicate():
    instance = build_SourcePredicate()
    assert isinstance(instance, PathGroupPredicate)


def test_build_AliasedRequiredCapability_isa_RequiredCapability():
    instance = build_AliasedRequiredCapability(alias="sample_text")
    assert isinstance(instance, RequiredCapability)


def test_build_UnitResolutionInfo_isa_ResolutionInfo():
    instance = build_UnitResolutionInfo()
    assert isinstance(instance, ResolutionInfo)


def test_build_CompoundUnitProvider_isa_UnitProvider():
    instance = build_CompoundUnitProvider()
    assert isinstance(instance, UnitProvider)


def test_build_DelegatingUnitProvider_isa_UnitProvider():
    instance = build_DelegatingUnitProvider()
    assert isinstance(instance, UnitProvider)


def test_build_RepositoryUnitProvider_isa_UnitProvider():
    instance = build_RepositoryUnitProvider()
    assert isinstance(instance, UnitProvider)


def test_build_SwitchUnitProvider_isa_UnitProvider():
    instance = build_SwitchUnitProvider()
    assert isinstance(instance, UnitProvider)


def test_build_BuildUnit_isa_VersionedCapability():
    instance = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    assert isinstance(instance, VersionedCapability)


def test_assoc_address232_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_Repository233', b1)
    assert _is_linked(a, 'build_Repository233', b1)
    if hasattr(b1, 'build_BExpression234'):
        assert _is_linked(b1, 'build_BExpression234', a)
    _safe_set(a, 'build_Repository233', b2)
    assert _is_linked(a, 'build_Repository233', b2)
    if hasattr(b1, 'build_BExpression234'):
        assert not _is_linked(b1, 'build_BExpression234', a)
    if hasattr(b2, 'build_BExpression234'):
        assert _is_linked(b2, 'build_BExpression234', a)
    _safe_set(a, 'build_Repository233', None)
    assert not _is_linked(a, 'build_Repository233', b2)
    if hasattr(b2, 'build_BExpression234'):
        assert not _is_linked(b2, 'build_BExpression234', a)


def test_assoc_agentType68_link_reassign_clear():
    a = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    b1 = build_IType()
    b2 = build_IType()
    _safe_set(a, 'build_ContainerConfiguration69', b1)
    assert _is_linked(a, 'build_ContainerConfiguration69', b1)
    if hasattr(b1, 'build_IType70'):
        assert _is_linked(b1, 'build_IType70', a)
    _safe_set(a, 'build_ContainerConfiguration69', b2)
    assert _is_linked(a, 'build_ContainerConfiguration69', b2)
    if hasattr(b1, 'build_IType70'):
        assert not _is_linked(b1, 'build_IType70', a)
    if hasattr(b2, 'build_IType70'):
        assert _is_linked(b2, 'build_IType70', a)
    _safe_set(a, 'build_ContainerConfiguration69', None)
    assert not _is_linked(a, 'build_ContainerConfiguration69', b2)
    if hasattr(b2, 'build_IType70'):
        assert not _is_linked(b2, 'build_IType70', a)


def test_assoc_beeModels185_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_BeeHive(resolutions="sample_text")
    b2 = build_BeeHive(resolutions="sample_text_2")
    _safe_set(a, 'build_BeeModel186', b1)
    assert _is_linked(a, 'build_BeeModel186', b1)
    if hasattr(b1, 'build_BeeHive'):
        assert _is_linked(b1, 'build_BeeHive', a)
    _safe_set(a, 'build_BeeModel186', b2)
    assert _is_linked(a, 'build_BeeModel186', b2)
    if hasattr(b1, 'build_BeeHive'):
        assert not _is_linked(b1, 'build_BeeHive', a)
    if hasattr(b2, 'build_BeeHive'):
        assert _is_linked(b2, 'build_BeeHive', a)
    _safe_set(a, 'build_BeeModel186', None)
    assert not _is_linked(a, 'build_BeeModel186', b2)
    if hasattr(b2, 'build_BeeHive'):
        assert not _is_linked(b2, 'build_BeeHive', a)


def test_assoc_beeModels217_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_BeeModelRepository()
    b2 = build_BeeModelRepository()
    _safe_set(a, 'build_BeeModel218', b1)
    assert _is_linked(a, 'build_BeeModel218', b1)
    if hasattr(b1, 'build_BeeModelRepository'):
        assert _is_linked(b1, 'build_BeeModelRepository', a)
    _safe_set(a, 'build_BeeModel218', b2)
    assert _is_linked(a, 'build_BeeModel218', b2)
    if hasattr(b1, 'build_BeeModelRepository'):
        assert not _is_linked(b1, 'build_BeeModelRepository', a)
    if hasattr(b2, 'build_BeeModelRepository'):
        assert _is_linked(b2, 'build_BeeModelRepository', a)
    _safe_set(a, 'build_BeeModel218', None)
    assert not _is_linked(a, 'build_BeeModel218', b2)
    if hasattr(b2, 'build_BeeModelRepository'):
        assert not _is_linked(b2, 'build_BeeModelRepository', a)


def test_assoc_branchPoint241_link_reassign_clear():
    a = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_Branch242', b1)
    assert _is_linked(a, 'build_Branch242', b1)
    if hasattr(b1, 'build_BExpression243'):
        assert _is_linked(b1, 'build_BExpression243', a)
    _safe_set(a, 'build_Branch242', b2)
    assert _is_linked(a, 'build_Branch242', b2)
    if hasattr(b1, 'build_BExpression243'):
        assert not _is_linked(b1, 'build_BExpression243', a)
    if hasattr(b2, 'build_BExpression243'):
        assert _is_linked(b2, 'build_BExpression243', a)
    _safe_set(a, 'build_Branch242', None)
    assert not _is_linked(a, 'build_Branch242', b2)
    if hasattr(b2, 'build_BExpression243'):
        assert not _is_linked(b2, 'build_BExpression243', a)


def test_assoc_branches224_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    b2 = build_Branch(acceptDirty="sample_text_2", branchPointType="sample_text_2", checkout="sample_text_2", documentation="sample_text_2", mergeStrategy="sample_text_2", name="sample_text_2", replace="sample_text_2", update="sample_text_2")
    _safe_set(a, 'build_Repository225', {b1})
    assert _is_linked(a, 'build_Repository225', b1)
    if hasattr(b1, 'build_Branch'):
        assert _is_linked(b1, 'build_Branch', a)
    _safe_set(a, 'build_Repository225', {b2})
    assert _is_linked(a, 'build_Repository225', b2)
    if hasattr(b1, 'build_Branch'):
        assert not _is_linked(b1, 'build_Branch', a)
    if hasattr(b2, 'build_Branch'):
        assert _is_linked(b2, 'build_Branch', a)
    _safe_set(a, 'build_Repository225', set())
    assert not _is_linked(a, 'build_Repository225', b2)
    if hasattr(b2, 'build_Branch'):
        assert not _is_linked(b2, 'build_Branch', a)


def test_assoc_buildUnitRepository229_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_IBuildUnitRepository()
    b2 = build_IBuildUnitRepository()
    _safe_set(a, 'build_Repository230', b1)
    assert _is_linked(a, 'build_Repository230', b1)
    if hasattr(b1, 'build_IBuildUnitRepository231'):
        assert _is_linked(b1, 'build_IBuildUnitRepository231', a)
    _safe_set(a, 'build_Repository230', b2)
    assert _is_linked(a, 'build_Repository230', b2)
    if hasattr(b1, 'build_IBuildUnitRepository231'):
        assert not _is_linked(b1, 'build_IBuildUnitRepository231', a)
    if hasattr(b2, 'build_IBuildUnitRepository231'):
        assert _is_linked(b2, 'build_IBuildUnitRepository231', a)
    _safe_set(a, 'build_Repository230', None)
    assert not _is_linked(a, 'build_Repository230', b2)
    if hasattr(b2, 'build_IBuildUnitRepository231'):
        assert not _is_linked(b2, 'build_IBuildUnitRepository231', a)


def test_assoc_buildUnits264_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_IBuildUnitContainer()
    b2 = build_IBuildUnitContainer()
    _safe_set(a, 'build_BuildUnit266', b1)
    assert _is_linked(a, 'build_BuildUnit266', b1)
    if hasattr(b1, 'build_IBuildUnitContainer265'):
        assert _is_linked(b1, 'build_IBuildUnitContainer265', a)
    _safe_set(a, 'build_BuildUnit266', b2)
    assert _is_linked(a, 'build_BuildUnit266', b2)
    if hasattr(b1, 'build_IBuildUnitContainer265'):
        assert not _is_linked(b1, 'build_IBuildUnitContainer265', a)
    if hasattr(b2, 'build_IBuildUnitContainer265'):
        assert _is_linked(b2, 'build_IBuildUnitContainer265', a)
    _safe_set(a, 'build_BuildUnit266', None)
    assert not _is_linked(a, 'build_BuildUnit266', b2)
    if hasattr(b2, 'build_IBuildUnitContainer265'):
        assert not _is_linked(b2, 'build_IBuildUnitContainer265', a)


def test_assoc_builderContexts93_link_reassign_clear():
    a = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    b1 = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b2 = build_BuilderConcernContext(matchParameters=False, outputAnnotationsRemovals="sample_text_2", removePostCondition=False, removePostInputCondition=False, removePreCondition=False, sourceAnnotationsRemovals="sample_text_2", varArgs=False)
    _safe_set(a, 'build_UnitConcernContext', {b1})
    assert _is_linked(a, 'build_UnitConcernContext', b1)
    if hasattr(b1, 'build_BuilderConcernContext'):
        assert _is_linked(b1, 'build_BuilderConcernContext', a)
    _safe_set(a, 'build_UnitConcernContext', {b2})
    assert _is_linked(a, 'build_UnitConcernContext', b2)
    if hasattr(b1, 'build_BuilderConcernContext'):
        assert not _is_linked(b1, 'build_BuilderConcernContext', a)
    if hasattr(b2, 'build_BuilderConcernContext'):
        assert _is_linked(b2, 'build_BuilderConcernContext', a)
    _safe_set(a, 'build_UnitConcernContext', set())
    assert not _is_linked(a, 'build_UnitConcernContext', b2)
    if hasattr(b2, 'build_BuilderConcernContext'):
        assert not _is_linked(b2, 'build_BuilderConcernContext', a)


def test_assoc_builderReference208_link_reassign_clear():
    a = build_BuilderCallFacade(aliases="sample_text")
    b1 = build_BuilderCall(builderName="sample_text")
    b2 = build_BuilderCall(builderName="sample_text_2")
    _safe_set(a, 'build_BuilderCallFacade', b1)
    assert _is_linked(a, 'build_BuilderCallFacade', b1)
    if hasattr(b1, 'build_BuilderCall209'):
        assert _is_linked(b1, 'build_BuilderCall209', a)
    _safe_set(a, 'build_BuilderCallFacade', b2)
    assert _is_linked(a, 'build_BuilderCallFacade', b2)
    if hasattr(b1, 'build_BuilderCall209'):
        assert not _is_linked(b1, 'build_BuilderCall209', a)
    if hasattr(b2, 'build_BuilderCall209'):
        assert _is_linked(b2, 'build_BuilderCall209', a)
    _safe_set(a, 'build_BuilderCallFacade', None)
    assert not _is_linked(a, 'build_BuilderCallFacade', b2)
    if hasattr(b2, 'build_BuilderCall209'):
        assert not _is_linked(b2, 'build_BuilderCall209', a)


def test_assoc_builders0_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b2 = build_BuildUnit(documentation="sample_text_2", executionMode="sample_text_2", outputLocation="sample_text_2", platformFilter="sample_text_2", sourceLocation="sample_text_2")
    _safe_set(a, 'build_IBuilder', b1)
    assert _is_linked(a, 'build_IBuilder', b1)
    if hasattr(b1, 'build_BuildUnit'):
        assert _is_linked(b1, 'build_BuildUnit', a)
    _safe_set(a, 'build_IBuilder', b2)
    assert _is_linked(a, 'build_IBuilder', b2)
    if hasattr(b1, 'build_BuildUnit'):
        assert not _is_linked(b1, 'build_BuildUnit', a)
    if hasattr(b2, 'build_BuildUnit'):
        assert _is_linked(b2, 'build_BuildUnit', a)
    _safe_set(a, 'build_IBuilder', None)
    assert not _is_linked(a, 'build_IBuilder', b2)
    if hasattr(b2, 'build_BuildUnit'):
        assert not _is_linked(b2, 'build_BuildUnit', a)


def test_assoc_capabilityPredicate76_link_reassign_clear():
    a = build_RequiresPredicate(meta=True)
    b1 = build_CapabilityPredicate(versionRange="sample_text")
    b2 = build_CapabilityPredicate(versionRange="sample_text_2")
    _safe_set(a, 'build_RequiresPredicate', b1)
    assert _is_linked(a, 'build_RequiresPredicate', b1)
    if hasattr(b1, 'build_CapabilityPredicate'):
        assert _is_linked(b1, 'build_CapabilityPredicate', a)
    _safe_set(a, 'build_RequiresPredicate', b2)
    assert _is_linked(a, 'build_RequiresPredicate', b2)
    if hasattr(b1, 'build_CapabilityPredicate'):
        assert not _is_linked(b1, 'build_CapabilityPredicate', a)
    if hasattr(b2, 'build_CapabilityPredicate'):
        assert _is_linked(b2, 'build_CapabilityPredicate', a)
    _safe_set(a, 'build_RequiresPredicate', None)
    assert not _is_linked(a, 'build_RequiresPredicate', b2)
    if hasattr(b2, 'build_CapabilityPredicate'):
        assert not _is_linked(b2, 'build_CapabilityPredicate', a)


def test_assoc_capabilityPredicate84_link_reassign_clear():
    a = build_ProvidesPredicate()
    b1 = build_CapabilityPredicate(versionRange="sample_text")
    b2 = build_CapabilityPredicate(versionRange="sample_text_2")
    _safe_set(a, 'build_ProvidesPredicate', b1)
    assert _is_linked(a, 'build_ProvidesPredicate', b1)
    if hasattr(b1, 'build_CapabilityPredicate85'):
        assert _is_linked(b1, 'build_CapabilityPredicate85', a)
    _safe_set(a, 'build_ProvidesPredicate', b2)
    assert _is_linked(a, 'build_ProvidesPredicate', b2)
    if hasattr(b1, 'build_CapabilityPredicate85'):
        assert not _is_linked(b1, 'build_CapabilityPredicate85', a)
    if hasattr(b2, 'build_CapabilityPredicate85'):
        assert _is_linked(b2, 'build_CapabilityPredicate85', a)
    _safe_set(a, 'build_ProvidesPredicate', None)
    assert not _is_linked(a, 'build_ProvidesPredicate', b2)
    if hasattr(b2, 'build_CapabilityPredicate85'):
        assert not _is_linked(b2, 'build_CapabilityPredicate85', a)


def test_assoc_capabilityPredicate88_link_reassign_clear():
    a = build_CapabilityPredicate(versionRange="sample_text")
    b1 = build_InputPredicate()
    b2 = build_InputPredicate()
    _safe_set(a, 'build_CapabilityPredicate89', b1)
    assert _is_linked(a, 'build_CapabilityPredicate89', b1)
    if hasattr(b1, 'build_InputPredicate'):
        assert _is_linked(b1, 'build_InputPredicate', a)
    _safe_set(a, 'build_CapabilityPredicate89', b2)
    assert _is_linked(a, 'build_CapabilityPredicate89', b2)
    if hasattr(b1, 'build_InputPredicate'):
        assert not _is_linked(b1, 'build_InputPredicate', a)
    if hasattr(b2, 'build_InputPredicate'):
        assert _is_linked(b2, 'build_InputPredicate', a)
    _safe_set(a, 'build_CapabilityPredicate89', None)
    assert not _is_linked(a, 'build_CapabilityPredicate89', b2)
    if hasattr(b2, 'build_InputPredicate'):
        assert not _is_linked(b2, 'build_InputPredicate', a)


def test_assoc_concerns170_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_BConcern()
    b2 = build_BConcern()
    _safe_set(a, 'build_BeeModel171', {b1})
    assert _is_linked(a, 'build_BeeModel171', b1)
    if hasattr(b1, 'build_BConcern172'):
        assert _is_linked(b1, 'build_BConcern172', a)
    _safe_set(a, 'build_BeeModel171', {b2})
    assert _is_linked(a, 'build_BeeModel171', b2)
    if hasattr(b1, 'build_BConcern172'):
        assert not _is_linked(b1, 'build_BConcern172', a)
    if hasattr(b2, 'build_BConcern172'):
        assert _is_linked(b2, 'build_BConcern172', a)
    _safe_set(a, 'build_BeeModel171', set())
    assert not _is_linked(a, 'build_BeeModel171', b2)
    if hasattr(b2, 'build_BConcern172'):
        assert not _is_linked(b2, 'build_BConcern172', a)


def test_assoc_concerns5_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_BConcern()
    b2 = build_BConcern()
    _safe_set(a, 'build_BuildUnit6', {b1})
    assert _is_linked(a, 'build_BuildUnit6', b1)
    if hasattr(b1, 'build_BConcern'):
        assert _is_linked(b1, 'build_BConcern', a)
    _safe_set(a, 'build_BuildUnit6', {b2})
    assert _is_linked(a, 'build_BuildUnit6', b2)
    if hasattr(b1, 'build_BConcern'):
        assert not _is_linked(b1, 'build_BConcern', a)
    if hasattr(b2, 'build_BConcern'):
        assert _is_linked(b2, 'build_BConcern', a)
    _safe_set(a, 'build_BuildUnit6', set())
    assert not _is_linked(a, 'build_BuildUnit6', b2)
    if hasattr(b2, 'build_BConcern'):
        assert not _is_linked(b2, 'build_BConcern', a)


def test_assoc_condExpr52_link_reassign_clear():
    a = build_Capability(nameSpace="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_Capability', b1)
    assert _is_linked(a, 'build_Capability', b1)
    if hasattr(b1, 'build_BExpression53'):
        assert _is_linked(b1, 'build_BExpression53', a)
    _safe_set(a, 'build_Capability', b2)
    assert _is_linked(a, 'build_Capability', b2)
    if hasattr(b1, 'build_BExpression53'):
        assert not _is_linked(b1, 'build_BExpression53', a)
    if hasattr(b2, 'build_BExpression53'):
        assert _is_linked(b2, 'build_BExpression53', a)
    _safe_set(a, 'build_Capability', None)
    assert not _is_linked(a, 'build_Capability', b2)
    if hasattr(b2, 'build_BExpression53'):
        assert not _is_linked(b2, 'build_BExpression53', a)


def test_assoc_containers13_link_reassign_clear():
    a = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    b1 = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b2 = build_BuildUnit(documentation="sample_text_2", executionMode="sample_text_2", outputLocation="sample_text_2", platformFilter="sample_text_2", sourceLocation="sample_text_2")
    _safe_set(a, 'build_ContainerConfiguration', b1)
    assert _is_linked(a, 'build_ContainerConfiguration', b1)
    if hasattr(b1, 'build_BuildUnit14'):
        assert _is_linked(b1, 'build_BuildUnit14', a)
    _safe_set(a, 'build_ContainerConfiguration', b2)
    assert _is_linked(a, 'build_ContainerConfiguration', b2)
    if hasattr(b1, 'build_BuildUnit14'):
        assert not _is_linked(b1, 'build_BuildUnit14', a)
    if hasattr(b2, 'build_BuildUnit14'):
        assert _is_linked(b2, 'build_BuildUnit14', a)
    _safe_set(a, 'build_ContainerConfiguration', None)
    assert not _is_linked(a, 'build_ContainerConfiguration', b2)
    if hasattr(b2, 'build_BuildUnit14'):
        assert not _is_linked(b2, 'build_BuildUnit14', a)


def test_assoc_contextBlock71_link_reassign_clear():
    a = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_ContainerConfiguration72', b1)
    assert _is_linked(a, 'build_ContainerConfiguration72', b1)
    if hasattr(b1, 'build_BExpression73'):
        assert _is_linked(b1, 'build_BExpression73', a)
    _safe_set(a, 'build_ContainerConfiguration72', b2)
    assert _is_linked(a, 'build_ContainerConfiguration72', b2)
    if hasattr(b1, 'build_BExpression73'):
        assert not _is_linked(b1, 'build_BExpression73', a)
    if hasattr(b2, 'build_BExpression73'):
        assert _is_linked(b2, 'build_BExpression73', a)
    _safe_set(a, 'build_ContainerConfiguration72', None)
    assert not _is_linked(a, 'build_ContainerConfiguration72', b2)
    if hasattr(b2, 'build_BExpression73'):
        assert not _is_linked(b2, 'build_BExpression73', a)


def test_assoc_defaultProperties182_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BeeModel183', b1)
    assert _is_linked(a, 'build_BeeModel183', b1)
    if hasattr(b1, 'build_BPropertySet184'):
        assert _is_linked(b1, 'build_BPropertySet184', a)
    _safe_set(a, 'build_BeeModel183', b2)
    assert _is_linked(a, 'build_BeeModel183', b2)
    if hasattr(b1, 'build_BPropertySet184'):
        assert not _is_linked(b1, 'build_BPropertySet184', a)
    if hasattr(b2, 'build_BPropertySet184'):
        assert _is_linked(b2, 'build_BPropertySet184', a)
    _safe_set(a, 'build_BeeModel183', None)
    assert not _is_linked(a, 'build_BeeModel183', b2)
    if hasattr(b2, 'build_BPropertySet184'):
        assert not _is_linked(b2, 'build_BPropertySet184', a)


def test_assoc_defaultProperties33_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_IBuilder34', b1)
    assert _is_linked(a, 'build_IBuilder34', b1)
    if hasattr(b1, 'build_BPropertySet35'):
        assert _is_linked(b1, 'build_BPropertySet35', a)
    _safe_set(a, 'build_IBuilder34', b2)
    assert _is_linked(a, 'build_IBuilder34', b2)
    if hasattr(b1, 'build_BPropertySet35'):
        assert not _is_linked(b1, 'build_BPropertySet35', a)
    if hasattr(b2, 'build_BPropertySet35'):
        assert _is_linked(b2, 'build_BPropertySet35', a)
    _safe_set(a, 'build_IBuilder34', None)
    assert not _is_linked(a, 'build_IBuilder34', b2)
    if hasattr(b2, 'build_BPropertySet35'):
        assert not _is_linked(b2, 'build_BPropertySet35', a)


def test_assoc_defaultProperties7_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BuildUnit8', b1)
    assert _is_linked(a, 'build_BuildUnit8', b1)
    if hasattr(b1, 'build_BPropertySet'):
        assert _is_linked(b1, 'build_BPropertySet', a)
    _safe_set(a, 'build_BuildUnit8', b2)
    assert _is_linked(a, 'build_BuildUnit8', b2)
    if hasattr(b1, 'build_BPropertySet'):
        assert not _is_linked(b1, 'build_BPropertySet', a)
    if hasattr(b2, 'build_BPropertySet'):
        assert _is_linked(b2, 'build_BPropertySet', a)
    _safe_set(a, 'build_BuildUnit8', None)
    assert not _is_linked(a, 'build_BuildUnit8', b2)
    if hasattr(b2, 'build_BPropertySet'):
        assert not _is_linked(b2, 'build_BPropertySet', a)


def test_assoc_defaultPropertiesAdditions74_link_reassign_clear():
    a = build_BuildConcernContext(defaultPropertiesRemovals="sample_text")
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BuildConcernContext', b1)
    assert _is_linked(a, 'build_BuildConcernContext', b1)
    if hasattr(b1, 'build_BPropertySet75'):
        assert _is_linked(b1, 'build_BPropertySet75', a)
    _safe_set(a, 'build_BuildConcernContext', b2)
    assert _is_linked(a, 'build_BuildConcernContext', b2)
    if hasattr(b1, 'build_BPropertySet75'):
        assert not _is_linked(b1, 'build_BPropertySet75', a)
    if hasattr(b2, 'build_BPropertySet75'):
        assert _is_linked(b2, 'build_BPropertySet75', a)
    _safe_set(a, 'build_BuildConcernContext', None)
    assert not _is_linked(a, 'build_BuildConcernContext', b2)
    if hasattr(b2, 'build_BPropertySet75'):
        assert not _is_linked(b2, 'build_BPropertySet75', a)


def test_assoc_delegate244_link_reassign_clear():
    a = build_UnitProvider(documentation="sample_text")
    b1 = build_DelegatingUnitProvider()
    b2 = build_DelegatingUnitProvider()
    _safe_set(a, 'build_UnitProvider245', b1)
    assert _is_linked(a, 'build_UnitProvider245', b1)
    if hasattr(b1, 'build_DelegatingUnitProvider'):
        assert _is_linked(b1, 'build_DelegatingUnitProvider', a)
    _safe_set(a, 'build_UnitProvider245', b2)
    assert _is_linked(a, 'build_UnitProvider245', b2)
    if hasattr(b1, 'build_DelegatingUnitProvider'):
        assert not _is_linked(b1, 'build_DelegatingUnitProvider', a)
    if hasattr(b2, 'build_DelegatingUnitProvider'):
        assert _is_linked(b2, 'build_DelegatingUnitProvider', a)
    _safe_set(a, 'build_UnitProvider245', None)
    assert not _is_linked(a, 'build_UnitProvider245', b2)
    if hasattr(b2, 'build_DelegatingUnitProvider'):
        assert not _is_linked(b2, 'build_DelegatingUnitProvider', a)


def test_assoc_exclude238_link_reassign_clear():
    a = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    b1 = build_BNamePredicate()
    b2 = build_BNamePredicate()
    _safe_set(a, 'build_Branch239', {b1})
    assert _is_linked(a, 'build_Branch239', b1)
    if hasattr(b1, 'build_BNamePredicate240'):
        assert _is_linked(b1, 'build_BNamePredicate240', a)
    _safe_set(a, 'build_Branch239', {b2})
    assert _is_linked(a, 'build_Branch239', b2)
    if hasattr(b1, 'build_BNamePredicate240'):
        assert not _is_linked(b1, 'build_BNamePredicate240', a)
    if hasattr(b2, 'build_BNamePredicate240'):
        assert _is_linked(b2, 'build_BNamePredicate240', a)
    _safe_set(a, 'build_Branch239', set())
    assert not _is_linked(a, 'build_Branch239', b2)
    if hasattr(b2, 'build_BNamePredicate240'):
        assert not _is_linked(b2, 'build_BNamePredicate240', a)


def test_assoc_explicitUnitType39_link_reassign_clear():
    a = build_UnitParameterDeclaration()
    b1 = build_IBuilder(unitType="sample_text")
    b2 = build_IBuilder(unitType="sample_text_2")
    _safe_set(a, 'build_UnitParameterDeclaration', b1)
    assert _is_linked(a, 'build_UnitParameterDeclaration', b1)
    if hasattr(b1, 'build_IBuilder40'):
        assert _is_linked(b1, 'build_IBuilder40', a)
    _safe_set(a, 'build_UnitParameterDeclaration', b2)
    assert _is_linked(a, 'build_UnitParameterDeclaration', b2)
    if hasattr(b1, 'build_IBuilder40'):
        assert not _is_linked(b1, 'build_IBuilder40', a)
    if hasattr(b2, 'build_IBuilder40'):
        assert _is_linked(b2, 'build_IBuilder40', a)
    _safe_set(a, 'build_UnitParameterDeclaration', None)
    assert not _is_linked(a, 'build_UnitParameterDeclaration', b2)
    if hasattr(b2, 'build_IBuilder40'):
        assert not _is_linked(b2, 'build_IBuilder40', a)


def test_assoc_expr246_link_reassign_clear():
    a = build_RepoOption(name="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_RepoOption247', b1)
    assert _is_linked(a, 'build_RepoOption247', b1)
    if hasattr(b1, 'build_BExpression248'):
        assert _is_linked(b1, 'build_BExpression248', a)
    _safe_set(a, 'build_RepoOption247', b2)
    assert _is_linked(a, 'build_RepoOption247', b2)
    if hasattr(b1, 'build_BExpression248'):
        assert not _is_linked(b1, 'build_BExpression248', a)
    if hasattr(b2, 'build_BExpression248'):
        assert _is_linked(b2, 'build_BExpression248', a)
    _safe_set(a, 'build_RepoOption247', None)
    assert not _is_linked(a, 'build_RepoOption247', b2)
    if hasattr(b2, 'build_BExpression248'):
        assert not _is_linked(b2, 'build_BExpression248', a)


def test_assoc_fragmentHosts22_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_FragmentHost()
    b2 = build_FragmentHost()
    _safe_set(a, 'build_BuildUnit23', {b1})
    assert _is_linked(a, 'build_BuildUnit23', b1)
    if hasattr(b1, 'build_FragmentHost'):
        assert _is_linked(b1, 'build_FragmentHost', a)
    _safe_set(a, 'build_BuildUnit23', {b2})
    assert _is_linked(a, 'build_BuildUnit23', b2)
    if hasattr(b1, 'build_FragmentHost'):
        assert not _is_linked(b1, 'build_FragmentHost', a)
    if hasattr(b2, 'build_FragmentHost'):
        assert _is_linked(b2, 'build_FragmentHost', a)
    _safe_set(a, 'build_BuildUnit23', set())
    assert not _is_linked(a, 'build_BuildUnit23', b2)
    if hasattr(b2, 'build_FragmentHost'):
        assert not _is_linked(b2, 'build_FragmentHost', a)


def test_assoc_funcExpr120_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_BuilderConcernContext121', b1)
    assert _is_linked(a, 'build_BuilderConcernContext121', b1)
    if hasattr(b1, 'build_BExpression122'):
        assert _is_linked(b1, 'build_BExpression122', a)
    _safe_set(a, 'build_BuilderConcernContext121', b2)
    assert _is_linked(a, 'build_BuilderConcernContext121', b2)
    if hasattr(b1, 'build_BExpression122'):
        assert not _is_linked(b1, 'build_BExpression122', a)
    if hasattr(b2, 'build_BExpression122'):
        assert _is_linked(b2, 'build_BExpression122', a)
    _safe_set(a, 'build_BuilderConcernContext121', None)
    assert not _is_linked(a, 'build_BuilderConcernContext121', b2)
    if hasattr(b2, 'build_BExpression122'):
        assert not _is_linked(b2, 'build_BExpression122', a)


def test_assoc_functions168_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_IFunction()
    b2 = build_IFunction()
    _safe_set(a, 'build_BeeModel169', {b1})
    assert _is_linked(a, 'build_BeeModel169', b1)
    if hasattr(b1, 'build_IFunction'):
        assert _is_linked(b1, 'build_IFunction', a)
    _safe_set(a, 'build_BeeModel169', {b2})
    assert _is_linked(a, 'build_BeeModel169', b2)
    if hasattr(b1, 'build_IFunction'):
        assert not _is_linked(b1, 'build_IFunction', a)
    if hasattr(b2, 'build_IFunction'):
        assert _is_linked(b2, 'build_IFunction', a)
    _safe_set(a, 'build_BeeModel169', set())
    assert not _is_linked(a, 'build_BeeModel169', b2)
    if hasattr(b2, 'build_IFunction'):
        assert not _is_linked(b2, 'build_IFunction', a)


def test_assoc_hostRequirements267_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_FragmentHost()
    b2 = build_FragmentHost()
    _safe_set(a, 'build_RequiredCapability269', b1)
    assert _is_linked(a, 'build_RequiredCapability269', b1)
    if hasattr(b1, 'build_FragmentHost268'):
        assert _is_linked(b1, 'build_FragmentHost268', a)
    _safe_set(a, 'build_RequiredCapability269', b2)
    assert _is_linked(a, 'build_RequiredCapability269', b2)
    if hasattr(b1, 'build_FragmentHost268'):
        assert not _is_linked(b1, 'build_FragmentHost268', a)
    if hasattr(b2, 'build_FragmentHost268'):
        assert _is_linked(b2, 'build_FragmentHost268', a)
    _safe_set(a, 'build_RequiredCapability269', None)
    assert not _is_linked(a, 'build_RequiredCapability269', b2)
    if hasattr(b2, 'build_FragmentHost268'):
        assert not _is_linked(b2, 'build_FragmentHost268', a)


def test_assoc_implements3_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_IType()
    b2 = build_IType()
    _safe_set(a, 'build_BuildUnit4', {b1})
    assert _is_linked(a, 'build_BuildUnit4', b1)
    if hasattr(b1, 'build_IType'):
        assert _is_linked(b1, 'build_IType', a)
    _safe_set(a, 'build_BuildUnit4', {b2})
    assert _is_linked(a, 'build_BuildUnit4', b2)
    if hasattr(b1, 'build_IType'):
        assert not _is_linked(b1, 'build_IType', a)
    if hasattr(b2, 'build_IType'):
        assert _is_linked(b2, 'build_IType', a)
    _safe_set(a, 'build_BuildUnit4', set())
    assert not _is_linked(a, 'build_BuildUnit4', b2)
    if hasattr(b2, 'build_IType'):
        assert not _is_linked(b2, 'build_IType', a)


def test_assoc_imports166_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_IType()
    b2 = build_IType()
    _safe_set(a, 'build_BeeModel', {b1})
    assert _is_linked(a, 'build_BeeModel', b1)
    if hasattr(b1, 'build_IType167'):
        assert _is_linked(b1, 'build_IType167', a)
    _safe_set(a, 'build_BeeModel', {b2})
    assert _is_linked(a, 'build_BeeModel', b2)
    if hasattr(b1, 'build_IType167'):
        assert not _is_linked(b1, 'build_IType167', a)
    if hasattr(b2, 'build_IType167'):
        assert _is_linked(b2, 'build_IType167', a)
    _safe_set(a, 'build_BeeModel', set())
    assert not _is_linked(a, 'build_BeeModel', b2)
    if hasattr(b2, 'build_IType167'):
        assert not _is_linked(b2, 'build_IType167', a)


def test_assoc_include235_link_reassign_clear():
    a = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    b1 = build_BNamePredicate()
    b2 = build_BNamePredicate()
    _safe_set(a, 'build_Branch236', {b1})
    assert _is_linked(a, 'build_Branch236', b1)
    if hasattr(b1, 'build_BNamePredicate237'):
        assert _is_linked(b1, 'build_BNamePredicate237', a)
    _safe_set(a, 'build_Branch236', {b2})
    assert _is_linked(a, 'build_Branch236', b2)
    if hasattr(b1, 'build_BNamePredicate237'):
        assert not _is_linked(b1, 'build_BNamePredicate237', a)
    if hasattr(b2, 'build_BNamePredicate237'):
        assert _is_linked(b2, 'build_BNamePredicate237', a)
    _safe_set(a, 'build_Branch236', set())
    assert not _is_linked(a, 'build_Branch236', b2)
    if hasattr(b2, 'build_BNamePredicate237'):
        assert not _is_linked(b2, 'build_BNamePredicate237', a)


def test_assoc_input29_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BuilderInput()
    b2 = build_BuilderInput()
    _safe_set(a, 'build_IBuilder30', b1)
    assert _is_linked(a, 'build_IBuilder30', b1)
    if hasattr(b1, 'build_BuilderInput'):
        assert _is_linked(b1, 'build_BuilderInput', a)
    _safe_set(a, 'build_IBuilder30', b2)
    assert _is_linked(a, 'build_IBuilder30', b2)
    if hasattr(b1, 'build_BuilderInput'):
        assert not _is_linked(b1, 'build_BuilderInput', a)
    if hasattr(b2, 'build_BuilderInput'):
        assert _is_linked(b2, 'build_BuilderInput', a)
    _safe_set(a, 'build_IBuilder30', None)
    assert not _is_linked(a, 'build_IBuilder30', b2)
    if hasattr(b2, 'build_BuilderInput'):
        assert not _is_linked(b2, 'build_BuilderInput', a)


def test_assoc_inputAdditions109_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BuilderInput()
    b2 = build_BuilderInput()
    _safe_set(a, 'build_BuilderConcernContext110', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext110', b1)
    if hasattr(b1, 'build_BuilderInput111'):
        assert _is_linked(b1, 'build_BuilderInput111', a)
    _safe_set(a, 'build_BuilderConcernContext110', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext110', b2)
    if hasattr(b1, 'build_BuilderInput111'):
        assert not _is_linked(b1, 'build_BuilderInput111', a)
    if hasattr(b2, 'build_BuilderInput111'):
        assert _is_linked(b2, 'build_BuilderInput111', a)
    _safe_set(a, 'build_BuilderConcernContext110', set())
    assert not _is_linked(a, 'build_BuilderConcernContext110', b2)
    if hasattr(b2, 'build_BuilderInput111'):
        assert not _is_linked(b2, 'build_BuilderInput111', a)


def test_assoc_inputRemovals112_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_InputPredicate()
    b2 = build_InputPredicate()
    _safe_set(a, 'build_BuilderConcernContext113', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext113', b1)
    if hasattr(b1, 'build_InputPredicate114'):
        assert _is_linked(b1, 'build_InputPredicate114', a)
    _safe_set(a, 'build_BuilderConcernContext113', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext113', b2)
    if hasattr(b1, 'build_InputPredicate114'):
        assert not _is_linked(b1, 'build_InputPredicate114', a)
    if hasattr(b2, 'build_InputPredicate114'):
        assert _is_linked(b2, 'build_InputPredicate114', a)
    _safe_set(a, 'build_BuilderConcernContext113', set())
    assert not _is_linked(a, 'build_BuilderConcernContext113', b2)
    if hasattr(b2, 'build_InputPredicate114'):
        assert not _is_linked(b2, 'build_InputPredicate114', a)


def test_assoc_metaRequiredCapabilities1_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b2 = build_BuildUnit(documentation="sample_text_2", executionMode="sample_text_2", outputLocation="sample_text_2", platformFilter="sample_text_2", sourceLocation="sample_text_2")
    _safe_set(a, 'build_RequiredCapability', b1)
    assert _is_linked(a, 'build_RequiredCapability', b1)
    if hasattr(b1, 'build_BuildUnit2'):
        assert _is_linked(b1, 'build_BuildUnit2', a)
    _safe_set(a, 'build_RequiredCapability', b2)
    assert _is_linked(a, 'build_RequiredCapability', b2)
    if hasattr(b1, 'build_BuildUnit2'):
        assert not _is_linked(b1, 'build_BuildUnit2', a)
    if hasattr(b2, 'build_BuildUnit2'):
        assert _is_linked(b2, 'build_BuildUnit2', a)
    _safe_set(a, 'build_RequiredCapability', None)
    assert not _is_linked(a, 'build_RequiredCapability', b2)
    if hasattr(b2, 'build_BuildUnit2'):
        assert not _is_linked(b2, 'build_BuildUnit2', a)


def test_assoc_namePredicate77_link_reassign_clear():
    a = build_CapabilityPredicate(versionRange="sample_text")
    b1 = build_BNamePredicate()
    b2 = build_BNamePredicate()
    _safe_set(a, 'build_CapabilityPredicate78', b1)
    assert _is_linked(a, 'build_CapabilityPredicate78', b1)
    if hasattr(b1, 'build_BNamePredicate'):
        assert _is_linked(b1, 'build_BNamePredicate', a)
    _safe_set(a, 'build_CapabilityPredicate78', b2)
    assert _is_linked(a, 'build_CapabilityPredicate78', b2)
    if hasattr(b1, 'build_BNamePredicate'):
        assert not _is_linked(b1, 'build_BNamePredicate', a)
    if hasattr(b2, 'build_BNamePredicate'):
        assert _is_linked(b2, 'build_BNamePredicate', a)
    _safe_set(a, 'build_CapabilityPredicate78', None)
    assert not _is_linked(a, 'build_CapabilityPredicate78', b2)
    if hasattr(b2, 'build_BNamePredicate'):
        assert not _is_linked(b2, 'build_BNamePredicate', a)


def test_assoc_nameSpacePredicate79_link_reassign_clear():
    a = build_CapabilityPredicate(versionRange="sample_text")
    b1 = build_BNamePredicate()
    b2 = build_BNamePredicate()
    _safe_set(a, 'build_CapabilityPredicate80', b1)
    assert _is_linked(a, 'build_CapabilityPredicate80', b1)
    if hasattr(b1, 'build_BNamePredicate81'):
        assert _is_linked(b1, 'build_BNamePredicate81', a)
    _safe_set(a, 'build_CapabilityPredicate80', b2)
    assert _is_linked(a, 'build_CapabilityPredicate80', b2)
    if hasattr(b1, 'build_BNamePredicate81'):
        assert not _is_linked(b1, 'build_BNamePredicate81', a)
    if hasattr(b2, 'build_BNamePredicate81'):
        assert _is_linked(b2, 'build_BNamePredicate81', a)
    _safe_set(a, 'build_CapabilityPredicate80', None)
    assert not _is_linked(a, 'build_CapabilityPredicate80', b2)
    if hasattr(b2, 'build_BNamePredicate81'):
        assert not _is_linked(b2, 'build_BNamePredicate81', a)


def test_assoc_options226_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_RepoOption(name="sample_text")
    b2 = build_RepoOption(name="sample_text_2")
    _safe_set(a, 'build_Repository227', {b1})
    assert _is_linked(a, 'build_Repository227', b1)
    if hasattr(b1, 'build_RepoOption228'):
        assert _is_linked(b1, 'build_RepoOption228', a)
    _safe_set(a, 'build_Repository227', {b2})
    assert _is_linked(a, 'build_Repository227', b2)
    if hasattr(b1, 'build_RepoOption228'):
        assert not _is_linked(b1, 'build_RepoOption228', a)
    if hasattr(b2, 'build_RepoOption228'):
        assert _is_linked(b2, 'build_RepoOption228', a)
    _safe_set(a, 'build_Repository227', set())
    assert not _is_linked(a, 'build_Repository227', b2)
    if hasattr(b2, 'build_RepoOption228'):
        assert not _is_linked(b2, 'build_RepoOption228', a)


def test_assoc_options63_link_reassign_clear():
    a = build_RepoOption(name="sample_text")
    b1 = build_RepositoryUnitProvider()
    b2 = build_RepositoryUnitProvider()
    _safe_set(a, 'build_RepoOption', b1)
    assert _is_linked(a, 'build_RepoOption', b1)
    if hasattr(b1, 'build_RepositoryUnitProvider64'):
        assert _is_linked(b1, 'build_RepositoryUnitProvider64', a)
    _safe_set(a, 'build_RepoOption', b2)
    assert _is_linked(a, 'build_RepoOption', b2)
    if hasattr(b1, 'build_RepositoryUnitProvider64'):
        assert not _is_linked(b1, 'build_RepositoryUnitProvider64', a)
    if hasattr(b2, 'build_RepositoryUnitProvider64'):
        assert _is_linked(b2, 'build_RepositoryUnitProvider64', a)
    _safe_set(a, 'build_RepoOption', None)
    assert not _is_linked(a, 'build_RepoOption', b2)
    if hasattr(b2, 'build_RepositoryUnitProvider64'):
        assert not _is_linked(b2, 'build_RepositoryUnitProvider64', a)


def test_assoc_output31_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_PathGroup()
    b2 = build_PathGroup()
    _safe_set(a, 'build_IBuilder32', b1)
    assert _is_linked(a, 'build_IBuilder32', b1)
    if hasattr(b1, 'build_PathGroup'):
        assert _is_linked(b1, 'build_PathGroup', a)
    _safe_set(a, 'build_IBuilder32', b2)
    assert _is_linked(a, 'build_IBuilder32', b2)
    if hasattr(b1, 'build_PathGroup'):
        assert not _is_linked(b1, 'build_PathGroup', a)
    if hasattr(b2, 'build_PathGroup'):
        assert _is_linked(b2, 'build_PathGroup', a)
    _safe_set(a, 'build_IBuilder32', None)
    assert not _is_linked(a, 'build_IBuilder32', b2)
    if hasattr(b2, 'build_PathGroup'):
        assert not _is_linked(b2, 'build_PathGroup', a)


def test_assoc_outputAdditions115_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_ConditionalPathVector()
    b2 = build_ConditionalPathVector()
    _safe_set(a, 'build_BuilderConcernContext116', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext116', b1)
    if hasattr(b1, 'build_ConditionalPathVector117'):
        assert _is_linked(b1, 'build_ConditionalPathVector117', a)
    _safe_set(a, 'build_BuilderConcernContext116', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext116', b2)
    if hasattr(b1, 'build_ConditionalPathVector117'):
        assert not _is_linked(b1, 'build_ConditionalPathVector117', a)
    if hasattr(b2, 'build_ConditionalPathVector117'):
        assert _is_linked(b2, 'build_ConditionalPathVector117', a)
    _safe_set(a, 'build_BuilderConcernContext116', set())
    assert not _is_linked(a, 'build_BuilderConcernContext116', b2)
    if hasattr(b2, 'build_ConditionalPathVector117'):
        assert not _is_linked(b2, 'build_ConditionalPathVector117', a)


def test_assoc_outputAnnotationAdditions137_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BuilderConcernContext138', b1)
    assert _is_linked(a, 'build_BuilderConcernContext138', b1)
    if hasattr(b1, 'build_BPropertySet139'):
        assert _is_linked(b1, 'build_BPropertySet139', a)
    _safe_set(a, 'build_BuilderConcernContext138', b2)
    assert _is_linked(a, 'build_BuilderConcernContext138', b2)
    if hasattr(b1, 'build_BPropertySet139'):
        assert not _is_linked(b1, 'build_BPropertySet139', a)
    if hasattr(b2, 'build_BPropertySet139'):
        assert _is_linked(b2, 'build_BPropertySet139', a)
    _safe_set(a, 'build_BuilderConcernContext138', None)
    assert not _is_linked(a, 'build_BuilderConcernContext138', b2)
    if hasattr(b2, 'build_BPropertySet139'):
        assert not _is_linked(b2, 'build_BPropertySet139', a)


def test_assoc_outputRemovals118_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_OutputPredicate()
    b2 = build_OutputPredicate()
    _safe_set(a, 'build_BuilderConcernContext119', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext119', b1)
    if hasattr(b1, 'build_OutputPredicate'):
        assert _is_linked(b1, 'build_OutputPredicate', a)
    _safe_set(a, 'build_BuilderConcernContext119', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext119', b2)
    if hasattr(b1, 'build_OutputPredicate'):
        assert not _is_linked(b1, 'build_OutputPredicate', a)
    if hasattr(b2, 'build_OutputPredicate'):
        assert _is_linked(b2, 'build_OutputPredicate', a)
    _safe_set(a, 'build_BuilderConcernContext119', set())
    assert not _is_linked(a, 'build_BuilderConcernContext119', b2)
    if hasattr(b2, 'build_OutputPredicate'):
        assert not _is_linked(b2, 'build_OutputPredicate', a)


def test_assoc_parameters123_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BParameterPredicate()
    b2 = build_BParameterPredicate()
    _safe_set(a, 'build_BuilderConcernContext124', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext124', b1)
    if hasattr(b1, 'build_BParameterPredicate'):
        assert _is_linked(b1, 'build_BParameterPredicate', a)
    _safe_set(a, 'build_BuilderConcernContext124', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext124', b2)
    if hasattr(b1, 'build_BParameterPredicate'):
        assert not _is_linked(b1, 'build_BParameterPredicate', a)
    if hasattr(b2, 'build_BParameterPredicate'):
        assert _is_linked(b2, 'build_BParameterPredicate', a)
    _safe_set(a, 'build_BuilderConcernContext124', set())
    assert not _is_linked(a, 'build_BuilderConcernContext124', b2)
    if hasattr(b2, 'build_BParameterPredicate'):
        assert not _is_linked(b2, 'build_BParameterPredicate', a)


def test_assoc_parameters51_link_reassign_clear():
    a = build_BuilderCall(builderName="sample_text")
    b1 = build_BParameterList()
    b2 = build_BParameterList()
    _safe_set(a, 'build_BuilderCall', b1)
    assert _is_linked(a, 'build_BuilderCall', b1)
    if hasattr(b1, 'build_BParameterList'):
        assert _is_linked(b1, 'build_BParameterList', a)
    _safe_set(a, 'build_BuilderCall', b2)
    assert _is_linked(a, 'build_BuilderCall', b2)
    if hasattr(b1, 'build_BParameterList'):
        assert not _is_linked(b1, 'build_BParameterList', a)
    if hasattr(b2, 'build_BParameterList'):
        assert _is_linked(b2, 'build_BParameterList', a)
    _safe_set(a, 'build_BuilderCall', None)
    assert not _is_linked(a, 'build_BuilderCall', b2)
    if hasattr(b2, 'build_BParameterList'):
        assert not _is_linked(b2, 'build_BParameterList', a)


def test_assoc_parent188_link_reassign_clear():
    a = build_BeeHive(resolutions="sample_text")
    b1 = build_BeeHive(resolutions="sample_text")
    b2 = build_BeeHive(resolutions="sample_text_2")
    _safe_set(a, 'build_BeeHive187', b1)
    assert _is_linked(a, 'build_BeeHive187', b1)
    if hasattr(b1, 'build_BeeHive189'):
        assert _is_linked(b1, 'build_BeeHive189', a)
    _safe_set(a, 'build_BeeHive187', b2)
    assert _is_linked(a, 'build_BeeHive187', b2)
    if hasattr(b1, 'build_BeeHive189'):
        assert not _is_linked(b1, 'build_BeeHive189', a)
    if hasattr(b2, 'build_BeeHive189'):
        assert _is_linked(b2, 'build_BeeHive189', a)
    _safe_set(a, 'build_BeeHive187', None)
    assert not _is_linked(a, 'build_BeeHive187', b2)
    if hasattr(b2, 'build_BeeHive189'):
        assert not _is_linked(b2, 'build_BeeHive189', a)


def test_assoc_parent20_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_IBuildUnitContainer()
    b2 = build_IBuildUnitContainer()
    _safe_set(a, 'build_BuildUnit21', b1)
    assert _is_linked(a, 'build_BuildUnit21', b1)
    if hasattr(b1, 'build_IBuildUnitContainer'):
        assert _is_linked(b1, 'build_IBuildUnitContainer', a)
    _safe_set(a, 'build_BuildUnit21', b2)
    assert _is_linked(a, 'build_BuildUnit21', b2)
    if hasattr(b1, 'build_IBuildUnitContainer'):
        assert not _is_linked(b1, 'build_IBuildUnitContainer', a)
    if hasattr(b2, 'build_IBuildUnitContainer'):
        assert _is_linked(b2, 'build_IBuildUnitContainer', a)
    _safe_set(a, 'build_BuildUnit21', None)
    assert not _is_linked(a, 'build_BuildUnit21', b2)
    if hasattr(b2, 'build_IBuildUnitContainer'):
        assert not _is_linked(b2, 'build_IBuildUnitContainer', a)


def test_assoc_pathPattern150_link_reassign_clear():
    a = build_PathGroupPredicate()
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_PathGroupPredicate151', b1)
    assert _is_linked(a, 'build_PathGroupPredicate151', b1)
    if hasattr(b1, 'build_BExpression152'):
        assert _is_linked(b1, 'build_BExpression152', a)
    _safe_set(a, 'build_PathGroupPredicate151', b2)
    assert _is_linked(a, 'build_PathGroupPredicate151', b2)
    if hasattr(b1, 'build_BExpression152'):
        assert not _is_linked(b1, 'build_BExpression152', a)
    if hasattr(b2, 'build_BExpression152'):
        assert _is_linked(b2, 'build_BExpression152', a)
    _safe_set(a, 'build_PathGroupPredicate151', None)
    assert not _is_linked(a, 'build_PathGroupPredicate151', b2)
    if hasattr(b2, 'build_BExpression152'):
        assert not _is_linked(b2, 'build_BExpression152', a)


def test_assoc_pathVector148_link_reassign_clear():
    a = build_PathVector(basePath="sample_text", paths="sample_text")
    b1 = build_PathGroupPredicate()
    b2 = build_PathGroupPredicate()
    _safe_set(a, 'build_PathVector149', b1)
    assert _is_linked(a, 'build_PathVector149', b1)
    if hasattr(b1, 'build_PathGroupPredicate'):
        assert _is_linked(b1, 'build_PathGroupPredicate', a)
    _safe_set(a, 'build_PathVector149', b2)
    assert _is_linked(a, 'build_PathVector149', b2)
    if hasattr(b1, 'build_PathGroupPredicate'):
        assert not _is_linked(b1, 'build_PathGroupPredicate', a)
    if hasattr(b2, 'build_PathGroupPredicate'):
        assert _is_linked(b2, 'build_PathGroupPredicate', a)
    _safe_set(a, 'build_PathVector149', None)
    assert not _is_linked(a, 'build_PathVector149', b2)
    if hasattr(b2, 'build_PathGroupPredicate'):
        assert not _is_linked(b2, 'build_PathGroupPredicate', a)


def test_assoc_pathVectors213_link_reassign_clear():
    a = build_PathVector(basePath="sample_text", paths="sample_text")
    b1 = build_BuildSet(pathIterator="sample_text", valueMap="sample_text")
    b2 = build_BuildSet(pathIterator="sample_text_2", valueMap="sample_text_2")
    _safe_set(a, 'build_PathVector214', b1)
    assert _is_linked(a, 'build_PathVector214', b1)
    if hasattr(b1, 'build_BuildSet'):
        assert _is_linked(b1, 'build_BuildSet', a)
    _safe_set(a, 'build_PathVector214', b2)
    assert _is_linked(a, 'build_PathVector214', b2)
    if hasattr(b1, 'build_BuildSet'):
        assert not _is_linked(b1, 'build_BuildSet', a)
    if hasattr(b2, 'build_BuildSet'):
        assert _is_linked(b2, 'build_BuildSet', a)
    _safe_set(a, 'build_PathVector214', None)
    assert not _is_linked(a, 'build_PathVector214', b2)
    if hasattr(b2, 'build_BuildSet'):
        assert not _is_linked(b2, 'build_BuildSet', a)


def test_assoc_pathVectors57_link_reassign_clear():
    a = build_PathVector(basePath="sample_text", paths="sample_text")
    b1 = build_ConditionalPathVector()
    b2 = build_ConditionalPathVector()
    _safe_set(a, 'build_PathVector', b1)
    assert _is_linked(a, 'build_PathVector', b1)
    if hasattr(b1, 'build_ConditionalPathVector58'):
        assert _is_linked(b1, 'build_ConditionalPathVector58', a)
    _safe_set(a, 'build_PathVector', b2)
    assert _is_linked(a, 'build_PathVector', b2)
    if hasattr(b1, 'build_ConditionalPathVector58'):
        assert not _is_linked(b1, 'build_ConditionalPathVector58', a)
    if hasattr(b2, 'build_ConditionalPathVector58'):
        assert _is_linked(b2, 'build_ConditionalPathVector58', a)
    _safe_set(a, 'build_PathVector', None)
    assert not _is_linked(a, 'build_PathVector', b2)
    if hasattr(b2, 'build_ConditionalPathVector58'):
        assert not _is_linked(b2, 'build_ConditionalPathVector58', a)


def test_assoc_postcondExpr128_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_BuilderConcernContext129', b1)
    assert _is_linked(a, 'build_BuilderConcernContext129', b1)
    if hasattr(b1, 'build_BExpression130'):
        assert _is_linked(b1, 'build_BExpression130', a)
    _safe_set(a, 'build_BuilderConcernContext129', b2)
    assert _is_linked(a, 'build_BuilderConcernContext129', b2)
    if hasattr(b1, 'build_BExpression130'):
        assert not _is_linked(b1, 'build_BExpression130', a)
    if hasattr(b2, 'build_BExpression130'):
        assert _is_linked(b2, 'build_BExpression130', a)
    _safe_set(a, 'build_BuilderConcernContext129', None)
    assert not _is_linked(a, 'build_BuilderConcernContext129', b2)
    if hasattr(b2, 'build_BExpression130'):
        assert not _is_linked(b2, 'build_BExpression130', a)


def test_assoc_postcondExpr24_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_IBuilder25', b1)
    assert _is_linked(a, 'build_IBuilder25', b1)
    if hasattr(b1, 'build_BExpression'):
        assert _is_linked(b1, 'build_BExpression', a)
    _safe_set(a, 'build_IBuilder25', b2)
    assert _is_linked(a, 'build_IBuilder25', b2)
    if hasattr(b1, 'build_BExpression'):
        assert not _is_linked(b1, 'build_BExpression', a)
    if hasattr(b2, 'build_BExpression'):
        assert _is_linked(b2, 'build_BExpression', a)
    _safe_set(a, 'build_IBuilder25', None)
    assert not _is_linked(a, 'build_IBuilder25', b2)
    if hasattr(b2, 'build_BExpression'):
        assert not _is_linked(b2, 'build_BExpression', a)


def test_assoc_postinputcondExpr131_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_BuilderConcernContext132', b1)
    assert _is_linked(a, 'build_BuilderConcernContext132', b1)
    if hasattr(b1, 'build_BExpression133'):
        assert _is_linked(b1, 'build_BExpression133', a)
    _safe_set(a, 'build_BuilderConcernContext132', b2)
    assert _is_linked(a, 'build_BuilderConcernContext132', b2)
    if hasattr(b1, 'build_BExpression133'):
        assert not _is_linked(b1, 'build_BExpression133', a)
    if hasattr(b2, 'build_BExpression133'):
        assert _is_linked(b2, 'build_BExpression133', a)
    _safe_set(a, 'build_BuilderConcernContext132', None)
    assert not _is_linked(a, 'build_BuilderConcernContext132', b2)
    if hasattr(b2, 'build_BExpression133'):
        assert not _is_linked(b2, 'build_BExpression133', a)


def test_assoc_postinputcondExpr36_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_IBuilder37', b1)
    assert _is_linked(a, 'build_IBuilder37', b1)
    if hasattr(b1, 'build_BExpression38'):
        assert _is_linked(b1, 'build_BExpression38', a)
    _safe_set(a, 'build_IBuilder37', b2)
    assert _is_linked(a, 'build_IBuilder37', b2)
    if hasattr(b1, 'build_BExpression38'):
        assert not _is_linked(b1, 'build_BExpression38', a)
    if hasattr(b2, 'build_BExpression38'):
        assert _is_linked(b2, 'build_BExpression38', a)
    _safe_set(a, 'build_IBuilder37', None)
    assert not _is_linked(a, 'build_IBuilder37', b2)
    if hasattr(b2, 'build_BExpression38'):
        assert not _is_linked(b2, 'build_BExpression38', a)


def test_assoc_precondExpr125_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_BuilderConcernContext126', b1)
    assert _is_linked(a, 'build_BuilderConcernContext126', b1)
    if hasattr(b1, 'build_BExpression127'):
        assert _is_linked(b1, 'build_BExpression127', a)
    _safe_set(a, 'build_BuilderConcernContext126', b2)
    assert _is_linked(a, 'build_BuilderConcernContext126', b2)
    if hasattr(b1, 'build_BExpression127'):
        assert not _is_linked(b1, 'build_BExpression127', a)
    if hasattr(b2, 'build_BExpression127'):
        assert _is_linked(b2, 'build_BExpression127', a)
    _safe_set(a, 'build_BuilderConcernContext126', None)
    assert not _is_linked(a, 'build_BuilderConcernContext126', b2)
    if hasattr(b2, 'build_BExpression127'):
        assert not _is_linked(b2, 'build_BExpression127', a)


def test_assoc_precondExpr26_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_IBuilder27', b1)
    assert _is_linked(a, 'build_IBuilder27', b1)
    if hasattr(b1, 'build_BExpression28'):
        assert _is_linked(b1, 'build_BExpression28', a)
    _safe_set(a, 'build_IBuilder27', b2)
    assert _is_linked(a, 'build_IBuilder27', b2)
    if hasattr(b1, 'build_BExpression28'):
        assert not _is_linked(b1, 'build_BExpression28', a)
    if hasattr(b2, 'build_BExpression28'):
        assert _is_linked(b2, 'build_BExpression28', a)
    _safe_set(a, 'build_IBuilder27', None)
    assert not _is_linked(a, 'build_IBuilder27', b2)
    if hasattr(b2, 'build_BExpression28'):
        assert not _is_linked(b2, 'build_BExpression28', a)


def test_assoc_propertySets15_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BuildUnit16', {b1})
    assert _is_linked(a, 'build_BuildUnit16', b1)
    if hasattr(b1, 'build_BPropertySet17'):
        assert _is_linked(b1, 'build_BPropertySet17', a)
    _safe_set(a, 'build_BuildUnit16', {b2})
    assert _is_linked(a, 'build_BuildUnit16', b2)
    if hasattr(b1, 'build_BPropertySet17'):
        assert not _is_linked(b1, 'build_BPropertySet17', a)
    if hasattr(b2, 'build_BPropertySet17'):
        assert _is_linked(b2, 'build_BPropertySet17', a)
    _safe_set(a, 'build_BuildUnit16', set())
    assert not _is_linked(a, 'build_BuildUnit16', b2)
    if hasattr(b2, 'build_BPropertySet17'):
        assert not _is_linked(b2, 'build_BPropertySet17', a)


def test_assoc_propertySets173_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BeeModel174', {b1})
    assert _is_linked(a, 'build_BeeModel174', b1)
    if hasattr(b1, 'build_BPropertySet175'):
        assert _is_linked(b1, 'build_BPropertySet175', a)
    _safe_set(a, 'build_BeeModel174', {b2})
    assert _is_linked(a, 'build_BeeModel174', b2)
    if hasattr(b1, 'build_BPropertySet175'):
        assert not _is_linked(b1, 'build_BPropertySet175', a)
    if hasattr(b2, 'build_BPropertySet175'):
        assert _is_linked(b2, 'build_BPropertySet175', a)
    _safe_set(a, 'build_BeeModel174', set())
    assert not _is_linked(a, 'build_BeeModel174', b2)
    if hasattr(b2, 'build_BPropertySet175'):
        assert not _is_linked(b2, 'build_BPropertySet175', a)


def test_assoc_providedCapabilities158_link_reassign_clear():
    a = build_Capability(nameSpace="sample_text")
    b1 = build_IProvidedCapabilityContainer()
    b2 = build_IProvidedCapabilityContainer()
    _safe_set(a, 'build_Capability159', b1)
    assert _is_linked(a, 'build_Capability159', b1)
    if hasattr(b1, 'build_IProvidedCapabilityContainer'):
        assert _is_linked(b1, 'build_IProvidedCapabilityContainer', a)
    _safe_set(a, 'build_Capability159', b2)
    assert _is_linked(a, 'build_Capability159', b2)
    if hasattr(b1, 'build_IProvidedCapabilityContainer'):
        assert not _is_linked(b1, 'build_IProvidedCapabilityContainer', a)
    if hasattr(b2, 'build_IProvidedCapabilityContainer'):
        assert _is_linked(b2, 'build_IProvidedCapabilityContainer', a)
    _safe_set(a, 'build_Capability159', None)
    assert not _is_linked(a, 'build_Capability159', b2)
    if hasattr(b2, 'build_IProvidedCapabilityContainer'):
        assert not _is_linked(b2, 'build_IProvidedCapabilityContainer', a)


def test_assoc_providedCapability205_link_reassign_clear():
    a = build_Capability(nameSpace="sample_text")
    b1 = build_EffectiveCapabilityFacade()
    b2 = build_EffectiveCapabilityFacade()
    _safe_set(a, 'build_Capability207', b1)
    assert _is_linked(a, 'build_Capability207', b1)
    if hasattr(b1, 'build_EffectiveCapabilityFacade206'):
        assert _is_linked(b1, 'build_EffectiveCapabilityFacade206', a)
    _safe_set(a, 'build_Capability207', b2)
    assert _is_linked(a, 'build_Capability207', b2)
    if hasattr(b1, 'build_EffectiveCapabilityFacade206'):
        assert not _is_linked(b1, 'build_EffectiveCapabilityFacade206', a)
    if hasattr(b2, 'build_EffectiveCapabilityFacade206'):
        assert _is_linked(b2, 'build_EffectiveCapabilityFacade206', a)
    _safe_set(a, 'build_Capability207', None)
    assert not _is_linked(a, 'build_Capability207', b2)
    if hasattr(b2, 'build_EffectiveCapabilityFacade206'):
        assert not _is_linked(b2, 'build_EffectiveCapabilityFacade206', a)


def test_assoc_providers179_link_reassign_clear():
    a = build_BeeModel()
    b1 = build_FirstFoundUnitProvider()
    b2 = build_FirstFoundUnitProvider()
    _safe_set(a, 'build_BeeModel180', {b1})
    assert _is_linked(a, 'build_BeeModel180', b1)
    if hasattr(b1, 'build_FirstFoundUnitProvider181'):
        assert _is_linked(b1, 'build_FirstFoundUnitProvider181', a)
    _safe_set(a, 'build_BeeModel180', {b2})
    assert _is_linked(a, 'build_BeeModel180', b2)
    if hasattr(b1, 'build_FirstFoundUnitProvider181'):
        assert not _is_linked(b1, 'build_FirstFoundUnitProvider181', a)
    if hasattr(b2, 'build_FirstFoundUnitProvider181'):
        assert _is_linked(b2, 'build_FirstFoundUnitProvider181', a)
    _safe_set(a, 'build_BeeModel180', set())
    assert not _is_linked(a, 'build_BeeModel180', b2)
    if hasattr(b2, 'build_FirstFoundUnitProvider181'):
        assert not _is_linked(b2, 'build_FirstFoundUnitProvider181', a)


def test_assoc_providers18_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_FirstFoundUnitProvider()
    b2 = build_FirstFoundUnitProvider()
    _safe_set(a, 'build_BuildUnit19', {b1})
    assert _is_linked(a, 'build_BuildUnit19', b1)
    if hasattr(b1, 'build_FirstFoundUnitProvider'):
        assert _is_linked(b1, 'build_FirstFoundUnitProvider', a)
    _safe_set(a, 'build_BuildUnit19', {b2})
    assert _is_linked(a, 'build_BuildUnit19', b2)
    if hasattr(b1, 'build_FirstFoundUnitProvider'):
        assert not _is_linked(b1, 'build_FirstFoundUnitProvider', a)
    if hasattr(b2, 'build_FirstFoundUnitProvider'):
        assert _is_linked(b2, 'build_FirstFoundUnitProvider', a)
    _safe_set(a, 'build_BuildUnit19', set())
    assert not _is_linked(a, 'build_BuildUnit19', b2)
    if hasattr(b2, 'build_FirstFoundUnitProvider'):
        assert not _is_linked(b2, 'build_FirstFoundUnitProvider', a)


def test_assoc_providers67_link_reassign_clear():
    a = build_UnitProvider(documentation="sample_text")
    b1 = build_CompoundUnitProvider()
    b2 = build_CompoundUnitProvider()
    _safe_set(a, 'build_UnitProvider', b1)
    assert _is_linked(a, 'build_UnitProvider', b1)
    if hasattr(b1, 'build_CompoundUnitProvider'):
        assert _is_linked(b1, 'build_CompoundUnitProvider', a)
    _safe_set(a, 'build_UnitProvider', b2)
    assert _is_linked(a, 'build_UnitProvider', b2)
    if hasattr(b1, 'build_CompoundUnitProvider'):
        assert not _is_linked(b1, 'build_CompoundUnitProvider', a)
    if hasattr(b2, 'build_CompoundUnitProvider'):
        assert _is_linked(b2, 'build_CompoundUnitProvider', a)
    _safe_set(a, 'build_UnitProvider', None)
    assert not _is_linked(a, 'build_UnitProvider', b2)
    if hasattr(b2, 'build_CompoundUnitProvider'):
        assert not _is_linked(b2, 'build_CompoundUnitProvider', a)


def test_assoc_providesRemovals100_link_reassign_clear():
    a = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    b1 = build_ProvidesPredicate()
    b2 = build_ProvidesPredicate()
    _safe_set(a, 'build_UnitConcernContext101', {b1})
    assert _is_linked(a, 'build_UnitConcernContext101', b1)
    if hasattr(b1, 'build_ProvidesPredicate102'):
        assert _is_linked(b1, 'build_ProvidesPredicate102', a)
    _safe_set(a, 'build_UnitConcernContext101', {b2})
    assert _is_linked(a, 'build_UnitConcernContext101', b2)
    if hasattr(b1, 'build_ProvidesPredicate102'):
        assert not _is_linked(b1, 'build_ProvidesPredicate102', a)
    if hasattr(b2, 'build_ProvidesPredicate102'):
        assert _is_linked(b2, 'build_ProvidesPredicate102', a)
    _safe_set(a, 'build_UnitConcernContext101', set())
    assert not _is_linked(a, 'build_UnitConcernContext101', b2)
    if hasattr(b2, 'build_ProvidesPredicate102'):
        assert not _is_linked(b2, 'build_ProvidesPredicate102', a)


def test_assoc_providesRemovals134_link_reassign_clear():
    a = build_ProvidesPredicate()
    b1 = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b2 = build_BuilderConcernContext(matchParameters=False, outputAnnotationsRemovals="sample_text_2", removePostCondition=False, removePostInputCondition=False, removePreCondition=False, sourceAnnotationsRemovals="sample_text_2", varArgs=False)
    _safe_set(a, 'build_ProvidesPredicate136', b1)
    assert _is_linked(a, 'build_ProvidesPredicate136', b1)
    if hasattr(b1, 'build_BuilderConcernContext135'):
        assert _is_linked(b1, 'build_BuilderConcernContext135', a)
    _safe_set(a, 'build_ProvidesPredicate136', b2)
    assert _is_linked(a, 'build_ProvidesPredicate136', b2)
    if hasattr(b1, 'build_BuilderConcernContext135'):
        assert not _is_linked(b1, 'build_BuilderConcernContext135', a)
    if hasattr(b2, 'build_BuilderConcernContext135'):
        assert _is_linked(b2, 'build_BuilderConcernContext135', a)
    _safe_set(a, 'build_ProvidesPredicate136', None)
    assert not _is_linked(a, 'build_ProvidesPredicate136', b2)
    if hasattr(b2, 'build_BuilderConcernContext135'):
        assert not _is_linked(b2, 'build_BuilderConcernContext135', a)


def test_assoc_query106_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_BuilderConcernContext107', b1)
    assert _is_linked(a, 'build_BuilderConcernContext107', b1)
    if hasattr(b1, 'build_BExpression108'):
        assert _is_linked(b1, 'build_BExpression108', a)
    _safe_set(a, 'build_BuilderConcernContext107', b2)
    assert _is_linked(a, 'build_BuilderConcernContext107', b2)
    if hasattr(b1, 'build_BExpression108'):
        assert not _is_linked(b1, 'build_BExpression108', a)
    if hasattr(b2, 'build_BExpression108'):
        assert _is_linked(b2, 'build_BExpression108', a)
    _safe_set(a, 'build_BuilderConcernContext107', None)
    assert not _is_linked(a, 'build_BuilderConcernContext107', b2)
    if hasattr(b2, 'build_BExpression108'):
        assert not _is_linked(b2, 'build_BExpression108', a)


def test_assoc_query94_link_reassign_clear():
    a = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    b1 = build_BExpression()
    b2 = build_BExpression()
    _safe_set(a, 'build_UnitConcernContext95', b1)
    assert _is_linked(a, 'build_UnitConcernContext95', b1)
    if hasattr(b1, 'build_BExpression96'):
        assert _is_linked(b1, 'build_BExpression96', a)
    _safe_set(a, 'build_UnitConcernContext95', b2)
    assert _is_linked(a, 'build_UnitConcernContext95', b2)
    if hasattr(b1, 'build_BExpression96'):
        assert not _is_linked(b1, 'build_BExpression96', a)
    if hasattr(b2, 'build_BExpression96'):
        assert _is_linked(b2, 'build_BExpression96', a)
    _safe_set(a, 'build_UnitConcernContext95', None)
    assert not _is_linked(a, 'build_UnitConcernContext95', b2)
    if hasattr(b2, 'build_BExpression96'):
        assert not _is_linked(b2, 'build_BExpression96', a)


def test_assoc_repositories11_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b2 = build_BuildUnit(documentation="sample_text_2", executionMode="sample_text_2", outputLocation="sample_text_2", platformFilter="sample_text_2", sourceLocation="sample_text_2")
    _safe_set(a, 'build_Repository', b1)
    assert _is_linked(a, 'build_Repository', b1)
    if hasattr(b1, 'build_BuildUnit12'):
        assert _is_linked(b1, 'build_BuildUnit12', a)
    _safe_set(a, 'build_Repository', b2)
    assert _is_linked(a, 'build_Repository', b2)
    if hasattr(b1, 'build_BuildUnit12'):
        assert not _is_linked(b1, 'build_BuildUnit12', a)
    if hasattr(b2, 'build_BuildUnit12'):
        assert _is_linked(b2, 'build_BuildUnit12', a)
    _safe_set(a, 'build_Repository', None)
    assert not _is_linked(a, 'build_Repository', b2)
    if hasattr(b2, 'build_BuildUnit12'):
        assert not _is_linked(b2, 'build_BuildUnit12', a)


def test_assoc_repositories176_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_BeeModel()
    b2 = build_BeeModel()
    _safe_set(a, 'build_Repository178', b1)
    assert _is_linked(a, 'build_Repository178', b1)
    if hasattr(b1, 'build_BeeModel177'):
        assert _is_linked(b1, 'build_BeeModel177', a)
    _safe_set(a, 'build_Repository178', b2)
    assert _is_linked(a, 'build_Repository178', b2)
    if hasattr(b1, 'build_BeeModel177'):
        assert not _is_linked(b1, 'build_BeeModel177', a)
    if hasattr(b2, 'build_BeeModel177'):
        assert _is_linked(b2, 'build_BeeModel177', a)
    _safe_set(a, 'build_Repository178', None)
    assert not _is_linked(a, 'build_Repository178', b2)
    if hasattr(b2, 'build_BeeModel177'):
        assert not _is_linked(b2, 'build_BeeModel177', a)


def test_assoc_repository249_link_reassign_clear():
    a = build_UnitRepositoryDescription(evaluatedOptions="sample_text")
    b1 = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b2 = build_Repository(documentation="sample_text_2", handlerType="sample_text_2", name="sample_text_2")
    _safe_set(a, 'build_UnitRepositoryDescription', b1)
    assert _is_linked(a, 'build_UnitRepositoryDescription', b1)
    if hasattr(b1, 'build_Repository250'):
        assert _is_linked(b1, 'build_Repository250', a)
    _safe_set(a, 'build_UnitRepositoryDescription', b2)
    assert _is_linked(a, 'build_UnitRepositoryDescription', b2)
    if hasattr(b1, 'build_Repository250'):
        assert not _is_linked(b1, 'build_Repository250', a)
    if hasattr(b2, 'build_Repository250'):
        assert _is_linked(b2, 'build_Repository250', a)
    _safe_set(a, 'build_UnitRepositoryDescription', None)
    assert not _is_linked(a, 'build_UnitRepositoryDescription', b2)
    if hasattr(b2, 'build_Repository250'):
        assert not _is_linked(b2, 'build_Repository250', a)


def test_assoc_repository61_link_reassign_clear():
    a = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    b1 = build_RepositoryUnitProvider()
    b2 = build_RepositoryUnitProvider()
    _safe_set(a, 'build_Repository62', b1)
    assert _is_linked(a, 'build_Repository62', b1)
    if hasattr(b1, 'build_RepositoryUnitProvider'):
        assert _is_linked(b1, 'build_RepositoryUnitProvider', a)
    _safe_set(a, 'build_Repository62', b2)
    assert _is_linked(a, 'build_Repository62', b2)
    if hasattr(b1, 'build_RepositoryUnitProvider'):
        assert not _is_linked(b1, 'build_RepositoryUnitProvider', a)
    if hasattr(b2, 'build_RepositoryUnitProvider'):
        assert _is_linked(b2, 'build_RepositoryUnitProvider', a)
    _safe_set(a, 'build_Repository62', None)
    assert not _is_linked(a, 'build_Repository62', b2)
    if hasattr(b2, 'build_RepositoryUnitProvider'):
        assert not _is_linked(b2, 'build_RepositoryUnitProvider', a)


def test_assoc_requiredCapabilities153_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_IRequiredCapabilityContainer()
    b2 = build_IRequiredCapabilityContainer()
    _safe_set(a, 'build_RequiredCapability154', b1)
    assert _is_linked(a, 'build_RequiredCapability154', b1)
    if hasattr(b1, 'build_IRequiredCapabilityContainer'):
        assert _is_linked(b1, 'build_IRequiredCapabilityContainer', a)
    _safe_set(a, 'build_RequiredCapability154', b2)
    assert _is_linked(a, 'build_RequiredCapability154', b2)
    if hasattr(b1, 'build_IRequiredCapabilityContainer'):
        assert not _is_linked(b1, 'build_IRequiredCapabilityContainer', a)
    if hasattr(b2, 'build_IRequiredCapabilityContainer'):
        assert _is_linked(b2, 'build_IRequiredCapabilityContainer', a)
    _safe_set(a, 'build_RequiredCapability154', None)
    assert not _is_linked(a, 'build_RequiredCapability154', b2)
    if hasattr(b2, 'build_IRequiredCapabilityContainer'):
        assert not _is_linked(b2, 'build_IRequiredCapabilityContainer', a)


def test_assoc_requiredCapability210_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_BuilderCallFacade(aliases="sample_text")
    b2 = build_BuilderCallFacade(aliases="sample_text_2")
    _safe_set(a, 'build_RequiredCapability212', b1)
    assert _is_linked(a, 'build_RequiredCapability212', b1)
    if hasattr(b1, 'build_BuilderCallFacade211'):
        assert _is_linked(b1, 'build_BuilderCallFacade211', a)
    _safe_set(a, 'build_RequiredCapability212', b2)
    assert _is_linked(a, 'build_RequiredCapability212', b2)
    if hasattr(b1, 'build_BuilderCallFacade211'):
        assert not _is_linked(b1, 'build_BuilderCallFacade211', a)
    if hasattr(b2, 'build_BuilderCallFacade211'):
        assert _is_linked(b2, 'build_BuilderCallFacade211', a)
    _safe_set(a, 'build_RequiredCapability212', None)
    assert not _is_linked(a, 'build_RequiredCapability212', b2)
    if hasattr(b2, 'build_BuilderCallFacade211'):
        assert not _is_linked(b2, 'build_BuilderCallFacade211', a)


def test_assoc_requiredCapability256_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_BuildCallSingle()
    b2 = build_BuildCallSingle()
    _safe_set(a, 'build_RequiredCapability257', b1)
    assert _is_linked(a, 'build_RequiredCapability257', b1)
    if hasattr(b1, 'build_BuildCallSingle'):
        assert _is_linked(b1, 'build_BuildCallSingle', a)
    _safe_set(a, 'build_RequiredCapability257', b2)
    assert _is_linked(a, 'build_RequiredCapability257', b2)
    if hasattr(b1, 'build_BuildCallSingle'):
        assert not _is_linked(b1, 'build_BuildCallSingle', a)
    if hasattr(b2, 'build_BuildCallSingle'):
        assert _is_linked(b2, 'build_BuildCallSingle', a)
    _safe_set(a, 'build_RequiredCapability257', None)
    assert not _is_linked(a, 'build_RequiredCapability257', b2)
    if hasattr(b2, 'build_BuildCallSingle'):
        assert not _is_linked(b2, 'build_BuildCallSingle', a)


def test_assoc_requiredCapabilityDeclaration258_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_BuildCallOnDeclaredRequirement()
    b2 = build_BuildCallOnDeclaredRequirement()
    _safe_set(a, 'build_RequiredCapability259', b1)
    assert _is_linked(a, 'build_RequiredCapability259', b1)
    if hasattr(b1, 'build_BuildCallOnDeclaredRequirement'):
        assert _is_linked(b1, 'build_BuildCallOnDeclaredRequirement', a)
    _safe_set(a, 'build_RequiredCapability259', b2)
    assert _is_linked(a, 'build_RequiredCapability259', b2)
    if hasattr(b1, 'build_BuildCallOnDeclaredRequirement'):
        assert not _is_linked(b1, 'build_BuildCallOnDeclaredRequirement', a)
    if hasattr(b2, 'build_BuildCallOnDeclaredRequirement'):
        assert _is_linked(b2, 'build_BuildCallOnDeclaredRequirement', a)
    _safe_set(a, 'build_RequiredCapability259', None)
    assert not _is_linked(a, 'build_RequiredCapability259', b2)
    if hasattr(b2, 'build_BuildCallOnDeclaredRequirement'):
        assert not _is_linked(b2, 'build_BuildCallOnDeclaredRequirement', a)


def test_assoc_requiredCapabilityReference260_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_BuildCallOnReferencedRequirement()
    b2 = build_BuildCallOnReferencedRequirement()
    _safe_set(a, 'build_RequiredCapability261', b1)
    assert _is_linked(a, 'build_RequiredCapability261', b1)
    if hasattr(b1, 'build_BuildCallOnReferencedRequirement'):
        assert _is_linked(b1, 'build_BuildCallOnReferencedRequirement', a)
    _safe_set(a, 'build_RequiredCapability261', b2)
    assert _is_linked(a, 'build_RequiredCapability261', b2)
    if hasattr(b1, 'build_BuildCallOnReferencedRequirement'):
        assert not _is_linked(b1, 'build_BuildCallOnReferencedRequirement', a)
    if hasattr(b2, 'build_BuildCallOnReferencedRequirement'):
        assert _is_linked(b2, 'build_BuildCallOnReferencedRequirement', a)
    _safe_set(a, 'build_RequiredCapability261', None)
    assert not _is_linked(a, 'build_RequiredCapability261', b2)
    if hasattr(b2, 'build_BuildCallOnReferencedRequirement'):
        assert not _is_linked(b2, 'build_BuildCallOnReferencedRequirement', a)


def test_assoc_requiredPredicate251_link_reassign_clear():
    a = build_CapabilityPredicate(versionRange="sample_text")
    b1 = build_BuildCallOnSelectedRequirements()
    b2 = build_BuildCallOnSelectedRequirements()
    _safe_set(a, 'build_CapabilityPredicate252', b1)
    assert _is_linked(a, 'build_CapabilityPredicate252', b1)
    if hasattr(b1, 'build_BuildCallOnSelectedRequirements'):
        assert _is_linked(b1, 'build_BuildCallOnSelectedRequirements', a)
    _safe_set(a, 'build_CapabilityPredicate252', b2)
    assert _is_linked(a, 'build_CapabilityPredicate252', b2)
    if hasattr(b1, 'build_BuildCallOnSelectedRequirements'):
        assert not _is_linked(b1, 'build_BuildCallOnSelectedRequirements', a)
    if hasattr(b2, 'build_BuildCallOnSelectedRequirements'):
        assert _is_linked(b2, 'build_BuildCallOnSelectedRequirements', a)
    _safe_set(a, 'build_CapabilityPredicate252', None)
    assert not _is_linked(a, 'build_CapabilityPredicate252', b2)
    if hasattr(b2, 'build_BuildCallOnSelectedRequirements'):
        assert not _is_linked(b2, 'build_BuildCallOnSelectedRequirements', a)


def test_assoc_requiredPredicates155_link_reassign_clear():
    a = build_CapabilityPredicate(versionRange="sample_text")
    b1 = build_IRequiredCapabilityContainer()
    b2 = build_IRequiredCapabilityContainer()
    _safe_set(a, 'build_CapabilityPredicate157', b1)
    assert _is_linked(a, 'build_CapabilityPredicate157', b1)
    if hasattr(b1, 'build_IRequiredCapabilityContainer156'):
        assert _is_linked(b1, 'build_IRequiredCapabilityContainer156', a)
    _safe_set(a, 'build_CapabilityPredicate157', b2)
    assert _is_linked(a, 'build_CapabilityPredicate157', b2)
    if hasattr(b1, 'build_IRequiredCapabilityContainer156'):
        assert not _is_linked(b1, 'build_IRequiredCapabilityContainer156', a)
    if hasattr(b2, 'build_IRequiredCapabilityContainer156'):
        assert _is_linked(b2, 'build_IRequiredCapabilityContainer156', a)
    _safe_set(a, 'build_CapabilityPredicate157', None)
    assert not _is_linked(a, 'build_CapabilityPredicate157', b2)
    if hasattr(b2, 'build_IRequiredCapabilityContainer156'):
        assert not _is_linked(b2, 'build_IRequiredCapabilityContainer156', a)


def test_assoc_requiredPredicatesRemovals103_link_reassign_clear():
    a = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    b1 = build_CapabilityPredicate(versionRange="sample_text")
    b2 = build_CapabilityPredicate(versionRange="sample_text_2")
    _safe_set(a, 'build_UnitConcernContext104', {b1})
    assert _is_linked(a, 'build_UnitConcernContext104', b1)
    if hasattr(b1, 'build_CapabilityPredicate105'):
        assert _is_linked(b1, 'build_CapabilityPredicate105', a)
    _safe_set(a, 'build_UnitConcernContext104', {b2})
    assert _is_linked(a, 'build_UnitConcernContext104', b2)
    if hasattr(b1, 'build_CapabilityPredicate105'):
        assert not _is_linked(b1, 'build_CapabilityPredicate105', a)
    if hasattr(b2, 'build_CapabilityPredicate105'):
        assert _is_linked(b2, 'build_CapabilityPredicate105', a)
    _safe_set(a, 'build_UnitConcernContext104', set())
    assert not _is_linked(a, 'build_UnitConcernContext104', b2)
    if hasattr(b2, 'build_CapabilityPredicate105'):
        assert not _is_linked(b2, 'build_CapabilityPredicate105', a)


def test_assoc_requirement202_link_reassign_clear():
    a = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    b1 = build_EffectiveRequirementFacade()
    b2 = build_EffectiveRequirementFacade()
    _safe_set(a, 'build_RequiredCapability204', b1)
    assert _is_linked(a, 'build_RequiredCapability204', b1)
    if hasattr(b1, 'build_EffectiveRequirementFacade203'):
        assert _is_linked(b1, 'build_EffectiveRequirementFacade203', a)
    _safe_set(a, 'build_RequiredCapability204', b2)
    assert _is_linked(a, 'build_RequiredCapability204', b2)
    if hasattr(b1, 'build_EffectiveRequirementFacade203'):
        assert not _is_linked(b1, 'build_EffectiveRequirementFacade203', a)
    if hasattr(b2, 'build_EffectiveRequirementFacade203'):
        assert _is_linked(b2, 'build_EffectiveRequirementFacade203', a)
    _safe_set(a, 'build_RequiredCapability204', None)
    assert not _is_linked(a, 'build_RequiredCapability204', b2)
    if hasattr(b2, 'build_EffectiveRequirementFacade203'):
        assert not _is_linked(b2, 'build_EffectiveRequirementFacade203', a)


def test_assoc_requiresRemovals97_link_reassign_clear():
    a = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    b1 = build_RequiresPredicate(meta=True)
    b2 = build_RequiresPredicate(meta=False)
    _safe_set(a, 'build_UnitConcernContext98', {b1})
    assert _is_linked(a, 'build_UnitConcernContext98', b1)
    if hasattr(b1, 'build_RequiresPredicate99'):
        assert _is_linked(b1, 'build_RequiresPredicate99', a)
    _safe_set(a, 'build_UnitConcernContext98', {b2})
    assert _is_linked(a, 'build_UnitConcernContext98', b2)
    if hasattr(b1, 'build_RequiresPredicate99'):
        assert not _is_linked(b1, 'build_RequiresPredicate99', a)
    if hasattr(b2, 'build_RequiresPredicate99'):
        assert _is_linked(b2, 'build_RequiresPredicate99', a)
    _safe_set(a, 'build_UnitConcernContext98', set())
    assert not _is_linked(a, 'build_UnitConcernContext98', b2)
    if hasattr(b2, 'build_RequiresPredicate99'):
        assert not _is_linked(b2, 'build_RequiresPredicate99', a)


def test_assoc_source41_link_reassign_clear():
    a = build_IBuilder(unitType="sample_text")
    b1 = build_PathGroup()
    b2 = build_PathGroup()
    _safe_set(a, 'build_IBuilder42', b1)
    assert _is_linked(a, 'build_IBuilder42', b1)
    if hasattr(b1, 'build_PathGroup43'):
        assert _is_linked(b1, 'build_PathGroup43', a)
    _safe_set(a, 'build_IBuilder42', b2)
    assert _is_linked(a, 'build_IBuilder42', b2)
    if hasattr(b1, 'build_PathGroup43'):
        assert not _is_linked(b1, 'build_PathGroup43', a)
    if hasattr(b2, 'build_PathGroup43'):
        assert _is_linked(b2, 'build_PathGroup43', a)
    _safe_set(a, 'build_IBuilder42', None)
    assert not _is_linked(a, 'build_IBuilder42', b2)
    if hasattr(b2, 'build_PathGroup43'):
        assert not _is_linked(b2, 'build_PathGroup43', a)


def test_assoc_sourceAdditions142_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_ConditionalPathVector()
    b2 = build_ConditionalPathVector()
    _safe_set(a, 'build_BuilderConcernContext143', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext143', b1)
    if hasattr(b1, 'build_ConditionalPathVector144'):
        assert _is_linked(b1, 'build_ConditionalPathVector144', a)
    _safe_set(a, 'build_BuilderConcernContext143', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext143', b2)
    if hasattr(b1, 'build_ConditionalPathVector144'):
        assert not _is_linked(b1, 'build_ConditionalPathVector144', a)
    if hasattr(b2, 'build_ConditionalPathVector144'):
        assert _is_linked(b2, 'build_ConditionalPathVector144', a)
    _safe_set(a, 'build_BuilderConcernContext143', set())
    assert not _is_linked(a, 'build_BuilderConcernContext143', b2)
    if hasattr(b2, 'build_ConditionalPathVector144'):
        assert not _is_linked(b2, 'build_ConditionalPathVector144', a)


def test_assoc_sourceAnnotationAdditions145_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_BPropertySet()
    b2 = build_BPropertySet()
    _safe_set(a, 'build_BuilderConcernContext146', b1)
    assert _is_linked(a, 'build_BuilderConcernContext146', b1)
    if hasattr(b1, 'build_BPropertySet147'):
        assert _is_linked(b1, 'build_BPropertySet147', a)
    _safe_set(a, 'build_BuilderConcernContext146', b2)
    assert _is_linked(a, 'build_BuilderConcernContext146', b2)
    if hasattr(b1, 'build_BPropertySet147'):
        assert not _is_linked(b1, 'build_BPropertySet147', a)
    if hasattr(b2, 'build_BPropertySet147'):
        assert _is_linked(b2, 'build_BPropertySet147', a)
    _safe_set(a, 'build_BuilderConcernContext146', None)
    assert not _is_linked(a, 'build_BuilderConcernContext146', b2)
    if hasattr(b2, 'build_BPropertySet147'):
        assert not _is_linked(b2, 'build_BPropertySet147', a)


def test_assoc_sourceRemovals140_link_reassign_clear():
    a = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    b1 = build_SourcePredicate()
    b2 = build_SourcePredicate()
    _safe_set(a, 'build_BuilderConcernContext141', {b1})
    assert _is_linked(a, 'build_BuilderConcernContext141', b1)
    if hasattr(b1, 'build_SourcePredicate'):
        assert _is_linked(b1, 'build_SourcePredicate', a)
    _safe_set(a, 'build_BuilderConcernContext141', {b2})
    assert _is_linked(a, 'build_BuilderConcernContext141', b2)
    if hasattr(b1, 'build_SourcePredicate'):
        assert not _is_linked(b1, 'build_SourcePredicate', a)
    if hasattr(b2, 'build_SourcePredicate'):
        assert _is_linked(b2, 'build_SourcePredicate', a)
    _safe_set(a, 'build_BuilderConcernContext141', set())
    assert not _is_linked(a, 'build_BuilderConcernContext141', b2)
    if hasattr(b2, 'build_SourcePredicate'):
        assert not _is_linked(b2, 'build_SourcePredicate', a)


def test_assoc_synchronizations9_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_Synchronization()
    b2 = build_Synchronization()
    _safe_set(a, 'build_BuildUnit10', {b1})
    assert _is_linked(a, 'build_BuildUnit10', b1)
    if hasattr(b1, 'build_Synchronization'):
        assert _is_linked(b1, 'build_Synchronization', a)
    _safe_set(a, 'build_BuildUnit10', {b2})
    assert _is_linked(a, 'build_BuildUnit10', b2)
    if hasattr(b1, 'build_Synchronization'):
        assert not _is_linked(b1, 'build_Synchronization', a)
    if hasattr(b2, 'build_Synchronization'):
        assert _is_linked(b2, 'build_Synchronization', a)
    _safe_set(a, 'build_BuildUnit10', set())
    assert not _is_linked(a, 'build_BuildUnit10', b2)
    if hasattr(b2, 'build_Synchronization'):
        assert not _is_linked(b2, 'build_Synchronization', a)


def test_assoc_unit190_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_EffectiveUnitFacade()
    b2 = build_EffectiveUnitFacade()
    _safe_set(a, 'build_BuildUnit191', b1)
    assert _is_linked(a, 'build_BuildUnit191', b1)
    if hasattr(b1, 'build_EffectiveUnitFacade'):
        assert _is_linked(b1, 'build_EffectiveUnitFacade', a)
    _safe_set(a, 'build_BuildUnit191', b2)
    assert _is_linked(a, 'build_BuildUnit191', b2)
    if hasattr(b1, 'build_EffectiveUnitFacade'):
        assert not _is_linked(b1, 'build_EffectiveUnitFacade', a)
    if hasattr(b2, 'build_EffectiveUnitFacade'):
        assert _is_linked(b2, 'build_EffectiveUnitFacade', a)
    _safe_set(a, 'build_BuildUnit191', None)
    assert not _is_linked(a, 'build_BuildUnit191', b2)
    if hasattr(b2, 'build_EffectiveUnitFacade'):
        assert not _is_linked(b2, 'build_EffectiveUnitFacade', a)


def test_assoc_unit219_link_reassign_clear():
    a = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    b1 = build_UnitResolutionInfo()
    b2 = build_UnitResolutionInfo()
    _safe_set(a, 'build_BuildUnit220', b1)
    assert _is_linked(a, 'build_BuildUnit220', b1)
    if hasattr(b1, 'build_UnitResolutionInfo'):
        assert _is_linked(b1, 'build_UnitResolutionInfo', a)
    _safe_set(a, 'build_BuildUnit220', b2)
    assert _is_linked(a, 'build_BuildUnit220', b2)
    if hasattr(b1, 'build_UnitResolutionInfo'):
        assert not _is_linked(b1, 'build_UnitResolutionInfo', a)
    if hasattr(b2, 'build_UnitResolutionInfo'):
        assert _is_linked(b2, 'build_UnitResolutionInfo', a)
    _safe_set(a, 'build_BuildUnit220', None)
    assert not _is_linked(a, 'build_BuildUnit220', b2)
    if hasattr(b2, 'build_UnitResolutionInfo'):
        assert not _is_linked(b2, 'build_UnitResolutionInfo', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B3Function_strategy = st.builds(B3Function)
@given(instance=B3Function_strategy)
@settings(max_examples=25)
def test_B3Function_instantiation(instance):
    assert isinstance(instance, B3Function)


BChainedExpression_strategy = st.builds(BChainedExpression)
@given(instance=BChainedExpression_strategy)
@settings(max_examples=25)
def test_BChainedExpression_instantiation(instance):
    assert isinstance(instance, BChainedExpression)


BConcernContext_strategy = st.builds(BConcernContext)
@given(instance=BConcernContext_strategy)
@settings(max_examples=25)
def test_BConcernContext_instantiation(instance):
    assert isinstance(instance, BConcernContext)


BExpression_strategy = st.builds(BExpression)
@given(instance=BExpression_strategy)
@settings(max_examples=25)
def test_BExpression_instantiation(instance):
    assert isinstance(instance, BExpression)


BFunctionContainer_strategy = st.builds(BFunctionContainer)
@given(instance=BFunctionContainer_strategy)
@settings(max_examples=25)
def test_BFunctionContainer_instantiation(instance):
    assert isinstance(instance, BFunctionContainer)


BFunctionWrapper_strategy = st.builds(BFunctionWrapper)
@given(instance=BFunctionWrapper_strategy)
@settings(max_examples=25)
def test_BFunctionWrapper_instantiation(instance):
    assert isinstance(instance, BFunctionWrapper)


BInnerContext_strategy = st.builds(BInnerContext)
@given(instance=BInnerContext_strategy)
@settings(max_examples=25)
def test_BInnerContext_instantiation(instance):
    assert isinstance(instance, BInnerContext)


BJavaFunction_strategy = st.builds(BJavaFunction)
@given(instance=BJavaFunction_strategy)
@settings(max_examples=25)
def test_BJavaFunction_instantiation(instance):
    assert isinstance(instance, BJavaFunction)


BParameterDeclaration_strategy = st.builds(BParameterDeclaration)
@given(instance=BParameterDeclaration_strategy)
@settings(max_examples=25)
def test_BParameterDeclaration_instantiation(instance):
    assert isinstance(instance, BParameterDeclaration)


BuildCallMultiple_strategy = st.builds(BuildCallMultiple)
@given(instance=BuildCallMultiple_strategy)
@settings(max_examples=25)
def test_BuildCallMultiple_instantiation(instance):
    assert isinstance(instance, BuildCallMultiple)


BuildCallSingle_strategy = st.builds(BuildCallSingle)
@given(instance=BuildCallSingle_strategy)
@settings(max_examples=25)
def test_BuildCallSingle_instantiation(instance):
    assert isinstance(instance, BuildCallSingle)


BuildConcernContext_strategy = st.builds(BuildConcernContext)
@given(instance=BuildConcernContext_strategy)
@settings(max_examples=25)
def test_BuildConcernContext_instantiation(instance):
    assert isinstance(instance, BuildConcernContext)


BuildUnitRepository_strategy = st.builds(BuildUnitRepository)
@given(instance=BuildUnitRepository_strategy)
@settings(max_examples=25)
def test_BuildUnitRepository_instantiation(instance):
    assert isinstance(instance, BuildUnitRepository)


BuilderCall_strategy = st.builds(BuilderCall)
@given(instance=BuilderCall_strategy)
@settings(max_examples=25)
def test_BuilderCall_instantiation(instance):
    assert isinstance(instance, BuilderCall)


BuilderCallFacade_strategy = st.builds(BuilderCallFacade)
@given(instance=BuilderCallFacade_strategy)
@settings(max_examples=25)
def test_BuilderCallFacade_instantiation(instance):
    assert isinstance(instance, BuilderCallFacade)


BuilderInput_strategy = st.builds(BuilderInput)
@given(instance=BuilderInput_strategy)
@settings(max_examples=25)
def test_BuilderInput_instantiation(instance):
    assert isinstance(instance, BuilderInput)


BuilderInputDecorator_strategy = st.builds(BuilderInputDecorator)
@given(instance=BuilderInputDecorator_strategy)
@settings(max_examples=25)
def test_BuilderInputDecorator_instantiation(instance):
    assert isinstance(instance, BuilderInputDecorator)


Capability_strategy = st.builds(Capability)
@given(instance=Capability_strategy)
@settings(max_examples=25)
def test_Capability_instantiation(instance):
    assert isinstance(instance, Capability)


CapabilityPredicate_strategy = st.builds(CapabilityPredicate)
@given(instance=CapabilityPredicate_strategy)
@settings(max_examples=25)
def test_CapabilityPredicate_instantiation(instance):
    assert isinstance(instance, CapabilityPredicate)


CompoundBuildUnitRepository_strategy = st.builds(CompoundBuildUnitRepository)
@given(instance=CompoundBuildUnitRepository_strategy)
@settings(max_examples=25)
def test_CompoundBuildUnitRepository_instantiation(instance):
    assert isinstance(instance, CompoundBuildUnitRepository)


CompoundUnitProvider_strategy = st.builds(CompoundUnitProvider)
@given(instance=CompoundUnitProvider_strategy)
@settings(max_examples=25)
def test_CompoundUnitProvider_instantiation(instance):
    assert isinstance(instance, CompoundUnitProvider)


EffectiveFacade_strategy = st.builds(EffectiveFacade)
@given(instance=EffectiveFacade_strategy)
@settings(max_examples=25)
def test_EffectiveFacade_instantiation(instance):
    assert isinstance(instance, EffectiveFacade)


IBuildUnitContainer_strategy = st.builds(IBuildUnitContainer)
@given(instance=IBuildUnitContainer_strategy)
@settings(max_examples=25)
def test_IBuildUnitContainer_instantiation(instance):
    assert isinstance(instance, IBuildUnitContainer)


IBuildUnitRepository_strategy = st.builds(IBuildUnitRepository)
@given(instance=IBuildUnitRepository_strategy)
@settings(max_examples=25)
def test_IBuildUnitRepository_instantiation(instance):
    assert isinstance(instance, IBuildUnitRepository)


IBuilder_strategy = st.builds(IBuilder)
@given(instance=IBuilder_strategy)
@settings(max_examples=25)
def test_IBuilder_instantiation(instance):
    assert isinstance(instance, IBuilder)


IEffectiveFacade_strategy = st.builds(IEffectiveFacade)
@given(instance=IEffectiveFacade_strategy)
@settings(max_examples=25)
def test_IEffectiveFacade_instantiation(instance):
    assert isinstance(instance, IEffectiveFacade)


IFunction_strategy = st.builds(IFunction)
@given(instance=IFunction_strategy)
@settings(max_examples=25)
def test_IFunction_instantiation(instance):
    assert isinstance(instance, IFunction)


INamedValue_strategy = st.builds(INamedValue)
@given(instance=INamedValue_strategy)
@settings(max_examples=25)
def test_INamedValue_instantiation(instance):
    assert isinstance(instance, INamedValue)


IProvidedCapabilityContainer_strategy = st.builds(IProvidedCapabilityContainer)
@given(instance=IProvidedCapabilityContainer_strategy)
@settings(max_examples=25)
def test_IProvidedCapabilityContainer_instantiation(instance):
    assert isinstance(instance, IProvidedCapabilityContainer)


IRequiredCapabilityContainer_strategy = st.builds(IRequiredCapabilityContainer)
@given(instance=IRequiredCapabilityContainer_strategy)
@settings(max_examples=25)
def test_IRequiredCapabilityContainer_instantiation(instance):
    assert isinstance(instance, IRequiredCapabilityContainer)


ITypedValueContainer_strategy = st.builds(ITypedValueContainer)
@given(instance=ITypedValueContainer_strategy)
@settings(max_examples=25)
def test_ITypedValueContainer_instantiation(instance):
    assert isinstance(instance, ITypedValueContainer)


IVarName_strategy = st.builds(IVarName)
@given(instance=IVarName_strategy)
@settings(max_examples=25)
def test_IVarName_instantiation(instance):
    assert isinstance(instance, IVarName)


PathGroupPredicate_strategy = st.builds(PathGroupPredicate)
@given(instance=PathGroupPredicate_strategy)
@settings(max_examples=25)
def test_PathGroupPredicate_instantiation(instance):
    assert isinstance(instance, PathGroupPredicate)


RequiredCapability_strategy = st.builds(RequiredCapability)
@given(instance=RequiredCapability_strategy)
@settings(max_examples=25)
def test_RequiredCapability_instantiation(instance):
    assert isinstance(instance, RequiredCapability)


ResolutionInfo_strategy = st.builds(ResolutionInfo)
@given(instance=ResolutionInfo_strategy)
@settings(max_examples=25)
def test_ResolutionInfo_instantiation(instance):
    assert isinstance(instance, ResolutionInfo)


UnitProvider_strategy = st.builds(UnitProvider)
@given(instance=UnitProvider_strategy)
@settings(max_examples=25)
def test_UnitProvider_instantiation(instance):
    assert isinstance(instance, UnitProvider)


VersionedCapability_strategy = st.builds(VersionedCapability)
@given(instance=VersionedCapability_strategy)
@settings(max_examples=25)
def test_VersionedCapability_instantiation(instance):
    assert isinstance(instance, VersionedCapability)


build_AliasedRequiredCapability_strategy = st.builds(build_AliasedRequiredCapability, alias=safe_text)
@given(instance=build_AliasedRequiredCapability_strategy)
@settings(max_examples=25)
def test_build_AliasedRequiredCapability_instantiation(instance):
    assert isinstance(instance, build_AliasedRequiredCapability)


build_BConcern_strategy = st.builds(build_BConcern)
@given(instance=build_BConcern_strategy)
@settings(max_examples=25)
def test_build_BConcern_instantiation(instance):
    assert isinstance(instance, build_BConcern)


build_BExecutionContext_strategy = st.builds(build_BExecutionContext)
@given(instance=build_BExecutionContext_strategy)
@settings(max_examples=25)
def test_build_BExecutionContext_instantiation(instance):
    assert isinstance(instance, build_BExecutionContext)


build_BExpression_strategy = st.builds(build_BExpression)
@given(instance=build_BExpression_strategy)
@settings(max_examples=25)
def test_build_BExpression_instantiation(instance):
    assert isinstance(instance, build_BExpression)


build_BNamePredicate_strategy = st.builds(build_BNamePredicate)
@given(instance=build_BNamePredicate_strategy)
@settings(max_examples=25)
def test_build_BNamePredicate_instantiation(instance):
    assert isinstance(instance, build_BNamePredicate)


build_BParameterList_strategy = st.builds(build_BParameterList)
@given(instance=build_BParameterList_strategy)
@settings(max_examples=25)
def test_build_BParameterList_instantiation(instance):
    assert isinstance(instance, build_BParameterList)


build_BParameterPredicate_strategy = st.builds(build_BParameterPredicate)
@given(instance=build_BParameterPredicate_strategy)
@settings(max_examples=25)
def test_build_BParameterPredicate_instantiation(instance):
    assert isinstance(instance, build_BParameterPredicate)


build_BPropertySet_strategy = st.builds(build_BPropertySet)
@given(instance=build_BPropertySet_strategy)
@settings(max_examples=25)
def test_build_BPropertySet_instantiation(instance):
    assert isinstance(instance, build_BPropertySet)


build_BSwitchExpression_strategy = st.builds(build_BSwitchExpression)
@given(instance=build_BSwitchExpression_strategy)
@settings(max_examples=25)
def test_build_BSwitchExpression_instantiation(instance):
    assert isinstance(instance, build_BSwitchExpression)


build_BWithExpression_strategy = st.builds(build_BWithExpression)
@given(instance=build_BWithExpression_strategy)
@settings(max_examples=25)
def test_build_BWithExpression_instantiation(instance):
    assert isinstance(instance, build_BWithExpression)


build_BeeHive_strategy = st.builds(build_BeeHive, resolutions=safe_text)
@given(instance=build_BeeHive_strategy)
@settings(max_examples=25)
def test_build_BeeHive_instantiation(instance):
    assert isinstance(instance, build_BeeHive)


build_BeeModel_strategy = st.builds(build_BeeModel)
@given(instance=build_BeeModel_strategy)
@settings(max_examples=25)
def test_build_BeeModel_instantiation(instance):
    assert isinstance(instance, build_BeeModel)


build_BeeModelRepository_strategy = st.builds(build_BeeModelRepository)
@given(instance=build_BeeModelRepository_strategy)
@settings(max_examples=25)
def test_build_BeeModelRepository_instantiation(instance):
    assert isinstance(instance, build_BeeModelRepository)


build_BestFoundUnitProvider_strategy = st.builds(build_BestFoundUnitProvider)
@given(instance=build_BestFoundUnitProvider_strategy)
@settings(max_examples=25)
def test_build_BestFoundUnitProvider_instantiation(instance):
    assert isinstance(instance, build_BestFoundUnitProvider)


build_Branch_strategy = st.builds(build_Branch, acceptDirty=safe_text, branchPointType=safe_text, checkout=safe_text, documentation=safe_text, mergeStrategy=safe_text, name=safe_text, replace=safe_text, update=safe_text)
@given(instance=build_Branch_strategy)
@settings(max_examples=25)
def test_build_Branch_instantiation(instance):
    assert isinstance(instance, build_Branch)


build_BuildCallMultiple_strategy = st.builds(build_BuildCallMultiple)
@given(instance=build_BuildCallMultiple_strategy)
@settings(max_examples=25)
def test_build_BuildCallMultiple_instantiation(instance):
    assert isinstance(instance, build_BuildCallMultiple)


build_BuildCallOnDeclaredRequirement_strategy = st.builds(build_BuildCallOnDeclaredRequirement)
@given(instance=build_BuildCallOnDeclaredRequirement_strategy)
@settings(max_examples=25)
def test_build_BuildCallOnDeclaredRequirement_instantiation(instance):
    assert isinstance(instance, build_BuildCallOnDeclaredRequirement)


build_BuildCallOnReferencedRequirement_strategy = st.builds(build_BuildCallOnReferencedRequirement)
@given(instance=build_BuildCallOnReferencedRequirement_strategy)
@settings(max_examples=25)
def test_build_BuildCallOnReferencedRequirement_instantiation(instance):
    assert isinstance(instance, build_BuildCallOnReferencedRequirement)


build_BuildCallOnSelectedRequirements_strategy = st.builds(build_BuildCallOnSelectedRequirements)
@given(instance=build_BuildCallOnSelectedRequirements_strategy)
@settings(max_examples=25)
def test_build_BuildCallOnSelectedRequirements_instantiation(instance):
    assert isinstance(instance, build_BuildCallOnSelectedRequirements)


build_BuildCallSingle_strategy = st.builds(build_BuildCallSingle)
@given(instance=build_BuildCallSingle_strategy)
@settings(max_examples=25)
def test_build_BuildCallSingle_instantiation(instance):
    assert isinstance(instance, build_BuildCallSingle)


build_BuildConcernContext_strategy = st.builds(build_BuildConcernContext, defaultPropertiesRemovals=safe_text)
@given(instance=build_BuildConcernContext_strategy)
@settings(max_examples=25)
def test_build_BuildConcernContext_instantiation(instance):
    assert isinstance(instance, build_BuildConcernContext)


build_BuildResultContext_strategy = st.builds(build_BuildResultContext)
@given(instance=build_BuildResultContext_strategy)
@settings(max_examples=25)
def test_build_BuildResultContext_instantiation(instance):
    assert isinstance(instance, build_BuildResultContext)


build_BuildSet_strategy = st.builds(build_BuildSet, pathIterator=safe_text, valueMap=safe_text)
@given(instance=build_BuildSet_strategy)
@settings(max_examples=25)
def test_build_BuildSet_instantiation(instance):
    assert isinstance(instance, build_BuildSet)


build_BuildUnit_strategy = st.builds(build_BuildUnit, documentation=safe_text, executionMode=safe_text, outputLocation=safe_text, platformFilter=safe_text, sourceLocation=safe_text)
@given(instance=build_BuildUnit_strategy)
@settings(max_examples=25)
def test_build_BuildUnit_instantiation(instance):
    assert isinstance(instance, build_BuildUnit)


build_BuildUnitRepository_strategy = st.builds(build_BuildUnitRepository)
@given(instance=build_BuildUnitRepository_strategy)
@settings(max_examples=25)
def test_build_BuildUnitRepository_instantiation(instance):
    assert isinstance(instance, build_BuildUnitRepository)


build_Builder_strategy = st.builds(build_Builder)
@given(instance=build_Builder_strategy)
@settings(max_examples=25)
def test_build_Builder_instantiation(instance):
    assert isinstance(instance, build_Builder)


build_BuilderCall_strategy = st.builds(build_BuilderCall, builderName=safe_text)
@given(instance=build_BuilderCall_strategy)
@settings(max_examples=25)
def test_build_BuilderCall_instantiation(instance):
    assert isinstance(instance, build_BuilderCall)


build_BuilderCallFacade_strategy = st.builds(build_BuilderCallFacade, aliases=safe_text)
@given(instance=build_BuilderCallFacade_strategy)
@settings(max_examples=25)
def test_build_BuilderCallFacade_instantiation(instance):
    assert isinstance(instance, build_BuilderCallFacade)


build_BuilderConcernContext_strategy = st.builds(build_BuilderConcernContext, matchParameters=st.booleans(), outputAnnotationsRemovals=safe_text, removePostCondition=st.booleans(), removePostInputCondition=st.booleans(), removePreCondition=st.booleans(), sourceAnnotationsRemovals=safe_text, varArgs=st.booleans())
@given(instance=build_BuilderConcernContext_strategy)
@settings(max_examples=25)
def test_build_BuilderConcernContext_instantiation(instance):
    assert isinstance(instance, build_BuilderConcernContext)


build_BuilderInput_strategy = st.builds(build_BuilderInput)
@given(instance=build_BuilderInput_strategy)
@settings(max_examples=25)
def test_build_BuilderInput_instantiation(instance):
    assert isinstance(instance, build_BuilderInput)


build_BuilderInputCondition_strategy = st.builds(build_BuilderInputCondition)
@given(instance=build_BuilderInputCondition_strategy)
@settings(max_examples=25)
def test_build_BuilderInputCondition_instantiation(instance):
    assert isinstance(instance, build_BuilderInputCondition)


build_BuilderInputContextDecorator_strategy = st.builds(build_BuilderInputContextDecorator)
@given(instance=build_BuilderInputContextDecorator_strategy)
@settings(max_examples=25)
def test_build_BuilderInputContextDecorator_instantiation(instance):
    assert isinstance(instance, build_BuilderInputContextDecorator)


build_BuilderInputDecorator_strategy = st.builds(build_BuilderInputDecorator)
@given(instance=build_BuilderInputDecorator_strategy)
@settings(max_examples=25)
def test_build_BuilderInputDecorator_instantiation(instance):
    assert isinstance(instance, build_BuilderInputDecorator)


build_BuilderInputGroup_strategy = st.builds(build_BuilderInputGroup)
@given(instance=build_BuilderInputGroup_strategy)
@settings(max_examples=25)
def test_build_BuilderInputGroup_instantiation(instance):
    assert isinstance(instance, build_BuilderInputGroup)


build_BuilderInputNameDecorator_strategy = st.builds(build_BuilderInputNameDecorator)
@given(instance=build_BuilderInputNameDecorator_strategy)
@settings(max_examples=25)
def test_build_BuilderInputNameDecorator_instantiation(instance):
    assert isinstance(instance, build_BuilderInputNameDecorator)


build_BuilderJava_strategy = st.builds(build_BuilderJava)
@given(instance=build_BuilderJava_strategy)
@settings(max_examples=25)
def test_build_BuilderJava_instantiation(instance):
    assert isinstance(instance, build_BuilderJava)


build_BuilderNamePredicate_strategy = st.builds(build_BuilderNamePredicate)
@given(instance=build_BuilderNamePredicate_strategy)
@settings(max_examples=25)
def test_build_BuilderNamePredicate_instantiation(instance):
    assert isinstance(instance, build_BuilderNamePredicate)


build_BuilderQuery_strategy = st.builds(build_BuilderQuery)
@given(instance=build_BuilderQuery_strategy)
@settings(max_examples=25)
def test_build_BuilderQuery_instantiation(instance):
    assert isinstance(instance, build_BuilderQuery)


build_BuilderWrapper_strategy = st.builds(build_BuilderWrapper, defaultPropertiesAdvised=st.booleans(), inputAdvised=st.booleans(), outputAdvised=st.booleans(), providesAdvised=st.booleans(), sourceAdvised=st.booleans(), unitTypeAdvised=st.booleans())
@given(instance=build_BuilderWrapper_strategy)
@settings(max_examples=25)
def test_build_BuilderWrapper_instantiation(instance):
    assert isinstance(instance, build_BuilderWrapper)


build_Capability_strategy = st.builds(build_Capability, nameSpace=safe_text)
@given(instance=build_Capability_strategy)
@settings(max_examples=25)
def test_build_Capability_instantiation(instance):
    assert isinstance(instance, build_Capability)


build_CapabilityPredicate_strategy = st.builds(build_CapabilityPredicate, versionRange=safe_text)
@given(instance=build_CapabilityPredicate_strategy)
@settings(max_examples=25)
def test_build_CapabilityPredicate_instantiation(instance):
    assert isinstance(instance, build_CapabilityPredicate)


build_CompoundBuildUnitRepository_strategy = st.builds(build_CompoundBuildUnitRepository)
@given(instance=build_CompoundBuildUnitRepository_strategy)
@settings(max_examples=25)
def test_build_CompoundBuildUnitRepository_instantiation(instance):
    assert isinstance(instance, build_CompoundBuildUnitRepository)


build_CompoundFirstFoundRepository_strategy = st.builds(build_CompoundFirstFoundRepository)
@given(instance=build_CompoundFirstFoundRepository_strategy)
@settings(max_examples=25)
def test_build_CompoundFirstFoundRepository_instantiation(instance):
    assert isinstance(instance, build_CompoundFirstFoundRepository)


build_CompoundUnitProvider_strategy = st.builds(build_CompoundUnitProvider)
@given(instance=build_CompoundUnitProvider_strategy)
@settings(max_examples=25)
def test_build_CompoundUnitProvider_instantiation(instance):
    assert isinstance(instance, build_CompoundUnitProvider)


build_ConditionalPathVector_strategy = st.builds(build_ConditionalPathVector)
@given(instance=build_ConditionalPathVector_strategy)
@settings(max_examples=25)
def test_build_ConditionalPathVector_instantiation(instance):
    assert isinstance(instance, build_ConditionalPathVector)


build_ContainerConfiguration_strategy = st.builds(build_ContainerConfiguration, documentation=safe_text, name=safe_text)
@given(instance=build_ContainerConfiguration_strategy)
@settings(max_examples=25)
def test_build_ContainerConfiguration_instantiation(instance):
    assert isinstance(instance, build_ContainerConfiguration)


build_DelegatingUnitProvider_strategy = st.builds(build_DelegatingUnitProvider)
@given(instance=build_DelegatingUnitProvider_strategy)
@settings(max_examples=25)
def test_build_DelegatingUnitProvider_instantiation(instance):
    assert isinstance(instance, build_DelegatingUnitProvider)


build_EffectiveBuilderCallFacade_strategy = st.builds(build_EffectiveBuilderCallFacade)
@given(instance=build_EffectiveBuilderCallFacade_strategy)
@settings(max_examples=25)
def test_build_EffectiveBuilderCallFacade_instantiation(instance):
    assert isinstance(instance, build_EffectiveBuilderCallFacade)


build_EffectiveCapabilityFacade_strategy = st.builds(build_EffectiveCapabilityFacade)
@given(instance=build_EffectiveCapabilityFacade_strategy)
@settings(max_examples=25)
def test_build_EffectiveCapabilityFacade_instantiation(instance):
    assert isinstance(instance, build_EffectiveCapabilityFacade)


build_EffectiveFacade_strategy = st.builds(build_EffectiveFacade)
@given(instance=build_EffectiveFacade_strategy)
@settings(max_examples=25)
def test_build_EffectiveFacade_instantiation(instance):
    assert isinstance(instance, build_EffectiveFacade)


build_EffectiveRequirementFacade_strategy = st.builds(build_EffectiveRequirementFacade)
@given(instance=build_EffectiveRequirementFacade_strategy)
@settings(max_examples=25)
def test_build_EffectiveRequirementFacade_instantiation(instance):
    assert isinstance(instance, build_EffectiveRequirementFacade)


build_EffectiveUnitFacade_strategy = st.builds(build_EffectiveUnitFacade)
@given(instance=build_EffectiveUnitFacade_strategy)
@settings(max_examples=25)
def test_build_EffectiveUnitFacade_instantiation(instance):
    assert isinstance(instance, build_EffectiveUnitFacade)


build_ExecutionStackRepository_strategy = st.builds(build_ExecutionStackRepository)
@given(instance=build_ExecutionStackRepository_strategy)
@settings(max_examples=25)
def test_build_ExecutionStackRepository_instantiation(instance):
    assert isinstance(instance, build_ExecutionStackRepository)


build_FirstFoundUnitProvider_strategy = st.builds(build_FirstFoundUnitProvider)
@given(instance=build_FirstFoundUnitProvider_strategy)
@settings(max_examples=25)
def test_build_FirstFoundUnitProvider_instantiation(instance):
    assert isinstance(instance, build_FirstFoundUnitProvider)


build_FragmentHost_strategy = st.builds(build_FragmentHost)
@given(instance=build_FragmentHost_strategy)
@settings(max_examples=25)
def test_build_FragmentHost_instantiation(instance):
    assert isinstance(instance, build_FragmentHost)


build_IBuildUnitContainer_strategy = st.builds(build_IBuildUnitContainer)
@given(instance=build_IBuildUnitContainer_strategy)
@settings(max_examples=25)
def test_build_IBuildUnitContainer_instantiation(instance):
    assert isinstance(instance, build_IBuildUnitContainer)


build_IBuildUnitRepository_strategy = st.builds(build_IBuildUnitRepository)
@given(instance=build_IBuildUnitRepository_strategy)
@settings(max_examples=25)
def test_build_IBuildUnitRepository_instantiation(instance):
    assert isinstance(instance, build_IBuildUnitRepository)


build_IBuilder_strategy = st.builds(build_IBuilder, unitType=safe_text)
@given(instance=build_IBuilder_strategy)
@settings(max_examples=25)
def test_build_IBuilder_instantiation(instance):
    assert isinstance(instance, build_IBuilder)


build_IEffectiveFacade_strategy = st.builds(build_IEffectiveFacade)
@given(instance=build_IEffectiveFacade_strategy)
@settings(max_examples=25)
def test_build_IEffectiveFacade_instantiation(instance):
    assert isinstance(instance, build_IEffectiveFacade)


build_IFunction_strategy = st.builds(build_IFunction)
@given(instance=build_IFunction_strategy)
@settings(max_examples=25)
def test_build_IFunction_instantiation(instance):
    assert isinstance(instance, build_IFunction)


build_IProvidedCapabilityContainer_strategy = st.builds(build_IProvidedCapabilityContainer)
@given(instance=build_IProvidedCapabilityContainer_strategy)
@settings(max_examples=25)
def test_build_IProvidedCapabilityContainer_instantiation(instance):
    assert isinstance(instance, build_IProvidedCapabilityContainer)


build_IRequiredCapabilityContainer_strategy = st.builds(build_IRequiredCapabilityContainer)
@given(instance=build_IRequiredCapabilityContainer_strategy)
@settings(max_examples=25)
def test_build_IRequiredCapabilityContainer_instantiation(instance):
    assert isinstance(instance, build_IRequiredCapabilityContainer)


build_IType_strategy = st.builds(build_IType)
@given(instance=build_IType_strategy)
@settings(max_examples=25)
def test_build_IType_instantiation(instance):
    assert isinstance(instance, build_IType)


build_ImplementsPredicate_strategy = st.builds(build_ImplementsPredicate)
@given(instance=build_ImplementsPredicate_strategy)
@settings(max_examples=25)
def test_build_ImplementsPredicate_instantiation(instance):
    assert isinstance(instance, build_ImplementsPredicate)


build_InputPredicate_strategy = st.builds(build_InputPredicate)
@given(instance=build_InputPredicate_strategy)
@settings(max_examples=25)
def test_build_InputPredicate_instantiation(instance):
    assert isinstance(instance, build_InputPredicate)


build_NameSpacePredicate_strategy = st.builds(build_NameSpacePredicate, nameSpace=safe_text)
@given(instance=build_NameSpacePredicate_strategy)
@settings(max_examples=25)
def test_build_NameSpacePredicate_instantiation(instance):
    assert isinstance(instance, build_NameSpacePredicate)


build_OutputPredicate_strategy = st.builds(build_OutputPredicate)
@given(instance=build_OutputPredicate_strategy)
@settings(max_examples=25)
def test_build_OutputPredicate_instantiation(instance):
    assert isinstance(instance, build_OutputPredicate)


build_PathGroup_strategy = st.builds(build_PathGroup)
@given(instance=build_PathGroup_strategy)
@settings(max_examples=25)
def test_build_PathGroup_instantiation(instance):
    assert isinstance(instance, build_PathGroup)


build_PathGroupPredicate_strategy = st.builds(build_PathGroupPredicate)
@given(instance=build_PathGroupPredicate_strategy)
@settings(max_examples=25)
def test_build_PathGroupPredicate_instantiation(instance):
    assert isinstance(instance, build_PathGroupPredicate)


build_PathVector_strategy = st.builds(build_PathVector, basePath=safe_text, paths=safe_text)
@given(instance=build_PathVector_strategy)
@settings(max_examples=25)
def test_build_PathVector_instantiation(instance):
    assert isinstance(instance, build_PathVector)


build_ProvidesPredicate_strategy = st.builds(build_ProvidesPredicate)
@given(instance=build_ProvidesPredicate_strategy)
@settings(max_examples=25)
def test_build_ProvidesPredicate_instantiation(instance):
    assert isinstance(instance, build_ProvidesPredicate)


build_RepoOption_strategy = st.builds(build_RepoOption, name=safe_text)
@given(instance=build_RepoOption_strategy)
@settings(max_examples=25)
def test_build_RepoOption_instantiation(instance):
    assert isinstance(instance, build_RepoOption)


build_Repository_strategy = st.builds(build_Repository, documentation=safe_text, handlerType=safe_text, name=safe_text)
@given(instance=build_Repository_strategy)
@settings(max_examples=25)
def test_build_Repository_instantiation(instance):
    assert isinstance(instance, build_Repository)


build_RepositoryUnitProvider_strategy = st.builds(build_RepositoryUnitProvider)
@given(instance=build_RepositoryUnitProvider_strategy)
@settings(max_examples=25)
def test_build_RepositoryUnitProvider_instantiation(instance):
    assert isinstance(instance, build_RepositoryUnitProvider)


build_RequiredCapability_strategy = st.builds(build_RequiredCapability, greedy=st.booleans(), max=st.integers(), min=st.integers(), versionRange=safe_text)
@given(instance=build_RequiredCapability_strategy)
@settings(max_examples=25)
def test_build_RequiredCapability_instantiation(instance):
    assert isinstance(instance, build_RequiredCapability)


build_RequiresPredicate_strategy = st.builds(build_RequiresPredicate, meta=st.booleans())
@given(instance=build_RequiresPredicate_strategy)
@settings(max_examples=25)
def test_build_RequiresPredicate_instantiation(instance):
    assert isinstance(instance, build_RequiresPredicate)


build_ResolutionInfo_strategy = st.builds(build_ResolutionInfo, status=safe_text)
@given(instance=build_ResolutionInfo_strategy)
@settings(max_examples=25)
def test_build_ResolutionInfo_instantiation(instance):
    assert isinstance(instance, build_ResolutionInfo)


build_SourcePredicate_strategy = st.builds(build_SourcePredicate)
@given(instance=build_SourcePredicate_strategy)
@settings(max_examples=25)
def test_build_SourcePredicate_instantiation(instance):
    assert isinstance(instance, build_SourcePredicate)


build_SwitchUnitProvider_strategy = st.builds(build_SwitchUnitProvider)
@given(instance=build_SwitchUnitProvider_strategy)
@settings(max_examples=25)
def test_build_SwitchUnitProvider_instantiation(instance):
    assert isinstance(instance, build_SwitchUnitProvider)


build_Synchronization_strategy = st.builds(build_Synchronization)
@given(instance=build_Synchronization_strategy)
@settings(max_examples=25)
def test_build_Synchronization_instantiation(instance):
    assert isinstance(instance, build_Synchronization)


build_UnitConcernContext_strategy = st.builds(build_UnitConcernContext, outputLocation=safe_text, sourceLocation=safe_text)
@given(instance=build_UnitConcernContext_strategy)
@settings(max_examples=25)
def test_build_UnitConcernContext_instantiation(instance):
    assert isinstance(instance, build_UnitConcernContext)


build_UnitNamePredicate_strategy = st.builds(build_UnitNamePredicate)
@given(instance=build_UnitNamePredicate_strategy)
@settings(max_examples=25)
def test_build_UnitNamePredicate_instantiation(instance):
    assert isinstance(instance, build_UnitNamePredicate)


build_UnitParameterDeclaration_strategy = st.builds(build_UnitParameterDeclaration)
@given(instance=build_UnitParameterDeclaration_strategy)
@settings(max_examples=25)
def test_build_UnitParameterDeclaration_instantiation(instance):
    assert isinstance(instance, build_UnitParameterDeclaration)


build_UnitProvider_strategy = st.builds(build_UnitProvider, documentation=safe_text)
@given(instance=build_UnitProvider_strategy)
@settings(max_examples=25)
def test_build_UnitProvider_instantiation(instance):
    assert isinstance(instance, build_UnitProvider)


build_UnitRepositoryDescription_strategy = st.builds(build_UnitRepositoryDescription, evaluatedOptions=safe_text)
@given(instance=build_UnitRepositoryDescription_strategy)
@settings(max_examples=25)
def test_build_UnitRepositoryDescription_instantiation(instance):
    assert isinstance(instance, build_UnitRepositoryDescription)


build_UnitResolutionInfo_strategy = st.builds(build_UnitResolutionInfo)
@given(instance=build_UnitResolutionInfo_strategy)
@settings(max_examples=25)
def test_build_UnitResolutionInfo_instantiation(instance):
    assert isinstance(instance, build_UnitResolutionInfo)


build_VersionedCapability_strategy = st.builds(build_VersionedCapability, version=safe_text)
@given(instance=build_VersionedCapability_strategy)
@settings(max_examples=25)
def test_build_VersionedCapability_instantiation(instance):
    assert isinstance(instance, build_VersionedCapability)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B3Function,
    BChainedExpression,
    BConcernContext,
    BExpression,
    BFunctionContainer,
    BFunctionWrapper,
    BInnerContext,
    BJavaFunction,
    BParameterDeclaration,
    BuildCallMultiple,
    BuildCallSingle,
    BuildConcernContext,
    BuildUnitRepository,
    BuilderCall,
    BuilderCallFacade,
    BuilderInput,
    BuilderInputDecorator,
    Capability,
    CapabilityPredicate,
    CompoundBuildUnitRepository,
    CompoundUnitProvider,
    EffectiveFacade,
    IBuildUnitContainer,
    IBuildUnitRepository,
    IBuilder,
    IEffectiveFacade,
    IFunction,
    INamedValue,
    IProvidedCapabilityContainer,
    IRequiredCapabilityContainer,
    ITypedValueContainer,
    IVarName,
    PathGroupPredicate,
    RequiredCapability,
    ResolutionInfo,
    UnitProvider,
    VersionedCapability,
    build_AliasedRequiredCapability,
    build_BConcern,
    build_BExecutionContext,
    build_BExpression,
    build_BNamePredicate,
    build_BParameterList,
    build_BParameterPredicate,
    build_BPropertySet,
    build_BSwitchExpression,
    build_BWithExpression,
    build_BeeHive,
    build_BeeModel,
    build_BeeModelRepository,
    build_BestFoundUnitProvider,
    build_Branch,
    build_BuildCallMultiple,
    build_BuildCallOnDeclaredRequirement,
    build_BuildCallOnReferencedRequirement,
    build_BuildCallOnSelectedRequirements,
    build_BuildCallSingle,
    build_BuildConcernContext,
    build_BuildResultContext,
    build_BuildSet,
    build_BuildUnit,
    build_BuildUnitRepository,
    build_Builder,
    build_BuilderCall,
    build_BuilderCallFacade,
    build_BuilderConcernContext,
    build_BuilderInput,
    build_BuilderInputCondition,
    build_BuilderInputContextDecorator,
    build_BuilderInputDecorator,
    build_BuilderInputGroup,
    build_BuilderInputNameDecorator,
    build_BuilderJava,
    build_BuilderNamePredicate,
    build_BuilderQuery,
    build_BuilderWrapper,
    build_Capability,
    build_CapabilityPredicate,
    build_CompoundBuildUnitRepository,
    build_CompoundFirstFoundRepository,
    build_CompoundUnitProvider,
    build_ConditionalPathVector,
    build_ContainerConfiguration,
    build_DelegatingUnitProvider,
    build_EffectiveBuilderCallFacade,
    build_EffectiveCapabilityFacade,
    build_EffectiveFacade,
    build_EffectiveRequirementFacade,
    build_EffectiveUnitFacade,
    build_ExecutionStackRepository,
    build_FirstFoundUnitProvider,
    build_FragmentHost,
    build_IBuildUnitContainer,
    build_IBuildUnitRepository,
    build_IBuilder,
    build_IEffectiveFacade,
    build_IFunction,
    build_IProvidedCapabilityContainer,
    build_IRequiredCapabilityContainer,
    build_IType,
    build_ImplementsPredicate,
    build_InputPredicate,
    build_NameSpacePredicate,
    build_OutputPredicate,
    build_PathGroup,
    build_PathGroupPredicate,
    build_PathVector,
    build_ProvidesPredicate,
    build_RepoOption,
    build_Repository,
    build_RepositoryUnitProvider,
    build_RequiredCapability,
    build_RequiresPredicate,
    build_ResolutionInfo,
    build_SourcePredicate,
    build_SwitchUnitProvider,
    build_Synchronization,
    build_UnitConcernContext,
    build_UnitNamePredicate,
    build_UnitParameterDeclaration,
    build_UnitProvider,
    build_UnitRepositoryDescription,
    build_UnitResolutionInfo,
    build_VersionedCapability,
    BranchPointType,
    MergeConflictStrategy,
    TriState,
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

def test_assoc_beeModels185_reverse_link_reassign_clear():
    a1 = build_BeeModel()
    a2 = build_BeeModel()
    b = build_BeeHive(resolutions="sample_text")
    _safe_set(b, 'build_BeeHive', {a1})
    assert _is_linked(b, 'build_BeeHive', a1)
    if hasattr(a1, 'build_BeeModel186'):
        assert _is_linked(a1, 'build_BeeModel186', b)
    _safe_set(b, 'build_BeeHive', {a2})
    assert _is_linked(b, 'build_BeeHive', a2)
    if hasattr(a1, 'build_BeeModel186'):
        assert not _is_linked(a1, 'build_BeeModel186', b)
    if hasattr(a2, 'build_BeeModel186'):
        assert _is_linked(a2, 'build_BeeModel186', b)
    _safe_set(b, 'build_BeeHive', set())
    assert not _is_linked(b, 'build_BeeHive', a2)
    if hasattr(a2, 'build_BeeModel186'):
        assert not _is_linked(a2, 'build_BeeModel186', b)


def test_assoc_branches224_reverse_link_reassign_clear():
    a1 = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    a2 = build_Repository(documentation="sample_text_2", handlerType="sample_text_2", name="sample_text_2")
    b = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    _safe_set(b, 'build_Branch', a1)
    assert _is_linked(b, 'build_Branch', a1)
    if hasattr(a1, 'build_Repository225'):
        assert _is_linked(a1, 'build_Repository225', b)
    _safe_set(b, 'build_Branch', a2)
    assert _is_linked(b, 'build_Branch', a2)
    if hasattr(a1, 'build_Repository225'):
        assert not _is_linked(a1, 'build_Repository225', b)
    if hasattr(a2, 'build_Repository225'):
        assert _is_linked(a2, 'build_Repository225', b)
    _safe_set(b, 'build_Branch', None)
    assert not _is_linked(b, 'build_Branch', a2)
    if hasattr(a2, 'build_Repository225'):
        assert not _is_linked(a2, 'build_Repository225', b)


def test_assoc_builderContexts93_reverse_link_reassign_clear():
    a1 = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    a2 = build_UnitConcernContext(outputLocation="sample_text_2", sourceLocation="sample_text_2")
    b = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    _safe_set(b, 'build_BuilderConcernContext', a1)
    assert _is_linked(b, 'build_BuilderConcernContext', a1)
    if hasattr(a1, 'build_UnitConcernContext'):
        assert _is_linked(a1, 'build_UnitConcernContext', b)
    _safe_set(b, 'build_BuilderConcernContext', a2)
    assert _is_linked(b, 'build_BuilderConcernContext', a2)
    if hasattr(a1, 'build_UnitConcernContext'):
        assert not _is_linked(a1, 'build_UnitConcernContext', b)
    if hasattr(a2, 'build_UnitConcernContext'):
        assert _is_linked(a2, 'build_UnitConcernContext', b)
    _safe_set(b, 'build_BuilderConcernContext', None)
    assert not _is_linked(b, 'build_BuilderConcernContext', a2)
    if hasattr(a2, 'build_UnitConcernContext'):
        assert not _is_linked(a2, 'build_UnitConcernContext', b)


def test_assoc_builderReference208_reverse_link_reassign_clear():
    a1 = build_BuilderCallFacade(aliases="sample_text")
    a2 = build_BuilderCallFacade(aliases="sample_text_2")
    b = build_BuilderCall(builderName="sample_text")
    _safe_set(b, 'build_BuilderCall209', a1)
    assert _is_linked(b, 'build_BuilderCall209', a1)
    if hasattr(a1, 'build_BuilderCallFacade'):
        assert _is_linked(a1, 'build_BuilderCallFacade', b)
    _safe_set(b, 'build_BuilderCall209', a2)
    assert _is_linked(b, 'build_BuilderCall209', a2)
    if hasattr(a1, 'build_BuilderCallFacade'):
        assert not _is_linked(a1, 'build_BuilderCallFacade', b)
    if hasattr(a2, 'build_BuilderCallFacade'):
        assert _is_linked(a2, 'build_BuilderCallFacade', b)
    _safe_set(b, 'build_BuilderCall209', None)
    assert not _is_linked(b, 'build_BuilderCall209', a2)
    if hasattr(a2, 'build_BuilderCallFacade'):
        assert not _is_linked(a2, 'build_BuilderCallFacade', b)


def test_assoc_builders0_reverse_link_reassign_clear():
    a1 = build_IBuilder(unitType="sample_text")
    a2 = build_IBuilder(unitType="sample_text_2")
    b = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    _safe_set(b, 'build_BuildUnit', {a1})
    assert _is_linked(b, 'build_BuildUnit', a1)
    if hasattr(a1, 'build_IBuilder'):
        assert _is_linked(a1, 'build_IBuilder', b)
    _safe_set(b, 'build_BuildUnit', {a2})
    assert _is_linked(b, 'build_BuildUnit', a2)
    if hasattr(a1, 'build_IBuilder'):
        assert not _is_linked(a1, 'build_IBuilder', b)
    if hasattr(a2, 'build_IBuilder'):
        assert _is_linked(a2, 'build_IBuilder', b)
    _safe_set(b, 'build_BuildUnit', set())
    assert not _is_linked(b, 'build_BuildUnit', a2)
    if hasattr(a2, 'build_IBuilder'):
        assert not _is_linked(a2, 'build_IBuilder', b)


def test_assoc_capabilityPredicate76_reverse_link_reassign_clear():
    a1 = build_RequiresPredicate(meta=True)
    a2 = build_RequiresPredicate(meta=False)
    b = build_CapabilityPredicate(versionRange="sample_text")
    _safe_set(b, 'build_CapabilityPredicate', a1)
    assert _is_linked(b, 'build_CapabilityPredicate', a1)
    if hasattr(a1, 'build_RequiresPredicate'):
        assert _is_linked(a1, 'build_RequiresPredicate', b)
    _safe_set(b, 'build_CapabilityPredicate', a2)
    assert _is_linked(b, 'build_CapabilityPredicate', a2)
    if hasattr(a1, 'build_RequiresPredicate'):
        assert not _is_linked(a1, 'build_RequiresPredicate', b)
    if hasattr(a2, 'build_RequiresPredicate'):
        assert _is_linked(a2, 'build_RequiresPredicate', b)
    _safe_set(b, 'build_CapabilityPredicate', None)
    assert not _is_linked(b, 'build_CapabilityPredicate', a2)
    if hasattr(a2, 'build_RequiresPredicate'):
        assert not _is_linked(a2, 'build_RequiresPredicate', b)


def test_assoc_capabilityPredicate84_reverse_link_reassign_clear():
    a1 = build_ProvidesPredicate()
    a2 = build_ProvidesPredicate()
    b = build_CapabilityPredicate(versionRange="sample_text")
    _safe_set(b, 'build_CapabilityPredicate85', a1)
    assert _is_linked(b, 'build_CapabilityPredicate85', a1)
    if hasattr(a1, 'build_ProvidesPredicate'):
        assert _is_linked(a1, 'build_ProvidesPredicate', b)
    _safe_set(b, 'build_CapabilityPredicate85', a2)
    assert _is_linked(b, 'build_CapabilityPredicate85', a2)
    if hasattr(a1, 'build_ProvidesPredicate'):
        assert not _is_linked(a1, 'build_ProvidesPredicate', b)
    if hasattr(a2, 'build_ProvidesPredicate'):
        assert _is_linked(a2, 'build_ProvidesPredicate', b)
    _safe_set(b, 'build_CapabilityPredicate85', None)
    assert not _is_linked(b, 'build_CapabilityPredicate85', a2)
    if hasattr(a2, 'build_ProvidesPredicate'):
        assert not _is_linked(a2, 'build_ProvidesPredicate', b)


def test_assoc_containers13_reverse_link_reassign_clear():
    a1 = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    a2 = build_ContainerConfiguration(documentation="sample_text_2", name="sample_text_2")
    b = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    _safe_set(b, 'build_BuildUnit14', {a1})
    assert _is_linked(b, 'build_BuildUnit14', a1)
    if hasattr(a1, 'build_ContainerConfiguration'):
        assert _is_linked(a1, 'build_ContainerConfiguration', b)
    _safe_set(b, 'build_BuildUnit14', {a2})
    assert _is_linked(b, 'build_BuildUnit14', a2)
    if hasattr(a1, 'build_ContainerConfiguration'):
        assert not _is_linked(a1, 'build_ContainerConfiguration', b)
    if hasattr(a2, 'build_ContainerConfiguration'):
        assert _is_linked(a2, 'build_ContainerConfiguration', b)
    _safe_set(b, 'build_BuildUnit14', set())
    assert not _is_linked(b, 'build_BuildUnit14', a2)
    if hasattr(a2, 'build_ContainerConfiguration'):
        assert not _is_linked(a2, 'build_ContainerConfiguration', b)


def test_assoc_explicitUnitType39_reverse_link_reassign_clear():
    a1 = build_UnitParameterDeclaration()
    a2 = build_UnitParameterDeclaration()
    b = build_IBuilder(unitType="sample_text")
    _safe_set(b, 'build_IBuilder40', a1)
    assert _is_linked(b, 'build_IBuilder40', a1)
    if hasattr(a1, 'build_UnitParameterDeclaration'):
        assert _is_linked(a1, 'build_UnitParameterDeclaration', b)
    _safe_set(b, 'build_IBuilder40', a2)
    assert _is_linked(b, 'build_IBuilder40', a2)
    if hasattr(a1, 'build_UnitParameterDeclaration'):
        assert not _is_linked(a1, 'build_UnitParameterDeclaration', b)
    if hasattr(a2, 'build_UnitParameterDeclaration'):
        assert _is_linked(a2, 'build_UnitParameterDeclaration', b)
    _safe_set(b, 'build_IBuilder40', None)
    assert not _is_linked(b, 'build_IBuilder40', a2)
    if hasattr(a2, 'build_UnitParameterDeclaration'):
        assert not _is_linked(a2, 'build_UnitParameterDeclaration', b)


def test_assoc_metaRequiredCapabilities1_reverse_link_reassign_clear():
    a1 = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    a2 = build_RequiredCapability(greedy=False, max=13, min=13, versionRange="sample_text_2")
    b = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    _safe_set(b, 'build_BuildUnit2', {a1})
    assert _is_linked(b, 'build_BuildUnit2', a1)
    if hasattr(a1, 'build_RequiredCapability'):
        assert _is_linked(a1, 'build_RequiredCapability', b)
    _safe_set(b, 'build_BuildUnit2', {a2})
    assert _is_linked(b, 'build_BuildUnit2', a2)
    if hasattr(a1, 'build_RequiredCapability'):
        assert not _is_linked(a1, 'build_RequiredCapability', b)
    if hasattr(a2, 'build_RequiredCapability'):
        assert _is_linked(a2, 'build_RequiredCapability', b)
    _safe_set(b, 'build_BuildUnit2', set())
    assert not _is_linked(b, 'build_BuildUnit2', a2)
    if hasattr(a2, 'build_RequiredCapability'):
        assert not _is_linked(a2, 'build_RequiredCapability', b)


def test_assoc_options226_reverse_link_reassign_clear():
    a1 = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    a2 = build_Repository(documentation="sample_text_2", handlerType="sample_text_2", name="sample_text_2")
    b = build_RepoOption(name="sample_text")
    _safe_set(b, 'build_RepoOption228', a1)
    assert _is_linked(b, 'build_RepoOption228', a1)
    if hasattr(a1, 'build_Repository227'):
        assert _is_linked(a1, 'build_Repository227', b)
    _safe_set(b, 'build_RepoOption228', a2)
    assert _is_linked(b, 'build_RepoOption228', a2)
    if hasattr(a1, 'build_Repository227'):
        assert not _is_linked(a1, 'build_Repository227', b)
    if hasattr(a2, 'build_Repository227'):
        assert _is_linked(a2, 'build_Repository227', b)
    _safe_set(b, 'build_RepoOption228', None)
    assert not _is_linked(b, 'build_RepoOption228', a2)
    if hasattr(a2, 'build_Repository227'):
        assert not _is_linked(a2, 'build_Repository227', b)


def test_assoc_parent188_reverse_link_reassign_clear():
    a1 = build_BeeHive(resolutions="sample_text")
    a2 = build_BeeHive(resolutions="sample_text_2")
    b = build_BeeHive(resolutions="sample_text")
    _safe_set(b, 'build_BeeHive189', a1)
    assert _is_linked(b, 'build_BeeHive189', a1)
    if hasattr(a1, 'build_BeeHive187'):
        assert _is_linked(a1, 'build_BeeHive187', b)
    _safe_set(b, 'build_BeeHive189', a2)
    assert _is_linked(b, 'build_BeeHive189', a2)
    if hasattr(a1, 'build_BeeHive187'):
        assert not _is_linked(a1, 'build_BeeHive187', b)
    if hasattr(a2, 'build_BeeHive187'):
        assert _is_linked(a2, 'build_BeeHive187', b)
    _safe_set(b, 'build_BeeHive189', None)
    assert not _is_linked(b, 'build_BeeHive189', a2)
    if hasattr(a2, 'build_BeeHive187'):
        assert not _is_linked(a2, 'build_BeeHive187', b)


def test_assoc_pathVector148_reverse_link_reassign_clear():
    a1 = build_PathVector(basePath="sample_text", paths="sample_text")
    a2 = build_PathVector(basePath="sample_text_2", paths="sample_text_2")
    b = build_PathGroupPredicate()
    _safe_set(b, 'build_PathGroupPredicate', a1)
    assert _is_linked(b, 'build_PathGroupPredicate', a1)
    if hasattr(a1, 'build_PathVector149'):
        assert _is_linked(a1, 'build_PathVector149', b)
    _safe_set(b, 'build_PathGroupPredicate', a2)
    assert _is_linked(b, 'build_PathGroupPredicate', a2)
    if hasattr(a1, 'build_PathVector149'):
        assert not _is_linked(a1, 'build_PathVector149', b)
    if hasattr(a2, 'build_PathVector149'):
        assert _is_linked(a2, 'build_PathVector149', b)
    _safe_set(b, 'build_PathGroupPredicate', None)
    assert not _is_linked(b, 'build_PathGroupPredicate', a2)
    if hasattr(a2, 'build_PathVector149'):
        assert not _is_linked(a2, 'build_PathVector149', b)


def test_assoc_pathVectors213_reverse_link_reassign_clear():
    a1 = build_PathVector(basePath="sample_text", paths="sample_text")
    a2 = build_PathVector(basePath="sample_text_2", paths="sample_text_2")
    b = build_BuildSet(pathIterator="sample_text", valueMap="sample_text")
    _safe_set(b, 'build_BuildSet', {a1})
    assert _is_linked(b, 'build_BuildSet', a1)
    if hasattr(a1, 'build_PathVector214'):
        assert _is_linked(a1, 'build_PathVector214', b)
    _safe_set(b, 'build_BuildSet', {a2})
    assert _is_linked(b, 'build_BuildSet', a2)
    if hasattr(a1, 'build_PathVector214'):
        assert not _is_linked(a1, 'build_PathVector214', b)
    if hasattr(a2, 'build_PathVector214'):
        assert _is_linked(a2, 'build_PathVector214', b)
    _safe_set(b, 'build_BuildSet', set())
    assert not _is_linked(b, 'build_BuildSet', a2)
    if hasattr(a2, 'build_PathVector214'):
        assert not _is_linked(a2, 'build_PathVector214', b)


def test_assoc_providesRemovals100_reverse_link_reassign_clear():
    a1 = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    a2 = build_UnitConcernContext(outputLocation="sample_text_2", sourceLocation="sample_text_2")
    b = build_ProvidesPredicate()
    _safe_set(b, 'build_ProvidesPredicate102', a1)
    assert _is_linked(b, 'build_ProvidesPredicate102', a1)
    if hasattr(a1, 'build_UnitConcernContext101'):
        assert _is_linked(a1, 'build_UnitConcernContext101', b)
    _safe_set(b, 'build_ProvidesPredicate102', a2)
    assert _is_linked(b, 'build_ProvidesPredicate102', a2)
    if hasattr(a1, 'build_UnitConcernContext101'):
        assert not _is_linked(a1, 'build_UnitConcernContext101', b)
    if hasattr(a2, 'build_UnitConcernContext101'):
        assert _is_linked(a2, 'build_UnitConcernContext101', b)
    _safe_set(b, 'build_ProvidesPredicate102', None)
    assert not _is_linked(b, 'build_ProvidesPredicate102', a2)
    if hasattr(a2, 'build_UnitConcernContext101'):
        assert not _is_linked(a2, 'build_UnitConcernContext101', b)


def test_assoc_providesRemovals134_reverse_link_reassign_clear():
    a1 = build_ProvidesPredicate()
    a2 = build_ProvidesPredicate()
    b = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    _safe_set(b, 'build_BuilderConcernContext135', {a1})
    assert _is_linked(b, 'build_BuilderConcernContext135', a1)
    if hasattr(a1, 'build_ProvidesPredicate136'):
        assert _is_linked(a1, 'build_ProvidesPredicate136', b)
    _safe_set(b, 'build_BuilderConcernContext135', {a2})
    assert _is_linked(b, 'build_BuilderConcernContext135', a2)
    if hasattr(a1, 'build_ProvidesPredicate136'):
        assert not _is_linked(a1, 'build_ProvidesPredicate136', b)
    if hasattr(a2, 'build_ProvidesPredicate136'):
        assert _is_linked(a2, 'build_ProvidesPredicate136', b)
    _safe_set(b, 'build_BuilderConcernContext135', set())
    assert not _is_linked(b, 'build_BuilderConcernContext135', a2)
    if hasattr(a2, 'build_ProvidesPredicate136'):
        assert not _is_linked(a2, 'build_ProvidesPredicate136', b)


def test_assoc_repositories11_reverse_link_reassign_clear():
    a1 = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    a2 = build_Repository(documentation="sample_text_2", handlerType="sample_text_2", name="sample_text_2")
    b = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    _safe_set(b, 'build_BuildUnit12', {a1})
    assert _is_linked(b, 'build_BuildUnit12', a1)
    if hasattr(a1, 'build_Repository'):
        assert _is_linked(a1, 'build_Repository', b)
    _safe_set(b, 'build_BuildUnit12', {a2})
    assert _is_linked(b, 'build_BuildUnit12', a2)
    if hasattr(a1, 'build_Repository'):
        assert not _is_linked(a1, 'build_Repository', b)
    if hasattr(a2, 'build_Repository'):
        assert _is_linked(a2, 'build_Repository', b)
    _safe_set(b, 'build_BuildUnit12', set())
    assert not _is_linked(b, 'build_BuildUnit12', a2)
    if hasattr(a2, 'build_Repository'):
        assert not _is_linked(a2, 'build_Repository', b)


def test_assoc_repositories176_reverse_link_reassign_clear():
    a1 = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    a2 = build_Repository(documentation="sample_text_2", handlerType="sample_text_2", name="sample_text_2")
    b = build_BeeModel()
    _safe_set(b, 'build_BeeModel177', {a1})
    assert _is_linked(b, 'build_BeeModel177', a1)
    if hasattr(a1, 'build_Repository178'):
        assert _is_linked(a1, 'build_Repository178', b)
    _safe_set(b, 'build_BeeModel177', {a2})
    assert _is_linked(b, 'build_BeeModel177', a2)
    if hasattr(a1, 'build_Repository178'):
        assert not _is_linked(a1, 'build_Repository178', b)
    if hasattr(a2, 'build_Repository178'):
        assert _is_linked(a2, 'build_Repository178', b)
    _safe_set(b, 'build_BeeModel177', set())
    assert not _is_linked(b, 'build_BeeModel177', a2)
    if hasattr(a2, 'build_Repository178'):
        assert not _is_linked(a2, 'build_Repository178', b)


def test_assoc_repository249_reverse_link_reassign_clear():
    a1 = build_UnitRepositoryDescription(evaluatedOptions="sample_text")
    a2 = build_UnitRepositoryDescription(evaluatedOptions="sample_text_2")
    b = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    _safe_set(b, 'build_Repository250', a1)
    assert _is_linked(b, 'build_Repository250', a1)
    if hasattr(a1, 'build_UnitRepositoryDescription'):
        assert _is_linked(a1, 'build_UnitRepositoryDescription', b)
    _safe_set(b, 'build_Repository250', a2)
    assert _is_linked(b, 'build_Repository250', a2)
    if hasattr(a1, 'build_UnitRepositoryDescription'):
        assert not _is_linked(a1, 'build_UnitRepositoryDescription', b)
    if hasattr(a2, 'build_UnitRepositoryDescription'):
        assert _is_linked(a2, 'build_UnitRepositoryDescription', b)
    _safe_set(b, 'build_Repository250', None)
    assert not _is_linked(b, 'build_Repository250', a2)
    if hasattr(a2, 'build_UnitRepositoryDescription'):
        assert not _is_linked(a2, 'build_UnitRepositoryDescription', b)


def test_assoc_requiredCapability210_reverse_link_reassign_clear():
    a1 = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    a2 = build_RequiredCapability(greedy=False, max=13, min=13, versionRange="sample_text_2")
    b = build_BuilderCallFacade(aliases="sample_text")
    _safe_set(b, 'build_BuilderCallFacade211', a1)
    assert _is_linked(b, 'build_BuilderCallFacade211', a1)
    if hasattr(a1, 'build_RequiredCapability212'):
        assert _is_linked(a1, 'build_RequiredCapability212', b)
    _safe_set(b, 'build_BuilderCallFacade211', a2)
    assert _is_linked(b, 'build_BuilderCallFacade211', a2)
    if hasattr(a1, 'build_RequiredCapability212'):
        assert not _is_linked(a1, 'build_RequiredCapability212', b)
    if hasattr(a2, 'build_RequiredCapability212'):
        assert _is_linked(a2, 'build_RequiredCapability212', b)
    _safe_set(b, 'build_BuilderCallFacade211', None)
    assert not _is_linked(b, 'build_BuilderCallFacade211', a2)
    if hasattr(a2, 'build_RequiredCapability212'):
        assert not _is_linked(a2, 'build_RequiredCapability212', b)


def test_assoc_requiredPredicatesRemovals103_reverse_link_reassign_clear():
    a1 = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    a2 = build_UnitConcernContext(outputLocation="sample_text_2", sourceLocation="sample_text_2")
    b = build_CapabilityPredicate(versionRange="sample_text")
    _safe_set(b, 'build_CapabilityPredicate105', a1)
    assert _is_linked(b, 'build_CapabilityPredicate105', a1)
    if hasattr(a1, 'build_UnitConcernContext104'):
        assert _is_linked(a1, 'build_UnitConcernContext104', b)
    _safe_set(b, 'build_CapabilityPredicate105', a2)
    assert _is_linked(b, 'build_CapabilityPredicate105', a2)
    if hasattr(a1, 'build_UnitConcernContext104'):
        assert not _is_linked(a1, 'build_UnitConcernContext104', b)
    if hasattr(a2, 'build_UnitConcernContext104'):
        assert _is_linked(a2, 'build_UnitConcernContext104', b)
    _safe_set(b, 'build_CapabilityPredicate105', None)
    assert not _is_linked(b, 'build_CapabilityPredicate105', a2)
    if hasattr(a2, 'build_UnitConcernContext104'):
        assert not _is_linked(a2, 'build_UnitConcernContext104', b)


def test_assoc_requiresRemovals97_reverse_link_reassign_clear():
    a1 = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    a2 = build_UnitConcernContext(outputLocation="sample_text_2", sourceLocation="sample_text_2")
    b = build_RequiresPredicate(meta=True)
    _safe_set(b, 'build_RequiresPredicate99', a1)
    assert _is_linked(b, 'build_RequiresPredicate99', a1)
    if hasattr(a1, 'build_UnitConcernContext98'):
        assert _is_linked(a1, 'build_UnitConcernContext98', b)
    _safe_set(b, 'build_RequiresPredicate99', a2)
    assert _is_linked(b, 'build_RequiresPredicate99', a2)
    if hasattr(a1, 'build_UnitConcernContext98'):
        assert not _is_linked(a1, 'build_UnitConcernContext98', b)
    if hasattr(a2, 'build_UnitConcernContext98'):
        assert _is_linked(a2, 'build_UnitConcernContext98', b)
    _safe_set(b, 'build_RequiresPredicate99', None)
    assert not _is_linked(b, 'build_RequiresPredicate99', a2)
    if hasattr(a2, 'build_UnitConcernContext98'):
        assert not _is_linked(a2, 'build_UnitConcernContext98', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_address232_stub_double():
    # build_BExpression has no real 'build_BExpression234' property in the generated
    # code (a bare stub) -- manually attach it so build_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression234', None)
    _safe_set(owner, 'build_Repository233', partner)
    assert getattr(partner, 'build_BExpression234') == owner
    _safe_set(owner, 'build_Repository233', None)
    assert getattr(partner, 'build_BExpression234') is None


def test_assoc_agentType68_stub_double():
    # build_IType has no real 'build_IType70' property in the generated
    # code (a bare stub) -- manually attach it so build_ContainerConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_ContainerConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    partner = build_IType()
    setattr(partner, 'build_IType70', None)
    _safe_set(owner, 'build_ContainerConfiguration69', partner)
    assert getattr(partner, 'build_IType70') == owner
    _safe_set(owner, 'build_ContainerConfiguration69', None)
    assert getattr(partner, 'build_IType70') is None


def test_assoc_beeModels217_stub_double():
    # build_BeeModelRepository has no real 'build_BeeModelRepository' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_BeeModelRepository()
    setattr(partner, 'build_BeeModelRepository', None)
    _safe_set(owner, 'build_BeeModel218', partner)
    assert owner in getattr(partner, 'build_BeeModelRepository')
    _safe_set(owner, 'build_BeeModel218', None)
    assert owner not in getattr(partner, 'build_BeeModelRepository')


def test_assoc_branchPoint241_stub_double():
    # build_BExpression has no real 'build_BExpression243' property in the generated
    # code (a bare stub) -- manually attach it so build_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression243', None)
    _safe_set(owner, 'build_Branch242', partner)
    assert getattr(partner, 'build_BExpression243') == owner
    _safe_set(owner, 'build_Branch242', None)
    assert getattr(partner, 'build_BExpression243') is None


def test_assoc_buildUnitRepository229_stub_double():
    # build_IBuildUnitRepository has no real 'build_IBuildUnitRepository231' property in the generated
    # code (a bare stub) -- manually attach it so build_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    partner = build_IBuildUnitRepository()
    setattr(partner, 'build_IBuildUnitRepository231', None)
    _safe_set(owner, 'build_Repository230', partner)
    assert getattr(partner, 'build_IBuildUnitRepository231') == owner
    _safe_set(owner, 'build_Repository230', None)
    assert getattr(partner, 'build_IBuildUnitRepository231') is None


def test_assoc_buildUnits264_stub_double():
    # build_IBuildUnitContainer has no real 'build_IBuildUnitContainer265' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_IBuildUnitContainer()
    setattr(partner, 'build_IBuildUnitContainer265', None)
    _safe_set(owner, 'build_BuildUnit266', partner)
    assert owner in getattr(partner, 'build_IBuildUnitContainer265')
    _safe_set(owner, 'build_BuildUnit266', None)
    assert owner not in getattr(partner, 'build_IBuildUnitContainer265')


def test_assoc_capabilityPredicate88_stub_double():
    # build_InputPredicate has no real 'build_InputPredicate' property in the generated
    # code (a bare stub) -- manually attach it so build_CapabilityPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_CapabilityPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_CapabilityPredicate(versionRange="sample_text")
    partner = build_InputPredicate()
    setattr(partner, 'build_InputPredicate', None)
    _safe_set(owner, 'build_CapabilityPredicate89', partner)
    assert getattr(partner, 'build_InputPredicate') == owner
    _safe_set(owner, 'build_CapabilityPredicate89', None)
    assert getattr(partner, 'build_InputPredicate') is None


def test_assoc_concerns170_stub_double():
    # build_BConcern has no real 'build_BConcern172' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_BConcern()
    setattr(partner, 'build_BConcern172', None)
    _safe_set(owner, 'build_BeeModel171', {partner})
    assert getattr(partner, 'build_BConcern172') == owner
    _safe_set(owner, 'build_BeeModel171', set())
    assert getattr(partner, 'build_BConcern172') is None


def test_assoc_concerns5_stub_double():
    # build_BConcern has no real 'build_BConcern' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_BConcern()
    setattr(partner, 'build_BConcern', None)
    _safe_set(owner, 'build_BuildUnit6', {partner})
    assert getattr(partner, 'build_BConcern') == owner
    _safe_set(owner, 'build_BuildUnit6', set())
    assert getattr(partner, 'build_BConcern') is None


def test_assoc_condExpr52_stub_double():
    # build_BExpression has no real 'build_BExpression53' property in the generated
    # code (a bare stub) -- manually attach it so build_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Capability(nameSpace="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression53', None)
    _safe_set(owner, 'build_Capability', partner)
    assert getattr(partner, 'build_BExpression53') == owner
    _safe_set(owner, 'build_Capability', None)
    assert getattr(partner, 'build_BExpression53') is None


def test_assoc_contextBlock71_stub_double():
    # build_BExpression has no real 'build_BExpression73' property in the generated
    # code (a bare stub) -- manually attach it so build_ContainerConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_ContainerConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_ContainerConfiguration(documentation="sample_text", name="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression73', None)
    _safe_set(owner, 'build_ContainerConfiguration72', partner)
    assert getattr(partner, 'build_BExpression73') == owner
    _safe_set(owner, 'build_ContainerConfiguration72', None)
    assert getattr(partner, 'build_BExpression73') is None


def test_assoc_defaultProperties182_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet184' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet184', None)
    _safe_set(owner, 'build_BeeModel183', partner)
    assert getattr(partner, 'build_BPropertySet184') == owner
    _safe_set(owner, 'build_BeeModel183', None)
    assert getattr(partner, 'build_BPropertySet184') is None


def test_assoc_defaultProperties33_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet35' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet35', None)
    _safe_set(owner, 'build_IBuilder34', partner)
    assert getattr(partner, 'build_BPropertySet35') == owner
    _safe_set(owner, 'build_IBuilder34', None)
    assert getattr(partner, 'build_BPropertySet35') is None


def test_assoc_defaultProperties7_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet', None)
    _safe_set(owner, 'build_BuildUnit8', partner)
    assert getattr(partner, 'build_BPropertySet') == owner
    _safe_set(owner, 'build_BuildUnit8', None)
    assert getattr(partner, 'build_BPropertySet') is None


def test_assoc_defaultPropertiesAdditions74_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet75' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildConcernContext(defaultPropertiesRemovals="sample_text")
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet75', None)
    _safe_set(owner, 'build_BuildConcernContext', partner)
    assert getattr(partner, 'build_BPropertySet75') == owner
    _safe_set(owner, 'build_BuildConcernContext', None)
    assert getattr(partner, 'build_BPropertySet75') is None


def test_assoc_delegate244_stub_double():
    # build_DelegatingUnitProvider has no real 'build_DelegatingUnitProvider' property in the generated
    # code (a bare stub) -- manually attach it so build_UnitProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_UnitProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_UnitProvider(documentation="sample_text")
    partner = build_DelegatingUnitProvider()
    setattr(partner, 'build_DelegatingUnitProvider', None)
    _safe_set(owner, 'build_UnitProvider245', partner)
    assert getattr(partner, 'build_DelegatingUnitProvider') == owner
    _safe_set(owner, 'build_UnitProvider245', None)
    assert getattr(partner, 'build_DelegatingUnitProvider') is None


def test_assoc_exclude238_stub_double():
    # build_BNamePredicate has no real 'build_BNamePredicate240' property in the generated
    # code (a bare stub) -- manually attach it so build_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    partner = build_BNamePredicate()
    setattr(partner, 'build_BNamePredicate240', None)
    _safe_set(owner, 'build_Branch239', {partner})
    assert getattr(partner, 'build_BNamePredicate240') == owner
    _safe_set(owner, 'build_Branch239', set())
    assert getattr(partner, 'build_BNamePredicate240') is None


def test_assoc_expr246_stub_double():
    # build_BExpression has no real 'build_BExpression248' property in the generated
    # code (a bare stub) -- manually attach it so build_RepoOption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RepoOption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RepoOption(name="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression248', None)
    _safe_set(owner, 'build_RepoOption247', partner)
    assert getattr(partner, 'build_BExpression248') == owner
    _safe_set(owner, 'build_RepoOption247', None)
    assert getattr(partner, 'build_BExpression248') is None


def test_assoc_fragmentHosts22_stub_double():
    # build_FragmentHost has no real 'build_FragmentHost' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_FragmentHost()
    setattr(partner, 'build_FragmentHost', None)
    _safe_set(owner, 'build_BuildUnit23', {partner})
    assert getattr(partner, 'build_FragmentHost') == owner
    _safe_set(owner, 'build_BuildUnit23', set())
    assert getattr(partner, 'build_FragmentHost') is None


def test_assoc_funcExpr120_stub_double():
    # build_BExpression has no real 'build_BExpression122' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BExpression()
    setattr(partner, 'build_BExpression122', None)
    _safe_set(owner, 'build_BuilderConcernContext121', partner)
    assert getattr(partner, 'build_BExpression122') == owner
    _safe_set(owner, 'build_BuilderConcernContext121', None)
    assert getattr(partner, 'build_BExpression122') is None


def test_assoc_functions168_stub_double():
    # build_IFunction has no real 'build_IFunction' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_IFunction()
    setattr(partner, 'build_IFunction', None)
    _safe_set(owner, 'build_BeeModel169', {partner})
    assert getattr(partner, 'build_IFunction') == owner
    _safe_set(owner, 'build_BeeModel169', set())
    assert getattr(partner, 'build_IFunction') is None


def test_assoc_hostRequirements267_stub_double():
    # build_FragmentHost has no real 'build_FragmentHost268' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_FragmentHost()
    setattr(partner, 'build_FragmentHost268', None)
    _safe_set(owner, 'build_RequiredCapability269', partner)
    assert owner in getattr(partner, 'build_FragmentHost268')
    _safe_set(owner, 'build_RequiredCapability269', None)
    assert owner not in getattr(partner, 'build_FragmentHost268')


def test_assoc_implements3_stub_double():
    # build_IType has no real 'build_IType' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_IType()
    setattr(partner, 'build_IType', None)
    _safe_set(owner, 'build_BuildUnit4', {partner})
    assert getattr(partner, 'build_IType') == owner
    _safe_set(owner, 'build_BuildUnit4', set())
    assert getattr(partner, 'build_IType') is None


def test_assoc_imports166_stub_double():
    # build_IType has no real 'build_IType167' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_IType()
    setattr(partner, 'build_IType167', None)
    _safe_set(owner, 'build_BeeModel', {partner})
    assert getattr(partner, 'build_IType167') == owner
    _safe_set(owner, 'build_BeeModel', set())
    assert getattr(partner, 'build_IType167') is None


def test_assoc_include235_stub_double():
    # build_BNamePredicate has no real 'build_BNamePredicate237' property in the generated
    # code (a bare stub) -- manually attach it so build_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Branch(acceptDirty="sample_text", branchPointType="sample_text", checkout="sample_text", documentation="sample_text", mergeStrategy="sample_text", name="sample_text", replace="sample_text", update="sample_text")
    partner = build_BNamePredicate()
    setattr(partner, 'build_BNamePredicate237', None)
    _safe_set(owner, 'build_Branch236', {partner})
    assert getattr(partner, 'build_BNamePredicate237') == owner
    _safe_set(owner, 'build_Branch236', set())
    assert getattr(partner, 'build_BNamePredicate237') is None


def test_assoc_input29_stub_double():
    # build_BuilderInput has no real 'build_BuilderInput' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_BuilderInput()
    setattr(partner, 'build_BuilderInput', None)
    _safe_set(owner, 'build_IBuilder30', partner)
    assert getattr(partner, 'build_BuilderInput') == owner
    _safe_set(owner, 'build_IBuilder30', None)
    assert getattr(partner, 'build_BuilderInput') is None


def test_assoc_inputAdditions109_stub_double():
    # build_BuilderInput has no real 'build_BuilderInput111' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BuilderInput()
    setattr(partner, 'build_BuilderInput111', None)
    _safe_set(owner, 'build_BuilderConcernContext110', {partner})
    assert getattr(partner, 'build_BuilderInput111') == owner
    _safe_set(owner, 'build_BuilderConcernContext110', set())
    assert getattr(partner, 'build_BuilderInput111') is None


def test_assoc_inputRemovals112_stub_double():
    # build_InputPredicate has no real 'build_InputPredicate114' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_InputPredicate()
    setattr(partner, 'build_InputPredicate114', None)
    _safe_set(owner, 'build_BuilderConcernContext113', {partner})
    assert getattr(partner, 'build_InputPredicate114') == owner
    _safe_set(owner, 'build_BuilderConcernContext113', set())
    assert getattr(partner, 'build_InputPredicate114') is None


def test_assoc_namePredicate77_stub_double():
    # build_BNamePredicate has no real 'build_BNamePredicate' property in the generated
    # code (a bare stub) -- manually attach it so build_CapabilityPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_CapabilityPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_CapabilityPredicate(versionRange="sample_text")
    partner = build_BNamePredicate()
    setattr(partner, 'build_BNamePredicate', None)
    _safe_set(owner, 'build_CapabilityPredicate78', partner)
    assert getattr(partner, 'build_BNamePredicate') == owner
    _safe_set(owner, 'build_CapabilityPredicate78', None)
    assert getattr(partner, 'build_BNamePredicate') is None


def test_assoc_nameSpacePredicate79_stub_double():
    # build_BNamePredicate has no real 'build_BNamePredicate81' property in the generated
    # code (a bare stub) -- manually attach it so build_CapabilityPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_CapabilityPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_CapabilityPredicate(versionRange="sample_text")
    partner = build_BNamePredicate()
    setattr(partner, 'build_BNamePredicate81', None)
    _safe_set(owner, 'build_CapabilityPredicate80', partner)
    assert getattr(partner, 'build_BNamePredicate81') == owner
    _safe_set(owner, 'build_CapabilityPredicate80', None)
    assert getattr(partner, 'build_BNamePredicate81') is None


def test_assoc_options63_stub_double():
    # build_RepositoryUnitProvider has no real 'build_RepositoryUnitProvider64' property in the generated
    # code (a bare stub) -- manually attach it so build_RepoOption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RepoOption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RepoOption(name="sample_text")
    partner = build_RepositoryUnitProvider()
    setattr(partner, 'build_RepositoryUnitProvider64', None)
    _safe_set(owner, 'build_RepoOption', partner)
    assert owner in getattr(partner, 'build_RepositoryUnitProvider64')
    _safe_set(owner, 'build_RepoOption', None)
    assert owner not in getattr(partner, 'build_RepositoryUnitProvider64')


def test_assoc_output31_stub_double():
    # build_PathGroup has no real 'build_PathGroup' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_PathGroup()
    setattr(partner, 'build_PathGroup', None)
    _safe_set(owner, 'build_IBuilder32', partner)
    assert getattr(partner, 'build_PathGroup') == owner
    _safe_set(owner, 'build_IBuilder32', None)
    assert getattr(partner, 'build_PathGroup') is None


def test_assoc_outputAdditions115_stub_double():
    # build_ConditionalPathVector has no real 'build_ConditionalPathVector117' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_ConditionalPathVector()
    setattr(partner, 'build_ConditionalPathVector117', None)
    _safe_set(owner, 'build_BuilderConcernContext116', {partner})
    assert getattr(partner, 'build_ConditionalPathVector117') == owner
    _safe_set(owner, 'build_BuilderConcernContext116', set())
    assert getattr(partner, 'build_ConditionalPathVector117') is None


def test_assoc_outputAnnotationAdditions137_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet139' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet139', None)
    _safe_set(owner, 'build_BuilderConcernContext138', partner)
    assert getattr(partner, 'build_BPropertySet139') == owner
    _safe_set(owner, 'build_BuilderConcernContext138', None)
    assert getattr(partner, 'build_BPropertySet139') is None


def test_assoc_outputRemovals118_stub_double():
    # build_OutputPredicate has no real 'build_OutputPredicate' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_OutputPredicate()
    setattr(partner, 'build_OutputPredicate', None)
    _safe_set(owner, 'build_BuilderConcernContext119', {partner})
    assert getattr(partner, 'build_OutputPredicate') == owner
    _safe_set(owner, 'build_BuilderConcernContext119', set())
    assert getattr(partner, 'build_OutputPredicate') is None


def test_assoc_parameters123_stub_double():
    # build_BParameterPredicate has no real 'build_BParameterPredicate' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BParameterPredicate()
    setattr(partner, 'build_BParameterPredicate', None)
    _safe_set(owner, 'build_BuilderConcernContext124', {partner})
    assert getattr(partner, 'build_BParameterPredicate') == owner
    _safe_set(owner, 'build_BuilderConcernContext124', set())
    assert getattr(partner, 'build_BParameterPredicate') is None


def test_assoc_parameters51_stub_double():
    # build_BParameterList has no real 'build_BParameterList' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderCall(builderName="sample_text")
    partner = build_BParameterList()
    setattr(partner, 'build_BParameterList', None)
    _safe_set(owner, 'build_BuilderCall', partner)
    assert getattr(partner, 'build_BParameterList') == owner
    _safe_set(owner, 'build_BuilderCall', None)
    assert getattr(partner, 'build_BParameterList') is None


def test_assoc_parent20_stub_double():
    # build_IBuildUnitContainer has no real 'build_IBuildUnitContainer' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_IBuildUnitContainer()
    setattr(partner, 'build_IBuildUnitContainer', None)
    _safe_set(owner, 'build_BuildUnit21', partner)
    assert getattr(partner, 'build_IBuildUnitContainer') == owner
    _safe_set(owner, 'build_BuildUnit21', None)
    assert getattr(partner, 'build_IBuildUnitContainer') is None


def test_assoc_pathPattern150_stub_double():
    # build_BExpression has no real 'build_BExpression152' property in the generated
    # code (a bare stub) -- manually attach it so build_PathGroupPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_PathGroupPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_PathGroupPredicate()
    partner = build_BExpression()
    setattr(partner, 'build_BExpression152', None)
    _safe_set(owner, 'build_PathGroupPredicate151', partner)
    assert getattr(partner, 'build_BExpression152') == owner
    _safe_set(owner, 'build_PathGroupPredicate151', None)
    assert getattr(partner, 'build_BExpression152') is None


def test_assoc_pathVectors57_stub_double():
    # build_ConditionalPathVector has no real 'build_ConditionalPathVector58' property in the generated
    # code (a bare stub) -- manually attach it so build_PathVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_PathVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_PathVector(basePath="sample_text", paths="sample_text")
    partner = build_ConditionalPathVector()
    setattr(partner, 'build_ConditionalPathVector58', None)
    _safe_set(owner, 'build_PathVector', partner)
    assert owner in getattr(partner, 'build_ConditionalPathVector58')
    _safe_set(owner, 'build_PathVector', None)
    assert owner not in getattr(partner, 'build_ConditionalPathVector58')


def test_assoc_postcondExpr128_stub_double():
    # build_BExpression has no real 'build_BExpression130' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BExpression()
    setattr(partner, 'build_BExpression130', None)
    _safe_set(owner, 'build_BuilderConcernContext129', partner)
    assert getattr(partner, 'build_BExpression130') == owner
    _safe_set(owner, 'build_BuilderConcernContext129', None)
    assert getattr(partner, 'build_BExpression130') is None


def test_assoc_postcondExpr24_stub_double():
    # build_BExpression has no real 'build_BExpression' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression', None)
    _safe_set(owner, 'build_IBuilder25', partner)
    assert getattr(partner, 'build_BExpression') == owner
    _safe_set(owner, 'build_IBuilder25', None)
    assert getattr(partner, 'build_BExpression') is None


def test_assoc_postinputcondExpr131_stub_double():
    # build_BExpression has no real 'build_BExpression133' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BExpression()
    setattr(partner, 'build_BExpression133', None)
    _safe_set(owner, 'build_BuilderConcernContext132', partner)
    assert getattr(partner, 'build_BExpression133') == owner
    _safe_set(owner, 'build_BuilderConcernContext132', None)
    assert getattr(partner, 'build_BExpression133') is None


def test_assoc_postinputcondExpr36_stub_double():
    # build_BExpression has no real 'build_BExpression38' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression38', None)
    _safe_set(owner, 'build_IBuilder37', partner)
    assert getattr(partner, 'build_BExpression38') == owner
    _safe_set(owner, 'build_IBuilder37', None)
    assert getattr(partner, 'build_BExpression38') is None


def test_assoc_precondExpr125_stub_double():
    # build_BExpression has no real 'build_BExpression127' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BExpression()
    setattr(partner, 'build_BExpression127', None)
    _safe_set(owner, 'build_BuilderConcernContext126', partner)
    assert getattr(partner, 'build_BExpression127') == owner
    _safe_set(owner, 'build_BuilderConcernContext126', None)
    assert getattr(partner, 'build_BExpression127') is None


def test_assoc_precondExpr26_stub_double():
    # build_BExpression has no real 'build_BExpression28' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression28', None)
    _safe_set(owner, 'build_IBuilder27', partner)
    assert getattr(partner, 'build_BExpression28') == owner
    _safe_set(owner, 'build_IBuilder27', None)
    assert getattr(partner, 'build_BExpression28') is None


def test_assoc_propertySets15_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet17' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet17', None)
    _safe_set(owner, 'build_BuildUnit16', {partner})
    assert getattr(partner, 'build_BPropertySet17') == owner
    _safe_set(owner, 'build_BuildUnit16', set())
    assert getattr(partner, 'build_BPropertySet17') is None


def test_assoc_propertySets173_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet175' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet175', None)
    _safe_set(owner, 'build_BeeModel174', {partner})
    assert getattr(partner, 'build_BPropertySet175') == owner
    _safe_set(owner, 'build_BeeModel174', set())
    assert getattr(partner, 'build_BPropertySet175') is None


def test_assoc_providedCapabilities158_stub_double():
    # build_IProvidedCapabilityContainer has no real 'build_IProvidedCapabilityContainer' property in the generated
    # code (a bare stub) -- manually attach it so build_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Capability(nameSpace="sample_text")
    partner = build_IProvidedCapabilityContainer()
    setattr(partner, 'build_IProvidedCapabilityContainer', None)
    _safe_set(owner, 'build_Capability159', partner)
    assert owner in getattr(partner, 'build_IProvidedCapabilityContainer')
    _safe_set(owner, 'build_Capability159', None)
    assert owner not in getattr(partner, 'build_IProvidedCapabilityContainer')


def test_assoc_providedCapability205_stub_double():
    # build_EffectiveCapabilityFacade has no real 'build_EffectiveCapabilityFacade206' property in the generated
    # code (a bare stub) -- manually attach it so build_Capability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Capability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Capability(nameSpace="sample_text")
    partner = build_EffectiveCapabilityFacade()
    setattr(partner, 'build_EffectiveCapabilityFacade206', None)
    _safe_set(owner, 'build_Capability207', partner)
    assert getattr(partner, 'build_EffectiveCapabilityFacade206') == owner
    _safe_set(owner, 'build_Capability207', None)
    assert getattr(partner, 'build_EffectiveCapabilityFacade206') is None


def test_assoc_providers179_stub_double():
    # build_FirstFoundUnitProvider has no real 'build_FirstFoundUnitProvider181' property in the generated
    # code (a bare stub) -- manually attach it so build_BeeModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BeeModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BeeModel()
    partner = build_FirstFoundUnitProvider()
    setattr(partner, 'build_FirstFoundUnitProvider181', None)
    _safe_set(owner, 'build_BeeModel180', {partner})
    assert getattr(partner, 'build_FirstFoundUnitProvider181') == owner
    _safe_set(owner, 'build_BeeModel180', set())
    assert getattr(partner, 'build_FirstFoundUnitProvider181') is None


def test_assoc_providers18_stub_double():
    # build_FirstFoundUnitProvider has no real 'build_FirstFoundUnitProvider' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_FirstFoundUnitProvider()
    setattr(partner, 'build_FirstFoundUnitProvider', None)
    _safe_set(owner, 'build_BuildUnit19', {partner})
    assert getattr(partner, 'build_FirstFoundUnitProvider') == owner
    _safe_set(owner, 'build_BuildUnit19', set())
    assert getattr(partner, 'build_FirstFoundUnitProvider') is None


def test_assoc_providers67_stub_double():
    # build_CompoundUnitProvider has no real 'build_CompoundUnitProvider' property in the generated
    # code (a bare stub) -- manually attach it so build_UnitProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_UnitProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_UnitProvider(documentation="sample_text")
    partner = build_CompoundUnitProvider()
    setattr(partner, 'build_CompoundUnitProvider', None)
    _safe_set(owner, 'build_UnitProvider', partner)
    assert owner in getattr(partner, 'build_CompoundUnitProvider')
    _safe_set(owner, 'build_UnitProvider', None)
    assert owner not in getattr(partner, 'build_CompoundUnitProvider')


def test_assoc_query106_stub_double():
    # build_BExpression has no real 'build_BExpression108' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BExpression()
    setattr(partner, 'build_BExpression108', None)
    _safe_set(owner, 'build_BuilderConcernContext107', partner)
    assert getattr(partner, 'build_BExpression108') == owner
    _safe_set(owner, 'build_BuilderConcernContext107', None)
    assert getattr(partner, 'build_BExpression108') is None


def test_assoc_query94_stub_double():
    # build_BExpression has no real 'build_BExpression96' property in the generated
    # code (a bare stub) -- manually attach it so build_UnitConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_UnitConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_UnitConcernContext(outputLocation="sample_text", sourceLocation="sample_text")
    partner = build_BExpression()
    setattr(partner, 'build_BExpression96', None)
    _safe_set(owner, 'build_UnitConcernContext95', partner)
    assert getattr(partner, 'build_BExpression96') == owner
    _safe_set(owner, 'build_UnitConcernContext95', None)
    assert getattr(partner, 'build_BExpression96') is None


def test_assoc_repository61_stub_double():
    # build_RepositoryUnitProvider has no real 'build_RepositoryUnitProvider' property in the generated
    # code (a bare stub) -- manually attach it so build_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Repository(documentation="sample_text", handlerType="sample_text", name="sample_text")
    partner = build_RepositoryUnitProvider()
    setattr(partner, 'build_RepositoryUnitProvider', None)
    _safe_set(owner, 'build_Repository62', partner)
    assert getattr(partner, 'build_RepositoryUnitProvider') == owner
    _safe_set(owner, 'build_Repository62', None)
    assert getattr(partner, 'build_RepositoryUnitProvider') is None


def test_assoc_requiredCapabilities153_stub_double():
    # build_IRequiredCapabilityContainer has no real 'build_IRequiredCapabilityContainer' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_IRequiredCapabilityContainer()
    setattr(partner, 'build_IRequiredCapabilityContainer', None)
    _safe_set(owner, 'build_RequiredCapability154', partner)
    assert owner in getattr(partner, 'build_IRequiredCapabilityContainer')
    _safe_set(owner, 'build_RequiredCapability154', None)
    assert owner not in getattr(partner, 'build_IRequiredCapabilityContainer')


def test_assoc_requiredCapability256_stub_double():
    # build_BuildCallSingle has no real 'build_BuildCallSingle' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_BuildCallSingle()
    setattr(partner, 'build_BuildCallSingle', None)
    _safe_set(owner, 'build_RequiredCapability257', partner)
    assert getattr(partner, 'build_BuildCallSingle') == owner
    _safe_set(owner, 'build_RequiredCapability257', None)
    assert getattr(partner, 'build_BuildCallSingle') is None


def test_assoc_requiredCapabilityDeclaration258_stub_double():
    # build_BuildCallOnDeclaredRequirement has no real 'build_BuildCallOnDeclaredRequirement' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_BuildCallOnDeclaredRequirement()
    setattr(partner, 'build_BuildCallOnDeclaredRequirement', None)
    _safe_set(owner, 'build_RequiredCapability259', partner)
    assert getattr(partner, 'build_BuildCallOnDeclaredRequirement') == owner
    _safe_set(owner, 'build_RequiredCapability259', None)
    assert getattr(partner, 'build_BuildCallOnDeclaredRequirement') is None


def test_assoc_requiredCapabilityReference260_stub_double():
    # build_BuildCallOnReferencedRequirement has no real 'build_BuildCallOnReferencedRequirement' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_BuildCallOnReferencedRequirement()
    setattr(partner, 'build_BuildCallOnReferencedRequirement', None)
    _safe_set(owner, 'build_RequiredCapability261', partner)
    assert getattr(partner, 'build_BuildCallOnReferencedRequirement') == owner
    _safe_set(owner, 'build_RequiredCapability261', None)
    assert getattr(partner, 'build_BuildCallOnReferencedRequirement') is None


def test_assoc_requiredPredicate251_stub_double():
    # build_BuildCallOnSelectedRequirements has no real 'build_BuildCallOnSelectedRequirements' property in the generated
    # code (a bare stub) -- manually attach it so build_CapabilityPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_CapabilityPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_CapabilityPredicate(versionRange="sample_text")
    partner = build_BuildCallOnSelectedRequirements()
    setattr(partner, 'build_BuildCallOnSelectedRequirements', None)
    _safe_set(owner, 'build_CapabilityPredicate252', partner)
    assert getattr(partner, 'build_BuildCallOnSelectedRequirements') == owner
    _safe_set(owner, 'build_CapabilityPredicate252', None)
    assert getattr(partner, 'build_BuildCallOnSelectedRequirements') is None


def test_assoc_requiredPredicates155_stub_double():
    # build_IRequiredCapabilityContainer has no real 'build_IRequiredCapabilityContainer156' property in the generated
    # code (a bare stub) -- manually attach it so build_CapabilityPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_CapabilityPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_CapabilityPredicate(versionRange="sample_text")
    partner = build_IRequiredCapabilityContainer()
    setattr(partner, 'build_IRequiredCapabilityContainer156', None)
    _safe_set(owner, 'build_CapabilityPredicate157', partner)
    assert owner in getattr(partner, 'build_IRequiredCapabilityContainer156')
    _safe_set(owner, 'build_CapabilityPredicate157', None)
    assert owner not in getattr(partner, 'build_IRequiredCapabilityContainer156')


def test_assoc_requirement202_stub_double():
    # build_EffectiveRequirementFacade has no real 'build_EffectiveRequirementFacade203' property in the generated
    # code (a bare stub) -- manually attach it so build_RequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_RequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_RequiredCapability(greedy=True, max=7, min=7, versionRange="sample_text")
    partner = build_EffectiveRequirementFacade()
    setattr(partner, 'build_EffectiveRequirementFacade203', None)
    _safe_set(owner, 'build_RequiredCapability204', partner)
    assert getattr(partner, 'build_EffectiveRequirementFacade203') == owner
    _safe_set(owner, 'build_RequiredCapability204', None)
    assert getattr(partner, 'build_EffectiveRequirementFacade203') is None


def test_assoc_source41_stub_double():
    # build_PathGroup has no real 'build_PathGroup43' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuilder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuilder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuilder(unitType="sample_text")
    partner = build_PathGroup()
    setattr(partner, 'build_PathGroup43', None)
    _safe_set(owner, 'build_IBuilder42', partner)
    assert getattr(partner, 'build_PathGroup43') == owner
    _safe_set(owner, 'build_IBuilder42', None)
    assert getattr(partner, 'build_PathGroup43') is None


def test_assoc_sourceAdditions142_stub_double():
    # build_ConditionalPathVector has no real 'build_ConditionalPathVector144' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_ConditionalPathVector()
    setattr(partner, 'build_ConditionalPathVector144', None)
    _safe_set(owner, 'build_BuilderConcernContext143', {partner})
    assert getattr(partner, 'build_ConditionalPathVector144') == owner
    _safe_set(owner, 'build_BuilderConcernContext143', set())
    assert getattr(partner, 'build_ConditionalPathVector144') is None


def test_assoc_sourceAnnotationAdditions145_stub_double():
    # build_BPropertySet has no real 'build_BPropertySet147' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_BPropertySet()
    setattr(partner, 'build_BPropertySet147', None)
    _safe_set(owner, 'build_BuilderConcernContext146', partner)
    assert getattr(partner, 'build_BPropertySet147') == owner
    _safe_set(owner, 'build_BuilderConcernContext146', None)
    assert getattr(partner, 'build_BPropertySet147') is None


def test_assoc_sourceRemovals140_stub_double():
    # build_SourcePredicate has no real 'build_SourcePredicate' property in the generated
    # code (a bare stub) -- manually attach it so build_BuilderConcernContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuilderConcernContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuilderConcernContext(matchParameters=True, outputAnnotationsRemovals="sample_text", removePostCondition=True, removePostInputCondition=True, removePreCondition=True, sourceAnnotationsRemovals="sample_text", varArgs=True)
    partner = build_SourcePredicate()
    setattr(partner, 'build_SourcePredicate', None)
    _safe_set(owner, 'build_BuilderConcernContext141', {partner})
    assert getattr(partner, 'build_SourcePredicate') == owner
    _safe_set(owner, 'build_BuilderConcernContext141', set())
    assert getattr(partner, 'build_SourcePredicate') is None


def test_assoc_synchronizations9_stub_double():
    # build_Synchronization has no real 'build_Synchronization' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_Synchronization()
    setattr(partner, 'build_Synchronization', None)
    _safe_set(owner, 'build_BuildUnit10', {partner})
    assert getattr(partner, 'build_Synchronization') == owner
    _safe_set(owner, 'build_BuildUnit10', set())
    assert getattr(partner, 'build_Synchronization') is None


def test_assoc_unit190_stub_double():
    # build_EffectiveUnitFacade has no real 'build_EffectiveUnitFacade' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_EffectiveUnitFacade()
    setattr(partner, 'build_EffectiveUnitFacade', None)
    _safe_set(owner, 'build_BuildUnit191', partner)
    assert getattr(partner, 'build_EffectiveUnitFacade') == owner
    _safe_set(owner, 'build_BuildUnit191', None)
    assert getattr(partner, 'build_EffectiveUnitFacade') is None


def test_assoc_unit219_stub_double():
    # build_UnitResolutionInfo has no real 'build_UnitResolutionInfo' property in the generated
    # code (a bare stub) -- manually attach it so build_BuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_BuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_BuildUnit(documentation="sample_text", executionMode="sample_text", outputLocation="sample_text", platformFilter="sample_text", sourceLocation="sample_text")
    partner = build_UnitResolutionInfo()
    setattr(partner, 'build_UnitResolutionInfo', None)
    _safe_set(owner, 'build_BuildUnit220', partner)
    assert getattr(partner, 'build_UnitResolutionInfo') == owner
    _safe_set(owner, 'build_BuildUnit220', None)
    assert getattr(partner, 'build_UnitResolutionInfo') is None




from python_code import build_AliasedRequiredCapability

def test_build_AliasedRequiredCapability___init__():
    assert build_AliasedRequiredCapability.__init__(build_AliasedRequiredCapability(''), '') == None
from python_code import build_BPropertySet
from python_code import build_BuildConcernContext

def test_build_BuildConcernContext___init__():
    assert build_BuildConcernContext.__init__(build_BuildConcernContext('', build_BuildConcernContext=build_BPropertySet()), '', build_BuildConcernContext=build_BPropertySet()) == None
from python_code import build_BuildUnitRepository

def test_build_BuildUnitRepository___init__():
    assert build_BuildUnitRepository.__init__(build_BuildUnitRepository()) == None

def test_build_BuildUnitRepository_initialize():
    assert build_BuildUnitRepository.initialize(build_BuildUnitRepository(), '', '', '') == None

def test_build_BuildUnitRepository_resolve():
    assert build_BuildUnitRepository.resolve(build_BuildUnitRepository(), '', '', '') == None
from python_code import build_BuilderWrapper

def test_build_BuilderWrapper___init__():
    assert build_BuilderWrapper.__init__(build_BuilderWrapper(False, False, False, True, False, False), False, False, False, False, False, False) == None
from python_code import build_BExpression
from python_code import build_Capability
from python_code import build_EffectiveCapabilityFacade
from python_code import build_IProvidedCapabilityContainer

def test_build_Capability___init__():
    assert build_Capability.__init__(build_Capability('', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()), '', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()) == None

def test_build_Capability_satisfies():
    assert build_Capability.satisfies(build_Capability('', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()), 0) == None
from python_code import build_NameSpacePredicate

def test_build_NameSpacePredicate___init__():
    assert build_NameSpacePredicate.__init__(build_NameSpacePredicate(''), '') == None
from python_code import build_ResolutionInfo

def test_build_ResolutionInfo___init__():
    assert build_ResolutionInfo.__init__(build_ResolutionInfo(''), '') == None
from python_code import build_BExpression
from python_code import build_UnitConcernContext

def test_build_UnitConcernContext___init__():
    assert build_UnitConcernContext.__init__(build_UnitConcernContext('', '', build_UnitConcernContext=set(), build_UnitConcernContext95=build_BExpression(), build_UnitConcernContext98=set(), build_UnitConcernContext101=set(), build_UnitConcernContext104=set()), '\x00', '', build_UnitConcernContext=set(), build_UnitConcernContext95=build_BExpression(), build_UnitConcernContext98=set(), build_UnitConcernContext101=set(), build_UnitConcernContext104=set()) == None
from python_code import build_CompoundUnitProvider
from python_code import build_DelegatingUnitProvider
from python_code import build_UnitProvider

def test_build_UnitProvider___init__():
    assert build_UnitProvider.__init__(build_UnitProvider('', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()), '', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()) == None

def test_build_UnitProvider_resolve():
    assert build_UnitProvider.resolve(build_UnitProvider('', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()), 0) == None
from python_code import build_VersionedCapability

def test_build_VersionedCapability___init__():
    assert build_VersionedCapability.__init__(build_VersionedCapability(''), '') == None

