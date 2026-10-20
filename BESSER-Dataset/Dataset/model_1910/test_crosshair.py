from python_code import myDsl_Album

def test_myDsl_Album___init__():
    assert myDsl_Album.__init__(myDsl_Album(''), '') == None


from python_code import myDsl_AlbumManagement
from python_code import myDsl_AlbumManagementFunctions

def test_myDsl_AlbumManagementFunctions___init__():
    assert myDsl_AlbumManagementFunctions.__init__(myDsl_AlbumManagementFunctions('', myDsl_AlbumManagementFunctions=myDsl_AlbumManagement()), '', myDsl_AlbumManagementFunctions=myDsl_AlbumManagement()) == None


from python_code import myDsl_AmazonWebServices

def test_myDsl_AmazonWebServices___init__():
    assert myDsl_AmazonWebServices.__init__(myDsl_AmazonWebServices(''), '') == None


from python_code import myDsl_AppAccess
from python_code import myDsl_AppAccessFunctions

def test_myDsl_AppAccessFunctions___init__():
    assert myDsl_AppAccessFunctions.__init__(myDsl_AppAccessFunctions('', myDsl_AppAccessFunctions=myDsl_AppAccess()), '', myDsl_AppAccessFunctions=myDsl_AppAccess()) == None


from python_code import myDsl_BackEnd

def test_myDsl_BackEnd___init__():
    assert myDsl_BackEnd.__init__(myDsl_BackEnd(''), '') == None


from python_code import myDsl_BusinessLogicContent
from python_code import myDsl_BusinessLogicSegments

def test_myDsl_BusinessLogicSegments___init__():
    assert myDsl_BusinessLogicSegments.__init__(myDsl_BusinessLogicSegments('', myDsl_BusinessLogicSegments=myDsl_BusinessLogicContent()), '', myDsl_BusinessLogicSegments=myDsl_BusinessLogicContent()) == None


from python_code import myDsl_ComponentsLogic
from python_code import myDsl_ReactComponents

def test_myDsl_ComponentsLogic___init__():
    assert myDsl_ComponentsLogic.__init__(myDsl_ComponentsLogic('', myDsl_ComponentsLogic=myDsl_ReactComponents(), myDsl_ComponentsLogic95=set()), '', myDsl_ComponentsLogic=myDsl_ReactComponents(), myDsl_ComponentsLogic95=set()) == None


from python_code import myDsl_ComponentsUI
from python_code import myDsl_ReactComponents

def test_myDsl_ComponentsUI___init__():
    assert myDsl_ComponentsUI.__init__(myDsl_ComponentsUI('', myDsl_ComponentsUI=myDsl_ReactComponents(), myDsl_ComponentsUI101=set()), '', myDsl_ComponentsUI=myDsl_ReactComponents(), myDsl_ComponentsUI101=set()) == None


from python_code import myDsl_CoreFunctionsDeclaration

def test_myDsl_CoreFunctionsDeclaration___init__():
    assert myDsl_CoreFunctionsDeclaration.__init__(myDsl_CoreFunctionsDeclaration(''), '') == None


from python_code import myDsl_DataPersistenceContent
from python_code import myDsl_DataPersistenceSegments

def test_myDsl_DataPersistenceSegments___init__():
    assert myDsl_DataPersistenceSegments.__init__(myDsl_DataPersistenceSegments('', myDsl_DataPersistenceSegments=myDsl_DataPersistenceContent()), '', myDsl_DataPersistenceSegments=myDsl_DataPersistenceContent()) == None


from python_code import myDsl_Domain

def test_myDsl_Domain___init__():
    assert myDsl_Domain.__init__(myDsl_Domain('', myDsl_Domain=set()), '', myDsl_Domain=set()) == None


from python_code import myDsl_DomainConnection
from python_code import myDsl_DomainRelations

def test_myDsl_DomainRelations___init__():
    assert myDsl_DomainRelations.__init__(myDsl_DomainRelations('', myDsl_DomainRelations=myDsl_DomainConnection(), myDsl_DomainRelations30=set()), '', myDsl_DomainRelations=myDsl_DomainConnection(), myDsl_DomainRelations30=set()) == None


from python_code import myDsl_FrontEnd

def test_myDsl_FrontEnd___init__():
    assert myDsl_FrontEnd.__init__(myDsl_FrontEnd(''), '') == None


