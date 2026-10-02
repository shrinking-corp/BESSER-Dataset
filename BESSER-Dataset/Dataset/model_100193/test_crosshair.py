from enum import Enum
from python_code import BinaryStringTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BinaryStringTypes.BINARYVARYING, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BinaryStringTypes.BINARYVARYING, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BinaryStringTypes.BINARY, 0, '\x00', '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BinaryStringTypes.BINARY, 0)

def test_Enum___new___2():
    assert Enum.__new__(BinaryStringTypes.BINARY, 'BINARY') == BinaryStringTypes.BINARY

from enum import Enum
from python_code import BooleanTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BooleanTypes.BOOLEAN, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BooleanTypes.BOOLEAN, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BooleanTypes.BOOLEAN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BooleanTypes.BOOLEAN, 0)

def test_Enum___new___2():
    assert Enum.__new__(BooleanTypes.BOOLEAN, 'BOOLEAN') == BooleanTypes.BOOLEAN

from enum import Enum
from python_code import CharacterStringTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CharacterStringTypes.CHARACTER, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CharacterStringTypes.CHARACTER, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CharacterStringTypes.CHARACTER, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CharacterStringTypes.CHARACTER, 0)

def test_Enum___new___2():
    assert Enum.__new__(CharacterStringTypes.CHARACTER, 'CHARACTER') == CharacterStringTypes.CHARACTER

from enum import Enum
from python_code import DatetimeFeatures
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DatetimeFeatures.precision, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DatetimeFeatures.precision, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DatetimeFeatures.precision, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DatetimeFeatures.precision, 0)

def test_Enum___new___2():
    assert Enum.__new__(DatetimeFeatures.precision, 'precision') == DatetimeFeatures.precision

from enum import Enum
from python_code import DatetimeTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DatetimeTypes.DATE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DatetimeTypes.DATE, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DatetimeTypes.DATE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DatetimeTypes.DATE, 0)

def test_Enum___new___2():
    assert Enum.__new__(DatetimeTypes.DATE, 'DATE') == DatetimeTypes.DATE

from enum import Enum
from python_code import IntervalFeatures
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IntervalFeatures.second_precision, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IntervalFeatures.second_precision, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IntervalFeatures.second_precision, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IntervalFeatures.second_precision, 0)

def test_Enum___new___2():
    assert Enum.__new__(IntervalFeatures.second_precision, 'second_precision') == IntervalFeatures.second_precision

from enum import Enum
from python_code import IntervalTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IntervalTypes.HOUR, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IntervalTypes.YEAR, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IntervalTypes.HOUR, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IntervalTypes.YEAR, 0)

def test_Enum___new___2():
    assert Enum.__new__(IntervalTypes.SECOND, 'DAY') == IntervalTypes.DAY

from enum import Enum
from python_code import MatchTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MatchTypes.TOTAL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MatchTypes.TOTAL, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MatchTypes.SIMPLE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MatchTypes.TOTAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(MatchTypes.TOTAL, 'TOTAL') == MatchTypes.TOTAL

from enum import Enum
from python_code import Multiplier
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Multiplier.G, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Multiplier.T, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Multiplier.T, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Multiplier.K, 0)

def test_Enum___new___2():
    assert Enum.__new__(Multiplier.P, 'K') == Multiplier.K

