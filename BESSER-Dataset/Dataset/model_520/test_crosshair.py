from python_code import Families_Family
from python_code import aMember

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('\x00\x00', '', Families_Family=set(), Families_Family2=aMember(), Families_Family5=aMember()), '', '', Families_Family=set(), Families_Family2=aMember(), Families_Family5=aMember()) == None


from python_code import Families_Member
from python_code import aFamily

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member('', 0, Families_Member=aFamily()), '', 0, Families_Member=aFamily()) == None


from python_code import Families_uncertainty_UData

def test_Families_uncertainty_UData___init__():
    assert Families_uncertainty_UData.__init__(Families_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

