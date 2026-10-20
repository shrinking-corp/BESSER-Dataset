from python_code import relationworld_Category

def test_relationworld_Category___init__():
    assert relationworld_Category.__init__(relationworld_Category('', relationworld_Category17=set(), relationworld_Category=set(), relationworld_Category20=set()), '', relationworld_Category17=set(), relationworld_Category=set(), relationworld_Category20=set()) == None

def test_relationworld_Category_affectation():
    assert relationworld_Category.affectation(relationworld_Category('', relationworld_Category17=set(), relationworld_Category=set(), relationworld_Category20=set()), '', '') == None

def test_relationworld_Category_compare():
    assert relationworld_Category.compare(relationworld_Category('', relationworld_Category17=set(), relationworld_Category=set(), relationworld_Category20=set()), '', '') == None


from python_code import relationworld_NamedElement

def test_relationworld_NamedElement___init__():
    assert relationworld_NamedElement.__init__(relationworld_NamedElement(''), '') == None


from python_code import relationworld_World

def test_relationworld_World___init__():
    assert relationworld_World.__init__(relationworld_World(relationworld_World=set(), relationworld_World6=set(), relationworld_World9=set()), relationworld_World=set(), relationworld_World6=set(), relationworld_World9=set()) == None

def test_relationworld_World_affectation():
    assert relationworld_World.affectation(relationworld_World(relationworld_World=set(), relationworld_World6=set(), relationworld_World9=set()), '\x00', '') == None

def test_relationworld_World_compare():
    assert relationworld_World.compare(relationworld_World(relationworld_World=set(), relationworld_World6=set(), relationworld_World9=set()), '\x00', '') == None

