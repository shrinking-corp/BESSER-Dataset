from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '', '', '', '\x00', registeredUser58=set(), registeredUser60=set()), '', '', '', '', '', registeredUser58=set(), registeredUser60=set()) == None


from python_code import Add_Course_UseCase
from python_code import Address_UseCase
from python_code import Name_UseCase
from python_code import Student_ID_UseCase
from python_code import class_Student_Registration_Student

def test_class_Student_Registration_Student___init__():
    assert class_Student_Registration_Student.__init__(class_Student_Registration_Student('', Name_UseCase(), Student_ID_UseCase(), Address_UseCase(), '\x00', Add_Course_UseCase()), '\x00\x00', Name_UseCase(), Student_ID_UseCase(), Address_UseCase(), '', Add_Course_UseCase()) == None

