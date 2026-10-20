from python_code import MMInterModel_Element

def test_MMInterModel_Element___init__():
    assert MMInterModel_Element.__init__(MMInterModel_Element('', '\x00'), '\x00\x00', '') == None

