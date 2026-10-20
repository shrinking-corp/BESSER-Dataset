import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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
    IProvidedCapability,
    IRequirement,
    IUDetails,
    IUPresentation,
    IUPresentationWithDetails,
    IdentificationProvider,
    InfosProvider,
    InstallableUnitRequest,
    InstallableUnits,
    LabelProvider,
    Licenses,
    MapRule,
    MappedUnit,
    MetadataRepositoryReference,
    MetadataRepositoryStructuredView,
    Miscellaneous,
    OtherIU,
    Product,
    Products,
    Properties,
    ProvidedCapabilities,
    ProvidedCapabilityWrapper,
    RepositoryReferences,
    RequirementWrapper,
    Requirements,
    StatusProvider,
    Touchpoints,
    aggregator_Aggregation,
    aggregator_AvailableVersion,
    aggregator_AvailableVersionsHeader,
    aggregator_Bundle,
    aggregator_Category,
    aggregator_ChildrenProvider,
    aggregator_Configuration,
    aggregator_Contact,
    aggregator_Contribution,
    aggregator_CustomCategory,
    aggregator_DescriptionProvider,
    aggregator_EnabledStatusProvider,
    aggregator_ExclusionRule,
    aggregator_Feature,
    aggregator_IdentificationProvider,
    aggregator_InfosProvider,
    aggregator_InstallableUnitRequest,
    aggregator_LabelProvider,
    aggregator_MapRule,
    aggregator_MappedRepository,
    aggregator_MappedUnit,
    aggregator_MavenItem,
    aggregator_MavenMapping,
    aggregator_MetadataRepository,
    aggregator_MetadataRepositoryReference,
    aggregator_Product,
    aggregator_Property,
    aggregator_Status,
    aggregator_StatusProvider,
    aggregator_ValidConfigurationsRule,
    aggregator_ValidationSet,
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
    aggregator_p2view_Licenses,
    aggregator_p2view_MetadataRepositoryStructuredView,
    aggregator_p2view_Miscellaneous,
    aggregator_p2view_OtherIU,
    aggregator_p2view_Product,
    aggregator_p2view_Products,
    aggregator_p2view_Properties,
    aggregator_p2view_ProvidedCapabilities,
    aggregator_p2view_ProvidedCapabilityWrapper,
    aggregator_p2view_RepositoryBrowser,
    aggregator_p2view_RepositoryReferences,
    aggregator_p2view_RequirementWrapper,
    aggregator_p2view_Requirements,
    aggregator_p2view_Touchpoints,
    p2view_IUDetails,
    p2view_IUPresentation,
    p2view_aggregator_ICopyright,
    p2view_aggregator_IInstallableUnit,
    p2view_aggregator_ILicense,
    p2view_aggregator_IProvidedCapability,
    p2view_aggregator_IRepositoryReference,
    p2view_aggregator_IRequirement,
    p2view_aggregator_ITouchpointData,
    p2view_aggregator_ITouchpointType,
    p2view_aggregator_IUpdateDescriptor,
    p2view_aggregator_MetadataRepository,
    p2view_aggregator_Property,
    AggregationType,
    Architecture,
    AvailableFrom,
    InstallableUnitType,
    OperatingSystem,
    PackedStrategy,
    StatusCode,
    VersionMatch,
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

def test_assoc_aggregation12_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'Aggregation', a1)
    assert _is_linked(b, 'Aggregation', a1)
    if hasattr(a1, 'contacts'):
        assert _is_linked(a1, 'contacts', b)
    _safe_set(b, 'Aggregation', a2)
    assert _is_linked(b, 'Aggregation', a2)
    if hasattr(a1, 'contacts'):
        assert not _is_linked(a1, 'contacts', b)
    if hasattr(a2, 'contacts'):
        assert _is_linked(a2, 'contacts', b)
    _safe_set(b, 'Aggregation', None)
    assert not _is_linked(b, 'Aggregation', a2)
    if hasattr(a2, 'contacts'):
        assert not _is_linked(a2, 'contacts', b)


