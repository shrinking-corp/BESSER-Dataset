from enum import Enum
from python_code import Language
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Language.Java, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Language.C, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Language.C, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Language.C, 0)

def test_Enum___new___2():
    assert Enum.__new__(Language.C, 'C') == Language.C

from python_code import libraryElement_AdapterDeclaration
from python_code import libraryElement_AdapterFB

def test_libraryElement_AdapterFB___init__():
    assert libraryElement_AdapterFB.__init__(libraryElement_AdapterFB(AdapterFB=libraryElement_AdapterDeclaration(), adapterFB=libraryElement_AdapterDeclaration()), AdapterFB=libraryElement_AdapterDeclaration(), adapterFB=libraryElement_AdapterDeclaration()) == None

def test_libraryElement_AdapterFB_isSocket():
    assert libraryElement_AdapterFB.isSocket(libraryElement_AdapterFB(AdapterFB=libraryElement_AdapterDeclaration(), adapterFB=libraryElement_AdapterDeclaration())) == None

def test_libraryElement_AdapterFB_isPlug():
    assert libraryElement_AdapterFB.isPlug(libraryElement_AdapterFB(AdapterFB=libraryElement_AdapterDeclaration(), adapterFB=libraryElement_AdapterDeclaration())) == None

def test_libraryElement_AdapterFB_getType():
    assert libraryElement_AdapterFB.getType(libraryElement_AdapterFB(AdapterFB=libraryElement_AdapterDeclaration(), adapterFB=libraryElement_AdapterDeclaration())) == None

from python_code import libraryElement_AdapterFBType
from python_code import libraryElement_AdapterType

def test_libraryElement_AdapterType___init__():
    assert libraryElement_AdapterType.__init__(libraryElement_AdapterType(libraryElement_AdapterType=libraryElement_AdapterFBType(), libraryElement_AdapterType157=libraryElement_AdapterFBType()), libraryElement_AdapterType=libraryElement_AdapterFBType(), libraryElement_AdapterType157=libraryElement_AdapterFBType()) == None

def test_libraryElement_AdapterType_getInterfaceList():
    assert libraryElement_AdapterType.getInterfaceList(libraryElement_AdapterType(libraryElement_AdapterType=libraryElement_AdapterFBType(), libraryElement_AdapterType157=libraryElement_AdapterFBType())) == None

def test_libraryElement_AdapterType_getPlugType():
    assert libraryElement_AdapterType.getPlugType(libraryElement_AdapterType(libraryElement_AdapterType=libraryElement_AdapterFBType(), libraryElement_AdapterType157=libraryElement_AdapterFBType())) == None

def test_libraryElement_AdapterType_getSocketType():
    assert libraryElement_AdapterType.getSocketType(libraryElement_AdapterType(libraryElement_AdapterType=libraryElement_AdapterFBType(), libraryElement_AdapterType157=libraryElement_AdapterFBType())) == None

from python_code import libraryElement_Color
from python_code import libraryElement_ColorizableElement

def test_libraryElement_Color___init__():
    assert libraryElement_Color.__init__(libraryElement_Color('', '', '\x00\x00', libraryElement_Color=libraryElement_ColorizableElement()), '', '', '', libraryElement_Color=libraryElement_ColorizableElement()) == None

from python_code import libraryElement_CompilableType
from python_code import libraryElement_CompilerInfo

def test_libraryElement_CompilerInfo___init__():
    assert libraryElement_CompilerInfo.__init__(libraryElement_CompilerInfo('\x00\x00', '', libraryElement_CompilerInfo=set(), libraryElement_CompilerInfo133=libraryElement_CompilableType()), '', '', libraryElement_CompilerInfo=set(), libraryElement_CompilerInfo133=libraryElement_CompilableType()) == None

from python_code import libraryElement_ConfigurableObject

def test_libraryElement_ConfigurableObject___init__():
    assert libraryElement_ConfigurableObject.__init__(libraryElement_ConfigurableObject(libraryElement_ConfigurableObject=set()), libraryElement_ConfigurableObject=set()) == None

def test_libraryElement_ConfigurableObject_getParameter():
    assert libraryElement_ConfigurableObject.getParameter(libraryElement_ConfigurableObject(libraryElement_ConfigurableObject=set()), 0) == None

def test_libraryElement_ConfigurableObject_setParameter():
    assert libraryElement_ConfigurableObject.setParameter(libraryElement_ConfigurableObject(libraryElement_ConfigurableObject=set()), 0, '\x00\x00') == None

from python_code import libraryElement_FB

def test_libraryElement_FB___init__():
    assert libraryElement_FB.__init__(libraryElement_FB()) == None

def test_libraryElement_FB_getType():
    assert libraryElement_FB.getType(libraryElement_FB()) == None

