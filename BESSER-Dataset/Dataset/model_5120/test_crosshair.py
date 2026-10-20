from python_code import diva_Annotation
from python_code import diva_DiVAModelElement

def test_diva_Annotation___init__():
    assert diva_Annotation.__init__(diva_Annotation('', '\x00', diva_Annotation=diva_DiVAModelElement()), '\x00\x00', '', diva_Annotation=diva_DiVAModelElement()) == None


from python_code import diva_BaseModel
from python_code import diva_VariabilityModel

def test_diva_BaseModel___init__():
    assert diva_BaseModel.__init__(diva_BaseModel(diva_BaseModel=diva_VariabilityModel()), diva_BaseModel=diva_VariabilityModel()) == None

def test_diva_BaseModel_weave():
    assert diva_BaseModel.weave(diva_BaseModel(diva_BaseModel=diva_VariabilityModel())) == None


from python_code import diva_BoolVariableValue

def test_diva_BoolVariableValue___init__():
    assert diva_BoolVariableValue.__init__(diva_BoolVariableValue(True), False) == None


from python_code import diva_Expression
from python_code import diva_Invariant
from python_code import diva_Term

def test_diva_Expression___init__():
    assert diva_Expression.__init__(diva_Expression('', diva_Expression41=diva_Term(), diva_Expression=diva_Invariant()), '', diva_Expression41=diva_Term(), diva_Expression=diva_Invariant()) == None


from python_code import diva_NamedElement

def test_diva_NamedElement___init__():
    assert diva_NamedElement.__init__(diva_NamedElement('', '\x00'), '\x00\x00', '') == None

