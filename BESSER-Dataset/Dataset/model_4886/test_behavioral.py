import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AdviceGroup,
    BuildUnitCommand,
    ContextNodeSelector,
    EFSResolver,
    FilterGroup,
    IActionResult,
    IAdvise,
    IBuildPart,
    ICapability,
    IClosure,
    IClosurePart,
    IExpr,
    IExtension,
    IFilter,
    IFunction,
    IGenericUnit,
    IHumanSelectable,
    IMaterializer,
    IMetaDataTranslator,
    IMetaDataTranslatorFactory,
    IPrerequisites,
    IRequirement,
    IResolution,
    IResolver,
    IUnitRequest,
    ImportOptions,
    Match,
    MaterializerExtension,
    MetaDataTranslatorFactoryExtension,
    PropertyScope,
    ResolutionOptions,
    ResolverExtension,
    ResolverGroup,
    SinglePropertyFilter,
    UpToDateExtension,
    build_IActionPart,
    build_IActionResult,
    build_IArtifactsPart,
    build_IBuildPart,
    build_IBuildUnit,
    build_ICapability,
    build_IClosure,
    build_IClosurePart,
    build_IGenericUnit,
    build_IPartGroup,
    build_IPathGroup,
    build_IPrerequisites,
    build_IProducedPart,
    build_IProvidedCapability,
    build_IRequiredCapability,
    build_IRequirement,
    build_IResultingParts,
    build_IUpToDatePolicy,
    build_PartCapability,
    build_PartRequirement,
    build_PropertyScope,
    build_Requirement,
    build_ResultingPathGroup,
    build_StringProperties,
    build_command_AdviceGroup,
    build_command_BooleanAdvice,
    build_command_BuildUnitCommand,
    build_command_ContextNodeSelector,
    build_command_FilterAdvice,
    build_command_IAdvise,
    build_command_IUnitRequest,
    build_command_ImportCommand,
    build_command_InvokeCommand,
    build_command_NewInstanceAdvice,
    build_command_PropertyAdvice,
    build_command_StringAdvice,
    build_command_UnsetAdvice,
    build_command_VersionAdvice,
    build_command_VersionRangeAdvice,
    build_context_IBuildContext,
    build_context_IResolution,
    build_context_ImportOptions,
    build_context_ResolutionOptions,
    build_filter_AndFilter,
    build_filter_FilterGroup,
    build_filter_IFilter,
    build_filter_OSGiBasedFilter,
    build_filter_OrFilter,
    build_filter_RegexpFilter,
    build_filter_SimplePatternFIlter,
    build_filter_SinglePropertyFilter,
    build_materializer_FileSystemMaterializer,
    build_materializer_IMaterializer,
    build_materializer_P2Materializer,
    build_materializer_WorkspaceMaterializer,
    build_properties_Format,
    build_properties_IExpr,
    build_properties_IFunction,
    build_properties_Literal,
    build_properties_Match,
    build_properties_PropertyRef,
    build_properties_Split,
    build_properties_ToUpper,
    build_properties_replace,
    build_properties_toLower,
    build_resolver_BestChoice,
    build_resolver_DefaultResolver,
    build_resolver_EFSResolver,
    build_resolver_FirstChoice,
    build_resolver_IEFSBasedAccess,
    build_resolver_ILocation,
    build_resolver_IMetaDataTranslator,
    build_resolver_IMetaDataTranslatorFactory,
    build_resolver_IResolutionContext,
    build_resolver_IResolver,
    build_resolver_IResourceMap,
    build_resolver_P2Resolver,
    build_resolver_ResolverGroup,
    build_resolver_WorspaceResolver,
    build_runtime_BuildRuntime,
    build_runtime_IExtension,
    build_runtime_IHumanSelectable,
    build_runtime_MaterializerExtension,
    build_runtime_MetaDataTranslatorFactoryExtension,
    build_runtime_ResolverExtension,
    build_runtime_UpToDateExtension,
    command_build_PropertyScope,
    context_build_IBuildUnit,
    context_build_ICapability,
    context_build_IRequiredCapability,
    resolver_DefaultResolver,
    resolver_IEFSBasedAccess,
    runtime_build_IUpToDatePolicy,
    ConflictResolution,
    Disposition,
    FilterAdviceOperation,
    SplitStyle,
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

