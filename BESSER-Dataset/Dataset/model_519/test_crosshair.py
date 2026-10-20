from python_code import Families_Family
from python_code import aMember

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('', '', Families_Family=set(), Families_Family2=set(), Families_Family5=aMember(), Families_Family8=aMember(), Families_Family11=set()), '', '', Families_Family=set(), Families_Family2=set(), Families_Family5=aMember(), Families_Family8=aMember(), Families_Family11=set()) == None


from python_code import Families_Member
from python_code import aMember

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member('', 0, Families_Member=aMember()), '', 0, Families_Member=aMember()) == None


from python_code import Families_uncertainty_UData

def test_Families_uncertainty_UData___init__():
    assert Families_uncertainty_UData.__init__(Families_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

