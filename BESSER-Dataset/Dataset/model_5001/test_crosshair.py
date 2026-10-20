from python_code import cloudml_Artefact
from python_code import cloudml_ArtefactPort
from python_code import cloudml_ArtefactPortInstance

def test_cloudml_ArtefactPort___init__():
    assert cloudml_ArtefactPort.__init__(cloudml_ArtefactPort(0, False, cloudml_ArtefactPort=cloudml_Artefact(), cloudml_ArtefactPort28=cloudml_ArtefactPortInstance()), 0, False, cloudml_ArtefactPort=cloudml_Artefact(), cloudml_ArtefactPort28=cloudml_ArtefactPortInstance()) == None


from python_code import cloudml_Artefact
from python_code import cloudml_Binding
from python_code import cloudml_ClientPort

def test_cloudml_ClientPort___init__():
    assert cloudml_ClientPort.__init__(cloudml_ClientPort(True, cloudml_ClientPort=cloudml_Artefact(), cloudml_ClientPort46=cloudml_Binding()), False, cloudml_ClientPort=cloudml_Artefact(), cloudml_ClientPort46=cloudml_Binding()) == None


from python_code import cloudml_NamedElement

def test_cloudml_NamedElement___init__():
    assert cloudml_NamedElement.__init__(cloudml_NamedElement(''), '') == None


from python_code import cloudml_Property
from python_code import cloudml_WithProperties

def test_cloudml_Property___init__():
    assert cloudml_Property.__init__(cloudml_Property('', cloudml_Property=cloudml_WithProperties()), '', cloudml_Property=cloudml_WithProperties()) == None


from python_code import cloudml_Artefact
from python_code import cloudml_Binding
from python_code import cloudml_Resource

def test_cloudml_Resource___init__():
    assert cloudml_Resource.__init__(cloudml_Resource('', '', '', '', '', cloudml_Resource19=cloudml_Artefact(), cloudml_Resource=set(), cloudml_Resource52=cloudml_Binding(), cloudml_Resource55=cloudml_Binding()), '', '', '', '\x00', '', cloudml_Resource19=cloudml_Artefact(), cloudml_Resource=set(), cloudml_Resource52=cloudml_Binding(), cloudml_Resource55=cloudml_Binding()) == None

