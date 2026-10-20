from python_code import aggregator_DescriptionProvider

def test_aggregator_DescriptionProvider___init__():
    assert aggregator_DescriptionProvider.__init__(aggregator_DescriptionProvider(''), '') == None


from python_code import aggregator_EnabledStatusProvider

def test_aggregator_EnabledStatusProvider___init__():
    assert aggregator_EnabledStatusProvider.__init__(aggregator_EnabledStatusProvider(False, False), False, False) == None


from python_code import aggregator_IdentificationProvider

def test_aggregator_IdentificationProvider___init__():
    assert aggregator_IdentificationProvider.__init__(aggregator_IdentificationProvider()) == None

def test_aggregator_IdentificationProvider_getIdentification():
    assert aggregator_IdentificationProvider.getIdentification(aggregator_IdentificationProvider()) == None


from python_code import aggregator_InfosProvider

def test_aggregator_InfosProvider___init__():
    assert aggregator_InfosProvider.__init__(aggregator_InfosProvider('', '', '\x00\x00'), '', '', '') == None


from python_code import aggregator_AvailableVersionsHeader
from python_code import aggregator_InstallableUnitRequest

def test_aggregator_InstallableUnitRequest___init__():
    assert aggregator_InstallableUnitRequest.__init__(aggregator_InstallableUnitRequest('\x00\x00', '', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set()), '', '', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set()) == None

def test_aggregator_InstallableUnitRequest_resolveAvailableVersions():
    assert aggregator_InstallableUnitRequest.resolveAvailableVersions(aggregator_InstallableUnitRequest('', '\x00', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set()), '') == None

def test_aggregator_InstallableUnitRequest_isMappedRepositoryBroken():
    assert aggregator_InstallableUnitRequest.isMappedRepositoryBroken(aggregator_InstallableUnitRequest('', '\x00', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set())) == None

def test_aggregator_InstallableUnitRequest_resolveAsSingleton():
    assert aggregator_InstallableUnitRequest.resolveAsSingleton(aggregator_InstallableUnitRequest('', '\x00', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set()), '') == None

def test_aggregator_InstallableUnitRequest_isBranchEnabled():
    assert aggregator_InstallableUnitRequest.isBranchEnabled(aggregator_InstallableUnitRequest('', '\x00', InstallableUnitRequest=aggregator_AvailableVersionsHeader(), installableUnitRequest=aggregator_AvailableVersionsHeader(), aggregator_InstallableUnitRequest=set())) == None


from python_code import aggregator_LabelProvider

def test_aggregator_LabelProvider___init__():
    assert aggregator_LabelProvider.__init__(aggregator_LabelProvider(''), '') == None


from python_code import aggregator_Property

def test_aggregator_Property___init__():
    assert aggregator_Property.__init__(aggregator_Property('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_Status
from python_code import aggregator_StatusProvider

def test_aggregator_Status___init__():
    assert aggregator_Status.__init__(aggregator_Status('', '\x00', aggregator_Status=aggregator_StatusProvider()), '\x00\x00', '', aggregator_Status=aggregator_StatusProvider()) == None


from python_code import Bundles
from python_code import Features
from python_code import Fragments
from python_code import aggregator_p2view_Feature

def test_aggregator_p2view_Feature___init__():
    assert aggregator_p2view_Feature.__init__(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature71=Bundles(), aggregator_p2view_Feature74=Fragments()), aggregator_p2view_Feature=Features(), aggregator_p2view_Feature71=Bundles(), aggregator_p2view_Feature74=Fragments()) == None

def test_aggregator_p2view_Feature_getNotNullBundleContainer():
    assert aggregator_p2view_Feature.getNotNullBundleContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature71=Bundles(), aggregator_p2view_Feature74=Fragments())) == None

def test_aggregator_p2view_Feature_getNotNullFeatureContainer():
    assert aggregator_p2view_Feature.getNotNullFeatureContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature71=Bundles(), aggregator_p2view_Feature74=Fragments())) == None

