from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_Place
from python_code import lit_petriNets_TPArc

def test_lit_petriNets_Place___init__():
    assert lit_petriNets_Place.__init__(lit_petriNets_Place('', d=set(), s=set(), Place=lit_petriNets_Net(), places=lit_petriNets_Net(), Place27=lit_petriNets_TPArc(), Place19=lit_petriNets_PTArc()), '', d=set(), s=set(), Place=lit_petriNets_Net(), places=lit_petriNets_Net(), Place27=lit_petriNets_TPArc(), Place19=lit_petriNets_PTArc()) == None


from python_code import lit_petriNets_Net
from python_code import lit_petriNets_PTArc
from python_code import lit_petriNets_TPArc
from python_code import lit_petriNets_Transition

def test_lit_petriNets_Transition___init__():
    assert lit_petriNets_Transition.__init__(lit_petriNets_Transition('', transitions=lit_petriNets_Net(), Transition=lit_petriNets_Net(), Transition24=lit_petriNets_TPArc(), d11=set(), s14=set(), Transition21=lit_petriNets_PTArc()), '', transitions=lit_petriNets_Net(), Transition=lit_petriNets_Net(), Transition24=lit_petriNets_TPArc(), d11=set(), s14=set(), Transition21=lit_petriNets_PTArc()) == None

