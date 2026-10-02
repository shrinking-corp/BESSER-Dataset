from enum import Enum
from python_code import CapabilityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CapabilityType.Performance, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CapabilityType.Functional, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CapabilityType.Operational, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CapabilityType.Functional, 0)

def test_Enum___new___2():
    assert Enum.__new__(CapabilityType.Functional, 'Functional') == CapabilityType.Functional

from enum import Enum
from python_code import EnterpriseObjectiveType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EnterpriseObjectiveType.Tactic, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EnterpriseObjectiveType.None_, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EnterpriseObjectiveType.Tactic, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EnterpriseObjectiveType.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(EnterpriseObjectiveType.None_, 'None_') == EnterpriseObjectiveType.None_

from enum import Enum
from python_code import ObjectiveNature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ObjectiveNature.Delay, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ObjectiveNature.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ObjectiveNature.Cost, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ObjectiveNature.Delay, 0)

def test_Enum___new___2():
    assert Enum.__new__(ObjectiveNature.Cost, 'Cost') == ObjectiveNature.Cost

from enum import Enum
from python_code import Origin
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Origin.None_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Origin.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Origin.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Origin.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(Origin.None_, 'None_') == Origin.None_

from enum import Enum
from python_code import ProductNature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ProductNature.None_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ProductNature.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ProductNature.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ProductNature.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(ProductNature.None_, 'None_') == ProductNature.None_

from enum import Enum
from python_code import ProductState
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ProductState.None_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ProductState.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ProductState.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ProductState.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(ProductState.None_, 'None_') == ProductState.None_

from enum import Enum
from python_code import RequirementNature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RequirementNature.None_, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RequirementNature.None_, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RequirementNature.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RequirementNature.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(RequirementNature.None_, 'None_') == RequirementNature.None_

from enum import Enum
from python_code import RequirementOrigin
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RequirementOrigin.None_, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RequirementOrigin.None_, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RequirementOrigin.None_, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RequirementOrigin.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(RequirementOrigin.None_, 'None_') == RequirementOrigin.None_

from enum import Enum
from python_code import RoleType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RoleType.Decision, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RoleType.Controle, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RoleType.Controle, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RoleType.Controle, 0)

def test_Enum___new___2():
    assert Enum.__new__(RoleType.Decision, 'Decision') == RoleType.Decision

from enum import Enum
from python_code import ServiceState
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ServiceState.For_internal_usage, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ServiceState.For_internal_usage, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ServiceState.For_internal_usage, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ServiceState.For_internal_usage, 0)

def test_Enum___new___2():
    assert Enum.__new__(ServiceState.For_internal_usage, 'For_internal_usage') == ServiceState.For_internal_usage

from enum import Enum
from python_code import StakeholderType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(StakeholderType.EEnumLiteral0, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(StakeholderType.EEnumLiteral0, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(StakeholderType.EEnumLiteral0, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(StakeholderType.EEnumLiteral0, 0)

def test_Enum___new___2():
    assert Enum.__new__(StakeholderType.EEnumLiteral0, 'EEnumLiteral0') == StakeholderType.EEnumLiteral0

from python_code import sipme_Application

def test_sipme_Application___init__():
    assert sipme_Application.__init__(sipme_Application('', '\x00'), '\x00\x00', '') == None

from python_code import sipme_Device_Machine

def test_sipme_Device_Machine___init__():
    assert sipme_Device_Machine.__init__(sipme_Device_Machine('', '\x00'), '\x00\x00', '') == None

from python_code import sipme_SIPME_object

def test_sipme_SIPME_object___init__():
    assert sipme_SIPME_object.__init__(sipme_SIPME_object('', '', '\x00\x00'), '', '', '') == None
