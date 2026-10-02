from enum import Enum
from python_code import GoalReferenceType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GoalReferenceType.PLUS, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GoalReferenceType.PLUS, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GoalReferenceType.PLUS, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GoalReferenceType.PLUS, 0)

def test_Enum___new___2():
    assert Enum.__new__(GoalReferenceType.PLUS, 'PLUS') == GoalReferenceType.PLUS

from enum import Enum
from python_code import GoalType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GoalType.PRODUCT_GOAL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GoalType.PRODUCT_GOAL, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GoalType.PRODUCT_GOAL, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GoalType.PRODUCT_GOAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(GoalType.PRODUCT_GOAL, 'PRODUCT_GOAL') == GoalType.PRODUCT_GOAL

from python_code import urml_danger_Danger
from python_code import urml_danger_ProceduralMitigation

def test_urml_danger_ProceduralMitigation___init__():
    assert urml_danger_ProceduralMitigation.__init__(urml_danger_ProceduralMitigation('', Mitigation=urml_danger_Danger()), '', Mitigation=urml_danger_Danger()) == None

from python_code import Goal
from python_code import urml_goal_GoalReference

def test_urml_goal_GoalReference___init__():
    assert urml_goal_GoalReference.__init__(urml_goal_GoalReference('', influencedGoals=Goal(), influencingGoals=Goal()), '', influencedGoals=Goal(), influencingGoals=Goal()) == None

from python_code import urml_danger_Danger
from python_code import urml_requirement_Requirement

def test_urml_requirement_Requirement___init__():
    assert urml_requirement_Requirement.__init__(urml_requirement_Requirement(False, satisfiedRequirements=set(), Mitigation=urml_danger_Danger()), False, satisfiedRequirements=set(), Mitigation=urml_danger_Danger()) == None
