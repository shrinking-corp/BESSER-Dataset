from enum import Enum
from python_code import CSS2Color
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CSS2Color.BLUE, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CSS2Color.BLUE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CSS2Color.GRAY, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CSS2Color.BLUE, 0)

def test_Enum___new___2():
    assert Enum.__new__(CSS2Color.AQUA, 'RED') == CSS2Color.RED

from enum import Enum
from python_code import CSS2FontFamily
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CSS2FontFamily.ARIAL, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CSS2FontFamily.ARIAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CSS2FontFamily.ARIAL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CSS2FontFamily.TIMES, 0)

def test_Enum___new___2():
    assert Enum.__new__(CSS2FontFamily.TIMES, 'TIMES') == CSS2FontFamily.TIMES

from enum import Enum
from python_code import CSS2FontSize
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CSS2FontSize.XSMALL, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CSS2FontSize.XSMALL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CSS2FontSize.XSMALL, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CSS2FontSize.SMALL, 0)

def test_Enum___new___2():
    assert Enum.__new__(CSS2FontSize.SMALL, 'SMALL') == CSS2FontSize.SMALL

from enum import Enum
from python_code import CSS2FontStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CSS2FontStyle.NORMAL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CSS2FontStyle.NORMAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CSS2FontStyle.NORMAL, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CSS2FontStyle.ITALIC, 0)

def test_Enum___new___2():
    assert Enum.__new__(CSS2FontStyle.ITALIC, 'NORMAL') == CSS2FontStyle.NORMAL

from enum import Enum
from python_code import CSS2FontWeight
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CSS2FontWeight.BOLD, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CSS2FontWeight.BOLD, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CSS2FontWeight.BOLD, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CSS2FontWeight.BOLD, 0)

def test_Enum___new___2():
    assert Enum.__new__(CSS2FontWeight.BOLD, 'BOLD') == CSS2FontWeight.BOLD

from enum import Enum
from python_code import FontAlign
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FontAlign.LEFT, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FontAlign.LEFT, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FontAlign.LEFT, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FontAlign.LEFT, 0)

def test_Enum___new___2():
    assert Enum.__new__(FontAlign.LEFT, 'LEFT') == FontAlign.LEFT

from enum import Enum
from python_code import FontDecoration
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FontDecoration.UNDERLINE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FontDecoration.UNDERLINE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FontDecoration.UNDERLINE, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FontDecoration.OVERLINE, 0)

def test_Enum___new___2():
    assert Enum.__new__(FontDecoration.OVERLINE, 'OVERLINE') == FontDecoration.OVERLINE

from enum import Enum
from python_code import GSPNArcType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GSPNArcType.normal, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GSPNArcType.normal, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GSPNArcType.normal, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GSPNArcType.normal, 0)

def test_Enum___new___2():
    assert Enum.__new__(GSPNArcType.normal, 'normal') == GSPNArcType.normal

from enum import Enum
from python_code import GSPNTransitionType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GSPNTransitionType.timed, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GSPNTransitionType.timed, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GSPNTransitionType.timed, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GSPNTransitionType.timed, 0)

def test_Enum___new___2():
    assert Enum.__new__(GSPNTransitionType.timed, 'timed') == GSPNTransitionType.timed

from enum import Enum
from python_code import Gradient
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Gradient.DIAGONAL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Gradient.DIAGONAL, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Gradient.DIAGONAL, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Gradient.DIAGONAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(Gradient.DIAGONAL, 'DIAGONAL') == Gradient.DIAGONAL

from enum import Enum
from python_code import LineShape
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LineShape.CURVE, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LineShape.CURVE, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LineShape.LINE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LineShape.LINE, 0)

def test_Enum___new___2():
    assert Enum.__new__(LineShape.LINE, 'LINE') == LineShape.LINE

from enum import Enum
from python_code import LineStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LineStyle.DOT, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LineStyle.DOT, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LineStyle.DOT, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LineStyle.DOT, 0)

def test_Enum___new___2():
    assert Enum.__new__(LineStyle.DOT, 'DOT') == LineStyle.DOT

from enum import Enum
from python_code import PNType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PNType.GSPN, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PNType.GSPN, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PNType.HLPN, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PNType.GSPN, 0)

def test_Enum___new___2():
    assert Enum.__new__(PNType.HLPN, 'GSPN') == PNType.GSPN

from python_code import ptnet_Coordinate

def test_ptnet_Coordinate___init__():
    assert ptnet_Coordinate.__init__(ptnet_Coordinate('', '\x00'), '\x00\x00', '') == None

from python_code import ptnet_Deterministic

def test_ptnet_Deterministic___init__():
    assert ptnet_Deterministic.__init__(ptnet_Deterministic(0.0), 0.0) == None

from python_code import ptnet_Exponential

