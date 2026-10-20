from python_code import ref_D
from python_code import ref_E

def test_ref_E___init__():
    assert ref_E.__init__(ref_E('', '', '', E=ref_D(), e=set()), '', '', '', E=ref_D(), e=set()) == None


from python_code import ref_unsettable_EU

def test_ref_unsettable_EU___init__():
    assert ref_unsettable_EU.__init__(ref_unsettable_EU('', '', '', eu=set()), '', '', '', eu=set()) == None

