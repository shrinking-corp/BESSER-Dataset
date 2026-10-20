from python_code import capellacommon_ChangeEvent

def test_capellacommon_ChangeEvent___init__():
    assert capellacommon_ChangeEvent.__init__(capellacommon_ChangeEvent(''), '') == None


from python_code import capellacommon_TimeEvent

def test_capellacommon_TimeEvent___init__():
    assert capellacommon_TimeEvent.__init__(capellacommon_TimeEvent('', '\x00'), '\x00\x00', '') == None

