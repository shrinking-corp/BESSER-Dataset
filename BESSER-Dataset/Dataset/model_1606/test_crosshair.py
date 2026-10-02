from python_code import pn_NamedElement

def test_pn_NamedElement___init__():
    assert pn_NamedElement.__init__(pn_NamedElement(''), '') == None

from python_code import pn_Net
from python_code import pn_NetElement

def test_pn_Net___init__():
    assert pn_Net.__init__(pn_Net('', net=set(), Net=pn_NetElement()), '', net=set(), Net=pn_NetElement()) == None

from python_code import pn_Place
from python_code import pn_Transition

def test_pn_Place___init__():
    assert pn_Place.__init__(pn_Place(0, Place=pn_Transition(), Place4=pn_Transition(), srcP2T=set(), trgT2P=set()), 0, Place=pn_Transition(), Place4=pn_Transition(), srcP2T=set(), trgT2P=set()) == None
