from python_code import dbl_ActivateObject
from python_code import dbl_Expression

def test_dbl_ActivateObject___init__():
    assert dbl_ActivateObject.__init__(dbl_ActivateObject(0, dbl_ActivateObject=dbl_Expression()), 0, dbl_ActivateObject=dbl_Expression()) == None


from python_code import dbl_BooleanPropertyType

def test_dbl_BooleanPropertyType___init__():
    assert dbl_BooleanPropertyType.__init__(dbl_BooleanPropertyType(''), '') == None


from python_code import dbl_Class
from python_code import dbl_Constructor
from python_code import dbl_ExtensionDefinition
from python_code import dbl_LocalScope
from python_code import dbl_Module
from python_code import dbl_SuperClassSpecification

def test_dbl_Class___init__():
    assert dbl_Class.__init__(dbl_Class(False, dbl_Class=dbl_Module(), dbl_Class56=dbl_SuperClassSpecification(), dbl_Class61=set(), dbl_Class63=set(), owningClass=set(), dbl_Class67=set(), dbl_Class73=dbl_LocalScope(), dbl_Class70=set(), Class=dbl_Constructor(), dbl_Class167=dbl_ExtensionDefinition()), False, dbl_Class=dbl_Module(), dbl_Class56=dbl_SuperClassSpecification(), dbl_Class61=set(), dbl_Class63=set(), owningClass=set(), dbl_Class67=set(), dbl_Class73=dbl_LocalScope(), dbl_Class70=set(), Class=dbl_Constructor(), dbl_Class167=dbl_ExtensionDefinition()) == None


from python_code import dbl_CompositePropertyType

def test_dbl_CompositePropertyType___init__():
    assert dbl_CompositePropertyType.__init__(dbl_CompositePropertyType(True), False) == None


from python_code import dbl_DoubleLiteral

def test_dbl_DoubleLiteral___init__():
    assert dbl_DoubleLiteral.__init__(dbl_DoubleLiteral(0.0), 0.0) == None


from python_code import dbl_ExpandTextPart

def test_dbl_ExpandTextPart___init__():
    assert dbl_ExpandTextPart.__init__(dbl_ExpandTextPart(''), '') == None


from python_code import dbl_Import
from python_code import dbl_Model

def test_dbl_Import___init__():
    assert dbl_Import.__init__(dbl_Import('', dbl_Import=dbl_Model(), dbl_Import31=dbl_Model()), '', dbl_Import=dbl_Model(), dbl_Import31=dbl_Model()) == None


from python_code import dbl_IntLiteral

def test_dbl_IntLiteral___init__():
    assert dbl_IntLiteral.__init__(dbl_IntLiteral(0), 0) == None


from python_code import dbl_IdExpr
from python_code import dbl_NamedElement

def test_dbl_NamedElement___init__():
    assert dbl_NamedElement.__init__(dbl_NamedElement('', dbl_NamedElement=dbl_IdExpr()), '', dbl_NamedElement=dbl_IdExpr()) == None


from python_code import dbl_Parameter
from python_code import dbl_Pattern
from python_code import dbl_Statement

def test_dbl_Pattern___init__():
    assert dbl_Pattern.__init__(dbl_Pattern(True, dbl_Pattern=dbl_Parameter(), dbl_Pattern217=dbl_Statement()), False, dbl_Pattern=dbl_Parameter(), dbl_Pattern217=dbl_Statement()) == None


from python_code import dbl_ReferencePropertyType

def test_dbl_ReferencePropertyType___init__():
    assert dbl_ReferencePropertyType.__init__(dbl_ReferencePropertyType(True), False) == None


from python_code import dbl_Expression
from python_code import dbl_SetExpansionContextStatement

def test_dbl_SetExpansionContextStatement___init__():
    assert dbl_SetExpansionContextStatement.__init__(dbl_SetExpansionContextStatement(True, dbl_SetExpansionContextStatement=dbl_Expression()), False, dbl_SetExpansionContextStatement=dbl_Expression()) == None


from python_code import dbl_StringLiteral

def test_dbl_StringLiteral___init__():
    assert dbl_StringLiteral.__init__(dbl_StringLiteral(''), '') == None


from python_code import dbl_TerminalExpr

def test_dbl_TerminalExpr___init__():
    assert dbl_TerminalExpr.__init__(dbl_TerminalExpr(''), '') == None


from python_code import dbl_TestStatement

def test_dbl_TestStatement___init__():
    assert dbl_TestStatement.__init__(dbl_TestStatement(0), 0) == None


from python_code import dbl_UniqueIdExpr

def test_dbl_UniqueIdExpr___init__():
    assert dbl_UniqueIdExpr.__init__(dbl_UniqueIdExpr(''), '') == None

