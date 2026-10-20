from python_code import model_Adapter

def test_model_Adapter___init__():
    assert model_Adapter.__init__(model_Adapter()) == None

def test_model_Adapter_setAdapter():
    assert model_Adapter.setAdapter(model_Adapter(), '', '') == None

def test_model_Adapter_getAdapter():
    assert model_Adapter.getAdapter(model_Adapter(), '') == None


from python_code import model_Attribute
from python_code import model_BasicObject
from python_code import model_BasicRelationship

def test_model_Attribute___init__():
    assert model_Attribute.__init__(model_Attribute(0, 0, model_Attribute=model_BasicObject(), model_Attribute47=model_BasicRelationship(), model_Attribute50=model_BasicObject()), 0, 0, model_Attribute=model_BasicObject(), model_Attribute47=model_BasicRelationship(), model_Attribute50=model_BasicObject()) == None


from python_code import model_BorderObject

def test_model_BorderObject___init__():
    assert model_BorderObject.__init__(model_BorderObject(''), '') == None


from python_code import model_Cloneable

def test_model_Cloneable___init__():
    assert model_Cloneable.__init__(model_Cloneable()) == None

def test_model_Cloneable_getCopy():
    assert model_Cloneable.getCopy(model_Cloneable()) == None


from python_code import model_DiagramModelImageProvider

def test_model_DiagramModelImageProvider___init__():
    assert model_DiagramModelImageProvider.__init__(model_DiagramModelImageProvider(''), '') == None


from python_code import model_BasicRelationship
from python_code import model_DiagramModelZentaConnection

def test_model_DiagramModelZentaConnection___init__():
    assert model_DiagramModelZentaConnection.__init__(model_DiagramModelZentaConnection(diagConnections=model_BasicRelationship(), DiagramModelZentaConnection=model_BasicRelationship()), diagConnections=model_BasicRelationship(), DiagramModelZentaConnection=model_BasicRelationship()) == None

def test_model_DiagramModelZentaConnection_addRelationshipToModel():
    assert model_DiagramModelZentaConnection.addRelationshipToModel(model_DiagramModelZentaConnection(diagConnections=model_BasicRelationship(), DiagramModelZentaConnection=model_BasicRelationship()), '') == None

def test_model_DiagramModelZentaConnection_removeRelationshipFromModel():
    assert model_DiagramModelZentaConnection.removeRelationshipFromModel(model_DiagramModelZentaConnection(diagConnections=model_BasicRelationship(), DiagramModelZentaConnection=model_BasicRelationship())) == None


from python_code import model_DiagramModelZentaObject
from python_code import model_ZentaElement

def test_model_DiagramModelZentaObject___init__():
    assert model_DiagramModelZentaObject.__init__(model_DiagramModelZentaObject(0, diagObjects=model_ZentaElement(), DiagramModelZentaObject=model_ZentaElement()), 0, diagObjects=model_ZentaElement(), DiagramModelZentaObject=model_ZentaElement()) == None

def test_model_DiagramModelZentaObject_addZentaElementToModel():
    assert model_DiagramModelZentaObject.addZentaElementToModel(model_DiagramModelZentaObject(0, diagObjects=model_ZentaElement(), DiagramModelZentaObject=model_ZentaElement()), 0) == None

def test_model_DiagramModelZentaObject_removeZentaElementFromModel():
    assert model_DiagramModelZentaObject.removeZentaElementFromModel(model_DiagramModelZentaObject(0, diagObjects=model_ZentaElement(), DiagramModelZentaObject=model_ZentaElement())) == None


from python_code import model_Documentable

def test_model_Documentable___init__():
    assert model_Documentable.__init__(model_Documentable(''), '') == None


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


from python_code import model_Folder
from python_code import model_Nameable

def test_model_Nameable___init__():
    assert model_Nameable.__init__(model_Nameable('', model_Nameable=model_Folder()), '', model_Nameable=model_Folder()) == None


from python_code import model_Properties
from python_code import model_Property

def test_model_Property___init__():
    assert model_Property.__init__(model_Property('', '', False, model_Property=model_Properties()), '\x00', '', False, model_Property=model_Properties()) == None


from python_code import model_SketchModel

def test_model_SketchModel___init__():
    assert model_SketchModel.__init__(model_SketchModel(0), 0) == None


from python_code import model_TextContent

def test_model_TextContent___init__():
    assert model_TextContent.__init__(model_TextContent(''), '') == None


from python_code import model_ZentaDiagramModel

def test_model_ZentaDiagramModel___init__():
    assert model_ZentaDiagramModel.__init__(model_ZentaDiagramModel(0), 0) == None


from python_code import model_ZentaModel
from python_code import model_ZentaModelElement

def test_model_ZentaModel___init__():
    assert model_ZentaModel.__init__(model_ZentaModel('', '\x00', model_ZentaModel=model_ZentaModelElement()), '\x00\x00', '', model_ZentaModel=model_ZentaModelElement()) == None

def test_model_ZentaModel_getDefaultDiagramModel():
    assert model_ZentaModel.getDefaultDiagramModel(model_ZentaModel('', '', model_ZentaModel=model_ZentaModelElement())) == None

def test_model_ZentaModel_getDefaultFolderForElement():
    assert model_ZentaModel.getDefaultFolderForElement(model_ZentaModel('', '', model_ZentaModel=model_ZentaModelElement()), '') == None

def test_model_ZentaModel_getDiagramModels():
    assert model_ZentaModel.getDiagramModels(model_ZentaModel('', '', model_ZentaModel=model_ZentaModelElement())) == None

