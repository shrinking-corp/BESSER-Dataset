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
    assert model_ArchimateDiagramModel.__init__(model_ArchimateDiagramModel(''), '') == None


from python_code import model_ArchimateModel
from python_code import model_Metadata

def test_model_ArchimateModel___init__():
    assert model_ArchimateModel.__init__(model_ArchimateModel('', '', '\x00\x00', model_ArchimateModel=model_Metadata()), '', '', '', model_ArchimateModel=model_Metadata()) == None

def test_model_ArchimateModel_getFolder():
    assert model_ArchimateModel.getFolder(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_Metadata()), '') == None

def test_model_ArchimateModel_setDefaults():
    assert model_ArchimateModel.setDefaults(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_Metadata())) == None

def test_model_ArchimateModel_getDefaultFolderForObject():
    assert model_ArchimateModel.getDefaultFolderForObject(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_Metadata()), '') == None

def test_model_ArchimateModel_getDiagramModels():
    assert model_ArchimateModel.getDiagramModels(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_Metadata())) == None

def test_model_ArchimateModel_getDefaultDiagramModel():
    assert model_ArchimateModel.getDefaultDiagramModel(model_ArchimateModel('', '', '\x00', model_ArchimateModel=model_Metadata())) == None


from python_code import model_ArchimateModelObject

def test_model_ArchimateModelObject___init__():
    assert model_ArchimateModelObject.__init__(model_ArchimateModelObject()) == None

def test_model_ArchimateModelObject_getArchimateModel():
    assert model_ArchimateModelObject.getArchimateModel(model_ArchimateModelObject()) == None


from python_code import model_ArchimateConcept
from python_code import model_ArchimateRelationship
from python_code import model_DiagramModelArchimateConnection

def test_model_ArchimateRelationship___init__():
    assert model_ArchimateRelationship.__init__(model_ArchimateRelationship(model_ArchimateRelationship=model_ArchimateConcept(), model_ArchimateRelationship9=model_ArchimateConcept(), model_ArchimateRelationship31=model_DiagramModelArchimateConnection()), model_ArchimateRelationship=model_ArchimateConcept(), model_ArchimateRelationship9=model_ArchimateConcept(), model_ArchimateRelationship31=model_DiagramModelArchimateConnection()) == None

def test_model_ArchimateRelationship_reconnect():
    assert model_ArchimateRelationship.reconnect(model_ArchimateRelationship(model_ArchimateRelationship=model_ArchimateConcept(), model_ArchimateRelationship9=model_ArchimateConcept(), model_ArchimateRelationship31=model_DiagramModelArchimateConnection())) == None

def test_model_ArchimateRelationship_disconnect():
    assert model_ArchimateRelationship.disconnect(model_ArchimateRelationship(model_ArchimateRelationship=model_ArchimateConcept(), model_ArchimateRelationship9=model_ArchimateConcept(), model_ArchimateRelationship31=model_DiagramModelArchimateConnection())) == None

def test_model_ArchimateRelationship_connect():
    assert model_ArchimateRelationship.connect(model_ArchimateRelationship(model_ArchimateRelationship=model_ArchimateConcept(), model_ArchimateRelationship9=model_ArchimateConcept(), model_ArchimateRelationship31=model_DiagramModelArchimateConnection()), '', '') == None


from python_code import model_AssociationRelationship

def test_model_AssociationRelationship___init__():
    assert model_AssociationRelationship.__init__(model_AssociationRelationship(True), False) == None


from python_code import model_BorderObject

def test_model_BorderObject___init__():
    assert model_BorderObject.__init__(model_BorderObject(''), '') == None


from python_code import model_BorderType

def test_model_BorderType___init__():
    assert model_BorderType.__init__(model_BorderType(0), 0) == None


from python_code import model_Cloneable

def test_model_Cloneable___init__():
    assert model_Cloneable.__init__(model_Cloneable()) == None

def test_model_Cloneable_getCopy():
    assert model_Cloneable.getCopy(model_Cloneable()) == None


from python_code import model_DiagramModel
from python_code import model_DiagramModelReference

def test_model_DiagramModel___init__():
    assert model_DiagramModel.__init__(model_DiagramModel(0, model_DiagramModel=model_DiagramModelReference()), 0, model_DiagramModel=model_DiagramModelReference()) == None


from python_code import model_DiagramModelArchimateComponent

def test_model_DiagramModelArchimateComponent___init__():
    assert model_DiagramModelArchimateComponent.__init__(model_DiagramModelArchimateComponent()) == None

