from python_code import pnmlcoremodel_Coordinate

def test_pnmlcoremodel_Coordinate___init__():
    assert pnmlcoremodel_Coordinate.__init__(pnmlcoremodel_Coordinate('', '\x00'), '\x00\x00', '') == None


from python_code import pnmlcoremodel_AnnotationGraphics
from python_code import pnmlcoremodel_Fill
from python_code import pnmlcoremodel_NodeGraphics

def test_pnmlcoremodel_Fill___init__():
    assert pnmlcoremodel_Fill.__init__(pnmlcoremodel_Fill('\x00\x00', '', '', '', Fill=pnmlcoremodel_NodeGraphics(), Fill50=pnmlcoremodel_AnnotationGraphics(), fill=pnmlcoremodel_NodeGraphics(), fill60=pnmlcoremodel_AnnotationGraphics()), '', '', '', '', Fill=pnmlcoremodel_NodeGraphics(), Fill50=pnmlcoremodel_AnnotationGraphics(), fill=pnmlcoremodel_NodeGraphics(), fill60=pnmlcoremodel_AnnotationGraphics()) == None


from python_code import pnmlcoremodel_AnnotationGraphics
from python_code import pnmlcoremodel_Font

def test_pnmlcoremodel_Font___init__():
    assert pnmlcoremodel_Font.__init__(pnmlcoremodel_Font('', '', '', '', '', '', '', Font=pnmlcoremodel_AnnotationGraphics(), font=pnmlcoremodel_AnnotationGraphics()), '', '\x00', '', '', '', '', '', Font=pnmlcoremodel_AnnotationGraphics(), font=pnmlcoremodel_AnnotationGraphics()) == None


from python_code import pnmlcoremodel_AnnotationGraphics
from python_code import pnmlcoremodel_ArcGraphics
from python_code import pnmlcoremodel_Line
from python_code import pnmlcoremodel_NodeGraphics

def test_pnmlcoremodel_Line___init__():
    assert pnmlcoremodel_Line.__init__(pnmlcoremodel_Line('\x00\x00', '', '', '', Line=pnmlcoremodel_NodeGraphics(), Line53=pnmlcoremodel_AnnotationGraphics(), line=pnmlcoremodel_NodeGraphics(), line65=pnmlcoremodel_ArcGraphics(), line68=pnmlcoremodel_AnnotationGraphics(), Line74=pnmlcoremodel_ArcGraphics()), '', '', '', '', Line=pnmlcoremodel_NodeGraphics(), Line53=pnmlcoremodel_AnnotationGraphics(), line=pnmlcoremodel_NodeGraphics(), line65=pnmlcoremodel_ArcGraphics(), line68=pnmlcoremodel_AnnotationGraphics(), Line74=pnmlcoremodel_ArcGraphics()) == None

