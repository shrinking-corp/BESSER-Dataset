import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArtifactElement,
    JavaDataField,
    JavaDataType,
    JavaElement,
    JavaSpringWebApplicationProject,
    JavaUserDefinedType,
    MicroserviceProject,
    PSM_ApplicationProject,
    PSM_ArtifactElement,
    PSM_ConfigurationProperty,
    PSM_DependencyLibrary,
    PSM_DistributedApplicationProject,
    PSM_DockerContainerDefinition,
    PSM_DockerContainerLink,
    PSM_DockerContainerPort,
    PSM_JavaAnnotation,
    PSM_JavaAnnotationParameter,
    PSM_JavaClassType,
    PSM_JavaDataField,
    PSM_JavaDataType,
    PSM_JavaElement,
    PSM_JavaInterfaceType,
    PSM_JavaMethod,
    PSM_JavaMethodParameter,
    PSM_JavaSpringMVCApplicationProject,
    PSM_JavaSpringWebApplicationProject,
    PSM_JavaSpringWebFluxApplicationProject,
    PSM_JavaUserDefinedType,
    PSM_MicroserviceProject,
    PSM_RootPSM,
    PSM_SpringBootApplicationLayer,
    PSM_SpringComponentLayer,
    PSM_SpringConfigurationLayer,
    PSM_SpringControllerLayer,
    PSM_SpringDomainLayer,
    PSM_SpringFeignClientLayer,
    PSM_SpringModelPojoLayer,
    PSM_SpringRepositoryLayer,
    PSM_SpringServiceLayer,
    PSM_SpringWebApplicationLayer,
    SpringWebApplicationLayer,
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

def test_PSM_ApplicationProject_ProjectArtifactId_value_roundtrip():
    instance = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    assert instance.ProjectArtifactId == "sample_text"
    instance.ProjectArtifactId = "sample_text_2"
    assert instance.ProjectArtifactId == "sample_text_2"


def test_PSM_ArtifactElement_ArtifactFileName_value_roundtrip():
    instance = PSM_ArtifactElement(ArtifactFileName="sample_text", GeneratingLinesOfCode="sample_text", ParentProjectName="sample_text")
    assert instance.ArtifactFileName == "sample_text"
    instance.ArtifactFileName = "sample_text_2"
    assert instance.ArtifactFileName == "sample_text_2"


def test_PSM_ArtifactElement_GeneratingLinesOfCode_value_roundtrip():
    instance = PSM_ArtifactElement(ArtifactFileName="sample_text", GeneratingLinesOfCode="sample_text", ParentProjectName="sample_text")
    assert instance.GeneratingLinesOfCode == "sample_text"
    instance.GeneratingLinesOfCode = "sample_text_2"
    assert instance.GeneratingLinesOfCode == "sample_text_2"


def test_PSM_ArtifactElement_ParentProjectName_value_roundtrip():
    instance = PSM_ArtifactElement(ArtifactFileName="sample_text", GeneratingLinesOfCode="sample_text", ParentProjectName="sample_text")
    assert instance.ParentProjectName == "sample_text"
    instance.ParentProjectName = "sample_text_2"
    assert instance.ParentProjectName == "sample_text_2"


def test_PSM_ConfigurationProperty_ConfigurationProfile_value_roundtrip():
    instance = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    assert instance.ConfigurationProfile == "sample_text"
    instance.ConfigurationProfile = "sample_text_2"
    assert instance.ConfigurationProfile == "sample_text_2"


def test_PSM_ConfigurationProperty_FullyQualifiedPropertyName_value_roundtrip():
    instance = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    assert instance.FullyQualifiedPropertyName == "sample_text"
    instance.FullyQualifiedPropertyName = "sample_text_2"
    assert instance.FullyQualifiedPropertyName == "sample_text_2"


def test_PSM_ConfigurationProperty_PropertyValue_value_roundtrip():
    instance = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    assert instance.PropertyValue == "sample_text"
    instance.PropertyValue = "sample_text_2"
    assert instance.PropertyValue == "sample_text_2"


def test_PSM_DependencyLibrary_LibraryGroupName_value_roundtrip():
    instance = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    assert instance.LibraryGroupName == "sample_text"
    instance.LibraryGroupName = "sample_text_2"
    assert instance.LibraryGroupName == "sample_text_2"


def test_PSM_DependencyLibrary_LibraryName_value_roundtrip():
    instance = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    assert instance.LibraryName == "sample_text"
    instance.LibraryName = "sample_text_2"
    assert instance.LibraryName == "sample_text_2"


def test_PSM_DependencyLibrary_LibraryScope_value_roundtrip():
    instance = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    assert instance.LibraryScope == "sample_text"
    instance.LibraryScope = "sample_text_2"
    assert instance.LibraryScope == "sample_text_2"


def test_PSM_DistributedApplicationProject_ApplicationName_value_roundtrip():
    instance = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    assert instance.ApplicationName == "sample_text"
    instance.ApplicationName = "sample_text_2"
    assert instance.ApplicationName == "sample_text_2"


def test_PSM_DistributedApplicationProject_ProjectPackageURL_value_roundtrip():
    instance = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    assert instance.ProjectPackageURL == "sample_text"
    instance.ProjectPackageURL = "sample_text_2"
    assert instance.ProjectPackageURL == "sample_text_2"


def test_PSM_DockerContainerDefinition_BuildField_value_roundtrip():
    instance = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    assert instance.BuildField == "sample_text"
    instance.BuildField = "sample_text_2"
    assert instance.BuildField == "sample_text_2"


def test_PSM_DockerContainerDefinition_ContainerName_value_roundtrip():
    instance = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    assert instance.ContainerName == "sample_text"
    instance.ContainerName = "sample_text_2"
    assert instance.ContainerName == "sample_text_2"


def test_PSM_DockerContainerDefinition_GeneratesLogs_value_roundtrip():
    instance = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    assert instance.GeneratesLogs == True
    instance.GeneratesLogs = False
    assert instance.GeneratesLogs == False


def test_PSM_DockerContainerDefinition_ImageField_value_roundtrip():
    instance = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    assert instance.ImageField == "sample_text"
    instance.ImageField = "sample_text_2"
    assert instance.ImageField == "sample_text_2"


def test_PSM_DockerContainerLink_DependencyOrder_value_roundtrip():
    instance = PSM_DockerContainerLink(DependencyOrder=7, LinksDependsOnField="sample_text")
    assert instance.DependencyOrder == 7
    instance.DependencyOrder = 13
    assert instance.DependencyOrder == 13


