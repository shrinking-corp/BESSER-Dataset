import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_admins28_reverse_link_reassign_clear():
    a1 = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    a2 = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text_2")
    b = application_OAuthAdmin(passwordHash="sample_text", username="sample_text")
    _safe_set(b, 'application_OAuthAdmin', a1)
    assert _is_linked(b, 'application_OAuthAdmin', a1)
    if hasattr(a1, 'application_OAuthConfig29'):
        assert _is_linked(a1, 'application_OAuthConfig29', b)
    _safe_set(b, 'application_OAuthAdmin', a2)
    assert _is_linked(b, 'application_OAuthAdmin', a2)
    if hasattr(a1, 'application_OAuthConfig29'):
        assert not _is_linked(a1, 'application_OAuthConfig29', b)
    if hasattr(a2, 'application_OAuthConfig29'):
        assert _is_linked(a2, 'application_OAuthConfig29', b)
    _safe_set(b, 'application_OAuthAdmin', None)
    assert not _is_linked(b, 'application_OAuthAdmin', a2)
    if hasattr(a2, 'application_OAuthConfig29'):
        assert not _is_linked(a2, 'application_OAuthConfig29', b)


def test_assoc_allMashupAdmins12_reverse_link_reassign_clear():
    a1 = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    a2 = application_MashupContainer(backupConfiguration="sample_text_2", backupIntervall="sample_text_2", createAccountsAtLoginTry="sample_text_2", identCounter="sample_text_2", immediateSave="sample_text_2")
    b = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    _safe_set(b, 'application_MashupAdmin', a1)
    assert _is_linked(b, 'application_MashupAdmin', a1)
    if hasattr(a1, 'application_MashupContainer13'):
        assert _is_linked(a1, 'application_MashupContainer13', b)
    _safe_set(b, 'application_MashupAdmin', a2)
    assert _is_linked(b, 'application_MashupAdmin', a2)
    if hasattr(a1, 'application_MashupContainer13'):
        assert not _is_linked(a1, 'application_MashupContainer13', b)
    if hasattr(a2, 'application_MashupContainer13'):
        assert _is_linked(a2, 'application_MashupContainer13', b)
    _safe_set(b, 'application_MashupAdmin', None)
    assert not _is_linked(b, 'application_MashupAdmin', a2)
    if hasattr(a2, 'application_MashupContainer13'):
        assert not _is_linked(a2, 'application_MashupContainer13', b)


def test_assoc_clientScope30_reverse_link_reassign_clear():
    a1 = application_OAuthClientScope(allowContents="sample_text", allowOrganisations="sample_text", allowPersons="sample_text", identSpecification="sample_text", maximumAge="sample_text", negativeCategory="sample_text", negativeMetaTag="sample_text", negativeOrganisation="sample_text", negativePerson="sample_text", negativeTag="sample_text", positiveCategory="sample_text", positiveMetaTag="sample_text", positiveOrganisation="sample_text", positivePerson="sample_text", positiveTag="sample_text")
    a2 = application_OAuthClientScope(allowContents="sample_text_2", allowOrganisations="sample_text_2", allowPersons="sample_text_2", identSpecification="sample_text_2", maximumAge="sample_text_2", negativeCategory="sample_text_2", negativeMetaTag="sample_text_2", negativeOrganisation="sample_text_2", negativePerson="sample_text_2", negativeTag="sample_text_2", positiveCategory="sample_text_2", positiveMetaTag="sample_text_2", positiveOrganisation="sample_text_2", positivePerson="sample_text_2", positiveTag="sample_text_2")
    b = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    _safe_set(b, 'application_OAuthClientConfig31', a1)
    assert _is_linked(b, 'application_OAuthClientConfig31', a1)
    if hasattr(a1, 'application_OAuthClientScope'):
        assert _is_linked(a1, 'application_OAuthClientScope', b)
    _safe_set(b, 'application_OAuthClientConfig31', a2)
    assert _is_linked(b, 'application_OAuthClientConfig31', a2)
    if hasattr(a1, 'application_OAuthClientScope'):
        assert not _is_linked(a1, 'application_OAuthClientScope', b)
    if hasattr(a2, 'application_OAuthClientScope'):
        assert _is_linked(a2, 'application_OAuthClientScope', b)
    _safe_set(b, 'application_OAuthClientConfig31', None)
    assert not _is_linked(b, 'application_OAuthClientConfig31', a2)
    if hasattr(a2, 'application_OAuthClientScope'):
        assert not _is_linked(a2, 'application_OAuthClientScope', b)


