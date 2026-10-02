from enum import Enum
from python_code import DefencePositionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DefencePositionKind.right_defence, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DefencePositionKind.right_defence, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DefencePositionKind.left_defence, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DefencePositionKind.left_defence, 0)

def test_Enum___new___2():
    assert Enum.__new__(DefencePositionKind.left_defence, 'left_defence') == DefencePositionKind.left_defence

from enum import Enum
from python_code import ForwardPositionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ForwardPositionKind.center, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ForwardPositionKind.center, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ForwardPositionKind.center, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ForwardPositionKind.center, 0)

def test_Enum___new___2():
    assert Enum.__new__(ForwardPositionKind.center, 'center') == ForwardPositionKind.center

from enum import Enum
from python_code import HeightKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(HeightKind.inches, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(HeightKind.inches, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(HeightKind.inches, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(HeightKind.inches, 0)

def test_Enum___new___2():
    assert Enum.__new__(HeightKind.inches, 'inches') == HeightKind.inches

from enum import Enum
from python_code import ShotKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ShotKind.right, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ShotKind.right, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ShotKind.left, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ShotKind.left, 0)

def test_Enum___new___2():
    assert Enum.__new__(ShotKind.left, 'left') == ShotKind.left

from enum import Enum
from python_code import WeightKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(WeightKind.pounds, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(WeightKind.pounds, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(WeightKind.pounds, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(WeightKind.pounds, 0)

def test_Enum___new___2():
    assert Enum.__new__(WeightKind.pounds, 'pounds') == WeightKind.pounds

from python_code import hockeyleague_Arena
from python_code import hockeyleague_Team

def test_hockeyleague_Arena___init__():
    assert hockeyleague_Arena.__init__(hockeyleague_Arena('', 0, hockeyleague_Arena=hockeyleague_Team()), '', 0, hockeyleague_Arena=hockeyleague_Team()) == None

from python_code import hockeyleague_Defence
from python_code import hockeyleague_Team

def test_hockeyleague_Defence___init__():
    assert hockeyleague_Defence.__init__(hockeyleague_Defence('', hockeyleague_Defence=set(), hockeyleague_Defence16=hockeyleague_Team()), '', hockeyleague_Defence=set(), hockeyleague_Defence16=hockeyleague_Team()) == None

from python_code import hockeyleague_Forward
from python_code import hockeyleague_Team

def test_hockeyleague_Forward___init__():
    assert hockeyleague_Forward.__init__(hockeyleague_Forward('', hockeyleague_Forward=set(), hockeyleague_Forward13=hockeyleague_Team()), '', hockeyleague_Forward=set(), hockeyleague_Forward13=hockeyleague_Team()) == None

from python_code import hockeyleague_Goalie
from python_code import hockeyleague_GoalieStats
from python_code import hockeyleague_Team

def test_hockeyleague_GoalieStats___init__():
    assert hockeyleague_GoalieStats.__init__(hockeyleague_GoalieStats(0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0.0, 0, 0, hockeyleague_GoalieStats=hockeyleague_Goalie(), hockeyleague_GoalieStats5=hockeyleague_Team()), 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0.0, 0, 0, hockeyleague_GoalieStats=hockeyleague_Goalie(), hockeyleague_GoalieStats5=hockeyleague_Team()) == None

from python_code import hockeyleague_HockeyleagueObject

def test_hockeyleague_HockeyleagueObject___init__():
    assert hockeyleague_HockeyleagueObject.__init__(hockeyleague_HockeyleagueObject(''), '') == None

from python_code import hockeyleague_League

def test_hockeyleague_League___init__():
    assert hockeyleague_League.__init__(hockeyleague_League('', hockeyleague_League=set()), '', hockeyleague_League=set()) == None

from python_code import hockeyleague_Player

def test_hockeyleague_Player___init__():
    assert hockeyleague_Player.__init__(hockeyleague_Player(0, '', 0, '', 0, '', '\x00', ''), 0, '', 0, '', 0, '', '', '') == None
