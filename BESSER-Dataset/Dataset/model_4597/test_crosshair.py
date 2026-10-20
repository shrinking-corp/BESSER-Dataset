from python_code import dot_a_list
from python_code import dot_attr_list

def test_dot_a_list___init__():
    assert dot_a_list.__init__(dot_a_list('', '\x00', dot_a_list=dot_attr_list()), '\x00\x00', '', dot_a_list=dot_attr_list()) == None


from python_code import dot_attr_stmt

def test_dot_attr_stmt___init__():
    assert dot_attr_stmt.__init__(dot_attr_stmt('', dot_attr_stmt=set()), '', dot_attr_stmt=set()) == None


from python_code import dot_attribute

def test_dot_attribute___init__():
    assert dot_attribute.__init__(dot_attribute('', '\x00'), '\x00\x00', '') == None


from python_code import dot_edgeRHS
from python_code import dot_edge_stmt_node
from python_code import dot_edge_stmt_subgraph

def test_dot_edgeRHS___init__():
    assert dot_edgeRHS.__init__(dot_edgeRHS('', dot_edgeRHS=dot_edge_stmt_node(), dot_edgeRHS11=dot_edge_stmt_subgraph()), '', dot_edgeRHS=dot_edge_stmt_node(), dot_edgeRHS11=dot_edge_stmt_subgraph()) == None


from python_code import dot_graph
from python_code import dot_graphvizmodel

def test_dot_graph___init__():
    assert dot_graph.__init__(dot_graph('', '', False, dot_graph2=set(), dot_graph=dot_graphvizmodel()), '', '', True, dot_graph2=set(), dot_graph=dot_graphvizmodel()) == None


from python_code import dot_edgeRHS_node
from python_code import dot_edge_stmt_node
from python_code import dot_node_id

def test_dot_node_id___init__():
    assert dot_node_id.__init__(dot_node_id('', dot_node_id=dot_edge_stmt_node(), dot_node_id25=dot_edgeRHS_node()), '', dot_node_id=dot_edge_stmt_node(), dot_node_id25=dot_edgeRHS_node()) == None


from python_code import dot_node_stmt

def test_dot_node_stmt___init__():
    assert dot_node_stmt.__init__(dot_node_stmt('', dot_node_stmt=set()), '', dot_node_stmt=set()) == None


from python_code import dot_edgeRHS_subgraph
from python_code import dot_edge_stmt_subgraph
from python_code import dot_subgraph

def test_dot_subgraph___init__():
    assert dot_subgraph.__init__(dot_subgraph('', dot_subgraph22=set(), dot_subgraph=dot_edge_stmt_subgraph(), dot_subgraph27=dot_edgeRHS_subgraph()), '', dot_subgraph22=set(), dot_subgraph=dot_edge_stmt_subgraph(), dot_subgraph27=dot_edgeRHS_subgraph()) == None

