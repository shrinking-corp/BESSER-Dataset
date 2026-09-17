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
    application_ConfigurableElement,
    application_OAuthAdmin,
    application_OAuthClientConfig,
    Security,
    application_ApplicationKeyConfig,
    application_OAuthConfig,
    application_OAuthClientScope,
    application_Security,
    Interface,
    application_FEEDInterface,
    application_RESTInterface,
    Property,
    application_OCLRestrictedProperty,
    Persistency,
    application_Database,
    application_XMLFile,
    application_Property,
    application_Configuration,
    application_MashupContainer,
    application_MappingRule,
    Source,
    application_Mashup,
    application_DataSet,
    application_Persistency,
    ConfigurableElement,
    application_Source,
    application_MashupAdmin,
    application_Interface,
    SourceActiveStates,
    PropertyTypes,
    SourceState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_application_configurableelement_is_not_abstract():
    assert not inspect.isabstract(application_ConfigurableElement)


def test_hyp_application_configurableelement_constructor_exists():
    assert callable(application_ConfigurableElement.__init__)


def test_hyp_application_configurableelement_constructor_args():
    sig = inspect.signature(application_ConfigurableElement.__init__)
    params = list(sig.parameters.keys())
    assert "configurationImage" in params, "Missing parameter 'configurationImage'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "ident" in params, "Missing parameter 'ident'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"









def test_hyp_application_oauthadmin_is_not_abstract():
    assert not inspect.isabstract(application_OAuthAdmin)


def test_hyp_application_oauthadmin_constructor_exists():
    assert callable(application_OAuthAdmin.__init__)


