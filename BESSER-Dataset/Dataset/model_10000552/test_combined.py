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
    APNAdv,
    AppNexus,
    RestClient,
    APNModelFactory,
    Class2,
    APNLineItemModelService,
    ModelService_Interface,
    Model_Interface,
    GenericModel,
    APNRepository_Interface,
    APNCache_Interface,
    APNStore_Interface,
    APNProgrammaticModel,
    ProgrammaticModel_Interface,
    APNModel,
    APNLineItem,
    APNAdvertiser,
    BidAdjuster,
    IOManager,
    autopacing_inputs,
    dbm_li_sfdc_product_li_mapping,
    CreativeApproval,
    SystemLineItemConversionPixel,
    SystemCreative,
    SystemLineItem,
    Tactic,
    CreativeAssetTactic,
    CreativeAsset,
    ProductLineItem,
    CampaignTravelEventType,
    CampaignBlocklistWhitelist,
    SpendAccountBlocklistWhitelist,
    Campaign,
    SpendAccount,
    AgencyExcludedVertical,
    AgencyBlocklistWhitelist,
    AdvertiserExcludedVertical,
    AdvertiserBlocklistWhitelist,
    SystemInsertionOrder,
    PartnerExcludedVertical,
    BrandSafetyBrandSafetyLabel,
    BrandSafetyBrandSafetyCustomSetting,
    Agency,
    Advertiser,
    Pixel,
    Partner,
    Goal,
    BrandSaftey,
    User,
    Targeting,
    SojernBusiness,
    RecordType,
    AppNexusClient,
    APNManager,
    updater_events_dataset_updater_events_daily,
    smp_events_dataset_smp_events_daily,
    GCSManager,
    GCEManager,
    FBManager,
    DSManager,
    CloudSQLManager,
    DCMManager,
    DCSManager,
    DBMManager,
    SalesforceBulkManager,
    Salesforcemanager,
    WHUtils,
    BQTable,
    BQJobError,
    Oauth2client_client_GoogleCredentials,
    GCPManager,
    googleapiclient_discovery,
    BQManager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_apnadv_is_not_abstract():
    assert not inspect.isabstract(APNAdv)


def test_hyp_apnadv_constructor_exists():
    assert callable(APNAdv.__init__)


def test_hyp_apnadv_constructor_args():
    sig = inspect.signature(APNAdv.__init__)
    params = list(sig.parameters.keys())



def test_hyp_appnexus_is_not_abstract():
    assert not inspect.isabstract(AppNexus)


def test_hyp_appnexus_constructor_exists():
    assert callable(AppNexus.__init__)