def test_libraryElement_FB_isResourceTypeFB():
    assert libraryElement_FB.isResourceTypeFB(libraryElement_FB()) == None

def test_libraryElement_FB_isResourceFB():
    assert libraryElement_FB.isResourceFB(libraryElement_FB()) == None

from python_code import libraryElement_I4DIACElement

def test_libraryElement_I4DIACElement___init__():
    assert libraryElement_I4DIACElement.__init__(libraryElement_I4DIACElement(libraryElement_I4DIACElement=set()), libraryElement_I4DIACElement=set()) == None

def test_libraryElement_I4DIACElement_createAnnotation():
    assert libraryElement_I4DIACElement.createAnnotation(libraryElement_I4DIACElement(libraryElement_I4DIACElement=set()), 0) == None

def test_libraryElement_I4DIACElement_removeAnnotation():
    assert libraryElement_I4DIACElement.removeAnnotation(libraryElement_I4DIACElement(libraryElement_I4DIACElement=set()), 0) == None

from python_code import libraryElement_INamedElement

def test_libraryElement_INamedElement___init__():
    assert libraryElement_INamedElement.__init__(libraryElement_INamedElement('', '\x00'), '\x00\x00', '') == None

from python_code import libraryElement_Identification
from python_code import libraryElement_LibraryElement

def test_libraryElement_Identification___init__():
    assert libraryElement_Identification.__init__(libraryElement_Identification('', '', '', '', '', '', libraryElement_Identification=libraryElement_LibraryElement()), '', '', '', '', '\x00', '', libraryElement_Identification=libraryElement_LibraryElement()) == None

from python_code import libraryElement_OtherAlgorithm

def test_libraryElement_OtherAlgorithm___init__():
    assert libraryElement_OtherAlgorithm.__init__(libraryElement_OtherAlgorithm(''), '') == None

from python_code import libraryElement_PositionableElement

def test_libraryElement_PositionableElement___init__():
    assert libraryElement_PositionableElement.__init__(libraryElement_PositionableElement('', '\x00'), '\x00\x00', '') == None

from python_code import libraryElement_Primitive
from python_code import libraryElement_ServiceInterface

def test_libraryElement_Primitive___init__():
    assert libraryElement_Primitive.__init__(libraryElement_Primitive('', '\x00', libraryElement_Primitive=libraryElement_ServiceInterface()), '\x00\x00', '', libraryElement_Primitive=libraryElement_ServiceInterface()) == None

from python_code import libraryElement_ResourceTypeFB

def test_libraryElement_ResourceTypeFB___init__():
    assert libraryElement_ResourceTypeFB.__init__(libraryElement_ResourceTypeFB()) == None

def test_libraryElement_ResourceTypeFB_isResourceTypeFB():
    assert libraryElement_ResourceTypeFB.isResourceTypeFB(libraryElement_ResourceTypeFB()) == None

from python_code import libraryElement_Service
from python_code import libraryElement_ServiceSequence

def test_libraryElement_ServiceSequence___init__():
    assert libraryElement_ServiceSequence.__init__(libraryElement_ServiceSequence('', libraryElement_ServiceSequence=set(), libraryElement_ServiceSequence167=libraryElement_Service()), '', libraryElement_ServiceSequence=set(), libraryElement_ServiceSequence167=libraryElement_Service()) == None

from python_code import libraryElement_TextAlgorithm

def test_libraryElement_TextAlgorithm___init__():
    assert libraryElement_TextAlgorithm.__init__(libraryElement_TextAlgorithm(''), '') == None

from python_code import libraryElement_PaletteEntry
from python_code import libraryElement_TypedConfigureableObject

def test_libraryElement_TypedConfigureableObject___init__():
    assert libraryElement_TypedConfigureableObject.__init__(libraryElement_TypedConfigureableObject(libraryElement_TypedConfigureableObject=libraryElement_PaletteEntry()), libraryElement_TypedConfigureableObject=libraryElement_PaletteEntry()) == None

def test_libraryElement_TypedConfigureableObject_getType():
    assert libraryElement_TypedConfigureableObject.getType(libraryElement_TypedConfigureableObject(libraryElement_TypedConfigureableObject=libraryElement_PaletteEntry())) == None

def test_libraryElement_TypedConfigureableObject_getTypeName():
    assert libraryElement_TypedConfigureableObject.getTypeName(libraryElement_TypedConfigureableObject(libraryElement_TypedConfigureableObject=libraryElement_PaletteEntry())) == None

from python_code import libraryElement_LibraryElement
from python_code import libraryElement_VersionInfo

def test_libraryElement_VersionInfo___init__():
    assert libraryElement_VersionInfo.__init__(libraryElement_VersionInfo('', '', '', '', '', libraryElement_VersionInfo=libraryElement_LibraryElement()), '', '', '', '', '', libraryElement_VersionInfo=libraryElement_LibraryElement()) == None