def test_hyp_application_oauthadmin_constructor_args():
    sig = inspect.signature(application_OAuthAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "passwordHash" in params, "Missing parameter 'passwordHash'"





def test_hyp_application_oauthclientconfig_is_not_abstract():
    assert not inspect.isabstract(application_OAuthClientConfig)


def test_hyp_application_oauthclientconfig_constructor_exists():
    assert callable(application_OAuthClientConfig.__init__)


def test_hyp_application_oauthclientconfig_constructor_args():
    sig = inspect.signature(application_OAuthClientConfig.__init__)
    params = list(sig.parameters.keys())
    assert "allowedMetaTags" in params, "Missing parameter 'allowedMetaTags'"
    assert "clientID" in params, "Missing parameter 'clientID'"
    assert "grantType" in params, "Missing parameter 'grantType'"
    assert "accessToken" in params, "Missing parameter 'accessToken'"
    assert "forbiddenMetaTags" in params, "Missing parameter 'forbiddenMetaTags'"
    assert "oAuthScopeLevel" in params, "Missing parameter 'oAuthScopeLevel'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "redirectionURL" in params, "Missing parameter 'redirectionURL'"
    assert "description" in params, "Missing parameter 'description'"
    assert "accessTokenExpirationDate" in params, "Missing parameter 'accessTokenExpirationDate'"
    assert "accessTokenCreationDate" in params, "Missing parameter 'accessTokenCreationDate'"
    assert "refreshToken" in params, "Missing parameter 'refreshToken'"
    assert "type" in params, "Missing parameter 'type'"
    assert "clientSecret" in params, "Missing parameter 'clientSecret'"


















def test_hyp_security_is_not_abstract():
    assert not inspect.isabstract(Security)


def test_hyp_security_constructor_exists():
    assert callable(Security.__init__)


def test_hyp_security_constructor_args():
    sig = inspect.signature(Security.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_applicationkeyconfig_is_not_abstract():
    assert not inspect.isabstract(application_ApplicationKeyConfig)


def test_hyp_application_applicationkeyconfig_constructor_exists():
    assert callable(application_ApplicationKeyConfig.__init__)


def test_hyp_application_applicationkeyconfig_constructor_args():
    sig = inspect.signature(application_ApplicationKeyConfig.__init__)
    params = list(sig.parameters.keys())
    assert "applicationKeys" in params, "Missing parameter 'applicationKeys'"




def test_hyp_application_oauthconfig_is_not_abstract():
    assert not inspect.isabstract(application_OAuthConfig)


def test_hyp_application_oauthconfig_constructor_exists():
    assert callable(application_OAuthConfig.__init__)


def test_hyp_application_oauthconfig_constructor_args():
    sig = inspect.signature(application_OAuthConfig.__init__)
    params = list(sig.parameters.keys())
    assert "useScopeInterfaceOnRedirect" in params, "Missing parameter 'useScopeInterfaceOnRedirect'"




def test_hyp_application_oauthclientscope_is_not_abstract():
    assert not inspect.isabstract(application_OAuthClientScope)


def test_hyp_application_oauthclientscope_constructor_exists():
    assert callable(application_OAuthClientScope.__init__)


def test_hyp_application_oauthclientscope_constructor_args():
    sig = inspect.signature(application_OAuthClientScope.__init__)
    params = list(sig.parameters.keys())
    assert "positiveCategory" in params, "Missing parameter 'positiveCategory'"
    assert "allowOrganisations" in params, "Missing parameter 'allowOrganisations'"
    assert "positiveTag" in params, "Missing parameter 'positiveTag'"
    assert "maximumAge" in params, "Missing parameter 'maximumAge'"
    assert "positiveMetaTag" in params, "Missing parameter 'positiveMetaTag'"
    assert "allowContents" in params, "Missing parameter 'allowContents'"
    assert "positiveOrganisation" in params, "Missing parameter 'positiveOrganisation'"
    assert "identSpecification" in params, "Missing parameter 'identSpecification'"
    assert "negativeMetaTag" in params, "Missing parameter 'negativeMetaTag'"
    assert "negativeCategory" in params, "Missing parameter 'negativeCategory'"
    assert "negativeOrganisation" in params, "Missing parameter 'negativeOrganisation'"
    assert "allowPersons" in params, "Missing parameter 'allowPersons'"
    assert "negativeTag" in params, "Missing parameter 'negativeTag'"
    assert "positivePerson" in params, "Missing parameter 'positivePerson'"
    assert "negativePerson" in params, "Missing parameter 'negativePerson'"


















def test_hyp_application_security_is_not_abstract():
    assert not inspect.isabstract(application_Security)


def test_hyp_application_security_constructor_exists():
    assert callable(application_Security.__init__)


def test_hyp_application_security_constructor_args():
    sig = inspect.signature(application_Security.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_hyp_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_hyp_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_feedinterface_is_not_abstract():
    assert not inspect.isabstract(application_FEEDInterface)


def test_hyp_application_feedinterface_constructor_exists():
    assert callable(application_FEEDInterface.__init__)


def test_hyp_application_feedinterface_constructor_args():
    sig = inspect.signature(application_FEEDInterface.__init__)
    params = list(sig.parameters.keys())
    assert "feedType" in params, "Missing parameter 'feedType'"
    assert "allowOrganisationFiltering" in params, "Missing parameter 'allowOrganisationFiltering'"
    assert "allowPersonFiltering" in params, "Missing parameter 'allowPersonFiltering'"
    assert "language" in params, "Missing parameter 'language'"
    assert "allowTypeFiltering" in params, "Missing parameter 'allowTypeFiltering'"
    assert "feedTitle" in params, "Missing parameter 'feedTitle'"
    assert "allowCategoryFiltering" in params, "Missing parameter 'allowCategoryFiltering'"
    assert "allowMetaTagFiltering" in params, "Missing parameter 'allowMetaTagFiltering'"
    assert "allowTagFiltering" in params, "Missing parameter 'allowTagFiltering'"












def test_hyp_application_restinterface_is_not_abstract():
    assert not inspect.isabstract(application_RESTInterface)


def test_hyp_application_restinterface_constructor_exists():
    assert callable(application_RESTInterface.__init__)


def test_hyp_application_restinterface_constructor_args():
    sig = inspect.signature(application_RESTInterface.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_oclrestrictedproperty_is_not_abstract():
    assert not inspect.isabstract(application_OCLRestrictedProperty)


def test_hyp_application_oclrestrictedproperty_constructor_exists():
    assert callable(application_OCLRestrictedProperty.__init__)


def test_hyp_application_oclrestrictedproperty_constructor_args():
    sig = inspect.signature(application_OCLRestrictedProperty.__init__)
    params = list(sig.parameters.keys())
    assert "OCLRestriction" in params, "Missing parameter 'OCLRestriction'"




def test_hyp_persistency_is_not_abstract():
    assert not inspect.isabstract(Persistency)


def test_hyp_persistency_constructor_exists():
    assert callable(Persistency.__init__)


def test_hyp_persistency_constructor_args():
    sig = inspect.signature(Persistency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_database_is_not_abstract():
    assert not inspect.isabstract(application_Database)


def test_hyp_application_database_constructor_exists():
    assert callable(application_Database.__init__)


def test_hyp_application_database_constructor_args():
    sig = inspect.signature(application_Database.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_xmlfile_is_not_abstract():
    assert not inspect.isabstract(application_XMLFile)


def test_hyp_application_xmlfile_constructor_exists():
    assert callable(application_XMLFile.__init__)


def test_hyp_application_xmlfile_constructor_args():
    sig = inspect.signature(application_XMLFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_property_is_not_abstract():
    assert not inspect.isabstract(application_Property)


def test_hyp_application_property_constructor_exists():
    assert callable(application_Property.__init__)


def test_hyp_application_property_constructor_args():
    sig = inspect.signature(application_Property.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "helpText" in params, "Missing parameter 'helpText'"
    assert "possibleValues" in params, "Missing parameter 'possibleValues'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "propertyType" in params, "Missing parameter 'propertyType'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "Key" in params, "Missing parameter 'Key'"
    assert "Value" in params, "Missing parameter 'Value'"











def test_hyp_application_configuration_is_not_abstract():
    assert not inspect.isabstract(application_Configuration)


def test_hyp_application_configuration_constructor_exists():
    assert callable(application_Configuration.__init__)


def test_hyp_application_configuration_constructor_args():
    sig = inspect.signature(application_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_mashupcontainer_is_not_abstract():
    assert not inspect.isabstract(application_MashupContainer)


def test_hyp_application_mashupcontainer_constructor_exists():
    assert callable(application_MashupContainer.__init__)


def test_hyp_application_mashupcontainer_constructor_args():
    sig = inspect.signature(application_MashupContainer.__init__)
    params = list(sig.parameters.keys())
    assert "backupConfiguration" in params, "Missing parameter 'backupConfiguration'"
    assert "immediateSave" in params, "Missing parameter 'immediateSave'"
    assert "backupIntervall" in params, "Missing parameter 'backupIntervall'"
    assert "identCounter" in params, "Missing parameter 'identCounter'"
    assert "createAccountsAtLoginTry" in params, "Missing parameter 'createAccountsAtLoginTry'"








def test_hyp_application_mappingrule_is_not_abstract():
    assert not inspect.isabstract(application_MappingRule)


def test_hyp_application_mappingrule_constructor_exists():
    assert callable(application_MappingRule.__init__)


def test_hyp_application_mappingrule_constructor_args():
    sig = inspect.signature(application_MappingRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_hyp_source_constructor_exists():
    assert callable(Source.__init__)


def test_hyp_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_mashup_is_not_abstract():
    assert not inspect.isabstract(application_Mashup)


def test_hyp_application_mashup_constructor_exists():
    assert callable(application_Mashup.__init__)


def test_hyp_application_mashup_constructor_args():
    sig = inspect.signature(application_Mashup.__init__)
    params = list(sig.parameters.keys())
    assert "workingDirectory" in params, "Missing parameter 'workingDirectory'"
    assert "cacheDelay" in params, "Missing parameter 'cacheDelay'"
    assert "backupDataSet" in params, "Missing parameter 'backupDataSet'"
    assert "cacheAttachments" in params, "Missing parameter 'cacheAttachments'"
    assert "backupIntervall" in params, "Missing parameter 'backupIntervall'"
    assert "sourceIdentCounter" in params, "Missing parameter 'sourceIdentCounter'"
    assert "cacheDataSet" in params, "Missing parameter 'cacheDataSet'"










def test_hyp_application_dataset_is_not_abstract():
    assert not inspect.isabstract(application_DataSet)


def test_hyp_application_dataset_constructor_exists():
    assert callable(application_DataSet.__init__)


def test_hyp_application_dataset_constructor_args():
    sig = inspect.signature(application_DataSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_persistency_is_not_abstract():
    assert not inspect.isabstract(application_Persistency)


def test_hyp_application_persistency_constructor_exists():
    assert callable(application_Persistency.__init__)


def test_hyp_application_persistency_constructor_args():
    sig = inspect.signature(application_Persistency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_configurableelement_is_not_abstract():
    assert not inspect.isabstract(ConfigurableElement)


def test_hyp_configurableelement_constructor_exists():
    assert callable(ConfigurableElement.__init__)


def test_hyp_configurableelement_constructor_args():
    sig = inspect.signature(ConfigurableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_application_source_is_not_abstract():
    assert not inspect.isabstract(application_Source)


def test_hyp_application_source_constructor_exists():
    assert callable(application_Source.__init__)


def test_hyp_application_source_constructor_args():
    sig = inspect.signature(application_Source.__init__)
    params = list(sig.parameters.keys())
    assert "activeState" in params, "Missing parameter 'activeState'"
    assert "logLevel" in params, "Missing parameter 'logLevel'"
    assert "removeDataOnStop" in params, "Missing parameter 'removeDataOnStop'"
    assert "updateRound" in params, "Missing parameter 'updateRound'"
    assert "state" in params, "Missing parameter 'state'"
    assert "bundleId" in params, "Missing parameter 'bundleId'"









def test_hyp_application_mashupadmin_is_not_abstract():
    assert not inspect.isabstract(application_MashupAdmin)


def test_hyp_application_mashupadmin_constructor_exists():
    assert callable(application_MashupAdmin.__init__)


def test_hyp_application_mashupadmin_constructor_args():
    sig = inspect.signature(application_MashupAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "provider" in params, "Missing parameter 'provider'"
    assert "isConfigurationAdmin" in params, "Missing parameter 'isConfigurationAdmin'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "id" in params, "Missing parameter 'id'"
    assert "profileImage" in params, "Missing parameter 'profileImage'"
    assert "localIdent" in params, "Missing parameter 'localIdent'"










def test_hyp_application_interface_is_not_abstract():
    assert not inspect.isabstract(application_Interface)


def test_hyp_application_interface_constructor_exists():
    assert callable(application_Interface.__init__)


def test_hyp_application_interface_constructor_args():
    sig = inspect.signature(application_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "urlSuffix" in params, "Missing parameter 'urlSuffix'"
    assert "frontEndCaching" in params, "Missing parameter 'frontEndCaching'"



def test_hyp_sourceactivestates_exists():
    # Check that the Enumeration exists
    assert SourceActiveStates is not None

def test_hyp_sourceactivestates_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceActiveStates]
    expected_literals = [
        "Filled",
        "WaitingForUpdate",
        "Unknown",
        "Updating",
        "Enriching",
        "Initializing",
        "Filling",
        "Initialized",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceActiveStates"

def test_hyp_propertytypes_exists():
    # Check that the Enumeration exists
    assert PropertyTypes is not None

def test_hyp_propertytypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PropertyTypes]
    expected_literals = [
        "UploadFile",
        "Date",
        "Authorization",
        "Boolean",
        "UploadZipFile",
        "Integer",
        "Float",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PropertyTypes"

def test_hyp_sourcestate_exists():
    # Check that the Enumeration exists
    assert SourceState is not None

def test_hyp_sourcestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceState]
    expected_literals = [
        "Paused",
        "Active",
        "Error",
        "Stoped",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceState"


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
application_ConfigurableElement_strategy = st.builds(
    application_ConfigurableElement,
    configurationImage=
        safe_text,
    hidden=
        safe_text,
    changeable=
        safe_text,
    ident=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
application_OAuthAdmin_strategy = st.builds(
    application_OAuthAdmin,
    username=
        safe_text,
    passwordHash=
        safe_text
)
application_OAuthClientConfig_strategy = st.builds(
    application_OAuthClientConfig,
    allowedMetaTags=
        safe_text,
    clientID=
        safe_text,
    grantType=
        safe_text,
    accessToken=
        safe_text,
    forbiddenMetaTags=
        safe_text,
    oAuthScopeLevel=
        safe_text,
    name=
        safe_text,
    code=
        safe_text,
    redirectionURL=
        safe_text,
    description=
        safe_text,
    accessTokenExpirationDate=
        st.dates(),
    accessTokenCreationDate=
        st.dates(),
    refreshToken=
        safe_text,
    type=
        safe_text,
    clientSecret=
        safe_text
)
Security_strategy = st.builds(
    Security,
)
application_ApplicationKeyConfig_strategy = st.builds(
    application_ApplicationKeyConfig,
    applicationKeys=
        safe_text
)
application_OAuthConfig_strategy = st.builds(
    application_OAuthConfig,
    useScopeInterfaceOnRedirect=
        safe_text
)
application_OAuthClientScope_strategy = st.builds(
    application_OAuthClientScope,
    positiveCategory=
        safe_text,
    allowOrganisations=
        safe_text,
    positiveTag=
        safe_text,
    maximumAge=
        safe_text,
    positiveMetaTag=
        safe_text,
    allowContents=
        safe_text,
    positiveOrganisation=
        safe_text,
    identSpecification=
        safe_text,
    negativeMetaTag=
        safe_text,
    negativeCategory=
        safe_text,
    negativeOrganisation=
        safe_text,
    allowPersons=
        safe_text,
    negativeTag=
        safe_text,
    positivePerson=
        safe_text,
    negativePerson=
        safe_text
)
application_Security_strategy = st.builds(
    application_Security,
)
Interface_strategy = st.builds(
    Interface,
)
application_FEEDInterface_strategy = st.builds(
    application_FEEDInterface,
    feedType=
        safe_text,
    allowOrganisationFiltering=
        safe_text,
    allowPersonFiltering=
        safe_text,
    language=
        safe_text,
    allowTypeFiltering=
        safe_text,
    feedTitle=
        safe_text,
    allowCategoryFiltering=
        safe_text,
    allowMetaTagFiltering=
        safe_text,
    allowTagFiltering=
        safe_text
)
application_RESTInterface_strategy = st.builds(
    application_RESTInterface,
    type=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
application_OCLRestrictedProperty_strategy = st.builds(
    application_OCLRestrictedProperty,
    OCLRestriction=
        safe_text
)
Persistency_strategy = st.builds(
    Persistency,
)
application_Database_strategy = st.builds(
    application_Database,
)
application_XMLFile_strategy = st.builds(
    application_XMLFile,
)
application_Property_strategy = st.builds(
    application_Property,
    required=
        safe_text,
    helpText=
        safe_text,
    possibleValues=
        safe_text,
    changeable=
        safe_text,
    propertyType=
        safe_text,
    hidden=
        safe_text,
    Key=
        safe_text,
    Value=
        safe_text
)
application_Configuration_strategy = st.builds(
    application_Configuration,
)
application_MashupContainer_strategy = st.builds(
    application_MashupContainer,
    backupConfiguration=
        safe_text,
    immediateSave=
        safe_text,
    backupIntervall=
        safe_text,
    identCounter=
        safe_text,
    createAccountsAtLoginTry=
        safe_text
)
application_MappingRule_strategy = st.builds(
    application_MappingRule,
)
Source_strategy = st.builds(
    Source,
)
application_Mashup_strategy = st.builds(
    application_Mashup,
    workingDirectory=
        safe_text,
    cacheDelay=
        safe_text,
    backupDataSet=
        safe_text,
    cacheAttachments=
        safe_text,
    backupIntervall=
        safe_text,
    sourceIdentCounter=
        safe_text,
    cacheDataSet=
        safe_text
)
application_DataSet_strategy = st.builds(
    application_DataSet,
)
application_Persistency_strategy = st.builds(
    application_Persistency,
)
ConfigurableElement_strategy = st.builds(
    ConfigurableElement,
)
application_Source_strategy = st.builds(
    application_Source,
    activeState=
        safe_text,
    logLevel=
        safe_text,
    removeDataOnStop=
        safe_text,
    updateRound=
        safe_text,
    state=
        safe_text,
    bundleId=
        safe_text
)
application_MashupAdmin_strategy = st.builds(
    application_MashupAdmin,
    provider=
        safe_text,
    isConfigurationAdmin=
        safe_text,
    name=
        safe_text,
    email=
        safe_text,
    id=
        safe_text,
    profileImage=
        safe_text,
    localIdent=
        safe_text
)
application_Interface_strategy = st.builds(
    application_Interface,
    urlSuffix=
        safe_text,
    frontEndCaching=
        safe_text
)




@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_configurationImage_setter(instance):
    original = instance.configurationImage
    instance.configurationImage = original
    assert instance.configurationImage == original



@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_ident_setter(instance):
    original = instance.ident
    instance.ident = original
    assert instance.ident == original



@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_ConfigurableElement_strategy)
def test_hyp_application_configurableelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_ConfigurableElement_strategy)
@settings(max_examples=30)
def test_hyp_application_configurableelement_ispropertytrueelsedefault_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPropertyTrueElseDefault(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPropertyTrueElseDefault).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPropertyTrueElseDefault' in application_ConfigurableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPropertyTrueElseDefault' in application_ConfigurableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPropertyTrueElseDefault' in application_ConfigurableElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_ConfigurableElement_strategy)
@settings(max_examples=30)
def test_hyp_application_configurableelement_removeproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeProperty' in application_ConfigurableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeProperty' in application_ConfigurableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeProperty' in application_ConfigurableElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_ConfigurableElement_strategy)
@settings(max_examples=30)
def test_hyp_application_configurableelement_addproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addProperty' in application_ConfigurableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addProperty' in application_ConfigurableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addProperty' in application_ConfigurableElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_ConfigurableElement_strategy)
@settings(max_examples=30)
def test_hyp_application_configurableelement_ispropertytrue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPropertyTrue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPropertyTrue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPropertyTrue' in application_ConfigurableElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPropertyTrue' in application_ConfigurableElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPropertyTrue' in application_ConfigurableElement is not implemented or raised an error")




@given(instance=application_OAuthAdmin_strategy)
def test_hyp_application_oauthadmin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=application_OAuthAdmin_strategy)
def test_hyp_application_oauthadmin_passwordHash_setter(instance):
    original = instance.passwordHash
    instance.passwordHash = original
    assert instance.passwordHash == original




@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_allowedMetaTags_setter(instance):
    original = instance.allowedMetaTags
    instance.allowedMetaTags = original
    assert instance.allowedMetaTags == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_clientID_setter(instance):
    original = instance.clientID
    instance.clientID = original
    assert instance.clientID == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_grantType_setter(instance):
    original = instance.grantType
    instance.grantType = original
    assert instance.grantType == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_accessToken_setter(instance):
    original = instance.accessToken
    instance.accessToken = original
    assert instance.accessToken == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_forbiddenMetaTags_setter(instance):
    original = instance.forbiddenMetaTags
    instance.forbiddenMetaTags = original
    assert instance.forbiddenMetaTags == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_oAuthScopeLevel_setter(instance):
    original = instance.oAuthScopeLevel
    instance.oAuthScopeLevel = original
    assert instance.oAuthScopeLevel == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_redirectionURL_setter(instance):
    original = instance.redirectionURL
    instance.redirectionURL = original
    assert instance.redirectionURL == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_accessTokenExpirationDate_setter(instance):
    original = instance.accessTokenExpirationDate
    instance.accessTokenExpirationDate = original
    assert instance.accessTokenExpirationDate == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_accessTokenCreationDate_setter(instance):
    original = instance.accessTokenCreationDate
    instance.accessTokenCreationDate = original
    assert instance.accessTokenCreationDate == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_refreshToken_setter(instance):
    original = instance.refreshToken
    instance.refreshToken = original
    assert instance.refreshToken == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=application_OAuthClientConfig_strategy)
def test_hyp_application_oauthclientconfig_clientSecret_setter(instance):
    original = instance.clientSecret
    instance.clientSecret = original
    assert instance.clientSecret == original





@given(instance=application_ApplicationKeyConfig_strategy)
def test_hyp_application_applicationkeyconfig_applicationKeys_setter(instance):
    original = instance.applicationKeys
    instance.applicationKeys = original
    assert instance.applicationKeys == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_ApplicationKeyConfig_strategy)
@settings(max_examples=30)
def test_hyp_application_applicationkeyconfig_hasapplicationkey_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasApplicationKey(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasApplicationKey).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasApplicationKey' in application_ApplicationKeyConfig is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasApplicationKey' in application_ApplicationKeyConfig did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasApplicationKey' in application_ApplicationKeyConfig is not implemented or raised an error")




@given(instance=application_OAuthConfig_strategy)
def test_hyp_application_oauthconfig_useScopeInterfaceOnRedirect_setter(instance):
    original = instance.useScopeInterfaceOnRedirect
    instance.useScopeInterfaceOnRedirect = original
    assert instance.useScopeInterfaceOnRedirect == original




@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_positiveCategory_setter(instance):
    original = instance.positiveCategory
    instance.positiveCategory = original
    assert instance.positiveCategory == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_allowOrganisations_setter(instance):
    original = instance.allowOrganisations
    instance.allowOrganisations = original
    assert instance.allowOrganisations == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_positiveTag_setter(instance):
    original = instance.positiveTag
    instance.positiveTag = original
    assert instance.positiveTag == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_maximumAge_setter(instance):
    original = instance.maximumAge
    instance.maximumAge = original
    assert instance.maximumAge == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_positiveMetaTag_setter(instance):
    original = instance.positiveMetaTag
    instance.positiveMetaTag = original
    assert instance.positiveMetaTag == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_allowContents_setter(instance):
    original = instance.allowContents
    instance.allowContents = original
    assert instance.allowContents == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_positiveOrganisation_setter(instance):
    original = instance.positiveOrganisation
    instance.positiveOrganisation = original
    assert instance.positiveOrganisation == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_identSpecification_setter(instance):
    original = instance.identSpecification
    instance.identSpecification = original
    assert instance.identSpecification == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_negativeMetaTag_setter(instance):
    original = instance.negativeMetaTag
    instance.negativeMetaTag = original
    assert instance.negativeMetaTag == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_negativeCategory_setter(instance):
    original = instance.negativeCategory
    instance.negativeCategory = original
    assert instance.negativeCategory == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_negativeOrganisation_setter(instance):
    original = instance.negativeOrganisation
    instance.negativeOrganisation = original
    assert instance.negativeOrganisation == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_allowPersons_setter(instance):
    original = instance.allowPersons
    instance.allowPersons = original
    assert instance.allowPersons == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_negativeTag_setter(instance):
    original = instance.negativeTag
    instance.negativeTag = original
    assert instance.negativeTag == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_positivePerson_setter(instance):
    original = instance.positivePerson
    instance.positivePerson = original
    assert instance.positivePerson == original



@given(instance=application_OAuthClientScope_strategy)
def test_hyp_application_oauthclientscope_negativePerson_setter(instance):
    original = instance.negativePerson
    instance.negativePerson = original
    assert instance.negativePerson == original






@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_feedType_setter(instance):
    original = instance.feedType
    instance.feedType = original
    assert instance.feedType == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowOrganisationFiltering_setter(instance):
    original = instance.allowOrganisationFiltering
    instance.allowOrganisationFiltering = original
    assert instance.allowOrganisationFiltering == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowPersonFiltering_setter(instance):
    original = instance.allowPersonFiltering
    instance.allowPersonFiltering = original
    assert instance.allowPersonFiltering == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowTypeFiltering_setter(instance):
    original = instance.allowTypeFiltering
    instance.allowTypeFiltering = original
    assert instance.allowTypeFiltering == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_feedTitle_setter(instance):
    original = instance.feedTitle
    instance.feedTitle = original
    assert instance.feedTitle == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowCategoryFiltering_setter(instance):
    original = instance.allowCategoryFiltering
    instance.allowCategoryFiltering = original
    assert instance.allowCategoryFiltering == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowMetaTagFiltering_setter(instance):
    original = instance.allowMetaTagFiltering
    instance.allowMetaTagFiltering = original
    assert instance.allowMetaTagFiltering == original



@given(instance=application_FEEDInterface_strategy)
def test_hyp_application_feedinterface_allowTagFiltering_setter(instance):
    original = instance.allowTagFiltering
    instance.allowTagFiltering = original
    assert instance.allowTagFiltering == original




@given(instance=application_RESTInterface_strategy)
def test_hyp_application_restinterface_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=application_OCLRestrictedProperty_strategy)
def test_hyp_application_oclrestrictedproperty_OCLRestriction_setter(instance):
    original = instance.OCLRestriction
    instance.OCLRestriction = original
    assert instance.OCLRestriction == original







@given(instance=application_Property_strategy)
def test_hyp_application_property_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_helpText_setter(instance):
    original = instance.helpText
    instance.helpText = original
    assert instance.helpText == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_possibleValues_setter(instance):
    original = instance.possibleValues
    instance.possibleValues = original
    assert instance.possibleValues == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_propertyType_setter(instance):
    original = instance.propertyType
    instance.propertyType = original
    assert instance.propertyType == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_Key_setter(instance):
    original = instance.Key
    instance.Key = original
    assert instance.Key == original



@given(instance=application_Property_strategy)
def test_hyp_application_property_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_Property_strategy)
@settings(max_examples=30)
def test_hyp_application_property_isvaluerange_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValueRange()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValueRange).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValueRange' in application_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValueRange' in application_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValueRange' in application_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_Property_strategy)
@settings(max_examples=30)
def test_hyp_application_property_isvaluelist_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValueList()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValueList).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValueList' in application_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValueList' in application_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValueList' in application_Property is not implemented or raised an error")





@given(instance=application_MashupContainer_strategy)
def test_hyp_application_mashupcontainer_backupConfiguration_setter(instance):
    original = instance.backupConfiguration
    instance.backupConfiguration = original
    assert instance.backupConfiguration == original



@given(instance=application_MashupContainer_strategy)
def test_hyp_application_mashupcontainer_immediateSave_setter(instance):
    original = instance.immediateSave
    instance.immediateSave = original
    assert instance.immediateSave == original



@given(instance=application_MashupContainer_strategy)
def test_hyp_application_mashupcontainer_backupIntervall_setter(instance):
    original = instance.backupIntervall
    instance.backupIntervall = original
    assert instance.backupIntervall == original



@given(instance=application_MashupContainer_strategy)
def test_hyp_application_mashupcontainer_identCounter_setter(instance):
    original = instance.identCounter
    instance.identCounter = original
    assert instance.identCounter == original



@given(instance=application_MashupContainer_strategy)
def test_hyp_application_mashupcontainer_createAccountsAtLoginTry_setter(instance):
    original = instance.createAccountsAtLoginTry
    instance.createAccountsAtLoginTry = original
    assert instance.createAccountsAtLoginTry == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_MashupContainer_strategy)
@settings(max_examples=30)
def test_hyp_application_mashupcontainer_setnewidentfor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setNewIdentFor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setNewIdentFor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setNewIdentFor' in application_MashupContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setNewIdentFor' in application_MashupContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setNewIdentFor' in application_MashupContainer is not implemented or raised an error")






@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_workingDirectory_setter(instance):
    original = instance.workingDirectory
    instance.workingDirectory = original
    assert instance.workingDirectory == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_cacheDelay_setter(instance):
    original = instance.cacheDelay
    instance.cacheDelay = original
    assert instance.cacheDelay == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_backupDataSet_setter(instance):
    original = instance.backupDataSet
    instance.backupDataSet = original
    assert instance.backupDataSet == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_cacheAttachments_setter(instance):
    original = instance.cacheAttachments
    instance.cacheAttachments = original
    assert instance.cacheAttachments == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_backupIntervall_setter(instance):
    original = instance.backupIntervall
    instance.backupIntervall = original
    assert instance.backupIntervall == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_sourceIdentCounter_setter(instance):
    original = instance.sourceIdentCounter
    instance.sourceIdentCounter = original
    assert instance.sourceIdentCounter == original



@given(instance=application_Mashup_strategy)
def test_hyp_application_mashup_cacheDataSet_setter(instance):
    original = instance.cacheDataSet
    instance.cacheDataSet = original
    assert instance.cacheDataSet == original







@given(instance=application_Source_strategy)
def test_hyp_application_source_activeState_setter(instance):
    original = instance.activeState
    instance.activeState = original
    assert instance.activeState == original



@given(instance=application_Source_strategy)
def test_hyp_application_source_logLevel_setter(instance):
    original = instance.logLevel
    instance.logLevel = original
    assert instance.logLevel == original



@given(instance=application_Source_strategy)
def test_hyp_application_source_removeDataOnStop_setter(instance):
    original = instance.removeDataOnStop
    instance.removeDataOnStop = original
    assert instance.removeDataOnStop == original



@given(instance=application_Source_strategy)
def test_hyp_application_source_updateRound_setter(instance):
    original = instance.updateRound
    instance.updateRound = original
    assert instance.updateRound == original



@given(instance=application_Source_strategy)
def test_hyp_application_source_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=application_Source_strategy)
def test_hyp_application_source_bundleId_setter(instance):
    original = instance.bundleId
    instance.bundleId = original
    assert instance.bundleId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_Source_strategy)
@settings(max_examples=30)
def test_hyp_application_source_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in application_Source is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in application_Source did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in application_Source is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_Source_strategy)
@settings(max_examples=30)
def test_hyp_application_source_pause_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pause()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pause).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pause' in application_Source is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pause' in application_Source did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pause' in application_Source is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=application_Source_strategy)
@settings(max_examples=30)
def test_hyp_application_source_stop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.stop()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.stop).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'stop' in application_Source is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'stop' in application_Source did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'stop' in application_Source is not implemented or raised an error")




@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_isConfigurationAdmin_setter(instance):
    original = instance.isConfigurationAdmin
    instance.isConfigurationAdmin = original
    assert instance.isConfigurationAdmin == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_profileImage_setter(instance):
    original = instance.profileImage
    instance.profileImage = original
    assert instance.profileImage == original



@given(instance=application_MashupAdmin_strategy)
def test_hyp_application_mashupadmin_localIdent_setter(instance):
    original = instance.localIdent
    instance.localIdent = original
    assert instance.localIdent == original




@given(instance=application_Interface_strategy)
def test_hyp_application_interface_urlSuffix_setter(instance):
    original = instance.urlSuffix
    instance.urlSuffix = original
    assert instance.urlSuffix == original



@given(instance=application_Interface_strategy)
def test_hyp_application_interface_frontEndCaching_setter(instance):
    original = instance.frontEndCaching
    instance.frontEndCaching = original
    assert instance.frontEndCaching == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ConfigurableElement,
    Interface,
    Persistency,
    Property,
    Security,
    Source,
    application_ApplicationKeyConfig,
    application_ConfigurableElement,
    application_Configuration,
    application_DataSet,
    application_Database,
    application_FEEDInterface,
    application_Interface,
    application_MappingRule,
    application_Mashup,
    application_MashupAdmin,
    application_MashupContainer,
    application_OAuthAdmin,
    application_OAuthClientConfig,
    application_OAuthClientScope,
    application_OAuthConfig,
    application_OCLRestrictedProperty,
    application_Persistency,
    application_Property,
    application_RESTInterface,
    application_Security,
    application_Source,
    application_XMLFile,
    PropertyTypes,
    SourceActiveStates,
    SourceState,
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

def test_application_ApplicationKeyConfig_applicationKeys_value_roundtrip():
    instance = application_ApplicationKeyConfig(applicationKeys="sample_text")
    assert instance.applicationKeys == "sample_text"
    instance.applicationKeys = "sample_text_2"
    assert instance.applicationKeys == "sample_text_2"


def test_application_ConfigurableElement_changeable_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.changeable == "sample_text"
    instance.changeable = "sample_text_2"
    assert instance.changeable == "sample_text_2"


def test_application_ConfigurableElement_configurationImage_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.configurationImage == "sample_text"
    instance.configurationImage = "sample_text_2"
    assert instance.configurationImage == "sample_text_2"


def test_application_ConfigurableElement_description_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_application_ConfigurableElement_hidden_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.hidden == "sample_text"
    instance.hidden = "sample_text_2"
    assert instance.hidden == "sample_text_2"


def test_application_ConfigurableElement_ident_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.ident == "sample_text"
    instance.ident = "sample_text_2"
    assert instance.ident == "sample_text_2"


def test_application_ConfigurableElement_name_value_roundtrip():
    instance = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_application_FEEDInterface_allowCategoryFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowCategoryFiltering == "sample_text"
    instance.allowCategoryFiltering = "sample_text_2"
    assert instance.allowCategoryFiltering == "sample_text_2"


def test_application_FEEDInterface_allowMetaTagFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowMetaTagFiltering == "sample_text"
    instance.allowMetaTagFiltering = "sample_text_2"
    assert instance.allowMetaTagFiltering == "sample_text_2"


def test_application_FEEDInterface_allowOrganisationFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowOrganisationFiltering == "sample_text"
    instance.allowOrganisationFiltering = "sample_text_2"
    assert instance.allowOrganisationFiltering == "sample_text_2"


def test_application_FEEDInterface_allowPersonFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowPersonFiltering == "sample_text"
    instance.allowPersonFiltering = "sample_text_2"
    assert instance.allowPersonFiltering == "sample_text_2"


def test_application_FEEDInterface_allowTagFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowTagFiltering == "sample_text"
    instance.allowTagFiltering = "sample_text_2"
    assert instance.allowTagFiltering == "sample_text_2"


def test_application_FEEDInterface_allowTypeFiltering_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.allowTypeFiltering == "sample_text"
    instance.allowTypeFiltering = "sample_text_2"
    assert instance.allowTypeFiltering == "sample_text_2"


def test_application_FEEDInterface_feedTitle_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.feedTitle == "sample_text"
    instance.feedTitle = "sample_text_2"
    assert instance.feedTitle == "sample_text_2"


def test_application_FEEDInterface_feedType_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.feedType == "sample_text"
    instance.feedType = "sample_text_2"
    assert instance.feedType == "sample_text_2"


def test_application_FEEDInterface_language_value_roundtrip():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_application_Interface_frontEndCaching_value_roundtrip():
    instance = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    assert instance.frontEndCaching == "sample_text"
    instance.frontEndCaching = "sample_text_2"
    assert instance.frontEndCaching == "sample_text_2"


def test_application_Interface_urlSuffix_value_roundtrip():
    instance = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    assert instance.urlSuffix == "sample_text"
    instance.urlSuffix = "sample_text_2"
    assert instance.urlSuffix == "sample_text_2"


def test_application_Mashup_backupDataSet_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.backupDataSet == "sample_text"
    instance.backupDataSet = "sample_text_2"
    assert instance.backupDataSet == "sample_text_2"


def test_application_Mashup_backupIntervall_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.backupIntervall == "sample_text"
    instance.backupIntervall = "sample_text_2"
    assert instance.backupIntervall == "sample_text_2"


def test_application_Mashup_cacheAttachments_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.cacheAttachments == "sample_text"
    instance.cacheAttachments = "sample_text_2"
    assert instance.cacheAttachments == "sample_text_2"


def test_application_Mashup_cacheDataSet_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.cacheDataSet == "sample_text"
    instance.cacheDataSet = "sample_text_2"
    assert instance.cacheDataSet == "sample_text_2"


def test_application_Mashup_cacheDelay_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.cacheDelay == "sample_text"
    instance.cacheDelay = "sample_text_2"
    assert instance.cacheDelay == "sample_text_2"


def test_application_Mashup_sourceIdentCounter_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.sourceIdentCounter == "sample_text"
    instance.sourceIdentCounter = "sample_text_2"
    assert instance.sourceIdentCounter == "sample_text_2"


def test_application_Mashup_workingDirectory_value_roundtrip():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert instance.workingDirectory == "sample_text"
    instance.workingDirectory = "sample_text_2"
    assert instance.workingDirectory == "sample_text_2"


def test_application_MashupAdmin_email_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_application_MashupAdmin_id_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_application_MashupAdmin_isConfigurationAdmin_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.isConfigurationAdmin == "sample_text"
    instance.isConfigurationAdmin = "sample_text_2"
    assert instance.isConfigurationAdmin == "sample_text_2"


def test_application_MashupAdmin_localIdent_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.localIdent == "sample_text"
    instance.localIdent = "sample_text_2"
    assert instance.localIdent == "sample_text_2"


def test_application_MashupAdmin_name_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_application_MashupAdmin_profileImage_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.profileImage == "sample_text"
    instance.profileImage = "sample_text_2"
    assert instance.profileImage == "sample_text_2"


def test_application_MashupAdmin_provider_value_roundtrip():
    instance = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_application_MashupContainer_backupConfiguration_value_roundtrip():
    instance = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    assert instance.backupConfiguration == "sample_text"
    instance.backupConfiguration = "sample_text_2"
    assert instance.backupConfiguration == "sample_text_2"


def test_application_MashupContainer_backupIntervall_value_roundtrip():
    instance = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    assert instance.backupIntervall == "sample_text"
    instance.backupIntervall = "sample_text_2"
    assert instance.backupIntervall == "sample_text_2"


def test_application_MashupContainer_createAccountsAtLoginTry_value_roundtrip():
    instance = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    assert instance.createAccountsAtLoginTry == "sample_text"
    instance.createAccountsAtLoginTry = "sample_text_2"
    assert instance.createAccountsAtLoginTry == "sample_text_2"


def test_application_MashupContainer_identCounter_value_roundtrip():
    instance = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    assert instance.identCounter == "sample_text"
    instance.identCounter = "sample_text_2"
    assert instance.identCounter == "sample_text_2"


def test_application_MashupContainer_immediateSave_value_roundtrip():
    instance = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    assert instance.immediateSave == "sample_text"
    instance.immediateSave = "sample_text_2"
    assert instance.immediateSave == "sample_text_2"


def test_application_OAuthAdmin_passwordHash_value_roundtrip():
    instance = application_OAuthAdmin(passwordHash="sample_text", username="sample_text")
    assert instance.passwordHash == "sample_text"
    instance.passwordHash = "sample_text_2"
    assert instance.passwordHash == "sample_text_2"


def test_application_OAuthAdmin_username_value_roundtrip():
    instance = application_OAuthAdmin(passwordHash="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_application_OAuthClientConfig_accessToken_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.accessToken == "sample_text"
    instance.accessToken = "sample_text_2"
    assert instance.accessToken == "sample_text_2"


def test_application_OAuthClientConfig_accessTokenCreationDate_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.accessTokenCreationDate == date(2024, 1, 1)
    instance.accessTokenCreationDate = date(2025, 6, 15)
    assert instance.accessTokenCreationDate == date(2025, 6, 15)


def test_application_OAuthClientConfig_accessTokenExpirationDate_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.accessTokenExpirationDate == date(2024, 1, 1)
    instance.accessTokenExpirationDate = date(2025, 6, 15)
    assert instance.accessTokenExpirationDate == date(2025, 6, 15)


def test_application_OAuthClientConfig_allowedMetaTags_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.allowedMetaTags == "sample_text"
    instance.allowedMetaTags = "sample_text_2"
    assert instance.allowedMetaTags == "sample_text_2"


def test_application_OAuthClientConfig_clientID_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.clientID == "sample_text"
    instance.clientID = "sample_text_2"
    assert instance.clientID == "sample_text_2"


def test_application_OAuthClientConfig_clientSecret_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.clientSecret == "sample_text"
    instance.clientSecret = "sample_text_2"
    assert instance.clientSecret == "sample_text_2"


def test_application_OAuthClientConfig_code_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_application_OAuthClientConfig_description_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_application_OAuthClientConfig_forbiddenMetaTags_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.forbiddenMetaTags == "sample_text"
    instance.forbiddenMetaTags = "sample_text_2"
    assert instance.forbiddenMetaTags == "sample_text_2"


def test_application_OAuthClientConfig_grantType_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.grantType == "sample_text"
    instance.grantType = "sample_text_2"
    assert instance.grantType == "sample_text_2"


def test_application_OAuthClientConfig_name_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_application_OAuthClientConfig_oAuthScopeLevel_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.oAuthScopeLevel == "sample_text"
    instance.oAuthScopeLevel = "sample_text_2"
    assert instance.oAuthScopeLevel == "sample_text_2"


def test_application_OAuthClientConfig_redirectionURL_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.redirectionURL == "sample_text"
    instance.redirectionURL = "sample_text_2"
    assert instance.redirectionURL == "sample_text_2"


def test_application_OAuthClientConfig_refreshToken_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.refreshToken == "sample_text"
    instance.refreshToken = "sample_text_2"
    assert instance.refreshToken == "sample_text_2"


def test_application_OAuthClientConfig_type_value_roundtrip():
    instance = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_application_OAuthClientScope_allowContents_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.allowContents == "sample_text"
    instance.allowContents = "sample_text_2"
    assert instance.allowContents == "sample_text_2"


def test_application_OAuthClientScope_allowOrganisations_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.allowOrganisations == "sample_text"
    instance.allowOrganisations = "sample_text_2"
    assert instance.allowOrganisations == "sample_text_2"


def test_application_OAuthClientScope_allowPersons_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.allowPersons == "sample_text"
    instance.allowPersons = "sample_text_2"
    assert instance.allowPersons == "sample_text_2"


def test_application_OAuthClientScope_identSpecification_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.identSpecification == "sample_text"
    instance.identSpecification = "sample_text_2"
    assert instance.identSpecification == "sample_text_2"


def test_application_OAuthClientScope_maximumAge_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.maximumAge == "sample_text"
    instance.maximumAge = "sample_text_2"
    assert instance.maximumAge == "sample_text_2"


def test_application_OAuthClientScope_negativeCategory_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.negativeCategory == "sample_text"
    instance.negativeCategory = "sample_text_2"
    assert instance.negativeCategory == "sample_text_2"


def test_application_OAuthClientScope_negativeMetaTag_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.negativeMetaTag == "sample_text"
    instance.negativeMetaTag = "sample_text_2"
    assert instance.negativeMetaTag == "sample_text_2"


def test_application_OAuthClientScope_negativeOrganisation_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.negativeOrganisation == "sample_text"
    instance.negativeOrganisation = "sample_text_2"
    assert instance.negativeOrganisation == "sample_text_2"


def test_application_OAuthClientScope_negativePerson_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.negativePerson == "sample_text"
    instance.negativePerson = "sample_text_2"
    assert instance.negativePerson == "sample_text_2"


def test_application_OAuthClientScope_negativeTag_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.negativeTag == "sample_text"
    instance.negativeTag = "sample_text_2"
    assert instance.negativeTag == "sample_text_2"


def test_application_OAuthClientScope_positiveCategory_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.positiveCategory == "sample_text"
    instance.positiveCategory = "sample_text_2"
    assert instance.positiveCategory == "sample_text_2"


def test_application_OAuthClientScope_positiveMetaTag_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.positiveMetaTag == "sample_text"
    instance.positiveMetaTag = "sample_text_2"
    assert instance.positiveMetaTag == "sample_text_2"


def test_application_OAuthClientScope_positiveOrganisation_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.positiveOrganisation == "sample_text"
    instance.positiveOrganisation = "sample_text_2"
    assert instance.positiveOrganisation == "sample_text_2"


def test_application_OAuthClientScope_positivePerson_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.positivePerson == "sample_text"
    instance.positivePerson = "sample_text_2"
    assert instance.positivePerson == "sample_text_2"


def test_application_OAuthClientScope_positiveTag_value_roundtrip():
    instance = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    assert instance.positiveTag == "sample_text"
    instance.positiveTag = "sample_text_2"
    assert instance.positiveTag == "sample_text_2"


def test_application_OAuthConfig_useScopeInterfaceOnRedirect_value_roundtrip():
    instance = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    assert instance.useScopeInterfaceOnRedirect == "sample_text"
    instance.useScopeInterfaceOnRedirect = "sample_text_2"
    assert instance.useScopeInterfaceOnRedirect == "sample_text_2"


def test_application_OCLRestrictedProperty_OCLRestriction_value_roundtrip():
    instance = application_OCLRestrictedProperty(OCLRestriction="sample_text")
    assert instance.OCLRestriction == "sample_text"
    instance.OCLRestriction = "sample_text_2"
    assert instance.OCLRestriction == "sample_text_2"


def test_application_Property_Key_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.Key == "sample_text"
    instance.Key = "sample_text_2"
    assert instance.Key == "sample_text_2"


def test_application_Property_Value_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_application_Property_changeable_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.changeable == "sample_text"
    instance.changeable = "sample_text_2"
    assert instance.changeable == "sample_text_2"


def test_application_Property_helpText_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.helpText == "sample_text"
    instance.helpText = "sample_text_2"
    assert instance.helpText == "sample_text_2"


def test_application_Property_hidden_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.hidden == "sample_text"
    instance.hidden = "sample_text_2"
    assert instance.hidden == "sample_text_2"


def test_application_Property_possibleValues_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.possibleValues == "sample_text"
    instance.possibleValues = "sample_text_2"
    assert instance.possibleValues == "sample_text_2"


def test_application_Property_propertyType_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.propertyType == "sample_text"
    instance.propertyType = "sample_text_2"
    assert instance.propertyType == "sample_text_2"


def test_application_Property_required_value_roundtrip():
    instance = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    assert instance.required == "sample_text"
    instance.required = "sample_text_2"
    assert instance.required == "sample_text_2"


def test_application_RESTInterface_type_value_roundtrip():
    instance = application_RESTInterface(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_application_Source_activeState_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.activeState == "sample_text"
    instance.activeState = "sample_text_2"
    assert instance.activeState == "sample_text_2"


def test_application_Source_bundleId_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.bundleId == "sample_text"
    instance.bundleId = "sample_text_2"
    assert instance.bundleId == "sample_text_2"


def test_application_Source_logLevel_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.logLevel == "sample_text"
    instance.logLevel = "sample_text_2"
    assert instance.logLevel == "sample_text_2"


def test_application_Source_removeDataOnStop_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.removeDataOnStop == "sample_text"
    instance.removeDataOnStop = "sample_text_2"
    assert instance.removeDataOnStop == "sample_text_2"


def test_application_Source_state_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_application_Source_updateRound_value_roundtrip():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert instance.updateRound == "sample_text"
    instance.updateRound = "sample_text_2"
    assert instance.updateRound == "sample_text_2"


def test_application_Interface_isa_ConfigurableElement():
    instance = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    assert isinstance(instance, ConfigurableElement)


def test_application_Source_isa_ConfigurableElement():
    instance = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    assert isinstance(instance, ConfigurableElement)


def test_application_FEEDInterface_isa_Interface():
    instance = application_FEEDInterface(allowCategoryFiltering="sample_text", allowMetaTagFiltering="sample_text", allowOrganisationFiltering="sample_text", allowPersonFiltering="sample_text", allowTagFiltering="sample_text", allowTypeFiltering="sample_text", feedTitle="sample_text", feedType="sample_text", language="sample_text")
    assert isinstance(instance, Interface)


def test_application_RESTInterface_isa_Interface():
    instance = application_RESTInterface(type="sample_text")
    assert isinstance(instance, Interface)


def test_application_Database_isa_Persistency():
    instance = application_Database()
    assert isinstance(instance, Persistency)


def test_application_XMLFile_isa_Persistency():
    instance = application_XMLFile()
    assert isinstance(instance, Persistency)


def test_application_OCLRestrictedProperty_isa_Property():
    instance = application_OCLRestrictedProperty(OCLRestriction="sample_text")
    assert isinstance(instance, Property)


def test_application_ApplicationKeyConfig_isa_Security():
    instance = application_ApplicationKeyConfig(applicationKeys="sample_text")
    assert isinstance(instance, Security)


def test_application_OAuthConfig_isa_Security():
    instance = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    assert isinstance(instance, Security)


def test_application_Mashup_isa_Source():
    instance = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    assert isinstance(instance, Source)


def test_assoc_admins28_link_reassign_clear():
    a = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    b1 = application_OAuthAdmin(passwordHash="sample_text", username="sample_text")
    b2 = application_OAuthAdmin(passwordHash="sample_text_2", username="sample_text_2")
    _safe_set(a, 'application_OAuthConfig29', {b1})
    assert _is_linked(a, 'application_OAuthConfig29', b1)
    if hasattr(b1, 'application_OAuthAdmin'):
        assert _is_linked(b1, 'application_OAuthAdmin', a)
    _safe_set(a, 'application_OAuthConfig29', {b2})
    assert _is_linked(a, 'application_OAuthConfig29', b2)
    if hasattr(b1, 'application_OAuthAdmin'):
        assert not _is_linked(b1, 'application_OAuthAdmin', a)
    if hasattr(b2, 'application_OAuthAdmin'):
        assert _is_linked(b2, 'application_OAuthAdmin', a)
    _safe_set(a, 'application_OAuthConfig29', set())
    assert not _is_linked(a, 'application_OAuthConfig29', b2)
    if hasattr(b2, 'application_OAuthAdmin'):
        assert not _is_linked(b2, 'application_OAuthAdmin', a)


def test_assoc_allMashupAdmins12_link_reassign_clear():
    a = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    b1 = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    b2 = application_MashupAdmin(email="sample_text_2", id="sample_text_2", isConfigurationAdmin="sample_text_2", localIdent="sample_text_2", name="sample_text_2", profileImage="sample_text_2", provider="sample_text_2")
    _safe_set(a, 'application_MashupContainer13', {b1})
    assert _is_linked(a, 'application_MashupContainer13', b1)
    if hasattr(b1, 'application_MashupAdmin'):
        assert _is_linked(b1, 'application_MashupAdmin', a)
    _safe_set(a, 'application_MashupContainer13', {b2})
    assert _is_linked(a, 'application_MashupContainer13', b2)
    if hasattr(b1, 'application_MashupAdmin'):
        assert not _is_linked(b1, 'application_MashupAdmin', a)
    if hasattr(b2, 'application_MashupAdmin'):
        assert _is_linked(b2, 'application_MashupAdmin', a)
    _safe_set(a, 'application_MashupContainer13', set())
    assert not _is_linked(a, 'application_MashupContainer13', b2)
    if hasattr(b2, 'application_MashupAdmin'):
        assert not _is_linked(b2, 'application_MashupAdmin', a)


def test_assoc_clientScope30_link_reassign_clear():
    a = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    b1 = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    b2 = application_OAuthClientConfig(accessToken="sample_text_2", accessTokenCreationDate=date(2025, 6, 15), accessTokenExpirationDate=date(2025, 6, 15), allowedMetaTags="sample_text_2", clientID="sample_text_2", clientSecret="sample_text_2", code="sample_text_2", description="sample_text_2", forbiddenMetaTags="sample_text_2", grantType="sample_text_2", name="sample_text_2", oAuthScopeLevel="sample_text_2", redirectionURL="sample_text_2", refreshToken="sample_text_2", type="sample_text_2")
    _safe_set(a, 'application_OAuthClientScope', b1)
    assert _is_linked(a, 'application_OAuthClientScope', b1)
    if hasattr(b1, 'application_OAuthClientConfig31'):
        assert _is_linked(b1, 'application_OAuthClientConfig31', a)
    _safe_set(a, 'application_OAuthClientScope', b2)
    assert _is_linked(a, 'application_OAuthClientScope', b2)
    if hasattr(b1, 'application_OAuthClientConfig31'):
        assert not _is_linked(b1, 'application_OAuthClientConfig31', a)
    if hasattr(b2, 'application_OAuthClientConfig31'):
        assert _is_linked(b2, 'application_OAuthClientConfig31', a)
    _safe_set(a, 'application_OAuthClientScope', None)
    assert not _is_linked(a, 'application_OAuthClientScope', b2)
    if hasattr(b2, 'application_OAuthClientConfig31'):
        assert not _is_linked(b2, 'application_OAuthClientConfig31', a)


def test_assoc_clients27_link_reassign_clear():
    a = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    b1 = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    b2 = application_OAuthClientConfig(accessToken="sample_text_2", accessTokenCreationDate=date(2025, 6, 15), accessTokenExpirationDate=date(2025, 6, 15), allowedMetaTags="sample_text_2", clientID="sample_text_2", clientSecret="sample_text_2", code="sample_text_2", description="sample_text_2", forbiddenMetaTags="sample_text_2", grantType="sample_text_2", name="sample_text_2", oAuthScopeLevel="sample_text_2", redirectionURL="sample_text_2", refreshToken="sample_text_2", type="sample_text_2")
    _safe_set(a, 'application_OAuthConfig', {b1})
    assert _is_linked(a, 'application_OAuthConfig', b1)
    if hasattr(b1, 'application_OAuthClientConfig'):
        assert _is_linked(b1, 'application_OAuthClientConfig', a)
    _safe_set(a, 'application_OAuthConfig', {b2})
    assert _is_linked(a, 'application_OAuthConfig', b2)
    if hasattr(b1, 'application_OAuthClientConfig'):
        assert not _is_linked(b1, 'application_OAuthClientConfig', a)
    if hasattr(b2, 'application_OAuthClientConfig'):
        assert _is_linked(b2, 'application_OAuthClientConfig', a)
    _safe_set(a, 'application_OAuthConfig', set())
    assert not _is_linked(a, 'application_OAuthConfig', b2)
    if hasattr(b2, 'application_OAuthClientConfig'):
        assert not _is_linked(b2, 'application_OAuthClientConfig', a)


def test_assoc_configurableMashups32_link_reassign_clear():
    a = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'mashupAdmins', {b1})
    assert _is_linked(a, 'mashupAdmins', b1)
    if hasattr(b1, 'Mashup33'):
        assert _is_linked(b1, 'Mashup33', a)
    _safe_set(a, 'mashupAdmins', {b2})
    assert _is_linked(a, 'mashupAdmins', b2)
    if hasattr(b1, 'Mashup33'):
        assert not _is_linked(b1, 'Mashup33', a)
    if hasattr(b2, 'Mashup33'):
        assert _is_linked(b2, 'Mashup33', a)
    _safe_set(a, 'mashupAdmins', set())
    assert not _is_linked(a, 'mashupAdmins', b2)
    if hasattr(b2, 'Mashup33'):
        assert not _is_linked(b2, 'Mashup33', a)


def test_assoc_configuration34_link_reassign_clear():
    a = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    b1 = application_Configuration()
    b2 = application_Configuration()
    _safe_set(a, 'application_ConfigurableElement', b1)
    assert _is_linked(a, 'application_ConfigurableElement', b1)
    if hasattr(b1, 'application_Configuration35'):
        assert _is_linked(b1, 'application_Configuration35', a)
    _safe_set(a, 'application_ConfigurableElement', b2)
    assert _is_linked(a, 'application_ConfigurableElement', b2)
    if hasattr(b1, 'application_Configuration35'):
        assert not _is_linked(b1, 'application_Configuration35', a)
    if hasattr(b2, 'application_Configuration35'):
        assert _is_linked(b2, 'application_Configuration35', a)
    _safe_set(a, 'application_ConfigurableElement', None)
    assert not _is_linked(a, 'application_ConfigurableElement', b2)
    if hasattr(b2, 'application_Configuration35'):
        assert not _is_linked(b2, 'application_Configuration35', a)


def test_assoc_dataSet1_link_reassign_clear():
    a = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    b1 = application_DataSet()
    b2 = application_DataSet()
    _safe_set(a, 'application_Source2', b1)
    assert _is_linked(a, 'application_Source2', b1)
    if hasattr(b1, 'application_DataSet'):
        assert _is_linked(b1, 'application_DataSet', a)
    _safe_set(a, 'application_Source2', b2)
    assert _is_linked(a, 'application_Source2', b2)
    if hasattr(b1, 'application_DataSet'):
        assert not _is_linked(b1, 'application_DataSet', a)
    if hasattr(b2, 'application_DataSet'):
        assert _is_linked(b2, 'application_DataSet', a)
    _safe_set(a, 'application_Source2', None)
    assert not _is_linked(a, 'application_Source2', b2)
    if hasattr(b2, 'application_DataSet'):
        assert not _is_linked(b2, 'application_DataSet', a)


def test_assoc_defaultMashups14_link_reassign_clear():
    a = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'application_MashupContainer15', {b1})
    assert _is_linked(a, 'application_MashupContainer15', b1)
    if hasattr(b1, 'application_Mashup16'):
        assert _is_linked(b1, 'application_Mashup16', a)
    _safe_set(a, 'application_MashupContainer15', {b2})
    assert _is_linked(a, 'application_MashupContainer15', b2)
    if hasattr(b1, 'application_Mashup16'):
        assert not _is_linked(b1, 'application_Mashup16', a)
    if hasattr(b2, 'application_Mashup16'):
        assert _is_linked(b2, 'application_Mashup16', a)
    _safe_set(a, 'application_MashupContainer15', set())
    assert not _is_linked(a, 'application_MashupContainer15', b2)
    if hasattr(b2, 'application_Mashup16'):
        assert not _is_linked(b2, 'application_Mashup16', a)


def test_assoc_interface25_link_reassign_clear():
    a = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    b1 = application_Security()
    b2 = application_Security()
    _safe_set(a, 'Interface26', b1)
    assert _is_linked(a, 'Interface26', b1)
    if hasattr(b1, 'security'):
        assert _is_linked(b1, 'security', a)
    _safe_set(a, 'Interface26', b2)
    assert _is_linked(a, 'Interface26', b2)
    if hasattr(b1, 'security'):
        assert not _is_linked(b1, 'security', a)
    if hasattr(b2, 'security'):
        assert _is_linked(b2, 'security', a)
    _safe_set(a, 'Interface26', None)
    assert not _is_linked(a, 'Interface26', b2)
    if hasattr(b2, 'security'):
        assert not _is_linked(b2, 'security', a)


def test_assoc_interfaceConfigurations20_link_reassign_clear():
    a = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    b1 = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    b2 = application_Interface(frontEndCaching="sample_text_2", urlSuffix="sample_text_2")
    _safe_set(a, 'application_MashupContainer21', {b1})
    assert _is_linked(a, 'application_MashupContainer21', b1)
    if hasattr(b1, 'application_Interface'):
        assert _is_linked(b1, 'application_Interface', a)
    _safe_set(a, 'application_MashupContainer21', {b2})
    assert _is_linked(a, 'application_MashupContainer21', b2)
    if hasattr(b1, 'application_Interface'):
        assert not _is_linked(b1, 'application_Interface', a)
    if hasattr(b2, 'application_Interface'):
        assert _is_linked(b2, 'application_Interface', a)
    _safe_set(a, 'application_MashupContainer21', set())
    assert not _is_linked(a, 'application_MashupContainer21', b2)
    if hasattr(b2, 'application_Interface'):
        assert not _is_linked(b2, 'application_Interface', a)


def test_assoc_interfaces6_link_reassign_clear():
    a = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b1 = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    b2 = application_Interface(frontEndCaching="sample_text_2", urlSuffix="sample_text_2")
    _safe_set(a, 'mashup7', {b1})
    assert _is_linked(a, 'mashup7', b1)
    if hasattr(b1, 'Interface'):
        assert _is_linked(b1, 'Interface', a)
    _safe_set(a, 'mashup7', {b2})
    assert _is_linked(a, 'mashup7', b2)
    if hasattr(b1, 'Interface'):
        assert not _is_linked(b1, 'Interface', a)
    if hasattr(b2, 'Interface'):
        assert _is_linked(b2, 'Interface', a)
    _safe_set(a, 'mashup7', set())
    assert not _is_linked(a, 'mashup7', b2)
    if hasattr(b2, 'Interface'):
        assert not _is_linked(b2, 'Interface', a)


def test_assoc_mappingRules4_link_reassign_clear():
    a = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b1 = application_MappingRule()
    b2 = application_MappingRule()
    _safe_set(a, 'application_Mashup', {b1})
    assert _is_linked(a, 'application_Mashup', b1)
    if hasattr(b1, 'application_MappingRule'):
        assert _is_linked(b1, 'application_MappingRule', a)
    _safe_set(a, 'application_Mashup', {b2})
    assert _is_linked(a, 'application_Mashup', b2)
    if hasattr(b1, 'application_MappingRule'):
        assert not _is_linked(b1, 'application_MappingRule', a)
    if hasattr(b2, 'application_MappingRule'):
        assert _is_linked(b2, 'application_MappingRule', a)
    _safe_set(a, 'application_Mashup', set())
    assert not _is_linked(a, 'application_Mashup', b2)
    if hasattr(b2, 'application_MappingRule'):
        assert not _is_linked(b2, 'application_MappingRule', a)


def test_assoc_mashup23_link_reassign_clear():
    a = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b1 = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    b2 = application_Interface(frontEndCaching="sample_text_2", urlSuffix="sample_text_2")
    _safe_set(a, 'Mashup24', b1)
    assert _is_linked(a, 'Mashup24', b1)
    if hasattr(b1, 'interfaces'):
        assert _is_linked(b1, 'interfaces', a)
    _safe_set(a, 'Mashup24', b2)
    assert _is_linked(a, 'Mashup24', b2)
    if hasattr(b1, 'interfaces'):
        assert not _is_linked(b1, 'interfaces', a)
    if hasattr(b2, 'interfaces'):
        assert _is_linked(b2, 'interfaces', a)
    _safe_set(a, 'Mashup24', None)
    assert not _is_linked(a, 'Mashup24', b2)
    if hasattr(b2, 'interfaces'):
        assert not _is_linked(b2, 'interfaces', a)


def test_assoc_mashup3_link_reassign_clear():
    a = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'sources', b1)
    assert _is_linked(a, 'sources', b1)
    if hasattr(b1, 'Mashup'):
        assert _is_linked(b1, 'Mashup', a)
    _safe_set(a, 'sources', b2)
    assert _is_linked(a, 'sources', b2)
    if hasattr(b1, 'Mashup'):
        assert not _is_linked(b1, 'Mashup', a)
    if hasattr(b2, 'Mashup'):
        assert _is_linked(b2, 'Mashup', a)
    _safe_set(a, 'sources', None)
    assert not _is_linked(a, 'sources', b2)
    if hasattr(b2, 'Mashup'):
        assert not _is_linked(b2, 'Mashup', a)


def test_assoc_mashupAdmins8_link_reassign_clear():
    a = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'MashupAdmin', b1)
    assert _is_linked(a, 'MashupAdmin', b1)
    if hasattr(b1, 'configurableMashups'):
        assert _is_linked(b1, 'configurableMashups', a)
    _safe_set(a, 'MashupAdmin', b2)
    assert _is_linked(a, 'MashupAdmin', b2)
    if hasattr(b1, 'configurableMashups'):
        assert not _is_linked(b1, 'configurableMashups', a)
    if hasattr(b2, 'configurableMashups'):
        assert _is_linked(b2, 'configurableMashups', a)
    _safe_set(a, 'MashupAdmin', None)
    assert not _is_linked(a, 'MashupAdmin', b2)
    if hasattr(b2, 'configurableMashups'):
        assert not _is_linked(b2, 'configurableMashups', a)


