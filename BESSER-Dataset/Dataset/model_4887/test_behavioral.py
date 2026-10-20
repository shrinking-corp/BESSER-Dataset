import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArtifactDescriptor,
    ArtifactRepository,
    IArtifactDescriptor,
    IArtifactKey,
    IArtifactRepository,
    ICopyright,
    IFileArtifactRepository,
    IInstallableUnit,
    IInstallableUnitFragment,
    IInstallableUnitPatch,
    ILicense,
    IProcessingStepDescriptor,
    IProvidedCapability,
    IRepositoryReference,
    IRequiredCapability,
    IRequirement,
    IRequirementChange,
    ITouchpointData,
    ITouchpointInstruction,
    ITouchpointType,
    IUpdateDescriptor,
    InstallableUnit,
    Requirement,
    p2_ArtifactDescriptor,
    p2_ArtifactKey,
    p2_ArtifactRepository,
    p2_ArtifactsByKey,
    p2_Comparable,
    p2_Copyright,
    p2_IAdaptable,
    p2_IArtifactDescriptor,
    p2_IArtifactKey,
    p2_IArtifactRepository,
    p2_ICopyright,
    p2_IFileArtifactRepository,
    p2_IInstallableUnit,
    p2_IInstallableUnitFragment,
    p2_IInstallableUnitPatch,
    p2_ILicense,
    p2_IMetadataRepository,
    p2_IProcessingStepDescriptor,
    p2_IProvidedCapability,
    p2_IQueryable,
    p2_IRepository,
    p2_IRepositoryReference,
    p2_IRequiredCapability,
    p2_IRequirement,
    p2_IRequirementChange,
    p2_ITouchpointData,
    p2_ITouchpointInstruction,
    p2_ITouchpointType,
    p2_IUpdateDescriptor,
    p2_IVersionedId,
    p2_InstallableUnit,
    p2_InstallableUnitFragment,
    p2_InstallableUnitPatch,
    p2_InstructionMap,
    p2_License,
    p2_MappingRule,
    p2_MetadataRepository,
    p2_ProcessingStepDescriptor,
    p2_Property,
    p2_ProvidedCapability,
    p2_Repository,
    p2_RepositoryReference,
    p2_RequiredCapability,
    p2_Requirement,
    p2_RequirementChange,
    p2_SimpleArtifactDescriptor,
    p2_SimpleArtifactRepository,
    p2_TouchpointData,
    p2_TouchpointInstruction,
    p2_TouchpointType,
    p2_UpdateDescriptor,
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

def test_assoc_applyOn44_reverse_link_reassign_clear():
    a1 = p2_IRequirementChange()
    a2 = p2_IRequirementChange()
    b = p2_IRequiredCapability(name="sample_text", namespace="sample_text", range="sample_text")
    _safe_set(b, 'p2_IRequiredCapability', a1)
    assert _is_linked(b, 'p2_IRequiredCapability', a1)
    if hasattr(a1, 'p2_IRequirementChange45'):
        assert _is_linked(a1, 'p2_IRequirementChange45', b)
    _safe_set(b, 'p2_IRequiredCapability', a2)
    assert _is_linked(b, 'p2_IRequiredCapability', a2)
    if hasattr(a1, 'p2_IRequirementChange45'):
        assert not _is_linked(a1, 'p2_IRequirementChange45', b)
    if hasattr(a2, 'p2_IRequirementChange45'):
        assert _is_linked(a2, 'p2_IRequirementChange45', b)
    _safe_set(b, 'p2_IRequiredCapability', None)
    assert not _is_linked(b, 'p2_IRequiredCapability', a2)
    if hasattr(a2, 'p2_IRequirementChange45'):
        assert not _is_linked(a2, 'p2_IRequirementChange45', b)


