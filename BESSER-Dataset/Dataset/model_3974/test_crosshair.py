from python_code import l2_Call
from python_code import l2_Usage

def test_l2_Call___init__():
    assert l2_Call.__init__(l2_Call(l2_Call=l2_Usage()), l2_Call=l2_Usage()) == None

def test_l2_Call_client_and_supplier_are_operations():
    assert l2_Call.client_and_supplier_are_operations(l2_Call(l2_Call=l2_Usage()), '', '') == None


from python_code import l2_BehavioralFeature
from python_code import l2_Create
from python_code import l2_Usage

def test_l2_Create___init__():
    assert l2_Create.__init__(l2_Create(l2_Create=l2_BehavioralFeature(), l2_Create4=l2_Usage()), l2_Create=l2_BehavioralFeature(), l2_Create4=l2_Usage()) == None

def test_l2_Create_client_and_supplier_are_classifiers():
    assert l2_Create.client_and_supplier_are_classifiers(l2_Create(l2_Create=l2_BehavioralFeature(), l2_Create4=l2_Usage()), '', '') == None


from python_code import l2_Component
from python_code import l2_Implement

def test_l2_Implement___init__():
    assert l2_Implement.__init__(l2_Implement(l2_Implement=l2_Component()), l2_Implement=l2_Component()) == None

def test_l2_Implement_implements_specification():
    assert l2_Implement.implements_specification(l2_Implement(l2_Implement=l2_Component()), '', '') == None


from python_code import l2_Class
from python_code import l2_ImplementationClass

def test_l2_ImplementationClass___init__():
    assert l2_ImplementationClass.__init__(l2_ImplementationClass(l2_ImplementationClass=l2_Class()), l2_ImplementationClass=l2_Class()) == None

def test_l2_ImplementationClass_cannot_be_realization():
    assert l2_ImplementationClass.cannot_be_realization(l2_ImplementationClass(l2_ImplementationClass=l2_Class()), '', '') == None


from python_code import l2_Instantiate
from python_code import l2_Usage

def test_l2_Instantiate___init__():
    assert l2_Instantiate.__init__(l2_Instantiate(l2_Instantiate=l2_Usage()), l2_Instantiate=l2_Usage()) == None

def test_l2_Instantiate_client_and_supplier_are_classifiers():
    assert l2_Instantiate.client_and_supplier_are_classifiers(l2_Instantiate(l2_Instantiate=l2_Usage()), '', '') == None


from python_code import l2_Classifier
from python_code import l2_Realization

def test_l2_Realization___init__():
    assert l2_Realization.__init__(l2_Realization(l2_Realization=l2_Classifier()), l2_Realization=l2_Classifier()) == None

def test_l2_Realization_cannot_be_implementationClass():
    assert l2_Realization.cannot_be_implementationClass(l2_Realization(l2_Realization=l2_Classifier()), '', '') == None


from python_code import l2_Send
from python_code import l2_Usage

def test_l2_Send___init__():
    assert l2_Send.__init__(l2_Send(l2_Send=l2_Usage()), l2_Send=l2_Usage()) == None

def test_l2_Send_client_operation_sends_supplier_signal():
    assert l2_Send.client_operation_sends_supplier_signal(l2_Send(l2_Send=l2_Usage()), '', '') == None


from python_code import l2_Classifier
from python_code import l2_Specification

def test_l2_Specification___init__():
    assert l2_Specification.__init__(l2_Specification(l2_Specification=l2_Classifier()), l2_Specification=l2_Classifier()) == None

def test_l2_Specification_cannot_be_type():
    assert l2_Specification.cannot_be_type(l2_Specification(l2_Specification=l2_Classifier()), '', '') == None


from python_code import l2_Class
from python_code import l2_Type

def test_l2_Type___init__():
    assert l2_Type.__init__(l2_Type(l2_Type=l2_Class()), l2_Type=l2_Class()) == None

def test_l2_Type_cannot_be_specification():
    assert l2_Type.cannot_be_specification(l2_Type(l2_Type=l2_Class()), '', '') == None


from python_code import l2_Class
from python_code import l2_Utility

def test_l2_Utility___init__():
    assert l2_Utility.__init__(l2_Utility(l2_Utility=l2_Class()), l2_Utility=l2_Class()) == None

def test_l2_Utility_is_utility():
    assert l2_Utility.is_utility(l2_Utility(l2_Utility=l2_Class()), '', '') == None