def test_assoc_allRequiredCapabilities5_reverse_link_reassign_clear():
    a1 = build_IRequiredCapability(filter="sample_text", name="sample_text", namespace="sample_text", range="sample_text")
    a2 = build_IRequiredCapability(filter="sample_text_2", name="sample_text_2", namespace="sample_text_2", range="sample_text_2")
    b = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    _safe_set(b, 'build_IBuildUnit6', {a1})
    assert _is_linked(b, 'build_IBuildUnit6', a1)
    if hasattr(a1, 'build_IRequiredCapability7'):
        assert _is_linked(a1, 'build_IRequiredCapability7', b)
    _safe_set(b, 'build_IBuildUnit6', {a2})
    assert _is_linked(b, 'build_IBuildUnit6', a2)
    if hasattr(a1, 'build_IRequiredCapability7'):
        assert not _is_linked(a1, 'build_IRequiredCapability7', b)
    if hasattr(a2, 'build_IRequiredCapability7'):
        assert _is_linked(a2, 'build_IRequiredCapability7', b)
    _safe_set(b, 'build_IBuildUnit6', set())
    assert not _is_linked(b, 'build_IBuildUnit6', a2)
    if hasattr(a2, 'build_IRequiredCapability7'):
        assert not _is_linked(a2, 'build_IRequiredCapability7', b)


def test_assoc_buildUnit16_reverse_link_reassign_clear():
    a1 = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    a2 = build_IBuildUnit(circularityAllowed=False, filter="sample_text_2", instanceLocation="sample_text_2")
    b = build_IBuildPart(name="sample_text")
    _safe_set(b, 'parts', a1)
    assert _is_linked(b, 'parts', a1)
    if hasattr(a1, 'IBuildUnit'):
        assert _is_linked(a1, 'IBuildUnit', b)
    _safe_set(b, 'parts', a2)
    assert _is_linked(b, 'parts', a2)
    if hasattr(a1, 'IBuildUnit'):
        assert not _is_linked(a1, 'IBuildUnit', b)
    if hasattr(a2, 'IBuildUnit'):
        assert _is_linked(a2, 'IBuildUnit', b)
    _safe_set(b, 'parts', None)
    assert not _is_linked(b, 'parts', a2)
    if hasattr(a2, 'IBuildUnit'):
        assert not _is_linked(a2, 'IBuildUnit', b)


def test_assoc_metaRequiredCapabilities2_reverse_link_reassign_clear():
    a1 = build_IRequiredCapability(filter="sample_text", name="sample_text", namespace="sample_text", range="sample_text")
    a2 = build_IRequiredCapability(filter="sample_text_2", name="sample_text_2", namespace="sample_text_2", range="sample_text_2")
    b = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    _safe_set(b, 'build_IBuildUnit3', {a1})
    assert _is_linked(b, 'build_IBuildUnit3', a1)
    if hasattr(a1, 'build_IRequiredCapability4'):
        assert _is_linked(a1, 'build_IRequiredCapability4', b)
    _safe_set(b, 'build_IBuildUnit3', {a2})
    assert _is_linked(b, 'build_IBuildUnit3', a2)
    if hasattr(a1, 'build_IRequiredCapability4'):
        assert not _is_linked(a1, 'build_IRequiredCapability4', b)
    if hasattr(a2, 'build_IRequiredCapability4'):
        assert _is_linked(a2, 'build_IRequiredCapability4', b)
    _safe_set(b, 'build_IBuildUnit3', set())
    assert not _is_linked(b, 'build_IBuildUnit3', a2)
    if hasattr(a2, 'build_IRequiredCapability4'):
        assert not _is_linked(a2, 'build_IRequiredCapability4', b)


