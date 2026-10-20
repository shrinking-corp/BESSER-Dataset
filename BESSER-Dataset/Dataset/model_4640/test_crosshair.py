from python_code import notation_ArrowStyle

def test_notation_ArrowStyle___init__():
    assert notation_ArrowStyle.__init__(notation_ArrowStyle('', '\x00'), '\x00\x00', '') == None


from python_code import notation_BooleanListValueStyle

def test_notation_BooleanListValueStyle___init__():
    assert notation_BooleanListValueStyle.__init__(notation_BooleanListValueStyle(''), '') == None


from python_code import notation_BooleanValueStyle

def test_notation_BooleanValueStyle___init__():
    assert notation_BooleanValueStyle.__init__(notation_BooleanValueStyle(True), False) == None


from python_code import notation_ByteArrayValueStyle

def test_notation_ByteArrayValueStyle___init__():
    assert notation_ByteArrayValueStyle.__init__(notation_ByteArrayValueStyle(''), '') == None


from python_code import notation_CanonicalStyle

def test_notation_CanonicalStyle___init__():
    assert notation_CanonicalStyle.__init__(notation_CanonicalStyle(True), False) == None


from python_code import notation_DescriptionStyle

def test_notation_DescriptionStyle___init__():
    assert notation_DescriptionStyle.__init__(notation_DescriptionStyle(''), '') == None


from python_code import notation_DoubleListValueStyle

def test_notation_DoubleListValueStyle___init__():
    assert notation_DoubleListValueStyle.__init__(notation_DoubleListValueStyle(''), '') == None


from python_code import notation_DoubleValueStyle

def test_notation_DoubleValueStyle___init__():
    assert notation_DoubleValueStyle.__init__(notation_DoubleValueStyle(0.0), 0.0) == None


from python_code import notation_DrawerStyle

def test_notation_DrawerStyle___init__():
    assert notation_DrawerStyle.__init__(notation_DrawerStyle(True), False) == None


from python_code import notation_FillStyle

