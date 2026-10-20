from python_code import dbschema_Column
from python_code import dbschema_Table

def test_dbschema_Column___init__():
    assert dbschema_Column.__init__(dbschema_Column('', 0, False, dbschema_Column=dbschema_Table()), '\x00', 0, False, dbschema_Column=dbschema_Table()) == None


from python_code import dbschema_NamedElement

def test_dbschema_NamedElement___init__():
    assert dbschema_NamedElement.__init__(dbschema_NamedElement(''), '') == None