from enum import Enum
from python_code import NumericFeatures
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(NumericFeatures.scale, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(NumericFeatures.scale, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(NumericFeatures.scale, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(NumericFeatures.radix, 0)

def test_Enum___new___2():
    assert Enum.__new__(NumericFeatures.radix, 'scale') == NumericFeatures.scale

from enum import Enum
from python_code import NumericRadix
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(NumericRadix.BINARY, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(NumericRadix.BINARY, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(NumericRadix.DECIMAL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(NumericRadix.BINARY, 0)

def test_Enum___new___2():
    assert Enum.__new__(NumericRadix.BINARY, 'BINARY') == NumericRadix.BINARY

from enum import Enum
from python_code import NumericTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(NumericTypes.FLOAT, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(NumericTypes.REAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(NumericTypes.REAL, 0, 0, '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(NumericTypes.FLOAT, '')

def test_Enum___new___2():
    assert Enum.__new__(NumericTypes.REAL, 'REAL') == NumericTypes.REAL

from enum import Enum
from python_code import ParameterMode
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ParameterMode.IN, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ParameterMode.IN, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ParameterMode.IN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ParameterMode.IN, 0)

def test_Enum___new___2():
    assert Enum.__new__(ParameterMode.IN, 'IN') == ParameterMode.IN

from enum import Enum
from python_code import ReferentialAction
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ReferentialAction.CASCADE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ReferentialAction.SET_NULL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ReferentialAction.SET_NULL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ReferentialAction.CASCADE, 0)

def test_Enum___new___2():
    assert Enum.__new__(ReferentialAction.CASCADE, 'CASCADE') == ReferentialAction.CASCADE

from python_code import SQL2003_evo_ARRAY

def test_SQL2003_evo_ARRAY___init__():
    assert SQL2003_evo_ARRAY.__init__(SQL2003_evo_ARRAY(''), '') == None

from python_code import SQL2003_evo_BinaryStringType

def test_SQL2003_evo_BinaryStringType___init__():
    assert SQL2003_evo_BinaryStringType.__init__(SQL2003_evo_BinaryStringType('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_BooleanType

def test_SQL2003_evo_BooleanType___init__():
    assert SQL2003_evo_BooleanType.__init__(SQL2003_evo_BooleanType(''), '') == None

from python_code import SQL2003_evo_CharacterStringType

def test_SQL2003_evo_CharacterStringType___init__():
    assert SQL2003_evo_CharacterStringType.__init__(SQL2003_evo_CharacterStringType('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_ConstructedType

def test_SQL2003_evo_ConstructedType___init__():
    assert SQL2003_evo_ConstructedType.__init__(SQL2003_evo_ConstructedType(''), '') == None

from python_code import SQL2003_evo_DatetimeFeature

def test_SQL2003_evo_DatetimeFeature___init__():
    assert SQL2003_evo_DatetimeFeature.__init__(SQL2003_evo_DatetimeFeature('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_DatetimeType

def test_SQL2003_evo_DatetimeType___init__():
    assert SQL2003_evo_DatetimeType.__init__(SQL2003_evo_DatetimeType(''), '') == None

from python_code import SQL2003_evo_DerivedTable

def test_SQL2003_evo_DerivedTable___init__():
    assert SQL2003_evo_DerivedTable.__init__(SQL2003_evo_DerivedTable(''), '') == None

from python_code import SQL2003_evo_IntervalFeature

def test_SQL2003_evo_IntervalFeature___init__():
    assert SQL2003_evo_IntervalFeature.__init__(SQL2003_evo_IntervalFeature('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_IntervalType

def test_SQL2003_evo_IntervalType___init__():
    assert SQL2003_evo_IntervalType.__init__(SQL2003_evo_IntervalType(''), '') == None

from python_code import SQL2003_evo_NumericFeature

def test_SQL2003_evo_NumericFeature___init__():
    assert SQL2003_evo_NumericFeature.__init__(SQL2003_evo_NumericFeature('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_NumericType

def test_SQL2003_evo_NumericType___init__():
    assert SQL2003_evo_NumericType.__init__(SQL2003_evo_NumericType(''), '') == None

from python_code import SQL2003_evo_DataType
from python_code import SQL2003_evo_Parameter

def test_SQL2003_evo_Parameter___init__():
    assert SQL2003_evo_Parameter.__init__(SQL2003_evo_Parameter('', SQL2003_evo_Parameter=SQL2003_evo_DataType()), '', SQL2003_evo_Parameter=SQL2003_evo_DataType()) == None

from python_code import SQL2003_evo_ReferentialConstraint
from python_code import SQL2003_evo_UniqueConstraint

def test_SQL2003_evo_ReferentialConstraint___init__():
    assert SQL2003_evo_ReferentialConstraint.__init__(SQL2003_evo_ReferentialConstraint('', '', '\x00\x00', SQL2003_evo_ReferentialConstraint=SQL2003_evo_UniqueConstraint()), '', '', '', SQL2003_evo_ReferentialConstraint=SQL2003_evo_UniqueConstraint()) == None

from python_code import SQL2003_evo_StringFeature

def test_SQL2003_evo_StringFeature___init__():
    assert SQL2003_evo_StringFeature.__init__(SQL2003_evo_StringFeature('', '\x00'), '\x00\x00', '') == None

from python_code import SQL2003_evo_TableCheckConstraint

def test_SQL2003_evo_TableCheckConstraint___init__():
    assert SQL2003_evo_TableCheckConstraint.__init__(SQL2003_evo_TableCheckConstraint(''), '') == None

from python_code import SQL2003_evo_TableConstraint

def test_SQL2003_evo_TableConstraint___init__():
    assert SQL2003_evo_TableConstraint.__init__(SQL2003_evo_TableConstraint(''), '') == None

from python_code import SQL2003_evo_UserDefinedType

def test_SQL2003_evo_UserDefinedType___init__():
    assert SQL2003_evo_UserDefinedType.__init__(SQL2003_evo_UserDefinedType(''), '') == None

from python_code import SQL2003_evo_XMLType

def test_SQL2003_evo_XMLType___init__():
    assert SQL2003_evo_XMLType.__init__(SQL2003_evo_XMLType(''), '') == None

from enum import Enum
from python_code import StringFeatures
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(StringFeatures.length, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(StringFeatures.length, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(StringFeatures.length, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(StringFeatures.unit, 0)

def test_Enum___new___2():
    assert Enum.__new__(StringFeatures.unit, 'unit') == StringFeatures.unit

from enum import Enum
from python_code import TriggerActionTime
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TriggerActionTime.AFTER, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TriggerActionTime.AFTER, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TriggerActionTime.BEFORE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TriggerActionTime.AFTER, 0)

def test_Enum___new___2():
    assert Enum.__new__(TriggerActionTime.AFTER, 'AFTER') == TriggerActionTime.AFTER

from enum import Enum
from python_code import TriggerEvent
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TriggerEvent.UPDATE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TriggerEvent.INSERT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TriggerEvent.INSERT, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TriggerEvent.UPDATE, 0)

def test_Enum___new___2():
    assert Enum.__new__(TriggerEvent.UPDATE, 'UPDATE') == TriggerEvent.UPDATE

from enum import Enum
from python_code import TriggerLevel
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TriggerLevel.ROW_LEVEL, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TriggerLevel.ROW_LEVEL, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TriggerLevel.ROW_LEVEL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TriggerLevel.ROW_LEVEL, 0)

def test_Enum___new___2():
    assert Enum.__new__(TriggerLevel.ROW_LEVEL, 'ROW_LEVEL') == TriggerLevel.ROW_LEVEL

from enum import Enum
from python_code import Unit
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Unit.OCTETS, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Unit.OCTETS, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Unit.OCTETS, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Unit.OCTETS, 0)

def test_Enum___new___2():
    assert Enum.__new__(Unit.OCTETS, 'OCTETS') == Unit.OCTETS

from enum import Enum
from python_code import XMLTypes
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(XMLTypes.XMLTYPE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(XMLTypes.XMLTYPE, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(XMLTypes.XMLTYPE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(XMLTypes.XMLTYPE, 0)

def test_Enum___new___2():
    assert Enum.__new__(XMLTypes.XMLTYPE, 'XMLTYPE') == XMLTypes.XMLTYPE
