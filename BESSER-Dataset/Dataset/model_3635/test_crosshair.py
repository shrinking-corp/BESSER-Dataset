from python_code import umlknes_AcceptEventAction

def test_umlknes_AcceptEventAction___init__():
    assert umlknes_AcceptEventAction.__init__(umlknes_AcceptEventAction(False, umlknes_AcceptEventAction=set()), False, umlknes_AcceptEventAction=set()) == None


from python_code import umlknes_Activity
from python_code import umlknes_ActivityEdge
from python_code import umlknes_ActivityNode

def test_umlknes_Activity___init__():
    assert umlknes_Activity.__init__(umlknes_Activity(False, False, Activity=umlknes_ActivityNode(), Activity15=umlknes_ActivityEdge(), activity=set(), activity2=set()), False, True, Activity=umlknes_ActivityNode(), Activity15=umlknes_ActivityEdge(), activity=set(), activity2=set()) == None


from python_code import umlknes_NamedElement

def test_umlknes_NamedElement___init__():
    assert umlknes_NamedElement.__init__(umlknes_NamedElement(''), '') == None


from python_code import umlknes_RedefinableElement

def test_umlknes_RedefinableElement___init__():
    assert umlknes_RedefinableElement.__init__(umlknes_RedefinableElement(True), False) == None

