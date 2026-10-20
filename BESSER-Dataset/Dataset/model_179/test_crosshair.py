from python_code import petrinets_Net
from python_code import petrinets_PTArc
from python_code import petrinets_Place
from python_code import petrinets_TPArc

def test_petrinets_Place___init__():
    assert petrinets_Place.__init__(petrinets_Place('', Place=petrinets_Net(), Place19=petrinets_PTArc(), Place27=petrinets_TPArc(), places=petrinets_Net(), dst=set(), src=set()), '', Place=petrinets_Net(), Place19=petrinets_PTArc(), Place27=petrinets_TPArc(), places=petrinets_Net(), dst=set(), src=set()) == None


from python_code import petrinets_Net
from python_code import petrinets_PTArc
from python_code import petrinets_TPArc
from python_code import petrinets_Transition

def test_petrinets_Transition___init__():
    assert petrinets_Transition.__init__(petrinets_Transition('', Transition21=petrinets_PTArc(), Transition24=petrinets_TPArc(), Transition=petrinets_Net(), transitions=petrinets_Net(), dst11=set(), src14=set()), '', Transition21=petrinets_PTArc(), Transition24=petrinets_TPArc(), Transition=petrinets_Net(), transitions=petrinets_Net(), dst11=set(), src14=set()) == None

