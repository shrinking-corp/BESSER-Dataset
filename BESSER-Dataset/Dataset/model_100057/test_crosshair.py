from python_code import sistedesMM_Edition
from python_code import sistedesMM_SistedesMember

def test_sistedesMM_Edition___init__():
    assert sistedesMM_Edition.__init__(sistedesMM_Edition(0, '\x00', sistedesMM_Edition=sistedesMM_SistedesMember()), 0, '\x00', sistedesMM_Edition=sistedesMM_SistedesMember()) == None


from python_code import sistedesMM_Person
from python_code import sistedesMM_Publication

def test_sistedesMM_Person___init__():
    assert sistedesMM_Person.__init__(sistedesMM_Person('', '', '', '', Person=sistedesMM_Publication(), sistedesMM_Person=set(), authors=set()), '', '', '\x00', '', Person=sistedesMM_Publication(), sistedesMM_Person=set(), authors=set()) == None

