from python_code import hlcorestructure_Coordinate

def test_hlcorestructure_Coordinate___init__():
    assert hlcorestructure_Coordinate.__init__(hlcorestructure_Coordinate('', '\x00'), '\x00\x00', '') == None


from python_code import hlcorestructure_AnnotationGraphics
from python_code import hlcorestructure_Fill
from python_code import hlcorestructure_NodeGraphics

def test_hlcorestructure_Fill___init__():
    assert hlcorestructure_Fill.__init__(hlcorestructure_Fill('\x00\x00', '', '', '', Fill=hlcorestructure_NodeGraphics(), Fill53=hlcorestructure_AnnotationGraphics(), fill=hlcorestructure_NodeGraphics(), fill63=hlcorestructure_AnnotationGraphics()), '', '', '', '', Fill=hlcorestructure_NodeGraphics(), Fill53=hlcorestructure_AnnotationGraphics(), fill=hlcorestructure_NodeGraphics(), fill63=hlcorestructure_AnnotationGraphics()) == None


from python_code import hlcorestructure_AnnotationGraphics
from python_code import hlcorestructure_Font

def test_hlcorestructure_Font___init__():
    assert hlcorestructure_Font.__init__(hlcorestructure_Font('', '', '', '', '', '', '', font=hlcorestructure_AnnotationGraphics(), Font=hlcorestructure_AnnotationGraphics()), '', '\x00', '', '', '', '', '', font=hlcorestructure_AnnotationGraphics(), Font=hlcorestructure_AnnotationGraphics()) == None


from python_code import hlcorestructure_HLCoreAnnotation

def test_hlcorestructure_HLCoreAnnotation___init__():
    assert hlcorestructure_HLCoreAnnotation.__init__(hlcorestructure_HLCoreAnnotation(''), '') == None


from python_code import hlcorestructure_AnnotationGraphics
from python_code import hlcorestructure_ArcGraphics
from python_code import hlcorestructure_Line
from python_code import hlcorestructure_NodeGraphics

def test_hlcorestructure_Line___init__():
    assert hlcorestructure_Line.__init__(hlcorestructure_Line('\x00\x00', '', '', '', Line=hlcorestructure_NodeGraphics(), Line56=hlcorestructure_AnnotationGraphics(), Line77=hlcorestructure_ArcGraphics(), line=hlcorestructure_NodeGraphics(), line68=hlcorestructure_ArcGraphics(), line71=hlcorestructure_AnnotationGraphics()), '', '', '', '', Line=hlcorestructure_NodeGraphics(), Line56=hlcorestructure_AnnotationGraphics(), Line77=hlcorestructure_ArcGraphics(), line=hlcorestructure_NodeGraphics(), line68=hlcorestructure_ArcGraphics(), line71=hlcorestructure_AnnotationGraphics()) == None

