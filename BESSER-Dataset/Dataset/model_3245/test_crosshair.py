from python_code import remes_CompositeMode
from python_code import remes_ConditionalConnector
from python_code import remes_FromConditionalConnectorEdge
from python_code import remes_ToConditionalConnectorEdge

def test_remes_ConditionalConnector___init__():
    assert remes_ConditionalConnector.__init__(remes_ConditionalConnector('', ConditionalConnector35=remes_ToConditionalConnectorEdge(), ConditionalConnector=remes_CompositeMode(), connectTo8=set(), connectFrom10=set(), conditionalConnectors=remes_CompositeMode(), ConditionalConnector17=remes_FromConditionalConnectorEdge()), '', ConditionalConnector35=remes_ToConditionalConnectorEdge(), ConditionalConnector=remes_CompositeMode(), connectTo8=set(), connectFrom10=set(), conditionalConnectors=remes_CompositeMode(), ConditionalConnector17=remes_FromConditionalConnectorEdge()) == None


from python_code import remes_Edge

def test_remes_Edge___init__():
    assert remes_Edge.__init__(remes_Edge('', '\x00'), '\x00\x00', '') == None


from python_code import remes_InitEdge

def test_remes_InitEdge___init__():
    assert remes_InitEdge.__init__(remes_InitEdge(''), '') == None

