from python_code import aggregator_DescriptionProvider

def test_aggregator_DescriptionProvider___init__():
    assert aggregator_DescriptionProvider.__init__(aggregator_DescriptionProvider(''), '') == None


from python_code import aggregator_EnabledStatusProvider

def test_aggregator_EnabledStatusProvider___init__():
    assert aggregator_EnabledStatusProvider.__init__(aggregator_EnabledStatusProvider(True), False) == None


from python_code import aggregator_InfosProvider

def test_aggregator_InfosProvider___init__():
    assert aggregator_InfosProvider.__init__(aggregator_InfosProvider('', '', '\x00\x00'), '', '', '') == None


from python_code import InstallableUnit
from python_code import aggregator_InstallableUnitReference

def test_aggregator_InstallableUnitReference___init__():
    assert aggregator_InstallableUnitReference.__init__(aggregator_InstallableUnitReference(aggregator_InstallableUnitReference=InstallableUnit()), aggregator_InstallableUnitReference=InstallableUnit()) == None

def test_aggregator_InstallableUnitReference_getInstallableUnit():
    assert aggregator_InstallableUnitReference.getInstallableUnit(aggregator_InstallableUnitReference(aggregator_InstallableUnitReference=InstallableUnit()), '') == None

def test_aggregator_InstallableUnitReference_isBranchEnabled():
    assert aggregator_InstallableUnitReference.isBranchEnabled(aggregator_InstallableUnitReference(aggregator_InstallableUnitReference=InstallableUnit())) == None

def test_aggregator_InstallableUnitReference_isMappedRepositoryBroken():
    assert aggregator_InstallableUnitReference.isMappedRepositoryBroken(aggregator_InstallableUnitReference(aggregator_InstallableUnitReference=InstallableUnit())) == None


from python_code import aggregator_LabelProvider

def test_aggregator_LabelProvider___init__():
    assert aggregator_LabelProvider.__init__(aggregator_LabelProvider(''), '') == None


from python_code import aggregator_MavenItem

