from enum import Enum
from python_code import ActorType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActorType.SYSTEM, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActorType.SYSTEM, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActorType.SYSTEM, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActorType.SYSTEM, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActorType.SYSTEM, 'SYSTEM') == ActorType.SYSTEM

from python_code import useCases_Flow

def test_useCases_Flow___init__():
    assert useCases_Flow.__init__(useCases_Flow('', useCases_Flow=set()), '', useCases_Flow=set()) == None

from python_code import useCases_AlternativeFlowAlternative
from python_code import useCases_NamedFlow

def test_useCases_NamedFlow___init__():
    assert useCases_NamedFlow.__init__(useCases_NamedFlow('', useCases_NamedFlow=useCases_AlternativeFlowAlternative()), '', useCases_NamedFlow=useCases_AlternativeFlowAlternative()) == None

from python_code import useCases_NamespaceImport
from python_code import useCases_PackageDeclaration
from python_code import useCases_UseCasesModel

def test_useCases_PackageDeclaration___init__():
    assert useCases_PackageDeclaration.__init__(useCases_PackageDeclaration('', '', useCases_PackageDeclaration12=useCases_NamespaceImport(), useCases_PackageDeclaration15=useCases_NamespaceImport(), useCases_PackageDeclaration17=set(), useCases_PackageDeclaration=useCases_UseCasesModel(), useCases_PackageDeclaration20=set(), useCases_PackageDeclaration22=set(), useCases_PackageDeclaration5=useCases_NamespaceImport()), '', '', useCases_PackageDeclaration12=useCases_NamespaceImport(), useCases_PackageDeclaration15=useCases_NamespaceImport(), useCases_PackageDeclaration17=set(), useCases_PackageDeclaration=useCases_UseCasesModel(), useCases_PackageDeclaration20=set(), useCases_PackageDeclaration22=set(), useCases_PackageDeclaration5=useCases_NamespaceImport()) == None
