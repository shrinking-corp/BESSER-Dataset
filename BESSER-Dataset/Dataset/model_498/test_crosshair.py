from python_code import Families_LastNameElement

def test_Families_LastNameElement___init__():
    assert Families_LastNameElement.__init__(Families_LastNameElement(''), '') == None


from python_code import Families_Member
from python_code import Family

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member('', father=Family(), mother=Family(), sons=Family(), daughters=Family()), '', father=Family(), mother=Family(), sons=Family(), daughters=Family()) == None