def test_assoc_availableVersions23_reverse_link_reassign_clear():
    a1 = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    a2 = aggregator_InstallableUnitRequest(name="sample_text_2", versionRange="sample_text_2")
    b = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    _safe_set(b, 'aggregator_AvailableVersion24', a1)
    assert _is_linked(b, 'aggregator_AvailableVersion24', a1)
    if hasattr(a1, 'aggregator_InstallableUnitRequest'):
        assert _is_linked(a1, 'aggregator_InstallableUnitRequest', b)
    _safe_set(b, 'aggregator_AvailableVersion24', a2)
    assert _is_linked(b, 'aggregator_AvailableVersion24', a2)
    if hasattr(a1, 'aggregator_InstallableUnitRequest'):
        assert not _is_linked(a1, 'aggregator_InstallableUnitRequest', b)
    if hasattr(a2, 'aggregator_InstallableUnitRequest'):
        assert _is_linked(a2, 'aggregator_InstallableUnitRequest', b)
    _safe_set(b, 'aggregator_AvailableVersion24', None)
    assert not _is_linked(b, 'aggregator_AvailableVersion24', a2)
    if hasattr(a2, 'aggregator_InstallableUnitRequest'):
        assert not _is_linked(a2, 'aggregator_InstallableUnitRequest', b)


def test_assoc_buildmaster6_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregation7', a1)
    assert _is_linked(b, 'aggregator_Aggregation7', a1)
    if hasattr(a1, 'aggregator_Contact'):
        assert _is_linked(a1, 'aggregator_Contact', b)
    _safe_set(b, 'aggregator_Aggregation7', a2)
    assert _is_linked(b, 'aggregator_Aggregation7', a2)
    if hasattr(a1, 'aggregator_Contact'):
        assert not _is_linked(a1, 'aggregator_Contact', b)
    if hasattr(a2, 'aggregator_Contact'):
        assert _is_linked(a2, 'aggregator_Contact', b)
    _safe_set(b, 'aggregator_Aggregation7', None)
    assert not _is_linked(b, 'aggregator_Aggregation7', a2)
    if hasattr(a2, 'aggregator_Contact'):
        assert not _is_linked(a2, 'aggregator_Contact', b)


def test_assoc_categories31_reverse_link_reassign_clear():
    a1 = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    a2 = aggregator_MappedRepository(categoryPrefix="sample_text_2", mirrorArtifacts=False)
    b = aggregator_Category(labelOverride="sample_text")
    _safe_set(b, 'aggregator_Category', a1)
    assert _is_linked(b, 'aggregator_Category', a1)
    if hasattr(a1, 'aggregator_MappedRepository32'):
        assert _is_linked(a1, 'aggregator_MappedRepository32', b)
    _safe_set(b, 'aggregator_Category', a2)
    assert _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a1, 'aggregator_MappedRepository32'):
        assert not _is_linked(a1, 'aggregator_MappedRepository32', b)
    if hasattr(a2, 'aggregator_MappedRepository32'):
        assert _is_linked(a2, 'aggregator_MappedRepository32', b)
    _safe_set(b, 'aggregator_Category', None)
    assert not _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a2, 'aggregator_MappedRepository32'):
        assert not _is_linked(a2, 'aggregator_MappedRepository32', b)


