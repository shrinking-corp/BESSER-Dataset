from python_code import scxml_InitialState
from python_code import scxml_Script
from python_code import scxml_ServiceTemplate

def test_scxml_ServiceTemplate___init__():
    assert scxml_ServiceTemplate.__init__(scxml_ServiceTemplate('', '', '', '', '\x00', scxml_ServiceTemplate30=set(), scxml_ServiceTemplate33=scxml_InitialState(), scxml_ServiceTemplate36=set(), scxml_ServiceTemplate39=set(), scxml_ServiceTemplate42=set(), scxml_ServiceTemplate45=scxml_Script(), scxml_ServiceTemplate=set()), '', '', '', '', '', scxml_ServiceTemplate30=set(), scxml_ServiceTemplate33=scxml_InitialState(), scxml_ServiceTemplate36=set(), scxml_ServiceTemplate39=set(), scxml_ServiceTemplate42=set(), scxml_ServiceTemplate45=scxml_Script(), scxml_ServiceTemplate=set()) == None

