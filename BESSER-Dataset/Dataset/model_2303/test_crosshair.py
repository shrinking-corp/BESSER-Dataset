from python_code import Families2Persons_Member
from python_code import Families2Persons_MemberToPerson
from python_code import Families2Persons_Person

def test_Families2Persons_MemberToPerson___init__():
    assert Families2Persons_MemberToPerson.__init__(Families2Persons_MemberToPerson('', '\x00', Families2Persons_MemberToPerson=Families2Persons_Member(), Families2Persons_MemberToPerson2=Families2Persons_Person()), '\x00\x00', '', Families2Persons_MemberToPerson=Families2Persons_Member(), Families2Persons_MemberToPerson2=Families2Persons_Person()) == None

