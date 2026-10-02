from enum import Enum
from python_code import ComplexHTMLTypeKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ComplexHTMLTypeKinds.Checkbox, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ComplexHTMLTypeKinds.Select, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ComplexHTMLTypeKinds.Select, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ComplexHTMLTypeKinds.Select, 0)

def test_Enum___new___2():
    assert Enum.__new__(ComplexHTMLTypeKinds.Select, 'Select') == ComplexHTMLTypeKinds.Select

from enum import Enum
from python_code import CoreComponent
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CoreComponent.User, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CoreComponent.User, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CoreComponent.User, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CoreComponent.Menu, 0)

def test_Enum___new___2():
    assert Enum.__new__(CoreComponent.Menu, 'User') == CoreComponent.User

from enum import Enum
from python_code import DataAccessKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataAccessKinds.database, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataAccessKinds.database, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataAccessKinds.database, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataAccessKinds.database, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataAccessKinds.database, 'database') == DataAccessKinds.database

from enum import Enum
from python_code import PageActionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PageActionKind.CANCEL, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PageActionKind.NEW, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PageActionKind.CLOSE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PageActionKind.NEW, 0)

def test_Enum___new___2():
    assert Enum.__new__(PageActionKind.NEW, 'NEW') == PageActionKind.NEW

from enum import Enum
from python_code import PageActionPositionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PageActionPositionKind.top, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PageActionPositionKind.top, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PageActionPositionKind.top, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PageActionPositionKind.top, 0)

def test_Enum___new___2():
    assert Enum.__new__(PageActionPositionKind.top, 'top') == PageActionPositionKind.top

from enum import Enum
from python_code import PageKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PageKinds.list, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PageKinds.list, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PageKinds.list, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PageKinds.list, 0)

def test_Enum___new___2():
    assert Enum.__new__(PageKinds.list, 'list') == PageKinds.list

from enum import Enum
from python_code import PluginKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PluginKinds.finder, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PluginKinds.search, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PluginKinds.system, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PluginKinds.finder, 0)

def test_Enum___new___2():
    assert Enum.__new__(PluginKinds.user, 'finder') == PluginKinds.finder

from enum import Enum
from python_code import SimpleHTMLTypeKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SimpleHTMLTypeKinds.Link, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SimpleHTMLTypeKinds.Link, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SimpleHTMLTypeKinds.Link, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SimpleHTMLTypeKinds.Editor, 0)

def test_Enum___new___2():
    assert Enum.__new__(SimpleHTMLTypeKinds.Link, 'Link') == SimpleHTMLTypeKinds.Link

from enum import Enum
from python_code import StandardTypeKinds
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(StandardTypeKinds.Text, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(StandardTypeKinds.Time, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(StandardTypeKinds.File, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(StandardTypeKinds.Text, 0)

def test_Enum___new___2():
    assert Enum.__new__(StandardTypeKinds.Text, 'Text') == StandardTypeKinds.Text

from python_code import eJSL_ComplexHTMLTypes

def test_eJSL_ComplexHTMLTypes___init__():
    assert eJSL_ComplexHTMLTypes.__init__(eJSL_ComplexHTMLTypes(''), '') == None

from python_code import eJSL_CustomPage

def test_eJSL_CustomPage___init__():
    assert eJSL_CustomPage.__init__(eJSL_CustomPage('', '', eJSL_CustomPage=set()), '', '', eJSL_CustomPage=set()) == None

from python_code import eJSL_EJSLModel
from python_code import eJSL_EJSLPart

def test_eJSL_EJSLModel___init__():
    assert eJSL_EJSLModel.__init__(eJSL_EJSLModel('', eJSL_EJSLModel=eJSL_EJSLPart()), '', eJSL_EJSLModel=eJSL_EJSLPart()) == None

from python_code import eJSL_ExternalLink

def test_eJSL_ExternalLink___init__():
    assert eJSL_ExternalLink.__init__(eJSL_ExternalLink('', '\x00'), '\x00\x00', '') == None

from python_code import eJSL_Position
from python_code import eJSL_Template

def test_eJSL_Position___init__():
    assert eJSL_Position.__init__(eJSL_Position('', eJSL_Position=eJSL_Template(), eJSL_Position182=set()), '', eJSL_Position=eJSL_Template(), eJSL_Position182=set()) == None

from python_code import eJSL_SimpleHTMLTypes

def test_eJSL_SimpleHTMLTypes___init__():
    assert eJSL_SimpleHTMLTypes.__init__(eJSL_SimpleHTMLTypes(''), '') == None

from python_code import eJSL_StandardTypes

def test_eJSL_StandardTypes___init__():
    assert eJSL_StandardTypes.__init__(eJSL_StandardTypes('\x00\x00', False, '', True), '', False, '', False) == None

from python_code import eJSL_StaticPage

def test_eJSL_StaticPage___init__():
    assert eJSL_StaticPage.__init__(eJSL_StaticPage(False, '\x00'), False, '\x00') == None
