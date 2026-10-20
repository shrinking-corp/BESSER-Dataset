from python_code import ACADEMIC_PAGE

def test_ACADEMIC_PAGE___init__():
    assert ACADEMIC_PAGE.__init__(ACADEMIC_PAGE('\x00\x00', '', lineItems0=set()), '', '', lineItems0=set()) == None


from python_code import Database_system

def test_Database_system___init__():
    assert Database_system.__init__(Database_system(True), False) == None


from python_code import PLACEMENTS_PAGE

def test_PLACEMENTS_PAGE___init__():
    assert PLACEMENTS_PAGE.__init__(PLACEMENTS_PAGE(0, '', '\x00\x00'), 0, '', '') == None


from python_code import WebUser

def test_WebUser___init__():
    assert WebUser.__init__(WebUser('', '', '\x00\x00'), '', '', '') == None


from python_code import Welcome

def test_Welcome___init__():
    assert Welcome.__init__(Welcome('', '', '\x00\x00'), '', '', '') == None

