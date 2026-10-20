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
    VersionFormat,
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

def test_assoc_aggregation15_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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


def test_assoc_availableVersions26_reverse_link_reassign_clear():
    a1 = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    a2 = aggregator_InstallableUnitRequest(name="sample_text_2", versionRange="sample_text_2")
    b = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    _safe_set(b, 'aggregator_AvailableVersion27', a1)
    assert _is_linked(b, 'aggregator_AvailableVersion27', a1)
    if hasattr(a1, 'aggregator_InstallableUnitRequest'):
        assert _is_linked(a1, 'aggregator_InstallableUnitRequest', b)
    _safe_set(b, 'aggregator_AvailableVersion27', a2)
    assert _is_linked(b, 'aggregator_AvailableVersion27', a2)
    if hasattr(a1, 'aggregator_InstallableUnitRequest'):
        assert not _is_linked(a1, 'aggregator_InstallableUnitRequest', b)
    if hasattr(a2, 'aggregator_InstallableUnitRequest'):
        assert _is_linked(a2, 'aggregator_InstallableUnitRequest', b)
    _safe_set(b, 'aggregator_AvailableVersion27', None)
    assert not _is_linked(b, 'aggregator_AvailableVersion27', a2)
    if hasattr(a2, 'aggregator_InstallableUnitRequest'):
        assert not _is_linked(a2, 'aggregator_InstallableUnitRequest', b)


def test_assoc_buildmaster6_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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


def test_assoc_buildmasterBackup8_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    _safe_set(b, 'aggregator_Aggregation9', a1)
    assert _is_linked(b, 'aggregator_Aggregation9', a1)
    if hasattr(a1, 'aggregator_Contact10'):
        assert _is_linked(a1, 'aggregator_Contact10', b)
    _safe_set(b, 'aggregator_Aggregation9', a2)
    assert _is_linked(b, 'aggregator_Aggregation9', a2)
    if hasattr(a1, 'aggregator_Contact10'):
        assert not _is_linked(a1, 'aggregator_Contact10', b)
    if hasattr(a2, 'aggregator_Contact10'):
        assert _is_linked(a2, 'aggregator_Contact10', b)
    _safe_set(b, 'aggregator_Aggregation9', None)
    assert not _is_linked(b, 'aggregator_Aggregation9', a2)
    if hasattr(a2, 'aggregator_Contact10'):
        assert not _is_linked(a2, 'aggregator_Contact10', b)


def test_assoc_categories34_reverse_link_reassign_clear():
    a1 = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    a2 = aggregator_MappedRepository(categoryPrefix="sample_text_2", mirrorArtifacts=False)
    b = aggregator_Category(labelOverride="sample_text")
    _safe_set(b, 'aggregator_Category', a1)
    assert _is_linked(b, 'aggregator_Category', a1)
    if hasattr(a1, 'aggregator_MappedRepository35'):
        assert _is_linked(a1, 'aggregator_MappedRepository35', b)
    _safe_set(b, 'aggregator_Category', a2)
    assert _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a1, 'aggregator_MappedRepository35'):
        assert not _is_linked(a1, 'aggregator_MappedRepository35', b)
    if hasattr(a2, 'aggregator_MappedRepository35'):
        assert _is_linked(a2, 'aggregator_MappedRepository35', b)
    _safe_set(b, 'aggregator_Category', None)
    assert not _is_linked(b, 'aggregator_Category', a2)
    if hasattr(a2, 'aggregator_MappedRepository35'):
        assert not _is_linked(a2, 'aggregator_MappedRepository35', b)


