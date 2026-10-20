from python_code import Families_Member
from python_code import aMember

def test_Families_Member___init__():
    assert Families_Member.__init__(Families_Member('', 0, Families_Member=aMember()), '', 0, Families_Member=aMember()) == None


from python_code import Families_uncertainty_UData

def test_Families_uncertainty_UData___init__():
    assert Families_uncertainty_UData.__init__(Families_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

