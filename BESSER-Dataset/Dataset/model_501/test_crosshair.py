from python_code import Families_Daughter
from python_code import Families_Family
from python_code import Families_Father
from python_code import Families_Mother
from python_code import Families_Son

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('', familyMother=Families_Mother(), familySon=set(), familyDaughter=set(), Family8=Families_Son(), Family10=Families_Daughter(), Family=Families_Father(), Family6=Families_Mother(), familyFather=Families_Father()), '', familyMother=Families_Mother(), familySon=set(), familyDaughter=set(), Family8=Families_Son(), Family10=Families_Daughter(), Family=Families_Father(), Family6=Families_Mother(), familyFather=Families_Father()) == None


from python_code import Families_Member

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member(''), '') == None

