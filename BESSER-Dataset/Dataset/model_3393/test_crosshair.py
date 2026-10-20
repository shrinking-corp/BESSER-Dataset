from python_code import mindmap_CentralTopic
from python_code import mindmap_MindMap

def test_mindmap_MindMap___init__():
    assert mindmap_MindMap.__init__(mindmap_MindMap('', mindmap_MindMap=mindmap_CentralTopic()), '', mindmap_MindMap=mindmap_CentralTopic()) == None


from python_code import mindmap_Topic

def test_mindmap_Topic___init__():
    assert mindmap_Topic.__init__(mindmap_Topic('', 0), '', 0) == None

