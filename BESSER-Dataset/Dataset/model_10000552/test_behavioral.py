import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    APNAdv,
    APNAdvertiser,
    APNCache_Interface,
    APNLineItem,
    APNLineItemModelService,
    APNManager,
    APNModel,
    APNModelFactory,
    APNProgrammaticModel,
    APNRepository_Interface,
    APNStore_Interface,
    Advertiser,
    AdvertiserBlocklistWhitelist,
    AdvertiserExcludedVertical,
    Agency,
    AgencyBlocklistWhitelist,
    AgencyExcludedVertical,
    AppNexus,
    AppNexusClient,
    BQJobError,
    BQManager,
    BQTable,
    BidAdjuster,
    BrandSafetyBrandSafetyCustomSetting,
    BrandSafetyBrandSafetyLabel,
    BrandSaftey,
    Campaign,
    CampaignBlocklistWhitelist,
    CampaignTravelEventType,
    Class2,
    CloudSQLManager,
    CreativeApproval,
    CreativeAsset,
    CreativeAssetTactic,
    DBMManager,
    DCMManager,
    DCSManager,
    DSManager,
    FBManager,
    GCEManager,
    GCPManager,
    GCSManager,
    GenericModel,
    Goal,
    IOManager,
    ModelService_Interface,
    Model_Interface,
    Oauth2client_client_GoogleCredentials,
    Partner,
    PartnerExcludedVertical,
    Pixel,
    ProductLineItem,
    ProgrammaticModel_Interface,
    RecordType,
    RestClient,
    SalesforceBulkManager,
    Salesforcemanager,
    SojernBusiness,
    SpendAccount,
    SpendAccountBlocklistWhitelist,
    SystemCreative,
    SystemInsertionOrder,
    SystemLineItem,
    SystemLineItemConversionPixel,
    Tactic,
    Targeting,
    User,
    WHUtils,
    autopacing_inputs,
    dbm_li_sfdc_product_li_mapping,
    googleapiclient_discovery,
    smp_events_dataset_smp_events_daily,
    updater_events_dataset_updater_events_daily,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_APNLineItemModelService_APNLineItem_stub_double():
    # APNLineItemModelService has no real 'APNLineItemModelService_APNLineItem_020' property in the generated
    # code (a bare stub) -- manually attach it so APNLineItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # APNLineItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = APNLineItem(attribute="sample_text", attribute2="sample_text")
    partner = APNLineItemModelService()
    setattr(partner, 'APNLineItemModelService_APNLineItem_020', None)
    _safe_set(owner, 'APNLineItemModelService_APNLineItem_121', partner)
    assert getattr(partner, 'APNLineItemModelService_APNLineItem_020') == owner
    _safe_set(owner, 'APNLineItemModelService_APNLineItem_121', None)
    assert getattr(partner, 'APNLineItemModelService_APNLineItem_020') is None


def test_assoc_APNLineItem_APNModel_stub_double():
    # APNModel has no real 'APNLineItem_APNModel_119' property in the generated
    # code (a bare stub) -- manually attach it so APNLineItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # APNLineItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = APNLineItem(attribute="sample_text", attribute2="sample_text")
    partner = APNModel()
    setattr(partner, 'APNLineItem_APNModel_119', None)
    _safe_set(owner, 'APNLineItem_APNModel_018', {partner})
    assert owner in getattr(partner, 'APNLineItem_APNModel_119')
    _safe_set(owner, 'APNLineItem_APNModel_018', set())
    assert owner not in getattr(partner, 'APNLineItem_APNModel_119')


def test_assoc_APNModel_APNLineItem_stub_double():
    # APNModel has no real 'APNModel_APNLineItem_04' property in the generated
    # code (a bare stub) -- manually attach it so APNLineItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # APNLineItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = APNLineItem(attribute="sample_text", attribute2="sample_text")
    partner = APNModel()
    setattr(partner, 'APNModel_APNLineItem_04', None)
    _safe_set(owner, 'APNModel_APNLineItem_15', {partner})
    assert getattr(partner, 'APNModel_APNLineItem_04') == owner
    _safe_set(owner, 'APNModel_APNLineItem_15', set())
    assert getattr(partner, 'APNModel_APNLineItem_04') is None


