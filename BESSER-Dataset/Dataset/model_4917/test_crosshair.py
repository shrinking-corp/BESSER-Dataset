from python_code import service_BusinessOperation
from python_code import service_Service

def test_service_BusinessOperation___init__():
    assert service_BusinessOperation.__init__(service_BusinessOperation('\x00\x00', '', BusinessOperation=service_Service(), operations=service_Service(), service_BusinessOperation=set()), '', '', BusinessOperation=service_Service(), operations=service_Service(), service_BusinessOperation=set()) == None


from python_code import service_Constant
from python_code import service_ConstantReference

def test_service_ConstantReference___init__():
    assert service_ConstantReference.__init__(service_ConstantReference('', service_ConstantReference=service_Constant()), '', service_ConstantReference=service_Constant()) == None


from python_code import service_Feature
from python_code import service_ServiceFeatureReference

def test_service_ServiceFeatureReference___init__():
    assert service_ServiceFeatureReference.__init__(service_ServiceFeatureReference('', service_ServiceFeatureReference=service_Feature()), '', service_ServiceFeatureReference=service_Feature()) == None

