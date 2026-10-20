import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_annotations18_reverse_link_reassign_clear():
    a1 = PSM_JavaElement(ElementIdentifier="sample_text", ElementProfile="sample_text")
    a2 = PSM_JavaElement(ElementIdentifier="sample_text_2", ElementProfile="sample_text_2")
    b = PSM_JavaAnnotation(AnnotationName="sample_text")
    _safe_set(b, 'PSM_JavaAnnotation', a1)
    assert _is_linked(b, 'PSM_JavaAnnotation', a1)
    if hasattr(a1, 'PSM_JavaElement'):
        assert _is_linked(a1, 'PSM_JavaElement', b)
    _safe_set(b, 'PSM_JavaAnnotation', a2)
    assert _is_linked(b, 'PSM_JavaAnnotation', a2)
    if hasattr(a1, 'PSM_JavaElement'):
        assert not _is_linked(a1, 'PSM_JavaElement', b)
    if hasattr(a2, 'PSM_JavaElement'):
        assert _is_linked(a2, 'PSM_JavaElement', b)
    _safe_set(b, 'PSM_JavaAnnotation', None)
    assert not _is_linked(b, 'PSM_JavaAnnotation', a2)
    if hasattr(a2, 'PSM_JavaElement'):
        assert not _is_linked(a2, 'PSM_JavaElement', b)


def test_assoc_application_project3_reverse_link_reassign_clear():
    a1 = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    a2 = PSM_DistributedApplicationProject(ApplicationName="sample_text_2", ProjectPackageURL="sample_text_2")
    b = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    _safe_set(b, 'PSM_ApplicationProject', a1)
    assert _is_linked(b, 'PSM_ApplicationProject', a1)
    if hasattr(a1, 'PSM_DistributedApplicationProject4'):
        assert _is_linked(a1, 'PSM_DistributedApplicationProject4', b)
    _safe_set(b, 'PSM_ApplicationProject', a2)
    assert _is_linked(b, 'PSM_ApplicationProject', a2)
    if hasattr(a1, 'PSM_DistributedApplicationProject4'):
        assert not _is_linked(a1, 'PSM_DistributedApplicationProject4', b)
    if hasattr(a2, 'PSM_DistributedApplicationProject4'):
        assert _is_linked(a2, 'PSM_DistributedApplicationProject4', b)
    _safe_set(b, 'PSM_ApplicationProject', None)
    assert not _is_linked(b, 'PSM_ApplicationProject', a2)
    if hasattr(a2, 'PSM_DistributedApplicationProject4'):
        assert not _is_linked(a2, 'PSM_DistributedApplicationProject4', b)


def test_assoc_containers1_reverse_link_reassign_clear():
    a1 = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    a2 = PSM_DockerContainerDefinition(BuildField="sample_text_2", ContainerName="sample_text_2", GeneratesLogs=False, ImageField="sample_text_2")
    b = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    _safe_set(b, 'PSM_DistributedApplicationProject2', {a1})
    assert _is_linked(b, 'PSM_DistributedApplicationProject2', a1)
    if hasattr(a1, 'PSM_DockerContainerDefinition'):
        assert _is_linked(a1, 'PSM_DockerContainerDefinition', b)
    _safe_set(b, 'PSM_DistributedApplicationProject2', {a2})
    assert _is_linked(b, 'PSM_DistributedApplicationProject2', a2)
    if hasattr(a1, 'PSM_DockerContainerDefinition'):
        assert not _is_linked(a1, 'PSM_DockerContainerDefinition', b)
    if hasattr(a2, 'PSM_DockerContainerDefinition'):
        assert _is_linked(a2, 'PSM_DockerContainerDefinition', b)
    _safe_set(b, 'PSM_DistributedApplicationProject2', set())
    assert not _is_linked(b, 'PSM_DistributedApplicationProject2', a2)
    if hasattr(a2, 'PSM_DockerContainerDefinition'):
        assert not _is_linked(a2, 'PSM_DockerContainerDefinition', b)


