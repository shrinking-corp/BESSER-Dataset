from python_code import domainmodel_AbstractElement
from python_code import domainmodel_Domainmodel

def test_domainmodel_AbstractElement___init__():
    assert domainmodel_AbstractElement.__init__(domainmodel_AbstractElement('', domainmodel_AbstractElement=domainmodel_Domainmodel()), '', domainmodel_AbstractElement=domainmodel_Domainmodel()) == None


from python_code import domainmodel_BindEnumSource

def test_domainmodel_BindEnumSource___init__():
    assert domainmodel_BindEnumSource.__init__(domainmodel_BindEnumSource(''), '') == None


from python_code import domainmodel_ContainerElement

def test_domainmodel_ContainerElement___init__():
    assert domainmodel_ContainerElement.__init__(domainmodel_ContainerElement('', domainmodel_ContainerElement=set()), '', domainmodel_ContainerElement=set()) == None


from python_code import domainmodel_ContentElement

def test_domainmodel_ContentElement___init__():
    assert domainmodel_ContentElement.__init__(domainmodel_ContentElement(''), '') == None


from python_code import domainmodel_DataType

def test_domainmodel_DataType___init__():
    assert domainmodel_DataType.__init__(domainmodel_DataType('', '', '\x00\x00'), '', '', '') == None


from python_code import domainmodel_Import

def test_domainmodel_Import___init__():
    assert domainmodel_Import.__init__(domainmodel_Import(''), '') == None


from python_code import domainmodel_MainFeature
from python_code import domainmodel_MainFeatureOption

def test_domainmodel_MainFeatureOption___init__():
    assert domainmodel_MainFeatureOption.__init__(domainmodel_MainFeatureOption('', domainmodel_MainFeatureOption=domainmodel_MainFeature()), '', domainmodel_MainFeatureOption=domainmodel_MainFeature()) == None


from python_code import domainmodel_NavigateToAction
from python_code import domainmodel_ScreenFeature

def test_domainmodel_ScreenFeature___init__():
    assert domainmodel_ScreenFeature.__init__(domainmodel_ScreenFeature('', domainmodel_ScreenFeature101=set(), domainmodel_ScreenFeature=domainmodel_NavigateToAction()), '', domainmodel_ScreenFeature101=set(), domainmodel_ScreenFeature=domainmodel_NavigateToAction()) == None


from python_code import domainmodel_SetRestCallReceiverIDParameter

def test_domainmodel_SetRestCallReceiverIDParameter___init__():
    assert domainmodel_SetRestCallReceiverIDParameter.__init__(domainmodel_SetRestCallReceiverIDParameter(''), '') == None


from python_code import domainmodel_SetRestCallReceiverURLParameter

def test_domainmodel_SetRestCallReceiverURLParameter___init__():
    assert domainmodel_SetRestCallReceiverURLParameter.__init__(domainmodel_SetRestCallReceiverURLParameter(''), '') == None


from python_code import domainmodel_InterfaceOperationsUsageRule
from python_code import domainmodel_StatelessComponent

def test_domainmodel_StatelessComponent___init__():
    assert domainmodel_StatelessComponent.__init__(domainmodel_StatelessComponent('', domainmodel_StatelessComponent=domainmodel_InterfaceOperationsUsageRule()), '', domainmodel_StatelessComponent=domainmodel_InterfaceOperationsUsageRule()) == None


from python_code import domainmodel_AttachAction
from python_code import domainmodel_ExecuteAction
from python_code import domainmodel_UIActionModule

def test_domainmodel_UIActionModule___init__():
    assert domainmodel_UIActionModule.__init__(domainmodel_UIActionModule('', domainmodel_UIActionModule=domainmodel_AttachAction(), domainmodel_UIActionModule73=domainmodel_ExecuteAction(), domainmodel_UIActionModule98=set()), '', domainmodel_UIActionModule=domainmodel_AttachAction(), domainmodel_UIActionModule73=domainmodel_ExecuteAction(), domainmodel_UIActionModule98=set()) == None

