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
    assert Enum.__new__(InteractionOperator.opt, 'neg') == InteractionOperator.neg

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
        Enum.__new__(ParameterDirectionKind.in_, 0)

def test_Enum___new___2():
    assert Enum.__new__(ParameterDirectionKind.in_, 'out') == ParameterDirectionKind.out

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
        Enum.__new__(PseudostateKind.join, 0)

def test_Enum___new___2():
    assert Enum.__new__(PseudostateKind.choice, 'join') == PseudostateKind.join

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

from python_code import UML2WithID_AddStructuralFeatureValueAction
from python_code import UML2WithID_InputPin

def test_UML2WithID_AddStructuralFeatureValueAction___init__():
    assert UML2WithID_AddStructuralFeatureValueAction.__init__(UML2WithID_AddStructuralFeatureValueAction(True, UML2WithID_AddStructuralFeatureValueAction=UML2WithID_InputPin()), False, UML2WithID_AddStructuralFeatureValueAction=UML2WithID_InputPin()) == None

from python_code import UML2WithID_AddVariableValueAction
from python_code import UML2WithID_InputPin

def test_UML2WithID_AddVariableValueAction___init__():
    assert UML2WithID_AddVariableValueAction.__init__(UML2WithID_AddVariableValueAction(True, UML2WithID_AddVariableValueAction=UML2WithID_InputPin()), False, UML2WithID_AddVariableValueAction=UML2WithID_InputPin()) == None

from python_code import UML2WithID_CallAction

def test_UML2WithID_CallAction___init__():
    assert UML2WithID_CallAction.__init__(UML2WithID_CallAction(False, UML2WithID_CallAction=set()), False, UML2WithID_CallAction=set()) == None

from python_code import UML2WithID_ClassifierTemplateParameter

def test_UML2WithID_ClassifierTemplateParameter___init__():
    assert UML2WithID_ClassifierTemplateParameter.__init__(UML2WithID_ClassifierTemplateParameter(True), False) == None

from python_code import UML2WithID_CombinedFragment

def test_UML2WithID_CombinedFragment___init__():
    assert UML2WithID_CombinedFragment.__init__(UML2WithID_CombinedFragment('', UML2WithID_CombinedFragment=set(), UML2WithID_CombinedFragment672=set()), '', UML2WithID_CombinedFragment=set(), UML2WithID_CombinedFragment672=set()) == None

from python_code import UML2WithID_Component
from python_code import UML2WithID_Realization

def test_UML2WithID_Component___init__():
    assert UML2WithID_Component.__init__(UML2WithID_Component(False, Component=UML2WithID_Realization(), UML2WithID_Component={<python_code.UML2WithID_Interface object at 0x000001B31C07B790>}, UML2WithID_Component859=set(), abstraction=set(), UML2WithID_Component863=set()), True, Component=UML2WithID_Realization(), UML2WithID_Component=set(), UML2WithID_Component859=set(), abstraction=set(), UML2WithID_Component863=set()) == None

from python_code import UML2WithID_ConditionalNode

def test_UML2WithID_ConditionalNode___init__():
    assert UML2WithID_ConditionalNode.__init__(UML2WithID_ConditionalNode(False, False, UML2WithID_ConditionalNode=set(), UML2WithID_ConditionalNode478=set()), False, True, UML2WithID_ConditionalNode=set(), UML2WithID_ConditionalNode478=set()) == None

from python_code import UML2WithID_Continuation

def test_UML2WithID_Continuation___init__():
    assert UML2WithID_Continuation.__init__(UML2WithID_Continuation(True), False) == None

from python_code import UML2WithID_Deployment
from python_code import UML2WithID_DeploymentSpecification

def test_UML2WithID_DeploymentSpecification___init__():
    assert UML2WithID_DeploymentSpecification.__init__(UML2WithID_DeploymentSpecification('', '\x00', UML2WithID_DeploymentSpecification=UML2WithID_Deployment()), '\x00\x00', '', UML2WithID_DeploymentSpecification=UML2WithID_Deployment()) == None

