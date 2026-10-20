from python_code import dg_Bounds
from python_code import dg_Canvas

def test_dg_Canvas___init__():
    assert dg_Canvas.__init__(dg_Canvas(dg_Canvas=dg_Bounds()), dg_Canvas=dg_Bounds()) == None

def test_dg_Canvas_canvasCannotHaveTransforms():
    assert dg_Canvas.canvasCannotHaveTransforms(dg_Canvas(dg_Canvas=dg_Bounds()), '', '') == None


from python_code import dg_Circle
from python_code import dg_Point

def test_dg_Circle___init__():
    assert dg_Circle.__init__(dg_Circle('', dg_Circle=dg_Point()), '', dg_Circle=dg_Point()) == None

def test_dg_Circle_nonNegativeRadius():
    assert dg_Circle.nonNegativeRadius(dg_Circle('', dg_Circle=dg_Point()), 0, '\x00\x00') == None


from python_code import dg_Definition
from python_code import dg_Definitions

def test_dg_Definition___init__():
    assert dg_Definition.__init__(dg_Definition('', dg_Definition=dg_Definitions()), '', dg_Definition=dg_Definitions()) == None

def test_dg_Definition_idCannotBeEmpty():
    assert dg_Definition.idCannotBeEmpty(dg_Definition('', dg_Definition=dg_Definitions()), 0, '\x00\x00') == None


from python_code import dg_Dimension
from python_code import dg_EllipticalArcTo
from python_code import dg_Point

def test_dg_EllipticalArcTo___init__():
    assert dg_EllipticalArcTo.__init__(dg_EllipticalArcTo('', '', '\x00\x00', dg_EllipticalArcTo=dg_Dimension(), dg_EllipticalArcTo46=dg_Point()), '', '', '', dg_EllipticalArcTo=dg_Dimension(), dg_EllipticalArcTo46=dg_Point()) == None


from python_code import dg_Gradient
from python_code import dg_GradientStop

def test_dg_GradientStop___init__():
    assert dg_GradientStop.__init__(dg_GradientStop('', '', '\x00\x00', dg_GradientStop=dg_Gradient()), '', '', '', dg_GradientStop=dg_Gradient()) == None

def test_dg_GradientStop_validOffset():
    assert dg_GradientStop.validOffset(dg_GradientStop('', '', '\x00', dg_GradientStop=dg_Gradient()), '', '') == None

def test_dg_GradientStop_validOpacity():
    assert dg_GradientStop.validOpacity(dg_GradientStop('', '', '\x00', dg_GradientStop=dg_Gradient()), '', '') == None


from python_code import dg_Bounds
from python_code import dg_Image

def test_dg_Image___init__():
    assert dg_Image.__init__(dg_Image('', '\x00', dg_Image=dg_Bounds()), '\x00\x00', '', dg_Image=dg_Bounds()) == None

def test_dg_Image_sourceCannotBeEmpty():
    assert dg_Image.sourceCannotBeEmpty(dg_Image('', '', dg_Image=dg_Bounds()), '', '') == None


from python_code import dg_LinearGradient
from python_code import dg_Point

def test_dg_LinearGradient___init__():
    assert dg_LinearGradient.__init__(dg_LinearGradient(dg_LinearGradient=dg_Point(), dg_LinearGradient77=dg_Point()), dg_LinearGradient=dg_Point(), dg_LinearGradient77=dg_Point()) == None

def test_dg_LinearGradient_validGradientVector():
    assert dg_LinearGradient.validGradientVector(dg_LinearGradient(dg_LinearGradient=dg_Point(), dg_LinearGradient77=dg_Point()), '', '') == None


from python_code import dg_MarkedElement
from python_code import dg_Marker

def test_dg_MarkedElement___init__():
    assert dg_MarkedElement.__init__(dg_MarkedElement(dg_MarkedElement=dg_Marker(), dg_MarkedElement63=dg_Marker(), dg_MarkedElement66=dg_Marker()), dg_MarkedElement=dg_Marker(), dg_MarkedElement63=dg_Marker(), dg_MarkedElement66=dg_Marker()) == None

def test_dg_MarkedElement_referencedMidMarkerHasId():
    assert dg_MarkedElement.referencedMidMarkerHasId(dg_MarkedElement(dg_MarkedElement=dg_Marker(), dg_MarkedElement63=dg_Marker(), dg_MarkedElement66=dg_Marker()), '', '') == None

def test_dg_MarkedElement_referencedEndMarkerHasId():
    assert dg_MarkedElement.referencedEndMarkerHasId(dg_MarkedElement(dg_MarkedElement=dg_Marker(), dg_MarkedElement63=dg_Marker(), dg_MarkedElement66=dg_Marker()), '', '') == None

