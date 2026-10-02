from enum import Enum
from python_code import DataEntityCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataEntityCategory.Message, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataEntityCategory.Message, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataEntityCategory.Message, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataEntityCategory.Message, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataEntityCategory.Message, 'Message') == DataEntityCategory.Message

from enum import Enum
from python_code import LifeCycleStatus
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LifeCycleStatus.Live, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LifeCycleStatus.Live, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LifeCycleStatus.Live, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LifeCycleStatus.Live, 0)

def test_Enum___new___2():
    assert Enum.__new__(LifeCycleStatus.Live, 'Live') == LifeCycleStatus.Live

from enum import Enum
from python_code import PrincipleCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PrincipleCategory.DataPrinciple, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PrincipleCategory.DataPrinciple, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PrincipleCategory.DataPrinciple, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PrincipleCategory.DataPrinciple, 0)

def test_Enum___new___2():
    assert Enum.__new__(PrincipleCategory.DataPrinciple, 'DataPrinciple') == PrincipleCategory.DataPrinciple

from enum import Enum
from python_code import StandardsClass
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(StandardsClass.Retired, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(StandardsClass.Retired, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(StandardsClass.Retired, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(StandardsClass.Retired, 0)

def test_Enum___new___2():
    assert Enum.__new__(StandardsClass.Retired, 'Retired') == StandardsClass.Retired

from enum import Enum
from python_code import WorkPackageCategory
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(WorkPackageCategory.Program, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(WorkPackageCategory.Project, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(WorkPackageCategory.Program, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(WorkPackageCategory.Project, 0)

def test_Enum___new___2():
    assert Enum.__new__(WorkPackageCategory.Project, 'Project') == WorkPackageCategory.Project

from python_code import contentfwk_BusinessArchitecture
from python_code import contentfwk_Contract
from python_code import contentfwk_Service
from python_code import contentfwk_ServiceQuality

def test_contentfwk_Contract___init__():
    assert contentfwk_Contract.__init__(contentfwk_Contract('', '\x00', '', '\x01', '', '', '', '', '', '', '', '', '', '\x00', '\x00', '\x00', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract361=contentfwk_Service()), '', '', '', '', '\x00', '', '', '', '\x01', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', contentfwk_Contract=contentfwk_BusinessArchitecture(), Contract=contentfwk_ServiceQuality(), isGovernedAndMeasuredByContracts=set(), appliesToContracts=set(), Contract361=contentfwk_Service()) == None

from python_code import contentfwk_EnterpriseArchitecture

def test_contentfwk_EnterpriseArchitecture___init__():
    assert contentfwk_EnterpriseArchitecture.__init__(contentfwk_EnterpriseArchitecture('\x00', contentfwk_EnterpriseArchitecture=set()), '', contentfwk_EnterpriseArchitecture=set()) == None

def test_contentfwk_EnterpriseArchitecture_forceID():
    assert contentfwk_EnterpriseArchitecture.forceID(contentfwk_EnterpriseArchitecture('', contentfwk_EnterpriseArchitecture=set()), '') == None

from python_code import contentfwk_Principle

def test_contentfwk_Principle___init__():
    assert contentfwk_Principle.__init__(contentfwk_Principle('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import contentfwk_Requirement

def test_contentfwk_Requirement___init__():
    assert contentfwk_Requirement.__init__(contentfwk_Requirement('', '', '\x00\x00'), '', '', '') == None

from python_code import contentfwk_Standard

def test_contentfwk_Standard___init__():
    assert contentfwk_Standard.__init__(contentfwk_Standard('', datetime.date(1, 1, 1), datetime.date(1, 1, 1), datetime.date(1, 1, 2), datetime.date(1, 1, 1)), '\x00\x00', datetime.date(1, 1, 1), datetime.date(1, 1, 1), datetime.date(1, 1, 1), datetime.date(1, 1, 1)) == None
