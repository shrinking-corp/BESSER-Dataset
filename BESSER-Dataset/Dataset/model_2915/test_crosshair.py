from python_code import metamodel_EntityObserver
from python_code import metamodel_Extension_MQPublishing

def test_metamodel_Extension_MQPublishing___init__():
    assert metamodel_Extension_MQPublishing.__init__(metamodel_Extension_MQPublishing('', metamodel_Extension_MQPublishing=metamodel_EntityObserver()), '', metamodel_Extension_MQPublishing=metamodel_EntityObserver()) == None


from python_code import metamodel_Validation_ValueRestriction
from python_code import metamodel_ValueRestriction_Value

def test_metamodel_ValueRestriction_Value___init__():
    assert metamodel_ValueRestriction_Value.__init__(metamodel_ValueRestriction_Value('', metamodel_ValueRestriction_Value=metamodel_Validation_ValueRestriction()), '', metamodel_ValueRestriction_Value=metamodel_Validation_ValueRestriction()) == None