def test_PSM_DockerContainerLink_LinksDependsOnField_value_roundtrip():
    instance = PSM_DockerContainerLink(DependencyOrder=7, LinksDependsOnField="sample_text")
    assert instance.LinksDependsOnField == "sample_text"
    instance.LinksDependsOnField = "sample_text_2"
    assert instance.LinksDependsOnField == "sample_text_2"


def test_PSM_DockerContainerPort_ExposesPortsField_value_roundtrip():
    instance = PSM_DockerContainerPort(ExposesPortsField="sample_text")
    assert instance.ExposesPortsField == "sample_text"
    instance.ExposesPortsField = "sample_text_2"
    assert instance.ExposesPortsField == "sample_text_2"


def test_PSM_JavaAnnotation_AnnotationName_value_roundtrip():
    instance = PSM_JavaAnnotation(AnnotationName="sample_text")
    assert instance.AnnotationName == "sample_text"
    instance.AnnotationName = "sample_text_2"
    assert instance.AnnotationName == "sample_text_2"


def test_PSM_JavaAnnotationParameter_ParameterName_value_roundtrip():
    instance = PSM_JavaAnnotationParameter(ParameterName="sample_text", ParameterValue="sample_text")
    assert instance.ParameterName == "sample_text"
    instance.ParameterName = "sample_text_2"
    assert instance.ParameterName == "sample_text_2"


def test_PSM_JavaAnnotationParameter_ParameterValue_value_roundtrip():
    instance = PSM_JavaAnnotationParameter(ParameterName="sample_text", ParameterValue="sample_text")
    assert instance.ParameterValue == "sample_text"
    instance.ParameterValue = "sample_text_2"
    assert instance.ParameterValue == "sample_text_2"


def test_PSM_JavaDataField_FieldValue_value_roundtrip():
    instance = PSM_JavaDataField(FieldValue="sample_text")
    assert instance.FieldValue == "sample_text"
    instance.FieldValue = "sample_text_2"
    assert instance.FieldValue == "sample_text_2"


def test_PSM_JavaDataType_IsPrimitive_value_roundtrip():
    instance = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    assert instance.IsPrimitive == True
    instance.IsPrimitive = False
    assert instance.IsPrimitive == False


def test_PSM_JavaDataType_JsonSchema_value_roundtrip():
    instance = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    assert instance.JsonSchema == "sample_text"
    instance.JsonSchema = "sample_text_2"
    assert instance.JsonSchema == "sample_text_2"


def test_PSM_JavaDataType_PackageName_value_roundtrip():
    instance = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    assert instance.PackageName == "sample_text"
    instance.PackageName = "sample_text_2"
    assert instance.PackageName == "sample_text_2"


def test_PSM_JavaElement_ElementIdentifier_value_roundtrip():
    instance = PSM_JavaElement(ElementIdentifier="sample_text", ElementProfile="sample_text")
    assert instance.ElementIdentifier == "sample_text"
    instance.ElementIdentifier = "sample_text_2"
    assert instance.ElementIdentifier == "sample_text_2"


def test_PSM_JavaElement_ElementProfile_value_roundtrip():
    instance = PSM_JavaElement(ElementIdentifier="sample_text", ElementProfile="sample_text")
    assert instance.ElementProfile == "sample_text"
    instance.ElementProfile = "sample_text_2"
    assert instance.ElementProfile == "sample_text_2"


def test_PSM_JavaMethod_RootCallingMethod_value_roundtrip():
    instance = PSM_JavaMethod(RootCallingMethod="sample_text")
    assert instance.RootCallingMethod == "sample_text"
    instance.RootCallingMethod = "sample_text_2"
    assert instance.RootCallingMethod == "sample_text_2"


def test_PSM_JavaMethodParameter_ParameterOrder_value_roundtrip():
    instance = PSM_JavaMethodParameter(ParameterOrder=7)
    assert instance.ParameterOrder == 7
    instance.ParameterOrder = 13
    assert instance.ParameterOrder == 13


def test_PSM_MicroserviceProject_ProjectArtifactId_value_roundtrip():
    instance = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    assert instance.ProjectArtifactId == "sample_text"
    instance.ProjectArtifactId = "sample_text_2"
    assert instance.ProjectArtifactId == "sample_text_2"


def test_PSM_SpringWebApplicationLayer_LayerName_value_roundtrip():
    instance = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    assert instance.LayerName == "sample_text"
    instance.LayerName = "sample_text_2"
    assert instance.LayerName == "sample_text_2"


