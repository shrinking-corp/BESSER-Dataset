from python_code import model_AccessRelationship

def test_model_AccessRelationship___init__():
    assert model_AccessRelationship.__init__(model_AccessRelationship(0), 0) == None


from python_code import model_Adapter

def test_model_Adapter___init__():
    assert model_Adapter.__init__(model_Adapter()) == None

def test_model_Adapter_setAdapter():
    assert model_Adapter.setAdapter(model_Adapter(), '', '') == None

def test_model_Adapter_getAdapter():
    assert model_Adapter.getAdapter(model_Adapter(), '') == None


from python_code import model_ArchimateDiagramModel

def test_model_ArchimateDiagramModel___init__():
    assert model_ArchimateDiagramModel.__init__(model_ArchimateDiagramModel(0), 0) == None


from python_code import model_ArchimateModel
from python_code import model_ArchimateModelElement

def test_model_ArchimateModel___init__():
    assert model_ArchimateModel.__init__(model_ArchimateModel('', '', '\x00\x00', model_ArchimateModel=model_ArchimateModelElement()), '', '', '', model_ArchimateModel=model_ArchimateModelElement()) == None

def test_model_ArchimateModel_setDefaults():
    assert model_ArchimateModel.setDefaults(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement())) == None

def test_model_ArchimateModel_getDefaultDiagramModel():
    assert model_ArchimateModel.getDefaultDiagramModel(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement())) == None

def test_model_ArchimateModel_getFolder():
    assert model_ArchimateModel.getFolder(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement()), '') == None

def test_model_ArchimateModel_getDiagramModels():
    assert model_ArchimateModel.getDiagramModels(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement())) == None

def test_model_ArchimateModel_getDefaultFolderForElement():
    assert model_ArchimateModel.getDefaultFolderForElement(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement()), '') == None

def test_model_ArchimateModel_addDerivedRelationsFolder():
    assert model_ArchimateModel.addDerivedRelationsFolder(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement())) == None

def test_model_ArchimateModel_removeDerivedRelationsFolder():
    assert model_ArchimateModel.removeDerivedRelationsFolder(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_ArchimateModelElement())) == None


from python_code import model_BorderObject

def test_model_BorderObject___init__():
    assert model_BorderObject.__init__(model_BorderObject(''), '') == None


from python_code import model_Cloneable

def test_model_Cloneable___init__():
    assert model_Cloneable.__init__(model_Cloneable()) == None

def test_model_Cloneable_getCopy():
    assert model_Cloneable.getCopy(model_Cloneable()) == None


from python_code import model_DiagramModel
from python_code import model_DiagramModelComponent
from python_code import model_DiagramModelReference

def test_model_DiagramModel___init__():
    assert model_DiagramModel.__init__(model_DiagramModel(0, model_DiagramModel=model_DiagramModelComponent(), model_DiagramModel12=model_DiagramModelReference()), 0, model_DiagramModel=model_DiagramModelComponent(), model_DiagramModel12=model_DiagramModelReference()) == None


from python_code import model_DiagramModelArchimateConnection
from python_code import model_Relationship

def test_model_DiagramModelArchimateConnection___init__():
    assert model_DiagramModelArchimateConnection.__init__(model_DiagramModelArchimateConnection(model_DiagramModelArchimateConnection=model_Relationship()), model_DiagramModelArchimateConnection=model_Relationship()) == None

def test_model_DiagramModelArchimateConnection_addRelationshipToModel():
    assert model_DiagramModelArchimateConnection.addRelationshipToModel(model_DiagramModelArchimateConnection(model_DiagramModelArchimateConnection=model_Relationship()), '') == None

def test_model_DiagramModelArchimateConnection_removeRelationshipFromModel():
    assert model_DiagramModelArchimateConnection.removeRelationshipFromModel(model_DiagramModelArchimateConnection(model_DiagramModelArchimateConnection=model_Relationship())) == None


from python_code import model_ArchimateElement
from python_code import model_DiagramModelArchimateObject

def test_model_DiagramModelArchimateObject___init__():
    assert model_DiagramModelArchimateObject.__init__(model_DiagramModelArchimateObject(0, model_DiagramModelArchimateObject=model_ArchimateElement()), 0, model_DiagramModelArchimateObject=model_ArchimateElement()) == None

def test_model_DiagramModelArchimateObject_addArchimateElementToModel():
    assert model_DiagramModelArchimateObject.addArchimateElementToModel(model_DiagramModelArchimateObject(0, model_DiagramModelArchimateObject=model_ArchimateElement()), 0) == None

def test_model_DiagramModelArchimateObject_removeArchimateElementFromModel():
    assert model_DiagramModelArchimateObject.removeArchimateElementFromModel(model_DiagramModelArchimateObject(0, model_DiagramModelArchimateObject=model_ArchimateElement())) == None


from python_code import model_DiagramModelImageProvider

def test_model_DiagramModelImageProvider___init__():
    assert model_DiagramModelImageProvider.__init__(model_DiagramModelImageProvider(''), '') == None


from python_code import model_Documentable

def test_model_Documentable___init__():
    assert model_Documentable.__init__(model_Documentable(''), '') == None


from python_code import model_Folder
from python_code import model_FolderContainer

def test_model_Folder___init__():
    assert model_Folder.__init__(model_Folder('', model_Folder=model_FolderContainer(), model_Folder4=set()), '', model_Folder=model_FolderContainer(), model_Folder4=set()) == None


from python_code import model_FontAttribute

def test_model_FontAttribute___init__():
    assert model_FontAttribute.__init__(model_FontAttribute('\x00\x00', '', 0, 0), '', '', 0, 0) == None

def test_model_FontAttribute_getDefaultTextAlignment():
    assert model_FontAttribute.getDefaultTextAlignment(model_FontAttribute('', '\x00', 0, 0)) == None


from python_code import model_Identifier

def test_model_Identifier___init__():
    assert model_Identifier.__init__(model_Identifier(''), '') == None


from python_code import model_InterfaceElement

def test_model_InterfaceElement___init__():
    assert model_InterfaceElement.__init__(model_InterfaceElement(0), 0) == None


from python_code import model_Lockable

def test_model_Lockable___init__():
    assert model_Lockable.__init__(model_Lockable(True), False) == None


from python_code import model_Nameable

def test_model_Nameable___init__():
    assert model_Nameable.__init__(model_Nameable(''), '') == None


from python_code import model_Properties
from python_code import model_Property

def test_model_Property___init__():
    assert model_Property.__init__(model_Property('', '\x00', model_Property=model_Properties()), '\x00\x00', '', model_Property=model_Properties()) == None


from python_code import model_SketchModel

def test_model_SketchModel___init__():
    assert model_SketchModel.__init__(model_SketchModel(0), 0) == None


from python_code import model_TextContent

def test_model_TextContent___init__():
    assert model_TextContent.__init__(model_TextContent(''), '') == None

