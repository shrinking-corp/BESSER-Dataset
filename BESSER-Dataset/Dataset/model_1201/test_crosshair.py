from python_code import ACG_BooleanExp

def test_ACG_BooleanExp___init__():
    assert ACG_BooleanExp.__init__(ACG_BooleanExp(''), '') == None


from python_code import ACG_IntegerExp

def test_ACG_IntegerExp___init__():
    assert ACG_IntegerExp.__init__(ACG_IntegerExp(''), '') == None


from python_code import ACG_LocatedElement

def test_ACG_LocatedElement___init__():
    assert ACG_LocatedElement.__init__(ACG_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import ACG_StringExp

def test_ACG_StringExp___init__():
    assert ACG_StringExp.__init__(ACG_StringExp(''), '') == None


from python_code import ACG_VariableDecl

def test_ACG_VariableDecl___init__():
    assert ACG_VariableDecl.__init__(ACG_VariableDecl(''), '') == None

