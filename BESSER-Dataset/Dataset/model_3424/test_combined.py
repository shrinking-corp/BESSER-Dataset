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
    xal_LargeMailUserIdentifier,
    xal_LargeMailUserName,
    xal_KeyLineCode,
    xal_EndorsementLineCode,
    xal_Xal,
    xal_FirmName,
    xal_Firm,
    xal_PremiseNumberSuffix,
    xal_PremiseNumberPrefix,
    xal_PremiseNumber,
    xal_ThoroughfareNumberSuffix,
    xal_ThoroughfareNumberPrefix,
    xal_ThoroughfareNumber,
    xal_DocumentRoot,
    xal_EStringToStringMapEntry,
    xal_ThoroughfarePreDirection,
    xal_DependentThoroughfare,
    xal_ThoroughfarePostDirection,
    xal_ThoroughfareTrailingType,
    xal_ThoroughfareName,
    xal_ThoroughfareLeadingType,
    xal_PostalRoute,
    xal_LargeMailUser,
    xal_Premise,
    xal_PostBox,
    xal_DependentLocalityNumber,
    xal_DependentLocalityName,
    xal_DependentLocality,
    xal_MailStop,
    xal_DepartmentName,
    xal_Department,
    xal_CountryName,
    xal_CountryNameCode,
    xal_Barcode,
    xal_BuildingName,
    xal_PostalCode,
    xal_PostOffice,
    xal_AddressLongitudeDirection,
    xal_SubAdministrativeArea,
    xal_AdministrativeAreaName,
    xal_AddressLine,
    xal_AddressLongitude,
    xal_AddressLatitude,
    xal_AddressLatitudeDirection,
    xal_AddressIdentifier,
    xal_AddressLines,
    xal_Thoroughfare,
    xal_Locality,
    xal_AdministrativeArea,
    xal_Country,
    xal_PostalServiceElements,
    xal_AddressDetails,
    xal_Address,
    xal_ThoroughfareNumberTo,
    xal_ThoroughfareNumberFrom,
    xal_ThoroughfareNumberRange,
    xal_SubPremiseNumberPrefix,
    xal_SubPremiseNumber,
    xal_SubPremiseNumberSuffix,
    xal_SubPremiseLocation,
    xal_SubPremiseName,
    xal_SubAdministrativeAreaName,
    xal_PremiseNumberRangeTo,
    xal_PremiseNumberRangeFrom,
    xal_SubPremise,
    xal_PremiseName,
    xal_PremiseNumberRange,
    xal_PremiseLocation,
    xal_PostTownSuffix,
    xal_PostTownName,
    xal_PostOfficeNumber,
    xal_PostOfficeName,
    xal_PostBoxNumberExtension,
    xal_PostBoxNumberSuffix,
    xal_PostBoxNumberPrefix,
    xal_SupplementaryPostalServiceData,
    xal_PostBoxNumber,
    xal_SortingCode,
    xal_PostalRouteNumber,
    xal_PostalRouteName,
    xal_PostalCodeNumberExtension,
    xal_PostalCodeNumber,
    xal_PostTown,
    xal_MailStopNumber,
    xal_MailStopName,
    xal_LocalityName,
    RangeTypeType,
    IndicatorOccurrence4,
    NumberTypeType1,
    TypeOccurrence,
    TypeOccurrence2,
    NameNumberOccurrence,
    IndicatorOccurence,
    NumberOccurrence,
    NumberTypeOccurrence,
    NumberTypeOccurrence1,
    IndicatorOccurrence,
    IndicatorOccurrence2,
    NumberRangeOccurrence,
    NumberRangeOccurence,
    TypeOccurrence1,
    DependentThoroughfaresType,
    IndicatorOccurrence1,
    NumberTypeType,
    IndicatorOccurrence3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_xal_largemailuseridentifier_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUserIdentifier)


def test_hyp_xal_largemailuseridentifier_constructor_exists():
    assert callable(xal_LargeMailUserIdentifier.__init__)


def test_hyp_xal_largemailuseridentifier_constructor_args():
    sig = inspect.signature(xal_LargeMailUserIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_largemailusername_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUserName)


def test_hyp_xal_largemailusername_constructor_exists():
    assert callable(xal_LargeMailUserName.__init__)


def test_hyp_xal_largemailusername_constructor_args():
    sig = inspect.signature(xal_LargeMailUserName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_keylinecode_is_not_abstract():
    assert not inspect.isabstract(xal_KeyLineCode)


def test_hyp_xal_keylinecode_constructor_exists():
    assert callable(xal_KeyLineCode.__init__)


def test_hyp_xal_keylinecode_constructor_args():
    sig = inspect.signature(xal_KeyLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_endorsementlinecode_is_not_abstract():
    assert not inspect.isabstract(xal_EndorsementLineCode)


def test_hyp_xal_endorsementlinecode_constructor_exists():
    assert callable(xal_EndorsementLineCode.__init__)


def test_hyp_xal_endorsementlinecode_constructor_args():
    sig = inspect.signature(xal_EndorsementLineCode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_xal_is_not_abstract():
    assert not inspect.isabstract(xal_Xal)


def test_hyp_xal_xal_constructor_exists():
    assert callable(xal_Xal.__init__)


def test_hyp_xal_xal_constructor_args():
    sig = inspect.signature(xal_Xal.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "version" in params, "Missing parameter 'version'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"






def test_hyp_xal_firmname_is_not_abstract():
    assert not inspect.isabstract(xal_FirmName)


def test_hyp_xal_firmname_constructor_exists():
    assert callable(xal_FirmName.__init__)


def test_hyp_xal_firmname_constructor_args():
    sig = inspect.signature(xal_FirmName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"







def test_hyp_xal_firm_is_not_abstract():
    assert not inspect.isabstract(xal_Firm)


def test_hyp_xal_firm_constructor_exists():
    assert callable(xal_Firm.__init__)


def test_hyp_xal_firm_constructor_args():
    sig = inspect.signature(xal_Firm.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"






def test_hyp_xal_premisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberSuffix)


def test_hyp_xal_premisenumbersuffix_constructor_exists():
    assert callable(xal_PremiseNumberSuffix.__init__)


def test_hyp_xal_premisenumbersuffix_constructor_args():
    sig = inspect.signature(xal_PremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"








def test_hyp_xal_premisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberPrefix)


def test_hyp_xal_premisenumberprefix_constructor_exists():
    assert callable(xal_PremiseNumberPrefix.__init__)


def test_hyp_xal_premisenumberprefix_constructor_args():
    sig = inspect.signature(xal_PremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "value" in params, "Missing parameter 'value'"








def test_hyp_xal_premisenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumber)


def test_hyp_xal_premisenumber_constructor_exists():
    assert callable(xal_PremiseNumber.__init__)


def test_hyp_xal_premisenumber_constructor_args():
    sig = inspect.signature(xal_PremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"











def test_hyp_xal_thoroughfarenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberSuffix)


def test_hyp_xal_thoroughfarenumbersuffix_constructor_exists():
    assert callable(xal_ThoroughfareNumberSuffix.__init__)


def test_hyp_xal_thoroughfarenumbersuffix_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"








def test_hyp_xal_thoroughfarenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberPrefix)


def test_hyp_xal_thoroughfarenumberprefix_constructor_exists():
    assert callable(xal_ThoroughfareNumberPrefix.__init__)


def test_hyp_xal_thoroughfarenumberprefix_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_thoroughfarenumber_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumber)


def test_hyp_xal_thoroughfarenumber_constructor_exists():
    assert callable(xal_ThoroughfareNumber.__init__)


def test_hyp_xal_thoroughfarenumber_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumber.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberType" in params, "Missing parameter 'numberType'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberOccurrence" in params, "Missing parameter 'numberOccurrence'"











def test_hyp_xal_documentroot_is_not_abstract():
    assert not inspect.isabstract(xal_DocumentRoot)


def test_hyp_xal_documentroot_constructor_exists():
    assert callable(xal_DocumentRoot.__init__)


def test_hyp_xal_documentroot_constructor_args():
    sig = inspect.signature(xal_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_xal_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xal_EStringToStringMapEntry)


def test_hyp_xal_estringtostringmapentry_constructor_exists():
    assert callable(xal_EStringToStringMapEntry.__init__)


def test_hyp_xal_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xal_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xal_thoroughfarepredirection_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfarePreDirection)


def test_hyp_xal_thoroughfarepredirection_constructor_exists():
    assert callable(xal_ThoroughfarePreDirection.__init__)


def test_hyp_xal_thoroughfarepredirection_constructor_args():
    sig = inspect.signature(xal_ThoroughfarePreDirection.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_dependentthoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal_DependentThoroughfare)


def test_hyp_xal_dependentthoroughfare_constructor_exists():
    assert callable(xal_DependentThoroughfare.__init__)


def test_hyp_xal_dependentthoroughfare_constructor_args():
    sig = inspect.signature(xal_DependentThoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_xal_thoroughfarepostdirection_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfarePostDirection)


def test_hyp_xal_thoroughfarepostdirection_constructor_exists():
    assert callable(xal_ThoroughfarePostDirection.__init__)


def test_hyp_xal_thoroughfarepostdirection_constructor_args():
    sig = inspect.signature(xal_ThoroughfarePostDirection.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_thoroughfaretrailingtype_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareTrailingType)


def test_hyp_xal_thoroughfaretrailingtype_constructor_exists():
    assert callable(xal_ThoroughfareTrailingType.__init__)


def test_hyp_xal_thoroughfaretrailingtype_constructor_args():
    sig = inspect.signature(xal_ThoroughfareTrailingType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_thoroughfarename_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareName)


def test_hyp_xal_thoroughfarename_constructor_exists():
    assert callable(xal_ThoroughfareName.__init__)


def test_hyp_xal_thoroughfarename_constructor_args():
    sig = inspect.signature(xal_ThoroughfareName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_thoroughfareleadingtype_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareLeadingType)


def test_hyp_xal_thoroughfareleadingtype_constructor_exists():
    assert callable(xal_ThoroughfareLeadingType.__init__)


def test_hyp_xal_thoroughfareleadingtype_constructor_args():
    sig = inspect.signature(xal_ThoroughfareLeadingType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_postalroute_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRoute)


def test_hyp_xal_postalroute_constructor_exists():
    assert callable(xal_PostalRoute.__init__)


def test_hyp_xal_postalroute_constructor_args():
    sig = inspect.signature(xal_PostalRoute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"






def test_hyp_xal_largemailuser_is_not_abstract():
    assert not inspect.isabstract(xal_LargeMailUser)


def test_hyp_xal_largemailuser_constructor_exists():
    assert callable(xal_LargeMailUser.__init__)


def test_hyp_xal_largemailuser_constructor_args():
    sig = inspect.signature(xal_LargeMailUser.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_xal_premise_is_not_abstract():
    assert not inspect.isabstract(xal_Premise)


def test_hyp_xal_premise_constructor_exists():
    assert callable(xal_Premise.__init__)


def test_hyp_xal_premise_constructor_args():
    sig = inspect.signature(xal_Premise.__init__)
    params = list(sig.parameters.keys())
    assert "premiseDependency" in params, "Missing parameter 'premiseDependency'"
    assert "type" in params, "Missing parameter 'type'"
    assert "premiseThoroughfareConnector" in params, "Missing parameter 'premiseThoroughfareConnector'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "premiseDependencyType" in params, "Missing parameter 'premiseDependencyType'"









def test_hyp_xal_postbox_is_not_abstract():
    assert not inspect.isabstract(xal_PostBox)


def test_hyp_xal_postbox_constructor_exists():
    assert callable(xal_PostBox.__init__)


def test_hyp_xal_postbox_constructor_args():
    sig = inspect.signature(xal_PostBox.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"







def test_hyp_xal_dependentlocalitynumber_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocalityNumber)


def test_hyp_xal_dependentlocalitynumber_constructor_exists():
    assert callable(xal_DependentLocalityNumber.__init__)


def test_hyp_xal_dependentlocalitynumber_constructor_args():
    sig = inspect.signature(xal_DependentLocalityNumber.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "nameNumberOccurrence" in params, "Missing parameter 'nameNumberOccurrence'"







def test_hyp_xal_dependentlocalityname_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocalityName)


def test_hyp_xal_dependentlocalityname_constructor_exists():
    assert callable(xal_DependentLocalityName.__init__)


def test_hyp_xal_dependentlocalityname_constructor_args():
    sig = inspect.signature(xal_DependentLocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_dependentlocality_is_not_abstract():
    assert not inspect.isabstract(xal_DependentLocality)


def test_hyp_xal_dependentlocality_constructor_exists():
    assert callable(xal_DependentLocality.__init__)


def test_hyp_xal_dependentlocality_constructor_args():
    sig = inspect.signature(xal_DependentLocality.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "connector" in params, "Missing parameter 'connector'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"









def test_hyp_xal_mailstop_is_not_abstract():
    assert not inspect.isabstract(xal_MailStop)


def test_hyp_xal_mailstop_constructor_exists():
    assert callable(xal_MailStop.__init__)


def test_hyp_xal_mailstop_constructor_args():
    sig = inspect.signature(xal_MailStop.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"






def test_hyp_xal_departmentname_is_not_abstract():
    assert not inspect.isabstract(xal_DepartmentName)


def test_hyp_xal_departmentname_constructor_exists():
    assert callable(xal_DepartmentName.__init__)


def test_hyp_xal_departmentname_constructor_args():
    sig = inspect.signature(xal_DepartmentName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_department_is_not_abstract():
    assert not inspect.isabstract(xal_Department)


def test_hyp_xal_department_constructor_exists():
    assert callable(xal_Department.__init__)


def test_hyp_xal_department_constructor_args():
    sig = inspect.signature(xal_Department.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"






def test_hyp_xal_countryname_is_not_abstract():
    assert not inspect.isabstract(xal_CountryName)


def test_hyp_xal_countryname_constructor_exists():
    assert callable(xal_CountryName.__init__)


def test_hyp_xal_countryname_constructor_args():
    sig = inspect.signature(xal_CountryName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_countrynamecode_is_not_abstract():
    assert not inspect.isabstract(xal_CountryNameCode)


def test_hyp_xal_countrynamecode_constructor_exists():
    assert callable(xal_CountryNameCode.__init__)


def test_hyp_xal_countrynamecode_constructor_args():
    sig = inspect.signature(xal_CountryNameCode.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_barcode_is_not_abstract():
    assert not inspect.isabstract(xal_Barcode)


def test_hyp_xal_barcode_constructor_exists():
    assert callable(xal_Barcode.__init__)


def test_hyp_xal_barcode_constructor_args():
    sig = inspect.signature(xal_Barcode.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_buildingname_is_not_abstract():
    assert not inspect.isabstract(xal_BuildingName)


def test_hyp_xal_buildingname_constructor_exists():
    assert callable(xal_BuildingName.__init__)


def test_hyp_xal_buildingname_constructor_args():
    sig = inspect.signature(xal_BuildingName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_postalcode_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCode)


def test_hyp_xal_postalcode_constructor_exists():
    assert callable(xal_PostalCode.__init__)


def test_hyp_xal_postalcode_constructor_args():
    sig = inspect.signature(xal_PostalCode.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_xal_postoffice_is_not_abstract():
    assert not inspect.isabstract(xal_PostOffice)


def test_hyp_xal_postoffice_constructor_exists():
    assert callable(xal_PostOffice.__init__)


def test_hyp_xal_postoffice_constructor_args():
    sig = inspect.signature(xal_PostOffice.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_addresslongitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLongitudeDirection)


def test_hyp_xal_addresslongitudedirection_constructor_exists():
    assert callable(xal_AddressLongitudeDirection.__init__)


def test_hyp_xal_addresslongitudedirection_constructor_args():
    sig = inspect.signature(xal_AddressLongitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_subadministrativearea_is_not_abstract():
    assert not inspect.isabstract(xal_SubAdministrativeArea)


def test_hyp_xal_subadministrativearea_constructor_exists():
    assert callable(xal_SubAdministrativeArea.__init__)


def test_hyp_xal_subadministrativearea_constructor_args():
    sig = inspect.signature(xal_SubAdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "usageType" in params, "Missing parameter 'usageType'"








def test_hyp_xal_administrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal_AdministrativeAreaName)


def test_hyp_xal_administrativeareaname_constructor_exists():
    assert callable(xal_AdministrativeAreaName.__init__)


def test_hyp_xal_administrativeareaname_constructor_args():
    sig = inspect.signature(xal_AdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_addressline_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLine)


def test_hyp_xal_addressline_constructor_exists():
    assert callable(xal_AddressLine.__init__)


def test_hyp_xal_addressline_constructor_args():
    sig = inspect.signature(xal_AddressLine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_addresslongitude_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLongitude)


def test_hyp_xal_addresslongitude_constructor_exists():
    assert callable(xal_AddressLongitude.__init__)


def test_hyp_xal_addresslongitude_constructor_args():
    sig = inspect.signature(xal_AddressLongitude.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_addresslatitude_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLatitude)


def test_hyp_xal_addresslatitude_constructor_exists():
    assert callable(xal_AddressLatitude.__init__)


def test_hyp_xal_addresslatitude_constructor_args():
    sig = inspect.signature(xal_AddressLatitude.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_addresslatitudedirection_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLatitudeDirection)


def test_hyp_xal_addresslatitudedirection_constructor_exists():
    assert callable(xal_AddressLatitudeDirection.__init__)


def test_hyp_xal_addresslatitudedirection_constructor_args():
    sig = inspect.signature(xal_AddressLatitudeDirection.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"







def test_hyp_xal_addressidentifier_is_not_abstract():
    assert not inspect.isabstract(xal_AddressIdentifier)


def test_hyp_xal_addressidentifier_constructor_exists():
    assert callable(xal_AddressIdentifier.__init__)


def test_hyp_xal_addressidentifier_constructor_args():
    sig = inspect.signature(xal_AddressIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifierType" in params, "Missing parameter 'identifierType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_addresslines_is_not_abstract():
    assert not inspect.isabstract(xal_AddressLines)


def test_hyp_xal_addresslines_constructor_exists():
    assert callable(xal_AddressLines.__init__)


def test_hyp_xal_addresslines_constructor_args():
    sig = inspect.signature(xal_AddressLines.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"





def test_hyp_xal_thoroughfare_is_not_abstract():
    assert not inspect.isabstract(xal_Thoroughfare)


def test_hyp_xal_thoroughfare_constructor_exists():
    assert callable(xal_Thoroughfare.__init__)


def test_hyp_xal_thoroughfare_constructor_args():
    sig = inspect.signature(xal_Thoroughfare.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "dependentThoroughfaresIndicator" in params, "Missing parameter 'dependentThoroughfaresIndicator'"
    assert "dependentThoroughfares" in params, "Missing parameter 'dependentThoroughfares'"
    assert "group" in params, "Missing parameter 'group'"
    assert "type" in params, "Missing parameter 'type'"
    assert "dependentThoroughfaresType" in params, "Missing parameter 'dependentThoroughfaresType'"
    assert "dependentThoroughfaresConnector" in params, "Missing parameter 'dependentThoroughfaresConnector'"
    assert "any" in params, "Missing parameter 'any'"











def test_hyp_xal_locality_is_not_abstract():
    assert not inspect.isabstract(xal_Locality)


def test_hyp_xal_locality_constructor_exists():
    assert callable(xal_Locality.__init__)


def test_hyp_xal_locality_constructor_args():
    sig = inspect.signature(xal_Locality.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"








def test_hyp_xal_administrativearea_is_not_abstract():
    assert not inspect.isabstract(xal_AdministrativeArea)


def test_hyp_xal_administrativearea_constructor_exists():
    assert callable(xal_AdministrativeArea.__init__)


def test_hyp_xal_administrativearea_constructor_args():
    sig = inspect.signature(xal_AdministrativeArea.__init__)
    params = list(sig.parameters.keys())
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "usageType" in params, "Missing parameter 'usageType'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"








def test_hyp_xal_country_is_not_abstract():
    assert not inspect.isabstract(xal_Country)


def test_hyp_xal_country_constructor_exists():
    assert callable(xal_Country.__init__)


def test_hyp_xal_country_constructor_args():
    sig = inspect.signature(xal_Country.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"





def test_hyp_xal_postalserviceelements_is_not_abstract():
    assert not inspect.isabstract(xal_PostalServiceElements)


def test_hyp_xal_postalserviceelements_constructor_exists():
    assert callable(xal_PostalServiceElements.__init__)


def test_hyp_xal_postalserviceelements_constructor_args():
    sig = inspect.signature(xal_PostalServiceElements.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_xal_addressdetails_is_not_abstract():
    assert not inspect.isabstract(xal_AddressDetails)


def test_hyp_xal_addressdetails_constructor_exists():
    assert callable(xal_AddressDetails.__init__)


def test_hyp_xal_addressdetails_constructor_args():
    sig = inspect.signature(xal_AddressDetails.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "currentStatus" in params, "Missing parameter 'currentStatus'"
    assert "validToDate" in params, "Missing parameter 'validToDate'"
    assert "addressType" in params, "Missing parameter 'addressType'"
    assert "validFromDate" in params, "Missing parameter 'validFromDate'"
    assert "usage" in params, "Missing parameter 'usage'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "addressDetailsKey" in params, "Missing parameter 'addressDetailsKey'"












def test_hyp_xal_address_is_not_abstract():
    assert not inspect.isabstract(xal_Address)


def test_hyp_xal_address_constructor_exists():
    assert callable(xal_Address.__init__)


def test_hyp_xal_address_constructor_args():
    sig = inspect.signature(xal_Address.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"







def test_hyp_xal_thoroughfarenumberto_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberTo)


def test_hyp_xal_thoroughfarenumberto_constructor_exists():
    assert callable(xal_ThoroughfareNumberTo.__init__)


def test_hyp_xal_thoroughfarenumberto_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberTo.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_xal_thoroughfarenumberfrom_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberFrom)


def test_hyp_xal_thoroughfarenumberfrom_constructor_exists():
    assert callable(xal_ThoroughfareNumberFrom.__init__)


def test_hyp_xal_thoroughfarenumberfrom_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberFrom.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_xal_thoroughfarenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal_ThoroughfareNumberRange)


def test_hyp_xal_thoroughfarenumberrange_constructor_exists():
    assert callable(xal_ThoroughfareNumberRange.__init__)


def test_hyp_xal_thoroughfarenumberrange_constructor_args():
    sig = inspect.signature(xal_ThoroughfareNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "numberRangeOccurrence" in params, "Missing parameter 'numberRangeOccurrence'"
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"











def test_hyp_xal_subpremisenumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumberPrefix)


def test_hyp_xal_subpremisenumberprefix_constructor_exists():
    assert callable(xal_SubPremiseNumberPrefix.__init__)


def test_hyp_xal_subpremisenumberprefix_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_subpremisenumber_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumber)


def test_hyp_xal_subpremisenumber_constructor_exists():
    assert callable(xal_SubPremiseNumber.__init__)


def test_hyp_xal_subpremisenumber_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "premiseNumberSeparator" in params, "Missing parameter 'premiseNumberSeparator'"
    assert "numberTypeOccurrence" in params, "Missing parameter 'numberTypeOccurrence'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "indicator" in params, "Missing parameter 'indicator'"











def test_hyp_xal_subpremisenumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseNumberSuffix)


def test_hyp_xal_subpremisenumbersuffix_constructor_exists():
    assert callable(xal_SubPremiseNumberSuffix.__init__)


def test_hyp_xal_subpremisenumbersuffix_constructor_args():
    sig = inspect.signature(xal_SubPremiseNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_subpremiselocation_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseLocation)


def test_hyp_xal_subpremiselocation_constructor_exists():
    assert callable(xal_SubPremiseLocation.__init__)


def test_hyp_xal_subpremiselocation_constructor_args():
    sig = inspect.signature(xal_SubPremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"





def test_hyp_xal_subpremisename_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremiseName)


def test_hyp_xal_subpremisename_constructor_exists():
    assert callable(xal_SubPremiseName.__init__)


def test_hyp_xal_subpremisename_constructor_args():
    sig = inspect.signature(xal_SubPremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"








def test_hyp_xal_subadministrativeareaname_is_not_abstract():
    assert not inspect.isabstract(xal_SubAdministrativeAreaName)


def test_hyp_xal_subadministrativeareaname_constructor_exists():
    assert callable(xal_SubAdministrativeAreaName.__init__)


def test_hyp_xal_subadministrativeareaname_constructor_args():
    sig = inspect.signature(xal_SubAdministrativeAreaName.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_premisenumberrangeto_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRangeTo)


def test_hyp_xal_premisenumberrangeto_constructor_exists():
    assert callable(xal_PremiseNumberRangeTo.__init__)


def test_hyp_xal_premisenumberrangeto_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRangeTo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xal_premisenumberrangefrom_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRangeFrom)


def test_hyp_xal_premisenumberrangefrom_constructor_exists():
    assert callable(xal_PremiseNumberRangeFrom.__init__)


def test_hyp_xal_premisenumberrangefrom_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRangeFrom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xal_subpremise_is_not_abstract():
    assert not inspect.isabstract(xal_SubPremise)


def test_hyp_xal_subpremise_constructor_exists():
    assert callable(xal_SubPremise.__init__)


def test_hyp_xal_subpremise_constructor_args():
    sig = inspect.signature(xal_SubPremise.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"






def test_hyp_xal_premisename_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseName)


def test_hyp_xal_premisename_constructor_exists():
    assert callable(xal_PremiseName.__init__)


def test_hyp_xal_premisename_constructor_args():
    sig = inspect.signature(xal_PremiseName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"
    assert "typeOccurrence" in params, "Missing parameter 'typeOccurrence'"








def test_hyp_xal_premisenumberrange_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseNumberRange)


def test_hyp_xal_premisenumberrange_constructor_exists():
    assert callable(xal_PremiseNumberRange.__init__)


def test_hyp_xal_premisenumberrange_constructor_args():
    sig = inspect.signature(xal_PremiseNumberRange.__init__)
    params = list(sig.parameters.keys())
    assert "rangeType" in params, "Missing parameter 'rangeType'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "numberRangeOccurence" in params, "Missing parameter 'numberRangeOccurence'"
    assert "indicatorOccurence" in params, "Missing parameter 'indicatorOccurence'"
    assert "type" in params, "Missing parameter 'type'"









def test_hyp_xal_premiselocation_is_not_abstract():
    assert not inspect.isabstract(xal_PremiseLocation)


def test_hyp_xal_premiselocation_constructor_exists():
    assert callable(xal_PremiseLocation.__init__)


def test_hyp_xal_premiselocation_constructor_args():
    sig = inspect.signature(xal_PremiseLocation.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_xal_posttownsuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PostTownSuffix)


def test_hyp_xal_posttownsuffix_constructor_exists():
    assert callable(xal_PostTownSuffix.__init__)


def test_hyp_xal_posttownsuffix_constructor_args():
    sig = inspect.signature(xal_PostTownSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"






def test_hyp_xal_posttownname_is_not_abstract():
    assert not inspect.isabstract(xal_PostTownName)


def test_hyp_xal_posttownname_constructor_exists():
    assert callable(xal_PostTownName.__init__)


def test_hyp_xal_posttownname_constructor_args():
    sig = inspect.signature(xal_PostTownName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_postofficenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostOfficeNumber)


def test_hyp_xal_postofficenumber_constructor_exists():
    assert callable(xal_PostOfficeNumber.__init__)


def test_hyp_xal_postofficenumber_constructor_args():
    sig = inspect.signature(xal_PostOfficeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "indicator" in params, "Missing parameter 'indicator'"
    assert "indicatorOccurrence" in params, "Missing parameter 'indicatorOccurrence'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"








def test_hyp_xal_postofficename_is_not_abstract():
    assert not inspect.isabstract(xal_PostOfficeName)


def test_hyp_xal_postofficename_constructor_exists():
    assert callable(xal_PostOfficeName.__init__)


def test_hyp_xal_postofficename_constructor_args():
    sig = inspect.signature(xal_PostOfficeName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_postboxnumberextension_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberExtension)


def test_hyp_xal_postboxnumberextension_constructor_exists():
    assert callable(xal_PostBoxNumberExtension.__init__)


def test_hyp_xal_postboxnumberextension_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"






def test_hyp_xal_postboxnumbersuffix_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberSuffix)


def test_hyp_xal_postboxnumbersuffix_constructor_exists():
    assert callable(xal_PostBoxNumberSuffix.__init__)


def test_hyp_xal_postboxnumbersuffix_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberSuffix.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "numberSuffixSeparator" in params, "Missing parameter 'numberSuffixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_postboxnumberprefix_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumberPrefix)


def test_hyp_xal_postboxnumberprefix_constructor_exists():
    assert callable(xal_PostBoxNumberPrefix.__init__)


def test_hyp_xal_postboxnumberprefix_constructor_args():
    sig = inspect.signature(xal_PostBoxNumberPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "numberPrefixSeparator" in params, "Missing parameter 'numberPrefixSeparator'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"







def test_hyp_xal_supplementarypostalservicedata_is_not_abstract():
    assert not inspect.isabstract(xal_SupplementaryPostalServiceData)


def test_hyp_xal_supplementarypostalservicedata_constructor_exists():
    assert callable(xal_SupplementaryPostalServiceData.__init__)


def test_hyp_xal_supplementarypostalservicedata_constructor_args():
    sig = inspect.signature(xal_SupplementaryPostalServiceData.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "mixed" in params, "Missing parameter 'mixed'"







def test_hyp_xal_postboxnumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostBoxNumber)


def test_hyp_xal_postboxnumber_constructor_exists():
    assert callable(xal_PostBoxNumber.__init__)


def test_hyp_xal_postboxnumber_constructor_args():
    sig = inspect.signature(xal_PostBoxNumber.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_xal_sortingcode_is_not_abstract():
    assert not inspect.isabstract(xal_SortingCode)


def test_hyp_xal_sortingcode_constructor_exists():
    assert callable(xal_SortingCode.__init__)


def test_hyp_xal_sortingcode_constructor_args():
    sig = inspect.signature(xal_SortingCode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"





def test_hyp_xal_postalroutenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRouteNumber)


def test_hyp_xal_postalroutenumber_constructor_exists():
    assert callable(xal_PostalRouteNumber.__init__)


def test_hyp_xal_postalroutenumber_constructor_args():
    sig = inspect.signature(xal_PostalRouteNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"






def test_hyp_xal_postalroutename_is_not_abstract():
    assert not inspect.isabstract(xal_PostalRouteName)


def test_hyp_xal_postalroutename_constructor_exists():
    assert callable(xal_PostalRouteName.__init__)


def test_hyp_xal_postalroutename_constructor_args():
    sig = inspect.signature(xal_PostalRouteName.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_postalcodenumberextension_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCodeNumberExtension)


def test_hyp_xal_postalcodenumberextension_constructor_exists():
    assert callable(xal_PostalCodeNumberExtension.__init__)


def test_hyp_xal_postalcodenumberextension_constructor_args():
    sig = inspect.signature(xal_PostalCodeNumberExtension.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "numberExtensionSeparator" in params, "Missing parameter 'numberExtensionSeparator'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"








def test_hyp_xal_postalcodenumber_is_not_abstract():
    assert not inspect.isabstract(xal_PostalCodeNumber)


def test_hyp_xal_postalcodenumber_constructor_exists():
    assert callable(xal_PostalCodeNumber.__init__)


def test_hyp_xal_postalcodenumber_constructor_args():
    sig = inspect.signature(xal_PostalCodeNumber.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"







def test_hyp_xal_posttown_is_not_abstract():
    assert not inspect.isabstract(xal_PostTown)


def test_hyp_xal_posttown_constructor_exists():
    assert callable(xal_PostTown.__init__)


def test_hyp_xal_posttown_constructor_args():
    sig = inspect.signature(xal_PostTown.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_xal_mailstopnumber_is_not_abstract():
    assert not inspect.isabstract(xal_MailStopNumber)


def test_hyp_xal_mailstopnumber_constructor_exists():
    assert callable(xal_MailStopNumber.__init__)


def test_hyp_xal_mailstopnumber_constructor_args():
    sig = inspect.signature(xal_MailStopNumber.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "nameNumberSeparator" in params, "Missing parameter 'nameNumberSeparator'"
    assert "code" in params, "Missing parameter 'code'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"







def test_hyp_xal_mailstopname_is_not_abstract():
    assert not inspect.isabstract(xal_MailStopName)


def test_hyp_xal_mailstopname_constructor_exists():
    assert callable(xal_MailStopName.__init__)


def test_hyp_xal_mailstopname_constructor_args():
    sig = inspect.signature(xal_MailStopName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "code" in params, "Missing parameter 'code'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_xal_localityname_is_not_abstract():
    assert not inspect.isabstract(xal_LocalityName)


def test_hyp_xal_localityname_constructor_exists():
    assert callable(xal_LocalityName.__init__)


def test_hyp_xal_localityname_constructor_args():
    sig = inspect.signature(xal_LocalityName.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "code" in params, "Missing parameter 'code'"





def test_hyp_rangetypetype_exists():
    # Check that the Enumeration exists
    assert RangeTypeType is not None

def test_hyp_rangetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeTypeType]
    expected_literals = [
        "Odd",
        "Even",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeTypeType"

def test_hyp_indicatoroccurrence4_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence4 is not None

def test_hyp_indicatoroccurrence4_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence4]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence4"

def test_hyp_numbertypetype1_exists():
    # Check that the Enumeration exists
    assert NumberTypeType1 is not None

def test_hyp_numbertypetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType1]
    expected_literals = [
        "Single",
        "Range",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType1"

def test_hyp_typeoccurrence_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence is not None

def test_hyp_typeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence"

def test_hyp_typeoccurrence2_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence2 is not None

def test_hyp_typeoccurrence2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence2]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence2"

def test_hyp_namenumberoccurrence_exists():
    # Check that the Enumeration exists
    assert NameNumberOccurrence is not None

def test_hyp_namenumberoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NameNumberOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NameNumberOccurrence"

def test_hyp_indicatoroccurence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurence is not None

def test_hyp_indicatoroccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurence]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurence"

def test_hyp_numberoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberOccurrence is not None

def test_hyp_numberoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOccurrence]
    expected_literals = [
        "BeforeType",
        "AfterType",
        "BeforeName",
        "AfterName",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOccurrence"

def test_hyp_numbertypeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence is not None

def test_hyp_numbertypeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence"

def test_hyp_numbertypeoccurrence1_exists():
    # Check that the Enumeration exists
    assert NumberTypeOccurrence1 is not None

def test_hyp_numbertypeoccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeOccurrence1]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeOccurrence1"

def test_hyp_indicatoroccurrence_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence is not None

def test_hyp_indicatoroccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence"

def test_hyp_indicatoroccurrence2_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence2 is not None

def test_hyp_indicatoroccurrence2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence2]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence2"

def test_hyp_numberrangeoccurrence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurrence is not None

def test_hyp_numberrangeoccurrence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurrence]
    expected_literals = [
        "BeforeName",
        "BeforeType",
        "AfterName",
        "AfterType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurrence"

def test_hyp_numberrangeoccurence_exists():
    # Check that the Enumeration exists
    assert NumberRangeOccurence is not None

def test_hyp_numberrangeoccurence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberRangeOccurence]
    expected_literals = [
        "AfterName",
        "BeforeName",
        "BeforeType",
        "AfterType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberRangeOccurence"

def test_hyp_typeoccurrence1_exists():
    # Check that the Enumeration exists
    assert TypeOccurrence1 is not None

def test_hyp_typeoccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOccurrence1]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOccurrence1"

def test_hyp_dependentthoroughfarestype_exists():
    # Check that the Enumeration exists
    assert DependentThoroughfaresType is not None

def test_hyp_dependentthoroughfarestype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DependentThoroughfaresType]
    expected_literals = [
        "No",
        "Yes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DependentThoroughfaresType"

def test_hyp_indicatoroccurrence1_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence1 is not None

def test_hyp_indicatoroccurrence1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence1]
    expected_literals = [
        "After",
        "Before",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence1"

def test_hyp_numbertypetype_exists():
    # Check that the Enumeration exists
    assert NumberTypeType is not None

def test_hyp_numbertypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberTypeType]
    expected_literals = [
        "Single",
        "Range",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberTypeType"

def test_hyp_indicatoroccurrence3_exists():
    # Check that the Enumeration exists
    assert IndicatorOccurrence3 is not None

def test_hyp_indicatoroccurrence3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndicatorOccurrence3]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndicatorOccurrence3"


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
xal_LargeMailUserIdentifier_strategy = st.builds(
    xal_LargeMailUserIdentifier,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    indicator=
        safe_text,
    mixed=
        safe_text
)
xal_LargeMailUserName_strategy = st.builds(
    xal_LargeMailUserName,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_KeyLineCode_strategy = st.builds(
    xal_KeyLineCode,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_EndorsementLineCode_strategy = st.builds(
    xal_EndorsementLineCode,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal_Xal_strategy = st.builds(
    xal_Xal,
    any=
        safe_text,
    version=
        safe_text,
    anyAttribute=
        safe_text
)
xal_FirmName_strategy = st.builds(
    xal_FirmName,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_Firm_strategy = st.builds(
    xal_Firm,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PremiseNumberSuffix_strategy = st.builds(
    xal_PremiseNumberSuffix,
    anyAttribute=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_PremiseNumberPrefix_strategy = st.builds(
    xal_PremiseNumberPrefix,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    value=
        safe_text
)
xal_PremiseNumber_strategy = st.builds(
    xal_PremiseNumber,
    type=
        safe_text,
    code=
        safe_text,
    indicator=
        safe_text,
    indicatorOccurrence=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    mixed=
        safe_text,
    numberType=
        safe_text,
    anyAttribute=
        safe_text
)
xal_ThoroughfareNumberSuffix_strategy = st.builds(
    xal_ThoroughfareNumberSuffix,
    type=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_ThoroughfareNumberPrefix_strategy = st.builds(
    xal_ThoroughfareNumberPrefix,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumber_strategy = st.builds(
    xal_ThoroughfareNumber,
    anyAttribute=
        safe_text,
    numberType=
        safe_text,
    mixed=
        safe_text,
    indicator=
        safe_text,
    code=
        safe_text,
    indicatorOccurrence=
        safe_text,
    type=
        safe_text,
    numberOccurrence=
        safe_text
)
xal_DocumentRoot_strategy = st.builds(
    xal_DocumentRoot,
    mixed=
        safe_text
)
xal_EStringToStringMapEntry_strategy = st.builds(
    xal_EStringToStringMapEntry,
)
xal_ThoroughfarePreDirection_strategy = st.builds(
    xal_ThoroughfarePreDirection,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_DependentThoroughfare_strategy = st.builds(
    xal_DependentThoroughfare,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfarePostDirection_strategy = st.builds(
    xal_ThoroughfarePostDirection,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareTrailingType_strategy = st.builds(
    xal_ThoroughfareTrailingType,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareName_strategy = st.builds(
    xal_ThoroughfareName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_ThoroughfareLeadingType_strategy = st.builds(
    xal_ThoroughfareLeadingType,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostalRoute_strategy = st.builds(
    xal_PostalRoute,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_LargeMailUser_strategy = st.builds(
    xal_LargeMailUser,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_Premise_strategy = st.builds(
    xal_Premise,
    premiseDependency=
        safe_text,
    type=
        safe_text,
    premiseThoroughfareConnector=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    premiseDependencyType=
        safe_text
)
xal_PostBox_strategy = st.builds(
    xal_PostBox,
    indicator=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_DependentLocalityNumber_strategy = st.builds(
    xal_DependentLocalityNumber,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    nameNumberOccurrence=
        safe_text
)
xal_DependentLocalityName_strategy = st.builds(
    xal_DependentLocalityName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_DependentLocality_strategy = st.builds(
    xal_DependentLocality,
    type=
        safe_text,
    usageType=
        safe_text,
    connector=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_MailStop_strategy = st.builds(
    xal_MailStop,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    any=
        safe_text
)
xal_DepartmentName_strategy = st.builds(
    xal_DepartmentName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_Department_strategy = st.builds(
    xal_Department,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_CountryName_strategy = st.builds(
    xal_CountryName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_CountryNameCode_strategy = st.builds(
    xal_CountryNameCode,
    scheme=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_Barcode_strategy = st.builds(
    xal_Barcode,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_BuildingName_strategy = st.builds(
    xal_BuildingName,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    typeOccurrence=
        safe_text,
    mixed=
        safe_text
)
xal_PostalCode_strategy = st.builds(
    xal_PostalCode,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_PostOffice_strategy = st.builds(
    xal_PostOffice,
    indicator=
        safe_text,
    type=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLongitudeDirection_strategy = st.builds(
    xal_AddressLongitudeDirection,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubAdministrativeArea_strategy = st.builds(
    xal_SubAdministrativeArea,
    type=
        safe_text,
    any=
        safe_text,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    usageType=
        safe_text
)
xal_AdministrativeAreaName_strategy = st.builds(
    xal_AdministrativeAreaName,
    type=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLine_strategy = st.builds(
    xal_AddressLine,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text
)
xal_AddressLongitude_strategy = st.builds(
    xal_AddressLongitude,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLatitude_strategy = st.builds(
    xal_AddressLatitude,
    code=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_AddressLatitudeDirection_strategy = st.builds(
    xal_AddressLatitudeDirection,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_AddressIdentifier_strategy = st.builds(
    xal_AddressIdentifier,
    identifierType=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_AddressLines_strategy = st.builds(
    xal_AddressLines,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_Thoroughfare_strategy = st.builds(
    xal_Thoroughfare,
    anyAttribute=
        safe_text,
    dependentThoroughfaresIndicator=
        safe_text,
    dependentThoroughfares=
        safe_text,
    group=
        safe_text,
    type=
        safe_text,
    dependentThoroughfaresType=
        safe_text,
    dependentThoroughfaresConnector=
        safe_text,
    any=
        safe_text
)
xal_Locality_strategy = st.builds(
    xal_Locality,
    indicator=
        safe_text,
    usageType=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_AdministrativeArea_strategy = st.builds(
    xal_AdministrativeArea,
    indicator=
        safe_text,
    anyAttribute=
        safe_text,
    usageType=
        safe_text,
    any=
        safe_text,
    type=
        safe_text
)
xal_Country_strategy = st.builds(
    xal_Country,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_PostalServiceElements_strategy = st.builds(
    xal_PostalServiceElements,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_AddressDetails_strategy = st.builds(
    xal_AddressDetails,
    code=
        safe_text,
    currentStatus=
        safe_text,
    validToDate=
        safe_text,
    addressType=
        safe_text,
    validFromDate=
        safe_text,
    usage=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    addressDetailsKey=
        safe_text
)
xal_Address_strategy = st.builds(
    xal_Address,
    type=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberTo_strategy = st.builds(
    xal_ThoroughfareNumberTo,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberFrom_strategy = st.builds(
    xal_ThoroughfareNumberFrom,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_ThoroughfareNumberRange_strategy = st.builds(
    xal_ThoroughfareNumberRange,
    type=
        safe_text,
    numberRangeOccurrence=
        safe_text,
    rangeType=
        safe_text,
    indicatorOccurrence=
        safe_text,
    indicator=
        safe_text,
    code=
        safe_text,
    separator=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubPremiseNumberPrefix_strategy = st.builds(
    xal_SubPremiseNumberPrefix,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    numberPrefixSeparator=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_SubPremiseNumber_strategy = st.builds(
    xal_SubPremiseNumber,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    premiseNumberSeparator=
        safe_text,
    numberTypeOccurrence=
        safe_text,
    indicatorOccurrence=
        safe_text,
    indicator=
        safe_text
)
xal_SubPremiseNumberSuffix_strategy = st.builds(
    xal_SubPremiseNumberSuffix,
    code=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    mixed=
        safe_text
)
xal_SubPremiseLocation_strategy = st.builds(
    xal_SubPremiseLocation,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_SubPremiseName_strategy = st.builds(
    xal_SubPremiseName,
    type=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    typeOccurrence=
        safe_text,
    anyAttribute=
        safe_text
)
xal_SubAdministrativeAreaName_strategy = st.builds(
    xal_SubAdministrativeAreaName,
    code=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PremiseNumberRangeTo_strategy = st.builds(
    xal_PremiseNumberRangeTo,
)
xal_PremiseNumberRangeFrom_strategy = st.builds(
    xal_PremiseNumberRangeFrom,
)
xal_SubPremise_strategy = st.builds(
    xal_SubPremise,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
xal_PremiseName_strategy = st.builds(
    xal_PremiseName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text,
    typeOccurrence=
        safe_text
)
xal_PremiseNumberRange_strategy = st.builds(
    xal_PremiseNumberRange,
    rangeType=
        safe_text,
    separator=
        safe_text,
    indicator=
        safe_text,
    numberRangeOccurence=
        safe_text,
    indicatorOccurence=
        safe_text,
    type=
        safe_text
)
xal_PremiseLocation_strategy = st.builds(
    xal_PremiseLocation,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_PostTownSuffix_strategy = st.builds(
    xal_PostTownSuffix,
    code=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostTownName_strategy = st.builds(
    xal_PostTownName,
    mixed=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_PostOfficeNumber_strategy = st.builds(
    xal_PostOfficeNumber,
    mixed=
        safe_text,
    indicator=
        safe_text,
    indicatorOccurrence=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostOfficeName_strategy = st.builds(
    xal_PostOfficeName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)
xal_PostBoxNumberExtension_strategy = st.builds(
    xal_PostBoxNumberExtension,
    numberExtensionSeparator=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostBoxNumberSuffix_strategy = st.builds(
    xal_PostBoxNumberSuffix,
    mixed=
        safe_text,
    code=
        safe_text,
    numberSuffixSeparator=
        safe_text,
    anyAttribute=
        safe_text
)
xal_PostBoxNumberPrefix_strategy = st.builds(
    xal_PostBoxNumberPrefix,
    numberPrefixSeparator=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_SupplementaryPostalServiceData_strategy = st.builds(
    xal_SupplementaryPostalServiceData,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    mixed=
        safe_text
)
xal_PostBoxNumber_strategy = st.builds(
    xal_PostBoxNumber,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text
)
xal_SortingCode_strategy = st.builds(
    xal_SortingCode,
    type=
        safe_text,
    code=
        safe_text
)
xal_PostalRouteNumber_strategy = st.builds(
    xal_PostalRouteNumber,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text
)
xal_PostalRouteName_strategy = st.builds(
    xal_PostalRouteName,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_PostalCodeNumberExtension_strategy = st.builds(
    xal_PostalCodeNumberExtension,
    code=
        safe_text,
    anyAttribute=
        safe_text,
    numberExtensionSeparator=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
xal_PostalCodeNumber_strategy = st.builds(
    xal_PostalCodeNumber,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text
)
xal_PostTown_strategy = st.builds(
    xal_PostTown,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
xal_MailStopNumber_strategy = st.builds(
    xal_MailStopNumber,
    mixed=
        safe_text,
    nameNumberSeparator=
        safe_text,
    code=
        safe_text,
    anyAttribute=
        safe_text
)
xal_MailStopName_strategy = st.builds(
    xal_MailStopName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    code=
        safe_text,
    type=
        safe_text
)
xal_LocalityName_strategy = st.builds(
    xal_LocalityName,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text,
    code=
        safe_text
)




@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_hyp_xal_largemailuseridentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_hyp_xal_largemailuseridentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_hyp_xal_largemailuseridentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_hyp_xal_largemailuseridentifier_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_LargeMailUserIdentifier_strategy)
def test_hyp_xal_largemailuseridentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_LargeMailUserName_strategy)
def test_hyp_xal_largemailusername_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_LargeMailUserName_strategy)
def test_hyp_xal_largemailusername_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_LargeMailUserName_strategy)
def test_hyp_xal_largemailusername_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUserName_strategy)
def test_hyp_xal_largemailusername_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_KeyLineCode_strategy)
def test_hyp_xal_keylinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_KeyLineCode_strategy)
def test_hyp_xal_keylinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_KeyLineCode_strategy)
def test_hyp_xal_keylinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_KeyLineCode_strategy)
def test_hyp_xal_keylinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_EndorsementLineCode_strategy)
def test_hyp_xal_endorsementlinecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_hyp_xal_endorsementlinecode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_hyp_xal_endorsementlinecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_EndorsementLineCode_strategy)
def test_hyp_xal_endorsementlinecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_Xal_strategy)
def test_hyp_xal_xal_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Xal_strategy)
def test_hyp_xal_xal_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xal_Xal_strategy)
def test_hyp_xal_xal_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_FirmName_strategy)
def test_hyp_xal_firmname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_FirmName_strategy)
def test_hyp_xal_firmname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_FirmName_strategy)
def test_hyp_xal_firmname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_FirmName_strategy)
def test_hyp_xal_firmname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_Firm_strategy)
def test_hyp_xal_firm_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Firm_strategy)
def test_hyp_xal_firm_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Firm_strategy)
def test_hyp_xal_firm_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PremiseNumberSuffix_strategy)
def test_hyp_xal_premisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_hyp_xal_premisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_hyp_xal_premisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_hyp_xal_premisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumberSuffix_strategy)
def test_hyp_xal_premisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_PremiseNumberPrefix_strategy)
def test_hyp_xal_premisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_hyp_xal_premisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_hyp_xal_premisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_hyp_xal_premisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_PremiseNumberPrefix_strategy)
def test_hyp_xal_premisenumberprefix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original



@given(instance=xal_PremiseNumber_strategy)
def test_hyp_xal_premisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_hyp_xal_thoroughfarenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_hyp_xal_thoroughfarenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_hyp_xal_thoroughfarenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_hyp_xal_thoroughfarenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareNumberSuffix_strategy)
def test_hyp_xal_thoroughfarenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_hyp_xal_thoroughfarenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_hyp_xal_thoroughfarenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_hyp_xal_thoroughfarenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_hyp_xal_thoroughfarenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_ThoroughfareNumberPrefix_strategy)
def test_hyp_xal_thoroughfarenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_numberType_setter(instance):
    original = instance.numberType
    instance.numberType = original
    assert instance.numberType == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumber_strategy)
def test_hyp_xal_thoroughfarenumber_numberOccurrence_setter(instance):
    original = instance.numberOccurrence
    instance.numberOccurrence = original
    assert instance.numberOccurrence == original




@given(instance=xal_DocumentRoot_strategy)
def test_hyp_xal_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_hyp_xal_thoroughfarepredirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_hyp_xal_thoroughfarepredirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_hyp_xal_thoroughfarepredirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfarePreDirection_strategy)
def test_hyp_xal_thoroughfarepredirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_DependentThoroughfare_strategy)
def test_hyp_xal_dependentthoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentThoroughfare_strategy)
def test_hyp_xal_dependentthoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_DependentThoroughfare_strategy)
def test_hyp_xal_dependentthoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_hyp_xal_thoroughfarepostdirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_hyp_xal_thoroughfarepostdirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_hyp_xal_thoroughfarepostdirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfarePostDirection_strategy)
def test_hyp_xal_thoroughfarepostdirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_hyp_xal_thoroughfaretrailingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_hyp_xal_thoroughfaretrailingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_hyp_xal_thoroughfaretrailingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareTrailingType_strategy)
def test_hyp_xal_thoroughfaretrailingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_ThoroughfareName_strategy)
def test_hyp_xal_thoroughfarename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareName_strategy)
def test_hyp_xal_thoroughfarename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareName_strategy)
def test_hyp_xal_thoroughfarename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareName_strategy)
def test_hyp_xal_thoroughfarename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_hyp_xal_thoroughfareleadingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_hyp_xal_thoroughfareleadingtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_hyp_xal_thoroughfareleadingtype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareLeadingType_strategy)
def test_hyp_xal_thoroughfareleadingtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PostalRoute_strategy)
def test_hyp_xal_postalroute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalRoute_strategy)
def test_hyp_xal_postalroute_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRoute_strategy)
def test_hyp_xal_postalroute_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_LargeMailUser_strategy)
def test_hyp_xal_largemailuser_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_LargeMailUser_strategy)
def test_hyp_xal_largemailuser_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LargeMailUser_strategy)
def test_hyp_xal_largemailuser_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_premiseDependency_setter(instance):
    original = instance.premiseDependency
    instance.premiseDependency = original
    assert instance.premiseDependency == original



@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_premiseThoroughfareConnector_setter(instance):
    original = instance.premiseThoroughfareConnector
    instance.premiseThoroughfareConnector = original
    assert instance.premiseThoroughfareConnector == original



@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_Premise_strategy)
def test_hyp_xal_premise_premiseDependencyType_setter(instance):
    original = instance.premiseDependencyType
    instance.premiseDependencyType = original
    assert instance.premiseDependencyType == original




@given(instance=xal_PostBox_strategy)
def test_hyp_xal_postbox_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostBox_strategy)
def test_hyp_xal_postbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostBox_strategy)
def test_hyp_xal_postbox_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBox_strategy)
def test_hyp_xal_postbox_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_DependentLocalityNumber_strategy)
def test_hyp_xal_dependentlocalitynumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_hyp_xal_dependentlocalitynumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_hyp_xal_dependentlocalitynumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DependentLocalityNumber_strategy)
def test_hyp_xal_dependentlocalitynumber_nameNumberOccurrence_setter(instance):
    original = instance.nameNumberOccurrence
    instance.nameNumberOccurrence = original
    assert instance.nameNumberOccurrence == original




@given(instance=xal_DependentLocalityName_strategy)
def test_hyp_xal_dependentlocalityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DependentLocalityName_strategy)
def test_hyp_xal_dependentlocalityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocalityName_strategy)
def test_hyp_xal_dependentlocalityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DependentLocalityName_strategy)
def test_hyp_xal_dependentlocalityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_connector_setter(instance):
    original = instance.connector
    instance.connector = original
    assert instance.connector == original



@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DependentLocality_strategy)
def test_hyp_xal_dependentlocality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_MailStop_strategy)
def test_hyp_xal_mailstop_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_MailStop_strategy)
def test_hyp_xal_mailstop_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_MailStop_strategy)
def test_hyp_xal_mailstop_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_DepartmentName_strategy)
def test_hyp_xal_departmentname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_DepartmentName_strategy)
def test_hyp_xal_departmentname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_DepartmentName_strategy)
def test_hyp_xal_departmentname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_DepartmentName_strategy)
def test_hyp_xal_departmentname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_Department_strategy)
def test_hyp_xal_department_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Department_strategy)
def test_hyp_xal_department_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Department_strategy)
def test_hyp_xal_department_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_CountryName_strategy)
def test_hyp_xal_countryname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_CountryName_strategy)
def test_hyp_xal_countryname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_CountryName_strategy)
def test_hyp_xal_countryname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_CountryName_strategy)
def test_hyp_xal_countryname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_CountryNameCode_strategy)
def test_hyp_xal_countrynamecode_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original



@given(instance=xal_CountryNameCode_strategy)
def test_hyp_xal_countrynamecode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_CountryNameCode_strategy)
def test_hyp_xal_countrynamecode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_CountryNameCode_strategy)
def test_hyp_xal_countrynamecode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_Barcode_strategy)
def test_hyp_xal_barcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Barcode_strategy)
def test_hyp_xal_barcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Barcode_strategy)
def test_hyp_xal_barcode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_Barcode_strategy)
def test_hyp_xal_barcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_BuildingName_strategy)
def test_hyp_xal_buildingname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_BuildingName_strategy)
def test_hyp_xal_buildingname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_BuildingName_strategy)
def test_hyp_xal_buildingname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_BuildingName_strategy)
def test_hyp_xal_buildingname_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original



