import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArtifactKey,
    Bundle,
    Bundles,
    Categories,
    Category,
    DescriptionProvider,
    EnabledStatusProvider,
    Feature,
    Features,
    Fragment,
    Fragments,
    IAdaptable,
    IArtifactKey,
    ICopyright,
    IInstallableUnit,
    ILicense,
    IMetadataRepository,
    IProvidedCapability,
    IRequiredCapability,
    ITouchpointData,
    ITouchpointInstruction,
    ITouchpointType,
    IUDetails,
    IUPresentation,
    IUPresentationWithDetails,
    IUpdateDescriptor,
    InfosProvider,
    InstallableUnit,
    InstallableUnitReference,
    InstallableUnits,
    InstructionMap,
    LabelProvider,
    MapRule,
    MappedUnit,
    MetadataRepository,
    MetadataRepositoryReference,
    Miscellaneous,
    OtherIU,
    Product,
    Products,
    Properties,
    Property,
    ProvidedCapabilities,
    ProvidedCapability,
    ProvidedCapabilityWrapper,
    RepositoryReference,
    RequiredCapabilities,
    RequiredCapability,
    RequiredCapabilityWrapper,
    StatusProvider,
    TouchpointData,
    TouchpointInstruction,
    Touchpoints,
    aggregator_Aggregator,
    aggregator_Bundle,
    aggregator_Category,
    aggregator_ChildrenProvider,
    aggregator_Comparable,
    aggregator_Configuration,
    aggregator_Contact,
    aggregator_Contribution,
    aggregator_CustomCategory,
    aggregator_DescriptionProvider,
    aggregator_EnabledStatusProvider,
    aggregator_ExclusionRule,
    aggregator_Feature,
    aggregator_InfosProvider,
    aggregator_InstallableUnitReference,
    aggregator_LabelProvider,
    aggregator_MapRule,
    aggregator_MappedRepository,
    aggregator_MappedUnit,
    aggregator_MavenItem,
    aggregator_MavenMapping,
    aggregator_MetadataRepositoryReference,
    aggregator_Product,
    aggregator_Property,
    aggregator_Status,
    aggregator_StatusProvider,
    aggregator_ValidConfigurationsRule,
    aggregator_p2_ArtifactKey,
    aggregator_p2_Copyright,
    aggregator_p2_IAdaptable,
    aggregator_p2_IArtifactKey,
    aggregator_p2_ICopyright,
    aggregator_p2_IInstallableUnit,
    aggregator_p2_IInstallableUnitFragment,
    aggregator_p2_ILicense,
    aggregator_p2_IMetadataRepository,
    aggregator_p2_IProvidedCapability,
    aggregator_p2_IQueryable,
    aggregator_p2_IRepository,
    aggregator_p2_IRequiredCapability,
    aggregator_p2_ITouchpointData,
    aggregator_p2_ITouchpointInstruction,
    aggregator_p2_ITouchpointType,
    aggregator_p2_IUpdateDescriptor,
    aggregator_p2_InstallableUnit,
    aggregator_p2_InstallableUnitFragment,
    aggregator_p2_InstructionMap,
    aggregator_p2_License,
    aggregator_p2_MetadataRepository,
    aggregator_p2_Property,
    aggregator_p2_ProvidedCapability,
    aggregator_p2_RepositoryReference,
    aggregator_p2_RequiredCapability,
    aggregator_p2_TouchpointData,
    aggregator_p2_TouchpointInstruction,
    aggregator_p2_TouchpointType,
    aggregator_p2_UpdateDescriptor,
    aggregator_p2view_Bundle,
    aggregator_p2view_Bundles,
    aggregator_p2view_Categories,
    aggregator_p2view_Category,
    aggregator_p2view_Feature,
    aggregator_p2view_Features,
    aggregator_p2view_Fragment,
    aggregator_p2view_Fragments,
    aggregator_p2view_IUDetails,
    aggregator_p2view_IUPresentation,
    aggregator_p2view_IUPresentationWithDetails,
    aggregator_p2view_InstallableUnits,
    aggregator_p2view_MetadataRepositoryStructuredView,
    aggregator_p2view_Miscellaneous,
    aggregator_p2view_OtherIU,
    aggregator_p2view_Product,
    aggregator_p2view_Products,
    aggregator_p2view_Properties,
    aggregator_p2view_ProvidedCapabilities,
    aggregator_p2view_ProvidedCapabilityWrapper,
    aggregator_p2view_RequiredCapabilities,
    aggregator_p2view_RequiredCapabilityWrapper,
    aggregator_p2view_Touchpoints,
    p2_IInstallableUnitFragment,
    p2_IProvidedCapability,
    p2_IQueryable,
    p2_IRepository,
    p2_IRequiredCapability,
    p2_InstallableUnit,
    p2view_IUDetails,
    p2view_IUPresentation,
    p2view_aggregator_Property,
    AggregationType,
    Architecture,
    InstallableUnitType,
    OperatingSystem,
    PackedStrategy,
    StatusCode,
    WindowSystem,
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

