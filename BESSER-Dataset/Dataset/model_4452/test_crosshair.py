from enum import Enum
from python_code import ActuatorType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActuatorType.Led, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActuatorType.LCD, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActuatorType.LCD, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActuatorType.LCD, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActuatorType.Led, 'LCD') == ActuatorType.LCD

from enum import Enum
from python_code import CommunicationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CommunicationType.Serial, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CommunicationType.Serial, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CommunicationType.Serial, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CommunicationType.WiFi, 0)

def test_Enum___new___2():
    assert Enum.__new__(CommunicationType.WiFi, 'WiFi') == CommunicationType.WiFi

from enum import Enum
from python_code import ControllerType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ControllerType.ESP8266, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ControllerType.ESP8266, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ControllerType.ESP8266, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ControllerType.ESP8266, 0)

def test_Enum___new___2():
    assert Enum.__new__(ControllerType.ESP8266, 'ESP8266') == ControllerType.ESP8266

from enum import Enum
from python_code import DBType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DBType.MySQL, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DBType.MySQL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DBType.MySQL, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DBType.MySQL, 0)

def test_Enum___new___2():
    assert Enum.__new__(DBType.MySQL, 'MySQL') == DBType.MySQL

from enum import Enum
from python_code import MessageBrokerType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MessageBrokerType.MQTT, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MessageBrokerType.MQTT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MessageBrokerType.MQTT, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MessageBrokerType.MQTT, 0)

def test_Enum___new___2():
    assert Enum.__new__(MessageBrokerType.MQTT, 'MQTT') == MessageBrokerType.MQTT

from enum import Enum
from python_code import PortType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PortType.Analog, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PortType.Analog, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PortType.Digital, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PortType.Analog, 0)

def test_Enum___new___2():
    assert Enum.__new__(PortType.Analog, 'Analog') == PortType.Analog

from enum import Enum
from python_code import SensorType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SensorType.Button, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SensorType.Light, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SensorType.CO2, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SensorType.CO2, '')

def test_Enum___new___2():
    assert Enum.__new__(SensorType.CO2, 'CO2') == SensorType.CO2

from python_code import wsmodel3_DBServer
from python_code import wsmodel3_WebService

def test_wsmodel3_DBServer___init__():
    assert wsmodel3_DBServer.__init__(wsmodel3_DBServer('', '', '', '', 0, wsmodel3_DBServer=wsmodel3_WebService()), '', '', '', '', 0, wsmodel3_DBServer=wsmodel3_WebService()) == None

from python_code import wsmodel3_Data

def test_wsmodel3_Data___init__():
    assert wsmodel3_Data.__init__(wsmodel3_Data('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import wsmodel3_InputPort
from python_code import wsmodel3_OutputBridge
from python_code import wsmodel3_Sensor

def test_wsmodel3_Sensor___init__():
    assert wsmodel3_Sensor.__init__(wsmodel3_Sensor('', wsmodel3_Sensor=wsmodel3_InputPort(), wsmodel3_Sensor46=wsmodel3_OutputBridge()), '', wsmodel3_Sensor=wsmodel3_InputPort(), wsmodel3_Sensor46=wsmodel3_OutputBridge()) == None
