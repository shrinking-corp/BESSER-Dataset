from python_code import network_AbstractElement

def test_network_AbstractElement___init__():
    assert network_AbstractElement.__init__(network_AbstractElement(''), '') == None


from python_code import network_Network
from python_code import network_RunTimeNetwork

def test_network_RunTimeNetwork___init__():
    assert network_RunTimeNetwork.__init__(network_RunTimeNetwork(network_RunTimeNetwork=network_Network(), network_RunTimeNetwork22=set(), network_RunTimeNetwork24=set()), network_RunTimeNetwork=network_Network(), network_RunTimeNetwork22=set(), network_RunTimeNetwork24=set()) == None

def test_network_RunTimeNetwork_makeStep():
    assert network_RunTimeNetwork.makeStep(network_RunTimeNetwork(network_RunTimeNetwork=network_Network(), network_RunTimeNetwork22=set(), network_RunTimeNetwork24=set())) == None

def test_network_RunTimeNetwork_initialize():
    assert network_RunTimeNetwork.initialize(network_RunTimeNetwork(network_RunTimeNetwork=network_Network(), network_RunTimeNetwork22=set(), network_RunTimeNetwork24=set())) == None

