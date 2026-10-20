from python_code import etrace_CompositeLink

def test_etrace_CompositeLink___init__():
    assert etrace_CompositeLink.__init__(etrace_CompositeLink(etrace_CompositeLink=set()), etrace_CompositeLink=set()) == None

def test_etrace_CompositeLink_createLink():
    assert etrace_CompositeLink.createLink(etrace_CompositeLink(etrace_CompositeLink=set()), 0, '\x00\x00', '') == None

def test_etrace_CompositeLink_createCompositeLink():
    assert etrace_CompositeLink.createCompositeLink(etrace_CompositeLink(etrace_CompositeLink=set()), 0, '\x00\x00', '', '') == None

