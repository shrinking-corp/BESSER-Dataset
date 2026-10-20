from python_code import junitresult_AbstractAggregatedTest

def test_junitresult_AbstractAggregatedTest___init__():
    assert junitresult_AbstractAggregatedTest.__init__(junitresult_AbstractAggregatedTest('', 0, 0, 0, junitresult_AbstractAggregatedTest=set()), '', 0, 0, 0, junitresult_AbstractAggregatedTest=set()) == None


from python_code import junitresult_NegativeResult

def test_junitresult_NegativeResult___init__():
    assert junitresult_NegativeResult.__init__(junitresult_NegativeResult('', '', '\x00\x00'), '', '', '') == None


from python_code import junitresult_Testrun

def test_junitresult_Testrun___init__():
    assert junitresult_Testrun.__init__(junitresult_Testrun('', 0, 0), '\x00', 0, 0) == None


from python_code import junitresult_Testsuites

def test_junitresult_Testsuites___init__():
    assert junitresult_Testsuites.__init__(junitresult_Testsuites(0.0, 0), 0.0, 0) == None

