from python_code import dbl_ActivateObject
from python_code import dbl_Expression

def test_dbl_ActivateObject___init__():
    assert dbl_ActivateObject.__init__(dbl_ActivateObject(0, dbl_ActivateObject=dbl_Expression()), 0, dbl_ActivateObject=dbl_Expression()) == None


from python_code import dbl_Annotation
from python_code import dbl_AnnotationItem

def test_dbl_AnnotationItem___init__():
    assert dbl_AnnotationItem.__init__(dbl_AnnotationItem('', '\x00', dbl_AnnotationItem=dbl_Annotation()), '\x00\x00', '', dbl_AnnotationItem=dbl_Annotation()) == None


from python_code import dbl_DoubleLiteral

def test_dbl_DoubleLiteral___init__():
    assert dbl_DoubleLiteral.__init__(dbl_DoubleLiteral(0.0), 0.0) == None


from python_code import dbl_ExpandTextPart

def test_dbl_ExpandTextPart___init__():
    assert dbl_ExpandTextPart.__init__(dbl_ExpandTextPart(''), '') == None


from python_code import dbl_ExpansionStatement
from python_code import dbl_IdExpr

def test_dbl_ExpansionStatement___init__():
    assert dbl_ExpansionStatement.__init__(dbl_ExpansionStatement(False, True, False, dbl_ExpansionStatement174=set(), dbl_ExpansionStatement=dbl_IdExpr(), dbl_ExpansionStatement172=set()), False, False, False, dbl_ExpansionStatement174=set(), dbl_ExpansionStatement=dbl_IdExpr(), dbl_ExpansionStatement172=set()) == None


from python_code import dbl_ExtensibleElement

def test_dbl_ExtensibleElement___init__():
    assert dbl_ExtensibleElement.__init__(dbl_ExtensibleElement('', False), '', False) == None


from python_code import dbl_Import
from python_code import dbl_Model

def test_dbl_Import___init__():
    assert dbl_Import.__init__(dbl_Import('', dbl_Import=dbl_Model(), dbl_Import5=dbl_Model()), '', dbl_Import=dbl_Model(), dbl_Import5=dbl_Model()) == None


from python_code import dbl_IntLiteral

def test_dbl_IntLiteral___init__():
    assert dbl_IntLiteral.__init__(dbl_IntLiteral(0), 0) == None


from python_code import dbl_Keyword

def test_dbl_Keyword___init__():
    assert dbl_Keyword.__init__(dbl_Keyword(''), '') == None


from python_code import dbl_IdExpr
from python_code import dbl_NamedElement

def test_dbl_NamedElement___init__():
    assert dbl_NamedElement.__init__(dbl_NamedElement('', dbl_NamedElement=dbl_IdExpr()), '', dbl_NamedElement=dbl_IdExpr()) == None


from python_code import dbl_Parameter
from python_code import dbl_Pattern
from python_code import dbl_Statement

def test_dbl_Pattern___init__():
    assert dbl_Pattern.__init__(dbl_Pattern(True, dbl_Pattern193=dbl_Statement(), dbl_Pattern=dbl_Parameter()), False, dbl_Pattern193=dbl_Statement(), dbl_Pattern=dbl_Parameter()) == None


from python_code import dbl_StringLiteral

def test_dbl_StringLiteral___init__():
    assert dbl_StringLiteral.__init__(dbl_StringLiteral(''), '') == None


from python_code import dbl_StructuralSymbolReference

def test_dbl_StructuralSymbolReference___init__():
    assert dbl_StructuralSymbolReference.__init__(dbl_StructuralSymbolReference(False, False, False, False), False, False, False, True) == None


from python_code import dbl_TestStatement

def test_dbl_TestStatement___init__():
    assert dbl_TestStatement.__init__(dbl_TestStatement(0), 0) == None