def test_aggregator_MavenItem___init__():
    assert aggregator_MavenItem.__init__(aggregator_MavenItem('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_Property

def test_aggregator_Property___init__():
    assert aggregator_Property.__init__(aggregator_Property('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_Status
from python_code import aggregator_StatusProvider

def test_aggregator_Status___init__():
    assert aggregator_Status.__init__(aggregator_Status('', '\x00', aggregator_Status=aggregator_StatusProvider()), '\x00\x00', '', aggregator_Status=aggregator_StatusProvider()) == None


from python_code import aggregator_p2_IAdaptable

def test_aggregator_p2_IAdaptable___init__():
    assert aggregator_p2_IAdaptable.__init__(aggregator_p2_IAdaptable()) == None

def test_aggregator_p2_IAdaptable_getAdapter():
    assert aggregator_p2_IAdaptable.getAdapter(aggregator_p2_IAdaptable(), '') == None


from python_code import aggregator_p2_IArtifactKey

def test_aggregator_p2_IArtifactKey___init__():
    assert aggregator_p2_IArtifactKey.__init__(aggregator_p2_IArtifactKey('', '', '\x00\x00'), '', '', '') == None

def test_aggregator_p2_IArtifactKey_toExternalForm():
    assert aggregator_p2_IArtifactKey.toExternalForm(aggregator_p2_IArtifactKey('', '', '\x00')) == None


from python_code import aggregator_p2_ICopyright

def test_aggregator_p2_ICopyright___init__():
    assert aggregator_p2_ICopyright.__init__(aggregator_p2_ICopyright('', '\x00'), '\x00\x00', '') == None


from python_code import ICopyright
from python_code import ILicense
from python_code import ITouchpointType
from python_code import IUpdateDescriptor
from python_code import aggregator_p2_IInstallableUnit

def test_aggregator_p2_IInstallableUnit___init__():
    assert aggregator_p2_IInstallableUnit.__init__(aggregator_p2_IInstallableUnit('', '', '', False, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright()), '', '\x00', '', False, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright()) == None

def test_aggregator_p2_IInstallableUnit_getTouchpointData():
    assert aggregator_p2_IInstallableUnit.getTouchpointData(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_getArtifacts():
    assert aggregator_p2_IInstallableUnit.getArtifacts(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_getProperty():
    assert aggregator_p2_IInstallableUnit.getProperty(aggregator_p2_IInstallableUnit('', '', '', False, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright()), '') == None

def test_aggregator_p2_IInstallableUnit_getFragments():
    assert aggregator_p2_IInstallableUnit.getFragments(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_satisfies():
    assert aggregator_p2_IInstallableUnit.satisfies(aggregator_p2_IInstallableUnit('', '', '', False, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright()), '') == None

def test_aggregator_p2_IInstallableUnit_getRequiredCapabilities():
    assert aggregator_p2_IInstallableUnit.getRequiredCapabilities(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_getMetaRequiredCapabilities():
    assert aggregator_p2_IInstallableUnit.getMetaRequiredCapabilities(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_isFragment():
    assert aggregator_p2_IInstallableUnit.isFragment(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_getProvidedCapabilities():
    assert aggregator_p2_IInstallableUnit.getProvidedCapabilities(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_getProperties():
    assert aggregator_p2_IInstallableUnit.getProperties(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None

def test_aggregator_p2_IInstallableUnit_unresolved():
    assert aggregator_p2_IInstallableUnit.unresolved(aggregator_p2_IInstallableUnit('', '', '', True, False, aggregator_p2_IInstallableUnit=ITouchpointType(), aggregator_p2_IInstallableUnit43=IUpdateDescriptor(), aggregator_p2_IInstallableUnit45=ILicense(), aggregator_p2_IInstallableUnit47=ICopyright())) == None


from python_code import aggregator_p2_IInstallableUnitFragment

def test_aggregator_p2_IInstallableUnitFragment___init__():
    assert aggregator_p2_IInstallableUnitFragment.__init__(aggregator_p2_IInstallableUnitFragment()) == None

def test_aggregator_p2_IInstallableUnitFragment_getHost():
    assert aggregator_p2_IInstallableUnitFragment.getHost(aggregator_p2_IInstallableUnitFragment()) == None


from python_code import aggregator_p2_ILicense

def test_aggregator_p2_ILicense___init__():
    assert aggregator_p2_ILicense.__init__(aggregator_p2_ILicense('', '', '\x00\x00'), '', '', '') == None


from python_code import aggregator_p2_IMetadataRepository

def test_aggregator_p2_IMetadataRepository___init__():
    assert aggregator_p2_IMetadataRepository.__init__(aggregator_p2_IMetadataRepository()) == None

def test_aggregator_p2_IMetadataRepository_removeAll():
    assert aggregator_p2_IMetadataRepository.removeAll(aggregator_p2_IMetadataRepository()) == None

def test_aggregator_p2_IMetadataRepository_addInstallableUnits():
    assert aggregator_p2_IMetadataRepository.addInstallableUnits(aggregator_p2_IMetadataRepository(), '') == None

def test_aggregator_p2_IMetadataRepository_removeInstallableUnits():
    assert aggregator_p2_IMetadataRepository.removeInstallableUnits(aggregator_p2_IMetadataRepository(), '', '') == None

def test_aggregator_p2_IMetadataRepository_addReference():
    assert aggregator_p2_IMetadataRepository.addReference(aggregator_p2_IMetadataRepository(), '', '', '', '') == None


from python_code import aggregator_p2_IProvidedCapability

def test_aggregator_p2_IProvidedCapability___init__():
    assert aggregator_p2_IProvidedCapability.__init__(aggregator_p2_IProvidedCapability('', '', '\x00\x00'), '', '', '') == None

def test_aggregator_p2_IProvidedCapability_satisfies():
    assert aggregator_p2_IProvidedCapability.satisfies(aggregator_p2_IProvidedCapability('', '', '\x00'), '') == None


from python_code import aggregator_p2_IQueryable

def test_aggregator_p2_IQueryable___init__():
    assert aggregator_p2_IQueryable.__init__(aggregator_p2_IQueryable()) == None

def test_aggregator_p2_IQueryable_query():
    assert aggregator_p2_IQueryable.query(aggregator_p2_IQueryable(), '', '', '') == None


from python_code import aggregator_p2_IRepository

def test_aggregator_p2_IRepository___init__():
    assert aggregator_p2_IRepository.__init__(aggregator_p2_IRepository('', '', '', '', '', '', False), '', '\x00', '', '', '', '', False) == None

def test_aggregator_p2_IRepository_setProperty():
    assert aggregator_p2_IRepository.setProperty(aggregator_p2_IRepository('', '\x00\x00', '', '', '', '', False), 0, '') == None

def test_aggregator_p2_IRepository_getProperties():
    assert aggregator_p2_IRepository.getProperties(aggregator_p2_IRepository('', '\x00\x00', '', '', '', '', False)) == None


from python_code import aggregator_p2_IRequiredCapability

def test_aggregator_p2_IRequiredCapability___init__():
    assert aggregator_p2_IRequiredCapability.__init__(aggregator_p2_IRequiredCapability('', '', '', '', False, '', False, False, False), '', '', '', '', False, '', False, False, False) == None

def test_aggregator_p2_IRequiredCapability_getSelectors():
    assert aggregator_p2_IRequiredCapability.getSelectors(aggregator_p2_IRequiredCapability('\x00', '', '', '', True, '', False, False, False)) == None

def test_aggregator_p2_IRequiredCapability_satisfiedBy():
    assert aggregator_p2_IRequiredCapability.satisfiedBy(aggregator_p2_IRequiredCapability('\x00', '', '', '', True, '', False, False, False), '') == None

def test_aggregator_p2_IRequiredCapability_setSelectors():
    assert aggregator_p2_IRequiredCapability.setSelectors(aggregator_p2_IRequiredCapability('\x00', '', '', '', True, '', False, False, False), '') == None


from python_code import aggregator_p2_ITouchpointData

def test_aggregator_p2_ITouchpointData___init__():
    assert aggregator_p2_ITouchpointData.__init__(aggregator_p2_ITouchpointData()) == None

def test_aggregator_p2_ITouchpointData_getInstructions():
    assert aggregator_p2_ITouchpointData.getInstructions(aggregator_p2_ITouchpointData()) == None

def test_aggregator_p2_ITouchpointData_getInstruction():
    assert aggregator_p2_ITouchpointData.getInstruction(aggregator_p2_ITouchpointData(), '') == None


from python_code import aggregator_p2_ITouchpointInstruction

def test_aggregator_p2_ITouchpointInstruction___init__():
    assert aggregator_p2_ITouchpointInstruction.__init__(aggregator_p2_ITouchpointInstruction('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_p2_ITouchpointType

def test_aggregator_p2_ITouchpointType___init__():
    assert aggregator_p2_ITouchpointType.__init__(aggregator_p2_ITouchpointType('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_p2_IUpdateDescriptor

def test_aggregator_p2_IUpdateDescriptor___init__():
    assert aggregator_p2_IUpdateDescriptor.__init__(aggregator_p2_IUpdateDescriptor('\x00\x00', 0, '', ''), '', 0, '', '') == None

def test_aggregator_p2_IUpdateDescriptor_isUpdateOf():
    assert aggregator_p2_IUpdateDescriptor.isUpdateOf(aggregator_p2_IUpdateDescriptor('', 0, '', ''), '') == None


from python_code import aggregator_p2_InstallableUnit

def test_aggregator_p2_InstallableUnit___init__():
    assert aggregator_p2_InstallableUnit.__init__(aggregator_p2_InstallableUnit(aggregator_p2_InstallableUnit56=set(), aggregator_p2_InstallableUnit58=set(), aggregator_p2_InstallableUnit60=set(), aggregator_p2_InstallableUnit63=set(), aggregator_p2_InstallableUnit66=set(), aggregator_p2_InstallableUnit=set()), aggregator_p2_InstallableUnit56=set(), aggregator_p2_InstallableUnit58=set(), aggregator_p2_InstallableUnit60=set(), aggregator_p2_InstallableUnit63=set(), aggregator_p2_InstallableUnit66=set(), aggregator_p2_InstallableUnit=set()) == None

def test_aggregator_p2_InstallableUnit_compareTo():
    assert aggregator_p2_InstallableUnit.compareTo(aggregator_p2_InstallableUnit(aggregator_p2_InstallableUnit56=set(), aggregator_p2_InstallableUnit58=set(), aggregator_p2_InstallableUnit60=set(), aggregator_p2_InstallableUnit63=set(), aggregator_p2_InstallableUnit66=set(), aggregator_p2_InstallableUnit=set()), '') == None


from python_code import TouchpointInstruction
from python_code import aggregator_p2_InstructionMap

def test_aggregator_p2_InstructionMap___init__():
    assert aggregator_p2_InstructionMap.__init__(aggregator_p2_InstructionMap('', aggregator_p2_InstructionMap=TouchpointInstruction()), '', aggregator_p2_InstructionMap=TouchpointInstruction()) == None


from python_code import aggregator_p2_Property

def test_aggregator_p2_Property___init__():
    assert aggregator_p2_Property.__init__(aggregator_p2_Property('', '\x00'), '\x00\x00', '') == None


from python_code import aggregator_p2_RepositoryReference

def test_aggregator_p2_RepositoryReference___init__():
    assert aggregator_p2_RepositoryReference.__init__(aggregator_p2_RepositoryReference('\x00\x00', 0, 0, ''), '', 0, 0, '') == None


from python_code import Bundles
from python_code import Categories
from python_code import Features
from python_code import Fragments
from python_code import IUDetails
from python_code import Products
from python_code import aggregator_p2view_Category

def test_aggregator_p2view_Category___init__():
    assert aggregator_p2view_Category.__init__(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails()), aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails()) == None

def test_aggregator_p2view_Category_getNotNullFeatureContainer():
    assert aggregator_p2view_Category.getNotNullFeatureContainer(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None

def test_aggregator_p2view_Category_isNested():
    assert aggregator_p2view_Category.isNested(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None

def test_aggregator_p2view_Category_getNotNullBundleContainer():
    assert aggregator_p2view_Category.getNotNullBundleContainer(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None

def test_aggregator_p2view_Category_getNotNullCategoryContainer():
    assert aggregator_p2view_Category.getNotNullCategoryContainer(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None

def test_aggregator_p2view_Category_getNotNullFragmentContainer():
    assert aggregator_p2view_Category.getNotNullFragmentContainer(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None

def test_aggregator_p2view_Category_getNotNullProductContainer():
    assert aggregator_p2view_Category.getNotNullProductContainer(aggregator_p2view_Category(aggregator_p2view_Category=Categories(), aggregator_p2view_Category100=Features(), aggregator_p2view_Category103=Products(), aggregator_p2view_Category106=Bundles(), aggregator_p2view_Category109=Fragments(), aggregator_p2view_Category112=IUDetails())) == None


from python_code import Bundles
from python_code import Features
from python_code import Fragments
from python_code import aggregator_p2view_Feature

def test_aggregator_p2view_Feature___init__():
    assert aggregator_p2view_Feature.__init__(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature116=Bundles(), aggregator_p2view_Feature119=Fragments()), aggregator_p2view_Feature=Features(), aggregator_p2view_Feature116=Bundles(), aggregator_p2view_Feature119=Fragments()) == None

def test_aggregator_p2view_Feature_getNotNullFeatureContainer():
    assert aggregator_p2view_Feature.getNotNullFeatureContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature116=Bundles(), aggregator_p2view_Feature119=Fragments())) == None

def test_aggregator_p2view_Feature_getNotNullBundleContainer():
    assert aggregator_p2view_Feature.getNotNullBundleContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature116=Bundles(), aggregator_p2view_Feature119=Fragments())) == None

def test_aggregator_p2view_Feature_getNotNullFragmentContainer():
    assert aggregator_p2view_Feature.getNotNullFragmentContainer(aggregator_p2view_Feature(aggregator_p2view_Feature=Features(), aggregator_p2view_Feature116=Bundles(), aggregator_p2view_Feature119=Fragments())) == None


from python_code import InstallableUnit
from python_code import aggregator_p2view_IUPresentation

def test_aggregator_p2view_IUPresentation___init__():
    assert aggregator_p2view_IUPresentation.__init__(aggregator_p2view_IUPresentation('', '', '', '', '', '', aggregator_p2view_IUPresentation=InstallableUnit()), '', '', '', '', '\x00', '', aggregator_p2view_IUPresentation=InstallableUnit()) == None


from python_code import aggregator_p2view_IUPresentationWithDetails

def test_aggregator_p2view_IUPresentationWithDetails___init__():
    assert aggregator_p2view_IUPresentationWithDetails.__init__(aggregator_p2view_IUPresentationWithDetails(''), '') == None


from python_code import Bundles
from python_code import Categories
from python_code import Features
from python_code import Fragments
from python_code import Miscellaneous
from python_code import Products
from python_code import aggregator_p2view_InstallableUnits

def test_aggregator_p2view_InstallableUnits___init__():
    assert aggregator_p2view_InstallableUnits.__init__(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous()), aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous()) == None

def test_aggregator_p2view_InstallableUnits_getNotNullMiscellaneousContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullMiscellaneousContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None

def test_aggregator_p2view_InstallableUnits_getNotNullFragmentContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullFragmentContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None

def test_aggregator_p2view_InstallableUnits_getNotNullProductContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullProductContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None

def test_aggregator_p2view_InstallableUnits_getNotNullCategoryContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullCategoryContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None

def test_aggregator_p2view_InstallableUnits_getNotNullBundleContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullBundleContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None

def test_aggregator_p2view_InstallableUnits_getNotNullFeatureContainer():
    assert aggregator_p2view_InstallableUnits.getNotNullFeatureContainer(aggregator_p2view_InstallableUnits(aggregator_p2view_InstallableUnits85=Fragments(), aggregator_p2view_InstallableUnits=Categories(), aggregator_p2view_InstallableUnits79=Features(), aggregator_p2view_InstallableUnits81=Products(), aggregator_p2view_InstallableUnits83=Bundles(), aggregator_p2view_InstallableUnits87=Miscellaneous())) == None


from python_code import InstallableUnits
from python_code import MetadataRepository
from python_code import Properties
from python_code import aggregator_p2view_MetadataRepositoryStructuredView

def test_aggregator_p2view_MetadataRepositoryStructuredView___init__():
    assert aggregator_p2view_MetadataRepositoryStructuredView.__init__(aggregator_p2view_MetadataRepositoryStructuredView('', False, aggregator_p2view_MetadataRepositoryStructuredView=InstallableUnits(), aggregator_p2view_MetadataRepositoryStructuredView73=Properties(), aggregator_p2view_MetadataRepositoryStructuredView75=MetadataRepository()), '', False, aggregator_p2view_MetadataRepositoryStructuredView=InstallableUnits(), aggregator_p2view_MetadataRepositoryStructuredView73=Properties(), aggregator_p2view_MetadataRepositoryStructuredView75=MetadataRepository()) == None


from python_code import Bundles
from python_code import Features
from python_code import Fragments
from python_code import aggregator_p2view_Product

def test_aggregator_p2view_Product___init__():
    assert aggregator_p2view_Product.__init__(aggregator_p2view_Product(aggregator_p2view_Product=Features(), aggregator_p2view_Product124=Bundles(), aggregator_p2view_Product127=Fragments()), aggregator_p2view_Product=Features(), aggregator_p2view_Product124=Bundles(), aggregator_p2view_Product127=Fragments()) == None

def test_aggregator_p2view_Product_getNotNullBundleContainer():
    assert aggregator_p2view_Product.getNotNullBundleContainer(aggregator_p2view_Product(aggregator_p2view_Product=Features(), aggregator_p2view_Product124=Bundles(), aggregator_p2view_Product127=Fragments())) == None

def test_aggregator_p2view_Product_getNotNullFeatureContainer():
    assert aggregator_p2view_Product.getNotNullFeatureContainer(aggregator_p2view_Product(aggregator_p2view_Product=Features(), aggregator_p2view_Product124=Bundles(), aggregator_p2view_Product127=Fragments())) == None

def test_aggregator_p2view_Product_getNotNullFragmentContainer():
    assert aggregator_p2view_Product.getNotNullFragmentContainer(aggregator_p2view_Product(aggregator_p2view_Product=Features(), aggregator_p2view_Product124=Bundles(), aggregator_p2view_Product127=Fragments())) == None