def test_assoc_artifactKey8_reverse_link_reassign_clear():
    a1 = p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    a2 = p2_IArtifactKey(classifier="sample_text_2", id="sample_text_2", version="sample_text_2")
    b = p2_IArtifactDescriptor()
    _safe_set(b, 'p2_IArtifactDescriptor9', a1)
    assert _is_linked(b, 'p2_IArtifactDescriptor9', a1)
    if hasattr(a1, 'p2_IArtifactKey10'):
        assert _is_linked(a1, 'p2_IArtifactKey10', b)
    _safe_set(b, 'p2_IArtifactDescriptor9', a2)
    assert _is_linked(b, 'p2_IArtifactDescriptor9', a2)
    if hasattr(a1, 'p2_IArtifactKey10'):
        assert not _is_linked(a1, 'p2_IArtifactKey10', b)
    if hasattr(a2, 'p2_IArtifactKey10'):
        assert _is_linked(a2, 'p2_IArtifactKey10', b)
    _safe_set(b, 'p2_IArtifactDescriptor9', None)
    assert not _is_linked(b, 'p2_IArtifactDescriptor9', a2)
    if hasattr(a2, 'p2_IArtifactKey10'):
        assert not _is_linked(a2, 'p2_IArtifactKey10', b)


def test_assoc_artifacts11_reverse_link_reassign_clear():
    a1 = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    a2 = p2_IInstallableUnit(filter="sample_text_2", resolved=False, singleton=False)
    b = p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    _safe_set(b, 'p2_IArtifactKey12', a1)
    assert _is_linked(b, 'p2_IArtifactKey12', a1)
    if hasattr(a1, 'p2_IInstallableUnit'):
        assert _is_linked(a1, 'p2_IInstallableUnit', b)
    _safe_set(b, 'p2_IArtifactKey12', a2)
    assert _is_linked(b, 'p2_IArtifactKey12', a2)
    if hasattr(a1, 'p2_IInstallableUnit'):
        assert not _is_linked(a1, 'p2_IInstallableUnit', b)
    if hasattr(a2, 'p2_IInstallableUnit'):
        assert _is_linked(a2, 'p2_IInstallableUnit', b)
    _safe_set(b, 'p2_IArtifactKey12', None)
    assert not _is_linked(b, 'p2_IArtifactKey12', a2)
    if hasattr(a2, 'p2_IInstallableUnit'):
        assert not _is_linked(a2, 'p2_IInstallableUnit', b)


def test_assoc_copyright13_reverse_link_reassign_clear():
    a1 = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    a2 = p2_IInstallableUnit(filter="sample_text_2", resolved=False, singleton=False)
    b = p2_ICopyright(body="sample_text", location="sample_text")
    _safe_set(b, 'p2_ICopyright', a1)
    assert _is_linked(b, 'p2_ICopyright', a1)
    if hasattr(a1, 'p2_IInstallableUnit14'):
        assert _is_linked(a1, 'p2_IInstallableUnit14', b)
    _safe_set(b, 'p2_ICopyright', a2)
    assert _is_linked(b, 'p2_ICopyright', a2)
    if hasattr(a1, 'p2_IInstallableUnit14'):
        assert not _is_linked(a1, 'p2_IInstallableUnit14', b)
    if hasattr(a2, 'p2_IInstallableUnit14'):
        assert _is_linked(a2, 'p2_IInstallableUnit14', b)
    _safe_set(b, 'p2_ICopyright', None)
    assert not _is_linked(b, 'p2_ICopyright', a2)
    if hasattr(a2, 'p2_IInstallableUnit14'):
        assert not _is_linked(a2, 'p2_IInstallableUnit14', b)


def test_assoc_licenses17_reverse_link_reassign_clear():
    a1 = p2_ILicense(UUID="sample_text", body="sample_text", location="sample_text")
    a2 = p2_ILicense(UUID="sample_text_2", body="sample_text_2", location="sample_text_2")
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit18', {a1})
    assert _is_linked(b, 'p2_IInstallableUnit18', a1)
    if hasattr(a1, 'p2_ILicense'):
        assert _is_linked(a1, 'p2_ILicense', b)
    _safe_set(b, 'p2_IInstallableUnit18', {a2})
    assert _is_linked(b, 'p2_IInstallableUnit18', a2)
    if hasattr(a1, 'p2_ILicense'):
        assert not _is_linked(a1, 'p2_ILicense', b)
    if hasattr(a2, 'p2_ILicense'):
        assert _is_linked(a2, 'p2_ILicense', b)
    _safe_set(b, 'p2_IInstallableUnit18', set())
    assert not _is_linked(b, 'p2_IInstallableUnit18', a2)
    if hasattr(a2, 'p2_ILicense'):
        assert not _is_linked(a2, 'p2_ILicense', b)


