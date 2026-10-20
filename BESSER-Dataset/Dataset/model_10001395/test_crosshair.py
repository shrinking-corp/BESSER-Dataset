from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin(''), '') == None


from python_code import Email
from python_code import FileBinary

def test_Email___init__():
    assert Email.__init__(Email('', fileBinary6=FileBinary()), '', fileBinary6=FileBinary()) == None


from python_code import Finance

def test_Finance___init__():
    assert Finance.__init__(Finance('', '\x00'), '\x00\x00', '') == None


from python_code import FileBinary
from python_code import Insturctor

def test_Insturctor___init__():
    assert Insturctor.__init__(Insturctor('', fileBinary8=FileBinary()), '', fileBinary8=FileBinary()) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('', '', '\x00\x00'), '', '', '') == None


from python_code import FileBinary
from python_code import Student

def test_Student___init__():
    assert Student.__init__(Student(0, '', '\x00\x00', fileBinary10=FileBinary()), 0, '', '', fileBinary10=FileBinary()) == None

