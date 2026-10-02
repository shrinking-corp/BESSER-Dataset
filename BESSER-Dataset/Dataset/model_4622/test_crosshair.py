from enum import Enum
from python_code import Alignment
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Alignment.END, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Alignment.END, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Alignment.END, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Alignment.END, 0)

def test_Enum___new___2():
    assert Enum.__new__(Alignment.END, 'END') == Alignment.END

from enum import Enum
from python_code import ColorConstants
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ColorConstants.black, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ColorConstants.white, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ColorConstants.red, 0, '', '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ColorConstants.blue, 0)

def test_Enum___new___2():
    assert Enum.__new__(ColorConstants.blue, 'red') == ColorConstants.red

from enum import Enum
from python_code import Direction
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Direction.NONE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Direction.NONE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Direction.NSEW, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Direction.WEST, 0)

def test_Enum___new___2():
    assert Enum.__new__(Direction.NONE, 'WEST') == Direction.WEST

from enum import Enum
from python_code import FontStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FontStyle.ITALIC, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FontStyle.NORMAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FontStyle.NORMAL, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FontStyle.BOLD, 0)

def test_Enum___new___2():
    assert Enum.__new__(FontStyle.BOLD, 'BOLD') == FontStyle.BOLD

from enum import Enum
from python_code import LineKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LineKind.LINE_DOT, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LineKind.LINE_DOT, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LineKind.LINE_DASH, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LineKind.LINE_DOT, 0)

def test_Enum___new___2():
    assert Enum.__new__(LineKind.LINE_DOT, 'LINE_DOT') == LineKind.LINE_DOT

from python_code import gmfgraph_AlignmentFacet

def test_gmfgraph_AlignmentFacet___init__():
    assert gmfgraph_AlignmentFacet.__init__(gmfgraph_AlignmentFacet(''), '') == None

from python_code import gmfgraph_BasicFont

def test_gmfgraph_BasicFont___init__():
    assert gmfgraph_BasicFont.__init__(gmfgraph_BasicFont('', 0, '\x00\x00'), '', 0, '') == None

from python_code import gmfgraph_BorderLayoutData

def test_gmfgraph_BorderLayoutData___init__():
    assert gmfgraph_BorderLayoutData.__init__(gmfgraph_BorderLayoutData('', False), '', False) == None

from python_code import gmfgraph_ConstantColor

def test_gmfgraph_ConstantColor___init__():
    assert gmfgraph_ConstantColor.__init__(gmfgraph_ConstantColor(''), '') == None

from python_code import gmfgraph_CustomClass

def test_gmfgraph_CustomClass___init__():
    assert gmfgraph_CustomClass.__init__(gmfgraph_CustomClass('', gmfgraph_CustomClass=set()), '', gmfgraph_CustomClass=set()) == None

from python_code import gmfgraph_FlowLayout

def test_gmfgraph_FlowLayout___init__():
    assert gmfgraph_FlowLayout.__init__(gmfgraph_FlowLayout(False, '', '', 0, 0, False, False), False, '\x00', '', 0, 0, False, False) == None

from python_code import gmfgraph_GeneralFacet

def test_gmfgraph_GeneralFacet___init__():
    assert gmfgraph_GeneralFacet.__init__(gmfgraph_GeneralFacet('', '\x00'), '\x00\x00', '') == None

from python_code import gmfgraph_GradientFacet

def test_gmfgraph_GradientFacet___init__():
    assert gmfgraph_GradientFacet.__init__(gmfgraph_GradientFacet(''), '') == None

from python_code import gmfgraph_Identity

def test_gmfgraph_Identity___init__():
    assert gmfgraph_Identity.__init__(gmfgraph_Identity(''), '') == None

from python_code import gmfgraph_Figure
from python_code import gmfgraph_Insets
from python_code import gmfgraph_MarginBorder

def test_gmfgraph_Insets___init__():
    assert gmfgraph_Insets.__init__(gmfgraph_Insets(0, 0, 0, 0, gmfgraph_Insets=gmfgraph_Figure(), gmfgraph_Insets77=gmfgraph_MarginBorder()), 0, 0, 0, 0, gmfgraph_Insets=gmfgraph_Figure(), gmfgraph_Insets77=gmfgraph_MarginBorder()) == None

from python_code import gmfgraph_Label

def test_gmfgraph_Label___init__():
    assert gmfgraph_Label.__init__(gmfgraph_Label(''), '') == None

from python_code import gmfgraph_LabelOffsetFacet

def test_gmfgraph_LabelOffsetFacet___init__():
    assert gmfgraph_LabelOffsetFacet.__init__(gmfgraph_LabelOffsetFacet(0, 0), 0, 0) == None

from python_code import gmfgraph_Color
from python_code import gmfgraph_LineBorder

def test_gmfgraph_LineBorder___init__():
    assert gmfgraph_LineBorder.__init__(gmfgraph_LineBorder(0, gmfgraph_LineBorder=gmfgraph_Color()), 0, gmfgraph_LineBorder=gmfgraph_Color()) == None

from python_code import gmfgraph_Figure
from python_code import gmfgraph_Point
from python_code import gmfgraph_Polyline
from python_code import gmfgraph_XYLayoutData

def test_gmfgraph_Point___init__():
    assert gmfgraph_Point.__init__(gmfgraph_Point(0, 0, gmfgraph_Point=gmfgraph_Figure(), gmfgraph_Point55=gmfgraph_Figure(), gmfgraph_Point64=gmfgraph_Polyline(), gmfgraph_Point97=gmfgraph_XYLayoutData()), 0, 0, gmfgraph_Point=gmfgraph_Figure(), gmfgraph_Point55=gmfgraph_Figure(), gmfgraph_Point64=gmfgraph_Polyline(), gmfgraph_Point97=gmfgraph_XYLayoutData()) == None

from python_code import gmfgraph_RGBColor

def test_gmfgraph_RGBColor___init__():
    assert gmfgraph_RGBColor.__init__(gmfgraph_RGBColor(0, 0, 0), 0, 0, 0) == None

from python_code import gmfgraph_RoundedRectangle

def test_gmfgraph_RoundedRectangle___init__():
    assert gmfgraph_RoundedRectangle.__init__(gmfgraph_RoundedRectangle(0, 0), 0, 0) == None

from python_code import gmfgraph_Shape

def test_gmfgraph_Shape___init__():
    assert gmfgraph_Shape.__init__(gmfgraph_Shape(False, True, 0, '', False, False, gmfgraph_Shape=set()), False, True, 0, '', True, False, gmfgraph_Shape=set()) == None
