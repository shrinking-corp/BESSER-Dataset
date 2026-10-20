from python_code import umm_CCLibrary

def test_umm_CCLibrary___init__():
    assert umm_CCLibrary.__init__(umm_CCLibrary('', '', '\x00', '', '', '', '', '', umm_CCLibrary=set()), '', '', '', '', '\x00', '', '', '', umm_CCLibrary=set()) == None


from python_code import umm_CDTLibrary

def test_umm_CDTLibrary___init__():
    assert umm_CDTLibrary.__init__(umm_CDTLibrary('', '', '\x00', '', '', '', '', '', umm_CDTLibrary=set()), '', '', '', '', '\x00', '', '', '', umm_CDTLibrary=set()) == None


from python_code import umm_CDT_Supplement

def test_umm_CDT_Supplement___init__():
    assert umm_CDT_Supplement.__init__(umm_CDT_Supplement('', '', '\x00\x00'), '', '', '') == None


from python_code import umm_CodelistEntry
from python_code import umm_Original
from python_code import umm_Subset

def test_umm_CodelistEntry___init__():
    assert umm_CodelistEntry.__init__(umm_CodelistEntry('', '\x00', umm_CodelistEntry=umm_Original(), umm_CodelistEntry51=umm_Subset()), '\x00\x00', '', umm_CodelistEntry=umm_Original(), umm_CodelistEntry51=umm_Subset()) == None


from python_code import umm_Content

def test_umm_Content___init__():
    assert umm_Content.__init__(umm_Content(0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0) == None


from python_code import umm_Constraint
from python_code import umm_ContextRef

def test_umm_ContextRef___init__():
    assert umm_ContextRef.__init__(umm_ContextRef('', umm_ContextRef=umm_Constraint()), '', umm_ContextRef=umm_Constraint()) == None


from python_code import umm_ENUMLibrary

def test_umm_ENUMLibrary___init__():
    assert umm_ENUMLibrary.__init__(umm_ENUMLibrary('', '', '\x00', '', '', '', '', '', umm_ENUMLibrary=set()), '', '', '', '', '\x00', '', '', '', umm_ENUMLibrary=set()) == None


from python_code import umm_Library

def test_umm_Library___init__():
    assert umm_Library.__init__(umm_Library(''), '') == None


from python_code import umm_OclEnumerationLiteral

def test_umm_OclEnumerationLiteral___init__():
    assert umm_OclEnumerationLiteral.__init__(umm_OclEnumerationLiteral(''), '') == None


from python_code import umm_OclIntegerLiteral

def test_umm_OclIntegerLiteral___init__():
    assert umm_OclIntegerLiteral.__init__(umm_OclIntegerLiteral(0), 0) == None


from python_code import umm_OclPathFeatureHead
from python_code import umm_OclPathTail
from python_code import umm_OclRef

def test_umm_OclRef___init__():
    assert umm_OclRef.__init__(umm_OclRef('', '\x00', umm_OclRef=umm_OclPathFeatureHead(), umm_OclRef78=umm_OclPathTail()), '\x00\x00', '', umm_OclRef=umm_OclPathFeatureHead(), umm_OclRef78=umm_OclPathTail()) == None


from python_code import umm_OclStringLiteral

def test_umm_OclStringLiteral___init__():
    assert umm_OclStringLiteral.__init__(umm_OclStringLiteral(''), '') == None


from python_code import umm_Supplement

def test_umm_Supplement___init__():
    assert umm_Supplement.__init__(umm_Supplement('', '', '\x00\x00'), '', '', '') == None


from python_code import umm_Constraint
from python_code import umm_TC_Constraint

def test_umm_TC_Constraint___init__():
    assert umm_TC_Constraint.__init__(umm_TC_Constraint('', '', '\x00\x00', umm_TC_Constraint=umm_Constraint()), '', '', '', umm_TC_Constraint=umm_Constraint()) == None

