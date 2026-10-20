from python_code import Other_employees

def test_Other_employees___init__():
    assert Other_employees.__init__(Other_employees('', '\x00'), '\x00\x00', '') == None


from python_code import Questionnaire_survey

def test_Questionnaire_survey___init__():
    assert Questionnaire_survey.__init__(Questionnaire_survey('', '\x00'), '\x00\x00', '') == None


from python_code import Training_materials_IITU

def test_Training_materials_IITU___init__():
    assert Training_materials_IITU.__init__(Training_materials_IITU(''), '') == None

