from enum import Enum
from python_code import AlignmentKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AlignmentKind.SQUARE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AlignmentKind.SQUARE, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AlignmentKind.SQUARE, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AlignmentKind.SQUARE, 0)

def test_Enum___new___2():
    assert Enum.__new__(AlignmentKind.SQUARE, 'SQUARE') == AlignmentKind.SQUARE

from enum import Enum
from python_code import ArrangeConstraint
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ArrangeConstraint.KEEP_RATIO, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ArrangeConstraint.KEEP_RATIO, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ArrangeConstraint.KEEP_RATIO, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ArrangeConstraint.KEEP_SIZE, 0)

def test_Enum___new___2():
    assert Enum.__new__(ArrangeConstraint.KEEP_SIZE, 'KEEP_SIZE') == ArrangeConstraint.KEEP_SIZE

from enum import Enum
from python_code import BackgroundStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BackgroundStyle.GradientTopToBottom, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BackgroundStyle.GradientLeftToRight, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BackgroundStyle.Liquid, 0, '\x00', '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BackgroundStyle.Liquid, 0)

def test_Enum___new___2():
    assert Enum.__new__(BackgroundStyle.Liquid, 'Liquid') == BackgroundStyle.Liquid

from enum import Enum
from python_code import BundledImageShape
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(BundledImageShape.dot, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(BundledImageShape.ring, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(BundledImageShape.dot, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(BundledImageShape.dot, 0)

def test_Enum___new___2():
    assert Enum.__new__(BundledImageShape.dot, 'dot') == BundledImageShape.dot

from enum import Enum
from python_code import CenteringStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CenteringStyle.Both, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CenteringStyle.Both, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CenteringStyle.Both, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CenteringStyle.Both, 0)

def test_Enum___new___2():
    assert Enum.__new__(CenteringStyle.Both, 'Both') == CenteringStyle.Both

from enum import Enum
from python_code import ContainerLayout
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ContainerLayout.List, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ContainerLayout.List, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ContainerLayout.List, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ContainerLayout.List, 0)

def test_Enum___new___2():
    assert Enum.__new__(ContainerLayout.List, 'List') == ContainerLayout.List

from enum import Enum
from python_code import ContainerShape
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ContainerShape.parallelogram, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ContainerShape.parallelogram, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ContainerShape.parallelogram, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ContainerShape.parallelogram, 0)

def test_Enum___new___2():
    assert Enum.__new__(ContainerShape.parallelogram, 'parallelogram') == ContainerShape.parallelogram

from enum import Enum
from python_code import EdgeArrows
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EdgeArrows.InputArrow, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EdgeArrows.Diamond, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EdgeArrows.Diamond, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EdgeArrows.InputArrow, 0)

def test_Enum___new___2():
    assert Enum.__new__(EdgeArrows.Diamond, 'InputArrow') == EdgeArrows.InputArrow

from enum import Enum
from python_code import EdgeRouting
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EdgeRouting.tree, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EdgeRouting.tree, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EdgeRouting.tree, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EdgeRouting.tree, 0)

def test_Enum___new___2():
    assert Enum.__new__(EdgeRouting.tree, 'tree') == EdgeRouting.tree

from enum import Enum
from python_code import FilterKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FilterKind.HIDE, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FilterKind.HIDE, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FilterKind.HIDE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FilterKind.HIDE, 0)

def test_Enum___new___2():
    assert Enum.__new__(FilterKind.HIDE, 'HIDE') == FilterKind.HIDE

from enum import Enum
from python_code import FoldingStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FoldingStyle.NONE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FoldingStyle.NONE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FoldingStyle.NONE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FoldingStyle.NONE, 0)

def test_Enum___new___2():
    assert Enum.__new__(FoldingStyle.NONE, 'NONE') == FoldingStyle.NONE

from enum import Enum
from python_code import LabelPosition
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LabelPosition.node, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LabelPosition.node, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LabelPosition.node, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LabelPosition.node, 0)

def test_Enum___new___2():
    assert Enum.__new__(LabelPosition.node, 'node') == LabelPosition.node

from enum import Enum
from python_code import LayoutDirection
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LayoutDirection.BottomToTop, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LayoutDirection.TopToBottom, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LayoutDirection.TopToBottom, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LayoutDirection.BottomToTop, 0)

def test_Enum___new___2():
    assert Enum.__new__(LayoutDirection.BottomToTop, 'BottomToTop') == LayoutDirection.BottomToTop

from enum import Enum
from python_code import LayoutOptionTarget
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LayoutOptionTarget.NODE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LayoutOptionTarget.EDGE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LayoutOptionTarget.EDGE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LayoutOptionTarget.EDGE, 0)

def test_Enum___new___2():
    assert Enum.__new__(LayoutOptionTarget.EDGE, 'EDGE') == LayoutOptionTarget.EDGE

from enum import Enum
from python_code import LineStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LineStyle.dot, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LineStyle.dot, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LineStyle.dot, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LineStyle.dot, 0)

def test_Enum___new___2():
    assert Enum.__new__(LineStyle.dot, 'dot') == LineStyle.dot

from enum import Enum
from python_code import ReconnectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ReconnectionKind.RECONNECT_BOTH, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ReconnectionKind.RECONNECT_BOTH, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ReconnectionKind.RECONNECT_BOTH, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ReconnectionKind.RECONNECT_BOTH, 0)

def test_Enum___new___2():
    assert Enum.__new__(ReconnectionKind.RECONNECT_BOTH, 'RECONNECT_BOTH') == ReconnectionKind.RECONNECT_BOTH

from enum import Enum
from python_code import ResizeKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ResizeKind.NSEW, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ResizeKind.NSEW, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ResizeKind.NSEW, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ResizeKind.NSEW, 0)

def test_Enum___new___2():
    assert Enum.__new__(ResizeKind.NSEW, 'NSEW') == ResizeKind.NSEW

from enum import Enum
from python_code import Side
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Side.EAST, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Side.EAST, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Side.EAST, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Side.EAST, 0)

def test_Enum___new___2():
    assert Enum.__new__(Side.EAST, 'EAST') == Side.EAST

from python_code import diagram_AbsoluteBoundsFilter

def test_diagram_AbsoluteBoundsFilter___init__():
    assert diagram_AbsoluteBoundsFilter.__init__(diagram_AbsoluteBoundsFilter('\x00\x00', '', '', ''), '', '', '', '') == None
