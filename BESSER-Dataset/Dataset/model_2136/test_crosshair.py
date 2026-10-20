from python_code import model_administration_ProblemDetail

def test_model_administration_ProblemDetail___init__():
    assert model_administration_ProblemDetail.__init__(model_administration_ProblemDetail('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import model_administration_Status

def test_model_administration_Status___init__():
    assert model_administration_Status.__init__(model_administration_Status(''), '') == None


from python_code import model_base_Folder

def test_model_base_Folder___init__():
    assert model_base_Folder.__init__(model_base_Folder(True), False) == None


from python_code import model_base_IDescribed

def test_model_base_IDescribed___init__():
    assert model_base_IDescribed.__init__(model_base_IDescribed(''), '') == None


from python_code import model_base_IExternal

def test_model_base_IExternal___init__():
    assert model_base_IExternal.__init__(model_base_IExternal('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import model_base_IID

def test_model_base_IID___init__():
    assert model_base_IID.__init__(model_base_IID(''), '') == None


from python_code import model_base_INamed

def test_model_base_INamed___init__():
    assert model_base_INamed.__init__(model_base_INamed(''), '') == None


from python_code import model_base_IPositionable

def test_model_base_IPositionable___init__():
    assert model_base_IPositionable.__init__(model_base_IPositionable(0), 0) == None


from python_code import model_base_IRecycled

def test_model_base_IRecycled___init__():
    assert model_base_IRecycled.__init__(model_base_IRecycled(False, False), False, False) == None


from python_code import model_base_ISpecmatePositionableModelObject

def test_model_base_ISpecmatePositionableModelObject___init__():
    assert model_base_ISpecmatePositionableModelObject.__init__(model_base_ISpecmatePositionableModelObject(0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0) == None


from python_code import IContentElement
from python_code import model_batch_Operation

def test_model_batch_Operation___init__():
    assert model_batch_Operation.__init__(model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), '', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()) == None


from python_code import model_export_Export

def test_model_export_Export___init__():
    assert model_export_Export.__init__(model_export_Export('', '\x00'), '\x00\x00', '') == None


from python_code import model_history_Change

def test_model_history_Change___init__():
    assert model_history_Change.__init__(model_history_Change('', '', '', '', '', False, False), '', '\x00', '', '', '', False, False) == None


from python_code import model_history_HistoryEntry

def test_model_history_HistoryEntry___init__():
    assert model_history_HistoryEntry.__init__(model_history_HistoryEntry('', '', '', '', model_history_HistoryEntry=set()), '', '', '', '', model_history_HistoryEntry=set()) == None


from python_code import model_base_IModelNode
from python_code import model_processes_ProcessConnection

def test_model_processes_ProcessConnection___init__():
    assert model_processes_ProcessConnection.__init__(model_processes_ProcessConnection('', 0.0, 0.0, IModelConnection6=model_base_IModelNode(), IModelConnection=model_base_IModelNode()), '', 0.0, 0.0, IModelConnection6=model_base_IModelNode(), IModelConnection=model_base_IModelNode()) == None


from python_code import model_processes_ProcessStep

def test_model_processes_ProcessStep___init__():
    assert model_processes_ProcessStep.__init__(model_processes_ProcessStep(''), '') == None


from python_code import model_base_IModelNode
from python_code import model_requirements_CEGConnection

def test_model_requirements_CEGConnection___init__():
    assert model_requirements_CEGConnection.__init__(model_requirements_CEGConnection(True, IModelConnection6=model_base_IModelNode(), IModelConnection=model_base_IModelNode()), False, IModelConnection6=model_base_IModelNode(), IModelConnection=model_base_IModelNode()) == None


from python_code import model_requirements_CEGModel

def test_model_requirements_CEGModel___init__():
    assert model_requirements_CEGModel.__init__(model_requirements_CEGModel(''), '') == None


from python_code import model_base_IModelConnection
from python_code import model_requirements_CEGNode

def test_model_requirements_CEGNode___init__():
    assert model_requirements_CEGNode.__init__(model_requirements_CEGNode('', '', '\x00\x00', IModelNode3=model_base_IModelConnection(), IModelNode=model_base_IModelConnection()), '', '', '', IModelNode3=model_base_IModelConnection(), IModelNode=model_base_IModelConnection()) == None


from python_code import model_requirements_Requirement

def test_model_requirements_Requirement___init__():
    assert model_requirements_Requirement.__init__(model_requirements_Requirement(0, '', '', '', '\x00', '', '', False, ''), 0, '', '', '', '', '\x00', '', False, '') == None


from python_code import IContentElement
from python_code import TestParameter
from python_code import model_base_IContainer
from python_code import model_batch_Operation
from python_code import model_testspecification_ParameterAssignment

def test_model_testspecification_ParameterAssignment___init__():
    assert model_testspecification_ParameterAssignment.__init__(model_testspecification_ParameterAssignment('', '', assignments=TestParameter(), IContentElement18=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement21=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement=model_base_IContainer()), '', '', assignments=TestParameter(), IContentElement18=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=model_base_IContainer()), IContentElement21=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement=model_base_IContainer()) == None


from python_code import model_testspecification_TestCase

def test_model_testspecification_TestCase___init__():
    assert model_testspecification_TestCase.__init__(model_testspecification_TestCase(True), False) == None


from python_code import IContentElement
from python_code import model_base_IContainer
from python_code import model_batch_Operation
from python_code import model_testspecification_TestParameter

def test_model_testspecification_TestParameter___init__():
    assert model_testspecification_TestParameter.__init__(model_testspecification_TestParameter('', parameter=set(), IContentElement18=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement21=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement=model_base_IContainer()), '', parameter=set(), IContentElement18=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement21=model_batch_Operation('', model_batch_Operation=IContentElement(), model_batch_Operation20=IContentElement()), IContentElement=model_base_IContainer()) == None


from python_code import model_testspecification_TestProcedure

def test_model_testspecification_TestProcedure___init__():
    assert model_testspecification_TestProcedure.__init__(model_testspecification_TestProcedure(True), False) == None


from python_code import model_testspecification_TestStep

def test_model_testspecification_TestStep___init__():
    assert model_testspecification_TestStep.__init__(model_testspecification_TestStep('', model_testspecification_TestStep=set()), '', model_testspecification_TestStep=set()) == None