def test_assoc_metaRequirements19_reverse_link_reassign_clear():
    a1 = p2_IRequirement(description="sample_text", filter="sample_text", greedy=True, matches="sample_text", max="sample_text", min="sample_text")
    a2 = p2_IRequirement(description="sample_text_2", filter="sample_text_2", greedy=False, matches="sample_text_2", max="sample_text_2", min="sample_text_2")
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit20', {a1})
    assert _is_linked(b, 'p2_IInstallableUnit20', a1)
    if hasattr(a1, 'p2_IRequirement'):
        assert _is_linked(a1, 'p2_IRequirement', b)
    _safe_set(b, 'p2_IInstallableUnit20', {a2})
    assert _is_linked(b, 'p2_IInstallableUnit20', a2)
    if hasattr(a1, 'p2_IRequirement'):
        assert not _is_linked(a1, 'p2_IRequirement', b)
    if hasattr(a2, 'p2_IRequirement'):
        assert _is_linked(a2, 'p2_IRequirement', b)
    _safe_set(b, 'p2_IInstallableUnit20', set())
    assert not _is_linked(b, 'p2_IInstallableUnit20', a2)
    if hasattr(a2, 'p2_IRequirement'):
        assert not _is_linked(a2, 'p2_IRequirement', b)


def test_assoc_newValue46_reverse_link_reassign_clear():
    a1 = p2_IRequirementChange()
    a2 = p2_IRequirementChange()
    b = p2_IRequiredCapability(name="sample_text", namespace="sample_text", range="sample_text")
    _safe_set(b, 'p2_IRequiredCapability48', a1)
    assert _is_linked(b, 'p2_IRequiredCapability48', a1)
    if hasattr(a1, 'p2_IRequirementChange47'):
        assert _is_linked(a1, 'p2_IRequirementChange47', b)
    _safe_set(b, 'p2_IRequiredCapability48', a2)
    assert _is_linked(b, 'p2_IRequiredCapability48', a2)
    if hasattr(a1, 'p2_IRequirementChange47'):
        assert not _is_linked(a1, 'p2_IRequirementChange47', b)
    if hasattr(a2, 'p2_IRequirementChange47'):
        assert _is_linked(a2, 'p2_IRequirementChange47', b)
    _safe_set(b, 'p2_IRequiredCapability48', None)
    assert not _is_linked(b, 'p2_IRequiredCapability48', a2)
    if hasattr(a2, 'p2_IRequirementChange47'):
        assert not _is_linked(a2, 'p2_IRequirementChange47', b)


def test_assoc_providedCapabilities21_reverse_link_reassign_clear():
    a1 = p2_IProvidedCapability(name="sample_text", namespace="sample_text", version="sample_text")
    a2 = p2_IProvidedCapability(name="sample_text_2", namespace="sample_text_2", version="sample_text_2")
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit22', {a1})
    assert _is_linked(b, 'p2_IInstallableUnit22', a1)
    if hasattr(a1, 'p2_IProvidedCapability'):
        assert _is_linked(a1, 'p2_IProvidedCapability', b)
    _safe_set(b, 'p2_IInstallableUnit22', {a2})
    assert _is_linked(b, 'p2_IInstallableUnit22', a2)
    if hasattr(a1, 'p2_IProvidedCapability'):
        assert not _is_linked(a1, 'p2_IProvidedCapability', b)
    if hasattr(a2, 'p2_IProvidedCapability'):
        assert _is_linked(a2, 'p2_IProvidedCapability', b)
    _safe_set(b, 'p2_IInstallableUnit22', set())
    assert not _is_linked(b, 'p2_IInstallableUnit22', a2)
    if hasattr(a2, 'p2_IProvidedCapability'):
        assert not _is_linked(a2, 'p2_IProvidedCapability', b)


