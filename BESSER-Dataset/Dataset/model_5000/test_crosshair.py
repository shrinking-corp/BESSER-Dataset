from python_code import cloudml_core_ArtefactPort

def test_cloudml_core_ArtefactPort___init__():
    assert cloudml_core_ArtefactPort.__init__(cloudml_core_ArtefactPort(0, False), 0, False) == None


from python_code import cloudml_core_Artefact
from python_code import cloudml_core_ArtefactPortInstance
from python_code import cloudml_core_ClientPort

def test_cloudml_core_ClientPort___init__():
    assert cloudml_core_ClientPort.__init__(cloudml_core_ClientPort(True, ArtefactPort25=cloudml_core_ArtefactPortInstance(), ArtefactPort=cloudml_core_Artefact()), False, ArtefactPort25=cloudml_core_ArtefactPortInstance(), ArtefactPort=cloudml_core_Artefact()) == None


from python_code import cloudml_core_NamedElement

def test_cloudml_core_NamedElement___init__():
    assert cloudml_core_NamedElement.__init__(cloudml_core_NamedElement(''), '') == None


from python_code import Provider
from python_code import cloudml_core_Node

def test_cloudml_core_Node___init__():
    assert cloudml_core_Node.__init__(cloudml_core_Node(0, 0, 0, '', '', '', '', '', '', '', False, cloudml_core_Node=Provider()), 0, 0, 0, '', '', '', '', '', '', '', True, cloudml_core_Node=Provider()) == None


from python_code import Node
from python_code import cloudml_core_NodeInstance

def test_cloudml_core_NodeInstance___init__():
    assert cloudml_core_NodeInstance.__init__(cloudml_core_NodeInstance('', '\x00', cloudml_core_NodeInstance=Node()), '\x00\x00', '', cloudml_core_NodeInstance=Node()) == None


from python_code import cloudml_core_Property

def test_cloudml_core_Property___init__():
    assert cloudml_core_Property.__init__(cloudml_core_Property(''), '') == None


from python_code import cloudml_core_Provider

def test_cloudml_core_Provider___init__():
    assert cloudml_core_Provider.__init__(cloudml_core_Provider(''), '') == None


from python_code import cloudml_core_Resource

def test_cloudml_core_Resource___init__():
    assert cloudml_core_Resource.__init__(cloudml_core_Resource('', '', '', '', '', cloudml_core_Resource=set()), '', '', '', '\x00', '', cloudml_core_Resource=set()) == None


from python_code import cloudml_core_UploadCommand

def test_cloudml_core_UploadCommand___init__():
    assert cloudml_core_UploadCommand.__init__(cloudml_core_UploadCommand('', '\x00'), '\x00\x00', '') == None

