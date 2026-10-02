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
from python_code import CallConcurrencyFeature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CallConcurrencyFeature.concurrent, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CallConcurrencyFeature.sequential, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CallConcurrencyFeature.sequential, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CallConcurrencyFeature.guarded, 0)

def test_Enum___new___2():
    assert Enum.__new__(CallConcurrencyFeature.guarded, 'guarded') == CallConcurrencyFeature.guarded

from python_code import CompleteDSLPckg_AcceptEventAction

def test_CompleteDSLPckg_AcceptEventAction___init__():
    assert CompleteDSLPckg_AcceptEventAction.__init__(CompleteDSLPckg_AcceptEventAction(False, CompleteDSLPckg_AcceptEventAction=set(), CompleteDSLPckg_AcceptEventAction503=set()), False, CompleteDSLPckg_AcceptEventAction=set(), CompleteDSLPckg_AcceptEventAction503=set()) == None

from python_code import CompleteDSLPckg_CallAction

def test_CompleteDSLPckg_CallAction___init__():
    assert CompleteDSLPckg_CallAction.__init__(CompleteDSLPckg_CallAction(False, CompleteDSLPckg_CallAction=set()), False, CompleteDSLPckg_CallAction=set()) == None

from python_code import CompleteDSLPckg_CombinedFragment
from python_code import CompleteDSLPckg_InteractionOperand

def test_CompleteDSLPckg_CombinedFragment___init__():
    assert CompleteDSLPckg_CombinedFragment.__init__(CompleteDSLPckg_CombinedFragment('', CompleteDSLPckg_CombinedFragment=CompleteDSLPckg_InteractionOperand(), CompleteDSLPckg_CombinedFragment959=set()), '', CompleteDSLPckg_CombinedFragment=CompleteDSLPckg_InteractionOperand(), CompleteDSLPckg_CombinedFragment959=set()) == None

from python_code import CompleteDSLPckg_Comment
from python_code import CompleteDSLPckg_Element

def test_CompleteDSLPckg_Comment___init__():
    assert CompleteDSLPckg_Comment.__init__(CompleteDSLPckg_Comment('', ownedComment=CompleteDSLPckg_Element(), CompleteDSLPckg_Comment=set(), Comment=CompleteDSLPckg_Element()), '', ownedComment=CompleteDSLPckg_Element(), CompleteDSLPckg_Comment=set(), Comment=CompleteDSLPckg_Element()) == None

from python_code import CompleteDSLPckg_Component
from python_code import CompleteDSLPckg_ComponentRealization

def test_CompleteDSLPckg_Component___init__():
    assert CompleteDSLPckg_Component.__init__(CompleteDSLPckg_Component(False, CompleteDSLPckg_Component=set(), CompleteDSLPckg_Component298=set(), CompleteDSLPckg_Component301=set(), CompleteDSLPckg_Component303=set(), CompleteDSLPckg_Component307=CompleteDSLPckg_ComponentRealization()), False, CompleteDSLPckg_Component=set(), CompleteDSLPckg_Component298=set(), CompleteDSLPckg_Component301=set(), CompleteDSLPckg_Component303=set(), CompleteDSLPckg_Component307=CompleteDSLPckg_ComponentRealization()) == None

from python_code import CompleteDSLPckg_ConditionalNode

def test_CompleteDSLPckg_ConditionalNode___init__():
    assert CompleteDSLPckg_ConditionalNode.__init__(CompleteDSLPckg_ConditionalNode(False, False, CompleteDSLPckg_ConditionalNode=set(), CompleteDSLPckg_ConditionalNode842=set(), CompleteDSLPckg_ConditionalNode845=set(), CompleteDSLPckg_ConditionalNode848=set()), False, False, CompleteDSLPckg_ConditionalNode=set(), CompleteDSLPckg_ConditionalNode842=set(), CompleteDSLPckg_ConditionalNode845=set(), CompleteDSLPckg_ConditionalNode848=set()) == None

from python_code import CompleteDSLPckg_Continuation

def test_CompleteDSLPckg_Continuation___init__():
    assert CompleteDSLPckg_Continuation.__init__(CompleteDSLPckg_Continuation(True), False) == None

from python_code import CompleteDSLPckg_Deployment
from python_code import CompleteDSLPckg_DeploymentSpecification

def test_CompleteDSLPckg_DeploymentSpecification___init__():
    assert CompleteDSLPckg_DeploymentSpecification.__init__(CompleteDSLPckg_DeploymentSpecification('', '\x00', CompleteDSLPckg_DeploymentSpecification=CompleteDSLPckg_Deployment(), CompleteDSLPckg_DeploymentSpecification390=CompleteDSLPckg_Deployment()), '\x00\x00', '', CompleteDSLPckg_DeploymentSpecification=CompleteDSLPckg_Deployment(), CompleteDSLPckg_DeploymentSpecification390=CompleteDSLPckg_Deployment()) == None

