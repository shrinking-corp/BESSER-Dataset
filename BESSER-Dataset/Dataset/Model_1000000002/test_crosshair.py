from python_code import Review

def test_Review___init__():
    assert Review.__init__(Review(0, 0, '\x00\x00'), 0, 0, '') == None


import datetime as _ch_datetime
from python_code import Review
from python_code import Session
from python_code import SessionType

def test_Session___init__():
    assert Session.__init__(Session(0, _ch_datetime.date(1, 1, 1), 0, SessionType.ONLINE, review=Review(0, 0, '')), 0, _ch_datetime.date(1, 1, 1), 0, SessionType.HYBRID, review=Review(0, 0, '')) == None


from python_code import Skill
from python_code import TechSkillLevel

def test_Skill___init__():
    assert Skill.__init__(Skill(0, '', '', '\x00', TechSkillLevel.MASTERCLASS, 0, skillrequest_2=set()), 0, '', '', '', TechSkillLevel.BEGINNER, 0, skillrequest_2=set()) == None


import datetime as _ch_datetime
from python_code import SkillMatch
from python_code import SkillMatchStatus

def test_SkillMatch___init__():
    assert SkillMatch.__init__(SkillMatch(0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), SkillMatchStatus.ACTIVE, session=set()), 0, _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 2), SkillMatchStatus.ACTIVE, session=set()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '', '', skillrequest=set(), userskill=set()), 0, '', '', skillrequest=set(), userskill=set()) == None


from python_code import Skill
from python_code import TechSkillLevel
from python_code import UserSkill
from python_code import UserSkillLevel

def test_UserSkill___init__():
    assert UserSkill.__init__(UserSkill(0, UserSkillLevel.EXPERT, 0, False, skill=Skill(0, '', '', '', TechSkillLevel.BEGINNER, 0, skillrequest_2=set())), 0, UserSkillLevel.NOVICE, 0, True, skill=Skill(0, '', '', '', TechSkillLevel.EXPERT, 0, skillrequest_2=set())) == None

