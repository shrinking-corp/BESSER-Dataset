from python_code import jointPackage_PetriNet2PNML_SrcArc
from python_code import jointPackage_PetriNet2PNML_SrcPetriNet

def test_jointPackage_PetriNet2PNML_SrcArc___init__():
    assert jointPackage_PetriNet2PNML_SrcArc.__init__(jointPackage_PetriNet2PNML_SrcArc(0, SrcArc=jointPackage_PetriNet2PNML_SrcPetriNet(), arcs=jointPackage_PetriNet2PNML_SrcPetriNet()), 0, SrcArc=jointPackage_PetriNet2PNML_SrcPetriNet(), arcs=jointPackage_PetriNet2PNML_SrcPetriNet()) == None


from python_code import jointPackage_PetriNet2PNML_SrcLocatedElement

def test_jointPackage_PetriNet2PNML_SrcLocatedElement___init__():
    assert jointPackage_PetriNet2PNML_SrcLocatedElement.__init__(jointPackage_PetriNet2PNML_SrcLocatedElement(''), '') == None


from python_code import jointPackage_PetriNet2PNML_SrcNamedElement

def test_jointPackage_PetriNet2PNML_SrcNamedElement___init__():
    assert jointPackage_PetriNet2PNML_SrcNamedElement.__init__(jointPackage_PetriNet2PNML_SrcNamedElement(''), '') == None


from python_code import jointPackage_PetriNet2PNML_TrgIdedElement

def test_jointPackage_PetriNet2PNML_TrgIdedElement___init__():
    assert jointPackage_PetriNet2PNML_TrgIdedElement.__init__(jointPackage_PetriNet2PNML_TrgIdedElement(''), '') == None


from python_code import jointPackage_PetriNet2PNML_TrgLabel
from python_code import jointPackage_PetriNet2PNML_TrgLabeledElement

def test_jointPackage_PetriNet2PNML_TrgLabel___init__():
    assert jointPackage_PetriNet2PNML_TrgLabel.__init__(jointPackage_PetriNet2PNML_TrgLabel('', jointPackage_PetriNet2PNML_TrgLabel=jointPackage_PetriNet2PNML_TrgLabeledElement()), '', jointPackage_PetriNet2PNML_TrgLabel=jointPackage_PetriNet2PNML_TrgLabeledElement()) == None


from python_code import jointPackage_PetriNet2PNML_TrgLocatedElement

def test_jointPackage_PetriNet2PNML_TrgLocatedElement___init__():
    assert jointPackage_PetriNet2PNML_TrgLocatedElement.__init__(jointPackage_PetriNet2PNML_TrgLocatedElement(''), '') == None


from python_code import jointPackage_PetriNet2PNML_TrgNetElement
from python_code import jointPackage_PetriNet2PNML_TrgPNMLDocument
from python_code import jointPackage_PetriNet2PNML_TrgURI

def test_jointPackage_PetriNet2PNML_TrgURI___init__():
    assert jointPackage_PetriNet2PNML_TrgURI.__init__(jointPackage_PetriNet2PNML_TrgURI('', jointPackage_PetriNet2PNML_TrgURI=jointPackage_PetriNet2PNML_TrgPNMLDocument(), jointPackage_PetriNet2PNML_TrgURI31=jointPackage_PetriNet2PNML_TrgNetElement()), '', jointPackage_PetriNet2PNML_TrgURI=jointPackage_PetriNet2PNML_TrgPNMLDocument(), jointPackage_PetriNet2PNML_TrgURI31=jointPackage_PetriNet2PNML_TrgNetElement()) == None

