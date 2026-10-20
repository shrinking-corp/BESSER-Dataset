from python_code import standard_Call
from python_code import standard_Usage

def test_standard_Call___init__():
    assert standard_Call.__init__(standard_Call(standard_Call=standard_Usage()), standard_Call=standard_Usage()) == None

def test_standard_Call_client_and_supplier_are_operations():
    assert standard_Call.client_and_supplier_are_operations(standard_Call(standard_Call=standard_Usage()), '', '') == None


from python_code import standard_BehavioralFeature
from python_code import standard_Create
from python_code import standard_Usage

def test_standard_Create___init__():
    assert standard_Create.__init__(standard_Create(standard_Create=standard_BehavioralFeature(), standard_Create4=standard_Usage()), standard_Create=standard_BehavioralFeature(), standard_Create4=standard_Usage()) == None

def test_standard_Create_client_and_supplier_are_classifiers():
    assert standard_Create.client_and_supplier_are_classifiers(standard_Create(standard_Create=standard_BehavioralFeature(), standard_Create4=standard_Usage()), '', '') == None


from python_code import standard_Component
from python_code import standard_Implement

def test_standard_Implement___init__():
    assert standard_Implement.__init__(standard_Implement(standard_Implement=standard_Component()), standard_Implement=standard_Component()) == None

def test_standard_Implement_implements_specification():
    assert standard_Implement.implements_specification(standard_Implement(standard_Implement=standard_Component()), '', '') == None


from python_code import standard_Class
from python_code import standard_ImplementationClass

def test_standard_ImplementationClass___init__():
    assert standard_ImplementationClass.__init__(standard_ImplementationClass(standard_ImplementationClass=standard_Class()), standard_ImplementationClass=standard_Class()) == None

def test_standard_ImplementationClass_cannot_be_realization():
    assert standard_ImplementationClass.cannot_be_realization(standard_ImplementationClass(standard_ImplementationClass=standard_Class()), '', '') == None


from python_code import standard_Instantiate
from python_code import standard_Usage

def test_standard_Instantiate___init__():
    assert standard_Instantiate.__init__(standard_Instantiate(standard_Instantiate=standard_Usage()), standard_Instantiate=standard_Usage()) == None

def test_standard_Instantiate_client_and_supplier_are_classifiers():
    assert standard_Instantiate.client_and_supplier_are_classifiers(standard_Instantiate(standard_Instantiate=standard_Usage()), '', '') == None


from python_code import standard_Classifier
from python_code import standard_Realization

def test_standard_Realization___init__():
    assert standard_Realization.__init__(standard_Realization(standard_Realization=standard_Classifier()), standard_Realization=standard_Classifier()) == None

def test_standard_Realization_cannot_be_implementationClass():
    assert standard_Realization.cannot_be_implementationClass(standard_Realization(standard_Realization=standard_Classifier()), '', '') == None


from python_code import standard_Send
from python_code import standard_Usage

def test_standard_Send___init__():
    assert standard_Send.__init__(standard_Send(standard_Send=standard_Usage()), standard_Send=standard_Usage()) == None

def test_standard_Send_client_operation_sends_supplier_signal():
    assert standard_Send.client_operation_sends_supplier_signal(standard_Send(standard_Send=standard_Usage()), '', '') == None


from python_code import standard_Classifier
from python_code import standard_Specification

def test_standard_Specification___init__():
    assert standard_Specification.__init__(standard_Specification(standard_Specification=standard_Classifier()), standard_Specification=standard_Classifier()) == None

def test_standard_Specification_cannot_be_type():
    assert standard_Specification.cannot_be_type(standard_Specification(standard_Specification=standard_Classifier()), '', '') == None


from python_code import standard_Class
from python_code import standard_Type

def test_standard_Type___init__():
    assert standard_Type.__init__(standard_Type(standard_Type=standard_Class()), standard_Type=standard_Class()) == None

def test_standard_Type_cannot_be_specification():
    assert standard_Type.cannot_be_specification(standard_Type(standard_Type=standard_Class()), '', '') == None


from python_code import standard_Class
from python_code import standard_Utility

def test_standard_Utility___init__():
    assert standard_Utility.__init__(standard_Utility(standard_Utility=standard_Class()), standard_Utility=standard_Class()) == None

def test_standard_Utility_is_utility():
    assert standard_Utility.is_utility(standard_Utility(standard_Utility=standard_Class()), '', '') == None

