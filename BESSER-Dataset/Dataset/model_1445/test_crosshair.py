from python_code import graph_EMapPropertyHolder
from python_code import graph_ElkPropertyToValueMapEntry

def test_graph_ElkPropertyToValueMapEntry___init__():
    assert graph_ElkPropertyToValueMapEntry.__init__(graph_ElkPropertyToValueMapEntry('', '\x00', graph_ElkPropertyToValueMapEntry=graph_EMapPropertyHolder()), '\x00\x00', '', graph_ElkPropertyToValueMapEntry=graph_EMapPropertyHolder()) == None


from python_code import graph_ElkShape

def test_graph_ElkShape___init__():
    assert graph_ElkShape.__init__(graph_ElkShape(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None

def test_graph_ElkShape_setDimensions():
    assert graph_ElkShape.setDimensions(graph_ElkShape(0.0, 0.0, 0.0, 0.0), 0, 0) == None

def test_graph_ElkShape_setLocation():
    assert graph_ElkShape.setLocation(graph_ElkShape(0.0, 0.0, 0.0, 0.0), 0, 0) == None


from python_code import graph_IPropertyHolder

def test_graph_IPropertyHolder___init__():
    assert graph_IPropertyHolder.__init__(graph_IPropertyHolder()) == None

def test_graph_IPropertyHolder_setProperty():
    assert graph_IPropertyHolder.setProperty(graph_IPropertyHolder(), '', '') == None

def test_graph_IPropertyHolder_hasProperty():
    assert graph_IPropertyHolder.hasProperty(graph_IPropertyHolder(), '') == None

def test_graph_IPropertyHolder_getProperty():
    assert graph_IPropertyHolder.getProperty(graph_IPropertyHolder(), '') == None

def test_graph_IPropertyHolder_getAllProperties():
    assert graph_IPropertyHolder.getAllProperties(graph_IPropertyHolder()) == None

def test_graph_IPropertyHolder_copyProperties():
    assert graph_IPropertyHolder.copyProperties(graph_IPropertyHolder(), '') == None

