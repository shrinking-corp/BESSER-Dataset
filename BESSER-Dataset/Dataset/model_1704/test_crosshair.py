from python_code import library_Library

def test_library_Library___init__():
    assert library_Library.__init__(library_Library('', library_Library=set()), '', library_Library=set()) == None


from python_code import library_TextAnnotation

def test_library_TextAnnotation___init__():
    assert library_TextAnnotation.__init__(library_TextAnnotation('', '\x00'), '\x00\x00', '') == None

