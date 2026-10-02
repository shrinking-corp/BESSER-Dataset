from enum import Enum
from python_code import AttributeTargetsE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AttributeTargetsE.TASK, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AttributeTargetsE.TASK, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AttributeTargetsE.TASK, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AttributeTargetsE.TASK, 0)

def test_Enum___new___2():
    assert Enum.__new__(AttributeTargetsE.TASK, 'TASK') == AttributeTargetsE.TASK

from enum import Enum
from python_code import AttributeTypesE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AttributeTypesE.BOOL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AttributeTypesE.BOOL, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AttributeTypesE.BOOL, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AttributeTypesE.BOOL, 0)

def test_Enum___new___2():
    assert Enum.__new__(AttributeTypesE.BOOL, 'BOOL') == AttributeTypesE.BOOL

from enum import Enum
from python_code import BoolOperationTypesE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BoolOperationTypesE.XOR, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BoolOperationTypesE.AND, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BoolOperationTypesE.AND, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BoolOperationTypesE.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(BoolOperationTypesE.OR, 'OR') == BoolOperationTypesE.OR

from enum import Enum
from python_code import EndianessE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EndianessE.BIG, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EndianessE.BIG, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EndianessE.BIG, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EndianessE.BIG, 0)

def test_Enum___new___2():
    assert Enum.__new__(EndianessE.BIG, 'BIG') == EndianessE.BIG

from enum import Enum
from python_code import IntegretyStateE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IntegretyStateE.FAILED, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IntegretyStateE.FAILED, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IntegretyStateE.UNKNOWN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IntegretyStateE.OK, 0)

def test_Enum___new___2():
    assert Enum.__new__(IntegretyStateE.OK, 'OK') == IntegretyStateE.OK

from enum import Enum
from python_code import IoDirectionE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IoDirectionE.IN, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IoDirectionE.IN, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IoDirectionE.IN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IoDirectionE.IN, 0)

def test_Enum___new___2():
    assert Enum.__new__(IoDirectionE.IN, 'IN') == IoDirectionE.IN

from enum import Enum
from python_code import SymmetryTypesE
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SymmetryTypesE.AREA, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SymmetryTypesE.AREA, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SymmetryTypesE.AREA, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SymmetryTypesE.AREA, 0)

def test_Enum___new___2():
    assert Enum.__new__(SymmetryTypesE.AREA, 'AREA') == SymmetryTypesE.AREA

from python_code import MessageType
from python_code import oaam_allocations_MessageA

def test_oaam_allocations_MessageA___init__():
    assert oaam_allocations_MessageA.__init__(oaam_allocations_MessageA(False, 0, oaam_allocations_MessageA=set(), oaam_allocations_MessageA692=set(), oaam_allocations_MessageA694=set(), oaam_allocations_MessageA696=set(), oaam_allocations_MessageA698=MessageType()), False, 0, oaam_allocations_MessageA=set(), oaam_allocations_MessageA692=set(), oaam_allocations_MessageA694=set(), oaam_allocations_MessageA696=set(), oaam_allocations_MessageA698=MessageType()) == None

from python_code import oaam_allocations_Schedule

def test_oaam_allocations_Schedule___init__():
    assert oaam_allocations_Schedule.__init__(oaam_allocations_Schedule(0.0, False, 0, oaam_allocations_Schedule=set()), 0.0, False, 0, oaam_allocations_Schedule=set()) == None

from python_code import oaam_allocations_ScheduledTime

def test_oaam_allocations_ScheduledTime___init__():
    assert oaam_allocations_ScheduledTime.__init__(oaam_allocations_ScheduledTime(0, 0.0, 0.0, False), 0, 0.0, 0.0, True) == None

from python_code import SubmessageInMessageCapability
from python_code import oaam_allocations_Submessage

def test_oaam_allocations_Submessage___init__():
    assert oaam_allocations_Submessage.__init__(oaam_allocations_Submessage(0, oaam_allocations_Submessage=SubmessageInMessageCapability()), 0, oaam_allocations_Submessage=SubmessageInMessageCapability()) == None

from python_code import DuctOpening
from python_code import DuctType
from python_code import oaam_anatomy_Duct

def test_oaam_anatomy_Duct___init__():
    assert oaam_anatomy_Duct.__init__(oaam_anatomy_Duct(0.0, oaam_anatomy_Duct=DuctType(), oaam_anatomy_Duct414=DuctOpening(), oaam_anatomy_Duct417=DuctOpening()), 0.0, oaam_anatomy_Duct=DuctType(), oaam_anatomy_Duct414=DuctOpening(), oaam_anatomy_Duct417=DuctOpening()) == None