def test_ptnet_Exponential___init__():
    assert ptnet_Exponential.__init__(ptnet_Exponential(0.0), 0.0) == None

from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Fill
from python_code import ptnet_NodeGraphics

def test_ptnet_Fill___init__():
    assert ptnet_Fill.__init__(ptnet_Fill('\x00\x00', '', '', '', Fill52=ptnet_AnnotationGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics(), Fill=ptnet_NodeGraphics()), '', '', '', '', Fill52=ptnet_AnnotationGraphics(), fill62=ptnet_AnnotationGraphics(), fill=ptnet_NodeGraphics(), Fill=ptnet_NodeGraphics()) == None

from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_Font

def test_ptnet_Font___init__():
    assert ptnet_Font.__init__(ptnet_Font('', '', '', '', '', '', '', Font=ptnet_AnnotationGraphics(), font=ptnet_AnnotationGraphics()), '', '\x00', '', '', '', '', '', Font=ptnet_AnnotationGraphics(), font=ptnet_AnnotationGraphics()) == None

from python_code import ptnet_ArithmeticExpression
from python_code import ptnet_GSPNArc

def test_ptnet_GSPNArc___init__():
    assert ptnet_GSPNArc.__init__(ptnet_GSPNArc('', ptnet_GSPNArc=ptnet_ArithmeticExpression()), '', ptnet_GSPNArc=ptnet_ArithmeticExpression()) == None

from python_code import ptnet_GSPNImmediateTransition

def test_ptnet_GSPNImmediateTransition___init__():
    assert ptnet_GSPNImmediateTransition.__init__(ptnet_GSPNImmediateTransition(0, 0.0), 0, 0.0) == None

from python_code import ptnet_Gamma

def test_ptnet_Gamma___init__():
    assert ptnet_Gamma.__init__(ptnet_Gamma(0.0, 0.0), 0.0, 0.0) == None

from python_code import ptnet_Gaussian

def test_ptnet_Gaussian___init__():
    assert ptnet_Gaussian.__init__(ptnet_Gaussian(0.0, 0.0), 0.0, 0.0) == None

from python_code import ptnet_AnnotationGraphics
from python_code import ptnet_ArcGraphics
from python_code import ptnet_Line
from python_code import ptnet_NodeGraphics

def test_ptnet_Line___init__():
    assert ptnet_Line.__init__(ptnet_Line('\x00\x00', '', '', '', Line55=ptnet_AnnotationGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), line70=ptnet_AnnotationGraphics(), Line=ptnet_NodeGraphics(), Line76=ptnet_ArcGraphics()), '', '', '', '', Line55=ptnet_AnnotationGraphics(), line=ptnet_NodeGraphics(), line67=ptnet_ArcGraphics(), line70=ptnet_AnnotationGraphics(), Line=ptnet_NodeGraphics(), Line76=ptnet_ArcGraphics()) == None

from python_code import ptnet_ArithmeticExpression
from python_code import ptnet_EvaluationList
from python_code import ptnet_EvaluationType
from python_code import ptnet_Measure

def test_ptnet_Measure___init__():
    assert ptnet_Measure.__init__(ptnet_Measure('', ptnet_Measure117=ptnet_EvaluationType(), ptnet_Measure=ptnet_EvaluationList(), ptnet_Measure114=ptnet_ArithmeticExpression()), '', ptnet_Measure117=ptnet_EvaluationType(), ptnet_Measure=ptnet_EvaluationList(), ptnet_Measure114=ptnet_ArithmeticExpression()) == None

from python_code import ptnet_Arc
from python_code import ptnet_PTArcAnnotation

def test_ptnet_PTArcAnnotation___init__():
    assert ptnet_PTArcAnnotation.__init__(ptnet_PTArcAnnotation('', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()), '', inscription=ptnet_Arc(), PTArcAnnotation=ptnet_Arc()) == None

from python_code import ptnet_PTMarking
from python_code import ptnet_Place

def test_ptnet_PTMarking___init__():
    assert ptnet_PTMarking.__init__(ptnet_PTMarking('', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()), '', initialMarking=ptnet_Place(), PTMarking=ptnet_Place()) == None

from python_code import ptnet_Uniform

def test_ptnet_Uniform___init__():
    assert ptnet_Uniform.__init__(ptnet_Uniform(0.0, 0.0), 0.0, 0.0) == None

from python_code import ptnet_ValueExpression

def test_ptnet_ValueExpression___init__():
    assert ptnet_ValueExpression.__init__(ptnet_ValueExpression(0.0), 0.0) == None

from python_code import ptnet_Weibull

def test_ptnet_Weibull___init__():
    assert ptnet_Weibull.__init__(ptnet_Weibull(0.0, 0.0), 0.0, 0.0) == None
