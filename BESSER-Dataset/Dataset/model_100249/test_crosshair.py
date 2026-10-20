from python_code import styles_ColorConstantRef

def test_styles_ColorConstantRef___init__():
    assert styles_ColorConstantRef.__init__(styles_ColorConstantRef(''), '') == None


from python_code import styles_Color
from python_code import styles_GradientColorArea
from python_code import styles_GradientLayout

def test_styles_GradientColorArea___init__():
    assert styles_GradientColorArea.__init__(styles_GradientColorArea(0.0, styles_GradientColorArea31=styles_Color(), styles_GradientColorArea=styles_GradientLayout()), 0.0, styles_GradientColorArea31=styles_Color(), styles_GradientColorArea=styles_GradientLayout()) == None


from python_code import styles_RGBColor

def test_styles_RGBColor___init__():
    assert styles_RGBColor.__init__(styles_RGBColor(0, 0, 0), 0, 0, 0) == None


from python_code import styles_StyleContainer
from python_code import styles_StyleContainerElement

def test_styles_StyleContainerElement___init__():
    assert styles_StyleContainerElement.__init__(styles_StyleContainerElement('', '\x00', styles_StyleContainerElement=styles_StyleContainer()), '\x00\x00', '', styles_StyleContainerElement=styles_StyleContainer()) == None


from python_code import styles_Color
from python_code import styles_ColorOrGradient
from python_code import styles_ColorWithTransparency
from python_code import styles_HighlightingValues
from python_code import styles_Style
from python_code import styles_StyleLayout

def test_styles_StyleLayout___init__():
    assert styles_StyleLayout.__init__(styles_StyleLayout(0.0, '', 0, '\x00', '', 0, '', '', styles_StyleLayout9=styles_ColorOrGradient(), styles_StyleLayout=styles_Style(), styles_StyleLayout11=styles_HighlightingValues(), styles_StyleLayout13=styles_ColorWithTransparency(), styles_StyleLayout15=styles_Color()), 0.0, '', 0, '', '', 0, '', '', styles_StyleLayout9=styles_ColorOrGradient(), styles_StyleLayout=styles_Style(), styles_StyleLayout11=styles_HighlightingValues(), styles_StyleLayout13=styles_ColorWithTransparency(), styles_StyleLayout15=styles_Color()) == None


from python_code import styles_Transparent

def test_styles_Transparent___init__():
    assert styles_Transparent.__init__(styles_Transparent(True), False) == None

