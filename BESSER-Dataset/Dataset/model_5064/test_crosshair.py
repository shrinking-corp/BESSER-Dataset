from enum import Enum
from python_code import AdHocOrdering
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AdHocOrdering.Parallel, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AdHocOrdering.Parallel, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AdHocOrdering.Parallel, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AdHocOrdering.Parallel, 0)

def test_Enum___new___2():
    assert Enum.__new__(AdHocOrdering.Parallel, 'Parallel') == AdHocOrdering.Parallel

from enum import Enum
from python_code import AssociationDirection
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssociationDirection.Both, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssociationDirection.Both, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssociationDirection.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssociationDirection.One, 0)

def test_Enum___new___2():
    assert Enum.__new__(AssociationDirection.One, 'One') == AssociationDirection.One

from enum import Enum
from python_code import ChoreographyLoopType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ChoreographyLoopType.Standard, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ChoreographyLoopType.None_, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ChoreographyLoopType.None_, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ChoreographyLoopType.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(ChoreographyLoopType.None_, 'None_') == ChoreographyLoopType.None_

from enum import Enum
from python_code import EventBasedGatewayType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EventBasedGatewayType.Exclusive, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EventBasedGatewayType.Exclusive, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EventBasedGatewayType.Parallel, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EventBasedGatewayType.Parallel, 0)

def test_Enum___new___2():
    assert Enum.__new__(EventBasedGatewayType.Parallel, 'Parallel') == EventBasedGatewayType.Parallel

from enum import Enum
from python_code import GatewayDirection
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GatewayDirection.Diverging, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GatewayDirection.Mixed, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GatewayDirection.Mixed, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GatewayDirection.Mixed, 0)

def test_Enum___new___2():
    assert Enum.__new__(GatewayDirection.Mixed, 'Mixed') == GatewayDirection.Mixed

from enum import Enum
from python_code import ItemKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ItemKind.Physical, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ItemKind.Physical, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ItemKind.Physical, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ItemKind.Physical, 0)

def test_Enum___new___2():
    assert Enum.__new__(ItemKind.Physical, 'Physical') == ItemKind.Physical

from enum import Enum
from python_code import MultiInstanceBehavior
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(MultiInstanceBehavior.None_, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MultiInstanceBehavior.One, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MultiInstanceBehavior.One, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(MultiInstanceBehavior.One, 0)

def test_Enum___new___2():
    assert Enum.__new__(MultiInstanceBehavior.One, 'One') == MultiInstanceBehavior.One

from enum import Enum
from python_code import ProcessType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ProcessType.None_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ProcessType.None_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ProcessType.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ProcessType.None_, 0)

def test_Enum___new___2():
    assert Enum.__new__(ProcessType.None_, 'None_') == ProcessType.None_

from enum import Enum
from python_code import RelationshipDirection
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RelationshipDirection.Forward, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RelationshipDirection.Both, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RelationshipDirection.Both, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RelationshipDirection.Both, 0)

def test_Enum___new___2():
    assert Enum.__new__(RelationshipDirection.Both, 'Both') == RelationshipDirection.Both

from python_code import bpmn2_AdHocSubProcess
from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Expression

def test_bpmn2_AdHocSubProcess___init__():
    assert bpmn2_AdHocSubProcess.__init__(bpmn2_AdHocSubProcess(False, '\x00', bpmn2_AdHocSubProcess=bpmn2_DocumentRoot(), bpmn2_AdHocSubProcess318=bpmn2_Expression()), False, '\x00', bpmn2_AdHocSubProcess=bpmn2_DocumentRoot(), bpmn2_AdHocSubProcess318=bpmn2_Expression()) == None

from python_code import bpmn2_BusinessRuleTask
from python_code import bpmn2_DocumentRoot

