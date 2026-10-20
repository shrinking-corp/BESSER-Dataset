from python_code import AsmL_BooleanConstant

def test_AsmL_BooleanConstant___init__():
    assert AsmL_BooleanConstant.__init__(AsmL_BooleanConstant(''), '') == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Case
from python_code import AsmL_Structure

def test_AsmL_Case___init__():
    assert AsmL_Case.__init__(AsmL_Case('', AsmL_Case=set(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile())), '', AsmL_Case=set(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile())) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Class

def test_AsmL_Class___init__():
    assert AsmL_Class.__init__(AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile()), '', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Enumeration

def test_AsmL_Enumeration___init__():
    assert AsmL_Enumeration.__init__(AsmL_Enumeration('', AsmL_Enumeration=set(), AsmLElement=AsmL_AsmLFile()), '', AsmL_Enumeration=set(), AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_ExistsTerm

def test_AsmL_ExistsTerm___init__():
    assert AsmL_ExistsTerm.__init__(AsmL_ExistsTerm(''), '') == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Function
from python_code import Body

def test_AsmL_Function___init__():
    assert AsmL_Function.__init__(AsmL_Function('', AsmL_Function=Body(), AsmLElement=AsmL_AsmLFile()), '', AsmL_Function=Body(), AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_IntegerConstant

def test_AsmL_IntegerConstant___init__():
    assert AsmL_IntegerConstant.__init__(AsmL_IntegerConstant(''), '') == None


from python_code import AsmL_LocatedElement

def test_AsmL_LocatedElement___init__():
    assert AsmL_LocatedElement.__init__(AsmL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Class
from python_code import AsmL_Method
from python_code import Type

def test_AsmL_Method___init__():
    assert AsmL_Method.__init__(AsmL_Method('', '', '', '', ownerMethod=Type(), ownerMethod27=set(), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())), '', '', '', '', ownerMethod=Type(), ownerMethod27=set(), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Class
from python_code import AsmL_MapType
from python_code import AsmL_Method
from python_code import AsmL_NamedType
from python_code import AsmL_Parameter
from python_code import AsmL_SequenceType
from python_code import AsmL_SetType
from python_code import AsmL_Structure
from python_code import AsmL_TupletType
from python_code import AsmL_VarDeclaration
from python_code import Method
from python_code import Type

def test_AsmL_NamedType___init__():
    assert AsmL_NamedType.__init__(AsmL_NamedType('', Type98=AsmL_MapType(), Type29=AsmL_Parameter('', ownerParameter=AsmL_TupletType(), parameters=Method()), Type=AsmL_VarDeclaration('', '', '', '', ownerDeclaration=Type(), AsmLElement=AsmL_AsmLFile(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())), Type101=AsmL_MapType(), Type105=AsmL_SetType(), Type103=AsmL_TupletType(), Type107=AsmL_SequenceType(), Type25=AsmL_Method('', '', '', '', ownerMethod=Type(), ownerMethod27=set(), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile()))), '', Type98=AsmL_MapType(), Type29=AsmL_Parameter('', ownerParameter=Type(), parameters=Method()), Type=AsmL_VarDeclaration('', '', '', '\x00', ownerDeclaration=Type(), AsmLElement=AsmL_AsmLFile(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())), Type101=AsmL_MapType(), Type105=AsmL_SetType(), Type103=AsmL_TupletType(), Type107=AsmL_SequenceType(), Type25=AsmL_Method('', '', '', '', ownerMethod=AsmL_MapType(), ownerMethod27=set(), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile()))) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Namespace

def test_AsmL_Namespace___init__():
    assert AsmL_Namespace.__init__(AsmL_Namespace('', AsmLElement=AsmL_AsmLFile()), '', AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_Parameter
from python_code import Method
from python_code import Type

def test_AsmL_Parameter___init__():
    assert AsmL_Parameter.__init__(AsmL_Parameter('\x00', ownerParameter=Type(), parameters=Method()), '', ownerParameter=Type(), parameters=Method()) == None


from python_code import AsmL_Body
from python_code import AsmL_Step

def test_AsmL_Step___init__():
    assert AsmL_Step.__init__(AsmL_Step('', Rule=AsmL_Body()), '', Rule=AsmL_Body()) == None


from python_code import AsmL_StringConstant

def test_AsmL_StringConstant___init__():
    assert AsmL_StringConstant.__init__(AsmL_StringConstant(''), '') == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Structure

def test_AsmL_Structure___init__():
    assert AsmL_Structure.__init__(AsmL_Structure('\x00\x00', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()), '', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Type
from python_code import Method
from python_code import Parameter
from python_code import VarDeclaration

def test_AsmL_Type___init__():
    assert AsmL_Type.__init__(AsmL_Type('', type=VarDeclaration(), returnType=Method(), type95=Parameter(), AsmLElement=AsmL_AsmLFile()), '', type=VarDeclaration(), returnType=Method(), type95=Parameter(), AsmLElement=AsmL_AsmLFile()) == None


from python_code import AsmL_AsmLFile
from python_code import AsmL_Class
from python_code import AsmL_Structure
from python_code import AsmL_VarDeclaration
from python_code import Type

def test_AsmL_VarDeclaration___init__():
    assert AsmL_VarDeclaration.__init__(AsmL_VarDeclaration('', '', '', '', ownerDeclaration=Type(), AsmLElement=AsmL_AsmLFile(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())), '', '', '\x00', '', ownerDeclaration=Type(), AsmLElement=AsmL_AsmLFile(), VarOrCase=AsmL_Structure('', '', ownerStructure=set(), AsmLElement=AsmL_AsmLFile()), VarOrMethod=AsmL_Class('', '', '', ownerClass=set(), AsmLElement=AsmL_AsmLFile())) == None

