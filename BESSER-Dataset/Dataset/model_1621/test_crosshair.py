from python_code import pnw_Edge

def test_pnw_Edge___init__():
    assert pnw_Edge.__init__(pnw_Edge(0), 0) == None

from python_code import pnw_NamedElement

def test_pnw_NamedElement___init__():
    assert pnw_NamedElement.__init__(pnw_NamedElement(''), '') == None

from python_code import pnw_Net
from python_code import pnw_NetElement

def test_pnw_Net___init__():
    assert pnw_Net.__init__(pnw_Net('', net=set(), Net=pnw_NetElement()), '', net=set(), Net=pnw_NetElement()) == None

from python_code import pnw_PTEdge
from python_code import pnw_Place
from python_code import pnw_TPEdge

def test_pnw_Place___init__():
    assert pnw_Place.__init__(pnw_Place(0, fromPlace=set(), toPlace=set(), Place=pnw_TPEdge(), Place11=pnw_PTEdge()), 0, fromPlace=set(), toPlace=set(), Place=pnw_TPEdge(), Place11=pnw_PTEdge()) == None
