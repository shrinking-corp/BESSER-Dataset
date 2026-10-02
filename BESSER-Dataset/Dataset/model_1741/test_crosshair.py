from python_code import MediaLibrary_AudioBook

def test_MediaLibrary_AudioBook___init__():
    assert MediaLibrary_AudioBook.__init__(MediaLibrary_AudioBook(0), 0) == None

from python_code import MediaLibrary_DurationArtifact

def test_MediaLibrary_DurationArtifact___init__():
    assert MediaLibrary_DurationArtifact.__init__(MediaLibrary_DurationArtifact(0), 0) == None

from python_code import MediaLibrary_EReader

def test_MediaLibrary_EReader___init__():
    assert MediaLibrary_EReader.__init__(MediaLibrary_EReader('', '\x00'), '\x00\x00', '') == None

from python_code import MediaLibrary_Ebook

def test_MediaLibrary_Ebook___init__():
    assert MediaLibrary_Ebook.__init__(MediaLibrary_Ebook(0), 0) == None

from python_code import MediaLibrary_ExternalSource

def test_MediaLibrary_ExternalSource___init__():
    assert MediaLibrary_ExternalSource.__init__(MediaLibrary_ExternalSource(''), '') == None

from python_code import MediaLibrary_Image

def test_MediaLibrary_Image___init__():
    assert MediaLibrary_Image.__init__(MediaLibrary_Image(''), '') == None

from python_code import MediaLibrary_Ecosystem
from python_code import MediaLibrary_Library

def test_MediaLibrary_Library___init__():
    assert MediaLibrary_Library.__init__(MediaLibrary_Library('', MediaLibrary_Library=MediaLibrary_Ecosystem(), MediaLibrary_Library8=set()), '', MediaLibrary_Library=MediaLibrary_Ecosystem(), MediaLibrary_Library8=set()) == None

from python_code import MediaLibrary_MusicTrack

def test_MediaLibrary_MusicTrack___init__():
    assert MediaLibrary_MusicTrack.__init__(MediaLibrary_MusicTrack(''), '') == None

from python_code import MediaLibrary_Store

def test_MediaLibrary_Store___init__():
    assert MediaLibrary_Store.__init__(MediaLibrary_Store('', '\x00'), '\x00\x00', '') == None

from python_code import MediaLibrary_Video

def test_MediaLibrary_Video___init__():
    assert MediaLibrary_Video.__init__(MediaLibrary_Video(''), '') == None

from enum import Enum
from python_code import SourceType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SourceType.HDD, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SourceType.CD, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SourceType.HDD, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SourceType.CD, 0)

def test_Enum___new___2():
    assert Enum.__new__(SourceType.CD, 'CD') == SourceType.CD
