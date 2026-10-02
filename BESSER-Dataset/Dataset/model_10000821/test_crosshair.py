from python_code import Flight

def test_Flight___init__():
    assert Flight.__init__(Flight(True), False) == None

from python_code import Management_Director
from python_code import Management_DirectorTest

def test_Management_Director___init__():
    assert Management_Director.__init__(Management_Director(0.0, directortest6=Management_DirectorTest()), 0.0, directortest6=Management_DirectorTest()) == None

from python_code import Management_Manager
from python_code import Management_ManagerTest

def test_Management_Manager___init__():
    assert Management_Manager.__init__(Management_Manager('', managertest4=Management_ManagerTest()), '', managertest4=Management_ManagerTest()) == None

from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('\x00', datetime.date(1, 1, 1), 0.0, False), '', datetime.date(1, 1, 1), 0.0, False) == None

from python_code import Staff_Employee

def test_Staff_Employee___init__():
    assert Staff_Employee.__init__(Staff_Employee('', '', 0.0), '', '', 0.0) == None

from python_code import Taxi

def test_Taxi___init__():
    assert Taxi.__init__(Taxi(True), False) == None

from python_code import Ticket

def test_Ticket___init__():
    assert Ticket.__init__(Ticket('', '', False), '\x00', '', False) == None

from python_code import TransportationProduct

def test_TransportationProduct___init__():
    assert TransportationProduct.__init__(TransportationProduct('', '', 0.0), '', '', 0.0) == None
