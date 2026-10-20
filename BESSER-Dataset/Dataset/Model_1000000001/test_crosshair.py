from python_code import Tag

def test_Tag___init__():
    assert Tag.__init__(Tag('', '', 0, tagged_contacts=set(), tagged_companies=set()), '', '', 0, tagged_contacts=set(), tagged_companies=set()) == None