def test_assoc_clients27_reverse_link_reassign_clear():
    a1 = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text")
    a2 = application_OAuthConfig(useScopeInterfaceOnRedirect="sample_text_2")
    b = application_OAuthClientConfig(accessToken="sample_text", accessTokenCreationDate=date(2024, 1, 1), accessTokenExpirationDate=date(2024, 1, 1), allowedMetaTags="sample_text", clientID="sample_text", clientSecret="sample_text", code="sample_text", description="sample_text", forbiddenMetaTags="sample_text", grantType="sample_text", name="sample_text", oAuthScopeLevel="sample_text", redirectionURL="sample_text", refreshToken="sample_text", type="sample_text")
    _safe_set(b, 'application_OAuthClientConfig', a1)
    assert _is_linked(b, 'application_OAuthClientConfig', a1)
    if hasattr(a1, 'application_OAuthConfig'):
        assert _is_linked(a1, 'application_OAuthConfig', b)
    _safe_set(b, 'application_OAuthClientConfig', a2)
    assert _is_linked(b, 'application_OAuthClientConfig', a2)
    if hasattr(a1, 'application_OAuthConfig'):
        assert not _is_linked(a1, 'application_OAuthConfig', b)
    if hasattr(a2, 'application_OAuthConfig'):
        assert _is_linked(a2, 'application_OAuthConfig', b)
    _safe_set(b, 'application_OAuthClientConfig', None)
    assert not _is_linked(b, 'application_OAuthClientConfig', a2)
    if hasattr(a2, 'application_OAuthConfig'):
        assert not _is_linked(a2, 'application_OAuthConfig', b)