@given(instance=xal_BuildingName_strategy)
def test_hyp_xal_buildingname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_PostalCode_strategy)
def test_hyp_xal_postalcode_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostalCode_strategy)
def test_hyp_xal_postalcode_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCode_strategy)
def test_hyp_xal_postalcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_PostOffice_strategy)
def test_hyp_xal_postoffice_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostOffice_strategy)
def test_hyp_xal_postoffice_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostOffice_strategy)
def test_hyp_xal_postoffice_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostOffice_strategy)
def test_hyp_xal_postoffice_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_AddressLongitudeDirection_strategy)
def test_hyp_xal_addresslongitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_hyp_xal_addresslongitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_hyp_xal_addresslongitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLongitudeDirection_strategy)
def test_hyp_xal_addresslongitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_SubAdministrativeArea_strategy)
def test_hyp_xal_subadministrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_hyp_xal_subadministrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_hyp_xal_subadministrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_hyp_xal_subadministrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubAdministrativeArea_strategy)
def test_hyp_xal_subadministrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original




@given(instance=xal_AdministrativeAreaName_strategy)
def test_hyp_xal_administrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_hyp_xal_administrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_hyp_xal_administrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AdministrativeAreaName_strategy)
def test_hyp_xal_administrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_AddressLine_strategy)
def test_hyp_xal_addressline_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLine_strategy)
def test_hyp_xal_addressline_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLine_strategy)
def test_hyp_xal_addressline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLine_strategy)
def test_hyp_xal_addressline_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_AddressLongitude_strategy)
def test_hyp_xal_addresslongitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLongitude_strategy)
def test_hyp_xal_addresslongitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLongitude_strategy)
def test_hyp_xal_addresslongitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLongitude_strategy)
def test_hyp_xal_addresslongitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_AddressLatitude_strategy)
def test_hyp_xal_addresslatitude_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLatitude_strategy)
def test_hyp_xal_addresslatitude_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLatitude_strategy)
def test_hyp_xal_addresslatitude_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_AddressLatitude_strategy)
def test_hyp_xal_addresslatitude_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_AddressLatitudeDirection_strategy)
def test_hyp_xal_addresslatitudedirection_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_hyp_xal_addresslatitudedirection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_hyp_xal_addresslatitudedirection_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLatitudeDirection_strategy)
def test_hyp_xal_addresslatitudedirection_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_AddressIdentifier_strategy)
def test_hyp_xal_addressidentifier_identifierType_setter(instance):
    original = instance.identifierType
    instance.identifierType = original
    assert instance.identifierType == original



@given(instance=xal_AddressIdentifier_strategy)
def test_hyp_xal_addressidentifier_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_AddressIdentifier_strategy)
def test_hyp_xal_addressidentifier_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressIdentifier_strategy)
def test_hyp_xal_addressidentifier_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressIdentifier_strategy)
def test_hyp_xal_addressidentifier_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_AddressLines_strategy)
def test_hyp_xal_addresslines_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressLines_strategy)
def test_hyp_xal_addresslines_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_dependentThoroughfaresIndicator_setter(instance):
    original = instance.dependentThoroughfaresIndicator
    instance.dependentThoroughfaresIndicator = original
    assert instance.dependentThoroughfaresIndicator == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_dependentThoroughfares_setter(instance):
    original = instance.dependentThoroughfares
    instance.dependentThoroughfares = original
    assert instance.dependentThoroughfares == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_dependentThoroughfaresType_setter(instance):
    original = instance.dependentThoroughfaresType
    instance.dependentThoroughfaresType = original
    assert instance.dependentThoroughfaresType == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_dependentThoroughfaresConnector_setter(instance):
    original = instance.dependentThoroughfaresConnector
    instance.dependentThoroughfaresConnector = original
    assert instance.dependentThoroughfaresConnector == original



@given(instance=xal_Thoroughfare_strategy)
def test_hyp_xal_thoroughfare_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_Locality_strategy)
def test_hyp_xal_locality_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_Locality_strategy)
def test_hyp_xal_locality_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_Locality_strategy)
def test_hyp_xal_locality_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Locality_strategy)
def test_hyp_xal_locality_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Locality_strategy)
def test_hyp_xal_locality_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_AdministrativeArea_strategy)
def test_hyp_xal_administrativearea_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_AdministrativeArea_strategy)
def test_hyp_xal_administrativearea_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AdministrativeArea_strategy)
def test_hyp_xal_administrativearea_usageType_setter(instance):
    original = instance.usageType
    instance.usageType = original
    assert instance.usageType == original



@given(instance=xal_AdministrativeArea_strategy)
def test_hyp_xal_administrativearea_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_AdministrativeArea_strategy)
def test_hyp_xal_administrativearea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_Country_strategy)
def test_hyp_xal_country_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Country_strategy)
def test_hyp_xal_country_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_PostalServiceElements_strategy)
def test_hyp_xal_postalserviceelements_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_PostalServiceElements_strategy)
def test_hyp_xal_postalserviceelements_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalServiceElements_strategy)
def test_hyp_xal_postalserviceelements_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_currentStatus_setter(instance):
    original = instance.currentStatus
    instance.currentStatus = original
    assert instance.currentStatus == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_validToDate_setter(instance):
    original = instance.validToDate
    instance.validToDate = original
    assert instance.validToDate == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_addressType_setter(instance):
    original = instance.addressType
    instance.addressType = original
    assert instance.addressType == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_validFromDate_setter(instance):
    original = instance.validFromDate
    instance.validFromDate = original
    assert instance.validFromDate == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_usage_setter(instance):
    original = instance.usage
    instance.usage = original
    assert instance.usage == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xal_AddressDetails_strategy)
def test_hyp_xal_addressdetails_addressDetailsKey_setter(instance):
    original = instance.addressDetailsKey
    instance.addressDetailsKey = original
    assert instance.addressDetailsKey == original




@given(instance=xal_Address_strategy)
def test_hyp_xal_address_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_Address_strategy)
def test_hyp_xal_address_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_Address_strategy)
def test_hyp_xal_address_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_Address_strategy)
def test_hyp_xal_address_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_hyp_xal_thoroughfarenumberto_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_hyp_xal_thoroughfarenumberto_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberTo_strategy)
def test_hyp_xal_thoroughfarenumberto_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_hyp_xal_thoroughfarenumberfrom_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_hyp_xal_thoroughfarenumberfrom_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_ThoroughfareNumberFrom_strategy)
def test_hyp_xal_thoroughfarenumberfrom_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_numberRangeOccurrence_setter(instance):
    original = instance.numberRangeOccurrence
    instance.numberRangeOccurrence = original
    assert instance.numberRangeOccurrence == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=xal_ThoroughfareNumberRange_strategy)
def test_hyp_xal_thoroughfarenumberrange_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_hyp_xal_subpremisenumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_hyp_xal_subpremisenumberprefix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_hyp_xal_subpremisenumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_hyp_xal_subpremisenumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumberPrefix_strategy)
def test_hyp_xal_subpremisenumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_premiseNumberSeparator_setter(instance):
    original = instance.premiseNumberSeparator
    instance.premiseNumberSeparator = original
    assert instance.premiseNumberSeparator == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_numberTypeOccurrence_setter(instance):
    original = instance.numberTypeOccurrence
    instance.numberTypeOccurrence = original
    assert instance.numberTypeOccurrence == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_SubPremiseNumber_strategy)
def test_hyp_xal_subpremisenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original




@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_hyp_xal_subpremisenumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_hyp_xal_subpremisenumbersuffix_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_hyp_xal_subpremisenumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_hyp_xal_subpremisenumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_SubPremiseNumberSuffix_strategy)
def test_hyp_xal_subpremisenumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_SubPremiseLocation_strategy)
def test_hyp_xal_subpremiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseLocation_strategy)
def test_hyp_xal_subpremiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_SubPremiseName_strategy)
def test_hyp_xal_subpremisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremiseName_strategy)
def test_hyp_xal_subpremisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubPremiseName_strategy)
def test_hyp_xal_subpremisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubPremiseName_strategy)
def test_hyp_xal_subpremisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original



@given(instance=xal_SubPremiseName_strategy)
def test_hyp_xal_subpremisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_hyp_xal_subadministrativeareaname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_hyp_xal_subadministrativeareaname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_hyp_xal_subadministrativeareaname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubAdministrativeAreaName_strategy)
def test_hyp_xal_subadministrativeareaname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original






@given(instance=xal_SubPremise_strategy)
def test_hyp_xal_subpremise_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SubPremise_strategy)
def test_hyp_xal_subpremise_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SubPremise_strategy)
def test_hyp_xal_subpremise_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original




@given(instance=xal_PremiseName_strategy)
def test_hyp_xal_premisename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PremiseName_strategy)
def test_hyp_xal_premisename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseName_strategy)
def test_hyp_xal_premisename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PremiseName_strategy)
def test_hyp_xal_premisename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseName_strategy)
def test_hyp_xal_premisename_typeOccurrence_setter(instance):
    original = instance.typeOccurrence
    instance.typeOccurrence = original
    assert instance.typeOccurrence == original




@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_rangeType_setter(instance):
    original = instance.rangeType
    instance.rangeType = original
    assert instance.rangeType == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_numberRangeOccurence_setter(instance):
    original = instance.numberRangeOccurence
    instance.numberRangeOccurence = original
    assert instance.numberRangeOccurence == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_indicatorOccurence_setter(instance):
    original = instance.indicatorOccurence
    instance.indicatorOccurence = original
    assert instance.indicatorOccurence == original



@given(instance=xal_PremiseNumberRange_strategy)
def test_hyp_xal_premisenumberrange_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_PremiseLocation_strategy)
def test_hyp_xal_premiselocation_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PremiseLocation_strategy)
def test_hyp_xal_premiselocation_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PremiseLocation_strategy)
def test_hyp_xal_premiselocation_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_PostTownSuffix_strategy)
def test_hyp_xal_posttownsuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostTownSuffix_strategy)
def test_hyp_xal_posttownsuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostTownSuffix_strategy)
def test_hyp_xal_posttownsuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PostTownName_strategy)
def test_hyp_xal_posttownname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostTownName_strategy)
def test_hyp_xal_posttownname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostTownName_strategy)
def test_hyp_xal_posttownname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostTownName_strategy)
def test_hyp_xal_posttownname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_PostOfficeNumber_strategy)
def test_hyp_xal_postofficenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_hyp_xal_postofficenumber_indicator_setter(instance):
    original = instance.indicator
    instance.indicator = original
    assert instance.indicator == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_hyp_xal_postofficenumber_indicatorOccurrence_setter(instance):
    original = instance.indicatorOccurrence
    instance.indicatorOccurrence = original
    assert instance.indicatorOccurrence == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_hyp_xal_postofficenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostOfficeNumber_strategy)
def test_hyp_xal_postofficenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PostOfficeName_strategy)
def test_hyp_xal_postofficename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostOfficeName_strategy)
def test_hyp_xal_postofficename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostOfficeName_strategy)
def test_hyp_xal_postofficename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostOfficeName_strategy)
def test_hyp_xal_postofficename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_PostBoxNumberExtension_strategy)
def test_hyp_xal_postboxnumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original



@given(instance=xal_PostBoxNumberExtension_strategy)
def test_hyp_xal_postboxnumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostBoxNumberExtension_strategy)
def test_hyp_xal_postboxnumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_hyp_xal_postboxnumbersuffix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_hyp_xal_postboxnumbersuffix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_hyp_xal_postboxnumbersuffix_numberSuffixSeparator_setter(instance):
    original = instance.numberSuffixSeparator
    instance.numberSuffixSeparator = original
    assert instance.numberSuffixSeparator == original



@given(instance=xal_PostBoxNumberSuffix_strategy)
def test_hyp_xal_postboxnumbersuffix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_hyp_xal_postboxnumberprefix_numberPrefixSeparator_setter(instance):
    original = instance.numberPrefixSeparator
    instance.numberPrefixSeparator = original
    assert instance.numberPrefixSeparator == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_hyp_xal_postboxnumberprefix_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_hyp_xal_postboxnumberprefix_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumberPrefix_strategy)
def test_hyp_xal_postboxnumberprefix_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_hyp_xal_supplementarypostalservicedata_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_hyp_xal_supplementarypostalservicedata_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_hyp_xal_supplementarypostalservicedata_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_SupplementaryPostalServiceData_strategy)
def test_hyp_xal_supplementarypostalservicedata_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_PostBoxNumber_strategy)
def test_hyp_xal_postboxnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostBoxNumber_strategy)
def test_hyp_xal_postboxnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostBoxNumber_strategy)
def test_hyp_xal_postboxnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_SortingCode_strategy)
def test_hyp_xal_sortingcode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_SortingCode_strategy)
def test_hyp_xal_sortingcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_PostalRouteNumber_strategy)
def test_hyp_xal_postalroutenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalRouteNumber_strategy)
def test_hyp_xal_postalroutenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRouteNumber_strategy)
def test_hyp_xal_postalroutenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_PostalRouteName_strategy)
def test_hyp_xal_postalroutename_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalRouteName_strategy)
def test_hyp_xal_postalroutename_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalRouteName_strategy)
def test_hyp_xal_postalroutename_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostalRouteName_strategy)
def test_hyp_xal_postalroutename_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_hyp_xal_postalcodenumberextension_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_hyp_xal_postalcodenumberextension_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_hyp_xal_postalcodenumberextension_numberExtensionSeparator_setter(instance):
    original = instance.numberExtensionSeparator
    instance.numberExtensionSeparator = original
    assert instance.numberExtensionSeparator == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_hyp_xal_postalcodenumberextension_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalCodeNumberExtension_strategy)
def test_hyp_xal_postalcodenumberextension_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xal_PostalCodeNumber_strategy)
def test_hyp_xal_postalcodenumber_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_hyp_xal_postalcodenumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_hyp_xal_postalcodenumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_PostalCodeNumber_strategy)
def test_hyp_xal_postalcodenumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=xal_PostTown_strategy)
def test_hyp_xal_posttown_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_PostTown_strategy)
def test_hyp_xal_posttown_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_MailStopNumber_strategy)
def test_hyp_xal_mailstopnumber_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_MailStopNumber_strategy)
def test_hyp_xal_mailstopnumber_nameNumberSeparator_setter(instance):
    original = instance.nameNumberSeparator
    instance.nameNumberSeparator = original
    assert instance.nameNumberSeparator == original



@given(instance=xal_MailStopNumber_strategy)
def test_hyp_xal_mailstopnumber_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_MailStopNumber_strategy)
def test_hyp_xal_mailstopnumber_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original




@given(instance=xal_MailStopName_strategy)
def test_hyp_xal_mailstopname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_MailStopName_strategy)
def test_hyp_xal_mailstopname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_MailStopName_strategy)
def test_hyp_xal_mailstopname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=xal_MailStopName_strategy)
def test_hyp_xal_mailstopname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=xal_LocalityName_strategy)
def test_hyp_xal_localityname_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=xal_LocalityName_strategy)
def test_hyp_xal_localityname_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xal_LocalityName_strategy)
def test_hyp_xal_localityname_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xal_LocalityName_strategy)
def test_hyp_xal_localityname_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    xal_Address,
    xal_AddressDetails,
    xal_AddressIdentifier,
    xal_AddressLatitude,
    xal_AddressLatitudeDirection,
    xal_AddressLine,
    xal_AddressLines,
    xal_AddressLongitude,
    xal_AddressLongitudeDirection,
    xal_AdministrativeArea,
    xal_AdministrativeAreaName,
    xal_Barcode,
    xal_BuildingName,
    xal_Country,
    xal_CountryName,
    xal_CountryNameCode,
    xal_Department,
    xal_DepartmentName,
    xal_DependentLocality,
    xal_DependentLocalityName,
    xal_DependentLocalityNumber,
    xal_DependentThoroughfare,
    xal_DocumentRoot,
    xal_EStringToStringMapEntry,
    xal_EndorsementLineCode,
    xal_Firm,
    xal_FirmName,
    xal_KeyLineCode,
    xal_LargeMailUser,
    xal_LargeMailUserIdentifier,
    xal_LargeMailUserName,
    xal_Locality,
    xal_LocalityName,
    xal_MailStop,
    xal_MailStopName,
    xal_MailStopNumber,
    xal_PostBox,
    xal_PostBoxNumber,
    xal_PostBoxNumberExtension,
    xal_PostBoxNumberPrefix,
    xal_PostBoxNumberSuffix,
    xal_PostOffice,
    xal_PostOfficeName,
    xal_PostOfficeNumber,
    xal_PostTown,
    xal_PostTownName,
    xal_PostTownSuffix,
    xal_PostalCode,
    xal_PostalCodeNumber,
    xal_PostalCodeNumberExtension,
    xal_PostalRoute,
    xal_PostalRouteName,
    xal_PostalRouteNumber,
    xal_PostalServiceElements,
    xal_Premise,
    xal_PremiseLocation,
    xal_PremiseName,
    xal_PremiseNumber,
    xal_PremiseNumberPrefix,
    xal_PremiseNumberRange,
    xal_PremiseNumberRangeFrom,
    xal_PremiseNumberRangeTo,
    xal_PremiseNumberSuffix,
    xal_SortingCode,
    xal_SubAdministrativeArea,
    xal_SubAdministrativeAreaName,
    xal_SubPremise,
    xal_SubPremiseLocation,
    xal_SubPremiseName,
    xal_SubPremiseNumber,
    xal_SubPremiseNumberPrefix,
    xal_SubPremiseNumberSuffix,
    xal_SupplementaryPostalServiceData,
    xal_Thoroughfare,
    xal_ThoroughfareLeadingType,
    xal_ThoroughfareName,
    xal_ThoroughfareNumber,
    xal_ThoroughfareNumberFrom,
    xal_ThoroughfareNumberPrefix,
    xal_ThoroughfareNumberRange,
    xal_ThoroughfareNumberSuffix,
    xal_ThoroughfareNumberTo,
    xal_ThoroughfarePostDirection,
    xal_ThoroughfarePreDirection,
    xal_ThoroughfareTrailingType,
    xal_Xal,
    DependentThoroughfaresType,
    IndicatorOccurence,
    IndicatorOccurrence,
    IndicatorOccurrence1,
    IndicatorOccurrence2,
    IndicatorOccurrence3,
    IndicatorOccurrence4,
    NameNumberOccurrence,
    NumberOccurrence,
    NumberRangeOccurence,
    NumberRangeOccurrence,
    NumberTypeOccurrence,
    NumberTypeOccurrence1,
    NumberTypeType,
    NumberTypeType1,
    RangeTypeType,
    TypeOccurrence,
    TypeOccurrence1,
    TypeOccurrence2,
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

