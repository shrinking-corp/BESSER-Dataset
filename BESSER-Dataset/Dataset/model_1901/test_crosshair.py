from python_code import fIDL_Attribute
from python_code import fIDL_AttributedDeclaration

def test_fIDL_Attribute___init__():
    assert fIDL_Attribute.__init__(fIDL_Attribute('', '\x00', fIDL_Attribute=fIDL_AttributedDeclaration()), '\x00\x00', '', fIDL_Attribute=fIDL_AttributedDeclaration()) == None


from python_code import fIDL_BooleanLiteral

def test_fIDL_BooleanLiteral___init__():
    assert fIDL_BooleanLiteral.__init__(fIDL_BooleanLiteral(True), False) == None


from python_code import fIDL_HandleType

def test_fIDL_HandleType___init__():
    assert fIDL_HandleType.__init__(fIDL_HandleType('', False), '', False) == None


from python_code import fIDL_InterfaceMethod
from python_code import fIDL_InterfaceParameters
from python_code import fIDL_ParameterList

def test_fIDL_InterfaceParameters___init__():
    assert fIDL_InterfaceParameters.__init__(fIDL_InterfaceParameters('', '\x00', fIDL_InterfaceParameters23=fIDL_ParameterList(), fIDL_InterfaceParameters25=fIDL_ParameterList(), fIDL_InterfaceParameters=fIDL_InterfaceMethod()), '\x00\x00', '', fIDL_InterfaceParameters23=fIDL_ParameterList(), fIDL_InterfaceParameters25=fIDL_ParameterList(), fIDL_InterfaceParameters=fIDL_InterfaceMethod()) == None


from python_code import fIDL_LibraryHeader

def test_fIDL_LibraryHeader___init__():
    assert fIDL_LibraryHeader.__init__(fIDL_LibraryHeader('', fIDL_LibraryHeader=set(), fIDL_LibraryHeader2=set()), '', fIDL_LibraryHeader=set(), fIDL_LibraryHeader2=set()) == None


from python_code import fIDL_Parameter
from python_code import fIDL_ParameterList
from python_code import fIDL_Type

def test_fIDL_Parameter___init__():
    assert fIDL_Parameter.__init__(fIDL_Parameter('', fIDL_Parameter=fIDL_ParameterList(), fIDL_Parameter30=fIDL_Type()), '', fIDL_Parameter=fIDL_ParameterList(), fIDL_Parameter30=fIDL_Type()) == None


from python_code import fIDL_Type
from python_code import fIDL_UnionField

def test_fIDL_UnionField___init__():
    assert fIDL_UnionField.__init__(fIDL_UnionField('', fIDL_UnionField=fIDL_Type()), '', fIDL_UnionField=fIDL_Type()) == None

