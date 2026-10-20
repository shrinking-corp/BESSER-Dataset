from python_code import study_Department
from python_code import study_Programme

def test_study_Programme___init__():
    assert study_Programme.__init__(study_Programme('\x00\x00', '', study_Programme=study_Department(), study_Programme4=set()), '', '', study_Programme=study_Department(), study_Programme4=set()) == None


from python_code import study_Specialization
from python_code import study_StudyPlan

def test_study_Specialization___init__():
    assert study_Specialization.__init__(study_Specialization('', study_Specialization=study_StudyPlan(), study_Specialization10=set()), '', study_Specialization=study_StudyPlan(), study_Specialization10=set()) == None

