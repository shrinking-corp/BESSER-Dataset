from python_code import family_FNamedElement

def test_family_FNamedElement___init__():
    assert family_FNamedElement.__init__(family_FNamedElement(''), '') == None


from python_code import family_Family
from python_code import family_Person

def test_family_Person___init__():
    assert family_Person.__init__(family_Person(0, '\x00', family_Person=family_Family()), 0, '\x00', family_Person=family_Family()) == None