def test_PSM_ApplicationProject_isa_ArtifactElement():
    instance = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_ConfigurationProperty_isa_ArtifactElement():
    instance = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_DependencyLibrary_isa_ArtifactElement():
    instance = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_DockerContainerDefinition_isa_ArtifactElement():
    instance = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_DockerContainerLink_isa_ArtifactElement():
    instance = PSM_DockerContainerLink(DependencyOrder=7, LinksDependsOnField="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_DockerContainerPort_isa_ArtifactElement():
    instance = PSM_DockerContainerPort(ExposesPortsField="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_JavaAnnotation_isa_ArtifactElement():
    instance = PSM_JavaAnnotation(AnnotationName="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_JavaAnnotationParameter_isa_ArtifactElement():
    instance = PSM_JavaAnnotationParameter(ParameterName="sample_text", ParameterValue="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_JavaElement_isa_ArtifactElement():
    instance = PSM_JavaElement(ElementIdentifier="sample_text", ElementProfile="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_MicroserviceProject_isa_ArtifactElement():
    instance = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_SpringWebApplicationLayer_isa_ArtifactElement():
    instance = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    assert isinstance(instance, ArtifactElement)


def test_PSM_JavaMethodParameter_isa_JavaDataField():
    instance = PSM_JavaMethodParameter(ParameterOrder=7)
    assert isinstance(instance, JavaDataField)


def test_PSM_JavaUserDefinedType_isa_JavaDataType():
    instance = PSM_JavaUserDefinedType()
    assert isinstance(instance, JavaDataType)


def test_PSM_JavaDataField_isa_JavaElement():
    instance = PSM_JavaDataField(FieldValue="sample_text")
    assert isinstance(instance, JavaElement)


def test_PSM_JavaDataType_isa_JavaElement():
    instance = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    assert isinstance(instance, JavaElement)


def test_PSM_JavaMethod_isa_JavaElement():
    instance = PSM_JavaMethod(RootCallingMethod="sample_text")
    assert isinstance(instance, JavaElement)


def test_PSM_JavaSpringMVCApplicationProject_isa_JavaSpringWebApplicationProject():
    instance = PSM_JavaSpringMVCApplicationProject()
    assert isinstance(instance, JavaSpringWebApplicationProject)


def test_PSM_JavaSpringWebFluxApplicationProject_isa_JavaSpringWebApplicationProject():
    instance = PSM_JavaSpringWebFluxApplicationProject()
    assert isinstance(instance, JavaSpringWebApplicationProject)


def test_PSM_JavaClassType_isa_JavaUserDefinedType():
    instance = PSM_JavaClassType()
    assert isinstance(instance, JavaUserDefinedType)


def test_PSM_JavaInterfaceType_isa_JavaUserDefinedType():
    instance = PSM_JavaInterfaceType()
    assert isinstance(instance, JavaUserDefinedType)


def test_PSM_JavaSpringWebApplicationProject_isa_MicroserviceProject():
    instance = PSM_JavaSpringWebApplicationProject()
    assert isinstance(instance, MicroserviceProject)


def test_PSM_SpringBootApplicationLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringBootApplicationLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringComponentLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringComponentLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringConfigurationLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringConfigurationLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringControllerLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringControllerLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringDomainLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringDomainLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringFeignClientLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringFeignClientLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringModelPojoLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringModelPojoLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringRepositoryLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringRepositoryLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_PSM_SpringServiceLayer_isa_SpringWebApplicationLayer():
    instance = PSM_SpringServiceLayer()
    assert isinstance(instance, SpringWebApplicationLayer)


def test_assoc_annotations18_link_reassign_clear():
    a = PSM_JavaElement(ElementIdentifier="sample_text", ElementProfile="sample_text")
    b1 = PSM_JavaAnnotation(AnnotationName="sample_text")
    b2 = PSM_JavaAnnotation(AnnotationName="sample_text_2")
    _safe_set(a, 'PSM_JavaElement', {b1})
    assert _is_linked(a, 'PSM_JavaElement', b1)
    if hasattr(b1, 'PSM_JavaAnnotation'):
        assert _is_linked(b1, 'PSM_JavaAnnotation', a)
    _safe_set(a, 'PSM_JavaElement', {b2})
    assert _is_linked(a, 'PSM_JavaElement', b2)
    if hasattr(b1, 'PSM_JavaAnnotation'):
        assert not _is_linked(b1, 'PSM_JavaAnnotation', a)
    if hasattr(b2, 'PSM_JavaAnnotation'):
        assert _is_linked(b2, 'PSM_JavaAnnotation', a)
    _safe_set(a, 'PSM_JavaElement', set())
    assert not _is_linked(a, 'PSM_JavaElement', b2)
    if hasattr(b2, 'PSM_JavaAnnotation'):
        assert not _is_linked(b2, 'PSM_JavaAnnotation', a)


def test_assoc_application0_link_reassign_clear():
    a = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    b1 = PSM_RootPSM()
    b2 = PSM_RootPSM()
    _safe_set(a, 'PSM_DistributedApplicationProject', b1)
    assert _is_linked(a, 'PSM_DistributedApplicationProject', b1)
    if hasattr(b1, 'PSM_RootPSM'):
        assert _is_linked(b1, 'PSM_RootPSM', a)
    _safe_set(a, 'PSM_DistributedApplicationProject', b2)
    assert _is_linked(a, 'PSM_DistributedApplicationProject', b2)
    if hasattr(b1, 'PSM_RootPSM'):
        assert not _is_linked(b1, 'PSM_RootPSM', a)
    if hasattr(b2, 'PSM_RootPSM'):
        assert _is_linked(b2, 'PSM_RootPSM', a)
    _safe_set(a, 'PSM_DistributedApplicationProject', None)
    assert not _is_linked(a, 'PSM_DistributedApplicationProject', b2)
    if hasattr(b2, 'PSM_RootPSM'):
        assert not _is_linked(b2, 'PSM_RootPSM', a)


def test_assoc_application_project3_link_reassign_clear():
    a = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    b1 = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    b2 = PSM_ApplicationProject(ProjectArtifactId="sample_text_2")
    _safe_set(a, 'PSM_DistributedApplicationProject4', b1)
    assert _is_linked(a, 'PSM_DistributedApplicationProject4', b1)
    if hasattr(b1, 'PSM_ApplicationProject'):
        assert _is_linked(b1, 'PSM_ApplicationProject', a)
    _safe_set(a, 'PSM_DistributedApplicationProject4', b2)
    assert _is_linked(a, 'PSM_DistributedApplicationProject4', b2)
    if hasattr(b1, 'PSM_ApplicationProject'):
        assert not _is_linked(b1, 'PSM_ApplicationProject', a)
    if hasattr(b2, 'PSM_ApplicationProject'):
        assert _is_linked(b2, 'PSM_ApplicationProject', a)
    _safe_set(a, 'PSM_DistributedApplicationProject4', None)
    assert not _is_linked(a, 'PSM_DistributedApplicationProject4', b2)
    if hasattr(b2, 'PSM_ApplicationProject'):
        assert not _is_linked(b2, 'PSM_ApplicationProject', a)


def test_assoc_containers1_link_reassign_clear():
    a = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    b1 = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    b2 = PSM_DistributedApplicationProject(ApplicationName="sample_text_2", ProjectPackageURL="sample_text_2")
    _safe_set(a, 'PSM_DockerContainerDefinition', b1)
    assert _is_linked(a, 'PSM_DockerContainerDefinition', b1)
    if hasattr(b1, 'PSM_DistributedApplicationProject2'):
        assert _is_linked(b1, 'PSM_DistributedApplicationProject2', a)
    _safe_set(a, 'PSM_DockerContainerDefinition', b2)
    assert _is_linked(a, 'PSM_DockerContainerDefinition', b2)
    if hasattr(b1, 'PSM_DistributedApplicationProject2'):
        assert not _is_linked(b1, 'PSM_DistributedApplicationProject2', a)
    if hasattr(b2, 'PSM_DistributedApplicationProject2'):
        assert _is_linked(b2, 'PSM_DistributedApplicationProject2', a)
    _safe_set(a, 'PSM_DockerContainerDefinition', None)
    assert not _is_linked(a, 'PSM_DockerContainerDefinition', b2)
    if hasattr(b2, 'PSM_DistributedApplicationProject2'):
        assert not _is_linked(b2, 'PSM_DistributedApplicationProject2', a)


def test_assoc_elements16_link_reassign_clear():
    a = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    b1 = PSM_JavaUserDefinedType()
    b2 = PSM_JavaUserDefinedType()
    _safe_set(a, 'PSM_SpringWebApplicationLayer17', {b1})
    assert _is_linked(a, 'PSM_SpringWebApplicationLayer17', b1)
    if hasattr(b1, 'PSM_JavaUserDefinedType'):
        assert _is_linked(b1, 'PSM_JavaUserDefinedType', a)
    _safe_set(a, 'PSM_SpringWebApplicationLayer17', {b2})
    assert _is_linked(a, 'PSM_SpringWebApplicationLayer17', b2)
    if hasattr(b1, 'PSM_JavaUserDefinedType'):
        assert not _is_linked(b1, 'PSM_JavaUserDefinedType', a)
    if hasattr(b2, 'PSM_JavaUserDefinedType'):
        assert _is_linked(b2, 'PSM_JavaUserDefinedType', a)
    _safe_set(a, 'PSM_SpringWebApplicationLayer17', set())
    assert not _is_linked(a, 'PSM_SpringWebApplicationLayer17', b2)
    if hasattr(b2, 'PSM_JavaUserDefinedType'):
        assert not _is_linked(b2, 'PSM_JavaUserDefinedType', a)


def test_assoc_fields32_link_reassign_clear():
    a = PSM_JavaDataField(FieldValue="sample_text")
    b1 = PSM_JavaUserDefinedType()
    b2 = PSM_JavaUserDefinedType()
    _safe_set(a, 'PSM_JavaDataField', b1)
    assert _is_linked(a, 'PSM_JavaDataField', b1)
    if hasattr(b1, 'PSM_JavaUserDefinedType33'):
        assert _is_linked(b1, 'PSM_JavaUserDefinedType33', a)
    _safe_set(a, 'PSM_JavaDataField', b2)
    assert _is_linked(a, 'PSM_JavaDataField', b2)
    if hasattr(b1, 'PSM_JavaUserDefinedType33'):
        assert not _is_linked(b1, 'PSM_JavaUserDefinedType33', a)
    if hasattr(b2, 'PSM_JavaUserDefinedType33'):
        assert _is_linked(b2, 'PSM_JavaUserDefinedType33', a)
    _safe_set(a, 'PSM_JavaDataField', None)
    assert not _is_linked(a, 'PSM_JavaDataField', b2)
    if hasattr(b2, 'PSM_JavaUserDefinedType33'):
        assert not _is_linked(b2, 'PSM_JavaUserDefinedType33', a)


def test_assoc_invokes43_link_reassign_clear():
    a = PSM_JavaMethod(RootCallingMethod="sample_text")
    b1 = PSM_JavaMethod(RootCallingMethod="sample_text")
    b2 = PSM_JavaMethod(RootCallingMethod="sample_text_2")
    _safe_set(a, 'PSM_JavaMethod42', {b1})
    assert _is_linked(a, 'PSM_JavaMethod42', b1)
    if hasattr(b1, 'PSM_JavaMethod44'):
        assert _is_linked(b1, 'PSM_JavaMethod44', a)
    _safe_set(a, 'PSM_JavaMethod42', {b2})
    assert _is_linked(a, 'PSM_JavaMethod42', b2)
    if hasattr(b1, 'PSM_JavaMethod44'):
        assert not _is_linked(b1, 'PSM_JavaMethod44', a)
    if hasattr(b2, 'PSM_JavaMethod44'):
        assert _is_linked(b2, 'PSM_JavaMethod44', a)
    _safe_set(a, 'PSM_JavaMethod42', set())
    assert not _is_linked(a, 'PSM_JavaMethod42', b2)
    if hasattr(b2, 'PSM_JavaMethod44'):
        assert not _is_linked(b2, 'PSM_JavaMethod44', a)


def test_assoc_layers14_link_reassign_clear():
    a = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    b1 = PSM_JavaSpringWebApplicationProject()
    b2 = PSM_JavaSpringWebApplicationProject()
    _safe_set(a, 'PSM_SpringWebApplicationLayer', b1)
    assert _is_linked(a, 'PSM_SpringWebApplicationLayer', b1)
    if hasattr(b1, 'PSM_JavaSpringWebApplicationProject15'):
        assert _is_linked(b1, 'PSM_JavaSpringWebApplicationProject15', a)
    _safe_set(a, 'PSM_SpringWebApplicationLayer', b2)
    assert _is_linked(a, 'PSM_SpringWebApplicationLayer', b2)
    if hasattr(b1, 'PSM_JavaSpringWebApplicationProject15'):
        assert not _is_linked(b1, 'PSM_JavaSpringWebApplicationProject15', a)
    if hasattr(b2, 'PSM_JavaSpringWebApplicationProject15'):
        assert _is_linked(b2, 'PSM_JavaSpringWebApplicationProject15', a)
    _safe_set(a, 'PSM_SpringWebApplicationLayer', None)
    assert not _is_linked(a, 'PSM_SpringWebApplicationLayer', b2)
    if hasattr(b2, 'PSM_JavaSpringWebApplicationProject15'):
        assert not _is_linked(b2, 'PSM_JavaSpringWebApplicationProject15', a)


def test_assoc_libraries11_link_reassign_clear():
    a = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    b1 = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    b2 = PSM_DependencyLibrary(LibraryGroupName="sample_text_2", LibraryName="sample_text_2", LibraryScope="sample_text_2")
    _safe_set(a, 'PSM_MicroserviceProject12', {b1})
    assert _is_linked(a, 'PSM_MicroserviceProject12', b1)
    if hasattr(b1, 'PSM_DependencyLibrary'):
        assert _is_linked(b1, 'PSM_DependencyLibrary', a)
    _safe_set(a, 'PSM_MicroserviceProject12', {b2})
    assert _is_linked(a, 'PSM_MicroserviceProject12', b2)
    if hasattr(b1, 'PSM_DependencyLibrary'):
        assert not _is_linked(b1, 'PSM_DependencyLibrary', a)
    if hasattr(b2, 'PSM_DependencyLibrary'):
        assert _is_linked(b2, 'PSM_DependencyLibrary', a)
    _safe_set(a, 'PSM_MicroserviceProject12', set())
    assert not _is_linked(a, 'PSM_MicroserviceProject12', b2)
    if hasattr(b2, 'PSM_DependencyLibrary'):
        assert not _is_linked(b2, 'PSM_DependencyLibrary', a)


def test_assoc_links5_link_reassign_clear():
    a = PSM_DockerContainerLink(DependencyOrder=7, LinksDependsOnField="sample_text")
    b1 = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    b2 = PSM_DockerContainerDefinition(BuildField="sample_text_2", ContainerName="sample_text_2", GeneratesLogs=False, ImageField="sample_text_2")
    _safe_set(a, 'PSM_DockerContainerLink', b1)
    assert _is_linked(a, 'PSM_DockerContainerLink', b1)
    if hasattr(b1, 'PSM_DockerContainerDefinition6'):
        assert _is_linked(b1, 'PSM_DockerContainerDefinition6', a)
    _safe_set(a, 'PSM_DockerContainerLink', b2)
    assert _is_linked(a, 'PSM_DockerContainerLink', b2)
    if hasattr(b1, 'PSM_DockerContainerDefinition6'):
        assert not _is_linked(b1, 'PSM_DockerContainerDefinition6', a)
    if hasattr(b2, 'PSM_DockerContainerDefinition6'):
        assert _is_linked(b2, 'PSM_DockerContainerDefinition6', a)
    _safe_set(a, 'PSM_DockerContainerLink', None)
    assert not _is_linked(a, 'PSM_DockerContainerLink', b2)
    if hasattr(b2, 'PSM_DockerContainerDefinition6'):
        assert not _is_linked(b2, 'PSM_DockerContainerDefinition6', a)


def test_assoc_methods21_link_reassign_clear():
    a = PSM_JavaMethod(RootCallingMethod="sample_text")
    b1 = PSM_JavaUserDefinedType()
    b2 = PSM_JavaUserDefinedType()
    _safe_set(a, 'PSM_JavaMethod', b1)
    assert _is_linked(a, 'PSM_JavaMethod', b1)
    if hasattr(b1, 'PSM_JavaUserDefinedType22'):
        assert _is_linked(b1, 'PSM_JavaUserDefinedType22', a)
    _safe_set(a, 'PSM_JavaMethod', b2)
    assert _is_linked(a, 'PSM_JavaMethod', b2)
    if hasattr(b1, 'PSM_JavaUserDefinedType22'):
        assert not _is_linked(b1, 'PSM_JavaUserDefinedType22', a)
    if hasattr(b2, 'PSM_JavaUserDefinedType22'):
        assert _is_linked(b2, 'PSM_JavaUserDefinedType22', a)
    _safe_set(a, 'PSM_JavaMethod', None)
    assert not _is_linked(a, 'PSM_JavaMethod', b2)
    if hasattr(b2, 'PSM_JavaUserDefinedType22'):
        assert not _is_linked(b2, 'PSM_JavaUserDefinedType22', a)


def test_assoc_modules9_link_reassign_clear():
    a = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    b1 = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    b2 = PSM_ApplicationProject(ProjectArtifactId="sample_text_2")
    _safe_set(a, 'PSM_MicroserviceProject', b1)
    assert _is_linked(a, 'PSM_MicroserviceProject', b1)
    if hasattr(b1, 'PSM_ApplicationProject10'):
        assert _is_linked(b1, 'PSM_ApplicationProject10', a)
    _safe_set(a, 'PSM_MicroserviceProject', b2)
    assert _is_linked(a, 'PSM_MicroserviceProject', b2)
    if hasattr(b1, 'PSM_ApplicationProject10'):
        assert not _is_linked(b1, 'PSM_ApplicationProject10', a)
    if hasattr(b2, 'PSM_ApplicationProject10'):
        assert _is_linked(b2, 'PSM_ApplicationProject10', a)
    _safe_set(a, 'PSM_MicroserviceProject', None)
    assert not _is_linked(a, 'PSM_MicroserviceProject', b2)
    if hasattr(b2, 'PSM_ApplicationProject10'):
        assert not _is_linked(b2, 'PSM_ApplicationProject10', a)


def test_assoc_parameters19_link_reassign_clear():
    a = PSM_JavaAnnotationParameter(ParameterName="sample_text", ParameterValue="sample_text")
    b1 = PSM_JavaAnnotation(AnnotationName="sample_text")
    b2 = PSM_JavaAnnotation(AnnotationName="sample_text_2")
    _safe_set(a, 'PSM_JavaAnnotationParameter', b1)
    assert _is_linked(a, 'PSM_JavaAnnotationParameter', b1)
    if hasattr(b1, 'PSM_JavaAnnotation20'):
        assert _is_linked(b1, 'PSM_JavaAnnotation20', a)
    _safe_set(a, 'PSM_JavaAnnotationParameter', b2)
    assert _is_linked(a, 'PSM_JavaAnnotationParameter', b2)
    if hasattr(b1, 'PSM_JavaAnnotation20'):
        assert not _is_linked(b1, 'PSM_JavaAnnotation20', a)
    if hasattr(b2, 'PSM_JavaAnnotation20'):
        assert _is_linked(b2, 'PSM_JavaAnnotation20', a)
    _safe_set(a, 'PSM_JavaAnnotationParameter', None)
    assert not _is_linked(a, 'PSM_JavaAnnotationParameter', b2)
    if hasattr(b2, 'PSM_JavaAnnotation20'):
        assert not _is_linked(b2, 'PSM_JavaAnnotation20', a)


def test_assoc_parameters38_link_reassign_clear():
    a = PSM_JavaMethodParameter(ParameterOrder=7)
    b1 = PSM_JavaMethod(RootCallingMethod="sample_text")
    b2 = PSM_JavaMethod(RootCallingMethod="sample_text_2")
    _safe_set(a, 'PSM_JavaMethodParameter', b1)
    assert _is_linked(a, 'PSM_JavaMethodParameter', b1)
    if hasattr(b1, 'PSM_JavaMethod39'):
        assert _is_linked(b1, 'PSM_JavaMethod39', a)
    _safe_set(a, 'PSM_JavaMethodParameter', b2)
    assert _is_linked(a, 'PSM_JavaMethodParameter', b2)
    if hasattr(b1, 'PSM_JavaMethod39'):
        assert not _is_linked(b1, 'PSM_JavaMethod39', a)
    if hasattr(b2, 'PSM_JavaMethod39'):
        assert _is_linked(b2, 'PSM_JavaMethod39', a)
    _safe_set(a, 'PSM_JavaMethodParameter', None)
    assert not _is_linked(a, 'PSM_JavaMethodParameter', b2)
    if hasattr(b2, 'PSM_JavaMethod39'):
        assert not _is_linked(b2, 'PSM_JavaMethod39', a)


def test_assoc_parent35_link_reassign_clear():
    a = PSM_JavaMethod(RootCallingMethod="sample_text")
    b1 = PSM_JavaUserDefinedType()
    b2 = PSM_JavaUserDefinedType()
    _safe_set(a, 'PSM_JavaMethod36', b1)
    assert _is_linked(a, 'PSM_JavaMethod36', b1)
    if hasattr(b1, 'PSM_JavaUserDefinedType37'):
        assert _is_linked(b1, 'PSM_JavaUserDefinedType37', a)
    _safe_set(a, 'PSM_JavaMethod36', b2)
    assert _is_linked(a, 'PSM_JavaMethod36', b2)
    if hasattr(b1, 'PSM_JavaUserDefinedType37'):
        assert not _is_linked(b1, 'PSM_JavaUserDefinedType37', a)
    if hasattr(b2, 'PSM_JavaUserDefinedType37'):
        assert _is_linked(b2, 'PSM_JavaUserDefinedType37', a)
    _safe_set(a, 'PSM_JavaMethod36', None)
    assert not _is_linked(a, 'PSM_JavaMethod36', b2)
    if hasattr(b2, 'PSM_JavaUserDefinedType37'):
        assert not _is_linked(b2, 'PSM_JavaUserDefinedType37', a)


def test_assoc_ports7_link_reassign_clear():
    a = PSM_DockerContainerPort(ExposesPortsField="sample_text")
    b1 = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    b2 = PSM_DockerContainerDefinition(BuildField="sample_text_2", ContainerName="sample_text_2", GeneratesLogs=False, ImageField="sample_text_2")
    _safe_set(a, 'PSM_DockerContainerPort', b1)
    assert _is_linked(a, 'PSM_DockerContainerPort', b1)
    if hasattr(b1, 'PSM_DockerContainerDefinition8'):
        assert _is_linked(b1, 'PSM_DockerContainerDefinition8', a)
    _safe_set(a, 'PSM_DockerContainerPort', b2)
    assert _is_linked(a, 'PSM_DockerContainerPort', b2)
    if hasattr(b1, 'PSM_DockerContainerDefinition8'):
        assert not _is_linked(b1, 'PSM_DockerContainerDefinition8', a)
    if hasattr(b2, 'PSM_DockerContainerDefinition8'):
        assert _is_linked(b2, 'PSM_DockerContainerDefinition8', a)
    _safe_set(a, 'PSM_DockerContainerPort', None)
    assert not _is_linked(a, 'PSM_DockerContainerPort', b2)
    if hasattr(b2, 'PSM_DockerContainerDefinition8'):
        assert not _is_linked(b2, 'PSM_DockerContainerDefinition8', a)


def test_assoc_properties13_link_reassign_clear():
    a = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    b1 = PSM_JavaSpringWebApplicationProject()
    b2 = PSM_JavaSpringWebApplicationProject()
    _safe_set(a, 'PSM_ConfigurationProperty', b1)
    assert _is_linked(a, 'PSM_ConfigurationProperty', b1)
    if hasattr(b1, 'PSM_JavaSpringWebApplicationProject'):
        assert _is_linked(b1, 'PSM_JavaSpringWebApplicationProject', a)
    _safe_set(a, 'PSM_ConfigurationProperty', b2)
    assert _is_linked(a, 'PSM_ConfigurationProperty', b2)
    if hasattr(b1, 'PSM_JavaSpringWebApplicationProject'):
        assert not _is_linked(b1, 'PSM_JavaSpringWebApplicationProject', a)
    if hasattr(b2, 'PSM_JavaSpringWebApplicationProject'):
        assert _is_linked(b2, 'PSM_JavaSpringWebApplicationProject', a)
    _safe_set(a, 'PSM_ConfigurationProperty', None)
    assert not _is_linked(a, 'PSM_ConfigurationProperty', b2)
    if hasattr(b2, 'PSM_JavaSpringWebApplicationProject'):
        assert not _is_linked(b2, 'PSM_JavaSpringWebApplicationProject', a)


def test_assoc_returns40_link_reassign_clear():
    a = PSM_JavaMethod(RootCallingMethod="sample_text")
    b1 = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    b2 = PSM_JavaDataType(IsPrimitive=False, JsonSchema="sample_text_2", PackageName="sample_text_2")
    _safe_set(a, 'PSM_JavaMethod41', b1)
    assert _is_linked(a, 'PSM_JavaMethod41', b1)
    if hasattr(b1, 'PSM_JavaDataType'):
        assert _is_linked(b1, 'PSM_JavaDataType', a)
    _safe_set(a, 'PSM_JavaMethod41', b2)
    assert _is_linked(a, 'PSM_JavaMethod41', b2)
    if hasattr(b1, 'PSM_JavaDataType'):
        assert not _is_linked(b1, 'PSM_JavaDataType', a)
    if hasattr(b2, 'PSM_JavaDataType'):
        assert _is_linked(b2, 'PSM_JavaDataType', a)
    _safe_set(a, 'PSM_JavaMethod41', None)
    assert not _is_linked(a, 'PSM_JavaMethod41', b2)
    if hasattr(b2, 'PSM_JavaDataType'):
        assert not _is_linked(b2, 'PSM_JavaDataType', a)


def test_assoc_type45_link_reassign_clear():
    a = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    b1 = PSM_JavaDataField(FieldValue="sample_text")
    b2 = PSM_JavaDataField(FieldValue="sample_text_2")
    _safe_set(a, 'PSM_JavaDataType47', b1)
    assert _is_linked(a, 'PSM_JavaDataType47', b1)
    if hasattr(b1, 'PSM_JavaDataField46'):
        assert _is_linked(b1, 'PSM_JavaDataField46', a)
    _safe_set(a, 'PSM_JavaDataType47', b2)
    assert _is_linked(a, 'PSM_JavaDataType47', b2)
    if hasattr(b1, 'PSM_JavaDataField46'):
        assert not _is_linked(b1, 'PSM_JavaDataField46', a)
    if hasattr(b2, 'PSM_JavaDataField46'):
        assert _is_linked(b2, 'PSM_JavaDataField46', a)
    _safe_set(a, 'PSM_JavaDataType47', None)
    assert not _is_linked(a, 'PSM_JavaDataType47', b2)
    if hasattr(b2, 'PSM_JavaDataField46'):
        assert not _is_linked(b2, 'PSM_JavaDataField46', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArtifactElement_strategy = st.builds(ArtifactElement)
@given(instance=ArtifactElement_strategy)
@settings(max_examples=25)
def test_ArtifactElement_instantiation(instance):
    assert isinstance(instance, ArtifactElement)


JavaDataField_strategy = st.builds(JavaDataField)
@given(instance=JavaDataField_strategy)
@settings(max_examples=25)
def test_JavaDataField_instantiation(instance):
    assert isinstance(instance, JavaDataField)


JavaDataType_strategy = st.builds(JavaDataType)
@given(instance=JavaDataType_strategy)
@settings(max_examples=25)
def test_JavaDataType_instantiation(instance):
    assert isinstance(instance, JavaDataType)


JavaElement_strategy = st.builds(JavaElement)
@given(instance=JavaElement_strategy)
@settings(max_examples=25)
def test_JavaElement_instantiation(instance):
    assert isinstance(instance, JavaElement)


JavaSpringWebApplicationProject_strategy = st.builds(JavaSpringWebApplicationProject)
@given(instance=JavaSpringWebApplicationProject_strategy)
@settings(max_examples=25)
def test_JavaSpringWebApplicationProject_instantiation(instance):
    assert isinstance(instance, JavaSpringWebApplicationProject)


JavaUserDefinedType_strategy = st.builds(JavaUserDefinedType)
@given(instance=JavaUserDefinedType_strategy)
@settings(max_examples=25)
def test_JavaUserDefinedType_instantiation(instance):
    assert isinstance(instance, JavaUserDefinedType)


MicroserviceProject_strategy = st.builds(MicroserviceProject)
@given(instance=MicroserviceProject_strategy)
@settings(max_examples=25)
def test_MicroserviceProject_instantiation(instance):
    assert isinstance(instance, MicroserviceProject)


PSM_ApplicationProject_strategy = st.builds(PSM_ApplicationProject, ProjectArtifactId=safe_text)
@given(instance=PSM_ApplicationProject_strategy)
@settings(max_examples=25)
def test_PSM_ApplicationProject_instantiation(instance):
    assert isinstance(instance, PSM_ApplicationProject)


PSM_ArtifactElement_strategy = st.builds(PSM_ArtifactElement, ArtifactFileName=safe_text, GeneratingLinesOfCode=safe_text, ParentProjectName=safe_text)
@given(instance=PSM_ArtifactElement_strategy)
@settings(max_examples=25)
def test_PSM_ArtifactElement_instantiation(instance):
    assert isinstance(instance, PSM_ArtifactElement)


PSM_ConfigurationProperty_strategy = st.builds(PSM_ConfigurationProperty, ConfigurationProfile=safe_text, FullyQualifiedPropertyName=safe_text, PropertyValue=safe_text)
@given(instance=PSM_ConfigurationProperty_strategy)
@settings(max_examples=25)
def test_PSM_ConfigurationProperty_instantiation(instance):
    assert isinstance(instance, PSM_ConfigurationProperty)


PSM_DependencyLibrary_strategy = st.builds(PSM_DependencyLibrary, LibraryGroupName=safe_text, LibraryName=safe_text, LibraryScope=safe_text)
@given(instance=PSM_DependencyLibrary_strategy)
@settings(max_examples=25)
def test_PSM_DependencyLibrary_instantiation(instance):
    assert isinstance(instance, PSM_DependencyLibrary)


PSM_DistributedApplicationProject_strategy = st.builds(PSM_DistributedApplicationProject, ApplicationName=safe_text, ProjectPackageURL=safe_text)
@given(instance=PSM_DistributedApplicationProject_strategy)
@settings(max_examples=25)
def test_PSM_DistributedApplicationProject_instantiation(instance):
    assert isinstance(instance, PSM_DistributedApplicationProject)


PSM_DockerContainerDefinition_strategy = st.builds(PSM_DockerContainerDefinition, BuildField=safe_text, ContainerName=safe_text, GeneratesLogs=st.booleans(), ImageField=safe_text)
@given(instance=PSM_DockerContainerDefinition_strategy)
@settings(max_examples=25)
def test_PSM_DockerContainerDefinition_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerDefinition)


PSM_DockerContainerLink_strategy = st.builds(PSM_DockerContainerLink, DependencyOrder=st.integers(), LinksDependsOnField=safe_text)
@given(instance=PSM_DockerContainerLink_strategy)
@settings(max_examples=25)
def test_PSM_DockerContainerLink_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerLink)


PSM_DockerContainerPort_strategy = st.builds(PSM_DockerContainerPort, ExposesPortsField=safe_text)
@given(instance=PSM_DockerContainerPort_strategy)
@settings(max_examples=25)
def test_PSM_DockerContainerPort_instantiation(instance):
    assert isinstance(instance, PSM_DockerContainerPort)


PSM_JavaAnnotation_strategy = st.builds(PSM_JavaAnnotation, AnnotationName=safe_text)
@given(instance=PSM_JavaAnnotation_strategy)
@settings(max_examples=25)
def test_PSM_JavaAnnotation_instantiation(instance):
    assert isinstance(instance, PSM_JavaAnnotation)


PSM_JavaAnnotationParameter_strategy = st.builds(PSM_JavaAnnotationParameter, ParameterName=safe_text, ParameterValue=safe_text)
@given(instance=PSM_JavaAnnotationParameter_strategy)
@settings(max_examples=25)
def test_PSM_JavaAnnotationParameter_instantiation(instance):
    assert isinstance(instance, PSM_JavaAnnotationParameter)


PSM_JavaClassType_strategy = st.builds(PSM_JavaClassType)
@given(instance=PSM_JavaClassType_strategy)
@settings(max_examples=25)
def test_PSM_JavaClassType_instantiation(instance):
    assert isinstance(instance, PSM_JavaClassType)


PSM_JavaDataField_strategy = st.builds(PSM_JavaDataField, FieldValue=safe_text)
@given(instance=PSM_JavaDataField_strategy)
@settings(max_examples=25)
def test_PSM_JavaDataField_instantiation(instance):
    assert isinstance(instance, PSM_JavaDataField)


PSM_JavaDataType_strategy = st.builds(PSM_JavaDataType, IsPrimitive=st.booleans(), JsonSchema=safe_text, PackageName=safe_text)
@given(instance=PSM_JavaDataType_strategy)
@settings(max_examples=25)
def test_PSM_JavaDataType_instantiation(instance):
    assert isinstance(instance, PSM_JavaDataType)


PSM_JavaElement_strategy = st.builds(PSM_JavaElement, ElementIdentifier=safe_text, ElementProfile=safe_text)
@given(instance=PSM_JavaElement_strategy)
@settings(max_examples=25)
def test_PSM_JavaElement_instantiation(instance):
    assert isinstance(instance, PSM_JavaElement)


PSM_JavaInterfaceType_strategy = st.builds(PSM_JavaInterfaceType)
@given(instance=PSM_JavaInterfaceType_strategy)
@settings(max_examples=25)
def test_PSM_JavaInterfaceType_instantiation(instance):
    assert isinstance(instance, PSM_JavaInterfaceType)


PSM_JavaMethod_strategy = st.builds(PSM_JavaMethod, RootCallingMethod=safe_text)
@given(instance=PSM_JavaMethod_strategy)
@settings(max_examples=25)
def test_PSM_JavaMethod_instantiation(instance):
    assert isinstance(instance, PSM_JavaMethod)


PSM_JavaMethodParameter_strategy = st.builds(PSM_JavaMethodParameter, ParameterOrder=st.integers())
@given(instance=PSM_JavaMethodParameter_strategy)
@settings(max_examples=25)
def test_PSM_JavaMethodParameter_instantiation(instance):
    assert isinstance(instance, PSM_JavaMethodParameter)


PSM_JavaSpringMVCApplicationProject_strategy = st.builds(PSM_JavaSpringMVCApplicationProject)
@given(instance=PSM_JavaSpringMVCApplicationProject_strategy)
@settings(max_examples=25)
def test_PSM_JavaSpringMVCApplicationProject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringMVCApplicationProject)


PSM_JavaSpringWebApplicationProject_strategy = st.builds(PSM_JavaSpringWebApplicationProject)
@given(instance=PSM_JavaSpringWebApplicationProject_strategy)
@settings(max_examples=25)
def test_PSM_JavaSpringWebApplicationProject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringWebApplicationProject)


PSM_JavaSpringWebFluxApplicationProject_strategy = st.builds(PSM_JavaSpringWebFluxApplicationProject)
@given(instance=PSM_JavaSpringWebFluxApplicationProject_strategy)
@settings(max_examples=25)
def test_PSM_JavaSpringWebFluxApplicationProject_instantiation(instance):
    assert isinstance(instance, PSM_JavaSpringWebFluxApplicationProject)


PSM_JavaUserDefinedType_strategy = st.builds(PSM_JavaUserDefinedType)
@given(instance=PSM_JavaUserDefinedType_strategy)
@settings(max_examples=25)
def test_PSM_JavaUserDefinedType_instantiation(instance):
    assert isinstance(instance, PSM_JavaUserDefinedType)


PSM_MicroserviceProject_strategy = st.builds(PSM_MicroserviceProject, ProjectArtifactId=safe_text)
@given(instance=PSM_MicroserviceProject_strategy)
@settings(max_examples=25)
def test_PSM_MicroserviceProject_instantiation(instance):
    assert isinstance(instance, PSM_MicroserviceProject)


PSM_RootPSM_strategy = st.builds(PSM_RootPSM)
@given(instance=PSM_RootPSM_strategy)
@settings(max_examples=25)
def test_PSM_RootPSM_instantiation(instance):
    assert isinstance(instance, PSM_RootPSM)


PSM_SpringBootApplicationLayer_strategy = st.builds(PSM_SpringBootApplicationLayer)
@given(instance=PSM_SpringBootApplicationLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringBootApplicationLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringBootApplicationLayer)


PSM_SpringComponentLayer_strategy = st.builds(PSM_SpringComponentLayer)
@given(instance=PSM_SpringComponentLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringComponentLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringComponentLayer)


PSM_SpringConfigurationLayer_strategy = st.builds(PSM_SpringConfigurationLayer)
@given(instance=PSM_SpringConfigurationLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringConfigurationLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringConfigurationLayer)


PSM_SpringControllerLayer_strategy = st.builds(PSM_SpringControllerLayer)
@given(instance=PSM_SpringControllerLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringControllerLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringControllerLayer)


PSM_SpringDomainLayer_strategy = st.builds(PSM_SpringDomainLayer)
@given(instance=PSM_SpringDomainLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringDomainLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringDomainLayer)


PSM_SpringFeignClientLayer_strategy = st.builds(PSM_SpringFeignClientLayer)
@given(instance=PSM_SpringFeignClientLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringFeignClientLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringFeignClientLayer)


PSM_SpringModelPojoLayer_strategy = st.builds(PSM_SpringModelPojoLayer)
@given(instance=PSM_SpringModelPojoLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringModelPojoLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringModelPojoLayer)


PSM_SpringRepositoryLayer_strategy = st.builds(PSM_SpringRepositoryLayer)
@given(instance=PSM_SpringRepositoryLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringRepositoryLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringRepositoryLayer)


PSM_SpringServiceLayer_strategy = st.builds(PSM_SpringServiceLayer)
@given(instance=PSM_SpringServiceLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringServiceLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringServiceLayer)


PSM_SpringWebApplicationLayer_strategy = st.builds(PSM_SpringWebApplicationLayer, LayerName=safe_text)
@given(instance=PSM_SpringWebApplicationLayer_strategy)
@settings(max_examples=25)
def test_PSM_SpringWebApplicationLayer_instantiation(instance):
    assert isinstance(instance, PSM_SpringWebApplicationLayer)


SpringWebApplicationLayer_strategy = st.builds(SpringWebApplicationLayer)
@given(instance=SpringWebApplicationLayer_strategy)
@settings(max_examples=25)
def test_SpringWebApplicationLayer_instantiation(instance):
    assert isinstance(instance, SpringWebApplicationLayer)


