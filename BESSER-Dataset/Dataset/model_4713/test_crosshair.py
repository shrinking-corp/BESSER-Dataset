from enum import Enum
from python_code import Connective
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Connective.Or, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Connective.Eqv, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Connective.Or, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Connective.If, 0)

def test_Enum___new___2():
    assert Enum.__new__(Connective.Or, 'Or') == Connective.Or

from enum import Enum
from python_code import ElementKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ElementKind.Query, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ElementKind.Query, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ElementKind.Query, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ElementKind.Group, 0)

def test_Enum___new___2():
    assert Enum.__new__(ElementKind.Query, 'Noun') == ElementKind.Noun

from enum import Enum
from python_code import FormElementKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FormElementKind.ObjectRole, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FormElementKind.ObjectRole, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FormElementKind.ObjectRole, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FormElementKind.ObjectRole, 0)

def test_Enum___new___2():
    assert Enum.__new__(FormElementKind.ObjectRole, 'ObjectRole') == FormElementKind.ObjectRole

from enum import Enum
from python_code import GroupKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GroupKind.All, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GroupKind.All, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GroupKind.All, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GroupKind.All, 0)

def test_Enum___new___2():
    assert Enum.__new__(GroupKind.All, 'All') == GroupKind.All

from enum import Enum
from python_code import InstanceKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InstanceKind.Name, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InstanceKind.Name, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InstanceKind.Name, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InstanceKind.Name, 0)

def test_Enum___new___2():
    assert Enum.__new__(InstanceKind.Name, 'Name') == InstanceKind.Name

from enum import Enum
from python_code import KeywordKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(KeywordKind.K_The, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(KeywordKind.K_An, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(KeywordKind.K_The, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(KeywordKind.K_The, 0)

def test_Enum___new___2():
    assert Enum.__new__(KeywordKind.K_An, 'K_An') == KeywordKind.K_An

from enum import Enum
from python_code import Modality
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Modality.None_, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Modality.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Modality.None_, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Modality.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(Modality.None_, 'None_') == Modality.None_

from python_code import NBVR_Grammar_Dimension
from python_code import VocUnit

def test_NBVR_Grammar_Dimension___init__():
    assert NBVR_Grammar_Dimension.__init__(NBVR_Grammar_Dimension(0, NBVR_Grammar_Dimension=VocUnit()), 0, NBVR_Grammar_Dimension=VocUnit()) == None
