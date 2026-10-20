from python_code import ptnet_Coordinate

def test_ptnet_Coordinate___init__():
    assert ptnet_Coordinate.__init__(ptnet_Coordinate('', '\x00'), '\x00\x00', '') == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Fill
from python_code import ptnet_NodeGraphics

def test_ptnet_Fill___init__():
    assert ptnet_Fill.__init__(ptnet_Fill('\x00\x00', '', '', '', Fill=ptnet_NodeGraphics(), Fill52=ptnet_AnnotationGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics()), '', '', '', '', Fill=ptnet_NodeGraphics(), Fill52=ptnet_AnnotationGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics()) == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Font

def test_ptnet_Font___init__():
    assert ptnet_Font.__init__(ptnet_Font('', '', '', '', '', '', '', font=ptnet_AnnotationGraphics(), Font=ptnet_AnnotationGraphics()), '', '\x00', '', '', '', '', '', font=ptnet_AnnotationGraphics(), Font=ptnet_AnnotationGraphics()) == None


from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_ArcGraphics
from python_code import ptnet_Line
from python_code import ptnet_NodeGraphics

def test_ptnet_Line___init__():
    assert ptnet_Line.__init__(ptnet_Line('\x00\x00', '', '', '', Line=ptnet_NodeGraphics(), Line55=ptnet_AnnotationGraphics(), line70=ptnet_AnnotationGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), Line76=ptnet_ArcGraphics()), '', '', '', '', Line=ptnet_NodeGraphics(), Line55=ptnet_AnnotationGraphics(), line70=ptnet_AnnotationGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), Line76=ptnet_ArcGraphics()) == None


from python_code import ptnet_Arc
from python_code import ptnet_PTArcAnnotation

def test_ptnet_PTArcAnnotation___init__():
    assert ptnet_PTArcAnnotation.__init__(ptnet_PTArcAnnotation('', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()), '', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()) == None


from python_code import ptnet_PTMarking
from python_code import ptnet_Place

def test_ptnet_PTMarking___init__():
    assert ptnet_PTMarking.__init__(ptnet_PTMarking('', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()), '', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()) == None

