from python_code import statechart_CompositeState
from python_code import statechart_StateVertex

def test_statechart_CompositeState___init__():
    assert statechart_CompositeState.__init__(statechart_CompositeState(False, sv_container=set(), CompositeState=statechart_StateVertex()), False, sv_container=set(), CompositeState=statechart_StateVertex()) == None


from python_code import statechart_Label
from python_code import statechart_StateVertex

def test_statechart_Label___init__():
    assert statechart_Label.__init__(statechart_Label('', statechart_Label=statechart_StateVertex()), '', statechart_Label=statechart_StateVertex()) == None

