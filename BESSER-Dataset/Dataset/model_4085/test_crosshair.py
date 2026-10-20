from python_code import simpleUML_Generalization
from python_code import simpleUML_Model
from python_code import simpleUML_UMLClass

def test_simpleUML_UMLClass___init__():
    assert simpleUML_UMLClass.__init__(simpleUML_UMLClass('', simpleUML_UMLClass=simpleUML_Model(), simpleUML_UMLClass2=set(), simpleUML_UMLClass5=simpleUML_Generalization()), '', simpleUML_UMLClass=simpleUML_Model(), simpleUML_UMLClass2=set(), simpleUML_UMLClass5=simpleUML_Generalization()) == None

