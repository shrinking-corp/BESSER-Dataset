from python_code import OCL_BooleanLiteralExp

def test_OCL_BooleanLiteralExp___init__():
    assert OCL_BooleanLiteralExp.__init__(OCL_BooleanLiteralExp(''), '') == None


from python_code import OCL_Class
from python_code import OCL_CollectionType
from python_code import OCL_Comment
from python_code import OCL_Operation
from python_code import OCL_Package
from python_code import OCL_TypedElement

def test_OCL_Class___init__():
    assert OCL_Class.__init__(OCL_Class('', OCL_Class=set(), OCL_Class41=set(), Type27=OCL_Package('', OCL_Package=set(), OCL_Package29=set(), NamedElement=OCL_Comment()), Type36=OCL_Operation(), Type=OCL_TypedElement(), Type45=OCL_CollectionType()), '', OCL_Class=set(), OCL_Class41=set(), Type27=OCL_Package('\x00', OCL_Package=set(), OCL_Package29=set(), NamedElement=OCL_Comment()), Type36=OCL_Operation(), Type=OCL_TypedElement(), Type45=OCL_CollectionType()) == None


from python_code import OCL_CollectionLiteralExp

def test_OCL_CollectionLiteralExp___init__():
    assert OCL_CollectionLiteralExp.__init__(OCL_CollectionLiteralExp('', OCL_CollectionLiteralExp=set()), '', OCL_CollectionLiteralExp=set()) == None


from python_code import OCL_IntegerLiteralExp

def test_OCL_IntegerLiteralExp___init__():
    assert OCL_IntegerLiteralExp.__init__(OCL_IntegerLiteralExp(''), '') == None


from python_code import OCL_IfExp
from python_code import OCL_Invariant
from python_code import OCL_OclModule
from python_code import Variable

def test_OCL_Invariant___init__():
    assert OCL_Invariant.__init__(OCL_Invariant('', OCL_Invariant22=Variable(), OCL_Invariant=OCL_IfExp(), OclModuleElement=OCL_OclModule()), '', OCL_Invariant22=Variable(), OCL_Invariant=OCL_IfExp(), OclModuleElement=OCL_OclModule()) == None


from python_code import OCL_MultiplicityElement

def test_OCL_MultiplicityElement___init__():
    assert OCL_MultiplicityElement.__init__(OCL_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import OCL_Comment
from python_code import OCL_Package

def test_OCL_Package___init__():
    assert OCL_Package.__init__(OCL_Package('', OCL_Package=set(), OCL_Package29=set(), NamedElement=OCL_Comment()), '', OCL_Package=set(), OCL_Package29=set(), NamedElement=OCL_Comment()) == None


from python_code import OCL_Property
from python_code import Property

def test_OCL_Property___init__():
    assert OCL_Property.__init__(OCL_Property('', '', '', '', '', OCL_Property=Property()), '', '', '', '', '', OCL_Property=Property()) == None


from python_code import OCL_RealLiteralExp

def test_OCL_RealLiteralExp___init__():
    assert OCL_RealLiteralExp.__init__(OCL_RealLiteralExp(''), '') == None


from python_code import OCL_StringLiteralExp

def test_OCL_StringLiteralExp___init__():
    assert OCL_StringLiteralExp.__init__(OCL_StringLiteralExp(''), '') == None