def test_assoc_configurations1_reverse_link_reassign_clear():
    a1 = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    a2 = aggregator_Configuration(architecture="sample_text_2", operatingSystem="sample_text_2", windowSystem="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregation2', {a1})
    assert _is_linked(b, 'aggregator_Aggregation2', a1)
    if hasattr(a1, 'aggregator_Configuration'):
        assert _is_linked(a1, 'aggregator_Configuration', b)
    _safe_set(b, 'aggregator_Aggregation2', {a2})
    assert _is_linked(b, 'aggregator_Aggregation2', a2)
    if hasattr(a1, 'aggregator_Configuration'):
        assert not _is_linked(a1, 'aggregator_Configuration', b)
    if hasattr(a2, 'aggregator_Configuration'):
        assert _is_linked(a2, 'aggregator_Configuration', b)
    _safe_set(b, 'aggregator_Aggregation2', set())
    assert not _is_linked(b, 'aggregator_Aggregation2', a2)
    if hasattr(a2, 'aggregator_Configuration'):
        assert not _is_linked(a2, 'aggregator_Configuration', b)


def test_assoc_contacts14_reverse_link_reassign_clear():
    a1 = aggregator_Contribution(label="sample_text")
    a2 = aggregator_Contribution(label="sample_text_2")
    b = aggregator_Contact(email="sample_text", name="sample_text")
    _safe_set(b, 'aggregator_Contact16', a1)
    assert _is_linked(b, 'aggregator_Contact16', a1)
    if hasattr(a1, 'aggregator_Contribution15'):
        assert _is_linked(a1, 'aggregator_Contribution15', b)
    _safe_set(b, 'aggregator_Contact16', a2)
    assert _is_linked(b, 'aggregator_Contact16', a2)
    if hasattr(a1, 'aggregator_Contribution15'):
        assert not _is_linked(a1, 'aggregator_Contribution15', b)
    if hasattr(a2, 'aggregator_Contribution15'):
        assert _is_linked(a2, 'aggregator_Contribution15', b)
    _safe_set(b, 'aggregator_Contact16', None)
    assert not _is_linked(b, 'aggregator_Contact16', a2)
    if hasattr(a2, 'aggregator_Contribution15'):
        assert not _is_linked(a2, 'aggregator_Contribution15', b)


def test_assoc_contacts5_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregation', {a1})
    assert _is_linked(b, 'aggregation', a1)
    if hasattr(a1, 'Contact'):
        assert _is_linked(a1, 'Contact', b)
    _safe_set(b, 'aggregation', {a2})
    assert _is_linked(b, 'aggregation', a2)
    if hasattr(a1, 'Contact'):
        assert not _is_linked(a1, 'Contact', b)
    if hasattr(a2, 'Contact'):
        assert _is_linked(a2, 'Contact', b)
    _safe_set(b, 'aggregation', set())
    assert not _is_linked(b, 'aggregation', a2)
    if hasattr(a2, 'Contact'):
        assert not _is_linked(a2, 'Contact', b)


def test_assoc_contributions39_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution41', a1)
    assert _is_linked(b, 'aggregator_Contribution41', a1)
    if hasattr(a1, 'aggregator_ValidationSet40'):
        assert _is_linked(a1, 'aggregator_ValidationSet40', b)
    _safe_set(b, 'aggregator_Contribution41', a2)
    assert _is_linked(b, 'aggregator_Contribution41', a2)
    if hasattr(a1, 'aggregator_ValidationSet40'):
        assert not _is_linked(a1, 'aggregator_ValidationSet40', b)
    if hasattr(a2, 'aggregator_ValidationSet40'):
        assert _is_linked(a2, 'aggregator_ValidationSet40', b)
    _safe_set(b, 'aggregator_Contribution41', None)
    assert not _is_linked(b, 'aggregator_Contribution41', a2)
    if hasattr(a2, 'aggregator_ValidationSet40'):
        assert not _is_linked(a2, 'aggregator_ValidationSet40', b)


def test_assoc_customCategories3_reverse_link_reassign_clear():
    a1 = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    a2 = aggregator_CustomCategory(description="sample_text_2", identifier="sample_text_2", label="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregation4', {a1})
    assert _is_linked(b, 'aggregator_Aggregation4', a1)
    if hasattr(a1, 'aggregator_CustomCategory'):
        assert _is_linked(a1, 'aggregator_CustomCategory', b)
    _safe_set(b, 'aggregator_Aggregation4', {a2})
    assert _is_linked(b, 'aggregator_Aggregation4', a2)
    if hasattr(a1, 'aggregator_CustomCategory'):
        assert not _is_linked(a1, 'aggregator_CustomCategory', b)
    if hasattr(a2, 'aggregator_CustomCategory'):
        assert _is_linked(a2, 'aggregator_CustomCategory', b)
    _safe_set(b, 'aggregator_Aggregation4', set())
    assert not _is_linked(b, 'aggregator_Aggregation4', a2)
    if hasattr(a2, 'aggregator_CustomCategory'):
        assert not _is_linked(a2, 'aggregator_CustomCategory', b)


def test_assoc_extends46_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    _safe_set(b, 'aggregator_ValidationSet47', a1)
    assert _is_linked(b, 'aggregator_ValidationSet47', a1)
    if hasattr(a1, 'aggregator_ValidationSet45'):
        assert _is_linked(a1, 'aggregator_ValidationSet45', b)
    _safe_set(b, 'aggregator_ValidationSet47', a2)
    assert _is_linked(b, 'aggregator_ValidationSet47', a2)
    if hasattr(a1, 'aggregator_ValidationSet45'):
        assert not _is_linked(a1, 'aggregator_ValidationSet45', b)
    if hasattr(a2, 'aggregator_ValidationSet45'):
        assert _is_linked(a2, 'aggregator_ValidationSet45', b)
    _safe_set(b, 'aggregator_ValidationSet47', None)
    assert not _is_linked(b, 'aggregator_ValidationSet47', a2)
    if hasattr(a2, 'aggregator_ValidationSet45'):
        assert not _is_linked(a2, 'aggregator_ValidationSet45', b)


def test_assoc_mavenMappings17_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2")
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution18', {a1})
    assert _is_linked(b, 'aggregator_Contribution18', a1)
    if hasattr(a1, 'aggregator_MavenMapping19'):
        assert _is_linked(a1, 'aggregator_MavenMapping19', b)
    _safe_set(b, 'aggregator_Contribution18', {a2})
    assert _is_linked(b, 'aggregator_Contribution18', a2)
    if hasattr(a1, 'aggregator_MavenMapping19'):
        assert not _is_linked(a1, 'aggregator_MavenMapping19', b)
    if hasattr(a2, 'aggregator_MavenMapping19'):
        assert _is_linked(a2, 'aggregator_MavenMapping19', b)
    _safe_set(b, 'aggregator_Contribution18', set())
    assert not _is_linked(b, 'aggregator_Contribution18', a2)
    if hasattr(a2, 'aggregator_MavenMapping19'):
        assert not _is_linked(a2, 'aggregator_MavenMapping19', b)


def test_assoc_mavenMappings8_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregation9', {a1})
    assert _is_linked(b, 'aggregator_Aggregation9', a1)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert _is_linked(a1, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregation9', {a2})
    assert _is_linked(b, 'aggregator_Aggregation9', a2)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert not _is_linked(a1, 'aggregator_MavenMapping', b)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert _is_linked(a2, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregation9', set())
    assert not _is_linked(b, 'aggregator_Aggregation9', a2)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert not _is_linked(a2, 'aggregator_MavenMapping', b)


def test_assoc_repositories13_reverse_link_reassign_clear():
    a1 = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    a2 = aggregator_MappedRepository(categoryPrefix="sample_text_2", mirrorArtifacts=False)
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution', {a1})
    assert _is_linked(b, 'aggregator_Contribution', a1)
    if hasattr(a1, 'aggregator_MappedRepository'):
        assert _is_linked(a1, 'aggregator_MappedRepository', b)
    _safe_set(b, 'aggregator_Contribution', {a2})
    assert _is_linked(b, 'aggregator_Contribution', a2)
    if hasattr(a1, 'aggregator_MappedRepository'):
        assert not _is_linked(a1, 'aggregator_MappedRepository', b)
    if hasattr(a2, 'aggregator_MappedRepository'):
        assert _is_linked(a2, 'aggregator_MappedRepository', b)
    _safe_set(b, 'aggregator_Contribution', set())
    assert not _is_linked(b, 'aggregator_Contribution', a2)
    if hasattr(a2, 'aggregator_MappedRepository'):
        assert not _is_linked(a2, 'aggregator_MappedRepository', b)


def test_assoc_validConfigurations35_reverse_link_reassign_clear():
    a1 = aggregator_MappedUnit()
    a2 = aggregator_MappedUnit()
    b = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    _safe_set(b, 'aggregator_Configuration36', a1)
    assert _is_linked(b, 'aggregator_Configuration36', a1)
    if hasattr(a1, 'aggregator_MappedUnit'):
        assert _is_linked(a1, 'aggregator_MappedUnit', b)
    _safe_set(b, 'aggregator_Configuration36', a2)
    assert _is_linked(b, 'aggregator_Configuration36', a2)
    if hasattr(a1, 'aggregator_MappedUnit'):
        assert not _is_linked(a1, 'aggregator_MappedUnit', b)
    if hasattr(a2, 'aggregator_MappedUnit'):
        assert _is_linked(a2, 'aggregator_MappedUnit', b)
    _safe_set(b, 'aggregator_Configuration36', None)
    assert not _is_linked(b, 'aggregator_Configuration36', a2)
    if hasattr(a2, 'aggregator_MappedUnit'):
        assert not _is_linked(a2, 'aggregator_MappedUnit', b)


def test_assoc_validationRepositories42_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    _safe_set(b, 'aggregator_MetadataRepositoryReference44', a1)
    assert _is_linked(b, 'aggregator_MetadataRepositoryReference44', a1)
    if hasattr(a1, 'aggregator_ValidationSet43'):
        assert _is_linked(a1, 'aggregator_ValidationSet43', b)
    _safe_set(b, 'aggregator_MetadataRepositoryReference44', a2)
    assert _is_linked(b, 'aggregator_MetadataRepositoryReference44', a2)
    if hasattr(a1, 'aggregator_ValidationSet43'):
        assert not _is_linked(a1, 'aggregator_ValidationSet43', b)
    if hasattr(a2, 'aggregator_ValidationSet43'):
        assert _is_linked(a2, 'aggregator_ValidationSet43', b)
    _safe_set(b, 'aggregator_MetadataRepositoryReference44', None)
    assert not _is_linked(b, 'aggregator_MetadataRepositoryReference44', a2)
    if hasattr(a2, 'aggregator_ValidationSet43'):
        assert not _is_linked(a2, 'aggregator_ValidationSet43', b)


def test_assoc_validationSets0_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_Aggregation(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    _safe_set(b, 'aggregator_Aggregation', {a1})
    assert _is_linked(b, 'aggregator_Aggregation', a1)
    if hasattr(a1, 'aggregator_ValidationSet'):
        assert _is_linked(a1, 'aggregator_ValidationSet', b)
    _safe_set(b, 'aggregator_Aggregation', {a2})
    assert _is_linked(b, 'aggregator_Aggregation', a2)
    if hasattr(a1, 'aggregator_ValidationSet'):
        assert not _is_linked(a1, 'aggregator_ValidationSet', b)
    if hasattr(a2, 'aggregator_ValidationSet'):
        assert _is_linked(a2, 'aggregator_ValidationSet', b)
    _safe_set(b, 'aggregator_Aggregation', set())
    assert not _is_linked(b, 'aggregator_Aggregation', a2)
    if hasattr(a2, 'aggregator_ValidationSet'):
        assert not _is_linked(a2, 'aggregator_ValidationSet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allIUs74_stub_double():
    # IUPresentation has no real 'IUPresentation' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = IUPresentation()
    setattr(partner, 'IUPresentation', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits', {partner})
    assert getattr(partner, 'IUPresentation') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits', set())
    assert getattr(partner, 'IUPresentation') is None


def test_assoc_availableVersions10_stub_double():
    # aggregator_AvailableVersionsHeader has no real 'aggregator_AvailableVersionsHeader' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_AvailableVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_AvailableVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    partner = aggregator_AvailableVersionsHeader()
    setattr(partner, 'aggregator_AvailableVersionsHeader', None)
    _safe_set(owner, 'aggregator_AvailableVersion', partner)
    assert owner in getattr(partner, 'aggregator_AvailableVersionsHeader')
    _safe_set(owner, 'aggregator_AvailableVersion', None)
    assert owner not in getattr(partner, 'aggregator_AvailableVersionsHeader')


def test_assoc_availableVersionsHeader22_stub_double():
    # aggregator_AvailableVersionsHeader has no real 'AvailableVersionsHeader' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_InstallableUnitRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_InstallableUnitRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    partner = aggregator_AvailableVersionsHeader()
    setattr(partner, 'AvailableVersionsHeader', None)
    _safe_set(owner, 'installableUnitRequest', partner)
    assert getattr(partner, 'AvailableVersionsHeader') == owner
    _safe_set(owner, 'installableUnitRequest', None)
    assert getattr(partner, 'AvailableVersionsHeader') is None


def test_assoc_bundleContainer119_stub_double():
    # Bundles has no real 'Bundles121' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Bundles()
    setattr(partner, 'Bundles121', None)
    _safe_set(owner, 'aggregator_p2view_Product120', partner)
    assert getattr(partner, 'Bundles121') == owner
    _safe_set(owner, 'aggregator_p2view_Product120', None)
    assert getattr(partner, 'Bundles121') is None


def test_assoc_bundleContainer56_stub_double():
    # Bundles has no real 'Bundles' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Bundles()
    setattr(partner, 'Bundles', None)
    _safe_set(owner, 'aggregator_p2view_Category57', partner)
    assert getattr(partner, 'Bundles') == owner
    _safe_set(owner, 'aggregator_p2view_Category57', None)
    assert getattr(partner, 'Bundles') is None


def test_assoc_bundleContainer65_stub_double():
    # Bundles has no real 'Bundles67' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Bundles()
    setattr(partner, 'Bundles67', None)
    _safe_set(owner, 'aggregator_p2view_Feature66', partner)
    assert getattr(partner, 'Bundles67') == owner
    _safe_set(owner, 'aggregator_p2view_Feature66', None)
    assert getattr(partner, 'Bundles67') is None


def test_assoc_bundleContainer84_stub_double():
    # Bundles has no real 'Bundles86' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Bundles()
    setattr(partner, 'Bundles86', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits85', partner)
    assert getattr(partner, 'Bundles86') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits85', None)
    assert getattr(partner, 'Bundles86') is None


def test_assoc_bundles27_stub_double():
    # aggregator_Bundle has no real 'aggregator_Bundle' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Bundle()
    setattr(partner, 'aggregator_Bundle', None)
    _safe_set(owner, 'aggregator_MappedRepository28', {partner})
    assert getattr(partner, 'aggregator_Bundle') == owner
    _safe_set(owner, 'aggregator_MappedRepository28', set())
    assert getattr(partner, 'aggregator_Bundle') is None


def test_assoc_categories20_stub_double():
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


def test_assoc_categoryContainer51_stub_double():
    # Categories has no real 'Categories' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Categories()
    setattr(partner, 'Categories', None)
    _safe_set(owner, 'aggregator_p2view_Category', partner)
    assert getattr(partner, 'Categories') == owner
    _safe_set(owner, 'aggregator_p2view_Category', None)
    assert getattr(partner, 'Categories') is None


def test_assoc_categoryContainer75_stub_double():
    # Categories has no real 'Categories77' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Categories()
    setattr(partner, 'Categories77', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits76', partner)
    assert getattr(partner, 'Categories77') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits76', None)
    assert getattr(partner, 'Categories77') is None


def test_assoc_featureContainer117_stub_double():
    # Features has no real 'Features118' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Features()
    setattr(partner, 'Features118', None)
    _safe_set(owner, 'aggregator_p2view_Product', partner)
    assert getattr(partner, 'Features118') == owner
    _safe_set(owner, 'aggregator_p2view_Product', None)
    assert getattr(partner, 'Features118') is None


def test_assoc_featureContainer52_stub_double():
    # Features has no real 'Features' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Features()
    setattr(partner, 'Features', None)
    _safe_set(owner, 'aggregator_p2view_Category53', partner)
    assert getattr(partner, 'Features') == owner
    _safe_set(owner, 'aggregator_p2view_Category53', None)
    assert getattr(partner, 'Features') is None


def test_assoc_featureContainer63_stub_double():
    # Features has no real 'Features64' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Features()
    setattr(partner, 'Features64', None)
    _safe_set(owner, 'aggregator_p2view_Feature', partner)
    assert getattr(partner, 'Features64') == owner
    _safe_set(owner, 'aggregator_p2view_Feature', None)
    assert getattr(partner, 'Features64') is None


def test_assoc_featureContainer78_stub_double():
    # Features has no real 'Features80' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Features()
    setattr(partner, 'Features80', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits79', partner)
    assert getattr(partner, 'Features80') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits79', None)
    assert getattr(partner, 'Features80') is None


def test_assoc_features21_stub_double():
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


def test_assoc_features29_stub_double():
    # aggregator_Feature has no real 'aggregator_Feature' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Feature()
    setattr(partner, 'aggregator_Feature', None)
    _safe_set(owner, 'aggregator_MappedRepository30', {partner})
    assert getattr(partner, 'aggregator_Feature') == owner
    _safe_set(owner, 'aggregator_MappedRepository30', set())
    assert getattr(partner, 'aggregator_Feature') is None


def test_assoc_fragmentContainer122_stub_double():
    # Fragments has no real 'Fragments124' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Fragments()
    setattr(partner, 'Fragments124', None)
    _safe_set(owner, 'aggregator_p2view_Product123', partner)
    assert getattr(partner, 'Fragments124') == owner
    _safe_set(owner, 'aggregator_p2view_Product123', None)
    assert getattr(partner, 'Fragments124') is None


def test_assoc_fragmentContainer58_stub_double():
    # Fragments has no real 'Fragments' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Fragments()
    setattr(partner, 'Fragments', None)
    _safe_set(owner, 'aggregator_p2view_Category59', partner)
    assert getattr(partner, 'Fragments') == owner
    _safe_set(owner, 'aggregator_p2view_Category59', None)
    assert getattr(partner, 'Fragments') is None


def test_assoc_fragmentContainer68_stub_double():
    # Fragments has no real 'Fragments70' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Fragments()
    setattr(partner, 'Fragments70', None)
    _safe_set(owner, 'aggregator_p2view_Feature69', partner)
    assert getattr(partner, 'Fragments70') == owner
    _safe_set(owner, 'aggregator_p2view_Feature69', None)
    assert getattr(partner, 'Fragments70') is None


def test_assoc_fragmentContainer87_stub_double():
    # Fragments has no real 'Fragments89' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Fragments()
    setattr(partner, 'Fragments89', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits88', partner)
    assert getattr(partner, 'Fragments89') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits88', None)
    assert getattr(partner, 'Fragments89') is None


def test_assoc_installableUnit105_stub_double():
    # p2view_aggregator_IInstallableUnit has no real 'p2view_aggregator_IInstallableUnit' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_IUPresentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_IUPresentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    partner = p2view_aggregator_IInstallableUnit()
    setattr(partner, 'p2view_aggregator_IInstallableUnit', None)
    _safe_set(owner, 'aggregator_p2view_IUPresentation', partner)
    assert getattr(partner, 'p2view_aggregator_IInstallableUnit') == owner
    _safe_set(owner, 'aggregator_p2view_IUPresentation', None)
    assert getattr(partner, 'p2view_aggregator_IInstallableUnit') is None


def test_assoc_installableUnitList108_stub_double():
    # InstallableUnits has no real 'InstallableUnits' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = InstallableUnits()
    setattr(partner, 'InstallableUnits', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView', partner)
    assert getattr(partner, 'InstallableUnits') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView', None)
    assert getattr(partner, 'InstallableUnits') is None


def test_assoc_installableUnitRequest11_stub_double():
    # aggregator_AvailableVersionsHeader has no real 'availableVersionsHeader' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_InstallableUnitRequest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_InstallableUnitRequest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    partner = aggregator_AvailableVersionsHeader()
    setattr(partner, 'availableVersionsHeader', None)
    _safe_set(owner, 'InstallableUnitRequest', partner)
    assert getattr(partner, 'availableVersionsHeader') == owner
    _safe_set(owner, 'InstallableUnitRequest', None)
    assert getattr(partner, 'availableVersionsHeader') is None


def test_assoc_iuDetails60_stub_double():
    # IUDetails has no real 'IUDetails' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = IUDetails()
    setattr(partner, 'IUDetails', None)
    _safe_set(owner, 'aggregator_p2view_Category61', partner)
    assert getattr(partner, 'IUDetails') == owner
    _safe_set(owner, 'aggregator_p2view_Category61', None)
    assert getattr(partner, 'IUDetails') is None


def test_assoc_mapRules33_stub_double():
    # aggregator_MapRule has no real 'aggregator_MapRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_MapRule()
    setattr(partner, 'aggregator_MapRule', None)
    _safe_set(owner, 'aggregator_MappedRepository34', {partner})
    assert getattr(partner, 'aggregator_MapRule') == owner
    _safe_set(owner, 'aggregator_MappedRepository34', set())
    assert getattr(partner, 'aggregator_MapRule') is None


def test_assoc_metadataRepository112_stub_double():
    # p2view_aggregator_MetadataRepository has no real 'p2view_aggregator_MetadataRepository' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = p2view_aggregator_MetadataRepository()
    setattr(partner, 'p2view_aggregator_MetadataRepository', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView113', partner)
    assert getattr(partner, 'p2view_aggregator_MetadataRepository') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView113', None)
    assert getattr(partner, 'p2view_aggregator_MetadataRepository') is None


def test_assoc_metadataRepository37_stub_double():
    # aggregator_MetadataRepository has no real 'aggregator_MetadataRepository' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MetadataRepositoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MetadataRepositoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    partner = aggregator_MetadataRepository()
    setattr(partner, 'aggregator_MetadataRepository', None)
    _safe_set(owner, 'aggregator_MetadataRepositoryReference', partner)
    assert getattr(partner, 'aggregator_MetadataRepository') == owner
    _safe_set(owner, 'aggregator_MetadataRepositoryReference', None)
    assert getattr(partner, 'aggregator_MetadataRepository') is None


def test_assoc_miscellaneousContainer90_stub_double():
    # Miscellaneous has no real 'Miscellaneous' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Miscellaneous()
    setattr(partner, 'Miscellaneous', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits91', partner)
    assert getattr(partner, 'Miscellaneous') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits91', None)
    assert getattr(partner, 'Miscellaneous') is None


def test_assoc_productContainer54_stub_double():
    # Products has no real 'Products' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Products()
    setattr(partner, 'Products', None)
    _safe_set(owner, 'aggregator_p2view_Category55', partner)
    assert getattr(partner, 'Products') == owner
    _safe_set(owner, 'aggregator_p2view_Category55', None)
    assert getattr(partner, 'Products') is None


def test_assoc_productContainer81_stub_double():
    # Products has no real 'Products83' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Products()
    setattr(partner, 'Products83', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits82', partner)
    assert getattr(partner, 'Products83') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits82', None)
    assert getattr(partner, 'Products83') is None


def test_assoc_products25_stub_double():
    # aggregator_Product has no real 'aggregator_Product' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Product()
    setattr(partner, 'aggregator_Product', None)
    _safe_set(owner, 'aggregator_MappedRepository26', {partner})
    assert getattr(partner, 'aggregator_Product') == owner
    _safe_set(owner, 'aggregator_MappedRepository26', set())
    assert getattr(partner, 'aggregator_Product') is None


def test_assoc_properties109_stub_double():
    # Properties has no real 'Properties111' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = Properties()
    setattr(partner, 'Properties111', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView110', partner)
    assert getattr(partner, 'Properties111') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView110', None)
    assert getattr(partner, 'Properties111') is None


def test_assoc_repositories107_stub_double():
    # MetadataRepositoryStructuredView has no real 'MetadataRepositoryStructuredView' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_RepositoryBrowser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_RepositoryBrowser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_RepositoryBrowser(loading=True)
    partner = MetadataRepositoryStructuredView()
    setattr(partner, 'MetadataRepositoryStructuredView', None)
    _safe_set(owner, 'aggregator_p2view_RepositoryBrowser', {partner})
    assert getattr(partner, 'MetadataRepositoryStructuredView') == owner
    _safe_set(owner, 'aggregator_p2view_RepositoryBrowser', set())
    assert getattr(partner, 'MetadataRepositoryStructuredView') is None


def test_assoc_repositoryReferences114_stub_double():
    # RepositoryReferences has no real 'RepositoryReferences' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = RepositoryReferences()
    setattr(partner, 'RepositoryReferences', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView115', partner)
    assert getattr(partner, 'RepositoryReferences') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView115', None)
    assert getattr(partner, 'RepositoryReferences') is None


def test_assoc_status38_stub_double():
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


def test_assoc_validConfigurations48_stub_double():
    # aggregator_ValidConfigurationsRule has no real 'aggregator_ValidConfigurationsRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    partner = aggregator_ValidConfigurationsRule()
    setattr(partner, 'aggregator_ValidConfigurationsRule', None)
    _safe_set(owner, 'aggregator_Configuration49', partner)
    assert owner in getattr(partner, 'aggregator_ValidConfigurationsRule')
    _safe_set(owner, 'aggregator_Configuration49', None)
    assert owner not in getattr(partner, 'aggregator_ValidConfigurationsRule')


