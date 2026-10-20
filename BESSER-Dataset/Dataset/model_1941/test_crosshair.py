from python_code import addressbook_Category
from python_code import addressbook_Entry

def test_addressbook_Entry___init__():
    assert addressbook_Entry.__init__(addressbook_Entry(0, Entry=addressbook_Category(), entries=addressbook_Category()), 0, Entry=addressbook_Category(), entries=addressbook_Category()) == None


from python_code import addressbook_NamedElement

def test_addressbook_NamedElement___init__():
    assert addressbook_NamedElement.__init__(addressbook_NamedElement(''), '') == None

