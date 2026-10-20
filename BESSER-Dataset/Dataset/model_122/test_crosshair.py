from python_code import JMM_Model

def test_JMM_Model___init__():
    assert JMM_Model.__init__(JMM_Model('', JMM_Model=set()), '', JMM_Model=set()) == None


from python_code import JMM_BodyDeclaration
from python_code import JMM_Modifier

def test_JMM_Modifier___init__():
    assert JMM_Modifier.__init__(JMM_Modifier('', JMM_Modifier=JMM_BodyDeclaration()), '', JMM_Modifier=JMM_BodyDeclaration()) == None


from python_code import JMM_NamedElement

def test_JMM_NamedElement___init__():
    assert JMM_NamedElement.__init__(JMM_NamedElement(False, '\x00'), False, '\x00') == None

