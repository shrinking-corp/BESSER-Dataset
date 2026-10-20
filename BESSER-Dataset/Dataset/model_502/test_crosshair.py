from python_code import Families_Daughter
from python_code import Families_Family
from python_code import Families_Father
from python_code import Families_Mother
from python_code import Families_Son

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('', family=Families_Father(), family2=Families_Mother(), family4=set(), family6=set(), Family=Families_Father(), Family9=Families_Mother(), Family11=Families_Son(), Family13=Families_Daughter()), '', family=Families_Father(), family2=Families_Mother(), family4=set(), family6=set(), Family=Families_Father(), Family9=Families_Mother(), Family11=Families_Son(), Family13=Families_Daughter()) == None


from python_code import Families_Member

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member(''), '') == None

