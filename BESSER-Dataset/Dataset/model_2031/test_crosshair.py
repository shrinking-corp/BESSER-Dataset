from python_code import ioT_metamodel_AtomicData
from python_code import ioT_metamodel_AtomicDataAttributes

def test_ioT_metamodel_AtomicDataAttributes___init__():
    assert ioT_metamodel_AtomicDataAttributes.__init__(ioT_metamodel_AtomicDataAttributes('', '\x00', ioT_metamodel_AtomicDataAttributes=ioT_metamodel_AtomicData()), '\x00\x00', '', ioT_metamodel_AtomicDataAttributes=ioT_metamodel_AtomicData()) == None


from python_code import ioT_metamodel_Attribute
from python_code import ioT_metamodel_InformationResource

def test_ioT_metamodel_Attribute___init__():
    assert ioT_metamodel_Attribute.__init__(ioT_metamodel_Attribute('', '\x00', ioT_metamodel_Attribute=ioT_metamodel_InformationResource()), '\x00\x00', '', ioT_metamodel_Attribute=ioT_metamodel_InformationResource()) == None


from python_code import ioT_metamodel_Container
from python_code import ioT_metamodel_FogNode
from python_code import ioT_metamodel_Fog_Services
from python_code import ioT_metamodel_Operations

def test_ioT_metamodel_Container___init__():
    assert ioT_metamodel_Container.__init__(ioT_metamodel_Container('', '\x00', ioT_metamodel_Container=ioT_metamodel_FogNode(), ioT_metamodel_Container113=ioT_metamodel_Fog_Services(), ioT_metamodel_Container129=ioT_metamodel_Operations()), '\x00\x00', '', ioT_metamodel_Container=ioT_metamodel_FogNode(), ioT_metamodel_Container113=ioT_metamodel_Fog_Services(), ioT_metamodel_Container129=ioT_metamodel_Operations()) == None


from python_code import ioT_metamodel_DataStreamAttributes
from python_code import ioT_metamodel_DataStreams

def test_ioT_metamodel_DataStreamAttributes___init__():
    assert ioT_metamodel_DataStreamAttributes.__init__(ioT_metamodel_DataStreamAttributes('', '', '', '', '', '', '', ioT_metamodel_DataStreamAttributes=ioT_metamodel_DataStreams()), '', '\x00', '', '', '', '', '', ioT_metamodel_DataStreamAttributes=ioT_metamodel_DataStreams()) == None


from python_code import ioT_metamodel_Tag

def test_ioT_metamodel_Tag___init__():
    assert ioT_metamodel_Tag.__init__(ioT_metamodel_Tag('', ioT_metamodel_Tag=set()), '', ioT_metamodel_Tag=set()) == None

