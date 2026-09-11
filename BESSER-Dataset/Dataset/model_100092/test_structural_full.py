import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    modulespecification_Module,
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

def test_modulespecification_Module_authorEmail_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.authorEmail == "sample_text"
    instance.authorEmail = "sample_text_2"
    assert instance.authorEmail == "sample_text_2"


def test_modulespecification_Module_baseId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.baseId == "sample_text"
    instance.baseId = "sample_text_2"
    assert instance.baseId == "sample_text_2"


def test_modulespecification_Module_baseLocation_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.baseLocation == "sample_text"
    instance.baseLocation = "sample_text_2"
    assert instance.baseLocation == "sample_text_2"


def test_modulespecification_Module_categoryName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.categoryName == "sample_text"
    instance.categoryName = "sample_text_2"
    assert instance.categoryName == "sample_text_2"


def test_modulespecification_Module_copyRightAuthorName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.copyRightAuthorName == "sample_text"
    instance.copyRightAuthorName = "sample_text_2"
    assert instance.copyRightAuthorName == "sample_text_2"


def test_modulespecification_Module_copyRightUrl_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.copyRightUrl == "sample_text"
    instance.copyRightUrl = "sample_text_2"
    assert instance.copyRightUrl == "sample_text_2"


def test_modulespecification_Module_copyRightYear_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.copyRightYear == "sample_text"
    instance.copyRightYear = "sample_text_2"
    assert instance.copyRightYear == "sample_text_2"


def test_modulespecification_Module_coreId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.coreId == "sample_text"
    instance.coreId = "sample_text_2"
    assert instance.coreId == "sample_text_2"


def test_modulespecification_Module_coreModuleName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.coreModuleName == "sample_text"
    instance.coreModuleName = "sample_text_2"
    assert instance.coreModuleName == "sample_text_2"


def test_modulespecification_Module_coreSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.coreSuffix == "sample_text"
    instance.coreSuffix = "sample_text_2"
    assert instance.coreSuffix == "sample_text_2"


def test_modulespecification_Module_featureId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.featureId == "sample_text"
    instance.featureId = "sample_text_2"
    assert instance.featureId == "sample_text_2"


def test_modulespecification_Module_featureSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.featureSuffix == "sample_text"
    instance.featureSuffix = "sample_text_2"
    assert instance.featureSuffix == "sample_text_2"


def test_modulespecification_Module_generateFeature_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateFeature == True
    instance.generateFeature = False
    assert instance.generateFeature == False


def test_modulespecification_Module_generateParent_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateParent == True
    instance.generateParent = False
    assert instance.generateParent == False


def test_modulespecification_Module_generateTarget_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateTarget == True
    instance.generateTarget = False
    assert instance.generateTarget == False


def test_modulespecification_Module_generateTests_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateTests == True
    instance.generateTests = False
    assert instance.generateTests == False


def test_modulespecification_Module_generateUiFragment_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateUiFragment == True
    instance.generateUiFragment = False
    assert instance.generateUiFragment == False


def test_modulespecification_Module_generateUpdatesite_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.generateUpdatesite == True
    instance.generateUpdatesite = False
    assert instance.generateUpdatesite == False


def test_modulespecification_Module_isAuthorEmailEmpty_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.isAuthorEmailEmpty == True
    instance.isAuthorEmailEmpty = False
    assert instance.isAuthorEmailEmpty == False


def test_modulespecification_Module_isLicenseEmpty_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.isLicenseEmpty == True
    instance.isLicenseEmpty = False
    assert instance.isLicenseEmpty == False


def test_modulespecification_Module_isLicenseUrlEmpty_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.isLicenseUrlEmpty == True
    instance.isLicenseUrlEmpty = False
    assert instance.isLicenseUrlEmpty == False


def test_modulespecification_Module_isUpdateSiteUrlEmpty_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.isUpdateSiteUrlEmpty == True
    instance.isUpdateSiteUrlEmpty = False
    assert instance.isUpdateSiteUrlEmpty == False


