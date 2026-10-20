from python_code import customerDatabase

def test_customerDatabase___init__():
    assert customerDatabase.__init__(customerDatabase('', '', 0, 0, card20=set()), '', '', 0, 0, card20=set()) == None

