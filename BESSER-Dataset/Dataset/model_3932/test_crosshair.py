from python_code import entity_Method
from python_code import entity_Service

def test_entity_Method___init__():
    assert entity_Method.__init__(entity_Method(True, entity_Method=entity_Service()), False, entity_Method=entity_Service()) == None


from python_code import entity_NamedElement

def test_entity_NamedElement___init__():
    assert entity_NamedElement.__init__(entity_NamedElement(''), '') == None