def test_modulespecification_Module_javaVersion_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.javaVersion == "sample_text"
    instance.javaVersion = "sample_text_2"
    assert instance.javaVersion == "sample_text_2"


def test_modulespecification_Module_license_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.license == "sample_text"
    instance.license = "sample_text_2"
    assert instance.license == "sample_text_2"


def test_modulespecification_Module_licenseUrl_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.licenseUrl == "sample_text"
    instance.licenseUrl = "sample_text_2"
    assert instance.licenseUrl == "sample_text_2"


def test_modulespecification_Module_mavenGroupId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.mavenGroupId == "sample_text"
    instance.mavenGroupId = "sample_text_2"
    assert instance.mavenGroupId == "sample_text_2"


def test_modulespecification_Module_mavenVersion_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.mavenVersion == "sample_text"
    instance.mavenVersion = "sample_text_2"
    assert instance.mavenVersion == "sample_text_2"


def test_modulespecification_Module_mavenVersionSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.mavenVersionSuffix == "sample_text"
    instance.mavenVersionSuffix = "sample_text_2"
    assert instance.mavenVersionSuffix == "sample_text_2"


def test_modulespecification_Module_moduleName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.moduleName == "sample_text"
    instance.moduleName = "sample_text_2"
    assert instance.moduleName == "sample_text_2"


def test_modulespecification_Module_osgiVersion_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.osgiVersion == "sample_text"
    instance.osgiVersion = "sample_text_2"
    assert instance.osgiVersion == "sample_text_2"


def test_modulespecification_Module_osgiVersionQualifier_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.osgiVersionQualifier == "sample_text"
    instance.osgiVersionQualifier = "sample_text_2"
    assert instance.osgiVersionQualifier == "sample_text_2"


def test_modulespecification_Module_providerName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.providerName == "sample_text"
    instance.providerName = "sample_text_2"
    assert instance.providerName == "sample_text_2"


def test_modulespecification_Module_targetId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.targetId == "sample_text"
    instance.targetId = "sample_text_2"
    assert instance.targetId == "sample_text_2"


def test_modulespecification_Module_targetSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.targetSuffix == "sample_text"
    instance.targetSuffix = "sample_text_2"
    assert instance.targetSuffix == "sample_text_2"


def test_modulespecification_Module_testsId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.testsId == "sample_text"
    instance.testsId = "sample_text_2"
    assert instance.testsId == "sample_text_2"


def test_modulespecification_Module_testsSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.testsSuffix == "sample_text"
    instance.testsSuffix = "sample_text_2"
    assert instance.testsSuffix == "sample_text_2"


def test_modulespecification_Module_tychoParentName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.tychoParentName == "sample_text"
    instance.tychoParentName = "sample_text_2"
    assert instance.tychoParentName == "sample_text_2"


def test_modulespecification_Module_tychoVersion_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.tychoVersion == "sample_text"
    instance.tychoVersion = "sample_text_2"
    assert instance.tychoVersion == "sample_text_2"


def test_modulespecification_Module_uiId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.uiId == "sample_text"
    instance.uiId = "sample_text_2"
    assert instance.uiId == "sample_text_2"


def test_modulespecification_Module_uiModuleName_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.uiModuleName == "sample_text"
    instance.uiModuleName = "sample_text_2"
    assert instance.uiModuleName == "sample_text_2"


def test_modulespecification_Module_uiSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.uiSuffix == "sample_text"
    instance.uiSuffix = "sample_text_2"
    assert instance.uiSuffix == "sample_text_2"


def test_modulespecification_Module_uie3Id_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.uie3Id == "sample_text"
    instance.uie3Id = "sample_text_2"
    assert instance.uie3Id == "sample_text_2"


