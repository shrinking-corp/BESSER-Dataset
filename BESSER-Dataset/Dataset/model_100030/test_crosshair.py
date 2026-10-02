from enum import Enum
from python_code import SequenceType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SequenceType.startToFinish, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SequenceType.startToStart, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SequenceType.finishToStart, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SequenceType.startToStart, 0)

def test_Enum___new___2():
    assert Enum.__new__(SequenceType.startToStart, 'startToStart') == SequenceType.startToStart

from python_code import publication_Counted

def test_publication_Counted___init__():
    assert publication_Counted.__init__(publication_Counted(0), 0) == None

from python_code import publication_Labelled

def test_publication_Labelled___init__():
    assert publication_Labelled.__init__(publication_Labelled(''), '') == None

from python_code import publication_Named

def test_publication_Named___init__():
    assert publication_Named.__init__(publication_Named(''), '') == None

from python_code import publication_Paper
from python_code import publication_Paragraph
from python_code import publication_Write

def test_publication_Paragraph___init__():
    assert publication_Paragraph.__init__(publication_Paragraph('\x00', publication_Paragraph31=set(), publication_Paragraph40=publication_Write(), publication_Paragraph=publication_Paper()), '', publication_Paragraph31=set(), publication_Paragraph40=publication_Write(), publication_Paragraph=publication_Paper()) == None
