from python_code import geoff_Color

def test_geoff_Color___init__():
    assert geoff_Color.__init__(geoff_Color(0, 0, 0, 0.0), 0, 0, 0, 0.0) == None


from python_code import geoff_Descriptive

def test_geoff_Descriptive___init__():
    assert geoff_Descriptive.__init__(geoff_Descriptive('', '\x00'), '\x00\x00', '') == None


from python_code import Geometry
from python_code import Style
from python_code import geoff_Feature

def test_geoff_Feature___init__():
    assert geoff_Feature.__init__(geoff_Feature('', geoff_Feature=Geometry(), geoff_Feature11=Style(), geoff_Feature13=set()), '', geoff_Feature=Geometry(), geoff_Feature11=Style(), geoff_Feature13=set()) == None


from python_code import geoff_Identifiable

def test_geoff_Identifiable___init__():
    assert geoff_Identifiable.__init__(geoff_Identifiable(''), '') == None


from python_code import Style
from python_code import geoff_StyleEntry

def test_geoff_StyleEntry___init__():
    assert geoff_StyleEntry.__init__(geoff_StyleEntry('', geoff_StyleEntry=Style()), '', geoff_StyleEntry=Style()) == None


from python_code import geoff_XYZLocation

def test_geoff_XYZLocation___init__():
    assert geoff_XYZLocation.__init__(geoff_XYZLocation(0.0, 0.0, 0.0), 0.0, 0.0, 0.0) == None


from python_code import geoff_source_BingMaps

def test_geoff_source_BingMaps___init__():
    assert geoff_source_BingMaps.__init__(geoff_source_BingMaps('', '\x00'), '\x00\x00', '') == None


from python_code import geoff_source_MapQuest

def test_geoff_source_MapQuest___init__():
    assert geoff_source_MapQuest.__init__(geoff_source_MapQuest(''), '') == None


from python_code import geoff_layer_Layer
from python_code import geoff_source_VectorSource

def test_geoff_source_VectorSource___init__():
    assert geoff_source_VectorSource.__init__(geoff_source_VectorSource('', '', '', geoff_source_VectorSource=set(), Source=geoff_layer_Layer()), '', '', '', geoff_source_VectorSource=set(), Source=geoff_layer_Layer()) == None


from python_code import Fill
from python_code import Image
from python_code import Stroke
from python_code import Text
from python_code import geoff_style_Circle
from python_code import geoff_style_Style

def test_geoff_style_Circle___init__():
    assert geoff_style_Circle.__init__(geoff_style_Circle(0.0, geoff_style_Circle=Fill(), geoff_style_Circle37=Stroke(), Image=geoff_style_Style('', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text())), 0.0, geoff_style_Circle=Fill(), geoff_style_Circle37=Stroke(), Image=geoff_style_Style('', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text())) == None


from python_code import Fill
from python_code import Image
from python_code import Stroke
from python_code import Text
from python_code import geoff_style_Icon
from python_code import geoff_style_Style

def test_geoff_style_Icon___init__():
    assert geoff_style_Icon.__init__(geoff_style_Icon('', Image=geoff_style_Style('\x00', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text())), '', Image=geoff_style_Style('', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text())) == None


from python_code import geoff_style_Stroke
from python_code import style_geoff_Color

def test_geoff_style_Stroke___init__():
    assert geoff_style_Stroke.__init__(geoff_style_Stroke('', '', '', '', 0.0, geoff_style_Stroke=style_geoff_Color()), '', '', '', '', 0.0, geoff_style_Stroke=style_geoff_Color()) == None


from python_code import Fill
from python_code import Image
from python_code import Stroke
from python_code import Text
from python_code import geoff_style_Style

def test_geoff_style_Style___init__():
    assert geoff_style_Style.__init__(geoff_style_Style('', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text()), '\x00', geoff_style_Style=Image(), geoff_style_Style26=Fill(), geoff_style_Style28=Stroke(), geoff_style_Style30=Text()) == None


from python_code import Fill
from python_code import Stroke
from python_code import geoff_style_Text

def test_geoff_style_Text___init__():
    assert geoff_style_Text.__init__(geoff_style_Text('', '', '', '', 0.0, 0.0, '', '', geoff_style_Text=Fill(), geoff_style_Text42=Stroke()), '', '', '', '', 0.0, 0.0, '', '', geoff_style_Text=Fill(), geoff_style_Text42=Stroke()) == None

