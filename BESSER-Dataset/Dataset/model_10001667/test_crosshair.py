from python_code import Admin
from python_code import int

def test_Admin___init__():
    assert Admin.__init__(Admin(int(), homeTheatre5=set()), int(), homeTheatre5=set()) == None


from python_code import Employee
from python_code import int

def test_Employee___init__():
    assert Employee.__init__(Employee(int()), int()) == None


from python_code import Light

def test_Light___init__():
    assert Light.__init__(Light(''), '') == None


from python_code import UDP_Controller

def test_UDP_Controller___init__():
    assert UDP_Controller.__init__(UDP_Controller(''), '') == None


from python_code import UDP_Socket
from python_code import int

def test_UDP_Socket___init__():
    assert UDP_Socket.__init__(UDP_Socket(int()), int()) == None

