from python_code import trace_AbstractTrace

def test_trace_AbstractTrace___init__():
    assert trace_AbstractTrace.__init__(trace_AbstractTrace(0, False), 0, False) == None


from python_code import trace_MatchingTrace

def test_trace_MatchingTrace___init__():
    assert trace_MatchingTrace.__init__(trace_MatchingTrace(''), '') == None

def test_trace_MatchingTrace_getEClassComparision():
    assert trace_MatchingTrace.getEClassComparision(trace_MatchingTrace(''), 0, '\x00\x00') == None

def test_trace_MatchingTrace_getQueryContext():
    assert trace_MatchingTrace.getQueryContext(trace_MatchingTrace('')) == None

def test_trace_MatchingTrace_getEStructuralFeatureComparison():
    assert trace_MatchingTrace.getEStructuralFeatureComparison(trace_MatchingTrace(''), 0, '\x00\x00') == None

