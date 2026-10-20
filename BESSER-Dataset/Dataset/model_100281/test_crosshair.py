from python_code import model_HLAnnotationAddin

def test_model_HLAnnotationAddin___init__():
    assert model_HLAnnotationAddin.__init__(model_HLAnnotationAddin(''), '') == None


from python_code import model_HLAnnotation
from python_code import model_HLArcAddin

def test_model_HLArcAddin___init__():
    assert model_HLArcAddin.__init__(model_HLArcAddin('', model_HLArcAddin=model_HLAnnotation()), '', model_HLArcAddin=model_HLAnnotation()) == None


from python_code import model_HasId

def test_model_HasId___init__():
    assert model_HasId.__init__(model_HasId(''), '') == None


from python_code import model_HasLabel
from python_code import model_Label

def test_model_Label___init__():
    assert model_Label.__init__(model_Label(Label=model_HasLabel(), label=model_HasLabel()), Label=model_HasLabel(), label=model_HasLabel()) == None

def test_model_Label_asString():
    assert model_Label.asString(model_Label(Label=model_HasLabel(), label=model_HasLabel())) == None


from python_code import model_FusionGroup
from python_code import model_Page
from python_code import model_PetriNet

def test_model_PetriNet___init__():
    assert model_PetriNet.__init__(model_PetriNet('', '', PetriNet=model_FusionGroup(), PetriNet28=model_Page(), petriNet=set(), petriNet38=set(), petriNet40=set()), '', '', PetriNet=model_FusionGroup(), PetriNet28=model_Page(), petriNet=set(), petriNet38=set(), petriNet40=set()) == None


from python_code import model_HasToolInfo
from python_code import model_ToolInfo

def test_model_ToolInfo___init__():
    assert model_ToolInfo.__init__(model_ToolInfo('', '\x00', ToolInfo=model_HasToolInfo(), toolinfo=model_HasToolInfo()), '\x00\x00', '', ToolInfo=model_HasToolInfo(), toolinfo=model_HasToolInfo()) == None

