from python_code import classDiagram_UMLClassDiagram
from python_code import classDiagram_UMLElement

def test_classDiagram_UMLElement___init__():
    assert classDiagram_UMLElement.__init__(classDiagram_UMLElement('', UMLElement=classDiagram_UMLClassDiagram(), elements=classDiagram_UMLClassDiagram()), '', UMLElement=classDiagram_UMLClassDiagram(), elements=classDiagram_UMLClassDiagram()) == None


from python_code import classDiagram_UMLIncrement
from python_code import classDiagram_UMLStereotype

def test_classDiagram_UMLStereotype___init__():
    assert classDiagram_UMLStereotype.__init__(classDiagram_UMLStereotype('', UMLStereotype=classDiagram_UMLIncrement(), stereotypes=classDiagram_UMLIncrement()), '', UMLStereotype=classDiagram_UMLIncrement(), stereotypes=classDiagram_UMLIncrement()) == None

