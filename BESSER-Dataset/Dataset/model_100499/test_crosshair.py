import datetime as _ch_datetime
from python_code import gore_PerformativeRequirement

def test_gore_PerformativeRequirement___init__():
    assert gore_PerformativeRequirement.__init__(gore_PerformativeRequirement(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None

def test_gore_PerformativeRequirement_cancel():
    assert gore_PerformativeRequirement.cancel(gore_PerformativeRequirement(_ch_datetime.date(1, 1, 2))) == None

def test_gore_PerformativeRequirement_checkState():
    assert gore_PerformativeRequirement.checkState(gore_PerformativeRequirement(_ch_datetime.date(1, 1, 2))) == None


from python_code import gore_QualityConstraint
from python_code import gore_Softgoal

def test_gore_QualityConstraint___init__():
    assert gore_QualityConstraint.__init__(gore_QualityConstraint(QualityConstraint=gore_Softgoal(), constraints=gore_Softgoal()), QualityConstraint=gore_Softgoal(), constraints=gore_Softgoal()) == None

def test_gore_QualityConstraint_replaceWith():
    assert gore_QualityConstraint.replaceWith(gore_QualityConstraint(QualityConstraint=gore_Softgoal(), constraints=gore_Softgoal()), '') == None

