from enum import Enum
from python_code import PropertyTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PropertyTypes.Date, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PropertyTypes.Date, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PropertyTypes.Date, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PropertyTypes.Date, 0)

def test_Enum___new___2():
    assert Enum.__new__(PropertyTypes.Float, 'Date') == PropertyTypes.Date

from enum import Enum
from python_code import SourceActiveStates
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SourceActiveStates.Filled, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SourceActiveStates.Unknown, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SourceActiveStates.Filling, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SourceActiveStates.Filled, 0)

def test_Enum___new___2():
    assert Enum.__new__(SourceActiveStates.Filled, 'Filled') == SourceActiveStates.Filled

from enum import Enum
from python_code import SourceState
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SourceState.Error, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SourceState.Error, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SourceState.Error, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SourceState.Error, 0)

def test_Enum___new___2():
    assert Enum.__new__(SourceState.Error, 'Error') == SourceState.Error

from python_code import application_ApplicationKeyConfig

def test_application_ApplicationKeyConfig___init__():
    assert application_ApplicationKeyConfig.__init__(application_ApplicationKeyConfig(''), '') == None

def test_application_ApplicationKeyConfig_hasApplicationKey():
    assert application_ApplicationKeyConfig.hasApplicationKey(application_ApplicationKeyConfig(''), 0) == None

from python_code import application_ConfigurableElement
from python_code import application_Configuration

def test_application_ConfigurableElement___init__():
    assert application_ConfigurableElement.__init__(application_ConfigurableElement('', '', '', '', '', '', application_ConfigurableElement=application_Configuration()), '', '', '', '', '\x00', '', application_ConfigurableElement=application_Configuration()) == None

def test_application_ConfigurableElement_isPropertyTrueElseDefault():
    assert application_ConfigurableElement.isPropertyTrueElseDefault(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '', '') == None

def test_application_ConfigurableElement_removeProperty():
    assert application_ConfigurableElement.removeProperty(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '') == None

def test_application_ConfigurableElement_addProperty():
    assert application_ConfigurableElement.addProperty(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '') == None

def test_application_ConfigurableElement_getProperty():
    assert application_ConfigurableElement.getProperty(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '') == None

def test_application_ConfigurableElement_getPropertyValueElseDefault():
    assert application_ConfigurableElement.getPropertyValueElseDefault(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '', '') == None

def test_application_ConfigurableElement_getPropertyValue():
    assert application_ConfigurableElement.getPropertyValue(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '') == None

def test_application_ConfigurableElement_isPropertyTrue():
    assert application_ConfigurableElement.isPropertyTrue(application_ConfigurableElement('', '', '\x00\x00', '', '', '', application_ConfigurableElement=application_Configuration()), '') == None

from python_code import application_FEEDInterface

def test_application_FEEDInterface___init__():
    assert application_FEEDInterface.__init__(application_FEEDInterface('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None

from python_code import application_OAuthConfig

def test_application_OAuthConfig___init__():
    assert application_OAuthConfig.__init__(application_OAuthConfig('', application_OAuthConfig=set(), application_OAuthConfig29=set()), '', application_OAuthConfig=set(), application_OAuthConfig29=set()) == None

from python_code import application_OCLRestrictedProperty

def test_application_OCLRestrictedProperty___init__():
    assert application_OCLRestrictedProperty.__init__(application_OCLRestrictedProperty(''), '') == None

from python_code import application_Configuration
from python_code import application_Property

def test_application_Property___init__():
    assert application_Property.__init__(application_Property('', '', '', '', '', '', '\x00', '', application_Property=application_Configuration()), '', '', '', '', '', '', '', '', application_Property=application_Configuration()) == None

def test_application_Property_isValueRange():
    assert application_Property.isValueRange(application_Property('\x00\x00', '', '', '', '', '', '', '', application_Property=application_Configuration())) == None

def test_application_Property_getMaxValue():
    assert application_Property.getMaxValue(application_Property('\x00\x00', '', '', '', '', '', '', '', application_Property=application_Configuration())) == None

def test_application_Property_getMinValue():
    assert application_Property.getMinValue(application_Property('\x00\x00', '', '', '', '', '', '', '', application_Property=application_Configuration())) == None

def test_application_Property_isValueList():
    assert application_Property.isValueList(application_Property('\x00\x00', '', '', '', '', '', '', '', application_Property=application_Configuration())) == None

def test_application_Property_getListOfValues():
    assert application_Property.getListOfValues(application_Property('\x00\x00', '', '', '', '', '', '', '', application_Property=application_Configuration())) == None

from python_code import application_RESTInterface

def test_application_RESTInterface___init__():
    assert application_RESTInterface.__init__(application_RESTInterface(''), '') == None
