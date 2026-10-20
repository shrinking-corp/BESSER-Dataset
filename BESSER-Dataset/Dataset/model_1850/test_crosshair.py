from python_code import style_StyleLibrary
from python_code import style_StylePointer

def test_style_StyleLibrary___init__():
    assert style_StyleLibrary.__init__(style_StyleLibrary('\x00\x00', '', style_StyleLibrary=set(), style_StyleLibrary2=style_StylePointer()), '', '', style_StyleLibrary=set(), style_StyleLibrary2=style_StylePointer()) == None

