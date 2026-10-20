from python_code import p2_Comparable

def test_p2_Comparable___init__():
    assert p2_Comparable.__init__(p2_Comparable()) == None

def test_p2_Comparable_compareTo():
    assert p2_Comparable.compareTo(p2_Comparable(), '') == None


from python_code import p2_IAdaptable

def test_p2_IAdaptable___init__():
    assert p2_IAdaptable.__init__(p2_IAdaptable()) == None

def test_p2_IAdaptable_getAdapter():
    assert p2_IAdaptable.getAdapter(p2_IAdaptable(), '') == None


from python_code import p2_IArtifactRepository

def test_p2_IArtifactRepository___init__():
    assert p2_IArtifactRepository.__init__(p2_IArtifactRepository()) == None

def test_p2_IArtifactRepository_getArtifacts():
    assert p2_IArtifactRepository.getArtifacts(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_addDescriptors():
    assert p2_IArtifactRepository.addDescriptors(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_contains():
    assert p2_IArtifactRepository.contains(p2_IArtifactRepository(), '') == None

def test_p2_IArtifactRepository_createArtifactKey():
    assert p2_IArtifactRepository.createArtifactKey(p2_IArtifactRepository(), '', '', '') == None

def test_p2_IArtifactRepository_executeBatch():
    assert p2_IArtifactRepository.executeBatch(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_createArtifactDescriptor():
    assert p2_IArtifactRepository.createArtifactDescriptor(p2_IArtifactRepository(), '') == None

def test_p2_IArtifactRepository_removeDescriptors():
    assert p2_IArtifactRepository.removeDescriptors(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_addDescriptor():
    assert p2_IArtifactRepository.addDescriptor(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_getRawArtifact():
    assert p2_IArtifactRepository.getRawArtifact(p2_IArtifactRepository(), '', '', '') == None

def test_p2_IArtifactRepository_removeDescriptor():
    assert p2_IArtifactRepository.removeDescriptor(p2_IArtifactRepository(), '', '') == None

def test_p2_IArtifactRepository_removeAll():
    assert p2_IArtifactRepository.removeAll(p2_IArtifactRepository(), '') == None

def test_p2_IArtifactRepository_getArtifact():
    assert p2_IArtifactRepository.getArtifact(p2_IArtifactRepository(), '', '', '') == None

def test_p2_IArtifactRepository_getArtifactDescriptors():
    assert p2_IArtifactRepository.getArtifactDescriptors(p2_IArtifactRepository(), '') == None

def test_p2_IArtifactRepository_descriptorQueryable():
    assert p2_IArtifactRepository.descriptorQueryable(p2_IArtifactRepository()) == None

def test_p2_IArtifactRepository_getOutputStream():
    assert p2_IArtifactRepository.getOutputStream(p2_IArtifactRepository(), '') == None


from python_code import p2_IFileArtifactRepository

def test_p2_IFileArtifactRepository___init__():
    assert p2_IFileArtifactRepository.__init__(p2_IFileArtifactRepository()) == None

def test_p2_IFileArtifactRepository_getArtifactFile():
    assert p2_IFileArtifactRepository.getArtifactFile(p2_IFileArtifactRepository(), '') == None


from python_code import p2_IMetadataRepository

def test_p2_IMetadataRepository___init__():
    assert p2_IMetadataRepository.__init__(p2_IMetadataRepository()) == None

def test_p2_IMetadataRepository_removeInstallableUnits():
    assert p2_IMetadataRepository.removeInstallableUnits(p2_IMetadataRepository(), '') == None

def test_p2_IMetadataRepository_compress():
    assert p2_IMetadataRepository.compress(p2_IMetadataRepository(), '') == None

def test_p2_IMetadataRepository_executeBatch():
    assert p2_IMetadataRepository.executeBatch(p2_IMetadataRepository(), '', '') == None

def test_p2_IMetadataRepository_addInstallableUnits():
    assert p2_IMetadataRepository.addInstallableUnits(p2_IMetadataRepository(), '') == None

def test_p2_IMetadataRepository_removeAll():
    assert p2_IMetadataRepository.removeAll(p2_IMetadataRepository()) == None

def test_p2_IMetadataRepository_addReferences():
    assert p2_IMetadataRepository.addReferences(p2_IMetadataRepository(), '') == None


from python_code import p2_ArtifactDescriptor
from python_code import p2_IProcessingStepDescriptor

def test_p2_IProcessingStepDescriptor___init__():
    assert p2_IProcessingStepDescriptor.__init__(p2_IProcessingStepDescriptor('', '', False, p2_IProcessingStepDescriptor=p2_ArtifactDescriptor()), '\x00', '', False, p2_IProcessingStepDescriptor=p2_ArtifactDescriptor()) == None


from python_code import p2_IQueryable

def test_p2_IQueryable___init__():
    assert p2_IQueryable.__init__(p2_IQueryable()) == None

def test_p2_IQueryable_query():
    assert p2_IQueryable.query(p2_IQueryable(), '', '') == None


from python_code import p2_IRepository

def test_p2_IRepository___init__():
    assert p2_IRepository.__init__(p2_IRepository('', '', '', False, '', '', '\x00', ''), '', '', '', False, '', '', '', '') == None

def test_p2_IRepository_setProperty():
    assert p2_IRepository.setProperty(p2_IRepository('\x00\x00', '', '', True, '', '', '', ''), '', '', '') == None

def test_p2_IRepository_getProperty():
    assert p2_IRepository.getProperty(p2_IRepository('\x00\x00', '', '', True, '', '', '', ''), '') == None

def test_p2_IRepository_getProperties():
    assert p2_IRepository.getProperties(p2_IRepository('\x00\x00', '', '', True, '', '', '', '')) == None


from python_code import p2_IRepositoryReference
from python_code import p2_MetadataRepository

def test_p2_IRepositoryReference___init__():
    assert p2_IRepositoryReference.__init__(p2_IRepositoryReference('\x00\x00', 0, 0, '', p2_IRepositoryReference=p2_MetadataRepository()), '', 0, 0, '', p2_IRepositoryReference=p2_MetadataRepository()) == None


from python_code import p2_IVersionedId

def test_p2_IVersionedId___init__():
    assert p2_IVersionedId.__init__(p2_IVersionedId('', '\x00'), '\x00\x00', '') == None


from python_code import p2_InstallableUnitPatch

def test_p2_InstallableUnitPatch___init__():
    assert p2_InstallableUnitPatch.__init__(p2_InstallableUnitPatch()) == None

def test_p2_InstallableUnitPatch_getApplicabilityScope():
    assert p2_InstallableUnitPatch.getApplicabilityScope(p2_InstallableUnitPatch()) == None


from python_code import p2_MappingRule
from python_code import p2_SimpleArtifactRepository

def test_p2_MappingRule___init__():
    assert p2_MappingRule.__init__(p2_MappingRule('', '\x00', p2_MappingRule=p2_SimpleArtifactRepository()), '\x00\x00', '', p2_MappingRule=p2_SimpleArtifactRepository()) == None


from python_code import p2_SimpleArtifactDescriptor

def test_p2_SimpleArtifactDescriptor___init__():
    assert p2_SimpleArtifactDescriptor.__init__(p2_SimpleArtifactDescriptor(p2_SimpleArtifactDescriptor=set()), p2_SimpleArtifactDescriptor=set()) == None

def test_p2_SimpleArtifactDescriptor_getRepositoryProperties():
    assert p2_SimpleArtifactDescriptor.getRepositoryProperties(p2_SimpleArtifactDescriptor(p2_SimpleArtifactDescriptor=set())) == None

def test_p2_SimpleArtifactDescriptor_getRepositoryProperty():
    assert p2_SimpleArtifactDescriptor.getRepositoryProperty(p2_SimpleArtifactDescriptor(p2_SimpleArtifactDescriptor=set()), 0) == None

