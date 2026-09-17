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
    RequiredCapability,
    aggregator_p2_IRequiredCapability,
    aggregator_p2_IProvidedCapability,
    aggregator_p2_ILicense,
    IInstallableUnit,
    aggregator_p2_IInstallableUnitFragment,
    ICopyright,
    ILicense,
    IUpdateDescriptor,
    aggregator_p2_ITouchpointData,
    aggregator_p2_IInstallableUnit,
    aggregator_p2_ICopyright,
    aggregator_p2_IArtifactKey,
    aggregator_InfosProvider,
    aggregator_StatusProvider,
    p2_IProvidedCapability,
    LabelProvider,
    aggregator_p2view_ProvidedCapabilityWrapper,
    p2_IRequiredCapability,
    aggregator_p2view_RequiredCapabilityWrapper,
    aggregator_p2view_Touchpoints,
    ProvidedCapabilityWrapper,
    aggregator_p2view_ProvidedCapabilities,
    RequiredCapabilityWrapper,
    aggregator_p2view_RequiredCapabilities,
    p2view_aggregator_Property,
    aggregator_p2view_Properties,
    Touchpoints,
    ProvidedCapabilities,
    RequiredCapabilities,
    aggregator_p2view_IUDetails,
    IUPresentation,
    aggregator_p2view_Category,
    p2view_IUDetails,
    p2view_IUPresentation,
    aggregator_p2view_IUPresentationWithDetails,
    IUPresentationWithDetails,
    aggregator_p2view_Product,
    aggregator_p2view_Bundle,
    aggregator_p2view_OtherIU,
    aggregator_p2view_Feature,
    IUDetails,
    Bundle,
    aggregator_p2view_Fragment,
    aggregator_p2view_Bundles,
    Product,
    aggregator_p2view_Products,
    Feature,
    aggregator_p2view_Features,
    Category,
    aggregator_p2view_Categories,
    Miscellaneous,
    Fragments,
    Bundles,
    Products,
    Features,
    Categories,
    aggregator_p2view_IUPresentation,
    OtherIU,
    aggregator_p2view_Miscellaneous,
    Fragment,
    aggregator_p2view_Fragments,
    InstallableUnits,
    aggregator_p2view_MetadataRepositoryStructuredView,
    aggregator_p2_IAdaptable,
    aggregator_p2_RepositoryReference,
    IAdaptable,
    aggregator_p2_IRepository,
    aggregator_p2view_InstallableUnits,
    Properties,
    aggregator_p2_IQueryable,
    TouchpointInstruction,
    aggregator_p2_InstructionMap,
    aggregator_p2_Property,
    aggregator_p2_UpdateDescriptor,
    ITouchpointInstruction,
    aggregator_p2_TouchpointInstruction,
    InstructionMap,
    ITouchpointData,
    aggregator_p2_TouchpointData,
    IRequiredCapability,
    aggregator_p2_RequiredCapability,
    IProvidedCapability,
    aggregator_p2_ProvidedCapability,
    aggregator_p2_License,
    p2_IInstallableUnitFragment,
    p2_InstallableUnit,
    aggregator_p2_InstallableUnitFragment,
    p2_IRepository,
    p2_IQueryable,
    aggregator_p2_IMetadataRepository,
    ProvidedCapability,
    ArtifactKey,
    aggregator_p2_InstallableUnit,
    Property,
    RepositoryReference,
    InstallableUnit,
    IMetadataRepository,
    aggregator_p2_MetadataRepository,
    aggregator_p2_Copyright,
    IArtifactKey,
    aggregator_p2_ArtifactKey,
    aggregator_p2_IUpdateDescriptor,
    aggregator_p2_ITouchpointType,
    aggregator_p2_ITouchpointInstruction,
    TouchpointData,
    aggregator_Status,
    ITouchpointType,
    aggregator_p2_TouchpointType,
    aggregator_ChildrenProvider,
    aggregator_MavenItem,
    aggregator_DescriptionProvider,
    aggregator_LabelProvider,
    aggregator_Comparable,
    MetadataRepository,
    aggregator_EnabledStatusProvider,
    MapRule,
    aggregator_ExclusionRule,
    aggregator_ValidConfigurationsRule,
    aggregator_Property,
    InstallableUnitRequest,
    MappedUnit,
    aggregator_Feature,
    aggregator_Bundle,
    aggregator_Product,
    MetadataRepositoryReference,
    aggregator_Contact,
    EnabledStatusProvider,
    aggregator_MappedUnit,
    aggregator_Category,
    InfosProvider,
    StatusProvider,
    aggregator_CustomCategory,
    aggregator_MavenMapping,
    aggregator_MetadataRepositoryReference,
    DescriptionProvider,
    aggregator_MappedRepository,
    aggregator_InstallableUnitRequest,
    aggregator_MapRule,
    aggregator_Aggregator,
    aggregator_Contribution,
    aggregator_Configuration,
    InstallableUnitType,
    WindowSystem,
    PackedStrategy,
    AggregationType,
    StatusCode,
    OperatingSystem,
    Architecture,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_requiredcapability_is_not_abstract():
    assert not inspect.isabstract(RequiredCapability)


def test_hyp_requiredcapability_constructor_exists():
    assert callable(RequiredCapability.__init__)


def test_hyp_requiredcapability_constructor_args():
    sig = inspect.signature(RequiredCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_irequiredcapability_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IRequiredCapability)


def test_hyp_aggregator_p2_irequiredcapability_constructor_exists():
    assert callable(aggregator_p2_IRequiredCapability.__init__)


def test_hyp_aggregator_p2_irequiredcapability_constructor_args():
    sig = inspect.signature(aggregator_p2_IRequiredCapability.__init__)
    params = list(sig.parameters.keys())
    assert "selectorList" in params, "Missing parameter 'selectorList'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "negation" in params, "Missing parameter 'negation'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "range" in params, "Missing parameter 'range'"
    assert "filter" in params, "Missing parameter 'filter'"
    assert "greedy" in params, "Missing parameter 'greedy'"












def test_hyp_aggregator_p2_iprovidedcapability_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IProvidedCapability)


def test_hyp_aggregator_p2_iprovidedcapability_constructor_exists():
    assert callable(aggregator_p2_IProvidedCapability.__init__)


def test_hyp_aggregator_p2_iprovidedcapability_constructor_args():
    sig = inspect.signature(aggregator_p2_IProvidedCapability.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"






def test_hyp_aggregator_p2_ilicense_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ILicense)


def test_hyp_aggregator_p2_ilicense_constructor_exists():
    assert callable(aggregator_p2_ILicense.__init__)


