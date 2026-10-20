from python_code import presentation_common_NamedElement

def test_presentation_common_NamedElement___init__():
    assert presentation_common_NamedElement.__init__(presentation_common_NamedElement(''), '') == None


from python_code import presentation_general_CoordinateDefinition

def test_presentation_general_CoordinateDefinition___init__():
    assert presentation_general_CoordinateDefinition.__init__(presentation_general_CoordinateDefinition('', '', '\x00\x00'), '', '', '') == None


from python_code import presentation_general_NamedElement

def test_presentation_general_NamedElement___init__():
    assert presentation_general_NamedElement.__init__(presentation_general_NamedElement(''), '') == None


from python_code import presentation_literal_BooleanLiteral

def test_presentation_literal_BooleanLiteral___init__():
    assert presentation_literal_BooleanLiteral.__init__(presentation_literal_BooleanLiteral(True), False) == None


from python_code import presentation_literal_NumberLiteral

def test_presentation_literal_NumberLiteral___init__():
    assert presentation_literal_NumberLiteral.__init__(presentation_literal_NumberLiteral(0), 0) == None


from python_code import presentation_literal_TextLiteral

def test_presentation_literal_TextLiteral___init__():
    assert presentation_literal_TextLiteral.__init__(presentation_literal_TextLiteral(''), '') == None


from python_code import FilenameParameter
from python_code import presentation_picture_Bitmap

def test_presentation_picture_Bitmap___init__():
    assert presentation_picture_Bitmap.__init__(presentation_picture_Bitmap('', presentation_picture_Bitmap=FilenameParameter()), '', presentation_picture_Bitmap=FilenameParameter()) == None

