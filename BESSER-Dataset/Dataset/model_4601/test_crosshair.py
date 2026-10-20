from python_code import gv_AssignmentStatement

def test_gv_AssignmentStatement___init__():
    assert gv_AssignmentStatement.__init__(gv_AssignmentStatement('', '\x00'), '\x00\x00', '') == None


from python_code import gv_AList
from python_code import gv_Attribute

def test_gv_Attribute___init__():
    assert gv_Attribute.__init__(gv_Attribute('', '\x00', gv_Attribute=gv_AList()), '\x00\x00', '', gv_Attribute=gv_AList()) == None


from python_code import gv_AttributeList
from python_code import gv_AttributeStatement

def test_gv_AttributeStatement___init__():
    assert gv_AttributeStatement.__init__(gv_AttributeStatement('', gv_AttributeStatement=gv_AttributeList()), '', gv_AttributeStatement=gv_AttributeList()) == None


from python_code import gv_Commentable

def test_gv_Commentable___init__():
    assert gv_Commentable.__init__(gv_Commentable(''), '') == None


from python_code import gv_Graph

def test_gv_Graph___init__():
    assert gv_Graph.__init__(gv_Graph('', '\x00'), '\x00\x00', '') == None


from python_code import gv_Identifiable

def test_gv_Identifiable___init__():
    assert gv_Identifiable.__init__(gv_Identifiable(''), '') == None


from python_code import gv_NodeID
from python_code import gv_Port

def test_gv_Port___init__():
    assert gv_Port.__init__(gv_Port('', gv_Port=gv_NodeID()), '', gv_Port=gv_NodeID()) == None


from python_code import gv_StrictIdentifiable

def test_gv_StrictIdentifiable___init__():
    assert gv_StrictIdentifiable.__init__(gv_StrictIdentifiable(''), '') == None


from python_code import gv_Subgraph

def test_gv_Subgraph___init__():
    assert gv_Subgraph.__init__(gv_Subgraph(''), '') == None

