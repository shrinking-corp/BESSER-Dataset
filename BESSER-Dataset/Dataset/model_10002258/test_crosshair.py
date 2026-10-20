from python_code import admin
from python_code import login_admin

def test_login_admin___init__():
    assert login_admin.__init__(login_admin('', '\x00', admin21=admin()), '\x00\x00', '', admin21=admin()) == None


from python_code import admin
from python_code import news

def test_news___init__():
    assert news.__init__(news(0, '\x00', '', '', admin5=admin()), 0, '', '', '', admin5=admin()) == None


from python_code import admin
from python_code import our_costumer___major

def test_our_costumer___major___init__():
    assert our_costumer___major.__init__(our_costumer___major(0, '\x00', admin1=admin()), 0, '\x00', admin1=admin()) == None


from python_code import admin
from python_code import produk

def test_produk___init__():
    assert produk.__init__(produk(0, '', '\x00\x00', admin3=admin()), 0, '', '', admin3=admin()) == None


from python_code import admin
from python_code import register_admin

def test_register_admin___init__():
    assert register_admin.__init__(register_admin(0, '', '', '', '', admin19=admin()), 0, '', '', '', '', admin19=admin()) == None

