from enum import Enum
from python_code import HLArcType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HLArcType.Test, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HLArcType.Test, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HLArcType.Test, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HLArcType.Test, 0)

def test_Enum___new___2():
    assert Enum.__new__(HLArcType.Test, 'Test') == HLArcType.Test

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
    assert model_PetriNet.__init__(model_PetriNet('', PetriNet=model_Page(), petriNet=set(), petriNet23=set(), PetriNet40=model_FusionGroup()), '', PetriNet=model_Page(), petriNet=set(), petriNet23=set(), PetriNet40=model_FusionGroup()) == None

from python_code import model_HasToolInfo
from python_code import model_ToolInfo

def test_model_ToolInfo___init__():
    assert model_ToolInfo.__init__(model_ToolInfo('', '\x00', ToolInfo=model_HasToolInfo(), toolinfo=model_HasToolInfo()), '\x00\x00', '', ToolInfo=model_HasToolInfo(), toolinfo=model_HasToolInfo()) == None
