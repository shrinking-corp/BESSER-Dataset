from python_code import adfg_AperiodicActor

def test_adfg_AperiodicActor___init__():
    assert adfg_AperiodicActor.__init__(adfg_AperiodicActor('', '\x00'), '\x00\x00', '') == None


from python_code import adfg_Channel

def test_adfg_Channel___init__():
    assert adfg_Channel.__init__(adfg_Channel(0), 0) == None