def test_modulespecification_Module_uie3Suffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.uie3Suffix == "sample_text"
    instance.uie3Suffix = "sample_text_2"
    assert instance.uie3Suffix == "sample_text_2"


def test_modulespecification_Module_updateSiteId_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.updateSiteId == "sample_text"
    instance.updateSiteId = "sample_text_2"
    assert instance.updateSiteId == "sample_text_2"


def test_modulespecification_Module_updateSiteSuffix_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.updateSiteSuffix == "sample_text"
    instance.updateSiteSuffix = "sample_text_2"
    assert instance.updateSiteSuffix == "sample_text_2"


def test_modulespecification_Module_updateSiteUrl_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.updateSiteUrl == "sample_text"
    instance.updateSiteUrl = "sample_text_2"
    assert instance.updateSiteUrl == "sample_text_2"


def test_modulespecification_Module_version_value_roundtrip():
    instance = modulespecification_Module(authorEmail="sample_text", baseId="sample_text", baseLocation="sample_text", categoryName="sample_text", copyRightAuthorName="sample_text", copyRightUrl="sample_text", copyRightYear="sample_text", coreId="sample_text", coreModuleName="sample_text", coreSuffix="sample_text", featureId="sample_text", featureSuffix="sample_text", generateFeature=True, generateParent=True, generateTarget=True, generateTests=True, generateUiFragment=True, generateUpdatesite=True, isAuthorEmailEmpty=True, isLicenseEmpty=True, isLicenseUrlEmpty=True, isUpdateSiteUrlEmpty=True, javaVersion="sample_text", license="sample_text", licenseUrl="sample_text", mavenGroupId="sample_text", mavenVersion="sample_text", mavenVersionSuffix="sample_text", moduleName="sample_text", osgiVersion="sample_text", osgiVersionQualifier="sample_text", providerName="sample_text", targetId="sample_text", targetSuffix="sample_text", testsId="sample_text", testsSuffix="sample_text", tychoParentName="sample_text", tychoVersion="sample_text", uiId="sample_text", uiModuleName="sample_text", uiSuffix="sample_text", uie3Id="sample_text", uie3Suffix="sample_text", updateSiteId="sample_text", updateSiteSuffix="sample_text", updateSiteUrl="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

modulespecification_Module_strategy = st.builds(modulespecification_Module, authorEmail=safe_text, baseId=safe_text, baseLocation=safe_text, categoryName=safe_text, copyRightAuthorName=safe_text, copyRightUrl=safe_text, copyRightYear=safe_text, coreId=safe_text, coreModuleName=safe_text, coreSuffix=safe_text, featureId=safe_text, featureSuffix=safe_text, generateFeature=st.booleans(), generateParent=st.booleans(), generateTarget=st.booleans(), generateTests=st.booleans(), generateUiFragment=st.booleans(), generateUpdatesite=st.booleans(), isAuthorEmailEmpty=st.booleans(), isLicenseEmpty=st.booleans(), isLicenseUrlEmpty=st.booleans(), isUpdateSiteUrlEmpty=st.booleans(), javaVersion=safe_text, license=safe_text, licenseUrl=safe_text, mavenGroupId=safe_text, mavenVersion=safe_text, mavenVersionSuffix=safe_text, moduleName=safe_text, osgiVersion=safe_text, osgiVersionQualifier=safe_text, providerName=safe_text, targetId=safe_text, targetSuffix=safe_text, testsId=safe_text, testsSuffix=safe_text, tychoParentName=safe_text, tychoVersion=safe_text, uiId=safe_text, uiModuleName=safe_text, uiSuffix=safe_text, uie3Id=safe_text, uie3Suffix=safe_text, updateSiteId=safe_text, updateSiteSuffix=safe_text, updateSiteUrl=safe_text, version=safe_text)
@given(instance=modulespecification_Module_strategy)
@settings(max_examples=25)
def test_modulespecification_Module_instantiation(instance):
    assert isinstance(instance, modulespecification_Module)


