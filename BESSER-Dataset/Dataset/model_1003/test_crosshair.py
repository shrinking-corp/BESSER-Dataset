from python_code import dot_AttributeStatement

def test_dot_AttributeStatement___init__():
    assert dot_AttributeStatement.__init__(dot_AttributeStatement('', dot_AttributeStatement=set()), '', dot_AttributeStatement=set()) == None


from python_code import dot_Graph
from python_code import dot_GraphvizModel

def test_dot_Graph___init__():
    assert dot_Graph.__init__(dot_Graph(False, '', '', dot_Graph=dot_GraphvizModel(), dot_Graph2=set()), False, '', '', dot_Graph=dot_GraphvizModel(), dot_Graph2=set()) == None

