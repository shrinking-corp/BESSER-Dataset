from python_code import addressbook_Electronic

def test_addressbook_Electronic___init__():
    assert addressbook_Electronic.__init__(addressbook_Electronic('', '\x00'), '\x00\x00', '') == None


from python_code import addressbook_Office

def test_addressbook_Office___init__():
    assert addressbook_Office.__init__(addressbook_Office(''), '') == None


from python_code import addressbook_AddressBook
from python_code import addressbook_People

def test_addressbook_People___init__():
    assert addressbook_People.__init__(addressbook_People('', addressbook_People=set(), addressbook_People2=addressbook_AddressBook()), '', addressbook_People=set(), addressbook_People2=addressbook_AddressBook()) == None


from python_code import addressbook_AddressBook
from python_code import addressbook_Repository

def test_addressbook_Repository___init__():
    assert addressbook_Repository.__init__(addressbook_Repository(addressbook_Repository=addressbook_AddressBook(), addressbook_Repository6=set()), addressbook_Repository=addressbook_AddressBook(), addressbook_Repository6=set()) == None

def test_addressbook_Repository_checkout():
    assert addressbook_Repository.checkout(addressbook_Repository(addressbook_Repository=addressbook_AddressBook(), addressbook_Repository6=set()), 0) == None

def test_addressbook_Repository_checkin():
    assert addressbook_Repository.checkin(addressbook_Repository(addressbook_Repository=addressbook_AddressBook(), addressbook_Repository6=set())) == None

