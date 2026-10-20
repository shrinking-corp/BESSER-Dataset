from python_code import iotsystem_Action
from python_code import iotsystem_Rule

def test_iotsystem_Action___init__():
    assert iotsystem_Action.__init__(iotsystem_Action('', iotsystem_Action=iotsystem_Rule(), iotsystem_Action10=set()), '', iotsystem_Action=iotsystem_Rule(), iotsystem_Action10=set()) == None


from python_code import iotsystem_Condition
from python_code import iotsystem_Rule
from python_code import iotsystem_Sensor

def test_iotsystem_Condition___init__():
    assert iotsystem_Condition.__init__(iotsystem_Condition(0.0, '\x00\x00', iotsystem_Condition=iotsystem_Rule(), iotsystem_Condition19=iotsystem_Sensor()), 0.0, '', iotsystem_Condition=iotsystem_Rule(), iotsystem_Condition19=iotsystem_Sensor()) == None


from python_code import iotsystem_NamedElement

def test_iotsystem_NamedElement___init__():
    assert iotsystem_NamedElement.__init__(iotsystem_NamedElement(''), '') == None


from python_code import iotsystem_Device
from python_code import iotsystem_DigitalArtifact
from python_code import iotsystem_Resource

def test_iotsystem_Resource___init__():
    assert iotsystem_Resource.__init__(iotsystem_Resource('', '\x00', iotsystem_Resource=iotsystem_Device(), iotsystem_Resource2=iotsystem_DigitalArtifact()), '\x00\x00', '', iotsystem_Resource=iotsystem_Device(), iotsystem_Resource2=iotsystem_DigitalArtifact()) == None