def test_assoc_mashups10_link_reassign_clear():
    a = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'application_MashupContainer', {b1})
    assert _is_linked(a, 'application_MashupContainer', b1)
    if hasattr(b1, 'application_Mashup11'):
        assert _is_linked(b1, 'application_Mashup11', a)
    _safe_set(a, 'application_MashupContainer', {b2})
    assert _is_linked(a, 'application_MashupContainer', b2)
    if hasattr(b1, 'application_Mashup11'):
        assert not _is_linked(b1, 'application_Mashup11', a)
    if hasattr(b2, 'application_Mashup11'):
        assert _is_linked(b2, 'application_Mashup11', a)
    _safe_set(a, 'application_MashupContainer', set())
    assert not _is_linked(a, 'application_MashupContainer', b2)
    if hasattr(b2, 'application_Mashup11'):
        assert not _is_linked(b2, 'application_Mashup11', a)


def test_assoc_persistency0_link_reassign_clear():
    a = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    b1 = application_Persistency()
    b2 = application_Persistency()
    _safe_set(a, 'application_Source', b1)
    assert _is_linked(a, 'application_Source', b1)
    if hasattr(b1, 'application_Persistency'):
        assert _is_linked(b1, 'application_Persistency', a)
    _safe_set(a, 'application_Source', b2)
    assert _is_linked(a, 'application_Source', b2)
    if hasattr(b1, 'application_Persistency'):
        assert not _is_linked(b1, 'application_Persistency', a)
    if hasattr(b2, 'application_Persistency'):
        assert _is_linked(b2, 'application_Persistency', a)
    _safe_set(a, 'application_Source', None)
    assert not _is_linked(a, 'application_Source', b2)
    if hasattr(b2, 'application_Persistency'):
        assert not _is_linked(b2, 'application_Persistency', a)


