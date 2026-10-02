from python_code import admin

def test_admin___init__():
    assert admin.__init__(admin('', '', '\x00', '', 0, 0, customer5=set(), flights8=set()), '', '', '', '', 0, 0, customer5=set(), flights8=set()) == None

from python_code import ticket

def test_ticket___init__():
    assert ticket.__init__(ticket(0, '', '', 0, '', customer3=set()), 0, '', '', 0, '', customer3=set()) == None
