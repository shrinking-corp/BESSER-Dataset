from python_code import Database
from python_code import ui_project_Project

def test_ui_project_Project___init__():
    assert ui_project_Project.__init__(ui_project_Project('\x00\x00', '', ui_project_Project=Database(), ui_project_Project2=set()), '', '', ui_project_Project=Database(), ui_project_Project2=set()) == None

def test_ui_project_Project_isValid():
    assert ui_project_Project.isValid(ui_project_Project('', '\x00', ui_project_Project=Database(), ui_project_Project2=set()), '', '') == None