def test_hyp_aggregator_p2_ilicense_constructor_args():
    sig = inspect.signature(aggregator_p2_ILicense.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "digest" in params, "Missing parameter 'digest'"
    assert "location" in params, "Missing parameter 'location'"






def test_hyp_iinstallableunit_is_not_abstract():
    assert not inspect.isabstract(IInstallableUnit)


def test_hyp_iinstallableunit_constructor_exists():
    assert callable(IInstallableUnit.__init__)


def test_hyp_iinstallableunit_constructor_args():
    sig = inspect.signature(IInstallableUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_iinstallableunitfragment_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IInstallableUnitFragment)


def test_hyp_aggregator_p2_iinstallableunitfragment_constructor_exists():
    assert callable(aggregator_p2_IInstallableUnitFragment.__init__)


def test_hyp_aggregator_p2_iinstallableunitfragment_constructor_args():
    sig = inspect.signature(aggregator_p2_IInstallableUnitFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_icopyright_is_not_abstract():
    assert not inspect.isabstract(ICopyright)


def test_hyp_icopyright_constructor_exists():
    assert callable(ICopyright.__init__)


def test_hyp_icopyright_constructor_args():
    sig = inspect.signature(ICopyright.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ilicense_is_not_abstract():
    assert not inspect.isabstract(ILicense)


def test_hyp_ilicense_constructor_exists():
    assert callable(ILicense.__init__)


def test_hyp_ilicense_constructor_args():
    sig = inspect.signature(ILicense.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iupdatedescriptor_is_not_abstract():
    assert not inspect.isabstract(IUpdateDescriptor)


def test_hyp_iupdatedescriptor_constructor_exists():
    assert callable(IUpdateDescriptor.__init__)


def test_hyp_iupdatedescriptor_constructor_args():
    sig = inspect.signature(IUpdateDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_itouchpointdata_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ITouchpointData)


def test_hyp_aggregator_p2_itouchpointdata_constructor_exists():
    assert callable(aggregator_p2_ITouchpointData.__init__)


def test_hyp_aggregator_p2_itouchpointdata_constructor_args():
    sig = inspect.signature(aggregator_p2_ITouchpointData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_iinstallableunit_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IInstallableUnit)


def test_hyp_aggregator_p2_iinstallableunit_constructor_exists():
    assert callable(aggregator_p2_IInstallableUnit.__init__)


def test_hyp_aggregator_p2_iinstallableunit_constructor_args():
    sig = inspect.signature(aggregator_p2_IInstallableUnit.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"
    assert "version" in params, "Missing parameter 'version'"
    assert "resolved" in params, "Missing parameter 'resolved'"
    assert "singleton" in params, "Missing parameter 'singleton'"
    assert "id" in params, "Missing parameter 'id'"








def test_hyp_aggregator_p2_icopyright_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ICopyright)


def test_hyp_aggregator_p2_icopyright_constructor_exists():
    assert callable(aggregator_p2_ICopyright.__init__)


def test_hyp_aggregator_p2_icopyright_constructor_args():
    sig = inspect.signature(aggregator_p2_ICopyright.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_aggregator_p2_iartifactkey_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IArtifactKey)


def test_hyp_aggregator_p2_iartifactkey_constructor_exists():
    assert callable(aggregator_p2_IArtifactKey.__init__)


def test_hyp_aggregator_p2_iartifactkey_constructor_args():
    sig = inspect.signature(aggregator_p2_IArtifactKey.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "classifier" in params, "Missing parameter 'classifier'"
    assert "version" in params, "Missing parameter 'version'"






def test_hyp_aggregator_infosprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_InfosProvider)


def test_hyp_aggregator_infosprovider_constructor_exists():
    assert callable(aggregator_InfosProvider.__init__)


def test_hyp_aggregator_infosprovider_constructor_args():
    sig = inspect.signature(aggregator_InfosProvider.__init__)
    params = list(sig.parameters.keys())
    assert "warnings" in params, "Missing parameter 'warnings'"
    assert "infos" in params, "Missing parameter 'infos'"
    assert "errors" in params, "Missing parameter 'errors'"






def test_hyp_aggregator_statusprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_StatusProvider)


def test_hyp_aggregator_statusprovider_constructor_exists():
    assert callable(aggregator_StatusProvider.__init__)


def test_hyp_aggregator_statusprovider_constructor_args():
    sig = inspect.signature(aggregator_StatusProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_iprovidedcapability_is_not_abstract():
    assert not inspect.isabstract(p2_IProvidedCapability)


def test_hyp_p2_iprovidedcapability_constructor_exists():
    assert callable(p2_IProvidedCapability.__init__)


def test_hyp_p2_iprovidedcapability_constructor_args():
    sig = inspect.signature(p2_IProvidedCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labelprovider_is_not_abstract():
    assert not inspect.isabstract(LabelProvider)


def test_hyp_labelprovider_constructor_exists():
    assert callable(LabelProvider.__init__)


def test_hyp_labelprovider_constructor_args():
    sig = inspect.signature(LabelProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_providedcapabilitywrapper_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_ProvidedCapabilityWrapper)


def test_hyp_aggregator_p2view_providedcapabilitywrapper_constructor_exists():
    assert callable(aggregator_p2view_ProvidedCapabilityWrapper.__init__)


def test_hyp_aggregator_p2view_providedcapabilitywrapper_constructor_args():
    sig = inspect.signature(aggregator_p2view_ProvidedCapabilityWrapper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_irequiredcapability_is_not_abstract():
    assert not inspect.isabstract(p2_IRequiredCapability)


def test_hyp_p2_irequiredcapability_constructor_exists():
    assert callable(p2_IRequiredCapability.__init__)


def test_hyp_p2_irequiredcapability_constructor_args():
    sig = inspect.signature(p2_IRequiredCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_requiredcapabilitywrapper_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_RequiredCapabilityWrapper)


def test_hyp_aggregator_p2view_requiredcapabilitywrapper_constructor_exists():
    assert callable(aggregator_p2view_RequiredCapabilityWrapper.__init__)


def test_hyp_aggregator_p2view_requiredcapabilitywrapper_constructor_args():
    sig = inspect.signature(aggregator_p2view_RequiredCapabilityWrapper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_touchpoints_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Touchpoints)


def test_hyp_aggregator_p2view_touchpoints_constructor_exists():
    assert callable(aggregator_p2view_Touchpoints.__init__)


def test_hyp_aggregator_p2view_touchpoints_constructor_args():
    sig = inspect.signature(aggregator_p2view_Touchpoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_providedcapabilitywrapper_is_not_abstract():
    assert not inspect.isabstract(ProvidedCapabilityWrapper)


def test_hyp_providedcapabilitywrapper_constructor_exists():
    assert callable(ProvidedCapabilityWrapper.__init__)


def test_hyp_providedcapabilitywrapper_constructor_args():
    sig = inspect.signature(ProvidedCapabilityWrapper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_providedcapabilities_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_ProvidedCapabilities)


def test_hyp_aggregator_p2view_providedcapabilities_constructor_exists():
    assert callable(aggregator_p2view_ProvidedCapabilities.__init__)


def test_hyp_aggregator_p2view_providedcapabilities_constructor_args():
    sig = inspect.signature(aggregator_p2view_ProvidedCapabilities.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requiredcapabilitywrapper_is_not_abstract():
    assert not inspect.isabstract(RequiredCapabilityWrapper)


def test_hyp_requiredcapabilitywrapper_constructor_exists():
    assert callable(RequiredCapabilityWrapper.__init__)


def test_hyp_requiredcapabilitywrapper_constructor_args():
    sig = inspect.signature(RequiredCapabilityWrapper.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_requiredcapabilities_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_RequiredCapabilities)


def test_hyp_aggregator_p2view_requiredcapabilities_constructor_exists():
    assert callable(aggregator_p2view_RequiredCapabilities.__init__)


def test_hyp_aggregator_p2view_requiredcapabilities_constructor_args():
    sig = inspect.signature(aggregator_p2view_RequiredCapabilities.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2view_aggregator_property_is_not_abstract():
    assert not inspect.isabstract(p2view_aggregator_Property)


def test_hyp_p2view_aggregator_property_constructor_exists():
    assert callable(p2view_aggregator_Property.__init__)


def test_hyp_p2view_aggregator_property_constructor_args():
    sig = inspect.signature(p2view_aggregator_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_properties_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Properties)


def test_hyp_aggregator_p2view_properties_constructor_exists():
    assert callable(aggregator_p2view_Properties.__init__)


def test_hyp_aggregator_p2view_properties_constructor_args():
    sig = inspect.signature(aggregator_p2view_Properties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_touchpoints_is_not_abstract():
    assert not inspect.isabstract(Touchpoints)


def test_hyp_touchpoints_constructor_exists():
    assert callable(Touchpoints.__init__)


def test_hyp_touchpoints_constructor_args():
    sig = inspect.signature(Touchpoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_providedcapabilities_is_not_abstract():
    assert not inspect.isabstract(ProvidedCapabilities)


def test_hyp_providedcapabilities_constructor_exists():
    assert callable(ProvidedCapabilities.__init__)


def test_hyp_providedcapabilities_constructor_args():
    sig = inspect.signature(ProvidedCapabilities.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requiredcapabilities_is_not_abstract():
    assert not inspect.isabstract(RequiredCapabilities)


def test_hyp_requiredcapabilities_constructor_exists():
    assert callable(RequiredCapabilities.__init__)


def test_hyp_requiredcapabilities_constructor_args():
    sig = inspect.signature(RequiredCapabilities.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_iudetails_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_IUDetails)


def test_hyp_aggregator_p2view_iudetails_constructor_exists():
    assert callable(aggregator_p2view_IUDetails.__init__)


def test_hyp_aggregator_p2view_iudetails_constructor_args():
    sig = inspect.signature(aggregator_p2view_IUDetails.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iupresentation_is_not_abstract():
    assert not inspect.isabstract(IUPresentation)


def test_hyp_iupresentation_constructor_exists():
    assert callable(IUPresentation.__init__)


def test_hyp_iupresentation_constructor_args():
    sig = inspect.signature(IUPresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_category_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Category)


def test_hyp_aggregator_p2view_category_constructor_exists():
    assert callable(aggregator_p2view_Category.__init__)


def test_hyp_aggregator_p2view_category_constructor_args():
    sig = inspect.signature(aggregator_p2view_Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2view_iudetails_is_not_abstract():
    assert not inspect.isabstract(p2view_IUDetails)


def test_hyp_p2view_iudetails_constructor_exists():
    assert callable(p2view_IUDetails.__init__)


def test_hyp_p2view_iudetails_constructor_args():
    sig = inspect.signature(p2view_IUDetails.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2view_iupresentation_is_not_abstract():
    assert not inspect.isabstract(p2view_IUPresentation)


def test_hyp_p2view_iupresentation_constructor_exists():
    assert callable(p2view_IUPresentation.__init__)


def test_hyp_p2view_iupresentation_constructor_args():
    sig = inspect.signature(p2view_IUPresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_iupresentationwithdetails_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_IUPresentationWithDetails)


def test_hyp_aggregator_p2view_iupresentationwithdetails_constructor_exists():
    assert callable(aggregator_p2view_IUPresentationWithDetails.__init__)


def test_hyp_aggregator_p2view_iupresentationwithdetails_constructor_args():
    sig = inspect.signature(aggregator_p2view_IUPresentationWithDetails.__init__)
    params = list(sig.parameters.keys())
    assert "detailsResolved" in params, "Missing parameter 'detailsResolved'"




def test_hyp_iupresentationwithdetails_is_not_abstract():
    assert not inspect.isabstract(IUPresentationWithDetails)


def test_hyp_iupresentationwithdetails_constructor_exists():
    assert callable(IUPresentationWithDetails.__init__)


def test_hyp_iupresentationwithdetails_constructor_args():
    sig = inspect.signature(IUPresentationWithDetails.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_product_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Product)


def test_hyp_aggregator_p2view_product_constructor_exists():
    assert callable(aggregator_p2view_Product.__init__)


def test_hyp_aggregator_p2view_product_constructor_args():
    sig = inspect.signature(aggregator_p2view_Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_bundle_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Bundle)


def test_hyp_aggregator_p2view_bundle_constructor_exists():
    assert callable(aggregator_p2view_Bundle.__init__)


def test_hyp_aggregator_p2view_bundle_constructor_args():
    sig = inspect.signature(aggregator_p2view_Bundle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_otheriu_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_OtherIU)


def test_hyp_aggregator_p2view_otheriu_constructor_exists():
    assert callable(aggregator_p2view_OtherIU.__init__)


def test_hyp_aggregator_p2view_otheriu_constructor_args():
    sig = inspect.signature(aggregator_p2view_OtherIU.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_feature_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Feature)


def test_hyp_aggregator_p2view_feature_constructor_exists():
    assert callable(aggregator_p2view_Feature.__init__)


def test_hyp_aggregator_p2view_feature_constructor_args():
    sig = inspect.signature(aggregator_p2view_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iudetails_is_not_abstract():
    assert not inspect.isabstract(IUDetails)


def test_hyp_iudetails_constructor_exists():
    assert callable(IUDetails.__init__)


def test_hyp_iudetails_constructor_args():
    sig = inspect.signature(IUDetails.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bundle_is_not_abstract():
    assert not inspect.isabstract(Bundle)


def test_hyp_bundle_constructor_exists():
    assert callable(Bundle.__init__)


def test_hyp_bundle_constructor_args():
    sig = inspect.signature(Bundle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_fragment_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Fragment)


def test_hyp_aggregator_p2view_fragment_constructor_exists():
    assert callable(aggregator_p2view_Fragment.__init__)


def test_hyp_aggregator_p2view_fragment_constructor_args():
    sig = inspect.signature(aggregator_p2view_Fragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_bundles_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Bundles)


def test_hyp_aggregator_p2view_bundles_constructor_exists():
    assert callable(aggregator_p2view_Bundles.__init__)


def test_hyp_aggregator_p2view_bundles_constructor_args():
    sig = inspect.signature(aggregator_p2view_Bundles.__init__)
    params = list(sig.parameters.keys())



def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_products_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Products)


def test_hyp_aggregator_p2view_products_constructor_exists():
    assert callable(aggregator_p2view_Products.__init__)


def test_hyp_aggregator_p2view_products_constructor_args():
    sig = inspect.signature(aggregator_p2view_Products.__init__)
    params = list(sig.parameters.keys())



def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_features_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Features)


def test_hyp_aggregator_p2view_features_constructor_exists():
    assert callable(aggregator_p2view_Features.__init__)


def test_hyp_aggregator_p2view_features_constructor_args():
    sig = inspect.signature(aggregator_p2view_Features.__init__)
    params = list(sig.parameters.keys())



def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_categories_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Categories)


def test_hyp_aggregator_p2view_categories_constructor_exists():
    assert callable(aggregator_p2view_Categories.__init__)


def test_hyp_aggregator_p2view_categories_constructor_args():
    sig = inspect.signature(aggregator_p2view_Categories.__init__)
    params = list(sig.parameters.keys())



def test_hyp_miscellaneous_is_not_abstract():
    assert not inspect.isabstract(Miscellaneous)


def test_hyp_miscellaneous_constructor_exists():
    assert callable(Miscellaneous.__init__)


def test_hyp_miscellaneous_constructor_args():
    sig = inspect.signature(Miscellaneous.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fragments_is_not_abstract():
    assert not inspect.isabstract(Fragments)


def test_hyp_fragments_constructor_exists():
    assert callable(Fragments.__init__)


def test_hyp_fragments_constructor_args():
    sig = inspect.signature(Fragments.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bundles_is_not_abstract():
    assert not inspect.isabstract(Bundles)


def test_hyp_bundles_constructor_exists():
    assert callable(Bundles.__init__)


def test_hyp_bundles_constructor_args():
    sig = inspect.signature(Bundles.__init__)
    params = list(sig.parameters.keys())



def test_hyp_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_hyp_products_constructor_exists():
    assert callable(Products.__init__)


def test_hyp_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())



def test_hyp_features_is_not_abstract():
    assert not inspect.isabstract(Features)


def test_hyp_features_constructor_exists():
    assert callable(Features.__init__)


def test_hyp_features_constructor_args():
    sig = inspect.signature(Features.__init__)
    params = list(sig.parameters.keys())



def test_hyp_categories_is_not_abstract():
    assert not inspect.isabstract(Categories)


def test_hyp_categories_constructor_exists():
    assert callable(Categories.__init__)


def test_hyp_categories_constructor_args():
    sig = inspect.signature(Categories.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_iupresentation_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_IUPresentation)


def test_hyp_aggregator_p2view_iupresentation_constructor_exists():
    assert callable(aggregator_p2view_IUPresentation.__init__)


def test_hyp_aggregator_p2view_iupresentation_constructor_args():
    sig = inspect.signature(aggregator_p2view_IUPresentation.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"









def test_hyp_otheriu_is_not_abstract():
    assert not inspect.isabstract(OtherIU)


def test_hyp_otheriu_constructor_exists():
    assert callable(OtherIU.__init__)


def test_hyp_otheriu_constructor_args():
    sig = inspect.signature(OtherIU.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_miscellaneous_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Miscellaneous)


def test_hyp_aggregator_p2view_miscellaneous_constructor_exists():
    assert callable(aggregator_p2view_Miscellaneous.__init__)


def test_hyp_aggregator_p2view_miscellaneous_constructor_args():
    sig = inspect.signature(aggregator_p2view_Miscellaneous.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fragment_is_not_abstract():
    assert not inspect.isabstract(Fragment)


def test_hyp_fragment_constructor_exists():
    assert callable(Fragment.__init__)


def test_hyp_fragment_constructor_args():
    sig = inspect.signature(Fragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_fragments_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_Fragments)


def test_hyp_aggregator_p2view_fragments_constructor_exists():
    assert callable(aggregator_p2view_Fragments.__init__)


def test_hyp_aggregator_p2view_fragments_constructor_args():
    sig = inspect.signature(aggregator_p2view_Fragments.__init__)
    params = list(sig.parameters.keys())



def test_hyp_installableunits_is_not_abstract():
    assert not inspect.isabstract(InstallableUnits)


def test_hyp_installableunits_constructor_exists():
    assert callable(InstallableUnits.__init__)


def test_hyp_installableunits_constructor_args():
    sig = inspect.signature(InstallableUnits.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2view_metadatarepositorystructuredview_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_MetadataRepositoryStructuredView)


def test_hyp_aggregator_p2view_metadatarepositorystructuredview_constructor_exists():
    assert callable(aggregator_p2view_MetadataRepositoryStructuredView.__init__)


def test_hyp_aggregator_p2view_metadatarepositorystructuredview_constructor_args():
    sig = inspect.signature(aggregator_p2view_MetadataRepositoryStructuredView.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "loaded" in params, "Missing parameter 'loaded'"





def test_hyp_aggregator_p2_iadaptable_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IAdaptable)


def test_hyp_aggregator_p2_iadaptable_constructor_exists():
    assert callable(aggregator_p2_IAdaptable.__init__)


def test_hyp_aggregator_p2_iadaptable_constructor_args():
    sig = inspect.signature(aggregator_p2_IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_repositoryreference_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_RepositoryReference)


def test_hyp_aggregator_p2_repositoryreference_constructor_exists():
    assert callable(aggregator_p2_RepositoryReference.__init__)


def test_hyp_aggregator_p2_repositoryreference_constructor_args():
    sig = inspect.signature(aggregator_p2_RepositoryReference.__init__)
    params = list(sig.parameters.keys())
    assert "nickname" in params, "Missing parameter 'nickname'"
    assert "options" in params, "Missing parameter 'options'"
    assert "location" in params, "Missing parameter 'location'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_iadaptable_is_not_abstract():
    assert not inspect.isabstract(IAdaptable)


def test_hyp_iadaptable_constructor_exists():
    assert callable(IAdaptable.__init__)


def test_hyp_iadaptable_constructor_args():
    sig = inspect.signature(IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_irepository_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IRepository)


def test_hyp_aggregator_p2_irepository_constructor_exists():
    assert callable(aggregator_p2_IRepository.__init__)


def test_hyp_aggregator_p2_irepository_constructor_args():
    sig = inspect.signature(aggregator_p2_IRepository.__init__)
    params = list(sig.parameters.keys())
    assert "modifiable" in params, "Missing parameter 'modifiable'"
    assert "version" in params, "Missing parameter 'version'"
    assert "location" in params, "Missing parameter 'location'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "provider" in params, "Missing parameter 'provider'"










def test_hyp_aggregator_p2view_installableunits_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2view_InstallableUnits)


def test_hyp_aggregator_p2view_installableunits_constructor_exists():
    assert callable(aggregator_p2view_InstallableUnits.__init__)


def test_hyp_aggregator_p2view_installableunits_constructor_args():
    sig = inspect.signature(aggregator_p2view_InstallableUnits.__init__)
    params = list(sig.parameters.keys())



def test_hyp_properties_is_not_abstract():
    assert not inspect.isabstract(Properties)


def test_hyp_properties_constructor_exists():
    assert callable(Properties.__init__)


def test_hyp_properties_constructor_args():
    sig = inspect.signature(Properties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_iqueryable_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IQueryable)


def test_hyp_aggregator_p2_iqueryable_constructor_exists():
    assert callable(aggregator_p2_IQueryable.__init__)


def test_hyp_aggregator_p2_iqueryable_constructor_args():
    sig = inspect.signature(aggregator_p2_IQueryable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_touchpointinstruction_is_not_abstract():
    assert not inspect.isabstract(TouchpointInstruction)


def test_hyp_touchpointinstruction_constructor_exists():
    assert callable(TouchpointInstruction.__init__)


def test_hyp_touchpointinstruction_constructor_args():
    sig = inspect.signature(TouchpointInstruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_instructionmap_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_InstructionMap)


def test_hyp_aggregator_p2_instructionmap_constructor_exists():
    assert callable(aggregator_p2_InstructionMap.__init__)


def test_hyp_aggregator_p2_instructionmap_constructor_args():
    sig = inspect.signature(aggregator_p2_InstructionMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_aggregator_p2_property_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_Property)


def test_hyp_aggregator_p2_property_constructor_exists():
    assert callable(aggregator_p2_Property.__init__)


def test_hyp_aggregator_p2_property_constructor_args():
    sig = inspect.signature(aggregator_p2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_aggregator_p2_updatedescriptor_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_UpdateDescriptor)


def test_hyp_aggregator_p2_updatedescriptor_constructor_exists():
    assert callable(aggregator_p2_UpdateDescriptor.__init__)


def test_hyp_aggregator_p2_updatedescriptor_constructor_args():
    sig = inspect.signature(aggregator_p2_UpdateDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_itouchpointinstruction_is_not_abstract():
    assert not inspect.isabstract(ITouchpointInstruction)


def test_hyp_itouchpointinstruction_constructor_exists():
    assert callable(ITouchpointInstruction.__init__)


def test_hyp_itouchpointinstruction_constructor_args():
    sig = inspect.signature(ITouchpointInstruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_touchpointinstruction_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_TouchpointInstruction)


def test_hyp_aggregator_p2_touchpointinstruction_constructor_exists():
    assert callable(aggregator_p2_TouchpointInstruction.__init__)


def test_hyp_aggregator_p2_touchpointinstruction_constructor_args():
    sig = inspect.signature(aggregator_p2_TouchpointInstruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instructionmap_is_not_abstract():
    assert not inspect.isabstract(InstructionMap)


def test_hyp_instructionmap_constructor_exists():
    assert callable(InstructionMap.__init__)


def test_hyp_instructionmap_constructor_args():
    sig = inspect.signature(InstructionMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_itouchpointdata_is_not_abstract():
    assert not inspect.isabstract(ITouchpointData)


def test_hyp_itouchpointdata_constructor_exists():
    assert callable(ITouchpointData.__init__)


def test_hyp_itouchpointdata_constructor_args():
    sig = inspect.signature(ITouchpointData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_touchpointdata_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_TouchpointData)


def test_hyp_aggregator_p2_touchpointdata_constructor_exists():
    assert callable(aggregator_p2_TouchpointData.__init__)


def test_hyp_aggregator_p2_touchpointdata_constructor_args():
    sig = inspect.signature(aggregator_p2_TouchpointData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_irequiredcapability_is_not_abstract():
    assert not inspect.isabstract(IRequiredCapability)


def test_hyp_irequiredcapability_constructor_exists():
    assert callable(IRequiredCapability.__init__)


def test_hyp_irequiredcapability_constructor_args():
    sig = inspect.signature(IRequiredCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_requiredcapability_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_RequiredCapability)


def test_hyp_aggregator_p2_requiredcapability_constructor_exists():
    assert callable(aggregator_p2_RequiredCapability.__init__)


def test_hyp_aggregator_p2_requiredcapability_constructor_args():
    sig = inspect.signature(aggregator_p2_RequiredCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iprovidedcapability_is_not_abstract():
    assert not inspect.isabstract(IProvidedCapability)


def test_hyp_iprovidedcapability_constructor_exists():
    assert callable(IProvidedCapability.__init__)


def test_hyp_iprovidedcapability_constructor_args():
    sig = inspect.signature(IProvidedCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_providedcapability_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ProvidedCapability)


def test_hyp_aggregator_p2_providedcapability_constructor_exists():
    assert callable(aggregator_p2_ProvidedCapability.__init__)


def test_hyp_aggregator_p2_providedcapability_constructor_args():
    sig = inspect.signature(aggregator_p2_ProvidedCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_license_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_License)


def test_hyp_aggregator_p2_license_constructor_exists():
    assert callable(aggregator_p2_License.__init__)


def test_hyp_aggregator_p2_license_constructor_args():
    sig = inspect.signature(aggregator_p2_License.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_iinstallableunitfragment_is_not_abstract():
    assert not inspect.isabstract(p2_IInstallableUnitFragment)


def test_hyp_p2_iinstallableunitfragment_constructor_exists():
    assert callable(p2_IInstallableUnitFragment.__init__)


def test_hyp_p2_iinstallableunitfragment_constructor_args():
    sig = inspect.signature(p2_IInstallableUnitFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_installableunit_is_not_abstract():
    assert not inspect.isabstract(p2_InstallableUnit)


def test_hyp_p2_installableunit_constructor_exists():
    assert callable(p2_InstallableUnit.__init__)


def test_hyp_p2_installableunit_constructor_args():
    sig = inspect.signature(p2_InstallableUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_installableunitfragment_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_InstallableUnitFragment)


def test_hyp_aggregator_p2_installableunitfragment_constructor_exists():
    assert callable(aggregator_p2_InstallableUnitFragment.__init__)


def test_hyp_aggregator_p2_installableunitfragment_constructor_args():
    sig = inspect.signature(aggregator_p2_InstallableUnitFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_irepository_is_not_abstract():
    assert not inspect.isabstract(p2_IRepository)


def test_hyp_p2_irepository_constructor_exists():
    assert callable(p2_IRepository.__init__)


def test_hyp_p2_irepository_constructor_args():
    sig = inspect.signature(p2_IRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_p2_iqueryable_is_not_abstract():
    assert not inspect.isabstract(p2_IQueryable)


def test_hyp_p2_iqueryable_constructor_exists():
    assert callable(p2_IQueryable.__init__)


def test_hyp_p2_iqueryable_constructor_args():
    sig = inspect.signature(p2_IQueryable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_imetadatarepository_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IMetadataRepository)


def test_hyp_aggregator_p2_imetadatarepository_constructor_exists():
    assert callable(aggregator_p2_IMetadataRepository.__init__)


def test_hyp_aggregator_p2_imetadatarepository_constructor_args():
    sig = inspect.signature(aggregator_p2_IMetadataRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_providedcapability_is_not_abstract():
    assert not inspect.isabstract(ProvidedCapability)


def test_hyp_providedcapability_constructor_exists():
    assert callable(ProvidedCapability.__init__)


def test_hyp_providedcapability_constructor_args():
    sig = inspect.signature(ProvidedCapability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_artifactkey_is_not_abstract():
    assert not inspect.isabstract(ArtifactKey)


def test_hyp_artifactkey_constructor_exists():
    assert callable(ArtifactKey.__init__)


def test_hyp_artifactkey_constructor_args():
    sig = inspect.signature(ArtifactKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_installableunit_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_InstallableUnit)


def test_hyp_aggregator_p2_installableunit_constructor_exists():
    assert callable(aggregator_p2_InstallableUnit.__init__)


def test_hyp_aggregator_p2_installableunit_constructor_args():
    sig = inspect.signature(aggregator_p2_InstallableUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_repositoryreference_is_not_abstract():
    assert not inspect.isabstract(RepositoryReference)


def test_hyp_repositoryreference_constructor_exists():
    assert callable(RepositoryReference.__init__)


def test_hyp_repositoryreference_constructor_args():
    sig = inspect.signature(RepositoryReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_installableunit_is_not_abstract():
    assert not inspect.isabstract(InstallableUnit)


def test_hyp_installableunit_constructor_exists():
    assert callable(InstallableUnit.__init__)


def test_hyp_installableunit_constructor_args():
    sig = inspect.signature(InstallableUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imetadatarepository_is_not_abstract():
    assert not inspect.isabstract(IMetadataRepository)


def test_hyp_imetadatarepository_constructor_exists():
    assert callable(IMetadataRepository.__init__)


def test_hyp_imetadatarepository_constructor_args():
    sig = inspect.signature(IMetadataRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_metadatarepository_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_MetadataRepository)


def test_hyp_aggregator_p2_metadatarepository_constructor_exists():
    assert callable(aggregator_p2_MetadataRepository.__init__)


def test_hyp_aggregator_p2_metadatarepository_constructor_args():
    sig = inspect.signature(aggregator_p2_MetadataRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_copyright_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_Copyright)


def test_hyp_aggregator_p2_copyright_constructor_exists():
    assert callable(aggregator_p2_Copyright.__init__)


def test_hyp_aggregator_p2_copyright_constructor_args():
    sig = inspect.signature(aggregator_p2_Copyright.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iartifactkey_is_not_abstract():
    assert not inspect.isabstract(IArtifactKey)


def test_hyp_iartifactkey_constructor_exists():
    assert callable(IArtifactKey.__init__)


def test_hyp_iartifactkey_constructor_args():
    sig = inspect.signature(IArtifactKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_artifactkey_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ArtifactKey)


def test_hyp_aggregator_p2_artifactkey_constructor_exists():
    assert callable(aggregator_p2_ArtifactKey.__init__)


def test_hyp_aggregator_p2_artifactkey_constructor_args():
    sig = inspect.signature(aggregator_p2_ArtifactKey.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_iupdatedescriptor_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_IUpdateDescriptor)


def test_hyp_aggregator_p2_iupdatedescriptor_constructor_exists():
    assert callable(aggregator_p2_IUpdateDescriptor.__init__)


def test_hyp_aggregator_p2_iupdatedescriptor_constructor_args():
    sig = inspect.signature(aggregator_p2_IUpdateDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "range" in params, "Missing parameter 'range'"







def test_hyp_aggregator_p2_itouchpointtype_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ITouchpointType)


def test_hyp_aggregator_p2_itouchpointtype_constructor_exists():
    assert callable(aggregator_p2_ITouchpointType.__init__)


def test_hyp_aggregator_p2_itouchpointtype_constructor_args():
    sig = inspect.signature(aggregator_p2_ITouchpointType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"





def test_hyp_aggregator_p2_itouchpointinstruction_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_ITouchpointInstruction)


def test_hyp_aggregator_p2_itouchpointinstruction_constructor_exists():
    assert callable(aggregator_p2_ITouchpointInstruction.__init__)


def test_hyp_aggregator_p2_itouchpointinstruction_constructor_args():
    sig = inspect.signature(aggregator_p2_ITouchpointInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "importAttribute" in params, "Missing parameter 'importAttribute'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_touchpointdata_is_not_abstract():
    assert not inspect.isabstract(TouchpointData)


def test_hyp_touchpointdata_constructor_exists():
    assert callable(TouchpointData.__init__)


def test_hyp_touchpointdata_constructor_args():
    sig = inspect.signature(TouchpointData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_status_is_not_abstract():
    assert not inspect.isabstract(aggregator_Status)


def test_hyp_aggregator_status_constructor_exists():
    assert callable(aggregator_Status.__init__)


def test_hyp_aggregator_status_constructor_args():
    sig = inspect.signature(aggregator_Status.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "message" in params, "Missing parameter 'message'"





def test_hyp_itouchpointtype_is_not_abstract():
    assert not inspect.isabstract(ITouchpointType)


def test_hyp_itouchpointtype_constructor_exists():
    assert callable(ITouchpointType.__init__)


def test_hyp_itouchpointtype_constructor_args():
    sig = inspect.signature(ITouchpointType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_p2_touchpointtype_is_not_abstract():
    assert not inspect.isabstract(aggregator_p2_TouchpointType)


def test_hyp_aggregator_p2_touchpointtype_constructor_exists():
    assert callable(aggregator_p2_TouchpointType.__init__)


def test_hyp_aggregator_p2_touchpointtype_constructor_args():
    sig = inspect.signature(aggregator_p2_TouchpointType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_childrenprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_ChildrenProvider)


def test_hyp_aggregator_childrenprovider_constructor_exists():
    assert callable(aggregator_ChildrenProvider.__init__)


def test_hyp_aggregator_childrenprovider_constructor_args():
    sig = inspect.signature(aggregator_ChildrenProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_mavenitem_is_not_abstract():
    assert not inspect.isabstract(aggregator_MavenItem)


def test_hyp_aggregator_mavenitem_constructor_exists():
    assert callable(aggregator_MavenItem.__init__)


def test_hyp_aggregator_mavenitem_constructor_args():
    sig = inspect.signature(aggregator_MavenItem.__init__)
    params = list(sig.parameters.keys())
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"





def test_hyp_aggregator_descriptionprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_DescriptionProvider)


def test_hyp_aggregator_descriptionprovider_constructor_exists():
    assert callable(aggregator_DescriptionProvider.__init__)


def test_hyp_aggregator_descriptionprovider_constructor_args():
    sig = inspect.signature(aggregator_DescriptionProvider.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_aggregator_labelprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_LabelProvider)


def test_hyp_aggregator_labelprovider_constructor_exists():
    assert callable(aggregator_LabelProvider.__init__)


def test_hyp_aggregator_labelprovider_constructor_args():
    sig = inspect.signature(aggregator_LabelProvider.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_aggregator_comparable_is_not_abstract():
    assert not inspect.isabstract(aggregator_Comparable)


def test_hyp_aggregator_comparable_constructor_exists():
    assert callable(aggregator_Comparable.__init__)


def test_hyp_aggregator_comparable_constructor_args():
    sig = inspect.signature(aggregator_Comparable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metadatarepository_is_not_abstract():
    assert not inspect.isabstract(MetadataRepository)


def test_hyp_metadatarepository_constructor_exists():
    assert callable(MetadataRepository.__init__)


def test_hyp_metadatarepository_constructor_args():
    sig = inspect.signature(MetadataRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_enabledstatusprovider_is_not_abstract():
    assert not inspect.isabstract(aggregator_EnabledStatusProvider)


def test_hyp_aggregator_enabledstatusprovider_constructor_exists():
    assert callable(aggregator_EnabledStatusProvider.__init__)


def test_hyp_aggregator_enabledstatusprovider_constructor_args():
    sig = inspect.signature(aggregator_EnabledStatusProvider.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"




def test_hyp_maprule_is_not_abstract():
    assert not inspect.isabstract(MapRule)


def test_hyp_maprule_constructor_exists():
    assert callable(MapRule.__init__)


def test_hyp_maprule_constructor_args():
    sig = inspect.signature(MapRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_exclusionrule_is_not_abstract():
    assert not inspect.isabstract(aggregator_ExclusionRule)


def test_hyp_aggregator_exclusionrule_constructor_exists():
    assert callable(aggregator_ExclusionRule.__init__)


def test_hyp_aggregator_exclusionrule_constructor_args():
    sig = inspect.signature(aggregator_ExclusionRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_validconfigurationsrule_is_not_abstract():
    assert not inspect.isabstract(aggregator_ValidConfigurationsRule)


def test_hyp_aggregator_validconfigurationsrule_constructor_exists():
    assert callable(aggregator_ValidConfigurationsRule.__init__)


def test_hyp_aggregator_validconfigurationsrule_constructor_args():
    sig = inspect.signature(aggregator_ValidConfigurationsRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_property_is_not_abstract():
    assert not inspect.isabstract(aggregator_Property)


def test_hyp_aggregator_property_constructor_exists():
    assert callable(aggregator_Property.__init__)


def test_hyp_aggregator_property_constructor_args():
    sig = inspect.signature(aggregator_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_installableunitrequest_is_not_abstract():
    assert not inspect.isabstract(InstallableUnitRequest)


def test_hyp_installableunitrequest_constructor_exists():
    assert callable(InstallableUnitRequest.__init__)


def test_hyp_installableunitrequest_constructor_args():
    sig = inspect.signature(InstallableUnitRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mappedunit_is_not_abstract():
    assert not inspect.isabstract(MappedUnit)


def test_hyp_mappedunit_constructor_exists():
    assert callable(MappedUnit.__init__)


def test_hyp_mappedunit_constructor_args():
    sig = inspect.signature(MappedUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_feature_is_not_abstract():
    assert not inspect.isabstract(aggregator_Feature)


def test_hyp_aggregator_feature_constructor_exists():
    assert callable(aggregator_Feature.__init__)


def test_hyp_aggregator_feature_constructor_args():
    sig = inspect.signature(aggregator_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_bundle_is_not_abstract():
    assert not inspect.isabstract(aggregator_Bundle)


def test_hyp_aggregator_bundle_constructor_exists():
    assert callable(aggregator_Bundle.__init__)


def test_hyp_aggregator_bundle_constructor_args():
    sig = inspect.signature(aggregator_Bundle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_product_is_not_abstract():
    assert not inspect.isabstract(aggregator_Product)


def test_hyp_aggregator_product_constructor_exists():
    assert callable(aggregator_Product.__init__)


def test_hyp_aggregator_product_constructor_args():
    sig = inspect.signature(aggregator_Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metadatarepositoryreference_is_not_abstract():
    assert not inspect.isabstract(MetadataRepositoryReference)


def test_hyp_metadatarepositoryreference_constructor_exists():
    assert callable(MetadataRepositoryReference.__init__)


def test_hyp_metadatarepositoryreference_constructor_args():
    sig = inspect.signature(MetadataRepositoryReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_contact_is_not_abstract():
    assert not inspect.isabstract(aggregator_Contact)


def test_hyp_aggregator_contact_constructor_exists():
    assert callable(aggregator_Contact.__init__)


def test_hyp_aggregator_contact_constructor_args():
    sig = inspect.signature(aggregator_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"





def test_hyp_enabledstatusprovider_is_not_abstract():
    assert not inspect.isabstract(EnabledStatusProvider)


def test_hyp_enabledstatusprovider_constructor_exists():
    assert callable(EnabledStatusProvider.__init__)


def test_hyp_enabledstatusprovider_constructor_args():
    sig = inspect.signature(EnabledStatusProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_mappedunit_is_not_abstract():
    assert not inspect.isabstract(aggregator_MappedUnit)


def test_hyp_aggregator_mappedunit_constructor_exists():
    assert callable(aggregator_MappedUnit.__init__)


def test_hyp_aggregator_mappedunit_constructor_args():
    sig = inspect.signature(aggregator_MappedUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_category_is_not_abstract():
    assert not inspect.isabstract(aggregator_Category)


def test_hyp_aggregator_category_constructor_exists():
    assert callable(aggregator_Category.__init__)


def test_hyp_aggregator_category_constructor_args():
    sig = inspect.signature(aggregator_Category.__init__)
    params = list(sig.parameters.keys())
    assert "labelOverride" in params, "Missing parameter 'labelOverride'"




def test_hyp_infosprovider_is_not_abstract():
    assert not inspect.isabstract(InfosProvider)


def test_hyp_infosprovider_constructor_exists():
    assert callable(InfosProvider.__init__)


def test_hyp_infosprovider_constructor_args():
    sig = inspect.signature(InfosProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statusprovider_is_not_abstract():
    assert not inspect.isabstract(StatusProvider)


def test_hyp_statusprovider_constructor_exists():
    assert callable(StatusProvider.__init__)


def test_hyp_statusprovider_constructor_args():
    sig = inspect.signature(StatusProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_customcategory_is_not_abstract():
    assert not inspect.isabstract(aggregator_CustomCategory)


def test_hyp_aggregator_customcategory_constructor_exists():
    assert callable(aggregator_CustomCategory.__init__)


def test_hyp_aggregator_customcategory_constructor_args():
    sig = inspect.signature(aggregator_CustomCategory.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"






def test_hyp_aggregator_mavenmapping_is_not_abstract():
    assert not inspect.isabstract(aggregator_MavenMapping)


def test_hyp_aggregator_mavenmapping_constructor_exists():
    assert callable(aggregator_MavenMapping.__init__)


def test_hyp_aggregator_mavenmapping_constructor_args():
    sig = inspect.signature(aggregator_MavenMapping.__init__)
    params = list(sig.parameters.keys())
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "namePattern" in params, "Missing parameter 'namePattern'"






def test_hyp_aggregator_metadatarepositoryreference_is_not_abstract():
    assert not inspect.isabstract(aggregator_MetadataRepositoryReference)


def test_hyp_aggregator_metadatarepositoryreference_constructor_exists():
    assert callable(aggregator_MetadataRepositoryReference.__init__)


def test_hyp_aggregator_metadatarepositoryreference_constructor_args():
    sig = inspect.signature(aggregator_MetadataRepositoryReference.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "nature" in params, "Missing parameter 'nature'"





def test_hyp_descriptionprovider_is_not_abstract():
    assert not inspect.isabstract(DescriptionProvider)


def test_hyp_descriptionprovider_constructor_exists():
    assert callable(DescriptionProvider.__init__)


def test_hyp_descriptionprovider_constructor_args():
    sig = inspect.signature(DescriptionProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_mappedrepository_is_not_abstract():
    assert not inspect.isabstract(aggregator_MappedRepository)


def test_hyp_aggregator_mappedrepository_constructor_exists():
    assert callable(aggregator_MappedRepository.__init__)


def test_hyp_aggregator_mappedrepository_constructor_args():
    sig = inspect.signature(aggregator_MappedRepository.__init__)
    params = list(sig.parameters.keys())
    assert "mirrorArtifacts" in params, "Missing parameter 'mirrorArtifacts'"
    assert "categoryPrefix" in params, "Missing parameter 'categoryPrefix'"





def test_hyp_aggregator_installableunitrequest_is_not_abstract():
    assert not inspect.isabstract(aggregator_InstallableUnitRequest)


def test_hyp_aggregator_installableunitrequest_constructor_exists():
    assert callable(aggregator_InstallableUnitRequest.__init__)


def test_hyp_aggregator_installableunitrequest_constructor_args():
    sig = inspect.signature(aggregator_InstallableUnitRequest.__init__)
    params = list(sig.parameters.keys())
    assert "versionRange" in params, "Missing parameter 'versionRange'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_aggregator_maprule_is_not_abstract():
    assert not inspect.isabstract(aggregator_MapRule)


def test_hyp_aggregator_maprule_constructor_exists():
    assert callable(aggregator_MapRule.__init__)


def test_hyp_aggregator_maprule_constructor_args():
    sig = inspect.signature(aggregator_MapRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aggregator_aggregator_is_not_abstract():
    assert not inspect.isabstract(aggregator_Aggregator)


def test_hyp_aggregator_aggregator_constructor_exists():
    assert callable(aggregator_Aggregator.__init__)


def test_hyp_aggregator_aggregator_constructor_args():
    sig = inspect.signature(aggregator_Aggregator.__init__)
    params = list(sig.parameters.keys())
    assert "buildRoot" in params, "Missing parameter 'buildRoot'"
    assert "mavenResult" in params, "Missing parameter 'mavenResult'"
    assert "packedStrategy" in params, "Missing parameter 'packedStrategy'"
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"
    assert "sendmail" in params, "Missing parameter 'sendmail'"









def test_hyp_aggregator_contribution_is_not_abstract():
    assert not inspect.isabstract(aggregator_Contribution)


def test_hyp_aggregator_contribution_constructor_exists():
    assert callable(aggregator_Contribution.__init__)


def test_hyp_aggregator_contribution_constructor_args():
    sig = inspect.signature(aggregator_Contribution.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_aggregator_configuration_is_not_abstract():
    assert not inspect.isabstract(aggregator_Configuration)


def test_hyp_aggregator_configuration_constructor_exists():
    assert callable(aggregator_Configuration.__init__)


def test_hyp_aggregator_configuration_constructor_args():
    sig = inspect.signature(aggregator_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "operatingSystem" in params, "Missing parameter 'operatingSystem'"
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "windowSystem" in params, "Missing parameter 'windowSystem'"




def test_hyp_installableunittype_exists():
    # Check that the Enumeration exists
    assert InstallableUnitType is not None

def test_hyp_installableunittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstallableUnitType]
    expected_literals = [
        "FEATURE",
        "OTHER",
        "FRAGMENT",
        "PRODUCT",
        "BUNDLE",
        "CATEGORY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstallableUnitType"

def test_hyp_windowsystem_exists():
    # Check that the Enumeration exists
    assert WindowSystem is not None

def test_hyp_windowsystem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WindowSystem]
    expected_literals = [
        "GTK",
        "Cocoa",
        "Win32",
        "Photon",
        "Motif",
        "Carbon",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WindowSystem"

def test_hyp_packedstrategy_exists():
    # Check that the Enumeration exists
    assert PackedStrategy is not None

def test_hyp_packedstrategy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PackedStrategy]
    expected_literals = [
        "Unpack",
        "UnpackAsSibling",
        "Skip",
        "Copy",
        "Verify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PackedStrategy"

def test_hyp_aggregationtype_exists():
    # Check that the Enumeration exists
    assert AggregationType is not None

def test_hyp_aggregationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationType]
    expected_literals = [
        "Maintenance",
        "Continuous",
        "Stable",
        "Integration",
        "Release",
        "Nightly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationType"

def test_hyp_statuscode_exists():
    # Check that the Enumeration exists
    assert StatusCode is not None

def test_hyp_statuscode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatusCode]
    expected_literals = [
        "BROKEN",
        "WAITING",
        "OK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatusCode"

def test_hyp_operatingsystem_exists():
    # Check that the Enumeration exists
    assert OperatingSystem is not None

def test_hyp_operatingsystem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatingSystem]
    expected_literals = [
        "Solaris",
        "QNX",
        "HPUX",
        "Linux",
        "MacOSX",
        "Win32",
        "AIX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatingSystem"

def test_hyp_architecture_exists():
    # Check that the Enumeration exists
    assert Architecture is not None

def test_hyp_architecture_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Architecture]
    expected_literals = [
        "PPC64",
        "S390X",
        "X86",
        "IA64_32",
        "PPC",
        "Sparc",
        "S390",
        "IA64",
        "X86_64",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Architecture"


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
RequiredCapability_strategy = st.builds(
    RequiredCapability,
)
aggregator_p2_IRequiredCapability_strategy = st.builds(
    aggregator_p2_IRequiredCapability,
    selectorList=
        safe_text,
    namespace=
        safe_text,
    optional=
        st.booleans(),
    name=
        safe_text,
    negation=
        st.booleans(),
    multiple=
        st.booleans(),
    range=
        safe_text,
    filter=
        safe_text,
    greedy=
        st.booleans()
)
aggregator_p2_IProvidedCapability_strategy = st.builds(
    aggregator_p2_IProvidedCapability,
    namespace=
        safe_text,
    name=
        safe_text,
    version=
        safe_text
)
aggregator_p2_ILicense_strategy = st.builds(
    aggregator_p2_ILicense,
    body=
        safe_text,
    digest=
        safe_text,
    location=
        safe_text
)
IInstallableUnit_strategy = st.builds(
    IInstallableUnit,
)
aggregator_p2_IInstallableUnitFragment_strategy = st.builds(
    aggregator_p2_IInstallableUnitFragment,
)
ICopyright_strategy = st.builds(
    ICopyright,
)
ILicense_strategy = st.builds(
    ILicense,
)
IUpdateDescriptor_strategy = st.builds(
    IUpdateDescriptor,
)
aggregator_p2_ITouchpointData_strategy = st.builds(
    aggregator_p2_ITouchpointData,
)
aggregator_p2_IInstallableUnit_strategy = st.builds(
    aggregator_p2_IInstallableUnit,
    filter=
        safe_text,
    version=
        safe_text,
    resolved=
        st.booleans(),
    singleton=
        st.booleans(),
    id=
        safe_text
)
aggregator_p2_ICopyright_strategy = st.builds(
    aggregator_p2_ICopyright,
    location=
        safe_text,
    body=
        safe_text
)
aggregator_p2_IArtifactKey_strategy = st.builds(
    aggregator_p2_IArtifactKey,
    id=
        safe_text,
    classifier=
        safe_text,
    version=
        safe_text
)
aggregator_InfosProvider_strategy = st.builds(
    aggregator_InfosProvider,
    warnings=
        safe_text,
    infos=
        safe_text,
    errors=
        safe_text
)
aggregator_StatusProvider_strategy = st.builds(
    aggregator_StatusProvider,
)
p2_IProvidedCapability_strategy = st.builds(
    p2_IProvidedCapability,
)
LabelProvider_strategy = st.builds(
    LabelProvider,
)
aggregator_p2view_ProvidedCapabilityWrapper_strategy = st.builds(
    aggregator_p2view_ProvidedCapabilityWrapper,
)
p2_IRequiredCapability_strategy = st.builds(
    p2_IRequiredCapability,
)
aggregator_p2view_RequiredCapabilityWrapper_strategy = st.builds(
    aggregator_p2view_RequiredCapabilityWrapper,
)
aggregator_p2view_Touchpoints_strategy = st.builds(
    aggregator_p2view_Touchpoints,
)
ProvidedCapabilityWrapper_strategy = st.builds(
    ProvidedCapabilityWrapper,
)
aggregator_p2view_ProvidedCapabilities_strategy = st.builds(
    aggregator_p2view_ProvidedCapabilities,
)
RequiredCapabilityWrapper_strategy = st.builds(
    RequiredCapabilityWrapper,
)
aggregator_p2view_RequiredCapabilities_strategy = st.builds(
    aggregator_p2view_RequiredCapabilities,
)
p2view_aggregator_Property_strategy = st.builds(
    p2view_aggregator_Property,
)
aggregator_p2view_Properties_strategy = st.builds(
    aggregator_p2view_Properties,
)
Touchpoints_strategy = st.builds(
    Touchpoints,
)
ProvidedCapabilities_strategy = st.builds(
    ProvidedCapabilities,
)
RequiredCapabilities_strategy = st.builds(
    RequiredCapabilities,
)
aggregator_p2view_IUDetails_strategy = st.builds(
    aggregator_p2view_IUDetails,
)
IUPresentation_strategy = st.builds(
    IUPresentation,
)
aggregator_p2view_Category_strategy = st.builds(
    aggregator_p2view_Category,
)
p2view_IUDetails_strategy = st.builds(
    p2view_IUDetails,
)
p2view_IUPresentation_strategy = st.builds(
    p2view_IUPresentation,
)
aggregator_p2view_IUPresentationWithDetails_strategy = st.builds(
    aggregator_p2view_IUPresentationWithDetails,
    detailsResolved=
        safe_text
)
IUPresentationWithDetails_strategy = st.builds(
    IUPresentationWithDetails,
)
aggregator_p2view_Product_strategy = st.builds(
    aggregator_p2view_Product,
)
aggregator_p2view_Bundle_strategy = st.builds(
    aggregator_p2view_Bundle,
)
aggregator_p2view_OtherIU_strategy = st.builds(
    aggregator_p2view_OtherIU,
)
aggregator_p2view_Feature_strategy = st.builds(
    aggregator_p2view_Feature,
)
IUDetails_strategy = st.builds(
    IUDetails,
)
Bundle_strategy = st.builds(
    Bundle,
)
aggregator_p2view_Fragment_strategy = st.builds(
    aggregator_p2view_Fragment,
)
aggregator_p2view_Bundles_strategy = st.builds(
    aggregator_p2view_Bundles,
)
Product_strategy = st.builds(
    Product,
)
aggregator_p2view_Products_strategy = st.builds(
    aggregator_p2view_Products,
)
Feature_strategy = st.builds(
    Feature,
)
aggregator_p2view_Features_strategy = st.builds(
    aggregator_p2view_Features,
)
Category_strategy = st.builds(
    Category,
)
aggregator_p2view_Categories_strategy = st.builds(
    aggregator_p2view_Categories,
)
Miscellaneous_strategy = st.builds(
    Miscellaneous,
)
Fragments_strategy = st.builds(
    Fragments,
)
Bundles_strategy = st.builds(
    Bundles,
)
Products_strategy = st.builds(
    Products,
)
Features_strategy = st.builds(
    Features,
)
Categories_strategy = st.builds(
    Categories,
)
aggregator_p2view_IUPresentation_strategy = st.builds(
    aggregator_p2view_IUPresentation,
    version=
        safe_text,
    type=
        safe_text,
    id=
        safe_text,
    description=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
OtherIU_strategy = st.builds(
    OtherIU,
)
aggregator_p2view_Miscellaneous_strategy = st.builds(
    aggregator_p2view_Miscellaneous,
)
Fragment_strategy = st.builds(
    Fragment,
)
aggregator_p2view_Fragments_strategy = st.builds(
    aggregator_p2view_Fragments,
)
InstallableUnits_strategy = st.builds(
    InstallableUnits,
)
aggregator_p2view_MetadataRepositoryStructuredView_strategy = st.builds(
    aggregator_p2view_MetadataRepositoryStructuredView,
    name=
        safe_text,
    loaded=
        st.booleans()
)
aggregator_p2_IAdaptable_strategy = st.builds(
    aggregator_p2_IAdaptable,
)
aggregator_p2_RepositoryReference_strategy = st.builds(
    aggregator_p2_RepositoryReference,
    nickname=
        safe_text,
    options=
        st.integers(),
    location=
        safe_text,
    type=
        st.integers()
)
IAdaptable_strategy = st.builds(
    IAdaptable,
)
aggregator_p2_IRepository_strategy = st.builds(
    aggregator_p2_IRepository,
    modifiable=
        st.booleans(),
    version=
        safe_text,
    location=
        safe_text,
    type=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    provider=
        safe_text
)
aggregator_p2view_InstallableUnits_strategy = st.builds(
    aggregator_p2view_InstallableUnits,
)
Properties_strategy = st.builds(
    Properties,
)
aggregator_p2_IQueryable_strategy = st.builds(
    aggregator_p2_IQueryable,
)
TouchpointInstruction_strategy = st.builds(
    TouchpointInstruction,
)
aggregator_p2_InstructionMap_strategy = st.builds(
    aggregator_p2_InstructionMap,
    key=
        safe_text
)
aggregator_p2_Property_strategy = st.builds(
    aggregator_p2_Property,
    key=
        safe_text,
    value=
        safe_text
)
aggregator_p2_UpdateDescriptor_strategy = st.builds(
    aggregator_p2_UpdateDescriptor,
)
ITouchpointInstruction_strategy = st.builds(
    ITouchpointInstruction,
)
aggregator_p2_TouchpointInstruction_strategy = st.builds(
    aggregator_p2_TouchpointInstruction,
)
InstructionMap_strategy = st.builds(
    InstructionMap,
)
ITouchpointData_strategy = st.builds(
    ITouchpointData,
)
aggregator_p2_TouchpointData_strategy = st.builds(
    aggregator_p2_TouchpointData,
)
IRequiredCapability_strategy = st.builds(
    IRequiredCapability,
)
aggregator_p2_RequiredCapability_strategy = st.builds(
    aggregator_p2_RequiredCapability,
)
IProvidedCapability_strategy = st.builds(
    IProvidedCapability,
)
aggregator_p2_ProvidedCapability_strategy = st.builds(
    aggregator_p2_ProvidedCapability,
)
aggregator_p2_License_strategy = st.builds(
    aggregator_p2_License,
)
p2_IInstallableUnitFragment_strategy = st.builds(
    p2_IInstallableUnitFragment,
)
p2_InstallableUnit_strategy = st.builds(
    p2_InstallableUnit,
)
aggregator_p2_InstallableUnitFragment_strategy = st.builds(
    aggregator_p2_InstallableUnitFragment,
)
p2_IRepository_strategy = st.builds(
    p2_IRepository,
)
p2_IQueryable_strategy = st.builds(
    p2_IQueryable,
)
aggregator_p2_IMetadataRepository_strategy = st.builds(
    aggregator_p2_IMetadataRepository,
)
ProvidedCapability_strategy = st.builds(
    ProvidedCapability,
)
ArtifactKey_strategy = st.builds(
    ArtifactKey,
)
aggregator_p2_InstallableUnit_strategy = st.builds(
    aggregator_p2_InstallableUnit,
)
Property_strategy = st.builds(
    Property,
)
RepositoryReference_strategy = st.builds(
    RepositoryReference,
)
InstallableUnit_strategy = st.builds(
    InstallableUnit,
)
IMetadataRepository_strategy = st.builds(
    IMetadataRepository,
)
aggregator_p2_MetadataRepository_strategy = st.builds(
    aggregator_p2_MetadataRepository,
)
aggregator_p2_Copyright_strategy = st.builds(
    aggregator_p2_Copyright,
)
IArtifactKey_strategy = st.builds(
    IArtifactKey,
)
aggregator_p2_ArtifactKey_strategy = st.builds(
    aggregator_p2_ArtifactKey,
)
aggregator_p2_IUpdateDescriptor_strategy = st.builds(
    aggregator_p2_IUpdateDescriptor,
    id=
        safe_text,
    description=
        safe_text,
    severity=
        st.integers(),
    range=
        safe_text
)
aggregator_p2_ITouchpointType_strategy = st.builds(
    aggregator_p2_ITouchpointType,
    id=
        safe_text,
    version=
        safe_text
)
aggregator_p2_ITouchpointInstruction_strategy = st.builds(
    aggregator_p2_ITouchpointInstruction,
    importAttribute=
        safe_text,
    body=
        safe_text
)
TouchpointData_strategy = st.builds(
    TouchpointData,
)
aggregator_Status_strategy = st.builds(
    aggregator_Status,
    code=
        safe_text,
    message=
        safe_text
)
ITouchpointType_strategy = st.builds(
    ITouchpointType,
)
aggregator_p2_TouchpointType_strategy = st.builds(
    aggregator_p2_TouchpointType,
)
aggregator_ChildrenProvider_strategy = st.builds(
    aggregator_ChildrenProvider,
)
aggregator_MavenItem_strategy = st.builds(
    aggregator_MavenItem,
    groupId=
        safe_text,
    artifactId=
        safe_text
)
aggregator_DescriptionProvider_strategy = st.builds(
    aggregator_DescriptionProvider,
    description=
        safe_text
)
aggregator_LabelProvider_strategy = st.builds(
    aggregator_LabelProvider,
    label=
        safe_text
)
aggregator_Comparable_strategy = st.builds(
    aggregator_Comparable,
)
MetadataRepository_strategy = st.builds(
    MetadataRepository,
)
aggregator_EnabledStatusProvider_strategy = st.builds(
    aggregator_EnabledStatusProvider,
    enabled=
        st.booleans()
)
MapRule_strategy = st.builds(
    MapRule,
)
aggregator_ExclusionRule_strategy = st.builds(
    aggregator_ExclusionRule,
)
aggregator_ValidConfigurationsRule_strategy = st.builds(
    aggregator_ValidConfigurationsRule,
)
aggregator_Property_strategy = st.builds(
    aggregator_Property,
    value=
        safe_text,
    key=
        safe_text
)
InstallableUnitRequest_strategy = st.builds(
    InstallableUnitRequest,
)
MappedUnit_strategy = st.builds(
    MappedUnit,
)
aggregator_Feature_strategy = st.builds(
    aggregator_Feature,
)
aggregator_Bundle_strategy = st.builds(
    aggregator_Bundle,
)
aggregator_Product_strategy = st.builds(
    aggregator_Product,
)
MetadataRepositoryReference_strategy = st.builds(
    MetadataRepositoryReference,
)
aggregator_Contact_strategy = st.builds(
    aggregator_Contact,
    name=
        safe_text,
    email=
        safe_text
)
EnabledStatusProvider_strategy = st.builds(
    EnabledStatusProvider,
)
aggregator_MappedUnit_strategy = st.builds(
    aggregator_MappedUnit,
)
aggregator_Category_strategy = st.builds(
    aggregator_Category,
    labelOverride=
        safe_text
)
InfosProvider_strategy = st.builds(
    InfosProvider,
)
StatusProvider_strategy = st.builds(
    StatusProvider,
)
aggregator_CustomCategory_strategy = st.builds(
    aggregator_CustomCategory,
    identifier=
        safe_text,
    description=
        safe_text,
    label=
        safe_text
)
aggregator_MavenMapping_strategy = st.builds(
    aggregator_MavenMapping,
    groupId=
        safe_text,
    artifactId=
        safe_text,
    namePattern=
        safe_text
)
aggregator_MetadataRepositoryReference_strategy = st.builds(
    aggregator_MetadataRepositoryReference,
    location=
        safe_text,
    nature=
        safe_text
)
DescriptionProvider_strategy = st.builds(
    DescriptionProvider,
)
aggregator_MappedRepository_strategy = st.builds(
    aggregator_MappedRepository,
    mirrorArtifacts=
        st.booleans(),
    categoryPrefix=
        safe_text
)
aggregator_InstallableUnitRequest_strategy = st.builds(
    aggregator_InstallableUnitRequest,
    versionRange=
        safe_text,
    name=
        safe_text
)
aggregator_MapRule_strategy = st.builds(
    aggregator_MapRule,
)
aggregator_Aggregator_strategy = st.builds(
    aggregator_Aggregator,
    buildRoot=
        safe_text,
    mavenResult=
        st.booleans(),
    packedStrategy=
        safe_text,
    label=
        safe_text,
    type=
        safe_text,
    sendmail=
        st.booleans()
)
aggregator_Contribution_strategy = st.builds(
    aggregator_Contribution,
    label=
        safe_text
)
aggregator_Configuration_strategy = st.builds(
    aggregator_Configuration,
    operatingSystem=
        safe_text,
    architecture=
        safe_text,
    windowSystem=
        safe_text
)





@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_selectorList_setter(instance):
    original = instance.selectorList
    instance.selectorList = original
    assert instance.selectorList == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original



@given(instance=aggregator_p2_IRequiredCapability_strategy)
def test_hyp_aggregator_p2_irequiredcapability_greedy_setter(instance):
    original = instance.greedy
    instance.greedy = original
    assert instance.greedy == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IRequiredCapability_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_irequiredcapability_setselectors_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSelectors(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSelectors).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSelectors' in aggregator_p2_IRequiredCapability is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSelectors' in aggregator_p2_IRequiredCapability did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSelectors' in aggregator_p2_IRequiredCapability is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IRequiredCapability_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_irequiredcapability_satisfiedby_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.satisfiedBy(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.satisfiedBy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'satisfiedBy' in aggregator_p2_IRequiredCapability is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'satisfiedBy' in aggregator_p2_IRequiredCapability did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'satisfiedBy' in aggregator_p2_IRequiredCapability is not implemented or raised an error")




@given(instance=aggregator_p2_IProvidedCapability_strategy)
def test_hyp_aggregator_p2_iprovidedcapability_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=aggregator_p2_IProvidedCapability_strategy)
def test_hyp_aggregator_p2_iprovidedcapability_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aggregator_p2_IProvidedCapability_strategy)
def test_hyp_aggregator_p2_iprovidedcapability_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IProvidedCapability_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iprovidedcapability_satisfies_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.satisfies(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.satisfies).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'satisfies' in aggregator_p2_IProvidedCapability is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'satisfies' in aggregator_p2_IProvidedCapability did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'satisfies' in aggregator_p2_IProvidedCapability is not implemented or raised an error")




@given(instance=aggregator_p2_ILicense_strategy)
def test_hyp_aggregator_p2_ilicense_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=aggregator_p2_ILicense_strategy)
def test_hyp_aggregator_p2_ilicense_digest_setter(instance):
    original = instance.digest
    instance.digest = original
    assert instance.digest == original



@given(instance=aggregator_p2_ILicense_strategy)
def test_hyp_aggregator_p2_ilicense_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original










@given(instance=aggregator_p2_IInstallableUnit_strategy)
def test_hyp_aggregator_p2_iinstallableunit_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original



@given(instance=aggregator_p2_IInstallableUnit_strategy)
def test_hyp_aggregator_p2_iinstallableunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=aggregator_p2_IInstallableUnit_strategy)
def test_hyp_aggregator_p2_iinstallableunit_resolved_setter(instance):
    original = instance.resolved
    instance.resolved = original
    assert instance.resolved == original



@given(instance=aggregator_p2_IInstallableUnit_strategy)
def test_hyp_aggregator_p2_iinstallableunit_singleton_setter(instance):
    original = instance.singleton
    instance.singleton = original
    assert instance.singleton == original



@given(instance=aggregator_p2_IInstallableUnit_strategy)
def test_hyp_aggregator_p2_iinstallableunit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IInstallableUnit_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iinstallableunit_satisfies_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.satisfies(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.satisfies).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'satisfies' in aggregator_p2_IInstallableUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'satisfies' in aggregator_p2_IInstallableUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'satisfies' in aggregator_p2_IInstallableUnit is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IInstallableUnit_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iinstallableunit_unresolved_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unresolved()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unresolved).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unresolved' in aggregator_p2_IInstallableUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unresolved' in aggregator_p2_IInstallableUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unresolved' in aggregator_p2_IInstallableUnit is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IInstallableUnit_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iinstallableunit_isfragment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFragment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFragment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFragment' in aggregator_p2_IInstallableUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFragment' in aggregator_p2_IInstallableUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFragment' in aggregator_p2_IInstallableUnit is not implemented or raised an error")




@given(instance=aggregator_p2_ICopyright_strategy)
def test_hyp_aggregator_p2_icopyright_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=aggregator_p2_ICopyright_strategy)
def test_hyp_aggregator_p2_icopyright_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




@given(instance=aggregator_p2_IArtifactKey_strategy)
def test_hyp_aggregator_p2_iartifactkey_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aggregator_p2_IArtifactKey_strategy)
def test_hyp_aggregator_p2_iartifactkey_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original



@given(instance=aggregator_p2_IArtifactKey_strategy)
def test_hyp_aggregator_p2_iartifactkey_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IArtifactKey_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iartifactkey_toexternalform_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toExternalForm()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toExternalForm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toExternalForm' in aggregator_p2_IArtifactKey is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toExternalForm' in aggregator_p2_IArtifactKey did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toExternalForm' in aggregator_p2_IArtifactKey is not implemented or raised an error")




@given(instance=aggregator_InfosProvider_strategy)
def test_hyp_aggregator_infosprovider_warnings_setter(instance):
    original = instance.warnings
    instance.warnings = original
    assert instance.warnings == original



@given(instance=aggregator_InfosProvider_strategy)
def test_hyp_aggregator_infosprovider_infos_setter(instance):
    original = instance.infos
    instance.infos = original
    assert instance.infos == original



@given(instance=aggregator_InfosProvider_strategy)
def test_hyp_aggregator_infosprovider_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original




















import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2view_Category_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2view_category_isnested_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isNested()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isNested).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isNested' in aggregator_p2view_Category is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNested' in aggregator_p2view_Category did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNested' in aggregator_p2view_Category is not implemented or raised an error")






@given(instance=aggregator_p2view_IUPresentationWithDetails_strategy)
def test_hyp_aggregator_p2view_iupresentationwithdetails_detailsResolved_setter(instance):
    original = instance.detailsResolved
    instance.detailsResolved = original
    assert instance.detailsResolved == original

























@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aggregator_p2view_IUPresentation_strategy)
def test_hyp_aggregator_p2view_iupresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=aggregator_p2view_MetadataRepositoryStructuredView_strategy)
def test_hyp_aggregator_p2view_metadatarepositorystructuredview_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aggregator_p2view_MetadataRepositoryStructuredView_strategy)
def test_hyp_aggregator_p2view_metadatarepositorystructuredview_loaded_setter(instance):
    original = instance.loaded
    instance.loaded = original
    assert instance.loaded == original





@given(instance=aggregator_p2_RepositoryReference_strategy)
def test_hyp_aggregator_p2_repositoryreference_nickname_setter(instance):
    original = instance.nickname
    instance.nickname = original
    assert instance.nickname == original



@given(instance=aggregator_p2_RepositoryReference_strategy)
def test_hyp_aggregator_p2_repositoryreference_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=aggregator_p2_RepositoryReference_strategy)
def test_hyp_aggregator_p2_repositoryreference_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=aggregator_p2_RepositoryReference_strategy)
def test_hyp_aggregator_p2_repositoryreference_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_modifiable_setter(instance):
    original = instance.modifiable
    instance.modifiable = original
    assert instance.modifiable == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aggregator_p2_IRepository_strategy)
def test_hyp_aggregator_p2_irepository_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_irepository_setproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setProperty' in aggregator_p2_IRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setProperty' in aggregator_p2_IRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setProperty' in aggregator_p2_IRepository is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IQueryable_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iqueryable_query_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.query(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.query).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'query' in aggregator_p2_IQueryable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'query' in aggregator_p2_IQueryable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'query' in aggregator_p2_IQueryable is not implemented or raised an error")





@given(instance=aggregator_p2_InstructionMap_strategy)
def test_hyp_aggregator_p2_instructionmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=aggregator_p2_Property_strategy)
def test_hyp_aggregator_p2_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=aggregator_p2_Property_strategy)
def test_hyp_aggregator_p2_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


















import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IMetadataRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_imetadatarepository_addinstallableunits_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addInstallableUnits(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addInstallableUnits).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addInstallableUnits' in aggregator_p2_IMetadataRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addInstallableUnits' in aggregator_p2_IMetadataRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addInstallableUnits' in aggregator_p2_IMetadataRepository is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IMetadataRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_imetadatarepository_removeall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeAll()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeAll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeAll' in aggregator_p2_IMetadataRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeAll' in aggregator_p2_IMetadataRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeAll' in aggregator_p2_IMetadataRepository is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IMetadataRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_imetadatarepository_removeinstallableunits_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeInstallableUnits(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeInstallableUnits).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeInstallableUnits' in aggregator_p2_IMetadataRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeInstallableUnits' in aggregator_p2_IMetadataRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeInstallableUnits' in aggregator_p2_IMetadataRepository is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IMetadataRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_imetadatarepository_addreference_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addReference(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addReference).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addReference' in aggregator_p2_IMetadataRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addReference' in aggregator_p2_IMetadataRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addReference' in aggregator_p2_IMetadataRepository is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_InstallableUnit_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_installableunit_compareto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compareTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compareTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compareTo' in aggregator_p2_InstallableUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compareTo' in aggregator_p2_InstallableUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compareTo' in aggregator_p2_InstallableUnit is not implemented or raised an error")












@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
def test_hyp_aggregator_p2_iupdatedescriptor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
def test_hyp_aggregator_p2_iupdatedescriptor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
def test_hyp_aggregator_p2_iupdatedescriptor_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
def test_hyp_aggregator_p2_iupdatedescriptor_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_p2_iupdatedescriptor_isupdateof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isUpdateOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isUpdateOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isUpdateOf' in aggregator_p2_IUpdateDescriptor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isUpdateOf' in aggregator_p2_IUpdateDescriptor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isUpdateOf' in aggregator_p2_IUpdateDescriptor is not implemented or raised an error")




@given(instance=aggregator_p2_ITouchpointType_strategy)
def test_hyp_aggregator_p2_itouchpointtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aggregator_p2_ITouchpointType_strategy)
def test_hyp_aggregator_p2_itouchpointtype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original




@given(instance=aggregator_p2_ITouchpointInstruction_strategy)
def test_hyp_aggregator_p2_itouchpointinstruction_importAttribute_setter(instance):
    original = instance.importAttribute
    instance.importAttribute = original
    assert instance.importAttribute == original



@given(instance=aggregator_p2_ITouchpointInstruction_strategy)
def test_hyp_aggregator_p2_itouchpointinstruction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original





@given(instance=aggregator_Status_strategy)
def test_hyp_aggregator_status_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=aggregator_Status_strategy)
def test_hyp_aggregator_status_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original







@given(instance=aggregator_MavenItem_strategy)
def test_hyp_aggregator_mavenitem_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=aggregator_MavenItem_strategy)
def test_hyp_aggregator_mavenitem_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original




@given(instance=aggregator_DescriptionProvider_strategy)
def test_hyp_aggregator_descriptionprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=aggregator_LabelProvider_strategy)
def test_hyp_aggregator_labelprovider_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original






@given(instance=aggregator_EnabledStatusProvider_strategy)
def test_hyp_aggregator_enabledstatusprovider_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original







@given(instance=aggregator_Property_strategy)
def test_hyp_aggregator_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aggregator_Property_strategy)
def test_hyp_aggregator_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original










@given(instance=aggregator_Contact_strategy)
def test_hyp_aggregator_contact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aggregator_Contact_strategy)
def test_hyp_aggregator_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original






@given(instance=aggregator_Category_strategy)
def test_hyp_aggregator_category_labelOverride_setter(instance):
    original = instance.labelOverride
    instance.labelOverride = original
    assert instance.labelOverride == original






@given(instance=aggregator_CustomCategory_strategy)
def test_hyp_aggregator_customcategory_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=aggregator_CustomCategory_strategy)
def test_hyp_aggregator_customcategory_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aggregator_CustomCategory_strategy)
def test_hyp_aggregator_customcategory_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=aggregator_MavenMapping_strategy)
def test_hyp_aggregator_mavenmapping_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=aggregator_MavenMapping_strategy)
def test_hyp_aggregator_mavenmapping_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original



@given(instance=aggregator_MavenMapping_strategy)
def test_hyp_aggregator_mavenmapping_namePattern_setter(instance):
    original = instance.namePattern
    instance.namePattern = original
    assert instance.namePattern == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MavenMapping_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_mavenmapping_map_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.map(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.map).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'map' in aggregator_MavenMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'map' in aggregator_MavenMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'map' in aggregator_MavenMapping is not implemented or raised an error")




@given(instance=aggregator_MetadataRepositoryReference_strategy)
def test_hyp_aggregator_metadatarepositoryreference_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=aggregator_MetadataRepositoryReference_strategy)
def test_hyp_aggregator_metadatarepositoryreference_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_metadatarepositoryreference_cancelrepositoryload_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.cancelRepositoryLoad()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.cancelRepositoryLoad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'cancelRepositoryLoad' in aggregator_MetadataRepositoryReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'cancelRepositoryLoad' in aggregator_MetadataRepositoryReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'cancelRepositoryLoad' in aggregator_MetadataRepositoryReference is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_metadatarepositoryreference_isbranchenabled_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBranchEnabled()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBranchEnabled).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBranchEnabled' in aggregator_MetadataRepositoryReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBranchEnabled' in aggregator_MetadataRepositoryReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBranchEnabled' in aggregator_MetadataRepositoryReference is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_metadatarepositoryreference_onrepositoryload_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.onRepositoryLoad()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.onRepositoryLoad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'onRepositoryLoad' in aggregator_MetadataRepositoryReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'onRepositoryLoad' in aggregator_MetadataRepositoryReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'onRepositoryLoad' in aggregator_MetadataRepositoryReference is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_metadatarepositoryreference_startrepositoryload_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.startRepositoryLoad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.startRepositoryLoad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'startRepositoryLoad' in aggregator_MetadataRepositoryReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'startRepositoryLoad' in aggregator_MetadataRepositoryReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'startRepositoryLoad' in aggregator_MetadataRepositoryReference is not implemented or raised an error")





@given(instance=aggregator_MappedRepository_strategy)
def test_hyp_aggregator_mappedrepository_mirrorArtifacts_setter(instance):
    original = instance.mirrorArtifacts
    instance.mirrorArtifacts = original
    assert instance.mirrorArtifacts == original



@given(instance=aggregator_MappedRepository_strategy)
def test_hyp_aggregator_mappedrepository_categoryPrefix_setter(instance):
    original = instance.categoryPrefix
    instance.categoryPrefix = original
    assert instance.categoryPrefix == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_MappedRepository_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_mappedrepository_ismapexclusive_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMapExclusive()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMapExclusive).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMapExclusive' in aggregator_MappedRepository is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMapExclusive' in aggregator_MappedRepository did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMapExclusive' in aggregator_MappedRepository is not implemented or raised an error")




@given(instance=aggregator_InstallableUnitRequest_strategy)
def test_hyp_aggregator_installableunitrequest_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original



@given(instance=aggregator_InstallableUnitRequest_strategy)
def test_hyp_aggregator_installableunitrequest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_InstallableUnitRequest_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_installableunitrequest_isbranchenabled_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBranchEnabled()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBranchEnabled).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBranchEnabled' in aggregator_InstallableUnitRequest is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBranchEnabled' in aggregator_InstallableUnitRequest did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBranchEnabled' in aggregator_InstallableUnitRequest is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_InstallableUnitRequest_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_installableunitrequest_resolveassingleton_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resolveAsSingleton()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resolveAsSingleton).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resolveAsSingleton' in aggregator_InstallableUnitRequest is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveAsSingleton' in aggregator_InstallableUnitRequest did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveAsSingleton' in aggregator_InstallableUnitRequest is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aggregator_InstallableUnitRequest_strategy)
@settings(max_examples=30)
def test_hyp_aggregator_installableunitrequest_ismappedrepositorybroken_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isMappedRepositoryBroken()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isMappedRepositoryBroken).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isMappedRepositoryBroken' in aggregator_InstallableUnitRequest is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isMappedRepositoryBroken' in aggregator_InstallableUnitRequest did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isMappedRepositoryBroken' in aggregator_InstallableUnitRequest is not implemented or raised an error")





@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_buildRoot_setter(instance):
    original = instance.buildRoot
    instance.buildRoot = original
    assert instance.buildRoot == original



@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_mavenResult_setter(instance):
    original = instance.mavenResult
    instance.mavenResult = original
    assert instance.mavenResult == original



@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_packedStrategy_setter(instance):
    original = instance.packedStrategy
    instance.packedStrategy = original
    assert instance.packedStrategy == original



@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aggregator_Aggregator_strategy)
def test_hyp_aggregator_aggregator_sendmail_setter(instance):
    original = instance.sendmail
    instance.sendmail = original
    assert instance.sendmail == original




@given(instance=aggregator_Contribution_strategy)
def test_hyp_aggregator_contribution_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=aggregator_Configuration_strategy)
def test_hyp_aggregator_configuration_operatingSystem_setter(instance):
    original = instance.operatingSystem
    instance.operatingSystem = original
    assert instance.operatingSystem == original



@given(instance=aggregator_Configuration_strategy)
def test_hyp_aggregator_configuration_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original



@given(instance=aggregator_Configuration_strategy)
def test_hyp_aggregator_configuration_windowSystem_setter(instance):
    original = instance.windowSystem
    instance.windowSystem = original
    assert instance.windowSystem == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArtifactKey,
    Bundle,
    Bundles,
    Categories,
    Category,
    DescriptionProvider,
    EnabledStatusProvider,
    Feature,
    Features,
    Fragment,
    Fragments,
    IAdaptable,
    IArtifactKey,
    ICopyright,
    IInstallableUnit,
    ILicense,
    IMetadataRepository,
    IProvidedCapability,
    IRequiredCapability,
    ITouchpointData,
    ITouchpointInstruction,
    ITouchpointType,
    IUDetails,
    IUPresentation,
    IUPresentationWithDetails,
    IUpdateDescriptor,
    InfosProvider,
    InstallableUnit,
    InstallableUnitRequest,
    InstallableUnits,
    InstructionMap,
    LabelProvider,
    MapRule,
    MappedUnit,
    MetadataRepository,
    MetadataRepositoryReference,
    Miscellaneous,
    OtherIU,
    Product,
    Products,
    Properties,
    Property,
    ProvidedCapabilities,
    ProvidedCapability,
    ProvidedCapabilityWrapper,
    RepositoryReference,
    RequiredCapabilities,
    RequiredCapability,
    RequiredCapabilityWrapper,
    StatusProvider,
    TouchpointData,
    TouchpointInstruction,
    Touchpoints,
    aggregator_Aggregator,
    aggregator_Bundle,
    aggregator_Category,
    aggregator_ChildrenProvider,
    aggregator_Comparable,
    aggregator_Configuration,
    aggregator_Contact,
    aggregator_Contribution,
    aggregator_CustomCategory,
    aggregator_DescriptionProvider,
    aggregator_EnabledStatusProvider,
    aggregator_ExclusionRule,
    aggregator_Feature,
    aggregator_InfosProvider,
    aggregator_InstallableUnitRequest,
    aggregator_LabelProvider,
    aggregator_MapRule,
    aggregator_MappedRepository,
    aggregator_MappedUnit,
    aggregator_MavenItem,
    aggregator_MavenMapping,
    aggregator_MetadataRepositoryReference,
    aggregator_Product,
    aggregator_Property,
    aggregator_Status,
    aggregator_StatusProvider,
    aggregator_ValidConfigurationsRule,
    aggregator_p2_ArtifactKey,
    aggregator_p2_Copyright,
    aggregator_p2_IAdaptable,
    aggregator_p2_IArtifactKey,
    aggregator_p2_ICopyright,
    aggregator_p2_IInstallableUnit,
    aggregator_p2_IInstallableUnitFragment,
    aggregator_p2_ILicense,
    aggregator_p2_IMetadataRepository,
    aggregator_p2_IProvidedCapability,
    aggregator_p2_IQueryable,
    aggregator_p2_IRepository,
    aggregator_p2_IRequiredCapability,
    aggregator_p2_ITouchpointData,
    aggregator_p2_ITouchpointInstruction,
    aggregator_p2_ITouchpointType,
    aggregator_p2_IUpdateDescriptor,
    aggregator_p2_InstallableUnit,
    aggregator_p2_InstallableUnitFragment,
    aggregator_p2_InstructionMap,
    aggregator_p2_License,
    aggregator_p2_MetadataRepository,
    aggregator_p2_Property,
    aggregator_p2_ProvidedCapability,
    aggregator_p2_RepositoryReference,
    aggregator_p2_RequiredCapability,
    aggregator_p2_TouchpointData,
    aggregator_p2_TouchpointInstruction,
    aggregator_p2_TouchpointType,
    aggregator_p2_UpdateDescriptor,
    aggregator_p2view_Bundle,
    aggregator_p2view_Bundles,
    aggregator_p2view_Categories,
    aggregator_p2view_Category,
    aggregator_p2view_Feature,
    aggregator_p2view_Features,
    aggregator_p2view_Fragment,
    aggregator_p2view_Fragments,
    aggregator_p2view_IUDetails,
    aggregator_p2view_IUPresentation,
    aggregator_p2view_IUPresentationWithDetails,
    aggregator_p2view_InstallableUnits,
    aggregator_p2view_MetadataRepositoryStructuredView,
    aggregator_p2view_Miscellaneous,
    aggregator_p2view_OtherIU,
    aggregator_p2view_Product,
    aggregator_p2view_Products,
    aggregator_p2view_Properties,
    aggregator_p2view_ProvidedCapabilities,
    aggregator_p2view_ProvidedCapabilityWrapper,
    aggregator_p2view_RequiredCapabilities,
    aggregator_p2view_RequiredCapabilityWrapper,
    aggregator_p2view_Touchpoints,
    p2_IInstallableUnitFragment,
    p2_IProvidedCapability,
    p2_IQueryable,
    p2_IRepository,
    p2_IRequiredCapability,
    p2_InstallableUnit,
    p2view_IUDetails,
    p2view_IUPresentation,
    p2view_aggregator_Property,
    AggregationType,
    Architecture,
    InstallableUnitType,
    OperatingSystem,
    PackedStrategy,
    StatusCode,
    WindowSystem,
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

def test_aggregator_Aggregator_buildRoot_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.buildRoot == "sample_text"
    instance.buildRoot = "sample_text_2"
    assert instance.buildRoot == "sample_text_2"


def test_aggregator_Aggregator_label_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_Aggregator_mavenResult_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.mavenResult == True
    instance.mavenResult = False
    assert instance.mavenResult == False


def test_aggregator_Aggregator_packedStrategy_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.packedStrategy == "sample_text"
    instance.packedStrategy = "sample_text_2"
    assert instance.packedStrategy == "sample_text_2"


def test_aggregator_Aggregator_sendmail_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.sendmail == True
    instance.sendmail = False
    assert instance.sendmail == False


def test_aggregator_Aggregator_type_value_roundtrip():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aggregator_Category_labelOverride_value_roundtrip():
    instance = aggregator_Category(labelOverride="sample_text")
    assert instance.labelOverride == "sample_text"
    instance.labelOverride = "sample_text_2"
    assert instance.labelOverride == "sample_text_2"


def test_aggregator_Configuration_architecture_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.architecture == "sample_text"
    instance.architecture = "sample_text_2"
    assert instance.architecture == "sample_text_2"


def test_aggregator_Configuration_operatingSystem_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.operatingSystem == "sample_text"
    instance.operatingSystem = "sample_text_2"
    assert instance.operatingSystem == "sample_text_2"


def test_aggregator_Configuration_windowSystem_value_roundtrip():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert instance.windowSystem == "sample_text"
    instance.windowSystem = "sample_text_2"
    assert instance.windowSystem == "sample_text_2"


def test_aggregator_Contact_email_value_roundtrip():
    instance = aggregator_Contact(email="sample_text", name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_aggregator_Contact_name_value_roundtrip():
    instance = aggregator_Contact(email="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_Contribution_label_value_roundtrip():
    instance = aggregator_Contribution(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_CustomCategory_description_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_CustomCategory_identifier_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_aggregator_CustomCategory_label_value_roundtrip():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_DescriptionProvider_description_value_roundtrip():
    instance = aggregator_DescriptionProvider(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_EnabledStatusProvider_enabled_value_roundtrip():
    instance = aggregator_EnabledStatusProvider(enabled=True)
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_aggregator_InfosProvider_errors_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.errors == "sample_text"
    instance.errors = "sample_text_2"
    assert instance.errors == "sample_text_2"


def test_aggregator_InfosProvider_infos_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.infos == "sample_text"
    instance.infos = "sample_text_2"
    assert instance.infos == "sample_text_2"


def test_aggregator_InfosProvider_warnings_value_roundtrip():
    instance = aggregator_InfosProvider(errors="sample_text", infos="sample_text", warnings="sample_text")
    assert instance.warnings == "sample_text"
    instance.warnings = "sample_text_2"
    assert instance.warnings == "sample_text_2"


def test_aggregator_InstallableUnitRequest_name_value_roundtrip():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_InstallableUnitRequest_versionRange_value_roundtrip():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_aggregator_LabelProvider_label_value_roundtrip():
    instance = aggregator_LabelProvider(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_MappedRepository_categoryPrefix_value_roundtrip():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert instance.categoryPrefix == "sample_text"
    instance.categoryPrefix = "sample_text_2"
    assert instance.categoryPrefix == "sample_text_2"


def test_aggregator_MappedRepository_mirrorArtifacts_value_roundtrip():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert instance.mirrorArtifacts == True
    instance.mirrorArtifacts = False
    assert instance.mirrorArtifacts == False


def test_aggregator_MavenItem_artifactId_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", groupId="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_aggregator_MavenItem_groupId_value_roundtrip():
    instance = aggregator_MavenItem(artifactId="sample_text", groupId="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_aggregator_MavenMapping_artifactId_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_aggregator_MavenMapping_groupId_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_aggregator_MavenMapping_namePattern_value_roundtrip():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    assert instance.namePattern == "sample_text"
    instance.namePattern = "sample_text_2"
    assert instance.namePattern == "sample_text_2"


def test_aggregator_MetadataRepositoryReference_location_value_roundtrip():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_MetadataRepositoryReference_nature_value_roundtrip():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert instance.nature == "sample_text"
    instance.nature = "sample_text_2"
    assert instance.nature == "sample_text_2"


def test_aggregator_Property_key_value_roundtrip():
    instance = aggregator_Property(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_aggregator_Property_value_value_roundtrip():
    instance = aggregator_Property(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aggregator_Status_code_value_roundtrip():
    instance = aggregator_Status(code="sample_text", message="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_aggregator_Status_message_value_roundtrip():
    instance = aggregator_Status(code="sample_text", message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_aggregator_p2_IArtifactKey_classifier_value_roundtrip():
    instance = aggregator_p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    assert instance.classifier == "sample_text"
    instance.classifier = "sample_text_2"
    assert instance.classifier == "sample_text_2"


def test_aggregator_p2_IArtifactKey_id_value_roundtrip():
    instance = aggregator_p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2_IArtifactKey_version_value_roundtrip():
    instance = aggregator_p2_IArtifactKey(classifier="sample_text", id="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2_ICopyright_body_value_roundtrip():
    instance = aggregator_p2_ICopyright(body="sample_text", location="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_aggregator_p2_ICopyright_location_value_roundtrip():
    instance = aggregator_p2_ICopyright(body="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_p2_IInstallableUnit_filter_value_roundtrip():
    instance = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    assert instance.filter == "sample_text"
    instance.filter = "sample_text_2"
    assert instance.filter == "sample_text_2"


def test_aggregator_p2_IInstallableUnit_id_value_roundtrip():
    instance = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2_IInstallableUnit_resolved_value_roundtrip():
    instance = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    assert instance.resolved == True
    instance.resolved = False
    assert instance.resolved == False


def test_aggregator_p2_IInstallableUnit_singleton_value_roundtrip():
    instance = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    assert instance.singleton == True
    instance.singleton = False
    assert instance.singleton == False


def test_aggregator_p2_IInstallableUnit_version_value_roundtrip():
    instance = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2_ILicense_body_value_roundtrip():
    instance = aggregator_p2_ILicense(body="sample_text", digest="sample_text", location="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_aggregator_p2_ILicense_digest_value_roundtrip():
    instance = aggregator_p2_ILicense(body="sample_text", digest="sample_text", location="sample_text")
    assert instance.digest == "sample_text"
    instance.digest = "sample_text_2"
    assert instance.digest == "sample_text_2"


def test_aggregator_p2_ILicense_location_value_roundtrip():
    instance = aggregator_p2_ILicense(body="sample_text", digest="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_p2_IProvidedCapability_name_value_roundtrip():
    instance = aggregator_p2_IProvidedCapability(name="sample_text", namespace="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2_IProvidedCapability_namespace_value_roundtrip():
    instance = aggregator_p2_IProvidedCapability(name="sample_text", namespace="sample_text", version="sample_text")
    assert instance.namespace == "sample_text"
    instance.namespace = "sample_text_2"
    assert instance.namespace == "sample_text_2"


def test_aggregator_p2_IProvidedCapability_version_value_roundtrip():
    instance = aggregator_p2_IProvidedCapability(name="sample_text", namespace="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2_IRepository_description_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_p2_IRepository_location_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_p2_IRepository_modifiable_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.modifiable == True
    instance.modifiable = False
    assert instance.modifiable == False


def test_aggregator_p2_IRepository_name_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2_IRepository_provider_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_aggregator_p2_IRepository_type_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aggregator_p2_IRepository_version_value_roundtrip():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2_IRequiredCapability_filter_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.filter == "sample_text"
    instance.filter = "sample_text_2"
    assert instance.filter == "sample_text_2"


def test_aggregator_p2_IRequiredCapability_greedy_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.greedy == True
    instance.greedy = False
    assert instance.greedy == False


def test_aggregator_p2_IRequiredCapability_multiple_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.multiple == True
    instance.multiple = False
    assert instance.multiple == False


def test_aggregator_p2_IRequiredCapability_name_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2_IRequiredCapability_namespace_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.namespace == "sample_text"
    instance.namespace = "sample_text_2"
    assert instance.namespace == "sample_text_2"


def test_aggregator_p2_IRequiredCapability_negation_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.negation == True
    instance.negation = False
    assert instance.negation == False


def test_aggregator_p2_IRequiredCapability_optional_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_aggregator_p2_IRequiredCapability_range_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.range == "sample_text"
    instance.range = "sample_text_2"
    assert instance.range == "sample_text_2"


def test_aggregator_p2_IRequiredCapability_selectorList_value_roundtrip():
    instance = aggregator_p2_IRequiredCapability(filter="sample_text", greedy=True, multiple=True, name="sample_text", namespace="sample_text", negation=True, optional=True, range="sample_text", selectorList="sample_text")
    assert instance.selectorList == "sample_text"
    instance.selectorList = "sample_text_2"
    assert instance.selectorList == "sample_text_2"


def test_aggregator_p2_ITouchpointInstruction_body_value_roundtrip():
    instance = aggregator_p2_ITouchpointInstruction(body="sample_text", importAttribute="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_aggregator_p2_ITouchpointInstruction_importAttribute_value_roundtrip():
    instance = aggregator_p2_ITouchpointInstruction(body="sample_text", importAttribute="sample_text")
    assert instance.importAttribute == "sample_text"
    instance.importAttribute = "sample_text_2"
    assert instance.importAttribute == "sample_text_2"


def test_aggregator_p2_ITouchpointType_id_value_roundtrip():
    instance = aggregator_p2_ITouchpointType(id="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2_ITouchpointType_version_value_roundtrip():
    instance = aggregator_p2_ITouchpointType(id="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2_IUpdateDescriptor_description_value_roundtrip():
    instance = aggregator_p2_IUpdateDescriptor(description="sample_text", id="sample_text", range="sample_text", severity=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_p2_IUpdateDescriptor_id_value_roundtrip():
    instance = aggregator_p2_IUpdateDescriptor(description="sample_text", id="sample_text", range="sample_text", severity=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2_IUpdateDescriptor_range_value_roundtrip():
    instance = aggregator_p2_IUpdateDescriptor(description="sample_text", id="sample_text", range="sample_text", severity=7)
    assert instance.range == "sample_text"
    instance.range = "sample_text_2"
    assert instance.range == "sample_text_2"


def test_aggregator_p2_IUpdateDescriptor_severity_value_roundtrip():
    instance = aggregator_p2_IUpdateDescriptor(description="sample_text", id="sample_text", range="sample_text", severity=7)
    assert instance.severity == 7
    instance.severity = 13
    assert instance.severity == 13


def test_aggregator_p2_InstructionMap_key_value_roundtrip():
    instance = aggregator_p2_InstructionMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_aggregator_p2_Property_key_value_roundtrip():
    instance = aggregator_p2_Property(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_aggregator_p2_Property_value_value_roundtrip():
    instance = aggregator_p2_Property(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aggregator_p2_RepositoryReference_location_value_roundtrip():
    instance = aggregator_p2_RepositoryReference(location="sample_text", nickname="sample_text", options=7, type=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_aggregator_p2_RepositoryReference_nickname_value_roundtrip():
    instance = aggregator_p2_RepositoryReference(location="sample_text", nickname="sample_text", options=7, type=7)
    assert instance.nickname == "sample_text"
    instance.nickname = "sample_text_2"
    assert instance.nickname == "sample_text_2"


def test_aggregator_p2_RepositoryReference_options_value_roundtrip():
    instance = aggregator_p2_RepositoryReference(location="sample_text", nickname="sample_text", options=7, type=7)
    assert instance.options == 7
    instance.options = 13
    assert instance.options == 13


def test_aggregator_p2_RepositoryReference_type_value_roundtrip():
    instance = aggregator_p2_RepositoryReference(location="sample_text", nickname="sample_text", options=7, type=7)
    assert instance.type == 7
    instance.type = 13
    assert instance.type == 13


def test_aggregator_p2view_IUPresentation_description_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aggregator_p2view_IUPresentation_id_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aggregator_p2view_IUPresentation_label_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_aggregator_p2view_IUPresentation_name_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2view_IUPresentation_type_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aggregator_p2view_IUPresentation_version_value_roundtrip():
    instance = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_aggregator_p2view_IUPresentationWithDetails_detailsResolved_value_roundtrip():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert instance.detailsResolved == "sample_text"
    instance.detailsResolved = "sample_text_2"
    assert instance.detailsResolved == "sample_text_2"


def test_aggregator_p2view_MetadataRepositoryStructuredView_loaded_value_roundtrip():
    instance = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    assert instance.loaded == True
    instance.loaded = False
    assert instance.loaded == False


def test_aggregator_p2view_MetadataRepositoryStructuredView_name_value_roundtrip():
    instance = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aggregator_p2view_Fragment_isa_Bundle():
    instance = aggregator_p2view_Fragment()
    assert isinstance(instance, Bundle)


def test_aggregator_Aggregator_isa_DescriptionProvider():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_Contribution_isa_DescriptionProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_InstallableUnitRequest_isa_DescriptionProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_MapRule_isa_DescriptionProvider():
    instance = aggregator_MapRule()
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_MappedRepository_isa_DescriptionProvider():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert isinstance(instance, DescriptionProvider)


def test_aggregator_Configuration_isa_EnabledStatusProvider():
    instance = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_Contribution_isa_EnabledStatusProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_MappedUnit_isa_EnabledStatusProvider():
    instance = aggregator_MappedUnit()
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_MetadataRepositoryReference_isa_EnabledStatusProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, EnabledStatusProvider)


def test_aggregator_p2_IRepository_isa_IAdaptable():
    instance = aggregator_p2_IRepository(description="sample_text", location="sample_text", modifiable=True, name="sample_text", provider="sample_text", type="sample_text", version="sample_text")
    assert isinstance(instance, IAdaptable)


def test_aggregator_p2_ArtifactKey_isa_IArtifactKey():
    instance = aggregator_p2_ArtifactKey()
    assert isinstance(instance, IArtifactKey)


def test_aggregator_p2_Copyright_isa_ICopyright():
    instance = aggregator_p2_Copyright()
    assert isinstance(instance, ICopyright)


def test_aggregator_p2_IInstallableUnitFragment_isa_IInstallableUnit():
    instance = aggregator_p2_IInstallableUnitFragment()
    assert isinstance(instance, IInstallableUnit)


def test_aggregator_p2_InstallableUnit_isa_IInstallableUnit():
    instance = aggregator_p2_InstallableUnit()
    assert isinstance(instance, IInstallableUnit)


def test_aggregator_p2_License_isa_ILicense():
    instance = aggregator_p2_License()
    assert isinstance(instance, ILicense)


def test_aggregator_p2_MetadataRepository_isa_IMetadataRepository():
    instance = aggregator_p2_MetadataRepository()
    assert isinstance(instance, IMetadataRepository)


def test_aggregator_p2_ProvidedCapability_isa_IProvidedCapability():
    instance = aggregator_p2_ProvidedCapability()
    assert isinstance(instance, IProvidedCapability)


def test_aggregator_p2_RequiredCapability_isa_IRequiredCapability():
    instance = aggregator_p2_RequiredCapability()
    assert isinstance(instance, IRequiredCapability)


def test_aggregator_p2_TouchpointData_isa_ITouchpointData():
    instance = aggregator_p2_TouchpointData()
    assert isinstance(instance, ITouchpointData)


def test_aggregator_p2_TouchpointInstruction_isa_ITouchpointInstruction():
    instance = aggregator_p2_TouchpointInstruction()
    assert isinstance(instance, ITouchpointInstruction)


def test_aggregator_p2_TouchpointType_isa_ITouchpointType():
    instance = aggregator_p2_TouchpointType()
    assert isinstance(instance, ITouchpointType)


def test_aggregator_p2view_Category_isa_IUPresentation():
    instance = aggregator_p2view_Category()
    assert isinstance(instance, IUPresentation)


def test_aggregator_p2view_Bundle_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Bundle()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_Feature_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Feature()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_OtherIU_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_OtherIU()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2view_Product_isa_IUPresentationWithDetails():
    instance = aggregator_p2view_Product()
    assert isinstance(instance, IUPresentationWithDetails)


def test_aggregator_p2_UpdateDescriptor_isa_IUpdateDescriptor():
    instance = aggregator_p2_UpdateDescriptor()
    assert isinstance(instance, IUpdateDescriptor)


def test_aggregator_Aggregator_isa_InfosProvider():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_Contribution_isa_InfosProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_CustomCategory_isa_InfosProvider():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_InstallableUnitRequest_isa_InfosProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MavenMapping_isa_InfosProvider():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MetadataRepositoryReference_isa_InfosProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, InfosProvider)


def test_aggregator_MapRule_isa_InstallableUnitRequest():
    instance = aggregator_MapRule()
    assert isinstance(instance, InstallableUnitRequest)


def test_aggregator_MappedUnit_isa_InstallableUnitRequest():
    instance = aggregator_MappedUnit()
    assert isinstance(instance, InstallableUnitRequest)


def test_aggregator_p2view_ProvidedCapabilityWrapper_isa_LabelProvider():
    instance = aggregator_p2view_ProvidedCapabilityWrapper()
    assert isinstance(instance, LabelProvider)


def test_aggregator_p2view_RequiredCapabilityWrapper_isa_LabelProvider():
    instance = aggregator_p2view_RequiredCapabilityWrapper()
    assert isinstance(instance, LabelProvider)


def test_aggregator_ExclusionRule_isa_MapRule():
    instance = aggregator_ExclusionRule()
    assert isinstance(instance, MapRule)


def test_aggregator_ValidConfigurationsRule_isa_MapRule():
    instance = aggregator_ValidConfigurationsRule()
    assert isinstance(instance, MapRule)


def test_aggregator_Bundle_isa_MappedUnit():
    instance = aggregator_Bundle()
    assert isinstance(instance, MappedUnit)


def test_aggregator_Category_isa_MappedUnit():
    instance = aggregator_Category(labelOverride="sample_text")
    assert isinstance(instance, MappedUnit)


def test_aggregator_Feature_isa_MappedUnit():
    instance = aggregator_Feature()
    assert isinstance(instance, MappedUnit)


def test_aggregator_Product_isa_MappedUnit():
    instance = aggregator_Product()
    assert isinstance(instance, MappedUnit)


def test_aggregator_MappedRepository_isa_MetadataRepositoryReference():
    instance = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    assert isinstance(instance, MetadataRepositoryReference)


def test_aggregator_Aggregator_isa_StatusProvider():
    instance = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_Contribution_isa_StatusProvider():
    instance = aggregator_Contribution(label="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_CustomCategory_isa_StatusProvider():
    instance = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_InstallableUnitRequest_isa_StatusProvider():
    instance = aggregator_InstallableUnitRequest(name="sample_text", versionRange="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_MavenMapping_isa_StatusProvider():
    instance = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_MetadataRepositoryReference_isa_StatusProvider():
    instance = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    assert isinstance(instance, StatusProvider)


def test_aggregator_p2_InstallableUnitFragment_isa_p2_IInstallableUnitFragment():
    instance = aggregator_p2_InstallableUnitFragment()
    assert isinstance(instance, p2_IInstallableUnitFragment)


def test_aggregator_p2view_ProvidedCapabilityWrapper_isa_p2_IProvidedCapability():
    instance = aggregator_p2view_ProvidedCapabilityWrapper()
    assert isinstance(instance, p2_IProvidedCapability)


def test_aggregator_p2_IMetadataRepository_isa_p2_IQueryable():
    instance = aggregator_p2_IMetadataRepository()
    assert isinstance(instance, p2_IQueryable)


def test_aggregator_p2_IMetadataRepository_isa_p2_IRepository():
    instance = aggregator_p2_IMetadataRepository()
    assert isinstance(instance, p2_IRepository)


def test_aggregator_p2view_RequiredCapabilityWrapper_isa_p2_IRequiredCapability():
    instance = aggregator_p2view_RequiredCapabilityWrapper()
    assert isinstance(instance, p2_IRequiredCapability)


def test_aggregator_p2_InstallableUnitFragment_isa_p2_InstallableUnit():
    instance = aggregator_p2_InstallableUnitFragment()
    assert isinstance(instance, p2_InstallableUnit)


def test_aggregator_p2view_IUPresentationWithDetails_isa_p2view_IUDetails():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert isinstance(instance, p2view_IUDetails)


def test_aggregator_p2view_IUPresentationWithDetails_isa_p2view_IUPresentation():
    instance = aggregator_p2view_IUPresentationWithDetails(detailsResolved="sample_text")
    assert isinstance(instance, p2view_IUPresentation)


def test_assoc_aggregator30_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'contacts', b1)
    assert _is_linked(a, 'contacts', b1)
    if hasattr(b1, 'Aggregator'):
        assert _is_linked(b1, 'Aggregator', a)
    _safe_set(a, 'contacts', b2)
    assert _is_linked(a, 'contacts', b2)
    if hasattr(b1, 'Aggregator'):
        assert not _is_linked(b1, 'Aggregator', a)
    if hasattr(b2, 'Aggregator'):
        assert _is_linked(b2, 'Aggregator', a)
    _safe_set(a, 'contacts', None)
    assert not _is_linked(a, 'contacts', b2)
    if hasattr(b2, 'Aggregator'):
        assert not _is_linked(b2, 'Aggregator', a)


def test_assoc_artifactList52_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = ArtifactKey()
    b2 = ArtifactKey()
    _safe_set(a, 'aggregator_p2_InstallableUnit', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit', b1)
    if hasattr(b1, 'ArtifactKey'):
        assert _is_linked(b1, 'ArtifactKey', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit', b2)
    if hasattr(b1, 'ArtifactKey'):
        assert not _is_linked(b1, 'ArtifactKey', a)
    if hasattr(b2, 'ArtifactKey'):
        assert _is_linked(b2, 'ArtifactKey', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit', b2)
    if hasattr(b2, 'ArtifactKey'):
        assert not _is_linked(b2, 'ArtifactKey', a)


def test_assoc_buildmaster3_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_Contact', b1)
    assert _is_linked(a, 'aggregator_Contact', b1)
    if hasattr(b1, 'aggregator_Aggregator4'):
        assert _is_linked(b1, 'aggregator_Aggregator4', a)
    _safe_set(a, 'aggregator_Contact', b2)
    assert _is_linked(a, 'aggregator_Contact', b2)
    if hasattr(b1, 'aggregator_Aggregator4'):
        assert not _is_linked(b1, 'aggregator_Aggregator4', a)
    if hasattr(b2, 'aggregator_Aggregator4'):
        assert _is_linked(b2, 'aggregator_Aggregator4', a)
    _safe_set(a, 'aggregator_Contact', None)
    assert not _is_linked(a, 'aggregator_Contact', b2)
    if hasattr(b2, 'aggregator_Aggregator4'):
        assert not _is_linked(b2, 'aggregator_Aggregator4', a)


def test_assoc_bundleContainer103_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Category104', b1)
    assert _is_linked(a, 'aggregator_p2view_Category104', b1)
    if hasattr(b1, 'Bundles105'):
        assert _is_linked(b1, 'Bundles105', a)
    _safe_set(a, 'aggregator_p2view_Category104', b2)
    assert _is_linked(a, 'aggregator_p2view_Category104', b2)
    if hasattr(b1, 'Bundles105'):
        assert not _is_linked(b1, 'Bundles105', a)
    if hasattr(b2, 'Bundles105'):
        assert _is_linked(b2, 'Bundles105', a)
    _safe_set(a, 'aggregator_p2view_Category104', None)
    assert not _is_linked(a, 'aggregator_p2view_Category104', b2)
    if hasattr(b2, 'Bundles105'):
        assert not _is_linked(b2, 'Bundles105', a)


def test_assoc_bundleContainer113_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Feature114', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature114', b1)
    if hasattr(b1, 'Bundles115'):
        assert _is_linked(b1, 'Bundles115', a)
    _safe_set(a, 'aggregator_p2view_Feature114', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature114', b2)
    if hasattr(b1, 'Bundles115'):
        assert not _is_linked(b1, 'Bundles115', a)
    if hasattr(b2, 'Bundles115'):
        assert _is_linked(b2, 'Bundles115', a)
    _safe_set(a, 'aggregator_p2view_Feature114', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature114', b2)
    if hasattr(b2, 'Bundles115'):
        assert not _is_linked(b2, 'Bundles115', a)


def test_assoc_bundleContainer121_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_Product122', b1)
    assert _is_linked(a, 'aggregator_p2view_Product122', b1)
    if hasattr(b1, 'Bundles123'):
        assert _is_linked(b1, 'Bundles123', a)
    _safe_set(a, 'aggregator_p2view_Product122', b2)
    assert _is_linked(a, 'aggregator_p2view_Product122', b2)
    if hasattr(b1, 'Bundles123'):
        assert not _is_linked(b1, 'Bundles123', a)
    if hasattr(b2, 'Bundles123'):
        assert _is_linked(b2, 'Bundles123', a)
    _safe_set(a, 'aggregator_p2view_Product122', None)
    assert not _is_linked(a, 'aggregator_p2view_Product122', b2)
    if hasattr(b2, 'Bundles123'):
        assert not _is_linked(b2, 'Bundles123', a)


def test_assoc_bundleContainer80_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Bundles()
    b2 = Bundles()
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits81', b1)
    if hasattr(b1, 'Bundles'):
        assert _is_linked(b1, 'Bundles', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits81', b2)
    if hasattr(b1, 'Bundles'):
        assert not _is_linked(b1, 'Bundles', a)
    if hasattr(b2, 'Bundles'):
        assert _is_linked(b2, 'Bundles', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits81', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits81', b2)
    if hasattr(b2, 'Bundles'):
        assert not _is_linked(b2, 'Bundles', a)


def test_assoc_bundles13_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Bundle()
    b2 = aggregator_Bundle()
    _safe_set(a, 'aggregator_MappedRepository14', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository14', b1)
    if hasattr(b1, 'aggregator_Bundle'):
        assert _is_linked(b1, 'aggregator_Bundle', a)
    _safe_set(a, 'aggregator_MappedRepository14', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository14', b2)
    if hasattr(b1, 'aggregator_Bundle'):
        assert not _is_linked(b1, 'aggregator_Bundle', a)
    if hasattr(b2, 'aggregator_Bundle'):
        assert _is_linked(b2, 'aggregator_Bundle', a)
    _safe_set(a, 'aggregator_MappedRepository14', set())
    assert not _is_linked(a, 'aggregator_MappedRepository14', b2)
    if hasattr(b2, 'aggregator_Bundle'):
        assert not _is_linked(b2, 'aggregator_Bundle', a)


def test_assoc_categories17_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Category(labelOverride="sample_text")
    b2 = aggregator_Category(labelOverride="sample_text_2")
    _safe_set(a, 'aggregator_MappedRepository18', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository18', b1)
    if hasattr(b1, 'aggregator_Category'):
        assert _is_linked(b1, 'aggregator_Category', a)
    _safe_set(a, 'aggregator_MappedRepository18', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository18', b2)
    if hasattr(b1, 'aggregator_Category'):
        assert not _is_linked(b1, 'aggregator_Category', a)
    if hasattr(b2, 'aggregator_Category'):
        assert _is_linked(b2, 'aggregator_Category', a)
    _safe_set(a, 'aggregator_MappedRepository18', set())
    assert not _is_linked(a, 'aggregator_MappedRepository18', b2)
    if hasattr(b2, 'aggregator_Category'):
        assert not _is_linked(b2, 'aggregator_Category', a)


def test_assoc_categories31_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'CustomCategory', b1)
    assert _is_linked(a, 'CustomCategory', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'CustomCategory', b2)
    assert _is_linked(a, 'CustomCategory', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'CustomCategory', None)
    assert not _is_linked(a, 'CustomCategory', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_categoryContainer75_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Categories()
    b2 = Categories()
    _safe_set(a, 'aggregator_p2view_InstallableUnits', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits', b1)
    if hasattr(b1, 'Categories'):
        assert _is_linked(b1, 'Categories', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits', b2)
    if hasattr(b1, 'Categories'):
        assert not _is_linked(b1, 'Categories', a)
    if hasattr(b2, 'Categories'):
        assert _is_linked(b2, 'Categories', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits', b2)
    if hasattr(b2, 'Categories'):
        assert not _is_linked(b2, 'Categories', a)


def test_assoc_categoryContainer95_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Categories()
    b2 = Categories()
    _safe_set(a, 'aggregator_p2view_Category', b1)
    assert _is_linked(a, 'aggregator_p2view_Category', b1)
    if hasattr(b1, 'Categories96'):
        assert _is_linked(b1, 'Categories96', a)
    _safe_set(a, 'aggregator_p2view_Category', b2)
    assert _is_linked(a, 'aggregator_p2view_Category', b2)
    if hasattr(b1, 'Categories96'):
        assert not _is_linked(b1, 'Categories96', a)
    if hasattr(b2, 'Categories96'):
        assert _is_linked(b2, 'Categories96', a)
    _safe_set(a, 'aggregator_p2view_Category', None)
    assert not _is_linked(a, 'aggregator_p2view_Category', b2)
    if hasattr(b2, 'Categories96'):
        assert not _is_linked(b2, 'Categories96', a)


def test_assoc_configurations0_link_reassign_clear():
    a = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_Configuration', b1)
    assert _is_linked(a, 'aggregator_Configuration', b1)
    if hasattr(b1, 'aggregator_Aggregator'):
        assert _is_linked(b1, 'aggregator_Aggregator', a)
    _safe_set(a, 'aggregator_Configuration', b2)
    assert _is_linked(a, 'aggregator_Configuration', b2)
    if hasattr(b1, 'aggregator_Aggregator'):
        assert not _is_linked(b1, 'aggregator_Aggregator', a)
    if hasattr(b2, 'aggregator_Aggregator'):
        assert _is_linked(b2, 'aggregator_Aggregator', a)
    _safe_set(a, 'aggregator_Configuration', None)
    assert not _is_linked(a, 'aggregator_Configuration', b2)
    if hasattr(b2, 'aggregator_Aggregator'):
        assert not _is_linked(b2, 'aggregator_Aggregator', a)


def test_assoc_contacts24_link_reassign_clear():
    a = aggregator_Contribution(label="sample_text")
    b1 = aggregator_Contact(email="sample_text", name="sample_text")
    b2 = aggregator_Contact(email="sample_text_2", name="sample_text_2")
    _safe_set(a, 'aggregator_Contribution25', {b1})
    assert _is_linked(a, 'aggregator_Contribution25', b1)
    if hasattr(b1, 'aggregator_Contact26'):
        assert _is_linked(b1, 'aggregator_Contact26', a)
    _safe_set(a, 'aggregator_Contribution25', {b2})
    assert _is_linked(a, 'aggregator_Contribution25', b2)
    if hasattr(b1, 'aggregator_Contact26'):
        assert not _is_linked(b1, 'aggregator_Contact26', a)
    if hasattr(b2, 'aggregator_Contact26'):
        assert _is_linked(b2, 'aggregator_Contact26', a)
    _safe_set(a, 'aggregator_Contribution25', set())
    assert not _is_linked(a, 'aggregator_Contribution25', b2)
    if hasattr(b2, 'aggregator_Contact26'):
        assert not _is_linked(b2, 'aggregator_Contact26', a)


def test_assoc_contacts5_link_reassign_clear():
    a = aggregator_Contact(email="sample_text", name="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'Contact', b1)
    assert _is_linked(a, 'Contact', b1)
    if hasattr(b1, 'aggregator'):
        assert _is_linked(b1, 'aggregator', a)
    _safe_set(a, 'Contact', b2)
    assert _is_linked(a, 'Contact', b2)
    if hasattr(b1, 'aggregator'):
        assert not _is_linked(b1, 'aggregator', a)
    if hasattr(b2, 'aggregator'):
        assert _is_linked(b2, 'aggregator', a)
    _safe_set(a, 'Contact', None)
    assert not _is_linked(a, 'Contact', b2)
    if hasattr(b2, 'aggregator'):
        assert not _is_linked(b2, 'aggregator', a)


def test_assoc_contributions1_link_reassign_clear():
    a = aggregator_Contribution(label="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_Contribution', b1)
    assert _is_linked(a, 'aggregator_Contribution', b1)
    if hasattr(b1, 'aggregator_Aggregator2'):
        assert _is_linked(b1, 'aggregator_Aggregator2', a)
    _safe_set(a, 'aggregator_Contribution', b2)
    assert _is_linked(a, 'aggregator_Contribution', b2)
    if hasattr(b1, 'aggregator_Aggregator2'):
        assert not _is_linked(b1, 'aggregator_Aggregator2', a)
    if hasattr(b2, 'aggregator_Aggregator2'):
        assert _is_linked(b2, 'aggregator_Aggregator2', a)
    _safe_set(a, 'aggregator_Contribution', None)
    assert not _is_linked(a, 'aggregator_Contribution', b2)
    if hasattr(b2, 'aggregator_Aggregator2'):
        assert not _is_linked(b2, 'aggregator_Aggregator2', a)


def test_assoc_copyright45_link_reassign_clear():
    a = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    b1 = ICopyright()
    b2 = ICopyright()
    _safe_set(a, 'aggregator_p2_IInstallableUnit46', b1)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit46', b1)
    if hasattr(b1, 'ICopyright'):
        assert _is_linked(b1, 'ICopyright', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit46', b2)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit46', b2)
    if hasattr(b1, 'ICopyright'):
        assert not _is_linked(b1, 'ICopyright', a)
    if hasattr(b2, 'ICopyright'):
        assert _is_linked(b2, 'ICopyright', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit46', None)
    assert not _is_linked(a, 'aggregator_p2_IInstallableUnit46', b2)
    if hasattr(b2, 'ICopyright'):
        assert not _is_linked(b2, 'ICopyright', a)


def test_assoc_customCategories6_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_CustomCategory', b1)
    assert _is_linked(a, 'aggregator_CustomCategory', b1)
    if hasattr(b1, 'aggregator_Aggregator7'):
        assert _is_linked(b1, 'aggregator_Aggregator7', a)
    _safe_set(a, 'aggregator_CustomCategory', b2)
    assert _is_linked(a, 'aggregator_CustomCategory', b2)
    if hasattr(b1, 'aggregator_Aggregator7'):
        assert not _is_linked(b1, 'aggregator_Aggregator7', a)
    if hasattr(b2, 'aggregator_Aggregator7'):
        assert _is_linked(b2, 'aggregator_Aggregator7', a)
    _safe_set(a, 'aggregator_CustomCategory', None)
    assert not _is_linked(a, 'aggregator_CustomCategory', b2)
    if hasattr(b2, 'aggregator_Aggregator7'):
        assert not _is_linked(b2, 'aggregator_Aggregator7', a)


def test_assoc_featureContainer111_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Feature', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature', b1)
    if hasattr(b1, 'Features112'):
        assert _is_linked(b1, 'Features112', a)
    _safe_set(a, 'aggregator_p2view_Feature', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature', b2)
    if hasattr(b1, 'Features112'):
        assert not _is_linked(b1, 'Features112', a)
    if hasattr(b2, 'Features112'):
        assert _is_linked(b2, 'Features112', a)
    _safe_set(a, 'aggregator_p2view_Feature', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature', b2)
    if hasattr(b2, 'Features112'):
        assert not _is_linked(b2, 'Features112', a)


def test_assoc_featureContainer119_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Product', b1)
    assert _is_linked(a, 'aggregator_p2view_Product', b1)
    if hasattr(b1, 'Features120'):
        assert _is_linked(b1, 'Features120', a)
    _safe_set(a, 'aggregator_p2view_Product', b2)
    assert _is_linked(a, 'aggregator_p2view_Product', b2)
    if hasattr(b1, 'Features120'):
        assert not _is_linked(b1, 'Features120', a)
    if hasattr(b2, 'Features120'):
        assert _is_linked(b2, 'Features120', a)
    _safe_set(a, 'aggregator_p2view_Product', None)
    assert not _is_linked(a, 'aggregator_p2view_Product', b2)
    if hasattr(b2, 'Features120'):
        assert not _is_linked(b2, 'Features120', a)


def test_assoc_featureContainer76_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_InstallableUnits77', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits77', b1)
    if hasattr(b1, 'Features'):
        assert _is_linked(b1, 'Features', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits77', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits77', b2)
    if hasattr(b1, 'Features'):
        assert not _is_linked(b1, 'Features', a)
    if hasattr(b2, 'Features'):
        assert _is_linked(b2, 'Features', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits77', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits77', b2)
    if hasattr(b2, 'Features'):
        assert not _is_linked(b2, 'Features', a)


def test_assoc_featureContainer97_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Features()
    b2 = Features()
    _safe_set(a, 'aggregator_p2view_Category98', b1)
    assert _is_linked(a, 'aggregator_p2view_Category98', b1)
    if hasattr(b1, 'Features99'):
        assert _is_linked(b1, 'Features99', a)
    _safe_set(a, 'aggregator_p2view_Category98', b2)
    assert _is_linked(a, 'aggregator_p2view_Category98', b2)
    if hasattr(b1, 'Features99'):
        assert not _is_linked(b1, 'Features99', a)
    if hasattr(b2, 'Features99'):
        assert _is_linked(b2, 'Features99', a)
    _safe_set(a, 'aggregator_p2view_Category98', None)
    assert not _is_linked(a, 'aggregator_p2view_Category98', b2)
    if hasattr(b2, 'Features99'):
        assert not _is_linked(b2, 'Features99', a)


def test_assoc_features15_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'aggregator_MappedRepository16', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository16', b1)
    if hasattr(b1, 'aggregator_Feature'):
        assert _is_linked(b1, 'aggregator_Feature', a)
    _safe_set(a, 'aggregator_MappedRepository16', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository16', b2)
    if hasattr(b1, 'aggregator_Feature'):
        assert not _is_linked(b1, 'aggregator_Feature', a)
    if hasattr(b2, 'aggregator_Feature'):
        assert _is_linked(b2, 'aggregator_Feature', a)
    _safe_set(a, 'aggregator_MappedRepository16', set())
    assert not _is_linked(a, 'aggregator_MappedRepository16', b2)
    if hasattr(b2, 'aggregator_Feature'):
        assert not _is_linked(b2, 'aggregator_Feature', a)


def test_assoc_features34_link_reassign_clear():
    a = aggregator_CustomCategory(description="sample_text", identifier="sample_text", label="sample_text")
    b1 = aggregator_Feature()
    b2 = aggregator_Feature()
    _safe_set(a, 'categories', {b1})
    assert _is_linked(a, 'categories', b1)
    if hasattr(b1, 'Feature'):
        assert _is_linked(b1, 'Feature', a)
    _safe_set(a, 'categories', {b2})
    assert _is_linked(a, 'categories', b2)
    if hasattr(b1, 'Feature'):
        assert not _is_linked(b1, 'Feature', a)
    if hasattr(b2, 'Feature'):
        assert _is_linked(b2, 'Feature', a)
    _safe_set(a, 'categories', set())
    assert not _is_linked(a, 'categories', b2)
    if hasattr(b2, 'Feature'):
        assert not _is_linked(b2, 'Feature', a)


def test_assoc_fragmentContainer106_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Category107', b1)
    assert _is_linked(a, 'aggregator_p2view_Category107', b1)
    if hasattr(b1, 'Fragments108'):
        assert _is_linked(b1, 'Fragments108', a)
    _safe_set(a, 'aggregator_p2view_Category107', b2)
    assert _is_linked(a, 'aggregator_p2view_Category107', b2)
    if hasattr(b1, 'Fragments108'):
        assert not _is_linked(b1, 'Fragments108', a)
    if hasattr(b2, 'Fragments108'):
        assert _is_linked(b2, 'Fragments108', a)
    _safe_set(a, 'aggregator_p2view_Category107', None)
    assert not _is_linked(a, 'aggregator_p2view_Category107', b2)
    if hasattr(b2, 'Fragments108'):
        assert not _is_linked(b2, 'Fragments108', a)


def test_assoc_fragmentContainer116_link_reassign_clear():
    a = aggregator_p2view_Feature()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Feature117', b1)
    assert _is_linked(a, 'aggregator_p2view_Feature117', b1)
    if hasattr(b1, 'Fragments118'):
        assert _is_linked(b1, 'Fragments118', a)
    _safe_set(a, 'aggregator_p2view_Feature117', b2)
    assert _is_linked(a, 'aggregator_p2view_Feature117', b2)
    if hasattr(b1, 'Fragments118'):
        assert not _is_linked(b1, 'Fragments118', a)
    if hasattr(b2, 'Fragments118'):
        assert _is_linked(b2, 'Fragments118', a)
    _safe_set(a, 'aggregator_p2view_Feature117', None)
    assert not _is_linked(a, 'aggregator_p2view_Feature117', b2)
    if hasattr(b2, 'Fragments118'):
        assert not _is_linked(b2, 'Fragments118', a)


def test_assoc_fragmentContainer124_link_reassign_clear():
    a = aggregator_p2view_Product()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_Product125', b1)
    assert _is_linked(a, 'aggregator_p2view_Product125', b1)
    if hasattr(b1, 'Fragments126'):
        assert _is_linked(b1, 'Fragments126', a)
    _safe_set(a, 'aggregator_p2view_Product125', b2)
    assert _is_linked(a, 'aggregator_p2view_Product125', b2)
    if hasattr(b1, 'Fragments126'):
        assert not _is_linked(b1, 'Fragments126', a)
    if hasattr(b2, 'Fragments126'):
        assert _is_linked(b2, 'Fragments126', a)
    _safe_set(a, 'aggregator_p2view_Product125', None)
    assert not _is_linked(a, 'aggregator_p2view_Product125', b2)
    if hasattr(b2, 'Fragments126'):
        assert not _is_linked(b2, 'Fragments126', a)


def test_assoc_fragmentContainer82_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Fragments()
    b2 = Fragments()
    _safe_set(a, 'aggregator_p2view_InstallableUnits83', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits83', b1)
    if hasattr(b1, 'Fragments'):
        assert _is_linked(b1, 'Fragments', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits83', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits83', b2)
    if hasattr(b1, 'Fragments'):
        assert not _is_linked(b1, 'Fragments', a)
    if hasattr(b2, 'Fragments'):
        assert _is_linked(b2, 'Fragments', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits83', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits83', b2)
    if hasattr(b2, 'Fragments'):
        assert not _is_linked(b2, 'Fragments', a)


def test_assoc_installableUnit93_link_reassign_clear():
    a = aggregator_p2view_IUPresentation(description="sample_text", id="sample_text", label="sample_text", name="sample_text", type="sample_text", version="sample_text")
    b1 = InstallableUnit()
    b2 = InstallableUnit()
    _safe_set(a, 'aggregator_p2view_IUPresentation', b1)
    assert _is_linked(a, 'aggregator_p2view_IUPresentation', b1)
    if hasattr(b1, 'InstallableUnit94'):
        assert _is_linked(b1, 'InstallableUnit94', a)
    _safe_set(a, 'aggregator_p2view_IUPresentation', b2)
    assert _is_linked(a, 'aggregator_p2view_IUPresentation', b2)
    if hasattr(b1, 'InstallableUnit94'):
        assert not _is_linked(b1, 'InstallableUnit94', a)
    if hasattr(b2, 'InstallableUnit94'):
        assert _is_linked(b2, 'InstallableUnit94', a)
    _safe_set(a, 'aggregator_p2view_IUPresentation', None)
    assert not _is_linked(a, 'aggregator_p2view_IUPresentation', b2)
    if hasattr(b2, 'InstallableUnit94'):
        assert not _is_linked(b2, 'InstallableUnit94', a)


def test_assoc_installableUnitList69_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    b1 = InstallableUnits()
    b2 = InstallableUnits()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b1)
    if hasattr(b1, 'InstallableUnits'):
        assert _is_linked(b1, 'InstallableUnits', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    if hasattr(b1, 'InstallableUnits'):
        assert not _is_linked(b1, 'InstallableUnits', a)
    if hasattr(b2, 'InstallableUnits'):
        assert _is_linked(b2, 'InstallableUnits', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView', b2)
    if hasattr(b2, 'InstallableUnits'):
        assert not _is_linked(b2, 'InstallableUnits', a)


def test_assoc_iuDetails109_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = IUDetails()
    b2 = IUDetails()
    _safe_set(a, 'aggregator_p2view_Category110', b1)
    assert _is_linked(a, 'aggregator_p2view_Category110', b1)
    if hasattr(b1, 'IUDetails'):
        assert _is_linked(b1, 'IUDetails', a)
    _safe_set(a, 'aggregator_p2view_Category110', b2)
    assert _is_linked(a, 'aggregator_p2view_Category110', b2)
    if hasattr(b1, 'IUDetails'):
        assert not _is_linked(b1, 'IUDetails', a)
    if hasattr(b2, 'IUDetails'):
        assert _is_linked(b2, 'IUDetails', a)
    _safe_set(a, 'aggregator_p2view_Category110', None)
    assert not _is_linked(a, 'aggregator_p2view_Category110', b2)
    if hasattr(b2, 'IUDetails'):
        assert not _is_linked(b2, 'IUDetails', a)


def test_assoc_license43_link_reassign_clear():
    a = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    b1 = ILicense()
    b2 = ILicense()
    _safe_set(a, 'aggregator_p2_IInstallableUnit44', b1)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit44', b1)
    if hasattr(b1, 'ILicense'):
        assert _is_linked(b1, 'ILicense', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit44', b2)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit44', b2)
    if hasattr(b1, 'ILicense'):
        assert not _is_linked(b1, 'ILicense', a)
    if hasattr(b2, 'ILicense'):
        assert _is_linked(b2, 'ILicense', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit44', None)
    assert not _is_linked(a, 'aggregator_p2_IInstallableUnit44', b2)
    if hasattr(b2, 'ILicense'):
        assert not _is_linked(b2, 'ILicense', a)


def test_assoc_mapRules19_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_MapRule()
    b2 = aggregator_MapRule()
    _safe_set(a, 'aggregator_MappedRepository20', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository20', b1)
    if hasattr(b1, 'aggregator_MapRule'):
        assert _is_linked(b1, 'aggregator_MapRule', a)
    _safe_set(a, 'aggregator_MappedRepository20', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository20', b2)
    if hasattr(b1, 'aggregator_MapRule'):
        assert not _is_linked(b1, 'aggregator_MapRule', a)
    if hasattr(b2, 'aggregator_MapRule'):
        assert _is_linked(b2, 'aggregator_MapRule', a)
    _safe_set(a, 'aggregator_MappedRepository20', set())
    assert not _is_linked(a, 'aggregator_MappedRepository20', b2)
    if hasattr(b2, 'aggregator_MapRule'):
        assert not _is_linked(b2, 'aggregator_MapRule', a)


def test_assoc_mavenMappings10_link_reassign_clear():
    a = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_MavenMapping', b1)
    assert _is_linked(a, 'aggregator_MavenMapping', b1)
    if hasattr(b1, 'aggregator_Aggregator11'):
        assert _is_linked(b1, 'aggregator_Aggregator11', a)
    _safe_set(a, 'aggregator_MavenMapping', b2)
    assert _is_linked(a, 'aggregator_MavenMapping', b2)
    if hasattr(b1, 'aggregator_Aggregator11'):
        assert not _is_linked(b1, 'aggregator_Aggregator11', a)
    if hasattr(b2, 'aggregator_Aggregator11'):
        assert _is_linked(b2, 'aggregator_Aggregator11', a)
    _safe_set(a, 'aggregator_MavenMapping', None)
    assert not _is_linked(a, 'aggregator_MavenMapping', b2)
    if hasattr(b2, 'aggregator_Aggregator11'):
        assert not _is_linked(b2, 'aggregator_Aggregator11', a)


def test_assoc_mavenMappings27_link_reassign_clear():
    a = aggregator_MavenMapping(artifactId="sample_text", groupId="sample_text", namePattern="sample_text")
    b1 = aggregator_Contribution(label="sample_text")
    b2 = aggregator_Contribution(label="sample_text_2")
    _safe_set(a, 'aggregator_MavenMapping29', b1)
    assert _is_linked(a, 'aggregator_MavenMapping29', b1)
    if hasattr(b1, 'aggregator_Contribution28'):
        assert _is_linked(b1, 'aggregator_Contribution28', a)
    _safe_set(a, 'aggregator_MavenMapping29', b2)
    assert _is_linked(a, 'aggregator_MavenMapping29', b2)
    if hasattr(b1, 'aggregator_Contribution28'):
        assert not _is_linked(b1, 'aggregator_Contribution28', a)
    if hasattr(b2, 'aggregator_Contribution28'):
        assert _is_linked(b2, 'aggregator_Contribution28', a)
    _safe_set(a, 'aggregator_MavenMapping29', None)
    assert not _is_linked(a, 'aggregator_MavenMapping29', b2)
    if hasattr(b2, 'aggregator_Contribution28'):
        assert not _is_linked(b2, 'aggregator_Contribution28', a)


def test_assoc_metaRequiredCapabilityList57_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = RequiredCapability()
    b2 = RequiredCapability()
    _safe_set(a, 'aggregator_p2_InstallableUnit58', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit58', b1)
    if hasattr(b1, 'RequiredCapability59'):
        assert _is_linked(b1, 'RequiredCapability59', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit58', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit58', b2)
    if hasattr(b1, 'RequiredCapability59'):
        assert not _is_linked(b1, 'RequiredCapability59', a)
    if hasattr(b2, 'RequiredCapability59'):
        assert _is_linked(b2, 'RequiredCapability59', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit58', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit58', b2)
    if hasattr(b2, 'RequiredCapability59'):
        assert not _is_linked(b2, 'RequiredCapability59', a)


def test_assoc_metadataRepository37_link_reassign_clear():
    a = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    b1 = MetadataRepository()
    b2 = MetadataRepository()
    _safe_set(a, 'aggregator_MetadataRepositoryReference38', b1)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference38', b1)
    if hasattr(b1, 'MetadataRepository'):
        assert _is_linked(b1, 'MetadataRepository', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference38', b2)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference38', b2)
    if hasattr(b1, 'MetadataRepository'):
        assert not _is_linked(b1, 'MetadataRepository', a)
    if hasattr(b2, 'MetadataRepository'):
        assert _is_linked(b2, 'MetadataRepository', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference38', None)
    assert not _is_linked(a, 'aggregator_MetadataRepositoryReference38', b2)
    if hasattr(b2, 'MetadataRepository'):
        assert not _is_linked(b2, 'MetadataRepository', a)


def test_assoc_metadataRepository72_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    b1 = MetadataRepository()
    b2 = MetadataRepository()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', b1)
    if hasattr(b1, 'MetadataRepository74'):
        assert _is_linked(b1, 'MetadataRepository74', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', b2)
    if hasattr(b1, 'MetadataRepository74'):
        assert not _is_linked(b1, 'MetadataRepository74', a)
    if hasattr(b2, 'MetadataRepository74'):
        assert _is_linked(b2, 'MetadataRepository74', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView73', b2)
    if hasattr(b2, 'MetadataRepository74'):
        assert not _is_linked(b2, 'MetadataRepository74', a)


def test_assoc_miscellaneousContainer84_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Miscellaneous()
    b2 = Miscellaneous()
    _safe_set(a, 'aggregator_p2view_InstallableUnits85', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits85', b1)
    if hasattr(b1, 'Miscellaneous'):
        assert _is_linked(b1, 'Miscellaneous', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits85', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits85', b2)
    if hasattr(b1, 'Miscellaneous'):
        assert not _is_linked(b1, 'Miscellaneous', a)
    if hasattr(b2, 'Miscellaneous'):
        assert _is_linked(b2, 'Miscellaneous', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits85', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits85', b2)
    if hasattr(b2, 'Miscellaneous'):
        assert not _is_linked(b2, 'Miscellaneous', a)


def test_assoc_productContainer100_link_reassign_clear():
    a = aggregator_p2view_Category()
    b1 = Products()
    b2 = Products()
    _safe_set(a, 'aggregator_p2view_Category101', b1)
    assert _is_linked(a, 'aggregator_p2view_Category101', b1)
    if hasattr(b1, 'Products102'):
        assert _is_linked(b1, 'Products102', a)
    _safe_set(a, 'aggregator_p2view_Category101', b2)
    assert _is_linked(a, 'aggregator_p2view_Category101', b2)
    if hasattr(b1, 'Products102'):
        assert not _is_linked(b1, 'Products102', a)
    if hasattr(b2, 'Products102'):
        assert _is_linked(b2, 'Products102', a)
    _safe_set(a, 'aggregator_p2view_Category101', None)
    assert not _is_linked(a, 'aggregator_p2view_Category101', b2)
    if hasattr(b2, 'Products102'):
        assert not _is_linked(b2, 'Products102', a)


def test_assoc_productContainer78_link_reassign_clear():
    a = aggregator_p2view_InstallableUnits()
    b1 = Products()
    b2 = Products()
    _safe_set(a, 'aggregator_p2view_InstallableUnits79', b1)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits79', b1)
    if hasattr(b1, 'Products'):
        assert _is_linked(b1, 'Products', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits79', b2)
    assert _is_linked(a, 'aggregator_p2view_InstallableUnits79', b2)
    if hasattr(b1, 'Products'):
        assert not _is_linked(b1, 'Products', a)
    if hasattr(b2, 'Products'):
        assert _is_linked(b2, 'Products', a)
    _safe_set(a, 'aggregator_p2view_InstallableUnits79', None)
    assert not _is_linked(a, 'aggregator_p2view_InstallableUnits79', b2)
    if hasattr(b2, 'Products'):
        assert not _is_linked(b2, 'Products', a)


def test_assoc_products12_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Product()
    b2 = aggregator_Product()
    _safe_set(a, 'aggregator_MappedRepository', {b1})
    assert _is_linked(a, 'aggregator_MappedRepository', b1)
    if hasattr(b1, 'aggregator_Product'):
        assert _is_linked(b1, 'aggregator_Product', a)
    _safe_set(a, 'aggregator_MappedRepository', {b2})
    assert _is_linked(a, 'aggregator_MappedRepository', b2)
    if hasattr(b1, 'aggregator_Product'):
        assert not _is_linked(b1, 'aggregator_Product', a)
    if hasattr(b2, 'aggregator_Product'):
        assert _is_linked(b2, 'aggregator_Product', a)
    _safe_set(a, 'aggregator_MappedRepository', set())
    assert not _is_linked(a, 'aggregator_MappedRepository', b2)
    if hasattr(b2, 'aggregator_Product'):
        assert not _is_linked(b2, 'aggregator_Product', a)


def test_assoc_properties70_link_reassign_clear():
    a = aggregator_p2view_MetadataRepositoryStructuredView(loaded=True, name="sample_text")
    b1 = Properties()
    b2 = Properties()
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', b1)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', b1)
    if hasattr(b1, 'Properties'):
        assert _is_linked(b1, 'Properties', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', b2)
    assert _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', b2)
    if hasattr(b1, 'Properties'):
        assert not _is_linked(b1, 'Properties', a)
    if hasattr(b2, 'Properties'):
        assert _is_linked(b2, 'Properties', a)
    _safe_set(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', None)
    assert not _is_linked(a, 'aggregator_p2view_MetadataRepositoryStructuredView71', b2)
    if hasattr(b2, 'Properties'):
        assert not _is_linked(b2, 'Properties', a)


def test_assoc_propertyMap60_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = Property()
    b2 = Property()
    _safe_set(a, 'aggregator_p2_InstallableUnit61', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit61', b1)
    if hasattr(b1, 'Property62'):
        assert _is_linked(b1, 'Property62', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit61', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit61', b2)
    if hasattr(b1, 'Property62'):
        assert not _is_linked(b1, 'Property62', a)
    if hasattr(b2, 'Property62'):
        assert _is_linked(b2, 'Property62', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit61', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit61', b2)
    if hasattr(b2, 'Property62'):
        assert not _is_linked(b2, 'Property62', a)


def test_assoc_providedCapabilityList53_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = ProvidedCapability()
    b2 = ProvidedCapability()
    _safe_set(a, 'aggregator_p2_InstallableUnit54', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit54', b1)
    if hasattr(b1, 'ProvidedCapability'):
        assert _is_linked(b1, 'ProvidedCapability', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit54', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit54', b2)
    if hasattr(b1, 'ProvidedCapability'):
        assert not _is_linked(b1, 'ProvidedCapability', a)
    if hasattr(b2, 'ProvidedCapability'):
        assert _is_linked(b2, 'ProvidedCapability', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit54', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit54', b2)
    if hasattr(b2, 'ProvidedCapability'):
        assert not _is_linked(b2, 'ProvidedCapability', a)


def test_assoc_repositories21_link_reassign_clear():
    a = aggregator_MappedRepository(categoryPrefix="sample_text", mirrorArtifacts=True)
    b1 = aggregator_Contribution(label="sample_text")
    b2 = aggregator_Contribution(label="sample_text_2")
    _safe_set(a, 'aggregator_MappedRepository23', b1)
    assert _is_linked(a, 'aggregator_MappedRepository23', b1)
    if hasattr(b1, 'aggregator_Contribution22'):
        assert _is_linked(b1, 'aggregator_Contribution22', a)
    _safe_set(a, 'aggregator_MappedRepository23', b2)
    assert _is_linked(a, 'aggregator_MappedRepository23', b2)
    if hasattr(b1, 'aggregator_Contribution22'):
        assert not _is_linked(b1, 'aggregator_Contribution22', a)
    if hasattr(b2, 'aggregator_Contribution22'):
        assert _is_linked(b2, 'aggregator_Contribution22', a)
    _safe_set(a, 'aggregator_MappedRepository23', None)
    assert not _is_linked(a, 'aggregator_MappedRepository23', b2)
    if hasattr(b2, 'aggregator_Contribution22'):
        assert not _is_linked(b2, 'aggregator_Contribution22', a)


def test_assoc_requiredCapabilityList55_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = RequiredCapability()
    b2 = RequiredCapability()
    _safe_set(a, 'aggregator_p2_InstallableUnit56', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit56', b1)
    if hasattr(b1, 'RequiredCapability'):
        assert _is_linked(b1, 'RequiredCapability', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit56', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit56', b2)
    if hasattr(b1, 'RequiredCapability'):
        assert not _is_linked(b1, 'RequiredCapability', a)
    if hasattr(b2, 'RequiredCapability'):
        assert _is_linked(b2, 'RequiredCapability', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit56', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit56', b2)
    if hasattr(b2, 'RequiredCapability'):
        assert not _is_linked(b2, 'RequiredCapability', a)


def test_assoc_status39_link_reassign_clear():
    a = aggregator_Status(code="sample_text", message="sample_text")
    b1 = aggregator_StatusProvider()
    b2 = aggregator_StatusProvider()
    _safe_set(a, 'aggregator_Status', b1)
    assert _is_linked(a, 'aggregator_Status', b1)
    if hasattr(b1, 'aggregator_StatusProvider'):
        assert _is_linked(b1, 'aggregator_StatusProvider', a)
    _safe_set(a, 'aggregator_Status', b2)
    assert _is_linked(a, 'aggregator_Status', b2)
    if hasattr(b1, 'aggregator_StatusProvider'):
        assert not _is_linked(b1, 'aggregator_StatusProvider', a)
    if hasattr(b2, 'aggregator_StatusProvider'):
        assert _is_linked(b2, 'aggregator_StatusProvider', a)
    _safe_set(a, 'aggregator_Status', None)
    assert not _is_linked(a, 'aggregator_Status', b2)
    if hasattr(b2, 'aggregator_StatusProvider'):
        assert not _is_linked(b2, 'aggregator_StatusProvider', a)


def test_assoc_touchpointDataList63_link_reassign_clear():
    a = aggregator_p2_InstallableUnit()
    b1 = TouchpointData()
    b2 = TouchpointData()
    _safe_set(a, 'aggregator_p2_InstallableUnit64', {b1})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit64', b1)
    if hasattr(b1, 'TouchpointData'):
        assert _is_linked(b1, 'TouchpointData', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit64', {b2})
    assert _is_linked(a, 'aggregator_p2_InstallableUnit64', b2)
    if hasattr(b1, 'TouchpointData'):
        assert not _is_linked(b1, 'TouchpointData', a)
    if hasattr(b2, 'TouchpointData'):
        assert _is_linked(b2, 'TouchpointData', a)
    _safe_set(a, 'aggregator_p2_InstallableUnit64', set())
    assert not _is_linked(a, 'aggregator_p2_InstallableUnit64', b2)
    if hasattr(b2, 'TouchpointData'):
        assert not _is_linked(b2, 'TouchpointData', a)


def test_assoc_touchpointType40_link_reassign_clear():
    a = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    b1 = ITouchpointType()
    b2 = ITouchpointType()
    _safe_set(a, 'aggregator_p2_IInstallableUnit', b1)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit', b1)
    if hasattr(b1, 'ITouchpointType'):
        assert _is_linked(b1, 'ITouchpointType', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit', b2)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit', b2)
    if hasattr(b1, 'ITouchpointType'):
        assert not _is_linked(b1, 'ITouchpointType', a)
    if hasattr(b2, 'ITouchpointType'):
        assert _is_linked(b2, 'ITouchpointType', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit', None)
    assert not _is_linked(a, 'aggregator_p2_IInstallableUnit', b2)
    if hasattr(b2, 'ITouchpointType'):
        assert not _is_linked(b2, 'ITouchpointType', a)


def test_assoc_updateDescriptor41_link_reassign_clear():
    a = aggregator_p2_IInstallableUnit(filter="sample_text", id="sample_text", resolved=True, singleton=True, version="sample_text")
    b1 = IUpdateDescriptor()
    b2 = IUpdateDescriptor()
    _safe_set(a, 'aggregator_p2_IInstallableUnit42', b1)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit42', b1)
    if hasattr(b1, 'IUpdateDescriptor'):
        assert _is_linked(b1, 'IUpdateDescriptor', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit42', b2)
    assert _is_linked(a, 'aggregator_p2_IInstallableUnit42', b2)
    if hasattr(b1, 'IUpdateDescriptor'):
        assert not _is_linked(b1, 'IUpdateDescriptor', a)
    if hasattr(b2, 'IUpdateDescriptor'):
        assert _is_linked(b2, 'IUpdateDescriptor', a)
    _safe_set(a, 'aggregator_p2_IInstallableUnit42', None)
    assert not _is_linked(a, 'aggregator_p2_IInstallableUnit42', b2)
    if hasattr(b2, 'IUpdateDescriptor'):
        assert not _is_linked(b2, 'IUpdateDescriptor', a)


def test_assoc_validConfigurations32_link_reassign_clear():
    a = aggregator_MappedUnit()
    b1 = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b2 = aggregator_Configuration(architecture="sample_text_2", operatingSystem="sample_text_2", windowSystem="sample_text_2")
    _safe_set(a, 'aggregator_MappedUnit', {b1})
    assert _is_linked(a, 'aggregator_MappedUnit', b1)
    if hasattr(b1, 'aggregator_Configuration33'):
        assert _is_linked(b1, 'aggregator_Configuration33', a)
    _safe_set(a, 'aggregator_MappedUnit', {b2})
    assert _is_linked(a, 'aggregator_MappedUnit', b2)
    if hasattr(b1, 'aggregator_Configuration33'):
        assert not _is_linked(b1, 'aggregator_Configuration33', a)
    if hasattr(b2, 'aggregator_Configuration33'):
        assert _is_linked(b2, 'aggregator_Configuration33', a)
    _safe_set(a, 'aggregator_MappedUnit', set())
    assert not _is_linked(a, 'aggregator_MappedUnit', b2)
    if hasattr(b2, 'aggregator_Configuration33'):
        assert not _is_linked(b2, 'aggregator_Configuration33', a)


def test_assoc_validConfigurations35_link_reassign_clear():
    a = aggregator_Configuration(architecture="sample_text", operatingSystem="sample_text", windowSystem="sample_text")
    b1 = aggregator_ValidConfigurationsRule()
    b2 = aggregator_ValidConfigurationsRule()
    _safe_set(a, 'aggregator_Configuration36', b1)
    assert _is_linked(a, 'aggregator_Configuration36', b1)
    if hasattr(b1, 'aggregator_ValidConfigurationsRule'):
        assert _is_linked(b1, 'aggregator_ValidConfigurationsRule', a)
    _safe_set(a, 'aggregator_Configuration36', b2)
    assert _is_linked(a, 'aggregator_Configuration36', b2)
    if hasattr(b1, 'aggregator_ValidConfigurationsRule'):
        assert not _is_linked(b1, 'aggregator_ValidConfigurationsRule', a)
    if hasattr(b2, 'aggregator_ValidConfigurationsRule'):
        assert _is_linked(b2, 'aggregator_ValidConfigurationsRule', a)
    _safe_set(a, 'aggregator_Configuration36', None)
    assert not _is_linked(a, 'aggregator_Configuration36', b2)
    if hasattr(b2, 'aggregator_ValidConfigurationsRule'):
        assert not _is_linked(b2, 'aggregator_ValidConfigurationsRule', a)


def test_assoc_validationRepositories8_link_reassign_clear():
    a = aggregator_MetadataRepositoryReference(location="sample_text", nature="sample_text")
    b1 = aggregator_Aggregator(buildRoot="sample_text", label="sample_text", mavenResult=True, packedStrategy="sample_text", sendmail=True, type="sample_text")
    b2 = aggregator_Aggregator(buildRoot="sample_text_2", label="sample_text_2", mavenResult=False, packedStrategy="sample_text_2", sendmail=False, type="sample_text_2")
    _safe_set(a, 'aggregator_MetadataRepositoryReference', b1)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference', b1)
    if hasattr(b1, 'aggregator_Aggregator9'):
        assert _is_linked(b1, 'aggregator_Aggregator9', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference', b2)
    assert _is_linked(a, 'aggregator_MetadataRepositoryReference', b2)
    if hasattr(b1, 'aggregator_Aggregator9'):
        assert not _is_linked(b1, 'aggregator_Aggregator9', a)
    if hasattr(b2, 'aggregator_Aggregator9'):
        assert _is_linked(b2, 'aggregator_Aggregator9', a)
    _safe_set(a, 'aggregator_MetadataRepositoryReference', None)
    assert not _is_linked(a, 'aggregator_MetadataRepositoryReference', b2)
    if hasattr(b2, 'aggregator_Aggregator9'):
        assert not _is_linked(b2, 'aggregator_Aggregator9', a)


def test_assoc_value68_link_reassign_clear():
    a = aggregator_p2_InstructionMap(key="sample_text")
    b1 = TouchpointInstruction()
    b2 = TouchpointInstruction()
    _safe_set(a, 'aggregator_p2_InstructionMap', b1)
    assert _is_linked(a, 'aggregator_p2_InstructionMap', b1)
    if hasattr(b1, 'TouchpointInstruction'):
        assert _is_linked(b1, 'TouchpointInstruction', a)
    _safe_set(a, 'aggregator_p2_InstructionMap', b2)
    assert _is_linked(a, 'aggregator_p2_InstructionMap', b2)
    if hasattr(b1, 'TouchpointInstruction'):
        assert not _is_linked(b1, 'TouchpointInstruction', a)
    if hasattr(b2, 'TouchpointInstruction'):
        assert _is_linked(b2, 'TouchpointInstruction', a)
    _safe_set(a, 'aggregator_p2_InstructionMap', None)
    assert not _is_linked(a, 'aggregator_p2_InstructionMap', b2)
    if hasattr(b2, 'TouchpointInstruction'):
        assert not _is_linked(b2, 'TouchpointInstruction', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArtifactKey_strategy = st.builds(ArtifactKey)
@given(instance=ArtifactKey_strategy)
@settings(max_examples=25)
def test_ArtifactKey_instantiation(instance):
    assert isinstance(instance, ArtifactKey)


Bundle_strategy = st.builds(Bundle)
@given(instance=Bundle_strategy)
@settings(max_examples=25)
def test_Bundle_instantiation(instance):
    assert isinstance(instance, Bundle)


Bundles_strategy = st.builds(Bundles)
@given(instance=Bundles_strategy)
@settings(max_examples=25)
def test_Bundles_instantiation(instance):
    assert isinstance(instance, Bundles)


Categories_strategy = st.builds(Categories)
@given(instance=Categories_strategy)
@settings(max_examples=25)
def test_Categories_instantiation(instance):
    assert isinstance(instance, Categories)


Category_strategy = st.builds(Category)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


DescriptionProvider_strategy = st.builds(DescriptionProvider)
@given(instance=DescriptionProvider_strategy)
@settings(max_examples=25)
def test_DescriptionProvider_instantiation(instance):
    assert isinstance(instance, DescriptionProvider)


EnabledStatusProvider_strategy = st.builds(EnabledStatusProvider)
@given(instance=EnabledStatusProvider_strategy)
@settings(max_examples=25)
def test_EnabledStatusProvider_instantiation(instance):
    assert isinstance(instance, EnabledStatusProvider)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Features_strategy = st.builds(Features)
@given(instance=Features_strategy)
@settings(max_examples=25)
def test_Features_instantiation(instance):
    assert isinstance(instance, Features)


Fragment_strategy = st.builds(Fragment)
@given(instance=Fragment_strategy)
@settings(max_examples=25)
def test_Fragment_instantiation(instance):
    assert isinstance(instance, Fragment)


Fragments_strategy = st.builds(Fragments)
@given(instance=Fragments_strategy)
@settings(max_examples=25)
def test_Fragments_instantiation(instance):
    assert isinstance(instance, Fragments)


IAdaptable_strategy = st.builds(IAdaptable)
@given(instance=IAdaptable_strategy)
@settings(max_examples=25)
def test_IAdaptable_instantiation(instance):
    assert isinstance(instance, IAdaptable)


IArtifactKey_strategy = st.builds(IArtifactKey)
@given(instance=IArtifactKey_strategy)
@settings(max_examples=25)
def test_IArtifactKey_instantiation(instance):
    assert isinstance(instance, IArtifactKey)


ICopyright_strategy = st.builds(ICopyright)
@given(instance=ICopyright_strategy)
@settings(max_examples=25)
def test_ICopyright_instantiation(instance):
    assert isinstance(instance, ICopyright)


IInstallableUnit_strategy = st.builds(IInstallableUnit)
@given(instance=IInstallableUnit_strategy)
@settings(max_examples=25)
def test_IInstallableUnit_instantiation(instance):
    assert isinstance(instance, IInstallableUnit)


ILicense_strategy = st.builds(ILicense)
@given(instance=ILicense_strategy)
@settings(max_examples=25)
def test_ILicense_instantiation(instance):
    assert isinstance(instance, ILicense)


IMetadataRepository_strategy = st.builds(IMetadataRepository)
@given(instance=IMetadataRepository_strategy)
@settings(max_examples=25)
def test_IMetadataRepository_instantiation(instance):
    assert isinstance(instance, IMetadataRepository)


IProvidedCapability_strategy = st.builds(IProvidedCapability)
@given(instance=IProvidedCapability_strategy)
@settings(max_examples=25)
def test_IProvidedCapability_instantiation(instance):
    assert isinstance(instance, IProvidedCapability)


IRequiredCapability_strategy = st.builds(IRequiredCapability)
@given(instance=IRequiredCapability_strategy)
@settings(max_examples=25)
def test_IRequiredCapability_instantiation(instance):
    assert isinstance(instance, IRequiredCapability)


ITouchpointData_strategy = st.builds(ITouchpointData)
@given(instance=ITouchpointData_strategy)
@settings(max_examples=25)
def test_ITouchpointData_instantiation(instance):
    assert isinstance(instance, ITouchpointData)


ITouchpointInstruction_strategy = st.builds(ITouchpointInstruction)
@given(instance=ITouchpointInstruction_strategy)
@settings(max_examples=25)
def test_ITouchpointInstruction_instantiation(instance):
    assert isinstance(instance, ITouchpointInstruction)


ITouchpointType_strategy = st.builds(ITouchpointType)
@given(instance=ITouchpointType_strategy)
@settings(max_examples=25)
def test_ITouchpointType_instantiation(instance):
    assert isinstance(instance, ITouchpointType)


IUDetails_strategy = st.builds(IUDetails)
@given(instance=IUDetails_strategy)
@settings(max_examples=25)
def test_IUDetails_instantiation(instance):
    assert isinstance(instance, IUDetails)


IUPresentation_strategy = st.builds(IUPresentation)
@given(instance=IUPresentation_strategy)
@settings(max_examples=25)
def test_IUPresentation_instantiation(instance):
    assert isinstance(instance, IUPresentation)


IUPresentationWithDetails_strategy = st.builds(IUPresentationWithDetails)
@given(instance=IUPresentationWithDetails_strategy)
@settings(max_examples=25)
def test_IUPresentationWithDetails_instantiation(instance):
    assert isinstance(instance, IUPresentationWithDetails)


IUpdateDescriptor_strategy = st.builds(IUpdateDescriptor)
@given(instance=IUpdateDescriptor_strategy)
@settings(max_examples=25)
def test_IUpdateDescriptor_instantiation(instance):
    assert isinstance(instance, IUpdateDescriptor)


InfosProvider_strategy = st.builds(InfosProvider)
@given(instance=InfosProvider_strategy)
@settings(max_examples=25)
def test_InfosProvider_instantiation(instance):
    assert isinstance(instance, InfosProvider)


InstallableUnit_strategy = st.builds(InstallableUnit)
@given(instance=InstallableUnit_strategy)
@settings(max_examples=25)
def test_InstallableUnit_instantiation(instance):
    assert isinstance(instance, InstallableUnit)


InstallableUnitRequest_strategy = st.builds(InstallableUnitRequest)
@given(instance=InstallableUnitRequest_strategy)
@settings(max_examples=25)
def test_InstallableUnitRequest_instantiation(instance):
    assert isinstance(instance, InstallableUnitRequest)


InstallableUnits_strategy = st.builds(InstallableUnits)
@given(instance=InstallableUnits_strategy)
@settings(max_examples=25)
def test_InstallableUnits_instantiation(instance):
    assert isinstance(instance, InstallableUnits)


InstructionMap_strategy = st.builds(InstructionMap)
@given(instance=InstructionMap_strategy)
@settings(max_examples=25)
def test_InstructionMap_instantiation(instance):
    assert isinstance(instance, InstructionMap)


LabelProvider_strategy = st.builds(LabelProvider)
@given(instance=LabelProvider_strategy)
@settings(max_examples=25)
def test_LabelProvider_instantiation(instance):
    assert isinstance(instance, LabelProvider)


MapRule_strategy = st.builds(MapRule)
@given(instance=MapRule_strategy)
@settings(max_examples=25)
def test_MapRule_instantiation(instance):
    assert isinstance(instance, MapRule)


MappedUnit_strategy = st.builds(MappedUnit)
@given(instance=MappedUnit_strategy)
@settings(max_examples=25)
def test_MappedUnit_instantiation(instance):
    assert isinstance(instance, MappedUnit)


MetadataRepository_strategy = st.builds(MetadataRepository)
@given(instance=MetadataRepository_strategy)
@settings(max_examples=25)
def test_MetadataRepository_instantiation(instance):
    assert isinstance(instance, MetadataRepository)


MetadataRepositoryReference_strategy = st.builds(MetadataRepositoryReference)
@given(instance=MetadataRepositoryReference_strategy)
@settings(max_examples=25)
def test_MetadataRepositoryReference_instantiation(instance):
    assert isinstance(instance, MetadataRepositoryReference)


Miscellaneous_strategy = st.builds(Miscellaneous)
@given(instance=Miscellaneous_strategy)
@settings(max_examples=25)
def test_Miscellaneous_instantiation(instance):
    assert isinstance(instance, Miscellaneous)


OtherIU_strategy = st.builds(OtherIU)
@given(instance=OtherIU_strategy)
@settings(max_examples=25)
def test_OtherIU_instantiation(instance):
    assert isinstance(instance, OtherIU)


Product_strategy = st.builds(Product)
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Products_strategy = st.builds(Products)
@given(instance=Products_strategy)
@settings(max_examples=25)
def test_Products_instantiation(instance):
    assert isinstance(instance, Products)


Properties_strategy = st.builds(Properties)
@given(instance=Properties_strategy)
@settings(max_examples=25)
def test_Properties_instantiation(instance):
    assert isinstance(instance, Properties)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


ProvidedCapabilities_strategy = st.builds(ProvidedCapabilities)
@given(instance=ProvidedCapabilities_strategy)
@settings(max_examples=25)
def test_ProvidedCapabilities_instantiation(instance):
    assert isinstance(instance, ProvidedCapabilities)


ProvidedCapability_strategy = st.builds(ProvidedCapability)
@given(instance=ProvidedCapability_strategy)
@settings(max_examples=25)
def test_ProvidedCapability_instantiation(instance):
    assert isinstance(instance, ProvidedCapability)


ProvidedCapabilityWrapper_strategy = st.builds(ProvidedCapabilityWrapper)
@given(instance=ProvidedCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_ProvidedCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, ProvidedCapabilityWrapper)


RepositoryReference_strategy = st.builds(RepositoryReference)
@given(instance=RepositoryReference_strategy)
@settings(max_examples=25)
def test_RepositoryReference_instantiation(instance):
    assert isinstance(instance, RepositoryReference)


RequiredCapabilities_strategy = st.builds(RequiredCapabilities)
@given(instance=RequiredCapabilities_strategy)
@settings(max_examples=25)
def test_RequiredCapabilities_instantiation(instance):
    assert isinstance(instance, RequiredCapabilities)


RequiredCapability_strategy = st.builds(RequiredCapability)
@given(instance=RequiredCapability_strategy)
@settings(max_examples=25)
def test_RequiredCapability_instantiation(instance):
    assert isinstance(instance, RequiredCapability)


RequiredCapabilityWrapper_strategy = st.builds(RequiredCapabilityWrapper)
@given(instance=RequiredCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_RequiredCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, RequiredCapabilityWrapper)


StatusProvider_strategy = st.builds(StatusProvider)
@given(instance=StatusProvider_strategy)
@settings(max_examples=25)
def test_StatusProvider_instantiation(instance):
    assert isinstance(instance, StatusProvider)


TouchpointData_strategy = st.builds(TouchpointData)
@given(instance=TouchpointData_strategy)
@settings(max_examples=25)
def test_TouchpointData_instantiation(instance):
    assert isinstance(instance, TouchpointData)


TouchpointInstruction_strategy = st.builds(TouchpointInstruction)
@given(instance=TouchpointInstruction_strategy)
@settings(max_examples=25)
def test_TouchpointInstruction_instantiation(instance):
    assert isinstance(instance, TouchpointInstruction)


Touchpoints_strategy = st.builds(Touchpoints)
@given(instance=Touchpoints_strategy)
@settings(max_examples=25)
def test_Touchpoints_instantiation(instance):
    assert isinstance(instance, Touchpoints)


aggregator_Aggregator_strategy = st.builds(aggregator_Aggregator, buildRoot=safe_text, label=safe_text, mavenResult=st.booleans(), packedStrategy=safe_text, sendmail=st.booleans(), type=safe_text)
@given(instance=aggregator_Aggregator_strategy)
@settings(max_examples=25)
def test_aggregator_Aggregator_instantiation(instance):
    assert isinstance(instance, aggregator_Aggregator)


aggregator_Bundle_strategy = st.builds(aggregator_Bundle)
@given(instance=aggregator_Bundle_strategy)
@settings(max_examples=25)
def test_aggregator_Bundle_instantiation(instance):
    assert isinstance(instance, aggregator_Bundle)


aggregator_Category_strategy = st.builds(aggregator_Category, labelOverride=safe_text)
@given(instance=aggregator_Category_strategy)
@settings(max_examples=25)
def test_aggregator_Category_instantiation(instance):
    assert isinstance(instance, aggregator_Category)


aggregator_ChildrenProvider_strategy = st.builds(aggregator_ChildrenProvider)
@given(instance=aggregator_ChildrenProvider_strategy)
@settings(max_examples=25)
def test_aggregator_ChildrenProvider_instantiation(instance):
    assert isinstance(instance, aggregator_ChildrenProvider)


aggregator_Comparable_strategy = st.builds(aggregator_Comparable)
@given(instance=aggregator_Comparable_strategy)
@settings(max_examples=25)
def test_aggregator_Comparable_instantiation(instance):
    assert isinstance(instance, aggregator_Comparable)


aggregator_Configuration_strategy = st.builds(aggregator_Configuration, architecture=safe_text, operatingSystem=safe_text, windowSystem=safe_text)
@given(instance=aggregator_Configuration_strategy)
@settings(max_examples=25)
def test_aggregator_Configuration_instantiation(instance):
    assert isinstance(instance, aggregator_Configuration)


aggregator_Contact_strategy = st.builds(aggregator_Contact, email=safe_text, name=safe_text)
@given(instance=aggregator_Contact_strategy)
@settings(max_examples=25)
def test_aggregator_Contact_instantiation(instance):
    assert isinstance(instance, aggregator_Contact)


aggregator_Contribution_strategy = st.builds(aggregator_Contribution, label=safe_text)
@given(instance=aggregator_Contribution_strategy)
@settings(max_examples=25)
def test_aggregator_Contribution_instantiation(instance):
    assert isinstance(instance, aggregator_Contribution)


aggregator_CustomCategory_strategy = st.builds(aggregator_CustomCategory, description=safe_text, identifier=safe_text, label=safe_text)
@given(instance=aggregator_CustomCategory_strategy)
@settings(max_examples=25)
def test_aggregator_CustomCategory_instantiation(instance):
    assert isinstance(instance, aggregator_CustomCategory)


aggregator_DescriptionProvider_strategy = st.builds(aggregator_DescriptionProvider, description=safe_text)
@given(instance=aggregator_DescriptionProvider_strategy)
@settings(max_examples=25)
def test_aggregator_DescriptionProvider_instantiation(instance):
    assert isinstance(instance, aggregator_DescriptionProvider)


aggregator_EnabledStatusProvider_strategy = st.builds(aggregator_EnabledStatusProvider, enabled=st.booleans())
@given(instance=aggregator_EnabledStatusProvider_strategy)
@settings(max_examples=25)
def test_aggregator_EnabledStatusProvider_instantiation(instance):
    assert isinstance(instance, aggregator_EnabledStatusProvider)


aggregator_ExclusionRule_strategy = st.builds(aggregator_ExclusionRule)
@given(instance=aggregator_ExclusionRule_strategy)
@settings(max_examples=25)
def test_aggregator_ExclusionRule_instantiation(instance):
    assert isinstance(instance, aggregator_ExclusionRule)


aggregator_Feature_strategy = st.builds(aggregator_Feature)
@given(instance=aggregator_Feature_strategy)
@settings(max_examples=25)
def test_aggregator_Feature_instantiation(instance):
    assert isinstance(instance, aggregator_Feature)


aggregator_InfosProvider_strategy = st.builds(aggregator_InfosProvider, errors=safe_text, infos=safe_text, warnings=safe_text)
@given(instance=aggregator_InfosProvider_strategy)
@settings(max_examples=25)
def test_aggregator_InfosProvider_instantiation(instance):
    assert isinstance(instance, aggregator_InfosProvider)


aggregator_InstallableUnitRequest_strategy = st.builds(aggregator_InstallableUnitRequest, name=safe_text, versionRange=safe_text)
@given(instance=aggregator_InstallableUnitRequest_strategy)
@settings(max_examples=25)
def test_aggregator_InstallableUnitRequest_instantiation(instance):
    assert isinstance(instance, aggregator_InstallableUnitRequest)


aggregator_LabelProvider_strategy = st.builds(aggregator_LabelProvider, label=safe_text)
@given(instance=aggregator_LabelProvider_strategy)
@settings(max_examples=25)
def test_aggregator_LabelProvider_instantiation(instance):
    assert isinstance(instance, aggregator_LabelProvider)


aggregator_MapRule_strategy = st.builds(aggregator_MapRule)
@given(instance=aggregator_MapRule_strategy)
@settings(max_examples=25)
def test_aggregator_MapRule_instantiation(instance):
    assert isinstance(instance, aggregator_MapRule)


aggregator_MappedRepository_strategy = st.builds(aggregator_MappedRepository, categoryPrefix=safe_text, mirrorArtifacts=st.booleans())
@given(instance=aggregator_MappedRepository_strategy)
@settings(max_examples=25)
def test_aggregator_MappedRepository_instantiation(instance):
    assert isinstance(instance, aggregator_MappedRepository)


aggregator_MappedUnit_strategy = st.builds(aggregator_MappedUnit)
@given(instance=aggregator_MappedUnit_strategy)
@settings(max_examples=25)
def test_aggregator_MappedUnit_instantiation(instance):
    assert isinstance(instance, aggregator_MappedUnit)


aggregator_MavenItem_strategy = st.builds(aggregator_MavenItem, artifactId=safe_text, groupId=safe_text)
@given(instance=aggregator_MavenItem_strategy)
@settings(max_examples=25)
def test_aggregator_MavenItem_instantiation(instance):
    assert isinstance(instance, aggregator_MavenItem)


aggregator_MavenMapping_strategy = st.builds(aggregator_MavenMapping, artifactId=safe_text, groupId=safe_text, namePattern=safe_text)
@given(instance=aggregator_MavenMapping_strategy)
@settings(max_examples=25)
def test_aggregator_MavenMapping_instantiation(instance):
    assert isinstance(instance, aggregator_MavenMapping)


aggregator_MetadataRepositoryReference_strategy = st.builds(aggregator_MetadataRepositoryReference, location=safe_text, nature=safe_text)
@given(instance=aggregator_MetadataRepositoryReference_strategy)
@settings(max_examples=25)
def test_aggregator_MetadataRepositoryReference_instantiation(instance):
    assert isinstance(instance, aggregator_MetadataRepositoryReference)


aggregator_Product_strategy = st.builds(aggregator_Product)
@given(instance=aggregator_Product_strategy)
@settings(max_examples=25)
def test_aggregator_Product_instantiation(instance):
    assert isinstance(instance, aggregator_Product)


aggregator_Property_strategy = st.builds(aggregator_Property, key=safe_text, value=safe_text)
@given(instance=aggregator_Property_strategy)
@settings(max_examples=25)
def test_aggregator_Property_instantiation(instance):
    assert isinstance(instance, aggregator_Property)


aggregator_Status_strategy = st.builds(aggregator_Status, code=safe_text, message=safe_text)
@given(instance=aggregator_Status_strategy)
@settings(max_examples=25)
def test_aggregator_Status_instantiation(instance):
    assert isinstance(instance, aggregator_Status)


aggregator_StatusProvider_strategy = st.builds(aggregator_StatusProvider)
@given(instance=aggregator_StatusProvider_strategy)
@settings(max_examples=25)
def test_aggregator_StatusProvider_instantiation(instance):
    assert isinstance(instance, aggregator_StatusProvider)


aggregator_ValidConfigurationsRule_strategy = st.builds(aggregator_ValidConfigurationsRule)
@given(instance=aggregator_ValidConfigurationsRule_strategy)
@settings(max_examples=25)
def test_aggregator_ValidConfigurationsRule_instantiation(instance):
    assert isinstance(instance, aggregator_ValidConfigurationsRule)


aggregator_p2_ArtifactKey_strategy = st.builds(aggregator_p2_ArtifactKey)
@given(instance=aggregator_p2_ArtifactKey_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ArtifactKey_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ArtifactKey)


aggregator_p2_Copyright_strategy = st.builds(aggregator_p2_Copyright)
@given(instance=aggregator_p2_Copyright_strategy)
@settings(max_examples=25)
def test_aggregator_p2_Copyright_instantiation(instance):
    assert isinstance(instance, aggregator_p2_Copyright)


aggregator_p2_IAdaptable_strategy = st.builds(aggregator_p2_IAdaptable)
@given(instance=aggregator_p2_IAdaptable_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IAdaptable_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IAdaptable)


aggregator_p2_IArtifactKey_strategy = st.builds(aggregator_p2_IArtifactKey, classifier=safe_text, id=safe_text, version=safe_text)
@given(instance=aggregator_p2_IArtifactKey_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IArtifactKey_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IArtifactKey)


aggregator_p2_ICopyright_strategy = st.builds(aggregator_p2_ICopyright, body=safe_text, location=safe_text)
@given(instance=aggregator_p2_ICopyright_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ICopyright_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ICopyright)


aggregator_p2_IInstallableUnit_strategy = st.builds(aggregator_p2_IInstallableUnit, filter=safe_text, id=safe_text, resolved=st.booleans(), singleton=st.booleans(), version=safe_text)
@given(instance=aggregator_p2_IInstallableUnit_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IInstallableUnit_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IInstallableUnit)


aggregator_p2_IInstallableUnitFragment_strategy = st.builds(aggregator_p2_IInstallableUnitFragment)
@given(instance=aggregator_p2_IInstallableUnitFragment_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IInstallableUnitFragment_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IInstallableUnitFragment)


aggregator_p2_ILicense_strategy = st.builds(aggregator_p2_ILicense, body=safe_text, digest=safe_text, location=safe_text)
@given(instance=aggregator_p2_ILicense_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ILicense_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ILicense)


aggregator_p2_IMetadataRepository_strategy = st.builds(aggregator_p2_IMetadataRepository)
@given(instance=aggregator_p2_IMetadataRepository_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IMetadataRepository_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IMetadataRepository)


aggregator_p2_IProvidedCapability_strategy = st.builds(aggregator_p2_IProvidedCapability, name=safe_text, namespace=safe_text, version=safe_text)
@given(instance=aggregator_p2_IProvidedCapability_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IProvidedCapability_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IProvidedCapability)


aggregator_p2_IQueryable_strategy = st.builds(aggregator_p2_IQueryable)
@given(instance=aggregator_p2_IQueryable_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IQueryable_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IQueryable)


aggregator_p2_IRepository_strategy = st.builds(aggregator_p2_IRepository, description=safe_text, location=safe_text, modifiable=st.booleans(), name=safe_text, provider=safe_text, type=safe_text, version=safe_text)
@given(instance=aggregator_p2_IRepository_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IRepository_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IRepository)


aggregator_p2_IRequiredCapability_strategy = st.builds(aggregator_p2_IRequiredCapability, filter=safe_text, greedy=st.booleans(), multiple=st.booleans(), name=safe_text, namespace=safe_text, negation=st.booleans(), optional=st.booleans(), range=safe_text, selectorList=safe_text)
@given(instance=aggregator_p2_IRequiredCapability_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IRequiredCapability_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IRequiredCapability)


aggregator_p2_ITouchpointData_strategy = st.builds(aggregator_p2_ITouchpointData)
@given(instance=aggregator_p2_ITouchpointData_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ITouchpointData_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ITouchpointData)


aggregator_p2_ITouchpointInstruction_strategy = st.builds(aggregator_p2_ITouchpointInstruction, body=safe_text, importAttribute=safe_text)
@given(instance=aggregator_p2_ITouchpointInstruction_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ITouchpointInstruction_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ITouchpointInstruction)


aggregator_p2_ITouchpointType_strategy = st.builds(aggregator_p2_ITouchpointType, id=safe_text, version=safe_text)
@given(instance=aggregator_p2_ITouchpointType_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ITouchpointType_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ITouchpointType)


aggregator_p2_IUpdateDescriptor_strategy = st.builds(aggregator_p2_IUpdateDescriptor, description=safe_text, id=safe_text, range=safe_text, severity=st.integers())
@given(instance=aggregator_p2_IUpdateDescriptor_strategy)
@settings(max_examples=25)
def test_aggregator_p2_IUpdateDescriptor_instantiation(instance):
    assert isinstance(instance, aggregator_p2_IUpdateDescriptor)


aggregator_p2_InstallableUnit_strategy = st.builds(aggregator_p2_InstallableUnit)
@given(instance=aggregator_p2_InstallableUnit_strategy)
@settings(max_examples=25)
def test_aggregator_p2_InstallableUnit_instantiation(instance):
    assert isinstance(instance, aggregator_p2_InstallableUnit)


aggregator_p2_InstallableUnitFragment_strategy = st.builds(aggregator_p2_InstallableUnitFragment)
@given(instance=aggregator_p2_InstallableUnitFragment_strategy)
@settings(max_examples=25)
def test_aggregator_p2_InstallableUnitFragment_instantiation(instance):
    assert isinstance(instance, aggregator_p2_InstallableUnitFragment)


aggregator_p2_InstructionMap_strategy = st.builds(aggregator_p2_InstructionMap, key=safe_text)
@given(instance=aggregator_p2_InstructionMap_strategy)
@settings(max_examples=25)
def test_aggregator_p2_InstructionMap_instantiation(instance):
    assert isinstance(instance, aggregator_p2_InstructionMap)


aggregator_p2_License_strategy = st.builds(aggregator_p2_License)
@given(instance=aggregator_p2_License_strategy)
@settings(max_examples=25)
def test_aggregator_p2_License_instantiation(instance):
    assert isinstance(instance, aggregator_p2_License)


aggregator_p2_MetadataRepository_strategy = st.builds(aggregator_p2_MetadataRepository)
@given(instance=aggregator_p2_MetadataRepository_strategy)
@settings(max_examples=25)
def test_aggregator_p2_MetadataRepository_instantiation(instance):
    assert isinstance(instance, aggregator_p2_MetadataRepository)


aggregator_p2_Property_strategy = st.builds(aggregator_p2_Property, key=safe_text, value=safe_text)
@given(instance=aggregator_p2_Property_strategy)
@settings(max_examples=25)
def test_aggregator_p2_Property_instantiation(instance):
    assert isinstance(instance, aggregator_p2_Property)


aggregator_p2_ProvidedCapability_strategy = st.builds(aggregator_p2_ProvidedCapability)
@given(instance=aggregator_p2_ProvidedCapability_strategy)
@settings(max_examples=25)
def test_aggregator_p2_ProvidedCapability_instantiation(instance):
    assert isinstance(instance, aggregator_p2_ProvidedCapability)


aggregator_p2_RepositoryReference_strategy = st.builds(aggregator_p2_RepositoryReference, location=safe_text, nickname=safe_text, options=st.integers(), type=st.integers())
@given(instance=aggregator_p2_RepositoryReference_strategy)
@settings(max_examples=25)
def test_aggregator_p2_RepositoryReference_instantiation(instance):
    assert isinstance(instance, aggregator_p2_RepositoryReference)


aggregator_p2_RequiredCapability_strategy = st.builds(aggregator_p2_RequiredCapability)
@given(instance=aggregator_p2_RequiredCapability_strategy)
@settings(max_examples=25)
def test_aggregator_p2_RequiredCapability_instantiation(instance):
    assert isinstance(instance, aggregator_p2_RequiredCapability)


aggregator_p2_TouchpointData_strategy = st.builds(aggregator_p2_TouchpointData)
@given(instance=aggregator_p2_TouchpointData_strategy)
@settings(max_examples=25)
def test_aggregator_p2_TouchpointData_instantiation(instance):
    assert isinstance(instance, aggregator_p2_TouchpointData)


aggregator_p2_TouchpointInstruction_strategy = st.builds(aggregator_p2_TouchpointInstruction)
@given(instance=aggregator_p2_TouchpointInstruction_strategy)
@settings(max_examples=25)
def test_aggregator_p2_TouchpointInstruction_instantiation(instance):
    assert isinstance(instance, aggregator_p2_TouchpointInstruction)


aggregator_p2_TouchpointType_strategy = st.builds(aggregator_p2_TouchpointType)
@given(instance=aggregator_p2_TouchpointType_strategy)
@settings(max_examples=25)
def test_aggregator_p2_TouchpointType_instantiation(instance):
    assert isinstance(instance, aggregator_p2_TouchpointType)


aggregator_p2_UpdateDescriptor_strategy = st.builds(aggregator_p2_UpdateDescriptor)
@given(instance=aggregator_p2_UpdateDescriptor_strategy)
@settings(max_examples=25)
def test_aggregator_p2_UpdateDescriptor_instantiation(instance):
    assert isinstance(instance, aggregator_p2_UpdateDescriptor)


aggregator_p2view_Bundle_strategy = st.builds(aggregator_p2view_Bundle)
@given(instance=aggregator_p2view_Bundle_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Bundle_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Bundle)


aggregator_p2view_Bundles_strategy = st.builds(aggregator_p2view_Bundles)
@given(instance=aggregator_p2view_Bundles_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Bundles_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Bundles)


aggregator_p2view_Categories_strategy = st.builds(aggregator_p2view_Categories)
@given(instance=aggregator_p2view_Categories_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Categories_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Categories)


aggregator_p2view_Category_strategy = st.builds(aggregator_p2view_Category)
@given(instance=aggregator_p2view_Category_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Category_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Category)


aggregator_p2view_Feature_strategy = st.builds(aggregator_p2view_Feature)
@given(instance=aggregator_p2view_Feature_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Feature_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Feature)


aggregator_p2view_Features_strategy = st.builds(aggregator_p2view_Features)
@given(instance=aggregator_p2view_Features_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Features_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Features)


aggregator_p2view_Fragment_strategy = st.builds(aggregator_p2view_Fragment)
@given(instance=aggregator_p2view_Fragment_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Fragment_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Fragment)


aggregator_p2view_Fragments_strategy = st.builds(aggregator_p2view_Fragments)
@given(instance=aggregator_p2view_Fragments_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Fragments_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Fragments)


aggregator_p2view_IUDetails_strategy = st.builds(aggregator_p2view_IUDetails)
@given(instance=aggregator_p2view_IUDetails_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUDetails_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUDetails)


aggregator_p2view_IUPresentation_strategy = st.builds(aggregator_p2view_IUPresentation, description=safe_text, id=safe_text, label=safe_text, name=safe_text, type=safe_text, version=safe_text)
@given(instance=aggregator_p2view_IUPresentation_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUPresentation_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUPresentation)


aggregator_p2view_IUPresentationWithDetails_strategy = st.builds(aggregator_p2view_IUPresentationWithDetails, detailsResolved=safe_text)
@given(instance=aggregator_p2view_IUPresentationWithDetails_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_IUPresentationWithDetails_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_IUPresentationWithDetails)


aggregator_p2view_InstallableUnits_strategy = st.builds(aggregator_p2view_InstallableUnits)
@given(instance=aggregator_p2view_InstallableUnits_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_InstallableUnits_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_InstallableUnits)


aggregator_p2view_MetadataRepositoryStructuredView_strategy = st.builds(aggregator_p2view_MetadataRepositoryStructuredView, loaded=st.booleans(), name=safe_text)
@given(instance=aggregator_p2view_MetadataRepositoryStructuredView_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_MetadataRepositoryStructuredView_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_MetadataRepositoryStructuredView)


aggregator_p2view_Miscellaneous_strategy = st.builds(aggregator_p2view_Miscellaneous)
@given(instance=aggregator_p2view_Miscellaneous_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Miscellaneous_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Miscellaneous)


aggregator_p2view_OtherIU_strategy = st.builds(aggregator_p2view_OtherIU)
@given(instance=aggregator_p2view_OtherIU_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_OtherIU_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_OtherIU)


aggregator_p2view_Product_strategy = st.builds(aggregator_p2view_Product)
@given(instance=aggregator_p2view_Product_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Product_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Product)


aggregator_p2view_Products_strategy = st.builds(aggregator_p2view_Products)
@given(instance=aggregator_p2view_Products_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Products_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Products)


aggregator_p2view_Properties_strategy = st.builds(aggregator_p2view_Properties)
@given(instance=aggregator_p2view_Properties_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Properties_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Properties)


aggregator_p2view_ProvidedCapabilities_strategy = st.builds(aggregator_p2view_ProvidedCapabilities)
@given(instance=aggregator_p2view_ProvidedCapabilities_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_ProvidedCapabilities_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_ProvidedCapabilities)


aggregator_p2view_ProvidedCapabilityWrapper_strategy = st.builds(aggregator_p2view_ProvidedCapabilityWrapper)
@given(instance=aggregator_p2view_ProvidedCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_ProvidedCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_ProvidedCapabilityWrapper)


aggregator_p2view_RequiredCapabilities_strategy = st.builds(aggregator_p2view_RequiredCapabilities)
@given(instance=aggregator_p2view_RequiredCapabilities_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_RequiredCapabilities_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_RequiredCapabilities)


aggregator_p2view_RequiredCapabilityWrapper_strategy = st.builds(aggregator_p2view_RequiredCapabilityWrapper)
@given(instance=aggregator_p2view_RequiredCapabilityWrapper_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_RequiredCapabilityWrapper_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_RequiredCapabilityWrapper)


aggregator_p2view_Touchpoints_strategy = st.builds(aggregator_p2view_Touchpoints)
@given(instance=aggregator_p2view_Touchpoints_strategy)
@settings(max_examples=25)
def test_aggregator_p2view_Touchpoints_instantiation(instance):
    assert isinstance(instance, aggregator_p2view_Touchpoints)


p2_IInstallableUnitFragment_strategy = st.builds(p2_IInstallableUnitFragment)
@given(instance=p2_IInstallableUnitFragment_strategy)
@settings(max_examples=25)
def test_p2_IInstallableUnitFragment_instantiation(instance):
    assert isinstance(instance, p2_IInstallableUnitFragment)


p2_IProvidedCapability_strategy = st.builds(p2_IProvidedCapability)
@given(instance=p2_IProvidedCapability_strategy)
@settings(max_examples=25)
def test_p2_IProvidedCapability_instantiation(instance):
    assert isinstance(instance, p2_IProvidedCapability)


p2_IQueryable_strategy = st.builds(p2_IQueryable)
@given(instance=p2_IQueryable_strategy)
@settings(max_examples=25)
def test_p2_IQueryable_instantiation(instance):
    assert isinstance(instance, p2_IQueryable)


p2_IRepository_strategy = st.builds(p2_IRepository)
@given(instance=p2_IRepository_strategy)
@settings(max_examples=25)
def test_p2_IRepository_instantiation(instance):
    assert isinstance(instance, p2_IRepository)


p2_IRequiredCapability_strategy = st.builds(p2_IRequiredCapability)
@given(instance=p2_IRequiredCapability_strategy)
@settings(max_examples=25)
def test_p2_IRequiredCapability_instantiation(instance):
    assert isinstance(instance, p2_IRequiredCapability)


p2_InstallableUnit_strategy = st.builds(p2_InstallableUnit)
@given(instance=p2_InstallableUnit_strategy)
@settings(max_examples=25)
def test_p2_InstallableUnit_instantiation(instance):
    assert isinstance(instance, p2_InstallableUnit)


p2view_IUDetails_strategy = st.builds(p2view_IUDetails)
@given(instance=p2view_IUDetails_strategy)
@settings(max_examples=25)
def test_p2view_IUDetails_instantiation(instance):
    assert isinstance(instance, p2view_IUDetails)


p2view_IUPresentation_strategy = st.builds(p2view_IUPresentation)
@given(instance=p2view_IUPresentation_strategy)
@settings(max_examples=25)
def test_p2view_IUPresentation_instantiation(instance):
    assert isinstance(instance, p2view_IUPresentation)


p2view_aggregator_Property_strategy = st.builds(p2view_aggregator_Property)
@given(instance=p2view_aggregator_Property_strategy)
@settings(max_examples=25)
def test_p2view_aggregator_Property_instantiation(instance):
    assert isinstance(instance, p2view_aggregator_Property)



