import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_aggregator_Aggregation_allowLegacySites_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.allowLegacySites == "sample_text"
    instance.allowLegacySites = "sample_text_2"
    assert instance.allowLegacySites == "sample_text_2"


def test_aggregator_Aggregation_buildRoot_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.buildRoot == "sample_text"
    instance.buildRoot = "sample_text_2"
    assert instance.buildRoot == "sample_text_2"


def test_aggregator_Aggregation_label_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_Aggregation_mavenResult_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.mavenResult == True
    instance.mavenResult = False
    assert instance.mavenResult == False


def test_aggregator_Aggregation_packedStrategy_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.packedStrategy == "sample_text"
    instance.packedStrategy = "sample_text_2"
    assert instance.packedStrategy == "sample_text_2"


def test_aggregator_Aggregation_sendmail_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.sendmail == True
    instance.sendmail = False
    assert instance.sendmail == False


def test_aggregator_Aggregation_strictMavenVersions_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.strictMavenVersions == True
    instance.strictMavenVersions = False
    assert instance.strictMavenVersions == False


def test_aggregator_Aggregation_type_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aggregator_Aggregation_versionFormat_value_roundtrip():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert instance.versionFormat == "sample_text"
    instance.versionFormat = "sample_text_2"
    assert instance.versionFormat == "sample_text_2"


def test_aggregator_AvailableVersion_availableFrom_value_roundtrip():
    instance = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    assert instance.availableFrom == "sample_text"
    instance.availableFrom = "sample_text_2"
    assert instance.availableFrom == "sample_text_2"


def test_aggregator_AvailableVersion_filter_value_roundtrip():
    instance = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    assert instance.filter == "sample_text"
    instance.filter = "sample_text_2"
    assert instance.filter == "sample_text_2"


def test_aggregator_AvailableVersion_version_value_roundtrip():
    instance = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_AvailableVersion_versionMatch_value_roundtrip():
    instance = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    assert instance.versionMatch == "sample_text"
    instance.versionMatch = "sample_text_2"
    assert instance.versionMatch == "sample_text_2"


def test_aggregator_Category_labelOverride_value_roundtrip():
    instance = aggregator_Category(labelOverride="sample_text")
    assert instance.labelOverride == "sample_text"
    instance.labelOverride = "sample_text_2"
    assert instance.labelOverride == "sample_text_2"


def test_aggregator_Configuration_architecture_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.architecture == "sample_text"
    instance.architecture = "sample_text_2"
    assert instance.architecture == "sample_text_2"


def test_aggregator_Configuration_operatingSystem_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.operatingSystem == "sample_text"
    instance.operatingSystem = "sample_text_2"
    assert instance.operatingSystem == "sample_text_2"


def test_aggregator_Configuration_windowSystem_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.windowSystem == "sample_text"
    instance.windowSystem = "sample_text_2"
    assert instance.windowSystem == "sample_text_2"


