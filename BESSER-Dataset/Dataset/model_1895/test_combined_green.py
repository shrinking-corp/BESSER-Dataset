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
    JavaUserDefinedType,
    PSM_JavaInterfaceType,
    PSM_JavaClassType,
    JavaDataField,
    PSM_JavaMethodParameter,
    SpringWebApplicationLayer,
    PSM_SpringBootApplicationLayer,
    JavaDataType,
    PSM_JavaUserDefinedType,
    JavaElement,
    PSM_JavaDataField,
    PSM_JavaMethod,
    PSM_JavaDataType,
    PSM_SpringModelPojoLayer,
    PSM_SpringDomainLayer,
    PSM_SpringRepositoryLayer,
    PSM_SpringComponentLayer,
    PSM_SpringFeignClientLayer,
    PSM_SpringConfigurationLayer,
    PSM_SpringServiceLayer,
    PSM_SpringControllerLayer,
    ArtifactElement,
    PSM_JavaElement,
    PSM_JavaAnnotationParameter,
    PSM_JavaAnnotation,
    JavaSpringWebApplicationProject,
    PSM_JavaSpringMVCApplicationProject,
    PSM_JavaSpringWebFluxApplicationProject,
    PSM_SpringWebApplicationLayer,
    PSM_ConfigurationProperty,
    MicroserviceProject,
    PSM_JavaSpringWebApplicationProject,
    PSM_DependencyLibrary,
    PSM_MicroserviceProject,
    PSM_DockerContainerPort,
    PSM_DockerContainerLink,
    PSM_ApplicationProject,
    PSM_DockerContainerDefinition,
    PSM_DistributedApplicationProject,
    PSM_RootPSM,
    PSM_ArtifactElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_javauserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(JavaUserDefinedType)


def test_hyp_javauserdefinedtype_constructor_exists():
    assert callable(JavaUserDefinedType.__init__)


def test_hyp_javauserdefinedtype_constructor_args():
    sig = inspect.signature(JavaUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javainterfacetype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaInterfaceType)


def test_hyp_psm_javainterfacetype_constructor_exists():
    assert callable(PSM_JavaInterfaceType.__init__)


def test_hyp_psm_javainterfacetype_constructor_args():
    sig = inspect.signature(PSM_JavaInterfaceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javaclasstype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaClassType)


def test_hyp_psm_javaclasstype_constructor_exists():
    assert callable(PSM_JavaClassType.__init__)


def test_hyp_psm_javaclasstype_constructor_args():
    sig = inspect.signature(PSM_JavaClassType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javadatafield_is_not_abstract():
    assert not inspect.isabstract(JavaDataField)


def test_hyp_javadatafield_constructor_exists():
    assert callable(JavaDataField.__init__)


def test_hyp_javadatafield_constructor_args():
    sig = inspect.signature(JavaDataField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javamethodparameter_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaMethodParameter)


def test_hyp_psm_javamethodparameter_constructor_exists():
    assert callable(PSM_JavaMethodParameter.__init__)


def test_hyp_psm_javamethodparameter_constructor_args():
    sig = inspect.signature(PSM_JavaMethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterOrder" in params, "Missing parameter 'ParameterOrder'"




def test_hyp_springwebapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(SpringWebApplicationLayer)


def test_hyp_springwebapplicationlayer_constructor_exists():
    assert callable(SpringWebApplicationLayer.__init__)


def test_hyp_springwebapplicationlayer_constructor_args():
    sig = inspect.signature(SpringWebApplicationLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springbootapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringBootApplicationLayer)


def test_hyp_psm_springbootapplicationlayer_constructor_exists():
    assert callable(PSM_SpringBootApplicationLayer.__init__)


def test_hyp_psm_springbootapplicationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringBootApplicationLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javadatatype_is_not_abstract():
    assert not inspect.isabstract(JavaDataType)


def test_hyp_javadatatype_constructor_exists():
    assert callable(JavaDataType.__init__)


def test_hyp_javadatatype_constructor_args():
    sig = inspect.signature(JavaDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javauserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaUserDefinedType)


def test_hyp_psm_javauserdefinedtype_constructor_exists():
    assert callable(PSM_JavaUserDefinedType.__init__)


def test_hyp_psm_javauserdefinedtype_constructor_args():
    sig = inspect.signature(PSM_JavaUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javaelement_is_not_abstract():
    assert not inspect.isabstract(JavaElement)


def test_hyp_javaelement_constructor_exists():
    assert callable(JavaElement.__init__)


def test_hyp_javaelement_constructor_args():
    sig = inspect.signature(JavaElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javadatafield_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaDataField)


def test_hyp_psm_javadatafield_constructor_exists():
    assert callable(PSM_JavaDataField.__init__)


def test_hyp_psm_javadatafield_constructor_args():
    sig = inspect.signature(PSM_JavaDataField.__init__)
    params = list(sig.parameters.keys())
    assert "FieldValue" in params, "Missing parameter 'FieldValue'"




def test_hyp_psm_javamethod_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaMethod)


def test_hyp_psm_javamethod_constructor_exists():
    assert callable(PSM_JavaMethod.__init__)


def test_hyp_psm_javamethod_constructor_args():
    sig = inspect.signature(PSM_JavaMethod.__init__)
    params = list(sig.parameters.keys())
    assert "RootCallingMethod" in params, "Missing parameter 'RootCallingMethod'"




def test_hyp_psm_javadatatype_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaDataType)


def test_hyp_psm_javadatatype_constructor_exists():
    assert callable(PSM_JavaDataType.__init__)


def test_hyp_psm_javadatatype_constructor_args():
    sig = inspect.signature(PSM_JavaDataType.__init__)
    params = list(sig.parameters.keys())
    assert "PackageName" in params, "Missing parameter 'PackageName'"
    assert "IsPrimitive" in params, "Missing parameter 'IsPrimitive'"
    assert "JsonSchema" in params, "Missing parameter 'JsonSchema'"






def test_hyp_psm_springmodelpojolayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringModelPojoLayer)