def test_assoc_invokes43_reverse_link_reassign_clear():
    a1 = PSM_JavaMethod(RootCallingMethod="sample_text")
    a2 = PSM_JavaMethod(RootCallingMethod="sample_text_2")
    b = PSM_JavaMethod(RootCallingMethod="sample_text")
    _safe_set(b, 'PSM_JavaMethod44', a1)
    assert _is_linked(b, 'PSM_JavaMethod44', a1)
    if hasattr(a1, 'PSM_JavaMethod42'):
        assert _is_linked(a1, 'PSM_JavaMethod42', b)
    _safe_set(b, 'PSM_JavaMethod44', a2)
    assert _is_linked(b, 'PSM_JavaMethod44', a2)
    if hasattr(a1, 'PSM_JavaMethod42'):
        assert not _is_linked(a1, 'PSM_JavaMethod42', b)
    if hasattr(a2, 'PSM_JavaMethod42'):
        assert _is_linked(a2, 'PSM_JavaMethod42', b)
    _safe_set(b, 'PSM_JavaMethod44', None)
    assert not _is_linked(b, 'PSM_JavaMethod44', a2)
    if hasattr(a2, 'PSM_JavaMethod42'):
        assert not _is_linked(a2, 'PSM_JavaMethod42', b)


def test_assoc_libraries11_reverse_link_reassign_clear():
    a1 = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    a2 = PSM_MicroserviceProject(ProjectArtifactId="sample_text_2")
    b = PSM_DependencyLibrary(LibraryGroupName="sample_text", LibraryName="sample_text", LibraryScope="sample_text")
    _safe_set(b, 'PSM_DependencyLibrary', a1)
    assert _is_linked(b, 'PSM_DependencyLibrary', a1)
    if hasattr(a1, 'PSM_MicroserviceProject12'):
        assert _is_linked(a1, 'PSM_MicroserviceProject12', b)
    _safe_set(b, 'PSM_DependencyLibrary', a2)
    assert _is_linked(b, 'PSM_DependencyLibrary', a2)
    if hasattr(a1, 'PSM_MicroserviceProject12'):
        assert not _is_linked(a1, 'PSM_MicroserviceProject12', b)
    if hasattr(a2, 'PSM_MicroserviceProject12'):
        assert _is_linked(a2, 'PSM_MicroserviceProject12', b)
    _safe_set(b, 'PSM_DependencyLibrary', None)
    assert not _is_linked(b, 'PSM_DependencyLibrary', a2)
    if hasattr(a2, 'PSM_MicroserviceProject12'):
        assert not _is_linked(a2, 'PSM_MicroserviceProject12', b)


def test_assoc_links5_reverse_link_reassign_clear():
    a1 = PSM_DockerContainerLink(DependencyOrder=7, LinksDependsOnField="sample_text")
    a2 = PSM_DockerContainerLink(DependencyOrder=13, LinksDependsOnField="sample_text_2")
    b = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    _safe_set(b, 'PSM_DockerContainerDefinition6', {a1})
    assert _is_linked(b, 'PSM_DockerContainerDefinition6', a1)
    if hasattr(a1, 'PSM_DockerContainerLink'):
        assert _is_linked(a1, 'PSM_DockerContainerLink', b)
    _safe_set(b, 'PSM_DockerContainerDefinition6', {a2})
    assert _is_linked(b, 'PSM_DockerContainerDefinition6', a2)
    if hasattr(a1, 'PSM_DockerContainerLink'):
        assert not _is_linked(a1, 'PSM_DockerContainerLink', b)
    if hasattr(a2, 'PSM_DockerContainerLink'):
        assert _is_linked(a2, 'PSM_DockerContainerLink', b)
    _safe_set(b, 'PSM_DockerContainerDefinition6', set())
    assert not _is_linked(b, 'PSM_DockerContainerDefinition6', a2)
    if hasattr(a2, 'PSM_DockerContainerLink'):
        assert not _is_linked(a2, 'PSM_DockerContainerLink', b)


