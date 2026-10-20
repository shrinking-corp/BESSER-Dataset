from python_code import Group

def test_Group___init__():
    assert Group.__init__(Group('', card1=set()), '', card1=set()) == None