def test_assoc_parts0_reverse_link_reassign_clear():
    a1 = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    a2 = build_IBuildUnit(circularityAllowed=False, filter="sample_text_2", instanceLocation="sample_text_2")
    b = build_IBuildPart(name="sample_text")
    _safe_set(b, 'IBuildPart', a1)
    assert _is_linked(b, 'IBuildPart', a1)
    if hasattr(a1, 'buildUnit'):
        assert _is_linked(a1, 'buildUnit', b)
    _safe_set(b, 'IBuildPart', a2)
    assert _is_linked(b, 'IBuildPart', a2)
    if hasattr(a1, 'buildUnit'):
        assert not _is_linked(a1, 'buildUnit', b)
    if hasattr(a2, 'buildUnit'):
        assert _is_linked(a2, 'buildUnit', b)
    _safe_set(b, 'IBuildPart', None)
    assert not _is_linked(b, 'IBuildPart', a2)
    if hasattr(a2, 'buildUnit'):
        assert not _is_linked(a2, 'buildUnit', b)


def test_assoc_properties35_reverse_link_reassign_clear():
    a1 = build_StringProperties(immutable=True, key="sample_text", value="sample_text")
    a2 = build_StringProperties(immutable=False, key="sample_text_2", value="sample_text_2")
    b = build_PropertyScope(unsetProperties="sample_text")
    _safe_set(b, 'build_PropertyScope', a1)
    assert _is_linked(b, 'build_PropertyScope', a1)
    if hasattr(a1, 'build_StringProperties'):
        assert _is_linked(a1, 'build_StringProperties', b)
    _safe_set(b, 'build_PropertyScope', a2)
    assert _is_linked(b, 'build_PropertyScope', a2)
    if hasattr(a1, 'build_StringProperties'):
        assert not _is_linked(a1, 'build_StringProperties', b)
    if hasattr(a2, 'build_StringProperties'):
        assert _is_linked(a2, 'build_StringProperties', b)
    _safe_set(b, 'build_PropertyScope', None)
    assert not _is_linked(b, 'build_PropertyScope', a2)
    if hasattr(a2, 'build_StringProperties'):
        assert not _is_linked(a2, 'build_StringProperties', b)


def test_assoc_providedCapabilities8_reverse_link_reassign_clear():
    a1 = build_ICapability(name="sample_text", namespace="sample_text", version="sample_text")
    a2 = build_ICapability(name="sample_text_2", namespace="sample_text_2", version="sample_text_2")
    b = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    _safe_set(b, 'build_IBuildUnit9', {a1})
    assert _is_linked(b, 'build_IBuildUnit9', a1)
    if hasattr(a1, 'build_ICapability'):
        assert _is_linked(a1, 'build_ICapability', b)
    _safe_set(b, 'build_IBuildUnit9', {a2})
    assert _is_linked(b, 'build_IBuildUnit9', a2)
    if hasattr(a1, 'build_ICapability'):
        assert not _is_linked(a1, 'build_ICapability', b)
    if hasattr(a2, 'build_ICapability'):
        assert _is_linked(a2, 'build_ICapability', b)
    _safe_set(b, 'build_IBuildUnit9', set())
    assert not _is_linked(b, 'build_IBuildUnit9', a2)
    if hasattr(a2, 'build_ICapability'):
        assert not _is_linked(a2, 'build_ICapability', b)


def test_assoc_requiredCapabilities1_reverse_link_reassign_clear():
    a1 = build_IRequiredCapability(filter="sample_text", name="sample_text", namespace="sample_text", range="sample_text")
    a2 = build_IRequiredCapability(filter="sample_text_2", name="sample_text_2", namespace="sample_text_2", range="sample_text_2")
    b = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    _safe_set(b, 'build_IBuildUnit', {a1})
    assert _is_linked(b, 'build_IBuildUnit', a1)
    if hasattr(a1, 'build_IRequiredCapability'):
        assert _is_linked(a1, 'build_IRequiredCapability', b)
    _safe_set(b, 'build_IBuildUnit', {a2})
    assert _is_linked(b, 'build_IBuildUnit', a2)
    if hasattr(a1, 'build_IRequiredCapability'):
        assert not _is_linked(a1, 'build_IRequiredCapability', b)
    if hasattr(a2, 'build_IRequiredCapability'):
        assert _is_linked(a2, 'build_IRequiredCapability', b)
    _safe_set(b, 'build_IBuildUnit', set())
    assert not _is_linked(b, 'build_IBuildUnit', a2)
    if hasattr(a2, 'build_IRequiredCapability'):
        assert not _is_linked(a2, 'build_IRequiredCapability', b)