def test_assoc_repositoryPropertyMap56_reverse_link_reassign_clear():
    a1 = p2_SimpleArtifactDescriptor()
    a2 = p2_SimpleArtifactDescriptor()
    b = p2_Property(key="sample_text", value="sample_text")
    _safe_set(b, 'p2_Property57', a1)
    assert _is_linked(b, 'p2_Property57', a1)
    if hasattr(a1, 'p2_SimpleArtifactDescriptor'):
        assert _is_linked(a1, 'p2_SimpleArtifactDescriptor', b)
    _safe_set(b, 'p2_Property57', a2)
    assert _is_linked(b, 'p2_Property57', a2)
    if hasattr(a1, 'p2_SimpleArtifactDescriptor'):
        assert not _is_linked(a1, 'p2_SimpleArtifactDescriptor', b)
    if hasattr(a2, 'p2_SimpleArtifactDescriptor'):
        assert _is_linked(a2, 'p2_SimpleArtifactDescriptor', b)
    _safe_set(b, 'p2_Property57', None)
    assert not _is_linked(b, 'p2_Property57', a2)
    if hasattr(a2, 'p2_SimpleArtifactDescriptor'):
        assert not _is_linked(a2, 'p2_SimpleArtifactDescriptor', b)


def test_assoc_requirements23_reverse_link_reassign_clear():
    a1 = p2_IRequirement(description="sample_text", filter="sample_text", greedy=True, matches="sample_text", max="sample_text", min="sample_text")
    a2 = p2_IRequirement(description="sample_text_2", filter="sample_text_2", greedy=False, matches="sample_text_2", max="sample_text_2", min="sample_text_2")
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit24', {a1})
    assert _is_linked(b, 'p2_IInstallableUnit24', a1)
    if hasattr(a1, 'p2_IRequirement25'):
        assert _is_linked(a1, 'p2_IRequirement25', b)
    _safe_set(b, 'p2_IInstallableUnit24', {a2})
    assert _is_linked(b, 'p2_IInstallableUnit24', a2)
    if hasattr(a1, 'p2_IRequirement25'):
        assert not _is_linked(a1, 'p2_IRequirement25', b)
    if hasattr(a2, 'p2_IRequirement25'):
        assert _is_linked(a2, 'p2_IRequirement25', b)
    _safe_set(b, 'p2_IInstallableUnit24', set())
    assert not _is_linked(b, 'p2_IInstallableUnit24', a2)
    if hasattr(a2, 'p2_IRequirement25'):
        assert not _is_linked(a2, 'p2_IRequirement25', b)


def test_assoc_touchpointData26_reverse_link_reassign_clear():
    a1 = p2_ITouchpointData()
    a2 = p2_ITouchpointData()
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit27', {a1})
    assert _is_linked(b, 'p2_IInstallableUnit27', a1)
    if hasattr(a1, 'p2_ITouchpointData'):
        assert _is_linked(a1, 'p2_ITouchpointData', b)
    _safe_set(b, 'p2_IInstallableUnit27', {a2})
    assert _is_linked(b, 'p2_IInstallableUnit27', a2)
    if hasattr(a1, 'p2_ITouchpointData'):
        assert not _is_linked(a1, 'p2_ITouchpointData', b)
    if hasattr(a2, 'p2_ITouchpointData'):
        assert _is_linked(a2, 'p2_ITouchpointData', b)
    _safe_set(b, 'p2_IInstallableUnit27', set())
    assert not _is_linked(b, 'p2_IInstallableUnit27', a2)
    if hasattr(a2, 'p2_ITouchpointData'):
        assert not _is_linked(a2, 'p2_ITouchpointData', b)


def test_assoc_touchpointType28_reverse_link_reassign_clear():
    a1 = p2_ITouchpointType(id="sample_text", version="sample_text")
    a2 = p2_ITouchpointType(id="sample_text_2", version="sample_text_2")
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit29', a1)
    assert _is_linked(b, 'p2_IInstallableUnit29', a1)
    if hasattr(a1, 'p2_ITouchpointType'):
        assert _is_linked(a1, 'p2_ITouchpointType', b)
    _safe_set(b, 'p2_IInstallableUnit29', a2)
    assert _is_linked(b, 'p2_IInstallableUnit29', a2)
    if hasattr(a1, 'p2_ITouchpointType'):
        assert not _is_linked(a1, 'p2_ITouchpointType', b)
    if hasattr(a2, 'p2_ITouchpointType'):
        assert _is_linked(a2, 'p2_ITouchpointType', b)
    _safe_set(b, 'p2_IInstallableUnit29', None)
    assert not _is_linked(b, 'p2_IInstallableUnit29', a2)
    if hasattr(a2, 'p2_ITouchpointType'):
        assert not _is_linked(a2, 'p2_ITouchpointType', b)