from python_code import myDsl_LandingActions
from python_code import myDsl_LandingFunctions

def test_myDsl_LandingFunctions___init__():
    assert myDsl_LandingFunctions.__init__(myDsl_LandingFunctions('', myDsl_LandingFunctions=myDsl_LandingActions()), '', myDsl_LandingFunctions=myDsl_LandingActions()) == None


from python_code import myDsl_LayerRelations

def test_myDsl_LayerRelations___init__():
    assert myDsl_LayerRelations.__init__(myDsl_LayerRelations('', '', myDsl_LayerRelations=set(), myDsl_LayerRelations56=set()), '', '', myDsl_LayerRelations=set(), myDsl_LayerRelations56=set()) == None


from python_code import myDsl_Directories
from python_code import myDsl_MultipleFile

def test_myDsl_MultipleFile___init__():
    assert myDsl_MultipleFile.__init__(myDsl_MultipleFile('', myDsl_MultipleFile=myDsl_Directories()), '', myDsl_MultipleFile=myDsl_Directories()) == None


from python_code import myDsl_NTiersConnections

def test_myDsl_NTiersConnections___init__():
    assert myDsl_NTiersConnections.__init__(myDsl_NTiersConnections('', '', myDsl_NTiersConnections=set(), myDsl_NTiersConnections61=set()), '', '', myDsl_NTiersConnections=set(), myDsl_NTiersConnections61=set()) == None


from python_code import myDsl_NTierSource
from python_code import myDsl_NTierTarget
from python_code import myDsl_NTiersRelations

def test_myDsl_NTiersRelations___init__():
    assert myDsl_NTiersRelations.__init__(myDsl_NTiersRelations('', myDsl_NTiersRelations=myDsl_NTierSource(), myDsl_NTiersRelations66=myDsl_NTierTarget()), '', myDsl_NTiersRelations=myDsl_NTierSource(), myDsl_NTiersRelations66=myDsl_NTierTarget()) == None


from python_code import myDsl_PackageName

def test_myDsl_PackageName___init__():
    assert myDsl_PackageName.__init__(myDsl_PackageName(''), '') == None


from python_code import myDsl_PackageVersion

def test_myDsl_PackageVersion___init__():
    assert myDsl_PackageVersion.__init__(myDsl_PackageVersion(''), '') == None


from python_code import myDsl_PersistenceDataComponent

def test_myDsl_PersistenceDataComponent___init__():
    assert myDsl_PersistenceDataComponent.__init__(myDsl_PersistenceDataComponent(''), '') == None


from python_code import myDsl_Photo

def test_myDsl_Photo___init__():
    assert myDsl_Photo.__init__(myDsl_Photo(''), '') == None


from python_code import myDsl_PhotoActions
from python_code import myDsl_PhotoActionsFunctions

def test_myDsl_PhotoActionsFunctions___init__():
    assert myDsl_PhotoActionsFunctions.__init__(myDsl_PhotoActionsFunctions('', myDsl_PhotoActionsFunctions=myDsl_PhotoActions()), '', myDsl_PhotoActionsFunctions=myDsl_PhotoActions()) == None


from python_code import myDsl_PostgreSQL

def test_myDsl_PostgreSQL___init__():
    assert myDsl_PostgreSQL.__init__(myDsl_PostgreSQL(''), '') == None


from python_code import myDsl_PresentationContent
from python_code import myDsl_PresentationSegments

def test_myDsl_PresentationSegments___init__():
    assert myDsl_PresentationSegments.__init__(myDsl_PresentationSegments('', myDsl_PresentationSegments=myDsl_PresentationContent()), '', myDsl_PresentationSegments=myDsl_PresentationContent()) == None


from python_code import myDsl_ProfileManagement
from python_code import myDsl_ProfileManagementFunctions

def test_myDsl_ProfileManagementFunctions___init__():
    assert myDsl_ProfileManagementFunctions.__init__(myDsl_ProfileManagementFunctions('', myDsl_ProfileManagementFunctions=myDsl_ProfileManagement()), '', myDsl_ProfileManagementFunctions=myDsl_ProfileManagement()) == None


from python_code import myDsl_Props