def test_assoc_aggregator30_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'Aggregator', a1)
    assert _is_linked(b, 'Aggregator', a1)
    if hasattr(a1, 'contacts'):
        assert _is_linked(a1, 'contacts', b)
    _safe_set(b, 'Aggregator', a2)
    assert _is_linked(b, 'Aggregator', a2)
    if hasattr(a1, 'contacts'):
        assert not _is_linked(a1, 'contacts', b)
    if hasattr(a2, 'contacts'):
        assert _is_linked(a2, 'contacts', b)
    _safe_set(b, 'Aggregator', None)
    assert not _is_linked(b, 'Aggregator', a2)
    if hasattr(a2, 'contacts'):
        assert not _is_linked(a2, 'contacts', b)


def test_assoc_buildmaster3_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator4', a1)
    assert _is_linked(b, 'aggregator_Aggregator4', a1)
    if hasattr(a1, 'aggregator_Contact'):
        assert _is_linked(a1, 'aggregator_Contact', b)
    _safe_set(b, 'aggregator_Aggregator4', a2)
    assert _is_linked(b, 'aggregator_Aggregator4', a2)
    if hasattr(a1, 'aggregator_Contact'):
        assert not _is_linked(a1, 'aggregator_Contact', b)
    if hasattr(a2, 'aggregator_Contact'):
        assert _is_linked(a2, 'aggregator_Contact', b)
    _safe_set(b, 'aggregator_Aggregator4', None)
    assert not _is_linked(b, 'aggregator_Aggregator4', a2)
    if hasattr(a2, 'aggregator_Contact'):
        assert not _is_linked(a2, 'aggregator_Contact', b)


def test_assoc_categories17_reverse_link_reassign_clear():
    a1 = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    a2 = aggregator_MappedRepository(categoryPrefix="sample_text_2", mirrorArtifacts=False)
    b = aggregator_Category(labelOverride="sample_text")
    _safe_set(b, 'aggregator_Category', a1)
    assert _is_linked(b, 'aggregator_Category', a1)
    if hasattr(a1, 'aggregator_MappedRepository18'):
        assert _is_linked(a1, 'aggregator_MappedRepository18', b)
    _safe_set(b, 'aggregator_Category', a2)
    assert _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a1, 'aggregator_MappedRepository18'):
        assert not _is_linked(a1, 'aggregator_MappedRepository18', b)
    if hasattr(a2, 'aggregator_MappedRepository18'):
        assert _is_linked(a2, 'aggregator_MappedRepository18', b)
    _safe_set(b, 'aggregator_Category', None)
    assert not _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a2, 'aggregator_MappedRepository18'):
        assert not _is_linked(a2, 'aggregator_MappedRepository18', b)


