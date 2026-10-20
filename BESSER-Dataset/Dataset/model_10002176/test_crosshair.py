from python_code import Class
from python_code import Reservation

def test_Reservation___init__():
    assert Reservation.__init__(Reservation(Class(), Class(), order5=set()), Class(), Class(), order5=set()) == None

