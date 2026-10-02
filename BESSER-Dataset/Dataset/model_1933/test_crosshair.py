from enum import Enum
from python_code import Comparator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Comparator.EQ, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Comparator.LEQ, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Comparator.GEQ, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Comparator.GT, 0)

def test_Enum___new___2():
    assert Enum.__new__(Comparator.LT, 'EQ') == Comparator.EQ

from enum import Enum
from python_code import Order
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Order.DESC, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Order.DESC, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Order.ASC, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Order.ASC, 0)

def test_Enum___new___2():
    assert Enum.__new__(Order.ASC, 'ASC') == Order.ASC

from enum import Enum
from python_code import Orientation
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Orientation.Left, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Orientation.Top, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Orientation.Left, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Orientation.Top, 0)

def test_Enum___new___2():
    assert Enum.__new__(Orientation.Top, 'Top') == Orientation.Top

from enum import Enum
from python_code import PlatformLayers
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PlatformLayers.UILayer, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PlatformLayers.UILayer, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PlatformLayers.UILayer, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PlatformLayers.UILayer, 0)

def test_Enum___new___2():
    assert Enum.__new__(PlatformLayers.UILayer, 'UILayer') == PlatformLayers.UILayer

from enum import Enum
from python_code import RelationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RelationType.One2One, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RelationType.One2One, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RelationType.One2One, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RelationType.One2One, 0)

def test_Enum___new___2():
    assert Enum.__new__(RelationType.One2One, 'One2One') == RelationType.One2One

from python_code import domain_Button

def test_domain_Button___init__():
    assert domain_Button.__init__(domain_Button(''), '') == None

from python_code import domain_DefaultCavas

def test_domain_DefaultCavas___init__():
    assert domain_DefaultCavas.__init__(domain_DefaultCavas(True), False) == None

from python_code import domain_Context
from python_code import domain_DropDownSelection
from python_code import domain_Selection

def test_domain_DropDownSelection___init__():
    assert domain_DropDownSelection.__init__(domain_DropDownSelection('', domain_DropDownSelection=domain_Selection(), domain_DropDownSelection458=domain_Context()), '', domain_DropDownSelection=domain_Selection(), domain_DropDownSelection458=domain_Context()) == None

from python_code import domain_EnumAttribute
from python_code import domain_Enumarator

def test_domain_EnumAttribute___init__():
    assert domain_EnumAttribute.__init__(domain_EnumAttribute('', '', '\x00\x00', EnumAttribute=domain_Enumarator(), values=domain_Enumarator()), '', '', '', EnumAttribute=domain_Enumarator(), values=domain_Enumarator()) == None

from python_code import domain_Formatable

def test_domain_Formatable___init__():
    assert domain_Formatable.__init__(domain_Formatable(''), '') == None

from python_code import domain_HTMLLayerHolder

def test_domain_HTMLLayerHolder___init__():
    assert domain_HTMLLayerHolder.__init__(domain_HTMLLayerHolder(0), 0) == None

from python_code import domain_JavaComponent

def test_domain_JavaComponent___init__():
    assert domain_JavaComponent.__init__(domain_JavaComponent('\x00\x00', '', '', ''), '', '', '', '') == None

from python_code import domain_JavaMapper

def test_domain_JavaMapper___init__():
    assert domain_JavaMapper.__init__(domain_JavaMapper('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None

from python_code import domain_JavaScriptMapper

def test_domain_JavaScriptMapper___init__():
    assert domain_JavaScriptMapper.__init__(domain_JavaScriptMapper(''), '') == None

from python_code import domain_Menu

def test_domain_Menu___init__():
    assert domain_Menu.__init__(domain_Menu(''), '') == None

from python_code import domain_Orderable

def test_domain_Orderable___init__():
    assert domain_Orderable.__init__(domain_Orderable(0), 0) == None

from python_code import domain_PopupCanvas

def test_domain_PopupCanvas___init__():
    assert domain_PopupCanvas.__init__(domain_PopupCanvas(True), False) == None

from python_code import domain_EObject
from python_code import domain_RoleMapper

def test_domain_RoleMapper___init__():
    assert domain_RoleMapper.__init__(domain_RoleMapper('', '', '\x00\x00', domain_RoleMapper=domain_EObject()), '', '', '', domain_RoleMapper=domain_EObject()) == None

from python_code import domain_Table

def test_domain_Table___init__():
    assert domain_Table.__init__(domain_Table('', 0, domain_Table=set()), '', 0, domain_Table=set()) == None

from python_code import domain_Context
from python_code import domain_Tree

def test_domain_Tree___init__():
    assert domain_Tree.__init__(domain_Tree('', domain_Tree=domain_Context(), domain_Tree467=set()), '', domain_Tree=domain_Context(), domain_Tree467=set()) == None