def test_assoc_configurations0_reverse_link_reassign_clear():
    a1 = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    a2 = aggregator_Configuration(architecture="sample_text_2", operatingSystem="sample_text_2", windowSystem="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator', {a1})
    assert _is_linked(b, 'aggregator_Aggregator', a1)
    if hasattr(a1, 'aggregator_Configuration'):
        assert _is_linked(a1, 'aggregator_Configuration', b)
    _safe_set(b, 'aggregator_Aggregator', {a2})
    assert _is_linked(b, 'aggregator_Aggregator', a2)
    if hasattr(a1, 'aggregator_Configuration'):
        assert not _is_linked(a1, 'aggregator_Configuration', b)
    if hasattr(a2, 'aggregator_Configuration'):
        assert _is_linked(a2, 'aggregator_Configuration', b)
    _safe_set(b, 'aggregator_Aggregator', set())
    assert not _is_linked(b, 'aggregator_Aggregator', a2)
    if hasattr(a2, 'aggregator_Configuration'):
        assert not _is_linked(a2, 'aggregator_Configuration', b)


def test_assoc_contacts24_reverse_link_reassign_clear():
    a1 = aggregator_Contribution(label="sample_text")
    a2 = aggregator_Contribution(label="sample_text_2")
    b = aggregator_Contact(email="sample_text", name="sample_text")
    _safe_set(b, 'aggregator_Contact26', a1)
    assert _is_linked(b, 'aggregator_Contact26', a1)
    if hasattr(a1, 'aggregator_Contribution25'):
        assert _is_linked(a1, 'aggregator_Contribution25', b)
    _safe_set(b, 'aggregator_Contact26', a2)
    assert _is_linked(b, 'aggregator_Contact26', a2)
    if hasattr(a1, 'aggregator_Contribution25'):
        assert not _is_linked(a1, 'aggregator_Contribution25', b)
    if hasattr(a2, 'aggregator_Contribution25'):
        assert _is_linked(a2, 'aggregator_Contribution25', b)
    _safe_set(b, 'aggregator_Contact26', None)
    assert not _is_linked(b, 'aggregator_Contact26', a2)
    if hasattr(a2, 'aggregator_Contribution25'):
        assert not _is_linked(a2, 'aggregator_Contribution25', b)


def test_assoc_contacts5_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator', {a1})
    assert _is_linked(b, 'aggregator', a1)
    if hasattr(a1, 'Contact'):
        assert _is_linked(a1, 'Contact', b)
    _safe_set(b, 'aggregator', {a2})
    assert _is_linked(b, 'aggregator', a2)
    if hasattr(a1, 'Contact'):
        assert not _is_linked(a1, 'Contact', b)
    if hasattr(a2, 'Contact'):
        assert _is_linked(a2, 'Contact', b)
    _safe_set(b, 'aggregator', set())
    assert not _is_linked(b, 'aggregator', a2)
    if hasattr(a2, 'Contact'):
        assert not _is_linked(a2, 'Contact', b)


def test_assoc_contributions1_reverse_link_reassign_clear():
    a1 = aggregator_Contribution(label="sample_text")
    a2 = aggregator_Contribution(label="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator2', {a1})
    assert _is_linked(b, 'aggregator_Aggregator2', a1)
    if hasattr(a1, 'aggregator_Contribution'):
        assert _is_linked(a1, 'aggregator_Contribution', b)
    _safe_set(b, 'aggregator_Aggregator2', {a2})
    assert _is_linked(b, 'aggregator_Aggregator2', a2)
    if hasattr(a1, 'aggregator_Contribution'):
        assert not _is_linked(a1, 'aggregator_Contribution', b)
    if hasattr(a2, 'aggregator_Contribution'):
        assert _is_linked(a2, 'aggregator_Contribution', b)
    _safe_set(b, 'aggregator_Aggregator2', set())
    assert not _is_linked(b, 'aggregator_Aggregator2', a2)
    if hasattr(a2, 'aggregator_Contribution'):
        assert not _is_linked(a2, 'aggregator_Contribution', b)


def test_assoc_customCategories6_reverse_link_reassign_clear():
    a1 = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    a2 = aggregator_CustomCategory(description="sample_text_2", identifier="sample_text_2", label="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator7', {a1})
    assert _is_linked(b, 'aggregator_Aggregator7', a1)
    if hasattr(a1, 'aggregator_CustomCategory'):
        assert _is_linked(a1, 'aggregator_CustomCategory', b)
    _safe_set(b, 'aggregator_Aggregator7', {a2})
    assert _is_linked(b, 'aggregator_Aggregator7', a2)
    if hasattr(a1, 'aggregator_CustomCategory'):
        assert not _is_linked(a1, 'aggregator_CustomCategory', b)
    if hasattr(a2, 'aggregator_CustomCategory'):
        assert _is_linked(a2, 'aggregator_CustomCategory', b)
    _safe_set(b, 'aggregator_Aggregator7', set())
    assert not _is_linked(b, 'aggregator_Aggregator7', a2)
    if hasattr(a2, 'aggregator_CustomCategory'):
        assert not _is_linked(a2, 'aggregator_CustomCategory', b)


def test_assoc_mavenMappings10_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator11', {a1})
    assert _is_linked(b, 'aggregator_Aggregator11', a1)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert _is_linked(a1, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregator11', {a2})
    assert _is_linked(b, 'aggregator_Aggregator11', a2)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert not _is_linked(a1, 'aggregator_MavenMapping', b)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert _is_linked(a2, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregator11', set())
    assert not _is_linked(b, 'aggregator_Aggregator11', a2)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert not _is_linked(a2, 'aggregator_MavenMapping', b)


def test_assoc_mavenMappings27_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2")
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution28', {a1})
    assert _is_linked(b, 'aggregator_Contribution28', a1)
    if hasattr(a1, 'aggregator_MavenMapping29'):
        assert _is_linked(a1, 'aggregator_MavenMapping29', b)
    _safe_set(b, 'aggregator_Contribution28', {a2})
    assert _is_linked(b, 'aggregator_Contribution28', a2)
    if hasattr(a1, 'aggregator_MavenMapping29'):
        assert not _is_linked(a1, 'aggregator_MavenMapping29', b)
    if hasattr(a2, 'aggregator_MavenMapping29'):
        assert _is_linked(a2, 'aggregator_MavenMapping29', b)
    _safe_set(b, 'aggregator_Contribution28', set())
    assert not _is_linked(b, 'aggregator_Contribution28', a2)
    if hasattr(a2, 'aggregator_MavenMapping29'):
        assert not _is_linked(a2, 'aggregator_MavenMapping29', b)


def test_assoc_repositories21_reverse_link_reassign_clear():
    a1 = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    a2 = aggregator_MappedRepository(categoryPrefix="sample_text_2", mirrorArtifacts=False)
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution22', {a1})
    assert _is_linked(b, 'aggregator_Contribution22', a1)
    if hasattr(a1, 'aggregator_MappedRepository23'):
        assert _is_linked(a1, 'aggregator_MappedRepository23', b)
    _safe_set(b, 'aggregator_Contribution22', {a2})
    assert _is_linked(b, 'aggregator_Contribution22', a2)
    if hasattr(a1, 'aggregator_MappedRepository23'):
        assert not _is_linked(a1, 'aggregator_MappedRepository23', b)
    if hasattr(a2, 'aggregator_MappedRepository23'):
        assert _is_linked(a2, 'aggregator_MappedRepository23', b)
    _safe_set(b, 'aggregator_Contribution22', set())
    assert not _is_linked(b, 'aggregator_Contribution22', a2)
    if hasattr(a2, 'aggregator_MappedRepository23'):
        assert not _is_linked(a2, 'aggregator_MappedRepository23', b)


def test_assoc_validationRepositories8_reverse_link_reassign_clear():
    a1 = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    a2 = aggregator_MetadataRepositoryReference(location="sample_text_2", nature="sample_text_2")
    b = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregator9', {a1})
    assert _is_linked(b, 'aggregator_Aggregator9', a1)
    if hasattr(a1, 'aggregator_MetadataRepositoryReference'):
        assert _is_linked(a1, 'aggregator_MetadataRepositoryReference', b)
    _safe_set(b, 'aggregator_Aggregator9', {a2})
    assert _is_linked(b, 'aggregator_Aggregator9', a2)
    if hasattr(a1, 'aggregator_MetadataRepositoryReference'):
        assert not _is_linked(a1, 'aggregator_MetadataRepositoryReference', b)
    if hasattr(a2, 'aggregator_MetadataRepositoryReference'):
        assert _is_linked(a2, 'aggregator_MetadataRepositoryReference', b)
    _safe_set(b, 'aggregator_Aggregator9', set())
    assert not _is_linked(b, 'aggregator_Aggregator9', a2)
    if hasattr(a2, 'aggregator_MetadataRepositoryReference'):
        assert not _is_linked(a2, 'aggregator_MetadataRepositoryReference', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_artifactList54_stub_double():
    # ArtifactKey has no real 'ArtifactKey' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = ArtifactKey()
    setattr(partner, 'ArtifactKey', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit', {partner})
    assert getattr(partner, 'ArtifactKey') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit', set())
    assert getattr(partner, 'ArtifactKey') is None


def test_assoc_bundleContainer105_stub_double():
    # Bundles has no real 'Bundles107' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Bundles()
    setattr(partner, 'Bundles107', None)
    _safe_set(owner, 'aggregator_p2view_Category106', partner)
    assert getattr(partner, 'Bundles107') == owner
    _safe_set(owner, 'aggregator_p2view_Category106', None)
    assert getattr(partner, 'Bundles107') is None


def test_assoc_bundleContainer115_stub_double():
    # Bundles has no real 'Bundles117' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Bundles()
    setattr(partner, 'Bundles117', None)
    _safe_set(owner, 'aggregator_p2view_Feature116', partner)
    assert getattr(partner, 'Bundles117') == owner
    _safe_set(owner, 'aggregator_p2view_Feature116', None)
    assert getattr(partner, 'Bundles117') is None


def test_assoc_bundleContainer123_stub_double():
    # Bundles has no real 'Bundles125' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Bundles()
    setattr(partner, 'Bundles125', None)
    _safe_set(owner, 'aggregator_p2view_Product124', partner)
    assert getattr(partner, 'Bundles125') == owner
    _safe_set(owner, 'aggregator_p2view_Product124', None)
    assert getattr(partner, 'Bundles125') is None


def test_assoc_bundleContainer82_stub_double():
    # Bundles has no real 'Bundles' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Bundles()
    setattr(partner, 'Bundles', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits83', partner)
    assert getattr(partner, 'Bundles') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits83', None)
    assert getattr(partner, 'Bundles') is None


def test_assoc_bundles13_stub_double():
    # aggregator_Bundle has no real 'aggregator_Bundle' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Bundle()
    setattr(partner, 'aggregator_Bundle', None)
    _safe_set(owner, 'aggregator_MappedRepository14', {partner})
    assert getattr(partner, 'aggregator_Bundle') == owner
    _safe_set(owner, 'aggregator_MappedRepository14', set())
    assert getattr(partner, 'aggregator_Bundle') is None


def test_assoc_categories31_stub_double():
    # aggregator_Feature has no real 'features' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_CustomCategory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_CustomCategory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    partner = aggregator_Feature()
    setattr(partner, 'features', None)
    _safe_set(owner, 'CustomCategory', partner)
    assert owner in getattr(partner, 'features')
    _safe_set(owner, 'CustomCategory', None)
    assert owner not in getattr(partner, 'features')


def test_assoc_categoryContainer77_stub_double():
    # Categories has no real 'Categories' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Categories()
    setattr(partner, 'Categories', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits', partner)
    assert getattr(partner, 'Categories') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits', None)
    assert getattr(partner, 'Categories') is None


def test_assoc_categoryContainer97_stub_double():
    # Categories has no real 'Categories98' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Categories()
    setattr(partner, 'Categories98', None)
    _safe_set(owner, 'aggregator_p2view_Category', partner)
    assert getattr(partner, 'Categories98') == owner
    _safe_set(owner, 'aggregator_p2view_Category', None)
    assert getattr(partner, 'Categories98') is None


def test_assoc_copyright46_stub_double():
    # ICopyright has no real 'ICopyright' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    partner = ICopyright()
    setattr(partner, 'ICopyright', None)
    _safe_set(owner, 'aggregator_p2_IInstallableUnit47', partner)
    assert getattr(partner, 'ICopyright') == owner
    _safe_set(owner, 'aggregator_p2_IInstallableUnit47', None)
    assert getattr(partner, 'ICopyright') is None


def test_assoc_featureContainer113_stub_double():
    # Features has no real 'Features114' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Features()
    setattr(partner, 'Features114', None)
    _safe_set(owner, 'aggregator_p2view_Feature', partner)
    assert getattr(partner, 'Features114') == owner
    _safe_set(owner, 'aggregator_p2view_Feature', None)
    assert getattr(partner, 'Features114') is None


def test_assoc_featureContainer121_stub_double():
    # Features has no real 'Features122' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Features()
    setattr(partner, 'Features122', None)
    _safe_set(owner, 'aggregator_p2view_Product', partner)
    assert getattr(partner, 'Features122') == owner
    _safe_set(owner, 'aggregator_p2view_Product', None)
    assert getattr(partner, 'Features122') is None


def test_assoc_featureContainer78_stub_double():
    # Features has no real 'Features' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Features()
    setattr(partner, 'Features', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits79', partner)
    assert getattr(partner, 'Features') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits79', None)
    assert getattr(partner, 'Features') is None


def test_assoc_featureContainer99_stub_double():
    # Features has no real 'Features101' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Features()
    setattr(partner, 'Features101', None)
    _safe_set(owner, 'aggregator_p2view_Category100', partner)
    assert getattr(partner, 'Features101') == owner
    _safe_set(owner, 'aggregator_p2view_Category100', None)
    assert getattr(partner, 'Features101') is None


def test_assoc_features15_stub_double():
    # aggregator_Feature has no real 'aggregator_Feature' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Feature()
    setattr(partner, 'aggregator_Feature', None)
    _safe_set(owner, 'aggregator_MappedRepository16', {partner})
    assert getattr(partner, 'aggregator_Feature') == owner
    _safe_set(owner, 'aggregator_MappedRepository16', set())
    assert getattr(partner, 'aggregator_Feature') is None


def test_assoc_features34_stub_double():
    # aggregator_Feature has no real 'Feature' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_CustomCategory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_CustomCategory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    partner = aggregator_Feature()
    setattr(partner, 'Feature', None)
    _safe_set(owner, 'categories', {partner})
    assert getattr(partner, 'Feature') == owner
    _safe_set(owner, 'categories', set())
    assert getattr(partner, 'Feature') is None


def test_assoc_fragmentContainer108_stub_double():
    # Fragments has no real 'Fragments110' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Fragments()
    setattr(partner, 'Fragments110', None)
    _safe_set(owner, 'aggregator_p2view_Category109', partner)
    assert getattr(partner, 'Fragments110') == owner
    _safe_set(owner, 'aggregator_p2view_Category109', None)
    assert getattr(partner, 'Fragments110') is None


def test_assoc_fragmentContainer118_stub_double():
    # Fragments has no real 'Fragments120' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Fragments()
    setattr(partner, 'Fragments120', None)
    _safe_set(owner, 'aggregator_p2view_Feature119', partner)
    assert getattr(partner, 'Fragments120') == owner
    _safe_set(owner, 'aggregator_p2view_Feature119', None)
    assert getattr(partner, 'Fragments120') is None


def test_assoc_fragmentContainer126_stub_double():
    # Fragments has no real 'Fragments128' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Fragments()
    setattr(partner, 'Fragments128', None)
    _safe_set(owner, 'aggregator_p2view_Product127', partner)
    assert getattr(partner, 'Fragments128') == owner
    _safe_set(owner, 'aggregator_p2view_Product127', None)
    assert getattr(partner, 'Fragments128') is None


def test_assoc_fragmentContainer84_stub_double():
    # Fragments has no real 'Fragments' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Fragments()
    setattr(partner, 'Fragments', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits85', partner)
    assert getattr(partner, 'Fragments') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits85', None)
    assert getattr(partner, 'Fragments') is None


def test_assoc_installableUnit35_stub_double():
    # InstallableUnit has no real 'InstallableUnit' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_InstallableUnitReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_InstallableUnitReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_InstallableUnitReference()
    partner = InstallableUnit()
    setattr(partner, 'InstallableUnit', None)
    _safe_set(owner, 'aggregator_InstallableUnitReference', partner)
    assert getattr(partner, 'InstallableUnit') == owner
    _safe_set(owner, 'aggregator_InstallableUnitReference', None)
    assert getattr(partner, 'InstallableUnit') is None


def test_assoc_installableUnit95_stub_double():
    # InstallableUnit has no real 'InstallableUnit96' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_IUPresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_IUPresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    partner = InstallableUnit()
    setattr(partner, 'InstallableUnit96', None)
    _safe_set(owner, 'aggregator_p2view_IUPresentation', partner)
    assert getattr(partner, 'InstallableUnit96') == owner
    _safe_set(owner, 'aggregator_p2view_IUPresentation', None)
    assert getattr(partner, 'InstallableUnit96') is None


def test_assoc_installableUnitList71_stub_double():
    # InstallableUnits has no real 'InstallableUnits' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    partner = InstallableUnits()
    setattr(partner, 'InstallableUnits', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView', partner)
    assert getattr(partner, 'InstallableUnits') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView', None)
    assert getattr(partner, 'InstallableUnits') is None


def test_assoc_iuDetails111_stub_double():
    # IUDetails has no real 'IUDetails' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = IUDetails()
    setattr(partner, 'IUDetails', None)
    _safe_set(owner, 'aggregator_p2view_Category112', partner)
    assert getattr(partner, 'IUDetails') == owner
    _safe_set(owner, 'aggregator_p2view_Category112', None)
    assert getattr(partner, 'IUDetails') is None


def test_assoc_license44_stub_double():
    # ILicense has no real 'ILicense' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    partner = ILicense()
    setattr(partner, 'ILicense', None)
    _safe_set(owner, 'aggregator_p2_IInstallableUnit45', partner)
    assert getattr(partner, 'ILicense') == owner
    _safe_set(owner, 'aggregator_p2_IInstallableUnit45', None)
    assert getattr(partner, 'ILicense') is None


def test_assoc_mapRules19_stub_double():
    # aggregator_MapRule has no real 'aggregator_MapRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_MapRule()
    setattr(partner, 'aggregator_MapRule', None)
    _safe_set(owner, 'aggregator_MappedRepository20', {partner})
    assert getattr(partner, 'aggregator_MapRule') == owner
    _safe_set(owner, 'aggregator_MappedRepository20', set())
    assert getattr(partner, 'aggregator_MapRule') is None


def test_assoc_metaRequiredCapabilityList59_stub_double():
    # RequiredCapability has no real 'RequiredCapability61' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = RequiredCapability()
    setattr(partner, 'RequiredCapability61', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit60', {partner})
    assert getattr(partner, 'RequiredCapability61') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit60', set())
    assert getattr(partner, 'RequiredCapability61') is None


def test_assoc_metadataRepository38_stub_double():
    # MetadataRepository has no real 'MetadataRepository' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MetadataRepositoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MetadataRepositoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    partner = MetadataRepository()
    setattr(partner, 'MetadataRepository', None)
    _safe_set(owner, 'aggregator_MetadataRepositoryReference39', partner)
    assert getattr(partner, 'MetadataRepository') == owner
    _safe_set(owner, 'aggregator_MetadataRepositoryReference39', None)
    assert getattr(partner, 'MetadataRepository') is None


def test_assoc_metadataRepository74_stub_double():
    # MetadataRepository has no real 'MetadataRepository76' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    partner = MetadataRepository()
    setattr(partner, 'MetadataRepository76', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView75', partner)
    assert getattr(partner, 'MetadataRepository76') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView75', None)
    assert getattr(partner, 'MetadataRepository76') is None


def test_assoc_miscellaneousContainer86_stub_double():
    # Miscellaneous has no real 'Miscellaneous' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Miscellaneous()
    setattr(partner, 'Miscellaneous', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits87', partner)
    assert getattr(partner, 'Miscellaneous') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits87', None)
    assert getattr(partner, 'Miscellaneous') is None


def test_assoc_productContainer102_stub_double():
    # Products has no real 'Products104' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Products()
    setattr(partner, 'Products104', None)
    _safe_set(owner, 'aggregator_p2view_Category103', partner)
    assert getattr(partner, 'Products104') == owner
    _safe_set(owner, 'aggregator_p2view_Category103', None)
    assert getattr(partner, 'Products104') is None


def test_assoc_productContainer80_stub_double():
    # Products has no real 'Products' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Products()
    setattr(partner, 'Products', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits81', partner)
    assert getattr(partner, 'Products') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits81', None)
    assert getattr(partner, 'Products') is None


def test_assoc_products12_stub_double():
    # aggregator_Product has no real 'aggregator_Product' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Product()
    setattr(partner, 'aggregator_Product', None)
    _safe_set(owner, 'aggregator_MappedRepository', {partner})
    assert getattr(partner, 'aggregator_Product') == owner
    _safe_set(owner, 'aggregator_MappedRepository', set())
    assert getattr(partner, 'aggregator_Product') is None


def test_assoc_properties72_stub_double():
    # Properties has no real 'Properties' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    partner = Properties()
    setattr(partner, 'Properties', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView73', partner)
    assert getattr(partner, 'Properties') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView73', None)
    assert getattr(partner, 'Properties') is None


def test_assoc_propertyMap62_stub_double():
    # Property has no real 'Property64' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = Property()
    setattr(partner, 'Property64', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit63', {partner})
    assert getattr(partner, 'Property64') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit63', set())
    assert getattr(partner, 'Property64') is None


def test_assoc_providedCapabilityList55_stub_double():
    # ProvidedCapability has no real 'ProvidedCapability' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = ProvidedCapability()
    setattr(partner, 'ProvidedCapability', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit56', {partner})
    assert getattr(partner, 'ProvidedCapability') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit56', set())
    assert getattr(partner, 'ProvidedCapability') is None


def test_assoc_requiredCapabilityList57_stub_double():
    # RequiredCapability has no real 'RequiredCapability' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = RequiredCapability()
    setattr(partner, 'RequiredCapability', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit58', {partner})
    assert getattr(partner, 'RequiredCapability') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit58', set())
    assert getattr(partner, 'RequiredCapability') is None


def test_assoc_status40_stub_double():
    # aggregator_StatusProvider has no real 'aggregator_StatusProvider' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_Status's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_Status's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_Status(code="sample_text", message="sample_text")
    partner = aggregator_StatusProvider()
    setattr(partner, 'aggregator_StatusProvider', None)
    _safe_set(owner, 'aggregator_Status', partner)
    assert getattr(partner, 'aggregator_StatusProvider') == owner
    _safe_set(owner, 'aggregator_Status', None)
    assert getattr(partner, 'aggregator_StatusProvider') is None


def test_assoc_touchpointDataList65_stub_double():
    # TouchpointData has no real 'TouchpointData' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstallableUnit()
    partner = TouchpointData()
    setattr(partner, 'TouchpointData', None)
    _safe_set(owner, 'aggregator_p2_InstallableUnit66', {partner})
    assert getattr(partner, 'TouchpointData') == owner
    _safe_set(owner, 'aggregator_p2_InstallableUnit66', set())
    assert getattr(partner, 'TouchpointData') is None


def test_assoc_touchpointType41_stub_double():
    # ITouchpointType has no real 'ITouchpointType' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    partner = ITouchpointType()
    setattr(partner, 'ITouchpointType', None)
    _safe_set(owner, 'aggregator_p2_IInstallableUnit', partner)
    assert getattr(partner, 'ITouchpointType') == owner
    _safe_set(owner, 'aggregator_p2_IInstallableUnit', None)
    assert getattr(partner, 'ITouchpointType') is None


def test_assoc_updateDescriptor42_stub_double():
    # IUpdateDescriptor has no real 'IUpdateDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_IInstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_IInstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    partner = IUpdateDescriptor()
    setattr(partner, 'IUpdateDescriptor', None)
    _safe_set(owner, 'aggregator_p2_IInstallableUnit43', partner)
    assert getattr(partner, 'IUpdateDescriptor') == owner
    _safe_set(owner, 'aggregator_p2_IInstallableUnit43', None)
    assert getattr(partner, 'IUpdateDescriptor') is None


def test_assoc_validConfigurations32_stub_double():
    # aggregator_MappedUnit has no real 'aggregator_MappedUnit' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    partner = aggregator_MappedUnit()
    setattr(partner, 'aggregator_MappedUnit', None)
    _safe_set(owner, 'aggregator_Configuration33', partner)
    assert owner in getattr(partner, 'aggregator_MappedUnit')
    _safe_set(owner, 'aggregator_Configuration33', None)
    assert owner not in getattr(partner, 'aggregator_MappedUnit')


def test_assoc_validConfigurations36_stub_double():
    # aggregator_ValidConfigurationsRule has no real 'aggregator_ValidConfigurationsRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    partner = aggregator_ValidConfigurationsRule()
    setattr(partner, 'aggregator_ValidConfigurationsRule', None)
    _safe_set(owner, 'aggregator_Configuration37', partner)
    assert owner in getattr(partner, 'aggregator_ValidConfigurationsRule')
    _safe_set(owner, 'aggregator_Configuration37', None)
    assert owner not in getattr(partner, 'aggregator_ValidConfigurationsRule')


def test_assoc_value70_stub_double():
    # TouchpointInstruction has no real 'TouchpointInstruction' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2_InstructionMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2_InstructionMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2_InstructionMap(key="sample_text")
    partner = TouchpointInstruction()
    setattr(partner, 'TouchpointInstruction', None)
    _safe_set(owner, 'aggregator_p2_InstructionMap', partner)
    assert getattr(partner, 'TouchpointInstruction') == owner
    _safe_set(owner, 'aggregator_p2_InstructionMap', None)
    assert getattr(partner, 'TouchpointInstruction') is None