from python_code import CompleteDSLPckg_DurationConstraint
from python_code import CompleteDSLPckg_DurationInterval

def test_CompleteDSLPckg_DurationConstraint___init__():
    assert CompleteDSLPckg_DurationConstraint.__init__(CompleteDSLPckg_DurationConstraint(True, CompleteDSLPckg_DurationConstraint=CompleteDSLPckg_DurationInterval()), False, CompleteDSLPckg_DurationConstraint=CompleteDSLPckg_DurationInterval()) == None

from python_code import CompleteDSLPckg_ElementImport
from python_code import CompleteDSLPckg_Namespace
from python_code import CompleteDSLPckg_PackageableElement

def test_CompleteDSLPckg_ElementImport___init__():
    assert CompleteDSLPckg_ElementImport.__init__(CompleteDSLPckg_ElementImport('', '\x00', CompleteDSLPckg_ElementImport=CompleteDSLPckg_PackageableElement(), elementImport=CompleteDSLPckg_Namespace(), ElementImport=CompleteDSLPckg_Namespace()), '\x00\x00', '', CompleteDSLPckg_ElementImport=CompleteDSLPckg_PackageableElement(), elementImport=CompleteDSLPckg_Namespace(), ElementImport=CompleteDSLPckg_Namespace()) == None

from python_code import CompleteDSLPckg_ExpansionNode
from python_code import CompleteDSLPckg_ExpansionRegion

def test_CompleteDSLPckg_ExpansionRegion___init__():
    assert CompleteDSLPckg_ExpansionRegion.__init__(CompleteDSLPckg_ExpansionRegion('', CompleteDSLPckg_ExpansionRegion878=CompleteDSLPckg_ExpansionNode(), CompleteDSLPckg_ExpansionRegion881=CompleteDSLPckg_ExpansionNode(), CompleteDSLPckg_ExpansionRegion=set(), CompleteDSLPckg_ExpansionRegion874=set()), '', CompleteDSLPckg_ExpansionRegion878=CompleteDSLPckg_ExpansionNode(), CompleteDSLPckg_ExpansionRegion881=CompleteDSLPckg_ExpansionNode(), CompleteDSLPckg_ExpansionRegion=set(), CompleteDSLPckg_ExpansionRegion874=set()) == None

from python_code import CompleteDSLPckg_Expression
from python_code import CompleteDSLPckg_ValueSpecification

def test_CompleteDSLPckg_Expression___init__():
    assert CompleteDSLPckg_Expression.__init__(CompleteDSLPckg_Expression('', CompleteDSLPckg_Expression=CompleteDSLPckg_ValueSpecification()), '', CompleteDSLPckg_Expression=CompleteDSLPckg_ValueSpecification()) == None

from python_code import CompleteDSLPckg_JoinNode
from python_code import CompleteDSLPckg_ValueSpecification

def test_CompleteDSLPckg_JoinNode___init__():
    assert CompleteDSLPckg_JoinNode.__init__(CompleteDSLPckg_JoinNode(True, CompleteDSLPckg_JoinNode=CompleteDSLPckg_ValueSpecification()), False, CompleteDSLPckg_JoinNode=CompleteDSLPckg_ValueSpecification()) == None

from python_code import CompleteDSLPckg_InputPin
from python_code import CompleteDSLPckg_LinkEndCreationData

def test_CompleteDSLPckg_LinkEndCreationData___init__():
    assert CompleteDSLPckg_LinkEndCreationData.__init__(CompleteDSLPckg_LinkEndCreationData(True, CompleteDSLPckg_LinkEndCreationData=CompleteDSLPckg_InputPin()), False, CompleteDSLPckg_LinkEndCreationData=CompleteDSLPckg_InputPin()) == None

from python_code import CompleteDSLPckg_InputPin
from python_code import CompleteDSLPckg_LinkEndDestructionData

def test_CompleteDSLPckg_LinkEndDestructionData___init__():
    assert CompleteDSLPckg_LinkEndDestructionData.__init__(CompleteDSLPckg_LinkEndDestructionData(True, CompleteDSLPckg_LinkEndDestructionData=CompleteDSLPckg_InputPin()), False, CompleteDSLPckg_LinkEndDestructionData=CompleteDSLPckg_InputPin()) == None

from python_code import CompleteDSLPckg_LoopNode
from python_code import CompleteDSLPckg_OutputPin

