from python_code import remes_CompositeMode
from python_code import remes_ConditionalConnector
from python_code import remes_FromConditionalConnectorEdge
from python_code import remes_ToConditionalConnectorEdge

def test_remes_ConditionalConnector___init__():
    assert remes_ConditionalConnector.__init__(remes_ConditionalConnector('', ConditionalConnector=remes_CompositeMode(), connectTo8=set(), connectFrom10=set(), conditionalConnectors=remes_CompositeMode(), ConditionalConnector17=remes_FromConditionalConnectorEdge(), ConditionalConnector32=remes_ToConditionalConnectorEdge()), '', ConditionalConnector=remes_CompositeMode(), connectTo8=set(), connectFrom10=set(), conditionalConnectors=remes_CompositeMode(), ConditionalConnector17=remes_FromConditionalConnectorEdge(), ConditionalConnector32=remes_ToConditionalConnectorEdge()) == None


from python_code import remes_Edge

def test_remes_Edge___init__():
    assert remes_Edge.__init__(remes_Edge('', '\x00'), '\x00\x00', '') == None


from python_code import remes_InitEdge

def test_remes_InitEdge___init__():
    assert remes_InitEdge.__init__(remes_InitEdge(''), '') == None


from python_code import remes_Mode
from python_code import remes_RemesDiagram

def test_remes_Mode___init__():
    assert remes_Mode.__init__(remes_Mode('', '\x00', remes_Mode=remes_RemesDiagram()), '\x00\x00', '', remes_Mode=remes_RemesDiagram()) == None


from python_code import remes_CompositeMode
from python_code import remes_FromSubModeEdge
from python_code import remes_SubMode
from python_code import remes_ToSubModeEdge

def test_remes_SubMode___init__():
    assert remes_SubMode.__init__(remes_SubMode('', '', '', '', '\x00', SubMode=remes_CompositeMode(), SubMode20=remes_FromSubModeEdge(), connectTo23=set(), connectFrom25=set(), subModes=remes_CompositeMode(), SubMode35=remes_ToSubModeEdge()), '', '', '', '', '', SubMode=remes_CompositeMode(), SubMode20=remes_FromSubModeEdge(), connectTo23=set(), connectFrom25=set(), subModes=remes_CompositeMode(), SubMode35=remes_ToSubModeEdge()) == None