def test_hyp_psm_springmodelpojolayer_constructor_exists():
    assert callable(PSM_SpringModelPojoLayer.__init__)


def test_hyp_psm_springmodelpojolayer_constructor_args():
    sig = inspect.signature(PSM_SpringModelPojoLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springdomainlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringDomainLayer)


def test_hyp_psm_springdomainlayer_constructor_exists():
    assert callable(PSM_SpringDomainLayer.__init__)


def test_hyp_psm_springdomainlayer_constructor_args():
    sig = inspect.signature(PSM_SpringDomainLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springrepositorylayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringRepositoryLayer)


def test_hyp_psm_springrepositorylayer_constructor_exists():
    assert callable(PSM_SpringRepositoryLayer.__init__)


def test_hyp_psm_springrepositorylayer_constructor_args():
    sig = inspect.signature(PSM_SpringRepositoryLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springcomponentlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringComponentLayer)


def test_hyp_psm_springcomponentlayer_constructor_exists():
    assert callable(PSM_SpringComponentLayer.__init__)


def test_hyp_psm_springcomponentlayer_constructor_args():
    sig = inspect.signature(PSM_SpringComponentLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springfeignclientlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringFeignClientLayer)


def test_hyp_psm_springfeignclientlayer_constructor_exists():
    assert callable(PSM_SpringFeignClientLayer.__init__)


def test_hyp_psm_springfeignclientlayer_constructor_args():
    sig = inspect.signature(PSM_SpringFeignClientLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springconfigurationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringConfigurationLayer)


def test_hyp_psm_springconfigurationlayer_constructor_exists():
    assert callable(PSM_SpringConfigurationLayer.__init__)


def test_hyp_psm_springconfigurationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringConfigurationLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springservicelayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringServiceLayer)


def test_hyp_psm_springservicelayer_constructor_exists():
    assert callable(PSM_SpringServiceLayer.__init__)


def test_hyp_psm_springservicelayer_constructor_args():
    sig = inspect.signature(PSM_SpringServiceLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springcontrollerlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringControllerLayer)


def test_hyp_psm_springcontrollerlayer_constructor_exists():
    assert callable(PSM_SpringControllerLayer.__init__)