def test_model_DiagramModelArchimateComponent_getArchimateConcept():
    assert model_DiagramModelArchimateComponent.getArchimateConcept(model_DiagramModelArchimateComponent()) == None

def test_model_DiagramModelArchimateComponent_removeArchimateConceptFromModel():
    assert model_DiagramModelArchimateComponent.removeArchimateConceptFromModel(model_DiagramModelArchimateComponent()) == None

def test_model_DiagramModelArchimateComponent_addArchimateConceptToModel():
    assert model_DiagramModelArchimateComponent.addArchimateConceptToModel(model_DiagramModelArchimateComponent(), '') == None

def test_model_DiagramModelArchimateComponent_setArchimateConcept():
    assert model_DiagramModelArchimateComponent.setArchimateConcept(model_DiagramModelArchimateComponent(), '') == None


from python_code import model_ArchimateElement
from python_code import model_DiagramModelArchimateObject

def test_model_DiagramModelArchimateObject___init__():
    assert model_DiagramModelArchimateObject.__init__(model_DiagramModelArchimateObject(0, model_DiagramModelArchimateObject=model_ArchimateElement()), 0, model_DiagramModelArchimateObject=model_ArchimateElement()) == None


from python_code import model_DiagramModelComponent

def test_model_DiagramModelComponent___init__():
    assert model_DiagramModelComponent.__init__(model_DiagramModelComponent()) == None

def test_model_DiagramModelComponent_getDiagramModel():
    assert model_DiagramModelComponent.getDiagramModel(model_DiagramModelComponent()) == None


from python_code import model_DiagramModelImageProvider

def test_model_DiagramModelImageProvider___init__():
    assert model_DiagramModelImageProvider.__init__(model_DiagramModelImageProvider(''), '') == None


from python_code import model_Documentable

def test_model_Documentable___init__():
    assert model_Documentable.__init__(model_Documentable(''), '') == None


from python_code import model_Feature
from python_code import model_Features

def test_model_Feature___init__():
    assert model_Feature.__init__(model_Feature('', '\x00', model_Feature=model_Features()), '\x00\x00', '', model_Feature=model_Features()) == None


from python_code import model_Folder
from python_code import model_FolderContainer

def test_model_Folder___init__():
    assert model_Folder.__init__(model_Folder('', model_Folder=model_FolderContainer(), model_Folder6=set()), '', model_Folder=model_FolderContainer(), model_Folder6=set()) == None


from python_code import model_FontAttribute

def test_model_FontAttribute___init__():
    assert model_FontAttribute.__init__(model_FontAttribute('', '\x00'), '\x00\x00', '') == None


from python_code import model_Identifier

def test_model_Identifier___init__():
    assert model_Identifier.__init__(model_Identifier(''), '') == None


from python_code import model_InfluenceRelationship

def test_model_InfluenceRelationship___init__():
    assert model_InfluenceRelationship.__init__(model_InfluenceRelationship(''), '') == None


from python_code import model_Junction

def test_model_Junction___init__():
    assert model_Junction.__init__(model_Junction(''), '') == None


from python_code import model_LineObject

def test_model_LineObject___init__():
    assert model_LineObject.__init__(model_LineObject(0, '\x00'), 0, '\x00') == None


from python_code import model_Lockable

def test_model_Lockable___init__():
    assert model_Lockable.__init__(model_Lockable(True), False) == None


from python_code import model_Nameable

def test_model_Nameable___init__():
    assert model_Nameable.__init__(model_Nameable(''), '') == None


from python_code import model_Metadata
from python_code import model_Properties
from python_code import model_Property

def test_model_Property___init__():
    assert model_Property.__init__(model_Property('', '\x00', model_Property3=model_Metadata(), model_Property=model_Properties()), '\x00\x00', '', model_Property3=model_Metadata(), model_Property=model_Properties()) == None


from python_code import model_SketchModel

def test_model_SketchModel___init__():
    assert model_SketchModel.__init__(model_SketchModel(0), 0) == None


from python_code import model_TextAlignment

def test_model_TextAlignment___init__():
    assert model_TextAlignment.__init__(model_TextAlignment(0), 0) == None


from python_code import model_TextContent

def test_model_TextContent___init__():
    assert model_TextContent.__init__(model_TextContent(''), '') == None


from python_code import model_TextPosition

def test_model_TextPosition___init__():
    assert model_TextPosition.__init__(model_TextPosition(0), 0) == None