def test_myDsl_Props___init__():
    assert myDsl_Props.__init__(myDsl_Props('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl_React

def test_myDsl_React___init__():
    assert myDsl_React.__init__(myDsl_React('', myDsl_React=set()), '', myDsl_React=set()) == None


from python_code import myDsl_ReactConfiguration
from python_code import myDsl_ReactConfigurations

def test_myDsl_ReactConfigurations___init__():
    assert myDsl_ReactConfigurations.__init__(myDsl_ReactConfigurations('', myDsl_ReactConfigurations=myDsl_ReactConfiguration(), myDsl_ReactConfigurations90=set()), '', myDsl_ReactConfigurations=myDsl_ReactConfiguration(), myDsl_ReactConfigurations90=set()) == None


from python_code import myDsl_ReactCoreFunctions

def test_myDsl_ReactCoreFunctions___init__():
    assert myDsl_ReactCoreFunctions.__init__(myDsl_ReactCoreFunctions(''), '') == None


from python_code import myDsl_ReactDependencies
from python_code import myDsl_ReactDependenciesRules

def test_myDsl_ReactDependenciesRules___init__():
    assert myDsl_ReactDependenciesRules.__init__(myDsl_ReactDependenciesRules('', myDsl_ReactDependenciesRules=myDsl_ReactDependencies(), myDsl_ReactDependenciesRules83=set()), '', myDsl_ReactDependenciesRules=myDsl_ReactDependencies(), myDsl_ReactDependenciesRules83=set()) == None


from python_code import myDsl_ReactFunctions

def test_myDsl_ReactFunctions___init__():
    assert myDsl_ReactFunctions.__init__(myDsl_ReactFunctions('\x00\x00', '', myDsl_ReactFunctions=set()), '', '', myDsl_ReactFunctions=set()) == None


from python_code import myDsl_ReactInfo
from python_code import myDsl_ReactInformation

def test_myDsl_ReactInformation___init__():
    assert myDsl_ReactInformation.__init__(myDsl_ReactInformation('', myDsl_ReactInformation=myDsl_ReactInfo()), '', myDsl_ReactInformation=myDsl_ReactInfo()) == None


from python_code import myDsl_ReactLibraries
from python_code import myDsl_ReactLibrary

def test_myDsl_ReactLibrary___init__():
    assert myDsl_ReactLibrary.__init__(myDsl_ReactLibrary('', myDsl_ReactLibrary=myDsl_ReactLibraries()), '', myDsl_ReactLibrary=myDsl_ReactLibraries()) == None


from python_code import myDsl_ReactActionsContent
from python_code import myDsl_ReactServicesRelation

def test_myDsl_ReactServicesRelation___init__():
    assert myDsl_ReactServicesRelation.__init__(myDsl_ReactServicesRelation('\x00', myDsl_ReactServicesRelation=myDsl_ReactActionsContent(), myDsl_ReactServicesRelation116=set()), '', myDsl_ReactServicesRelation=myDsl_ReactActionsContent(), myDsl_ReactServicesRelation116=set()) == None


from python_code import myDsl_SegmentStructure
from python_code import myDsl_SegmentStructureContent

def test_myDsl_SegmentStructureContent___init__():
    assert myDsl_SegmentStructureContent.__init__(myDsl_SegmentStructureContent('', myDsl_SegmentStructureContent49=set(), myDsl_SegmentStructureContent=myDsl_SegmentStructure()), '', myDsl_SegmentStructureContent49=set(), myDsl_SegmentStructureContent=myDsl_SegmentStructure()) == None


from python_code import myDsl_SingleFile

def test_myDsl_SingleFile___init__():
    assert myDsl_SingleFile.__init__(myDsl_SingleFile(''), '') == None


from python_code import myDsl_Spring

def test_myDsl_Spring___init__():
    assert myDsl_Spring.__init__(myDsl_Spring(''), '') == None


from python_code import myDsl_State

def test_myDsl_State___init__():
    assert myDsl_State.__init__(myDsl_State('', '\x00'), '\x00\x00', '') == None


from python_code import myDsl_Technology

def test_myDsl_Technology___init__():
    assert myDsl_Technology.__init__(myDsl_Technology('', myDsl_Technology=set()), '', myDsl_Technology=set()) == None


from python_code import myDsl_UserDomain

def test_myDsl_UserDomain___init__():
    assert myDsl_UserDomain.__init__(myDsl_UserDomain(''), '') == None