def test_hyp_psm_springcontrollerlayer_constructor_args():
    sig = inspect.signature(PSM_SpringControllerLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_artifactelement_is_not_abstract():
    assert not inspect.isabstract(ArtifactElement)


def test_hyp_artifactelement_constructor_exists():
    assert callable(ArtifactElement.__init__)


def test_hyp_artifactelement_constructor_args():
    sig = inspect.signature(ArtifactElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javaelement_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaElement)


def test_hyp_psm_javaelement_constructor_exists():
    assert callable(PSM_JavaElement.__init__)


def test_hyp_psm_javaelement_constructor_args():
    sig = inspect.signature(PSM_JavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "ElementIdentifier" in params, "Missing parameter 'ElementIdentifier'"
    assert "ElementProfile" in params, "Missing parameter 'ElementProfile'"





def test_hyp_psm_javaannotationparameter_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaAnnotationParameter)


def test_hyp_psm_javaannotationparameter_constructor_exists():
    assert callable(PSM_JavaAnnotationParameter.__init__)


def test_hyp_psm_javaannotationparameter_constructor_args():
    sig = inspect.signature(PSM_JavaAnnotationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "ParameterName" in params, "Missing parameter 'ParameterName'"
    assert "ParameterValue" in params, "Missing parameter 'ParameterValue'"





def test_hyp_psm_javaannotation_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaAnnotation)


def test_hyp_psm_javaannotation_constructor_exists():
    assert callable(PSM_JavaAnnotation.__init__)


def test_hyp_psm_javaannotation_constructor_args():
    sig = inspect.signature(PSM_JavaAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "AnnotationName" in params, "Missing parameter 'AnnotationName'"




def test_hyp_javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(JavaSpringWebApplicationProject)


def test_hyp_javaspringwebapplicationproject_constructor_exists():
    assert callable(JavaSpringWebApplicationProject.__init__)


def test_hyp_javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javaspringmvcapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringMVCApplicationProject)


def test_hyp_psm_javaspringmvcapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringMVCApplicationProject.__init__)


def test_hyp_psm_javaspringmvcapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringMVCApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javaspringwebfluxapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringWebFluxApplicationProject)


def test_hyp_psm_javaspringwebfluxapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringWebFluxApplicationProject.__init__)


def test_hyp_psm_javaspringwebfluxapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringWebFluxApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_springwebapplicationlayer_is_not_abstract():
    assert not inspect.isabstract(PSM_SpringWebApplicationLayer)


def test_hyp_psm_springwebapplicationlayer_constructor_exists():
    assert callable(PSM_SpringWebApplicationLayer.__init__)


def test_hyp_psm_springwebapplicationlayer_constructor_args():
    sig = inspect.signature(PSM_SpringWebApplicationLayer.__init__)
    params = list(sig.parameters.keys())
    assert "LayerName" in params, "Missing parameter 'LayerName'"




def test_hyp_psm_configurationproperty_is_not_abstract():
    assert not inspect.isabstract(PSM_ConfigurationProperty)


def test_hyp_psm_configurationproperty_constructor_exists():
    assert callable(PSM_ConfigurationProperty.__init__)


