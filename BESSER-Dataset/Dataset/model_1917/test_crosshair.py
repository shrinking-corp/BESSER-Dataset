from python_code import mancoosimm_MimeType
from python_code import mancoosimm_MimeTypeHandler
from python_code import mancoosimm_MimeTypeHandlerCache

def test_mancoosimm_MimeType___init__():
    assert mancoosimm_MimeType.__init__(mancoosimm_MimeType('\x00\x00', '', MimeType=mancoosimm_MimeTypeHandlerCache(), MimeType210=mancoosimm_MimeTypeHandler(), type=set(), mimeTypes=mancoosimm_MimeTypeHandlerCache()), '', '', MimeType=mancoosimm_MimeTypeHandlerCache(), MimeType210=mancoosimm_MimeTypeHandler(), type=set(), mimeTypes=mancoosimm_MimeTypeHandlerCache()) == None


from python_code import mancoosimm_Environment
from python_code import mancoosimm_Module
from python_code import mancoosimm_ModuleCache

def test_mancoosimm_ModuleCache___init__():
    assert mancoosimm_ModuleCache.__init__(mancoosimm_ModuleCache('', ModuleCache=mancoosimm_Environment(), moduleCache=set(), moduleCache236=mancoosimm_Environment(), ModuleCache241=mancoosimm_Module()), '', ModuleCache=mancoosimm_Environment(), moduleCache=set(), moduleCache236=mancoosimm_Environment(), ModuleCache241=mancoosimm_Module()) == None


from python_code import mancoosimm_NamedElement

def test_mancoosimm_NamedElement___init__():
    assert mancoosimm_NamedElement.__init__(mancoosimm_NamedElement(''), '') == None


from python_code import mancoosimm_Conflict
from python_code import mancoosimm_SingleConflict

def test_mancoosimm_SingleConflict___init__():
    assert mancoosimm_SingleConflict.__init__(mancoosimm_SingleConflict('', '\x00', singleConflict=mancoosimm_Conflict(), SingleConflict=mancoosimm_Conflict()), '\x00\x00', '', singleConflict=mancoosimm_Conflict(), SingleConflict=mancoosimm_Conflict()) == None


from python_code import mancoosimm_Dependence
from python_code import mancoosimm_SingleDep

def test_mancoosimm_SingleDep___init__():
    assert mancoosimm_SingleDep.__init__(mancoosimm_SingleDep('', '\x00', SingleDep=mancoosimm_Dependence(), singleDep=mancoosimm_Dependence()), '\x00\x00', '', SingleDep=mancoosimm_Dependence(), singleDep=mancoosimm_Dependence()) == None


from python_code import mancoosimm_Environment
from python_code import mancoosimm_XFont
from python_code import mancoosimm_XFontCache

def test_mancoosimm_XFontCache___init__():
    assert mancoosimm_XFontCache.__init__(mancoosimm_XFontCache('', XFontCache=mancoosimm_Environment(), xfontCache=set(), xfontCaches=mancoosimm_Environment(), XFontCache221=mancoosimm_XFont()), '', XFontCache=mancoosimm_Environment(), xfontCache=set(), xfontCaches=mancoosimm_Environment(), XFontCache221=mancoosimm_XFont()) == None

