from python_code import Families_Family
from python_code import Member

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('', familyDaughter=set(), familyFather=Member(), familyMother=Member(), familySon=set()), '', familyDaughter=set(), familyFather=Member(), familyMother=Member(), familySon=set()) == None


from python_code import Families_Member
from python_code import Family

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member('', '\x00', father=Family(), mother=Family(), sons=Family(), daughters=Family()), '\x00\x00', '', father=Family(), mother=Family(), sons=Family(), daughters=Family()) == None

