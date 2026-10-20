from python_code import activitydiagram_BooleanValue

def test_activitydiagram_BooleanValue___init__():
    assert activitydiagram_BooleanValue.__init__(activitydiagram_BooleanValue(True), False) == None


from python_code import activitydiagram_IntegerCalculationExpression
from python_code import activitydiagram_IntegerVariable

def test_activitydiagram_IntegerCalculationExpression___init__():
    assert activitydiagram_IntegerCalculationExpression.__init__(activitydiagram_IntegerCalculationExpression('', activitydiagram_IntegerCalculationExpression=activitydiagram_IntegerVariable()), '', activitydiagram_IntegerCalculationExpression=activitydiagram_IntegerVariable()) == None


from python_code import activitydiagram_IntegerValue

def test_activitydiagram_IntegerValue___init__():
    assert activitydiagram_IntegerValue.__init__(activitydiagram_IntegerValue(0), 0) == None


from python_code import activitydiagram_NamedElement

def test_activitydiagram_NamedElement___init__():
    assert activitydiagram_NamedElement.__init__(activitydiagram_NamedElement(''), '') == None


from python_code import activitydiagram_StringValue

def test_activitydiagram_StringValue___init__():
    assert activitydiagram_StringValue.__init__(activitydiagram_StringValue(''), '') == None

