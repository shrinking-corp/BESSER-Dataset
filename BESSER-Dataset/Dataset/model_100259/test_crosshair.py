from python_code import xdoc_Code

def test_xdoc_Code___init__():
    assert xdoc_Code.__init__(xdoc_Code(''), '') == None


from python_code import xdoc_Glossary
from python_code import xdoc_GlossaryEntry

def test_xdoc_GlossaryEntry___init__():
    assert xdoc_GlossaryEntry.__init__(xdoc_GlossaryEntry('\x00\x00', '', xdoc_GlossaryEntry=set(), xdoc_GlossaryEntry67=xdoc_Glossary()), '', '', xdoc_GlossaryEntry=set(), xdoc_GlossaryEntry67=xdoc_Glossary()) == None


from python_code import xdoc_Identifiable
from python_code import xdoc_Ref

def test_xdoc_Identifiable___init__():
    assert xdoc_Identifiable.__init__(xdoc_Identifiable('', xdoc_Identifiable=xdoc_Ref()), '', xdoc_Identifiable=xdoc_Ref()) == None


from python_code import xdoc_ImageProxy
from python_code import xdoc_ImageRef

def test_xdoc_ImageRef___init__():
    assert xdoc_ImageRef.__init__(xdoc_ImageRef('', '', '', '', '', xdoc_ImageRef=xdoc_ImageProxy()), '', '', '', '', '', xdoc_ImageRef=xdoc_ImageProxy()) == None


from python_code import xdoc_CodeBlock
from python_code import xdoc_Document
from python_code import xdoc_LangDef

def test_xdoc_LangDef___init__():
    assert xdoc_LangDef.__init__(xdoc_LangDef('', '\x00', xdoc_LangDef=xdoc_Document(), xdoc_LangDef62=xdoc_CodeBlock()), '\x00\x00', '', xdoc_LangDef=xdoc_Document(), xdoc_LangDef62=xdoc_CodeBlock()) == None


from python_code import xdoc_Link

def test_xdoc_Link___init__():
    assert xdoc_Link.__init__(xdoc_Link('', '\x00'), '\x00\x00', '') == None


from python_code import xdoc_TextPart

def test_xdoc_TextPart___init__():
    assert xdoc_TextPart.__init__(xdoc_TextPart(''), '') == None


from python_code import xdoc_Todo

def test_xdoc_Todo___init__():
    assert xdoc_Todo.__init__(xdoc_Todo(''), '') == None