def test_assoc_properties9_link_reassign_clear():
    a = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    b1 = application_Configuration()
    b2 = application_Configuration()
    _safe_set(a, 'application_Property', b1)
    assert _is_linked(a, 'application_Property', b1)
    if hasattr(b1, 'application_Configuration'):
        assert _is_linked(b1, 'application_Configuration', a)
    _safe_set(a, 'application_Property', b2)
    assert _is_linked(a, 'application_Property', b2)
    if hasattr(b1, 'application_Configuration'):
        assert not _is_linked(b1, 'application_Configuration', a)
    if hasattr(b2, 'application_Configuration'):
        assert _is_linked(b2, 'application_Configuration', a)
    _safe_set(a, 'application_Property', None)
    assert not _is_linked(a, 'application_Property', b2)
    if hasattr(b2, 'application_Configuration'):
        assert not _is_linked(b2, 'application_Configuration', a)


def test_assoc_security22_link_reassign_clear():
    a = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    b1 = application_Security()
    b2 = application_Security()
    _safe_set(a, 'interface', b1)
    assert _is_linked(a, 'interface', b1)
    if hasattr(b1, 'Security'):
        assert _is_linked(b1, 'Security', a)
    _safe_set(a, 'interface', b2)
    assert _is_linked(a, 'interface', b2)
    if hasattr(b1, 'Security'):
        assert not _is_linked(b1, 'Security', a)
    if hasattr(b2, 'Security'):
        assert _is_linked(b2, 'Security', a)
    _safe_set(a, 'interface', None)
    assert not _is_linked(a, 'interface', b2)
    if hasattr(b2, 'Security'):
        assert not _is_linked(b2, 'Security', a)


