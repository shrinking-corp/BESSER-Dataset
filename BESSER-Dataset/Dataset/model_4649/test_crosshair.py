from python_code import di_Container

def test_di_Container___init__():
    assert di_Container.__init__(di_Container('', '', di_Container=set(), di_Container8=set()), '', '', di_Container=set(), di_Container8=set()) == None


from python_code import di_GradientShape

def test_di_GradientShape___init__():
    assert di_GradientShape.__init__(di_GradientShape(0, False, False), 0, False, False) == None


from python_code import di_CommentLink
from python_code import di_Connector
from python_code import di_Node

def test_di_Node___init__():
    assert di_Node.__init__(di_Node('', '', source=set(), target=set(), source3=set(), Node21=di_Connector(), Node=di_Connector(), Node28=di_CommentLink()), '', '', source=set(), target=set(), source3=set(), Node21=di_Connector(), Node=di_Connector(), Node28=di_CommentLink()) == None

