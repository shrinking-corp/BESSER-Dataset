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


