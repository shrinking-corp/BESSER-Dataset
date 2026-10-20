from python_code import studyPlan_Semester

def test_studyPlan_Semester___init__():
    assert studyPlan_Semester.__init__(studyPlan_Semester('', 0, '\x00\x00'), '', 0, '') == None

