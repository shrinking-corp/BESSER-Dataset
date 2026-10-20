from python_code import scribbleTraceDsl_Messagetransfer
from python_code import scribbleTraceDsl_Parameter

def test_scribbleTraceDsl_Parameter___init__():
    assert scribbleTraceDsl_Parameter.__init__(scribbleTraceDsl_Parameter('', '\x00', scribbleTraceDsl_Parameter=scribbleTraceDsl_Messagetransfer()), '\x00\x00', '', scribbleTraceDsl_Parameter=scribbleTraceDsl_Messagetransfer()) == None


from python_code import scribbleTraceDsl_Trace

def test_scribbleTraceDsl_Trace___init__():
    assert scribbleTraceDsl_Trace.__init__(scribbleTraceDsl_Trace('', scribbleTraceDsl_Trace=set()), '', scribbleTraceDsl_Trace=set()) == None

