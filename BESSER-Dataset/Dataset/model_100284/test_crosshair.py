from python_code import nppn_Pragmatic
from python_code import org_k1s_nppn_Binding

def test_org_k1s_nppn_Binding___init__():
    assert org_k1s_nppn_Binding.__init__(org_k1s_nppn_Binding('', org_k1s_nppn_Binding=nppn_Pragmatic()), '', org_k1s_nppn_Binding=nppn_Pragmatic()) == None


from python_code import nppn_HLAnnotation
from python_code import org_k1s_nppn_HLArcAddin

def test_org_k1s_nppn_HLArcAddin___init__():
    assert org_k1s_nppn_HLArcAddin.__init__(org_k1s_nppn_HLArcAddin('', org_k1s_nppn_HLArcAddin=nppn_HLAnnotation()), '', org_k1s_nppn_HLArcAddin=nppn_HLAnnotation()) == None


from python_code import org_k1s_nppn_Instance

def test_org_k1s_nppn_Instance___init__():
    assert org_k1s_nppn_Instance.__init__(org_k1s_nppn_Instance(''), '') == None


from python_code import nppn_HasLabel
from python_code import org_k1s_nppn_Label

def test_org_k1s_nppn_Label___init__():
    assert org_k1s_nppn_Label.__init__(org_k1s_nppn_Label(label=nppn_HasLabel()), label=nppn_HasLabel()) == None

def test_org_k1s_nppn_Label_asString():
    assert org_k1s_nppn_Label.asString(org_k1s_nppn_Label(label=nppn_HasLabel())) == None


from python_code import org_k1s_nppn_PetriNet

def test_org_k1s_nppn_PetriNet___init__():
    assert org_k1s_nppn_PetriNet.__init__(org_k1s_nppn_PetriNet('', '', petriNet23=set(), petriNet=set()), '', '', petriNet23=set(), petriNet=set()) == None


from python_code import org_k1s_nppn_Pragmatic

def test_org_k1s_nppn_Pragmatic___init__():
    assert org_k1s_nppn_Pragmatic.__init__(org_k1s_nppn_Pragmatic('', org_k1s_nppn_Pragmatic=set()), '', org_k1s_nppn_Pragmatic=set()) == None