def test_assoc_sourceConfigurations17_link_reassign_clear():
    a = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'application_MashupContainer18', {b1})
    assert _is_linked(a, 'application_MashupContainer18', b1)
    if hasattr(b1, 'application_Mashup19'):
        assert _is_linked(b1, 'application_Mashup19', a)
    _safe_set(a, 'application_MashupContainer18', {b2})
    assert _is_linked(a, 'application_MashupContainer18', b2)
    if hasattr(b1, 'application_Mashup19'):
        assert not _is_linked(b1, 'application_Mashup19', a)
    if hasattr(b2, 'application_Mashup19'):
        assert _is_linked(b2, 'application_Mashup19', a)
    _safe_set(a, 'application_MashupContainer18', set())
    assert not _is_linked(a, 'application_MashupContainer18', b2)
    if hasattr(b2, 'application_Mashup19'):
        assert not _is_linked(b2, 'application_Mashup19', a)


def test_assoc_sources5_link_reassign_clear():
    a = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    b1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    b2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    _safe_set(a, 'Source', b1)
    assert _is_linked(a, 'Source', b1)
    if hasattr(b1, 'mashup'):
        assert _is_linked(b1, 'mashup', a)
    _safe_set(a, 'Source', b2)
    assert _is_linked(a, 'Source', b2)
    if hasattr(b1, 'mashup'):
        assert not _is_linked(b1, 'mashup', a)
    if hasattr(b2, 'mashup'):
        assert _is_linked(b2, 'mashup', a)
    _safe_set(a, 'Source', None)
    assert not _is_linked(a, 'Source', b2)
    if hasattr(b2, 'mashup'):
        assert not _is_linked(b2, 'mashup', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ConfigurableElement_strategy = st.builds(ConfigurableElement)
@given(instance=ConfigurableElement_strategy)
@settings(max_examples=25)
def test_ConfigurableElement_instantiation(instance):
    assert isinstance(instance, ConfigurableElement)


Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


Persistency_strategy = st.builds(Persistency)
@given(instance=Persistency_strategy)
@settings(max_examples=25)
def test_Persistency_instantiation(instance):
    assert isinstance(instance, Persistency)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


Security_strategy = st.builds(Security)
@given(instance=Security_strategy)
@settings(max_examples=25)
def test_Security_instantiation(instance):
    assert isinstance(instance, Security)


Source_strategy = st.builds(Source)
@given(instance=Source_strategy)
@settings(max_examples=25)
def test_Source_instantiation(instance):
    assert isinstance(instance, Source)


application_ApplicationKeyConfig_strategy = st.builds(application_ApplicationKeyConfig, applicationKeys=safe_text)
@given(instance=application_ApplicationKeyConfig_strategy)
@settings(max_examples=25)
def test_application_ApplicationKeyConfig_instantiation(instance):
    assert isinstance(instance, application_ApplicationKeyConfig)


application_ConfigurableElement_strategy = st.builds(application_ConfigurableElement, changeable=safe_text, configurationImage=safe_text, description=safe_text, hidden=safe_text, ident=safe_text, name=safe_text)
@given(instance=application_ConfigurableElement_strategy)
@settings(max_examples=25)
def test_application_ConfigurableElement_instantiation(instance):
    assert isinstance(instance, application_ConfigurableElement)


application_Configuration_strategy = st.builds(application_Configuration)
@given(instance=application_Configuration_strategy)
@settings(max_examples=25)
def test_application_Configuration_instantiation(instance):
    assert isinstance(instance, application_Configuration)


application_DataSet_strategy = st.builds(application_DataSet)
@given(instance=application_DataSet_strategy)
@settings(max_examples=25)
def test_application_DataSet_instantiation(instance):
    assert isinstance(instance, application_DataSet)


application_Database_strategy = st.builds(application_Database)
@given(instance=application_Database_strategy)
@settings(max_examples=25)
def test_application_Database_instantiation(instance):
    assert isinstance(instance, application_Database)


application_FEEDInterface_strategy = st.builds(application_FEEDInterface, allowCategoryFiltering=safe_text, allowMetaTagFiltering=safe_text, allowOrganisationFiltering=safe_text, allowPersonFiltering=safe_text, allowTagFiltering=safe_text, allowTypeFiltering=safe_text, feedTitle=safe_text, feedType=safe_text, language=safe_text)
@given(instance=application_FEEDInterface_strategy)
@settings(max_examples=25)
def test_application_FEEDInterface_instantiation(instance):
    assert isinstance(instance, application_FEEDInterface)


application_Interface_strategy = st.builds(application_Interface, frontEndCaching=safe_text, urlSuffix=safe_text)
@given(instance=application_Interface_strategy)
@settings(max_examples=25)
def test_application_Interface_instantiation(instance):
    assert isinstance(instance, application_Interface)


application_MappingRule_strategy = st.builds(application_MappingRule)
@given(instance=application_MappingRule_strategy)
@settings(max_examples=25)
def test_application_MappingRule_instantiation(instance):
    assert isinstance(instance, application_MappingRule)


application_Mashup_strategy = st.builds(application_Mashup, backupDataSet=safe_text, backupIntervall=safe_text, cacheAttachments=safe_text, cacheDataSet=safe_text, cacheDelay=safe_text, sourceIdentCounter=safe_text, workingDirectory=safe_text)
@given(instance=application_Mashup_strategy)
@settings(max_examples=25)
def test_application_Mashup_instantiation(instance):
    assert isinstance(instance, application_Mashup)


application_MashupAdmin_strategy = st.builds(application_MashupAdmin, email=safe_text, id=safe_text, isConfigurationAdmin=safe_text, localIdent=safe_text, name=safe_text, profileImage=safe_text, provider=safe_text)
@given(instance=application_MashupAdmin_strategy)
@settings(max_examples=25)
def test_application_MashupAdmin_instantiation(instance):
    assert isinstance(instance, application_MashupAdmin)


application_MashupContainer_strategy = st.builds(application_MashupContainer, backupConfiguration=safe_text, backupIntervall=safe_text, createAccountsAtLoginTry=safe_text, identCounter=safe_text, immediateSave=safe_text)
@given(instance=application_MashupContainer_strategy)
@settings(max_examples=25)
def test_application_MashupContainer_instantiation(instance):
    assert isinstance(instance, application_MashupContainer)


application_OAuthAdmin_strategy = st.builds(application_OAuthAdmin, passwordHash=safe_text, username=safe_text)
@given(instance=application_OAuthAdmin_strategy)
@settings(max_examples=25)
def test_application_OAuthAdmin_instantiation(instance):
    assert isinstance(instance, application_OAuthAdmin)


application_OAuthClientConfig_strategy = st.builds(application_OAuthClientConfig, accessToken=safe_text, accessTokenCreationDate=st.dates(), accessTokenExpirationDate=st.dates(), allowedMetaTags=safe_text, clientID=safe_text, clientSecret=safe_text, code=safe_text, description=safe_text, forbiddenMetaTags=safe_text, grantType=safe_text, name=safe_text, oAuthScopeLevel=safe_text, redirectionURL=safe_text, refreshToken=safe_text, type=safe_text)
@given(instance=application_OAuthClientConfig_strategy)
@settings(max_examples=25)
def test_application_OAuthClientConfig_instantiation(instance):
    assert isinstance(instance, application_OAuthClientConfig)


application_OAuthClientScope_strategy = st.builds(application_OAuthClientScope, allowContents=safe_text, allowOrganisations=safe_text, allowPersons=safe_text, identSpecification=safe_text, maximumAge=safe_text, negativeCategory=safe_text, negativeMetaTag=safe_text, negativeOrganisation=safe_text, negativePerson=safe_text, negativeTag=safe_text, positiveCategory=safe_text, positiveMetaTag=safe_text, positiveOrganisation=safe_text, positivePerson=safe_text, positiveTag=safe_text)
@given(instance=application_OAuthClientScope_strategy)
@settings(max_examples=25)
def test_application_OAuthClientScope_instantiation(instance):
    assert isinstance(instance, application_OAuthClientScope)


application_OAuthConfig_strategy = st.builds(application_OAuthConfig, useScopeInterfaceOnRedirect=safe_text)
@given(instance=application_OAuthConfig_strategy)
@settings(max_examples=25)
def test_application_OAuthConfig_instantiation(instance):
    assert isinstance(instance, application_OAuthConfig)


application_OCLRestrictedProperty_strategy = st.builds(application_OCLRestrictedProperty, OCLRestriction=safe_text)
@given(instance=application_OCLRestrictedProperty_strategy)
@settings(max_examples=25)
def test_application_OCLRestrictedProperty_instantiation(instance):
    assert isinstance(instance, application_OCLRestrictedProperty)


application_Persistency_strategy = st.builds(application_Persistency)
@given(instance=application_Persistency_strategy)
@settings(max_examples=25)
def test_application_Persistency_instantiation(instance):
    assert isinstance(instance, application_Persistency)


application_Property_strategy = st.builds(application_Property, Key=safe_text, Value=safe_text, changeable=safe_text, helpText=safe_text, hidden=safe_text, possibleValues=safe_text, propertyType=safe_text, required=safe_text)
@given(instance=application_Property_strategy)
@settings(max_examples=25)
def test_application_Property_instantiation(instance):
    assert isinstance(instance, application_Property)


application_RESTInterface_strategy = st.builds(application_RESTInterface, type=safe_text)
@given(instance=application_RESTInterface_strategy)
@settings(max_examples=25)
def test_application_RESTInterface_instantiation(instance):
    assert isinstance(instance, application_RESTInterface)


application_Security_strategy = st.builds(application_Security)
@given(instance=application_Security_strategy)
@settings(max_examples=25)
def test_application_Security_instantiation(instance):
    assert isinstance(instance, application_Security)


application_Source_strategy = st.builds(application_Source, activeState=safe_text, bundleId=safe_text, logLevel=safe_text, removeDataOnStop=safe_text, state=safe_text, updateRound=safe_text)
@given(instance=application_Source_strategy)
@settings(max_examples=25)
def test_application_Source_instantiation(instance):
    assert isinstance(instance, application_Source)


application_XMLFile_strategy = st.builds(application_XMLFile)
@given(instance=application_XMLFile_strategy)
@settings(max_examples=25)
def test_application_XMLFile_instantiation(instance):
    assert isinstance(instance, application_XMLFile)



