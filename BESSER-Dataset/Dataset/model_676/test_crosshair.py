from python_code import emof_Class
from python_code import emof_Comment
from python_code import emof_Operation
from python_code import emof_Package
from python_code import emof_TypedElement

def test_emof_Class___init__():
    assert emof_Class.__init__(emof_Class('', emof_Class=set(), emof_Class2=set(), emof_Class4=set(), Type32=emof_TypedElement(), Type=emof_Operation(), Type20=emof_Package('', emof_Package=set(), emof_Package19=set(), NamedElement=emof_Comment())), '', emof_Class=set(), emof_Class2=set(), emof_Class4=set(), Type32=emof_TypedElement(), Type=emof_Operation(), Type20=emof_Package('', emof_Package=set(), emof_Package19=set(), NamedElement=emof_Comment())) == None


from python_code import emof_MultiplicityElement

def test_emof_MultiplicityElement___init__():
    assert emof_MultiplicityElement.__init__(emof_MultiplicityElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import emof_Comment
from python_code import emof_Package

def test_emof_Package___init__():
    assert emof_Package.__init__(emof_Package('', emof_Package=set(), emof_Package19=set(), NamedElement=emof_Comment()), '', emof_Package=set(), emof_Package19=set(), NamedElement=emof_Comment()) == None


from python_code import Class
from python_code import Property
from python_code import emof_Property

def test_emof_Property___init__():
    assert emof_Property.__init__(emof_Property('', '', '', '', '', emof_Property26=Property(), emof_Property=Class()), '', '', '', '', '', emof_Property26=Property(), emof_Property=Class()) == None

