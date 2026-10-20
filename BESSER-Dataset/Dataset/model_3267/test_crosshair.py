from python_code import aadl2_Access

def test_aadl2_Access___init__():
    assert aadl2_Access.__init__(aadl2_Access('', '\x00'), '\x00\x00', '') == None


from python_code import aadl2_ArrayDimension
from python_code import aadl2_ArraySize
from python_code import aadl2_ArraySizeProperty

def test_aadl2_ArraySize___init__():
    assert aadl2_ArraySize.__init__(aadl2_ArraySize('', aadl2_ArraySize91=aadl2_ArraySizeProperty(), aadl2_ArraySize=aadl2_ArrayDimension()), '', aadl2_ArraySize91=aadl2_ArraySizeProperty(), aadl2_ArraySize=aadl2_ArrayDimension()) == None


from python_code import aadl2_BehavioredImplementation

def test_aadl2_BehavioredImplementation___init__():
    assert aadl2_BehavioredImplementation.__init__(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation422=set()), aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation422=set()) == None

def test_aadl2_BehavioredImplementation_subprogramCalls():
    assert aadl2_BehavioredImplementation.subprogramCalls(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation422=set())) == None


from python_code import aadl2_BooleanLiteral

def test_aadl2_BooleanLiteral___init__():
    assert aadl2_BooleanLiteral.__init__(aadl2_BooleanLiteral(''), '') == None


from python_code import aadl2_AbstractType
from python_code import aadl2_BusAccess
from python_code import aadl2_BusFeatureClassifier
from python_code import aadl2_BusType
from python_code import aadl2_DeviceType
from python_code import aadl2_FeatureGroupType
from python_code import aadl2_MemoryType
from python_code import aadl2_ProcessorType
from python_code import aadl2_SystemType
from python_code import aadl2_VirtualBusType
from python_code import aadl2_VirtualProcessorType

def test_aadl2_BusAccess___init__():
    assert aadl2_BusAccess.__init__(aadl2_BusAccess('', aadl2_BusAccess242=aadl2_BusFeatureClassifier(), aadl2_BusAccess=aadl2_FeatureGroupType(), aadl2_BusAccess425=aadl2_AbstractType(), aadl2_BusAccess499=aadl2_BusType(), aadl2_BusAccess534=aadl2_DeviceType(), aadl2_BusAccess550=aadl2_MemoryType(), aadl2_BusAccess601=aadl2_SystemType(), aadl2_BusAccess662=aadl2_ProcessorType(), aadl2_BusAccess777=aadl2_VirtualBusType(), aadl2_BusAccess796=aadl2_VirtualProcessorType()), '', aadl2_BusAccess242=aadl2_BusFeatureClassifier(), aadl2_BusAccess=aadl2_FeatureGroupType(), aadl2_BusAccess425=aadl2_AbstractType(), aadl2_BusAccess499=aadl2_BusType(), aadl2_BusAccess534=aadl2_DeviceType(), aadl2_BusAccess550=aadl2_MemoryType(), aadl2_BusAccess601=aadl2_SystemType(), aadl2_BusAccess662=aadl2_ProcessorType(), aadl2_BusAccess777=aadl2_VirtualBusType(), aadl2_BusAccess796=aadl2_VirtualProcessorType()) == None


from python_code import aadl2_ComponentPrototypeActual
from python_code import aadl2_ComponentPrototypeBinding
from python_code import aadl2_SubcomponentType

def test_aadl2_ComponentPrototypeActual___init__():
    assert aadl2_ComponentPrototypeActual.__init__(aadl2_ComponentPrototypeActual('', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding(), aadl2_ComponentPrototypeActual389=set(), aadl2_ComponentPrototypeActual392=aadl2_SubcomponentType()), '', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding(), aadl2_ComponentPrototypeActual389=set(), aadl2_ComponentPrototypeActual392=aadl2_SubcomponentType()) == None


from python_code import aadl2_ComputedValue

def test_aadl2_ComputedValue___init__():
    assert aadl2_ComputedValue.__init__(aadl2_ComputedValue(''), '') == None


from python_code import aadl2_AnnexLibrary
from python_code import aadl2_DefaultAnnexLibrary

def test_aadl2_DefaultAnnexLibrary___init__():
    assert aadl2_DefaultAnnexLibrary.__init__(aadl2_DefaultAnnexLibrary('', aadl2_DefaultAnnexLibrary=aadl2_AnnexLibrary()), '', aadl2_DefaultAnnexLibrary=aadl2_AnnexLibrary()) == None


from python_code import aadl2_AnnexSubclause
from python_code import aadl2_DefaultAnnexSubclause

def test_aadl2_DefaultAnnexSubclause___init__():
    assert aadl2_DefaultAnnexSubclause.__init__(aadl2_DefaultAnnexSubclause('', aadl2_DefaultAnnexSubclause=aadl2_AnnexSubclause()), '', aadl2_DefaultAnnexSubclause=aadl2_AnnexSubclause()) == None


from python_code import aadl2_DirectedFeature

def test_aadl2_DirectedFeature___init__():
    assert aadl2_DirectedFeature.__init__(aadl2_DirectedFeature('', '', '\x00\x00'), '', '', '') == None


from python_code import aadl2_IntegerLiteral

def test_aadl2_IntegerLiteral___init__():
    assert aadl2_IntegerLiteral.__init__(aadl2_IntegerLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import aadl2_ModalPath

def test_aadl2_ModalPath___init__():
    assert aadl2_ModalPath.__init__(aadl2_ModalPath(aadl2_ModalPath=set()), aadl2_ModalPath=set()) == None

def test_aadl2_ModalPath_getInModes():
    assert aadl2_ModalPath.getInModes(aadl2_ModalPath(aadl2_ModalPath=set())) == None

def test_aadl2_ModalPath_getInModeTransitions():
    assert aadl2_ModalPath.getInModeTransitions(aadl2_ModalPath(aadl2_ModalPath=set())) == None

def test_aadl2_ModalPath_getAllInModeTransitions():
    assert aadl2_ModalPath.getAllInModeTransitions(aadl2_ModalPath(aadl2_ModalPath=set())) == None


from python_code import aadl2_Operation

def test_aadl2_Operation___init__():
    assert aadl2_Operation.__init__(aadl2_Operation('', aadl2_Operation=set()), '', aadl2_Operation=set()) == None

