from python_code import type_Assosiation
from python_code import type_TypePointer

def test_type_Assosiation___init__():
    assert type_Assosiation.__init__(type_Assosiation('', '', False, '', '', type_Assosiation=set(), type_Assosiation16=type_TypePointer()), '', '', True, '', '', type_Assosiation=set(), type_Assosiation16=type_TypePointer()) == None


from python_code import type_EnumAttribute
from python_code import type_Enumerator

def test_type_EnumAttribute___init__():
    assert type_EnumAttribute.__init__(type_EnumAttribute('', '', '\x00\x00', type_EnumAttribute=type_Enumerator()), '', '', '', type_EnumAttribute=type_Enumerator()) == None


from python_code import type_PackagePointer
from python_code import type_TypeGroup

def test_type_TypeGroup___init__():
    assert type_TypeGroup.__init__(type_TypeGroup('', '', type_TypeGroup=set(), type_TypeGroup2=set(), type_TypeGroup13=type_PackagePointer()), '', '', type_TypeGroup=set(), type_TypeGroup2=set(), type_TypeGroup13=type_PackagePointer()) == None

