from python_code import service_SL
from python_code import service_ServiceConsumer

def test_service_ServiceConsumer___init__():
    assert service_ServiceConsumer.__init__(service_ServiceConsumer('', service_ServiceConsumer=set(), service_ServiceConsumer20=service_SL()), '', service_ServiceConsumer=set(), service_ServiceConsumer20=service_SL()) == None


from python_code import ExecutionFramework
from python_code import service_architecture_DeployedService

def test_service_architecture_DeployedService___init__():
    assert service_architecture_DeployedService.__init__(service_architecture_DeployedService('', deployedService=ExecutionFramework()), '', deployedService=ExecutionFramework()) == None


from python_code import service_architecture_ExecutionFramework

def test_service_architecture_ExecutionFramework___init__():
    assert service_architecture_ExecutionFramework.__init__(service_architecture_ExecutionFramework('', deploy=set()), '', deploy=set()) == None


from python_code import semantics_service_Service
from python_code import service_semantics_ProcessModel

def test_service_semantics_ProcessModel___init__():
    assert service_semantics_ProcessModel.__init__(service_semantics_ProcessModel('', describedBy=semantics_service_Service()), '', describedBy=semantics_service_Service()) == None


from python_code import service_semantics_ServiceCategory

def test_service_semantics_ServiceCategory___init__():
    assert service_semantics_ServiceCategory.__init__(service_semantics_ServiceCategory('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import InterfaceDescription
from python_code import ProcessModel
from python_code import semantics_service_Service
from python_code import service_semantics_ServiceGrounding

def test_service_semantics_ServiceGrounding___init__():
    assert service_semantics_ServiceGrounding.__init__(service_semantics_ServiceGrounding('', '\x00', supports=semantics_service_Service(), service_semantics_ServiceGrounding=ProcessModel(), service_semantics_ServiceGrounding66=InterfaceDescription()), '\x00\x00', '', supports=semantics_service_Service(), service_semantics_ServiceGrounding=ProcessModel(), service_semantics_ServiceGrounding66=InterfaceDescription()) == None


from python_code import semantics_service_EObject
from python_code import service_semantics_ServiceParameter

def test_service_semantics_ServiceParameter___init__():
    assert service_semantics_ServiceParameter.__init__(service_semantics_ServiceParameter('', service_semantics_ServiceParameter=semantics_service_EObject()), '', service_semantics_ServiceParameter=semantics_service_EObject()) == None


from python_code import ProcessModel
from python_code import ServiceCategory
from python_code import semantics_service_Service
from python_code import service_semantics_ServiceProfile

def test_service_semantics_ServiceProfile___init__():
    assert service_semantics_ServiceProfile.__init__(service_semantics_ServiceProfile('', '', presents=semantics_service_Service(), service_semantics_ServiceProfile=ProcessModel(), service_semantics_ServiceProfile52=ServiceCategory(), service_semantics_ServiceProfile54=set(), service_semantics_ServiceProfile56=set(), service_semantics_ServiceProfile58=set(), service_semantics_ServiceProfile60=set()), '\x00', '', presents=semantics_service_Service(), service_semantics_ServiceProfile=ProcessModel(), service_semantics_ServiceProfile52=ServiceCategory(), service_semantics_ServiceProfile54=set(), service_semantics_ServiceProfile56=set(), service_semantics_ServiceProfile58=set(), service_semantics_ServiceProfile60=set()) == None


from python_code import InterfaceDescription
from python_code import service_syntax_Binding

def test_service_syntax_Binding___init__():
    assert service_syntax_Binding.__init__(service_syntax_Binding('', '', '\x00\x00', binding=InterfaceDescription()), '', '', '', binding=InterfaceDescription()) == None


from python_code import Binding
from python_code import DeployedService
from python_code import service_syntax_Endpoint
from python_code import syntax_service_ServiceImplemetation

def test_service_syntax_Endpoint___init__():
    assert service_syntax_Endpoint.__init__(service_syntax_Endpoint('', '\x00', service_syntax_Endpoint=Binding(), service_syntax_Endpoint43=syntax_service_ServiceImplemetation(), service_syntax_Endpoint45=DeployedService()), '\x00\x00', '', service_syntax_Endpoint=Binding(), service_syntax_Endpoint43=syntax_service_ServiceImplemetation(), service_syntax_Endpoint45=DeployedService()) == None


from python_code import service_syntax_InterfaceDescription
from python_code import syntax_service_SchemaType

def test_service_syntax_InterfaceDescription___init__():
    assert service_syntax_InterfaceDescription.__init__(service_syntax_InterfaceDescription('', service_syntax_InterfaceDescription=set(), type=set(), service_syntax_InterfaceDescription26=syntax_service_SchemaType(), service_syntax_InterfaceDescription28=set()), '', service_syntax_InterfaceDescription=set(), type=set(), service_syntax_InterfaceDescription26=syntax_service_SchemaType(), service_syntax_InterfaceDescription28=set()) == None


from python_code import service_syntax_Message
from python_code import syntax_service_TopLevelComplexType
from python_code import syntax_service_TopLevelElement

def test_service_syntax_Message___init__():
    assert service_syntax_Message.__init__(service_syntax_Message('', service_syntax_Message=syntax_service_TopLevelComplexType(), service_syntax_Message39=syntax_service_TopLevelElement()), '', service_syntax_Message=syntax_service_TopLevelComplexType(), service_syntax_Message39=syntax_service_TopLevelElement()) == None


from python_code import service_syntax_OperationDescription

def test_service_syntax_OperationDescription___init__():
    assert service_syntax_OperationDescription.__init__(service_syntax_OperationDescription('', service_syntax_OperationDescription=set(), service_syntax_OperationDescription32=set(), service_syntax_OperationDescription35=set()), '', service_syntax_OperationDescription=set(), service_syntax_OperationDescription32=set(), service_syntax_OperationDescription35=set()) == None


from python_code import service_template_AbstractProcessModel

def test_service_template_AbstractProcessModel___init__():
    assert service_template_AbstractProcessModel.__init__(service_template_AbstractProcessModel(''), '') == None


from python_code import ServiceTemplate
from python_code import service_template_GroundTemplate
from python_code import template_service_Service

def test_service_template_GroundTemplate___init__():
    assert service_template_GroundTemplate.__init__(service_template_GroundTemplate('', service_template_GroundTemplate=ServiceTemplate(), service_template_GroundTemplate97=set(), service_template_GroundTemplate99=set(), adaptedBy=template_service_Service()), '', service_template_GroundTemplate=ServiceTemplate(), service_template_GroundTemplate97=set(), service_template_GroundTemplate99=set(), adaptedBy=template_service_Service()) == None


from python_code import AbstractProcessModel
from python_code import TemplateFlow
from python_code import service_template_ServiceTemplate

def test_service_template_ServiceTemplate___init__():
    assert service_template_ServiceTemplate.__init__(service_template_ServiceTemplate('', service_template_ServiceTemplate=TemplateFlow(), service_template_ServiceTemplate89=set(), service_template_ServiceTemplate91=AbstractProcessModel(), service_template_ServiceTemplate93=set()), '', service_template_ServiceTemplate=TemplateFlow(), service_template_ServiceTemplate89=set(), service_template_ServiceTemplate91=AbstractProcessModel(), service_template_ServiceTemplate93=set()) == None