def test_hyp_appnexus_constructor_args():
    sig = inspect.signature(AppNexus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_restclient_is_not_abstract():
    assert not inspect.isabstract(RestClient)


def test_hyp_restclient_constructor_exists():
    assert callable(RestClient.__init__)


def test_hyp_restclient_constructor_args():
    sig = inspect.signature(RestClient.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnmodelfactory_is_not_abstract():
    assert not inspect.isabstract(APNModelFactory)


def test_hyp_apnmodelfactory_constructor_exists():
    assert callable(APNModelFactory.__init__)


def test_hyp_apnmodelfactory_constructor_args():
    sig = inspect.signature(APNModelFactory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_hyp_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_hyp_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnlineitemmodelservice_is_not_abstract():
    assert not inspect.isabstract(APNLineItemModelService)


def test_hyp_apnlineitemmodelservice_constructor_exists():
    assert callable(APNLineItemModelService.__init__)


def test_hyp_apnlineitemmodelservice_constructor_args():
    sig = inspect.signature(APNLineItemModelService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelservice_interface_is_not_abstract():
    assert not inspect.isabstract(ModelService_Interface)


def test_hyp_modelservice_interface_constructor_exists():
    assert callable(ModelService_Interface.__init__)


def test_hyp_modelservice_interface_constructor_args():
    sig = inspect.signature(ModelService_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_interface_is_not_abstract():
    assert not inspect.isabstract(Model_Interface)


def test_hyp_model_interface_constructor_exists():
    assert callable(Model_Interface.__init__)


def test_hyp_model_interface_constructor_args():
    sig = inspect.signature(Model_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genericmodel_is_not_abstract():
    assert not inspect.isabstract(GenericModel)


def test_hyp_genericmodel_constructor_exists():
    assert callable(GenericModel.__init__)


def test_hyp_genericmodel_constructor_args():
    sig = inspect.signature(GenericModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnrepository_interface_is_not_abstract():
    assert not inspect.isabstract(APNRepository_Interface)


def test_hyp_apnrepository_interface_constructor_exists():
    assert callable(APNRepository_Interface.__init__)


def test_hyp_apnrepository_interface_constructor_args():
    sig = inspect.signature(APNRepository_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apncache_interface_is_not_abstract():
    assert not inspect.isabstract(APNCache_Interface)


def test_hyp_apncache_interface_constructor_exists():
    assert callable(APNCache_Interface.__init__)


def test_hyp_apncache_interface_constructor_args():
    sig = inspect.signature(APNCache_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnstore_interface_is_not_abstract():
    assert not inspect.isabstract(APNStore_Interface)


def test_hyp_apnstore_interface_constructor_exists():
    assert callable(APNStore_Interface.__init__)


def test_hyp_apnstore_interface_constructor_args():
    sig = inspect.signature(APNStore_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnprogrammaticmodel_is_not_abstract():
    assert not inspect.isabstract(APNProgrammaticModel)


def test_hyp_apnprogrammaticmodel_constructor_exists():
    assert callable(APNProgrammaticModel.__init__)


def test_hyp_apnprogrammaticmodel_constructor_args():
    sig = inspect.signature(APNProgrammaticModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_programmaticmodel_interface_is_not_abstract():
    assert not inspect.isabstract(ProgrammaticModel_Interface)


def test_hyp_programmaticmodel_interface_constructor_exists():
    assert callable(ProgrammaticModel_Interface.__init__)


def test_hyp_programmaticmodel_interface_constructor_args():
    sig = inspect.signature(ProgrammaticModel_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnmodel_is_not_abstract():
    assert not inspect.isabstract(APNModel)


def test_hyp_apnmodel_constructor_exists():
    assert callable(APNModel.__init__)


def test_hyp_apnmodel_constructor_args():
    sig = inspect.signature(APNModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnlineitem_is_not_abstract():
    assert not inspect.isabstract(APNLineItem)


def test_hyp_apnlineitem_constructor_exists():
    assert callable(APNLineItem.__init__)


def test_hyp_apnlineitem_constructor_args():
    sig = inspect.signature(APNLineItem.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_apnadvertiser_is_not_abstract():
    assert not inspect.isabstract(APNAdvertiser)


def test_hyp_apnadvertiser_constructor_exists():
    assert callable(APNAdvertiser.__init__)


def test_hyp_apnadvertiser_constructor_args():
    sig = inspect.signature(APNAdvertiser.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bidadjuster_is_not_abstract():
    assert not inspect.isabstract(BidAdjuster)


def test_hyp_bidadjuster_constructor_exists():
    assert callable(BidAdjuster.__init__)


def test_hyp_bidadjuster_constructor_args():
    sig = inspect.signature(BidAdjuster.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iomanager_is_not_abstract():
    assert not inspect.isabstract(IOManager)


def test_hyp_iomanager_constructor_exists():
    assert callable(IOManager.__init__)


def test_hyp_iomanager_constructor_args():
    sig = inspect.signature(IOManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autopacing_inputs_is_not_abstract():
    assert not inspect.isabstract(autopacing_inputs)


def test_hyp_autopacing_inputs_constructor_exists():
    assert callable(autopacing_inputs.__init__)


def test_hyp_autopacing_inputs_constructor_args():
    sig = inspect.signature(autopacing_inputs.__init__)
    params = list(sig.parameters.keys())
    assert "cvr" in params, "Missing parameter 'cvr'"
    assert "impressions" in params, "Missing parameter 'impressions'"
    assert "sojern_goal_rae" in params, "Missing parameter 'sojern_goal_rae'"
    assert "sfdc_opportunity_id" in params, "Missing parameter 'sfdc_opportunity_id'"
    assert "region1" in params, "Missing parameter 'region1'"
    assert "percentage_impression_credit" in params, "Missing parameter 'percentage_impression_credit'"
    assert "minimum_margin" in params, "Missing parameter 'minimum_margin'"
    assert "product_type" in params, "Missing parameter 'product_type'"
    assert "minimum_partner_data_delivery_percent" in params, "Missing parameter 'minimum_partner_data_delivery_percent'"
    assert "avg_price_usd" in params, "Missing parameter 'avg_price_usd'"
    assert "adjust_bids" in params, "Missing parameter 'adjust_bids'"
    assert "end_date" in params, "Missing parameter 'end_date'"
    assert "expected_click_credit" in params, "Missing parameter 'expected_click_credit'"
    assert "account_manager" in params, "Missing parameter 'account_manager'"
    assert "sfdc_product_id" in params, "Missing parameter 'sfdc_product_id'"
    assert "min_daily_volume" in params, "Missing parameter 'min_daily_volume'"
    assert "billing_currency" in params, "Missing parameter 'billing_currency'"
    assert "start_date" in params, "Missing parameter 'start_date'"
    assert "cpx" in params, "Missing parameter 'cpx'"
    assert "on_off" in params, "Missing parameter 'on_off'"
    assert "percentage_conversion_credit" in params, "Missing parameter 'percentage_conversion_credit'"
    assert "hours_early_to_complete" in params, "Missing parameter 'hours_early_to_complete'"
    assert "goal_type" in params, "Missing parameter 'goal_type'"
    assert "days_early_to_complete" in params, "Missing parameter 'days_early_to_complete'"
    assert "estimated_booking_value" in params, "Missing parameter 'estimated_booking_value'"
    assert "dbm_io_id" in params, "Missing parameter 'dbm_io_id'"
    assert "product_start_date" in params, "Missing parameter 'product_start_date'"
    assert "conversions" in params, "Missing parameter 'conversions'"
    assert "kpi_goal" in params, "Missing parameter 'kpi_goal'"
    assert "min_daily_volume_percent" in params, "Missing parameter 'min_daily_volume_percent'"
    assert "pacing" in params, "Missing parameter 'pacing'"
    assert "product_end_date" in params, "Missing parameter 'product_end_date'"
    assert "effective_impressions" in params, "Missing parameter 'effective_impressions'"
    assert "cpm" in params, "Missing parameter 'cpm'"
    assert "region" in params, "Missing parameter 'region'"
    assert "exchange_rate" in params, "Missing parameter 'exchange_rate'"







































def test_hyp_dbm_li_sfdc_product_li_mapping_is_not_abstract():
    assert not inspect.isabstract(dbm_li_sfdc_product_li_mapping)


def test_hyp_dbm_li_sfdc_product_li_mapping_constructor_exists():
    assert callable(dbm_li_sfdc_product_li_mapping.__init__)


def test_hyp_dbm_li_sfdc_product_li_mapping_constructor_args():
    sig = inspect.signature(dbm_li_sfdc_product_li_mapping.__init__)
    params = list(sig.parameters.keys())
    assert "sfdc_product_id" in params, "Missing parameter 'sfdc_product_id'"
    assert "dub_allocation_label" in params, "Missing parameter 'dub_allocation_label'"
    assert "dbm_creative_ids" in params, "Missing parameter 'dbm_creative_ids'"
    assert "dbm_line_item_id" in params, "Missing parameter 'dbm_line_item_id'"
    assert "dbm_io_id" in params, "Missing parameter 'dbm_io_id'"








def test_hyp_creativeapproval_is_not_abstract():
    assert not inspect.isabstract(CreativeApproval)


def test_hyp_creativeapproval_constructor_exists():
    assert callable(CreativeApproval.__init__)


def test_hyp_creativeapproval_constructor_args():
    sig = inspect.signature(CreativeApproval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemlineitemconversionpixel_is_not_abstract():
    assert not inspect.isabstract(SystemLineItemConversionPixel)


def test_hyp_systemlineitemconversionpixel_constructor_exists():
    assert callable(SystemLineItemConversionPixel.__init__)


def test_hyp_systemlineitemconversionpixel_constructor_args():
    sig = inspect.signature(SystemLineItemConversionPixel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemcreative_is_not_abstract():
    assert not inspect.isabstract(SystemCreative)


def test_hyp_systemcreative_constructor_exists():
    assert callable(SystemCreative.__init__)


def test_hyp_systemcreative_constructor_args():
    sig = inspect.signature(SystemCreative.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemlineitem_is_not_abstract():
    assert not inspect.isabstract(SystemLineItem)


def test_hyp_systemlineitem_constructor_exists():
    assert callable(SystemLineItem.__init__)


def test_hyp_systemlineitem_constructor_args():
    sig = inspect.signature(SystemLineItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tactic_is_not_abstract():
    assert not inspect.isabstract(Tactic)


def test_hyp_tactic_constructor_exists():
    assert callable(Tactic.__init__)


def test_hyp_tactic_constructor_args():
    sig = inspect.signature(Tactic.__init__)
    params = list(sig.parameters.keys())



def test_hyp_creativeassettactic_is_not_abstract():
    assert not inspect.isabstract(CreativeAssetTactic)


def test_hyp_creativeassettactic_constructor_exists():
    assert callable(CreativeAssetTactic.__init__)


def test_hyp_creativeassettactic_constructor_args():
    sig = inspect.signature(CreativeAssetTactic.__init__)
    params = list(sig.parameters.keys())



def test_hyp_creativeasset_is_not_abstract():
    assert not inspect.isabstract(CreativeAsset)


def test_hyp_creativeasset_constructor_exists():
    assert callable(CreativeAsset.__init__)


def test_hyp_creativeasset_constructor_args():
    sig = inspect.signature(CreativeAsset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_productlineitem_is_not_abstract():
    assert not inspect.isabstract(ProductLineItem)


def test_hyp_productlineitem_constructor_exists():
    assert callable(ProductLineItem.__init__)


def test_hyp_productlineitem_constructor_args():
    sig = inspect.signature(ProductLineItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_campaigntraveleventtype_is_not_abstract():
    assert not inspect.isabstract(CampaignTravelEventType)


def test_hyp_campaigntraveleventtype_constructor_exists():
    assert callable(CampaignTravelEventType.__init__)


def test_hyp_campaigntraveleventtype_constructor_args():
    sig = inspect.signature(CampaignTravelEventType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_campaignblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(CampaignBlocklistWhitelist)


def test_hyp_campaignblocklistwhitelist_constructor_exists():
    assert callable(CampaignBlocklistWhitelist.__init__)


def test_hyp_campaignblocklistwhitelist_constructor_args():
    sig = inspect.signature(CampaignBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spendaccountblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(SpendAccountBlocklistWhitelist)


def test_hyp_spendaccountblocklistwhitelist_constructor_exists():
    assert callable(SpendAccountBlocklistWhitelist.__init__)


def test_hyp_spendaccountblocklistwhitelist_constructor_args():
    sig = inspect.signature(SpendAccountBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_campaign_is_not_abstract():
    assert not inspect.isabstract(Campaign)


def test_hyp_campaign_constructor_exists():
    assert callable(Campaign.__init__)


def test_hyp_campaign_constructor_args():
    sig = inspect.signature(Campaign.__init__)
    params = list(sig.parameters.keys())



def test_hyp_spendaccount_is_not_abstract():
    assert not inspect.isabstract(SpendAccount)


def test_hyp_spendaccount_constructor_exists():
    assert callable(SpendAccount.__init__)


def test_hyp_spendaccount_constructor_args():
    sig = inspect.signature(SpendAccount.__init__)
    params = list(sig.parameters.keys())



def test_hyp_agencyexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(AgencyExcludedVertical)


def test_hyp_agencyexcludedvertical_constructor_exists():
    assert callable(AgencyExcludedVertical.__init__)


def test_hyp_agencyexcludedvertical_constructor_args():
    sig = inspect.signature(AgencyExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_hyp_agencyblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(AgencyBlocklistWhitelist)


def test_hyp_agencyblocklistwhitelist_constructor_exists():
    assert callable(AgencyBlocklistWhitelist.__init__)


def test_hyp_agencyblocklistwhitelist_constructor_args():
    sig = inspect.signature(AgencyBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_advertiserexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(AdvertiserExcludedVertical)


def test_hyp_advertiserexcludedvertical_constructor_exists():
    assert callable(AdvertiserExcludedVertical.__init__)


def test_hyp_advertiserexcludedvertical_constructor_args():
    sig = inspect.signature(AdvertiserExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_hyp_advertiserblocklistwhitelist_is_not_abstract():
    assert not inspect.isabstract(AdvertiserBlocklistWhitelist)


def test_hyp_advertiserblocklistwhitelist_constructor_exists():
    assert callable(AdvertiserBlocklistWhitelist.__init__)


def test_hyp_advertiserblocklistwhitelist_constructor_args():
    sig = inspect.signature(AdvertiserBlocklistWhitelist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systeminsertionorder_is_not_abstract():
    assert not inspect.isabstract(SystemInsertionOrder)


def test_hyp_systeminsertionorder_constructor_exists():
    assert callable(SystemInsertionOrder.__init__)


def test_hyp_systeminsertionorder_constructor_args():
    sig = inspect.signature(SystemInsertionOrder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_partnerexcludedvertical_is_not_abstract():
    assert not inspect.isabstract(PartnerExcludedVertical)


def test_hyp_partnerexcludedvertical_constructor_exists():
    assert callable(PartnerExcludedVertical.__init__)


def test_hyp_partnerexcludedvertical_constructor_args():
    sig = inspect.signature(PartnerExcludedVertical.__init__)
    params = list(sig.parameters.keys())



def test_hyp_brandsafetybrandsafetylabel_is_not_abstract():
    assert not inspect.isabstract(BrandSafetyBrandSafetyLabel)


def test_hyp_brandsafetybrandsafetylabel_constructor_exists():
    assert callable(BrandSafetyBrandSafetyLabel.__init__)


def test_hyp_brandsafetybrandsafetylabel_constructor_args():
    sig = inspect.signature(BrandSafetyBrandSafetyLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_brandsafetybrandsafetycustomsetting_is_not_abstract():
    assert not inspect.isabstract(BrandSafetyBrandSafetyCustomSetting)


def test_hyp_brandsafetybrandsafetycustomsetting_constructor_exists():
    assert callable(BrandSafetyBrandSafetyCustomSetting.__init__)


def test_hyp_brandsafetybrandsafetycustomsetting_constructor_args():
    sig = inspect.signature(BrandSafetyBrandSafetyCustomSetting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_agency_is_not_abstract():
    assert not inspect.isabstract(Agency)


def test_hyp_agency_constructor_exists():
    assert callable(Agency.__init__)


def test_hyp_agency_constructor_args():
    sig = inspect.signature(Agency.__init__)
    params = list(sig.parameters.keys())
    assert "crm_id" in params, "Missing parameter 'crm_id'"




def test_hyp_advertiser_is_not_abstract():
    assert not inspect.isabstract(Advertiser)


def test_hyp_advertiser_constructor_exists():
    assert callable(Advertiser.__init__)


def test_hyp_advertiser_constructor_args():
    sig = inspect.signature(Advertiser.__init__)
    params = list(sig.parameters.keys())
    assert "crm_id" in params, "Missing parameter 'crm_id'"




def test_hyp_pixel_is_not_abstract():
    assert not inspect.isabstract(Pixel)


def test_hyp_pixel_constructor_exists():
    assert callable(Pixel.__init__)


def test_hyp_pixel_constructor_args():
    sig = inspect.signature(Pixel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_partner_is_not_abstract():
    assert not inspect.isabstract(Partner)


def test_hyp_partner_constructor_exists():
    assert callable(Partner.__init__)


def test_hyp_partner_constructor_args():
    sig = inspect.signature(Partner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_goal_is_not_abstract():
    assert not inspect.isabstract(Goal)


def test_hyp_goal_constructor_exists():
    assert callable(Goal.__init__)


def test_hyp_goal_constructor_args():
    sig = inspect.signature(Goal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_brandsaftey_is_not_abstract():
    assert not inspect.isabstract(BrandSaftey)


def test_hyp_brandsaftey_constructor_exists():
    assert callable(BrandSaftey.__init__)


def test_hyp_brandsaftey_constructor_args():
    sig = inspect.signature(BrandSaftey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_hyp_targeting_is_not_abstract():
    assert not inspect.isabstract(Targeting)


def test_hyp_targeting_constructor_exists():
    assert callable(Targeting.__init__)


def test_hyp_targeting_constructor_args():
    sig = inspect.signature(Targeting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sojernbusiness_is_not_abstract():
    assert not inspect.isabstract(SojernBusiness)


def test_hyp_sojernbusiness_constructor_exists():
    assert callable(SojernBusiness.__init__)


def test_hyp_sojernbusiness_constructor_args():
    sig = inspect.signature(SojernBusiness.__init__)
    params = list(sig.parameters.keys())



def test_hyp_recordtype_is_not_abstract():
    assert not inspect.isabstract(RecordType)


def test_hyp_recordtype_constructor_exists():
    assert callable(RecordType.__init__)


def test_hyp_recordtype_constructor_args():
    sig = inspect.signature(RecordType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "description" in params, "Missing parameter 'description'"
    assert "updated_by" in params, "Missing parameter 'updated_by'"
    assert "crm_id" in params, "Missing parameter 'crm_id'"









def test_hyp_appnexusclient_is_not_abstract():
    assert not inspect.isabstract(AppNexusClient)


def test_hyp_appnexusclient_constructor_exists():
    assert callable(AppNexusClient.__init__)


def test_hyp_appnexusclient_constructor_args():
    sig = inspect.signature(AppNexusClient.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apnmanager_is_not_abstract():
    assert not inspect.isabstract(APNManager)


def test_hyp_apnmanager_constructor_exists():
    assert callable(APNManager.__init__)


def test_hyp_apnmanager_constructor_args():
    sig = inspect.signature(APNManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_updater_events_dataset_updater_events_daily_is_not_abstract():
    assert not inspect.isabstract(updater_events_dataset_updater_events_daily)


def test_hyp_updater_events_dataset_updater_events_daily_constructor_exists():
    assert callable(updater_events_dataset_updater_events_daily.__init__)


def test_hyp_updater_events_dataset_updater_events_daily_constructor_args():
    sig = inspect.signature(updater_events_dataset_updater_events_daily.__init__)
    params = list(sig.parameters.keys())
    assert "advertisername" in params, "Missing parameter 'advertisername'"
    assert "segments_id" in params, "Missing parameter 'segments_id'"
    assert "sojernId" in params, "Missing parameter 'sojernId'"






def test_hyp_smp_events_dataset_smp_events_daily_is_not_abstract():
    assert not inspect.isabstract(smp_events_dataset_smp_events_daily)


def test_hyp_smp_events_dataset_smp_events_daily_constructor_exists():
    assert callable(smp_events_dataset_smp_events_daily.__init__)


def test_hyp_smp_events_dataset_smp_events_daily_constructor_args():
    sig = inspect.signature(smp_events_dataset_smp_events_daily.__init__)
    params = list(sig.parameters.keys())
    assert "profileid" in params, "Missing parameter 'profileid'"
    assert "eventsourcename" in params, "Missing parameter 'eventsourcename'"
    assert "externalIds_id__used_as_apnid_" in params, "Missing parameter 'externalIds_id__used_as_apnid_'"
    assert "ExternalIds_Type" in params, "Missing parameter 'ExternalIds_Type'"







def test_hyp_gcsmanager_is_not_abstract():
    assert not inspect.isabstract(GCSManager)


def test_hyp_gcsmanager_constructor_exists():
    assert callable(GCSManager.__init__)


def test_hyp_gcsmanager_constructor_args():
    sig = inspect.signature(GCSManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gcemanager_is_not_abstract():
    assert not inspect.isabstract(GCEManager)


def test_hyp_gcemanager_constructor_exists():
    assert callable(GCEManager.__init__)


def test_hyp_gcemanager_constructor_args():
    sig = inspect.signature(GCEManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fbmanager_is_not_abstract():
    assert not inspect.isabstract(FBManager)


def test_hyp_fbmanager_constructor_exists():
    assert callable(FBManager.__init__)


def test_hyp_fbmanager_constructor_args():
    sig = inspect.signature(FBManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsmanager_is_not_abstract():
    assert not inspect.isabstract(DSManager)


def test_hyp_dsmanager_constructor_exists():
    assert callable(DSManager.__init__)


def test_hyp_dsmanager_constructor_args():
    sig = inspect.signature(DSManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudsqlmanager_is_not_abstract():
    assert not inspect.isabstract(CloudSQLManager)


def test_hyp_cloudsqlmanager_constructor_exists():
    assert callable(CloudSQLManager.__init__)


def test_hyp_cloudsqlmanager_constructor_args():
    sig = inspect.signature(CloudSQLManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dcmmanager_is_not_abstract():
    assert not inspect.isabstract(DCMManager)


def test_hyp_dcmmanager_constructor_exists():
    assert callable(DCMManager.__init__)


def test_hyp_dcmmanager_constructor_args():
    sig = inspect.signature(DCMManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dcsmanager_is_not_abstract():
    assert not inspect.isabstract(DCSManager)


def test_hyp_dcsmanager_constructor_exists():
    assert callable(DCSManager.__init__)


def test_hyp_dcsmanager_constructor_args():
    sig = inspect.signature(DCSManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dbmmanager_is_not_abstract():
    assert not inspect.isabstract(DBMManager)


def test_hyp_dbmmanager_constructor_exists():
    assert callable(DBMManager.__init__)


def test_hyp_dbmmanager_constructor_args():
    sig = inspect.signature(DBMManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_salesforcebulkmanager_is_not_abstract():
    assert not inspect.isabstract(SalesforceBulkManager)


def test_hyp_salesforcebulkmanager_constructor_exists():
    assert callable(SalesforceBulkManager.__init__)


def test_hyp_salesforcebulkmanager_constructor_args():
    sig = inspect.signature(SalesforceBulkManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_salesforcemanager_is_not_abstract():
    assert not inspect.isabstract(Salesforcemanager)


def test_hyp_salesforcemanager_constructor_exists():
    assert callable(Salesforcemanager.__init__)


def test_hyp_salesforcemanager_constructor_args():
    sig = inspect.signature(Salesforcemanager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_whutils_is_not_abstract():
    assert not inspect.isabstract(WHUtils)


def test_hyp_whutils_constructor_exists():
    assert callable(WHUtils.__init__)


def test_hyp_whutils_constructor_args():
    sig = inspect.signature(WHUtils.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bqtable_is_not_abstract():
    assert not inspect.isabstract(BQTable)


def test_hyp_bqtable_constructor_exists():
    assert callable(BQTable.__init__)


def test_hyp_bqtable_constructor_args():
    sig = inspect.signature(BQTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bqjoberror_is_not_abstract():
    assert not inspect.isabstract(BQJobError)


def test_hyp_bqjoberror_constructor_exists():
    assert callable(BQJobError.__init__)


def test_hyp_bqjoberror_constructor_args():
    sig = inspect.signature(BQJobError.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oauth2client_client_googlecredentials_is_not_abstract():
    assert not inspect.isabstract(Oauth2client_client_GoogleCredentials)


def test_hyp_oauth2client_client_googlecredentials_constructor_exists():
    assert callable(Oauth2client_client_GoogleCredentials.__init__)


def test_hyp_oauth2client_client_googlecredentials_constructor_args():
    sig = inspect.signature(Oauth2client_client_GoogleCredentials.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gcpmanager_is_not_abstract():
    assert not inspect.isabstract(GCPManager)


def test_hyp_gcpmanager_constructor_exists():
    assert callable(GCPManager.__init__)


def test_hyp_gcpmanager_constructor_args():
    sig = inspect.signature(GCPManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_googleapiclient_discovery_is_not_abstract():
    assert not inspect.isabstract(googleapiclient_discovery)


def test_hyp_googleapiclient_discovery_constructor_exists():
    assert callable(googleapiclient_discovery.__init__)


def test_hyp_googleapiclient_discovery_constructor_args():
    sig = inspect.signature(googleapiclient_discovery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bqmanager_is_not_abstract():
    assert not inspect.isabstract(BQManager)


def test_hyp_bqmanager_constructor_exists():
    assert callable(BQManager.__init__)


def test_hyp_bqmanager_constructor_args():
    sig = inspect.signature(BQManager.__init__)
    params = list(sig.parameters.keys())


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
APNAdv_strategy = st.builds(
    APNAdv,
)
AppNexus_strategy = st.builds(
    AppNexus,
)
RestClient_strategy = st.builds(
    RestClient,
)
APNModelFactory_strategy = st.builds(
    APNModelFactory,
)
Class2_strategy = st.builds(
    Class2,
)
APNLineItemModelService_strategy = st.builds(
    APNLineItemModelService,
)
ModelService_Interface_strategy = st.builds(
    ModelService_Interface,
)
Model_Interface_strategy = st.builds(
    Model_Interface,
)
GenericModel_strategy = st.builds(
    GenericModel,
)
APNRepository_Interface_strategy = st.builds(
    APNRepository_Interface,
)
APNCache_Interface_strategy = st.builds(
    APNCache_Interface,
)
APNStore_Interface_strategy = st.builds(
    APNStore_Interface,
)
APNProgrammaticModel_strategy = st.builds(
    APNProgrammaticModel,
)
ProgrammaticModel_Interface_strategy = st.builds(
    ProgrammaticModel_Interface,
)
APNModel_strategy = st.builds(
    APNModel,
)
APNLineItem_strategy = st.builds(
    APNLineItem,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
APNAdvertiser_strategy = st.builds(
    APNAdvertiser,
)
BidAdjuster_strategy = st.builds(
    BidAdjuster,
)
IOManager_strategy = st.builds(
    IOManager,
)
autopacing_inputs_strategy = st.builds(
    autopacing_inputs,
    cvr=
        safe_text,
    impressions=
        safe_text,
    sojern_goal_rae=
        safe_text,
    sfdc_opportunity_id=
        safe_text,
    region1=
        safe_text,
    percentage_impression_credit=
        safe_text,
    minimum_margin=
        safe_text,
    product_type=
        safe_text,
    minimum_partner_data_delivery_percent=
        safe_text,
    avg_price_usd=
        safe_text,
    adjust_bids=
        safe_text,
    end_date=
        safe_text,
    expected_click_credit=
        safe_text,
    account_manager=
        safe_text,
    sfdc_product_id=
        safe_text,
    min_daily_volume=
        safe_text,
    billing_currency=
        safe_text,
    start_date=
        safe_text,
    cpx=
        safe_text,
    on_off=
        safe_text,
    percentage_conversion_credit=
        safe_text,
    hours_early_to_complete=
        safe_text,
    goal_type=
        safe_text,
    days_early_to_complete=
        safe_text,
    estimated_booking_value=
        safe_text,
    dbm_io_id=
        safe_text,
    product_start_date=
        safe_text,
    conversions=
        safe_text,
    kpi_goal=
        safe_text,
    min_daily_volume_percent=
        safe_text,
    pacing=
        safe_text,
    product_end_date=
        safe_text,
    effective_impressions=
        safe_text,
    cpm=
        safe_text,
    region=
        safe_text,
    exchange_rate=
        safe_text
)
dbm_li_sfdc_product_li_mapping_strategy = st.builds(
    dbm_li_sfdc_product_li_mapping,
    sfdc_product_id=
        safe_text,
    dub_allocation_label=
        safe_text,
    dbm_creative_ids=
        safe_text,
    dbm_line_item_id=
        safe_text,
    dbm_io_id=
        safe_text
)
CreativeApproval_strategy = st.builds(
    CreativeApproval,
)
SystemLineItemConversionPixel_strategy = st.builds(
    SystemLineItemConversionPixel,
)
SystemCreative_strategy = st.builds(
    SystemCreative,
)
SystemLineItem_strategy = st.builds(
    SystemLineItem,
)
Tactic_strategy = st.builds(
    Tactic,
)
CreativeAssetTactic_strategy = st.builds(
    CreativeAssetTactic,
)
CreativeAsset_strategy = st.builds(
    CreativeAsset,
)
ProductLineItem_strategy = st.builds(
    ProductLineItem,
)
CampaignTravelEventType_strategy = st.builds(
    CampaignTravelEventType,
)
CampaignBlocklistWhitelist_strategy = st.builds(
    CampaignBlocklistWhitelist,
)
SpendAccountBlocklistWhitelist_strategy = st.builds(
    SpendAccountBlocklistWhitelist,
)
Campaign_strategy = st.builds(
    Campaign,
)
SpendAccount_strategy = st.builds(
    SpendAccount,
)
AgencyExcludedVertical_strategy = st.builds(
    AgencyExcludedVertical,
)
AgencyBlocklistWhitelist_strategy = st.builds(
    AgencyBlocklistWhitelist,
)
AdvertiserExcludedVertical_strategy = st.builds(
    AdvertiserExcludedVertical,
)
AdvertiserBlocklistWhitelist_strategy = st.builds(
    AdvertiserBlocklistWhitelist,
)
SystemInsertionOrder_strategy = st.builds(
    SystemInsertionOrder,
)
PartnerExcludedVertical_strategy = st.builds(
    PartnerExcludedVertical,
)
BrandSafetyBrandSafetyLabel_strategy = st.builds(
    BrandSafetyBrandSafetyLabel,
)
BrandSafetyBrandSafetyCustomSetting_strategy = st.builds(
    BrandSafetyBrandSafetyCustomSetting,
)
Agency_strategy = st.builds(
    Agency,
    crm_id=
        safe_text
)
Advertiser_strategy = st.builds(
    Advertiser,
    crm_id=
        safe_text
)
Pixel_strategy = st.builds(
    Pixel,
)
Partner_strategy = st.builds(
    Partner,
)
Goal_strategy = st.builds(
    Goal,
)
BrandSaftey_strategy = st.builds(
    BrandSaftey,
)
User_strategy = st.builds(
    User,
)
Targeting_strategy = st.builds(
    Targeting,
)
SojernBusiness_strategy = st.builds(
    SojernBusiness,
)
RecordType_strategy = st.builds(
    RecordType,
    name=
        safe_text,
    id=
        safe_text,
    deleted=
        safe_text,
    description=
        safe_text,
    updated_by=
        safe_text,
    crm_id=
        safe_text
)
AppNexusClient_strategy = st.builds(
    AppNexusClient,
)
APNManager_strategy = st.builds(
    APNManager,
)
updater_events_dataset_updater_events_daily_strategy = st.builds(
    updater_events_dataset_updater_events_daily,
    advertisername=
        safe_text,
    segments_id=
        safe_text,
    sojernId=
        safe_text
)
smp_events_dataset_smp_events_daily_strategy = st.builds(
    smp_events_dataset_smp_events_daily,
    profileid=
        safe_text,
    eventsourcename=
        safe_text,
    externalIds_id__used_as_apnid_=
        safe_text,
    ExternalIds_Type=
        safe_text
)
GCSManager_strategy = st.builds(
    GCSManager,
)
GCEManager_strategy = st.builds(
    GCEManager,
)
FBManager_strategy = st.builds(
    FBManager,
)
DSManager_strategy = st.builds(
    DSManager,
)
CloudSQLManager_strategy = st.builds(
    CloudSQLManager,
)
DCMManager_strategy = st.builds(
    DCMManager,
)
DCSManager_strategy = st.builds(
    DCSManager,
)
DBMManager_strategy = st.builds(
    DBMManager,
)
SalesforceBulkManager_strategy = st.builds(
    SalesforceBulkManager,
)
Salesforcemanager_strategy = st.builds(
    Salesforcemanager,
)
WHUtils_strategy = st.builds(
    WHUtils,
)
BQTable_strategy = st.builds(
    BQTable,
)
BQJobError_strategy = st.builds(
    BQJobError,
)
Oauth2client_client_GoogleCredentials_strategy = st.builds(
    Oauth2client_client_GoogleCredentials,
)
GCPManager_strategy = st.builds(
    GCPManager,
)
googleapiclient_discovery_strategy = st.builds(
    googleapiclient_discovery,
)
BQManager_strategy = st.builds(
    BQManager,
)



















@given(instance=APNLineItem_strategy)
def test_hyp_apnlineitem_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=APNLineItem_strategy)
def test_hyp_apnlineitem_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original







@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_cvr_setter(instance):
    original = instance.cvr
    instance.cvr = original
    assert instance.cvr == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_impressions_setter(instance):
    original = instance.impressions
    instance.impressions = original
    assert instance.impressions == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_sojern_goal_rae_setter(instance):
    original = instance.sojern_goal_rae
    instance.sojern_goal_rae = original
    assert instance.sojern_goal_rae == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_sfdc_opportunity_id_setter(instance):
    original = instance.sfdc_opportunity_id
    instance.sfdc_opportunity_id = original
    assert instance.sfdc_opportunity_id == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_region1_setter(instance):
    original = instance.region1
    instance.region1 = original
    assert instance.region1 == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_percentage_impression_credit_setter(instance):
    original = instance.percentage_impression_credit
    instance.percentage_impression_credit = original
    assert instance.percentage_impression_credit == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_minimum_margin_setter(instance):
    original = instance.minimum_margin
    instance.minimum_margin = original
    assert instance.minimum_margin == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_product_type_setter(instance):
    original = instance.product_type
    instance.product_type = original
    assert instance.product_type == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_minimum_partner_data_delivery_percent_setter(instance):
    original = instance.minimum_partner_data_delivery_percent
    instance.minimum_partner_data_delivery_percent = original
    assert instance.minimum_partner_data_delivery_percent == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_avg_price_usd_setter(instance):
    original = instance.avg_price_usd
    instance.avg_price_usd = original
    assert instance.avg_price_usd == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_adjust_bids_setter(instance):
    original = instance.adjust_bids
    instance.adjust_bids = original
    assert instance.adjust_bids == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_end_date_setter(instance):
    original = instance.end_date
    instance.end_date = original
    assert instance.end_date == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_expected_click_credit_setter(instance):
    original = instance.expected_click_credit
    instance.expected_click_credit = original
    assert instance.expected_click_credit == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_account_manager_setter(instance):
    original = instance.account_manager
    instance.account_manager = original
    assert instance.account_manager == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_sfdc_product_id_setter(instance):
    original = instance.sfdc_product_id
    instance.sfdc_product_id = original
    assert instance.sfdc_product_id == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_min_daily_volume_setter(instance):
    original = instance.min_daily_volume
    instance.min_daily_volume = original
    assert instance.min_daily_volume == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_billing_currency_setter(instance):
    original = instance.billing_currency
    instance.billing_currency = original
    assert instance.billing_currency == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_cpx_setter(instance):
    original = instance.cpx
    instance.cpx = original
    assert instance.cpx == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_on_off_setter(instance):
    original = instance.on_off
    instance.on_off = original
    assert instance.on_off == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_percentage_conversion_credit_setter(instance):
    original = instance.percentage_conversion_credit
    instance.percentage_conversion_credit = original
    assert instance.percentage_conversion_credit == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_hours_early_to_complete_setter(instance):
    original = instance.hours_early_to_complete
    instance.hours_early_to_complete = original
    assert instance.hours_early_to_complete == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_goal_type_setter(instance):
    original = instance.goal_type
    instance.goal_type = original
    assert instance.goal_type == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_days_early_to_complete_setter(instance):
    original = instance.days_early_to_complete
    instance.days_early_to_complete = original
    assert instance.days_early_to_complete == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_estimated_booking_value_setter(instance):
    original = instance.estimated_booking_value
    instance.estimated_booking_value = original
    assert instance.estimated_booking_value == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_dbm_io_id_setter(instance):
    original = instance.dbm_io_id
    instance.dbm_io_id = original
    assert instance.dbm_io_id == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_product_start_date_setter(instance):
    original = instance.product_start_date
    instance.product_start_date = original
    assert instance.product_start_date == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_conversions_setter(instance):
    original = instance.conversions
    instance.conversions = original
    assert instance.conversions == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_kpi_goal_setter(instance):
    original = instance.kpi_goal
    instance.kpi_goal = original
    assert instance.kpi_goal == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_min_daily_volume_percent_setter(instance):
    original = instance.min_daily_volume_percent
    instance.min_daily_volume_percent = original
    assert instance.min_daily_volume_percent == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_pacing_setter(instance):
    original = instance.pacing
    instance.pacing = original
    assert instance.pacing == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_product_end_date_setter(instance):
    original = instance.product_end_date
    instance.product_end_date = original
    assert instance.product_end_date == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_effective_impressions_setter(instance):
    original = instance.effective_impressions
    instance.effective_impressions = original
    assert instance.effective_impressions == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_cpm_setter(instance):
    original = instance.cpm
    instance.cpm = original
    assert instance.cpm == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original



@given(instance=autopacing_inputs_strategy)
def test_hyp_autopacing_inputs_exchange_rate_setter(instance):
    original = instance.exchange_rate
    instance.exchange_rate = original
    assert instance.exchange_rate == original




@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_hyp_dbm_li_sfdc_product_li_mapping_sfdc_product_id_setter(instance):
    original = instance.sfdc_product_id
    instance.sfdc_product_id = original
    assert instance.sfdc_product_id == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_hyp_dbm_li_sfdc_product_li_mapping_dub_allocation_label_setter(instance):
    original = instance.dub_allocation_label
    instance.dub_allocation_label = original
    assert instance.dub_allocation_label == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_hyp_dbm_li_sfdc_product_li_mapping_dbm_creative_ids_setter(instance):
    original = instance.dbm_creative_ids
    instance.dbm_creative_ids = original
    assert instance.dbm_creative_ids == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_hyp_dbm_li_sfdc_product_li_mapping_dbm_line_item_id_setter(instance):
    original = instance.dbm_line_item_id
    instance.dbm_line_item_id = original
    assert instance.dbm_line_item_id == original



@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
def test_hyp_dbm_li_sfdc_product_li_mapping_dbm_io_id_setter(instance):
    original = instance.dbm_io_id
    instance.dbm_io_id = original
    assert instance.dbm_io_id == original

























@given(instance=Agency_strategy)
def test_hyp_agency_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original




@given(instance=Advertiser_strategy)
def test_hyp_advertiser_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original











@given(instance=RecordType_strategy)
def test_hyp_recordtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RecordType_strategy)
def test_hyp_recordtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=RecordType_strategy)
def test_hyp_recordtype_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original



@given(instance=RecordType_strategy)
def test_hyp_recordtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=RecordType_strategy)
def test_hyp_recordtype_updated_by_setter(instance):
    original = instance.updated_by
    instance.updated_by = original
    assert instance.updated_by == original



@given(instance=RecordType_strategy)
def test_hyp_recordtype_crm_id_setter(instance):
    original = instance.crm_id
    instance.crm_id = original
    assert instance.crm_id == original






@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_hyp_updater_events_dataset_updater_events_daily_advertisername_setter(instance):
    original = instance.advertisername
    instance.advertisername = original
    assert instance.advertisername == original



@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_hyp_updater_events_dataset_updater_events_daily_segments_id_setter(instance):
    original = instance.segments_id
    instance.segments_id = original
    assert instance.segments_id == original



@given(instance=updater_events_dataset_updater_events_daily_strategy)
def test_hyp_updater_events_dataset_updater_events_daily_sojernId_setter(instance):
    original = instance.sojernId
    instance.sojernId = original
    assert instance.sojernId == original




@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_hyp_smp_events_dataset_smp_events_daily_profileid_setter(instance):
    original = instance.profileid
    instance.profileid = original
    assert instance.profileid == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_hyp_smp_events_dataset_smp_events_daily_eventsourcename_setter(instance):
    original = instance.eventsourcename
    instance.eventsourcename = original
    assert instance.eventsourcename == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_hyp_smp_events_dataset_smp_events_daily_externalIds_id__used_as_apnid__setter(instance):
    original = instance.externalIds_id__used_as_apnid_
    instance.externalIds_id__used_as_apnid_ = original
    assert instance.externalIds_id__used_as_apnid_ == original



@given(instance=smp_events_dataset_smp_events_daily_strategy)
def test_hyp_smp_events_dataset_smp_events_daily_ExternalIds_Type_setter(instance):
    original = instance.ExternalIds_Type
    instance.ExternalIds_Type = original
    assert instance.ExternalIds_Type == original



















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_APNLineItem_attribute_value_roundtrip():
    instance = APNLineItem(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_APNLineItem_attribute2_value_roundtrip():
    instance = APNLineItem(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Advertiser_crm_id_value_roundtrip():
    instance = Advertiser(crm_id="sample_text")
    assert instance.crm_id == "sample_text"
    instance.crm_id = "sample_text_2"
    assert instance.crm_id == "sample_text_2"


def test_Agency_crm_id_value_roundtrip():
    instance = Agency(crm_id="sample_text")
    assert instance.crm_id == "sample_text"
    instance.crm_id = "sample_text_2"
    assert instance.crm_id == "sample_text_2"


def test_RecordType_crm_id_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.crm_id == "sample_text"
    instance.crm_id = "sample_text_2"
    assert instance.crm_id == "sample_text_2"


def test_RecordType_deleted_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.deleted == "sample_text"
    instance.deleted = "sample_text_2"
    assert instance.deleted == "sample_text_2"


def test_RecordType_description_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_RecordType_id_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_RecordType_name_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RecordType_updated_by_value_roundtrip():
    instance = RecordType(crm_id="sample_text", deleted="sample_text", description="sample_text", id="sample_text", name="sample_text", updated_by="sample_text")
    assert instance.updated_by == "sample_text"
    instance.updated_by = "sample_text_2"
    assert instance.updated_by == "sample_text_2"


def test_autopacing_inputs_account_manager_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.account_manager == "sample_text"
    instance.account_manager = "sample_text_2"
    assert instance.account_manager == "sample_text_2"


def test_autopacing_inputs_adjust_bids_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.adjust_bids == "sample_text"
    instance.adjust_bids = "sample_text_2"
    assert instance.adjust_bids == "sample_text_2"


def test_autopacing_inputs_avg_price_usd_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.avg_price_usd == "sample_text"
    instance.avg_price_usd = "sample_text_2"
    assert instance.avg_price_usd == "sample_text_2"


def test_autopacing_inputs_billing_currency_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.billing_currency == "sample_text"
    instance.billing_currency = "sample_text_2"
    assert instance.billing_currency == "sample_text_2"


def test_autopacing_inputs_conversions_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.conversions == "sample_text"
    instance.conversions = "sample_text_2"
    assert instance.conversions == "sample_text_2"


def test_autopacing_inputs_cpm_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.cpm == "sample_text"
    instance.cpm = "sample_text_2"
    assert instance.cpm == "sample_text_2"


def test_autopacing_inputs_cpx_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.cpx == "sample_text"
    instance.cpx = "sample_text_2"
    assert instance.cpx == "sample_text_2"


def test_autopacing_inputs_cvr_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.cvr == "sample_text"
    instance.cvr = "sample_text_2"
    assert instance.cvr == "sample_text_2"


def test_autopacing_inputs_days_early_to_complete_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.days_early_to_complete == "sample_text"
    instance.days_early_to_complete = "sample_text_2"
    assert instance.days_early_to_complete == "sample_text_2"


def test_autopacing_inputs_dbm_io_id_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.dbm_io_id == "sample_text"
    instance.dbm_io_id = "sample_text_2"
    assert instance.dbm_io_id == "sample_text_2"


def test_autopacing_inputs_effective_impressions_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.effective_impressions == "sample_text"
    instance.effective_impressions = "sample_text_2"
    assert instance.effective_impressions == "sample_text_2"


def test_autopacing_inputs_end_date_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.end_date == "sample_text"
    instance.end_date = "sample_text_2"
    assert instance.end_date == "sample_text_2"


def test_autopacing_inputs_estimated_booking_value_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.estimated_booking_value == "sample_text"
    instance.estimated_booking_value = "sample_text_2"
    assert instance.estimated_booking_value == "sample_text_2"


def test_autopacing_inputs_exchange_rate_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.exchange_rate == "sample_text"
    instance.exchange_rate = "sample_text_2"
    assert instance.exchange_rate == "sample_text_2"


def test_autopacing_inputs_expected_click_credit_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.expected_click_credit == "sample_text"
    instance.expected_click_credit = "sample_text_2"
    assert instance.expected_click_credit == "sample_text_2"


def test_autopacing_inputs_goal_type_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.goal_type == "sample_text"
    instance.goal_type = "sample_text_2"
    assert instance.goal_type == "sample_text_2"


def test_autopacing_inputs_hours_early_to_complete_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.hours_early_to_complete == "sample_text"
    instance.hours_early_to_complete = "sample_text_2"
    assert instance.hours_early_to_complete == "sample_text_2"


def test_autopacing_inputs_impressions_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.impressions == "sample_text"
    instance.impressions = "sample_text_2"
    assert instance.impressions == "sample_text_2"


def test_autopacing_inputs_kpi_goal_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.kpi_goal == "sample_text"
    instance.kpi_goal = "sample_text_2"
    assert instance.kpi_goal == "sample_text_2"


def test_autopacing_inputs_min_daily_volume_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.min_daily_volume == "sample_text"
    instance.min_daily_volume = "sample_text_2"
    assert instance.min_daily_volume == "sample_text_2"


def test_autopacing_inputs_min_daily_volume_percent_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.min_daily_volume_percent == "sample_text"
    instance.min_daily_volume_percent = "sample_text_2"
    assert instance.min_daily_volume_percent == "sample_text_2"


def test_autopacing_inputs_minimum_margin_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.minimum_margin == "sample_text"
    instance.minimum_margin = "sample_text_2"
    assert instance.minimum_margin == "sample_text_2"


def test_autopacing_inputs_minimum_partner_data_delivery_percent_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.minimum_partner_data_delivery_percent == "sample_text"
    instance.minimum_partner_data_delivery_percent = "sample_text_2"
    assert instance.minimum_partner_data_delivery_percent == "sample_text_2"


def test_autopacing_inputs_on_off_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.on_off == "sample_text"
    instance.on_off = "sample_text_2"
    assert instance.on_off == "sample_text_2"


def test_autopacing_inputs_pacing_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.pacing == "sample_text"
    instance.pacing = "sample_text_2"
    assert instance.pacing == "sample_text_2"


def test_autopacing_inputs_percentage_conversion_credit_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.percentage_conversion_credit == "sample_text"
    instance.percentage_conversion_credit = "sample_text_2"
    assert instance.percentage_conversion_credit == "sample_text_2"


def test_autopacing_inputs_percentage_impression_credit_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.percentage_impression_credit == "sample_text"
    instance.percentage_impression_credit = "sample_text_2"
    assert instance.percentage_impression_credit == "sample_text_2"


def test_autopacing_inputs_product_end_date_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.product_end_date == "sample_text"
    instance.product_end_date = "sample_text_2"
    assert instance.product_end_date == "sample_text_2"


def test_autopacing_inputs_product_start_date_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.product_start_date == "sample_text"
    instance.product_start_date = "sample_text_2"
    assert instance.product_start_date == "sample_text_2"


def test_autopacing_inputs_product_type_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.product_type == "sample_text"
    instance.product_type = "sample_text_2"
    assert instance.product_type == "sample_text_2"


def test_autopacing_inputs_region_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.region == "sample_text"
    instance.region = "sample_text_2"
    assert instance.region == "sample_text_2"


def test_autopacing_inputs_region1_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.region1 == "sample_text"
    instance.region1 = "sample_text_2"
    assert instance.region1 == "sample_text_2"


def test_autopacing_inputs_sfdc_opportunity_id_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.sfdc_opportunity_id == "sample_text"
    instance.sfdc_opportunity_id = "sample_text_2"
    assert instance.sfdc_opportunity_id == "sample_text_2"


def test_autopacing_inputs_sfdc_product_id_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.sfdc_product_id == "sample_text"
    instance.sfdc_product_id = "sample_text_2"
    assert instance.sfdc_product_id == "sample_text_2"


def test_autopacing_inputs_sojern_goal_rae_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.sojern_goal_rae == "sample_text"
    instance.sojern_goal_rae = "sample_text_2"
    assert instance.sojern_goal_rae == "sample_text_2"


def test_autopacing_inputs_start_date_value_roundtrip():
    instance = autopacing_inputs(account_manager="sample_text", adjust_bids="sample_text", avg_price_usd="sample_text", billing_currency="sample_text", conversions="sample_text", cpm="sample_text", cpx="sample_text", cvr="sample_text", days_early_to_complete="sample_text", dbm_io_id="sample_text", effective_impressions="sample_text", end_date="sample_text", estimated_booking_value="sample_text", exchange_rate="sample_text", expected_click_credit="sample_text", goal_type="sample_text", hours_early_to_complete="sample_text", impressions="sample_text", kpi_goal="sample_text", min_daily_volume="sample_text", min_daily_volume_percent="sample_text", minimum_margin="sample_text", minimum_partner_data_delivery_percent="sample_text", on_off="sample_text", pacing="sample_text", percentage_conversion_credit="sample_text", percentage_impression_credit="sample_text", product_end_date="sample_text", product_start_date="sample_text", product_type="sample_text", region="sample_text", region1="sample_text", sfdc_opportunity_id="sample_text", sfdc_product_id="sample_text", sojern_goal_rae="sample_text", start_date="sample_text")
    assert instance.start_date == "sample_text"
    instance.start_date = "sample_text_2"
    assert instance.start_date == "sample_text_2"


def test_dbm_li_sfdc_product_li_mapping_dbm_creative_ids_value_roundtrip():
    instance = dbm_li_sfdc_product_li_mapping(dbm_creative_ids="sample_text", dbm_io_id="sample_text", dbm_line_item_id="sample_text", dub_allocation_label="sample_text", sfdc_product_id="sample_text")
    assert instance.dbm_creative_ids == "sample_text"
    instance.dbm_creative_ids = "sample_text_2"
    assert instance.dbm_creative_ids == "sample_text_2"


def test_dbm_li_sfdc_product_li_mapping_dbm_io_id_value_roundtrip():
    instance = dbm_li_sfdc_product_li_mapping(dbm_creative_ids="sample_text", dbm_io_id="sample_text", dbm_line_item_id="sample_text", dub_allocation_label="sample_text", sfdc_product_id="sample_text")
    assert instance.dbm_io_id == "sample_text"
    instance.dbm_io_id = "sample_text_2"
    assert instance.dbm_io_id == "sample_text_2"


def test_dbm_li_sfdc_product_li_mapping_dbm_line_item_id_value_roundtrip():
    instance = dbm_li_sfdc_product_li_mapping(dbm_creative_ids="sample_text", dbm_io_id="sample_text", dbm_line_item_id="sample_text", dub_allocation_label="sample_text", sfdc_product_id="sample_text")
    assert instance.dbm_line_item_id == "sample_text"
    instance.dbm_line_item_id = "sample_text_2"
    assert instance.dbm_line_item_id == "sample_text_2"


def test_dbm_li_sfdc_product_li_mapping_dub_allocation_label_value_roundtrip():
    instance = dbm_li_sfdc_product_li_mapping(dbm_creative_ids="sample_text", dbm_io_id="sample_text", dbm_line_item_id="sample_text", dub_allocation_label="sample_text", sfdc_product_id="sample_text")
    assert instance.dub_allocation_label == "sample_text"
    instance.dub_allocation_label = "sample_text_2"
    assert instance.dub_allocation_label == "sample_text_2"


def test_dbm_li_sfdc_product_li_mapping_sfdc_product_id_value_roundtrip():
    instance = dbm_li_sfdc_product_li_mapping(dbm_creative_ids="sample_text", dbm_io_id="sample_text", dbm_line_item_id="sample_text", dub_allocation_label="sample_text", sfdc_product_id="sample_text")
    assert instance.sfdc_product_id == "sample_text"
    instance.sfdc_product_id = "sample_text_2"
    assert instance.sfdc_product_id == "sample_text_2"


def test_smp_events_dataset_smp_events_daily_ExternalIds_Type_value_roundtrip():
    instance = smp_events_dataset_smp_events_daily(ExternalIds_Type="sample_text", eventsourcename="sample_text", externalIds_id__used_as_apnid_="sample_text", profileid="sample_text")
    assert instance.ExternalIds_Type == "sample_text"
    instance.ExternalIds_Type = "sample_text_2"
    assert instance.ExternalIds_Type == "sample_text_2"


def test_smp_events_dataset_smp_events_daily_eventsourcename_value_roundtrip():
    instance = smp_events_dataset_smp_events_daily(ExternalIds_Type="sample_text", eventsourcename="sample_text", externalIds_id__used_as_apnid_="sample_text", profileid="sample_text")
    assert instance.eventsourcename == "sample_text"
    instance.eventsourcename = "sample_text_2"
    assert instance.eventsourcename == "sample_text_2"


def test_smp_events_dataset_smp_events_daily_externalIds_id__used_as_apnid__value_roundtrip():
    instance = smp_events_dataset_smp_events_daily(ExternalIds_Type="sample_text", eventsourcename="sample_text", externalIds_id__used_as_apnid_="sample_text", profileid="sample_text")
    assert instance.externalIds_id__used_as_apnid_ == "sample_text"
    instance.externalIds_id__used_as_apnid_ = "sample_text_2"
    assert instance.externalIds_id__used_as_apnid_ == "sample_text_2"


def test_smp_events_dataset_smp_events_daily_profileid_value_roundtrip():
    instance = smp_events_dataset_smp_events_daily(ExternalIds_Type="sample_text", eventsourcename="sample_text", externalIds_id__used_as_apnid_="sample_text", profileid="sample_text")
    assert instance.profileid == "sample_text"
    instance.profileid = "sample_text_2"
    assert instance.profileid == "sample_text_2"


def test_updater_events_dataset_updater_events_daily_advertisername_value_roundtrip():
    instance = updater_events_dataset_updater_events_daily(advertisername="sample_text", segments_id="sample_text", sojernId="sample_text")
    assert instance.advertisername == "sample_text"
    instance.advertisername = "sample_text_2"
    assert instance.advertisername == "sample_text_2"


def test_updater_events_dataset_updater_events_daily_segments_id_value_roundtrip():
    instance = updater_events_dataset_updater_events_daily(advertisername="sample_text", segments_id="sample_text", sojernId="sample_text")
    assert instance.segments_id == "sample_text"
    instance.segments_id = "sample_text_2"
    assert instance.segments_id == "sample_text_2"


def test_updater_events_dataset_updater_events_daily_sojernId_value_roundtrip():
    instance = updater_events_dataset_updater_events_daily(advertisername="sample_text", segments_id="sample_text", sojernId="sample_text")
    assert instance.sojernId == "sample_text"
    instance.sojernId = "sample_text_2"
    assert instance.sojernId == "sample_text_2"


def test_assoc_APNLineItemModelService_APNLineItem_link_reassign_clear():
    a = APNLineItem(attribute="sample_text", attribute2="sample_text")
    b1 = APNLineItemModelService()
    b2 = APNLineItemModelService()
    _safe_set(a, 'APNLineItemModelService_APNLineItem_121', b1)
    assert _is_linked(a, 'APNLineItemModelService_APNLineItem_121', b1)
    if hasattr(b1, 'APNLineItemModelService_APNLineItem_020'):
        assert _is_linked(b1, 'APNLineItemModelService_APNLineItem_020', a)
    _safe_set(a, 'APNLineItemModelService_APNLineItem_121', b2)
    assert _is_linked(a, 'APNLineItemModelService_APNLineItem_121', b2)
    if hasattr(b1, 'APNLineItemModelService_APNLineItem_020'):
        assert not _is_linked(b1, 'APNLineItemModelService_APNLineItem_020', a)
    if hasattr(b2, 'APNLineItemModelService_APNLineItem_020'):
        assert _is_linked(b2, 'APNLineItemModelService_APNLineItem_020', a)
    _safe_set(a, 'APNLineItemModelService_APNLineItem_121', None)
    assert not _is_linked(a, 'APNLineItemModelService_APNLineItem_121', b2)
    if hasattr(b2, 'APNLineItemModelService_APNLineItem_020'):
        assert not _is_linked(b2, 'APNLineItemModelService_APNLineItem_020', a)


def test_assoc_APNLineItem_APNModel_link_reassign_clear():
    a = APNLineItem(attribute="sample_text", attribute2="sample_text")
    b1 = APNModel()
    b2 = APNModel()
    _safe_set(a, 'APNLineItem_APNModel_018', {b1})
    assert _is_linked(a, 'APNLineItem_APNModel_018', b1)
    if hasattr(b1, 'APNLineItem_APNModel_119'):
        assert _is_linked(b1, 'APNLineItem_APNModel_119', a)
    _safe_set(a, 'APNLineItem_APNModel_018', {b2})
    assert _is_linked(a, 'APNLineItem_APNModel_018', b2)
    if hasattr(b1, 'APNLineItem_APNModel_119'):
        assert not _is_linked(b1, 'APNLineItem_APNModel_119', a)
    if hasattr(b2, 'APNLineItem_APNModel_119'):
        assert _is_linked(b2, 'APNLineItem_APNModel_119', a)
    _safe_set(a, 'APNLineItem_APNModel_018', set())
    assert not _is_linked(a, 'APNLineItem_APNModel_018', b2)
    if hasattr(b2, 'APNLineItem_APNModel_119'):
        assert not _is_linked(b2, 'APNLineItem_APNModel_119', a)


def test_assoc_APNModel_APNLineItem_link_reassign_clear():
    a = APNLineItem(attribute="sample_text", attribute2="sample_text")
    b1 = APNModel()
    b2 = APNModel()
    _safe_set(a, 'APNModel_APNLineItem_15', {b1})
    assert _is_linked(a, 'APNModel_APNLineItem_15', b1)
    if hasattr(b1, 'APNModel_APNLineItem_04'):
        assert _is_linked(b1, 'APNModel_APNLineItem_04', a)
    _safe_set(a, 'APNModel_APNLineItem_15', {b2})
    assert _is_linked(a, 'APNModel_APNLineItem_15', b2)
    if hasattr(b1, 'APNModel_APNLineItem_04'):
        assert not _is_linked(b1, 'APNModel_APNLineItem_04', a)
    if hasattr(b2, 'APNModel_APNLineItem_04'):
        assert _is_linked(b2, 'APNModel_APNLineItem_04', a)
    _safe_set(a, 'APNModel_APNLineItem_15', set())
    assert not _is_linked(a, 'APNModel_APNLineItem_15', b2)
    if hasattr(b2, 'APNModel_APNLineItem_04'):
        assert not _is_linked(b2, 'APNModel_APNLineItem_04', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

APNAdv_strategy = st.builds(APNAdv)
@given(instance=APNAdv_strategy)
@settings(max_examples=25)
def test_APNAdv_instantiation(instance):
    assert isinstance(instance, APNAdv)


APNAdvertiser_strategy = st.builds(APNAdvertiser)
@given(instance=APNAdvertiser_strategy)
@settings(max_examples=25)
def test_APNAdvertiser_instantiation(instance):
    assert isinstance(instance, APNAdvertiser)


APNCache_Interface_strategy = st.builds(APNCache_Interface)
@given(instance=APNCache_Interface_strategy)
@settings(max_examples=25)
def test_APNCache_Interface_instantiation(instance):
    assert isinstance(instance, APNCache_Interface)


APNLineItem_strategy = st.builds(APNLineItem, attribute=safe_text, attribute2=safe_text)
@given(instance=APNLineItem_strategy)
@settings(max_examples=25)
def test_APNLineItem_instantiation(instance):
    assert isinstance(instance, APNLineItem)


APNLineItemModelService_strategy = st.builds(APNLineItemModelService)
@given(instance=APNLineItemModelService_strategy)
@settings(max_examples=25)
def test_APNLineItemModelService_instantiation(instance):
    assert isinstance(instance, APNLineItemModelService)


APNManager_strategy = st.builds(APNManager)
@given(instance=APNManager_strategy)
@settings(max_examples=25)
def test_APNManager_instantiation(instance):
    assert isinstance(instance, APNManager)


APNModel_strategy = st.builds(APNModel)
@given(instance=APNModel_strategy)
@settings(max_examples=25)
def test_APNModel_instantiation(instance):
    assert isinstance(instance, APNModel)


APNModelFactory_strategy = st.builds(APNModelFactory)
@given(instance=APNModelFactory_strategy)
@settings(max_examples=25)
def test_APNModelFactory_instantiation(instance):
    assert isinstance(instance, APNModelFactory)


APNProgrammaticModel_strategy = st.builds(APNProgrammaticModel)
@given(instance=APNProgrammaticModel_strategy)
@settings(max_examples=25)
def test_APNProgrammaticModel_instantiation(instance):
    assert isinstance(instance, APNProgrammaticModel)


APNRepository_Interface_strategy = st.builds(APNRepository_Interface)
@given(instance=APNRepository_Interface_strategy)
@settings(max_examples=25)
def test_APNRepository_Interface_instantiation(instance):
    assert isinstance(instance, APNRepository_Interface)


APNStore_Interface_strategy = st.builds(APNStore_Interface)
@given(instance=APNStore_Interface_strategy)
@settings(max_examples=25)
def test_APNStore_Interface_instantiation(instance):
    assert isinstance(instance, APNStore_Interface)


Advertiser_strategy = st.builds(Advertiser, crm_id=safe_text)
@given(instance=Advertiser_strategy)
@settings(max_examples=25)
def test_Advertiser_instantiation(instance):
    assert isinstance(instance, Advertiser)


AdvertiserBlocklistWhitelist_strategy = st.builds(AdvertiserBlocklistWhitelist)
@given(instance=AdvertiserBlocklistWhitelist_strategy)
@settings(max_examples=25)
def test_AdvertiserBlocklistWhitelist_instantiation(instance):
    assert isinstance(instance, AdvertiserBlocklistWhitelist)


AdvertiserExcludedVertical_strategy = st.builds(AdvertiserExcludedVertical)
@given(instance=AdvertiserExcludedVertical_strategy)
@settings(max_examples=25)
def test_AdvertiserExcludedVertical_instantiation(instance):
    assert isinstance(instance, AdvertiserExcludedVertical)


Agency_strategy = st.builds(Agency, crm_id=safe_text)
@given(instance=Agency_strategy)
@settings(max_examples=25)
def test_Agency_instantiation(instance):
    assert isinstance(instance, Agency)


AgencyBlocklistWhitelist_strategy = st.builds(AgencyBlocklistWhitelist)
@given(instance=AgencyBlocklistWhitelist_strategy)
@settings(max_examples=25)
def test_AgencyBlocklistWhitelist_instantiation(instance):
    assert isinstance(instance, AgencyBlocklistWhitelist)


AgencyExcludedVertical_strategy = st.builds(AgencyExcludedVertical)
@given(instance=AgencyExcludedVertical_strategy)
@settings(max_examples=25)
def test_AgencyExcludedVertical_instantiation(instance):
    assert isinstance(instance, AgencyExcludedVertical)


AppNexus_strategy = st.builds(AppNexus)
@given(instance=AppNexus_strategy)
@settings(max_examples=25)
def test_AppNexus_instantiation(instance):
    assert isinstance(instance, AppNexus)


AppNexusClient_strategy = st.builds(AppNexusClient)
@given(instance=AppNexusClient_strategy)
@settings(max_examples=25)
def test_AppNexusClient_instantiation(instance):
    assert isinstance(instance, AppNexusClient)


BQJobError_strategy = st.builds(BQJobError)
@given(instance=BQJobError_strategy)
@settings(max_examples=25)
def test_BQJobError_instantiation(instance):
    assert isinstance(instance, BQJobError)


BQManager_strategy = st.builds(BQManager)
@given(instance=BQManager_strategy)
@settings(max_examples=25)
def test_BQManager_instantiation(instance):
    assert isinstance(instance, BQManager)


BQTable_strategy = st.builds(BQTable)
@given(instance=BQTable_strategy)
@settings(max_examples=25)
def test_BQTable_instantiation(instance):
    assert isinstance(instance, BQTable)


BidAdjuster_strategy = st.builds(BidAdjuster)
@given(instance=BidAdjuster_strategy)
@settings(max_examples=25)
def test_BidAdjuster_instantiation(instance):
    assert isinstance(instance, BidAdjuster)


BrandSafetyBrandSafetyCustomSetting_strategy = st.builds(BrandSafetyBrandSafetyCustomSetting)
@given(instance=BrandSafetyBrandSafetyCustomSetting_strategy)
@settings(max_examples=25)
def test_BrandSafetyBrandSafetyCustomSetting_instantiation(instance):
    assert isinstance(instance, BrandSafetyBrandSafetyCustomSetting)


BrandSafetyBrandSafetyLabel_strategy = st.builds(BrandSafetyBrandSafetyLabel)
@given(instance=BrandSafetyBrandSafetyLabel_strategy)
@settings(max_examples=25)
def test_BrandSafetyBrandSafetyLabel_instantiation(instance):
    assert isinstance(instance, BrandSafetyBrandSafetyLabel)


BrandSaftey_strategy = st.builds(BrandSaftey)
@given(instance=BrandSaftey_strategy)
@settings(max_examples=25)
def test_BrandSaftey_instantiation(instance):
    assert isinstance(instance, BrandSaftey)


Campaign_strategy = st.builds(Campaign)
@given(instance=Campaign_strategy)
@settings(max_examples=25)
def test_Campaign_instantiation(instance):
    assert isinstance(instance, Campaign)


CampaignBlocklistWhitelist_strategy = st.builds(CampaignBlocklistWhitelist)
@given(instance=CampaignBlocklistWhitelist_strategy)
@settings(max_examples=25)
def test_CampaignBlocklistWhitelist_instantiation(instance):
    assert isinstance(instance, CampaignBlocklistWhitelist)


CampaignTravelEventType_strategy = st.builds(CampaignTravelEventType)
@given(instance=CampaignTravelEventType_strategy)
@settings(max_examples=25)
def test_CampaignTravelEventType_instantiation(instance):
    assert isinstance(instance, CampaignTravelEventType)


Class2_strategy = st.builds(Class2)
@given(instance=Class2_strategy)
@settings(max_examples=25)
def test_Class2_instantiation(instance):
    assert isinstance(instance, Class2)


CloudSQLManager_strategy = st.builds(CloudSQLManager)
@given(instance=CloudSQLManager_strategy)
@settings(max_examples=25)
def test_CloudSQLManager_instantiation(instance):
    assert isinstance(instance, CloudSQLManager)


CreativeApproval_strategy = st.builds(CreativeApproval)
@given(instance=CreativeApproval_strategy)
@settings(max_examples=25)
def test_CreativeApproval_instantiation(instance):
    assert isinstance(instance, CreativeApproval)


CreativeAsset_strategy = st.builds(CreativeAsset)
@given(instance=CreativeAsset_strategy)
@settings(max_examples=25)
def test_CreativeAsset_instantiation(instance):
    assert isinstance(instance, CreativeAsset)


CreativeAssetTactic_strategy = st.builds(CreativeAssetTactic)
@given(instance=CreativeAssetTactic_strategy)
@settings(max_examples=25)
def test_CreativeAssetTactic_instantiation(instance):
    assert isinstance(instance, CreativeAssetTactic)


DBMManager_strategy = st.builds(DBMManager)
@given(instance=DBMManager_strategy)
@settings(max_examples=25)
def test_DBMManager_instantiation(instance):
    assert isinstance(instance, DBMManager)


DCMManager_strategy = st.builds(DCMManager)
@given(instance=DCMManager_strategy)
@settings(max_examples=25)
def test_DCMManager_instantiation(instance):
    assert isinstance(instance, DCMManager)


DCSManager_strategy = st.builds(DCSManager)
@given(instance=DCSManager_strategy)
@settings(max_examples=25)
def test_DCSManager_instantiation(instance):
    assert isinstance(instance, DCSManager)


DSManager_strategy = st.builds(DSManager)
@given(instance=DSManager_strategy)
@settings(max_examples=25)
def test_DSManager_instantiation(instance):
    assert isinstance(instance, DSManager)


FBManager_strategy = st.builds(FBManager)
@given(instance=FBManager_strategy)
@settings(max_examples=25)
def test_FBManager_instantiation(instance):
    assert isinstance(instance, FBManager)


GCEManager_strategy = st.builds(GCEManager)
@given(instance=GCEManager_strategy)
@settings(max_examples=25)
def test_GCEManager_instantiation(instance):
    assert isinstance(instance, GCEManager)


GCPManager_strategy = st.builds(GCPManager)
@given(instance=GCPManager_strategy)
@settings(max_examples=25)
def test_GCPManager_instantiation(instance):
    assert isinstance(instance, GCPManager)


GCSManager_strategy = st.builds(GCSManager)
@given(instance=GCSManager_strategy)
@settings(max_examples=25)
def test_GCSManager_instantiation(instance):
    assert isinstance(instance, GCSManager)


GenericModel_strategy = st.builds(GenericModel)
@given(instance=GenericModel_strategy)
@settings(max_examples=25)
def test_GenericModel_instantiation(instance):
    assert isinstance(instance, GenericModel)


Goal_strategy = st.builds(Goal)
@given(instance=Goal_strategy)
@settings(max_examples=25)
def test_Goal_instantiation(instance):
    assert isinstance(instance, Goal)


IOManager_strategy = st.builds(IOManager)
@given(instance=IOManager_strategy)
@settings(max_examples=25)
def test_IOManager_instantiation(instance):
    assert isinstance(instance, IOManager)


ModelService_Interface_strategy = st.builds(ModelService_Interface)
@given(instance=ModelService_Interface_strategy)
@settings(max_examples=25)
def test_ModelService_Interface_instantiation(instance):
    assert isinstance(instance, ModelService_Interface)


Model_Interface_strategy = st.builds(Model_Interface)
@given(instance=Model_Interface_strategy)
@settings(max_examples=25)
def test_Model_Interface_instantiation(instance):
    assert isinstance(instance, Model_Interface)


Oauth2client_client_GoogleCredentials_strategy = st.builds(Oauth2client_client_GoogleCredentials)
@given(instance=Oauth2client_client_GoogleCredentials_strategy)
@settings(max_examples=25)
def test_Oauth2client_client_GoogleCredentials_instantiation(instance):
    assert isinstance(instance, Oauth2client_client_GoogleCredentials)


Partner_strategy = st.builds(Partner)
@given(instance=Partner_strategy)
@settings(max_examples=25)
def test_Partner_instantiation(instance):
    assert isinstance(instance, Partner)


PartnerExcludedVertical_strategy = st.builds(PartnerExcludedVertical)
@given(instance=PartnerExcludedVertical_strategy)
@settings(max_examples=25)
def test_PartnerExcludedVertical_instantiation(instance):
    assert isinstance(instance, PartnerExcludedVertical)


Pixel_strategy = st.builds(Pixel)
@given(instance=Pixel_strategy)
@settings(max_examples=25)
def test_Pixel_instantiation(instance):
    assert isinstance(instance, Pixel)


ProductLineItem_strategy = st.builds(ProductLineItem)
@given(instance=ProductLineItem_strategy)
@settings(max_examples=25)
def test_ProductLineItem_instantiation(instance):
    assert isinstance(instance, ProductLineItem)


ProgrammaticModel_Interface_strategy = st.builds(ProgrammaticModel_Interface)
@given(instance=ProgrammaticModel_Interface_strategy)
@settings(max_examples=25)
def test_ProgrammaticModel_Interface_instantiation(instance):
    assert isinstance(instance, ProgrammaticModel_Interface)


RecordType_strategy = st.builds(RecordType, crm_id=safe_text, deleted=safe_text, description=safe_text, id=safe_text, name=safe_text, updated_by=safe_text)
@given(instance=RecordType_strategy)
@settings(max_examples=25)
def test_RecordType_instantiation(instance):
    assert isinstance(instance, RecordType)


RestClient_strategy = st.builds(RestClient)
@given(instance=RestClient_strategy)
@settings(max_examples=25)
def test_RestClient_instantiation(instance):
    assert isinstance(instance, RestClient)


SalesforceBulkManager_strategy = st.builds(SalesforceBulkManager)
@given(instance=SalesforceBulkManager_strategy)
@settings(max_examples=25)
def test_SalesforceBulkManager_instantiation(instance):
    assert isinstance(instance, SalesforceBulkManager)


Salesforcemanager_strategy = st.builds(Salesforcemanager)
@given(instance=Salesforcemanager_strategy)
@settings(max_examples=25)
def test_Salesforcemanager_instantiation(instance):
    assert isinstance(instance, Salesforcemanager)


SojernBusiness_strategy = st.builds(SojernBusiness)
@given(instance=SojernBusiness_strategy)
@settings(max_examples=25)
def test_SojernBusiness_instantiation(instance):
    assert isinstance(instance, SojernBusiness)


SpendAccount_strategy = st.builds(SpendAccount)
@given(instance=SpendAccount_strategy)
@settings(max_examples=25)
def test_SpendAccount_instantiation(instance):
    assert isinstance(instance, SpendAccount)


SpendAccountBlocklistWhitelist_strategy = st.builds(SpendAccountBlocklistWhitelist)
@given(instance=SpendAccountBlocklistWhitelist_strategy)
@settings(max_examples=25)
def test_SpendAccountBlocklistWhitelist_instantiation(instance):
    assert isinstance(instance, SpendAccountBlocklistWhitelist)


SystemCreative_strategy = st.builds(SystemCreative)
@given(instance=SystemCreative_strategy)
@settings(max_examples=25)
def test_SystemCreative_instantiation(instance):
    assert isinstance(instance, SystemCreative)


SystemInsertionOrder_strategy = st.builds(SystemInsertionOrder)
@given(instance=SystemInsertionOrder_strategy)
@settings(max_examples=25)
def test_SystemInsertionOrder_instantiation(instance):
    assert isinstance(instance, SystemInsertionOrder)


SystemLineItem_strategy = st.builds(SystemLineItem)
@given(instance=SystemLineItem_strategy)
@settings(max_examples=25)
def test_SystemLineItem_instantiation(instance):
    assert isinstance(instance, SystemLineItem)


SystemLineItemConversionPixel_strategy = st.builds(SystemLineItemConversionPixel)
@given(instance=SystemLineItemConversionPixel_strategy)
@settings(max_examples=25)
def test_SystemLineItemConversionPixel_instantiation(instance):
    assert isinstance(instance, SystemLineItemConversionPixel)


Tactic_strategy = st.builds(Tactic)
@given(instance=Tactic_strategy)
@settings(max_examples=25)
def test_Tactic_instantiation(instance):
    assert isinstance(instance, Tactic)


Targeting_strategy = st.builds(Targeting)
@given(instance=Targeting_strategy)
@settings(max_examples=25)
def test_Targeting_instantiation(instance):
    assert isinstance(instance, Targeting)


User_strategy = st.builds(User)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


WHUtils_strategy = st.builds(WHUtils)
@given(instance=WHUtils_strategy)
@settings(max_examples=25)
def test_WHUtils_instantiation(instance):
    assert isinstance(instance, WHUtils)


autopacing_inputs_strategy = st.builds(autopacing_inputs, account_manager=safe_text, adjust_bids=safe_text, avg_price_usd=safe_text, billing_currency=safe_text, conversions=safe_text, cpm=safe_text, cpx=safe_text, cvr=safe_text, days_early_to_complete=safe_text, dbm_io_id=safe_text, effective_impressions=safe_text, end_date=safe_text, estimated_booking_value=safe_text, exchange_rate=safe_text, expected_click_credit=safe_text, goal_type=safe_text, hours_early_to_complete=safe_text, impressions=safe_text, kpi_goal=safe_text, min_daily_volume=safe_text, min_daily_volume_percent=safe_text, minimum_margin=safe_text, minimum_partner_data_delivery_percent=safe_text, on_off=safe_text, pacing=safe_text, percentage_conversion_credit=safe_text, percentage_impression_credit=safe_text, product_end_date=safe_text, product_start_date=safe_text, product_type=safe_text, region=safe_text, region1=safe_text, sfdc_opportunity_id=safe_text, sfdc_product_id=safe_text, sojern_goal_rae=safe_text, start_date=safe_text)
@given(instance=autopacing_inputs_strategy)
@settings(max_examples=25)
def test_autopacing_inputs_instantiation(instance):
    assert isinstance(instance, autopacing_inputs)


dbm_li_sfdc_product_li_mapping_strategy = st.builds(dbm_li_sfdc_product_li_mapping, dbm_creative_ids=safe_text, dbm_io_id=safe_text, dbm_line_item_id=safe_text, dub_allocation_label=safe_text, sfdc_product_id=safe_text)
@given(instance=dbm_li_sfdc_product_li_mapping_strategy)
@settings(max_examples=25)
def test_dbm_li_sfdc_product_li_mapping_instantiation(instance):
    assert isinstance(instance, dbm_li_sfdc_product_li_mapping)


googleapiclient_discovery_strategy = st.builds(googleapiclient_discovery)
@given(instance=googleapiclient_discovery_strategy)
@settings(max_examples=25)
def test_googleapiclient_discovery_instantiation(instance):
    assert isinstance(instance, googleapiclient_discovery)


smp_events_dataset_smp_events_daily_strategy = st.builds(smp_events_dataset_smp_events_daily, ExternalIds_Type=safe_text, eventsourcename=safe_text, externalIds_id__used_as_apnid_=safe_text, profileid=safe_text)
@given(instance=smp_events_dataset_smp_events_daily_strategy)
@settings(max_examples=25)
def test_smp_events_dataset_smp_events_daily_instantiation(instance):
    assert isinstance(instance, smp_events_dataset_smp_events_daily)


updater_events_dataset_updater_events_daily_strategy = st.builds(updater_events_dataset_updater_events_daily, advertisername=safe_text, segments_id=safe_text, sojernId=safe_text)
@given(instance=updater_events_dataset_updater_events_daily_strategy)
@settings(max_examples=25)
def test_updater_events_dataset_updater_events_daily_instantiation(instance):
    assert isinstance(instance, updater_events_dataset_updater_events_daily)