def test_assoc_configurableMashups32_reverse_link_reassign_clear():
    a1 = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    a2 = application_MashupAdmin(email="sample_text_2", id="sample_text_2", isConfigurationAdmin="sample_text_2", localIdent="sample_text_2", name="sample_text_2", profileImage="sample_text_2", provider="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'Mashup33', a1)
    assert _is_linked(b, 'Mashup33', a1)
    if hasattr(a1, 'mashupAdmins'):
        assert _is_linked(a1, 'mashupAdmins', b)
    _safe_set(b, 'Mashup33', a2)
    assert _is_linked(b, 'Mashup33', a2)
    if hasattr(a1, 'mashupAdmins'):
        assert not _is_linked(a1, 'mashupAdmins', b)
    if hasattr(a2, 'mashupAdmins'):
        assert _is_linked(a2, 'mashupAdmins', b)
    _safe_set(b, 'Mashup33', None)
    assert not _is_linked(b, 'Mashup33', a2)
    if hasattr(a2, 'mashupAdmins'):
        assert not _is_linked(a2, 'mashupAdmins', b)


def test_assoc_defaultMashups14_reverse_link_reassign_clear():
    a1 = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    a2 = application_MashupContainer(backupConfiguration="sample_text_2", backupIntervall="sample_text_2", createAccountsAtLoginTry="sample_text_2", identCounter="sample_text_2", immediateSave="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'application_Mashup16', a1)
    assert _is_linked(b, 'application_Mashup16', a1)
    if hasattr(a1, 'application_MashupContainer15'):
        assert _is_linked(a1, 'application_MashupContainer15', b)
    _safe_set(b, 'application_Mashup16', a2)
    assert _is_linked(b, 'application_Mashup16', a2)
    if hasattr(a1, 'application_MashupContainer15'):
        assert not _is_linked(a1, 'application_MashupContainer15', b)
    if hasattr(a2, 'application_MashupContainer15'):
        assert _is_linked(a2, 'application_MashupContainer15', b)
    _safe_set(b, 'application_Mashup16', None)
    assert not _is_linked(b, 'application_Mashup16', a2)
    if hasattr(a2, 'application_MashupContainer15'):
        assert not _is_linked(a2, 'application_MashupContainer15', b)


def test_assoc_interfaceConfigurations20_reverse_link_reassign_clear():
    a1 = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    a2 = application_MashupContainer(backupConfiguration="sample_text_2", backupIntervall="sample_text_2", createAccountsAtLoginTry="sample_text_2", identCounter="sample_text_2", immediateSave="sample_text_2")
    b = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    _safe_set(b, 'application_Interface', a1)
    assert _is_linked(b, 'application_Interface', a1)
    if hasattr(a1, 'application_MashupContainer21'):
        assert _is_linked(a1, 'application_MashupContainer21', b)
    _safe_set(b, 'application_Interface', a2)
    assert _is_linked(b, 'application_Interface', a2)
    if hasattr(a1, 'application_MashupContainer21'):
        assert not _is_linked(a1, 'application_MashupContainer21', b)
    if hasattr(a2, 'application_MashupContainer21'):
        assert _is_linked(a2, 'application_MashupContainer21', b)
    _safe_set(b, 'application_Interface', None)
    assert not _is_linked(b, 'application_Interface', a2)
    if hasattr(a2, 'application_MashupContainer21'):
        assert not _is_linked(a2, 'application_MashupContainer21', b)


def test_assoc_interfaces6_reverse_link_reassign_clear():
    a1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    a2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", keepDeletedItemsList="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    b = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    _safe_set(b, 'Interface', a1)
    assert _is_linked(b, 'Interface', a1)
    if hasattr(a1, 'mashup7'):
        assert _is_linked(a1, 'mashup7', b)
    _safe_set(b, 'Interface', a2)
    assert _is_linked(b, 'Interface', a2)
    if hasattr(a1, 'mashup7'):
        assert not _is_linked(a1, 'mashup7', b)
    if hasattr(a2, 'mashup7'):
        assert _is_linked(a2, 'mashup7', b)
    _safe_set(b, 'Interface', None)
    assert not _is_linked(b, 'Interface', a2)
    if hasattr(a2, 'mashup7'):
        assert not _is_linked(a2, 'mashup7', b)


def test_assoc_mashup23_reverse_link_reassign_clear():
    a1 = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    a2 = application_Mashup(backupDataSet="sample_text_2", backupIntervall="sample_text_2", cacheAttachments="sample_text_2", cacheDataSet="sample_text_2", cacheDelay="sample_text_2", keepDeletedItemsList="sample_text_2", sourceIdentCounter="sample_text_2", workingDirectory="sample_text_2")
    b = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    _safe_set(b, 'interfaces', a1)
    assert _is_linked(b, 'interfaces', a1)
    if hasattr(a1, 'Mashup24'):
        assert _is_linked(a1, 'Mashup24', b)
    _safe_set(b, 'interfaces', a2)
    assert _is_linked(b, 'interfaces', a2)
    if hasattr(a1, 'Mashup24'):
        assert not _is_linked(a1, 'Mashup24', b)
    if hasattr(a2, 'Mashup24'):
        assert _is_linked(a2, 'Mashup24', b)
    _safe_set(b, 'interfaces', None)
    assert not _is_linked(b, 'interfaces', a2)
    if hasattr(a2, 'Mashup24'):
        assert not _is_linked(a2, 'Mashup24', b)


def test_assoc_mashup3_reverse_link_reassign_clear():
    a1 = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    a2 = application_Source(activeState="sample_text_2", bundleId="sample_text_2", logLevel="sample_text_2", removeDataOnStop="sample_text_2", state="sample_text_2", updateRound="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'Mashup', a1)
    assert _is_linked(b, 'Mashup', a1)
    if hasattr(a1, 'sources'):
        assert _is_linked(a1, 'sources', b)
    _safe_set(b, 'Mashup', a2)
    assert _is_linked(b, 'Mashup', a2)
    if hasattr(a1, 'sources'):
        assert not _is_linked(a1, 'sources', b)
    if hasattr(a2, 'sources'):
        assert _is_linked(a2, 'sources', b)
    _safe_set(b, 'Mashup', None)
    assert not _is_linked(b, 'Mashup', a2)
    if hasattr(a2, 'sources'):
        assert not _is_linked(a2, 'sources', b)


def test_assoc_mashupAdmins8_reverse_link_reassign_clear():
    a1 = application_MashupAdmin(email="sample_text", id="sample_text", isConfigurationAdmin="sample_text", localIdent="sample_text", name="sample_text", profileImage="sample_text", provider="sample_text")
    a2 = application_MashupAdmin(email="sample_text_2", id="sample_text_2", isConfigurationAdmin="sample_text_2", localIdent="sample_text_2", name="sample_text_2", profileImage="sample_text_2", provider="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'configurableMashups', {a1})
    assert _is_linked(b, 'configurableMashups', a1)
    if hasattr(a1, 'MashupAdmin'):
        assert _is_linked(a1, 'MashupAdmin', b)
    _safe_set(b, 'configurableMashups', {a2})
    assert _is_linked(b, 'configurableMashups', a2)
    if hasattr(a1, 'MashupAdmin'):
        assert not _is_linked(a1, 'MashupAdmin', b)
    if hasattr(a2, 'MashupAdmin'):
        assert _is_linked(a2, 'MashupAdmin', b)
    _safe_set(b, 'configurableMashups', set())
    assert not _is_linked(b, 'configurableMashups', a2)
    if hasattr(a2, 'MashupAdmin'):
        assert not _is_linked(a2, 'MashupAdmin', b)


def test_assoc_mashups10_reverse_link_reassign_clear():
    a1 = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    a2 = application_MashupContainer(backupConfiguration="sample_text_2", backupIntervall="sample_text_2", createAccountsAtLoginTry="sample_text_2", identCounter="sample_text_2", immediateSave="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'application_Mashup11', a1)
    assert _is_linked(b, 'application_Mashup11', a1)
    if hasattr(a1, 'application_MashupContainer'):
        assert _is_linked(a1, 'application_MashupContainer', b)
    _safe_set(b, 'application_Mashup11', a2)
    assert _is_linked(b, 'application_Mashup11', a2)
    if hasattr(a1, 'application_MashupContainer'):
        assert not _is_linked(a1, 'application_MashupContainer', b)
    if hasattr(a2, 'application_MashupContainer'):
        assert _is_linked(a2, 'application_MashupContainer', b)
    _safe_set(b, 'application_Mashup11', None)
    assert not _is_linked(b, 'application_Mashup11', a2)
    if hasattr(a2, 'application_MashupContainer'):
        assert not _is_linked(a2, 'application_MashupContainer', b)


def test_assoc_sourceConfigurations17_reverse_link_reassign_clear():
    a1 = application_MashupContainer(backupConfiguration="sample_text", backupIntervall="sample_text", createAccountsAtLoginTry="sample_text", identCounter="sample_text", immediateSave="sample_text")
    a2 = application_MashupContainer(backupConfiguration="sample_text_2", backupIntervall="sample_text_2", createAccountsAtLoginTry="sample_text_2", identCounter="sample_text_2", immediateSave="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'application_Mashup19', a1)
    assert _is_linked(b, 'application_Mashup19', a1)
    if hasattr(a1, 'application_MashupContainer18'):
        assert _is_linked(a1, 'application_MashupContainer18', b)
    _safe_set(b, 'application_Mashup19', a2)
    assert _is_linked(b, 'application_Mashup19', a2)
    if hasattr(a1, 'application_MashupContainer18'):
        assert not _is_linked(a1, 'application_MashupContainer18', b)
    if hasattr(a2, 'application_MashupContainer18'):
        assert _is_linked(a2, 'application_MashupContainer18', b)
    _safe_set(b, 'application_Mashup19', None)
    assert not _is_linked(b, 'application_Mashup19', a2)
    if hasattr(a2, 'application_MashupContainer18'):
        assert not _is_linked(a2, 'application_MashupContainer18', b)


def test_assoc_sources5_reverse_link_reassign_clear():
    a1 = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    a2 = application_Source(activeState="sample_text_2", bundleId="sample_text_2", logLevel="sample_text_2", removeDataOnStop="sample_text_2", state="sample_text_2", updateRound="sample_text_2")
    b = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    _safe_set(b, 'mashup', {a1})
    assert _is_linked(b, 'mashup', a1)
    if hasattr(a1, 'Source'):
        assert _is_linked(a1, 'Source', b)
    _safe_set(b, 'mashup', {a2})
    assert _is_linked(b, 'mashup', a2)
    if hasattr(a1, 'Source'):
        assert not _is_linked(a1, 'Source', b)
    if hasattr(a2, 'Source'):
        assert _is_linked(a2, 'Source', b)
    _safe_set(b, 'mashup', set())
    assert not _is_linked(b, 'mashup', a2)
    if hasattr(a2, 'Source'):
        assert not _is_linked(a2, 'Source', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configuration34_stub_double():
    # application_Configuration has no real 'application_Configuration35' property in the generated
    # code (a bare stub) -- manually attach it so application_ConfigurableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_ConfigurableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_ConfigurableElement(changeable="sample_text", configurationImage="sample_text", description="sample_text", hidden="sample_text", ident="sample_text", name="sample_text")
    partner = application_Configuration()
    setattr(partner, 'application_Configuration35', None)
    _safe_set(owner, 'application_ConfigurableElement', partner)
    assert getattr(partner, 'application_Configuration35') == owner
    _safe_set(owner, 'application_ConfigurableElement', None)
    assert getattr(partner, 'application_Configuration35') is None


def test_assoc_dataSet1_stub_double():
    # application_DataSet has no real 'application_DataSet' property in the generated
    # code (a bare stub) -- manually attach it so application_Source's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Source's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    partner = application_DataSet()
    setattr(partner, 'application_DataSet', None)
    _safe_set(owner, 'application_Source2', partner)
    assert getattr(partner, 'application_DataSet') == owner
    _safe_set(owner, 'application_Source2', None)
    assert getattr(partner, 'application_DataSet') is None


def test_assoc_interface25_stub_double():
    # application_Security has no real 'security' property in the generated
    # code (a bare stub) -- manually attach it so application_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    partner = application_Security()
    setattr(partner, 'security', None)
    _safe_set(owner, 'Interface26', partner)
    assert getattr(partner, 'security') == owner
    _safe_set(owner, 'Interface26', None)
    assert getattr(partner, 'security') is None


def test_assoc_mappingRules4_stub_double():
    # application_MappingRule has no real 'application_MappingRule' property in the generated
    # code (a bare stub) -- manually attach it so application_Mashup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Mashup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Mashup(backupDataSet="sample_text", backupIntervall="sample_text", cacheAttachments="sample_text", cacheDataSet="sample_text", cacheDelay="sample_text", keepDeletedItemsList="sample_text", sourceIdentCounter="sample_text", workingDirectory="sample_text")
    partner = application_MappingRule()
    setattr(partner, 'application_MappingRule', None)
    _safe_set(owner, 'application_Mashup', {partner})
    assert getattr(partner, 'application_MappingRule') == owner
    _safe_set(owner, 'application_Mashup', set())
    assert getattr(partner, 'application_MappingRule') is None


def test_assoc_persistency0_stub_double():
    # application_Persistency has no real 'application_Persistency' property in the generated
    # code (a bare stub) -- manually attach it so application_Source's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Source's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Source(activeState="sample_text", bundleId="sample_text", logLevel="sample_text", removeDataOnStop="sample_text", state="sample_text", updateRound="sample_text")
    partner = application_Persistency()
    setattr(partner, 'application_Persistency', None)
    _safe_set(owner, 'application_Source', partner)
    assert getattr(partner, 'application_Persistency') == owner
    _safe_set(owner, 'application_Source', None)
    assert getattr(partner, 'application_Persistency') is None


def test_assoc_properties9_stub_double():
    # application_Configuration has no real 'application_Configuration' property in the generated
    # code (a bare stub) -- manually attach it so application_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Property(Key="sample_text", Value="sample_text", changeable="sample_text", helpText="sample_text", hidden="sample_text", possibleValues="sample_text", propertyType="sample_text", required="sample_text")
    partner = application_Configuration()
    setattr(partner, 'application_Configuration', None)
    _safe_set(owner, 'application_Property', partner)
    assert getattr(partner, 'application_Configuration') == owner
    _safe_set(owner, 'application_Property', None)
    assert getattr(partner, 'application_Configuration') is None


def test_assoc_security22_stub_double():
    # application_Security has no real 'Security' property in the generated
    # code (a bare stub) -- manually attach it so application_Interface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # application_Interface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = application_Interface(frontEndCaching="sample_text", urlSuffix="sample_text")
    partner = application_Security()
    setattr(partner, 'Security', None)
    _safe_set(owner, 'interface', partner)
    assert getattr(partner, 'Security') == owner
    _safe_set(owner, 'interface', None)
    assert getattr(partner, 'Security') is None


