from python_code import Families_Family
from python_code import aFamilyMember
from python_code import aFamilyRegister

def test_Families_Family___init__():
    assert Families_Family.__init__(Families_Family('', Families_Family=aFamilyMember(), Families_Family3=aFamilyMember(), Families_Family6=set(), Families_Family9=set(), Families_Family12=aFamilyRegister()), '', Families_Family=aFamilyMember(), Families_Family3=aFamilyMember(), Families_Family6=set(), Families_Family9=set(), Families_Family12=aFamilyRegister()) == None


from python_code import Families_FamilyMember
from python_code import aFamily

def test_Families_FamilyMember___init__():
    assert Families_FamilyMember.__init__(Families_FamilyMember('', Families_FamilyMember=aFamily(), Families_FamilyMember16=aFamily(), Families_FamilyMember19=aFamily(), Families_FamilyMember22=aFamily()), '', Families_FamilyMember=aFamily(), Families_FamilyMember16=aFamily(), Families_FamilyMember19=aFamily(), Families_FamilyMember22=aFamily()) == None


from python_code import Families_uncertainty_UData

def test_Families_uncertainty_UData___init__():
    assert Families_uncertainty_UData.__init__(Families_uncertainty_UData('', '\x00'), '\x00\x00', '') == None

