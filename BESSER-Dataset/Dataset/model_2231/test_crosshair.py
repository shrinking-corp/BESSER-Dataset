from python_code import ra_Department
from python_code import ra_Programme
from python_code import ra_StudyPlan

def test_ra_Programme___init__():
    assert ra_Programme.__init__(ra_Programme('', '\x00', ra_Programme=ra_Department(), programme=ra_StudyPlan(), Programme=ra_StudyPlan()), '\x00\x00', '', ra_Programme=ra_Department(), programme=ra_StudyPlan(), Programme=ra_StudyPlan()) == None

