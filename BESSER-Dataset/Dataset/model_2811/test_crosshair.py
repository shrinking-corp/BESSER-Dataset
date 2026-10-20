from python_code import krendering_KAction
from python_code import krendering_KRendering

def test_krendering_KAction___init__():
    assert krendering_KAction.__init__(krendering_KAction('', '', '', '', '', krendering_KAction=krendering_KRendering()), '', '', '', '', '', krendering_KAction=krendering_KRendering()) == None


from python_code import krendering_KArc

def test_krendering_KArc___init__():
    assert krendering_KArc.__init__(krendering_KArc(0.0, 0.0, ''), 0.0, 0.0, '') == None


from python_code import krendering_KCustomRendering

def test_krendering_KCustomRendering___init__():
    assert krendering_KCustomRendering.__init__(krendering_KCustomRendering('', '', '\x00\x00'), '', '', '') == None


from python_code import krendering_KDecoratorPlacementData

def test_krendering_KDecoratorPlacementData___init__():
    assert krendering_KDecoratorPlacementData.__init__(krendering_KDecoratorPlacementData(0.0, 0.0, 0.0, False, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, False, 0.0, 0.0, 0.0) == None


from python_code import krendering_KFontBold

def test_krendering_KFontBold___init__():
    assert krendering_KFontBold.__init__(krendering_KFontBold(True), False) == None


from python_code import krendering_KFontItalic

def test_krendering_KFontItalic___init__():
    assert krendering_KFontItalic.__init__(krendering_KFontItalic(True), False) == None


from python_code import krendering_KFontName

def test_krendering_KFontName___init__():
    assert krendering_KFontName.__init__(krendering_KFontName(''), '') == None


from python_code import krendering_KFontSize

def test_krendering_KFontSize___init__():
    assert krendering_KFontSize.__init__(krendering_KFontSize(0, False), 0, False) == None


from python_code import krendering_KGridPlacementData

def test_krendering_KGridPlacementData___init__():
    assert krendering_KGridPlacementData.__init__(krendering_KGridPlacementData(0.0, 0.0, '', ''), 0.0, 0.0, '', '') == None


from python_code import krendering_KHorizontalAlignment

def test_krendering_KHorizontalAlignment___init__():
    assert krendering_KHorizontalAlignment.__init__(krendering_KHorizontalAlignment(''), '') == None


from python_code import krendering_KImage
from python_code import krendering_KRendering

def test_krendering_KImage___init__():
    assert krendering_KImage.__init__(krendering_KImage('', '', '\x00\x00', krendering_KImage=krendering_KRendering()), '', '', '', krendering_KImage=krendering_KRendering()) == None


from python_code import krendering_KInvisibility

def test_krendering_KInvisibility___init__():
    assert krendering_KInvisibility.__init__(krendering_KInvisibility(True), False) == None


from python_code import krendering_KLineCap

def test_krendering_KLineCap___init__():
    assert krendering_KLineCap.__init__(krendering_KLineCap(''), '') == None


from python_code import krendering_KLineJoin

def test_krendering_KLineJoin___init__():
    assert krendering_KLineJoin.__init__(krendering_KLineJoin('\x00', 0.0), '', 0.0) == None


from python_code import krendering_KLineStyle

def test_krendering_KLineStyle___init__():
    assert krendering_KLineStyle.__init__(krendering_KLineStyle('', 0.0, 0.0), '', 0.0, 0.0) == None


from python_code import krendering_KLineWidth

def test_krendering_KLineWidth___init__():
    assert krendering_KLineWidth.__init__(krendering_KLineWidth(0.0), 0.0) == None


from python_code import krendering_KRoundedBendsPolyline

def test_krendering_KRoundedBendsPolyline___init__():
    assert krendering_KRoundedBendsPolyline.__init__(krendering_KRoundedBendsPolyline(0.0), 0.0) == None


from python_code import krendering_KRoundedRectangle

def test_krendering_KRoundedRectangle___init__():
    assert krendering_KRoundedRectangle.__init__(krendering_KRoundedRectangle(0.0, 0.0), 0.0, 0.0) == None


from python_code import krendering_KText

def test_krendering_KText___init__():
    assert krendering_KText.__init__(krendering_KText('', False, False), '\x00', False, False) == None


from python_code import krendering_KVerticalAlignment

def test_krendering_KVerticalAlignment___init__():
    assert krendering_KVerticalAlignment.__init__(krendering_KVerticalAlignment(''), '') == None


from python_code import krendering_KXPosition

def test_krendering_KXPosition___init__():
    assert krendering_KXPosition.__init__(krendering_KXPosition(0.0, 0.0), 0.0, 0.0) == None

def test_krendering_KXPosition_equals():
    assert krendering_KXPosition.equals(krendering_KXPosition(0.0, 0.0), 0) == None

def test_krendering_KXPosition_setPosition():
    assert krendering_KXPosition.setPosition(krendering_KXPosition(0.0, 0.0), '', '') == None


from python_code import krendering_KYPosition

def test_krendering_KYPosition___init__():
    assert krendering_KYPosition.__init__(krendering_KYPosition(0.0, 0.0), 0.0, 0.0) == None

def test_krendering_KYPosition_setPosition():
    assert krendering_KYPosition.setPosition(krendering_KYPosition(0.0, 0.0), '', '') == None

def test_krendering_KYPosition_equals():
    assert krendering_KYPosition.equals(krendering_KYPosition(0.0, 0.0), 0) == None