def test_dg_MarkedElement_referencedStartMarkerHasId():
    assert dg_MarkedElement.referencedStartMarkerHasId(dg_MarkedElement(dg_MarkedElement=dg_Marker(), dg_MarkedElement63=dg_Marker(), dg_MarkedElement66=dg_Marker()), '', '') == None


from python_code import dg_Matrix

def test_dg_Matrix___init__():
    assert dg_Matrix.__init__(dg_Matrix('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import dg_Path

def test_dg_Path___init__():
    assert dg_Path.__init__(dg_Path(dg_Path=set()), dg_Path=set()) == None

def test_dg_Path_firstCommandMustBeMove():
    assert dg_Path.firstCommandMustBeMove(dg_Path(dg_Path=set()), 0, '\x00\x00') == None


from python_code import dg_Point
from python_code import dg_RadialGradient

def test_dg_RadialGradient___init__():
    assert dg_RadialGradient.__init__(dg_RadialGradient('', dg_RadialGradient=dg_Point(), dg_RadialGradient94=dg_Point()), '', dg_RadialGradient=dg_Point(), dg_RadialGradient94=dg_Point()) == None

def test_dg_RadialGradient_validRadius():
    assert dg_RadialGradient.validRadius(dg_RadialGradient('', dg_RadialGradient=dg_Point(), dg_RadialGradient94=dg_Point()), 0, '\x00\x00') == None

def test_dg_RadialGradient_validFocusPoint():
    assert dg_RadialGradient.validFocusPoint(dg_RadialGradient('', dg_RadialGradient=dg_Point(), dg_RadialGradient94=dg_Point()), 0, '\x00\x00') == None

def test_dg_RadialGradient_validCenterPoint():
    assert dg_RadialGradient.validCenterPoint(dg_RadialGradient('', dg_RadialGradient=dg_Point(), dg_RadialGradient94=dg_Point()), 0, '\x00\x00') == None


from python_code import dg_Bounds
from python_code import dg_Rectangle

def test_dg_Rectangle___init__():
    assert dg_Rectangle.__init__(dg_Rectangle('', dg_Rectangle=dg_Bounds()), '', dg_Rectangle=dg_Bounds()) == None

def test_dg_Rectangle_nonNegativeCornerRadius():
    assert dg_Rectangle.nonNegativeCornerRadius(dg_Rectangle('', dg_Rectangle=dg_Bounds()), 0, '\x00\x00') == None


from python_code import dg_Definitions
from python_code import dg_RootCanvas

def test_dg_RootCanvas___init__():
    assert dg_RootCanvas.__init__(dg_RootCanvas('', dg_RootCanvas=dg_Definitions(), dg_RootCanvas101=set()), '', dg_RootCanvas=dg_Definitions(), dg_RootCanvas101=set()) == None


from python_code import dg_Point
from python_code import dg_Rotate

def test_dg_Rotate___init__():
    assert dg_Rotate.__init__(dg_Rotate('', dg_Rotate=dg_Point()), '', dg_Rotate=dg_Point()) == None


from python_code import dg_Scale

def test_dg_Scale___init__():
    assert dg_Scale.__init__(dg_Scale('', '\x00'), '\x00\x00', '') == None

def test_dg_Scale_nonnegativescale():
    assert dg_Scale.nonnegativescale(dg_Scale('', ''), '', '') == None


from python_code import dg_Skew

def test_dg_Skew___init__():
    assert dg_Skew.__init__(dg_Skew('', '\x00'), '\x00\x00', '') == None


from python_code import dg_StyleRule
from python_code import dg_StyleSelector

def test_dg_StyleSelector___init__():
    assert dg_StyleSelector.__init__(dg_StyleSelector('', '\x00', dg_StyleSelector=dg_StyleRule()), '\x00\x00', '', dg_StyleSelector=dg_StyleRule()) == None


from python_code import dg_Bounds
from python_code import dg_Text

def test_dg_Text___init__():
    assert dg_Text.__init__(dg_Text('', '\x00', dg_Text=dg_Bounds()), '\x00\x00', '', dg_Text=dg_Bounds()) == None

def test_dg_Text_dataCannotBeEmpty():
    assert dg_Text.dataCannotBeEmpty(dg_Text('', '', dg_Text=dg_Bounds()), '', '') == None


from python_code import dg_Translate

def test_dg_Translate___init__():
    assert dg_Translate.__init__(dg_Translate('', '\x00'), '\x00\x00', '') == None