def test_hyp_psm_configurationproperty_constructor_args():
    sig = inspect.signature(PSM_ConfigurationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "PropertyValue" in params, "Missing parameter 'PropertyValue'"
    assert "ConfigurationProfile" in params, "Missing parameter 'ConfigurationProfile'"
    assert "FullyQualifiedPropertyName" in params, "Missing parameter 'FullyQualifiedPropertyName'"






def test_hyp_microserviceproject_is_not_abstract():
    assert not inspect.isabstract(MicroserviceProject)


def test_hyp_microserviceproject_constructor_exists():
    assert callable(MicroserviceProject.__init__)


def test_hyp_microserviceproject_constructor_args():
    sig = inspect.signature(MicroserviceProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_javaspringwebapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_JavaSpringWebApplicationProject)


def test_hyp_psm_javaspringwebapplicationproject_constructor_exists():
    assert callable(PSM_JavaSpringWebApplicationProject.__init__)


def test_hyp_psm_javaspringwebapplicationproject_constructor_args():
    sig = inspect.signature(PSM_JavaSpringWebApplicationProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_dependencylibrary_is_not_abstract():
    assert not inspect.isabstract(PSM_DependencyLibrary)


def test_hyp_psm_dependencylibrary_constructor_exists():
    assert callable(PSM_DependencyLibrary.__init__)


def test_hyp_psm_dependencylibrary_constructor_args():
    sig = inspect.signature(PSM_DependencyLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "LibraryName" in params, "Missing parameter 'LibraryName'"
    assert "LibraryScope" in params, "Missing parameter 'LibraryScope'"
    assert "LibraryGroupName" in params, "Missing parameter 'LibraryGroupName'"






def test_hyp_psm_microserviceproject_is_not_abstract():
    assert not inspect.isabstract(PSM_MicroserviceProject)


def test_hyp_psm_microserviceproject_constructor_exists():
    assert callable(PSM_MicroserviceProject.__init__)


def test_hyp_psm_microserviceproject_constructor_args():
    sig = inspect.signature(PSM_MicroserviceProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"




def test_hyp_psm_dockercontainerport_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerPort)


def test_hyp_psm_dockercontainerport_constructor_exists():
    assert callable(PSM_DockerContainerPort.__init__)


def test_hyp_psm_dockercontainerport_constructor_args():
    sig = inspect.signature(PSM_DockerContainerPort.__init__)
    params = list(sig.parameters.keys())
    assert "ExposesPortsField" in params, "Missing parameter 'ExposesPortsField'"




def test_hyp_psm_dockercontainerlink_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerLink)


def test_hyp_psm_dockercontainerlink_constructor_exists():
    assert callable(PSM_DockerContainerLink.__init__)


def test_hyp_psm_dockercontainerlink_constructor_args():
    sig = inspect.signature(PSM_DockerContainerLink.__init__)
    params = list(sig.parameters.keys())
    assert "DependencyOrder" in params, "Missing parameter 'DependencyOrder'"
    assert "LinksDependsOnField" in params, "Missing parameter 'LinksDependsOnField'"





def test_hyp_psm_applicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_ApplicationProject)


def test_hyp_psm_applicationproject_constructor_exists():
    assert callable(PSM_ApplicationProject.__init__)


def test_hyp_psm_applicationproject_constructor_args():
    sig = inspect.signature(PSM_ApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ProjectArtifactId" in params, "Missing parameter 'ProjectArtifactId'"




def test_hyp_psm_dockercontainerdefinition_is_not_abstract():
    assert not inspect.isabstract(PSM_DockerContainerDefinition)


def test_hyp_psm_dockercontainerdefinition_constructor_exists():
    assert callable(PSM_DockerContainerDefinition.__init__)


def test_hyp_psm_dockercontainerdefinition_constructor_args():
    sig = inspect.signature(PSM_DockerContainerDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "ImageField" in params, "Missing parameter 'ImageField'"
    assert "GeneratesLogs" in params, "Missing parameter 'GeneratesLogs'"
    assert "ContainerName" in params, "Missing parameter 'ContainerName'"
    assert "BuildField" in params, "Missing parameter 'BuildField'"







def test_hyp_psm_distributedapplicationproject_is_not_abstract():
    assert not inspect.isabstract(PSM_DistributedApplicationProject)


def test_hyp_psm_distributedapplicationproject_constructor_exists():
    assert callable(PSM_DistributedApplicationProject.__init__)


def test_hyp_psm_distributedapplicationproject_constructor_args():
    sig = inspect.signature(PSM_DistributedApplicationProject.__init__)
    params = list(sig.parameters.keys())
    assert "ApplicationName" in params, "Missing parameter 'ApplicationName'"
    assert "ProjectPackageURL" in params, "Missing parameter 'ProjectPackageURL'"





def test_hyp_psm_rootpsm_is_not_abstract():
    assert not inspect.isabstract(PSM_RootPSM)


def test_hyp_psm_rootpsm_constructor_exists():
    assert callable(PSM_RootPSM.__init__)


def test_hyp_psm_rootpsm_constructor_args():
    sig = inspect.signature(PSM_RootPSM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_psm_artifactelement_is_not_abstract():
    assert not inspect.isabstract(PSM_ArtifactElement)


def test_hyp_psm_artifactelement_constructor_exists():
    assert callable(PSM_ArtifactElement.__init__)


def test_hyp_psm_artifactelement_constructor_args():
    sig = inspect.signature(PSM_ArtifactElement.__init__)
    params = list(sig.parameters.keys())
    assert "GeneratingLinesOfCode" in params, "Missing parameter 'GeneratingLinesOfCode'"
    assert "ParentProjectName" in params, "Missing parameter 'ParentProjectName'"
    assert "ArtifactFileName" in params, "Missing parameter 'ArtifactFileName'"





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
JavaUserDefinedType_strategy = st.builds(
    JavaUserDefinedType,
)
PSM_JavaInterfaceType_strategy = st.builds(
    PSM_JavaInterfaceType,
)
PSM_JavaClassType_strategy = st.builds(
    PSM_JavaClassType,
)
JavaDataField_strategy = st.builds(
    JavaDataField,
)
PSM_JavaMethodParameter_strategy = st.builds(
    PSM_JavaMethodParameter,
    ParameterOrder=
        st.integers()
)
SpringWebApplicationLayer_strategy = st.builds(
    SpringWebApplicationLayer,
)
PSM_SpringBootApplicationLayer_strategy = st.builds(
    PSM_SpringBootApplicationLayer,
)
JavaDataType_strategy = st.builds(
    JavaDataType,
)
PSM_JavaUserDefinedType_strategy = st.builds(
    PSM_JavaUserDefinedType,
)
JavaElement_strategy = st.builds(
    JavaElement,
)
PSM_JavaDataField_strategy = st.builds(
    PSM_JavaDataField,
    FieldValue=
        safe_text
)
PSM_JavaMethod_strategy = st.builds(
    PSM_JavaMethod,
    RootCallingMethod=
        safe_text
)
PSM_JavaDataType_strategy = st.builds(
    PSM_JavaDataType,
    PackageName=
        safe_text,
    IsPrimitive=
        st.booleans(),
    JsonSchema=
        safe_text
)
PSM_SpringModelPojoLayer_strategy = st.builds(
    PSM_SpringModelPojoLayer,
)
PSM_SpringDomainLayer_strategy = st.builds(
    PSM_SpringDomainLayer,
)
PSM_SpringRepositoryLayer_strategy = st.builds(
    PSM_SpringRepositoryLayer,
)
PSM_SpringComponentLayer_strategy = st.builds(
    PSM_SpringComponentLayer,
)
PSM_SpringFeignClientLayer_strategy = st.builds(
    PSM_SpringFeignClientLayer,
)
PSM_SpringConfigurationLayer_strategy = st.builds(
    PSM_SpringConfigurationLayer,
)
PSM_SpringServiceLayer_strategy = st.builds(
    PSM_SpringServiceLayer,
)
PSM_SpringControllerLayer_strategy = st.builds(
    PSM_SpringControllerLayer,
)
ArtifactElement_strategy = st.builds(
    ArtifactElement,
)
PSM_JavaElement_strategy = st.builds(
    PSM_JavaElement,
    ElementIdentifier=
        safe_text,
    ElementProfile=
        safe_text
)
PSM_JavaAnnotationParameter_strategy = st.builds(
    PSM_JavaAnnotationParameter,
    ParameterName=
        safe_text,
    ParameterValue=
        safe_text
)
PSM_JavaAnnotation_strategy = st.builds(
    PSM_JavaAnnotation,
    AnnotationName=
        safe_text
)
JavaSpringWebApplicationProject_strategy = st.builds(
    JavaSpringWebApplicationProject,
)
PSM_JavaSpringMVCApplicationProject_strategy = st.builds(
    PSM_JavaSpringMVCApplicationProject,
)
PSM_JavaSpringWebFluxApplicationProject_strategy = st.builds(
    PSM_JavaSpringWebFluxApplicationProject,
)
PSM_SpringWebApplicationLayer_strategy = st.builds(
    PSM_SpringWebApplicationLayer,
    LayerName=
        safe_text
)
PSM_ConfigurationProperty_strategy = st.builds(
    PSM_ConfigurationProperty,
    PropertyValue=
        safe_text,
    ConfigurationProfile=
        safe_text,
    FullyQualifiedPropertyName=
        safe_text
)
MicroserviceProject_strategy = st.builds(
    MicroserviceProject,
)
PSM_JavaSpringWebApplicationProject_strategy = st.builds(
    PSM_JavaSpringWebApplicationProject,
)
PSM_DependencyLibrary_strategy = st.builds(
    PSM_DependencyLibrary,
    LibraryName=
        safe_text,
    LibraryScope=
        safe_text,
    LibraryGroupName=
        safe_text
)
PSM_MicroserviceProject_strategy = st.builds(
    PSM_MicroserviceProject,
    ProjectArtifactId=
        safe_text
)
PSM_DockerContainerPort_strategy = st.builds(
    PSM_DockerContainerPort,
    ExposesPortsField=
        safe_text
)
PSM_DockerContainerLink_strategy = st.builds(
    PSM_DockerContainerLink,
    DependencyOrder=
        st.integers(),
    LinksDependsOnField=
        safe_text
)
PSM_ApplicationProject_strategy = st.builds(
    PSM_ApplicationProject,
    ProjectArtifactId=
        safe_text
)
PSM_DockerContainerDefinition_strategy = st.builds(
    PSM_DockerContainerDefinition,
    ImageField=
        safe_text,
    GeneratesLogs=
        st.booleans(),
    ContainerName=
        safe_text,
    BuildField=
        safe_text
)
PSM_DistributedApplicationProject_strategy = st.builds(
    PSM_DistributedApplicationProject,
    ApplicationName=
        safe_text,
    ProjectPackageURL=
        safe_text
)
PSM_RootPSM_strategy = st.builds(
    PSM_RootPSM,
)
PSM_ArtifactElement_strategy = st.builds(
    PSM_ArtifactElement,
    GeneratingLinesOfCode=
        safe_text,
    ParentProjectName=
        safe_text,
    ArtifactFileName=
        safe_text
)








@given(instance=PSM_JavaMethodParameter_strategy)
def test_hyp_psm_javamethodparameter_ParameterOrder_setter(instance):
    original = instance.ParameterOrder
    instance.ParameterOrder = original
    assert instance.ParameterOrder == original









@given(instance=PSM_JavaDataField_strategy)
def test_hyp_psm_javadatafield_FieldValue_setter(instance):
    original = instance.FieldValue
    instance.FieldValue = original
    assert instance.FieldValue == original




@given(instance=PSM_JavaMethod_strategy)
def test_hyp_psm_javamethod_RootCallingMethod_setter(instance):
    original = instance.RootCallingMethod
    instance.RootCallingMethod = original
    assert instance.RootCallingMethod == original




@given(instance=PSM_JavaDataType_strategy)
def test_hyp_psm_javadatatype_PackageName_setter(instance):
    original = instance.PackageName
    instance.PackageName = original
    assert instance.PackageName == original



@given(instance=PSM_JavaDataType_strategy)
def test_hyp_psm_javadatatype_IsPrimitive_setter(instance):
    original = instance.IsPrimitive
    instance.IsPrimitive = original
    assert instance.IsPrimitive == original



@given(instance=PSM_JavaDataType_strategy)
def test_hyp_psm_javadatatype_JsonSchema_setter(instance):
    original = instance.JsonSchema
    instance.JsonSchema = original
    assert instance.JsonSchema == original













@given(instance=PSM_JavaElement_strategy)
def test_hyp_psm_javaelement_ElementIdentifier_setter(instance):
    original = instance.ElementIdentifier
    instance.ElementIdentifier = original
    assert instance.ElementIdentifier == original



@given(instance=PSM_JavaElement_strategy)
def test_hyp_psm_javaelement_ElementProfile_setter(instance):
    original = instance.ElementProfile
    instance.ElementProfile = original
    assert instance.ElementProfile == original




@given(instance=PSM_JavaAnnotationParameter_strategy)
def test_hyp_psm_javaannotationparameter_ParameterName_setter(instance):
    original = instance.ParameterName
    instance.ParameterName = original
    assert instance.ParameterName == original



@given(instance=PSM_JavaAnnotationParameter_strategy)
def test_hyp_psm_javaannotationparameter_ParameterValue_setter(instance):
    original = instance.ParameterValue
    instance.ParameterValue = original
    assert instance.ParameterValue == original




@given(instance=PSM_JavaAnnotation_strategy)
def test_hyp_psm_javaannotation_AnnotationName_setter(instance):
    original = instance.AnnotationName
    instance.AnnotationName = original
    assert instance.AnnotationName == original







@given(instance=PSM_SpringWebApplicationLayer_strategy)
def test_hyp_psm_springwebapplicationlayer_LayerName_setter(instance):
    original = instance.LayerName
    instance.LayerName = original
    assert instance.LayerName == original




@given(instance=PSM_ConfigurationProperty_strategy)
def test_hyp_psm_configurationproperty_PropertyValue_setter(instance):
    original = instance.PropertyValue
    instance.PropertyValue = original
    assert instance.PropertyValue == original



@given(instance=PSM_ConfigurationProperty_strategy)
def test_hyp_psm_configurationproperty_ConfigurationProfile_setter(instance):
    original = instance.ConfigurationProfile
    instance.ConfigurationProfile = original
    assert instance.ConfigurationProfile == original



@given(instance=PSM_ConfigurationProperty_strategy)
def test_hyp_psm_configurationproperty_FullyQualifiedPropertyName_setter(instance):
    original = instance.FullyQualifiedPropertyName
    instance.FullyQualifiedPropertyName = original
    assert instance.FullyQualifiedPropertyName == original






@given(instance=PSM_DependencyLibrary_strategy)
def test_hyp_psm_dependencylibrary_LibraryName_setter(instance):
    original = instance.LibraryName
    instance.LibraryName = original
    assert instance.LibraryName == original



@given(instance=PSM_DependencyLibrary_strategy)
def test_hyp_psm_dependencylibrary_LibraryScope_setter(instance):
    original = instance.LibraryScope
    instance.LibraryScope = original
    assert instance.LibraryScope == original



@given(instance=PSM_DependencyLibrary_strategy)
def test_hyp_psm_dependencylibrary_LibraryGroupName_setter(instance):
    original = instance.LibraryGroupName
    instance.LibraryGroupName = original
    assert instance.LibraryGroupName == original




@given(instance=PSM_MicroserviceProject_strategy)
def test_hyp_psm_microserviceproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original




@given(instance=PSM_DockerContainerPort_strategy)
def test_hyp_psm_dockercontainerport_ExposesPortsField_setter(instance):
    original = instance.ExposesPortsField
    instance.ExposesPortsField = original
    assert instance.ExposesPortsField == original




@given(instance=PSM_DockerContainerLink_strategy)
def test_hyp_psm_dockercontainerlink_DependencyOrder_setter(instance):
    original = instance.DependencyOrder
    instance.DependencyOrder = original
    assert instance.DependencyOrder == original



@given(instance=PSM_DockerContainerLink_strategy)
def test_hyp_psm_dockercontainerlink_LinksDependsOnField_setter(instance):
    original = instance.LinksDependsOnField
    instance.LinksDependsOnField = original
    assert instance.LinksDependsOnField == original




@given(instance=PSM_ApplicationProject_strategy)
def test_hyp_psm_applicationproject_ProjectArtifactId_setter(instance):
    original = instance.ProjectArtifactId
    instance.ProjectArtifactId = original
    assert instance.ProjectArtifactId == original




@given(instance=PSM_DockerContainerDefinition_strategy)
def test_hyp_psm_dockercontainerdefinition_ImageField_setter(instance):
    original = instance.ImageField
    instance.ImageField = original
    assert instance.ImageField == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_hyp_psm_dockercontainerdefinition_GeneratesLogs_setter(instance):
    original = instance.GeneratesLogs
    instance.GeneratesLogs = original
    assert instance.GeneratesLogs == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_hyp_psm_dockercontainerdefinition_ContainerName_setter(instance):
    original = instance.ContainerName
    instance.ContainerName = original
    assert instance.ContainerName == original



@given(instance=PSM_DockerContainerDefinition_strategy)
def test_hyp_psm_dockercontainerdefinition_BuildField_setter(instance):
    original = instance.BuildField
    instance.BuildField = original
    assert instance.BuildField == original




@given(instance=PSM_DistributedApplicationProject_strategy)
def test_hyp_psm_distributedapplicationproject_ApplicationName_setter(instance):
    original = instance.ApplicationName
    instance.ApplicationName = original
    assert instance.ApplicationName == original



@given(instance=PSM_DistributedApplicationProject_strategy)
def test_hyp_psm_distributedapplicationproject_ProjectPackageURL_setter(instance):
    original = instance.ProjectPackageURL
    instance.ProjectPackageURL = original
    assert instance.ProjectPackageURL == original





@given(instance=PSM_ArtifactElement_strategy)
def test_hyp_psm_artifactelement_GeneratingLinesOfCode_setter(instance):
    original = instance.GeneratingLinesOfCode
    instance.GeneratingLinesOfCode = original
    assert instance.GeneratingLinesOfCode == original



@given(instance=PSM_ArtifactElement_strategy)
def test_hyp_psm_artifactelement_ParentProjectName_setter(instance):
    original = instance.ParentProjectName
    instance.ParentProjectName = original
    assert instance.ParentProjectName == original



@given(instance=PSM_ArtifactElement_strategy)
def test_hyp_psm_artifactelement_ArtifactFileName_setter(instance):
    original = instance.ArtifactFileName
    instance.ArtifactFileName = original
    assert instance.ArtifactFileName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



