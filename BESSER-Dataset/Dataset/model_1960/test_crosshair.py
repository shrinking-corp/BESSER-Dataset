from enum import Enum
from python_code import FileEncoding
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FileEncoding.UTF_8, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FileEncoding.UTF_8, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FileEncoding.UTF_16, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FileEncoding.UTF_8, 0)

def test_Enum___new___2():
    assert Enum.__new__(FileEncoding.UTF_8, 'UTF_8') == FileEncoding.UTF_8

from python_code import file_ByteFile

def test_file_ByteFile___init__():
    assert file_ByteFile.__init__(file_ByteFile(''), '') == None

from python_code import file_File
from python_code import file_FileHandler
from python_code import file_FileOutput
from python_code import file_FileOwner

def test_file_File___init__():
    assert file_File.__init__(file_File('', file_File=file_FileHandler(), file_File3=file_FileHandler(), file_File5=file_FileOwner(), file_File7=file_FileOutput()), '', file_File=file_FileHandler(), file_File3=file_FileHandler(), file_File5=file_FileOwner(), file_File7=file_FileOutput()) == None

from python_code import file_FileInMemory

def test_file_FileInMemory___init__():
    assert file_FileInMemory.__init__(file_FileInMemory(''), '') == None

from python_code import file_FileLocal

def test_file_FileLocal___init__():
    assert file_FileLocal.__init__(file_FileLocal(''), '') == None

from python_code import file_FileReaderWriter

def test_file_FileReaderWriter___init__():
    assert file_FileReaderWriter.__init__(file_FileReaderWriter('\x00\x00', '', False, ''), '', '', False, '') == None

def test_file_FileReaderWriter_writeFile():
    assert file_FileReaderWriter.writeFile(file_FileReaderWriter('', '\x00', False, '\x00'), '') == None

def test_file_FileReaderWriter_close():
    assert file_FileReaderWriter.close(file_FileReaderWriter('', '\x00', False, '\x00')) == None

def test_file_FileReaderWriter_readFile():
    assert file_FileReaderWriter.readFile(file_FileReaderWriter('', '\x00', False, '\x00'), '') == None

def test_file_FileReaderWriter_getWriteFeedback():
    assert file_FileReaderWriter.getWriteFeedback(file_FileReaderWriter('', '\x00', False, '\x00'), '') == None

def test_file_FileReaderWriter_getReadFeedback():
    assert file_FileReaderWriter.getReadFeedback(file_FileReaderWriter('', '\x00', False, '\x00'), '') == None

from python_code import file_FileRemote

def test_file_FileRemote___init__():
    assert file_FileRemote.__init__(file_FileRemote(''), '') == None

from python_code import file_Files

def test_file_Files___init__():
    assert file_Files.__init__(file_Files(''), '') == None
