from python_code import notation_BorderStyle
from python_code import notation_Figure

def test_notation_BorderStyle___init__():
    assert notation_BorderStyle.__init__(notation_BorderStyle(0.0, '', '', notation_BorderStyle=notation_Figure()), 0.0, '', '', notation_BorderStyle=notation_Figure()) == None


from python_code import notation_Compartment
from python_code import notation_Node

def test_notation_Compartment___init__():
    assert notation_Compartment.__init__(notation_Compartment('', notation_Compartment=notation_Node()), '', notation_Compartment=notation_Node()) == None


from python_code import notation_Composite
from python_code import notation_GraphicalElement

def test_notation_Composite___init__():
    assert notation_Composite.__init__(notation_Composite('', notation_Composite=set(), notation_Composite16=notation_GraphicalElement()), '', notation_Composite=set(), notation_Composite16=notation_GraphicalElement()) == None


from python_code import notation_Figure
from python_code import notation_FigureContainment

def test_notation_FigureContainment___init__():
    assert notation_FigureContainment.__init__(notation_FigureContainment('', notation_FigureContainment=notation_Figure(), notation_FigureContainment28=set()), '', notation_FigureContainment=notation_Figure(), notation_FigureContainment28=set()) == None


from python_code import notation_Figure
from python_code import notation_FigureStyle

def test_notation_FigureStyle___init__():
    assert notation_FigureStyle.__init__(notation_FigureStyle(0.0, 0.0, '', 0, '', '', '', '', notation_FigureStyle=notation_Figure()), 0.0, 0.0, '', 0, '', '', '', '', notation_FigureStyle=notation_Figure()) == None


from python_code import notation_IDElement

def test_notation_IDElement___init__():
    assert notation_IDElement.__init__(notation_IDElement(''), '') == None


from python_code import notation_GraphicalElement
from python_code import notation_Image

def test_notation_Image___init__():
    assert notation_Image.__init__(notation_Image('', notation_Image=notation_GraphicalElement()), '', notation_Image=notation_GraphicalElement()) == None


from python_code import notation_Line
from python_code import notation_LineStyle

def test_notation_LineStyle___init__():
    assert notation_LineStyle.__init__(notation_LineStyle(0.0, '', '', 0.0, 0, '', notation_LineStyle=notation_Line()), 0.0, '', '', 0.0, 0, '', notation_LineStyle=notation_Line()) == None


from python_code import notation_NotationDefinition

def test_notation_NotationDefinition___init__():
    assert notation_NotationDefinition.__init__(notation_NotationDefinition('', notation_NotationDefinition=set()), '', notation_NotationDefinition=set()) == None


from python_code import notation_Point
from python_code import notation_Polyline

def test_notation_Point___init__():
    assert notation_Point.__init__(notation_Point(0, 0, notation_Point=notation_Polyline()), 0, 0, notation_Point=notation_Polyline()) == None


from python_code import notation_Label
from python_code import notation_TextStyle

def test_notation_TextStyle___init__():
    assert notation_TextStyle.__init__(notation_TextStyle(False, False, False, '', 0, '', notation_TextStyle=notation_Label()), False, False, False, '', 0, '', notation_TextStyle=notation_Label()) == None


from python_code import notation_Label
from python_code import notation_TextualContainment

def test_notation_TextualContainment___init__():
    assert notation_TextualContainment.__init__(notation_TextualContainment('', notation_TextualContainment=notation_Label(), notation_TextualContainment32=set()), '', notation_TextualContainment=notation_Label(), notation_TextualContainment32=set()) == None

