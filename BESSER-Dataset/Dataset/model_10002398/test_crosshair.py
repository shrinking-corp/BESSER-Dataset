from python_code import mypackage_FileManager
from python_code import mypackage_Perosn

def test_mypackage_Perosn___init__():
    assert mypackage_Perosn.__init__(mypackage_Perosn(0, '', '', '', 0, fileManager3=mypackage_FileManager()), 0, '', '', '', 0, fileManager3=mypackage_FileManager()) == None


from python_code import mypackage_Staff

def test_mypackage_Staff___init__():
    assert mypackage_Staff.__init__(mypackage_Staff(''), '') == None


from python_code import mypackage_Student

def test_mypackage_Student___init__():
    assert mypackage_Student.__init__(mypackage_Student(0, '', '\x00\x00'), 0, '', '') == None


from python_code import mypackage_Tutor

def test_mypackage_Tutor___init__():
    assert mypackage_Tutor.__init__(mypackage_Tutor('', '\x00'), '\x00\x00', '') == None


from python_code import mypackage_studentAffairsEmp

def test_mypackage_studentAffairsEmp___init__():
    assert mypackage_studentAffairsEmp.__init__(mypackage_studentAffairsEmp(''), '') == None