def test_bpmn2_BusinessRuleTask___init__():
    assert bpmn2_BusinessRuleTask.__init__(bpmn2_BusinessRuleTask('', bpmn2_BusinessRuleTask=bpmn2_DocumentRoot()), '', bpmn2_BusinessRuleTask=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_Category
from python_code import bpmn2_CategoryValue
from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_FlowElement
from python_code import bpmn2_Group

def test_bpmn2_CategoryValue___init__():
    assert bpmn2_CategoryValue.__init__(bpmn2_CategoryValue('', bpmn2_CategoryValue=bpmn2_DocumentRoot(), bpmn2_CategoryValue384=set(), bpmn2_CategoryValue382=bpmn2_Category(), bpmn2_CategoryValue573=bpmn2_FlowElement(), bpmn2_CategoryValue597=bpmn2_Group()), '', bpmn2_CategoryValue=bpmn2_DocumentRoot(), bpmn2_CategoryValue384=set(), bpmn2_CategoryValue382=bpmn2_Category(), bpmn2_CategoryValue573=bpmn2_FlowElement(), bpmn2_CategoryValue597=bpmn2_Group()) == None

from python_code import bpmn2_ChoreographyActivity
from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Participant

def test_bpmn2_ChoreographyActivity___init__():
    assert bpmn2_ChoreographyActivity.__init__(bpmn2_ChoreographyActivity('', bpmn2_ChoreographyActivity=bpmn2_DocumentRoot(), bpmn2_ChoreographyActivity387=set(), bpmn2_ChoreographyActivity390=set(), bpmn2_ChoreographyActivity393=bpmn2_Participant()), '', bpmn2_ChoreographyActivity=bpmn2_DocumentRoot(), bpmn2_ChoreographyActivity387=set(), bpmn2_ChoreographyActivity390=set(), bpmn2_ChoreographyActivity393=bpmn2_Participant()) == None

from python_code import bpmn2_DataObject
from python_code import bpmn2_DataObjectReference
from python_code import bpmn2_DocumentRoot

def test_bpmn2_DataObject___init__():
    assert bpmn2_DataObject.__init__(bpmn2_DataObject(True, bpmn2_DataObject=bpmn2_DocumentRoot(), bpmn2_DataObject512=bpmn2_DataObjectReference()), False, bpmn2_DataObject=bpmn2_DocumentRoot(), bpmn2_DataObject512=bpmn2_DataObjectReference()) == None

from python_code import bpmn2_DataStore
from python_code import bpmn2_DataStoreReference
from python_code import bpmn2_DocumentRoot

def test_bpmn2_DataStore___init__():
    assert bpmn2_DataStore.__init__(bpmn2_DataStore(0, False, bpmn2_DataStore=bpmn2_DocumentRoot(), bpmn2_DataStore522=bpmn2_DataStoreReference()), 0, False, bpmn2_DataStore=bpmn2_DocumentRoot(), bpmn2_DataStore522=bpmn2_DataStoreReference()) == None

from python_code import bpmn2_Definitions
from python_code import bpmn2_DocumentRoot

def test_bpmn2_Definitions___init__():
    assert bpmn2_Definitions.__init__(bpmn2_Definitions('', '', '', '', '\x00', bpmn2_Definitions=bpmn2_DocumentRoot(), bpmn2_Definitions524=set(), bpmn2_Definitions527=set(), bpmn2_Definitions530=set(), bpmn2_Definitions533=set(), bpmn2_Definitions535=set()), '', '', '', '', '', bpmn2_Definitions=bpmn2_DocumentRoot(), bpmn2_Definitions524=set(), bpmn2_Definitions527=set(), bpmn2_Definitions530=set(), bpmn2_Definitions533=set(), bpmn2_Definitions535=set()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_EventBasedGateway

def test_bpmn2_EventBasedGateway___init__():
    assert bpmn2_EventBasedGateway.__init__(bpmn2_EventBasedGateway('', False, bpmn2_EventBasedGateway=bpmn2_DocumentRoot()), '', False, bpmn2_EventBasedGateway=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Gateway

def test_bpmn2_Gateway___init__():
    assert bpmn2_Gateway.__init__(bpmn2_Gateway('', bpmn2_Gateway=bpmn2_DocumentRoot()), '', bpmn2_Gateway=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_GlobalBusinessRuleTask

def test_bpmn2_GlobalBusinessRuleTask___init__():
    assert bpmn2_GlobalBusinessRuleTask.__init__(bpmn2_GlobalBusinessRuleTask('', bpmn2_GlobalBusinessRuleTask=bpmn2_DocumentRoot()), '', bpmn2_GlobalBusinessRuleTask=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_GlobalScriptTask

def test_bpmn2_GlobalScriptTask___init__():
    assert bpmn2_GlobalScriptTask.__init__(bpmn2_GlobalScriptTask('', '\x00', bpmn2_GlobalScriptTask=bpmn2_DocumentRoot()), '\x00\x00', '', bpmn2_GlobalScriptTask=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_GlobalUserTask

def test_bpmn2_GlobalUserTask___init__():
    assert bpmn2_GlobalUserTask.__init__(bpmn2_GlobalUserTask('', bpmn2_GlobalUserTask=bpmn2_DocumentRoot(), bpmn2_GlobalUserTask593=set()), '', bpmn2_GlobalUserTask=bpmn2_DocumentRoot(), bpmn2_GlobalUserTask593=set()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Participant
from python_code import bpmn2_ParticipantMultiplicity

def test_bpmn2_ParticipantMultiplicity___init__():
    assert bpmn2_ParticipantMultiplicity.__init__(bpmn2_ParticipantMultiplicity(0, 0, bpmn2_ParticipantMultiplicity=bpmn2_DocumentRoot(), bpmn2_ParticipantMultiplicity766=bpmn2_Participant()), 0, 0, bpmn2_ParticipantMultiplicity=bpmn2_DocumentRoot(), bpmn2_ParticipantMultiplicity766=bpmn2_Participant()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Message
from python_code import bpmn2_Operation
from python_code import bpmn2_ReceiveTask

def test_bpmn2_ReceiveTask___init__():
    assert bpmn2_ReceiveTask.__init__(bpmn2_ReceiveTask('', False, bpmn2_ReceiveTask=bpmn2_DocumentRoot(), bpmn2_ReceiveTask807=bpmn2_Message(), bpmn2_ReceiveTask810=bpmn2_Operation()), '', False, bpmn2_ReceiveTask=bpmn2_DocumentRoot(), bpmn2_ReceiveTask807=bpmn2_Message(), bpmn2_ReceiveTask810=bpmn2_Operation()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_ScriptTask

def test_bpmn2_ScriptTask___init__():
    assert bpmn2_ScriptTask.__init__(bpmn2_ScriptTask('', '\x00', bpmn2_ScriptTask=bpmn2_DocumentRoot()), '\x00\x00', '', bpmn2_ScriptTask=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Message
from python_code import bpmn2_Operation
from python_code import bpmn2_SendTask

def test_bpmn2_SendTask___init__():
    assert bpmn2_SendTask.__init__(bpmn2_SendTask('', bpmn2_SendTask=bpmn2_DocumentRoot(), bpmn2_SendTask843=bpmn2_Message(), bpmn2_SendTask846=bpmn2_Operation()), '', bpmn2_SendTask=bpmn2_DocumentRoot(), bpmn2_SendTask843=bpmn2_Message(), bpmn2_SendTask846=bpmn2_Operation()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Operation
from python_code import bpmn2_ServiceTask

def test_bpmn2_ServiceTask___init__():
    assert bpmn2_ServiceTask.__init__(bpmn2_ServiceTask('', bpmn2_ServiceTask=bpmn2_DocumentRoot(), bpmn2_ServiceTask856=bpmn2_Operation()), '', bpmn2_ServiceTask=bpmn2_DocumentRoot(), bpmn2_ServiceTask856=bpmn2_Operation()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Expression
from python_code import bpmn2_StandardLoopCharacteristics

def test_bpmn2_StandardLoopCharacteristics___init__():
    assert bpmn2_StandardLoopCharacteristics.__init__(bpmn2_StandardLoopCharacteristics('', False, bpmn2_StandardLoopCharacteristics=bpmn2_DocumentRoot(), bpmn2_StandardLoopCharacteristics865=bpmn2_Expression()), '', False, bpmn2_StandardLoopCharacteristics=bpmn2_DocumentRoot(), bpmn2_StandardLoopCharacteristics865=bpmn2_Expression()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_StartEvent

def test_bpmn2_StartEvent___init__():
    assert bpmn2_StartEvent.__init__(bpmn2_StartEvent(True, bpmn2_StartEvent=bpmn2_DocumentRoot()), False, bpmn2_StartEvent=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_TextAnnotation

def test_bpmn2_TextAnnotation___init__():
    assert bpmn2_TextAnnotation.__init__(bpmn2_TextAnnotation('', '\x00', bpmn2_TextAnnotation=bpmn2_DocumentRoot()), '\x00\x00', '', bpmn2_TextAnnotation=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_Transaction

def test_bpmn2_Transaction___init__():
    assert bpmn2_Transaction.__init__(bpmn2_Transaction('', '\x00', bpmn2_Transaction=bpmn2_DocumentRoot()), '\x00\x00', '', bpmn2_Transaction=bpmn2_DocumentRoot()) == None

from python_code import bpmn2_DocumentRoot
from python_code import bpmn2_UserTask

def test_bpmn2_UserTask___init__():
    assert bpmn2_UserTask.__init__(bpmn2_UserTask('', bpmn2_UserTask=bpmn2_DocumentRoot(), bpmn2_UserTask906=set()), '', bpmn2_UserTask=bpmn2_DocumentRoot(), bpmn2_UserTask906=set()) == None