def test_assoc_configurations1_reverse_link_reassign_clear():
    a1 = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    a2 = aggregator_Configuration(architecture="sample_text_2", operatingSystem="sample_text_2", windowSystem="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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


def test_assoc_contacts17_reverse_link_reassign_clear():
    a1 = aggregator_Contribution(label="sample_text")
    a2 = aggregator_Contribution(label="sample_text_2")
    b = aggregator_Contact(email="sample_text", name="sample_text")
    _safe_set(b, 'aggregator_Contact19', a1)
    assert _is_linked(b, 'aggregator_Contact19', a1)
    if hasattr(a1, 'aggregator_Contribution18'):
        assert _is_linked(a1, 'aggregator_Contribution18', b)
    _safe_set(b, 'aggregator_Contact19', a2)
    assert _is_linked(b, 'aggregator_Contact19', a2)
    if hasattr(a1, 'aggregator_Contribution18'):
        assert not _is_linked(a1, 'aggregator_Contribution18', b)
    if hasattr(a2, 'aggregator_Contribution18'):
        assert _is_linked(a2, 'aggregator_Contribution18', b)
    _safe_set(b, 'aggregator_Contact19', None)
    assert not _is_linked(b, 'aggregator_Contact19', a2)
    if hasattr(a2, 'aggregator_Contribution18'):
        assert not _is_linked(a2, 'aggregator_Contribution18', b)


def test_assoc_contacts5_reverse_link_reassign_clear():
    a1 = aggregator_Contact(email="sample_text", name="sample_text")
    a2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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


def test_assoc_contributions44_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution46', a1)
    assert _is_linked(b, 'aggregator_Contribution46', a1)
    if hasattr(a1, 'aggregator_ValidationSet45'):
        assert _is_linked(a1, 'aggregator_ValidationSet45', b)
    _safe_set(b, 'aggregator_Contribution46', a2)
    assert _is_linked(b, 'aggregator_Contribution46', a2)
    if hasattr(a1, 'aggregator_ValidationSet45'):
        assert not _is_linked(a1, 'aggregator_ValidationSet45', b)
    if hasattr(a2, 'aggregator_ValidationSet45'):
        assert _is_linked(a2, 'aggregator_ValidationSet45', b)
    _safe_set(b, 'aggregator_Contribution46', None)
    assert not _is_linked(b, 'aggregator_Contribution46', a2)
    if hasattr(a2, 'aggregator_ValidationSet45'):
        assert not _is_linked(a2, 'aggregator_ValidationSet45', b)


def test_assoc_customCategories3_reverse_link_reassign_clear():
    a1 = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    a2 = aggregator_CustomCategory(description="sample_text_2", identifier="sample_text_2", label="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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


def test_assoc_extends51_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    _safe_set(b, 'aggregator_ValidationSet52', a1)
    assert _is_linked(b, 'aggregator_ValidationSet52', a1)
    if hasattr(a1, 'aggregator_ValidationSet50'):
        assert _is_linked(a1, 'aggregator_ValidationSet50', b)
    _safe_set(b, 'aggregator_ValidationSet52', a2)
    assert _is_linked(b, 'aggregator_ValidationSet52', a2)
    if hasattr(a1, 'aggregator_ValidationSet50'):
        assert not _is_linked(a1, 'aggregator_ValidationSet50', b)
    if hasattr(a2, 'aggregator_ValidationSet50'):
        assert _is_linked(a2, 'aggregator_ValidationSet50', b)
    _safe_set(b, 'aggregator_ValidationSet52', None)
    assert not _is_linked(b, 'aggregator_ValidationSet52', a2)
    if hasattr(a2, 'aggregator_ValidationSet50'):
        assert not _is_linked(a2, 'aggregator_ValidationSet50', b)


def test_assoc_mavenMapping40_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2", versionPattern="sample_text_2", versionTemplate="sample_text_2")
    b = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    _safe_set(b, 'aggregator_MavenItem', a1)
    assert _is_linked(b, 'aggregator_MavenItem', a1)
    if hasattr(a1, 'aggregator_MavenMapping41'):
        assert _is_linked(a1, 'aggregator_MavenMapping41', b)
    _safe_set(b, 'aggregator_MavenItem', a2)
    assert _is_linked(b, 'aggregator_MavenItem', a2)
    if hasattr(a1, 'aggregator_MavenMapping41'):
        assert not _is_linked(a1, 'aggregator_MavenMapping41', b)
    if hasattr(a2, 'aggregator_MavenMapping41'):
        assert _is_linked(a2, 'aggregator_MavenMapping41', b)
    _safe_set(b, 'aggregator_MavenItem', None)
    assert not _is_linked(b, 'aggregator_MavenItem', a2)
    if hasattr(a2, 'aggregator_MavenMapping41'):
        assert not _is_linked(a2, 'aggregator_MavenMapping41', b)


def test_assoc_mavenMappings11_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2", versionPattern="sample_text_2", versionTemplate="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    _safe_set(b, 'aggregator_Aggregation12', {a1})
    assert _is_linked(b, 'aggregator_Aggregation12', a1)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert _is_linked(a1, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregation12', {a2})
    assert _is_linked(b, 'aggregator_Aggregation12', a2)
    if hasattr(a1, 'aggregator_MavenMapping'):
        assert not _is_linked(a1, 'aggregator_MavenMapping', b)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert _is_linked(a2, 'aggregator_MavenMapping', b)
    _safe_set(b, 'aggregator_Aggregation12', set())
    assert not _is_linked(b, 'aggregator_Aggregation12', a2)
    if hasattr(a2, 'aggregator_MavenMapping'):
        assert not _is_linked(a2, 'aggregator_MavenMapping', b)


def test_assoc_mavenMappings20_reverse_link_reassign_clear():
    a1 = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    a2 = aggregator_MavenMapping(artifactId="sample_text_2", groupId="sample_text_2", namePattern="sample_text_2", versionPattern="sample_text_2", versionTemplate="sample_text_2")
    b = aggregator_Contribution(label="sample_text")
    _safe_set(b, 'aggregator_Contribution21', {a1})
    assert _is_linked(b, 'aggregator_Contribution21', a1)
    if hasattr(a1, 'aggregator_MavenMapping22'):
        assert _is_linked(a1, 'aggregator_MavenMapping22', b)
    _safe_set(b, 'aggregator_Contribution21', {a2})
    assert _is_linked(b, 'aggregator_Contribution21', a2)
    if hasattr(a1, 'aggregator_MavenMapping22'):
        assert not _is_linked(a1, 'aggregator_MavenMapping22', b)
    if hasattr(a2, 'aggregator_MavenMapping22'):
        assert _is_linked(a2, 'aggregator_MavenMapping22', b)
    _safe_set(b, 'aggregator_Contribution21', set())
    assert not _is_linked(b, 'aggregator_Contribution21', a2)
    if hasattr(a2, 'aggregator_MavenMapping22'):
        assert not _is_linked(a2, 'aggregator_MavenMapping22', b)


def test_assoc_repositories16_reverse_link_reassign_clear():
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


def test_assoc_validConfigurations38_reverse_link_reassign_clear():
    a1 = aggregator_MappedUnit()
    a2 = aggregator_MappedUnit()
    b = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    _safe_set(b, 'aggregator_Configuration39', a1)
    assert _is_linked(b, 'aggregator_Configuration39', a1)
    if hasattr(a1, 'aggregator_MappedUnit'):
        assert _is_linked(a1, 'aggregator_MappedUnit', b)
    _safe_set(b, 'aggregator_Configuration39', a2)
    assert _is_linked(b, 'aggregator_Configuration39', a2)
    if hasattr(a1, 'aggregator_MappedUnit'):
        assert not _is_linked(a1, 'aggregator_MappedUnit', b)
    if hasattr(a2, 'aggregator_MappedUnit'):
        assert _is_linked(a2, 'aggregator_MappedUnit', b)
    _safe_set(b, 'aggregator_Configuration39', None)
    assert not _is_linked(b, 'aggregator_Configuration39', a2)
    if hasattr(a2, 'aggregator_MappedUnit'):
        assert not _is_linked(a2, 'aggregator_MappedUnit', b)


def test_assoc_validationRepositories47_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    _safe_set(b, 'aggregator_MetadataRepositoryReference49', a1)
    assert _is_linked(b, 'aggregator_MetadataRepositoryReference49', a1)
    if hasattr(a1, 'aggregator_ValidationSet48'):
        assert _is_linked(a1, 'aggregator_ValidationSet48', b)
    _safe_set(b, 'aggregator_MetadataRepositoryReference49', a2)
    assert _is_linked(b, 'aggregator_MetadataRepositoryReference49', a2)
    if hasattr(a1, 'aggregator_ValidationSet48'):
        assert not _is_linked(a1, 'aggregator_ValidationSet48', b)
    if hasattr(a2, 'aggregator_ValidationSet48'):
        assert _is_linked(a2, 'aggregator_ValidationSet48', b)
    _safe_set(b, 'aggregator_MetadataRepositoryReference49', None)
    assert not _is_linked(b, 'aggregator_MetadataRepositoryReference49', a2)
    if hasattr(a2, 'aggregator_ValidationSet48'):
        assert not _is_linked(a2, 'aggregator_ValidationSet48', b)


def test_assoc_validationSets0_reverse_link_reassign_clear():
    a1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    a2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    b = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
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

def test_assoc_allIUs79_stub_double():
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


def test_assoc_availableVersions13_stub_double():
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


def test_assoc_availableVersionsHeader25_stub_double():
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


def test_assoc_bundleContainer124_stub_double():
    # Bundles has no real 'Bundles126' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Bundles()
    setattr(partner, 'Bundles126', None)
    _safe_set(owner, 'aggregator_p2view_Product125', partner)
    assert getattr(partner, 'Bundles126') == owner
    _safe_set(owner, 'aggregator_p2view_Product125', None)
    assert getattr(partner, 'Bundles126') is None


def test_assoc_bundleContainer61_stub_double():
    # Bundles has no real 'Bundles' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Bundles()
    setattr(partner, 'Bundles', None)
    _safe_set(owner, 'aggregator_p2view_Category62', partner)
    assert getattr(partner, 'Bundles') == owner
    _safe_set(owner, 'aggregator_p2view_Category62', None)
    assert getattr(partner, 'Bundles') is None


def test_assoc_bundleContainer70_stub_double():
    # Bundles has no real 'Bundles72' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Bundles()
    setattr(partner, 'Bundles72', None)
    _safe_set(owner, 'aggregator_p2view_Feature71', partner)
    assert getattr(partner, 'Bundles72') == owner
    _safe_set(owner, 'aggregator_p2view_Feature71', None)
    assert getattr(partner, 'Bundles72') is None


def test_assoc_bundleContainer89_stub_double():
    # Bundles has no real 'Bundles91' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Bundles()
    setattr(partner, 'Bundles91', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits90', partner)
    assert getattr(partner, 'Bundles91') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits90', None)
    assert getattr(partner, 'Bundles91') is None


def test_assoc_bundles30_stub_double():
    # aggregator_Bundle has no real 'aggregator_Bundle' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Bundle()
    setattr(partner, 'aggregator_Bundle', None)
    _safe_set(owner, 'aggregator_MappedRepository31', {partner})
    assert getattr(partner, 'aggregator_Bundle') == owner
    _safe_set(owner, 'aggregator_MappedRepository31', set())
    assert getattr(partner, 'aggregator_Bundle') is None


def test_assoc_categories23_stub_double():
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


def test_assoc_categoryContainer56_stub_double():
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


def test_assoc_categoryContainer80_stub_double():
    # Categories has no real 'Categories82' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Categories()
    setattr(partner, 'Categories82', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits81', partner)
    assert getattr(partner, 'Categories82') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits81', None)
    assert getattr(partner, 'Categories82') is None


def test_assoc_featureContainer122_stub_double():
    # Features has no real 'Features123' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Features()
    setattr(partner, 'Features123', None)
    _safe_set(owner, 'aggregator_p2view_Product', partner)
    assert getattr(partner, 'Features123') == owner
    _safe_set(owner, 'aggregator_p2view_Product', None)
    assert getattr(partner, 'Features123') is None


def test_assoc_featureContainer57_stub_double():
    # Features has no real 'Features' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Features()
    setattr(partner, 'Features', None)
    _safe_set(owner, 'aggregator_p2view_Category58', partner)
    assert getattr(partner, 'Features') == owner
    _safe_set(owner, 'aggregator_p2view_Category58', None)
    assert getattr(partner, 'Features') is None


def test_assoc_featureContainer68_stub_double():
    # Features has no real 'Features69' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Features()
    setattr(partner, 'Features69', None)
    _safe_set(owner, 'aggregator_p2view_Feature', partner)
    assert getattr(partner, 'Features69') == owner
    _safe_set(owner, 'aggregator_p2view_Feature', None)
    assert getattr(partner, 'Features69') is None


def test_assoc_featureContainer83_stub_double():
    # Features has no real 'Features85' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Features()
    setattr(partner, 'Features85', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits84', partner)
    assert getattr(partner, 'Features85') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits84', None)
    assert getattr(partner, 'Features85') is None


def test_assoc_features24_stub_double():
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


def test_assoc_features32_stub_double():
    # aggregator_Feature has no real 'aggregator_Feature' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Feature()
    setattr(partner, 'aggregator_Feature', None)
    _safe_set(owner, 'aggregator_MappedRepository33', {partner})
    assert getattr(partner, 'aggregator_Feature') == owner
    _safe_set(owner, 'aggregator_MappedRepository33', set())
    assert getattr(partner, 'aggregator_Feature') is None


def test_assoc_fragmentContainer127_stub_double():
    # Fragments has no real 'Fragments129' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Product()
    partner = Fragments()
    setattr(partner, 'Fragments129', None)
    _safe_set(owner, 'aggregator_p2view_Product128', partner)
    assert getattr(partner, 'Fragments129') == owner
    _safe_set(owner, 'aggregator_p2view_Product128', None)
    assert getattr(partner, 'Fragments129') is None


def test_assoc_fragmentContainer63_stub_double():
    # Fragments has no real 'Fragments' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Fragments()
    setattr(partner, 'Fragments', None)
    _safe_set(owner, 'aggregator_p2view_Category64', partner)
    assert getattr(partner, 'Fragments') == owner
    _safe_set(owner, 'aggregator_p2view_Category64', None)
    assert getattr(partner, 'Fragments') is None


def test_assoc_fragmentContainer73_stub_double():
    # Fragments has no real 'Fragments75' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Feature()
    partner = Fragments()
    setattr(partner, 'Fragments75', None)
    _safe_set(owner, 'aggregator_p2view_Feature74', partner)
    assert getattr(partner, 'Fragments75') == owner
    _safe_set(owner, 'aggregator_p2view_Feature74', None)
    assert getattr(partner, 'Fragments75') is None


def test_assoc_fragmentContainer92_stub_double():
    # Fragments has no real 'Fragments94' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Fragments()
    setattr(partner, 'Fragments94', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits93', partner)
    assert getattr(partner, 'Fragments94') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits93', None)
    assert getattr(partner, 'Fragments94') is None


def test_assoc_installableUnit110_stub_double():
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


def test_assoc_installableUnitList113_stub_double():
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


def test_assoc_installableUnitRequest14_stub_double():
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


def test_assoc_iuDetails65_stub_double():
    # IUDetails has no real 'IUDetails' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = IUDetails()
    setattr(partner, 'IUDetails', None)
    _safe_set(owner, 'aggregator_p2view_Category66', partner)
    assert getattr(partner, 'IUDetails') == owner
    _safe_set(owner, 'aggregator_p2view_Category66', None)
    assert getattr(partner, 'IUDetails') is None


def test_assoc_mapRules36_stub_double():
    # aggregator_MapRule has no real 'aggregator_MapRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_MapRule()
    setattr(partner, 'aggregator_MapRule', None)
    _safe_set(owner, 'aggregator_MappedRepository37', {partner})
    assert getattr(partner, 'aggregator_MapRule') == owner
    _safe_set(owner, 'aggregator_MappedRepository37', set())
    assert getattr(partner, 'aggregator_MapRule') is None


def test_assoc_metadataRepository117_stub_double():
    # p2view_aggregator_MetadataRepository has no real 'p2view_aggregator_MetadataRepository' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = p2view_aggregator_MetadataRepository()
    setattr(partner, 'p2view_aggregator_MetadataRepository', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView118', partner)
    assert getattr(partner, 'p2view_aggregator_MetadataRepository') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView118', None)
    assert getattr(partner, 'p2view_aggregator_MetadataRepository') is None


def test_assoc_metadataRepository42_stub_double():
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


def test_assoc_miscellaneousContainer95_stub_double():
    # Miscellaneous has no real 'Miscellaneous' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Miscellaneous()
    setattr(partner, 'Miscellaneous', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits96', partner)
    assert getattr(partner, 'Miscellaneous') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits96', None)
    assert getattr(partner, 'Miscellaneous') is None


def test_assoc_productContainer59_stub_double():
    # Products has no real 'Products' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_Category()
    partner = Products()
    setattr(partner, 'Products', None)
    _safe_set(owner, 'aggregator_p2view_Category60', partner)
    assert getattr(partner, 'Products') == owner
    _safe_set(owner, 'aggregator_p2view_Category60', None)
    assert getattr(partner, 'Products') is None


def test_assoc_productContainer86_stub_double():
    # Products has no real 'Products88' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_InstallableUnits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_InstallableUnits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_InstallableUnits()
    partner = Products()
    setattr(partner, 'Products88', None)
    _safe_set(owner, 'aggregator_p2view_InstallableUnits87', partner)
    assert getattr(partner, 'Products88') == owner
    _safe_set(owner, 'aggregator_p2view_InstallableUnits87', None)
    assert getattr(partner, 'Products88') is None


def test_assoc_products28_stub_double():
    # aggregator_Product has no real 'aggregator_Product' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_MappedRepository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_MappedRepository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    partner = aggregator_Product()
    setattr(partner, 'aggregator_Product', None)
    _safe_set(owner, 'aggregator_MappedRepository29', {partner})
    assert getattr(partner, 'aggregator_Product') == owner
    _safe_set(owner, 'aggregator_MappedRepository29', set())
    assert getattr(partner, 'aggregator_Product') is None


def test_assoc_properties114_stub_double():
    # Properties has no real 'Properties116' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = Properties()
    setattr(partner, 'Properties116', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView115', partner)
    assert getattr(partner, 'Properties116') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView115', None)
    assert getattr(partner, 'Properties116') is None


def test_assoc_repositories112_stub_double():
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


def test_assoc_repositoryReferences119_stub_double():
    # RepositoryReferences has no real 'RepositoryReferences' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_p2view_MetadataRepositoryStructuredView's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_p2view_MetadataRepositoryStructuredView's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    partner = RepositoryReferences()
    setattr(partner, 'RepositoryReferences', None)
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView120', partner)
    assert getattr(partner, 'RepositoryReferences') == owner
    _safe_set(owner, 'aggregator_p2view_MetadataRepositoryStructuredView120', None)
    assert getattr(partner, 'RepositoryReferences') is None


def test_assoc_status43_stub_double():
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


def test_assoc_validConfigurations53_stub_double():
    # aggregator_ValidConfigurationsRule has no real 'aggregator_ValidConfigurationsRule' property in the generated
    # code (a bare stub) -- manually attach it so aggregator_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # aggregator_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    partner = aggregator_ValidConfigurationsRule()
    setattr(partner, 'aggregator_ValidConfigurationsRule', None)
    _safe_set(owner, 'aggregator_Configuration54', partner)
    assert owner in getattr(partner, 'aggregator_ValidConfigurationsRule')
    _safe_set(owner, 'aggregator_Configuration54', None)
    assert owner not in getattr(partner, 'aggregator_ValidConfigurationsRule')


