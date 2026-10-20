from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Catering

def test_Catering___init__():
    assert Catering.__init__(Catering('', '\x00'), '\x00\x00', '') == None


from python_code import Catering_book

def test_Catering_book___init__():
    assert Catering_book.__init__(Catering_book('', '\x00'), '\x00\x00', '') == None


from python_code import Hall

def test_Hall___init__():
    assert Hall.__init__(Hall('', '', '\x00\x00'), '', '', '') == None


from python_code import Hall_book

def test_Hall_book___init__():
    assert Hall_book.__init__(Hall_book('', '', '\x00\x00'), '', '', '') == None


from python_code import LOGIN

def test_LOGIN___init__():
    assert LOGIN.__init__(LOGIN('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '', '\x00\x00'), 0, '', '') == None


from python_code import User
from python_code import View_and_place_order

def test_View_and_place_order___init__():
    assert View_and_place_order.__init__(View_and_place_order(User(0, '', ''), User(0, '', '')), User(0, '', ''), User(0, '\x00', '')) == None


from python_code import Admin
from python_code import View_and_update

def test_View_and_update___init__():
    assert View_and_update.__init__(View_and_update(Admin(0, '', ''), Admin(0, '', '')), Admin(0, '', ''), Admin(0, '\x00', '')) == None

