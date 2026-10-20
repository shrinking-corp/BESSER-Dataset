from python_code import migration_AbstractResource

def test_migration_AbstractResource___init__():
    assert migration_AbstractResource.__init__(migration_AbstractResource('', '\x00'), '\x00\x00', '') == None


from python_code import migration_AttributeSlot
from python_code import migration_EAttribute

def test_migration_AttributeSlot___init__():
    assert migration_AttributeSlot.__init__(migration_AttributeSlot('', migration_AttributeSlot=migration_EAttribute()), '', migration_AttributeSlot=migration_EAttribute()) == None

