from python_code import myDsl_School
from python_code import myDsl_SchoolModel

def test_myDsl_School___init__():
    assert myDsl_School.__init__(myDsl_School('\x00', myDsl_School=myDsl_SchoolModel(), myDsl_School2=set()), '', myDsl_School=myDsl_SchoolModel(), myDsl_School2=set()) == None


from python_code import myDsl_Student

def test_myDsl_Student___init__():
    assert myDsl_Student.__init__(myDsl_Student(0, myDsl_Student=set()), 0, myDsl_Student=set()) == None

