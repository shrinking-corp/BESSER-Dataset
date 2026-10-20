from python_code import gtrace_TTrace

def test_gtrace_TTrace___init__():
    assert gtrace_TTrace.__init__(gtrace_TTrace(''), '') == None


from python_code import gtrace_TTraceModel

def test_gtrace_TTraceModel___init__():
    assert gtrace_TTraceModel.__init__(gtrace_TTraceModel('', gtrace_TTraceModel2=set(), gtrace_TTraceModel4=set(), gtrace_TTraceModel=set()), '', gtrace_TTraceModel2=set(), gtrace_TTraceModel4=set(), gtrace_TTraceModel=set()) == None

