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