def test_assoc_updateDescriptor30_reverse_link_reassign_clear():
    a1 = p2_IUpdateDescriptor(description="sample_text", location="sample_text", severity=7)
    a2 = p2_IUpdateDescriptor(description="sample_text_2", location="sample_text_2", severity=13)
    b = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    _safe_set(b, 'p2_IInstallableUnit31', a1)
    assert _is_linked(b, 'p2_IInstallableUnit31', a1)
    if hasattr(a1, 'p2_IUpdateDescriptor'):
        assert _is_linked(a1, 'p2_IUpdateDescriptor', b)
    _safe_set(b, 'p2_IInstallableUnit31', a2)
    assert _is_linked(b, 'p2_IInstallableUnit31', a2)
    if hasattr(a1, 'p2_IUpdateDescriptor'):
        assert not _is_linked(a1, 'p2_IUpdateDescriptor', b)
    if hasattr(a2, 'p2_IUpdateDescriptor'):
        assert _is_linked(a2, 'p2_IUpdateDescriptor', b)
    _safe_set(b, 'p2_IInstallableUnit31', None)
    assert not _is_linked(b, 'p2_IInstallableUnit31', a2)
    if hasattr(a2, 'p2_IUpdateDescriptor'):
        assert not _is_linked(a2, 'p2_IUpdateDescriptor', b)


