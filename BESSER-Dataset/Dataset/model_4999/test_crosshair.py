from python_code import cloudml_core_NamedElement

def test_cloudml_core_NamedElement___init__():
    assert cloudml_core_NamedElement.__init__(cloudml_core_NamedElement(''), '') == None


from python_code import Provider
from python_code import cloudml_core_Node

def test_cloudml_core_Node___init__():
    assert cloudml_core_Node.__init__(cloudml_core_Node(0, 0, 0, '', '', '', '', '', '\x00', '', False, cloudml_core_Node25=Provider(), cloudml_core_Node=set()), 0, 0, 0, '', '', '', '', '', '', '', False, cloudml_core_Node25=Provider(), cloudml_core_Node=set()) == None


from python_code import NodeInstance
from python_code import cloudml_core_NodeInstance

def test_cloudml_core_NodeInstance___init__():
    assert cloudml_core_NodeInstance.__init__(cloudml_core_NodeInstance('', cloudml_core_NodeInstance=NodeInstance(), cloudml_core_NodeInstance48=set()), '', cloudml_core_NodeInstance=NodeInstance(), cloudml_core_NodeInstance48=set()) == None


from python_code import cloudml_core_Property

def test_cloudml_core_Property___init__():
    assert cloudml_core_Property.__init__(cloudml_core_Property(''), '') == None


from python_code import cloudml_core_Provider

def test_cloudml_core_Provider___init__():
    assert cloudml_core_Provider.__init__(cloudml_core_Provider('', '\x00'), '\x00\x00', '') == None


from python_code import cloudml_core_Resource

def test_cloudml_core_Resource___init__():
    assert cloudml_core_Resource.__init__(cloudml_core_Resource('', '\x00'), '\x00\x00', '') == None

