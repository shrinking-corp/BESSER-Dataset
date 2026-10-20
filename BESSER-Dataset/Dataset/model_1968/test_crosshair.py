from python_code import ASPT_TraceEdge

def test_ASPT_TraceEdge___init__():
    assert ASPT_TraceEdge.__init__(ASPT_TraceEdge('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ASPT_TraceModel

def test_ASPT_TraceModel___init__():
    assert ASPT_TraceModel.__init__(ASPT_TraceModel('', '', ASPT_TraceModel=set(), ASPT_TraceModel2=set()), '', '', ASPT_TraceModel=set(), ASPT_TraceModel2=set()) == None


from python_code import ASPT_TraceProp

def test_ASPT_TraceProp___init__():
    assert ASPT_TraceProp.__init__(ASPT_TraceProp('', '', '\x00\x00'), '', '', '') == None

