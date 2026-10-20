from python_code import jointPackage_Grafcet2PetriNet_SrcLocatedElement

def test_jointPackage_Grafcet2PetriNet_SrcLocatedElement___init__():
    assert jointPackage_Grafcet2PetriNet_SrcLocatedElement.__init__(jointPackage_Grafcet2PetriNet_SrcLocatedElement(''), '') == None


from python_code import jointPackage_Grafcet2PetriNet_SrcNamedElement

def test_jointPackage_Grafcet2PetriNet_SrcNamedElement___init__():
    assert jointPackage_Grafcet2PetriNet_SrcNamedElement.__init__(jointPackage_Grafcet2PetriNet_SrcNamedElement(''), '') == None


from python_code import jointPackage_Grafcet2PetriNet_SrcStep
from python_code import jointPackage_Grafcet2PetriNet_SrcStepToTransition
from python_code import jointPackage_Grafcet2PetriNet_SrcTransitionToStep

def test_jointPackage_Grafcet2PetriNet_SrcStep___init__():
    assert jointPackage_Grafcet2PetriNet_SrcStep.__init__(jointPackage_Grafcet2PetriNet_SrcStep(False, True, '', SrcStep=jointPackage_Grafcet2PetriNet_SrcStepToTransition(), SrcStep24=jointPackage_Grafcet2PetriNet_SrcTransitionToStep(), to=set(), from_=set()), False, False, '', SrcStep=jointPackage_Grafcet2PetriNet_SrcStepToTransition(), SrcStep24=jointPackage_Grafcet2PetriNet_SrcTransitionToStep(), to=set(), from_=set()) == None


from python_code import jointPackage_Grafcet2PetriNet_SrcStepToTransition
from python_code import jointPackage_Grafcet2PetriNet_SrcTransition
from python_code import jointPackage_Grafcet2PetriNet_SrcTransitionToStep

def test_jointPackage_Grafcet2PetriNet_SrcTransition___init__():
    assert jointPackage_Grafcet2PetriNet_SrcTransition.__init__(jointPackage_Grafcet2PetriNet_SrcTransition('', to10=set(), from_13=set(), SrcTransition=jointPackage_Grafcet2PetriNet_SrcStepToTransition(), SrcTransition21=jointPackage_Grafcet2PetriNet_SrcTransitionToStep()), '', to10=set(), from_13=set(), SrcTransition=jointPackage_Grafcet2PetriNet_SrcStepToTransition(), SrcTransition21=jointPackage_Grafcet2PetriNet_SrcTransitionToStep()) == None


from python_code import jointPackage_Grafcet2PetriNet_TrgArc
from python_code import jointPackage_Grafcet2PetriNet_TrgPetriNet

def test_jointPackage_Grafcet2PetriNet_TrgArc___init__():
    assert jointPackage_Grafcet2PetriNet_TrgArc.__init__(jointPackage_Grafcet2PetriNet_TrgArc(0, TrgArc=jointPackage_Grafcet2PetriNet_TrgPetriNet(), arcs=jointPackage_Grafcet2PetriNet_TrgPetriNet()), 0, TrgArc=jointPackage_Grafcet2PetriNet_TrgPetriNet(), arcs=jointPackage_Grafcet2PetriNet_TrgPetriNet()) == None


from python_code import jointPackage_Grafcet2PetriNet_TrgLocatedElement

def test_jointPackage_Grafcet2PetriNet_TrgLocatedElement___init__():
    assert jointPackage_Grafcet2PetriNet_TrgLocatedElement.__init__(jointPackage_Grafcet2PetriNet_TrgLocatedElement(''), '') == None


from python_code import jointPackage_Grafcet2PetriNet_TrgNamedElement

def test_jointPackage_Grafcet2PetriNet_TrgNamedElement___init__():
    assert jointPackage_Grafcet2PetriNet_TrgNamedElement.__init__(jointPackage_Grafcet2PetriNet_TrgNamedElement(''), '') == None

