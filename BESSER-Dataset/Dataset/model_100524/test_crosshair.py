from python_code import urml_danger_Danger
from python_code import urml_danger_ProceduralMitigation

def test_urml_danger_ProceduralMitigation___init__():
    assert urml_danger_ProceduralMitigation.__init__(urml_danger_ProceduralMitigation('', Mitigation=urml_danger_Danger()), '', Mitigation=urml_danger_Danger()) == None


from python_code import ApplicationDomainUseCase
from python_code import Goal
from python_code import urml_goal_Goal

def test_urml_goal_Goal___init__():
    assert urml_goal_Goal.__init__(urml_goal_Goal(False, '', goals=set(), goals3=set(), detailedGoal=ApplicationDomainUseCase(), parentGoal=set(), subGoals=Goal(), target=set(), source=set()), False, '', goals=set(), goals3=set(), detailedGoal=ApplicationDomainUseCase(), parentGoal=set(), subGoals=Goal(), target=set(), source=set()) == None


from python_code import Goal
from python_code import urml_goal_GoalReference

def test_urml_goal_GoalReference___init__():
    assert urml_goal_GoalReference.__init__(urml_goal_GoalReference('', influencingGoals=Goal(), influencedGoals=Goal()), '', influencingGoals=Goal(), influencedGoals=Goal()) == None


from python_code import urml_danger_Danger
from python_code import urml_requirement_Requirement

def test_urml_requirement_Requirement___init__():
    assert urml_requirement_Requirement.__init__(urml_requirement_Requirement(False, satisfiedRequirements=set(), Mitigation=urml_danger_Danger()), False, satisfiedRequirements=set(), Mitigation=urml_danger_Danger()) == None

