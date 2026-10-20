from python_code import Group

def test_Group___init__():
    assert Group.__init__(Group('', 0, deck5=set(), card8=set()), '', 0, deck5=set(), card8=set()) == None

