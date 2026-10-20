from python_code import ptnet_Coordinate

def test_ptnet_Coordinate___init__():
    assert ptnet_Coordinate.__init__(ptnet_Coordinate('', '\x00'), '\x00\x00', '') == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Fill
from python_code import ptnet_NodeGraphics

def test_ptnet_Fill___init__():
    assert ptnet_Fill.__init__(ptnet_Fill('\x00\x00', '', '', '', Fill52=ptnet_AnnotationGraphics(), Fill=ptnet_NodeGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics()), '', '', '', '', Fill52=ptnet_AnnotationGraphics(), Fill=ptnet_NodeGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics()) == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Font

def test_ptnet_Font___init__():
    assert ptnet_Font.__init__(ptnet_Font('', '', '', '', '', '', '', Font=ptnet_AnnotationGraphics(), font=ptnet_AnnotationGraphics()), '', '\x00', '', '', '', '', '', Font=ptnet_AnnotationGraphics(), font=ptnet_AnnotationGraphics()) == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_ArcGraphics
from python_code import ptnet_Line
from python_code import ptnet_NodeGraphics

def test_ptnet_Line___init__():
    assert ptnet_Line.__init__(ptnet_Line('\x00\x00', '', '', '', Line55=ptnet_AnnotationGraphics(), Line=ptnet_NodeGraphics(), Line76=ptnet_ArcGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), line70=ptnet_AnnotationGraphics()), '', '', '', '', Line55=ptnet_AnnotationGraphics(), Line=ptnet_NodeGraphics(), Line76=ptnet_ArcGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), line70=ptnet_AnnotationGraphics()) == None


from python_code import ptnet_Arc
from python_code import ptnet_PTArcAnnotation

def test_ptnet_PTArcAnnotation___init__():
    assert ptnet_PTArcAnnotation.__init__(ptnet_PTArcAnnotation('', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()), '', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()) == None


from python_code import ptnet_PTMarking
from python_code import ptnet_Place

def test_ptnet_PTMarking___init__():
    assert ptnet_PTMarking.__init__(ptnet_PTMarking('', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()), '', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()) == None

