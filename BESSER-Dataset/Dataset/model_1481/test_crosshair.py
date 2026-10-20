from python_code import graphpattern_EObjectList

def test_graphpattern_EObjectList___init__():
    assert graphpattern_EObjectList.__init__(graphpattern_EObjectList('', graphpattern_EObjectList=set()), '', graphpattern_EObjectList=set()) == None


from python_code import graphpattern_PatternElement

def test_graphpattern_PatternElement___init__():
    assert graphpattern_PatternElement.__init__(graphpattern_PatternElement('', '\x00'), '\x00\x00', '') == None


from python_code import graphpattern_ValueBinding

def test_graphpattern_ValueBinding___init__():
    assert graphpattern_ValueBinding.__init__(graphpattern_ValueBinding(''), '') == None

