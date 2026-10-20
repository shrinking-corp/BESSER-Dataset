from python_code import lit_petriNets_2_Net
from python_code import lit_petriNets_2_PTArc
from python_code import lit_petriNets_2_Place
from python_code import lit_petriNets_2_TPArc

def test_lit_petriNets_2_Place___init__():
    assert lit_petriNets_2_Place.__init__(lit_petriNets_2_Place('', Place19=lit_petriNets_2_PTArc(), Place27=lit_petriNets_2_TPArc(), Place=lit_petriNets_2_Net(), places=lit_petriNets_2_Net(), dst=set(), src=set()), '', Place19=lit_petriNets_2_PTArc(), Place27=lit_petriNets_2_TPArc(), Place=lit_petriNets_2_Net(), places=lit_petriNets_2_Net(), dst=set(), src=set()) == None


from python_code import lit_petriNets_2_Net
from python_code import lit_petriNets_2_PTArc
from python_code import lit_petriNets_2_TPArc
from python_code import lit_petriNets_2_Transition

def test_lit_petriNets_2_Transition___init__():
    assert lit_petriNets_2_Transition.__init__(lit_petriNets_2_Transition('', transitions=lit_petriNets_2_Net(), dst11=set(), src14=set(), Transition21=lit_petriNets_2_PTArc(), Transition24=lit_petriNets_2_TPArc(), Transition=lit_petriNets_2_Net()), '', transitions=lit_petriNets_2_Net(), dst11=set(), src14=set(), Transition21=lit_petriNets_2_PTArc(), Transition24=lit_petriNets_2_TPArc(), Transition=lit_petriNets_2_Net()) == None