def test_aggregator_p2view_Feature_getNotNullFragmentContainer():
    assert aggregator_p2view_Feature.getNotNullFragmentContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature71=Bundles(), aggregator_p2view_Feature74=Fragments())) == None


from python_code import aggregator_p2view_IUPresentation
from python_code import p2view_aggregator_IInstallableUnit

def test_aggregator_p2view_IUPresentation___init__():
    assert aggregator_p2view_IUPresentation.__init__(aggregator_p2view_IUPresentation('', '', '', '', '', '', '', aggregator_p2view_IUPresentation=p2view_aggregator_IInstallableUnit()), '', '\x00', '', '', '', '', '', aggregator_p2view_IUPresentation=p2view_aggregator_IInstallableUnit()) == None


from python_code import aggregator_p2view_IUPresentationWithDetails

def test_aggregator_p2view_IUPresentationWithDetails___init__():
    assert aggregator_p2view_IUPresentationWithDetails.__init__(aggregator_p2view_IUPresentationWithDetails(''), '') == None


from python_code import InstallableUnits
from python_code import Properties
from python_code import RepositoryReferences
from python_code import aggregator_p2view_MetadataRepositoryStructuredView
from python_code import p2view_aggregator_MetadataRepository

def test_aggregator_p2view_MetadataRepositoryStructuredView___init__():
    assert aggregator_p2view_MetadataRepositoryStructuredView.__init__(aggregator_p2view_MetadataRepositoryStructuredView('', False, '\x00\x00', aggregator_p2view_MetadataRepositoryStructuredView=InstallableUnits(), aggregator_p2view_MetadataRepositoryStructuredView115=Properties(), aggregator_p2view_MetadataRepositoryStructuredView118=p2view_aggregator_MetadataRepository(), aggregator_p2view_MetadataRepositoryStructuredView120=RepositoryReferences()), '', False, '', aggregator_p2view_MetadataRepositoryStructuredView=InstallableUnits(), aggregator_p2view_MetadataRepositoryStructuredView115=Properties(), aggregator_p2view_MetadataRepositoryStructuredView118=p2view_aggregator_MetadataRepository(), aggregator_p2view_MetadataRepositoryStructuredView120=RepositoryReferences()) == None


from python_code import Bundles
from python_code import Features
from python_code import Fragments
from python_code import aggregator_p2view_Product

def test_aggregator_p2view_Product___init__():
    assert aggregator_p2view_Product.__init__(aggregator_p2view_Product(aggregator_p2view_Product128=Fragments(), aggregator_p2view_Product=Features(), aggregator_p2view_Product125=Bundles()), aggregator_p2view_Product128=Fragments(), aggregator_p2view_Product=Features(), aggregator_p2view_Product125=Bundles()) == None

def test_aggregator_p2view_Product_getNotNullFragmentContainer():
    assert aggregator_p2view_Product.getNotNullFragmentContainer(aggregator_p2view_Product(aggregator_p2view_Product128=Fragments(), aggregator_p2view_Product=Features(), aggregator_p2view_Product125=Bundles())) == None

def test_aggregator_p2view_Product_getNotNullFeatureContainer():
    assert aggregator_p2view_Product.getNotNullFeatureContainer(aggregator_p2view_Product(aggregator_p2view_Product128=Fragments(), aggregator_p2view_Product=Features(), aggregator_p2view_Product125=Bundles())) == None

def test_aggregator_p2view_Product_getNotNullBundleContainer():
    assert aggregator_p2view_Product.getNotNullBundleContainer(aggregator_p2view_Product(aggregator_p2view_Product128=Fragments(), aggregator_p2view_Product=Features(), aggregator_p2view_Product125=Bundles())) == None


from python_code import aggregator_p2view_RepositoryBrowser

def test_aggregator_p2view_RepositoryBrowser___init__():
    assert aggregator_p2view_RepositoryBrowser.__init__(aggregator_p2view_RepositoryBrowser(False, aggregator_p2view_RepositoryBrowser=set()), False, aggregator_p2view_RepositoryBrowser=set()) == None

