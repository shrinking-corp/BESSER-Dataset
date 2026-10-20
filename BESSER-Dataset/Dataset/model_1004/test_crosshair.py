from python_code import ZestGraph_GraphItem
from python_code import ZestGraph_ZestGraph

def test_ZestGraph_GraphItem___init__():
    assert ZestGraph_GraphItem.__init__(ZestGraph_GraphItem('', GraphItem=ZestGraph_ZestGraph(), items=ZestGraph_ZestGraph()), '', GraphItem=ZestGraph_ZestGraph(), items=ZestGraph_ZestGraph()) == None


from python_code import ZestGraph_NamedElement

def test_ZestGraph_NamedElement___init__():
    assert ZestGraph_NamedElement.__init__(ZestGraph_NamedElement(''), '') == None