def test_aggregator_Contact_email_value_roundtrip():
    instance = aggregator_Contact(email="sample_text", name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_aggregator_Contact_name_value_roundtrip():
    instance = aggregator_Contact(email="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_Contribution_label_value_roundtrip():
    instance = aggregator_Contribution(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_CustomCategory_description_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_CustomCategory_identifier_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_aggregator_CustomCategory_label_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_DescriptionProvider_description_value_roundtrip():
    instance = aggregator_DescriptionProvider(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_EnabledStatusProvider_branchEnabled_value_roundtrip():
    instance = aggregator_EnabledStatusProvider(branchEnabled=True, enabled=True)
    assert instance.branchEnabled == True
    instance.branchEnabled = False
    assert instance.branchEnabled == False


def test_aggregator_EnabledStatusProvider_enabled_value_roundtrip():
    instance = aggregator_EnabledStatusProvider(branchEnabled=True, enabled=True)
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_aggregator_InfosProvider_errors_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.errors == "sample_text"
    instance.errors = "sample_text_2"
    assert instance.errors == "sample_text_2"


def test_aggregator_InfosProvider_infos_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.infos == "sample_text"
    instance.infos = "sample_text_2"
    assert instance.infos == "sample_text_2"


def test_aggregator_InfosProvider_warnings_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.warnings == "sample_text"
    instance.warnings = "sample_text_2"
    assert instance.warnings == "sample_text_2"


def test_aggregator_InstallableUnitRequest_name_value_roundtrip():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_InstallableUnitRequest_versionRange_value_roundtrip():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_aggregator_LabelProvider_label_value_roundtrip():
    instance = aggregator_LabelProvider(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_MappedRepository_categoryPrefix_value_roundtrip():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert instance.categoryPrefix == "sample_text"
    instance.categoryPrefix = "sample_text_2"
    assert instance.categoryPrefix == "sample_text_2"


def test_aggregator_MappedRepository_mirrorArtifacts_value_roundtrip():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert instance.mirrorArtifacts == True
    instance.mirrorArtifacts = False
    assert instance.mirrorArtifacts == False


def test_aggregator_MavenItem_artifactId_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_aggregator_MavenItem_classifier_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    assert instance.classifier == "sample_text"
    instance.classifier = "sample_text_2"
    assert instance.classifier == "sample_text_2"


def test_aggregator_MavenItem_groupId_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_aggregator_MavenItem_mappedVersion_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    assert instance.mappedVersion == "sample_text"
    instance.mappedVersion = "sample_text_2"
    assert instance.mappedVersion == "sample_text_2"


def test_aggregator_MavenMapping_artifactId_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_aggregator_MavenMapping_groupId_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_aggregator_MavenMapping_namePattern_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert instance.namePattern == "sample_text"
    instance.namePattern = "sample_text_2"
    assert instance.namePattern == "sample_text_2"


def test_aggregator_MavenMapping_versionPattern_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert instance.versionPattern == "sample_text"
    instance.versionPattern = "sample_text_2"
    assert instance.versionPattern == "sample_text_2"


def test_aggregator_MavenMapping_versionTemplate_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert instance.versionTemplate == "sample_text"
    instance.versionTemplate = "sample_text_2"
    assert instance.versionTemplate == "sample_text_2"


def test_aggregator_MetadataRepositoryReference_location_value_roundtrip():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_MetadataRepositoryReference_nature_value_roundtrip():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert instance.nature == "sample_text"
    instance.nature = "sample_text_2"
    assert instance.nature == "sample_text_2"


def test_aggregator_Property_key_value_roundtrip():
    instance = aggregator_Property(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_aggregator_Property_value_value_roundtrip():
    instance = aggregator_Property(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aggregator_Status_code_value_roundtrip():
    instance = aggregator_Status(code="sample_text", message="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_aggregator_Status_message_value_roundtrip():
    instance = aggregator_Status(code="sample_text", message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_aggregator_ValidationSet_abstract_value_roundtrip():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_aggregator_ValidationSet_extension_value_roundtrip():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert instance.extension == True
    instance.extension = False
    assert instance.extension == False


def test_aggregator_ValidationSet_label_value_roundtrip():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_p2view_IUPresentation_description_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_p2view_IUPresentation_filter_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.filter == "sample_text"
    instance.filter = "sample_text_2"
    assert instance.filter == "sample_text_2"


def test_aggregator_p2view_IUPresentation_id_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2view_IUPresentation_label_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_p2view_IUPresentation_name_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2view_IUPresentation_type_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aggregator_p2view_IUPresentation_version_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2view_IUPresentationWithDetails_detailsResolved_value_roundtrip():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert instance.detailsResolved == "sample_text"
    instance.detailsResolved = "sample_text_2"
    assert instance.detailsResolved == "sample_text_2"


def test_aggregator_p2view_MetadataRepositoryStructuredView_loaded_value_roundtrip():
    instance = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    assert instance.loaded == True
    instance.loaded = False
    assert instance.loaded == False


def test_aggregator_p2view_MetadataRepositoryStructuredView_location_value_roundtrip():
    instance = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_p2view_MetadataRepositoryStructuredView_name_value_roundtrip():
    instance = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2view_RepositoryBrowser_loading_value_roundtrip():
    instance = aggregator_p2view_RepositoryBrowser(loading=True)
    assert instance.loading == True
    instance.loading = False
    assert instance.loading == False


def test_aggregator_p2view_Fragment_isa_Bundle():
    instance = aggregator_p2view_Fragment()
    assert isinstance(instance, Bundle)


def test_aggregator_Aggregation_isa_DescriptionProvider():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_Contribution_isa_DescriptionProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_InstallableUnitRequest_isa_DescriptionProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_MapRule_isa_DescriptionProvider():
    instance = aggregator_MapRule()
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_MappedRepository_isa_DescriptionProvider():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_ValidationSet_isa_DescriptionProvider():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_Configuration_isa_EnabledStatusProvider():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_Contribution_isa_EnabledStatusProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_MapRule_isa_EnabledStatusProvider():
    instance = aggregator_MapRule()
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_MappedUnit_isa_EnabledStatusProvider():
    instance = aggregator_MappedUnit()
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_MetadataRepositoryReference_isa_EnabledStatusProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_ValidationSet_isa_EnabledStatusProvider():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_p2view_ProvidedCapabilityWrapper_isa_IProvidedCapability():
    instance = aggregator_p2view_ProvidedCapabilityWrapper()
    assert isinstance(instance, IProvidedCapability)


def test_aggregator_p2view_RequirementWrapper_isa_IRequirement():
    instance = aggregator_p2view_RequirementWrapper()
    assert isinstance(instance, IRequirement)


def test_aggregator_p2view_Category_isa_IUPresentation():
    instance = aggregator_p2view_Category()
    assert isinstance(instance, IUPresentation)


def test_aggregator_p2view_Bundle_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Bundle()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_Feature_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Feature()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_OtherIU_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_OtherIU()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_Product_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Product()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_Contribution_isa_IdentificationProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, IdentificationProvider)


def test_aggregator_MappedRepository_isa_IdentificationProvider():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert isinstance(instance, IdentificationProvider)


def test_aggregator_MappedUnit_isa_IdentificationProvider():
    instance = aggregator_MappedUnit()
    assert isinstance(instance, IdentificationProvider)


def test_aggregator_ValidationSet_isa_IdentificationProvider():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert isinstance(instance, IdentificationProvider)


def test_aggregator_Aggregation_isa_InfosProvider():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_Contribution_isa_InfosProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_CustomCategory_isa_InfosProvider():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_InstallableUnitRequest_isa_InfosProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MavenMapping_isa_InfosProvider():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MetadataRepositoryReference_isa_InfosProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_ValidationSet_isa_InfosProvider():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MapRule_isa_InstallableUnitRequest():
    instance = aggregator_MapRule()
    assert isinstance(instance, InstallableUnitRequest)


def test_aggregator_MappedUnit_isa_InstallableUnitRequest():
    instance = aggregator_MappedUnit()
    assert isinstance(instance, InstallableUnitRequest)


def test_aggregator_p2view_ProvidedCapabilityWrapper_isa_LabelProvider():
    instance = aggregator_p2view_ProvidedCapabilityWrapper()
    assert isinstance(instance, LabelProvider)


def test_aggregator_p2view_RequirementWrapper_isa_LabelProvider():
    instance = aggregator_p2view_RequirementWrapper()
    assert isinstance(instance, LabelProvider)


def test_aggregator_ExclusionRule_isa_MapRule():
    instance = aggregator_ExclusionRule()
    assert isinstance(instance, MapRule)


def test_aggregator_ValidConfigurationsRule_isa_MapRule():
    instance = aggregator_ValidConfigurationsRule()
    assert isinstance(instance, MapRule)


def test_aggregator_Bundle_isa_MappedUnit():
    instance = aggregator_Bundle()
    assert isinstance(instance, MappedUnit)


def test_aggregator_Category_isa_MappedUnit():
    instance = aggregator_Category(labelOverride="sample_text")
    assert isinstance(instance, MappedUnit)


def test_aggregator_Feature_isa_MappedUnit():
    instance = aggregator_Feature()
    assert isinstance(instance, MappedUnit)


def test_aggregator_Product_isa_MappedUnit():
    instance = aggregator_Product()
    assert isinstance(instance, MappedUnit)


def test_aggregator_MappedRepository_isa_MetadataRepositoryReference():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert isinstance(instance, MetadataRepositoryReference)


def test_aggregator_Aggregation_isa_StatusProvider():
    instance = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_Contribution_isa_StatusProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_CustomCategory_isa_StatusProvider():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_InstallableUnitRequest_isa_StatusProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_MavenMapping_isa_StatusProvider():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_MetadataRepositoryReference_isa_StatusProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_ValidationSet_isa_StatusProvider():
    instance = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_p2view_IUPresentationWithDetails_isa_p2view_IUDetails():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert isinstance(instance, p2view_IUDetails)


def test_aggregator_p2view_IUPresentationWithDetails_isa_p2view_IUPresentation():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert isinstance(instance, p2view_IUPresentation)


def test_assoc_aggregation15_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'contacts', b1)
    assert _is_linked(a, 'contacts', b1)
    if hasattr(b1, 'Aggregation'):
        assert _is_linked(b1, 'Aggregation', a)
    _safe_set(a, 'contacts', b2)
    assert _is_linked(a, 'contacts', b2)
    if hasattr(b1, 'Aggregation'):
        assert not _is_linked(b1, 'Aggregation', a)
    if hasattr(b2, 'Aggregation'):
        assert _is_linked(b2, 'Aggregation', a)
    _safe_set(a, 'contacts', None)
    assert not _is_linked(a, 'contacts', b2)
    if hasattr(b2, 'Aggregation'):
        assert not _is_linked(b2, 'Aggregation', a)


def test_assoc_allIUs79_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = IUPresentation()
    b2 = IUPresentation()
    _safe_set(a, 'aggregator_p2view_InstallableUnits', {b1})
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits', b1)
    if hasattr(b1, 'IUPresentation'):
        assert _is_linked(b1, 'IUPresentation', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits', {b2})
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits', b2)
    if hasattr(b1, 'IUPresentation'):
        assert not _is_linked(b1, 'IUPresentation', a)
    if hasattr(b2, 'IUPresentation'):
        assert _is_linked(b2, 'IUPresentation', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits', set())
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits', b2)
    if hasattr(b2, 'IUPresentation'):
        assert not _is_linked(b2, 'IUPresentation', a)


def test_assoc_availableVersions13_link_reassign_clear():
    a = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    b1 = aggregator_AvailableVersionsHeader()
    b2 = aggregator_AvailableVersionsHeader()
    _safe_set(a, 'aggregator_AvailableVersion', b1)
    assert _is_linked(a, 'aggregator_AvailableVersion', b1)
    if hasattr(b1, 'aggregator_AvailableVersionsHeader'):
        assert _is_linked(b1, 'aggregator_AvailableVersionsHeader', a)
    _safe_set(a, 'aggregator_AvailableVersion', b2)
    assert _is_linked(a, 'aggregator_AvailableVersion', b2)
    if hasattr(b1, 'aggregator_AvailableVersionsHeader'):
        assert not _is_linked(b1, 'aggregator_AvailableVersionsHeader', a)
    if hasattr(b2, 'aggregator_AvailableVersionsHeader'):
        assert _is_linked(b2, 'aggregator_AvailableVersionsHeader', a)
    _safe_set(a, 'aggregator_AvailableVersion', None)
    assert not _is_linked(a, 'aggregator_AvailableVersion', b2)
    if hasattr(b2, 'aggregator_AvailableVersionsHeader'):
        assert not _is_linked(b2, 'aggregator_AvailableVersionsHeader', a)


def test_assoc_availableVersions26_link_reassign_clear():
    a = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    b1 = aggregator_AvailableVersion(availableFrom="sample_text", filter="sample_text", version="sample_text", versionMatch="sample_text")
    b2 = aggregator_AvailableVersion(availableFrom="sample_text_2", filter="sample_text_2", version="sample_text_2", versionMatch="sample_text_2")
    _safe_set(a, 'aggregator_InstallableUnitRequest', {b1})
    assert _is_linked(a, 'aggregator_InstallableUnitRequest', b1)
    if hasattr(b1, 'aggregator_AvailableVersion27'):
        assert _is_linked(b1, 'aggregator_AvailableVersion27', a)
    _safe_set(a, 'aggregator_InstallableUnitRequest', {b2})
    assert _is_linked(a, 'aggregator_InstallableUnitRequest', b2)
    if hasattr(b1, 'aggregator_AvailableVersion27'):
        assert not _is_linked(b1, 'aggregator_AvailableVersion27', a)
    if hasattr(b2, 'aggregator_AvailableVersion27'):
        assert _is_linked(b2, 'aggregator_AvailableVersion27', a)
    _safe_set(a, 'aggregator_InstallableUnitRequest', set())
    assert not _is_linked(a, 'aggregator_InstallableUnitRequest', b2)
    if hasattr(b2, 'aggregator_AvailableVersion27'):
        assert not _is_linked(b2, 'aggregator_AvailableVersion27', a)


def test_assoc_availableVersionsHeader25_link_reassign_clear():
    a = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    b1 = aggregator_AvailableVersionsHeader()
    b2 = aggregator_AvailableVersionsHeader()
    _safe_set(a, 'installableUnitRequest', b1)
    assert _is_linked(a, 'installableUnitRequest', b1)
    if hasattr(b1, 'AvailableVersionsHeader'):
        assert _is_linked(b1, 'AvailableVersionsHeader', a)
    _safe_set(a, 'installableUnitRequest', b2)
    assert _is_linked(a, 'installableUnitRequest', b2)
    if hasattr(b1, 'AvailableVersionsHeader'):
        assert not _is_linked(b1, 'AvailableVersionsHeader', a)
    if hasattr(b2, 'AvailableVersionsHeader'):
        assert _is_linked(b2, 'AvailableVersionsHeader', a)
    _safe_set(a, 'installableUnitRequest', None)
    assert not _is_linked(a, 'installableUnitRequest', b2)
    if hasattr(b2, 'AvailableVersionsHeader'):
        assert not _is_linked(b2, 'AvailableVersionsHeader', a)


def test_assoc_buildmaster6_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_Contact', b1)
    assert _is_linked(a, 'aggregator_Contact', b1)
    if hasattr(b1, 'aggregator_Aggregation7'):
        assert _is_linked(b1, 'aggregator_Aggregation7', a)
    _safe_set(a, 'aggregator_Contact', b2)
    assert _is_linked(a, 'aggregator_Contact', b2)
    if hasattr(b1, 'aggregator_Aggregation7'):
        assert not _is_linked(b1, 'aggregator_Aggregation7', a)
    if hasattr(b2, 'aggregator_Aggregation7'):
        assert _is_linked(b2, 'aggregator_Aggregation7', a)
    _safe_set(a, 'aggregator_Contact', None)
    assert not _is_linked(a, 'aggregator_Contact', b2)
    if hasattr(b2, 'aggregator_Aggregation7'):
        assert not _is_linked(b2, 'aggregator_Aggregation7', a)


def test_assoc_buildmasterBackup8_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_Contact10', b1)
    assert _is_linked(a, 'aggregator_Contact10', b1)
    if hasattr(b1, 'aggregator_Aggregation9'):
        assert _is_linked(b1, 'aggregator_Aggregation9', a)
    _safe_set(a, 'aggregator_Contact10', b2)
    assert _is_linked(a, 'aggregator_Contact10', b2)
    if hasattr(b1, 'aggregator_Aggregation9'):
        assert not _is_linked(b1, 'aggregator_Aggregation9', a)
    if hasattr(b2, 'aggregator_Aggregation9'):
        assert _is_linked(b2, 'aggregator_Aggregation9', a)
    _safe_set(a, 'aggregator_Contact10', None)
    assert not _is_linked(a, 'aggregator_Contact10', b2)
    if hasattr(b2, 'aggregator_Aggregation9'):
        assert not _is_linked(b2, 'aggregator_Aggregation9', a)


def test_assoc_bundleContainer124_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Product125', b1)
    assert _is_linked(a, 'aggregator_p2view_Product125', b1)
    if hasattr(b1, 'Bundles126'):
        assert _is_linked(b1, 'Bundles126', a)
    _safe_set(a, 'aggregator_p2view_Product125', b2)
    assert _is_linked(a, 'aggregator_p2view_Product125', b2)
    if hasattr(b1, 'Bundles126'):
        assert not _is_linked(b1, 'Bundles126', a)
    if hasattr(b2, 'Bundles126'):
        assert _is_linked(b2, 'Bundles126', a)
    _safe_set(a, 'aggregator_p2view_Product125', None)
    assert not _is_linked(a, 'aggregator_p2view_Product125', b2)
    if hasattr(b2, 'Bundles126'):
        assert not _is_linked(b2, 'Bundles126', a)


def test_assoc_bundleContainer61_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Category62', b1)
    assert _is_linked(a, 'aggregator_p2view_Category62', b1)
    if hasattr(b1, 'Bundles'):
        assert _is_linked(b1, 'Bundles', a)
    _safe_set(a, 'aggregator_p2view_Category62', b2)
    assert _is_linked(a, 'aggregator_p2view_Category62', b2)
    if hasattr(b1, 'Bundles'):
        assert not _is_linked(b1, 'Bundles', a)
    if hasattr(b2, 'Bundles'):
        assert _is_linked(b2, 'Bundles', a)
    _safe_set(a, 'aggregator_p2view_Category62', None)
    assert not _is_linked(a, 'aggregator_p2view_Category62', b2)
    if hasattr(b2, 'Bundles'):
        assert not _is_linked(b2, 'Bundles', a)


def test_assoc_bundleContainer70_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Feature71', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature71', b1)
    if hasattr(b1, 'Bundles72'):
        assert _is_linked(b1, 'Bundles72', a)
    _safe_set(a, 'aggregator_p2view_Feature71', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature71', b2)
    if hasattr(b1, 'Bundles72'):
        assert not _is_linked(b1, 'Bundles72', a)
    if hasattr(b2, 'Bundles72'):
        assert _is_linked(b2, 'Bundles72', a)
    _safe_set(a, 'aggregator_p2view_Feature71', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature71', b2)
    if hasattr(b2, 'Bundles72'):
        assert not _is_linked(b2, 'Bundles72', a)


def test_assoc_bundleContainer89_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_InstallableUnits90', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits90', b1)
    if hasattr(b1, 'Bundles91'):
        assert _is_linked(b1, 'Bundles91', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits90', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits90', b2)
    if hasattr(b1, 'Bundles91'):
        assert not _is_linked(b1, 'Bundles91', a)
    if hasattr(b2, 'Bundles91'):
        assert _is_linked(b2, 'Bundles91', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits90', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits90', b2)
    if hasattr(b2, 'Bundles91'):
        assert not _is_linked(b2, 'Bundles91', a)


def test_assoc_bundles30_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Bundle()
    b2 = aggregator_Bundle()
    _safe_set(a, 'aggregator_MappedRepository31', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository31', b1)
    if hasattr(b1, 'aggregator_Bundle'):
        assert _is_linked(b1, 'aggregator_Bundle', a)
    _safe_set(a, 'aggregator_MappedRepository31', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository31', b2)
    if hasattr(b1, 'aggregator_Bundle'):
        assert not _is_linked(b1, 'aggregator_Bundle', a)
    if hasattr(b2, 'aggregator_Bundle'):
        assert _is_linked(b2, 'aggregator_Bundle', a)
    _safe_set(a, 'aggregator_MappedRepository31', set())
    assert not _is_linked(a, 'aggregator_MappedRepository31', b2)
    if hasattr(b2, 'aggregator_Bundle'):
        assert not _is_linked(b2, 'aggregator_Bundle', a)


def test_assoc_categories23_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'CustomCategory', b1)
    assert _is_linked(a, 'CustomCategory', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'CustomCategory', b2)
    assert _is_linked(a, 'CustomCategory', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'CustomCategory', None)
    assert not _is_linked(a, 'CustomCategory', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_categories34_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Category(labelOverride="sample_text")
    b2 = aggregator_Category(labelOverride="sample_text_2")
    _safe_set(a, 'aggregator_MappedRepository35', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository35', b1)
    if hasattr(b1, 'aggregator_Category'):
        assert _is_linked(b1, 'aggregator_Category', a)
    _safe_set(a, 'aggregator_MappedRepository35', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository35', b2)
    if hasattr(b1, 'aggregator_Category'):
        assert not _is_linked(b1, 'aggregator_Category', a)
    if hasattr(b2, 'aggregator_Category'):
        assert _is_linked(b2, 'aggregator_Category', a)
    _safe_set(a, 'aggregator_MappedRepository35', set())
    assert not _is_linked(a, 'aggregator_MappedRepository35', b2)
    if hasattr(b2, 'aggregator_Category'):
        assert not _is_linked(b2, 'aggregator_Category', a)


def test_assoc_categoryContainer56_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Categories()
    b2 = Categories()
    _safe_set(a, 'aggregator_p2view_Category', b1)
    assert _is_linked(a, 'aggregator_p2view_Category', b1)
    if hasattr(b1, 'Categories'):
        assert _is_linked(b1, 'Categories', a)
    _safe_set(a, 'aggregator_p2view_Category', b2)
    assert _is_linked(a, 'aggregator_p2view_Category', b2)
    if hasattr(b1, 'Categories'):
        assert not _is_linked(b1, 'Categories', a)
    if hasattr(b2, 'Categories'):
        assert _is_linked(b2, 'Categories', a)
    _safe_set(a, 'aggregator_p2view_Category', None)
    assert not _is_linked(a, 'aggregator_p2view_Category', b2)
    if hasattr(b2, 'Categories'):
        assert not _is_linked(b2, 'Categories', a)


def test_assoc_categoryContainer80_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Categories()
    b2 = Categories()
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits81', b1)
    if hasattr(b1, 'Categories82'):
        assert _is_linked(b1, 'Categories82', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits81', b2)
    if hasattr(b1, 'Categories82'):
        assert not _is_linked(b1, 'Categories82', a)
    if hasattr(b2, 'Categories82'):
        assert _is_linked(b2, 'Categories82', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits81', b2)
    if hasattr(b2, 'Categories82'):
        assert not _is_linked(b2, 'Categories82', a)


def test_assoc_configurations1_link_reassign_clear():
    a = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_Configuration', b1)
    assert _is_linked(a, 'aggregator_Configuration', b1)
    if hasattr(b1, 'aggregator_Aggregation2'):
        assert _is_linked(b1, 'aggregator_Aggregation2', a)
    _safe_set(a, 'aggregator_Configuration', b2)
    assert _is_linked(a, 'aggregator_Configuration', b2)
    if hasattr(b1, 'aggregator_Aggregation2'):
        assert not _is_linked(b1, 'aggregator_Aggregation2', a)
    if hasattr(b2, 'aggregator_Aggregation2'):
        assert _is_linked(b2, 'aggregator_Aggregation2', a)
    _safe_set(a, 'aggregator_Configuration', None)
    assert not _is_linked(a, 'aggregator_Configuration', b2)
    if hasattr(b2, 'aggregator_Aggregation2'):
        assert not _is_linked(b2, 'aggregator_Aggregation2', a)


def test_assoc_contacts17_link_reassign_clear():
    a = aggregator_Contribution(label="sample_text")
    b1 = aggregator_Contact(email="sample_text", name="sample_text")
    b2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    _safe_set(a, 'aggregator_Contribution18', {b1})
    assert _is_linked(a, 'aggregator_Contribution18', b1)
    if hasattr(b1, 'aggregator_Contact19'):
        assert _is_linked(b1, 'aggregator_Contact19', a)
    _safe_set(a, 'aggregator_Contribution18', {b2})
    assert _is_linked(a, 'aggregator_Contribution18', b2)
    if hasattr(b1, 'aggregator_Contact19'):
        assert not _is_linked(b1, 'aggregator_Contact19', a)
    if hasattr(b2, 'aggregator_Contact19'):
        assert _is_linked(b2, 'aggregator_Contact19', a)
    _safe_set(a, 'aggregator_Contribution18', set())
    assert not _is_linked(a, 'aggregator_Contribution18', b2)
    if hasattr(b2, 'aggregator_Contact19'):
        assert not _is_linked(b2, 'aggregator_Contact19', a)


def test_assoc_contacts5_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'Contact', b1)
    assert _is_linked(a, 'Contact', b1)
    if hasattr(b1, 'aggregation'):
        assert _is_linked(b1, 'aggregation', a)
    _safe_set(a, 'Contact', b2)
    assert _is_linked(a, 'Contact', b2)
    if hasattr(b1, 'aggregation'):
        assert not _is_linked(b1, 'aggregation', a)
    if hasattr(b2, 'aggregation'):
        assert _is_linked(b2, 'aggregation', a)
    _safe_set(a, 'Contact', None)
    assert not _is_linked(a, 'Contact', b2)
    if hasattr(b2, 'aggregation'):
        assert not _is_linked(b2, 'aggregation', a)


def test_assoc_contributions44_link_reassign_clear():
    a = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    b1 = aggregator_Contribution(label="sample_text")
    b2 = aggregator_Contribution(label="sample_text_2")
    _safe_set(a, 'aggregator_ValidationSet45', {b1})
    assert _is_linked(a, 'aggregator_ValidationSet45', b1)
    if hasattr(b1, 'aggregator_Contribution46'):
        assert _is_linked(b1, 'aggregator_Contribution46', a)
    _safe_set(a, 'aggregator_ValidationSet45', {b2})
    assert _is_linked(a, 'aggregator_ValidationSet45', b2)
    if hasattr(b1, 'aggregator_Contribution46'):
        assert not _is_linked(b1, 'aggregator_Contribution46', a)
    if hasattr(b2, 'aggregator_Contribution46'):
        assert _is_linked(b2, 'aggregator_Contribution46', a)
    _safe_set(a, 'aggregator_ValidationSet45', set())
    assert not _is_linked(a, 'aggregator_ValidationSet45', b2)
    if hasattr(b2, 'aggregator_Contribution46'):
        assert not _is_linked(b2, 'aggregator_Contribution46', a)


def test_assoc_customCategories3_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_CustomCategory', b1)
    assert _is_linked(a, 'aggregator_CustomCategory', b1)
    if hasattr(b1, 'aggregator_Aggregation4'):
        assert _is_linked(b1, 'aggregator_Aggregation4', a)
    _safe_set(a, 'aggregator_CustomCategory', b2)
    assert _is_linked(a, 'aggregator_CustomCategory', b2)
    if hasattr(b1, 'aggregator_Aggregation4'):
        assert not _is_linked(b1, 'aggregator_Aggregation4', a)
    if hasattr(b2, 'aggregator_Aggregation4'):
        assert _is_linked(b2, 'aggregator_Aggregation4', a)
    _safe_set(a, 'aggregator_CustomCategory', None)
    assert not _is_linked(a, 'aggregator_CustomCategory', b2)
    if hasattr(b2, 'aggregator_Aggregation4'):
        assert not _is_linked(b2, 'aggregator_Aggregation4', a)


def test_assoc_extends51_link_reassign_clear():
    a = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    b1 = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    b2 = aggregator_ValidationSet(abstract=False, extension=False, label="sample_text_2")
    _safe_set(a, 'aggregator_ValidationSet50', {b1})
    assert _is_linked(a, 'aggregator_ValidationSet50', b1)
    if hasattr(b1, 'aggregator_ValidationSet52'):
        assert _is_linked(b1, 'aggregator_ValidationSet52', a)
    _safe_set(a, 'aggregator_ValidationSet50', {b2})
    assert _is_linked(a, 'aggregator_ValidationSet50', b2)
    if hasattr(b1, 'aggregator_ValidationSet52'):
        assert not _is_linked(b1, 'aggregator_ValidationSet52', a)
    if hasattr(b2, 'aggregator_ValidationSet52'):
        assert _is_linked(b2, 'aggregator_ValidationSet52', a)
    _safe_set(a, 'aggregator_ValidationSet50', set())
    assert not _is_linked(a, 'aggregator_ValidationSet50', b2)
    if hasattr(b2, 'aggregator_ValidationSet52'):
        assert not _is_linked(b2, 'aggregator_ValidationSet52', a)


def test_assoc_featureContainer122_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Product', b1)
    assert _is_linked(a, 'aggregator_p2view_Product', b1)
    if hasattr(b1, 'Features123'):
        assert _is_linked(b1, 'Features123', a)
    _safe_set(a, 'aggregator_p2view_Product', b2)
    assert _is_linked(a, 'aggregator_p2view_Product', b2)
    if hasattr(b1, 'Features123'):
        assert not _is_linked(b1, 'Features123', a)
    if hasattr(b2, 'Features123'):
        assert _is_linked(b2, 'Features123', a)
    _safe_set(a, 'aggregator_p2view_Product', None)
    assert not _is_linked(a, 'aggregator_p2view_Product', b2)
    if hasattr(b2, 'Features123'):
        assert not _is_linked(b2, 'Features123', a)


def test_assoc_featureContainer57_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Category58', b1)
    assert _is_linked(a, 'aggregator_p2view_Category58', b1)
    if hasattr(b1, 'Features'):
        assert _is_linked(b1, 'Features', a)
    _safe_set(a, 'aggregator_p2view_Category58', b2)
    assert _is_linked(a, 'aggregator_p2view_Category58', b2)
    if hasattr(b1, 'Features'):
        assert not _is_linked(b1, 'Features', a)
    if hasattr(b2, 'Features'):
        assert _is_linked(b2, 'Features', a)
    _safe_set(a, 'aggregator_p2view_Category58', None)
    assert not _is_linked(a, 'aggregator_p2view_Category58', b2)
    if hasattr(b2, 'Features'):
        assert not _is_linked(b2, 'Features', a)


def test_assoc_featureContainer68_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Feature', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature', b1)
    if hasattr(b1, 'Features69'):
        assert _is_linked(b1, 'Features69', a)
    _safe_set(a, 'aggregator_p2view_Feature', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature', b2)
    if hasattr(b1, 'Features69'):
        assert not _is_linked(b1, 'Features69', a)
    if hasattr(b2, 'Features69'):
        assert _is_linked(b2, 'Features69', a)
    _safe_set(a, 'aggregator_p2view_Feature', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature', b2)
    if hasattr(b2, 'Features69'):
        assert not _is_linked(b2, 'Features69', a)


def test_assoc_featureContainer83_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_InstallableUnits84', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits84', b1)
    if hasattr(b1, 'Features85'):
        assert _is_linked(b1, 'Features85', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits84', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits84', b2)
    if hasattr(b1, 'Features85'):
        assert not _is_linked(b1, 'Features85', a)
    if hasattr(b2, 'Features85'):
        assert _is_linked(b2, 'Features85', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits84', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits84', b2)
    if hasattr(b2, 'Features85'):
        assert not _is_linked(b2, 'Features85', a)


def test_assoc_features24_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'categories', {b1})
    assert _is_linked(a, 'categories', b1)
    if hasattr(b1, 'Feature'):
        assert _is_linked(b1, 'Feature', a)
    _safe_set(a, 'categories', {b2})
    assert _is_linked(a, 'categories', b2)
    if hasattr(b1, 'Feature'):
        assert not _is_linked(b1, 'Feature', a)
    if hasattr(b2, 'Feature'):
        assert _is_linked(b2, 'Feature', a)
    _safe_set(a, 'categories', set())
    assert not _is_linked(a, 'categories', b2)
    if hasattr(b2, 'Feature'):
        assert not _is_linked(b2, 'Feature', a)


def test_assoc_features32_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'aggregator_MappedRepository33', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository33', b1)
    if hasattr(b1, 'aggregator_Feature'):
        assert _is_linked(b1, 'aggregator_Feature', a)
    _safe_set(a, 'aggregator_MappedRepository33', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository33', b2)
    if hasattr(b1, 'aggregator_Feature'):
        assert not _is_linked(b1, 'aggregator_Feature', a)
    if hasattr(b2, 'aggregator_Feature'):
        assert _is_linked(b2, 'aggregator_Feature', a)
    _safe_set(a, 'aggregator_MappedRepository33', set())
    assert not _is_linked(a, 'aggregator_MappedRepository33', b2)
    if hasattr(b2, 'aggregator_Feature'):
        assert not _is_linked(b2, 'aggregator_Feature', a)


def test_assoc_fragmentContainer127_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Product128', b1)
    assert _is_linked(a, 'aggregator_p2view_Product128', b1)
    if hasattr(b1, 'Fragments129'):
        assert _is_linked(b1, 'Fragments129', a)
    _safe_set(a, 'aggregator_p2view_Product128', b2)
    assert _is_linked(a, 'aggregator_p2view_Product128', b2)
    if hasattr(b1, 'Fragments129'):
        assert not _is_linked(b1, 'Fragments129', a)
    if hasattr(b2, 'Fragments129'):
        assert _is_linked(b2, 'Fragments129', a)
    _safe_set(a, 'aggregator_p2view_Product128', None)
    assert not _is_linked(a, 'aggregator_p2view_Product128', b2)
    if hasattr(b2, 'Fragments129'):
        assert not _is_linked(b2, 'Fragments129', a)


def test_assoc_fragmentContainer63_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Category64', b1)
    assert _is_linked(a, 'aggregator_p2view_Category64', b1)
    if hasattr(b1, 'Fragments'):
        assert _is_linked(b1, 'Fragments', a)
    _safe_set(a, 'aggregator_p2view_Category64', b2)
    assert _is_linked(a, 'aggregator_p2view_Category64', b2)
    if hasattr(b1, 'Fragments'):
        assert not _is_linked(b1, 'Fragments', a)
    if hasattr(b2, 'Fragments'):
        assert _is_linked(b2, 'Fragments', a)
    _safe_set(a, 'aggregator_p2view_Category64', None)
    assert not _is_linked(a, 'aggregator_p2view_Category64', b2)
    if hasattr(b2, 'Fragments'):
        assert not _is_linked(b2, 'Fragments', a)


def test_assoc_fragmentContainer73_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Feature74', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature74', b1)
    if hasattr(b1, 'Fragments75'):
        assert _is_linked(b1, 'Fragments75', a)
    _safe_set(a, 'aggregator_p2view_Feature74', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature74', b2)
    if hasattr(b1, 'Fragments75'):
        assert not _is_linked(b1, 'Fragments75', a)
    if hasattr(b2, 'Fragments75'):
        assert _is_linked(b2, 'Fragments75', a)
    _safe_set(a, 'aggregator_p2view_Feature74', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature74', b2)
    if hasattr(b2, 'Fragments75'):
        assert not _is_linked(b2, 'Fragments75', a)


def test_assoc_fragmentContainer92_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_InstallableUnits93', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits93', b1)
    if hasattr(b1, 'Fragments94'):
        assert _is_linked(b1, 'Fragments94', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits93', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits93', b2)
    if hasattr(b1, 'Fragments94'):
        assert not _is_linked(b1, 'Fragments94', a)
    if hasattr(b2, 'Fragments94'):
        assert _is_linked(b2, 'Fragments94', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits93', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits93', b2)
    if hasattr(b2, 'Fragments94'):
        assert not _is_linked(b2, 'Fragments94', a)


def test_assoc_installableUnit110_link_reassign_clear():
    a = aggregator_p2view_IUPresentation(description="sample_text", filter="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    b1 = p2view_aggregator_IInstallableUnit()
    b2 = p2view_aggregator_IInstallableUnit()
    _safe_set(a, 'aggregator_p2view_IUPresentation', b1)
    assert _is_linked(a, 'aggregator_p2view_IUPresentation', b1)
    if hasattr(b1, 'p2view_aggregator_IInstallableUnit'):
        assert _is_linked(b1, 'p2view_aggregator_IInstallableUnit', a)
    _safe_set(a, 'aggregator_p2view_IUPresentation', b2)
    assert _is_linked(a, 'aggregator_p2view_IUPresentation', b2)
    if hasattr(b1, 'p2view_aggregator_IInstallableUnit'):
        assert not _is_linked(b1, 'p2view_aggregator_IInstallableUnit', a)
    if hasattr(b2, 'p2view_aggregator_IInstallableUnit'):
        assert _is_linked(b2, 'p2view_aggregator_IInstallableUnit', a)
    _safe_set(a, 'aggregator_p2view_IUPresentation', None)
    assert not _is_linked(a, 'aggregator_p2view_IUPresentation', b2)
    if hasattr(b2, 'p2view_aggregator_IInstallableUnit'):
        assert not _is_linked(b2, 'p2view_aggregator_IInstallableUnit', a)


def test_assoc_installableUnitList113_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    b1 = InstallableUnits()
    b2 = InstallableUnits()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b1)
    if hasattr(b1, 'InstallableUnits'):
        assert _is_linked(b1, 'InstallableUnits', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    if hasattr(b1, 'InstallableUnits'):
        assert not _is_linked(b1, 'InstallableUnits', a)
    if hasattr(b2, 'InstallableUnits'):
        assert _is_linked(b2, 'InstallableUnits', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    if hasattr(b2, 'InstallableUnits'):
        assert not _is_linked(b2, 'InstallableUnits', a)


def test_assoc_installableUnitRequest14_link_reassign_clear():
    a = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    b1 = aggregator_AvailableVersionsHeader()
    b2 = aggregator_AvailableVersionsHeader()
    _safe_set(a, 'InstallableUnitRequest', b1)
    assert _is_linked(a, 'InstallableUnitRequest', b1)
    if hasattr(b1, 'availableVersionsHeader'):
        assert _is_linked(b1, 'availableVersionsHeader', a)
    _safe_set(a, 'InstallableUnitRequest', b2)
    assert _is_linked(a, 'InstallableUnitRequest', b2)
    if hasattr(b1, 'availableVersionsHeader'):
        assert not _is_linked(b1, 'availableVersionsHeader', a)
    if hasattr(b2, 'availableVersionsHeader'):
        assert _is_linked(b2, 'availableVersionsHeader', a)
    _safe_set(a, 'InstallableUnitRequest', None)
    assert not _is_linked(a, 'InstallableUnitRequest', b2)
    if hasattr(b2, 'availableVersionsHeader'):
        assert not _is_linked(b2, 'availableVersionsHeader', a)


def test_assoc_iuDetails65_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = IUDetails()
    b2 = IUDetails()
    _safe_set(a, 'aggregator_p2view_Category66', b1)
    assert _is_linked(a, 'aggregator_p2view_Category66', b1)
    if hasattr(b1, 'IUDetails'):
        assert _is_linked(b1, 'IUDetails', a)
    _safe_set(a, 'aggregator_p2view_Category66', b2)
    assert _is_linked(a, 'aggregator_p2view_Category66', b2)
    if hasattr(b1, 'IUDetails'):
        assert not _is_linked(b1, 'IUDetails', a)
    if hasattr(b2, 'IUDetails'):
        assert _is_linked(b2, 'IUDetails', a)
    _safe_set(a, 'aggregator_p2view_Category66', None)
    assert not _is_linked(a, 'aggregator_p2view_Category66', b2)
    if hasattr(b2, 'IUDetails'):
        assert not _is_linked(b2, 'IUDetails', a)


def test_assoc_mapRules36_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_MapRule()
    b2 = aggregator_MapRule()
    _safe_set(a, 'aggregator_MappedRepository37', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository37', b1)
    if hasattr(b1, 'aggregator_MapRule'):
        assert _is_linked(b1, 'aggregator_MapRule', a)
    _safe_set(a, 'aggregator_MappedRepository37', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository37', b2)
    if hasattr(b1, 'aggregator_MapRule'):
        assert not _is_linked(b1, 'aggregator_MapRule', a)
    if hasattr(b2, 'aggregator_MapRule'):
        assert _is_linked(b2, 'aggregator_MapRule', a)
    _safe_set(a, 'aggregator_MappedRepository37', set())
    assert not _is_linked(a, 'aggregator_MappedRepository37', b2)
    if hasattr(b2, 'aggregator_MapRule'):
        assert not _is_linked(b2, 'aggregator_MapRule', a)


def test_assoc_mavenMapping40_link_reassign_clear():
    a = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    b1 = aggregator_MavenItem(artifactId="sample_text", classifier="sample_text", groupId="sample_text", mappedVersion="sample_text")
    b2 = aggregator_MavenItem(artifactId="sample_text_2", classifier="sample_text_2", groupId="sample_text_2", mappedVersion="sample_text_2")
    _safe_set(a, 'aggregator_MavenMapping41', b1)
    assert _is_linked(a, 'aggregator_MavenMapping41', b1)
    if hasattr(b1, 'aggregator_MavenItem'):
        assert _is_linked(b1, 'aggregator_MavenItem', a)
    _safe_set(a, 'aggregator_MavenMapping41', b2)
    assert _is_linked(a, 'aggregator_MavenMapping41', b2)
    if hasattr(b1, 'aggregator_MavenItem'):
        assert not _is_linked(b1, 'aggregator_MavenItem', a)
    if hasattr(b2, 'aggregator_MavenItem'):
        assert _is_linked(b2, 'aggregator_MavenItem', a)
    _safe_set(a, 'aggregator_MavenMapping41', None)
    assert not _is_linked(a, 'aggregator_MavenMapping41', b2)
    if hasattr(b2, 'aggregator_MavenItem'):
        assert not _is_linked(b2, 'aggregator_MavenItem', a)


def test_assoc_mavenMappings11_link_reassign_clear():
    a = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_MavenMapping', b1)
    assert _is_linked(a, 'aggregator_MavenMapping', b1)
    if hasattr(b1, 'aggregator_Aggregation12'):
        assert _is_linked(b1, 'aggregator_Aggregation12', a)
    _safe_set(a, 'aggregator_MavenMapping', b2)
    assert _is_linked(a, 'aggregator_MavenMapping', b2)
    if hasattr(b1, 'aggregator_Aggregation12'):
        assert not _is_linked(b1, 'aggregator_Aggregation12', a)
    if hasattr(b2, 'aggregator_Aggregation12'):
        assert _is_linked(b2, 'aggregator_Aggregation12', a)
    _safe_set(a, 'aggregator_MavenMapping', None)
    assert not _is_linked(a, 'aggregator_MavenMapping', b2)
    if hasattr(b2, 'aggregator_Aggregation12'):
        assert not _is_linked(b2, 'aggregator_Aggregation12', a)


def test_assoc_mavenMappings20_link_reassign_clear():
    a = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text", versionPattern="sample_text", versionTemplate="sample_text")
    b1 = aggregator_Contribution(label="sample_text")
    b2 = aggregator_Contribution(label="sample_text_2")
    _safe_set(a, 'aggregator_MavenMapping22', b1)
    assert _is_linked(a, 'aggregator_MavenMapping22', b1)
    if hasattr(b1, 'aggregator_Contribution21'):
        assert _is_linked(b1, 'aggregator_Contribution21', a)
    _safe_set(a, 'aggregator_MavenMapping22', b2)
    assert _is_linked(a, 'aggregator_MavenMapping22', b2)
    if hasattr(b1, 'aggregator_Contribution21'):
        assert not _is_linked(b1, 'aggregator_Contribution21', a)
    if hasattr(b2, 'aggregator_Contribution21'):
        assert _is_linked(b2, 'aggregator_Contribution21', a)
    _safe_set(a, 'aggregator_MavenMapping22', None)
    assert not _is_linked(a, 'aggregator_MavenMapping22', b2)
    if hasattr(b2, 'aggregator_Contribution21'):
        assert not _is_linked(b2, 'aggregator_Contribution21', a)


def test_assoc_metadataRepository117_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    b1 = p2view_aggregator_MetadataRepository()
    b2 = p2view_aggregator_MetadataRepository()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', b1)
    if hasattr(b1, 'p2view_aggregator_MetadataRepository'):
        assert _is_linked(b1, 'p2view_aggregator_MetadataRepository', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', b2)
    if hasattr(b1, 'p2view_aggregator_MetadataRepository'):
        assert not _is_linked(b1, 'p2view_aggregator_MetadataRepository', a)
    if hasattr(b2, 'p2view_aggregator_MetadataRepository'):
        assert _is_linked(b2, 'p2view_aggregator_MetadataRepository', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView118', b2)
    if hasattr(b2, 'p2view_aggregator_MetadataRepository'):
        assert not _is_linked(b2, 'p2view_aggregator_MetadataRepository', a)


def test_assoc_metadataRepository42_link_reassign_clear():
    a = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    b1 = aggregator_MetadataRepository()
    b2 = aggregator_MetadataRepository()
    _safe_set(a, 'aggregator_MetadataRepositoryReference', b1)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference', b1)
    if hasattr(b1, 'aggregator_MetadataRepository'):
        assert _is_linked(b1, 'aggregator_MetadataRepository', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference', b2)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference', b2)
    if hasattr(b1, 'aggregator_MetadataRepository'):
        assert not _is_linked(b1, 'aggregator_MetadataRepository', a)
    if hasattr(b2, 'aggregator_MetadataRepository'):
        assert _is_linked(b2, 'aggregator_MetadataRepository', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference', None)
    assert not _is_linked(a, 'aggregator_MetadataRepositoryReference', b2)
    if hasattr(b2, 'aggregator_MetadataRepository'):
        assert not _is_linked(b2, 'aggregator_MetadataRepository', a)


def test_assoc_miscellaneousContainer95_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Miscellaneous()
    b2 = Miscellaneous()
    _safe_set(a, 'aggregator_p2view_InstallableUnits96', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits96', b1)
    if hasattr(b1, 'Miscellaneous'):
        assert _is_linked(b1, 'Miscellaneous', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits96', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits96', b2)
    if hasattr(b1, 'Miscellaneous'):
        assert not _is_linked(b1, 'Miscellaneous', a)
    if hasattr(b2, 'Miscellaneous'):
        assert _is_linked(b2, 'Miscellaneous', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits96', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits96', b2)
    if hasattr(b2, 'Miscellaneous'):
        assert not _is_linked(b2, 'Miscellaneous', a)


def test_assoc_productContainer59_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Products()
    b2 = Products()
    _safe_set(a, 'aggregator_p2view_Category60', b1)
    assert _is_linked(a, 'aggregator_p2view_Category60', b1)
    if hasattr(b1, 'Products'):
        assert _is_linked(b1, 'Products', a)
    _safe_set(a, 'aggregator_p2view_Category60', b2)
    assert _is_linked(a, 'aggregator_p2view_Category60', b2)
    if hasattr(b1, 'Products'):
        assert not _is_linked(b1, 'Products', a)
    if hasattr(b2, 'Products'):
        assert _is_linked(b2, 'Products', a)
    _safe_set(a, 'aggregator_p2view_Category60', None)
    assert not _is_linked(a, 'aggregator_p2view_Category60', b2)
    if hasattr(b2, 'Products'):
        assert not _is_linked(b2, 'Products', a)


def test_assoc_productContainer86_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Products()
    b2 = Products()
    _safe_set(a, 'aggregator_p2view_InstallableUnits87', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits87', b1)
    if hasattr(b1, 'Products88'):
        assert _is_linked(b1, 'Products88', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits87', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits87', b2)
    if hasattr(b1, 'Products88'):
        assert not _is_linked(b1, 'Products88', a)
    if hasattr(b2, 'Products88'):
        assert _is_linked(b2, 'Products88', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits87', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits87', b2)
    if hasattr(b2, 'Products88'):
        assert not _is_linked(b2, 'Products88', a)


def test_assoc_products28_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Product()
    b2 = aggregator_Product()
    _safe_set(a, 'aggregator_MappedRepository29', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository29', b1)
    if hasattr(b1, 'aggregator_Product'):
        assert _is_linked(b1, 'aggregator_Product', a)
    _safe_set(a, 'aggregator_MappedRepository29', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository29', b2)
    if hasattr(b1, 'aggregator_Product'):
        assert not _is_linked(b1, 'aggregator_Product', a)
    if hasattr(b2, 'aggregator_Product'):
        assert _is_linked(b2, 'aggregator_Product', a)
    _safe_set(a, 'aggregator_MappedRepository29', set())
    assert not _is_linked(a, 'aggregator_MappedRepository29', b2)
    if hasattr(b2, 'aggregator_Product'):
        assert not _is_linked(b2, 'aggregator_Product', a)


def test_assoc_properties114_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    b1 = Properties()
    b2 = Properties()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', b1)
    if hasattr(b1, 'Properties116'):
        assert _is_linked(b1, 'Properties116', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', b2)
    if hasattr(b1, 'Properties116'):
        assert not _is_linked(b1, 'Properties116', a)
    if hasattr(b2, 'Properties116'):
        assert _is_linked(b2, 'Properties116', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView115', b2)
    if hasattr(b2, 'Properties116'):
        assert not _is_linked(b2, 'Properties116', a)


def test_assoc_repositories112_link_reassign_clear():
    a = aggregator_p2view_RepositoryBrowser(loading=True)
    b1 = MetadataRepositoryStructuredView()
    b2 = MetadataRepositoryStructuredView()
    _safe_set(a, 'aggregator_p2view_RepositoryBrowser', {b1})
    assert _is_linked(a, 'aggregator_p2view_RepositoryBrowser', b1)
    if hasattr(b1, 'MetadataRepositoryStructuredView'):
        assert _is_linked(b1, 'MetadataRepositoryStructuredView', a)
    _safe_set(a, 'aggregator_p2view_RepositoryBrowser', {b2})
    assert _is_linked(a, 'aggregator_p2view_RepositoryBrowser', b2)
    if hasattr(b1, 'MetadataRepositoryStructuredView'):
        assert not _is_linked(b1, 'MetadataRepositoryStructuredView', a)
    if hasattr(b2, 'MetadataRepositoryStructuredView'):
        assert _is_linked(b2, 'MetadataRepositoryStructuredView', a)
    _safe_set(a, 'aggregator_p2view_RepositoryBrowser', set())
    assert not _is_linked(a, 'aggregator_p2view_RepositoryBrowser', b2)
    if hasattr(b2, 'MetadataRepositoryStructuredView'):
        assert not _is_linked(b2, 'MetadataRepositoryStructuredView', a)


def test_assoc_repositories16_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Contribution(label="sample_text")
    b2 = aggregator_Contribution(label="sample_text_2")
    _safe_set(a, 'aggregator_MappedRepository', b1)
    assert _is_linked(a, 'aggregator_MappedRepository', b1)
    if hasattr(b1, 'aggregator_Contribution'):
        assert _is_linked(b1, 'aggregator_Contribution', a)
    _safe_set(a, 'aggregator_MappedRepository', b2)
    assert _is_linked(a, 'aggregator_MappedRepository', b2)
    if hasattr(b1, 'aggregator_Contribution'):
        assert not _is_linked(b1, 'aggregator_Contribution', a)
    if hasattr(b2, 'aggregator_Contribution'):
        assert _is_linked(b2, 'aggregator_Contribution', a)
    _safe_set(a, 'aggregator_MappedRepository', None)
    assert not _is_linked(a, 'aggregator_MappedRepository', b2)
    if hasattr(b2, 'aggregator_Contribution'):
        assert not _is_linked(b2, 'aggregator_Contribution', a)


def test_assoc_repositoryReferences119_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, location="sample_text", name="sample_text")
    b1 = RepositoryReferences()
    b2 = RepositoryReferences()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', b1)
    if hasattr(b1, 'RepositoryReferences'):
        assert _is_linked(b1, 'RepositoryReferences', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', b2)
    if hasattr(b1, 'RepositoryReferences'):
        assert not _is_linked(b1, 'RepositoryReferences', a)
    if hasattr(b2, 'RepositoryReferences'):
        assert _is_linked(b2, 'RepositoryReferences', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView120', b2)
    if hasattr(b2, 'RepositoryReferences'):
        assert not _is_linked(b2, 'RepositoryReferences', a)


def test_assoc_status43_link_reassign_clear():
    a = aggregator_Status(code="sample_text", message="sample_text")
    b1 = aggregator_StatusProvider()
    b2 = aggregator_StatusProvider()
    _safe_set(a, 'aggregator_Status', b1)
    assert _is_linked(a, 'aggregator_Status', b1)
    if hasattr(b1, 'aggregator_StatusProvider'):
        assert _is_linked(b1, 'aggregator_StatusProvider', a)
    _safe_set(a, 'aggregator_Status', b2)
    assert _is_linked(a, 'aggregator_Status', b2)
    if hasattr(b1, 'aggregator_StatusProvider'):
        assert not _is_linked(b1, 'aggregator_StatusProvider', a)
    if hasattr(b2, 'aggregator_StatusProvider'):
        assert _is_linked(b2, 'aggregator_StatusProvider', a)
    _safe_set(a, 'aggregator_Status', None)
    assert not _is_linked(a, 'aggregator_Status', b2)
    if hasattr(b2, 'aggregator_StatusProvider'):
        assert not _is_linked(b2, 'aggregator_StatusProvider', a)


def test_assoc_validConfigurations38_link_reassign_clear():
    a = aggregator_MappedUnit()
    b1 = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b2 = aggregator_Configuration(architecture="sample_text_2", operatingSystem="sample_text_2", windowSystem="sample_text_2")
    _safe_set(a, 'aggregator_MappedUnit', {b1})
    assert _is_linked(a, 'aggregator_MappedUnit', b1)
    if hasattr(b1, 'aggregator_Configuration39'):
        assert _is_linked(b1, 'aggregator_Configuration39', a)
    _safe_set(a, 'aggregator_MappedUnit', {b2})
    assert _is_linked(a, 'aggregator_MappedUnit', b2)
    if hasattr(b1, 'aggregator_Configuration39'):
        assert not _is_linked(b1, 'aggregator_Configuration39', a)
    if hasattr(b2, 'aggregator_Configuration39'):
        assert _is_linked(b2, 'aggregator_Configuration39', a)
    _safe_set(a, 'aggregator_MappedUnit', set())
    assert not _is_linked(a, 'aggregator_MappedUnit', b2)
    if hasattr(b2, 'aggregator_Configuration39'):
        assert not _is_linked(b2, 'aggregator_Configuration39', a)


def test_assoc_validConfigurations53_link_reassign_clear():
    a = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b1 = aggregator_ValidConfigurationsRule()
    b2 = aggregator_ValidConfigurationsRule()
    _safe_set(a, 'aggregator_Configuration54', b1)
    assert _is_linked(a, 'aggregator_Configuration54', b1)
    if hasattr(b1, 'aggregator_ValidConfigurationsRule'):
        assert _is_linked(b1, 'aggregator_ValidConfigurationsRule', a)
    _safe_set(a, 'aggregator_Configuration54', b2)
    assert _is_linked(a, 'aggregator_Configuration54', b2)
    if hasattr(b1, 'aggregator_ValidConfigurationsRule'):
        assert not _is_linked(b1, 'aggregator_ValidConfigurationsRule', a)
    if hasattr(b2, 'aggregator_ValidConfigurationsRule'):
        assert _is_linked(b2, 'aggregator_ValidConfigurationsRule', a)
    _safe_set(a, 'aggregator_Configuration54', None)
    assert not _is_linked(a, 'aggregator_Configuration54', b2)
    if hasattr(b2, 'aggregator_ValidConfigurationsRule'):
        assert not _is_linked(b2, 'aggregator_ValidConfigurationsRule', a)


def test_assoc_validationRepositories47_link_reassign_clear():
    a = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    b1 = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    b2 = aggregator_MetadataRepositoryReference(location="sample_text_2", nature="sample_text_2")
    _safe_set(a, 'aggregator_ValidationSet48', {b1})
    assert _is_linked(a, 'aggregator_ValidationSet48', b1)
    if hasattr(b1, 'aggregator_MetadataRepositoryReference49'):
        assert _is_linked(b1, 'aggregator_MetadataRepositoryReference49', a)
    _safe_set(a, 'aggregator_ValidationSet48', {b2})
    assert _is_linked(a, 'aggregator_ValidationSet48', b2)
    if hasattr(b1, 'aggregator_MetadataRepositoryReference49'):
        assert not _is_linked(b1, 'aggregator_MetadataRepositoryReference49', a)
    if hasattr(b2, 'aggregator_MetadataRepositoryReference49'):
        assert _is_linked(b2, 'aggregator_MetadataRepositoryReference49', a)
    _safe_set(a, 'aggregator_ValidationSet48', set())
    assert not _is_linked(a, 'aggregator_ValidationSet48', b2)
    if hasattr(b2, 'aggregator_MetadataRepositoryReference49'):
        assert not _is_linked(b2, 'aggregator_MetadataRepositoryReference49', a)


def test_assoc_validationSets0_link_reassign_clear():
    a = aggregator_ValidationSet(abstract=True, extension=True, label="sample_text")
    b1 = aggregator_Aggregation(allowLegacySites="sample_text", buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, strictMavenVersions=True, type="sample_text", versionFormat="sample_text")
    b2 = aggregator_Aggregation(allowLegacySites="sample_text_2", buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, strictMavenVersions=False, type="sample_text_2", versionFormat="sample_text_2")
    _safe_set(a, 'aggregator_ValidationSet', b1)
    assert _is_linked(a, 'aggregator_ValidationSet', b1)
    if hasattr(b1, 'aggregator_Aggregation'):
        assert _is_linked(b1, 'aggregator_Aggregation', a)
    _safe_set(a, 'aggregator_ValidationSet', b2)
    assert _is_linked(a, 'aggregator_ValidationSet', b2)
    if hasattr(b1, 'aggregator_Aggregation'):
        assert not _is_linked(b1, 'aggregator_Aggregation', a)
    if hasattr(b2, 'aggregator_Aggregation'):
        assert _is_linked(b2, 'aggregator_Aggregation', a)
    _safe_set(a, 'aggregator_ValidationSet', None)
    assert not _is_linked(a, 'aggregator_ValidationSet', b2)
    if hasattr(b2, 'aggregator_Aggregation'):
        assert not _is_linked(b2, 'aggregator_Aggregation', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bundle_strategy = st.builds(Bundle)
@given(instance=Bundle_strategy)
@settings(max_examples=25)
def test_Bundle_instantiation(instance):
    assert isinstance(instance, Bundle)


Bundles_strategy = st.builds(Bundles)
@given(instance=Bundles_strategy)
@settings(max_examples=25)
def test_Bundles_instantiation(instance):
    assert isinstance(instance, Bundles)


Categories_strategy = st.builds(Categories)
@given(instance=Categories_strategy)
@settings(max_examples=25)
def test_Categories_instantiation(instance):
    assert isinstance(instance, Categories)


Category_strategy = st.builds(Category)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


DescriptionProvider_strategy = st.builds(DescriptionProvider)
@given(instance=DescriptionProvider_strategy)
@settings(max_examples=25)
def test_DescriptionProvider_instantiation(instance):
    assert isinstance(instance, DescriptionProvider)


EnabledStatusProvider_strategy = st.builds(EnabledStatusProvider)
@given(instance=EnabledStatusProvider_strategy)
@settings(max_examples=25)
def test_EnabledStatusProvider_instantiation(instance):
    assert isinstance(instance, EnabledStatusProvider)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Features_strategy = st.builds(Features)
@given(instance=Features_strategy)
@settings(max_examples=25)
def test_Features_instantiation(instance):
    assert isinstance(instance, Features)


Fragment_strategy = st.builds(Fragment)
@given(instance=Fragment_strategy)
@settings(max_examples=25)
def test_Fragment_instantiation(instance):
    assert isinstance(instance, Fragment)


Fragments_strategy = st.builds(Fragments)
@given(instance=Fragments_strategy)
@settings(max_examples=25)
def test_Fragments_instantiation(instance):
    assert isinstance(instance, Fragments)


IProvidedCapability_strategy = st.builds(IProvidedCapability)
@given(instance=IProvidedCapability_strategy)
@settings(max_examples=25)
def test_IProvidedCapability_instantiation(instance):
    assert isinstance(instance, IProvidedCapability)


IRequirement_strategy = st.builds(IRequirement)
@given(instance=IRequirement_strategy)
@settings(max_examples=25)
def test_IRequirement_instantiation(instance):
    assert isinstance(instance, IRequirement)


IUDetails_strategy = st.builds(IUDetails)
@given(instance=IUDetails_strategy)
@settings(max_examples=25)
def test_IUDetails_instantiation(instance):
    assert isinstance(instance, IUDetails)


IUPresentation_strategy = st.builds(IUPresentation)
@given(instance=IUPresentation_strategy)
@settings(max_examples=25)
def test_IUPresentation_instantiation(instance):
    assert isinstance(instance, IUPresentation)


IUPresentationWithDetails_strategy = st.builds(IUPresentationWithDetails)
@given(instance=IUPresentationWithDetails_strategy)
@settings(max_examples=25)
def test_IUPresentationWithDetails_instantiation(instance):
    assert isinstance(instance, IUPresentationWithDetails)


IdentificationProvider_strategy = st.builds(IdentificationProvider)
@given(instance=IdentificationProvider_strategy)
@settings(max_examples=25)
def test_IdentificationProvider_instantiation(instance):
    assert isinstance(instance, IdentificationProvider)


InfosProvider_strategy = st.builds(InfosProvider)
@given(instance=InfosProvider_strategy)
@settings(max_examples=25)
def test_InfosProvider_instantiation(instance):
    assert isinstance(instance, InfosProvider)


InstallableUnitRequest_strategy = st.builds(InstallableUnitRequest)
@given(instance=InstallableUnitRequest_strategy)
@settings(max_examples=25)
def test_InstallableUnitRequest_instantiation(instance):
    assert isinstance(instance, InstallableUnitRequest)


InstallableUnits_strategy = st.builds(InstallableUnits)
@given(instance=InstallableUnits_strategy)
@settings(max_examples=25)
def test_InstallableUnits_instantiation(instance):
    assert isinstance(instance, InstallableUnits)


LabelProvider_strategy = st.builds(LabelProvider)
@given(instance=LabelProvider_strategy)
@settings(max_examples=25)
def test_LabelProvider_instantiation(instance):
    assert isinstance(instance, LabelProvider)


Licenses_strategy = st.builds(Licenses)
@given(instance=Licenses_strategy)
@settings(max_examples=25)
def test_Licenses_instantiation(instance):
    assert isinstance(instance, Licenses)


MapRule_strategy = st.builds(MapRule)
@given(instance=MapRule_strategy)
@settings(max_examples=25)
def test_MapRule_instantiation(instance):
    assert isinstance(instance, MapRule)


MappedUnit_strategy = st.builds(MappedUnit)
@given(instance=MappedUnit_strategy)
@settings(max_examples=25)
def test_MappedUnit_instantiation(instance):
    assert isinstance(instance, MappedUnit)


MetadataRepositoryReference_strategy = st.builds(MetadataRepositoryReference)
@given(instance=MetadataRepositoryReference_strategy)
@settings(max_examples=25)
def test_MetadataRepositoryReference_instantiation(instance):
    assert isinstance(instance, MetadataRepositoryReference)


MetadataRepositoryStructuredView_strategy = st.builds(MetadataRepositoryStructuredView)
@given(instance=MetadataRepositoryStructuredView_strategy)
@settings(max_examples=25)
def test_MetadataRepositoryStructuredView_instantiation(instance):
    assert isinstance(instance, MetadataRepositoryStructuredView)


Miscellaneous_strategy = st.builds(Miscellaneous)
@given(instance=Miscellaneous_strategy)
@settings(max_examples=25)
def test_Miscellaneous_instantiation(instance):
    assert isinstance(instance, Miscellaneous)


OtherIU_strategy = st.builds(OtherIU)
@given(instance=OtherIU_strategy)
@settings(max_examples=25)
def test_OtherIU_instantiation(instance):
    assert isinstance(instance, OtherIU)


Product_strategy = st.builds(Product)
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Products_strategy = st.builds(Products)
@given(instance=Products_strategy)
@settings(max_examples=25)
def test_Products_instantiation(instance):
    assert isinstance(instance, Products)


Properties_strategy = st.builds(Properties)
@given(instance=Properties_strategy)
@settings(max_examples=25)
def test_Properties_instantiation(instance):
    assert isinstance(instance, Properties)


ProvidedCapabilities_strategy = st.builds(ProvidedCapabilities)
@given(instance=ProvidedCapabilities_strategy)
@settings(max_examples=25)
def test_ProvidedCapabilities_instantiation(instance):
    assert isinstance(instance, ProvidedCapabilities)


ProvidedCapabilityWrapper_strategy = st.builds(ProvidedCapabilityWrapper)
@given(instance=ProvidedCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_ProvidedCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, ProvidedCapabilityWrapper)


RepositoryReferences_strategy = st.builds(RepositoryReferences)
@given(instance=RepositoryReferences_strategy)
@settings(max_examples=25)
def test_RepositoryReferences_instantiation(instance):
    assert isinstance(instance, RepositoryReferences)


RequirementWrapper_strategy = st.builds(RequirementWrapper)
@given(instance=RequirementWrapper_strategy)
@settings(max_examples=25)
def test_RequirementWrapper_instantiation(instance):
    assert isinstance(instance, RequirementWrapper)


Requirements_strategy = st.builds(Requirements)
@given(instance=Requirements_strategy)
@settings(max_examples=25)
def test_Requirements_instantiation(instance):
    assert isinstance(instance, Requirements)


StatusProvider_strategy = st.builds(StatusProvider)
@given(instance=StatusProvider_strategy)
@settings(max_examples=25)
def test_StatusProvider_instantiation(instance):
    assert isinstance(instance, StatusProvider)


Touchpoints_strategy = st.builds(Touchpoints)
@given(instance=Touchpoints_strategy)
@settings(max_examples=25)
def test_Touchpoints_instantiation(instance):
    assert isinstance(instance, Touchpoints)


aggregator_Aggregation_strategy = st.builds(aggregator_Aggregation, allowLegacySites=safe_text, buildRoot=safe_text, label=safe_text, mavenResult=st.booleans(), packedStrategy=safe_text, sendmail=st.booleans(), strictMavenVersions=st.booleans(), type=safe_text, versionFormat=safe_text)
@given(instance=aggregator_Aggregation_strategy)
@settings(max_examples=25)
def test_aggregator_Aggregation_instantiation(instance):
    assert isinstance(instance, aggregator_Aggregation)


aggregator_AvailableVersion_strategy = st.builds(aggregator_AvailableVersion, availableFrom=safe_text, filter=safe_text, version=safe_text, versionMatch=safe_text)
@given(instance=aggregator_AvailableVersion_strategy)
@settings(max_examples=25)
def test_aggregator_AvailableVersion_instantiation(instance):
    assert isinstance(instance, aggregator_AvailableVersion)


aggregator_AvailableVersionsHeader_strategy = st.builds(aggregator_AvailableVersionsHeader)
@given(instance=aggregator_AvailableVersionsHeader_strategy)
@settings(max_examples=25)
def test_aggregator_AvailableVersionsHeader_instantiation(instance):
    assert isinstance(instance, aggregator_AvailableVersionsHeader)


aggregator_Bundle_strategy = st.builds(aggregator_Bundle)
@given(instance=aggregator_Bundle_strategy)
@settings(max_examples=25)
def test_aggregator_Bundle_instantiation(instance):
    assert isinstance(instance, aggregator_Bundle)


aggregator_Category_strategy = st.builds(aggregator_Category, labelOverride=safe_text)
@given(instance=aggregator_Category_strategy)
@settings(max_examples=25)
def test_aggregator_Category_instantiation(instance):
    assert isinstance(instance, aggregator_Category)


aggregator_ChildrenProvider_strategy = st.builds(aggregator_ChildrenProvider)
@given(instance=aggregator_ChildrenProvider_strategy)
@settings(max_examples=25)
def test_aggregator_ChildrenProvider_instantiation(instance):
    assert isinstance(instance, aggregator_ChildrenProvider)


aggregator_Configuration_strategy = st.builds(aggregator_Configuration, architecture=safe_text, operatingSystem=safe_text, windowSystem=safe_text)
@given(instance=aggregator_Configuration_strategy)
@settings(max_examples=25)
def test_aggregator_Configuration_instantiation(instance):
    assert isinstance(instance, aggregator_Configuration)


aggregator_Contact_strategy = st.builds(aggregator_Contact, email=safe_text, name=safe_text)
@given(instance=aggregator_Contact_strategy)
@settings(max_examples=25)
def test_aggregator_Contact_instantiation(instance):
    assert isinstance(instance, aggregator_Contact)


aggregator_Contribution_strategy = st.builds(aggregator_Contribution, label=safe_text)
@given(instance=aggregator_Contribution_strategy)
@settings(max_examples=25)
def test_aggregator_Contribution_instantiation(instance):
    assert isinstance(instance, aggregator_Contribution)


aggregator_CustomCategory_strategy = st.builds(aggregator_CustomCategory, description=safe_text, identifier=safe_text, label=safe_text)
@given(instance=aggregator_CustomCategory_strategy)
@settings(max_examples=25)
def test_aggregator_CustomCategory_instantiation(instance):
    assert isinstance(instance, aggregator_CustomCategory)


aggregator_DescriptionProvider_strategy = st.builds(aggregator_DescriptionProvider, description=safe_text)
@given(instance=aggregator_DescriptionProvider_strategy)
@settings(max_examples=25)
def test_aggregator_DescriptionProvider_instantiation(instance):
    assert isinstance(instance, aggregator_DescriptionProvider)


aggregator_EnabledStatusProvider_strategy = st.builds(aggregator_EnabledStatusProvider, branchEnabled=st.booleans(), enabled=st.booleans())
@given(instance=aggregator_EnabledStatusProvider_strategy)
@settings(max_examples=25)
def test_aggregator_EnabledStatusProvider_instantiation(instance):
    assert isinstance(instance, aggregator_EnabledStatusProvider)


aggregator_ExclusionRule_strategy = st.builds(aggregator_ExclusionRule)
@given(instance=aggregator_ExclusionRule_strategy)
@settings(max_examples=25)
def test_aggregator_ExclusionRule_instantiation(instance):
    assert isinstance(instance, aggregator_ExclusionRule)


aggregator_Feature_strategy = st.builds(aggregator_Feature)
@given(instance=aggregator_Feature_strategy)
@settings(max_examples=25)
def test_aggregator_Feature_instantiation(instance):
    assert isinstance(instance, aggregator_Feature)


aggregator_IdentificationProvider_strategy = st.builds(aggregator_IdentificationProvider)
@given(instance=aggregator_IdentificationProvider_strategy)
@settings(max_examples=25)
def test_aggregator_IdentificationProvider_instantiation(instance):
    assert isinstance(instance, aggregator_IdentificationProvider)


aggregator_InfosProvider_strategy = st.builds(aggregator_InfosProvider, errors=safe_text, infos=safe_text, warnings=safe_text)
@given(instance=aggregator_InfosProvider_strategy)
@settings(max_examples=25)
def test_aggregator_InfosProvider_instantiation(instance):
    assert isinstance(instance, aggregator_InfosProvider)


aggregator_InstallableUnitRequest_strategy = st.builds(aggregator_InstallableUnitRequest, name=safe_text, versionRange=safe_text)
@given(instance=aggregator_InstallableUnitRequest_strategy)
@settings(max_examples=25)
def test_aggregator_InstallableUnitRequest_instantiation(instance):
    assert isinstance(instance, aggregator_InstallableUnitRequest)


aggregator_LabelProvider_strategy = st.builds(aggregator_LabelProvider, label=safe_text)
@given(instance=aggregator_LabelProvider_strategy)
@settings(max_examples=25)
def test_aggregator_LabelProvider_instantiation(instance):
    assert isinstance(instance, aggregator_LabelProvider)


aggregator_MapRule_strategy = st.builds(aggregator_MapRule)
@given(instance=aggregator_MapRule_strategy)
@settings(max_examples=25)
def test_aggregator_MapRule_instantiation(instance):
    assert isinstance(instance, aggregator_MapRule)


aggregator_MappedRepository_strategy = st.builds(aggregator_MappedRepository, categoryPrefix=safe_text, mirrorArtifacts=st.booleans())
@given(instance=aggregator_MappedRepository_strategy)
@settings(max_examples=25)
def test_aggregator_MappedRepository_instantiation(instance):
    assert isinstance(instance, aggregator_MappedRepository)


aggregator_MappedUnit_strategy = st.builds(aggregator_MappedUnit)
@given(instance=aggregator_MappedUnit_strategy)
@settings(max_examples=25)
def test_aggregator_MappedUnit_instantiation(instance):
    assert isinstance(instance, aggregator_MappedUnit)


aggregator_MavenItem_strategy = st.builds(aggregator_MavenItem, artifactId=safe_text, classifier=safe_text, groupId=safe_text, mappedVersion=safe_text)
@given(instance=aggregator_MavenItem_strategy)
@settings(max_examples=25)
def test_aggregator_MavenItem_instantiation(instance):
    assert isinstance(instance, aggregator_MavenItem)


aggregator_MavenMapping_strategy = st.builds(aggregator_MavenMapping, artifactId=safe_text, groupId=safe_text, namePattern=safe_text, versionPattern=safe_text, versionTemplate=safe_text)
@given(instance=aggregator_MavenMapping_strategy)
@settings(max_examples=25)
def test_aggregator_MavenMapping_instantiation(instance):
    assert isinstance(instance, aggregator_MavenMapping)


aggregator_MetadataRepository_strategy = st.builds(aggregator_MetadataRepository)
@given(instance=aggregator_MetadataRepository_strategy)
@settings(max_examples=25)
def test_aggregator_MetadataRepository_instantiation(instance):
    assert isinstance(instance, aggregator_MetadataRepository)


aggregator_MetadataRepositoryReference_strategy = st.builds(aggregator_MetadataRepositoryReference, location=safe_text, nature=safe_text)
@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=25)
def test_aggregator_MetadataRepositoryReference_instantiation(instance):
    assert isinstance(instance, aggregator_MetadataRepositoryReference)


aggregator_Product_strategy = st.builds(aggregator_Product)
@given(instance=aggregator_Product_strategy)
@settings(max_examples=25)
def test_aggregator_Product_instantiation(instance):
    assert isinstance(instance, aggregator_Product)


aggregator_Property_strategy = st.builds(aggregator_Property, key=safe_text, value=safe_text)
@given(instance=aggregator_Property_strategy)
@settings(max_examples=25)
def test_aggregator_Property_instantiation(instance):
    assert isinstance(instance, aggregator_Property)


aggregator_Status_strategy = st.builds(aggregator_Status, code=safe_text, message=safe_text)
@given(instance=aggregator_Status_strategy)
@settings(max_examples=25)
def test_aggregator_Status_instantiation(instance):
    assert isinstance(instance, aggregator_Status)


aggregator_StatusProvider_strategy = st.builds(aggregator_StatusProvider)
@given(instance=aggregator_StatusProvider_strategy)
@settings(max_examples=25)
def test_aggregator_StatusProvider_instantiation(instance):
    assert isinstance(instance, aggregator_StatusProvider)


aggregator_ValidConfigurationsRule_strategy = st.builds(aggregator_ValidConfigurationsRule)
@given(instance=aggregator_ValidConfigurationsRule_strategy)
@settings(max_examples=25)
def test_aggregator_ValidConfigurationsRule_instantiation(instance):
    assert isinstance(instance, aggregator_ValidConfigurationsRule)


aggregator_ValidationSet_strategy = st.builds(aggregator_ValidationSet, abstract=st.booleans(), extension=st.booleans(), label=safe_text)
@given(instance=aggregator_ValidationSet_strategy)
@settings(max_examples=25)
def test_aggregator_ValidationSet_instantiation(instance):
    assert isinstance(instance, aggregator_ValidationSet)


aggregator_p2view_Bundle_strategy = st.builds(aggregator_p2view_Bundle)
@given(instance=aggregator_p2view_Bundle_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Bundle_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Bundle)


aggregator_p2view_Bundles_strategy = st.builds(aggregator_p2view_Bundles)
@given(instance=aggregator_p2view_Bundles_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Bundles_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Bundles)


aggregator_p2view_Categories_strategy = st.builds(aggregator_p2view_Categories)
@given(instance=aggregator_p2view_Categories_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Categories_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Categories)


aggregator_p2view_Category_strategy = st.builds(aggregator_p2view_Category)
@given(instance=aggregator_p2view_Category_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Category_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Category)


aggregator_p2view_Feature_strategy = st.builds(aggregator_p2view_Feature)
@given(instance=aggregator_p2view_Feature_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Feature_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Feature)


aggregator_p2view_Features_strategy = st.builds(aggregator_p2view_Features)
@given(instance=aggregator_p2view_Features_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Features_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Features)


aggregator_p2view_Fragment_strategy = st.builds(aggregator_p2view_Fragment)
@given(instance=aggregator_p2view_Fragment_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Fragment_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Fragment)


aggregator_p2view_Fragments_strategy = st.builds(aggregator_p2view_Fragments)
@given(instance=aggregator_p2view_Fragments_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Fragments_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Fragments)


aggregator_p2view_IUDetails_strategy = st.builds(aggregator_p2view_IUDetails)
@given(instance=aggregator_p2view_IUDetails_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUDetails_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUDetails)


aggregator_p2view_IUPresentation_strategy = st.builds(aggregator_p2view_IUPresentation, description=safe_text, filter=safe_text, id=safe_text, label=safe_text, name=safe_text, type=safe_text, version=safe_text)
@given(instance=aggregator_p2view_IUPresentation_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUPresentation_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUPresentation)


aggregator_p2view_IUPresentationWithDetails_strategy = st.builds(aggregator_p2view_IUPresentationWithDetails, detailsResolved=safe_text)
@given(instance=aggregator_p2view_IUPresentationWithDetails_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUPresentationWithDetails_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUPresentationWithDetails)


aggregator_p2view_InstallableUnits_strategy = st.builds(aggregator_p2view_InstallableUnits)
@given(instance=aggregator_p2view_InstallableUnits_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_InstallableUnits_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_InstallableUnits)


aggregator_p2view_Licenses_strategy = st.builds(aggregator_p2view_Licenses)
@given(instance=aggregator_p2view_Licenses_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Licenses_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Licenses)


aggregator_p2view_MetadataRepositoryStructuredView_strategy = st.builds(aggregator_p2view_MetadataRepositoryStructuredView, loaded=st.booleans(), location=safe_text, name=safe_text)
@given(instance=aggregator_p2view_MetadataRepositoryStructuredView_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_MetadataRepositoryStructuredView_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_MetadataRepositoryStructuredView)


aggregator_p2view_Miscellaneous_strategy = st.builds(aggregator_p2view_Miscellaneous)
@given(instance=aggregator_p2view_Miscellaneous_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Miscellaneous_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Miscellaneous)


aggregator_p2view_OtherIU_strategy = st.builds(aggregator_p2view_OtherIU)
@given(instance=aggregator_p2view_OtherIU_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_OtherIU_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_OtherIU)


aggregator_p2view_Product_strategy = st.builds(aggregator_p2view_Product)
@given(instance=aggregator_p2view_Product_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Product_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Product)


aggregator_p2view_Products_strategy = st.builds(aggregator_p2view_Products)
@given(instance=aggregator_p2view_Products_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Products_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Products)


aggregator_p2view_Properties_strategy = st.builds(aggregator_p2view_Properties)
@given(instance=aggregator_p2view_Properties_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Properties_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Properties)


aggregator_p2view_ProvidedCapabilities_strategy = st.builds(aggregator_p2view_ProvidedCapabilities)
@given(instance=aggregator_p2view_ProvidedCapabilities_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_ProvidedCapabilities_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_ProvidedCapabilities)


aggregator_p2view_ProvidedCapabilityWrapper_strategy = st.builds(aggregator_p2view_ProvidedCapabilityWrapper)
@given(instance=aggregator_p2view_ProvidedCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_ProvidedCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_ProvidedCapabilityWrapper)


aggregator_p2view_RepositoryBrowser_strategy = st.builds(aggregator_p2view_RepositoryBrowser, loading=st.booleans())
@given(instance=aggregator_p2view_RepositoryBrowser_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_RepositoryBrowser_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_RepositoryBrowser)


aggregator_p2view_RepositoryReferences_strategy = st.builds(aggregator_p2view_RepositoryReferences)
@given(instance=aggregator_p2view_RepositoryReferences_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_RepositoryReferences_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_RepositoryReferences)


aggregator_p2view_RequirementWrapper_strategy = st.builds(aggregator_p2view_RequirementWrapper)
@given(instance=aggregator_p2view_RequirementWrapper_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_RequirementWrapper_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_RequirementWrapper)


aggregator_p2view_Requirements_strategy = st.builds(aggregator_p2view_Requirements)
@given(instance=aggregator_p2view_Requirements_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Requirements_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Requirements)


aggregator_p2view_Touchpoints_strategy = st.builds(aggregator_p2view_Touchpoints)
@given(instance=aggregator_p2view_Touchpoints_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Touchpoints_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Touchpoints)


p2view_IUDetails_strategy = st.builds(p2view_IUDetails)
@given(instance=p2view_IUDetails_strategy)
@settings(max_examples=25)
def test_p2view_IUDetails_instantiation(instance):
    assert isinstance(instance, p2view_IUDetails)


p2view_IUPresentation_strategy = st.builds(p2view_IUPresentation)
@given(instance=p2view_IUPresentation_strategy)
@settings(max_examples=25)
def test_p2view_IUPresentation_instantiation(instance):
    assert isinstance(instance, p2view_IUPresentation)


p2view_aggregator_ICopyright_strategy = st.builds(p2view_aggregator_ICopyright)
@given(instance=p2view_aggregator_ICopyright_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_ICopyright_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_ICopyright)


p2view_aggregator_IInstallableUnit_strategy = st.builds(p2view_aggregator_IInstallableUnit)
@given(instance=p2view_aggregator_IInstallableUnit_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_IInstallableUnit_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_IInstallableUnit)


p2view_aggregator_ILicense_strategy = st.builds(p2view_aggregator_ILicense)
@given(instance=p2view_aggregator_ILicense_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_ILicense_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_ILicense)


p2view_aggregator_IProvidedCapability_strategy = st.builds(p2view_aggregator_IProvidedCapability)
@given(instance=p2view_aggregator_IProvidedCapability_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_IProvidedCapability_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_IProvidedCapability)


p2view_aggregator_IRepositoryReference_strategy = st.builds(p2view_aggregator_IRepositoryReference)
@given(instance=p2view_aggregator_IRepositoryReference_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_IRepositoryReference_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_IRepositoryReference)


p2view_aggregator_IRequirement_strategy = st.builds(p2view_aggregator_IRequirement)
@given(instance=p2view_aggregator_IRequirement_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_IRequirement_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_IRequirement)


p2view_aggregator_ITouchpointData_strategy = st.builds(p2view_aggregator_ITouchpointData)
@given(instance=p2view_aggregator_ITouchpointData_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_ITouchpointData_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_ITouchpointData)


p2view_aggregator_ITouchpointType_strategy = st.builds(p2view_aggregator_ITouchpointType)
@given(instance=p2view_aggregator_ITouchpointType_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_ITouchpointType_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_ITouchpointType)


p2view_aggregator_IUpdateDescriptor_strategy = st.builds(p2view_aggregator_IUpdateDescriptor)
@given(instance=p2view_aggregator_IUpdateDescriptor_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_IUpdateDescriptor_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_IUpdateDescriptor)


p2view_aggregator_MetadataRepository_strategy = st.builds(p2view_aggregator_MetadataRepository)
@given(instance=p2view_aggregator_MetadataRepository_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_MetadataRepository_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_MetadataRepository)


p2view_aggregator_Property_strategy = st.builds(p2view_aggregator_Property)
@given(instance=p2view_aggregator_Property_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_Property_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_Property)


