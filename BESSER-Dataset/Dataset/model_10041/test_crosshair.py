from enum import Enum
from python_code import AggregationKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AggregationKind.shared, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AggregationKind.shared, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AggregationKind.shared, '', '', '') == ''

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
        Enum._generate_next_value_(CallConcurrencyKind.guarded, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CallConcurrencyKind.guarded, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CallConcurrencyKind.guarded, 0, '', 0) == 0

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
        Enum._generate_next_value_(ConnectorKind.assembly, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConnectorKind.assembly, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConnectorKind.assembly, '', '', 0) == ''

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
from python_code import InteractionOperator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InteractionOperator.loop, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InteractionOperator.alt, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InteractionOperator.par, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InteractionOperator.opt, 0)

def test_Enum___new___2():
    assert Enum.__new__(InteractionOperator.par, 'par') == InteractionOperator.par

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
        Enum._generate_next_value_(MessageSort.synchCall, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MessageSort.synchCall, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MessageSort.synchCall, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MessageSort.synchCall, 0)

def test_Enum___new___2():
    assert Enum.__new__(MessageSort.synchCall, 'synchCall') == MessageSort.synchCall

from enum import Enum
from python_code import ObjectNodeOrderingKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ObjectNodeOrderingKind.ordered, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ObjectNodeOrderingKind.LIFO, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ObjectNodeOrderingKind.LIFO, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ObjectNodeOrderingKind.LIFO, 0)

def test_Enum___new___2():
    assert Enum.__new__(ObjectNodeOrderingKind.LIFO, 'LIFO') == ObjectNodeOrderingKind.LIFO

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
    assert Enum.__new__(ParameterDirectionKind.out, 'out') == ParameterDirectionKind.out

from enum import Enum
from python_code import ParameterEffectKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ParameterEffectKind.read, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ParameterEffectKind.read, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ParameterEffectKind.read, 0, '', 0) == 0

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
        Enum._generate_next_value_(PseudostateKind.join, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PseudostateKind.join, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PseudostateKind.join, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PseudostateKind.join, '')

def test_Enum___new___2():
    assert Enum.__new__(PseudostateKind.join, 'join') == PseudostateKind.join

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

from python_code import UML2_AddStructuralFeatureValueAction
from python_code import UML2_InputPin

def test_UML2_AddStructuralFeatureValueAction___init__():
    assert UML2_AddStructuralFeatureValueAction.__init__(UML2_AddStructuralFeatureValueAction(True, UML2_AddStructuralFeatureValueAction=UML2_InputPin()), False, UML2_AddStructuralFeatureValueAction=UML2_InputPin()) == None

from python_code import UML2_AddVariableValueAction
from python_code import UML2_InputPin

def test_UML2_AddVariableValueAction___init__():
    assert UML2_AddVariableValueAction.__init__(UML2_AddVariableValueAction(True, UML2_AddVariableValueAction=UML2_InputPin()), False, UML2_AddVariableValueAction=UML2_InputPin()) == None

from python_code import UML2_CallAction

def test_UML2_CallAction___init__():
    assert UML2_CallAction.__init__(UML2_CallAction(False, UML2_CallAction=set()), False, UML2_CallAction=set()) == None

from python_code import UML2_ClassifierTemplateParameter

def test_UML2_ClassifierTemplateParameter___init__():
    assert UML2_ClassifierTemplateParameter.__init__(UML2_ClassifierTemplateParameter(True), False) == None

from python_code import UML2_CombinedFragment

def test_UML2_CombinedFragment___init__():
    assert UML2_CombinedFragment.__init__(UML2_CombinedFragment('', UML2_CombinedFragment=set(), UML2_CombinedFragment672=set()), '', UML2_CombinedFragment=set(), UML2_CombinedFragment672=set()) == None

from python_code import UML2_Comment
from python_code import UML2_Element
from python_code import UML2_StringExpression

def test_UML2_Comment___init__():
    assert UML2_Comment.__init__(UML2_Comment('', UML2_Comment=UML2_Element(), UML2_Comment26=set(), UML2_Comment29=UML2_StringExpression()), '', UML2_Comment=UML2_Element(), UML2_Comment26=set(), UML2_Comment29=UML2_StringExpression()) == None

from python_code import UML2_Component
from python_code import UML2_Realization

def test_UML2_Component___init__():
    assert UML2_Component.__init__(UML2_Component(True, Component=UML2_Realization(), UML2_Component=set(), UML2_Component859=set(), abstraction=set(), UML2_Component863=set()), False, Component=UML2_Realization(), UML2_Component=set(), UML2_Component859=set(), abstraction=set(), UML2_Component863=set()) == None

from python_code import UML2_ConditionalNode

def test_UML2_ConditionalNode___init__():
    assert UML2_ConditionalNode.__init__(UML2_ConditionalNode(False, False, UML2_ConditionalNode=set(), UML2_ConditionalNode478=set()), False, True, UML2_ConditionalNode=set(), UML2_ConditionalNode478=set()) == None

from python_code import UML2_Continuation

def test_UML2_Continuation___init__():
    assert UML2_Continuation.__init__(UML2_Continuation(True), False) == None

from python_code import UML2_Deployment
from python_code import UML2_DeploymentSpecification

def test_UML2_DeploymentSpecification___init__():
    assert UML2_DeploymentSpecification.__init__(UML2_DeploymentSpecification('', '\x00', UML2_DeploymentSpecification=UML2_Deployment()), '\x00\x00', '', UML2_DeploymentSpecification=UML2_Deployment()) == None

from python_code import UML2_DestroyObjectAction
from python_code import UML2_InputPin

def test_UML2_DestroyObjectAction___init__():
    assert UML2_DestroyObjectAction.__init__(UML2_DestroyObjectAction(False, False, UML2_DestroyObjectAction=UML2_InputPin()), False, False, UML2_DestroyObjectAction=UML2_InputPin()) == None

from python_code import UML2_ExpansionNode
from python_code import UML2_ExpansionRegion

def test_UML2_ExpansionRegion___init__():
    assert UML2_ExpansionRegion.__init__(UML2_ExpansionRegion('', ExpansionRegion=UML2_ExpansionNode(), ExpansionRegion640=UML2_ExpansionNode(), regionAsOutput=set(), regionAsInput=set()), '', ExpansionRegion=UML2_ExpansionNode(), ExpansionRegion640=UML2_ExpansionNode(), regionAsOutput=set(), regionAsInput=set()) == None

from python_code import UML2_Expression

def test_UML2_Expression___init__():
    assert UML2_Expression.__init__(UML2_Expression('', UML2_Expression=set()), '', UML2_Expression=set()) == None
