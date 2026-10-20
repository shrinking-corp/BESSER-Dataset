from python_code import fiacre_ArgumentVariable
from python_code import fiacre_NodeDecl

def test_fiacre_ArgumentVariable___init__():
    assert fiacre_ArgumentVariable.__init__(fiacre_ArgumentVariable(False, False, False, fiacre_ArgumentVariable=fiacre_NodeDecl()), False, False, False, fiacre_ArgumentVariable=fiacre_NodeDecl()) == None


from python_code import fiacre_BinExp
from python_code import fiacre_Exp

def test_fiacre_BinExp___init__():
    assert fiacre_BinExp.__init__(fiacre_BinExp('', fiacre_BinExp=fiacre_Exp(), fiacre_BinExp83=fiacre_Exp()), '', fiacre_BinExp=fiacre_Exp(), fiacre_BinExp83=fiacre_Exp()) == None


from python_code import fiacre_BoolLiteral

def test_fiacre_BoolLiteral___init__():
    assert fiacre_BoolLiteral.__init__(fiacre_BoolLiteral(True), False) == None


from python_code import fiacre_ConstrExp
from python_code import fiacre_Exp

def test_fiacre_ConstrExp___init__():
    assert fiacre_ConstrExp.__init__(fiacre_ConstrExp('', fiacre_ConstrExp=fiacre_Exp()), '', fiacre_ConstrExp=fiacre_Exp()) == None


from python_code import fiacre_ConstrPattern
from python_code import fiacre_Pattern

def test_fiacre_ConstrPattern___init__():
    assert fiacre_ConstrPattern.__init__(fiacre_ConstrPattern('', fiacre_ConstrPattern=fiacre_Pattern()), '', fiacre_ConstrPattern=fiacre_Pattern()) == None


from python_code import fiacre_Declaration
from python_code import fiacre_Program

def test_fiacre_Declaration___init__():
    assert fiacre_Declaration.__init__(fiacre_Declaration('', fiacre_Declaration=fiacre_Program()), '', fiacre_Declaration=fiacre_Program()) == None


from python_code import fiacre_FieldPattern
from python_code import fiacre_Pattern

def test_fiacre_FieldPattern___init__():
    assert fiacre_FieldPattern.__init__(fiacre_FieldPattern('', fiacre_FieldPattern=fiacre_Pattern()), '', fiacre_FieldPattern=fiacre_Pattern()) == None


from python_code import fiacre_FiniteBound

def test_fiacre_FiniteBound___init__():
    assert fiacre_FiniteBound.__init__(fiacre_FiniteBound(False, 0), False, 0) == None


from python_code import fiacre_Instance
from python_code import fiacre_NodeDecl

def test_fiacre_Instance___init__():
    assert fiacre_Instance.__init__(fiacre_Instance('', fiacre_Instance=fiacre_NodeDecl(), fiacre_Instance29=set(), fiacre_Instance31=set()), '', fiacre_Instance=fiacre_NodeDecl(), fiacre_Instance29=set(), fiacre_Instance31=set()) == None


from python_code import fiacre_LabeledType
from python_code import fiacre_Type

def test_fiacre_LabeledType___init__():
    assert fiacre_LabeledType.__init__(fiacre_LabeledType('', fiacre_LabeledType=fiacre_Type()), '', fiacre_LabeledType=fiacre_Type()) == None


from python_code import fiacre_Exp
from python_code import fiacre_Foreach
from python_code import fiacre_LocalVariable
from python_code import fiacre_NodeDecl

def test_fiacre_LocalVariable___init__():
    assert fiacre_LocalVariable.__init__(fiacre_LocalVariable(True, fiacre_LocalVariable=fiacre_NodeDecl(), fiacre_LocalVariable24=fiacre_Exp(), fiacre_LocalVariable188=fiacre_Foreach()), False, fiacre_LocalVariable=fiacre_NodeDecl(), fiacre_LocalVariable24=fiacre_Exp(), fiacre_LocalVariable188=fiacre_Foreach()) == None


from python_code import fiacre_NatLiteral

def test_fiacre_NatLiteral___init__():
    assert fiacre_NatLiteral.__init__(fiacre_NatLiteral(0), 0) == None


from python_code import fiacre_Exp
from python_code import fiacre_RecordElem

def test_fiacre_RecordElem___init__():
    assert fiacre_RecordElem.__init__(fiacre_RecordElem('', fiacre_RecordElem=fiacre_Exp()), '', fiacre_RecordElem=fiacre_Exp()) == None


from python_code import fiacre_Exp
from python_code import fiacre_UnExp

def test_fiacre_UnExp___init__():
    assert fiacre_UnExp.__init__(fiacre_UnExp('', fiacre_UnExp=fiacre_Exp()), '', fiacre_UnExp=fiacre_Exp()) == None


from python_code import fiacre_Exp
from python_code import fiacre_InlineRecord
from python_code import fiacre_ValuedField

def test_fiacre_ValuedField___init__():
    assert fiacre_ValuedField.__init__(fiacre_ValuedField('', fiacre_ValuedField=fiacre_InlineRecord(), fiacre_ValuedField115=fiacre_Exp()), '', fiacre_ValuedField=fiacre_InlineRecord(), fiacre_ValuedField115=fiacre_Exp()) == None


from python_code import fiacre_RefArg
from python_code import fiacre_Type
from python_code import fiacre_VarRef
from python_code import fiacre_Variable

def test_fiacre_Variable___init__():
    assert fiacre_Variable.__init__(fiacre_Variable('', fiacre_Variable=fiacre_VarRef(), fiacre_Variable133=fiacre_Type(), fiacre_Variable164=fiacre_RefArg()), '', fiacre_Variable=fiacre_VarRef(), fiacre_Variable133=fiacre_Type(), fiacre_Variable164=fiacre_RefArg()) == None