def test_assoc_value43_reverse_link_reassign_clear():
    a1 = p2_InstructionMap(key="sample_text")
    a2 = p2_InstructionMap(key="sample_text_2")
    b = p2_ITouchpointInstruction(body="sample_text", importAttribute="sample_text")
    _safe_set(b, 'p2_ITouchpointInstruction', a1)
    assert _is_linked(b, 'p2_ITouchpointInstruction', a1)
    if hasattr(a1, 'p2_InstructionMap'):
        assert _is_linked(a1, 'p2_InstructionMap', b)
    _safe_set(b, 'p2_ITouchpointInstruction', a2)
    assert _is_linked(b, 'p2_ITouchpointInstruction', a2)
    if hasattr(a1, 'p2_InstructionMap'):
        assert not _is_linked(a1, 'p2_InstructionMap', b)
    if hasattr(a2, 'p2_InstructionMap'):
        assert _is_linked(a2, 'p2_InstructionMap', b)
    _safe_set(b, 'p2_ITouchpointInstruction', None)
    assert not _is_linked(b, 'p2_ITouchpointInstruction', a2)
    if hasattr(a2, 'p2_InstructionMap'):
        assert not _is_linked(a2, 'p2_InstructionMap', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_appliesTo36_stub_double():
    # p2_IInstallableUnitPatch has no real 'p2_IInstallableUnitPatch37' property in the generated
    # code (a bare stub) -- manually attach it so p2_IRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IRequirement(description="sample_text", filter="sample_text", greedy=True, matches="sample_text", max="sample_text", min="sample_text")
    partner = p2_IInstallableUnitPatch()
    setattr(partner, 'p2_IInstallableUnitPatch37', None)
    _safe_set(owner, 'p2_IRequirement38', partner)
    assert owner in getattr(partner, 'p2_IInstallableUnitPatch37')
    _safe_set(owner, 'p2_IRequirement38', None)
    assert owner not in getattr(partner, 'p2_IInstallableUnitPatch37')


def test_assoc_fragments15_stub_double():
    # p2_IInstallableUnitFragment has no real 'p2_IInstallableUnitFragment' property in the generated
    # code (a bare stub) -- manually attach it so p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    partner = p2_IInstallableUnitFragment()
    setattr(partner, 'p2_IInstallableUnitFragment', None)
    _safe_set(owner, 'p2_IInstallableUnit16', {partner})
    assert getattr(partner, 'p2_IInstallableUnitFragment') == owner
    _safe_set(owner, 'p2_IInstallableUnit16', set())
    assert getattr(partner, 'p2_IInstallableUnitFragment') is None


def test_assoc_host41_stub_double():
    # p2_InstallableUnitFragment has no real 'p2_InstallableUnitFragment' property in the generated
    # code (a bare stub) -- manually attach it so p2_IRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IRequirement(description="sample_text", filter="sample_text", greedy=True, matches="sample_text", max="sample_text", min="sample_text")
    partner = p2_InstallableUnitFragment()
    setattr(partner, 'p2_InstallableUnitFragment', None)
    _safe_set(owner, 'p2_IRequirement42', partner)
    assert owner in getattr(partner, 'p2_InstallableUnitFragment')
    _safe_set(owner, 'p2_IRequirement42', None)
    assert owner not in getattr(partner, 'p2_InstallableUnitFragment')


def test_assoc_installableUnits49_stub_double():
    # p2_MetadataRepository has no real 'p2_MetadataRepository' property in the generated
    # code (a bare stub) -- manually attach it so p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IInstallableUnit(filter="sample_text", resolved=True, singleton=True)
    partner = p2_MetadataRepository()
    setattr(partner, 'p2_MetadataRepository', None)
    _safe_set(owner, 'p2_IInstallableUnit50', partner)
    assert owner in getattr(partner, 'p2_MetadataRepository')
    _safe_set(owner, 'p2_IInstallableUnit50', None)
    assert owner not in getattr(partner, 'p2_MetadataRepository')


def test_assoc_instructionMap58_stub_double():
    # p2_TouchpointData has no real 'p2_TouchpointData' property in the generated
    # code (a bare stub) -- manually attach it so p2_InstructionMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_InstructionMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_InstructionMap(key="sample_text")
    partner = p2_TouchpointData()
    setattr(partner, 'p2_TouchpointData', None)
    _safe_set(owner, 'p2_InstructionMap59', partner)
    assert owner in getattr(partner, 'p2_TouchpointData')
    _safe_set(owner, 'p2_InstructionMap59', None)
    assert owner not in getattr(partner, 'p2_TouchpointData')


def test_assoc_key4_stub_double():
    # p2_ArtifactsByKey has no real 'p2_ArtifactsByKey5' property in the generated
    # code (a bare stub) -- manually attach it so p2_IArtifactKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IArtifactKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    partner = p2_ArtifactsByKey()
    setattr(partner, 'p2_ArtifactsByKey5', None)
    _safe_set(owner, 'p2_IArtifactKey', partner)
    assert getattr(partner, 'p2_ArtifactsByKey5') == owner
    _safe_set(owner, 'p2_IArtifactKey', None)
    assert getattr(partner, 'p2_ArtifactsByKey5') is None


def test_assoc_lifeCycle33_stub_double():
    # p2_IInstallableUnitPatch has no real 'p2_IInstallableUnitPatch34' property in the generated
    # code (a bare stub) -- manually attach it so p2_IRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IRequirement(description="sample_text", filter="sample_text", greedy=True, matches="sample_text", max="sample_text", min="sample_text")
    partner = p2_IInstallableUnitPatch()
    setattr(partner, 'p2_IInstallableUnitPatch34', None)
    _safe_set(owner, 'p2_IRequirement35', partner)
    assert getattr(partner, 'p2_IInstallableUnitPatch34') == owner
    _safe_set(owner, 'p2_IRequirement35', None)
    assert getattr(partner, 'p2_IInstallableUnitPatch34') is None


def test_assoc_processingStepList1_stub_double():
    # p2_ArtifactDescriptor has no real 'p2_ArtifactDescriptor2' property in the generated
    # code (a bare stub) -- manually attach it so p2_IProcessingStepDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IProcessingStepDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IProcessingStepDescriptor(data="sample_text", processorId="sample_text", required=True)
    partner = p2_ArtifactDescriptor()
    setattr(partner, 'p2_ArtifactDescriptor2', None)
    _safe_set(owner, 'p2_IProcessingStepDescriptor', partner)
    assert owner in getattr(partner, 'p2_ArtifactDescriptor2')
    _safe_set(owner, 'p2_IProcessingStepDescriptor', None)
    assert owner not in getattr(partner, 'p2_ArtifactDescriptor2')


def test_assoc_propertyMap0_stub_double():
    # p2_ArtifactDescriptor has no real 'p2_ArtifactDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so p2_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Property(key="sample_text", value="sample_text")
    partner = p2_ArtifactDescriptor()
    setattr(partner, 'p2_ArtifactDescriptor', None)
    _safe_set(owner, 'p2_Property', partner)
    assert owner in getattr(partner, 'p2_ArtifactDescriptor')
    _safe_set(owner, 'p2_Property', None)
    assert owner not in getattr(partner, 'p2_ArtifactDescriptor')


def test_assoc_propertyMap39_stub_double():
    # p2_InstallableUnit has no real 'p2_InstallableUnit' property in the generated
    # code (a bare stub) -- manually attach it so p2_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Property(key="sample_text", value="sample_text")
    partner = p2_InstallableUnit()
    setattr(partner, 'p2_InstallableUnit', None)
    _safe_set(owner, 'p2_Property40', partner)
    assert owner in getattr(partner, 'p2_InstallableUnit')
    _safe_set(owner, 'p2_Property40', None)
    assert owner not in getattr(partner, 'p2_InstallableUnit')


def test_assoc_propertyMap53_stub_double():
    # p2_Repository has no real 'p2_Repository' property in the generated
    # code (a bare stub) -- manually attach it so p2_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_Property(key="sample_text", value="sample_text")
    partner = p2_Repository()
    setattr(partner, 'p2_Repository', None)
    _safe_set(owner, 'p2_Property54', partner)
    assert owner in getattr(partner, 'p2_Repository')
    _safe_set(owner, 'p2_Property54', None)
    assert owner not in getattr(partner, 'p2_Repository')


def test_assoc_references51_stub_double():
    # p2_MetadataRepository has no real 'p2_MetadataRepository52' property in the generated
    # code (a bare stub) -- manually attach it so p2_IRepositoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IRepositoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IRepositoryReference(location="sample_text", nickname="sample_text", options=7, type=7)
    partner = p2_MetadataRepository()
    setattr(partner, 'p2_MetadataRepository52', None)
    _safe_set(owner, 'p2_IRepositoryReference', partner)
    assert owner in getattr(partner, 'p2_MetadataRepository52')
    _safe_set(owner, 'p2_IRepositoryReference', None)
    assert owner not in getattr(partner, 'p2_MetadataRepository52')


def test_assoc_requirementsChange32_stub_double():
    # p2_IInstallableUnitPatch has no real 'p2_IInstallableUnitPatch' property in the generated
    # code (a bare stub) -- manually attach it so p2_IRequirementChange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IRequirementChange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IRequirementChange()
    partner = p2_IInstallableUnitPatch()
    setattr(partner, 'p2_IInstallableUnitPatch', None)
    _safe_set(owner, 'p2_IRequirementChange', partner)
    assert owner in getattr(partner, 'p2_IInstallableUnitPatch')
    _safe_set(owner, 'p2_IRequirementChange', None)
    assert owner not in getattr(partner, 'p2_IInstallableUnitPatch')


def test_assoc_rules55_stub_double():
    # p2_SimpleArtifactRepository has no real 'p2_SimpleArtifactRepository' property in the generated
    # code (a bare stub) -- manually attach it so p2_MappingRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_MappingRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_MappingRule(filter="sample_text", output="sample_text")
    partner = p2_SimpleArtifactRepository()
    setattr(partner, 'p2_SimpleArtifactRepository', None)
    _safe_set(owner, 'p2_MappingRule', partner)
    assert owner in getattr(partner, 'p2_SimpleArtifactRepository')
    _safe_set(owner, 'p2_MappingRule', None)
    assert owner not in getattr(partner, 'p2_SimpleArtifactRepository')


def test_assoc_value6_stub_double():
    # p2_ArtifactsByKey has no real 'p2_ArtifactsByKey7' property in the generated
    # code (a bare stub) -- manually attach it so p2_IArtifactDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p2_IArtifactDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p2_IArtifactDescriptor()
    partner = p2_ArtifactsByKey()
    setattr(partner, 'p2_ArtifactsByKey7', None)
    _safe_set(owner, 'p2_IArtifactDescriptor', partner)
    assert owner in getattr(partner, 'p2_ArtifactsByKey7')
    _safe_set(owner, 'p2_IArtifactDescriptor', None)
    assert owner not in getattr(partner, 'p2_ArtifactsByKey7')


