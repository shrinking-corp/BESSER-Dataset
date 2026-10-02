from enum import Enum
from python_code import Align
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Align.center, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Align.left, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Align.left, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Align.left, 0)

def test_Enum___new___2():
    assert Enum.__new__(Align.left, 'left') == Align.left

from enum import Enum
from python_code import ButtonType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ButtonType.Push, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ButtonType.Push, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ButtonType.Push, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ButtonType.Push, 0)

def test_Enum___new___2():
    assert Enum.__new__(ButtonType.Push, 'Push') == ButtonType.Push

from enum import Enum
from python_code import DateFormat
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DateFormat.Full, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DateFormat.Full, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DateFormat.Full, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DateFormat.Full, 0)

def test_Enum___new___2():
    assert Enum.__new__(DateFormat.Full, 'Full') == DateFormat.Full

from enum import Enum
from python_code import EventType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EventType.onblur, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EventType.onclick, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EventType.onblur, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EventType.onload, 0)

def test_Enum___new___2():
    assert Enum.__new__(EventType.onload, 'onload') == EventType.onload

from enum import Enum
from python_code import Extension
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Extension.asp, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Extension.asp, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Extension.php, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Extension.jsp, 0)

def test_Enum___new___2():
    assert Enum.__new__(Extension.jsp, 'jsp') == Extension.jsp

from enum import Enum
from python_code import FieldSetLegendAlign
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FieldSetLegendAlign.top, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FieldSetLegendAlign.top, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FieldSetLegendAlign.top, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FieldSetLegendAlign.top, 0)

def test_Enum___new___2():
    assert Enum.__new__(FieldSetLegendAlign.top, 'top') == FieldSetLegendAlign.top

from enum import Enum
from python_code import HeadingLevel
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HeadingLevel.h1, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HeadingLevel.h6, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HeadingLevel.h4, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HeadingLevel.h6, 0)

def test_Enum___new___2():
    assert Enum.__new__(HeadingLevel.h3, 'h6') == HeadingLevel.h6

from enum import Enum
from python_code import Locale
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Locale.German, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Locale.German, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Locale.German, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Locale.German, 0)

def test_Enum___new___2():
    assert Enum.__new__(Locale.German, 'German') == Locale.German

from enum import Enum
from python_code import LogicalOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LogicalOperator.OR, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LogicalOperator.OR, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LogicalOperator.AND, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LogicalOperator.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(LogicalOperator.OR, 'OR') == LogicalOperator.OR

from enum import Enum
from python_code import MatchingOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MatchingOperator.Equals, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MatchingOperator.Equals, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MatchingOperator.Equals, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MatchingOperator.Equals, 0)

def test_Enum___new___2():
    assert Enum.__new__(MatchingOperator.Equals, 'Equals') == MatchingOperator.Equals

from enum import Enum
from python_code import MessageDialogEvent
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MessageDialogEvent.closeDialog, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MessageDialogEvent.closeDialog, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MessageDialogEvent.closeDialog, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MessageDialogEvent.closeDialog, 0)

def test_Enum___new___2():
    assert Enum.__new__(MessageDialogEvent.closeDialog, 'closeDialog') == MessageDialogEvent.closeDialog

from enum import Enum
from python_code import ObjectAlign
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ObjectAlign.top, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ObjectAlign.top, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ObjectAlign.top, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ObjectAlign.top, 0)

def test_Enum___new___2():
    assert Enum.__new__(ObjectAlign.top, 'top') == ObjectAlign.top

from enum import Enum
from python_code import OrderedListType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OrderedListType.none, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OrderedListType.none, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OrderedListType.none, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OrderedListType.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(OrderedListType.none, 'none') == OrderedListType.none

from enum import Enum
from python_code import Orientation
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Orientation.Vertical, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Orientation.Vertical, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Orientation.Vertical, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Orientation.Vertical, 0)

def test_Enum___new___2():
    assert Enum.__new__(Orientation.Vertical, 'Vertical') == Orientation.Vertical

from enum import Enum
from python_code import PhraseElementType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PhraseElementType.None_, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PhraseElementType.Emphasis, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PhraseElementType.None_, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PhraseElementType.None_, '')

def test_Enum___new___2():
    assert Enum.__new__(PhraseElementType.None_, 'None_') == PhraseElementType.None_

from enum import Enum
from python_code import ScriptType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ScriptType.textVBScript, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ScriptType.textVBScript, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ScriptType.textTcl, 0, '\x00', '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ScriptType.textTcl, 0)

def test_Enum___new___2():
    assert Enum.__new__(ScriptType.textTcl, 'textTcl') == ScriptType.textTcl

from enum import Enum
from python_code import SubmitFormMethod
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SubmitFormMethod.get, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SubmitFormMethod.get, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SubmitFormMethod.post, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SubmitFormMethod.get, 0)

def test_Enum___new___2():
    assert Enum.__new__(SubmitFormMethod.get, 'get') == SubmitFormMethod.get

from enum import Enum
from python_code import UnorderedListType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(UnorderedListType.square, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(UnorderedListType.none, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(UnorderedListType.none, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(UnorderedListType.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(UnorderedListType.none, 'disc') == UnorderedListType.disc

from python_code import ric_Button

def test_ric_Button___init__():
    assert ric_Button.__init__(ric_Button('', False, '\x00\x00'), '', False, '') == None

from python_code import ric_ClassifiableComponent

def test_ric_ClassifiableComponent___init__():
    assert ric_ClassifiableComponent.__init__(ric_ClassifiableComponent(''), '') == None

from python_code import ric_Datepicker

def test_ric_Datepicker___init__():
    assert ric_Datepicker.__init__(ric_Datepicker(False, '', '', 0, False, False, False, False), False, '', '', 0, False, False, False, False) == None

from python_code import ric_Heading

def test_ric_Heading___init__():
    assert ric_Heading.__init__(ric_Heading(''), '') == None

from python_code import ric_IdentifiableComponent

def test_ric_IdentifiableComponent___init__():
    assert ric_IdentifiableComponent.__init__(ric_IdentifiableComponent(''), '') == None

from python_code import ric_Image
from python_code import ric_Logo

def test_ric_Image___init__():
    assert ric_Image.__init__(ric_Image('', '\x00', ric_Image=ric_Logo()), '\x00\x00', '', ric_Image=ric_Logo()) == None

from python_code import ric_InputFile

def test_ric_InputFile___init__():
    assert ric_InputFile.__init__(ric_InputFile(0, 0, False), 0, 0, False) == None

from python_code import ric_MessageDialog

def test_ric_MessageDialog___init__():
    assert ric_MessageDialog.__init__(ric_MessageDialog(0, 0, 0, '', '', False, False, False, 0, 0, 0, ric_MessageDialog=set()), 0, 0, 0, '', '', False, True, False, 0, 0, 0, ric_MessageDialog=set()) == None

from python_code import ric_OrderedList

def test_ric_OrderedList___init__():
    assert ric_OrderedList.__init__(ric_OrderedList('', ric_OrderedList=set()), '', ric_OrderedList=set()) == None

from python_code import ric_Paragraph

def test_ric_Paragraph___init__():
    assert ric_Paragraph.__init__(ric_Paragraph(''), '') == None
