from python_code import model_Anchor
from python_code import model_EReference

def test_model_Anchor___init__():
    assert model_Anchor.__init__(model_Anchor('', 0, model_Anchor=model_EReference()), '', 0, model_Anchor=model_EReference()) == None


from python_code import model_BooleanValue

def test_model_BooleanValue___init__():
    assert model_BooleanValue.__init__(model_BooleanValue(''), '') == None


from python_code import model_Corner

def test_model_Corner___init__():
    assert model_Corner.__init__(model_Corner(0), 0) == None


from python_code import model_ConnectableElement
from python_code import model_Custom
from python_code import model_CustomFigure
from python_code import model_XDiagram

def test_model_CustomFigure___init__():
    assert model_CustomFigure.__init__(model_CustomFigure('', model_CustomFigure=model_XDiagram(), model_CustomFigure46=model_ConnectableElement(), model_CustomFigure49=model_Custom()), '', model_CustomFigure=model_XDiagram(), model_CustomFigure46=model_ConnectableElement(), model_CustomFigure49=model_Custom()) == None


from python_code import model_DoubleValue

def test_model_DoubleValue___init__():
    assert model_DoubleValue.__init__(model_DoubleValue(0, 0), 0, 0) == None


from python_code import model_Ellipse

def test_model_Ellipse___init__():
    assert model_Ellipse.__init__(model_Ellipse(False, False), False, False) == None


from python_code import model_EnumValue

def test_model_EnumValue___init__():
    assert model_EnumValue.__init__(model_EnumValue(''), '') == None


from python_code import model_EAttribute
from python_code import model_Feature
from python_code import model_FeatureConditional
from python_code import model_Value

def test_model_FeatureConditional___init__():
    assert model_FeatureConditional.__init__(model_FeatureConditional('', model_FeatureConditional=model_Feature(), model_FeatureConditional20=model_EAttribute(), model_FeatureConditional22=model_Value()), '', model_FeatureConditional=model_Feature(), model_FeatureConditional20=model_EAttribute(), model_FeatureConditional22=model_Value()) == None


from python_code import model_FontProperties

def test_model_FontProperties___init__():
    assert model_FontProperties.__init__(model_FontProperties('\x00\x00', 0, False, True), '', 0, False, False) == None


from python_code import model_Image

def test_model_Image___init__():
    assert model_Image.__init__(model_Image(''), '') == None


from python_code import model_ImportStatement

def test_model_ImportStatement___init__():
    assert model_ImportStatement.__init__(model_ImportStatement(''), '') == None


from python_code import model_IntValue

def test_model_IntValue___init__():
    assert model_IntValue.__init__(model_IntValue(0), 0) == None


from python_code import model_Layout

def test_model_Layout___init__():
    assert model_Layout.__init__(model_Layout(False, False, 0), False, False, 0) == None


from python_code import model_Line

def test_model_Line___init__():
    assert model_Line.__init__(model_Line(False, False), False, False) == None


from python_code import model_LineStyle

def test_model_LineStyle___init__():
    assert model_LineStyle.__init__(model_LineStyle('', False), '', False) == None


from python_code import model_LineWidth

def test_model_LineWidth___init__():
    assert model_LineWidth.__init__(model_LineWidth(0), 0) == None


from python_code import model_EReference
from python_code import model_Link

def test_model_Link___init__():
    assert model_Link.__init__(model_Link(False, False, model_Link=model_EReference(), model_Link26=model_EReference(), model_Link29=model_EReference(), model_Link32=set()), False, False, model_Link=model_EReference(), model_Link26=model_EReference(), model_Link29=model_EReference(), model_Link32=set()) == None


from python_code import model_MetaModel
from python_code import model_XDiagram

def test_model_MetaModel___init__():
    assert model_MetaModel.__init__(model_MetaModel('', '\x00', model_MetaModel=model_XDiagram()), '\x00\x00', '', model_MetaModel=model_XDiagram()) == None


from python_code import model_Point

def test_model_Point___init__():
    assert model_Point.__init__(model_Point(0, 0), 0, 0) == None


from python_code import model_Polyline

def test_model_Polyline___init__():
    assert model_Polyline.__init__(model_Polyline(False, False), False, False) == None


from python_code import model_Position

def test_model_Position___init__():
    assert model_Position.__init__(model_Position(False, 0, False, 0), False, 0, False, 0) == None


from python_code import model_Rectangle

def test_model_Rectangle___init__():
    assert model_Rectangle.__init__(model_Rectangle(False, False), False, False) == None


from python_code import model_Size

def test_model_Size___init__():
    assert model_Size.__init__(model_Size(0, False, 0, False, False), 0, False, 0, False, False) == None


from python_code import model_StringValue

def test_model_StringValue___init__():
    assert model_StringValue.__init__(model_StringValue(False, '\x00'), False, '\x00') == None


from python_code import model_TextAlign

def test_model_TextAlign___init__():
    assert model_TextAlign.__init__(model_TextAlign(''), '') == None


from python_code import model_EAttribute
from python_code import model_TextPart
from python_code import model_TextValue

def test_model_TextPart___init__():
    assert model_TextPart.__init__(model_TextPart('', False, model_TextPart=model_TextValue(), model_TextPart57=model_EAttribute()), '', False, model_TextPart=model_TextValue(), model_TextPart57=model_EAttribute()) == None


from python_code import model_Transparency

def test_model_Transparency___init__():
    assert model_Transparency.__init__(model_Transparency(0), 0) == None