def test_notation_FillStyle___init__():
    assert notation_FillStyle.__init__(notation_FillStyle(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import notation_FilteringStyle

def test_notation_FilteringStyle___init__():
    assert notation_FilteringStyle.__init__(notation_FilteringStyle('\x00\x00', '', notation_FilteringStyle=set()), '', '', notation_FilteringStyle=set()) == None


from python_code import notation_FontStyle

def test_notation_FontStyle___init__():
    assert notation_FontStyle.__init__(notation_FontStyle(0, '', 0, False, False, False, False), 0, '\x00', 0, False, False, False, False) == None


from python_code import notation_HintedDiagramLinkStyle

def test_notation_HintedDiagramLinkStyle___init__():
    assert notation_HintedDiagramLinkStyle.__init__(notation_HintedDiagramLinkStyle(''), '') == None


from python_code import notation_IdentityAnchor

def test_notation_IdentityAnchor___init__():
    assert notation_IdentityAnchor.__init__(notation_IdentityAnchor(''), '') == None


from python_code import notation_Image
from python_code import notation_ImageBufferStyle

def test_notation_Image___init__():
    assert notation_Image.__init__(notation_Image('', notation_Image=notation_ImageBufferStyle()), '', notation_Image=notation_ImageBufferStyle()) == None


from python_code import notation_Bounds
from python_code import notation_ImageStyle

def test_notation_ImageStyle___init__():
    assert notation_ImageStyle.__init__(notation_ImageStyle('', '\x00', notation_ImageStyle=notation_Bounds()), '\x00\x00', '', notation_ImageStyle=notation_Bounds()) == None


from python_code import notation_IntListValueStyle

def test_notation_IntListValueStyle___init__():
    assert notation_IntListValueStyle.__init__(notation_IntListValueStyle(0), 0) == None


from python_code import notation_IntValueStyle

def test_notation_IntValueStyle___init__():
    assert notation_IntValueStyle.__init__(notation_IntValueStyle(0), 0) == None


from python_code import notation_LineStyle

def test_notation_LineStyle___init__():
    assert notation_LineStyle.__init__(notation_LineStyle(0, 0), 0, 0) == None


from python_code import notation_LineTypeStyle

def test_notation_LineTypeStyle___init__():
    assert notation_LineTypeStyle.__init__(notation_LineTypeStyle(''), '') == None


from python_code import notation_ListValueStyle

def test_notation_ListValueStyle___init__():
    assert notation_ListValueStyle.__init__(notation_ListValueStyle(''), '') == None


from python_code import notation_Location

def test_notation_Location___init__():
    assert notation_Location.__init__(notation_Location(0, 0), 0, 0) == None


from python_code import notation_NamedStyle

def test_notation_NamedStyle___init__():
    assert notation_NamedStyle.__init__(notation_NamedStyle(''), '') == None


from python_code import notation_PageStyle

def test_notation_PageStyle___init__():
    assert notation_PageStyle.__init__(notation_PageStyle(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import notation_Ratio

def test_notation_Ratio___init__():
    assert notation_Ratio.__init__(notation_Ratio(0.0), 0.0) == None


from python_code import notation_RelativeBendpoints

def test_notation_RelativeBendpoints___init__():
    assert notation_RelativeBendpoints.__init__(notation_RelativeBendpoints(''), '') == None


from python_code import notation_RoundedCornersStyle

def test_notation_RoundedCornersStyle___init__():
    assert notation_RoundedCornersStyle.__init__(notation_RoundedCornersStyle(0), 0) == None


from python_code import notation_RoutingStyle

def test_notation_RoutingStyle___init__():
    assert notation_RoutingStyle.__init__(notation_RoutingStyle('', '', False, False, '', '', False), '', '\x00', False, False, '', '', False) == None


from python_code import notation_SingleValueStyle

def test_notation_SingleValueStyle___init__():
    assert notation_SingleValueStyle.__init__(notation_SingleValueStyle(''), '') == None

def test_notation_SingleValueStyle_getValue():
    assert notation_SingleValueStyle.getValue(notation_SingleValueStyle('')) == None

def test_notation_SingleValueStyle_setValue():
    assert notation_SingleValueStyle.setValue(notation_SingleValueStyle(''), 0) == None


from python_code import notation_Size

def test_notation_Size___init__():
    assert notation_Size.__init__(notation_Size(0, 0), 0, 0) == None


from python_code import notation_SortingStyle

def test_notation_SortingStyle___init__():
    assert notation_SortingStyle.__init__(notation_SortingStyle('\x00\x00', '', notation_SortingStyle=set()), '', '', notation_SortingStyle=set()) == None


from python_code import notation_StringListValueStyle

def test_notation_StringListValueStyle___init__():
    assert notation_StringListValueStyle.__init__(notation_StringListValueStyle(''), '') == None


from python_code import notation_StringObjectConverter

def test_notation_StringObjectConverter___init__():
    assert notation_StringObjectConverter.__init__(notation_StringObjectConverter()) == None

def test_notation_StringObjectConverter_getObjectFromString():
    assert notation_StringObjectConverter.getObjectFromString(notation_StringObjectConverter(), '') == None

def test_notation_StringObjectConverter_getStringFromObject():
    assert notation_StringObjectConverter.getStringFromObject(notation_StringObjectConverter(), '') == None


from python_code import notation_StringValueStyle

def test_notation_StringValueStyle___init__():
    assert notation_StringValueStyle.__init__(notation_StringValueStyle(''), '') == None


from python_code import notation_TextStyle

def test_notation_TextStyle___init__():
    assert notation_TextStyle.__init__(notation_TextStyle(''), '') == None


from python_code import notation_TitleStyle

def test_notation_TitleStyle___init__():
    assert notation_TitleStyle.__init__(notation_TitleStyle(True), False) == None

