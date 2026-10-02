from enum import Enum
from python_code import AccessCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessCategory.bus, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessCategory.data, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessCategory.data, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessCategory.bus, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessCategory.bus, 'bus') == AccessCategory.bus

from enum import Enum
from python_code import AccessType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessType.requires, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessType.requires, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessType.provides, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessType.requires, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessType.requires, 'requires') == AccessType.requires

from enum import Enum
from python_code import ComponentCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ComponentCategory.memory, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ComponentCategory.bus, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ComponentCategory.data, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ComponentCategory.bus, '')

def test_Enum___new___2():
    assert Enum.__new__(ComponentCategory.bus, 'bus') == ComponentCategory.bus

from enum import Enum
from python_code import DirectionType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DirectionType.in_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DirectionType.in_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DirectionType.in_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DirectionType.in_, 0)

def test_Enum___new___2():
    assert Enum.__new__(DirectionType.in_, 'in_') == DirectionType.in_

from enum import Enum
from python_code import FlowKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FlowKind.sink, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FlowKind.sink, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FlowKind.sink, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FlowKind.sink, 0)

def test_Enum___new___2():
    assert Enum.__new__(FlowKind.sink, 'sink') == FlowKind.sink

from enum import Enum
from python_code import OperationKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OperationKind.or_, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OperationKind.or_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OperationKind.or_, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OperationKind.or_, 0)

def test_Enum___new___2():
    assert Enum.__new__(OperationKind.or_, 'or_') == OperationKind.or_

from enum import Enum
from python_code import PortCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PortCategory.data, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PortCategory.data, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PortCategory.data, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PortCategory.data, 0)

def test_Enum___new___2():
    assert Enum.__new__(PortCategory.data, 'data') == PortCategory.data

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
    assert aadl2_BehavioredImplementation.__init__(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation421=set(), aadl2_BehavioredImplementation=set()), aadl2_BehavioredImplementation421=set(), aadl2_BehavioredImplementation=set()) == None

def test_aadl2_BehavioredImplementation_subprogramCalls():
    assert aadl2_BehavioredImplementation.subprogramCalls(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation421=set(), aadl2_BehavioredImplementation=set())) == None

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
    assert aadl2_BusAccess.__init__(aadl2_BusAccess('', aadl2_BusAccess=aadl2_FeatureGroupType(), aadl2_BusAccess242=aadl2_BusFeatureClassifier(), aadl2_BusAccess424=aadl2_AbstractType(), aadl2_BusAccess498=aadl2_BusType(), aadl2_BusAccess533=aadl2_DeviceType(), aadl2_BusAccess549=aadl2_MemoryType(), aadl2_BusAccess600=aadl2_SystemType(), aadl2_BusAccess661=aadl2_ProcessorType(), aadl2_BusAccess776=aadl2_VirtualBusType(), aadl2_BusAccess795=aadl2_VirtualProcessorType()), '', aadl2_BusAccess=aadl2_FeatureGroupType(), aadl2_BusAccess242=aadl2_BusFeatureClassifier(), aadl2_BusAccess424=aadl2_AbstractType(), aadl2_BusAccess498=aadl2_BusType(), aadl2_BusAccess533=aadl2_DeviceType(), aadl2_BusAccess549=aadl2_MemoryType(), aadl2_BusAccess600=aadl2_SystemType(), aadl2_BusAccess661=aadl2_ProcessorType(), aadl2_BusAccess776=aadl2_VirtualBusType(), aadl2_BusAccess795=aadl2_VirtualProcessorType()) == None

from python_code import aadl2_ComponentPrototypeActual
from python_code import aadl2_ComponentPrototypeBinding
from python_code import aadl2_SubcomponentType

def test_aadl2_ComponentPrototypeActual___init__():
    assert aadl2_ComponentPrototypeActual.__init__(aadl2_ComponentPrototypeActual('', aadl2_ComponentPrototypeActual388=set(), aadl2_ComponentPrototypeActual391=aadl2_SubcomponentType(), aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding()), '', aadl2_ComponentPrototypeActual388=set(), aadl2_ComponentPrototypeActual391=aadl2_SubcomponentType(), aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding()) == None

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

def test_aadl2_ModalPath_getAllInModeTransitions():
    assert aadl2_ModalPath.getAllInModeTransitions(aadl2_ModalPath(aadl2_ModalPath=set())) == None

def test_aadl2_ModalPath_getInModeTransitions():
    assert aadl2_ModalPath.getInModeTransitions(aadl2_ModalPath(aadl2_ModalPath=set())) == None

def test_aadl2_ModalPath_getInModes():
    assert aadl2_ModalPath.getInModes(aadl2_ModalPath(aadl2_ModalPath=set())) == None

from python_code import aadl2_Operation

def test_aadl2_Operation___init__():
    assert aadl2_Operation.__init__(aadl2_Operation('', aadl2_Operation=set()), '', aadl2_Operation=set()) == None
