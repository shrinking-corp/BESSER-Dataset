from python_code import activitydiagram_Activity
from python_code import activitydiagram_ActivityEdge
from python_code import activitydiagram_ActivityNode
from python_code import activitydiagram_Token
from python_code import activitydiagram_Trace

def test_activitydiagram_ActivityNode___init__():
    assert activitydiagram_ActivityNode.__init__(activitydiagram_ActivityNode(False, ActivityNode=activitydiagram_Activity(), source=set(), target=set(), nodes=activitydiagram_Activity(), holder=set(), ActivityNode13=activitydiagram_ActivityEdge(), ActivityNode15=activitydiagram_ActivityEdge(), activitydiagram_ActivityNode=activitydiagram_Trace(), ActivityNode33=activitydiagram_Token()), True, ActivityNode=activitydiagram_Activity(), source=set(), target=set(), nodes=activitydiagram_Activity(), holder=set(), ActivityNode13=activitydiagram_ActivityEdge(), ActivityNode15=activitydiagram_ActivityEdge(), activitydiagram_ActivityNode=activitydiagram_Trace(), ActivityNode33=activitydiagram_Token()) == None


from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_ForkedToken
from python_code import activitydiagram_Token

def test_activitydiagram_ForkedToken___init__():
    assert activitydiagram_ForkedToken.__init__(activitydiagram_ForkedToken(0, activitydiagram_ForkedToken=activitydiagram_Token()), 0, activitydiagram_ForkedToken=activitydiagram_Token()) == None


from python_code import activitydiagram_IntegerValue

def test_activitydiagram_IntegerValue___init__():
    assert activitydiagram_IntegerValue.__init__(activitydiagram_IntegerValue(0.0), 0.0) == None


from python_code import activitydiagram_NamedActivity

def test_activitydiagram_NamedActivity___init__():
    assert activitydiagram_NamedActivity.__init__(activitydiagram_NamedActivity(''), '') == None

