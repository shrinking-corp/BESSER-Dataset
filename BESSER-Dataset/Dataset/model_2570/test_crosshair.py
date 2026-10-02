from python_code import testpackage_Group

def test_testpackage_Group___init__():
    assert testpackage_Group.__init__(testpackage_Group('', testpackage_Group=set()), '', testpackage_Group=set()) == None

def test_testpackage_Group_isMember():
    assert testpackage_Group.isMember(testpackage_Group('', testpackage_Group=set()), '\x00') == None