from python_code import UML2WithID_DestroyObjectAction
from python_code import UML2WithID_InputPin

def test_UML2WithID_DestroyObjectAction___init__():
    assert UML2WithID_DestroyObjectAction.__init__(UML2WithID_DestroyObjectAction(False, False, UML2WithID_DestroyObjectAction=UML2WithID_InputPin()), False, False, UML2WithID_DestroyObjectAction=UML2WithID_InputPin()) == None

from python_code import UML2WithID_ExpansionNode
from python_code import UML2WithID_ExpansionRegion

def test_UML2WithID_ExpansionRegion___init__():
    assert UML2WithID_ExpansionRegion.__init__(UML2WithID_ExpansionRegion('', ExpansionRegion=UML2WithID_ExpansionNode(), ExpansionRegion640=UML2WithID_ExpansionNode(), regionAsOutput=set(), regionAsInput=set()), '', ExpansionRegion=UML2WithID_ExpansionNode(), ExpansionRegion640=UML2WithID_ExpansionNode(), regionAsOutput=set(), regionAsInput=set()) == None

from python_code import UML2WithID_Expression

def test_UML2WithID_Expression___init__():
    assert UML2WithID_Expression.__init__(UML2WithID_Expression('', UML2WithID_Expression=set()), '', UML2WithID_Expression=set()) == None

from python_code import UML2WithID_JoinNode
from python_code import UML2WithID_ValueSpecification

def test_UML2WithID_JoinNode___init__():
    assert UML2WithID_JoinNode.__init__(UML2WithID_JoinNode(True, UML2WithID_JoinNode=UML2WithID_ValueSpecification()), False, UML2WithID_JoinNode=UML2WithID_ValueSpecification()) == None

from python_code import UML2WithID_InputPin
from python_code import UML2WithID_LinkEndCreationData

def test_UML2WithID_LinkEndCreationData___init__():
    assert UML2WithID_LinkEndCreationData.__init__(UML2WithID_LinkEndCreationData(True, UML2WithID_LinkEndCreationData=UML2WithID_InputPin()), False, UML2WithID_LinkEndCreationData=UML2WithID_InputPin()) == None

from python_code import UML2WithID_LiteralBoolean

def test_UML2WithID_LiteralBoolean___init__():
    assert UML2WithID_LiteralBoolean.__init__(UML2WithID_LiteralBoolean(True), False) == None

from python_code import UML2WithID_LiteralInteger

def test_UML2WithID_LiteralInteger___init__():
    assert UML2WithID_LiteralInteger.__init__(UML2WithID_LiteralInteger(0), 0) == None

from python_code import UML2WithID_LiteralString

def test_UML2WithID_LiteralString___init__():
    assert UML2WithID_LiteralString.__init__(UML2WithID_LiteralString(''), '') == None

from python_code import UML2WithID_LiteralUnlimitedNatural

def test_UML2WithID_LiteralUnlimitedNatural___init__():
    assert UML2WithID_LiteralUnlimitedNatural.__init__(UML2WithID_LiteralUnlimitedNatural(''), '') == None

from python_code import UML2WithID_LoopNode
from python_code import UML2WithID_OutputPin

def test_UML2WithID_LoopNode___init__():
    assert UML2WithID_LoopNode.__init__(UML2WithID_LoopNode(False, UML2WithID_LoopNode=set(), UML2WithID_LoopNode500=set(), UML2WithID_LoopNode503=UML2WithID_OutputPin(), UML2WithID_LoopNode506=set(), UML2WithID_LoopNode509=set(), UML2WithID_LoopNode512=set(), UML2WithID_LoopNode515=set(), UML2WithID_LoopNode518=set()), False, UML2WithID_LoopNode=set(), UML2WithID_LoopNode500=set(), UML2WithID_LoopNode503=UML2WithID_OutputPin(), UML2WithID_LoopNode506=set(), UML2WithID_LoopNode509=set(), UML2WithID_LoopNode512=set(), UML2WithID_LoopNode515=set(), UML2WithID_LoopNode518=set()) == None