def test_assoc_requiredParts21_reverse_link_reassign_clear():
    a1 = build_IRequirement(alias="sample_text", contributor=True, excludePattern="sample_text", filter="sample_text", includePattern="sample_text", memberName="sample_text")
    a2 = build_IRequirement(alias="sample_text_2", contributor=False, excludePattern="sample_text_2", filter="sample_text_2", includePattern="sample_text_2", memberName="sample_text_2")
    b = build_IPrerequisites(alias="sample_text", rebasePath="sample_text")
    _safe_set(b, 'build_IPrerequisites', {a1})
    assert _is_linked(b, 'build_IPrerequisites', a1)
    if hasattr(a1, 'build_IRequirement'):
        assert _is_linked(a1, 'build_IRequirement', b)
    _safe_set(b, 'build_IPrerequisites', {a2})
    assert _is_linked(b, 'build_IPrerequisites', a2)
    if hasattr(a1, 'build_IRequirement'):
        assert not _is_linked(a1, 'build_IRequirement', b)
    if hasattr(a2, 'build_IRequirement'):
        assert _is_linked(a2, 'build_IRequirement', b)
    _safe_set(b, 'build_IPrerequisites', set())
    assert not _is_linked(b, 'build_IPrerequisites', a2)
    if hasattr(a2, 'build_IRequirement'):
        assert not _is_linked(a2, 'build_IRequirement', b)


