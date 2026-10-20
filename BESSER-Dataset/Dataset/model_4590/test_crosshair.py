from python_code import activitydiagram_ADElement
from python_code import activitydiagram_Activity

def test_activitydiagram_ADElement___init__():
    assert activitydiagram_ADElement.__init__(activitydiagram_ADElement('', ADElement=activitydiagram_Activity(), contains=activitydiagram_Activity()), '', ADElement=activitydiagram_Activity(), contains=activitydiagram_Activity()) == None


from python_code import activitydiagram_AcceptSignalNode

def test_activitydiagram_AcceptSignalNode___init__():
    assert activitydiagram_AcceptSignalNode.__init__(activitydiagram_AcceptSignalNode(''), '') == None


from python_code import activitydiagram_ActivityParameterNode

def test_activitydiagram_ActivityParameterNode___init__():
    assert activitydiagram_ActivityParameterNode.__init__(activitydiagram_ActivityParameterNode(''), '') == None


from python_code import activitydiagram_SignalNode

def test_activitydiagram_SignalNode___init__():
    assert activitydiagram_SignalNode.__init__(activitydiagram_SignalNode(''), '') == None


from python_code import activitydiagram_TimeEventNode

def test_activitydiagram_TimeEventNode___init__():
    assert activitydiagram_TimeEventNode.__init__(activitydiagram_TimeEventNode(''), '') == None

