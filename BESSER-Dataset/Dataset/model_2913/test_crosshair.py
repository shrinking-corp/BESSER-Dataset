from python_code import lSGL_Enum
from python_code import lSGL_EnumItem

def test_lSGL_EnumItem___init__():
    assert lSGL_EnumItem.__init__(lSGL_EnumItem('', '\x00', lSGL_EnumItem=lSGL_Enum()), '\x00\x00', '', lSGL_EnumItem=lSGL_Enum()) == None


from python_code import lSGL_GeneratorAnnotation
from python_code import lSGL_GeneratorConfig

def test_lSGL_GeneratorConfig___init__():
    assert lSGL_GeneratorConfig.__init__(lSGL_GeneratorConfig('', '\x00', lSGL_GeneratorConfig=lSGL_GeneratorAnnotation()), '\x00\x00', '', lSGL_GeneratorConfig=lSGL_GeneratorAnnotation()) == None