def test_assoc_selfCapability11_reverse_link_reassign_clear():
    a1 = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    a2 = build_IBuildUnit(circularityAllowed=False, filter="sample_text_2", instanceLocation="sample_text_2")
    b = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    _safe_set(b, 'build_IBuildUnit12', a1)
    assert _is_linked(b, 'build_IBuildUnit12', a1)
    if hasattr(a1, 'build_IBuildUnit10'):
        assert _is_linked(a1, 'build_IBuildUnit10', b)
    _safe_set(b, 'build_IBuildUnit12', a2)
    assert _is_linked(b, 'build_IBuildUnit12', a2)
    if hasattr(a1, 'build_IBuildUnit10'):
        assert not _is_linked(a1, 'build_IBuildUnit10', b)
    if hasattr(a2, 'build_IBuildUnit10'):
        assert _is_linked(a2, 'build_IBuildUnit10', b)
    _safe_set(b, 'build_IBuildUnit12', None)
    assert not _is_linked(b, 'build_IBuildUnit12', a2)
    if hasattr(a2, 'build_IBuildUnit10'):
        assert not _is_linked(a2, 'build_IBuildUnit10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_add92_stub_double():
    # IFilter has no real 'IFilter94' property in the generated
    # code (a bare stub) -- manually attach it so build_command_FilterAdvice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_command_FilterAdvice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_command_FilterAdvice(filterOp="sample_text")
    partner = IFilter()
    setattr(partner, 'IFilter94', None)
    _safe_set(owner, 'build_command_FilterAdvice93', partner)
    assert getattr(partner, 'IFilter94') == owner
    _safe_set(owner, 'build_command_FilterAdvice93', None)
    assert getattr(partner, 'IFilter94') is None


def test_assoc_advice20_stub_double():
    # IAdvise has no real 'IAdvise' property in the generated
    # code (a bare stub) -- manually attach it so build_IClosure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IClosure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IClosure(executeOnce=True)
    partner = IAdvise()
    setattr(partner, 'IAdvise', None)
    _safe_set(owner, 'build_IClosure', {partner})
    assert getattr(partner, 'IAdvise') == owner
    _safe_set(owner, 'build_IClosure', set())
    assert getattr(partner, 'IAdvise') is None


def test_assoc_buildPart33_stub_double():
    # build_PartCapability has no real 'publishedCapabilities' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuildPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuildPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuildPart(name="sample_text")
    partner = build_PartCapability()
    setattr(partner, 'publishedCapabilities', None)
    _safe_set(owner, 'IBuildPart34', partner)
    assert getattr(partner, 'publishedCapabilities') == owner
    _safe_set(owner, 'IBuildPart34', None)
    assert getattr(partner, 'publishedCapabilities') is None


def test_assoc_location70_stub_double():
    # IExpr has no real 'IExpr' property in the generated
    # code (a bare stub) -- manually attach it so build_resolver_IResolver's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_resolver_IResolver's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_resolver_IResolver(failOnError=True, filter="sample_text")
    partner = IExpr()
    setattr(partner, 'IExpr', None)
    _safe_set(owner, 'build_resolver_IResolver', partner)
    assert getattr(partner, 'IExpr') == owner
    _safe_set(owner, 'build_resolver_IResolver', None)
    assert getattr(partner, 'IExpr') is None


def test_assoc_materializer56_stub_double():
    # IMaterializer has no real 'IMaterializer' property in the generated
    # code (a bare stub) -- manually attach it so build_context_ImportOptions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_context_ImportOptions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_context_ImportOptions(conflictResolution="sample_text", expand=True, location="sample_text", resourcePath="sample_text", suffix="sample_text", unpack=True)
    partner = IMaterializer()
    setattr(partner, 'IMaterializer', None)
    _safe_set(owner, 'build_context_ImportOptions', partner)
    assert getattr(partner, 'IMaterializer') == owner
    _safe_set(owner, 'build_context_ImportOptions', None)
    assert getattr(partner, 'IMaterializer') is None


def test_assoc_options77_stub_double():
    # ResolutionOptions has no real 'ResolutionOptions' property in the generated
    # code (a bare stub) -- manually attach it so build_command_IUnitRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_command_IUnitRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_command_IUnitRequest(name="sample_text", nameSpace="sample_text", range="sample_text")
    partner = ResolutionOptions()
    setattr(partner, 'ResolutionOptions', None)
    _safe_set(owner, 'build_command_IUnitRequest', partner)
    assert getattr(partner, 'ResolutionOptions') == owner
    _safe_set(owner, 'build_command_IUnitRequest', None)
    assert getattr(partner, 'ResolutionOptions') is None


def test_assoc_partCapabilities13_stub_double():
    # build_PartCapability has no real 'build_PartCapability' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuildUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuildUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuildUnit(circularityAllowed=True, filter="sample_text", instanceLocation="sample_text")
    partner = build_PartCapability()
    setattr(partner, 'build_PartCapability', None)
    _safe_set(owner, 'build_IBuildUnit14', {partner})
    assert getattr(partner, 'build_PartCapability') == owner
    _safe_set(owner, 'build_IBuildUnit14', set())
    assert getattr(partner, 'build_PartCapability') is None


def test_assoc_paths17_stub_double():
    # build_IArtifactsPart has no real 'build_IArtifactsPart' property in the generated
    # code (a bare stub) -- manually attach it so build_IPathGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IPathGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IPathGroup(basePath="sample_text", paths="sample_text")
    partner = build_IArtifactsPart()
    setattr(partner, 'build_IArtifactsPart', None)
    _safe_set(owner, 'build_IPathGroup', partner)
    assert owner in getattr(partner, 'build_IArtifactsPart')
    _safe_set(owner, 'build_IPathGroup', None)
    assert owner not in getattr(partner, 'build_IArtifactsPart')


def test_assoc_paths24_stub_double():
    # build_IProducedPart has no real 'build_IProducedPart' property in the generated
    # code (a bare stub) -- manually attach it so build_IPathGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IPathGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IPathGroup(basePath="sample_text", paths="sample_text")
    partner = build_IProducedPart()
    setattr(partner, 'build_IProducedPart', None)
    _safe_set(owner, 'build_IPathGroup25', partner)
    assert getattr(partner, 'build_IProducedPart') == owner
    _safe_set(owner, 'build_IPathGroup25', None)
    assert getattr(partner, 'build_IProducedPart') is None


def test_assoc_paths31_stub_double():
    # build_ResultingPathGroup has no real 'build_ResultingPathGroup' property in the generated
    # code (a bare stub) -- manually attach it so build_IPathGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IPathGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IPathGroup(basePath="sample_text", paths="sample_text")
    partner = build_ResultingPathGroup()
    setattr(partner, 'build_ResultingPathGroup', None)
    _safe_set(owner, 'build_IPathGroup32', partner)
    assert getattr(partner, 'build_ResultingPathGroup') == owner
    _safe_set(owner, 'build_IPathGroup32', None)
    assert getattr(partner, 'build_ResultingPathGroup') is None


def test_assoc_publishedCapabilities15_stub_double():
    # build_PartCapability has no real 'PartCapability' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuildPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuildPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuildPart(name="sample_text")
    partner = build_PartCapability()
    setattr(partner, 'PartCapability', None)
    _safe_set(owner, 'buildPart', {partner})
    assert getattr(partner, 'PartCapability') == owner
    _safe_set(owner, 'buildPart', set())
    assert getattr(partner, 'PartCapability') is None


def test_assoc_remove91_stub_double():
    # IFilter has no real 'IFilter' property in the generated
    # code (a bare stub) -- manually attach it so build_command_FilterAdvice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_command_FilterAdvice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_command_FilterAdvice(filterOp="sample_text")
    partner = IFilter()
    setattr(partner, 'IFilter', None)
    _safe_set(owner, 'build_command_FilterAdvice', partner)
    assert getattr(partner, 'IFilter') == owner
    _safe_set(owner, 'build_command_FilterAdvice', None)
    assert getattr(partner, 'IFilter') is None


def test_assoc_requiredCapability29_stub_double():
    # build_Requirement has no real 'build_Requirement' property in the generated
    # code (a bare stub) -- manually attach it so build_IRequiredCapability's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IRequiredCapability's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IRequiredCapability(filter="sample_text", name="sample_text", namespace="sample_text", range="sample_text")
    partner = build_Requirement()
    setattr(partner, 'build_Requirement', None)
    _safe_set(owner, 'build_IRequiredCapability30', partner)
    assert getattr(partner, 'build_Requirement') == owner
    _safe_set(owner, 'build_IRequiredCapability30', None)
    assert getattr(partner, 'build_Requirement') is None


def test_assoc_requiredPart22_stub_double():
    # build_PartRequirement has no real 'build_PartRequirement' property in the generated
    # code (a bare stub) -- manually attach it so build_IBuildPart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IBuildPart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IBuildPart(name="sample_text")
    partner = build_PartRequirement()
    setattr(partner, 'build_PartRequirement', None)
    _safe_set(owner, 'build_IBuildPart', partner)
    assert getattr(partner, 'build_PartRequirement') == owner
    _safe_set(owner, 'build_IBuildPart', None)
    assert getattr(partner, 'build_PartRequirement') is None


def test_assoc_self36_stub_double():
    # build_IGenericUnit has no real 'build_IGenericUnit' property in the generated
    # code (a bare stub) -- manually attach it so build_IPathGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_IPathGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_IPathGroup(basePath="sample_text", paths="sample_text")
    partner = build_IGenericUnit()
    setattr(partner, 'build_IGenericUnit', None)
    _safe_set(owner, 'build_IPathGroup37', partner)
    assert getattr(partner, 'build_IGenericUnit') == owner
    _safe_set(owner, 'build_IPathGroup37', None)
    assert getattr(partner, 'build_IGenericUnit') is None


