from enum import Enum
from python_code import AggregationKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AggregationKind.none, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AggregationKind.none, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AggregationKind.none, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AggregationKind.none, 0)

def test_Enum___new___2():
    assert Enum.__new__(AggregationKind.none, 'none') == AggregationKind.none

from enum import Enum
from python_code import CallConcurrencyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CallConcurrencyKind.concurrent, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CallConcurrencyKind.sequential, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CallConcurrencyKind.sequential, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CallConcurrencyKind.guarded, 0)

def test_Enum___new___2():
    assert Enum.__new__(CallConcurrencyKind.guarded, 'guarded') == CallConcurrencyKind.guarded

from enum import Enum
from python_code import ConnectorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConnectorKind.assembly, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConnectorKind.assembly, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConnectorKind.assembly, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConnectorKind.assembly, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConnectorKind.assembly, 'assembly') == ConnectorKind.assembly

from enum import Enum
from python_code import ExpansionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ExpansionKind.stream, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ExpansionKind.stream, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ExpansionKind.stream, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ExpansionKind.stream, 0)

def test_Enum___new___2():
    assert Enum.__new__(ExpansionKind.stream, 'stream') == ExpansionKind.stream

from enum import Enum
from python_code import InteractionOperatorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InteractionOperatorKind.seq, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InteractionOperatorKind.seq, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InteractionOperatorKind.alt, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InteractionOperatorKind.opt, 0)

def test_Enum___new___2():
    assert Enum.__new__(InteractionOperatorKind.alt, 'alt') == InteractionOperatorKind.alt

from enum import Enum
from python_code import MessageKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MessageKind.lost, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MessageKind.lost, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MessageKind.lost, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MessageKind.lost, 0)

def test_Enum___new___2():
    assert Enum.__new__(MessageKind.lost, 'lost') == MessageKind.lost

from enum import Enum
from python_code import MessageSort
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MessageSort.reply, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MessageSort.reply, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MessageSort.reply, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MessageSort.reply, 0)

def test_Enum___new___2():
    assert Enum.__new__(MessageSort.reply, 'reply') == MessageSort.reply

from enum import Enum
from python_code import ObjectNodeOrderingKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ObjectNodeOrderingKind.LIFO, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ObjectNodeOrderingKind.FIFO, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ObjectNodeOrderingKind.FIFO, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ObjectNodeOrderingKind.FIFO, 0)

def test_Enum___new___2():
    assert Enum.__new__(ObjectNodeOrderingKind.LIFO, 'FIFO') == ObjectNodeOrderingKind.FIFO

from enum import Enum
from python_code import ParameterDirectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ParameterDirectionKind.out, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ParameterDirectionKind.out, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ParameterDirectionKind.out, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ParameterDirectionKind.out, 0)

def test_Enum___new___2():
    assert Enum.__new__(ParameterDirectionKind.in_, 'out') == ParameterDirectionKind.out

from enum import Enum
from python_code import ParameterEffectKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ParameterEffectKind.create, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ParameterEffectKind.read, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ParameterEffectKind.read, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ParameterEffectKind.read, 0)

def test_Enum___new___2():
    assert Enum.__new__(ParameterEffectKind.read, 'read') == ParameterEffectKind.read

from enum import Enum
from python_code import PseudostateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PseudostateKind.join, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PseudostateKind.fork, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PseudostateKind.join, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PseudostateKind.join, '')

def test_Enum___new___2():
    assert Enum.__new__(PseudostateKind.join, 'fork') == PseudostateKind.fork

from enum import Enum
from python_code import TransitionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TransitionKind.external, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TransitionKind.internal, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TransitionKind.internal, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TransitionKind.local, 0)

def test_Enum___new___2():
    assert Enum.__new__(TransitionKind.local, 'local') == TransitionKind.local

from enum import Enum
from python_code import VisibilityKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(VisibilityKind.private, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(VisibilityKind.public, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(VisibilityKind.package, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(VisibilityKind.public, 0)

def test_Enum___new___2():
    assert Enum.__new__(VisibilityKind.public, 'public') == VisibilityKind.public

from python_code import uml_AcceptEventAction

def test_uml_AcceptEventAction___init__():
    assert uml_AcceptEventAction.__init__(uml_AcceptEventAction('', uml_AcceptEventAction=set(), uml_AcceptEventAction968=set()), '', uml_AcceptEventAction=set(), uml_AcceptEventAction968=set()) == None

from python_code import uml_AddStructuralFeatureValueAction
from python_code import uml_InputPin

def test_uml_AddStructuralFeatureValueAction___init__():
    assert uml_AddStructuralFeatureValueAction.__init__(uml_AddStructuralFeatureValueAction('', uml_AddStructuralFeatureValueAction=uml_InputPin()), '', uml_AddStructuralFeatureValueAction=uml_InputPin()) == None

from python_code import uml_AddVariableValueAction
from python_code import uml_InputPin

def test_uml_AddVariableValueAction___init__():
    assert uml_AddVariableValueAction.__init__(uml_AddVariableValueAction('', uml_AddVariableValueAction=uml_InputPin()), '', uml_AddVariableValueAction=uml_InputPin()) == None

from python_code import uml_CallAction

def test_uml_CallAction___init__():
    assert uml_CallAction.__init__(uml_CallAction('', uml_CallAction=set()), '', uml_CallAction=set()) == None