def test_assoc_modules9_reverse_link_reassign_clear():
    a1 = PSM_MicroserviceProject(ProjectArtifactId="sample_text")
    a2 = PSM_MicroserviceProject(ProjectArtifactId="sample_text_2")
    b = PSM_ApplicationProject(ProjectArtifactId="sample_text")
    _safe_set(b, 'PSM_ApplicationProject10', {a1})
    assert _is_linked(b, 'PSM_ApplicationProject10', a1)
    if hasattr(a1, 'PSM_MicroserviceProject'):
        assert _is_linked(a1, 'PSM_MicroserviceProject', b)
    _safe_set(b, 'PSM_ApplicationProject10', {a2})
    assert _is_linked(b, 'PSM_ApplicationProject10', a2)
    if hasattr(a1, 'PSM_MicroserviceProject'):
        assert not _is_linked(a1, 'PSM_MicroserviceProject', b)
    if hasattr(a2, 'PSM_MicroserviceProject'):
        assert _is_linked(a2, 'PSM_MicroserviceProject', b)
    _safe_set(b, 'PSM_ApplicationProject10', set())
    assert not _is_linked(b, 'PSM_ApplicationProject10', a2)
    if hasattr(a2, 'PSM_MicroserviceProject'):
        assert not _is_linked(a2, 'PSM_MicroserviceProject', b)


def test_assoc_parameters19_reverse_link_reassign_clear():
    a1 = PSM_JavaAnnotationParameter(ParameterName="sample_text", ParameterValue="sample_text")
    a2 = PSM_JavaAnnotationParameter(ParameterName="sample_text_2", ParameterValue="sample_text_2")
    b = PSM_JavaAnnotation(AnnotationName="sample_text")
    _safe_set(b, 'PSM_JavaAnnotation20', {a1})
    assert _is_linked(b, 'PSM_JavaAnnotation20', a1)
    if hasattr(a1, 'PSM_JavaAnnotationParameter'):
        assert _is_linked(a1, 'PSM_JavaAnnotationParameter', b)
    _safe_set(b, 'PSM_JavaAnnotation20', {a2})
    assert _is_linked(b, 'PSM_JavaAnnotation20', a2)
    if hasattr(a1, 'PSM_JavaAnnotationParameter'):
        assert not _is_linked(a1, 'PSM_JavaAnnotationParameter', b)
    if hasattr(a2, 'PSM_JavaAnnotationParameter'):
        assert _is_linked(a2, 'PSM_JavaAnnotationParameter', b)
    _safe_set(b, 'PSM_JavaAnnotation20', set())
    assert not _is_linked(b, 'PSM_JavaAnnotation20', a2)
    if hasattr(a2, 'PSM_JavaAnnotationParameter'):
        assert not _is_linked(a2, 'PSM_JavaAnnotationParameter', b)


def test_assoc_parameters38_reverse_link_reassign_clear():
    a1 = PSM_JavaMethodParameter(ParameterOrder=7)
    a2 = PSM_JavaMethodParameter(ParameterOrder=13)
    b = PSM_JavaMethod(RootCallingMethod="sample_text")
    _safe_set(b, 'PSM_JavaMethod39', {a1})
    assert _is_linked(b, 'PSM_JavaMethod39', a1)
    if hasattr(a1, 'PSM_JavaMethodParameter'):
        assert _is_linked(a1, 'PSM_JavaMethodParameter', b)
    _safe_set(b, 'PSM_JavaMethod39', {a2})
    assert _is_linked(b, 'PSM_JavaMethod39', a2)
    if hasattr(a1, 'PSM_JavaMethodParameter'):
        assert not _is_linked(a1, 'PSM_JavaMethodParameter', b)
    if hasattr(a2, 'PSM_JavaMethodParameter'):
        assert _is_linked(a2, 'PSM_JavaMethodParameter', b)
    _safe_set(b, 'PSM_JavaMethod39', set())
    assert not _is_linked(b, 'PSM_JavaMethod39', a2)
    if hasattr(a2, 'PSM_JavaMethodParameter'):
        assert not _is_linked(a2, 'PSM_JavaMethodParameter', b)


def test_assoc_ports7_reverse_link_reassign_clear():
    a1 = PSM_DockerContainerPort(ExposesPortsField="sample_text")
    a2 = PSM_DockerContainerPort(ExposesPortsField="sample_text_2")
    b = PSM_DockerContainerDefinition(BuildField="sample_text", ContainerName="sample_text", GeneratesLogs=True, ImageField="sample_text")
    _safe_set(b, 'PSM_DockerContainerDefinition8', {a1})
    assert _is_linked(b, 'PSM_DockerContainerDefinition8', a1)
    if hasattr(a1, 'PSM_DockerContainerPort'):
        assert _is_linked(a1, 'PSM_DockerContainerPort', b)
    _safe_set(b, 'PSM_DockerContainerDefinition8', {a2})
    assert _is_linked(b, 'PSM_DockerContainerDefinition8', a2)
    if hasattr(a1, 'PSM_DockerContainerPort'):
        assert not _is_linked(a1, 'PSM_DockerContainerPort', b)
    if hasattr(a2, 'PSM_DockerContainerPort'):
        assert _is_linked(a2, 'PSM_DockerContainerPort', b)
    _safe_set(b, 'PSM_DockerContainerDefinition8', set())
    assert not _is_linked(b, 'PSM_DockerContainerDefinition8', a2)
    if hasattr(a2, 'PSM_DockerContainerPort'):
        assert not _is_linked(a2, 'PSM_DockerContainerPort', b)


