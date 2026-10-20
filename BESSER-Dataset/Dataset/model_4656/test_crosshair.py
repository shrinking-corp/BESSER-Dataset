from python_code import di_Diagram
from python_code import di_DiagramElement

def test_di_Diagram___init__():
    assert di_Diagram.__init__(di_Diagram('\x00', '', 0.0, di_Diagram=set(), owningDiagram=di_DiagramElement(), Diagram=di_DiagramElement()), '', '', 0.0, di_Diagram=set(), owningDiagram=di_DiagramElement(), Diagram=di_DiagramElement()) == None


from python_code import di_Plane

def test_di_Plane___init__():
    assert di_Plane.__init__(di_Plane(di_Plane=set()), di_Plane=set()) == None

def test_di_Plane_plane_element_type():
    assert di_Plane.plane_element_type(di_Plane(di_Plane=set()), 0, '\x00\x00') == None