from python_code import LocationType
from python_code import Position3D
from python_code import oaam_anatomy_Location

def test_oaam_anatomy_Location___init__():
    assert oaam_anatomy_Location.__init__(oaam_anatomy_Location(0.0, oaam_anatomy_Location=LocationType(), oaam_anatomy_Location403=Position3D(), oaam_anatomy_Location405=set()), 0.0, oaam_anatomy_Location=LocationType(), oaam_anatomy_Location403=Position3D(), oaam_anatomy_Location405=set()) == None

from python_code import oaam_anatomy_Position3D

def test_oaam_anatomy_Position3D___init__():
    assert oaam_anatomy_Position3D.__init__(oaam_anatomy_Position3D(0.0, 0.0, 0.0), 0.0, 0.0, 0.0) == None

from python_code import ConnectionType
from python_code import DeviceType
from python_code import MessageType
from python_code import oaam_capabilities_MessageOnConnectionOrDeviceCapability

def test_oaam_capabilities_MessageOnConnectionOrDeviceCapability___init__():
    assert oaam_capabilities_MessageOnConnectionOrDeviceCapability.__init__(oaam_capabilities_MessageOnConnectionOrDeviceCapability(0.0, oaam_capabilities_MessageOnConnectionOrDeviceCapability=MessageType(), oaam_capabilities_MessageOnConnectionOrDeviceCapability499=DeviceType(), oaam_capabilities_MessageOnConnectionOrDeviceCapability502=ConnectionType()), 0.0, oaam_capabilities_MessageOnConnectionOrDeviceCapability=MessageType(), oaam_capabilities_MessageOnConnectionOrDeviceCapability499=DeviceType(), oaam_capabilities_MessageOnConnectionOrDeviceCapability502=ConnectionType()) == None

from python_code import ResourceType
from python_code import oaam_capabilities_ResourceConsumption
from python_code import oaam_common_AttributeContainment
from python_code import oaam_common_AttributeReference

def test_oaam_capabilities_ResourceConsumption___init__():
    assert oaam_capabilities_ResourceConsumption.__init__(oaam_capabilities_ResourceConsumption(0.0, oaam_capabilities_ResourceConsumption=set(), oaam_capabilities_ResourceConsumption489=ResourceType(), OaamBaseElementA=oaam_common_AttributeContainment(), OaamBaseElementA23=oaam_common_AttributeReference()), 0.0, oaam_capabilities_ResourceConsumption=set(), oaam_capabilities_ResourceConsumption489=ResourceType(), OaamBaseElementA=oaam_common_AttributeContainment(), OaamBaseElementA23=oaam_common_AttributeReference()) == None

from python_code import ConnectionType
from python_code import DeviceType
from python_code import SignalType
from python_code import oaam_capabilities_SignalOnConnectionOrDeviceCapability

def test_oaam_capabilities_SignalOnConnectionOrDeviceCapability___init__():
    assert oaam_capabilities_SignalOnConnectionOrDeviceCapability.__init__(oaam_capabilities_SignalOnConnectionOrDeviceCapability(0.0, oaam_capabilities_SignalOnConnectionOrDeviceCapability=SignalType(), oaam_capabilities_SignalOnConnectionOrDeviceCapability471=DeviceType(), oaam_capabilities_SignalOnConnectionOrDeviceCapability474=ConnectionType()), 0.0, oaam_capabilities_SignalOnConnectionOrDeviceCapability=SignalType(), oaam_capabilities_SignalOnConnectionOrDeviceCapability471=DeviceType(), oaam_capabilities_SignalOnConnectionOrDeviceCapability474=ConnectionType()) == None

from python_code import DeviceType
from python_code import TaskType
from python_code import oaam_capabilities_TaskOnDeviceCapability

def test_oaam_capabilities_TaskOnDeviceCapability___init__():
    assert oaam_capabilities_TaskOnDeviceCapability.__init__(oaam_capabilities_TaskOnDeviceCapability(0.0, 0.0, oaam_capabilities_TaskOnDeviceCapability=TaskType(), oaam_capabilities_TaskOnDeviceCapability453=DeviceType()), 0.0, 0.0, oaam_capabilities_TaskOnDeviceCapability=TaskType(), oaam_capabilities_TaskOnDeviceCapability453=DeviceType()) == None