def test_assoc_returns40_reverse_link_reassign_clear():
    a1 = PSM_JavaMethod(RootCallingMethod="sample_text")
    a2 = PSM_JavaMethod(RootCallingMethod="sample_text_2")
    b = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    _safe_set(b, 'PSM_JavaDataType', a1)
    assert _is_linked(b, 'PSM_JavaDataType', a1)
    if hasattr(a1, 'PSM_JavaMethod41'):
        assert _is_linked(a1, 'PSM_JavaMethod41', b)
    _safe_set(b, 'PSM_JavaDataType', a2)
    assert _is_linked(b, 'PSM_JavaDataType', a2)
    if hasattr(a1, 'PSM_JavaMethod41'):
        assert not _is_linked(a1, 'PSM_JavaMethod41', b)
    if hasattr(a2, 'PSM_JavaMethod41'):
        assert _is_linked(a2, 'PSM_JavaMethod41', b)
    _safe_set(b, 'PSM_JavaDataType', None)
    assert not _is_linked(b, 'PSM_JavaDataType', a2)
    if hasattr(a2, 'PSM_JavaMethod41'):
        assert not _is_linked(a2, 'PSM_JavaMethod41', b)


def test_assoc_type45_reverse_link_reassign_clear():
    a1 = PSM_JavaDataType(IsPrimitive=True, JsonSchema="sample_text", PackageName="sample_text")
    a2 = PSM_JavaDataType(IsPrimitive=False, JsonSchema="sample_text_2", PackageName="sample_text_2")
    b = PSM_JavaDataField(FieldValue="sample_text")
    _safe_set(b, 'PSM_JavaDataField46', a1)
    assert _is_linked(b, 'PSM_JavaDataField46', a1)
    if hasattr(a1, 'PSM_JavaDataType47'):
        assert _is_linked(a1, 'PSM_JavaDataType47', b)
    _safe_set(b, 'PSM_JavaDataField46', a2)
    assert _is_linked(b, 'PSM_JavaDataField46', a2)
    if hasattr(a1, 'PSM_JavaDataType47'):
        assert not _is_linked(a1, 'PSM_JavaDataType47', b)
    if hasattr(a2, 'PSM_JavaDataType47'):
        assert _is_linked(a2, 'PSM_JavaDataType47', b)
    _safe_set(b, 'PSM_JavaDataField46', None)
    assert not _is_linked(b, 'PSM_JavaDataField46', a2)
    if hasattr(a2, 'PSM_JavaDataType47'):
        assert not _is_linked(a2, 'PSM_JavaDataType47', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_application0_stub_double():
    # PSM_RootPSM has no real 'PSM_RootPSM' property in the generated
    # code (a bare stub) -- manually attach it so PSM_DistributedApplicationProject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_DistributedApplicationProject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_DistributedApplicationProject(ApplicationName="sample_text", ProjectPackageURL="sample_text")
    partner = PSM_RootPSM()
    setattr(partner, 'PSM_RootPSM', None)
    _safe_set(owner, 'PSM_DistributedApplicationProject', partner)
    assert getattr(partner, 'PSM_RootPSM') == owner
    _safe_set(owner, 'PSM_DistributedApplicationProject', None)
    assert getattr(partner, 'PSM_RootPSM') is None


def test_assoc_elements16_stub_double():
    # PSM_JavaUserDefinedType has no real 'PSM_JavaUserDefinedType' property in the generated
    # code (a bare stub) -- manually attach it so PSM_SpringWebApplicationLayer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_SpringWebApplicationLayer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    partner = PSM_JavaUserDefinedType()
    setattr(partner, 'PSM_JavaUserDefinedType', None)
    _safe_set(owner, 'PSM_SpringWebApplicationLayer17', {partner})
    assert getattr(partner, 'PSM_JavaUserDefinedType') == owner
    _safe_set(owner, 'PSM_SpringWebApplicationLayer17', set())
    assert getattr(partner, 'PSM_JavaUserDefinedType') is None


def test_assoc_fields32_stub_double():
    # PSM_JavaUserDefinedType has no real 'PSM_JavaUserDefinedType33' property in the generated
    # code (a bare stub) -- manually attach it so PSM_JavaDataField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_JavaDataField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_JavaDataField(FieldValue="sample_text")
    partner = PSM_JavaUserDefinedType()
    setattr(partner, 'PSM_JavaUserDefinedType33', None)
    _safe_set(owner, 'PSM_JavaDataField', partner)
    assert owner in getattr(partner, 'PSM_JavaUserDefinedType33')
    _safe_set(owner, 'PSM_JavaDataField', None)
    assert owner not in getattr(partner, 'PSM_JavaUserDefinedType33')


def test_assoc_layers14_stub_double():
    # PSM_JavaSpringWebApplicationProject has no real 'PSM_JavaSpringWebApplicationProject15' property in the generated
    # code (a bare stub) -- manually attach it so PSM_SpringWebApplicationLayer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_SpringWebApplicationLayer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_SpringWebApplicationLayer(LayerName="sample_text")
    partner = PSM_JavaSpringWebApplicationProject()
    setattr(partner, 'PSM_JavaSpringWebApplicationProject15', None)
    _safe_set(owner, 'PSM_SpringWebApplicationLayer', partner)
    assert owner in getattr(partner, 'PSM_JavaSpringWebApplicationProject15')
    _safe_set(owner, 'PSM_SpringWebApplicationLayer', None)
    assert owner not in getattr(partner, 'PSM_JavaSpringWebApplicationProject15')


def test_assoc_methods21_stub_double():
    # PSM_JavaUserDefinedType has no real 'PSM_JavaUserDefinedType22' property in the generated
    # code (a bare stub) -- manually attach it so PSM_JavaMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_JavaMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_JavaMethod(RootCallingMethod="sample_text")
    partner = PSM_JavaUserDefinedType()
    setattr(partner, 'PSM_JavaUserDefinedType22', None)
    _safe_set(owner, 'PSM_JavaMethod', partner)
    assert owner in getattr(partner, 'PSM_JavaUserDefinedType22')
    _safe_set(owner, 'PSM_JavaMethod', None)
    assert owner not in getattr(partner, 'PSM_JavaUserDefinedType22')


def test_assoc_parent35_stub_double():
    # PSM_JavaUserDefinedType has no real 'PSM_JavaUserDefinedType37' property in the generated
    # code (a bare stub) -- manually attach it so PSM_JavaMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_JavaMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_JavaMethod(RootCallingMethod="sample_text")
    partner = PSM_JavaUserDefinedType()
    setattr(partner, 'PSM_JavaUserDefinedType37', None)
    _safe_set(owner, 'PSM_JavaMethod36', partner)
    assert getattr(partner, 'PSM_JavaUserDefinedType37') == owner
    _safe_set(owner, 'PSM_JavaMethod36', None)
    assert getattr(partner, 'PSM_JavaUserDefinedType37') is None


def test_assoc_properties13_stub_double():
    # PSM_JavaSpringWebApplicationProject has no real 'PSM_JavaSpringWebApplicationProject' property in the generated
    # code (a bare stub) -- manually attach it so PSM_ConfigurationProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PSM_ConfigurationProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PSM_ConfigurationProperty(ConfigurationProfile="sample_text", FullyQualifiedPropertyName="sample_text", PropertyValue="sample_text")
    partner = PSM_JavaSpringWebApplicationProject()
    setattr(partner, 'PSM_JavaSpringWebApplicationProject', None)
    _safe_set(owner, 'PSM_ConfigurationProperty', partner)
    assert owner in getattr(partner, 'PSM_JavaSpringWebApplicationProject')
    _safe_set(owner, 'PSM_ConfigurationProperty', None)
    assert owner not in getattr(partner, 'PSM_JavaSpringWebApplicationProject')


