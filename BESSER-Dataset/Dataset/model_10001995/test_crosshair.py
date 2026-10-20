from python_code import Management_Director
from python_code import Management_DirectorTest

def test_Management_Director___init__():
    assert Management_Director.__init__(Management_Director(0.0, directortest6=Management_DirectorTest()), 0.0, directortest6=Management_DirectorTest()) == None


from python_code import Management_Manager
from python_code import Management_ManagerTest

def test_Management_Manager___init__():
    assert Management_Manager.__init__(Management_Manager('', managertest4=Management_ManagerTest()), '', managertest4=Management_ManagerTest()) == None


from python_code import Staff_Employee

def test_Staff_Employee___init__():
    assert Staff_Employee.__init__(Staff_Employee('', '', 0.0), '', '', 0.0) == None

