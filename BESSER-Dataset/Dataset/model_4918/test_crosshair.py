from python_code import service_BusinessOperation
from python_code import service_Service

def test_service_BusinessOperation___init__():
    assert service_BusinessOperation.__init__(service_BusinessOperation('\x00\x00', '', service_BusinessOperation19=set(), service_BusinessOperation=service_Service()), '', '', service_BusinessOperation19=set(), service_BusinessOperation=service_Service()) == None


from python_code import service_Predicate
from python_code import service_Selection
from python_code import service_Service

def test_service_Selection___init__():
    assert service_Selection.__init__(service_Selection(False, 0, False, service_Selection9=set(), service_Selection13=set(), service_Selection11=service_Predicate(), Selection=service_Service(), selections=service_Service(), service_Selection=set()), False, 0, True, service_Selection9=set(), service_Selection13=set(), service_Selection11=service_Predicate(), Selection=service_Service(), selections=service_Service(), service_Selection=set()) == None


from python_code import service_Feature
from python_code import service_ServiceFeatureReference

def test_service_ServiceFeatureReference___init__():
    assert service_ServiceFeatureReference.__init__(service_ServiceFeatureReference('', service_ServiceFeatureReference=service_Feature()), '', service_ServiceFeatureReference=service_Feature()) == None

