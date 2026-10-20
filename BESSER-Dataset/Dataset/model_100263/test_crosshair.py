from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_Place
from python_code import lit_petriNets_TPArc

def test_lit_petriNets_Place___init__():
    assert lit_petriNets_Place.__init__(lit_petriNets_Place('', Place=lit_petriNets_Net(), places=lit_petriNets_Net(), dst=set(), src=set(), Place19=lit_petriNets_PTArc(), Place27=lit_petriNets_TPArc()), '', Place=lit_petriNets_Net(), places=lit_petriNets_Net(), dst=set(), src=set(), Place19=lit_petriNets_PTArc(), Place27=lit_petriNets_TPArc()) == None


from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_TPArc
from python_code import lit_petriNets_Transition

def test_lit_petriNets_Transition___init__():
    assert lit_petriNets_Transition.__init__(lit_petriNets_Transition('', dst11=set(), Transition=lit_petriNets_Net(), transitions=lit_petriNets_Net(), src14=set(), Transition21=lit_petriNets_PTArc(), Transition24=lit_petriNets_TPArc()), '', dst11=set(), Transition=lit_petriNets_Net(), transitions=lit_petriNets_Net(), src14=set(), Transition21=lit_petriNets_PTArc(), Transition24=lit_petriNets_TPArc()) == None

