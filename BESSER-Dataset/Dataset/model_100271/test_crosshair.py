from python_code import Grafcet_LocatedElement

def test_Grafcet_LocatedElement___init__():
    assert Grafcet_LocatedElement.__init__(Grafcet_LocatedElement(''), '') == None


from python_code import Grafcet_NamedElement

def test_Grafcet_NamedElement___init__():
    assert Grafcet_NamedElement.__init__(Grafcet_NamedElement(''), '') == None


from python_code import Grafcet_Grafcet
from python_code import Grafcet_Step

def test_Grafcet_Step___init__():
    assert Grafcet_Step.__init__(Grafcet_Step('', '', '', to=set(), from_=set(), Element=Grafcet_Grafcet()), '', '', '', to=set(), from_=set(), Element=Grafcet_Grafcet()) == None


from python_code import Grafcet_Grafcet
from python_code import Grafcet_Transition

def test_Grafcet_Transition___init__():
    assert Grafcet_Transition.__init__(Grafcet_Transition('', to7=set(), from_10=set(), Element=Grafcet_Grafcet()), '', to7=set(), from_10=set(), Element=Grafcet_Grafcet()) == None

