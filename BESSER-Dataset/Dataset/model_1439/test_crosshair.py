from python_code import mention_graph_HashTag
from python_code import mention_graph_User

def test_mention_graph_HashTag___init__():
    assert mention_graph_HashTag.__init__(mention_graph_HashTag(0, mention_graph_HashTag=mention_graph_User()), 0, mention_graph_HashTag=mention_graph_User()) == None


from python_code import mention_graph_Edge
from python_code import mention_graph_MentionGraph
from python_code import mention_graph_Node

def test_mention_graph_Node___init__():
    assert mention_graph_Node.__init__(mention_graph_Node('', mention_graph_Node=mention_graph_MentionGraph(), mention_graph_Node6=mention_graph_Edge(), mention_graph_Node9=mention_graph_Edge()), '', mention_graph_Node=mention_graph_MentionGraph(), mention_graph_Node6=mention_graph_Edge(), mention_graph_Node9=mention_graph_Edge()) == None

