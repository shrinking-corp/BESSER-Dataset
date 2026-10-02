from enum import Enum
from python_code import AccessCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessCategory.data, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessCategory.bus, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessCategory.data, 0, '', 0) == 0

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
        Enum._generate_next_value_(AccessType.required, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessType.required, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessType.provided, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessType.required, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessType.required, 'required') == AccessType.required

from enum import Enum
from python_code import ComponentCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ComponentCategory.bus, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ComponentCategory.bus, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ComponentCategory.bus, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ComponentCategory.data, 0)

def test_Enum___new___2():
    assert Enum.__new__(ComponentCategory.bus, 'bus') == ComponentCategory.bus

from enum import Enum
from python_code import ConnectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConnectionKind.Port, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConnectionKind.Port, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConnectionKind.Port, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConnectionKind.Port, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConnectionKind.Port, 'Port') == ConnectionKind.Port

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
        Enum._generate_next_value_(FlowKind.path, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FlowKind.path, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FlowKind.path, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FlowKind.path, 0)

def test_Enum___new___2():
    assert Enum.__new__(FlowKind.path, 'path') == FlowKind.path

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
        Enum._generate_next_value_(PortCategory.event, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PortCategory.event, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PortCategory.event, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PortCategory.data, 0)

def test_Enum___new___2():
    assert Enum.__new__(PortCategory.data, 'data') == PortCategory.data

from python_code import aadl2_Access

def test_aadl2_Access___init__():
    assert aadl2_Access.__init__(aadl2_Access('', '\x00'), '\x00\x00', '') == None

from python_code import aadl2_ArrayRange
from python_code import aadl2_ContainmentPathElement

def test_aadl2_ArrayRange___init__():
    assert aadl2_ArrayRange.__init__(aadl2_ArrayRange('', '\x00', aadl2_ArrayRange=aadl2_ContainmentPathElement()), '\x00\x00', '', aadl2_ArrayRange=aadl2_ContainmentPathElement()) == None

from python_code import aadl2_ArraySpecification
from python_code import aadl2_ArrayableElement

def test_aadl2_ArraySpecification___init__():
    assert aadl2_ArraySpecification.__init__(aadl2_ArraySpecification('', aadl2_ArraySpecification80=aadl2_ArrayableElement(), aadl2_ArraySpecification=set()), '', aadl2_ArraySpecification80=aadl2_ArrayableElement(), aadl2_ArraySpecification=set()) == None

from python_code import aadl2_BasicProperty
from python_code import aadl2_BasicPropertyAssociation
from python_code import aadl2_PropertyType
from python_code import aadl2_RecordType

def test_aadl2_BasicProperty___init__():
    assert aadl2_BasicProperty.__init__(aadl2_BasicProperty('', aadl2_BasicProperty=aadl2_PropertyType(), aadl2_BasicProperty825=aadl2_BasicPropertyAssociation(), aadl2_BasicProperty886=aadl2_RecordType()), '', aadl2_BasicProperty=aadl2_PropertyType(), aadl2_BasicProperty825=aadl2_BasicPropertyAssociation(), aadl2_BasicProperty886=aadl2_RecordType()) == None

from python_code import aadl2_BehavioredImplementation

def test_aadl2_BehavioredImplementation___init__():
    assert aadl2_BehavioredImplementation.__init__(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation452=set()), aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation452=set()) == None

def test_aadl2_BehavioredImplementation_callSpecifications():
    assert aadl2_BehavioredImplementation.callSpecifications(aadl2_BehavioredImplementation(aadl2_BehavioredImplementation=set(), aadl2_BehavioredImplementation452=set())) == None

from python_code import aadl2_BooleanLiteral

def test_aadl2_BooleanLiteral___init__():
    assert aadl2_BooleanLiteral.__init__(aadl2_BooleanLiteral(''), '') == None

from python_code import aadl2_ComponentPrototypeActual
from python_code import aadl2_ComponentPrototypeBinding

def test_aadl2_ComponentPrototypeActual___init__():
    assert aadl2_ComponentPrototypeActual.__init__(aadl2_ComponentPrototypeActual('', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding()), '', aadl2_ComponentPrototypeActual=aadl2_ComponentPrototypeBinding()) == None

from python_code import aadl2_ComputedValue

def test_aadl2_ComputedValue___init__():
    assert aadl2_ComputedValue.__init__(aadl2_ComputedValue(''), '') == None

from python_code import aadl2_DefaultAnnexLibrary

def test_aadl2_DefaultAnnexLibrary___init__():
    assert aadl2_DefaultAnnexLibrary.__init__(aadl2_DefaultAnnexLibrary(''), '') == None

from python_code import aadl2_DefaultAnnexSubclause

def test_aadl2_DefaultAnnexSubclause___init__():
    assert aadl2_DefaultAnnexSubclause.__init__(aadl2_DefaultAnnexSubclause(''), '') == None

from python_code import aadl2_DirectedFeature

def test_aadl2_DirectedFeature___init__():
    assert aadl2_DirectedFeature.__init__(aadl2_DirectedFeature(''), '') == None

from python_code import aadl2_IntegerLiteral

def test_aadl2_IntegerLiteral___init__():
    assert aadl2_IntegerLiteral.__init__(aadl2_IntegerLiteral('', '\x00'), '\x00\x00', '') == None

from python_code import aadl2_NumberValue
from python_code import aadl2_UnitLiteral

def test_aadl2_NumberValue___init__():
    assert aadl2_NumberValue.__init__(aadl2_NumberValue('', aadl2_NumberValue=aadl2_UnitLiteral(), aadl2_NumberValue837=aadl2_UnitLiteral()), '', aadl2_NumberValue=aadl2_UnitLiteral(), aadl2_NumberValue837=aadl2_UnitLiteral()) == None

from python_code import aadl2_Numeral

def test_aadl2_Numeral___init__():
    assert aadl2_Numeral.__init__(aadl2_Numeral(''), '') == None

from python_code import aadl2_Operation

def test_aadl2_Operation___init__():
    assert aadl2_Operation.__init__(aadl2_Operation('', aadl2_Operation=set()), '', aadl2_Operation=set()) == None
