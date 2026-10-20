from python_code import dot_AssignmentStatement

def test_dot_AssignmentStatement___init__():
    assert dot_AssignmentStatement.__init__(dot_AssignmentStatement('', '\x00'), '\x00\x00', '') == None


from python_code import dot_Attributable
from python_code import dot_AttributeList

def test_dot_Attributable___init__():
    assert dot_Attributable.__init__(dot_Attributable(dot_Attributable=dot_AttributeList()), dot_Attributable=dot_AttributeList()) == None

def test_dot_Attributable_getAllALists():
    assert dot_Attributable.getAllALists(dot_Attributable(dot_Attributable=dot_AttributeList())) == None


from python_code import dot_AttributeStatement

def test_dot_AttributeStatement___init__():
    assert dot_AttributeStatement.__init__(dot_AttributeStatement(''), '') == None


from python_code import dot_Commentable

def test_dot_Commentable___init__():
    assert dot_Commentable.__init__(dot_Commentable(''), '') == None


from python_code import dot_Graph

def test_dot_Graph___init__():
    assert dot_Graph.__init__(dot_Graph('', '\x00'), '\x00\x00', '') == None

def test_dot_Graph_getAllStatements():
    assert dot_Graph.getAllStatements(dot_Graph('', '')) == None


from python_code import dot_Identifiable

def test_dot_Identifiable___init__():
    assert dot_Identifiable.__init__(dot_Identifiable(''), '') == None


from python_code import dot_NodeID
from python_code import dot_Port

def test_dot_Port___init__():
    assert dot_Port.__init__(dot_Port('', dot_Port=dot_NodeID()), '', dot_Port=dot_NodeID()) == None


from python_code import dot_StrictIdentifiable

def test_dot_StrictIdentifiable___init__():
    assert dot_StrictIdentifiable.__init__(dot_StrictIdentifiable(''), '') == None


from python_code import dot_Subgraph

def test_dot_Subgraph___init__():
    assert dot_Subgraph.__init__(dot_Subgraph(''), '') == None

