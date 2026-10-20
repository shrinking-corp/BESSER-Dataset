from python_code import VorkursModel_Room
from python_code import VorkursModel_TeachingAssistant

def test_VorkursModel_Room___init__():
    assert VorkursModel_Room.__init__(VorkursModel_Room(0, False, 0, False, VorkursModel_Room=VorkursModel_TeachingAssistant()), 0, False, 0, True, VorkursModel_Room=VorkursModel_TeachingAssistant()) == None