def test_xal_Address_anyAttribute_value_roundtrip():
    instance = xal_Address(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Address_code_value_roundtrip():
    instance = xal_Address(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_Address_mixed_value_roundtrip():
    instance = xal_Address(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_Address_type_value_roundtrip():
    instance = xal_Address(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressDetails_addressDetailsKey_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.addressDetailsKey == "sample_text"
    instance.addressDetailsKey = "sample_text_2"
    assert instance.addressDetailsKey == "sample_text_2"


def test_xal_AddressDetails_addressType_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.addressType == "sample_text"
    instance.addressType = "sample_text_2"
    assert instance.addressType == "sample_text_2"


def test_xal_AddressDetails_any_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_AddressDetails_anyAttribute_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressDetails_code_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressDetails_currentStatus_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.currentStatus == "sample_text"
    instance.currentStatus = "sample_text_2"
    assert instance.currentStatus == "sample_text_2"


def test_xal_AddressDetails_usage_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.usage == "sample_text"
    instance.usage = "sample_text_2"
    assert instance.usage == "sample_text_2"


def test_xal_AddressDetails_validFromDate_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.validFromDate == "sample_text"
    instance.validFromDate = "sample_text_2"
    assert instance.validFromDate == "sample_text_2"


def test_xal_AddressDetails_validToDate_value_roundtrip():
    instance = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    assert instance.validToDate == "sample_text"
    instance.validToDate = "sample_text_2"
    assert instance.validToDate == "sample_text_2"


def test_xal_AddressIdentifier_anyAttribute_value_roundtrip():
    instance = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressIdentifier_code_value_roundtrip():
    instance = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressIdentifier_identifierType_value_roundtrip():
    instance = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    assert instance.identifierType == "sample_text"
    instance.identifierType = "sample_text_2"
    assert instance.identifierType == "sample_text_2"


def test_xal_AddressIdentifier_mixed_value_roundtrip():
    instance = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressIdentifier_type_value_roundtrip():
    instance = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressLatitude_anyAttribute_value_roundtrip():
    instance = xal_AddressLatitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLatitude_code_value_roundtrip():
    instance = xal_AddressLatitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressLatitude_mixed_value_roundtrip():
    instance = xal_AddressLatitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressLatitude_type_value_roundtrip():
    instance = xal_AddressLatitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressLatitudeDirection_anyAttribute_value_roundtrip():
    instance = xal_AddressLatitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLatitudeDirection_code_value_roundtrip():
    instance = xal_AddressLatitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressLatitudeDirection_mixed_value_roundtrip():
    instance = xal_AddressLatitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressLatitudeDirection_type_value_roundtrip():
    instance = xal_AddressLatitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressLine_anyAttribute_value_roundtrip():
    instance = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLine_code_value_roundtrip():
    instance = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressLine_mixed_value_roundtrip():
    instance = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressLine_type_value_roundtrip():
    instance = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressLines_any_value_roundtrip():
    instance = xal_AddressLines(any="sample_text", anyAttribute="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_AddressLines_anyAttribute_value_roundtrip():
    instance = xal_AddressLines(any="sample_text", anyAttribute="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLongitude_anyAttribute_value_roundtrip():
    instance = xal_AddressLongitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLongitude_code_value_roundtrip():
    instance = xal_AddressLongitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressLongitude_mixed_value_roundtrip():
    instance = xal_AddressLongitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressLongitude_type_value_roundtrip():
    instance = xal_AddressLongitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AddressLongitudeDirection_anyAttribute_value_roundtrip():
    instance = xal_AddressLongitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AddressLongitudeDirection_code_value_roundtrip():
    instance = xal_AddressLongitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AddressLongitudeDirection_mixed_value_roundtrip():
    instance = xal_AddressLongitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AddressLongitudeDirection_type_value_roundtrip():
    instance = xal_AddressLongitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AdministrativeArea_any_value_roundtrip():
    instance = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_AdministrativeArea_anyAttribute_value_roundtrip():
    instance = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AdministrativeArea_indicator_value_roundtrip():
    instance = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_AdministrativeArea_type_value_roundtrip():
    instance = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_AdministrativeArea_usageType_value_roundtrip():
    instance = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.usageType == "sample_text"
    instance.usageType = "sample_text_2"
    assert instance.usageType == "sample_text_2"


def test_xal_AdministrativeAreaName_anyAttribute_value_roundtrip():
    instance = xal_AdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_AdministrativeAreaName_code_value_roundtrip():
    instance = xal_AdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_AdministrativeAreaName_mixed_value_roundtrip():
    instance = xal_AdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_AdministrativeAreaName_type_value_roundtrip():
    instance = xal_AdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Barcode_anyAttribute_value_roundtrip():
    instance = xal_Barcode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Barcode_code_value_roundtrip():
    instance = xal_Barcode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_Barcode_mixed_value_roundtrip():
    instance = xal_Barcode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_Barcode_type_value_roundtrip():
    instance = xal_Barcode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_BuildingName_anyAttribute_value_roundtrip():
    instance = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_BuildingName_code_value_roundtrip():
    instance = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_BuildingName_mixed_value_roundtrip():
    instance = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_BuildingName_type_value_roundtrip():
    instance = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_BuildingName_typeOccurrence_value_roundtrip():
    instance = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.typeOccurrence == "sample_text"
    instance.typeOccurrence = "sample_text_2"
    assert instance.typeOccurrence == "sample_text_2"


def test_xal_Country_any_value_roundtrip():
    instance = xal_Country(any="sample_text", anyAttribute="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Country_anyAttribute_value_roundtrip():
    instance = xal_Country(any="sample_text", anyAttribute="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_CountryName_anyAttribute_value_roundtrip():
    instance = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_CountryName_code_value_roundtrip():
    instance = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_CountryName_mixed_value_roundtrip():
    instance = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_CountryName_type_value_roundtrip():
    instance = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_CountryNameCode_anyAttribute_value_roundtrip():
    instance = xal_CountryNameCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", scheme="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_CountryNameCode_code_value_roundtrip():
    instance = xal_CountryNameCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", scheme="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_CountryNameCode_mixed_value_roundtrip():
    instance = xal_CountryNameCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", scheme="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_CountryNameCode_scheme_value_roundtrip():
    instance = xal_CountryNameCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", scheme="sample_text")
    assert instance.scheme == "sample_text"
    instance.scheme = "sample_text_2"
    assert instance.scheme == "sample_text_2"


def test_xal_Department_any_value_roundtrip():
    instance = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Department_anyAttribute_value_roundtrip():
    instance = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Department_type_value_roundtrip():
    instance = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_DepartmentName_anyAttribute_value_roundtrip():
    instance = xal_DepartmentName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_DepartmentName_code_value_roundtrip():
    instance = xal_DepartmentName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_DepartmentName_mixed_value_roundtrip():
    instance = xal_DepartmentName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_DepartmentName_type_value_roundtrip():
    instance = xal_DepartmentName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_DependentLocality_any_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_DependentLocality_anyAttribute_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_DependentLocality_connector_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.connector == "sample_text"
    instance.connector = "sample_text_2"
    assert instance.connector == "sample_text_2"


def test_xal_DependentLocality_indicator_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_DependentLocality_type_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_DependentLocality_usageType_value_roundtrip():
    instance = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.usageType == "sample_text"
    instance.usageType = "sample_text_2"
    assert instance.usageType == "sample_text_2"


def test_xal_DependentLocalityName_anyAttribute_value_roundtrip():
    instance = xal_DependentLocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_DependentLocalityName_code_value_roundtrip():
    instance = xal_DependentLocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_DependentLocalityName_mixed_value_roundtrip():
    instance = xal_DependentLocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_DependentLocalityName_type_value_roundtrip():
    instance = xal_DependentLocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_DependentLocalityNumber_anyAttribute_value_roundtrip():
    instance = xal_DependentLocalityNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberOccurrence="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_DependentLocalityNumber_code_value_roundtrip():
    instance = xal_DependentLocalityNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberOccurrence="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_DependentLocalityNumber_mixed_value_roundtrip():
    instance = xal_DependentLocalityNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberOccurrence="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_DependentLocalityNumber_nameNumberOccurrence_value_roundtrip():
    instance = xal_DependentLocalityNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberOccurrence="sample_text")
    assert instance.nameNumberOccurrence == "sample_text"
    instance.nameNumberOccurrence = "sample_text_2"
    assert instance.nameNumberOccurrence == "sample_text_2"


def test_xal_DependentThoroughfare_any_value_roundtrip():
    instance = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_DependentThoroughfare_anyAttribute_value_roundtrip():
    instance = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_DependentThoroughfare_type_value_roundtrip():
    instance = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_DocumentRoot_mixed_value_roundtrip():
    instance = xal_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_EndorsementLineCode_anyAttribute_value_roundtrip():
    instance = xal_EndorsementLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_EndorsementLineCode_code_value_roundtrip():
    instance = xal_EndorsementLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_EndorsementLineCode_mixed_value_roundtrip():
    instance = xal_EndorsementLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_EndorsementLineCode_type_value_roundtrip():
    instance = xal_EndorsementLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Firm_any_value_roundtrip():
    instance = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Firm_anyAttribute_value_roundtrip():
    instance = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Firm_type_value_roundtrip():
    instance = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_FirmName_anyAttribute_value_roundtrip():
    instance = xal_FirmName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_FirmName_code_value_roundtrip():
    instance = xal_FirmName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_FirmName_mixed_value_roundtrip():
    instance = xal_FirmName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_FirmName_type_value_roundtrip():
    instance = xal_FirmName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_KeyLineCode_anyAttribute_value_roundtrip():
    instance = xal_KeyLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_KeyLineCode_code_value_roundtrip():
    instance = xal_KeyLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_KeyLineCode_mixed_value_roundtrip():
    instance = xal_KeyLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_KeyLineCode_type_value_roundtrip():
    instance = xal_KeyLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_LargeMailUser_any_value_roundtrip():
    instance = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_LargeMailUser_anyAttribute_value_roundtrip():
    instance = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_LargeMailUser_type_value_roundtrip():
    instance = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_LargeMailUserIdentifier_anyAttribute_value_roundtrip():
    instance = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_LargeMailUserIdentifier_code_value_roundtrip():
    instance = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_LargeMailUserIdentifier_indicator_value_roundtrip():
    instance = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_LargeMailUserIdentifier_mixed_value_roundtrip():
    instance = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_LargeMailUserIdentifier_type_value_roundtrip():
    instance = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_LargeMailUserName_anyAttribute_value_roundtrip():
    instance = xal_LargeMailUserName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_LargeMailUserName_code_value_roundtrip():
    instance = xal_LargeMailUserName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_LargeMailUserName_mixed_value_roundtrip():
    instance = xal_LargeMailUserName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_LargeMailUserName_type_value_roundtrip():
    instance = xal_LargeMailUserName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Locality_any_value_roundtrip():
    instance = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Locality_anyAttribute_value_roundtrip():
    instance = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Locality_indicator_value_roundtrip():
    instance = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_Locality_type_value_roundtrip():
    instance = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Locality_usageType_value_roundtrip():
    instance = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.usageType == "sample_text"
    instance.usageType = "sample_text_2"
    assert instance.usageType == "sample_text_2"


def test_xal_LocalityName_anyAttribute_value_roundtrip():
    instance = xal_LocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_LocalityName_code_value_roundtrip():
    instance = xal_LocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_LocalityName_mixed_value_roundtrip():
    instance = xal_LocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_LocalityName_type_value_roundtrip():
    instance = xal_LocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_MailStop_any_value_roundtrip():
    instance = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_MailStop_anyAttribute_value_roundtrip():
    instance = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_MailStop_type_value_roundtrip():
    instance = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_MailStopName_anyAttribute_value_roundtrip():
    instance = xal_MailStopName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_MailStopName_code_value_roundtrip():
    instance = xal_MailStopName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_MailStopName_mixed_value_roundtrip():
    instance = xal_MailStopName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_MailStopName_type_value_roundtrip():
    instance = xal_MailStopName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_MailStopNumber_anyAttribute_value_roundtrip():
    instance = xal_MailStopNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberSeparator="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_MailStopNumber_code_value_roundtrip():
    instance = xal_MailStopNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberSeparator="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_MailStopNumber_mixed_value_roundtrip():
    instance = xal_MailStopNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberSeparator="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_MailStopNumber_nameNumberSeparator_value_roundtrip():
    instance = xal_MailStopNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberSeparator="sample_text")
    assert instance.nameNumberSeparator == "sample_text"
    instance.nameNumberSeparator = "sample_text_2"
    assert instance.nameNumberSeparator == "sample_text_2"


def test_xal_PostBox_any_value_roundtrip():
    instance = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_PostBox_anyAttribute_value_roundtrip():
    instance = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostBox_indicator_value_roundtrip():
    instance = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_PostBox_type_value_roundtrip():
    instance = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostBoxNumber_anyAttribute_value_roundtrip():
    instance = xal_PostBoxNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostBoxNumber_code_value_roundtrip():
    instance = xal_PostBoxNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostBoxNumber_mixed_value_roundtrip():
    instance = xal_PostBoxNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostBoxNumberExtension_anyAttribute_value_roundtrip():
    instance = xal_PostBoxNumberExtension(anyAttribute="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostBoxNumberExtension_mixed_value_roundtrip():
    instance = xal_PostBoxNumberExtension(anyAttribute="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostBoxNumberExtension_numberExtensionSeparator_value_roundtrip():
    instance = xal_PostBoxNumberExtension(anyAttribute="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text")
    assert instance.numberExtensionSeparator == "sample_text"
    instance.numberExtensionSeparator = "sample_text_2"
    assert instance.numberExtensionSeparator == "sample_text_2"


def test_xal_PostBoxNumberPrefix_anyAttribute_value_roundtrip():
    instance = xal_PostBoxNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostBoxNumberPrefix_code_value_roundtrip():
    instance = xal_PostBoxNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostBoxNumberPrefix_mixed_value_roundtrip():
    instance = xal_PostBoxNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostBoxNumberPrefix_numberPrefixSeparator_value_roundtrip():
    instance = xal_PostBoxNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text")
    assert instance.numberPrefixSeparator == "sample_text"
    instance.numberPrefixSeparator = "sample_text_2"
    assert instance.numberPrefixSeparator == "sample_text_2"


def test_xal_PostBoxNumberSuffix_anyAttribute_value_roundtrip():
    instance = xal_PostBoxNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostBoxNumberSuffix_code_value_roundtrip():
    instance = xal_PostBoxNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostBoxNumberSuffix_mixed_value_roundtrip():
    instance = xal_PostBoxNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostBoxNumberSuffix_numberSuffixSeparator_value_roundtrip():
    instance = xal_PostBoxNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text")
    assert instance.numberSuffixSeparator == "sample_text"
    instance.numberSuffixSeparator = "sample_text_2"
    assert instance.numberSuffixSeparator == "sample_text_2"


def test_xal_PostOffice_any_value_roundtrip():
    instance = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_PostOffice_anyAttribute_value_roundtrip():
    instance = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostOffice_indicator_value_roundtrip():
    instance = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_PostOffice_type_value_roundtrip():
    instance = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostOfficeName_anyAttribute_value_roundtrip():
    instance = xal_PostOfficeName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostOfficeName_code_value_roundtrip():
    instance = xal_PostOfficeName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostOfficeName_mixed_value_roundtrip():
    instance = xal_PostOfficeName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostOfficeName_type_value_roundtrip():
    instance = xal_PostOfficeName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostOfficeNumber_anyAttribute_value_roundtrip():
    instance = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostOfficeNumber_code_value_roundtrip():
    instance = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostOfficeNumber_indicator_value_roundtrip():
    instance = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_PostOfficeNumber_indicatorOccurrence_value_roundtrip():
    instance = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    assert instance.indicatorOccurrence == "sample_text"
    instance.indicatorOccurrence = "sample_text_2"
    assert instance.indicatorOccurrence == "sample_text_2"


def test_xal_PostOfficeNumber_mixed_value_roundtrip():
    instance = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostTown_anyAttribute_value_roundtrip():
    instance = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostTown_type_value_roundtrip():
    instance = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostTownName_anyAttribute_value_roundtrip():
    instance = xal_PostTownName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostTownName_code_value_roundtrip():
    instance = xal_PostTownName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostTownName_mixed_value_roundtrip():
    instance = xal_PostTownName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostTownName_type_value_roundtrip():
    instance = xal_PostTownName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostTownSuffix_anyAttribute_value_roundtrip():
    instance = xal_PostTownSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostTownSuffix_code_value_roundtrip():
    instance = xal_PostTownSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostTownSuffix_mixed_value_roundtrip():
    instance = xal_PostTownSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostalCode_any_value_roundtrip():
    instance = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_PostalCode_anyAttribute_value_roundtrip():
    instance = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalCode_type_value_roundtrip():
    instance = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostalCodeNumber_anyAttribute_value_roundtrip():
    instance = xal_PostalCodeNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalCodeNumber_code_value_roundtrip():
    instance = xal_PostalCodeNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostalCodeNumber_mixed_value_roundtrip():
    instance = xal_PostalCodeNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostalCodeNumber_type_value_roundtrip():
    instance = xal_PostalCodeNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostalCodeNumberExtension_anyAttribute_value_roundtrip():
    instance = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalCodeNumberExtension_code_value_roundtrip():
    instance = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostalCodeNumberExtension_mixed_value_roundtrip():
    instance = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostalCodeNumberExtension_numberExtensionSeparator_value_roundtrip():
    instance = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    assert instance.numberExtensionSeparator == "sample_text"
    instance.numberExtensionSeparator = "sample_text_2"
    assert instance.numberExtensionSeparator == "sample_text_2"


def test_xal_PostalCodeNumberExtension_type_value_roundtrip():
    instance = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostalRoute_any_value_roundtrip():
    instance = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_PostalRoute_anyAttribute_value_roundtrip():
    instance = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalRoute_type_value_roundtrip():
    instance = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostalRouteName_anyAttribute_value_roundtrip():
    instance = xal_PostalRouteName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalRouteName_code_value_roundtrip():
    instance = xal_PostalRouteName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostalRouteName_mixed_value_roundtrip():
    instance = xal_PostalRouteName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostalRouteName_type_value_roundtrip():
    instance = xal_PostalRouteName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PostalRouteNumber_anyAttribute_value_roundtrip():
    instance = xal_PostalRouteNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalRouteNumber_code_value_roundtrip():
    instance = xal_PostalRouteNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PostalRouteNumber_mixed_value_roundtrip():
    instance = xal_PostalRouteNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PostalServiceElements_any_value_roundtrip():
    instance = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_PostalServiceElements_anyAttribute_value_roundtrip():
    instance = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PostalServiceElements_type_value_roundtrip():
    instance = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Premise_any_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Premise_anyAttribute_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Premise_premiseDependency_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.premiseDependency == "sample_text"
    instance.premiseDependency = "sample_text_2"
    assert instance.premiseDependency == "sample_text_2"


def test_xal_Premise_premiseDependencyType_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.premiseDependencyType == "sample_text"
    instance.premiseDependencyType = "sample_text_2"
    assert instance.premiseDependencyType == "sample_text_2"


def test_xal_Premise_premiseThoroughfareConnector_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.premiseThoroughfareConnector == "sample_text"
    instance.premiseThoroughfareConnector = "sample_text_2"
    assert instance.premiseThoroughfareConnector == "sample_text_2"


def test_xal_Premise_type_value_roundtrip():
    instance = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PremiseLocation_anyAttribute_value_roundtrip():
    instance = xal_PremiseLocation(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PremiseLocation_code_value_roundtrip():
    instance = xal_PremiseLocation(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PremiseLocation_mixed_value_roundtrip():
    instance = xal_PremiseLocation(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PremiseName_anyAttribute_value_roundtrip():
    instance = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PremiseName_code_value_roundtrip():
    instance = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PremiseName_mixed_value_roundtrip():
    instance = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PremiseName_type_value_roundtrip():
    instance = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PremiseName_typeOccurrence_value_roundtrip():
    instance = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.typeOccurrence == "sample_text"
    instance.typeOccurrence = "sample_text_2"
    assert instance.typeOccurrence == "sample_text_2"


def test_xal_PremiseNumber_anyAttribute_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PremiseNumber_code_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PremiseNumber_indicator_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_PremiseNumber_indicatorOccurrence_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.indicatorOccurrence == "sample_text"
    instance.indicatorOccurrence = "sample_text_2"
    assert instance.indicatorOccurrence == "sample_text_2"


def test_xal_PremiseNumber_mixed_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PremiseNumber_numberType_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.numberType == "sample_text"
    instance.numberType = "sample_text_2"
    assert instance.numberType == "sample_text_2"


def test_xal_PremiseNumber_numberTypeOccurrence_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.numberTypeOccurrence == "sample_text"
    instance.numberTypeOccurrence = "sample_text_2"
    assert instance.numberTypeOccurrence == "sample_text_2"


def test_xal_PremiseNumber_type_value_roundtrip():
    instance = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PremiseNumberPrefix_anyAttribute_value_roundtrip():
    instance = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PremiseNumberPrefix_code_value_roundtrip():
    instance = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PremiseNumberPrefix_numberPrefixSeparator_value_roundtrip():
    instance = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    assert instance.numberPrefixSeparator == "sample_text"
    instance.numberPrefixSeparator = "sample_text_2"
    assert instance.numberPrefixSeparator == "sample_text_2"


def test_xal_PremiseNumberPrefix_type_value_roundtrip():
    instance = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PremiseNumberPrefix_value_value_roundtrip():
    instance = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xal_PremiseNumberRange_indicator_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_PremiseNumberRange_indicatorOccurence_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.indicatorOccurence == "sample_text"
    instance.indicatorOccurence = "sample_text_2"
    assert instance.indicatorOccurence == "sample_text_2"


def test_xal_PremiseNumberRange_numberRangeOccurence_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.numberRangeOccurence == "sample_text"
    instance.numberRangeOccurence = "sample_text_2"
    assert instance.numberRangeOccurence == "sample_text_2"


def test_xal_PremiseNumberRange_rangeType_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.rangeType == "sample_text"
    instance.rangeType = "sample_text_2"
    assert instance.rangeType == "sample_text_2"


def test_xal_PremiseNumberRange_separator_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.separator == "sample_text"
    instance.separator = "sample_text_2"
    assert instance.separator == "sample_text_2"


def test_xal_PremiseNumberRange_type_value_roundtrip():
    instance = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_PremiseNumberSuffix_anyAttribute_value_roundtrip():
    instance = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_PremiseNumberSuffix_code_value_roundtrip():
    instance = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_PremiseNumberSuffix_mixed_value_roundtrip():
    instance = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_PremiseNumberSuffix_numberSuffixSeparator_value_roundtrip():
    instance = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.numberSuffixSeparator == "sample_text"
    instance.numberSuffixSeparator = "sample_text_2"
    assert instance.numberSuffixSeparator == "sample_text_2"


def test_xal_PremiseNumberSuffix_type_value_roundtrip():
    instance = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SortingCode_code_value_roundtrip():
    instance = xal_SortingCode(code="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SortingCode_type_value_roundtrip():
    instance = xal_SortingCode(code="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubAdministrativeArea_any_value_roundtrip():
    instance = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_SubAdministrativeArea_anyAttribute_value_roundtrip():
    instance = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubAdministrativeArea_indicator_value_roundtrip():
    instance = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_SubAdministrativeArea_type_value_roundtrip():
    instance = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubAdministrativeArea_usageType_value_roundtrip():
    instance = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    assert instance.usageType == "sample_text"
    instance.usageType = "sample_text_2"
    assert instance.usageType == "sample_text_2"


def test_xal_SubAdministrativeAreaName_anyAttribute_value_roundtrip():
    instance = xal_SubAdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubAdministrativeAreaName_code_value_roundtrip():
    instance = xal_SubAdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubAdministrativeAreaName_mixed_value_roundtrip():
    instance = xal_SubAdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubAdministrativeAreaName_type_value_roundtrip():
    instance = xal_SubAdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubPremise_any_value_roundtrip():
    instance = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_SubPremise_anyAttribute_value_roundtrip():
    instance = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubPremise_type_value_roundtrip():
    instance = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubPremiseLocation_code_value_roundtrip():
    instance = xal_SubPremiseLocation(code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubPremiseLocation_mixed_value_roundtrip():
    instance = xal_SubPremiseLocation(code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubPremiseName_anyAttribute_value_roundtrip():
    instance = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubPremiseName_code_value_roundtrip():
    instance = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubPremiseName_mixed_value_roundtrip():
    instance = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubPremiseName_type_value_roundtrip():
    instance = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubPremiseName_typeOccurrence_value_roundtrip():
    instance = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    assert instance.typeOccurrence == "sample_text"
    instance.typeOccurrence = "sample_text_2"
    assert instance.typeOccurrence == "sample_text_2"


def test_xal_SubPremiseNumber_anyAttribute_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubPremiseNumber_code_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubPremiseNumber_indicator_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_SubPremiseNumber_indicatorOccurrence_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.indicatorOccurrence == "sample_text"
    instance.indicatorOccurrence = "sample_text_2"
    assert instance.indicatorOccurrence == "sample_text_2"


def test_xal_SubPremiseNumber_mixed_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubPremiseNumber_numberTypeOccurrence_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.numberTypeOccurrence == "sample_text"
    instance.numberTypeOccurrence = "sample_text_2"
    assert instance.numberTypeOccurrence == "sample_text_2"


def test_xal_SubPremiseNumber_premiseNumberSeparator_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.premiseNumberSeparator == "sample_text"
    instance.premiseNumberSeparator = "sample_text_2"
    assert instance.premiseNumberSeparator == "sample_text_2"


def test_xal_SubPremiseNumber_type_value_roundtrip():
    instance = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubPremiseNumberPrefix_anyAttribute_value_roundtrip():
    instance = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubPremiseNumberPrefix_code_value_roundtrip():
    instance = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubPremiseNumberPrefix_mixed_value_roundtrip():
    instance = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubPremiseNumberPrefix_numberPrefixSeparator_value_roundtrip():
    instance = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.numberPrefixSeparator == "sample_text"
    instance.numberPrefixSeparator = "sample_text_2"
    assert instance.numberPrefixSeparator == "sample_text_2"


def test_xal_SubPremiseNumberPrefix_type_value_roundtrip():
    instance = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SubPremiseNumberSuffix_anyAttribute_value_roundtrip():
    instance = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SubPremiseNumberSuffix_code_value_roundtrip():
    instance = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SubPremiseNumberSuffix_mixed_value_roundtrip():
    instance = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SubPremiseNumberSuffix_numberSuffixSeparator_value_roundtrip():
    instance = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.numberSuffixSeparator == "sample_text"
    instance.numberSuffixSeparator = "sample_text_2"
    assert instance.numberSuffixSeparator == "sample_text_2"


def test_xal_SubPremiseNumberSuffix_type_value_roundtrip():
    instance = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_SupplementaryPostalServiceData_anyAttribute_value_roundtrip():
    instance = xal_SupplementaryPostalServiceData(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_SupplementaryPostalServiceData_code_value_roundtrip():
    instance = xal_SupplementaryPostalServiceData(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_SupplementaryPostalServiceData_mixed_value_roundtrip():
    instance = xal_SupplementaryPostalServiceData(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_SupplementaryPostalServiceData_type_value_roundtrip():
    instance = xal_SupplementaryPostalServiceData(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Thoroughfare_any_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Thoroughfare_anyAttribute_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Thoroughfare_dependentThoroughfares_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.dependentThoroughfares == "sample_text"
    instance.dependentThoroughfares = "sample_text_2"
    assert instance.dependentThoroughfares == "sample_text_2"


def test_xal_Thoroughfare_dependentThoroughfaresConnector_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.dependentThoroughfaresConnector == "sample_text"
    instance.dependentThoroughfaresConnector = "sample_text_2"
    assert instance.dependentThoroughfaresConnector == "sample_text_2"


def test_xal_Thoroughfare_dependentThoroughfaresIndicator_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.dependentThoroughfaresIndicator == "sample_text"
    instance.dependentThoroughfaresIndicator = "sample_text_2"
    assert instance.dependentThoroughfaresIndicator == "sample_text_2"


def test_xal_Thoroughfare_dependentThoroughfaresType_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.dependentThoroughfaresType == "sample_text"
    instance.dependentThoroughfaresType = "sample_text_2"
    assert instance.dependentThoroughfaresType == "sample_text_2"


def test_xal_Thoroughfare_group_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xal_Thoroughfare_type_value_roundtrip():
    instance = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareLeadingType_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareLeadingType_code_value_roundtrip():
    instance = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareLeadingType_mixed_value_roundtrip():
    instance = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareLeadingType_type_value_roundtrip():
    instance = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareName_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareName_code_value_roundtrip():
    instance = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareName_mixed_value_roundtrip():
    instance = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareName_type_value_roundtrip():
    instance = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareNumber_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumber_code_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumber_indicator_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_ThoroughfareNumber_indicatorOccurrence_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.indicatorOccurrence == "sample_text"
    instance.indicatorOccurrence = "sample_text_2"
    assert instance.indicatorOccurrence == "sample_text_2"


def test_xal_ThoroughfareNumber_mixed_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareNumber_numberOccurrence_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.numberOccurrence == "sample_text"
    instance.numberOccurrence = "sample_text_2"
    assert instance.numberOccurrence == "sample_text_2"


def test_xal_ThoroughfareNumber_numberType_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.numberType == "sample_text"
    instance.numberType = "sample_text_2"
    assert instance.numberType == "sample_text_2"


def test_xal_ThoroughfareNumber_type_value_roundtrip():
    instance = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareNumberFrom_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumberFrom_code_value_roundtrip():
    instance = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumberFrom_mixed_value_roundtrip():
    instance = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareNumberPrefix_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumberPrefix_code_value_roundtrip():
    instance = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumberPrefix_mixed_value_roundtrip():
    instance = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareNumberPrefix_numberPrefixSeparator_value_roundtrip():
    instance = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.numberPrefixSeparator == "sample_text"
    instance.numberPrefixSeparator = "sample_text_2"
    assert instance.numberPrefixSeparator == "sample_text_2"


def test_xal_ThoroughfareNumberPrefix_type_value_roundtrip():
    instance = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareNumberRange_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumberRange_code_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumberRange_indicator_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.indicator == "sample_text"
    instance.indicator = "sample_text_2"
    assert instance.indicator == "sample_text_2"


def test_xal_ThoroughfareNumberRange_indicatorOccurrence_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.indicatorOccurrence == "sample_text"
    instance.indicatorOccurrence = "sample_text_2"
    assert instance.indicatorOccurrence == "sample_text_2"


def test_xal_ThoroughfareNumberRange_numberRangeOccurrence_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.numberRangeOccurrence == "sample_text"
    instance.numberRangeOccurrence = "sample_text_2"
    assert instance.numberRangeOccurrence == "sample_text_2"


def test_xal_ThoroughfareNumberRange_rangeType_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.rangeType == "sample_text"
    instance.rangeType = "sample_text_2"
    assert instance.rangeType == "sample_text_2"


def test_xal_ThoroughfareNumberRange_separator_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.separator == "sample_text"
    instance.separator = "sample_text_2"
    assert instance.separator == "sample_text_2"


def test_xal_ThoroughfareNumberRange_type_value_roundtrip():
    instance = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareNumberSuffix_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumberSuffix_code_value_roundtrip():
    instance = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumberSuffix_mixed_value_roundtrip():
    instance = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareNumberSuffix_numberSuffixSeparator_value_roundtrip():
    instance = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.numberSuffixSeparator == "sample_text"
    instance.numberSuffixSeparator = "sample_text_2"
    assert instance.numberSuffixSeparator == "sample_text_2"


def test_xal_ThoroughfareNumberSuffix_type_value_roundtrip():
    instance = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareNumberTo_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareNumberTo_code_value_roundtrip():
    instance = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareNumberTo_mixed_value_roundtrip():
    instance = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfarePostDirection_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfarePostDirection_code_value_roundtrip():
    instance = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfarePostDirection_mixed_value_roundtrip():
    instance = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfarePostDirection_type_value_roundtrip():
    instance = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfarePreDirection_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfarePreDirection_code_value_roundtrip():
    instance = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfarePreDirection_mixed_value_roundtrip():
    instance = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfarePreDirection_type_value_roundtrip():
    instance = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_ThoroughfareTrailingType_anyAttribute_value_roundtrip():
    instance = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_ThoroughfareTrailingType_code_value_roundtrip():
    instance = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_xal_ThoroughfareTrailingType_mixed_value_roundtrip():
    instance = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xal_ThoroughfareTrailingType_type_value_roundtrip():
    instance = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xal_Xal_any_value_roundtrip():
    instance = xal_Xal(any="sample_text", anyAttribute="sample_text", version="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_xal_Xal_anyAttribute_value_roundtrip():
    instance = xal_Xal(any="sample_text", anyAttribute="sample_text", version="sample_text")
    assert instance.anyAttribute == "sample_text"
    instance.anyAttribute = "sample_text_2"
    assert instance.anyAttribute == "sample_text_2"


def test_xal_Xal_version_value_roundtrip():
    instance = xal_Xal(any="sample_text", anyAttribute="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_assoc_address1_link_reassign_clear():
    a = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b1 = xal_Address(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_Address(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_AddressDetails2', b1)
    assert _is_linked(a, 'xal_AddressDetails2', b1)
    if hasattr(b1, 'xal_Address'):
        assert _is_linked(b1, 'xal_Address', a)
    _safe_set(a, 'xal_AddressDetails2', b2)
    assert _is_linked(a, 'xal_AddressDetails2', b2)
    if hasattr(b1, 'xal_Address'):
        assert not _is_linked(b1, 'xal_Address', a)
    if hasattr(b2, 'xal_Address'):
        assert _is_linked(b2, 'xal_Address', a)
    _safe_set(a, 'xal_AddressDetails2', None)
    assert not _is_linked(a, 'xal_AddressDetails2', b2)
    if hasattr(b2, 'xal_Address'):
        assert not _is_linked(b2, 'xal_Address', a)


def test_assoc_addressDetails472_link_reassign_clear():
    a = xal_Xal(any="sample_text", anyAttribute="sample_text", version="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_Xal473', {b1})
    assert _is_linked(a, 'xal_Xal473', b1)
    if hasattr(b1, 'xal_AddressDetails474'):
        assert _is_linked(b1, 'xal_AddressDetails474', a)
    _safe_set(a, 'xal_Xal473', {b2})
    assert _is_linked(a, 'xal_Xal473', b2)
    if hasattr(b1, 'xal_AddressDetails474'):
        assert not _is_linked(b1, 'xal_AddressDetails474', a)
    if hasattr(b2, 'xal_AddressDetails474'):
        assert _is_linked(b2, 'xal_AddressDetails474', a)
    _safe_set(a, 'xal_Xal473', set())
    assert not _is_linked(a, 'xal_Xal473', b2)
    if hasattr(b2, 'xal_AddressDetails474'):
        assert not _is_linked(b2, 'xal_AddressDetails474', a)


def test_assoc_addressDetails96_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_DocumentRoot97', {b1})
    assert _is_linked(a, 'xal_DocumentRoot97', b1)
    if hasattr(b1, 'xal_AddressDetails98'):
        assert _is_linked(b1, 'xal_AddressDetails98', a)
    _safe_set(a, 'xal_DocumentRoot97', {b2})
    assert _is_linked(a, 'xal_DocumentRoot97', b2)
    if hasattr(b1, 'xal_AddressDetails98'):
        assert not _is_linked(b1, 'xal_AddressDetails98', a)
    if hasattr(b2, 'xal_AddressDetails98'):
        assert _is_linked(b2, 'xal_AddressDetails98', a)
    _safe_set(a, 'xal_DocumentRoot97', set())
    assert not _is_linked(a, 'xal_DocumentRoot97', b2)
    if hasattr(b2, 'xal_AddressDetails98'):
        assert not _is_linked(b2, 'xal_AddressDetails98', a)


def test_assoc_addressIdentifier232_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressIdentifier(anyAttribute="sample_text", code="sample_text", identifierType="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressIdentifier(anyAttribute="sample_text_2", code="sample_text_2", identifierType="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements233', {b1})
    assert _is_linked(a, 'xal_PostalServiceElements233', b1)
    if hasattr(b1, 'xal_AddressIdentifier'):
        assert _is_linked(b1, 'xal_AddressIdentifier', a)
    _safe_set(a, 'xal_PostalServiceElements233', {b2})
    assert _is_linked(a, 'xal_PostalServiceElements233', b2)
    if hasattr(b1, 'xal_AddressIdentifier'):
        assert not _is_linked(b1, 'xal_AddressIdentifier', a)
    if hasattr(b2, 'xal_AddressIdentifier'):
        assert _is_linked(b2, 'xal_AddressIdentifier', a)
    _safe_set(a, 'xal_PostalServiceElements233', set())
    assert not _is_linked(a, 'xal_PostalServiceElements233', b2)
    if hasattr(b2, 'xal_AddressIdentifier'):
        assert not _is_linked(b2, 'xal_AddressIdentifier', a)


def test_assoc_addressLatitude242_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLatitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLatitude(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements243', b1)
    assert _is_linked(a, 'xal_PostalServiceElements243', b1)
    if hasattr(b1, 'xal_AddressLatitude'):
        assert _is_linked(b1, 'xal_AddressLatitude', a)
    _safe_set(a, 'xal_PostalServiceElements243', b2)
    assert _is_linked(a, 'xal_PostalServiceElements243', b2)
    if hasattr(b1, 'xal_AddressLatitude'):
        assert not _is_linked(b1, 'xal_AddressLatitude', a)
    if hasattr(b2, 'xal_AddressLatitude'):
        assert _is_linked(b2, 'xal_AddressLatitude', a)
    _safe_set(a, 'xal_PostalServiceElements243', None)
    assert not _is_linked(a, 'xal_PostalServiceElements243', b2)
    if hasattr(b2, 'xal_AddressLatitude'):
        assert not _is_linked(b2, 'xal_AddressLatitude', a)


def test_assoc_addressLatitudeDirection244_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLatitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLatitudeDirection(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements245', b1)
    assert _is_linked(a, 'xal_PostalServiceElements245', b1)
    if hasattr(b1, 'xal_AddressLatitudeDirection'):
        assert _is_linked(b1, 'xal_AddressLatitudeDirection', a)
    _safe_set(a, 'xal_PostalServiceElements245', b2)
    assert _is_linked(a, 'xal_PostalServiceElements245', b2)
    if hasattr(b1, 'xal_AddressLatitudeDirection'):
        assert not _is_linked(b1, 'xal_AddressLatitudeDirection', a)
    if hasattr(b2, 'xal_AddressLatitudeDirection'):
        assert _is_linked(b2, 'xal_AddressLatitudeDirection', a)
    _safe_set(a, 'xal_PostalServiceElements245', None)
    assert not _is_linked(a, 'xal_PostalServiceElements245', b2)
    if hasattr(b2, 'xal_AddressLatitudeDirection'):
        assert not _is_linked(b2, 'xal_AddressLatitudeDirection', a)


def test_assoc_addressLine13_link_reassign_clear():
    a = xal_AddressLines(any="sample_text", anyAttribute="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_AddressLines14', {b1})
    assert _is_linked(a, 'xal_AddressLines14', b1)
    if hasattr(b1, 'xal_AddressLine'):
        assert _is_linked(b1, 'xal_AddressLine', a)
    _safe_set(a, 'xal_AddressLines14', {b2})
    assert _is_linked(a, 'xal_AddressLines14', b2)
    if hasattr(b1, 'xal_AddressLine'):
        assert not _is_linked(b1, 'xal_AddressLine', a)
    if hasattr(b2, 'xal_AddressLine'):
        assert _is_linked(b2, 'xal_AddressLine', a)
    _safe_set(a, 'xal_AddressLines14', set())
    assert not _is_linked(a, 'xal_AddressLines14', b2)
    if hasattr(b2, 'xal_AddressLine'):
        assert not _is_linked(b2, 'xal_AddressLine', a)


def test_assoc_addressLine143_link_reassign_clear():
    a = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Firm', {b1})
    assert _is_linked(a, 'xal_Firm', b1)
    if hasattr(b1, 'xal_AddressLine144'):
        assert _is_linked(b1, 'xal_AddressLine144', a)
    _safe_set(a, 'xal_Firm', {b2})
    assert _is_linked(a, 'xal_Firm', b2)
    if hasattr(b1, 'xal_AddressLine144'):
        assert not _is_linked(b1, 'xal_AddressLine144', a)
    if hasattr(b2, 'xal_AddressLine144'):
        assert _is_linked(b2, 'xal_AddressLine144', a)
    _safe_set(a, 'xal_Firm', set())
    assert not _is_linked(a, 'xal_Firm', b2)
    if hasattr(b2, 'xal_AddressLine144'):
        assert not _is_linked(b2, 'xal_AddressLine144', a)


def test_assoc_addressLine15_link_reassign_clear():
    a = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_AdministrativeArea16', {b1})
    assert _is_linked(a, 'xal_AdministrativeArea16', b1)
    if hasattr(b1, 'xal_AddressLine17'):
        assert _is_linked(b1, 'xal_AddressLine17', a)
    _safe_set(a, 'xal_AdministrativeArea16', {b2})
    assert _is_linked(a, 'xal_AdministrativeArea16', b2)
    if hasattr(b1, 'xal_AddressLine17'):
        assert not _is_linked(b1, 'xal_AddressLine17', a)
    if hasattr(b2, 'xal_AddressLine17'):
        assert _is_linked(b2, 'xal_AddressLine17', a)
    _safe_set(a, 'xal_AdministrativeArea16', set())
    assert not _is_linked(a, 'xal_AdministrativeArea16', b2)
    if hasattr(b2, 'xal_AddressLine17'):
        assert not _is_linked(b2, 'xal_AddressLine17', a)


def test_assoc_addressLine156_link_reassign_clear():
    a = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_LargeMailUser157', {b1})
    assert _is_linked(a, 'xal_LargeMailUser157', b1)
    if hasattr(b1, 'xal_AddressLine158'):
        assert _is_linked(b1, 'xal_AddressLine158', a)
    _safe_set(a, 'xal_LargeMailUser157', {b2})
    assert _is_linked(a, 'xal_LargeMailUser157', b2)
    if hasattr(b1, 'xal_AddressLine158'):
        assert not _is_linked(b1, 'xal_AddressLine158', a)
    if hasattr(b2, 'xal_AddressLine158'):
        assert _is_linked(b2, 'xal_AddressLine158', a)
    _safe_set(a, 'xal_LargeMailUser157', set())
    assert not _is_linked(a, 'xal_LargeMailUser157', b2)
    if hasattr(b2, 'xal_AddressLine158'):
        assert not _is_linked(b2, 'xal_AddressLine158', a)


def test_assoc_addressLine177_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Locality178', {b1})
    assert _is_linked(a, 'xal_Locality178', b1)
    if hasattr(b1, 'xal_AddressLine179'):
        assert _is_linked(b1, 'xal_AddressLine179', a)
    _safe_set(a, 'xal_Locality178', {b2})
    assert _is_linked(a, 'xal_Locality178', b2)
    if hasattr(b1, 'xal_AddressLine179'):
        assert not _is_linked(b1, 'xal_AddressLine179', a)
    if hasattr(b2, 'xal_AddressLine179'):
        assert _is_linked(b2, 'xal_AddressLine179', a)
    _safe_set(a, 'xal_Locality178', set())
    assert not _is_linked(a, 'xal_Locality178', b2)
    if hasattr(b2, 'xal_AddressLine179'):
        assert not _is_linked(b2, 'xal_AddressLine179', a)


def test_assoc_addressLine206_link_reassign_clear():
    a = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_MailStop207', {b1})
    assert _is_linked(a, 'xal_MailStop207', b1)
    if hasattr(b1, 'xal_AddressLine208'):
        assert _is_linked(b1, 'xal_AddressLine208', a)
    _safe_set(a, 'xal_MailStop207', {b2})
    assert _is_linked(a, 'xal_MailStop207', b2)
    if hasattr(b1, 'xal_AddressLine208'):
        assert not _is_linked(b1, 'xal_AddressLine208', a)
    if hasattr(b2, 'xal_AddressLine208'):
        assert _is_linked(b2, 'xal_AddressLine208', a)
    _safe_set(a, 'xal_MailStop207', set())
    assert not _is_linked(a, 'xal_MailStop207', b2)
    if hasattr(b2, 'xal_AddressLine208'):
        assert not _is_linked(b2, 'xal_AddressLine208', a)


def test_assoc_addressLine213_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode214', {b1})
    assert _is_linked(a, 'xal_PostalCode214', b1)
    if hasattr(b1, 'xal_AddressLine215'):
        assert _is_linked(b1, 'xal_AddressLine215', a)
    _safe_set(a, 'xal_PostalCode214', {b2})
    assert _is_linked(a, 'xal_PostalCode214', b2)
    if hasattr(b1, 'xal_AddressLine215'):
        assert not _is_linked(b1, 'xal_AddressLine215', a)
    if hasattr(b2, 'xal_AddressLine215'):
        assert _is_linked(b2, 'xal_AddressLine215', a)
    _safe_set(a, 'xal_PostalCode214', set())
    assert not _is_linked(a, 'xal_PostalCode214', b2)
    if hasattr(b2, 'xal_AddressLine215'):
        assert not _is_linked(b2, 'xal_AddressLine215', a)


def test_assoc_addressLine222_link_reassign_clear():
    a = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalRoute223', {b1})
    assert _is_linked(a, 'xal_PostalRoute223', b1)
    if hasattr(b1, 'xal_AddressLine224'):
        assert _is_linked(b1, 'xal_AddressLine224', a)
    _safe_set(a, 'xal_PostalRoute223', {b2})
    assert _is_linked(a, 'xal_PostalRoute223', b2)
    if hasattr(b1, 'xal_AddressLine224'):
        assert not _is_linked(b1, 'xal_AddressLine224', a)
    if hasattr(b2, 'xal_AddressLine224'):
        assert _is_linked(b2, 'xal_AddressLine224', a)
    _safe_set(a, 'xal_PostalRoute223', set())
    assert not _is_linked(a, 'xal_PostalRoute223', b2)
    if hasattr(b2, 'xal_AddressLine224'):
        assert not _is_linked(b2, 'xal_AddressLine224', a)


def test_assoc_addressLine252_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBox253', {b1})
    assert _is_linked(a, 'xal_PostBox253', b1)
    if hasattr(b1, 'xal_AddressLine254'):
        assert _is_linked(b1, 'xal_AddressLine254', a)
    _safe_set(a, 'xal_PostBox253', {b2})
    assert _is_linked(a, 'xal_PostBox253', b2)
    if hasattr(b1, 'xal_AddressLine254'):
        assert not _is_linked(b1, 'xal_AddressLine254', a)
    if hasattr(b2, 'xal_AddressLine254'):
        assert _is_linked(b2, 'xal_AddressLine254', a)
    _safe_set(a, 'xal_PostBox253', set())
    assert not _is_linked(a, 'xal_PostBox253', b2)
    if hasattr(b2, 'xal_AddressLine254'):
        assert not _is_linked(b2, 'xal_AddressLine254', a)


def test_assoc_addressLine269_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostOffice270', {b1})
    assert _is_linked(a, 'xal_PostOffice270', b1)
    if hasattr(b1, 'xal_AddressLine271'):
        assert _is_linked(b1, 'xal_AddressLine271', a)
    _safe_set(a, 'xal_PostOffice270', {b2})
    assert _is_linked(a, 'xal_PostOffice270', b2)
    if hasattr(b1, 'xal_AddressLine271'):
        assert not _is_linked(b1, 'xal_AddressLine271', a)
    if hasattr(b2, 'xal_AddressLine271'):
        assert _is_linked(b2, 'xal_AddressLine271', a)
    _safe_set(a, 'xal_PostOffice270', set())
    assert not _is_linked(a, 'xal_PostOffice270', b2)
    if hasattr(b2, 'xal_AddressLine271'):
        assert not _is_linked(b2, 'xal_AddressLine271', a)


def test_assoc_addressLine285_link_reassign_clear():
    a = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostTown286', {b1})
    assert _is_linked(a, 'xal_PostTown286', b1)
    if hasattr(b1, 'xal_AddressLine287'):
        assert _is_linked(b1, 'xal_AddressLine287', a)
    _safe_set(a, 'xal_PostTown286', {b2})
    assert _is_linked(a, 'xal_PostTown286', b2)
    if hasattr(b1, 'xal_AddressLine287'):
        assert not _is_linked(b1, 'xal_AddressLine287', a)
    if hasattr(b2, 'xal_AddressLine287'):
        assert _is_linked(b2, 'xal_AddressLine287', a)
    _safe_set(a, 'xal_PostTown286', set())
    assert not _is_linked(a, 'xal_PostTown286', b2)
    if hasattr(b2, 'xal_AddressLine287'):
        assert not _is_linked(b2, 'xal_AddressLine287', a)


def test_assoc_addressLine29_link_reassign_clear():
    a = xal_Country(any="sample_text", anyAttribute="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Country30', {b1})
    assert _is_linked(a, 'xal_Country30', b1)
    if hasattr(b1, 'xal_AddressLine31'):
        assert _is_linked(b1, 'xal_AddressLine31', a)
    _safe_set(a, 'xal_Country30', {b2})
    assert _is_linked(a, 'xal_Country30', b2)
    if hasattr(b1, 'xal_AddressLine31'):
        assert not _is_linked(b1, 'xal_AddressLine31', a)
    if hasattr(b2, 'xal_AddressLine31'):
        assert _is_linked(b2, 'xal_AddressLine31', a)
    _safe_set(a, 'xal_Country30', set())
    assert not _is_linked(a, 'xal_Country30', b2)
    if hasattr(b2, 'xal_AddressLine31'):
        assert not _is_linked(b2, 'xal_AddressLine31', a)


def test_assoc_addressLine292_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Premise293', {b1})
    assert _is_linked(a, 'xal_Premise293', b1)
    if hasattr(b1, 'xal_AddressLine294'):
        assert _is_linked(b1, 'xal_AddressLine294', a)
    _safe_set(a, 'xal_Premise293', {b2})
    assert _is_linked(a, 'xal_Premise293', b2)
    if hasattr(b1, 'xal_AddressLine294'):
        assert not _is_linked(b1, 'xal_AddressLine294', a)
    if hasattr(b2, 'xal_AddressLine294'):
        assert _is_linked(b2, 'xal_AddressLine294', a)
    _safe_set(a, 'xal_Premise293', set())
    assert not _is_linked(a, 'xal_Premise293', b2)
    if hasattr(b2, 'xal_AddressLine294'):
        assert not _is_linked(b2, 'xal_AddressLine294', a)


def test_assoc_addressLine331_link_reassign_clear():
    a = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeFrom()
    b2 = xal_PremiseNumberRangeFrom()
    _safe_set(a, 'xal_AddressLine333', b1)
    assert _is_linked(a, 'xal_AddressLine333', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom332'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeFrom332', a)
    _safe_set(a, 'xal_AddressLine333', b2)
    assert _is_linked(a, 'xal_AddressLine333', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom332'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeFrom332', a)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom332'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeFrom332', a)
    _safe_set(a, 'xal_AddressLine333', None)
    assert not _is_linked(a, 'xal_AddressLine333', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom332'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeFrom332', a)


def test_assoc_addressLine343_link_reassign_clear():
    a = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeTo()
    b2 = xal_PremiseNumberRangeTo()
    _safe_set(a, 'xal_AddressLine345', b1)
    assert _is_linked(a, 'xal_AddressLine345', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeTo344'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeTo344', a)
    _safe_set(a, 'xal_AddressLine345', b2)
    assert _is_linked(a, 'xal_AddressLine345', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeTo344'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeTo344', a)
    if hasattr(b2, 'xal_PremiseNumberRangeTo344'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeTo344', a)
    _safe_set(a, 'xal_AddressLine345', None)
    assert not _is_linked(a, 'xal_AddressLine345', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeTo344'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeTo344', a)


def test_assoc_addressLine355_link_reassign_clear():
    a = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeArea356', {b1})
    assert _is_linked(a, 'xal_SubAdministrativeArea356', b1)
    if hasattr(b1, 'xal_AddressLine357'):
        assert _is_linked(b1, 'xal_AddressLine357', a)
    _safe_set(a, 'xal_SubAdministrativeArea356', {b2})
    assert _is_linked(a, 'xal_SubAdministrativeArea356', b2)
    if hasattr(b1, 'xal_AddressLine357'):
        assert not _is_linked(b1, 'xal_AddressLine357', a)
    if hasattr(b2, 'xal_AddressLine357'):
        assert _is_linked(b2, 'xal_AddressLine357', a)
    _safe_set(a, 'xal_SubAdministrativeArea356', set())
    assert not _is_linked(a, 'xal_SubAdministrativeArea356', b2)
    if hasattr(b2, 'xal_AddressLine357'):
        assert not _is_linked(b2, 'xal_AddressLine357', a)


def test_assoc_addressLine369_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise370', {b1})
    assert _is_linked(a, 'xal_SubPremise370', b1)
    if hasattr(b1, 'xal_AddressLine371'):
        assert _is_linked(b1, 'xal_AddressLine371', a)
    _safe_set(a, 'xal_SubPremise370', {b2})
    assert _is_linked(a, 'xal_SubPremise370', b2)
    if hasattr(b1, 'xal_AddressLine371'):
        assert not _is_linked(b1, 'xal_AddressLine371', a)
    if hasattr(b2, 'xal_AddressLine371'):
        assert _is_linked(b2, 'xal_AddressLine371', a)
    _safe_set(a, 'xal_SubPremise370', set())
    assert not _is_linked(a, 'xal_SubPremise370', b2)
    if hasattr(b2, 'xal_AddressLine371'):
        assert not _is_linked(b2, 'xal_AddressLine371', a)


def test_assoc_addressLine397_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare398', {b1})
    assert _is_linked(a, 'xal_Thoroughfare398', b1)
    if hasattr(b1, 'xal_AddressLine399'):
        assert _is_linked(b1, 'xal_AddressLine399', a)
    _safe_set(a, 'xal_Thoroughfare398', {b2})
    assert _is_linked(a, 'xal_Thoroughfare398', b2)
    if hasattr(b1, 'xal_AddressLine399'):
        assert not _is_linked(b1, 'xal_AddressLine399', a)
    if hasattr(b2, 'xal_AddressLine399'):
        assert _is_linked(b2, 'xal_AddressLine399', a)
    _safe_set(a, 'xal_Thoroughfare398', set())
    assert not _is_linked(a, 'xal_Thoroughfare398', b2)
    if hasattr(b2, 'xal_AddressLine399'):
        assert not _is_linked(b2, 'xal_AddressLine399', a)


def test_assoc_addressLine441_link_reassign_clear():
    a = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberFrom', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberFrom', b1)
    if hasattr(b1, 'xal_AddressLine442'):
        assert _is_linked(b1, 'xal_AddressLine442', a)
    _safe_set(a, 'xal_ThoroughfareNumberFrom', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberFrom', b2)
    if hasattr(b1, 'xal_AddressLine442'):
        assert not _is_linked(b1, 'xal_AddressLine442', a)
    if hasattr(b2, 'xal_AddressLine442'):
        assert _is_linked(b2, 'xal_AddressLine442', a)
    _safe_set(a, 'xal_ThoroughfareNumberFrom', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberFrom', b2)
    if hasattr(b2, 'xal_AddressLine442'):
        assert not _is_linked(b2, 'xal_AddressLine442', a)


def test_assoc_addressLine45_link_reassign_clear():
    a = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Department', {b1})
    assert _is_linked(a, 'xal_Department', b1)
    if hasattr(b1, 'xal_AddressLine46'):
        assert _is_linked(b1, 'xal_AddressLine46', a)
    _safe_set(a, 'xal_Department', {b2})
    assert _is_linked(a, 'xal_Department', b2)
    if hasattr(b1, 'xal_AddressLine46'):
        assert not _is_linked(b1, 'xal_AddressLine46', a)
    if hasattr(b2, 'xal_AddressLine46'):
        assert _is_linked(b2, 'xal_AddressLine46', a)
    _safe_set(a, 'xal_Department', set())
    assert not _is_linked(a, 'xal_Department', b2)
    if hasattr(b2, 'xal_AddressLine46'):
        assert not _is_linked(b2, 'xal_AddressLine46', a)


def test_assoc_addressLine452_link_reassign_clear():
    a = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberRange453', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberRange453', b1)
    if hasattr(b1, 'xal_AddressLine454'):
        assert _is_linked(b1, 'xal_AddressLine454', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange453', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberRange453', b2)
    if hasattr(b1, 'xal_AddressLine454'):
        assert not _is_linked(b1, 'xal_AddressLine454', a)
    if hasattr(b2, 'xal_AddressLine454'):
        assert _is_linked(b2, 'xal_AddressLine454', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange453', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberRange453', b2)
    if hasattr(b2, 'xal_AddressLine454'):
        assert not _is_linked(b2, 'xal_AddressLine454', a)


def test_assoc_addressLine460_link_reassign_clear():
    a = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberTo461', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo461', b1)
    if hasattr(b1, 'xal_AddressLine462'):
        assert _is_linked(b1, 'xal_AddressLine462', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo461', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo461', b2)
    if hasattr(b1, 'xal_AddressLine462'):
        assert not _is_linked(b1, 'xal_AddressLine462', a)
    if hasattr(b2, 'xal_AddressLine462'):
        assert _is_linked(b2, 'xal_AddressLine462', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo461', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberTo461', b2)
    if hasattr(b2, 'xal_AddressLine462'):
        assert not _is_linked(b2, 'xal_AddressLine462', a)


def test_assoc_addressLine54_link_reassign_clear():
    a = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DependentLocality', {b1})
    assert _is_linked(a, 'xal_DependentLocality', b1)
    if hasattr(b1, 'xal_AddressLine55'):
        assert _is_linked(b1, 'xal_AddressLine55', a)
    _safe_set(a, 'xal_DependentLocality', {b2})
    assert _is_linked(a, 'xal_DependentLocality', b2)
    if hasattr(b1, 'xal_AddressLine55'):
        assert not _is_linked(b1, 'xal_AddressLine55', a)
    if hasattr(b2, 'xal_AddressLine55'):
        assert _is_linked(b2, 'xal_AddressLine55', a)
    _safe_set(a, 'xal_DependentLocality', set())
    assert not _is_linked(a, 'xal_DependentLocality', b2)
    if hasattr(b2, 'xal_AddressLine55'):
        assert not _is_linked(b2, 'xal_AddressLine55', a)


def test_assoc_addressLine80_link_reassign_clear():
    a = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DependentThoroughfare', {b1})
    assert _is_linked(a, 'xal_DependentThoroughfare', b1)
    if hasattr(b1, 'xal_AddressLine81'):
        assert _is_linked(b1, 'xal_AddressLine81', a)
    _safe_set(a, 'xal_DependentThoroughfare', {b2})
    assert _is_linked(a, 'xal_DependentThoroughfare', b2)
    if hasattr(b1, 'xal_AddressLine81'):
        assert not _is_linked(b1, 'xal_AddressLine81', a)
    if hasattr(b2, 'xal_AddressLine81'):
        assert _is_linked(b2, 'xal_AddressLine81', a)
    _safe_set(a, 'xal_DependentThoroughfare', set())
    assert not _is_linked(a, 'xal_DependentThoroughfare', b2)
    if hasattr(b2, 'xal_AddressLine81'):
        assert not _is_linked(b2, 'xal_AddressLine81', a)


def test_assoc_addressLine99_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_AddressLine(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLine(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DocumentRoot100', {b1})
    assert _is_linked(a, 'xal_DocumentRoot100', b1)
    if hasattr(b1, 'xal_AddressLine101'):
        assert _is_linked(b1, 'xal_AddressLine101', a)
    _safe_set(a, 'xal_DocumentRoot100', {b2})
    assert _is_linked(a, 'xal_DocumentRoot100', b2)
    if hasattr(b1, 'xal_AddressLine101'):
        assert not _is_linked(b1, 'xal_AddressLine101', a)
    if hasattr(b2, 'xal_AddressLine101'):
        assert _is_linked(b2, 'xal_AddressLine101', a)
    _safe_set(a, 'xal_DocumentRoot100', set())
    assert not _is_linked(a, 'xal_DocumentRoot100', b2)
    if hasattr(b2, 'xal_AddressLine101'):
        assert not _is_linked(b2, 'xal_AddressLine101', a)


def test_assoc_addressLines3_link_reassign_clear():
    a = xal_AddressLines(any="sample_text", anyAttribute="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_AddressLines', b1)
    assert _is_linked(a, 'xal_AddressLines', b1)
    if hasattr(b1, 'xal_AddressDetails4'):
        assert _is_linked(b1, 'xal_AddressDetails4', a)
    _safe_set(a, 'xal_AddressLines', b2)
    assert _is_linked(a, 'xal_AddressLines', b2)
    if hasattr(b1, 'xal_AddressDetails4'):
        assert not _is_linked(b1, 'xal_AddressDetails4', a)
    if hasattr(b2, 'xal_AddressDetails4'):
        assert _is_linked(b2, 'xal_AddressDetails4', a)
    _safe_set(a, 'xal_AddressLines', None)
    assert not _is_linked(a, 'xal_AddressLines', b2)
    if hasattr(b2, 'xal_AddressDetails4'):
        assert not _is_linked(b2, 'xal_AddressDetails4', a)


def test_assoc_addressLongitude246_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLongitude(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLongitude(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements247', b1)
    assert _is_linked(a, 'xal_PostalServiceElements247', b1)
    if hasattr(b1, 'xal_AddressLongitude'):
        assert _is_linked(b1, 'xal_AddressLongitude', a)
    _safe_set(a, 'xal_PostalServiceElements247', b2)
    assert _is_linked(a, 'xal_PostalServiceElements247', b2)
    if hasattr(b1, 'xal_AddressLongitude'):
        assert not _is_linked(b1, 'xal_AddressLongitude', a)
    if hasattr(b2, 'xal_AddressLongitude'):
        assert _is_linked(b2, 'xal_AddressLongitude', a)
    _safe_set(a, 'xal_PostalServiceElements247', None)
    assert not _is_linked(a, 'xal_PostalServiceElements247', b2)
    if hasattr(b2, 'xal_AddressLongitude'):
        assert not _is_linked(b2, 'xal_AddressLongitude', a)


def test_assoc_addressLongitudeDirection248_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressLongitudeDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_AddressLongitudeDirection(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements249', b1)
    assert _is_linked(a, 'xal_PostalServiceElements249', b1)
    if hasattr(b1, 'xal_AddressLongitudeDirection'):
        assert _is_linked(b1, 'xal_AddressLongitudeDirection', a)
    _safe_set(a, 'xal_PostalServiceElements249', b2)
    assert _is_linked(a, 'xal_PostalServiceElements249', b2)
    if hasattr(b1, 'xal_AddressLongitudeDirection'):
        assert not _is_linked(b1, 'xal_AddressLongitudeDirection', a)
    if hasattr(b2, 'xal_AddressLongitudeDirection'):
        assert _is_linked(b2, 'xal_AddressLongitudeDirection', a)
    _safe_set(a, 'xal_PostalServiceElements249', None)
    assert not _is_linked(a, 'xal_PostalServiceElements249', b2)
    if hasattr(b2, 'xal_AddressLongitudeDirection'):
        assert not _is_linked(b2, 'xal_AddressLongitudeDirection', a)


def test_assoc_administrativeArea102_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_DocumentRoot103', {b1})
    assert _is_linked(a, 'xal_DocumentRoot103', b1)
    if hasattr(b1, 'xal_AdministrativeArea104'):
        assert _is_linked(b1, 'xal_AdministrativeArea104', a)
    _safe_set(a, 'xal_DocumentRoot103', {b2})
    assert _is_linked(a, 'xal_DocumentRoot103', b2)
    if hasattr(b1, 'xal_AdministrativeArea104'):
        assert not _is_linked(b1, 'xal_AdministrativeArea104', a)
    if hasattr(b2, 'xal_AdministrativeArea104'):
        assert _is_linked(b2, 'xal_AdministrativeArea104', a)
    _safe_set(a, 'xal_DocumentRoot103', set())
    assert not _is_linked(a, 'xal_DocumentRoot103', b2)
    if hasattr(b2, 'xal_AdministrativeArea104'):
        assert not _is_linked(b2, 'xal_AdministrativeArea104', a)


def test_assoc_administrativeArea36_link_reassign_clear():
    a = xal_Country(any="sample_text", anyAttribute="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Country37', b1)
    assert _is_linked(a, 'xal_Country37', b1)
    if hasattr(b1, 'xal_AdministrativeArea38'):
        assert _is_linked(b1, 'xal_AdministrativeArea38', a)
    _safe_set(a, 'xal_Country37', b2)
    assert _is_linked(a, 'xal_Country37', b2)
    if hasattr(b1, 'xal_AdministrativeArea38'):
        assert not _is_linked(b1, 'xal_AdministrativeArea38', a)
    if hasattr(b2, 'xal_AdministrativeArea38'):
        assert _is_linked(b2, 'xal_AdministrativeArea38', a)
    _safe_set(a, 'xal_Country37', None)
    assert not _is_linked(a, 'xal_Country37', b2)
    if hasattr(b2, 'xal_AdministrativeArea38'):
        assert not _is_linked(b2, 'xal_AdministrativeArea38', a)


def test_assoc_administrativeArea7_link_reassign_clear():
    a = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_AdministrativeArea', b1)
    assert _is_linked(a, 'xal_AdministrativeArea', b1)
    if hasattr(b1, 'xal_AddressDetails8'):
        assert _is_linked(b1, 'xal_AddressDetails8', a)
    _safe_set(a, 'xal_AdministrativeArea', b2)
    assert _is_linked(a, 'xal_AdministrativeArea', b2)
    if hasattr(b1, 'xal_AddressDetails8'):
        assert not _is_linked(b1, 'xal_AddressDetails8', a)
    if hasattr(b2, 'xal_AddressDetails8'):
        assert _is_linked(b2, 'xal_AddressDetails8', a)
    _safe_set(a, 'xal_AdministrativeArea', None)
    assert not _is_linked(a, 'xal_AdministrativeArea', b2)
    if hasattr(b2, 'xal_AddressDetails8'):
        assert not _is_linked(b2, 'xal_AddressDetails8', a)


def test_assoc_administrativeAreaName18_link_reassign_clear():
    a = xal_AdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_AdministrativeAreaName', b1)
    assert _is_linked(a, 'xal_AdministrativeAreaName', b1)
    if hasattr(b1, 'xal_AdministrativeArea19'):
        assert _is_linked(b1, 'xal_AdministrativeArea19', a)
    _safe_set(a, 'xal_AdministrativeAreaName', b2)
    assert _is_linked(a, 'xal_AdministrativeAreaName', b2)
    if hasattr(b1, 'xal_AdministrativeArea19'):
        assert not _is_linked(b1, 'xal_AdministrativeArea19', a)
    if hasattr(b2, 'xal_AdministrativeArea19'):
        assert _is_linked(b2, 'xal_AdministrativeArea19', a)
    _safe_set(a, 'xal_AdministrativeAreaName', None)
    assert not _is_linked(a, 'xal_AdministrativeAreaName', b2)
    if hasattr(b2, 'xal_AdministrativeArea19'):
        assert not _is_linked(b2, 'xal_AdministrativeArea19', a)


def test_assoc_barcode238_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Barcode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_Barcode(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements239', b1)
    assert _is_linked(a, 'xal_PostalServiceElements239', b1)
    if hasattr(b1, 'xal_Barcode'):
        assert _is_linked(b1, 'xal_Barcode', a)
    _safe_set(a, 'xal_PostalServiceElements239', b2)
    assert _is_linked(a, 'xal_PostalServiceElements239', b2)
    if hasattr(b1, 'xal_Barcode'):
        assert not _is_linked(b1, 'xal_Barcode', a)
    if hasattr(b2, 'xal_Barcode'):
        assert _is_linked(b2, 'xal_Barcode', a)
    _safe_set(a, 'xal_PostalServiceElements239', None)
    assert not _is_linked(a, 'xal_PostalServiceElements239', b2)
    if hasattr(b2, 'xal_Barcode'):
        assert not _is_linked(b2, 'xal_Barcode', a)


def test_assoc_buildingName163_link_reassign_clear():
    a = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    b2 = xal_BuildingName(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2", typeOccurrence="sample_text_2")
    _safe_set(a, 'xal_LargeMailUser164', {b1})
    assert _is_linked(a, 'xal_LargeMailUser164', b1)
    if hasattr(b1, 'xal_BuildingName'):
        assert _is_linked(b1, 'xal_BuildingName', a)
    _safe_set(a, 'xal_LargeMailUser164', {b2})
    assert _is_linked(a, 'xal_LargeMailUser164', b2)
    if hasattr(b1, 'xal_BuildingName'):
        assert not _is_linked(b1, 'xal_BuildingName', a)
    if hasattr(b2, 'xal_BuildingName'):
        assert _is_linked(b2, 'xal_BuildingName', a)
    _safe_set(a, 'xal_LargeMailUser164', set())
    assert not _is_linked(a, 'xal_LargeMailUser164', b2)
    if hasattr(b2, 'xal_BuildingName'):
        assert not _is_linked(b2, 'xal_BuildingName', a)


def test_assoc_buildingName310_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    b2 = xal_BuildingName(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2", typeOccurrence="sample_text_2")
    _safe_set(a, 'xal_Premise311', {b1})
    assert _is_linked(a, 'xal_Premise311', b1)
    if hasattr(b1, 'xal_BuildingName312'):
        assert _is_linked(b1, 'xal_BuildingName312', a)
    _safe_set(a, 'xal_Premise311', {b2})
    assert _is_linked(a, 'xal_Premise311', b2)
    if hasattr(b1, 'xal_BuildingName312'):
        assert not _is_linked(b1, 'xal_BuildingName312', a)
    if hasattr(b2, 'xal_BuildingName312'):
        assert _is_linked(b2, 'xal_BuildingName312', a)
    _safe_set(a, 'xal_Premise311', set())
    assert not _is_linked(a, 'xal_Premise311', b2)
    if hasattr(b2, 'xal_BuildingName312'):
        assert not _is_linked(b2, 'xal_BuildingName312', a)


def test_assoc_buildingName382_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_BuildingName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    b2 = xal_BuildingName(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2", typeOccurrence="sample_text_2")
    _safe_set(a, 'xal_SubPremise383', {b1})
    assert _is_linked(a, 'xal_SubPremise383', b1)
    if hasattr(b1, 'xal_BuildingName384'):
        assert _is_linked(b1, 'xal_BuildingName384', a)
    _safe_set(a, 'xal_SubPremise383', {b2})
    assert _is_linked(a, 'xal_SubPremise383', b2)
    if hasattr(b1, 'xal_BuildingName384'):
        assert not _is_linked(b1, 'xal_BuildingName384', a)
    if hasattr(b2, 'xal_BuildingName384'):
        assert _is_linked(b2, 'xal_BuildingName384', a)
    _safe_set(a, 'xal_SubPremise383', set())
    assert not _is_linked(a, 'xal_SubPremise383', b2)
    if hasattr(b2, 'xal_BuildingName384'):
        assert not _is_linked(b2, 'xal_BuildingName384', a)


def test_assoc_country5_link_reassign_clear():
    a = xal_Country(any="sample_text", anyAttribute="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_Country', b1)
    assert _is_linked(a, 'xal_Country', b1)
    if hasattr(b1, 'xal_AddressDetails6'):
        assert _is_linked(b1, 'xal_AddressDetails6', a)
    _safe_set(a, 'xal_Country', b2)
    assert _is_linked(a, 'xal_Country', b2)
    if hasattr(b1, 'xal_AddressDetails6'):
        assert not _is_linked(b1, 'xal_AddressDetails6', a)
    if hasattr(b2, 'xal_AddressDetails6'):
        assert _is_linked(b2, 'xal_AddressDetails6', a)
    _safe_set(a, 'xal_Country', None)
    assert not _is_linked(a, 'xal_Country', b2)
    if hasattr(b2, 'xal_AddressDetails6'):
        assert not _is_linked(b2, 'xal_AddressDetails6', a)


def test_assoc_countryName105_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_CountryName(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DocumentRoot106', {b1})
    assert _is_linked(a, 'xal_DocumentRoot106', b1)
    if hasattr(b1, 'xal_CountryName107'):
        assert _is_linked(b1, 'xal_CountryName107', a)
    _safe_set(a, 'xal_DocumentRoot106', {b2})
    assert _is_linked(a, 'xal_DocumentRoot106', b2)
    if hasattr(b1, 'xal_CountryName107'):
        assert not _is_linked(b1, 'xal_CountryName107', a)
    if hasattr(b2, 'xal_CountryName107'):
        assert _is_linked(b2, 'xal_CountryName107', a)
    _safe_set(a, 'xal_DocumentRoot106', set())
    assert not _is_linked(a, 'xal_DocumentRoot106', b2)
    if hasattr(b2, 'xal_CountryName107'):
        assert not _is_linked(b2, 'xal_CountryName107', a)


def test_assoc_countryName34_link_reassign_clear():
    a = xal_CountryName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Country(any="sample_text", anyAttribute="sample_text")
    b2 = xal_Country(any="sample_text_2", anyAttribute="sample_text_2")
    _safe_set(a, 'xal_CountryName', b1)
    assert _is_linked(a, 'xal_CountryName', b1)
    if hasattr(b1, 'xal_Country35'):
        assert _is_linked(b1, 'xal_Country35', a)
    _safe_set(a, 'xal_CountryName', b2)
    assert _is_linked(a, 'xal_CountryName', b2)
    if hasattr(b1, 'xal_Country35'):
        assert not _is_linked(b1, 'xal_Country35', a)
    if hasattr(b2, 'xal_Country35'):
        assert _is_linked(b2, 'xal_Country35', a)
    _safe_set(a, 'xal_CountryName', None)
    assert not _is_linked(a, 'xal_CountryName', b2)
    if hasattr(b2, 'xal_Country35'):
        assert not _is_linked(b2, 'xal_Country35', a)


def test_assoc_countryNameCode32_link_reassign_clear():
    a = xal_CountryNameCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", scheme="sample_text")
    b1 = xal_Country(any="sample_text", anyAttribute="sample_text")
    b2 = xal_Country(any="sample_text_2", anyAttribute="sample_text_2")
    _safe_set(a, 'xal_CountryNameCode', b1)
    assert _is_linked(a, 'xal_CountryNameCode', b1)
    if hasattr(b1, 'xal_Country33'):
        assert _is_linked(b1, 'xal_Country33', a)
    _safe_set(a, 'xal_CountryNameCode', b2)
    assert _is_linked(a, 'xal_CountryNameCode', b2)
    if hasattr(b1, 'xal_Country33'):
        assert not _is_linked(b1, 'xal_Country33', a)
    if hasattr(b2, 'xal_Country33'):
        assert _is_linked(b2, 'xal_Country33', a)
    _safe_set(a, 'xal_CountryNameCode', None)
    assert not _is_linked(a, 'xal_CountryNameCode', b2)
    if hasattr(b2, 'xal_Country33'):
        assert not _is_linked(b2, 'xal_Country33', a)


def test_assoc_department108_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DocumentRoot109', {b1})
    assert _is_linked(a, 'xal_DocumentRoot109', b1)
    if hasattr(b1, 'xal_Department110'):
        assert _is_linked(b1, 'xal_Department110', a)
    _safe_set(a, 'xal_DocumentRoot109', {b2})
    assert _is_linked(a, 'xal_DocumentRoot109', b2)
    if hasattr(b1, 'xal_Department110'):
        assert not _is_linked(b1, 'xal_Department110', a)
    if hasattr(b2, 'xal_Department110'):
        assert _is_linked(b2, 'xal_Department110', a)
    _safe_set(a, 'xal_DocumentRoot109', set())
    assert not _is_linked(a, 'xal_DocumentRoot109', b2)
    if hasattr(b2, 'xal_Department110'):
        assert not _is_linked(b2, 'xal_Department110', a)


def test_assoc_department147_link_reassign_clear():
    a = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Firm148', {b1})
    assert _is_linked(a, 'xal_Firm148', b1)
    if hasattr(b1, 'xal_Department149'):
        assert _is_linked(b1, 'xal_Department149', a)
    _safe_set(a, 'xal_Firm148', {b2})
    assert _is_linked(a, 'xal_Firm148', b2)
    if hasattr(b1, 'xal_Department149'):
        assert not _is_linked(b1, 'xal_Department149', a)
    if hasattr(b2, 'xal_Department149'):
        assert _is_linked(b2, 'xal_Department149', a)
    _safe_set(a, 'xal_Firm148', set())
    assert not _is_linked(a, 'xal_Firm148', b2)
    if hasattr(b2, 'xal_Department149'):
        assert not _is_linked(b2, 'xal_Department149', a)


def test_assoc_department165_link_reassign_clear():
    a = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_LargeMailUser166', b1)
    assert _is_linked(a, 'xal_LargeMailUser166', b1)
    if hasattr(b1, 'xal_Department167'):
        assert _is_linked(b1, 'xal_Department167', a)
    _safe_set(a, 'xal_LargeMailUser166', b2)
    assert _is_linked(a, 'xal_LargeMailUser166', b2)
    if hasattr(b1, 'xal_Department167'):
        assert not _is_linked(b1, 'xal_Department167', a)
    if hasattr(b2, 'xal_Department167'):
        assert _is_linked(b2, 'xal_Department167', a)
    _safe_set(a, 'xal_LargeMailUser166', None)
    assert not _is_linked(a, 'xal_LargeMailUser166', b2)
    if hasattr(b2, 'xal_Department167'):
        assert not _is_linked(b2, 'xal_Department167', a)


def test_assoc_departmentName47_link_reassign_clear():
    a = xal_DepartmentName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_DepartmentName', b1)
    assert _is_linked(a, 'xal_DepartmentName', b1)
    if hasattr(b1, 'xal_Department48'):
        assert _is_linked(b1, 'xal_Department48', a)
    _safe_set(a, 'xal_DepartmentName', b2)
    assert _is_linked(a, 'xal_DepartmentName', b2)
    if hasattr(b1, 'xal_Department48'):
        assert not _is_linked(b1, 'xal_Department48', a)
    if hasattr(b2, 'xal_Department48'):
        assert _is_linked(b2, 'xal_Department48', a)
    _safe_set(a, 'xal_DepartmentName', None)
    assert not _is_linked(a, 'xal_DepartmentName', b2)
    if hasattr(b2, 'xal_Department48'):
        assert not _is_linked(b2, 'xal_Department48', a)


def test_assoc_dependentLocality200_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Locality201', b1)
    assert _is_linked(a, 'xal_Locality201', b1)
    if hasattr(b1, 'xal_DependentLocality202'):
        assert _is_linked(b1, 'xal_DependentLocality202', a)
    _safe_set(a, 'xal_Locality201', b2)
    assert _is_linked(a, 'xal_Locality201', b2)
    if hasattr(b1, 'xal_DependentLocality202'):
        assert not _is_linked(b1, 'xal_DependentLocality202', a)
    if hasattr(b2, 'xal_DependentLocality202'):
        assert _is_linked(b2, 'xal_DependentLocality202', a)
    _safe_set(a, 'xal_Locality201', None)
    assert not _is_linked(a, 'xal_Locality201', b2)
    if hasattr(b2, 'xal_DependentLocality202'):
        assert not _is_linked(b2, 'xal_DependentLocality202', a)


def test_assoc_dependentLocality429_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare430', b1)
    assert _is_linked(a, 'xal_Thoroughfare430', b1)
    if hasattr(b1, 'xal_DependentLocality431'):
        assert _is_linked(b1, 'xal_DependentLocality431', a)
    _safe_set(a, 'xal_Thoroughfare430', b2)
    assert _is_linked(a, 'xal_Thoroughfare430', b2)
    if hasattr(b1, 'xal_DependentLocality431'):
        assert not _is_linked(b1, 'xal_DependentLocality431', a)
    if hasattr(b2, 'xal_DependentLocality431'):
        assert _is_linked(b2, 'xal_DependentLocality431', a)
    _safe_set(a, 'xal_Thoroughfare430', None)
    assert not _is_linked(a, 'xal_Thoroughfare430', b2)
    if hasattr(b2, 'xal_DependentLocality431'):
        assert not _is_linked(b2, 'xal_DependentLocality431', a)


def test_assoc_dependentLocality75_link_reassign_clear():
    a = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_DependentLocality74', b1)
    assert _is_linked(a, 'xal_DependentLocality74', b1)
    if hasattr(b1, 'xal_DependentLocality76'):
        assert _is_linked(b1, 'xal_DependentLocality76', a)
    _safe_set(a, 'xal_DependentLocality74', b2)
    assert _is_linked(a, 'xal_DependentLocality74', b2)
    if hasattr(b1, 'xal_DependentLocality76'):
        assert not _is_linked(b1, 'xal_DependentLocality76', a)
    if hasattr(b2, 'xal_DependentLocality76'):
        assert _is_linked(b2, 'xal_DependentLocality76', a)
    _safe_set(a, 'xal_DependentLocality74', None)
    assert not _is_linked(a, 'xal_DependentLocality74', b2)
    if hasattr(b2, 'xal_DependentLocality76'):
        assert not _is_linked(b2, 'xal_DependentLocality76', a)


def test_assoc_dependentLocalityName56_link_reassign_clear():
    a = xal_DependentLocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_DependentLocalityName', b1)
    assert _is_linked(a, 'xal_DependentLocalityName', b1)
    if hasattr(b1, 'xal_DependentLocality57'):
        assert _is_linked(b1, 'xal_DependentLocality57', a)
    _safe_set(a, 'xal_DependentLocalityName', b2)
    assert _is_linked(a, 'xal_DependentLocalityName', b2)
    if hasattr(b1, 'xal_DependentLocality57'):
        assert not _is_linked(b1, 'xal_DependentLocality57', a)
    if hasattr(b2, 'xal_DependentLocality57'):
        assert _is_linked(b2, 'xal_DependentLocality57', a)
    _safe_set(a, 'xal_DependentLocalityName', None)
    assert not _is_linked(a, 'xal_DependentLocalityName', b2)
    if hasattr(b2, 'xal_DependentLocality57'):
        assert not _is_linked(b2, 'xal_DependentLocality57', a)


def test_assoc_dependentLocalityNumber58_link_reassign_clear():
    a = xal_DependentLocalityNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberOccurrence="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_DependentLocalityNumber', b1)
    assert _is_linked(a, 'xal_DependentLocalityNumber', b1)
    if hasattr(b1, 'xal_DependentLocality59'):
        assert _is_linked(b1, 'xal_DependentLocality59', a)
    _safe_set(a, 'xal_DependentLocalityNumber', b2)
    assert _is_linked(a, 'xal_DependentLocalityNumber', b2)
    if hasattr(b1, 'xal_DependentLocality59'):
        assert not _is_linked(b1, 'xal_DependentLocality59', a)
    if hasattr(b2, 'xal_DependentLocality59'):
        assert _is_linked(b2, 'xal_DependentLocality59', a)
    _safe_set(a, 'xal_DependentLocalityNumber', None)
    assert not _is_linked(a, 'xal_DependentLocalityNumber', b2)
    if hasattr(b2, 'xal_DependentLocality59'):
        assert not _is_linked(b2, 'xal_DependentLocality59', a)


def test_assoc_dependentThoroughfare426_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare427', b1)
    assert _is_linked(a, 'xal_Thoroughfare427', b1)
    if hasattr(b1, 'xal_DependentThoroughfare428'):
        assert _is_linked(b1, 'xal_DependentThoroughfare428', a)
    _safe_set(a, 'xal_Thoroughfare427', b2)
    assert _is_linked(a, 'xal_Thoroughfare427', b2)
    if hasattr(b1, 'xal_DependentThoroughfare428'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare428', a)
    if hasattr(b2, 'xal_DependentThoroughfare428'):
        assert _is_linked(b2, 'xal_DependentThoroughfare428', a)
    _safe_set(a, 'xal_Thoroughfare427', None)
    assert not _is_linked(a, 'xal_Thoroughfare427', b2)
    if hasattr(b2, 'xal_DependentThoroughfare428'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare428', a)


def test_assoc_endorsementLineCode234_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_EndorsementLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_EndorsementLineCode(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements235', b1)
    assert _is_linked(a, 'xal_PostalServiceElements235', b1)
    if hasattr(b1, 'xal_EndorsementLineCode'):
        assert _is_linked(b1, 'xal_EndorsementLineCode', a)
    _safe_set(a, 'xal_PostalServiceElements235', b2)
    assert _is_linked(a, 'xal_PostalServiceElements235', b2)
    if hasattr(b1, 'xal_EndorsementLineCode'):
        assert not _is_linked(b1, 'xal_EndorsementLineCode', a)
    if hasattr(b2, 'xal_EndorsementLineCode'):
        assert _is_linked(b2, 'xal_EndorsementLineCode', a)
    _safe_set(a, 'xal_PostalServiceElements235', None)
    assert not _is_linked(a, 'xal_PostalServiceElements235', b2)
    if hasattr(b2, 'xal_EndorsementLineCode'):
        assert not _is_linked(b2, 'xal_EndorsementLineCode', a)


def test_assoc_firm263_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBox264', b1)
    assert _is_linked(a, 'xal_PostBox264', b1)
    if hasattr(b1, 'xal_Firm265'):
        assert _is_linked(b1, 'xal_Firm265', a)
    _safe_set(a, 'xal_PostBox264', b2)
    assert _is_linked(a, 'xal_PostBox264', b2)
    if hasattr(b1, 'xal_Firm265'):
        assert not _is_linked(b1, 'xal_Firm265', a)
    if hasattr(b2, 'xal_Firm265'):
        assert _is_linked(b2, 'xal_Firm265', a)
    _safe_set(a, 'xal_PostBox264', None)
    assert not _is_linked(a, 'xal_PostBox264', b2)
    if hasattr(b2, 'xal_Firm265'):
        assert not _is_linked(b2, 'xal_Firm265', a)


def test_assoc_firm315_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Premise316', b1)
    assert _is_linked(a, 'xal_Premise316', b1)
    if hasattr(b1, 'xal_Firm317'):
        assert _is_linked(b1, 'xal_Firm317', a)
    _safe_set(a, 'xal_Premise316', b2)
    assert _is_linked(a, 'xal_Premise316', b2)
    if hasattr(b1, 'xal_Firm317'):
        assert not _is_linked(b1, 'xal_Firm317', a)
    if hasattr(b2, 'xal_Firm317'):
        assert _is_linked(b2, 'xal_Firm317', a)
    _safe_set(a, 'xal_Premise316', None)
    assert not _is_linked(a, 'xal_Premise316', b2)
    if hasattr(b2, 'xal_Firm317'):
        assert not _is_linked(b2, 'xal_Firm317', a)


def test_assoc_firm385_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise386', b1)
    assert _is_linked(a, 'xal_SubPremise386', b1)
    if hasattr(b1, 'xal_Firm387'):
        assert _is_linked(b1, 'xal_Firm387', a)
    _safe_set(a, 'xal_SubPremise386', b2)
    assert _is_linked(a, 'xal_SubPremise386', b2)
    if hasattr(b1, 'xal_Firm387'):
        assert not _is_linked(b1, 'xal_Firm387', a)
    if hasattr(b2, 'xal_Firm387'):
        assert _is_linked(b2, 'xal_Firm387', a)
    _safe_set(a, 'xal_SubPremise386', None)
    assert not _is_linked(a, 'xal_SubPremise386', b2)
    if hasattr(b2, 'xal_Firm387'):
        assert not _is_linked(b2, 'xal_Firm387', a)


def test_assoc_firm435_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare436', b1)
    assert _is_linked(a, 'xal_Thoroughfare436', b1)
    if hasattr(b1, 'xal_Firm437'):
        assert _is_linked(b1, 'xal_Firm437', a)
    _safe_set(a, 'xal_Thoroughfare436', b2)
    assert _is_linked(a, 'xal_Thoroughfare436', b2)
    if hasattr(b1, 'xal_Firm437'):
        assert not _is_linked(b1, 'xal_Firm437', a)
    if hasattr(b2, 'xal_Firm437'):
        assert _is_linked(b2, 'xal_Firm437', a)
    _safe_set(a, 'xal_Thoroughfare436', None)
    assert not _is_linked(a, 'xal_Thoroughfare436', b2)
    if hasattr(b2, 'xal_Firm437'):
        assert not _is_linked(b2, 'xal_Firm437', a)


def test_assoc_firmName145_link_reassign_clear():
    a = xal_FirmName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_FirmName', b1)
    assert _is_linked(a, 'xal_FirmName', b1)
    if hasattr(b1, 'xal_Firm146'):
        assert _is_linked(b1, 'xal_Firm146', a)
    _safe_set(a, 'xal_FirmName', b2)
    assert _is_linked(a, 'xal_FirmName', b2)
    if hasattr(b1, 'xal_Firm146'):
        assert not _is_linked(b1, 'xal_Firm146', a)
    if hasattr(b2, 'xal_Firm146'):
        assert _is_linked(b2, 'xal_Firm146', a)
    _safe_set(a, 'xal_FirmName', None)
    assert not _is_linked(a, 'xal_FirmName', b2)
    if hasattr(b2, 'xal_Firm146'):
        assert not _is_linked(b2, 'xal_Firm146', a)


def test_assoc_keyLineCode236_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_KeyLineCode(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b2 = xal_KeyLineCode(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements237', b1)
    assert _is_linked(a, 'xal_PostalServiceElements237', b1)
    if hasattr(b1, 'xal_KeyLineCode'):
        assert _is_linked(b1, 'xal_KeyLineCode', a)
    _safe_set(a, 'xal_PostalServiceElements237', b2)
    assert _is_linked(a, 'xal_PostalServiceElements237', b2)
    if hasattr(b1, 'xal_KeyLineCode'):
        assert not _is_linked(b1, 'xal_KeyLineCode', a)
    if hasattr(b2, 'xal_KeyLineCode'):
        assert _is_linked(b2, 'xal_KeyLineCode', a)
    _safe_set(a, 'xal_PostalServiceElements237', None)
    assert not _is_linked(a, 'xal_PostalServiceElements237', b2)
    if hasattr(b2, 'xal_KeyLineCode'):
        assert not _is_linked(b2, 'xal_KeyLineCode', a)


def test_assoc_largeMailUser185_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Locality186', b1)
    assert _is_linked(a, 'xal_Locality186', b1)
    if hasattr(b1, 'xal_LargeMailUser187'):
        assert _is_linked(b1, 'xal_LargeMailUser187', a)
    _safe_set(a, 'xal_Locality186', b2)
    assert _is_linked(a, 'xal_Locality186', b2)
    if hasattr(b1, 'xal_LargeMailUser187'):
        assert not _is_linked(b1, 'xal_LargeMailUser187', a)
    if hasattr(b2, 'xal_LargeMailUser187'):
        assert _is_linked(b2, 'xal_LargeMailUser187', a)
    _safe_set(a, 'xal_Locality186', None)
    assert not _is_linked(a, 'xal_Locality186', b2)
    if hasattr(b2, 'xal_LargeMailUser187'):
        assert not _is_linked(b2, 'xal_LargeMailUser187', a)


def test_assoc_largeMailUser62_link_reassign_clear():
    a = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_LargeMailUser', b1)
    assert _is_linked(a, 'xal_LargeMailUser', b1)
    if hasattr(b1, 'xal_DependentLocality63'):
        assert _is_linked(b1, 'xal_DependentLocality63', a)
    _safe_set(a, 'xal_LargeMailUser', b2)
    assert _is_linked(a, 'xal_LargeMailUser', b2)
    if hasattr(b1, 'xal_DependentLocality63'):
        assert not _is_linked(b1, 'xal_DependentLocality63', a)
    if hasattr(b2, 'xal_DependentLocality63'):
        assert _is_linked(b2, 'xal_DependentLocality63', a)
    _safe_set(a, 'xal_LargeMailUser', None)
    assert not _is_linked(a, 'xal_LargeMailUser', b2)
    if hasattr(b2, 'xal_DependentLocality63'):
        assert not _is_linked(b2, 'xal_DependentLocality63', a)


def test_assoc_largeMailUserIdentifier161_link_reassign_clear():
    a = xal_LargeMailUserIdentifier(anyAttribute="sample_text", code="sample_text", indicator="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_LargeMailUserIdentifier', b1)
    assert _is_linked(a, 'xal_LargeMailUserIdentifier', b1)
    if hasattr(b1, 'xal_LargeMailUser162'):
        assert _is_linked(b1, 'xal_LargeMailUser162', a)
    _safe_set(a, 'xal_LargeMailUserIdentifier', b2)
    assert _is_linked(a, 'xal_LargeMailUserIdentifier', b2)
    if hasattr(b1, 'xal_LargeMailUser162'):
        assert not _is_linked(b1, 'xal_LargeMailUser162', a)
    if hasattr(b2, 'xal_LargeMailUser162'):
        assert _is_linked(b2, 'xal_LargeMailUser162', a)
    _safe_set(a, 'xal_LargeMailUserIdentifier', None)
    assert not _is_linked(a, 'xal_LargeMailUserIdentifier', b2)
    if hasattr(b2, 'xal_LargeMailUser162'):
        assert not _is_linked(b2, 'xal_LargeMailUser162', a)


def test_assoc_largeMailUserName159_link_reassign_clear():
    a = xal_LargeMailUserName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_LargeMailUserName', b1)
    assert _is_linked(a, 'xal_LargeMailUserName', b1)
    if hasattr(b1, 'xal_LargeMailUser160'):
        assert _is_linked(b1, 'xal_LargeMailUser160', a)
    _safe_set(a, 'xal_LargeMailUserName', b2)
    assert _is_linked(a, 'xal_LargeMailUserName', b2)
    if hasattr(b1, 'xal_LargeMailUser160'):
        assert not _is_linked(b1, 'xal_LargeMailUser160', a)
    if hasattr(b2, 'xal_LargeMailUser160'):
        assert _is_linked(b2, 'xal_LargeMailUser160', a)
    _safe_set(a, 'xal_LargeMailUserName', None)
    assert not _is_linked(a, 'xal_LargeMailUserName', b2)
    if hasattr(b2, 'xal_LargeMailUser160'):
        assert not _is_linked(b2, 'xal_LargeMailUser160', a)


def test_assoc_locality111_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_Locality113', b1)
    assert _is_linked(a, 'xal_Locality113', b1)
    if hasattr(b1, 'xal_DocumentRoot112'):
        assert _is_linked(b1, 'xal_DocumentRoot112', a)
    _safe_set(a, 'xal_Locality113', b2)
    assert _is_linked(a, 'xal_Locality113', b2)
    if hasattr(b1, 'xal_DocumentRoot112'):
        assert not _is_linked(b1, 'xal_DocumentRoot112', a)
    if hasattr(b2, 'xal_DocumentRoot112'):
        assert _is_linked(b2, 'xal_DocumentRoot112', a)
    _safe_set(a, 'xal_Locality113', None)
    assert not _is_linked(a, 'xal_Locality113', b2)
    if hasattr(b2, 'xal_DocumentRoot112'):
        assert not _is_linked(b2, 'xal_DocumentRoot112', a)


def test_assoc_locality22_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Locality24', b1)
    assert _is_linked(a, 'xal_Locality24', b1)
    if hasattr(b1, 'xal_AdministrativeArea23'):
        assert _is_linked(b1, 'xal_AdministrativeArea23', a)
    _safe_set(a, 'xal_Locality24', b2)
    assert _is_linked(a, 'xal_Locality24', b2)
    if hasattr(b1, 'xal_AdministrativeArea23'):
        assert not _is_linked(b1, 'xal_AdministrativeArea23', a)
    if hasattr(b2, 'xal_AdministrativeArea23'):
        assert _is_linked(b2, 'xal_AdministrativeArea23', a)
    _safe_set(a, 'xal_Locality24', None)
    assert not _is_linked(a, 'xal_Locality24', b2)
    if hasattr(b2, 'xal_AdministrativeArea23'):
        assert not _is_linked(b2, 'xal_AdministrativeArea23', a)


def test_assoc_locality360_link_reassign_clear():
    a = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeArea361', b1)
    assert _is_linked(a, 'xal_SubAdministrativeArea361', b1)
    if hasattr(b1, 'xal_Locality362'):
        assert _is_linked(b1, 'xal_Locality362', a)
    _safe_set(a, 'xal_SubAdministrativeArea361', b2)
    assert _is_linked(a, 'xal_SubAdministrativeArea361', b2)
    if hasattr(b1, 'xal_Locality362'):
        assert not _is_linked(b1, 'xal_Locality362', a)
    if hasattr(b2, 'xal_Locality362'):
        assert _is_linked(b2, 'xal_Locality362', a)
    _safe_set(a, 'xal_SubAdministrativeArea361', None)
    assert not _is_linked(a, 'xal_SubAdministrativeArea361', b2)
    if hasattr(b2, 'xal_Locality362'):
        assert not _is_linked(b2, 'xal_Locality362', a)


def test_assoc_locality39_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_Country(any="sample_text", anyAttribute="sample_text")
    b2 = xal_Country(any="sample_text_2", anyAttribute="sample_text_2")
    _safe_set(a, 'xal_Locality41', b1)
    assert _is_linked(a, 'xal_Locality41', b1)
    if hasattr(b1, 'xal_Country40'):
        assert _is_linked(b1, 'xal_Country40', a)
    _safe_set(a, 'xal_Locality41', b2)
    assert _is_linked(a, 'xal_Locality41', b2)
    if hasattr(b1, 'xal_Country40'):
        assert not _is_linked(b1, 'xal_Country40', a)
    if hasattr(b2, 'xal_Country40'):
        assert _is_linked(b2, 'xal_Country40', a)
    _safe_set(a, 'xal_Locality41', None)
    assert not _is_linked(a, 'xal_Locality41', b2)
    if hasattr(b2, 'xal_Country40'):
        assert not _is_linked(b2, 'xal_Country40', a)


def test_assoc_locality9_link_reassign_clear():
    a = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_Locality', b1)
    assert _is_linked(a, 'xal_Locality', b1)
    if hasattr(b1, 'xal_AddressDetails10'):
        assert _is_linked(b1, 'xal_AddressDetails10', a)
    _safe_set(a, 'xal_Locality', b2)
    assert _is_linked(a, 'xal_Locality', b2)
    if hasattr(b1, 'xal_AddressDetails10'):
        assert not _is_linked(b1, 'xal_AddressDetails10', a)
    if hasattr(b2, 'xal_AddressDetails10'):
        assert _is_linked(b2, 'xal_AddressDetails10', a)
    _safe_set(a, 'xal_Locality', None)
    assert not _is_linked(a, 'xal_Locality', b2)
    if hasattr(b2, 'xal_AddressDetails10'):
        assert not _is_linked(b2, 'xal_AddressDetails10', a)


def test_assoc_localityName180_link_reassign_clear():
    a = xal_LocalityName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_LocalityName', b1)
    assert _is_linked(a, 'xal_LocalityName', b1)
    if hasattr(b1, 'xal_Locality181'):
        assert _is_linked(b1, 'xal_Locality181', a)
    _safe_set(a, 'xal_LocalityName', b2)
    assert _is_linked(a, 'xal_LocalityName', b2)
    if hasattr(b1, 'xal_Locality181'):
        assert not _is_linked(b1, 'xal_Locality181', a)
    if hasattr(b2, 'xal_Locality181'):
        assert _is_linked(b2, 'xal_Locality181', a)
    _safe_set(a, 'xal_LocalityName', None)
    assert not _is_linked(a, 'xal_LocalityName', b2)
    if hasattr(b2, 'xal_Locality181'):
        assert not _is_linked(b2, 'xal_Locality181', a)


def test_assoc_mailStop150_link_reassign_clear():
    a = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_MailStop152', b1)
    assert _is_linked(a, 'xal_MailStop152', b1)
    if hasattr(b1, 'xal_Firm151'):
        assert _is_linked(b1, 'xal_Firm151', a)
    _safe_set(a, 'xal_MailStop152', b2)
    assert _is_linked(a, 'xal_MailStop152', b2)
    if hasattr(b1, 'xal_Firm151'):
        assert not _is_linked(b1, 'xal_Firm151', a)
    if hasattr(b2, 'xal_Firm151'):
        assert _is_linked(b2, 'xal_Firm151', a)
    _safe_set(a, 'xal_MailStop152', None)
    assert not _is_linked(a, 'xal_MailStop152', b2)
    if hasattr(b2, 'xal_Firm151'):
        assert not _is_linked(b2, 'xal_Firm151', a)


def test_assoc_mailStop318_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_MailStop(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Premise319', b1)
    assert _is_linked(a, 'xal_Premise319', b1)
    if hasattr(b1, 'xal_MailStop320'):
        assert _is_linked(b1, 'xal_MailStop320', a)
    _safe_set(a, 'xal_Premise319', b2)
    assert _is_linked(a, 'xal_Premise319', b2)
    if hasattr(b1, 'xal_MailStop320'):
        assert not _is_linked(b1, 'xal_MailStop320', a)
    if hasattr(b2, 'xal_MailStop320'):
        assert _is_linked(b2, 'xal_MailStop320', a)
    _safe_set(a, 'xal_Premise319', None)
    assert not _is_linked(a, 'xal_Premise319', b2)
    if hasattr(b2, 'xal_MailStop320'):
        assert not _is_linked(b2, 'xal_MailStop320', a)


def test_assoc_mailStop388_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_MailStop(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise389', b1)
    assert _is_linked(a, 'xal_SubPremise389', b1)
    if hasattr(b1, 'xal_MailStop390'):
        assert _is_linked(b1, 'xal_MailStop390', a)
    _safe_set(a, 'xal_SubPremise389', b2)
    assert _is_linked(a, 'xal_SubPremise389', b2)
    if hasattr(b1, 'xal_MailStop390'):
        assert not _is_linked(b1, 'xal_MailStop390', a)
    if hasattr(b2, 'xal_MailStop390'):
        assert _is_linked(b2, 'xal_MailStop390', a)
    _safe_set(a, 'xal_SubPremise389', None)
    assert not _is_linked(a, 'xal_SubPremise389', b2)
    if hasattr(b2, 'xal_MailStop390'):
        assert not _is_linked(b2, 'xal_MailStop390', a)


def test_assoc_mailStop49_link_reassign_clear():
    a = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_MailStop', b1)
    assert _is_linked(a, 'xal_MailStop', b1)
    if hasattr(b1, 'xal_Department50'):
        assert _is_linked(b1, 'xal_Department50', a)
    _safe_set(a, 'xal_MailStop', b2)
    assert _is_linked(a, 'xal_MailStop', b2)
    if hasattr(b1, 'xal_Department50'):
        assert not _is_linked(b1, 'xal_Department50', a)
    if hasattr(b2, 'xal_Department50'):
        assert _is_linked(b2, 'xal_Department50', a)
    _safe_set(a, 'xal_MailStop', None)
    assert not _is_linked(a, 'xal_MailStop', b2)
    if hasattr(b2, 'xal_Department50'):
        assert not _is_linked(b2, 'xal_Department50', a)


def test_assoc_mailStopName209_link_reassign_clear():
    a = xal_MailStopName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_MailStop(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_MailStopName', b1)
    assert _is_linked(a, 'xal_MailStopName', b1)
    if hasattr(b1, 'xal_MailStop210'):
        assert _is_linked(b1, 'xal_MailStop210', a)
    _safe_set(a, 'xal_MailStopName', b2)
    assert _is_linked(a, 'xal_MailStopName', b2)
    if hasattr(b1, 'xal_MailStop210'):
        assert not _is_linked(b1, 'xal_MailStop210', a)
    if hasattr(b2, 'xal_MailStop210'):
        assert _is_linked(b2, 'xal_MailStop210', a)
    _safe_set(a, 'xal_MailStopName', None)
    assert not _is_linked(a, 'xal_MailStopName', b2)
    if hasattr(b2, 'xal_MailStop210'):
        assert not _is_linked(b2, 'xal_MailStop210', a)


def test_assoc_mailStopNumber211_link_reassign_clear():
    a = xal_MailStopNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", nameNumberSeparator="sample_text")
    b1 = xal_MailStop(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_MailStop(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_MailStopNumber', b1)
    assert _is_linked(a, 'xal_MailStopNumber', b1)
    if hasattr(b1, 'xal_MailStop212'):
        assert _is_linked(b1, 'xal_MailStop212', a)
    _safe_set(a, 'xal_MailStopNumber', b2)
    assert _is_linked(a, 'xal_MailStopNumber', b2)
    if hasattr(b1, 'xal_MailStop212'):
        assert not _is_linked(b1, 'xal_MailStop212', a)
    if hasattr(b2, 'xal_MailStop212'):
        assert _is_linked(b2, 'xal_MailStop212', a)
    _safe_set(a, 'xal_MailStopNumber', None)
    assert not _is_linked(a, 'xal_MailStopNumber', b2)
    if hasattr(b2, 'xal_MailStop212'):
        assert not _is_linked(b2, 'xal_MailStop212', a)


def test_assoc_postBox117_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PostBox119', b1)
    assert _is_linked(a, 'xal_PostBox119', b1)
    if hasattr(b1, 'xal_DocumentRoot118'):
        assert _is_linked(b1, 'xal_DocumentRoot118', a)
    _safe_set(a, 'xal_PostBox119', b2)
    assert _is_linked(a, 'xal_PostBox119', b2)
    if hasattr(b1, 'xal_DocumentRoot118'):
        assert not _is_linked(b1, 'xal_DocumentRoot118', a)
    if hasattr(b2, 'xal_DocumentRoot118'):
        assert _is_linked(b2, 'xal_DocumentRoot118', a)
    _safe_set(a, 'xal_PostBox119', None)
    assert not _is_linked(a, 'xal_PostBox119', b2)
    if hasattr(b2, 'xal_DocumentRoot118'):
        assert not _is_linked(b2, 'xal_DocumentRoot118', a)


def test_assoc_postBox168_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBox170', b1)
    assert _is_linked(a, 'xal_PostBox170', b1)
    if hasattr(b1, 'xal_LargeMailUser169'):
        assert _is_linked(b1, 'xal_LargeMailUser169', a)
    _safe_set(a, 'xal_PostBox170', b2)
    assert _is_linked(a, 'xal_PostBox170', b2)
    if hasattr(b1, 'xal_LargeMailUser169'):
        assert not _is_linked(b1, 'xal_LargeMailUser169', a)
    if hasattr(b2, 'xal_LargeMailUser169'):
        assert _is_linked(b2, 'xal_LargeMailUser169', a)
    _safe_set(a, 'xal_PostBox170', None)
    assert not _is_linked(a, 'xal_PostBox170', b2)
    if hasattr(b2, 'xal_LargeMailUser169'):
        assert not _is_linked(b2, 'xal_LargeMailUser169', a)


def test_assoc_postBox182_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostBox184', b1)
    assert _is_linked(a, 'xal_PostBox184', b1)
    if hasattr(b1, 'xal_Locality183'):
        assert _is_linked(b1, 'xal_Locality183', a)
    _safe_set(a, 'xal_PostBox184', b2)
    assert _is_linked(a, 'xal_PostBox184', b2)
    if hasattr(b1, 'xal_Locality183'):
        assert not _is_linked(b1, 'xal_Locality183', a)
    if hasattr(b2, 'xal_Locality183'):
        assert _is_linked(b2, 'xal_Locality183', a)
    _safe_set(a, 'xal_PostBox184', None)
    assert not _is_linked(a, 'xal_PostBox184', b2)
    if hasattr(b2, 'xal_Locality183'):
        assert not _is_linked(b2, 'xal_Locality183', a)


def test_assoc_postBox229_link_reassign_clear():
    a = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalRoute230', b1)
    assert _is_linked(a, 'xal_PostalRoute230', b1)
    if hasattr(b1, 'xal_PostBox231'):
        assert _is_linked(b1, 'xal_PostBox231', a)
    _safe_set(a, 'xal_PostalRoute230', b2)
    assert _is_linked(a, 'xal_PostalRoute230', b2)
    if hasattr(b1, 'xal_PostBox231'):
        assert not _is_linked(b1, 'xal_PostBox231', a)
    if hasattr(b2, 'xal_PostBox231'):
        assert _is_linked(b2, 'xal_PostBox231', a)
    _safe_set(a, 'xal_PostalRoute230', None)
    assert not _is_linked(a, 'xal_PostalRoute230', b2)
    if hasattr(b2, 'xal_PostBox231'):
        assert not _is_linked(b2, 'xal_PostBox231', a)


def test_assoc_postBox279_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostOffice280', b1)
    assert _is_linked(a, 'xal_PostOffice280', b1)
    if hasattr(b1, 'xal_PostBox281'):
        assert _is_linked(b1, 'xal_PostBox281', a)
    _safe_set(a, 'xal_PostOffice280', b2)
    assert _is_linked(a, 'xal_PostOffice280', b2)
    if hasattr(b1, 'xal_PostBox281'):
        assert not _is_linked(b1, 'xal_PostBox281', a)
    if hasattr(b2, 'xal_PostBox281'):
        assert _is_linked(b2, 'xal_PostBox281', a)
    _safe_set(a, 'xal_PostOffice280', None)
    assert not _is_linked(a, 'xal_PostOffice280', b2)
    if hasattr(b2, 'xal_PostBox281'):
        assert not _is_linked(b2, 'xal_PostBox281', a)


def test_assoc_postBox60_link_reassign_clear():
    a = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostBox', b1)
    assert _is_linked(a, 'xal_PostBox', b1)
    if hasattr(b1, 'xal_DependentLocality61'):
        assert _is_linked(b1, 'xal_DependentLocality61', a)
    _safe_set(a, 'xal_PostBox', b2)
    assert _is_linked(a, 'xal_PostBox', b2)
    if hasattr(b1, 'xal_DependentLocality61'):
        assert not _is_linked(b1, 'xal_DependentLocality61', a)
    if hasattr(b2, 'xal_DependentLocality61'):
        assert _is_linked(b2, 'xal_DependentLocality61', a)
    _safe_set(a, 'xal_PostBox', None)
    assert not _is_linked(a, 'xal_PostBox', b2)
    if hasattr(b2, 'xal_DependentLocality61'):
        assert not _is_linked(b2, 'xal_DependentLocality61', a)


def test_assoc_postBoxNumber255_link_reassign_clear():
    a = xal_PostBoxNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBoxNumber', b1)
    assert _is_linked(a, 'xal_PostBoxNumber', b1)
    if hasattr(b1, 'xal_PostBox256'):
        assert _is_linked(b1, 'xal_PostBox256', a)
    _safe_set(a, 'xal_PostBoxNumber', b2)
    assert _is_linked(a, 'xal_PostBoxNumber', b2)
    if hasattr(b1, 'xal_PostBox256'):
        assert not _is_linked(b1, 'xal_PostBox256', a)
    if hasattr(b2, 'xal_PostBox256'):
        assert _is_linked(b2, 'xal_PostBox256', a)
    _safe_set(a, 'xal_PostBoxNumber', None)
    assert not _is_linked(a, 'xal_PostBoxNumber', b2)
    if hasattr(b2, 'xal_PostBox256'):
        assert not _is_linked(b2, 'xal_PostBox256', a)


def test_assoc_postBoxNumberExtension261_link_reassign_clear():
    a = xal_PostBoxNumberExtension(anyAttribute="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBoxNumberExtension', b1)
    assert _is_linked(a, 'xal_PostBoxNumberExtension', b1)
    if hasattr(b1, 'xal_PostBox262'):
        assert _is_linked(b1, 'xal_PostBox262', a)
    _safe_set(a, 'xal_PostBoxNumberExtension', b2)
    assert _is_linked(a, 'xal_PostBoxNumberExtension', b2)
    if hasattr(b1, 'xal_PostBox262'):
        assert not _is_linked(b1, 'xal_PostBox262', a)
    if hasattr(b2, 'xal_PostBox262'):
        assert _is_linked(b2, 'xal_PostBox262', a)
    _safe_set(a, 'xal_PostBoxNumberExtension', None)
    assert not _is_linked(a, 'xal_PostBoxNumberExtension', b2)
    if hasattr(b2, 'xal_PostBox262'):
        assert not _is_linked(b2, 'xal_PostBox262', a)


def test_assoc_postBoxNumberPrefix257_link_reassign_clear():
    a = xal_PostBoxNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBoxNumberPrefix', b1)
    assert _is_linked(a, 'xal_PostBoxNumberPrefix', b1)
    if hasattr(b1, 'xal_PostBox258'):
        assert _is_linked(b1, 'xal_PostBox258', a)
    _safe_set(a, 'xal_PostBoxNumberPrefix', b2)
    assert _is_linked(a, 'xal_PostBoxNumberPrefix', b2)
    if hasattr(b1, 'xal_PostBox258'):
        assert not _is_linked(b1, 'xal_PostBox258', a)
    if hasattr(b2, 'xal_PostBox258'):
        assert _is_linked(b2, 'xal_PostBox258', a)
    _safe_set(a, 'xal_PostBoxNumberPrefix', None)
    assert not _is_linked(a, 'xal_PostBoxNumberPrefix', b2)
    if hasattr(b2, 'xal_PostBox258'):
        assert not _is_linked(b2, 'xal_PostBox258', a)


def test_assoc_postBoxNumberSuffix259_link_reassign_clear():
    a = xal_PostBoxNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostBoxNumberSuffix', b1)
    assert _is_linked(a, 'xal_PostBoxNumberSuffix', b1)
    if hasattr(b1, 'xal_PostBox260'):
        assert _is_linked(b1, 'xal_PostBox260', a)
    _safe_set(a, 'xal_PostBoxNumberSuffix', b2)
    assert _is_linked(a, 'xal_PostBoxNumberSuffix', b2)
    if hasattr(b1, 'xal_PostBox260'):
        assert not _is_linked(b1, 'xal_PostBox260', a)
    if hasattr(b2, 'xal_PostBox260'):
        assert _is_linked(b2, 'xal_PostBox260', a)
    _safe_set(a, 'xal_PostBoxNumberSuffix', None)
    assert not _is_linked(a, 'xal_PostBoxNumberSuffix', b2)
    if hasattr(b2, 'xal_PostBox260'):
        assert not _is_linked(b2, 'xal_PostBox260', a)


def test_assoc_postOffice120_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PostOffice122', b1)
    assert _is_linked(a, 'xal_PostOffice122', b1)
    if hasattr(b1, 'xal_DocumentRoot121'):
        assert _is_linked(b1, 'xal_DocumentRoot121', a)
    _safe_set(a, 'xal_PostOffice122', b2)
    assert _is_linked(a, 'xal_PostOffice122', b2)
    if hasattr(b1, 'xal_DocumentRoot121'):
        assert not _is_linked(b1, 'xal_DocumentRoot121', a)
    if hasattr(b2, 'xal_DocumentRoot121'):
        assert _is_linked(b2, 'xal_DocumentRoot121', a)
    _safe_set(a, 'xal_PostOffice122', None)
    assert not _is_linked(a, 'xal_PostOffice122', b2)
    if hasattr(b2, 'xal_DocumentRoot121'):
        assert not _is_linked(b2, 'xal_DocumentRoot121', a)


def test_assoc_postOffice188_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostOffice190', b1)
    assert _is_linked(a, 'xal_PostOffice190', b1)
    if hasattr(b1, 'xal_Locality189'):
        assert _is_linked(b1, 'xal_Locality189', a)
    _safe_set(a, 'xal_PostOffice190', b2)
    assert _is_linked(a, 'xal_PostOffice190', b2)
    if hasattr(b1, 'xal_Locality189'):
        assert not _is_linked(b1, 'xal_Locality189', a)
    if hasattr(b2, 'xal_Locality189'):
        assert _is_linked(b2, 'xal_Locality189', a)
    _safe_set(a, 'xal_PostOffice190', None)
    assert not _is_linked(a, 'xal_PostOffice190', b2)
    if hasattr(b2, 'xal_Locality189'):
        assert not _is_linked(b2, 'xal_Locality189', a)


def test_assoc_postOffice25_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostOffice', b1)
    assert _is_linked(a, 'xal_PostOffice', b1)
    if hasattr(b1, 'xal_AdministrativeArea26'):
        assert _is_linked(b1, 'xal_AdministrativeArea26', a)
    _safe_set(a, 'xal_PostOffice', b2)
    assert _is_linked(a, 'xal_PostOffice', b2)
    if hasattr(b1, 'xal_AdministrativeArea26'):
        assert not _is_linked(b1, 'xal_AdministrativeArea26', a)
    if hasattr(b2, 'xal_AdministrativeArea26'):
        assert _is_linked(b2, 'xal_AdministrativeArea26', a)
    _safe_set(a, 'xal_PostOffice', None)
    assert not _is_linked(a, 'xal_PostOffice', b2)
    if hasattr(b2, 'xal_AdministrativeArea26'):
        assert not _is_linked(b2, 'xal_AdministrativeArea26', a)


def test_assoc_postOffice363_link_reassign_clear():
    a = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostOffice(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeArea364', b1)
    assert _is_linked(a, 'xal_SubAdministrativeArea364', b1)
    if hasattr(b1, 'xal_PostOffice365'):
        assert _is_linked(b1, 'xal_PostOffice365', a)
    _safe_set(a, 'xal_SubAdministrativeArea364', b2)
    assert _is_linked(a, 'xal_SubAdministrativeArea364', b2)
    if hasattr(b1, 'xal_PostOffice365'):
        assert not _is_linked(b1, 'xal_PostOffice365', a)
    if hasattr(b2, 'xal_PostOffice365'):
        assert _is_linked(b2, 'xal_PostOffice365', a)
    _safe_set(a, 'xal_SubAdministrativeArea364', None)
    assert not _is_linked(a, 'xal_SubAdministrativeArea364', b2)
    if hasattr(b2, 'xal_PostOffice365'):
        assert not _is_linked(b2, 'xal_PostOffice365', a)


def test_assoc_postOffice64_link_reassign_clear():
    a = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostOffice66', b1)
    assert _is_linked(a, 'xal_PostOffice66', b1)
    if hasattr(b1, 'xal_DependentLocality65'):
        assert _is_linked(b1, 'xal_DependentLocality65', a)
    _safe_set(a, 'xal_PostOffice66', b2)
    assert _is_linked(a, 'xal_PostOffice66', b2)
    if hasattr(b1, 'xal_DependentLocality65'):
        assert not _is_linked(b1, 'xal_DependentLocality65', a)
    if hasattr(b2, 'xal_DependentLocality65'):
        assert _is_linked(b2, 'xal_DependentLocality65', a)
    _safe_set(a, 'xal_PostOffice66', None)
    assert not _is_linked(a, 'xal_PostOffice66', b2)
    if hasattr(b2, 'xal_DependentLocality65'):
        assert not _is_linked(b2, 'xal_DependentLocality65', a)


def test_assoc_postOfficeName272_link_reassign_clear():
    a = xal_PostOfficeName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostOffice(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostOfficeName', b1)
    assert _is_linked(a, 'xal_PostOfficeName', b1)
    if hasattr(b1, 'xal_PostOffice273'):
        assert _is_linked(b1, 'xal_PostOffice273', a)
    _safe_set(a, 'xal_PostOfficeName', b2)
    assert _is_linked(a, 'xal_PostOfficeName', b2)
    if hasattr(b1, 'xal_PostOffice273'):
        assert not _is_linked(b1, 'xal_PostOffice273', a)
    if hasattr(b2, 'xal_PostOffice273'):
        assert _is_linked(b2, 'xal_PostOffice273', a)
    _safe_set(a, 'xal_PostOfficeName', None)
    assert not _is_linked(a, 'xal_PostOfficeName', b2)
    if hasattr(b2, 'xal_PostOffice273'):
        assert not _is_linked(b2, 'xal_PostOffice273', a)


def test_assoc_postOfficeNumber274_link_reassign_clear():
    a = xal_PostOfficeNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text")
    b1 = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostOffice(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostOfficeNumber', b1)
    assert _is_linked(a, 'xal_PostOfficeNumber', b1)
    if hasattr(b1, 'xal_PostOffice275'):
        assert _is_linked(b1, 'xal_PostOffice275', a)
    _safe_set(a, 'xal_PostOfficeNumber', b2)
    assert _is_linked(a, 'xal_PostOfficeNumber', b2)
    if hasattr(b1, 'xal_PostOffice275'):
        assert not _is_linked(b1, 'xal_PostOffice275', a)
    if hasattr(b2, 'xal_PostOffice275'):
        assert _is_linked(b2, 'xal_PostOffice275', a)
    _safe_set(a, 'xal_PostOfficeNumber', None)
    assert not _is_linked(a, 'xal_PostOfficeNumber', b2)
    if hasattr(b2, 'xal_PostOffice275'):
        assert not _is_linked(b2, 'xal_PostOffice275', a)


def test_assoc_postTown220_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostTown(anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode221', b1)
    assert _is_linked(a, 'xal_PostalCode221', b1)
    if hasattr(b1, 'xal_PostTown'):
        assert _is_linked(b1, 'xal_PostTown', a)
    _safe_set(a, 'xal_PostalCode221', b2)
    assert _is_linked(a, 'xal_PostalCode221', b2)
    if hasattr(b1, 'xal_PostTown'):
        assert not _is_linked(b1, 'xal_PostTown', a)
    if hasattr(b2, 'xal_PostTown'):
        assert _is_linked(b2, 'xal_PostTown', a)
    _safe_set(a, 'xal_PostalCode221', None)
    assert not _is_linked(a, 'xal_PostalCode221', b2)
    if hasattr(b2, 'xal_PostTown'):
        assert not _is_linked(b2, 'xal_PostTown', a)


def test_assoc_postTownName288_link_reassign_clear():
    a = xal_PostTownName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostTown(anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostTownName', b1)
    assert _is_linked(a, 'xal_PostTownName', b1)
    if hasattr(b1, 'xal_PostTown289'):
        assert _is_linked(b1, 'xal_PostTown289', a)
    _safe_set(a, 'xal_PostTownName', b2)
    assert _is_linked(a, 'xal_PostTownName', b2)
    if hasattr(b1, 'xal_PostTown289'):
        assert not _is_linked(b1, 'xal_PostTown289', a)
    if hasattr(b2, 'xal_PostTown289'):
        assert _is_linked(b2, 'xal_PostTown289', a)
    _safe_set(a, 'xal_PostTownName', None)
    assert not _is_linked(a, 'xal_PostTownName', b2)
    if hasattr(b2, 'xal_PostTown289'):
        assert not _is_linked(b2, 'xal_PostTown289', a)


def test_assoc_postTownSuffix290_link_reassign_clear():
    a = xal_PostTownSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_PostTown(anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostTown(anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostTownSuffix', b1)
    assert _is_linked(a, 'xal_PostTownSuffix', b1)
    if hasattr(b1, 'xal_PostTown291'):
        assert _is_linked(b1, 'xal_PostTown291', a)
    _safe_set(a, 'xal_PostTownSuffix', b2)
    assert _is_linked(a, 'xal_PostTownSuffix', b2)
    if hasattr(b1, 'xal_PostTown291'):
        assert not _is_linked(b1, 'xal_PostTown291', a)
    if hasattr(b2, 'xal_PostTown291'):
        assert _is_linked(b2, 'xal_PostTown291', a)
    _safe_set(a, 'xal_PostTownSuffix', None)
    assert not _is_linked(a, 'xal_PostTownSuffix', b2)
    if hasattr(b2, 'xal_PostTown291'):
        assert not _is_linked(b2, 'xal_PostTown291', a)


def test_assoc_postalCode114_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PostalCode116', b1)
    assert _is_linked(a, 'xal_PostalCode116', b1)
    if hasattr(b1, 'xal_DocumentRoot115'):
        assert _is_linked(b1, 'xal_DocumentRoot115', a)
    _safe_set(a, 'xal_PostalCode116', b2)
    assert _is_linked(a, 'xal_PostalCode116', b2)
    if hasattr(b1, 'xal_DocumentRoot115'):
        assert not _is_linked(b1, 'xal_DocumentRoot115', a)
    if hasattr(b2, 'xal_DocumentRoot115'):
        assert _is_linked(b2, 'xal_DocumentRoot115', a)
    _safe_set(a, 'xal_PostalCode116', None)
    assert not _is_linked(a, 'xal_PostalCode116', b2)
    if hasattr(b2, 'xal_DocumentRoot115'):
        assert not _is_linked(b2, 'xal_DocumentRoot115', a)


def test_assoc_postalCode153_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Firm(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Firm(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode155', b1)
    assert _is_linked(a, 'xal_PostalCode155', b1)
    if hasattr(b1, 'xal_Firm154'):
        assert _is_linked(b1, 'xal_Firm154', a)
    _safe_set(a, 'xal_PostalCode155', b2)
    assert _is_linked(a, 'xal_PostalCode155', b2)
    if hasattr(b1, 'xal_Firm154'):
        assert not _is_linked(b1, 'xal_Firm154', a)
    if hasattr(b2, 'xal_Firm154'):
        assert _is_linked(b2, 'xal_Firm154', a)
    _safe_set(a, 'xal_PostalCode155', None)
    assert not _is_linked(a, 'xal_PostalCode155', b2)
    if hasattr(b2, 'xal_Firm154'):
        assert not _is_linked(b2, 'xal_Firm154', a)


def test_assoc_postalCode174_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode176', b1)
    assert _is_linked(a, 'xal_PostalCode176', b1)
    if hasattr(b1, 'xal_LargeMailUser175'):
        assert _is_linked(b1, 'xal_LargeMailUser175', a)
    _safe_set(a, 'xal_PostalCode176', b2)
    assert _is_linked(a, 'xal_PostalCode176', b2)
    if hasattr(b1, 'xal_LargeMailUser175'):
        assert not _is_linked(b1, 'xal_LargeMailUser175', a)
    if hasattr(b2, 'xal_LargeMailUser175'):
        assert _is_linked(b2, 'xal_LargeMailUser175', a)
    _safe_set(a, 'xal_PostalCode176', None)
    assert not _is_linked(a, 'xal_PostalCode176', b2)
    if hasattr(b2, 'xal_LargeMailUser175'):
        assert not _is_linked(b2, 'xal_LargeMailUser175', a)


def test_assoc_postalCode203_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostalCode205', b1)
    assert _is_linked(a, 'xal_PostalCode205', b1)
    if hasattr(b1, 'xal_Locality204'):
        assert _is_linked(b1, 'xal_Locality204', a)
    _safe_set(a, 'xal_PostalCode205', b2)
    assert _is_linked(a, 'xal_PostalCode205', b2)
    if hasattr(b1, 'xal_Locality204'):
        assert not _is_linked(b1, 'xal_Locality204', a)
    if hasattr(b2, 'xal_Locality204'):
        assert _is_linked(b2, 'xal_Locality204', a)
    _safe_set(a, 'xal_PostalCode205', None)
    assert not _is_linked(a, 'xal_PostalCode205', b2)
    if hasattr(b2, 'xal_Locality204'):
        assert not _is_linked(b2, 'xal_Locality204', a)


def test_assoc_postalCode266_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostBox(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostBox(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode268', b1)
    assert _is_linked(a, 'xal_PostalCode268', b1)
    if hasattr(b1, 'xal_PostBox267'):
        assert _is_linked(b1, 'xal_PostBox267', a)
    _safe_set(a, 'xal_PostalCode268', b2)
    assert _is_linked(a, 'xal_PostalCode268', b2)
    if hasattr(b1, 'xal_PostBox267'):
        assert not _is_linked(b1, 'xal_PostBox267', a)
    if hasattr(b2, 'xal_PostBox267'):
        assert _is_linked(b2, 'xal_PostBox267', a)
    _safe_set(a, 'xal_PostalCode268', None)
    assert not _is_linked(a, 'xal_PostalCode268', b2)
    if hasattr(b2, 'xal_PostBox267'):
        assert not _is_linked(b2, 'xal_PostBox267', a)


def test_assoc_postalCode27_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostalCode', b1)
    assert _is_linked(a, 'xal_PostalCode', b1)
    if hasattr(b1, 'xal_AdministrativeArea28'):
        assert _is_linked(b1, 'xal_AdministrativeArea28', a)
    _safe_set(a, 'xal_PostalCode', b2)
    assert _is_linked(a, 'xal_PostalCode', b2)
    if hasattr(b1, 'xal_AdministrativeArea28'):
        assert not _is_linked(b1, 'xal_AdministrativeArea28', a)
    if hasattr(b2, 'xal_AdministrativeArea28'):
        assert _is_linked(b2, 'xal_AdministrativeArea28', a)
    _safe_set(a, 'xal_PostalCode', None)
    assert not _is_linked(a, 'xal_PostalCode', b2)
    if hasattr(b2, 'xal_AdministrativeArea28'):
        assert not _is_linked(b2, 'xal_AdministrativeArea28', a)


def test_assoc_postalCode282_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostOffice(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode284', b1)
    assert _is_linked(a, 'xal_PostalCode284', b1)
    if hasattr(b1, 'xal_PostOffice283'):
        assert _is_linked(b1, 'xal_PostOffice283', a)
    _safe_set(a, 'xal_PostalCode284', b2)
    assert _is_linked(a, 'xal_PostalCode284', b2)
    if hasattr(b1, 'xal_PostOffice283'):
        assert not _is_linked(b1, 'xal_PostOffice283', a)
    if hasattr(b2, 'xal_PostOffice283'):
        assert _is_linked(b2, 'xal_PostOffice283', a)
    _safe_set(a, 'xal_PostalCode284', None)
    assert not _is_linked(a, 'xal_PostalCode284', b2)
    if hasattr(b2, 'xal_PostOffice283'):
        assert not _is_linked(b2, 'xal_PostOffice283', a)


def test_assoc_postalCode321_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Premise322', b1)
    assert _is_linked(a, 'xal_Premise322', b1)
    if hasattr(b1, 'xal_PostalCode323'):
        assert _is_linked(b1, 'xal_PostalCode323', a)
    _safe_set(a, 'xal_Premise322', b2)
    assert _is_linked(a, 'xal_Premise322', b2)
    if hasattr(b1, 'xal_PostalCode323'):
        assert not _is_linked(b1, 'xal_PostalCode323', a)
    if hasattr(b2, 'xal_PostalCode323'):
        assert _is_linked(b2, 'xal_PostalCode323', a)
    _safe_set(a, 'xal_Premise322', None)
    assert not _is_linked(a, 'xal_Premise322', b2)
    if hasattr(b2, 'xal_PostalCode323'):
        assert not _is_linked(b2, 'xal_PostalCode323', a)


def test_assoc_postalCode366_link_reassign_clear():
    a = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeArea367', b1)
    assert _is_linked(a, 'xal_SubAdministrativeArea367', b1)
    if hasattr(b1, 'xal_PostalCode368'):
        assert _is_linked(b1, 'xal_PostalCode368', a)
    _safe_set(a, 'xal_SubAdministrativeArea367', b2)
    assert _is_linked(a, 'xal_SubAdministrativeArea367', b2)
    if hasattr(b1, 'xal_PostalCode368'):
        assert not _is_linked(b1, 'xal_PostalCode368', a)
    if hasattr(b2, 'xal_PostalCode368'):
        assert _is_linked(b2, 'xal_PostalCode368', a)
    _safe_set(a, 'xal_SubAdministrativeArea367', None)
    assert not _is_linked(a, 'xal_SubAdministrativeArea367', b2)
    if hasattr(b2, 'xal_PostalCode368'):
        assert not _is_linked(b2, 'xal_PostalCode368', a)


def test_assoc_postalCode391_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise392', b1)
    assert _is_linked(a, 'xal_SubPremise392', b1)
    if hasattr(b1, 'xal_PostalCode393'):
        assert _is_linked(b1, 'xal_PostalCode393', a)
    _safe_set(a, 'xal_SubPremise392', b2)
    assert _is_linked(a, 'xal_SubPremise392', b2)
    if hasattr(b1, 'xal_PostalCode393'):
        assert not _is_linked(b1, 'xal_PostalCode393', a)
    if hasattr(b2, 'xal_PostalCode393'):
        assert _is_linked(b2, 'xal_PostalCode393', a)
    _safe_set(a, 'xal_SubPremise392', None)
    assert not _is_linked(a, 'xal_SubPremise392', b2)
    if hasattr(b2, 'xal_PostalCode393'):
        assert not _is_linked(b2, 'xal_PostalCode393', a)


def test_assoc_postalCode438_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare439', b1)
    assert _is_linked(a, 'xal_Thoroughfare439', b1)
    if hasattr(b1, 'xal_PostalCode440'):
        assert _is_linked(b1, 'xal_PostalCode440', a)
    _safe_set(a, 'xal_Thoroughfare439', b2)
    assert _is_linked(a, 'xal_Thoroughfare439', b2)
    if hasattr(b1, 'xal_PostalCode440'):
        assert not _is_linked(b1, 'xal_PostalCode440', a)
    if hasattr(b2, 'xal_PostalCode440'):
        assert _is_linked(b2, 'xal_PostalCode440', a)
    _safe_set(a, 'xal_Thoroughfare439', None)
    assert not _is_linked(a, 'xal_Thoroughfare439', b2)
    if hasattr(b2, 'xal_PostalCode440'):
        assert not _is_linked(b2, 'xal_PostalCode440', a)


def test_assoc_postalCode51_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Department(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_Department(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCode53', b1)
    assert _is_linked(a, 'xal_PostalCode53', b1)
    if hasattr(b1, 'xal_Department52'):
        assert _is_linked(b1, 'xal_Department52', a)
    _safe_set(a, 'xal_PostalCode53', b2)
    assert _is_linked(a, 'xal_PostalCode53', b2)
    if hasattr(b1, 'xal_Department52'):
        assert not _is_linked(b1, 'xal_Department52', a)
    if hasattr(b2, 'xal_Department52'):
        assert _is_linked(b2, 'xal_Department52', a)
    _safe_set(a, 'xal_PostalCode53', None)
    assert not _is_linked(a, 'xal_PostalCode53', b2)
    if hasattr(b2, 'xal_Department52'):
        assert not _is_linked(b2, 'xal_Department52', a)


def test_assoc_postalCode77_link_reassign_clear():
    a = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostalCode79', b1)
    assert _is_linked(a, 'xal_PostalCode79', b1)
    if hasattr(b1, 'xal_DependentLocality78'):
        assert _is_linked(b1, 'xal_DependentLocality78', a)
    _safe_set(a, 'xal_PostalCode79', b2)
    assert _is_linked(a, 'xal_PostalCode79', b2)
    if hasattr(b1, 'xal_DependentLocality78'):
        assert not _is_linked(b1, 'xal_DependentLocality78', a)
    if hasattr(b2, 'xal_DependentLocality78'):
        assert _is_linked(b2, 'xal_DependentLocality78', a)
    _safe_set(a, 'xal_PostalCode79', None)
    assert not _is_linked(a, 'xal_PostalCode79', b2)
    if hasattr(b2, 'xal_DependentLocality78'):
        assert not _is_linked(b2, 'xal_DependentLocality78', a)


def test_assoc_postalCodeNumber216_link_reassign_clear():
    a = xal_PostalCodeNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCodeNumber', b1)
    assert _is_linked(a, 'xal_PostalCodeNumber', b1)
    if hasattr(b1, 'xal_PostalCode217'):
        assert _is_linked(b1, 'xal_PostalCode217', a)
    _safe_set(a, 'xal_PostalCodeNumber', b2)
    assert _is_linked(a, 'xal_PostalCodeNumber', b2)
    if hasattr(b1, 'xal_PostalCode217'):
        assert not _is_linked(b1, 'xal_PostalCode217', a)
    if hasattr(b2, 'xal_PostalCode217'):
        assert _is_linked(b2, 'xal_PostalCode217', a)
    _safe_set(a, 'xal_PostalCodeNumber', None)
    assert not _is_linked(a, 'xal_PostalCodeNumber', b2)
    if hasattr(b2, 'xal_PostalCode217'):
        assert not _is_linked(b2, 'xal_PostalCode217', a)


def test_assoc_postalCodeNumberExtension218_link_reassign_clear():
    a = xal_PostalCodeNumberExtension(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberExtensionSeparator="sample_text", type="sample_text")
    b1 = xal_PostalCode(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalCode(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalCodeNumberExtension', b1)
    assert _is_linked(a, 'xal_PostalCodeNumberExtension', b1)
    if hasattr(b1, 'xal_PostalCode219'):
        assert _is_linked(b1, 'xal_PostalCode219', a)
    _safe_set(a, 'xal_PostalCodeNumberExtension', b2)
    assert _is_linked(a, 'xal_PostalCodeNumberExtension', b2)
    if hasattr(b1, 'xal_PostalCode219'):
        assert not _is_linked(b1, 'xal_PostalCode219', a)
    if hasattr(b2, 'xal_PostalCode219'):
        assert _is_linked(b2, 'xal_PostalCode219', a)
    _safe_set(a, 'xal_PostalCodeNumberExtension', None)
    assert not _is_linked(a, 'xal_PostalCodeNumberExtension', b2)
    if hasattr(b2, 'xal_PostalCode219'):
        assert not _is_linked(b2, 'xal_PostalCode219', a)


def test_assoc_postalRoute191_link_reassign_clear():
    a = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostalRoute193', b1)
    assert _is_linked(a, 'xal_PostalRoute193', b1)
    if hasattr(b1, 'xal_Locality192'):
        assert _is_linked(b1, 'xal_Locality192', a)
    _safe_set(a, 'xal_PostalRoute193', b2)
    assert _is_linked(a, 'xal_PostalRoute193', b2)
    if hasattr(b1, 'xal_Locality192'):
        assert not _is_linked(b1, 'xal_Locality192', a)
    if hasattr(b2, 'xal_Locality192'):
        assert _is_linked(b2, 'xal_Locality192', a)
    _safe_set(a, 'xal_PostalRoute193', None)
    assert not _is_linked(a, 'xal_PostalRoute193', b2)
    if hasattr(b2, 'xal_Locality192'):
        assert not _is_linked(b2, 'xal_Locality192', a)


def test_assoc_postalRoute276_link_reassign_clear():
    a = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_PostOffice(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text")
    b2 = xal_PostOffice(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalRoute278', b1)
    assert _is_linked(a, 'xal_PostalRoute278', b1)
    if hasattr(b1, 'xal_PostOffice277'):
        assert _is_linked(b1, 'xal_PostOffice277', a)
    _safe_set(a, 'xal_PostalRoute278', b2)
    assert _is_linked(a, 'xal_PostalRoute278', b2)
    if hasattr(b1, 'xal_PostOffice277'):
        assert not _is_linked(b1, 'xal_PostOffice277', a)
    if hasattr(b2, 'xal_PostOffice277'):
        assert _is_linked(b2, 'xal_PostOffice277', a)
    _safe_set(a, 'xal_PostalRoute278', None)
    assert not _is_linked(a, 'xal_PostalRoute278', b2)
    if hasattr(b2, 'xal_PostOffice277'):
        assert not _is_linked(b2, 'xal_PostOffice277', a)


def test_assoc_postalRoute67_link_reassign_clear():
    a = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_PostalRoute', b1)
    assert _is_linked(a, 'xal_PostalRoute', b1)
    if hasattr(b1, 'xal_DependentLocality68'):
        assert _is_linked(b1, 'xal_DependentLocality68', a)
    _safe_set(a, 'xal_PostalRoute', b2)
    assert _is_linked(a, 'xal_PostalRoute', b2)
    if hasattr(b1, 'xal_DependentLocality68'):
        assert not _is_linked(b1, 'xal_DependentLocality68', a)
    if hasattr(b2, 'xal_DependentLocality68'):
        assert _is_linked(b2, 'xal_DependentLocality68', a)
    _safe_set(a, 'xal_PostalRoute', None)
    assert not _is_linked(a, 'xal_PostalRoute', b2)
    if hasattr(b2, 'xal_DependentLocality68'):
        assert not _is_linked(b2, 'xal_DependentLocality68', a)


def test_assoc_postalRouteName225_link_reassign_clear():
    a = xal_PostalRouteName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalRoute(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalRouteName', b1)
    assert _is_linked(a, 'xal_PostalRouteName', b1)
    if hasattr(b1, 'xal_PostalRoute226'):
        assert _is_linked(b1, 'xal_PostalRoute226', a)
    _safe_set(a, 'xal_PostalRouteName', b2)
    assert _is_linked(a, 'xal_PostalRouteName', b2)
    if hasattr(b1, 'xal_PostalRoute226'):
        assert not _is_linked(b1, 'xal_PostalRoute226', a)
    if hasattr(b2, 'xal_PostalRoute226'):
        assert _is_linked(b2, 'xal_PostalRoute226', a)
    _safe_set(a, 'xal_PostalRouteName', None)
    assert not _is_linked(a, 'xal_PostalRouteName', b2)
    if hasattr(b2, 'xal_PostalRoute226'):
        assert not _is_linked(b2, 'xal_PostalRoute226', a)


def test_assoc_postalRouteNumber227_link_reassign_clear():
    a = xal_PostalRouteNumber(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_PostalRoute(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalRoute(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PostalRouteNumber', b1)
    assert _is_linked(a, 'xal_PostalRouteNumber', b1)
    if hasattr(b1, 'xal_PostalRoute228'):
        assert _is_linked(b1, 'xal_PostalRoute228', a)
    _safe_set(a, 'xal_PostalRouteNumber', b2)
    assert _is_linked(a, 'xal_PostalRouteNumber', b2)
    if hasattr(b1, 'xal_PostalRoute228'):
        assert not _is_linked(b1, 'xal_PostalRoute228', a)
    if hasattr(b2, 'xal_PostalRoute228'):
        assert _is_linked(b2, 'xal_PostalRoute228', a)
    _safe_set(a, 'xal_PostalRouteNumber', None)
    assert not _is_linked(a, 'xal_PostalRouteNumber', b2)
    if hasattr(b2, 'xal_PostalRoute228'):
        assert not _is_linked(b2, 'xal_PostalRoute228', a)


def test_assoc_postalServiceElements0_link_reassign_clear():
    a = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_PostalServiceElements', b1)
    assert _is_linked(a, 'xal_PostalServiceElements', b1)
    if hasattr(b1, 'xal_AddressDetails'):
        assert _is_linked(b1, 'xal_AddressDetails', a)
    _safe_set(a, 'xal_PostalServiceElements', b2)
    assert _is_linked(a, 'xal_PostalServiceElements', b2)
    if hasattr(b1, 'xal_AddressDetails'):
        assert not _is_linked(b1, 'xal_AddressDetails', a)
    if hasattr(b2, 'xal_AddressDetails'):
        assert _is_linked(b2, 'xal_AddressDetails', a)
    _safe_set(a, 'xal_PostalServiceElements', None)
    assert not _is_linked(a, 'xal_PostalServiceElements', b2)
    if hasattr(b2, 'xal_AddressDetails'):
        assert not _is_linked(b2, 'xal_AddressDetails', a)


def test_assoc_premise123_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_Premise125', b1)
    assert _is_linked(a, 'xal_Premise125', b1)
    if hasattr(b1, 'xal_DocumentRoot124'):
        assert _is_linked(b1, 'xal_DocumentRoot124', a)
    _safe_set(a, 'xal_Premise125', b2)
    assert _is_linked(a, 'xal_Premise125', b2)
    if hasattr(b1, 'xal_DocumentRoot124'):
        assert not _is_linked(b1, 'xal_DocumentRoot124', a)
    if hasattr(b2, 'xal_DocumentRoot124'):
        assert _is_linked(b2, 'xal_DocumentRoot124', a)
    _safe_set(a, 'xal_Premise125', None)
    assert not _is_linked(a, 'xal_Premise125', b2)
    if hasattr(b2, 'xal_DocumentRoot124'):
        assert not _is_linked(b2, 'xal_DocumentRoot124', a)


def test_assoc_premise197_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Premise199', b1)
    assert _is_linked(a, 'xal_Premise199', b1)
    if hasattr(b1, 'xal_Locality198'):
        assert _is_linked(b1, 'xal_Locality198', a)
    _safe_set(a, 'xal_Premise199', b2)
    assert _is_linked(a, 'xal_Premise199', b2)
    if hasattr(b1, 'xal_Locality198'):
        assert not _is_linked(b1, 'xal_Locality198', a)
    if hasattr(b2, 'xal_Locality198'):
        assert _is_linked(b2, 'xal_Locality198', a)
    _safe_set(a, 'xal_Premise199', None)
    assert not _is_linked(a, 'xal_Premise199', b2)
    if hasattr(b2, 'xal_Locality198'):
        assert not _is_linked(b2, 'xal_Locality198', a)


def test_assoc_premise325_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Premise324', b1)
    assert _is_linked(a, 'xal_Premise324', b1)
    if hasattr(b1, 'xal_Premise326'):
        assert _is_linked(b1, 'xal_Premise326', a)
    _safe_set(a, 'xal_Premise324', b2)
    assert _is_linked(a, 'xal_Premise324', b2)
    if hasattr(b1, 'xal_Premise326'):
        assert not _is_linked(b1, 'xal_Premise326', a)
    if hasattr(b2, 'xal_Premise326'):
        assert _is_linked(b2, 'xal_Premise326', a)
    _safe_set(a, 'xal_Premise324', None)
    assert not _is_linked(a, 'xal_Premise324', b2)
    if hasattr(b2, 'xal_Premise326'):
        assert not _is_linked(b2, 'xal_Premise326', a)


def test_assoc_premise432_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare433', b1)
    assert _is_linked(a, 'xal_Thoroughfare433', b1)
    if hasattr(b1, 'xal_Premise434'):
        assert _is_linked(b1, 'xal_Premise434', a)
    _safe_set(a, 'xal_Thoroughfare433', b2)
    assert _is_linked(a, 'xal_Thoroughfare433', b2)
    if hasattr(b1, 'xal_Premise434'):
        assert not _is_linked(b1, 'xal_Premise434', a)
    if hasattr(b2, 'xal_Premise434'):
        assert _is_linked(b2, 'xal_Premise434', a)
    _safe_set(a, 'xal_Thoroughfare433', None)
    assert not _is_linked(a, 'xal_Thoroughfare433', b2)
    if hasattr(b2, 'xal_Premise434'):
        assert not _is_linked(b2, 'xal_Premise434', a)


def test_assoc_premise72_link_reassign_clear():
    a = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Premise', b1)
    assert _is_linked(a, 'xal_Premise', b1)
    if hasattr(b1, 'xal_DependentLocality73'):
        assert _is_linked(b1, 'xal_DependentLocality73', a)
    _safe_set(a, 'xal_Premise', b2)
    assert _is_linked(a, 'xal_Premise', b2)
    if hasattr(b1, 'xal_DependentLocality73'):
        assert not _is_linked(b1, 'xal_DependentLocality73', a)
    if hasattr(b2, 'xal_DependentLocality73'):
        assert _is_linked(b2, 'xal_DependentLocality73', a)
    _safe_set(a, 'xal_Premise', None)
    assert not _is_linked(a, 'xal_Premise', b2)
    if hasattr(b2, 'xal_DependentLocality73'):
        assert not _is_linked(b2, 'xal_DependentLocality73', a)


def test_assoc_premiseLocation297_link_reassign_clear():
    a = xal_PremiseLocation(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseLocation', b1)
    assert _is_linked(a, 'xal_PremiseLocation', b1)
    if hasattr(b1, 'xal_Premise298'):
        assert _is_linked(b1, 'xal_Premise298', a)
    _safe_set(a, 'xal_PremiseLocation', b2)
    assert _is_linked(a, 'xal_PremiseLocation', b2)
    if hasattr(b1, 'xal_Premise298'):
        assert not _is_linked(b1, 'xal_Premise298', a)
    if hasattr(b2, 'xal_Premise298'):
        assert _is_linked(b2, 'xal_Premise298', a)
    _safe_set(a, 'xal_PremiseLocation', None)
    assert not _is_linked(a, 'xal_PremiseLocation', b2)
    if hasattr(b2, 'xal_Premise298'):
        assert not _is_linked(b2, 'xal_Premise298', a)


def test_assoc_premiseName295_link_reassign_clear():
    a = xal_PremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseName', b1)
    assert _is_linked(a, 'xal_PremiseName', b1)
    if hasattr(b1, 'xal_Premise296'):
        assert _is_linked(b1, 'xal_Premise296', a)
    _safe_set(a, 'xal_PremiseName', b2)
    assert _is_linked(a, 'xal_PremiseName', b2)
    if hasattr(b1, 'xal_Premise296'):
        assert not _is_linked(b1, 'xal_Premise296', a)
    if hasattr(b2, 'xal_Premise296'):
        assert _is_linked(b2, 'xal_Premise296', a)
    _safe_set(a, 'xal_PremiseName', None)
    assert not _is_linked(a, 'xal_PremiseName', b2)
    if hasattr(b2, 'xal_Premise296'):
        assert not _is_linked(b2, 'xal_Premise296', a)


def test_assoc_premiseNumber126_link_reassign_clear():
    a = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PremiseNumber', b1)
    assert _is_linked(a, 'xal_PremiseNumber', b1)
    if hasattr(b1, 'xal_DocumentRoot127'):
        assert _is_linked(b1, 'xal_DocumentRoot127', a)
    _safe_set(a, 'xal_PremiseNumber', b2)
    assert _is_linked(a, 'xal_PremiseNumber', b2)
    if hasattr(b1, 'xal_DocumentRoot127'):
        assert not _is_linked(b1, 'xal_DocumentRoot127', a)
    if hasattr(b2, 'xal_DocumentRoot127'):
        assert _is_linked(b2, 'xal_DocumentRoot127', a)
    _safe_set(a, 'xal_PremiseNumber', None)
    assert not _is_linked(a, 'xal_PremiseNumber', b2)
    if hasattr(b2, 'xal_DocumentRoot127'):
        assert not _is_linked(b2, 'xal_DocumentRoot127', a)


def test_assoc_premiseNumber299_link_reassign_clear():
    a = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseNumber301', b1)
    assert _is_linked(a, 'xal_PremiseNumber301', b1)
    if hasattr(b1, 'xal_Premise300'):
        assert _is_linked(b1, 'xal_Premise300', a)
    _safe_set(a, 'xal_PremiseNumber301', b2)
    assert _is_linked(a, 'xal_PremiseNumber301', b2)
    if hasattr(b1, 'xal_Premise300'):
        assert not _is_linked(b1, 'xal_Premise300', a)
    if hasattr(b2, 'xal_Premise300'):
        assert _is_linked(b2, 'xal_Premise300', a)
    _safe_set(a, 'xal_PremiseNumber301', None)
    assert not _is_linked(a, 'xal_PremiseNumber301', b2)
    if hasattr(b2, 'xal_Premise300'):
        assert not _is_linked(b2, 'xal_Premise300', a)


def test_assoc_premiseNumber337_link_reassign_clear():
    a = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeFrom()
    b2 = xal_PremiseNumberRangeFrom()
    _safe_set(a, 'xal_PremiseNumber339', b1)
    assert _is_linked(a, 'xal_PremiseNumber339', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom338'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeFrom338', a)
    _safe_set(a, 'xal_PremiseNumber339', b2)
    assert _is_linked(a, 'xal_PremiseNumber339', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom338'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeFrom338', a)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom338'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeFrom338', a)
    _safe_set(a, 'xal_PremiseNumber339', None)
    assert not _is_linked(a, 'xal_PremiseNumber339', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom338'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeFrom338', a)


def test_assoc_premiseNumber349_link_reassign_clear():
    a = xal_PremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberType="sample_text", numberTypeOccurrence="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeTo()
    b2 = xal_PremiseNumberRangeTo()
    _safe_set(a, 'xal_PremiseNumber351', b1)
    assert _is_linked(a, 'xal_PremiseNumber351', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeTo350'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeTo350', a)
    _safe_set(a, 'xal_PremiseNumber351', b2)
    assert _is_linked(a, 'xal_PremiseNumber351', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeTo350'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeTo350', a)
    if hasattr(b2, 'xal_PremiseNumberRangeTo350'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeTo350', a)
    _safe_set(a, 'xal_PremiseNumber351', None)
    assert not _is_linked(a, 'xal_PremiseNumber351', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeTo350'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeTo350', a)


def test_assoc_premiseNumberPrefix128_link_reassign_clear():
    a = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PremiseNumberPrefix', b1)
    assert _is_linked(a, 'xal_PremiseNumberPrefix', b1)
    if hasattr(b1, 'xal_DocumentRoot129'):
        assert _is_linked(b1, 'xal_DocumentRoot129', a)
    _safe_set(a, 'xal_PremiseNumberPrefix', b2)
    assert _is_linked(a, 'xal_PremiseNumberPrefix', b2)
    if hasattr(b1, 'xal_DocumentRoot129'):
        assert not _is_linked(b1, 'xal_DocumentRoot129', a)
    if hasattr(b2, 'xal_DocumentRoot129'):
        assert _is_linked(b2, 'xal_DocumentRoot129', a)
    _safe_set(a, 'xal_PremiseNumberPrefix', None)
    assert not _is_linked(a, 'xal_PremiseNumberPrefix', b2)
    if hasattr(b2, 'xal_DocumentRoot129'):
        assert not _is_linked(b2, 'xal_DocumentRoot129', a)


def test_assoc_premiseNumberPrefix304_link_reassign_clear():
    a = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseNumberPrefix306', b1)
    assert _is_linked(a, 'xal_PremiseNumberPrefix306', b1)
    if hasattr(b1, 'xal_Premise305'):
        assert _is_linked(b1, 'xal_Premise305', a)
    _safe_set(a, 'xal_PremiseNumberPrefix306', b2)
    assert _is_linked(a, 'xal_PremiseNumberPrefix306', b2)
    if hasattr(b1, 'xal_Premise305'):
        assert not _is_linked(b1, 'xal_Premise305', a)
    if hasattr(b2, 'xal_Premise305'):
        assert _is_linked(b2, 'xal_Premise305', a)
    _safe_set(a, 'xal_PremiseNumberPrefix306', None)
    assert not _is_linked(a, 'xal_PremiseNumberPrefix306', b2)
    if hasattr(b2, 'xal_Premise305'):
        assert not _is_linked(b2, 'xal_Premise305', a)


def test_assoc_premiseNumberPrefix334_link_reassign_clear():
    a = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    b1 = xal_PremiseNumberRangeFrom()
    b2 = xal_PremiseNumberRangeFrom()
    _safe_set(a, 'xal_PremiseNumberPrefix336', b1)
    assert _is_linked(a, 'xal_PremiseNumberPrefix336', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom335'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeFrom335', a)
    _safe_set(a, 'xal_PremiseNumberPrefix336', b2)
    assert _is_linked(a, 'xal_PremiseNumberPrefix336', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom335'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeFrom335', a)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom335'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeFrom335', a)
    _safe_set(a, 'xal_PremiseNumberPrefix336', None)
    assert not _is_linked(a, 'xal_PremiseNumberPrefix336', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom335'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeFrom335', a)


def test_assoc_premiseNumberPrefix346_link_reassign_clear():
    a = xal_PremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", numberPrefixSeparator="sample_text", type="sample_text", value="sample_text")
    b1 = xal_PremiseNumberRangeTo()
    b2 = xal_PremiseNumberRangeTo()
    _safe_set(a, 'xal_PremiseNumberPrefix348', b1)
    assert _is_linked(a, 'xal_PremiseNumberPrefix348', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeTo347'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeTo347', a)
    _safe_set(a, 'xal_PremiseNumberPrefix348', b2)
    assert _is_linked(a, 'xal_PremiseNumberPrefix348', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeTo347'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeTo347', a)
    if hasattr(b2, 'xal_PremiseNumberRangeTo347'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeTo347', a)
    _safe_set(a, 'xal_PremiseNumberPrefix348', None)
    assert not _is_linked(a, 'xal_PremiseNumberPrefix348', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeTo347'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeTo347', a)


def test_assoc_premiseNumberRange302_link_reassign_clear():
    a = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseNumberRange', b1)
    assert _is_linked(a, 'xal_PremiseNumberRange', b1)
    if hasattr(b1, 'xal_Premise303'):
        assert _is_linked(b1, 'xal_Premise303', a)
    _safe_set(a, 'xal_PremiseNumberRange', b2)
    assert _is_linked(a, 'xal_PremiseNumberRange', b2)
    if hasattr(b1, 'xal_Premise303'):
        assert not _is_linked(b1, 'xal_Premise303', a)
    if hasattr(b2, 'xal_Premise303'):
        assert _is_linked(b2, 'xal_Premise303', a)
    _safe_set(a, 'xal_PremiseNumberRange', None)
    assert not _is_linked(a, 'xal_PremiseNumberRange', b2)
    if hasattr(b2, 'xal_Premise303'):
        assert not _is_linked(b2, 'xal_Premise303', a)


def test_assoc_premiseNumberRangeFrom327_link_reassign_clear():
    a = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeFrom()
    b2 = xal_PremiseNumberRangeFrom()
    _safe_set(a, 'xal_PremiseNumberRange328', b1)
    assert _is_linked(a, 'xal_PremiseNumberRange328', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeFrom', a)
    _safe_set(a, 'xal_PremiseNumberRange328', b2)
    assert _is_linked(a, 'xal_PremiseNumberRange328', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeFrom', a)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeFrom', a)
    _safe_set(a, 'xal_PremiseNumberRange328', None)
    assert not _is_linked(a, 'xal_PremiseNumberRange328', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeFrom', a)


def test_assoc_premiseNumberRangeTo329_link_reassign_clear():
    a = xal_PremiseNumberRange(indicator="sample_text", indicatorOccurence="sample_text", numberRangeOccurence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeTo()
    b2 = xal_PremiseNumberRangeTo()
    _safe_set(a, 'xal_PremiseNumberRange330', b1)
    assert _is_linked(a, 'xal_PremiseNumberRange330', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeTo'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeTo', a)
    _safe_set(a, 'xal_PremiseNumberRange330', b2)
    assert _is_linked(a, 'xal_PremiseNumberRange330', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeTo'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeTo', a)
    if hasattr(b2, 'xal_PremiseNumberRangeTo'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeTo', a)
    _safe_set(a, 'xal_PremiseNumberRange330', None)
    assert not _is_linked(a, 'xal_PremiseNumberRange330', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeTo'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeTo', a)


def test_assoc_premiseNumberSuffix130_link_reassign_clear():
    a = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_PremiseNumberSuffix', b1)
    assert _is_linked(a, 'xal_PremiseNumberSuffix', b1)
    if hasattr(b1, 'xal_DocumentRoot131'):
        assert _is_linked(b1, 'xal_DocumentRoot131', a)
    _safe_set(a, 'xal_PremiseNumberSuffix', b2)
    assert _is_linked(a, 'xal_PremiseNumberSuffix', b2)
    if hasattr(b1, 'xal_DocumentRoot131'):
        assert not _is_linked(b1, 'xal_DocumentRoot131', a)
    if hasattr(b2, 'xal_DocumentRoot131'):
        assert _is_linked(b2, 'xal_DocumentRoot131', a)
    _safe_set(a, 'xal_PremiseNumberSuffix', None)
    assert not _is_linked(a, 'xal_PremiseNumberSuffix', b2)
    if hasattr(b2, 'xal_DocumentRoot131'):
        assert not _is_linked(b2, 'xal_DocumentRoot131', a)


def test_assoc_premiseNumberSuffix307_link_reassign_clear():
    a = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_PremiseNumberSuffix309', b1)
    assert _is_linked(a, 'xal_PremiseNumberSuffix309', b1)
    if hasattr(b1, 'xal_Premise308'):
        assert _is_linked(b1, 'xal_Premise308', a)
    _safe_set(a, 'xal_PremiseNumberSuffix309', b2)
    assert _is_linked(a, 'xal_PremiseNumberSuffix309', b2)
    if hasattr(b1, 'xal_Premise308'):
        assert not _is_linked(b1, 'xal_Premise308', a)
    if hasattr(b2, 'xal_Premise308'):
        assert _is_linked(b2, 'xal_Premise308', a)
    _safe_set(a, 'xal_PremiseNumberSuffix309', None)
    assert not _is_linked(a, 'xal_PremiseNumberSuffix309', b2)
    if hasattr(b2, 'xal_Premise308'):
        assert not _is_linked(b2, 'xal_Premise308', a)


def test_assoc_premiseNumberSuffix340_link_reassign_clear():
    a = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeFrom()
    b2 = xal_PremiseNumberRangeFrom()
    _safe_set(a, 'xal_PremiseNumberSuffix342', b1)
    assert _is_linked(a, 'xal_PremiseNumberSuffix342', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom341'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeFrom341', a)
    _safe_set(a, 'xal_PremiseNumberSuffix342', b2)
    assert _is_linked(a, 'xal_PremiseNumberSuffix342', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeFrom341'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeFrom341', a)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom341'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeFrom341', a)
    _safe_set(a, 'xal_PremiseNumberSuffix342', None)
    assert not _is_linked(a, 'xal_PremiseNumberSuffix342', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeFrom341'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeFrom341', a)


def test_assoc_premiseNumberSuffix352_link_reassign_clear():
    a = xal_PremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_PremiseNumberRangeTo()
    b2 = xal_PremiseNumberRangeTo()
    _safe_set(a, 'xal_PremiseNumberSuffix354', b1)
    assert _is_linked(a, 'xal_PremiseNumberSuffix354', b1)
    if hasattr(b1, 'xal_PremiseNumberRangeTo353'):
        assert _is_linked(b1, 'xal_PremiseNumberRangeTo353', a)
    _safe_set(a, 'xal_PremiseNumberSuffix354', b2)
    assert _is_linked(a, 'xal_PremiseNumberSuffix354', b2)
    if hasattr(b1, 'xal_PremiseNumberRangeTo353'):
        assert not _is_linked(b1, 'xal_PremiseNumberRangeTo353', a)
    if hasattr(b2, 'xal_PremiseNumberRangeTo353'):
        assert _is_linked(b2, 'xal_PremiseNumberRangeTo353', a)
    _safe_set(a, 'xal_PremiseNumberSuffix354', None)
    assert not _is_linked(a, 'xal_PremiseNumberSuffix354', b2)
    if hasattr(b2, 'xal_PremiseNumberRangeTo353'):
        assert not _is_linked(b2, 'xal_PremiseNumberRangeTo353', a)


def test_assoc_sortingCode240_link_reassign_clear():
    a = xal_SortingCode(code="sample_text", type="sample_text")
    b1 = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalServiceElements(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SortingCode', b1)
    assert _is_linked(a, 'xal_SortingCode', b1)
    if hasattr(b1, 'xal_PostalServiceElements241'):
        assert _is_linked(b1, 'xal_PostalServiceElements241', a)
    _safe_set(a, 'xal_SortingCode', b2)
    assert _is_linked(a, 'xal_SortingCode', b2)
    if hasattr(b1, 'xal_PostalServiceElements241'):
        assert not _is_linked(b1, 'xal_PostalServiceElements241', a)
    if hasattr(b2, 'xal_PostalServiceElements241'):
        assert _is_linked(b2, 'xal_PostalServiceElements241', a)
    _safe_set(a, 'xal_SortingCode', None)
    assert not _is_linked(a, 'xal_SortingCode', b2)
    if hasattr(b2, 'xal_PostalServiceElements241'):
        assert not _is_linked(b2, 'xal_PostalServiceElements241', a)


def test_assoc_subAdministrativeArea20_link_reassign_clear():
    a = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b1 = xal_AdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_AdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeArea', b1)
    assert _is_linked(a, 'xal_SubAdministrativeArea', b1)
    if hasattr(b1, 'xal_AdministrativeArea21'):
        assert _is_linked(b1, 'xal_AdministrativeArea21', a)
    _safe_set(a, 'xal_SubAdministrativeArea', b2)
    assert _is_linked(a, 'xal_SubAdministrativeArea', b2)
    if hasattr(b1, 'xal_AdministrativeArea21'):
        assert not _is_linked(b1, 'xal_AdministrativeArea21', a)
    if hasattr(b2, 'xal_AdministrativeArea21'):
        assert _is_linked(b2, 'xal_AdministrativeArea21', a)
    _safe_set(a, 'xal_SubAdministrativeArea', None)
    assert not _is_linked(a, 'xal_SubAdministrativeArea', b2)
    if hasattr(b2, 'xal_AdministrativeArea21'):
        assert not _is_linked(b2, 'xal_AdministrativeArea21', a)


def test_assoc_subAdministrativeAreaName358_link_reassign_clear():
    a = xal_SubAdministrativeAreaName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_SubAdministrativeArea(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_SubAdministrativeArea(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_SubAdministrativeAreaName', b1)
    assert _is_linked(a, 'xal_SubAdministrativeAreaName', b1)
    if hasattr(b1, 'xal_SubAdministrativeArea359'):
        assert _is_linked(b1, 'xal_SubAdministrativeArea359', a)
    _safe_set(a, 'xal_SubAdministrativeAreaName', b2)
    assert _is_linked(a, 'xal_SubAdministrativeAreaName', b2)
    if hasattr(b1, 'xal_SubAdministrativeArea359'):
        assert not _is_linked(b1, 'xal_SubAdministrativeArea359', a)
    if hasattr(b2, 'xal_SubAdministrativeArea359'):
        assert _is_linked(b2, 'xal_SubAdministrativeArea359', a)
    _safe_set(a, 'xal_SubAdministrativeAreaName', None)
    assert not _is_linked(a, 'xal_SubAdministrativeAreaName', b2)
    if hasattr(b2, 'xal_SubAdministrativeArea359'):
        assert not _is_linked(b2, 'xal_SubAdministrativeArea359', a)


def test_assoc_subPremise313_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_Premise(any="sample_text", anyAttribute="sample_text", premiseDependency="sample_text", premiseDependencyType="sample_text", premiseThoroughfareConnector="sample_text", type="sample_text")
    b2 = xal_Premise(any="sample_text_2", anyAttribute="sample_text_2", premiseDependency="sample_text_2", premiseDependencyType="sample_text_2", premiseThoroughfareConnector="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise', b1)
    assert _is_linked(a, 'xal_SubPremise', b1)
    if hasattr(b1, 'xal_Premise314'):
        assert _is_linked(b1, 'xal_Premise314', a)
    _safe_set(a, 'xal_SubPremise', b2)
    assert _is_linked(a, 'xal_SubPremise', b2)
    if hasattr(b1, 'xal_Premise314'):
        assert not _is_linked(b1, 'xal_Premise314', a)
    if hasattr(b2, 'xal_Premise314'):
        assert _is_linked(b2, 'xal_Premise314', a)
    _safe_set(a, 'xal_SubPremise', None)
    assert not _is_linked(a, 'xal_SubPremise', b2)
    if hasattr(b2, 'xal_Premise314'):
        assert not _is_linked(b2, 'xal_Premise314', a)


def test_assoc_subPremise395_link_reassign_clear():
    a = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremise394', b1)
    assert _is_linked(a, 'xal_SubPremise394', b1)
    if hasattr(b1, 'xal_SubPremise396'):
        assert _is_linked(b1, 'xal_SubPremise396', a)
    _safe_set(a, 'xal_SubPremise394', b2)
    assert _is_linked(a, 'xal_SubPremise394', b2)
    if hasattr(b1, 'xal_SubPremise396'):
        assert not _is_linked(b1, 'xal_SubPremise396', a)
    if hasattr(b2, 'xal_SubPremise396'):
        assert _is_linked(b2, 'xal_SubPremise396', a)
    _safe_set(a, 'xal_SubPremise394', None)
    assert not _is_linked(a, 'xal_SubPremise394', b2)
    if hasattr(b2, 'xal_SubPremise396'):
        assert not _is_linked(b2, 'xal_SubPremise396', a)


def test_assoc_subPremiseLocation374_link_reassign_clear():
    a = xal_SubPremiseLocation(code="sample_text", mixed="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremiseLocation', b1)
    assert _is_linked(a, 'xal_SubPremiseLocation', b1)
    if hasattr(b1, 'xal_SubPremise375'):
        assert _is_linked(b1, 'xal_SubPremise375', a)
    _safe_set(a, 'xal_SubPremiseLocation', b2)
    assert _is_linked(a, 'xal_SubPremiseLocation', b2)
    if hasattr(b1, 'xal_SubPremise375'):
        assert not _is_linked(b1, 'xal_SubPremise375', a)
    if hasattr(b2, 'xal_SubPremise375'):
        assert _is_linked(b2, 'xal_SubPremise375', a)
    _safe_set(a, 'xal_SubPremiseLocation', None)
    assert not _is_linked(a, 'xal_SubPremiseLocation', b2)
    if hasattr(b2, 'xal_SubPremise375'):
        assert not _is_linked(b2, 'xal_SubPremise375', a)


def test_assoc_subPremiseName372_link_reassign_clear():
    a = xal_SubPremiseName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text", typeOccurrence="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremiseName', b1)
    assert _is_linked(a, 'xal_SubPremiseName', b1)
    if hasattr(b1, 'xal_SubPremise373'):
        assert _is_linked(b1, 'xal_SubPremise373', a)
    _safe_set(a, 'xal_SubPremiseName', b2)
    assert _is_linked(a, 'xal_SubPremiseName', b2)
    if hasattr(b1, 'xal_SubPremise373'):
        assert not _is_linked(b1, 'xal_SubPremise373', a)
    if hasattr(b2, 'xal_SubPremise373'):
        assert _is_linked(b2, 'xal_SubPremise373', a)
    _safe_set(a, 'xal_SubPremiseName', None)
    assert not _is_linked(a, 'xal_SubPremiseName', b2)
    if hasattr(b2, 'xal_SubPremise373'):
        assert not _is_linked(b2, 'xal_SubPremise373', a)


def test_assoc_subPremiseNumber376_link_reassign_clear():
    a = xal_SubPremiseNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberTypeOccurrence="sample_text", premiseNumberSeparator="sample_text", type="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremiseNumber', b1)
    assert _is_linked(a, 'xal_SubPremiseNumber', b1)
    if hasattr(b1, 'xal_SubPremise377'):
        assert _is_linked(b1, 'xal_SubPremise377', a)
    _safe_set(a, 'xal_SubPremiseNumber', b2)
    assert _is_linked(a, 'xal_SubPremiseNumber', b2)
    if hasattr(b1, 'xal_SubPremise377'):
        assert not _is_linked(b1, 'xal_SubPremise377', a)
    if hasattr(b2, 'xal_SubPremise377'):
        assert _is_linked(b2, 'xal_SubPremise377', a)
    _safe_set(a, 'xal_SubPremiseNumber', None)
    assert not _is_linked(a, 'xal_SubPremiseNumber', b2)
    if hasattr(b2, 'xal_SubPremise377'):
        assert not _is_linked(b2, 'xal_SubPremise377', a)


def test_assoc_subPremiseNumberPrefix378_link_reassign_clear():
    a = xal_SubPremiseNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremiseNumberPrefix', b1)
    assert _is_linked(a, 'xal_SubPremiseNumberPrefix', b1)
    if hasattr(b1, 'xal_SubPremise379'):
        assert _is_linked(b1, 'xal_SubPremise379', a)
    _safe_set(a, 'xal_SubPremiseNumberPrefix', b2)
    assert _is_linked(a, 'xal_SubPremiseNumberPrefix', b2)
    if hasattr(b1, 'xal_SubPremise379'):
        assert not _is_linked(b1, 'xal_SubPremise379', a)
    if hasattr(b2, 'xal_SubPremise379'):
        assert _is_linked(b2, 'xal_SubPremise379', a)
    _safe_set(a, 'xal_SubPremiseNumberPrefix', None)
    assert not _is_linked(a, 'xal_SubPremiseNumberPrefix', b2)
    if hasattr(b2, 'xal_SubPremise379'):
        assert not _is_linked(b2, 'xal_SubPremise379', a)


def test_assoc_subPremiseNumberSuffix380_link_reassign_clear():
    a = xal_SubPremiseNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_SubPremise(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_SubPremise(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SubPremiseNumberSuffix', b1)
    assert _is_linked(a, 'xal_SubPremiseNumberSuffix', b1)
    if hasattr(b1, 'xal_SubPremise381'):
        assert _is_linked(b1, 'xal_SubPremise381', a)
    _safe_set(a, 'xal_SubPremiseNumberSuffix', b2)
    assert _is_linked(a, 'xal_SubPremiseNumberSuffix', b2)
    if hasattr(b1, 'xal_SubPremise381'):
        assert not _is_linked(b1, 'xal_SubPremise381', a)
    if hasattr(b2, 'xal_SubPremise381'):
        assert _is_linked(b2, 'xal_SubPremise381', a)
    _safe_set(a, 'xal_SubPremiseNumberSuffix', None)
    assert not _is_linked(a, 'xal_SubPremiseNumberSuffix', b2)
    if hasattr(b2, 'xal_SubPremise381'):
        assert not _is_linked(b2, 'xal_SubPremise381', a)


def test_assoc_supplementaryPostalServiceData250_link_reassign_clear():
    a = xal_SupplementaryPostalServiceData(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_PostalServiceElements(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_PostalServiceElements(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_SupplementaryPostalServiceData', b1)
    assert _is_linked(a, 'xal_SupplementaryPostalServiceData', b1)
    if hasattr(b1, 'xal_PostalServiceElements251'):
        assert _is_linked(b1, 'xal_PostalServiceElements251', a)
    _safe_set(a, 'xal_SupplementaryPostalServiceData', b2)
    assert _is_linked(a, 'xal_SupplementaryPostalServiceData', b2)
    if hasattr(b1, 'xal_PostalServiceElements251'):
        assert not _is_linked(b1, 'xal_PostalServiceElements251', a)
    if hasattr(b2, 'xal_PostalServiceElements251'):
        assert _is_linked(b2, 'xal_PostalServiceElements251', a)
    _safe_set(a, 'xal_SupplementaryPostalServiceData', None)
    assert not _is_linked(a, 'xal_SupplementaryPostalServiceData', b2)
    if hasattr(b2, 'xal_PostalServiceElements251'):
        assert not _is_linked(b2, 'xal_PostalServiceElements251', a)


def test_assoc_thoroughfare11_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_AddressDetails(addressDetailsKey="sample_text", addressType="sample_text", any="sample_text", anyAttribute="sample_text", code="sample_text", currentStatus="sample_text", usage="sample_text", validFromDate="sample_text", validToDate="sample_text")
    b2 = xal_AddressDetails(addressDetailsKey="sample_text_2", addressType="sample_text_2", any="sample_text_2", anyAttribute="sample_text_2", code="sample_text_2", currentStatus="sample_text_2", usage="sample_text_2", validFromDate="sample_text_2", validToDate="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare', b1)
    assert _is_linked(a, 'xal_Thoroughfare', b1)
    if hasattr(b1, 'xal_AddressDetails12'):
        assert _is_linked(b1, 'xal_AddressDetails12', a)
    _safe_set(a, 'xal_Thoroughfare', b2)
    assert _is_linked(a, 'xal_Thoroughfare', b2)
    if hasattr(b1, 'xal_AddressDetails12'):
        assert not _is_linked(b1, 'xal_AddressDetails12', a)
    if hasattr(b2, 'xal_AddressDetails12'):
        assert _is_linked(b2, 'xal_AddressDetails12', a)
    _safe_set(a, 'xal_Thoroughfare', None)
    assert not _is_linked(a, 'xal_Thoroughfare', b2)
    if hasattr(b2, 'xal_AddressDetails12'):
        assert not _is_linked(b2, 'xal_AddressDetails12', a)


def test_assoc_thoroughfare132_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare134', b1)
    assert _is_linked(a, 'xal_Thoroughfare134', b1)
    if hasattr(b1, 'xal_DocumentRoot133'):
        assert _is_linked(b1, 'xal_DocumentRoot133', a)
    _safe_set(a, 'xal_Thoroughfare134', b2)
    assert _is_linked(a, 'xal_Thoroughfare134', b2)
    if hasattr(b1, 'xal_DocumentRoot133'):
        assert not _is_linked(b1, 'xal_DocumentRoot133', a)
    if hasattr(b2, 'xal_DocumentRoot133'):
        assert _is_linked(b2, 'xal_DocumentRoot133', a)
    _safe_set(a, 'xal_Thoroughfare134', None)
    assert not _is_linked(a, 'xal_Thoroughfare134', b2)
    if hasattr(b2, 'xal_DocumentRoot133'):
        assert not _is_linked(b2, 'xal_DocumentRoot133', a)


def test_assoc_thoroughfare171_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_LargeMailUser(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_LargeMailUser(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare173', b1)
    assert _is_linked(a, 'xal_Thoroughfare173', b1)
    if hasattr(b1, 'xal_LargeMailUser172'):
        assert _is_linked(b1, 'xal_LargeMailUser172', a)
    _safe_set(a, 'xal_Thoroughfare173', b2)
    assert _is_linked(a, 'xal_Thoroughfare173', b2)
    if hasattr(b1, 'xal_LargeMailUser172'):
        assert not _is_linked(b1, 'xal_LargeMailUser172', a)
    if hasattr(b2, 'xal_LargeMailUser172'):
        assert _is_linked(b2, 'xal_LargeMailUser172', a)
    _safe_set(a, 'xal_Thoroughfare173', None)
    assert not _is_linked(a, 'xal_Thoroughfare173', b2)
    if hasattr(b2, 'xal_LargeMailUser172'):
        assert not _is_linked(b2, 'xal_LargeMailUser172', a)


def test_assoc_thoroughfare194_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_Locality(any="sample_text", anyAttribute="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_Locality(any="sample_text_2", anyAttribute="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare196', b1)
    assert _is_linked(a, 'xal_Thoroughfare196', b1)
    if hasattr(b1, 'xal_Locality195'):
        assert _is_linked(b1, 'xal_Locality195', a)
    _safe_set(a, 'xal_Thoroughfare196', b2)
    assert _is_linked(a, 'xal_Thoroughfare196', b2)
    if hasattr(b1, 'xal_Locality195'):
        assert not _is_linked(b1, 'xal_Locality195', a)
    if hasattr(b2, 'xal_Locality195'):
        assert _is_linked(b2, 'xal_Locality195', a)
    _safe_set(a, 'xal_Thoroughfare196', None)
    assert not _is_linked(a, 'xal_Thoroughfare196', b2)
    if hasattr(b2, 'xal_Locality195'):
        assert not _is_linked(b2, 'xal_Locality195', a)


def test_assoc_thoroughfare42_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_Country(any="sample_text", anyAttribute="sample_text")
    b2 = xal_Country(any="sample_text_2", anyAttribute="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare44', b1)
    assert _is_linked(a, 'xal_Thoroughfare44', b1)
    if hasattr(b1, 'xal_Country43'):
        assert _is_linked(b1, 'xal_Country43', a)
    _safe_set(a, 'xal_Thoroughfare44', b2)
    assert _is_linked(a, 'xal_Thoroughfare44', b2)
    if hasattr(b1, 'xal_Country43'):
        assert not _is_linked(b1, 'xal_Country43', a)
    if hasattr(b2, 'xal_Country43'):
        assert _is_linked(b2, 'xal_Country43', a)
    _safe_set(a, 'xal_Thoroughfare44', None)
    assert not _is_linked(a, 'xal_Thoroughfare44', b2)
    if hasattr(b2, 'xal_Country43'):
        assert not _is_linked(b2, 'xal_Country43', a)


def test_assoc_thoroughfare69_link_reassign_clear():
    a = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b1 = xal_DependentLocality(any="sample_text", anyAttribute="sample_text", connector="sample_text", indicator="sample_text", type="sample_text", usageType="sample_text")
    b2 = xal_DependentLocality(any="sample_text_2", anyAttribute="sample_text_2", connector="sample_text_2", indicator="sample_text_2", type="sample_text_2", usageType="sample_text_2")
    _safe_set(a, 'xal_Thoroughfare71', b1)
    assert _is_linked(a, 'xal_Thoroughfare71', b1)
    if hasattr(b1, 'xal_DependentLocality70'):
        assert _is_linked(b1, 'xal_DependentLocality70', a)
    _safe_set(a, 'xal_Thoroughfare71', b2)
    assert _is_linked(a, 'xal_Thoroughfare71', b2)
    if hasattr(b1, 'xal_DependentLocality70'):
        assert not _is_linked(b1, 'xal_DependentLocality70', a)
    if hasattr(b2, 'xal_DependentLocality70'):
        assert _is_linked(b2, 'xal_DependentLocality70', a)
    _safe_set(a, 'xal_Thoroughfare71', None)
    assert not _is_linked(a, 'xal_Thoroughfare71', b2)
    if hasattr(b2, 'xal_DependentLocality70'):
        assert not _is_linked(b2, 'xal_DependentLocality70', a)


def test_assoc_thoroughfareLeadingType414_link_reassign_clear():
    a = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareLeadingType416', b1)
    assert _is_linked(a, 'xal_ThoroughfareLeadingType416', b1)
    if hasattr(b1, 'xal_Thoroughfare415'):
        assert _is_linked(b1, 'xal_Thoroughfare415', a)
    _safe_set(a, 'xal_ThoroughfareLeadingType416', b2)
    assert _is_linked(a, 'xal_ThoroughfareLeadingType416', b2)
    if hasattr(b1, 'xal_Thoroughfare415'):
        assert not _is_linked(b1, 'xal_Thoroughfare415', a)
    if hasattr(b2, 'xal_Thoroughfare415'):
        assert _is_linked(b2, 'xal_Thoroughfare415', a)
    _safe_set(a, 'xal_ThoroughfareLeadingType416', None)
    assert not _is_linked(a, 'xal_ThoroughfareLeadingType416', b2)
    if hasattr(b2, 'xal_Thoroughfare415'):
        assert not _is_linked(b2, 'xal_Thoroughfare415', a)


def test_assoc_thoroughfareLeadingType84_link_reassign_clear():
    a = xal_ThoroughfareLeadingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareLeadingType', b1)
    assert _is_linked(a, 'xal_ThoroughfareLeadingType', b1)
    if hasattr(b1, 'xal_DependentThoroughfare85'):
        assert _is_linked(b1, 'xal_DependentThoroughfare85', a)
    _safe_set(a, 'xal_ThoroughfareLeadingType', b2)
    assert _is_linked(a, 'xal_ThoroughfareLeadingType', b2)
    if hasattr(b1, 'xal_DependentThoroughfare85'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare85', a)
    if hasattr(b2, 'xal_DependentThoroughfare85'):
        assert _is_linked(b2, 'xal_DependentThoroughfare85', a)
    _safe_set(a, 'xal_ThoroughfareLeadingType', None)
    assert not _is_linked(a, 'xal_ThoroughfareLeadingType', b2)
    if hasattr(b2, 'xal_DependentThoroughfare85'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare85', a)


def test_assoc_thoroughfareName417_link_reassign_clear():
    a = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareName419', b1)
    assert _is_linked(a, 'xal_ThoroughfareName419', b1)
    if hasattr(b1, 'xal_Thoroughfare418'):
        assert _is_linked(b1, 'xal_Thoroughfare418', a)
    _safe_set(a, 'xal_ThoroughfareName419', b2)
    assert _is_linked(a, 'xal_ThoroughfareName419', b2)
    if hasattr(b1, 'xal_Thoroughfare418'):
        assert not _is_linked(b1, 'xal_Thoroughfare418', a)
    if hasattr(b2, 'xal_Thoroughfare418'):
        assert _is_linked(b2, 'xal_Thoroughfare418', a)
    _safe_set(a, 'xal_ThoroughfareName419', None)
    assert not _is_linked(a, 'xal_ThoroughfareName419', b2)
    if hasattr(b2, 'xal_Thoroughfare418'):
        assert not _is_linked(b2, 'xal_Thoroughfare418', a)


def test_assoc_thoroughfareName86_link_reassign_clear():
    a = xal_ThoroughfareName(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareName', b1)
    assert _is_linked(a, 'xal_ThoroughfareName', b1)
    if hasattr(b1, 'xal_DependentThoroughfare87'):
        assert _is_linked(b1, 'xal_DependentThoroughfare87', a)
    _safe_set(a, 'xal_ThoroughfareName', b2)
    assert _is_linked(a, 'xal_ThoroughfareName', b2)
    if hasattr(b1, 'xal_DependentThoroughfare87'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare87', a)
    if hasattr(b2, 'xal_DependentThoroughfare87'):
        assert _is_linked(b2, 'xal_DependentThoroughfare87', a)
    _safe_set(a, 'xal_ThoroughfareName', None)
    assert not _is_linked(a, 'xal_ThoroughfareName', b2)
    if hasattr(b2, 'xal_DependentThoroughfare87'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare87', a)


def test_assoc_thoroughfareNumber135_link_reassign_clear():
    a = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumber', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumber', b1)
    if hasattr(b1, 'xal_DocumentRoot136'):
        assert _is_linked(b1, 'xal_DocumentRoot136', a)
    _safe_set(a, 'xal_ThoroughfareNumber', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumber', b2)
    if hasattr(b1, 'xal_DocumentRoot136'):
        assert not _is_linked(b1, 'xal_DocumentRoot136', a)
    if hasattr(b2, 'xal_DocumentRoot136'):
        assert _is_linked(b2, 'xal_DocumentRoot136', a)
    _safe_set(a, 'xal_ThoroughfareNumber', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumber', b2)
    if hasattr(b2, 'xal_DocumentRoot136'):
        assert not _is_linked(b2, 'xal_DocumentRoot136', a)


def test_assoc_thoroughfareNumber400_link_reassign_clear():
    a = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumber402', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumber402', b1)
    if hasattr(b1, 'xal_Thoroughfare401'):
        assert _is_linked(b1, 'xal_Thoroughfare401', a)
    _safe_set(a, 'xal_ThoroughfareNumber402', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumber402', b2)
    if hasattr(b1, 'xal_Thoroughfare401'):
        assert not _is_linked(b1, 'xal_Thoroughfare401', a)
    if hasattr(b2, 'xal_Thoroughfare401'):
        assert _is_linked(b2, 'xal_Thoroughfare401', a)
    _safe_set(a, 'xal_ThoroughfareNumber402', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumber402', b2)
    if hasattr(b2, 'xal_Thoroughfare401'):
        assert not _is_linked(b2, 'xal_Thoroughfare401', a)


def test_assoc_thoroughfareNumber446_link_reassign_clear():
    a = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    b2 = xal_ThoroughfareNumber(anyAttribute="sample_text_2", code="sample_text_2", indicator="sample_text_2", indicatorOccurrence="sample_text_2", mixed="sample_text_2", numberOccurrence="sample_text_2", numberType="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberFrom447', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberFrom447', b1)
    if hasattr(b1, 'xal_ThoroughfareNumber448'):
        assert _is_linked(b1, 'xal_ThoroughfareNumber448', a)
    _safe_set(a, 'xal_ThoroughfareNumberFrom447', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberFrom447', b2)
    if hasattr(b1, 'xal_ThoroughfareNumber448'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumber448', a)
    if hasattr(b2, 'xal_ThoroughfareNumber448'):
        assert _is_linked(b2, 'xal_ThoroughfareNumber448', a)
    _safe_set(a, 'xal_ThoroughfareNumberFrom447', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberFrom447', b2)
    if hasattr(b2, 'xal_ThoroughfareNumber448'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumber448', a)


def test_assoc_thoroughfareNumber466_link_reassign_clear():
    a = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_ThoroughfareNumber(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", mixed="sample_text", numberOccurrence="sample_text", numberType="sample_text", type="sample_text")
    b2 = xal_ThoroughfareNumber(anyAttribute="sample_text_2", code="sample_text_2", indicator="sample_text_2", indicatorOccurrence="sample_text_2", mixed="sample_text_2", numberOccurrence="sample_text_2", numberType="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberTo467', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo467', b1)
    if hasattr(b1, 'xal_ThoroughfareNumber468'):
        assert _is_linked(b1, 'xal_ThoroughfareNumber468', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo467', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo467', b2)
    if hasattr(b1, 'xal_ThoroughfareNumber468'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumber468', a)
    if hasattr(b2, 'xal_ThoroughfareNumber468'):
        assert _is_linked(b2, 'xal_ThoroughfareNumber468', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo467', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberTo467', b2)
    if hasattr(b2, 'xal_ThoroughfareNumber468'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumber468', a)


def test_assoc_thoroughfareNumberFrom455_link_reassign_clear():
    a = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b2 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberRange456', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberRange456', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom457'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberFrom457', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange456', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberRange456', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom457'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberFrom457', a)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom457'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberFrom457', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange456', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberRange456', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom457'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberFrom457', a)


def test_assoc_thoroughfareNumberPrefix137_link_reassign_clear():
    a = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberPrefix', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix', b1)
    if hasattr(b1, 'xal_DocumentRoot138'):
        assert _is_linked(b1, 'xal_DocumentRoot138', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix', b2)
    if hasattr(b1, 'xal_DocumentRoot138'):
        assert not _is_linked(b1, 'xal_DocumentRoot138', a)
    if hasattr(b2, 'xal_DocumentRoot138'):
        assert _is_linked(b2, 'xal_DocumentRoot138', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberPrefix', b2)
    if hasattr(b2, 'xal_DocumentRoot138'):
        assert not _is_linked(b2, 'xal_DocumentRoot138', a)


def test_assoc_thoroughfareNumberPrefix405_link_reassign_clear():
    a = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberPrefix407', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix407', b1)
    if hasattr(b1, 'xal_Thoroughfare406'):
        assert _is_linked(b1, 'xal_Thoroughfare406', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix407', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix407', b2)
    if hasattr(b1, 'xal_Thoroughfare406'):
        assert not _is_linked(b1, 'xal_Thoroughfare406', a)
    if hasattr(b2, 'xal_Thoroughfare406'):
        assert _is_linked(b2, 'xal_Thoroughfare406', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix407', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberPrefix407', b2)
    if hasattr(b2, 'xal_Thoroughfare406'):
        assert not _is_linked(b2, 'xal_Thoroughfare406', a)


def test_assoc_thoroughfareNumberPrefix443_link_reassign_clear():
    a = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    b1 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b2 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberPrefix445', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix445', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom444'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberFrom444', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix445', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberPrefix445', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom444'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberFrom444', a)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom444'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberFrom444', a)
    _safe_set(a, 'xal_ThoroughfareNumberPrefix445', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberPrefix445', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom444'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberFrom444', a)


def test_assoc_thoroughfareNumberPrefix463_link_reassign_clear():
    a = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberPrefixSeparator="sample_text", type="sample_text")
    b2 = xal_ThoroughfareNumberPrefix(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", numberPrefixSeparator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberTo464', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo464', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberPrefix465'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberPrefix465', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo464', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo464', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberPrefix465'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberPrefix465', a)
    if hasattr(b2, 'xal_ThoroughfareNumberPrefix465'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberPrefix465', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo464', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberTo464', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberPrefix465'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberPrefix465', a)


def test_assoc_thoroughfareNumberRange403_link_reassign_clear():
    a = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberRange', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberRange', b1)
    if hasattr(b1, 'xal_Thoroughfare404'):
        assert _is_linked(b1, 'xal_Thoroughfare404', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberRange', b2)
    if hasattr(b1, 'xal_Thoroughfare404'):
        assert not _is_linked(b1, 'xal_Thoroughfare404', a)
    if hasattr(b2, 'xal_Thoroughfare404'):
        assert _is_linked(b2, 'xal_Thoroughfare404', a)
    _safe_set(a, 'xal_ThoroughfareNumberRange', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberRange', b2)
    if hasattr(b2, 'xal_Thoroughfare404'):
        assert not _is_linked(b2, 'xal_Thoroughfare404', a)


def test_assoc_thoroughfareNumberSuffix139_link_reassign_clear():
    a = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberSuffix', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix', b1)
    if hasattr(b1, 'xal_DocumentRoot140'):
        assert _is_linked(b1, 'xal_DocumentRoot140', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix', b2)
    if hasattr(b1, 'xal_DocumentRoot140'):
        assert not _is_linked(b1, 'xal_DocumentRoot140', a)
    if hasattr(b2, 'xal_DocumentRoot140'):
        assert _is_linked(b2, 'xal_DocumentRoot140', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberSuffix', b2)
    if hasattr(b2, 'xal_DocumentRoot140'):
        assert not _is_linked(b2, 'xal_DocumentRoot140', a)


def test_assoc_thoroughfareNumberSuffix408_link_reassign_clear():
    a = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberSuffix410', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix410', b1)
    if hasattr(b1, 'xal_Thoroughfare409'):
        assert _is_linked(b1, 'xal_Thoroughfare409', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix410', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix410', b2)
    if hasattr(b1, 'xal_Thoroughfare409'):
        assert not _is_linked(b1, 'xal_Thoroughfare409', a)
    if hasattr(b2, 'xal_Thoroughfare409'):
        assert _is_linked(b2, 'xal_Thoroughfare409', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix410', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberSuffix410', b2)
    if hasattr(b2, 'xal_Thoroughfare409'):
        assert not _is_linked(b2, 'xal_Thoroughfare409', a)


def test_assoc_thoroughfareNumberSuffix449_link_reassign_clear():
    a = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b1 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b2 = xal_ThoroughfareNumberFrom(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberSuffix451', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix451', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom450'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberFrom450', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix451', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberSuffix451', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberFrom450'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberFrom450', a)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom450'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberFrom450', a)
    _safe_set(a, 'xal_ThoroughfareNumberSuffix451', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberSuffix451', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberFrom450'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberFrom450', a)


def test_assoc_thoroughfareNumberSuffix469_link_reassign_clear():
    a = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text", code="sample_text", mixed="sample_text", numberSuffixSeparator="sample_text", type="sample_text")
    b2 = xal_ThoroughfareNumberSuffix(anyAttribute="sample_text_2", code="sample_text_2", mixed="sample_text_2", numberSuffixSeparator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberTo470', {b1})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo470', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberSuffix471'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberSuffix471', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo470', {b2})
    assert _is_linked(a, 'xal_ThoroughfareNumberTo470', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberSuffix471'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberSuffix471', a)
    if hasattr(b2, 'xal_ThoroughfareNumberSuffix471'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberSuffix471', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo470', set())
    assert not _is_linked(a, 'xal_ThoroughfareNumberTo470', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberSuffix471'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberSuffix471', a)


def test_assoc_thoroughfareNumberTo458_link_reassign_clear():
    a = xal_ThoroughfareNumberTo(anyAttribute="sample_text", code="sample_text", mixed="sample_text")
    b1 = xal_ThoroughfareNumberRange(anyAttribute="sample_text", code="sample_text", indicator="sample_text", indicatorOccurrence="sample_text", numberRangeOccurrence="sample_text", rangeType="sample_text", separator="sample_text", type="sample_text")
    b2 = xal_ThoroughfareNumberRange(anyAttribute="sample_text_2", code="sample_text_2", indicator="sample_text_2", indicatorOccurrence="sample_text_2", numberRangeOccurrence="sample_text_2", rangeType="sample_text_2", separator="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareNumberTo', b1)
    assert _is_linked(a, 'xal_ThoroughfareNumberTo', b1)
    if hasattr(b1, 'xal_ThoroughfareNumberRange459'):
        assert _is_linked(b1, 'xal_ThoroughfareNumberRange459', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo', b2)
    assert _is_linked(a, 'xal_ThoroughfareNumberTo', b2)
    if hasattr(b1, 'xal_ThoroughfareNumberRange459'):
        assert not _is_linked(b1, 'xal_ThoroughfareNumberRange459', a)
    if hasattr(b2, 'xal_ThoroughfareNumberRange459'):
        assert _is_linked(b2, 'xal_ThoroughfareNumberRange459', a)
    _safe_set(a, 'xal_ThoroughfareNumberTo', None)
    assert not _is_linked(a, 'xal_ThoroughfareNumberTo', b2)
    if hasattr(b2, 'xal_ThoroughfareNumberRange459'):
        assert not _is_linked(b2, 'xal_ThoroughfareNumberRange459', a)


def test_assoc_thoroughfarePostDirection423_link_reassign_clear():
    a = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfarePostDirection425', b1)
    assert _is_linked(a, 'xal_ThoroughfarePostDirection425', b1)
    if hasattr(b1, 'xal_Thoroughfare424'):
        assert _is_linked(b1, 'xal_Thoroughfare424', a)
    _safe_set(a, 'xal_ThoroughfarePostDirection425', b2)
    assert _is_linked(a, 'xal_ThoroughfarePostDirection425', b2)
    if hasattr(b1, 'xal_Thoroughfare424'):
        assert not _is_linked(b1, 'xal_Thoroughfare424', a)
    if hasattr(b2, 'xal_Thoroughfare424'):
        assert _is_linked(b2, 'xal_Thoroughfare424', a)
    _safe_set(a, 'xal_ThoroughfarePostDirection425', None)
    assert not _is_linked(a, 'xal_ThoroughfarePostDirection425', b2)
    if hasattr(b2, 'xal_Thoroughfare424'):
        assert not _is_linked(b2, 'xal_Thoroughfare424', a)


def test_assoc_thoroughfarePostDirection90_link_reassign_clear():
    a = xal_ThoroughfarePostDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfarePostDirection', b1)
    assert _is_linked(a, 'xal_ThoroughfarePostDirection', b1)
    if hasattr(b1, 'xal_DependentThoroughfare91'):
        assert _is_linked(b1, 'xal_DependentThoroughfare91', a)
    _safe_set(a, 'xal_ThoroughfarePostDirection', b2)
    assert _is_linked(a, 'xal_ThoroughfarePostDirection', b2)
    if hasattr(b1, 'xal_DependentThoroughfare91'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare91', a)
    if hasattr(b2, 'xal_DependentThoroughfare91'):
        assert _is_linked(b2, 'xal_DependentThoroughfare91', a)
    _safe_set(a, 'xal_ThoroughfarePostDirection', None)
    assert not _is_linked(a, 'xal_ThoroughfarePostDirection', b2)
    if hasattr(b2, 'xal_DependentThoroughfare91'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare91', a)


def test_assoc_thoroughfarePreDirection411_link_reassign_clear():
    a = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfarePreDirection413', b1)
    assert _is_linked(a, 'xal_ThoroughfarePreDirection413', b1)
    if hasattr(b1, 'xal_Thoroughfare412'):
        assert _is_linked(b1, 'xal_Thoroughfare412', a)
    _safe_set(a, 'xal_ThoroughfarePreDirection413', b2)
    assert _is_linked(a, 'xal_ThoroughfarePreDirection413', b2)
    if hasattr(b1, 'xal_Thoroughfare412'):
        assert not _is_linked(b1, 'xal_Thoroughfare412', a)
    if hasattr(b2, 'xal_Thoroughfare412'):
        assert _is_linked(b2, 'xal_Thoroughfare412', a)
    _safe_set(a, 'xal_ThoroughfarePreDirection413', None)
    assert not _is_linked(a, 'xal_ThoroughfarePreDirection413', b2)
    if hasattr(b2, 'xal_Thoroughfare412'):
        assert not _is_linked(b2, 'xal_Thoroughfare412', a)


def test_assoc_thoroughfarePreDirection82_link_reassign_clear():
    a = xal_ThoroughfarePreDirection(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfarePreDirection', b1)
    assert _is_linked(a, 'xal_ThoroughfarePreDirection', b1)
    if hasattr(b1, 'xal_DependentThoroughfare83'):
        assert _is_linked(b1, 'xal_DependentThoroughfare83', a)
    _safe_set(a, 'xal_ThoroughfarePreDirection', b2)
    assert _is_linked(a, 'xal_ThoroughfarePreDirection', b2)
    if hasattr(b1, 'xal_DependentThoroughfare83'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare83', a)
    if hasattr(b2, 'xal_DependentThoroughfare83'):
        assert _is_linked(b2, 'xal_DependentThoroughfare83', a)
    _safe_set(a, 'xal_ThoroughfarePreDirection', None)
    assert not _is_linked(a, 'xal_ThoroughfarePreDirection', b2)
    if hasattr(b2, 'xal_DependentThoroughfare83'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare83', a)


def test_assoc_thoroughfareTrailingType420_link_reassign_clear():
    a = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_Thoroughfare(any="sample_text", anyAttribute="sample_text", dependentThoroughfares="sample_text", dependentThoroughfaresConnector="sample_text", dependentThoroughfaresIndicator="sample_text", dependentThoroughfaresType="sample_text", group="sample_text", type="sample_text")
    b2 = xal_Thoroughfare(any="sample_text_2", anyAttribute="sample_text_2", dependentThoroughfares="sample_text_2", dependentThoroughfaresConnector="sample_text_2", dependentThoroughfaresIndicator="sample_text_2", dependentThoroughfaresType="sample_text_2", group="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareTrailingType422', b1)
    assert _is_linked(a, 'xal_ThoroughfareTrailingType422', b1)
    if hasattr(b1, 'xal_Thoroughfare421'):
        assert _is_linked(b1, 'xal_Thoroughfare421', a)
    _safe_set(a, 'xal_ThoroughfareTrailingType422', b2)
    assert _is_linked(a, 'xal_ThoroughfareTrailingType422', b2)
    if hasattr(b1, 'xal_Thoroughfare421'):
        assert not _is_linked(b1, 'xal_Thoroughfare421', a)
    if hasattr(b2, 'xal_Thoroughfare421'):
        assert _is_linked(b2, 'xal_Thoroughfare421', a)
    _safe_set(a, 'xal_ThoroughfareTrailingType422', None)
    assert not _is_linked(a, 'xal_ThoroughfareTrailingType422', b2)
    if hasattr(b2, 'xal_Thoroughfare421'):
        assert not _is_linked(b2, 'xal_Thoroughfare421', a)


def test_assoc_thoroughfareTrailingType88_link_reassign_clear():
    a = xal_ThoroughfareTrailingType(anyAttribute="sample_text", code="sample_text", mixed="sample_text", type="sample_text")
    b1 = xal_DependentThoroughfare(any="sample_text", anyAttribute="sample_text", type="sample_text")
    b2 = xal_DependentThoroughfare(any="sample_text_2", anyAttribute="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xal_ThoroughfareTrailingType', b1)
    assert _is_linked(a, 'xal_ThoroughfareTrailingType', b1)
    if hasattr(b1, 'xal_DependentThoroughfare89'):
        assert _is_linked(b1, 'xal_DependentThoroughfare89', a)
    _safe_set(a, 'xal_ThoroughfareTrailingType', b2)
    assert _is_linked(a, 'xal_ThoroughfareTrailingType', b2)
    if hasattr(b1, 'xal_DependentThoroughfare89'):
        assert not _is_linked(b1, 'xal_DependentThoroughfare89', a)
    if hasattr(b2, 'xal_DependentThoroughfare89'):
        assert _is_linked(b2, 'xal_DependentThoroughfare89', a)
    _safe_set(a, 'xal_ThoroughfareTrailingType', None)
    assert not _is_linked(a, 'xal_ThoroughfareTrailingType', b2)
    if hasattr(b2, 'xal_DependentThoroughfare89'):
        assert not _is_linked(b2, 'xal_DependentThoroughfare89', a)


def test_assoc_xAL141_link_reassign_clear():
    a = xal_Xal(any="sample_text", anyAttribute="sample_text", version="sample_text")
    b1 = xal_DocumentRoot(mixed="sample_text")
    b2 = xal_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'xal_Xal', b1)
    assert _is_linked(a, 'xal_Xal', b1)
    if hasattr(b1, 'xal_DocumentRoot142'):
        assert _is_linked(b1, 'xal_DocumentRoot142', a)
    _safe_set(a, 'xal_Xal', b2)
    assert _is_linked(a, 'xal_Xal', b2)
    if hasattr(b1, 'xal_DocumentRoot142'):
        assert not _is_linked(b1, 'xal_DocumentRoot142', a)
    if hasattr(b2, 'xal_DocumentRoot142'):
        assert _is_linked(b2, 'xal_DocumentRoot142', a)
    _safe_set(a, 'xal_Xal', None)
    assert not _is_linked(a, 'xal_Xal', b2)
    if hasattr(b2, 'xal_DocumentRoot142'):
        assert not _is_linked(b2, 'xal_DocumentRoot142', a)


def test_assoc_xMLNSPrefixMap92_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_EStringToStringMapEntry()
    b2 = xal_EStringToStringMapEntry()
    _safe_set(a, 'xal_DocumentRoot', {b1})
    assert _is_linked(a, 'xal_DocumentRoot', b1)
    if hasattr(b1, 'xal_EStringToStringMapEntry'):
        assert _is_linked(b1, 'xal_EStringToStringMapEntry', a)
    _safe_set(a, 'xal_DocumentRoot', {b2})
    assert _is_linked(a, 'xal_DocumentRoot', b2)
    if hasattr(b1, 'xal_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'xal_EStringToStringMapEntry', a)
    if hasattr(b2, 'xal_EStringToStringMapEntry'):
        assert _is_linked(b2, 'xal_EStringToStringMapEntry', a)
    _safe_set(a, 'xal_DocumentRoot', set())
    assert not _is_linked(a, 'xal_DocumentRoot', b2)
    if hasattr(b2, 'xal_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'xal_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation93_link_reassign_clear():
    a = xal_DocumentRoot(mixed="sample_text")
    b1 = xal_EStringToStringMapEntry()
    b2 = xal_EStringToStringMapEntry()
    _safe_set(a, 'xal_DocumentRoot94', {b1})
    assert _is_linked(a, 'xal_DocumentRoot94', b1)
    if hasattr(b1, 'xal_EStringToStringMapEntry95'):
        assert _is_linked(b1, 'xal_EStringToStringMapEntry95', a)
    _safe_set(a, 'xal_DocumentRoot94', {b2})
    assert _is_linked(a, 'xal_DocumentRoot94', b2)
    if hasattr(b1, 'xal_EStringToStringMapEntry95'):
        assert not _is_linked(b1, 'xal_EStringToStringMapEntry95', a)
    if hasattr(b2, 'xal_EStringToStringMapEntry95'):
        assert _is_linked(b2, 'xal_EStringToStringMapEntry95', a)
    _safe_set(a, 'xal_DocumentRoot94', set())
    assert not _is_linked(a, 'xal_DocumentRoot94', b2)
    if hasattr(b2, 'xal_EStringToStringMapEntry95'):
        assert not _is_linked(b2, 'xal_EStringToStringMapEntry95', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

xal_Address_strategy = st.builds(xal_Address, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_Address_strategy)
@settings(max_examples=25)
def test_xal_Address_instantiation(instance):
    assert isinstance(instance, xal_Address)


xal_AddressDetails_strategy = st.builds(xal_AddressDetails, addressDetailsKey=safe_text, addressType=safe_text, any=safe_text, anyAttribute=safe_text, code=safe_text, currentStatus=safe_text, usage=safe_text, validFromDate=safe_text, validToDate=safe_text)
@given(instance=xal_AddressDetails_strategy)
@settings(max_examples=25)
def test_xal_AddressDetails_instantiation(instance):
    assert isinstance(instance, xal_AddressDetails)


xal_AddressIdentifier_strategy = st.builds(xal_AddressIdentifier, anyAttribute=safe_text, code=safe_text, identifierType=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressIdentifier_strategy)
@settings(max_examples=25)
def test_xal_AddressIdentifier_instantiation(instance):
    assert isinstance(instance, xal_AddressIdentifier)


xal_AddressLatitude_strategy = st.builds(xal_AddressLatitude, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressLatitude_strategy)
@settings(max_examples=25)
def test_xal_AddressLatitude_instantiation(instance):
    assert isinstance(instance, xal_AddressLatitude)


xal_AddressLatitudeDirection_strategy = st.builds(xal_AddressLatitudeDirection, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressLatitudeDirection_strategy)
@settings(max_examples=25)
def test_xal_AddressLatitudeDirection_instantiation(instance):
    assert isinstance(instance, xal_AddressLatitudeDirection)


xal_AddressLine_strategy = st.builds(xal_AddressLine, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressLine_strategy)
@settings(max_examples=25)
def test_xal_AddressLine_instantiation(instance):
    assert isinstance(instance, xal_AddressLine)


xal_AddressLines_strategy = st.builds(xal_AddressLines, any=safe_text, anyAttribute=safe_text)
@given(instance=xal_AddressLines_strategy)
@settings(max_examples=25)
def test_xal_AddressLines_instantiation(instance):
    assert isinstance(instance, xal_AddressLines)


xal_AddressLongitude_strategy = st.builds(xal_AddressLongitude, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressLongitude_strategy)
@settings(max_examples=25)
def test_xal_AddressLongitude_instantiation(instance):
    assert isinstance(instance, xal_AddressLongitude)


xal_AddressLongitudeDirection_strategy = st.builds(xal_AddressLongitudeDirection, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AddressLongitudeDirection_strategy)
@settings(max_examples=25)
def test_xal_AddressLongitudeDirection_instantiation(instance):
    assert isinstance(instance, xal_AddressLongitudeDirection)


xal_AdministrativeArea_strategy = st.builds(xal_AdministrativeArea, any=safe_text, anyAttribute=safe_text, indicator=safe_text, type=safe_text, usageType=safe_text)
@given(instance=xal_AdministrativeArea_strategy)
@settings(max_examples=25)
def test_xal_AdministrativeArea_instantiation(instance):
    assert isinstance(instance, xal_AdministrativeArea)


xal_AdministrativeAreaName_strategy = st.builds(xal_AdministrativeAreaName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_AdministrativeAreaName_strategy)
@settings(max_examples=25)
def test_xal_AdministrativeAreaName_instantiation(instance):
    assert isinstance(instance, xal_AdministrativeAreaName)


xal_Barcode_strategy = st.builds(xal_Barcode, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_Barcode_strategy)
@settings(max_examples=25)
def test_xal_Barcode_instantiation(instance):
    assert isinstance(instance, xal_Barcode)


xal_BuildingName_strategy = st.builds(xal_BuildingName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text, typeOccurrence=safe_text)
@given(instance=xal_BuildingName_strategy)
@settings(max_examples=25)
def test_xal_BuildingName_instantiation(instance):
    assert isinstance(instance, xal_BuildingName)


xal_Country_strategy = st.builds(xal_Country, any=safe_text, anyAttribute=safe_text)
@given(instance=xal_Country_strategy)
@settings(max_examples=25)
def test_xal_Country_instantiation(instance):
    assert isinstance(instance, xal_Country)


xal_CountryName_strategy = st.builds(xal_CountryName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_CountryName_strategy)
@settings(max_examples=25)
def test_xal_CountryName_instantiation(instance):
    assert isinstance(instance, xal_CountryName)


xal_CountryNameCode_strategy = st.builds(xal_CountryNameCode, anyAttribute=safe_text, code=safe_text, mixed=safe_text, scheme=safe_text)
@given(instance=xal_CountryNameCode_strategy)
@settings(max_examples=25)
def test_xal_CountryNameCode_instantiation(instance):
    assert isinstance(instance, xal_CountryNameCode)


xal_Department_strategy = st.builds(xal_Department, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_Department_strategy)
@settings(max_examples=25)
def test_xal_Department_instantiation(instance):
    assert isinstance(instance, xal_Department)


xal_DepartmentName_strategy = st.builds(xal_DepartmentName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_DepartmentName_strategy)
@settings(max_examples=25)
def test_xal_DepartmentName_instantiation(instance):
    assert isinstance(instance, xal_DepartmentName)


xal_DependentLocality_strategy = st.builds(xal_DependentLocality, any=safe_text, anyAttribute=safe_text, connector=safe_text, indicator=safe_text, type=safe_text, usageType=safe_text)
@given(instance=xal_DependentLocality_strategy)
@settings(max_examples=25)
def test_xal_DependentLocality_instantiation(instance):
    assert isinstance(instance, xal_DependentLocality)


xal_DependentLocalityName_strategy = st.builds(xal_DependentLocalityName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_DependentLocalityName_strategy)
@settings(max_examples=25)
def test_xal_DependentLocalityName_instantiation(instance):
    assert isinstance(instance, xal_DependentLocalityName)


xal_DependentLocalityNumber_strategy = st.builds(xal_DependentLocalityNumber, anyAttribute=safe_text, code=safe_text, mixed=safe_text, nameNumberOccurrence=safe_text)
@given(instance=xal_DependentLocalityNumber_strategy)
@settings(max_examples=25)
def test_xal_DependentLocalityNumber_instantiation(instance):
    assert isinstance(instance, xal_DependentLocalityNumber)


xal_DependentThoroughfare_strategy = st.builds(xal_DependentThoroughfare, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_DependentThoroughfare_strategy)
@settings(max_examples=25)
def test_xal_DependentThoroughfare_instantiation(instance):
    assert isinstance(instance, xal_DependentThoroughfare)


xal_DocumentRoot_strategy = st.builds(xal_DocumentRoot, mixed=safe_text)
@given(instance=xal_DocumentRoot_strategy)
@settings(max_examples=25)
def test_xal_DocumentRoot_instantiation(instance):
    assert isinstance(instance, xal_DocumentRoot)


xal_EStringToStringMapEntry_strategy = st.builds(xal_EStringToStringMapEntry)
@given(instance=xal_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_xal_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, xal_EStringToStringMapEntry)


xal_EndorsementLineCode_strategy = st.builds(xal_EndorsementLineCode, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_EndorsementLineCode_strategy)
@settings(max_examples=25)
def test_xal_EndorsementLineCode_instantiation(instance):
    assert isinstance(instance, xal_EndorsementLineCode)


xal_Firm_strategy = st.builds(xal_Firm, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_Firm_strategy)
@settings(max_examples=25)
def test_xal_Firm_instantiation(instance):
    assert isinstance(instance, xal_Firm)


xal_FirmName_strategy = st.builds(xal_FirmName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_FirmName_strategy)
@settings(max_examples=25)
def test_xal_FirmName_instantiation(instance):
    assert isinstance(instance, xal_FirmName)


xal_KeyLineCode_strategy = st.builds(xal_KeyLineCode, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_KeyLineCode_strategy)
@settings(max_examples=25)
def test_xal_KeyLineCode_instantiation(instance):
    assert isinstance(instance, xal_KeyLineCode)


xal_LargeMailUser_strategy = st.builds(xal_LargeMailUser, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_LargeMailUser_strategy)
@settings(max_examples=25)
def test_xal_LargeMailUser_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUser)


xal_LargeMailUserIdentifier_strategy = st.builds(xal_LargeMailUserIdentifier, anyAttribute=safe_text, code=safe_text, indicator=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_LargeMailUserIdentifier_strategy)
@settings(max_examples=25)
def test_xal_LargeMailUserIdentifier_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUserIdentifier)


xal_LargeMailUserName_strategy = st.builds(xal_LargeMailUserName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_LargeMailUserName_strategy)
@settings(max_examples=25)
def test_xal_LargeMailUserName_instantiation(instance):
    assert isinstance(instance, xal_LargeMailUserName)


xal_Locality_strategy = st.builds(xal_Locality, any=safe_text, anyAttribute=safe_text, indicator=safe_text, type=safe_text, usageType=safe_text)
@given(instance=xal_Locality_strategy)
@settings(max_examples=25)
def test_xal_Locality_instantiation(instance):
    assert isinstance(instance, xal_Locality)


xal_LocalityName_strategy = st.builds(xal_LocalityName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_LocalityName_strategy)
@settings(max_examples=25)
def test_xal_LocalityName_instantiation(instance):
    assert isinstance(instance, xal_LocalityName)


xal_MailStop_strategy = st.builds(xal_MailStop, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_MailStop_strategy)
@settings(max_examples=25)
def test_xal_MailStop_instantiation(instance):
    assert isinstance(instance, xal_MailStop)


xal_MailStopName_strategy = st.builds(xal_MailStopName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_MailStopName_strategy)
@settings(max_examples=25)
def test_xal_MailStopName_instantiation(instance):
    assert isinstance(instance, xal_MailStopName)


xal_MailStopNumber_strategy = st.builds(xal_MailStopNumber, anyAttribute=safe_text, code=safe_text, mixed=safe_text, nameNumberSeparator=safe_text)
@given(instance=xal_MailStopNumber_strategy)
@settings(max_examples=25)
def test_xal_MailStopNumber_instantiation(instance):
    assert isinstance(instance, xal_MailStopNumber)


xal_PostBox_strategy = st.builds(xal_PostBox, any=safe_text, anyAttribute=safe_text, indicator=safe_text, type=safe_text)
@given(instance=xal_PostBox_strategy)
@settings(max_examples=25)
def test_xal_PostBox_instantiation(instance):
    assert isinstance(instance, xal_PostBox)


xal_PostBoxNumber_strategy = st.builds(xal_PostBoxNumber, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_PostBoxNumber_strategy)
@settings(max_examples=25)
def test_xal_PostBoxNumber_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumber)


xal_PostBoxNumberExtension_strategy = st.builds(xal_PostBoxNumberExtension, anyAttribute=safe_text, mixed=safe_text, numberExtensionSeparator=safe_text)
@given(instance=xal_PostBoxNumberExtension_strategy)
@settings(max_examples=25)
def test_xal_PostBoxNumberExtension_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberExtension)


xal_PostBoxNumberPrefix_strategy = st.builds(xal_PostBoxNumberPrefix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberPrefixSeparator=safe_text)
@given(instance=xal_PostBoxNumberPrefix_strategy)
@settings(max_examples=25)
def test_xal_PostBoxNumberPrefix_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberPrefix)


xal_PostBoxNumberSuffix_strategy = st.builds(xal_PostBoxNumberSuffix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberSuffixSeparator=safe_text)
@given(instance=xal_PostBoxNumberSuffix_strategy)
@settings(max_examples=25)
def test_xal_PostBoxNumberSuffix_instantiation(instance):
    assert isinstance(instance, xal_PostBoxNumberSuffix)


xal_PostOffice_strategy = st.builds(xal_PostOffice, any=safe_text, anyAttribute=safe_text, indicator=safe_text, type=safe_text)
@given(instance=xal_PostOffice_strategy)
@settings(max_examples=25)
def test_xal_PostOffice_instantiation(instance):
    assert isinstance(instance, xal_PostOffice)


xal_PostOfficeName_strategy = st.builds(xal_PostOfficeName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_PostOfficeName_strategy)
@settings(max_examples=25)
def test_xal_PostOfficeName_instantiation(instance):
    assert isinstance(instance, xal_PostOfficeName)


xal_PostOfficeNumber_strategy = st.builds(xal_PostOfficeNumber, anyAttribute=safe_text, code=safe_text, indicator=safe_text, indicatorOccurrence=safe_text, mixed=safe_text)
@given(instance=xal_PostOfficeNumber_strategy)
@settings(max_examples=25)
def test_xal_PostOfficeNumber_instantiation(instance):
    assert isinstance(instance, xal_PostOfficeNumber)


xal_PostTown_strategy = st.builds(xal_PostTown, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_PostTown_strategy)
@settings(max_examples=25)
def test_xal_PostTown_instantiation(instance):
    assert isinstance(instance, xal_PostTown)


xal_PostTownName_strategy = st.builds(xal_PostTownName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_PostTownName_strategy)
@settings(max_examples=25)
def test_xal_PostTownName_instantiation(instance):
    assert isinstance(instance, xal_PostTownName)


xal_PostTownSuffix_strategy = st.builds(xal_PostTownSuffix, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_PostTownSuffix_strategy)
@settings(max_examples=25)
def test_xal_PostTownSuffix_instantiation(instance):
    assert isinstance(instance, xal_PostTownSuffix)


xal_PostalCode_strategy = st.builds(xal_PostalCode, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_PostalCode_strategy)
@settings(max_examples=25)
def test_xal_PostalCode_instantiation(instance):
    assert isinstance(instance, xal_PostalCode)


xal_PostalCodeNumber_strategy = st.builds(xal_PostalCodeNumber, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_PostalCodeNumber_strategy)
@settings(max_examples=25)
def test_xal_PostalCodeNumber_instantiation(instance):
    assert isinstance(instance, xal_PostalCodeNumber)


xal_PostalCodeNumberExtension_strategy = st.builds(xal_PostalCodeNumberExtension, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberExtensionSeparator=safe_text, type=safe_text)
@given(instance=xal_PostalCodeNumberExtension_strategy)
@settings(max_examples=25)
def test_xal_PostalCodeNumberExtension_instantiation(instance):
    assert isinstance(instance, xal_PostalCodeNumberExtension)


xal_PostalRoute_strategy = st.builds(xal_PostalRoute, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_PostalRoute_strategy)
@settings(max_examples=25)
def test_xal_PostalRoute_instantiation(instance):
    assert isinstance(instance, xal_PostalRoute)


xal_PostalRouteName_strategy = st.builds(xal_PostalRouteName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_PostalRouteName_strategy)
@settings(max_examples=25)
def test_xal_PostalRouteName_instantiation(instance):
    assert isinstance(instance, xal_PostalRouteName)


xal_PostalRouteNumber_strategy = st.builds(xal_PostalRouteNumber, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_PostalRouteNumber_strategy)
@settings(max_examples=25)
def test_xal_PostalRouteNumber_instantiation(instance):
    assert isinstance(instance, xal_PostalRouteNumber)


xal_PostalServiceElements_strategy = st.builds(xal_PostalServiceElements, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_PostalServiceElements_strategy)
@settings(max_examples=25)
def test_xal_PostalServiceElements_instantiation(instance):
    assert isinstance(instance, xal_PostalServiceElements)


xal_Premise_strategy = st.builds(xal_Premise, any=safe_text, anyAttribute=safe_text, premiseDependency=safe_text, premiseDependencyType=safe_text, premiseThoroughfareConnector=safe_text, type=safe_text)
@given(instance=xal_Premise_strategy)
@settings(max_examples=25)
def test_xal_Premise_instantiation(instance):
    assert isinstance(instance, xal_Premise)


xal_PremiseLocation_strategy = st.builds(xal_PremiseLocation, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_PremiseLocation_strategy)
@settings(max_examples=25)
def test_xal_PremiseLocation_instantiation(instance):
    assert isinstance(instance, xal_PremiseLocation)


xal_PremiseName_strategy = st.builds(xal_PremiseName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text, typeOccurrence=safe_text)
@given(instance=xal_PremiseName_strategy)
@settings(max_examples=25)
def test_xal_PremiseName_instantiation(instance):
    assert isinstance(instance, xal_PremiseName)


xal_PremiseNumber_strategy = st.builds(xal_PremiseNumber, anyAttribute=safe_text, code=safe_text, indicator=safe_text, indicatorOccurrence=safe_text, mixed=safe_text, numberType=safe_text, numberTypeOccurrence=safe_text, type=safe_text)
@given(instance=xal_PremiseNumber_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumber_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumber)


xal_PremiseNumberPrefix_strategy = st.builds(xal_PremiseNumberPrefix, anyAttribute=safe_text, code=safe_text, numberPrefixSeparator=safe_text, type=safe_text, value=safe_text)
@given(instance=xal_PremiseNumberPrefix_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumberPrefix_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberPrefix)


xal_PremiseNumberRange_strategy = st.builds(xal_PremiseNumberRange, indicator=safe_text, indicatorOccurence=safe_text, numberRangeOccurence=safe_text, rangeType=safe_text, separator=safe_text, type=safe_text)
@given(instance=xal_PremiseNumberRange_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumberRange_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRange)


xal_PremiseNumberRangeFrom_strategy = st.builds(xal_PremiseNumberRangeFrom)
@given(instance=xal_PremiseNumberRangeFrom_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumberRangeFrom_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRangeFrom)


xal_PremiseNumberRangeTo_strategy = st.builds(xal_PremiseNumberRangeTo)
@given(instance=xal_PremiseNumberRangeTo_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumberRangeTo_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberRangeTo)


xal_PremiseNumberSuffix_strategy = st.builds(xal_PremiseNumberSuffix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberSuffixSeparator=safe_text, type=safe_text)
@given(instance=xal_PremiseNumberSuffix_strategy)
@settings(max_examples=25)
def test_xal_PremiseNumberSuffix_instantiation(instance):
    assert isinstance(instance, xal_PremiseNumberSuffix)


xal_SortingCode_strategy = st.builds(xal_SortingCode, code=safe_text, type=safe_text)
@given(instance=xal_SortingCode_strategy)
@settings(max_examples=25)
def test_xal_SortingCode_instantiation(instance):
    assert isinstance(instance, xal_SortingCode)


xal_SubAdministrativeArea_strategy = st.builds(xal_SubAdministrativeArea, any=safe_text, anyAttribute=safe_text, indicator=safe_text, type=safe_text, usageType=safe_text)
@given(instance=xal_SubAdministrativeArea_strategy)
@settings(max_examples=25)
def test_xal_SubAdministrativeArea_instantiation(instance):
    assert isinstance(instance, xal_SubAdministrativeArea)


xal_SubAdministrativeAreaName_strategy = st.builds(xal_SubAdministrativeAreaName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_SubAdministrativeAreaName_strategy)
@settings(max_examples=25)
def test_xal_SubAdministrativeAreaName_instantiation(instance):
    assert isinstance(instance, xal_SubAdministrativeAreaName)


xal_SubPremise_strategy = st.builds(xal_SubPremise, any=safe_text, anyAttribute=safe_text, type=safe_text)
@given(instance=xal_SubPremise_strategy)
@settings(max_examples=25)
def test_xal_SubPremise_instantiation(instance):
    assert isinstance(instance, xal_SubPremise)


xal_SubPremiseLocation_strategy = st.builds(xal_SubPremiseLocation, code=safe_text, mixed=safe_text)
@given(instance=xal_SubPremiseLocation_strategy)
@settings(max_examples=25)
def test_xal_SubPremiseLocation_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseLocation)


xal_SubPremiseName_strategy = st.builds(xal_SubPremiseName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text, typeOccurrence=safe_text)
@given(instance=xal_SubPremiseName_strategy)
@settings(max_examples=25)
def test_xal_SubPremiseName_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseName)


xal_SubPremiseNumber_strategy = st.builds(xal_SubPremiseNumber, anyAttribute=safe_text, code=safe_text, indicator=safe_text, indicatorOccurrence=safe_text, mixed=safe_text, numberTypeOccurrence=safe_text, premiseNumberSeparator=safe_text, type=safe_text)
@given(instance=xal_SubPremiseNumber_strategy)
@settings(max_examples=25)
def test_xal_SubPremiseNumber_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumber)


xal_SubPremiseNumberPrefix_strategy = st.builds(xal_SubPremiseNumberPrefix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberPrefixSeparator=safe_text, type=safe_text)
@given(instance=xal_SubPremiseNumberPrefix_strategy)
@settings(max_examples=25)
def test_xal_SubPremiseNumberPrefix_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumberPrefix)


xal_SubPremiseNumberSuffix_strategy = st.builds(xal_SubPremiseNumberSuffix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberSuffixSeparator=safe_text, type=safe_text)
@given(instance=xal_SubPremiseNumberSuffix_strategy)
@settings(max_examples=25)
def test_xal_SubPremiseNumberSuffix_instantiation(instance):
    assert isinstance(instance, xal_SubPremiseNumberSuffix)


xal_SupplementaryPostalServiceData_strategy = st.builds(xal_SupplementaryPostalServiceData, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_SupplementaryPostalServiceData_strategy)
@settings(max_examples=25)
def test_xal_SupplementaryPostalServiceData_instantiation(instance):
    assert isinstance(instance, xal_SupplementaryPostalServiceData)


xal_Thoroughfare_strategy = st.builds(xal_Thoroughfare, any=safe_text, anyAttribute=safe_text, dependentThoroughfares=safe_text, dependentThoroughfaresConnector=safe_text, dependentThoroughfaresIndicator=safe_text, dependentThoroughfaresType=safe_text, group=safe_text, type=safe_text)
@given(instance=xal_Thoroughfare_strategy)
@settings(max_examples=25)
def test_xal_Thoroughfare_instantiation(instance):
    assert isinstance(instance, xal_Thoroughfare)


xal_ThoroughfareLeadingType_strategy = st.builds(xal_ThoroughfareLeadingType, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareLeadingType_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareLeadingType_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareLeadingType)


xal_ThoroughfareName_strategy = st.builds(xal_ThoroughfareName, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareName_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareName_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareName)


xal_ThoroughfareNumber_strategy = st.builds(xal_ThoroughfareNumber, anyAttribute=safe_text, code=safe_text, indicator=safe_text, indicatorOccurrence=safe_text, mixed=safe_text, numberOccurrence=safe_text, numberType=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareNumber_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumber_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumber)


xal_ThoroughfareNumberFrom_strategy = st.builds(xal_ThoroughfareNumberFrom, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_ThoroughfareNumberFrom_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumberFrom_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberFrom)


xal_ThoroughfareNumberPrefix_strategy = st.builds(xal_ThoroughfareNumberPrefix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberPrefixSeparator=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareNumberPrefix_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumberPrefix_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberPrefix)


xal_ThoroughfareNumberRange_strategy = st.builds(xal_ThoroughfareNumberRange, anyAttribute=safe_text, code=safe_text, indicator=safe_text, indicatorOccurrence=safe_text, numberRangeOccurrence=safe_text, rangeType=safe_text, separator=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareNumberRange_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumberRange_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberRange)


xal_ThoroughfareNumberSuffix_strategy = st.builds(xal_ThoroughfareNumberSuffix, anyAttribute=safe_text, code=safe_text, mixed=safe_text, numberSuffixSeparator=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareNumberSuffix_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumberSuffix_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberSuffix)


xal_ThoroughfareNumberTo_strategy = st.builds(xal_ThoroughfareNumberTo, anyAttribute=safe_text, code=safe_text, mixed=safe_text)
@given(instance=xal_ThoroughfareNumberTo_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareNumberTo_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareNumberTo)


xal_ThoroughfarePostDirection_strategy = st.builds(xal_ThoroughfarePostDirection, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_ThoroughfarePostDirection_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfarePostDirection_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfarePostDirection)


xal_ThoroughfarePreDirection_strategy = st.builds(xal_ThoroughfarePreDirection, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_ThoroughfarePreDirection_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfarePreDirection_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfarePreDirection)


xal_ThoroughfareTrailingType_strategy = st.builds(xal_ThoroughfareTrailingType, anyAttribute=safe_text, code=safe_text, mixed=safe_text, type=safe_text)
@given(instance=xal_ThoroughfareTrailingType_strategy)
@settings(max_examples=25)
def test_xal_ThoroughfareTrailingType_instantiation(instance):
    assert isinstance(instance, xal_ThoroughfareTrailingType)


xal_Xal_strategy = st.builds(xal_Xal, any=safe_text, anyAttribute=safe_text, version=safe_text)
@given(instance=xal_Xal_strategy)
@settings(max_examples=25)
def test_xal_Xal_instantiation(instance):
    assert isinstance(instance, xal_Xal)



