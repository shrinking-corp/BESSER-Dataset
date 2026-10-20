from python_code import zlvp_Jahr

def test_zlvp_Jahr___init__():
    assert zlvp_Jahr.__init__(zlvp_Jahr('\x00\x00', 0, zlvp_Jahr=set()), '', 0, zlvp_Jahr=set()) == None

