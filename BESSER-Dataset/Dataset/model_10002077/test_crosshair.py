from python_code import Quota

def test_Quota___init__():
    assert Quota.__init__(Quota('', '', 0, 0, '', quotaItem0=set()), '', '', 0, 0, '', quotaItem0=set()) == None

