from enum import Enum
from python_code import AdHocOrdering
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AdHocOrdering.Parallel, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AdHocOrdering.Parallel, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AdHocOrdering.Parallel, 0, 0, 0) == 0

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
        Enum._generate_next_value_(MultiInstanceBehavior.All, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(MultiInstanceBehavior.One, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(MultiInstanceBehavior.One, 0, '', 0) == 0

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
from python_code import bpmn2_Expression

def test_bpmn2_AdHocSubProcess___init__():
    assert bpmn2_AdHocSubProcess.__init__(bpmn2_AdHocSubProcess('', False, bpmn2_AdHocSubProcess=bpmn2_Expression()), '', False, bpmn2_AdHocSubProcess=bpmn2_Expression()) == None

from python_code import bpmn2_BusinessRuleTask

def test_bpmn2_BusinessRuleTask___init__():
    assert bpmn2_BusinessRuleTask.__init__(bpmn2_BusinessRuleTask(''), '') == None

from python_code import bpmn2_DataObject
from python_code import bpmn2_DataObjectReference

def test_bpmn2_DataObject___init__():
    assert bpmn2_DataObject.__init__(bpmn2_DataObject(True, bpmn2_DataObject=bpmn2_DataObjectReference()), False, bpmn2_DataObject=bpmn2_DataObjectReference()) == None

from python_code import bpmn2_DataState
from python_code import bpmn2_ItemAwareElement

def test_bpmn2_DataState___init__():
    assert bpmn2_DataState.__init__(bpmn2_DataState('', bpmn2_DataState=bpmn2_ItemAwareElement()), '', bpmn2_DataState=bpmn2_ItemAwareElement()) == None

from python_code import bpmn2_DataStore
from python_code import bpmn2_DataStoreReference

def test_bpmn2_DataStore___init__():
    assert bpmn2_DataStore.__init__(bpmn2_DataStore(0, False, '\x00\x00', bpmn2_DataStore=bpmn2_DataStoreReference()), 0, False, '', bpmn2_DataStore=bpmn2_DataStoreReference()) == None

from python_code import bpmn2_EventBasedGateway

def test_bpmn2_EventBasedGateway___init__():
    assert bpmn2_EventBasedGateway.__init__(bpmn2_EventBasedGateway(False, '\x00'), False, '\x00') == None

from python_code import bpmn2_Gateway

def test_bpmn2_Gateway___init__():
    assert bpmn2_Gateway.__init__(bpmn2_Gateway(''), '') == None

from python_code import bpmn2_GlobalBusinessRuleTask

def test_bpmn2_GlobalBusinessRuleTask___init__():
    assert bpmn2_GlobalBusinessRuleTask.__init__(bpmn2_GlobalBusinessRuleTask(''), '') == None

from python_code import bpmn2_GlobalScriptTask

def test_bpmn2_GlobalScriptTask___init__():
    assert bpmn2_GlobalScriptTask.__init__(bpmn2_GlobalScriptTask('', '\x00'), '\x00\x00', '') == None

from python_code import bpmn2_GlobalUserTask

def test_bpmn2_GlobalUserTask___init__():
    assert bpmn2_GlobalUserTask.__init__(bpmn2_GlobalUserTask('', bpmn2_GlobalUserTask=set()), '', bpmn2_GlobalUserTask=set()) == None
