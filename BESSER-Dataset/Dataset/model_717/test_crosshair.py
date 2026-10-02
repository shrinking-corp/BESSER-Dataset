from enum import Enum
from python_code import VisibilityKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(VisibilityKind.private, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(VisibilityKind.public, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(VisibilityKind.package, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(VisibilityKind.public, 0)

def test_Enum___new___2():
    assert Enum.__new__(VisibilityKind.public, 'public') == VisibilityKind.public

from python_code import uml_BehavioralFeature

def test_uml_BehavioralFeature___init__():
    assert uml_BehavioralFeature.__init__(uml_BehavioralFeature('', uml_BehavioralFeature=set(), uml_BehavioralFeature82=set()), '', uml_BehavioralFeature=set(), uml_BehavioralFeature82=set()) == None

from python_code import uml_Comment
from python_code import uml_Element

def test_uml_Comment___init__():
    assert uml_Comment.__init__(uml_Comment('', uml_Comment=set(), uml_Comment8=uml_Element()), '', uml_Comment=set(), uml_Comment8=uml_Element()) == None

from python_code import uml_ElementImport
from python_code import uml_Namespace
from python_code import uml_PackageableElement

def test_uml_ElementImport___init__():
    assert uml_ElementImport.__init__(uml_ElementImport('', '\x00', ElementImport=uml_Namespace(), uml_ElementImport=uml_PackageableElement(), elementImport=uml_Namespace()), '\x00\x00', '', ElementImport=uml_Namespace(), uml_ElementImport=uml_PackageableElement(), elementImport=uml_Namespace()) == None

from python_code import uml_Model

def test_uml_Model___init__():
    assert uml_Model.__init__(uml_Model('', uml_Model=set()), '', uml_Model=set()) == None