def test_CompleteDSLPckg_LoopNode___init__():
    assert CompleteDSLPckg_LoopNode.__init__(CompleteDSLPckg_LoopNode(False, CompleteDSLPckg_LoopNode=set(), CompleteDSLPckg_LoopNode820=set(), CompleteDSLPckg_LoopNode823=set(), CompleteDSLPckg_LoopNode826=CompleteDSLPckg_OutputPin(), CompleteDSLPckg_LoopNode829=set(), CompleteDSLPckg_LoopNode832=set(), CompleteDSLPckg_LoopNode835=set(), CompleteDSLPckg_LoopNode838=set()), False, CompleteDSLPckg_LoopNode=set(), CompleteDSLPckg_LoopNode820=set(), CompleteDSLPckg_LoopNode823=set(), CompleteDSLPckg_LoopNode826=CompleteDSLPckg_OutputPin(), CompleteDSLPckg_LoopNode829=set(), CompleteDSLPckg_LoopNode832=set(), CompleteDSLPckg_LoopNode835=set(), CompleteDSLPckg_LoopNode838=set()) == None

from python_code import CompleteDSLPckg_MultiplicityElement
from python_code import CompleteDSLPckg_ValueSpecification

def test_CompleteDSLPckg_MultiplicityElement___init__():
    assert CompleteDSLPckg_MultiplicityElement.__init__(CompleteDSLPckg_MultiplicityElement(False, False, 0, 0, MultiplicityElement=CompleteDSLPckg_ValueSpecification(), MultiplicityElement48=CompleteDSLPckg_ValueSpecification(), owningUpper=CompleteDSLPckg_ValueSpecification(), owningLower=CompleteDSLPckg_ValueSpecification()), False, False, 0, 0, MultiplicityElement=CompleteDSLPckg_ValueSpecification(), MultiplicityElement48=CompleteDSLPckg_ValueSpecification(), owningUpper=CompleteDSLPckg_ValueSpecification(), owningLower=CompleteDSLPckg_ValueSpecification()) == None

from python_code import CompleteDSLPckg_OpaqueAction

def test_CompleteDSLPckg_OpaqueAction___init__():
    assert CompleteDSLPckg_OpaqueAction.__init__(CompleteDSLPckg_OpaqueAction('', '', CompleteDSLPckg_OpaqueAction=set(), CompleteDSLPckg_OpaqueAction401=set()), '', '', CompleteDSLPckg_OpaqueAction=set(), CompleteDSLPckg_OpaqueAction401=set()) == None

from python_code import CompleteDSLPckg_OpaqueBehavior

def test_CompleteDSLPckg_OpaqueBehavior___init__():
    assert CompleteDSLPckg_OpaqueBehavior.__init__(CompleteDSLPckg_OpaqueBehavior('', '\x00'), '\x00\x00', '') == None

from python_code import CompleteDSLPckg_Slot
from python_code import CompleteDSLPckg_StructuralFeature
from python_code import CompleteDSLPckg_StructuralFeatureAction

def test_CompleteDSLPckg_StructuralFeature___init__():
    assert CompleteDSLPckg_StructuralFeature.__init__(CompleteDSLPckg_StructuralFeature(True, CompleteDSLPckg_StructuralFeature=CompleteDSLPckg_Slot(), CompleteDSLPckg_StructuralFeature449=CompleteDSLPckg_StructuralFeatureAction()), False, CompleteDSLPckg_StructuralFeature=CompleteDSLPckg_Slot(), CompleteDSLPckg_StructuralFeature449=CompleteDSLPckg_StructuralFeatureAction()) == None

from python_code import CompleteDSLPckg_TimeConstraint
from python_code import CompleteDSLPckg_TimeInterval

def test_CompleteDSLPckg_TimeConstraint___init__():
    assert CompleteDSLPckg_TimeConstraint.__init__(CompleteDSLPckg_TimeConstraint(True, CompleteDSLPckg_TimeConstraint=CompleteDSLPckg_TimeInterval()), False, CompleteDSLPckg_TimeConstraint=CompleteDSLPckg_TimeInterval()) == None

from python_code import CompleteDSLPckg_TimeEvent
from python_code import CompleteDSLPckg_TimeExpression

def test_CompleteDSLPckg_TimeEvent___init__():
    assert CompleteDSLPckg_TimeEvent.__init__(CompleteDSLPckg_TimeEvent(True, CompleteDSLPckg_TimeEvent=CompleteDSLPckg_TimeExpression()), False, CompleteDSLPckg_TimeEvent=CompleteDSLPckg_TimeExpression()) == None

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
from python_code import InteractionOperandKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InteractionOperandKind.seq, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InteractionOperandKind.seq, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InteractionOperandKind.alt, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InteractionOperandKind.opt, 0)

def test_Enum___new___2():
    assert Enum.__new__(InteractionOperandKind.alt, 'alt') == InteractionOperandKind.alt
