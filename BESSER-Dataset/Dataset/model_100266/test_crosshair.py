from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_Place
from python_code import lit_petriNets_TPArc

def test_lit_petriNets_Place___init__():
    assert lit_petriNets_Place.__init__(lit_petriNets_Place('', Place=lit_petriNets_Net(), Place17=lit_petriNets_PTArc(), places=lit_petriNets_Net(), src=set(), dst=set(), Place25=lit_petriNets_TPArc()), '', Place=lit_petriNets_Net(), Place17=lit_petriNets_PTArc(), places=lit_petriNets_Net(), src=set(), dst=set(), Place25=lit_petriNets_TPArc()) == None


from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_TPArc
from python_code import lit_petriNets_Transition

def test_lit_petriNets_Transition___init__():
    assert lit_petriNets_Transition.__init__(lit_petriNets_Transition('', Transition=lit_petriNets_Net(), src14=set(), transitions=lit_petriNets_Net(), dst11=set(), Transition19=lit_petriNets_PTArc(), Transition22=lit_petriNets_TPArc()), '', Transition=lit_petriNets_Net(), src14=set(), transitions=lit_petriNets_Net(), dst11=set(), Transition19=lit_petriNets_PTArc(), Transition22=lit_petriNets_TPArc()) == None

